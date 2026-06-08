# class 1
class Author:
    def __init__(self, name):
        self.name = name
           
# class 2
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# class 3
class Library:
    def __init__(self, books):
        self.books = books
    
    def display_books(self):
        print("Books in the library:")
        for book in self.books:
            print("- {} by {}".format(book.title, book.author.name))
                   
# beberapa object dari kelas Author
author1 = Author("Semmy Taju")
author2 = Author("Eugenie Patricia")
author3 = Author("Stevi Gabriel")

# beberapa object dari kelas Book
book1 = Book("Java Programming", author1)
book2 = Book("Python Programming", author2)
book3 = Book("Python Programming", author3)

# object dari kelas Library dan menambahkan buku-buku ke dalam object
library = Library([book1, book2, book3])

# call metode display_books untuk menampilkan buku-buku di dalam perpustakaan
library.display_books()

