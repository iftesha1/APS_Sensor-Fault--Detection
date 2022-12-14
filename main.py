from sensor.configuration.mongo_db_connection import MongoDBClient


if __name__=='__main__':
    mongo_client=MongoDBClient()
    print("collection names:",mongo_client.database.list_collection_names())
