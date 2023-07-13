from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "dojo_ninja"


class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    #read
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query) 
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    
    # Write
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) Values ( %(name)s);"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    #update
    @classmethod
    def update(cls, data):
        query = """
                UPDATE dojos
                SET name = %(name)s
                WHERE id = %(id)s; 
                """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    @classmethod
    def get_user(cls, data):
        query = """SELECT * 
                   FROM dojos 
                   WHERE id = %(num)s;        
                """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])
    
    # delete
    @classmethod
    def delete(cls, data):
        query = """
            DELETE 
            FROM dojos 
            WHERE id = %(num)s;        
        """
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
