import os, sys, pandas as pd

from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.constant import training_pipeline
from networksecurity.entity.config_entity import DataValidationConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
from networksecurity.constant.training_pipeline import SCHEMA_FILE_PATH
from networksecurity.utils.main_utils.utils import read_yaml_file, write_yaml_file
from scipy.stats import ks_2samp

class DataValidation:
    def __init__(self, data_ingestion_artifact: DataIngestionArtifact, data_validation_config: DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    @staticmethod
    def read_yaml_file(file_path):
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def validate_columns(self, df:pd.DataFrame)->bool:
        try:
            num_columns = len(self._schema_config)
            logging.info(f"Number of columns in schema file: {num_columns}")
            logging.info(f"Number of columns in dataframe: {len(df.columns)}")
            if len(df.columns) == num_columns:
                return True
            return False    
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def detect_dataset_drift(self, base_df, current_df, threshold=0.05)->bool:
        try:
            status = True
            report = {}
            for column in base_df.columns:
                base_data, current_data = base_df[column], current_df[column]
                same_distribution = ks_2samp(base_data, current_data)
                if same_distribution.pvalue > threshold:
                    is_found = False
                else:
                    is_found = True
                    status = False
                report[column] = {
                        "p_value": float(same_distribution.pvalue),
                        "drift_status": is_found
                    }
            drift_report_file_path = self.data_validation_config.drift_report_file_path
            os.makedirs(os.path.dirname(drift_report_file_path), exist_ok=True)
            write_yaml_file(file_path=drift_report_file_path, content=report)
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def initiate_data_validation(self)->DataValidationArtifact:
        try:
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            
            train_df = DataValidation.read_yaml_file(train_file_path)
            test_df = DataValidation.read_yaml_file(test_file_path)
            
            status=self.validate_columns(train_df)
            if not status:
                error = f"Train dataset does not contain all columns."
            status=self.validate_columns(test_df)
            if not status:
                error = f"Test dataset does not contain all columns."

            status=self.detect_dataset_drift(train_df, test_df)
            dir_path = os.path.dirname(self.data_validation_config.valid_train_file_path)
            os.makedirs(dir_path, exist_ok=True)
            
            train_df.to_csv(self.data_validation_config.valid_train_file_path, index=False, header=True)
            test_df.to_csv(self.data_validation_config.valid_test_file_path, index=False, header=True)

            data_validation_artifact = DataValidationArtifact(
                validation_status=status,
                valid_train_file_path=self.data_ingestion_artifact.train_file_path,
                valid_test_file_path=self.data_ingestion_artifact.test_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path,
            )
            return data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
            