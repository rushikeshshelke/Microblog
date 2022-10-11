from flask import Flask
from flask_restful import Api
from resources.home import Home
from commonLibs.initialiseLogging import InitialiseLogging
from pymongo import MongoClient
from commonLibs.globalvariables import GlobalVariables

GlobalVariables.APP = Flask(__name__)
api = Api(GlobalVariables.APP)
client = MongoClient("mongodb://rushi:Rushi2020@ac-h77fpjp-shard-00-00.g92obdv.mongodb.net:27017,ac-h77fpjp-shard-00-01.g92obdv.mongodb.net:27017,ac-h77fpjp-shard-00-02.g92obdv.mongodb.net:27017/?ssl=true&replicaSet=atlas-ht8ez8-shard-0&authSource=admin&retryWrites=true&w=majority")
GlobalVariables.APP.db = client.microblog

InitialiseLogging().setupLogging()

api.add_resource(Home,'/microblog')

if __name__ == "__main__":
    GlobalVariables.APP.run(host="0.0.0.0",port=5000,debug=True)