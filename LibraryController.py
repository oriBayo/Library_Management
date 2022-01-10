from Book import Book
from Library import Library
from Service import Service
from View import Menu

class LibraryController:

    def __init__(self,model,view) -> None:
        self.model = model
        self.view = view
    
    def run(self):
        username,email = self.view.show_login()
        login_result = Service.login(username,email)
        if login_result:
            app_run = True
            while(app_run):
                user_choice = self.view.show_menu()      
                app_run = self.__handle_user_choice(user_choice)
                
                
        else:
            self.view.wrong_pass_or_email()
    
    def __handle_user_choice(self,user_choice):
        match user_choice:

            case '1':           
               self.__add_new_book()
               return True

            case '2':
                self.__delete_book()
                return True
            
            case '3':
                self.__change_location()
                return True
            
            case '4':
                self.__register_reader()
                return True
            
            case '5':
                self.__remove_reader()
                return True
            
            case '6':
                self.__search_by_author()
                return True

            case '7':
                self.__reader_read_book()
                return True

            case '8':
                self.__order_books()
                return True
            
            case '9':
                self.__save_data()
                return True

            case '10':
                self.__load_data()
                return True
            
            case '11':
                self.view.display_library(self.model)
                return True

            case '12':
                return False

            case _:
                self.view.type_valid_option()
                return True

    def __add_new_book(self):
        title,author,num_of_pages = self.view.press1() 
        book = Book(author,title,num_of_pages)
        result = self.model.add_new_book(book)
        self.view.add_book_faild(result)
        
    def __delete_book(self):
        title = self.view.press2() 
        self.model.delete_book(title)

    def __change_location(self):
        book1_title,book2_title = self.view.press3() 
        result = self.model.change_location(book1_title,book2_title) 
        self.view.book_not_found(result)

    def __register_reader(self):
        reader_name,reader_id = self.view.press4() 
        self.model.register_reader(reader_name,reader_id)

    def __remove_reader(self):
        reader_name = self.view.press5() 
        self.model.remove_reader(reader_name)

    def __search_by_author(self):
        author_name = self.view.press6() 
        books = self.model.search_by_author(author_name)
        self.view.display_books_by_author(books)

    def __reader_read_book(self):
        reader_id,book_title = self.view.press7() 
        self.model.reader_read_book(book_title,reader_id)

    def __order_books(self):
        self.view.press8() 
        self.model.order_books()

    def __save_data(self):
        file_name = self.view.press9()
        data = self.model.library_encoder()
        Service.save_file(file_name,data)
        

    def __load_data(self):
        file_name = self.view.press10() 
        data = Service.load_file(file_name)
        self.model.library_decoder(data)        

def main():
    view = Menu()
    model = Library()
    library_controller = LibraryController(model ,view )
    library_controller.run()


if __name__ == "__main__":
    main()
    
