from utils.utils import generate_id, search_book

class Book:
    books = []

    def __init__(self, title=None, isbn=None, author=None, description=None, plot=None, image_url=None):
        self.id = None
        self.title = title        
        self.isbn = isbn
        self.author = author
        self.description = description
        self.plot = plot
        self.image_url = image_url


    def list_books(self):
        return [item.to_json() for item in self.books]


    def search_books_by_id(self, book_id):
        book_searched = search_book(self, book_id)

        if book_searched is not None:
            return book_searched.to_json()
        
        return None


    def insert_book(self, book):
        book.id = generate_id(self.books)
        self.books.append(book)


    def update_book(self, book_id, request):
        book_searched = search_book(self, book_id)

        if book_searched is None:
            return "Libro no encontrado"
        
        book_searched.title = request.get("title", book_searched.title)
        book_searched.isbn = request.get("isbn", book_searched.isbn)
        book_searched.author = request.get("author", book_searched.author)
        book_searched.description = request.get("description", book_searched.description)
        book_searched.plot = request.get("plot", book_searched.plot)
        book_searched.image_url = request.get("image_url", book_searched.image_url)

        return book_searched.to_json()


    def delete_book(self, book_id):
        current_book = search_book(self, book_id)
        try:
            self.books.remove(current_book)
            return "Eliminado correctamente"
        except Exception as e:
            return str(e)


    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "isbn": self.isbn,
            "author": self.author,
            "description": self.description,
            "plot": self.plot,
            "image_url": self.image_url
        }