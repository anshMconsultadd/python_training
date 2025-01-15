class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"


    def __lt__(self, other):
        return self.title < other.title


    def __gt__(self, other):
        return self.author < other.author


    def __eq__(self, other):
        return self.year == other.year

  
    @staticmethod
    def sort_by_title(books):
        return sorted(books, key=lambda book: book.title)

 
    @staticmethod
    def sort_by_author(books):
        return sorted(books, key=lambda book: book.author)

  
    @staticmethod
    def sort_by_year(books):
        return sorted(books, key=lambda book: book.year)



books = [
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("1984", "George Orwell", 1949),
]


sorted_by_title = Book.sort_by_title(books)
print("Sorted by title:", sorted_by_title)

# Sorting by author
sorted_by_author = Book.sort_by_author(books)
print("Sorted by author:", sorted_by_author)

# Sorting by year
sorted_by_year = Book.sort_by_year(books)
print("Sorted by year:", sorted_by_year)
