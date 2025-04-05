from random import choice


number = '1234567890'
sogl = 'QWRTPSDFGHJKLZXCVBNMqwrtpsdfghjlkzxcvbnm'
glas = 'EYUIOAeyuoai'
symbols = '!@#$%^&*-=_+'
slog = int(input('введи количество слогов:'))
numb = int(input('введи количество цифр:'))
symb = int(input('введи количество символов:'))
password = ''
for i in range(slog):
    password += choice(sogl) + choice(glas)
for i in range(numb):
    password += choice(number)
for i in range(symb):
    password += choice(symbols)  
print(password)
