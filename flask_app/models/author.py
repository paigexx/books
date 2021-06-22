from flask_app.config.mysqlconnection import connectToMySQL

class Author():
    def __init__(self, data): 
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def all_authors(cls):
        query = "SELECT * FROM authors"
        results = connectToMySQL("books").query_db(query)
        print(results)
        authors = []
        for author in results: 
            authors.append(cls(author))        
        print(authors)
        return authors

    @classmethod
    def create_author(cls, data): 
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        author_id = connectToMySQL("books").query_db(query, data)
        print(author_id)
        return author_id