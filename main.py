from random import choice

#all_symbols = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@!#$%*&'
#lenght  = int(input('введите количество символов:'))
#password = ''

#for i in range(lenght):
 #   password += choice(all_symbols)
#print(password)

number = '1234567890'
sogl = 'QWRTPSDFGHJKLZXCVBNMqwrtpsdfghjlkzxcvbnm'
glas = 'EYUIOAeyuoai'
symbols = '!@#$%^&*-=_+'
password = ''
for i in range(5):
    password += choice(sogl) + choice(glas)
for i in range(3):
    password += choice(number)
for i in range(2):
    password += choice(symbols)  
print(password)
