import mysql.connector

class LibraryManagement:
    mydb=mysql.connector.connect(host="localhost",user='root',password='')
    a=mydb.cursor()
    a.execute('Create database if not exists LibraryManagementSystem')

    mydb=mysql.connector.connect(host="localhost",user='root',password='',database='LibraryManagementSystem')
    
    c=mydb.cursor()

    #Creating a table
    c.execute('Create table if not exists Library(Id varchar(50),Books varchar(50),Status varchar(50))')

    def view(self):
        LibraryManagement().c.execute('select * from Library')
        records=LibraryManagement.c.fetchall()
        return records

    def lend(self):
        book=input('Which book you want to lend? ')
        LibraryManagement().c.execute(f"select * from Library where Books='{book}' AND Status='available'")
        records=LibraryManagement().c.fetchall()
        if records!=[]:
            id=records[0][0]
            name=input('What is your name ')
            sql="update Library set Status=%s where Id=%s"
            val=(name,id)
            LibraryManagement().c.execute(sql,val)
            LibraryManagement().mydb.commit()
            return'You have lended the book succesfully'
        else:
            return 'The book you want to lend is currently unavailable'

    def return_(self):
        book=input('Which book you want to return ')
        LibraryManagement().c.execute(f"select * from Library where Books='{book}'")
        records=LibraryManagement().c.fetchall()
        if book not in str(records):
            return 'The book you want to return is not register with our library' 
        else:
            id=input('Enter the book id:')
            if id not in str(records):
                return 'The book you want to return is not register with our library'
            else:
                status='available'
                sql="update Library set Status=%s where Id=%s"
                val=(status,id)
                LibraryManagement().c.execute(sql,val)
                LibraryManagement().mydb.commit()
                return 'The book returned successfully'

    def add_(self):
        book=input('Enter the book name ')
        id=input('Enter the Book id:- ')
        status='available'
        LibraryManagement().c.execute("select * from Library")
        records=LibraryManagement().c.fetchall()
        if id in str(records):
            return "The id you want to give to this book is already exists. Plese give another id."
        else:
            sql='insert into Library values (%s,%s,%s)'
            val=(id,book,status)
            LibraryManagement().c.execute(sql,val)
            LibraryManagement().mydb.commit()
            return 'The book added successfully in library'

    def del_(self):
        book=input('Which book you want to delete? ')
        LibraryManagement().c.execute(f"select * from Library where Books='{book}'")
        records=LibraryManagement().c.fetchall()
        if book not in str(records):
            return 'The book you want to delete is not register with our library'
        else:
            id=input('Enter the book id:')
            if id not in str(records):
                return 'The book you want to delete is not register with our library'
            else:
                LibraryManagement().c.execute(f"delete from Library where Id='{id}'")
                LibraryManagement().mydb.commit()
                return 'The book deleted successfully from library'

    def exit(self):
        return 'Thank you for using our Library Management System 🙂'


Lib=LibraryManagement()
while True:
    print('\nWelcome to our library management system \nEnter the choice \n1.View Books \n2.Lend a book \n3.Return a book \n4.Add a book \n5.Delete a Book \n6.Exit')
    choice=input('Enter the choice:- ')
    if choice=='1':
        print(Lib.view())
    elif choice=='2':
        print(Lib.lend())
    elif choice=='3':
        print(Lib.return_())
    elif choice=='4':
        print(Lib.add_())
    elif choice=='5':
        print(Lib.del_())
    elif choice=='6':
        print(Lib.exit())
        break
    else:
        print('Please enter the correct option')
