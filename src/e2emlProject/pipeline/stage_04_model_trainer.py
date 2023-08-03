from e2emlProject.componenets.model_trainer import ModelTrainer
from e2emlProject.config.configuration import ConfigurationManager
from e2emlProject import logger
from pathlib import Path

STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__=="__main__":
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>{STAGE_NAME} completed <<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e