import logging

class JobStageCurated:
    """
    JobStageCurated class to represent a job stage in a curated manner.
    """

    def __init__(self, job_stage_id: str, job_stage_name: str, logging: logging.Logger = None):

        self.job_stage_id = job_stage_id
        self.job_stage_name = job_stage_name
        self.logging = logging

    def run(self):
        logging.info(f"Running job stage: {self.job_stage_id} - {self.job_stage_name}")