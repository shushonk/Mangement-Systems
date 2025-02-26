import tkinter as tk
from tkinter import messagebox

class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def displayAvailableBooks(self):
        return self.books

    def borrowBook(self, name, bookname):
        if bookname not in self.books:
            return f"{bookname} BOOK IS NOT AVAILABLE, IT HAS ALREADY BEEN BORROWED OR DOESN'T EXIST."
        else:
            track.append({name: bookname})
            self.books.remove(bookname)
            return f"BOOK ISSUED: THANK YOU, {bookname} has been issued to you, please return it on time."

    def returnBook(self, name, bookname):
        self.books.append(bookname)
        for record in track:
            if name in record and record[name] == bookname:
                track.remove(record)
                break
        return f"BOOK RETURNED: THANK YOU, {bookname} has been returned."

    def donateBook(self, bookname):
        self.books.append(bookname)
        return f"BOOK DONATED: THANK YOU VERY MUCH, {bookname} has been added to the library."


class Student:
    def requestBook(self):
        return input("Enter the name of the book you want to borrow: ")

    def returnBook(self):
        name = input("Enter your name: ")
        book = input("Enter the name of the book you want to return: ")
        return name, book

    def donateBook(self):
        return input("Enter the name of the book you want to donate: ")

track = []  # Track borrowed books as a list of dictionaries

# GUI Class
class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Karnataka Library Management System")
        self.library = Library(["Vistas","shakespeare", "Invention", "Rich & Poor", "Indian", "Macroeconomics", "Microeconomics"])
        self.student = Student()

        # Set up the interface components
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        self.title_label = tk.Label(self.root, text="Welcome to the Karnataka Library", font=("Helvetica", 18))
        self.title_label.pack(pady=20)

        # List available books
        self.list_button = tk.Button(self.root, text="List Available Books", width=20, command=self.list_books)
        self.list_button.pack(pady=10)

        # Borrow Book
        self.borrow_button = tk.Button(self.root, text="Borrow a Book", width=20, command=self.borrow_book)
        self.borrow_button.pack(pady=10)

        # Return Book
        self.return_button = tk.Button(self.root, text="Return a Book", width=20, command=self.return_book)
        self.return_button.pack(pady=10)

        # Donate Book
        self.donate_button = tk.Button(self.root, text="Donate a Book", width=20, command=self.donate_book)
        self.donate_button.pack(pady=10)

        # Track Borrowed Books
        self.track_button = tk.Button(self.root, text="Track Borrowed Books", width=20, command=self.track_books)
        self.track_button.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", width=20, command=self.root.quit)
        self.exit_button.pack(pady=20)

    def list_books(self):
        available_books = self.library.displayAvailableBooks()
        book_list = "\n".join(available_books)
        messagebox.showinfo("Available Books", f"Available Books:\n{book_list}")

    def borrow_book(self):
        # Create new window for borrowing book
        borrow_window = tk.Toplevel(self.root)
        borrow_window.title("Borrow a Book")

        tk.Label(borrow_window, text="Enter your name:").pack(pady=10)
        name_entry = tk.Entry(borrow_window, width=30)
        name_entry.pack(pady=10)

        tk.Label(borrow_window, text="Enter the name of the book you want to borrow:").pack(pady=10)
        book_entry = tk.Entry(borrow_window, width=30)
        book_entry.pack(pady=10)

        def borrow_action():
            name = name_entry.get()
            book = book_entry.get()
            result = self.library.borrowBook(name, book)
            messagebox.showinfo("Borrow Book Result", result)
            borrow_window.destroy()

        borrow_button = tk.Button(borrow_window, text="Borrow Book", width=20, command=borrow_action)
        borrow_button.pack(pady=20)

    def return_book(self):
        # Create new window for returning book
        return_window = tk.Toplevel(self.root)
        return_window.title("Return a Book")

        tk.Label(return_window, text="Enter your name:").pack(pady=10)
        name_entry = tk.Entry(return_window, width=30)
        name_entry.pack(pady=10)

        tk.Label(return_window, text="Enter the name of the book you want to return:").pack(pady=10)
        book_entry = tk.Entry(return_window, width=30)
        book_entry.pack(pady=10)

        def return_action():
            name = name_entry.get()
            book = book_entry.get()
            result = self.library.returnBook(name, book)
            messagebox.showinfo("Return Book Result", result)
            return_window.destroy()

        return_button = tk.Button(return_window, text="Return Book", width=20, command=return_action)
        return_button.pack(pady=20)

    def donate_book(self):
        # Create new window for donating book
        donate_window = tk.Toplevel(self.root)
        donate_window.title("Donate a Book")

        tk.Label(donate_window, text="Enter the name of the book you want to donate:").pack(pady=10)
        book_entry = tk.Entry(donate_window, width=30)
        book_entry.pack(pady=10)

        def donate_action():
            book = book_entry.get()
            result = self.library.donateBook(book)
            messagebox.showinfo("Donate Book Result", result)
            donate_window.destroy()

        donate_button = tk.Button(donate_window, text="Donate Book", width=20, command=donate_action)
        donate_button.pack(pady=20)

    def track_books(self):
        if track:
            borrowed_books = "\n".join([f"{book} is taken by {holder}" for record in track for holder, book in record.items()])
            messagebox.showinfo("Borrowed Books", borrowed_books)
        else:
            messagebox.showinfo("Borrowed Books", "No books are currently borrowed.")

# Create the main window and run the app
if __name__ == "__main__":
    root = tk.Tk()
    library_gui = LibraryGUI(root)
    root.mainloop()
