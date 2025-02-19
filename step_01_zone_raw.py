import requests
import os
import pandas as pd

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
GITHUB_API_URL = "https://api.github.com"


def get_auth_header():
    return {"Authorization": f"token {GITHUB_TOKEN}"}

def get_my_profile():
    response = requests.get(f"{GITHUB_API_URL}/user", headers=get_auth_header())
    return response.json()

def get_my_repos():
    response = requests.get(f"{GITHUB_API_URL}/user/repos", headers=get_auth_header())
    return response.json()

def get_repos(organization):
    response = requests.get(f"{GITHUB_API_URL}/orgs/{organization}/repos", headers=get_auth_header())
    return response.json()

# Montando Zona RAW

data_raw = get_repos("microsoft") # return json

df_microsft = pd.DataFrame.from_dict(data_raw)
df_microsft = df_microsft[["id", "full_name", "name", "language", "created_at", "updated_at"]]
df_microsft.to_csv("data/raw/microsoft_repos.csv", index=False)