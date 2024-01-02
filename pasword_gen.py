import random
import string
def create_password():
    alpha = list(string.ascii_letters)
    number=['1','2','3','4','5','6','7','8','9','0'] 
    symbols=['!','@','#','%','^','&','*',]
    no_letters=4
    no_symbols=2
    no_numbers=4
    password_list=[]
    for char in range(1,no_letters+1):
        password_list.append(random.choice(alpha))
    for char in range(1,no_symbols+1):
        password_list.append(random.choice(number))
    for char in range(1,no_numbers +1):
        password_list.append(random.choice(symbols))
    random.shuffle(password_list)

    password = "".join(password_list)
    return password

