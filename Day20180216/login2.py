# __author : "Flouis"
# date : 2018/2/17
import sys

# Login decorator:

#global login_status
login_status = False

def changeLoginStatus():
    print(login_status)
    login_status = 2

changeLoginStatus()
print(login_status)

def toggleStatus(login_status):
    if login_status == True:
        login_status = False
    else:
        login_status = True
    return login_status

#login_status = toggleStatus(login_status)
#print(login_status)

def login(f):
#    print(login_status)
    def inner():
        if login_status == True:
            f()
        else:
            username = input('UserName:')
            password = input('Password:')
            if username == 'admin' and password == 'admin123':
                f()
#                login_status = True
                toggleStatus()
            else:
                print('Username or password occurs error,please try again!')
    return inner

@login
def home():
    print('Welcome to Home Page!')
    
#@login
def clothes():
    print('Welcome to Clothes Page!')
    
#@login
def book():
    print('Welcome to Book Page!')


def start():
    while True:
        print('1.Home\n2.Clothes\n3.Book')
        choice_num = input('Please choose one item number:')  
        if choice_num == '-1':
            print('Bye!')
            sys.exit()
        elif choice_num == '1':
            home()
        elif choice_num == '2':
            clothes()
        elif choice_num == '3':
            book()
        else:
            print('No relative result!')

#start()