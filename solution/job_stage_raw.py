import logging
import pandas as pd
from solution.helpers.helper_github import Github

class JobStageRaw:
    """
    JobStageRaw class to represent a job stage in a data processing pipeline.
    """

    def __init__(self, job_stage_id: str, job_stage_name: str, logging: logging.Logger = None):

        self.job_stage_id = job_stage_id
        self.job_stage_name = job_stage_name
        self.logging = logging

    def run(self):

        logging.info(f"Running job stage: {self.job_stage_id} - {self.job_stage_name}")

        api_github = Github()

        organizations = ["microsoft", "aws", "oracle", "ibm", "apache"]

        logging.info("Iniciando coleta dos repositórios das organizações.")
        data_raw = api_github.get_repos_orgs(organizations) # return json

        logging.info("Convertendo dados para DataFrame.")
        df_repos = pd.DataFrame.from_dict(data_raw)
        df_repos = df_repos[["id", "full_name", "name", "language","created_at", "updated_at", "size", "stargazers_count", "watchers_count", "forks_count", "open_issues_count", "archived", "disabled", "visibility"]]

        output_path = "data/raw/repos.csv"
        logging.info(f"Salvando dados em {output_path}")
        df_repos.to_csv(output_path, index=False)
        logging.info("Processo finalizado com sucesso.")

        