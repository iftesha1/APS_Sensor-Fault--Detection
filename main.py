from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
import os,sys
from sensor.logger import logging
#3.from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.pipeline import training_pipeline
# def test_exception():
#     try:
#         logging.info("the test for logging by dividing")
#         x=1/0
#     except Exception as e:
#         raise SensorException(e,sys)

if __name__=='__main__':

    try:

        training_pipeline=TrainPipeline()
        training_pipeline.run_pipeline()
    except Exception as e:
        print(e)
        logging.exception(e)
    
    # 3.train_pipeline_config=TrainingPipelineConfig()
    # data_igestion_config=DataIngestionConfig(training_pipeline_config=train_pipeline_config)
    # print(data_igestion_config.__dict__)



    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)


    # mongo_client=MongoDBClient()
    # print("collection names:",mongo_client.database.list_collection_names())
