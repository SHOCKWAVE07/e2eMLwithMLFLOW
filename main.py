from src.e2emlProject import logger
from e2emlProject.pipeline.state_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>{STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e
