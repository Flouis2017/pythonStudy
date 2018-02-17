# __author : "Flouis"
# date : 2018/2/17
import sys
import time

login_status = [False]

tmpList = [False,0]

def toggleStatus(login_status):
    if login_status == True:
        login_status = False
    else:
        login_status = True
    return login_status

# Login decorator:
def login(f):
    def inner():
        if tmpList[0] == True:
            f()
        else:
            while True:
                if tmpList[1] == 3:
                    print('Error occurred triple times,please try again later!')
                    time.sleep(5)
                    tmpList[1] = 0
                    continue
                username = input('UserName:')
                password = input('Password:')
                if username == 'admin' and password == 'admin123':
                    f()
                    tmpList[0] = True
                    break
                else:
                    print('Username or password occurs error,please try again!')
                    tmpList[1] += 1
    return inner

@login
def home():
    print('Welcome to Home Page!')

@login
def clothes():
    print('Welcome to Clothes Page!')
    
@login
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

start()