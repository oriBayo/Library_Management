class Menu:

    def show_login(self):
        print('-------------Welcome-------------')   
        user_name = input("Please enter your Username:")
        user_email = input("Please enter your email:")
        return user_name,user_email

    def show_menu(self):
        print()
        print('-------------Menu-------------')
        print("For adding a book - Press 1")
        print("For deleting a book - Press 2")
        print("For changing book locations - Press 3")
        print("For registering a new reader - Press 4")
        print("For removing a reader - Press 5")
        print("For searching books by author - Press 6")
        print("For reading a book by a reader - Press 7")
        print("For ordering all data - Press 8")
        print("For saving all data - Press 9")
        print("For loading data - Press 10")
        print("For display data - Press 11")
        print("For exit - Press 12")
        print('-------------Menu-------------')
        print()
        user_choice = input("Option:")
        return user_choice

    def press1(self):
        print("-------------Add Book-------------")
        title = input("Book Title:")
        author = input("Author Name:")
        num_of_pages = input("Pages:") 
        return title,author,num_of_pages

    def press2(self):
        print("-------------Delete Book-------------")
        title = input("Book Title:")
        return title

    def press3(self):
        print("-------------Changing Books Location-------------")
        book1_title = input("Title of Book 1:")
        book2_title = input("Title of Book 2:")
        return book1_title,book2_title

    def press4(self):
        print("-------------Register New Reader-------------")
        reader_name = input("Reader Name:")
        reader_ID = input("Reader ID:")
        return reader_name,reader_ID

    def press5(self):
        print("-------------Removing Reader-------------")
        reader_name = input("Reader Name:")
        return reader_name

    def press6(self):
        print("-------------Searching By Author-------------")
        author_name = input("Author Name:")
        return author_name
    
    def press7(self):
        print("-------------Reading A Book-------------")
        reader_id = input("Reader ID:")
        book_title = input("Book Title:")

        return reader_id,book_title

    def press8(self):
        print("-------------Ordring All Books-------------")

    def press9(self):
        print("-------------Saving All Data-------------")
        file_name = input("File Name:")
        return file_name

    def press10(self):
        print("-------------Loading Data-------------")
        file_name = input("file Name:")
        return file_name

    def wrong_pass_or_email(self):
        print("Sorry you type Wrong User/Email!")

    def type_valid_option(self):
        print("Error - you type invalid option")

    def display_books_by_author(self,books):
        for book in books:
            print(book)

    def add_book_faild(self ,result):
        if result == False:
            print("Error - There is no place for a new book")


    def book_not_found(self,result):
        if result == False:
            print("Error - One of the books is not exists")

    def display_library(self,library):
        print()
        print("-------------Display Data-------------")
        print("Reader")
        for reader in library.get_readers():
            reader.display_reader()
        print("Books")
        for index,shelf in enumerate(library.get_shelves()):
            print(f"Shelf {index + 1}:")
            shelf.display_shelf()
        print()
