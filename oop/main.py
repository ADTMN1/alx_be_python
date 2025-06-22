from book_class import Book as BookWithYear
from library_system import Book, EBook, PrintBook, Library
from polymorphism_demo import Shape, Rectangle, Circle

def main():
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")

if __name__ == "__main__":
    main()

def test_library():
    my_library = Library()
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)
    my_library.list_books()

def test_book_class():
    my_book = BookWithYear("1984", "George Orwell", 1949)
    print(my_book)          # __str__
    print(repr(my_book))    # __repr__
    del my_book

if __name__ == "__main__":
    test_library()
    print()  # separate output
    test_book_class()
