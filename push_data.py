import os,sys,json

from dotenv import load_dotenv
load_dotenv()

MONGO__DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO__DB_URL)

import certifi

ca = certifi.where()

import pandas as pd, numpy as np, pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def csv_to_json_convertor(self, file_path):
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            records = list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            self.mongo_client = pymongo.MongoClient(MONGO__DB_URL)
            self.database = self.mongo_client[self.database]

            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

if __name__ == "__main__":
    FILE_PATH = r"Network_Data\phisingData.csv"
    DATABASE = "AKP"
    collection = "NetworkData"
    networkonj= NetworkDataExtract()
    records = networkonj.csv_to_json_convertor(file_path=FILE_PATH)
    print(records)
    no_of_records = networkonj.insert_data_mongodb(records,DATABASE,collection)
    print(no_of_records)