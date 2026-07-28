import os
from src.textSummarizer.logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk

from src.textSummarizer.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch):
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)
        target_encodings = self.tokenizer(example_batch['summary'], max_length=128, truncation=True)

        return {
            "input_ids": input_encodings["input_ids"],
            "attention_mask": input_encodings["attention_mask"],
            "labels": target_encodings["input_ids"],
        }

    def convert(self):
        input_dataset_path = os.path.join(self.config.root_dir, "input_dataset")

        if os.path.exists(input_dataset_path):
            dataset_samsum = load_from_disk(input_dataset_path)
        else:
            try:
                dataset_samsum = load_dataset("samsum", split="train")
            except Exception:
                dataset_samsum = load_dataset("knkarthick/dialogsum", split="train")

            os.makedirs(os.path.dirname(input_dataset_path), exist_ok=True)
            dataset_samsum.save_to_disk(input_dataset_path)

        dataset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)
        os.makedirs(self.config.root_dir, exist_ok=True)
        output_path = os.path.join(self.config.root_dir, "processed_dataset")
        dataset_samsum_pt.save_to_disk(output_path)