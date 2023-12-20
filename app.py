from flask import Flask , request , jsonify , json
from db_conn import connection
import db_info
import psycopg2

app = Flask(__name__)

@app.get("/")
def home():
    return('Welcome to RunVerse \nLets help ourself by Adopting Tree')



"""  
while the POST method does not inherently provide encryption, 
using HTTPS for transmission and implementing encryption at the server level can 
help ensure data security from the web source to the backend database
"""

# For Users
@app.route("/api/users" , methods = ["POST" , "GET"])
def create_user():
    if request.method == 'POST':
        data = request.get_json() #python dict
        name = f"{data['FirstName']} {data['LastName']}"
        
        # Adding to DataBase
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(db_info.create_users_table_query)
                try:
                    cursor.execute(db_info.insert_users , tuple(data.values()))
                    user_id = cursor.fetchone()
                    print(user_id)
                    return  {
                        "id" : user_id[0] ,
                        "message": f"new User {name} added"
                        }
                except psycopg2.errors.UniqueViolation as e:
                    connection.rollback()
                    return {"error": str(e)}
    else:
        return "API END FOR USER TABLE"


#For Species
@app.route("/api/species" , methods = ["POST" , "GET"])
def create_species():
    if request.method == 'POST':
        data = request.get_json() #python dict
        name = data['ScientificName']
        # Adding to DataBase
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(db_info.create_species_table_query)
                try:
                    cursor.execute(db_info.insert_species , tuple(data.values()))
                    species_id = cursor.fetchone()
                    print(species_id)
                    
                    return  {
                        "id" : species_id[0] ,
                        "message": f"new species {name} added"
                        }
                except psycopg2.errors.UniqueViolation as e:
                    connection.rollback()
                    return {"error": str(e)}
    else:
        return "API END FOR species TABLE"
    

#For Trees
@app.route("/api/trees" , methods = ["POST" , "GET"])
def create_trees():
    if request.method == 'POST':
        data = request.get_json() #python dict
        name = data['Location']
        # Adding to DataBase
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(db_info.create_trees_table_query)
                try:
                    cursor.execute(db_info.insert_trees , tuple(data.values()))
                    trees_id = cursor.fetchone()
                    print(trees_id)
                    
                    return  {
                        "id" : trees_id[0] ,
                        "message": f"new tree at {name} Planted"
                        }
                except psycopg2.errors.UniqueViolation as e:
                    connection.rollback()
                    return {"error": str(e)}
    else:
        return "API END FOR trees TABLE"




#For Adoption
@app.route("/api/adoptions" , methods = ["POST" , "GET"])
def create_adoptions():
    if request.method == 'POST':
        data = request.get_json() #python dict
        donation = data['DonationAmount']
        # Adding to DataBase
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(db_info.create_adoptions_table_query)
                try:
                    cursor.execute(db_info.insert_adoptions , tuple(data.values()))
                    adoptions_id = cursor.fetchone()
                    print(adoptions_id)
                    
                    return  {
                        "id" : adoptions_id[0] ,
                        "message": f"new tree is Adopted , Thanks for your {donation} Donations :)"
                        }
                except psycopg2.errors.UniqueViolation as e:
                    connection.rollback()
                    return {"error": str(e)}
    else:
        
        return "API END FOR adoptions TABLE"


#For Dashbord
@app.route("/dashbord" , methods = ["POST" , "GET"])
def dashbord():
    return "Here one can see analytical dashbord"