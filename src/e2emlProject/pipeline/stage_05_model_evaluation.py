from e2emlProject.componenets.model_evaluation import ModelEvaluation
from e2emlProject.config.configuration import ConfigurationManager
from e2emlProject import logger
from pathlib import Path

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_confing = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_confing)
        model_evaluation.log_into_mlflow()


if __name__=="__main__":
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>{STAGE_NAME} completed <<<<<<<<<")
    except Exception as e:
        logger.exception(e)
        raise e
