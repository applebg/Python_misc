import random

symbollist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
              'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
              '1','2','3','4','5','6','7','8','9','0']
symbollist_2=['~','!','@','#','$','%','^','&','*','*','(',')','_','+','-','/']

length = 10
password = ""
for x in range(0, length):
    password = password + random.choice(symbollist)


print(password)