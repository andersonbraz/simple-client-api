from solution.job_stage_raw import JobStageRaw
from solution.job_stage_curated import JobStageCurated
from solution.job_stage_analytics import JobStageAnalytics

stage_raw = JobStageRaw(job_stage_id="1", job_stage_name="Data Ingestion")
print(stage_raw)

stage_curated = JobStageCurated(job_stage_id="2", job_stage_name="Data Cleaning")
print(stage_curated)

stage_analytics = JobStageAnalytics(job_stage_id="3", job_stage_name="Data Analysis")
print(stage_analytics)