def add_book(catalog, title, author, category):
    book = {
        'title': title,
        'author': author,
        'category': category
    }
    catalog.append(book)

def search_by_title(catalog, title):
    return [book for book in catalog if book['title'].lower() == title.lower()]

def search_by_author(catalog, author):
    return [book for book in catalog if book['author'].lower() == author.lower()]

def search_by_category(catalog, category):
    return [book for book in catalog if book['category'].lower() == category.lower()]

def main():
    catalog = []
    add_book(catalog, "The Great Gatsby", "F. Scott Fitzgerald", "Fiction")
    add_book(catalog, "To Kill a Mockingbird", "Harper Lee", "Fiction")
    add_book(catalog, "A Brief History of Time", "Stephen Hawking", "Science")

    print("Search by title 'The Great Gatsby':")
    print(search_by_title(catalog, "The Great Gatsby"))

    print("\nSearch by author 'Harper Lee':")
    print(search_by_author(catalog, "Harper Lee"))

    print("\nSearch by category 'Science':")
    print(search_by_category(catalog, "Science"))

if __name__ == "__main__":
    main()
