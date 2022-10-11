import os

from flask import Flask
from flask_restful import Api
from resources.home import Home
from commonLibs.initialiseLogging import InitialiseLogging
from pymongo import MongoClient
from commonLibs.globalvariables import GlobalVariables
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
GlobalVariables.APP = app
api = Api(GlobalVariables.APP)
client = MongoClient(os.environ.get("MONGODB_URI"))
GlobalVariables.APP.db = client.microblog

InitialiseLogging().setupLogging()

api.add_resource(Home,'/microblog')

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)