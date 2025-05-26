import os
import pandas as pd
import logging
from datetime import datetime

from solution.job_stage_raw import JobStageRaw
from solution.job_stage_curated import JobStageCurated
from solution.job_stage_analytics import JobStageAnalytics

LOG_DATE = datetime.now().strftime("%Y-%m-%d")
LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"logs/application_{LOG_DATE}.log")

if not os.path.exists(os.path.dirname(LOG_FILE)):
    os.makedirs(os.path.dirname(LOG_FILE))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_FILE, mode='a', encoding='utf-8')
    ]
)

start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

stage_raw = JobStageRaw(
    job_stage_id="1", 
    job_stage_name="Data Ingestion", 
    logging=logging
)

stage_raw.run()

stage_curated = JobStageCurated(
    job_stage_id="2", 
    job_stage_name="Data Cleaning", 
    logging=logging
)

stage_curated.run()

stage_analytics = JobStageAnalytics(
    job_stage_id="3", 
    job_stage_name="Data Analysis", 
    logging=logging
)

stage_analytics.run()

end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

duration = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S") - datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
logging.info(f"Job completed in {duration}.")