# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import model_email
# model the class after the friend table from our database
import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

DB = "email_validation_schema"

class Email:

    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at ) VALUES ( %(email)s, NOW() , NOW() );"
        email_id = connectToMySQL(DB).query_db(query, data)
        return email_id

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL(DB).query_db(query)
        
        all_emails = []
        for dict in results:
            all_emails.append(cls(dict))
        return all_emails


    @classmethod
    def get_one(cls, email_id):
        query = "SELECT * FROM emails WHERE id = %(id)s"
        data = {'id': email_id}
        results = connectToMySQL(DB).query_db(query, data)
        return cls(results[0])


    @staticmethod
    def validate_user( data ):
        is_valid = True
        # test whether a field matches the pattern
        if not data['email']:
            is_valid = False
            flash("email is required", "err_user_email")
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", "err_user_email")
            is_valid = False
        return is_valid