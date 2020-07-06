#1. user registration
def user_registration():
    name= input("Enter your name : ")
    user_contact = int(input("Enter your contact no :"))
    password = input("Create your password :")
    user_name = input("Create your user-name : ")
    return (name, user_contact,password,user_name)

def user_registeration_successful(id):
    print("User successfully registered! Your user id is: ", id)

def already_exist_user():
    print("This user_name used by another user, Please choose another user_name")

def user_registeration_failed():
    print("Enter a valid information ")

    
#3. user login
def user_login():
    # user_id = int(input("Enter your U_ID no :"))
    user_name= input("Enter your User_Name : ")
    password = input("Enter you password :")
    # user_contact = int(input("Enter your contact no :"))
    # return (user_id,user_name,user_contact)
    return (user_name,password)

def user_login_successful(name):
    print(f"Hi! {name} You have succesfully logged in, Welcome to library  ")
    
def user_login_failed():
    print("Enter a valid information")


#3-B. Notified to the librarian and user
def display_user_books(row):
    print(row)
    
def display_notification():
    print("\nThese books have been more than 14 days since you took the book, its detail below :")

# def notifiy_user():   #****************
#     userid = int(input("Enter your user_id :"))
#     return (userid)

# def notifiy_user_success(b_name,b_author,b_rented_date):
#     print(f"It has been more than 14 days since you took the book, your book name : {b_name},author name : {b_author}")
#     # print("")


#3A. user option choice for action perform
def user_choise():
    print("\n============= Welcome to 'User-Library' Management System! ====================\n")
    print("Press 31 for update your details")
    print("Press 32 for issue a book")
    print("Press 33 for get your fees")
    print("Press 34 for return your issued book ")
    print("Press 0 to log out")
    return input()

#3-31. update user detal
def update_user_details():
    # user_id = int(input("Enter USER-ID number :"))
    update_user_name = input("Enter your new_name : ")
    update_user_contact = int(input("Enter your new_contact no :"))
    update_user_password = input("Enter a new password : ")
    # return (update_user_name, update_user_contact, user_id)
    return (update_user_name, update_user_contact,update_user_password)

def update_user_successfully():
    print("User detail has been updated successfully")

def update_user_failed():
    print("Enter valid user_id ")



#3-32. user issue book from library
def user_issue_book():
    # user_id = int(input("Enter your u_id : "))  # because 1st user logged in then then he issue a book so user_id comes from global 'id' 
    # today_date = date.today()
    book_id = int(input("Enter your book_id :"))
    # return (user_id,book_id)
    return book_id

def user_issue_book_successfully():
    print("User issue a book successfully")

def user_isuue_book_failed():
    print("Sorry! This book is not available")


#3-33/3-34. Get and Update user_fee detail
#    Get rental day
def rental_day():
    book_id = int(input("Enter your book_id :"))
    # user_id = int(input("Enter your user Id : "))

    return (book_id)

def show_get_day_success(days):
    print("Total days you rent the book : ",days)
def show_get_day_failed():
    print("Enter a valid information")

#  update user_fee detail
# def return_book():
#     book_id = int(input("Enter book_id : "))
#     return (book_id)

def update_user_fee_success(total_fine):
    print("Total fee you rented the book : ",total_fine)
def update_user_fee_failed():
    print("Enter a valid information")

def no_book_issue():
    print("You are not issue this book")

def get_fee_detail():
    print("Please enter your issued book-id")


 #3-34. return book(update u_fee(u_id), rented_date(b_id), rented_user(uid))

# def get_user_id():
#     book_id = int(input("Enter your book_id :"))  # used by another function no (3-33)
#     return (book_id)

def get_user_id_successfully(user_id):
    print("Your user id : ", user_id)
    print("You have sucessfull return book with fee")

def user_id_failed():
    print("Please enter valid Id ")
    
   
#2. librarian registration
def librarian_registration():
    librarian_name= input("Enter your name : ")
    librarian_contact = int(input("Enter your contact no :"))
    password = input("Create your password : ")
    user_name = input("Create your user-name :")
    return (librarian_name,librarian_contact, password,user_name)

def librarian_registration_successful(id):
    print("User successfully registered! Your librarian id is: ", id)

