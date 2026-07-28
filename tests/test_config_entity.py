from pathlib import Path

from src.textSummarizer.entity.config_entity import DataIngestionConfig


def test_data_ingestion_config_can_be_instantiated():
    config = DataIngestionConfig(
        root_dir=Path("artifacts/data_ingestion"),
        source_URL=Path("https://example.com/data.zip"),
        local_data_file=Path("artifacts/data_ingestion/data.zip"),
        unzip_dir=Path("artifacts/data_ingestion/unzipped"),
    )

    assert config.root_dir == Path("artifacts/data_ingestion")
    assert config.local_data_file == Path("artifacts/data_ingestion/data.zip")
