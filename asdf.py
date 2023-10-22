import math

text = input('Введите текст: ')

def enc(text):
    if math.sqrt(len(text)) <= 5:
        n = 5
    else: 
        n = math.ceil(math.sqrt(len(text)))

    a = ['_'] * n
    for i in range(n):
        a[i] = ['_'] * n

    text = text.replace(' ', '_')
    t = 0

    for i in range(0, n):
        for j in range(n * (i % 2) - i % 2,  n * ((i + 1) % 2)  - i % 2, 1 - (i % 2) * 2):
            if t < len(text):
                a[j][i] = text[t]
                t += 1
    
    enctext = ''

    for i in range(n):
        for j in range(n):
            enctext += a[i][j]
    return enctext

def dec(text):
    if math.sqrt(len(text)) <= 5:
        n = 5
    else: 
        n = math.ceil(math.sqrt(len(text)))

    a = ['_'] * n
    for i in range(n):
        a[i] = ['_'] * n

    t = 0

    for i in range(n):
        for j in range(n):
            if t < len(text):
                a[i][j] = text[t]
                t += 1
    
    dectext = ''

    for i in range(0, n):
        for j in range(n * (i % 2) - i % 2,  n * ((i + 1) % 2)  - i % 2, 1 - (i % 2) * 2):
            dectext += a[j][i]
    dectext = dectext.replace('_', ' ').strip()
    return dectext
    
    

print("Шифрованный текст: " + enc(text))
print("Дешифрованный текст: " + dec(enc(text)))