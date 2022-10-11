import datetime

from flask_restful import Resource
from flask import render_template, make_response, request
from commonLibs.globalvariables import GlobalVariables

class Home(Resource):

    def get(self):
        GlobalVariables.LOGGER.info("MongoDB content : {}".format(str([entry for entry in GlobalVariables.APP.db.entries.find({})])))
        entriesWithDate = [
            (
                entry['content'],
                entry['date'],
                datetime.datetime.strptime(entry['date'],"%Y-%m-%d").strftime("%b %d %Y") 
            )
            for entry in GlobalVariables.APP.db.entries.find({})
        ]
        return make_response(render_template(GlobalVariables.HOME_PAGE,entries=entriesWithDate), 200)

    def post(self):
        entryContent = request.form.get("content")
        formattedDate = datetime.datetime.today().strftime("%Y-%m-%d")
        GlobalVariables.LOGGER.info("Microblog entry : {}, Date : {}".format(entryContent,formattedDate))
        GlobalVariables.LOGGER.info("Insert MongoDB content : {}".format(str({"content":entryContent,"date":formattedDate})))
        GlobalVariables.APP.db.entries.insert_one({"content":entryContent,"date":formattedDate})
        entries = [entry for entry in GlobalVariables.APP.db.entries.find({})]
        entriesWithDate = [
            (
                entry['content'],
                entry['date'],
                datetime.datetime.strptime(entry['date'],"%Y-%m-%d").strftime("%b %d %Y") 
            )
            for entry in GlobalVariables.APP.db.entries.find({})
        ]

        return make_response(render_template(GlobalVariables.HOME_PAGE,entries=entriesWithDate), 201)
