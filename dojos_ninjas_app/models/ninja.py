from dojos_ninjas_app.config.mysqlconnection import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    # @classmethod
    # def save( cls , data ):
    #     query = "INSERT * INTO dojos ( name , bun, meat, calories, restaurant_id, created_at , updated_at ) VALUES (%(name)s, %(bun)s, %(meat)s, %(calories)s, %(restaurant_id)s,NOW(),NOW());"
    #     return connectToMySQL('burgers').query_db(query,data)

    # @classmethod 
    # def save(cls, data):
    #     query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s), %(dojo_id)s, NOW() , NOW();'
    #     results = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
    #     return results

    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas ( first_name, last_name, age, dojo_id ) VALUES ( %(first_name)s , %(last_name)s, %(age)s, %(dojo_id)s);"
        result = connectToMySQL('dojos_ninjas_schema').query_db(query, data)
        return result
        
  
    # @classmethod 
    # def get_ninja(cls, data):
    # query = 'SELECT FROM ninjas WHERE id = %(id)s;' VALUES ()