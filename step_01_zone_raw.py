import requests
import os
import pandas as pd
import logging

LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "application.log")

# Configuração do logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, mode='a', encoding='utf-8')
    ]
)

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
GITHUB_API_URL = "https://api.github.com"

def get_auth_header():
    return {"Authorization": f"token {GITHUB_TOKEN}"}

def get_my_profile():
    logging.info("Buscando perfil do usuário autenticado.")
    response = requests.get(f"{GITHUB_API_URL}/user", headers=get_auth_header())
    if response.status_code == 200:
        logging.info("Perfil obtido com sucesso.")
    else:
        logging.error(f"Erro ao buscar perfil: {response.status_code}")
    return response.json()

def get_my_repos():
    logging.info("Buscando repositórios do usuário autenticado.")
    response = requests.get(f"{GITHUB_API_URL}/user/repos", headers=get_auth_header())
    if response.status_code == 200:
        logging.info("Repositórios obtidos com sucesso.")
    else:
        logging.error(f"Erro ao buscar repositórios: {response.status_code}")
    return response.json()

def get_repos(organizations):
    all_repos = []
    for organization in organizations:
        page = 1
        logging.info(f"Buscando repositórios da organização: {organization.upper()}")
        while True:
            response = requests.get(
                f"{GITHUB_API_URL}/orgs/{organization}/repos",
                headers=get_auth_header(),
                params={"per_page": 100, "page": page}
            )
            if response.status_code == 200:
                repos = response.json()
                all_repos.extend(repos)
                logging.info(f"Página {page}: {len(repos)} repositórios obtidos de {organization.upper()}.")
                if not repos or len(repos) < 100:
                    break
                page += 1
            else:
                logging.error(f"Erro ao buscar repositórios para {organization.upper()}: {response.status_code}")
                break
    logging.info(f"Total de repositórios coletados: {len(all_repos)}")
    return all_repos

# Montando Zona RAW

organizations = ["microsoft", "aws", "oracle", "ibm", "apache"]

logging.info("Iniciando coleta dos repositórios das organizações.")
data_raw = get_repos(organizations) # return json

logging.info("Convertendo dados para DataFrame.")
df_repos = pd.DataFrame.from_dict(data_raw)
df_repos = df_repos[["id", "full_name", "name", "language","created_at", "updated_at", "size", "stargazers_count", "watchers_count", "forks_count", "open_issues_count", "archived", "disabled", "visibility"]]

output_path = "data/raw/repos.csv"
logging.info(f"Salvando dados em {output_path}")
df_repos.to_csv(output_path, index=False)
logging.info("Processo finalizado com sucesso.")