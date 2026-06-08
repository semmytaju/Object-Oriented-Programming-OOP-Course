# class 1
class Book:
    # constructor with parameters
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author}."

# class 2
class Library:
    # constructor without parameter
    def __init__(self):
        self.books = []

    # fungsi menambah buku
    def addBook(self, book):
        print("Added this book: "+book.__str__())
        self.books.append(book)

    # fungsi menghapus buku
    def removeBook(self, book):
        self.books.remove(book)

    # fungsi mencari buku berdasarkan judul
    def searchBook(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

# class 3
class Student:
    # constructor with parameter
    def __init__(self, name):
        self.name = name
        self.borrowed_book = None
        print(f"{self.name} has been registered.")

    # fungsi meminjam buku
    def borrowBook(self, book):
        if self.borrowed_book is None:
            self.borrowed_book = book
            print(f"{self.name} has borrowed {book.title}.")
        else:
            print(f"{self.name} has already borrowed {self.borrowed_book.title}.")

    # fungsi mengembalikan buku
    def returnBook(self):
        if self.borrowed_book is not None:
            book = self.borrowed_book
            self.borrowed_book = None
            print(f"{self.name} has returned {book.title}.")
        else:
            print(f"{self.name} has not borrowed any book.")

    # fungsi menampilkan buka yang dipinjam
    def viewBorrowedBooks(self):
        if self.borrowed_book is not None:
            print(f"{self.name} has borrowed {self.borrowed_book.title}.")
        else:
            print(f"{self.name} has not borrowed any book.")



# create objek library
unklab_library = Library()

print("INPUT BUKU KE PERPUSTAKAAN:");
print("==========================");
# add beberapa buku ke perpustakaan
book1 = Book("Python Programming", "Semmy Taju", "123456")
book2 = Book("Java Programming", "Green Sandag", "234567")
book3 = Book("C++ Programming", "Patricia Eugenie", "345678")
unklab_library.addBook(book1)
unklab_library.addBook(book2)
unklab_library.addBook(book3)

print("\nMAHASISWA DAFTAR DI PERPUSTAKAAN:");
print("==================================");
# creat objek mahasiswa
student1 = Student("Kadek")
student2 = Student("Jeremy")
student3 = Student("Ellen")
student4 = Student("Bobby")
student5 = Student("Putra")

print("\nPROSES PINJAM BUKU DI PERPUSTAKAAN:");
print("====================================");
# meminjam buku
student1.borrowBook(book1)
student2.borrowBook(book2)
student2.borrowBook(book3) # tidak bisa meminjam lebih dari satu buku.
student3.borrowBook(book2)
student4.borrowBook(book3)
student5.borrowBook(book3)

# view buku yang dipinjam
student1.viewBorrowedBooks() 
student2.viewBorrowedBooks() 

# mengembalikan buku
student1.returnBook()
student2.returnBook()

# view buku yang dipinjam setelah dikembalikan
student1.viewBorrowedBooks() 
student2.viewBorrowedBooks() 