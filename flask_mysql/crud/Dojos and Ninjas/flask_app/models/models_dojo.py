# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app.models import models_ninja
DATABASE = 'dojos_and_ninjas_schema'

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']

        

    @classmethod
    def create(cls, data): 
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        dojo_id = connectToMySQL(DATABASE).query_db(query, data)
        return dojo_id


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)

        all_dojos = []
        for dict in results:
            all_dojos.append( cls(dict) )
        return all_dojos


    @classmethod
    def get_one( cls , data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db( query , data )
        # results will be a list of topping objects with the burger attached to each row. 
        dojo_instance = cls(results[0])
        all_ninjas = []
        for dict in results:
            # Now we parse the burger data to make instances of burgers and add them into our list.
            ninja_data = {
                "id" : dict["ninjas.id"],
                "first_name" : dict["first_name"],
                "last_name" : dict["last_name"],
                "age" : dict["age"],
                "created_at" : dict["ninjas.created_at"],
                "updated_at" : dict["updated_at"],
                "dojo_id" : dict["dojo_id"]
            }
            
            ninja_instance = models_ninja.Ninja(ninja_data)
            all_ninjas.append(ninja_instance)

        dojo_instance.all_ninjas = all_ninjas
        return dojo_instance

    




