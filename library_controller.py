from datetime import datetime
from datetime import date
# from date.utils import relative delta
from dateutil.relativedelta import relativedelta

import library_view
import library_model

# global variable user and librarian
id = 0
is_librarian = False


#1. user registration
def user_registration():
    try:
        result = library_view.user_registration()
        account = library_model.create_user_check(result[3])

        if account != None:
            library_view.already_exist_user()

            # user_registration()
            startLMS()
            return

    
        id = library_model.create_user(result[0], result[1], result[2],result[3])

        if(id > 0):  # (id != None)
            library_view.user_registeration_successful(id)
        
        else:
            library_view.user_registeration_failed() # for same user_name
        startLMS()

    except ValueError:
        library_view.user_error() # for enter valid information
        startLMS()
    except:
        library_view.unknown_error()
        startLMS()


#3A. user option choice for action perform
def user_option_choice():
    user_inp = library_view.user_choise()
    if(user_inp == '0'):
        library_view.exit()
        global id
        id = 0
        startLMS()
        return 
    elif(user_inp == '31'): 
        update_user_details()
    elif(user_inp == '32'): 
        user_issue_book()
    elif(user_inp == '33'):
        rental_day()
    elif(user_inp == '34'):
        pay_book_fee()
    else:
        library_view.enter_valid_choice()
        user_option_choice()


#3. user login
def user_login():
    try:
        result = library_view.user_login()
        account = library_model.user_login(result[0], result[1])
        
        if account != None:
            library_view.user_login_successful(account[1])
            
            # library_view.display_user_books()
            
            global id
            id = account[0]
            notified_rental_day_book()
            user_option_choice()
            return #********  

        else:
            library_view.user_login_failed()
            user_login()

    except:
        library_view.unknown_error()


#3B. Notified user for 14 days to the user his issued book detail
def notified_rental_day_book():
    try:
        u_detail = library_model.notify_day(id)
    
        for row in u_detail:
            newRow = (row[0],row[1],row[2],row[3].strftime('%d/%m/%Y'))
            library_view.display_notification()
            library_view.display_user_books(newRow)
        # user_option_choice()  #***********
            # user_option_choice()
    except:
        library_view.unknown_error()


#3-31. User update detals
def update_user_details():
    try:
        result = library_view.update_user_details()
        # id = library_model.update_user_details(result[0],result[1],result[2])
        u_id = library_model.update_user_details(result[0],result[1],result[2],id)

        # if id != None:
        if u_id > 0:
            library_view.update_user_successfully()
            
        else:
            library_view.update_user_failed()

    except ValueError:
        library_view.user_error()
        update_user_details()
        # user_option_choice()                  # create option choise to exit or continue
    except:
        library_view.unknown_error()
        user_option_choice()
        return # ***********


#3-32. user issued a book from library
def user_issue_book():
    try:
        # today_date = date.today()
        result = library_view.user_issue_book()
        u_id = library_model.user_issue_book(id,result)

        if u_id > 0:
            library_view.user_issue_book_successfully()
            user_option_choice()
            return #*********
        else:
            library_view.user_isuue_book_failed()
            user_option_choice()
            return #******
    except ValueError:
        library_view.user_issue_book_error()
        user_issue_book()
    except:
        library_view.unknown_error() 


#3-33. Get user_fee detail and update fee on user id on data-base
def rental_day():
    try:
        result = library_view.rental_day() # book_id
        details = library_model.get_day(result) # result = book_id, details = [b_rented_date, b_rented_user]// [0],[1]

        if details == None:
            library_view.no_book_issue()
            user_option_choice()
            # rental_day()
        else:
            pass

        if  id != details[1]: # if user enter other user's book -id its get invalid information 
            library_view.get_fee_detail()
            return rental_day()
        else:
            pass

        if details != None:            #.......3-33-B. Get total fine of user who issued book from library
            #    get - fine
            #if fine > 0, update fine in db
            #If ok.. successful return book
            #else not successul
            today_date = date.today()  
            rdelta = today_date - details[0] # detail[0] = b_rented_date= rdelta= yyyy-mm-dd formate

            total_fee_value = total_fine(rdelta.days) # res = total amount of fine// rdelta.days convert rdelta into days int formate//
            user_fee_update = library_model.update_user_fee(total_fee_value, details[1])  #detail[1] = b_rented_user= user_id  #3-33-B  update_user_fee
            if user_fee_update != None:
                library_view.update_user_fee_success(total_fee_value) # total_fee_value = how many rs
                user_option_choice()
            else:
                library_view.update_user_fee_failed()

        else:
            library_view.show_get_day_failed()

    except ValueError:
        library_view.rental_day_error()
        user_option_choice()
        # rental_day()
        
    except:
        library_view.unknown_error()
        user_option_choice()


#3-33-C. Get total fine of user who issued book from library
def total_fine(total_days):
    total_fee = 0
#     day = 35
    j = int((total_days -20)/5)
    for i in range(j+1):
        total_fee += (20+5*i)
    return total_fee


#3-34. Return issued book by login user& update user fee of logged in user
def pay_book_fee():
    try:
        result = library_view.rental_day()
        user_detail = library_model.get_user_id(result)

        if user_detail == None:
            library_view.book_id_not_available()
            pay_book_fee()
        else:
            pass 

        if user_detail[0] == id and user_detail != None:
            library_model.paid_user_fee(user_detail[0])  #3-34-B
            library_model.return_book(result) #3-34-C

            library_view.get_user_id_successfully(user_detail[0])
            user_option_choice()
        else:
            library_view.get_fee_detail()
            pay_book_fee()
  
    except ValueError:
        library_view.rental_day_error()
        pay_book_fee()
        # user_option_choice()
    except:
        library_view.unknown_error()


