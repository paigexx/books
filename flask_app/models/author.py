from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book


class Author():
    def __init__(self, data): 
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.books = []

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
    
    # @classmethod
    # def get_author(cls, data):
    #     query = "SELECT * FROM authors WHERE authors.id = %(author_id)s;"
    #     results = connectToMySQL("books").query_db(query, data)
    #     # author = cls(results[0])
    #     return cls(results[0])

    @classmethod 
    def get_author_join(cls, data):
        query = "SELECT * FROM books JOIN favorite ON books.id = favorite.book_id JOIN authors ON favorite.author_id = authors.id WHERE authors.id = %(author_id)s;"

        results = connectToMySQL("books").query_db(query, data)
        print(results)

        if len(results) < 1: 
            query = "SELECT * FROM authors WHERE authors.id = %(author_id)s;"
            result = connectToMySQL("books").query_db(query, data)
            return cls(result[0])

        author = cls(results[0])

        for row in results: 

            book_data = {
                "id": row["book_id"],
                "title": row["title"],
                "num_of_pages": row["num_of_pages"]
            }

            author.books.append(book.Book(book_data))
        print(author.books)
        return author





# SELECT books.id AS book_id, authors.id AS author_id, title, num_of_pages, books.created_at AS book_created_at, books.updated_at AS book_updated_at, name, authors.created_at AS author_create_at, authors.updated_at AS author_updated_at FROM books JOIN favorite ON books.id = favorite.book_id JOIN authors ON favorite.author_id = authors.id;