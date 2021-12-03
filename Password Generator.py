import random

nums = '123456789'
alphas = 'qwertyuiopasdfghjklzxcvbnm'
ls = list(nums+alphas+alphas.upper())
random.shuffle(ls)

# The number of characters in the password, corresponds range()
psw = ''.join([random.choice(ls) for x in range(12)])

print(psw)