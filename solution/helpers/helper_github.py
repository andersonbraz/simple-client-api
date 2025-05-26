import requests
import os
import logging


class Github(Exception):

    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
    GITHUB_API_URL = "https://api.github.com"

    def __init__(self):
        super().__init__()
        if not self.GITHUB_TOKEN:
            raise Exception("GITHUB_TOKEN não encontrado nas variáveis de ambiente.")

    def get_auth_header(self):
        logging.debug("Obtendo header de autenticação.")
        return {"Authorization": f"token {self.GITHUB_TOKEN}"}
    
    def get_my_profile(self):
        logging.info("Buscando perfil do usuário autenticado.")
        try:
            response = requests.get(f"{self.GITHUB_API_URL}/user", headers=self.get_auth_header())
            if response.status_code == 200:
                logging.info("Perfil obtido com sucesso.")
            else:
                logging.error(f"Erro ao buscar perfil: {response.status_code} - {response.text}")
            return response.json()
        except Exception as e:
            logging.exception("Exceção ao buscar perfil do usuário.")
            raise

    def get_repos_orgs(self, organizations):
        logging.info(f"Buscando repositórios das organizações: {organizations}")
        all_repos = []
        for organization in organizations:
            page = 1
            while True:
                try:
                    logging.debug(f"Buscando página {page} dos repositórios da organização {organization}.")
                    response = requests.get(
                        f"{self.GITHUB_API_URL}/orgs/{organization}/repos",
                        headers=self.get_auth_header(),
                        params={"per_page": 100, "page": page}
                    )
                    response.raise_for_status()
                    repos = response.json()
                    all_repos.extend(repos)
                    logging.info(f"Página {page}: {len(repos)} repositórios obtidos de {organization.upper()}.")
                    if not repos or len(repos) < 100:
                        logging.info(f"Finalizada busca de repositórios para {organization}. Total: {len(all_repos)}")
                        break
                    page += 1
                except Exception as e:
                    logging.exception(f"Erro ao buscar repositórios da organização {organization}.")
                    break
        return all_repos
