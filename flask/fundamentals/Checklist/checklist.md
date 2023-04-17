#pre-req
`this only needs to be done once on your computer
```````
pip install pipenv
```````

#checklist 
`steps we need to take to go from 0 to hero (aka a hello world application)

- create a folder for  our current assignment/project
- go into the folder in console using cd 
- open a terminal inside the folder
- create a virtenv with the correct dependantcies 
````
python -m pipenv install flask -> Windows
````
- `Warning`: Check and make sure we have __pipfile__ and __pipfile.loc__ inside our folder!!! If we dont we need to fix it. 

- jump into virt env
```
python -m pipenv shell
```

- set up a file structure 
    - project folder
        - pipfile.loc
        - pipfile
        - server.py
        -config
            -mysqlconnection.py
        -models
            -model_friend.py

## server.py
````py 


from flask import Flask
app = Flask(__name__)

#This will move locations later

@app.route('/')
def hello_world():
    return 'Hello World!'


    #must be at the bottom
    
if __name__=="__main__":
    app.run(debug=True)



#without comments for easy use
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

    
if __name__=="__main__":
    app.run(debug=True)







##Connecting to a database

    # a cursor is the object we use to interact with the database
import pymysql.cursors
# this class will give us an instance of a connection to our database
class MySQLConnection:
    def __init__(self, db):
        # change the user and password as needed
        connection = pymysql.connect(host = 'localhost',
                                    user = 'root', 
                                    password = 'root', 
                                    db = db,
                                    charset = 'utf8mb4',
                                    cursorclass = pymysql.cursors.DictCursor,
                                    autocommit = True)
        # establish the connection to the database
        self.connection = connection
    # the method to query the database
    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                query = cursor.mogrify(query, data)
                print("Running Query:", query)
     
                cursor.execute(query)
                if query.lower().find("insert") >= 0:
                    # INSERT queries will return the ID NUMBER of the row inserted
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().find("select") >= 0:
                    # SELECT queries will return the data from the database as a LIST OF DICTIONARIES
                    result = cursor.fetchall()
                    return result
                else:
                    # UPDATE and DELETE queries will return nothing
                    self.connection.commit()
            except Exception as e:
                # if the query fails the method will return FALSE
                print("Something went wrong", e)
                return False
            finally:
                # close the connection
                self.connection.close() 
# connectToMySQL receives the database we're using and uses it to create an instance of MySQLConnection
def connectToMySQL(db):
    return MySQLConnection(db)






## model.py

# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask').query_db(query)
        # Create an empty list to append our instances of friends
        all_friends = []
        # Iterate over the db results and create instances of friends with cls.
        for dict in results:
            all_friends.append( cls(dict) )
        return all_friends # returns a list with a instances
            




from flask import Flask, render_template
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html")
            
if __name__ == "__main__":
    app.run(debug=True)



