from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database

DATABASE = 'dojos_and_ninjas_schema'

class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        


    @classmethod
    def save(cls , data):
        query = "INSERT INTO ninjas ( first_name, last_name, age, dojo_id, created_at , updated_at ) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(),NOW());"
        ninja_id = connectToMySQL(DATABASE).query_db(query, data)
        return ninja_id