def already_exist_librarian():
    print("This user_name used by another librarian, Please choose another user_name")

def librarian_registration_failed():
    print("Librarian Registeration Failed!")


#4. librarian login
def librarian_login():
    # librarian_id = int(input("Enter your L_ID no :"))
    user_name= input("Enter your User Name : ")
    password = input("Enter you password :")
    # librarian_contact = int(input("Enter your contact no :"))
    return (user_name,password)

def librarian_login_successful(name):
    print(f"Hi! {name} You have succesfully logged in, Welcome to library  ")
    
def librarian_login_failed():
    print("Enter a valid information")

#4-B. Notify Librarian detail of user whose issued book day complete 14 days
def display_librarian_user_books_detail(rows):
    print(rows)
def display_notification_for_librarian():
    print("\nThese books have been taken by user by more than 14 days , its detail below :")

#4A. Librarian choice to perform actions
def librarian_choise():
    print("============= Welcome to Librarian Library Management System! ====================")
    print("Press 41 for add books")
    print("Press 42 for delete books")
    print("Press 43 for udate books details")
    print("Press 44 for delete user detail")
    print("Press 0 to log out")
    return input()


 #4-41. Add books on data base (add books by librarian)
def add_books():
    book_name= input("Enter new book name : ")
    book_author = input("Enter book author name :")
    book_publication = input("Enter book publication name : ")
    return (book_name, book_author, book_publication)

def add_books_successfully():
    print("successfully add this book on library")

def add_book_failed():
    print("something went wrong book has not add")

#4-42. Delete book on data base
def delete_book():
    book_id = int(input("Enter book_ID for delete data : "))
    return (book_id)

def delete_book_successfully():
    print("Book has been deleted successfully")

def delete_book_failed():
    print("Enter valid book_id no")

def book_not_available():
    print("This book id is not available in library")

#4-43. Update book details
def update_book_details():
    book_id = int(input("Enter your BOOK-ID number :"))
    update_book_name = input("Update your book name :")
    update_book_author = input("Update book author name : ")
    update_book_publication = input("Update book publication name :")
    return (update_book_name, update_book_author, update_book_publication, book_id)

def update_book_successfully():
    print("Book has been updated successfully")

def update_book_failed():
    print("Enter valid book_id no")

#4-44. delete user
def delete_user():
    user_id = int(input("Enter USER_ID for delete data : "))
    return (user_id)

def delete_user_successfully():
    print("User has been deleted successfully")

def delete_user_failed():
    print("Enter valid user_id no")

def user_not_available():
    print("This user id is not available")


#5. Dsplay all books in library
def display_all_books(row):
    print(row)

#6 Display avilable books
def display_available_books(row):
    print(row)



# 0. exit from LMS
def exit():
    print("Thankyou for using LMS!")

    
#User Options choice for else condition
def enter_valid_choice():
    print("Enter valid integer number ")


def start():
    print("\n============= Welcome to Library Management System! ====================\n")

    print("Press 1 for User Registration")
    print("Press 2 for Librarian Registration")

    print("Press 3 for User Login")
    # print("Press 31 for user login update his details")
    # print("Press 32 for user issue a book")
    # print("Press 33 for get fees")
    # print("Press 34 for return issued book ")

    print("Press 4 for Librarian Login")
    # print("Press 41 for Librarian Login and add books")
    # print("Press 42 for Librarian Login and delete books")
    # print("Press 43 for Librarian Login and udate books details")
    # print("Press 44 for delete user detail")

    print("Press 5 for display all book are in library")
    print("Press 6 for display available books in libraray")

    print("Press 0 to exit")
    return input()


# Different Error handling message 
def user_error(): # for ValueError
    print("Please enter contacta no only in digit")

def user_issue_book_error():
    print("Enter a valid book- id no")

def rental_day_error():
    print("Enter only integer value for book-id")

def librarian_delete_book_error():
    print("Please Enter book id in iterger formate")

def update_book_error():
    print("Please Enter book id in iterger formate")

def delete_user_error():
    print("Enter user id in integer value ")

def del_user_error():
    print("This user id does not exists")

def book_id_not_available():
    print("This book id is not present in library choose your issued_book_id")

# unexpected error for for all method/function
def unknown_error(): # Unexpected Error
    print("Unexpected Error found")


    