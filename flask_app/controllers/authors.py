import re
from flask_app.config import mysqlconnection
from flask_app import app
from flask import redirect, render_template, request
from flask_app.models import author


@app.route("/")
def index():
    return redirect("/authors")


@app.route("/authors")
def author_homepage():
    authors = author.Author.all_authors()
    return render_template("authors.html", authors = authors)

@app.route("/author/create", methods = ["POST"])
def create_author():
    author_id  = author.Author.create_author(request.form)
    return redirect("/authors")

@app.route("/author/<int:author_id>")
def show_author(author_id):
    data = {
        "author_id": author_id
    }
    author_in_db = author.Author.get_author_join(data)
    return render_template("show_author.html", author = author_in_db)

