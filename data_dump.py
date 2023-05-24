# Here we have inserted our data to our database.which is pymongo.

import pymongo
import pandas as pd
import json

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://rahulharshawardhan:uyIAF7VZRnM9y3sn@cluster0.7mr9e03.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

DATA_FILE_PATH = (r"C:\Users\rahul\Engg Wale Bhaiya\Insurance Prediction\Insurance_Prediction\insurance.csv")

DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__ == "__main__":

    df = pd.read_csv(DATA_FILE_PATH)
    print(f"rows & columns: {df.shape}")

    df.reset_index(drop = True, inplace = True)
    # since our mongodb takes data in key and value pair, we need to transpose our data.

    json_record = list(json.loads(df.T.to_json()).values()) # here the data is in key and value pair.
    # Now we will insert into mongo db.
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
