from flask import Blueprint, request
from models.book import Book
from utils.utils import response

books = Blueprint('books', __name__, url_prefix="/api/v1/books")

book = Book() 


@books.route("/")
def get_books():
    return response(book.list_books()) # book es instancia vacía (llama funciones)


@books.route("/", methods=['POST'])
def create_book():
    try:
        data = request.get_json()
        new_book = Book(**data)
        book.insert_book(new_book)

        return response("Libro creado correctamente", 201)
    except Exception as e:
        return response(e, 500)
    

@books.route("/<int:book_id>")
def book_by_id(book_id):
    try:
        searched = book.search_books_by_id(int(book_id))

        if not searched:
            return response("No se encontró el libro", 500)
        
        return searched
    
    except Exception as e:
        return response(e, 500)


@books.route("/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    try:
        return response(book.update_book(book_id, request.get_json()))
        
    except Exception as e:
        return response(e, 500)
    

@books.route("/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    try:
        return response(book.delete_book(int(book_id)))
    except Exception as e:
        return response(e, 500)