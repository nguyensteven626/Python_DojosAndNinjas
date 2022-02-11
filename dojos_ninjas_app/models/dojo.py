from dojos_ninjas_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja 

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas =[]

    @classmethod
    def get_dojo(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of friends
        all_dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for one_dojo in results:
            all_dojos.append( cls(one_dojo) )
        return all_dojos
    
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s , NOW() , NOW() );"
        result = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        return result 

    # @classmethod
    # def get_one_with_ninjas(cls, data):
    #     query = 'SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
    #     results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
    #     print('======================')
    #     print(results)  
    #     display_dojo = cls(results[0])
    #     for row in results:
    #         n = {
    #             'id':row['ninjas.id'],
    #             'first_name':row['first_name'],
    #             'last_name':row['last_name'],
    #             'age':row['age'],
    #             'created_at':row['ninjas.created_at'],
    #             'updated_at':row['ninjas.updated_at']
    #         }
    #     display_dojo.ninjas.append(Ninja(n))

    #     return display_dojo


    @classmethod
    def get_one_with_ninjas(cls, data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        print(results)
        return results

    
    
    
    
    
    
    # @classmethod 
    # def get_dojo(cls, data):
    #     query = "SELECT * FROM dojos WHERE id = %(id)s;"
    #     result = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
    #     one_dojo = cls(result[0])
    #     return one_dojo
 