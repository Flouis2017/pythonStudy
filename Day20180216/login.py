# __author : "Flouis"
# date : 2018/2/16
import time
import sys

def welcome(f):
    def inner():
        print('Welcome!')
        f()
    return inner

@welcome    
def foo():
    print('Flouis')
#foo()


def home():
    print('Welcome to Home Page!')
    
def clothes():
    print('Welcome to Clothes Page!')

def book():
    print('Welcome to Book Page!')
    
ls = False

def input_check():
    usn = input('Username:')
    pwd = input('Password:')
    if usn == 'admin' and pwd =='admin123':
        return True

def start(ls2):
    login_status = ls2
    cnt = 3
    while True:
        print('1.Home\n2.Clothes\n3.Book')
        choice_num = input('Please Choose one item above:')
        if choice_num == '-1':
            print('Bye!')
            sys.exit()
        else:
            if login_status == False:
                print('Please login at first!')
                login_status = input_check()
                if login_status == True:
                    continue
                else:
                    while cnt > 0:
                        if cnt == 1:
                            print('Frequently input,Please try again later!')
                            time.sleep(5)
#                            print(ls)
                            start(ls)
                        print('The Wrong username or password,please try again.')
                        login_status = input_check()
                        cnt -= 1
                        if login_status == True:
                            break
                        else:
                            continue
            elif choice_num == '1':
                home()
            elif choice_num == '2':
                clothes()
            elif choice_num == '3':
                book()
            else:
                print('No relative result!')
    
#start(ls)



def start2():
    cnt = 3
    while True:
        print('1.Home\n2.Clothes\n3.Book')
        choice_num = input('Please Choose one item above:')
        if choice_num == '-1':
            print('Bye!')
            break
        else:
            if ls == False: # 这里为什么访问不到全局变量ls ?????
                print('Please login at first!')
                ls = input_check()
                if ls == True:
                    continue
                else:
                    while cnt > 0:
                        if cnt == 1:
                            print('Frequently input,Please try again later!')
                            time.sleep(5)
                            print(ls)
                            start(ls)
                        print('The Wrong username or password,please try again.')
                        ls = input_check()
                        cnt -= 1
                        if ls == True:
                            break
                        else:
                            continue
            elif choice_num == '1':
                home()
            elif choice_num == '2':
                clothes()
            elif choice_num == '3':
                book()
            else:
                print('No relative result!')

#start2(ls)

