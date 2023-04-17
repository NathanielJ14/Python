from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database

DB = 'recipes_schema'

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30min = data['under_30min']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        


    @classmethod
    def save(cls , data):
        query = "INSERT INTO ninjas ( name, description, instructions, under_30min, user_id, created_at , updated_at ) VALUES (%(name)s, %(description)s, %(instructions)s, %(under_30min)s, %(user_id)s, NOW(),NOW());"
        ninja_id = connectToMySQL(DB).query_db(query, data)
        return ninja_id

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s"
        results = connectToMySQL(DB).query_db(query, data) 
        if not results:
            return False
        return cls(results[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(DB).query_db(query)

        all_recipes = []
        for dict in results:
            all_recipes.append( cls(dict) )
        return all_recipes
