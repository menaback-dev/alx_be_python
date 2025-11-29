class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self._is_checked_out = True
    def return_book(self):
        self._is_checked_out = False

class Library:
        def __init__(self):
            self._books = []
            
        def add_book(self, book):
            self._books.append(book)

        def check_out_book(self, title):
            for book in self._books:
                if book.title == title:
                    if not book._is_checked_out:
                         book.check_out()
                    else:
                         print(f"'{title}' is already checked out.")
                    return
            print(f"Book '{title}' not found in library.")
        
        def return_book(self, title):
            for book in self._books:
                if book.title == title:
                    if book._is_checked_out:
                        book.return_book()
                    else:
                        print(f"'{title}' was not checked out.")
                    return
            print(f"Book '{title}' not found in library.")

        def list_available_books(self):
            available = False
            for book in self._books:
                if not book._is_checked_out:
                    print(f"{book.title} by {book.author}")
                    available = True
            if not available:
                print("No available books.")

