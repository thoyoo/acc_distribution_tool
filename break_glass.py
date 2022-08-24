from xml.dom.minidom import Identified
import csv
import secrets
import string

def pw_generator(length):
    alphabet = string.ascii_letters + string.digits + '-_#$#+'
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (sum(c.islower() for c in password) >=3
                and sum(c.isupper() for c in password) >=3
                and sum(c.isdigit() for c in password) >=3):
            return password

class account(object):
    def __init__(self,accountname, password):
        self.accountname = accountname
        self.password = password
    
    def __str__(self):
        return  '\n'.join((str(item) + ' = ' + str(self.__dict__[item]) for item in sorted(self.__dict__)))

class acc_class(account):
    pass

class users(object):
    def __init__(self,username, permissions):
        self.username = username
        self.permissions = permissions
    
    def __str__(self):
        return  '\n'.join((str(item) + ' = ' + str(self.__dict__[item]) for item in (self.__dict__)))

class user_class(users):
    pass

acc_list = []
user_list = []

with open('users.csv', newline='') as user_csv:
    read_user = csv.reader(user_csv)
    next(read_user)  # Skip the header
    for username, permissions in read_user:
        user_obj=user_class(username,permissions)
        with open('accounts.csv', newline='') as acc_csv:
            read_acc = csv.reader(acc_csv)
            next(read_acc)  # Skip the header
            print(user_obj.username)
            for accountname, password in read_acc:
                acc_password=pw_generator(10)
                acc_obj=acc_class(accountname,acc_password)
                if acc_obj.accountname in user_obj.permissions:
                    #print(acc_obj.accountname,acc_obj.password)
                    with open(user_obj.username +'.txt', 'w') as f:
                        exp=(acc_obj.accountname)+' '+(acc_obj.password)
                        for line in exp:
                            f.writelines((exp))
                            f.write('\n')
                        
    
        #print(accountname, acc_password)
        #if accountname = username.


