from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
import os 
import json 
import sys
import certifi
import pandas as pd 
import numpy as np 
from networksecurity.logger.logger import logging
from networksecurity.exception.exception import NetworkSecurityException

# Replace with your connection string

load_dotenv()

uri=os.getenv('uri')
ca= certifi.where()

class NetowrkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(drop=True,inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        

    def instert_data_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records

            self.mongo_client=MongoClient(uri)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)


            return(len(self.records))
        

        except Exception as e: 
            raise NetworkSecurityException(e,sys)


if __name__=="__main__":
    FILE_PATH="Network_Data/phisingData.csv"
    DATABASE='network_etl'
    COLLECTION='NetworkData'
    networkobj=NetowrkDataExtract()
    records=networkobj.csv_to_json_convertor(file_path=FILE_PATH)
    no_of_records=networkobj.instert_data_mongodb(records,DATABASE,COLLECTION)
    print(no_of_records)
        
    
