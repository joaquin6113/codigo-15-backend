from flask import jsonify


def response(e, status=200):
    if status == 500:
        output = jsonify({"ok": False, "data": str(e)}), status
    else:
        output = jsonify({"ok": True, "data": e}), status

    return output


def generate_id(data):
    return len(data) + 1


def search_book(books, book_id):
        for book in books.books:
            if book.id == book_id:
                return book
        return None