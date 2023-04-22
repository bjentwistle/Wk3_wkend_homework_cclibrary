from models.book import Book

#book instance = Book(title, author, genre, loaned, location, synopsis, unique_id)
book1 = Book("Ender's Game", "Orson Scott-Card", "Science Fiction", True, "Aisle 4, shelf O", "A young boy, Ender, is trained to become the ultimate leader against a deadly enemy","A001")
book2 = Book("Persuasion", "Jane Austen", "Period (fiction)", False, "Aisle 10, shelf A", "A lesson in not listening to your elders when love and your happiness is involved", "B001")
book3 = Book("Diary of a Wimpy Kid", "Jeff Kinney", "Humor (fiction)", True, "Aisle 1, shelf K", "Sixth grader Greg Heffeley chronicles his first year of middle school", "C001")

books = [book1, book2, book3]

#Class methods needed:

def add_new_book(book):
    books.append(book)

#def remove_book_to_library(book):




