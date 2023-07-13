from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "dojo_ninja"


class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    #read
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        results = connectToMySQL(DATABASE).query_db(query) 
        ninjas = []
        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    
    # Write
    @classmethod
    def save(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age) Values ( %(first_name)s, %(last_name)s, %(age)s);"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    #update
    @classmethod
    def update(cls, data):
        query = """
                UPDATE ninjas
                SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s
                WHERE id = %(id)s; 
                """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    # get one
    @classmethod
    def get_user(cls, data):
        query = """SELECT * 
                   FROM ninjas 
                   WHERE id = %(num)s;        
                """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])
    
    # delete
    @classmethod
    def delete(cls, data):
        query = """
            DELETE 
            FROM ninjas 
            WHERE id = %(num)s;        
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
