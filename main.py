from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_2_data_transformation_pipeline import DataTransformationTrainingPipeline


# ---------------- Data Ingestion Stage ----------------
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


# ---------------- Data Transformation Stage ----------------
STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_transformation_pipeline = DataTransformationTrainingPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


# ---------------- Model Training Stage ----------------