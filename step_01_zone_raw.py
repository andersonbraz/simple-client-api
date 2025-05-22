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

def get_repos(organizations):

    all_repos = []
    for organization in organizations:
        page = 1
        while True:
            response = requests.get(
                f"{GITHUB_API_URL}/orgs/{organization}/repos",
                headers=get_auth_header(),
                params={"per_page": 100, "page": page}
            )

            if response.status_code == 200:
                repos = response.json()
                all_repos.extend(repos)
                if not repos or len(repos) < 100:
                    break
                page += 1
                print(f"Fetched {len(repos)} repos from {organization} (page {page})")
            else:
                print(f"Error fetching repos for {organization}: {response.status_code}")
                break

    return all_repos

# Montando Zona RAW

organizations = ["microsoft","aws","oracle","ibm","apache"]

data_raw = get_repos(organizations) # return json

df_microsft = pd.DataFrame.from_dict(data_raw)

df_microsft = df_microsft[["id", "full_name", "name", "language","created_at", "updated_at", "size", "stargazers_count", "watchers_count", "forks_count", "open_issues_count", "archived", "disabled", "visibility"]]

df_microsft.to_csv("data/raw/repos.csv", index=False)