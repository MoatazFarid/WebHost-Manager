import functions , HostManagerdb

# functions.addnewUser()
def login():
    username = raw_input("user : ")
    password = raw_input("password : ")
    res = functions.login_Auth(username,password)
    if res == 1:
        print "Welcome "+username
        menu()
    else:
        print "Wrong Credintials"
        login()


def menu():
    print '''\t \t Welcome to WebHost Manager \t \t \n
    1- Add User\n
    2- Add Host\n
    3- Add Domain\n
    4- Search for User \n
    5- Search for Domain \n
    6- Search for a Host \n
    7- view All Users \n
    8- view All Domains \n
    9- exit
    '''
    option = raw_input("selection = ")
    handler(int(option))

def handler(option):
    if option == 1:
        functions.addnewUser()
        menu()
    elif option == 2 :
        functions.addnewHost()
        menu()
    elif option == 3 :
        functions.addnewDomain()
        menu()
    elif option == 4 :
        functions.searchUser()
        menu()
    elif option == 5 :
        functions.searchDomain()
        menu()
    elif option == 6 :
        functions.searchHost()
        menu()
    elif option == 7 :
        functions.PrintAllUsers()
        menu()
    elif option == 8 :
        functions.PrintDomainsAndUserId()
        menu()
    elif option == 9 :
        return 0
    else:
        print "Wrong Choise"
        menu()

login()
# HostManagerdb.init()
