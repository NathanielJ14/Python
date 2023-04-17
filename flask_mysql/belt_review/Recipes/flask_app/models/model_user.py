# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app import app, bcrypt

from flask_app.models import model_user

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


DB = "recipes_schema"

class User:
    

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
    
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        user_id = connectToMySQL(DB).query_db(query, data)
        return user_id

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(DB).query_db(query, data) 
        if not results:
            return False
        return cls(results[0])


    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL(DB).query_db(query, data)
        if not result:
            return False
        return cls(result[0])

    @classmethod
    def get_all(cls, data):
        query = "SELECT * FROM users"
        result = connectToMySQL(DB).query_db(query, data)
        all_users = []
        for dict in result:
            all_users.append(cls(dict))
        return all_users

    @staticmethod
    def validate_user(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 3:
            flash("First Name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last Name must be at least 3 characters.")
            is_valid = False
        if len(user['email']) < 3:
            flash("Email must be at least 3 characters.")
            is_valid = False
        elif not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", "err_user_email")
            is_valid = False
        else:
            potential_user = User.get_one_by_email(user)
            if potential_user:
                is_valid = False
                flash('Email is already in use!', 'err_user_email')
        if len(user['password']) < 3:
            flash("Password must be at least 3 characters.")
            is_valid = False
        if not user['password'] == user['confirmpassword']:
            flash("Passwords dont match")
        return is_valid


    @staticmethod
    def validator_login(data):
        is_valid = True
        if not data["email"]:
            is_valid = False
            flash("Email is requried", "err_user_email_login")
        elif not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email address", "err_user_email")
        if not data["password"]:
            is_valid = False
            flash("Password is required", "err_user_password_login")
        if is_valid:
            potential_user = User.get_one_by_email(data)
            if not potential_user:
                is_valid = False
                flash("invalid Credentails", "err_user_password_login")
            else:
                if not bcrypt.check_password_hash(potential_user.password, data["password"]):
                    is_valid = False
                    flash("invalid Credentails", "err_user_password_login")
                else:
                    session['uuid'] = potential_user.id
        return is_valid

