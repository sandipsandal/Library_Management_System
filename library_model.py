import mysql.connector
from mysql.connector import Error,MySQLConnection
# from mysql.connector import 
# from configparser import ConfigParser
from datetime import datetime
from datetime import date, timedelta
from conpars import read_db_config
 
#1. user registration
def create_user(name, user_contact,password,user_name):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    
    sql = "INSERT INTO library_user(u_name,u_contact,password,user_name) VALUES (%s, %s, %s, %s)"   
    val = (name,user_contact,password,user_name)


    cursor.execute(sql, val)
    connection.commit()
    cursor.close()
    return cursor.lastrowid

#check user registration
def create_user_check(user_name):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    
    sql = 'SELECT * FROM library_user WHERE user_name = %s'
    val = (user_name,)

    cursor.execute(sql, val)
    account = cursor.fetchone()
    cursor.close()
    return account

#3. user login
def user_login(user_name,password):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    sql = 'SELECT u_id, u_name FROM library_user WHERE user_name = %s AND password = %s'
    val = (user_name,password)
    
    cursor.execute(sql, val)
    account = cursor.fetchone()
    cursor.close()
    return account


#3A. user option choice for action perform
#3B. Notified user for 14 days to the user his issued book detail
def notify_day(user_id):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor(buffered=True)
    dt = date.today() - timedelta(14)
    sql = "SELECT b_id,b_name,b_author,b_rented_date FROM library_books WHERE b_rented_date < %s and b_rented_user =%s"
    val = (dt,user_id)

    cursor.execute(sql,val)
    book_details = cursor.fetchall()
    cursor.close()
    return book_details

#3-31. update user detail
def update_user_details(update_user_name, update_user_contact,update_user_password, user_id):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    sql = "UPDATE library_user SET u_name = %s, u_contact = %s, password = %s WHERE u_id = %s"
    val = (update_user_name, update_user_contact, update_user_password,user_id)

    cursor.execute(sql, val)
    
    connection.commit()
    id = cursor.rowcount
    cursor.close()
    # return cursor.lastrowid
    return id

#3-32. user issue a book from library
def user_issue_book(user_id,book_id):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    today_date = date.today()
    sql = "UPDATE library_books SET b_rented_user = %s, b_rented_date = %s  WHERE (b_id = %s) AND (b_rented_user IS NULL)"
    val = (user_id,today_date,book_id)
    
    cursor.execute(sql, val)
    
    connection.commit()
    id = cursor.rowcount
    cursor.close()
    return id

#3-33. Get and Update user_fee detail
def get_day(book_id):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    sql = "select b_rented_date, b_rented_user from library_books where b_id = %s"
    val = (book_id,)
    
    cursor.execute(sql,val)
    rent_day_user = cursor.fetchone()
    # cursor.fetchone()
    # connection.commit()
    cursor.close()
    return rent_day_user

#3-33-B  update_user_fee
def update_user_fee(fine,user_id): # fine = total_fee_value//user_id = details[1] = b_rented_user
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    sql = "UPDATE library_user SET u_fee = %s WHERE u_id = %s"
    val = (fine,user_id)
    cursor.execute(sql,val)
    cursor.rowcount
    connection.commit()
    cursor.close()
    return cursor.lastrowid

#3-34. return book & update user fee (Return issued book by login user& update user fee of logged in user)
def get_user_id(book_id):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    # sql = "select b_rented_date, b_rented_user from books where b_id = %s"
    sql = "select b_rented_user from library_books where b_id = %s"
    val = (book_id,)
    
    cursor.execute(sql,val)
    user_id = cursor.fetchone()
    cursor.close()
    return user_id

#3-34 B
def paid_user_fee(user_id):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    sql = "UPDATE library_user SET u_fee = NULL WHERE u_id = %s"
    val = (user_id,)

    cursor.execute(sql,val)
    cursor.rowcount
    connection.commit()
    cursor.close()
    return cursor.lastrowid

#3-34-C
def return_book(book_id):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    sql = "UPDATE library_books SET b_rented_date = NULL, b_rented_user = NULL WHERE b_id = %s"
    val = (book_id,)

    cursor.execute(sql,val)
    cursor.rowcount
    connection.commit()
    cursor.close()
    return cursor.lastrowid