#2. librarian registration
def librarian_registration():
    try:
        result = library_view.librarian_registration()

        account = library_model.create_librarian_check(result[3])

        if account != None:
            library_view.already_exist_librarian()
            # library_view.exit()
            startLMS()
            return

        id = library_model.create_librarian(result[0],result[1],result[2],result[3])
        if(id != None):
            library_view.librarian_registration_successful(id)
        else:
            library_view.librarian_registration_failed()
        startLMS()
    except ValueError:
        library_view.user_error() # for enter valid information
        startLMS()
    except:
        library_view.unknown_error()
        startLMS()

#4A. Librarian choice to perform actions
def librarian_option_choice():
    librarian_inp = library_view.librarian_choise()
    if(librarian_inp == '0'):
        library_view.exit()
        global id
        id = 0
        global is_librarian
        is_librarian = False
        startLMS()
        return
    elif(librarian_inp == '41'):
        add_books()
    elif(librarian_inp == '42'):
        delete_book()
    elif(librarian_inp == '43'):
        update_book_details()
    elif(librarian_inp == '44'):
        delete_user()
    else:
        library_view.enter_valid_choice()
        librarian_option_choice()


#4. librarian_login 
def librarian_login():
    try:
        result = library_view.librarian_login()
        account = library_model.librarian_login(result[0], result[1])
        if account != None:
            library_view.librarian_login_successful(account[1])

            global is_librarian
            is_librarian = True
            global id
            id = account[0]
            notified_librarian_user_rental_day()
            librarian_option_choice()
            return #*********

        else:
            library_view.librarian_login_failed()
            librarian_login()
    except:
        library_view.unknown_error()


#4B. Notified librarian for 14 days to the user his issued book detail after librarian login
def notified_librarian_user_rental_day():
    try:
        u_detail = library_model.notify_librarian_user_day()
        library_view.display_notification_for_librarian()
        
        for row in u_detail:
            newRow = (row[0],row[1],row[2],row[3].strftime('%d/%m/%Y'))
            library_view.display_librarian_user_books_detail(newRow)
    except:
        library_view.unknown_error()


#4-41. add books by librarian
def add_books():
    try:
        result = library_view.add_books()
        librarian_id = library_model.add_books(result[0], result[1], result[2])

        if librarian_id != None:
            library_view.add_books_successfully()
            librarian_option_choice()
            return #********
        else:
            library_view.add_book_failed()
    except:
        library_view.unknown_error()

    
#4-42. Delete book from library by librarian 
def delete_book():
    try:
        result = library_view.delete_book()
        book_detail = library_model.del_book_available(result)
        if book_detail == None:
            library_view.book_not_available()
            # librarian_option_choice()
            delete_book()
        else:
            pass

        id = library_model.delete_book(result)
        
        if id != None:
            library_view.delete_book_successfully()
            librarian_option_choice()
            return #******
        else:
            library_view.delete_book_failed()

    except ValueError:
        library_view.librarian_delete_book_error()
        delete_book()
        # librarian_option_choice()
    except:
        library_view.unknown_error()


#4-43. Update books details by librarian
def update_book_details():
    try:
        result = library_view.update_book_details()
        book_detail = library_model.del_book_available(result[3])
        if book_detail == None:
            library_view.book_not_available()
            # librarian_option_choice()
            update_book_details()
        else:
            pass

        id = library_model.update_book_details(result[0],result[1],result[2],result[3])

        if id != None:
            library_view.update_book_successfully()
            librarian_option_choice()
            return #maindatory
        else:
            library_view.update_book_failed()
    except ValueError:
        library_view.update_book_error()
        update_book_details()
        # librarian_option_choice()
    except:
        library_view.unknown_error()


#4-44. Delete Student(user) detail by librarian
def delete_user():
    try:
        result = library_view.delete_user()
        account = library_model.delete_user_error(result)

        if account == None:
            library_view.del_user_error()
            delete_user()
        else:
            pass

        id = library_model.delete_user(result)

        if id != None:
            library_view.delete_user_successfully()
            librarian_option_choice()
            return # maindatory
        else:
            library_view.delete_user_failed()
    except ValueError:
        library_view.delete_user_error()
        delete_user()
    except:
        library_view.unknown_error()


#5. Display all books 
def display_all_books():
    try:
        rows = library_model.display_all_books()
        
        for row in rows:
            library_view.display_all_books(row)
        startLMS()

    except:
        library_view.unknown_error()


# 6. Display Available Books
def display_available_books():
    try:
        rows = library_model.display_available_books()
        
        for row in rows:
            library_view.display_available_books(row)
        startLMS()

    except:
        library_view.unknown_error()



# Choosen operators        

def startLMS():
    inp = library_view.start()
    if(inp == '0'):
        library_view.exit()
        return
    elif(inp == '1'):
        user_registration()
    elif(inp == '2'):
        librarian_registration()
    elif(inp == '3'):
        user_login()
    elif(inp == '4'):
        librarian_login()  
    elif(inp == '5'):
        display_all_books()
    elif(inp == '6'):
        display_available_books()
    else:
        library_view.enter_valid_choice()
        startLMS()
        
startLMS()





