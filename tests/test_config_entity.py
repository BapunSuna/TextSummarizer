from pathlib import Path

from src.textSummarizer.entity.config_entity import DataIngestionConfig, DataTransformationConfig


def test_data_ingestion_config_can_be_instantiated():
    config = DataIngestionConfig(
        root_dir=Path("artifacts/data_ingestion"),
        source_URL=Path("https://example.com/data.zip"),
        local_data_file=Path("artifacts/data_ingestion/data.zip"),
        unzip_dir=Path("artifacts/data_ingestion/unzipped"),
    )

    assert config.root_dir == Path("artifacts/data_ingestion")
    assert config.local_data_file == Path("artifacts/data_ingestion/data.zip")


def test_data_transformation_config_can_be_instantiated():
    config = DataTransformationConfig(
        root_dir=Path("artifacts/data_transformation"),
        data_path=Path("artifacts/data_transformation/dataset"),
        tokenizer_name=Path("google/pegasus-cnn_dailymail"),
    )

    assert config.root_dir == Path("artifacts/data_transformation")
    assert config.tokenizer_name == Path("google/pegasus-cnn_dailymail")