#2. librarian registration(for add new librarian data)
def create_librarian(librarian_name,librarian_contact,password,user_name):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    sql = "INSERT INTO college_librarian(l_name,l_contact,password,user_name) VALUES (%s, %s, %s, %s)" 
    val = (librarian_name,librarian_contact,password,user_name)
    
    
    cursor.execute(sql, val)
    cursor.rowcount
    connection.commit()
    cursor.close()
    return cursor.lastrowid

# check librarian registration
def create_librarian_check(user_name):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    
    sql = 'SELECT * FROM college_librarian WHERE user_name = %s'
    val = (user_name,)

    cursor.execute(sql, val)
    account = cursor.fetchone()
    cursor.close()
    return account

#4.librarian_login
def librarian_login(user_name,password):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    sql = 'SELECT l_id,l_name FROM college_librarian WHERE user_name = %s AND password = %s'
    val = (user_name,password)
    
    cursor.execute(sql, val)
    account = cursor.fetchone()
    cursor.close()
    return account

#4B. Notified librarian for 14 days to the user his issued book detail after librarian login
def notify_librarian_user_day():
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor(buffered=True)
    dt = date.today() - timedelta(14)
    sql = "SELECT b_rented_user,b_name,b_author,b_rented_date FROM library_books WHERE b_rented_date < %s "
    val = (dt,)

    cursor.execute(sql,val)
    book_details = cursor.fetchall()
    cursor.close()
    return book_details

#4-41. add books
def add_books(book_name, book_author, book_publication):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    sql = "INSERT INTO library_books(b_name,b_author,b_publication) VALUES (%s, %s, %s)"   
    val = (book_name, book_author, book_publication)

    
    cursor.execute(sql, val)
    # cursor.rowcount
    connection.commit()
    cursor.close()
    return cursor.lastrowid

#4-42. delete book
def delete_book(book_id):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    sql = "DELETE FROM library_books WHERE b_id = %s"
    val = (book_id,)

    cursor.execute(sql, val)
    # cursor.rowcount
    connection.commit()
    cursor.close()
    return cursor.lastrowid

def del_book_available(book_id):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    sql = "SELECT * FROM library_books WHERE b_id = %s"
    val = (book_id,)

    cursor.execute(sql, val)
    avl_book = cursor.fetchone()
    cursor.close()
    return avl_book


#4-43. update book details by Librarian
def update_book_details(update_book_name, update_book_author, update_book_publication, book_id):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    sql = "UPDATE library_books SET b_name = %s, b_author = %s, b_publication = %s WHERE b_id = %s"
    val = (update_book_name, update_book_author, update_book_publication, book_id)

    cursor.execute(sql, val)
    cursor.rowcount
    connection.commit()
    cursor.close()
    return cursor.lastrowid

#4-44. Delete Student(user) detail by librarianr
def delete_user(user_id):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    sql = "DELETE FROM library_user WHERE u_id = %s"
    val = (user_id,)

    cursor.execute(sql, val)
    cursor.rowcount
    connection.commit()
    id = cursor.lastrowid
    cursor.close()
    return id

def delete_user_error(user_id):
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()

    sql = "SELECT u_name FROM library_user WHERE u_id = %s"
    val = (user_id,)

    cursor.execute(sql, val)
    account = cursor.fetchone()
    cursor.close()
    return account


# 5. Display all books in library
def display_all_books():
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    cursor.execute("SELECT b_id, b_name, b_author, b_publication FROM library_books")
    rows = cursor.fetchall()
    cursor.close()
    return rows


# 6. Diplay available books
def display_available_books():
    # connection = mysql.connector.connect(host='127.0.0.1',database='library_management_sys_db',user='root',password='Password@123')
    # cursor = connection.cursor()
    dbconfig = read_db_config()
    connection =MySQLConnection(**dbconfig)
    cursor = connection.cursor()
    cursor.execute('SELECT  b_id,b_name, b_author, b_publication FROM library_books WHERE b_rented_user IS  NULL')

    rows = cursor.fetchall()
    cursor.close()
    return rows 



    



