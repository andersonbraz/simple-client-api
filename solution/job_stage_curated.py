class JobStageCurated:
    """
    JobStageCurated class to represent a job stage in a curated manner.
    """

    def __init__(self, job_stage_id: str, job_stage_name: str):
        """
        Initialize the JobStageCurated instance.

        :param job_stage_id: Unique identifier for the job stage.
        :param job_stage_name: Name of the job stage.
        """
        self.job_stage_id = job_stage_id
        self.job_stage_name = job_stage_name

    def __repr__(self):
        return f"JobStageCurated(job_stage_id={self.job_stage_id}, job_stage_name={self.job_stage_name})"