# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
# model the class after the friend table from our database
class User:
    DB = "dojo_survey_schema"

    def __init__( self , data ):
        self.id = data['id']
        self.name = ['name']
        self.email = ['email']
        self.game = ['game']
        self.comment = ['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['email']) < 3:
            flash("Email must be at least 3 characters.")
            is_valid = False
        if len(user['why']) < 5:
            flash("Comment must be at least 5 characters.")
            is_valid = False
        return is_valid
