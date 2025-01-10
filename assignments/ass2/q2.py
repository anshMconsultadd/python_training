def library_menu():
    library = []

    menu_options = [
        "1. Add a book",
        "2. Remove a book",
        "3. Search for a book",
        "4. List all books",
        "5. Exit"
    ]
    for menu in menu_options:
        print(menu)
   
    while True:
        print("\nLibrary Menu:")
        
        try:
            choice = int(input("Enter your choice: "))
            
            if choice == 1:
                book = input("Enter the name of the book to add: ").strip()

                library.append(book)
                print(f"'{book}' added to the library.")
                
            
            elif choice == 2:
                book = input("Enter the name of the book to remove: ").strip()
                library.remove(book)
                print(f"'{book}' removed from the library.")
                
            
            elif choice == 3:
                book = input("Enter the name of the book to search: ").strip()
                print({book})
            
            elif choice == 4:
                print("Books in the library:")
                for books in library:
                    print(books)
            
            elif choice == 5:
                print("Exiting")
                break
            
            else:
                print("Invalid choice! ")

        except :
            print("Invalid input! Please enter a valid number.")

library_menu()
