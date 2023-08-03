from src.e2emlProject import logger
from e2emlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from e2emlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from e2emlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from e2emlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>{STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>>>> {STAGE_NAME} started <<<<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>{STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>{STAGE_NAME} completed <<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e