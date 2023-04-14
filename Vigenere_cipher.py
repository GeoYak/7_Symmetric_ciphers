def encrypt(k, m):
    list_key, list_str = [i for i in (k, m)]
    ls = []
    for a in range(len(list_str)):
        for i, j in [(list_str[a], list_key[a])]:
            ls.append(ord(i) ^ ord(j))
    rez = ''.join(map(chr, ls))
    return rez


def decrypt(k, c):
    list_key, list_str = [i for i in (k, c)]
    ls = []
    for a in range(len(list_str)):
        for i, j in [(list_str[a], list_key[a])]:
            ls.append(ord(i) ^ ord(j))
    rez = ''.join(map(chr, ls))
    return rez


m = input('Введите текст: ')
k = input('Введите ключ(строка из чисел): ')
while len(k) < len(m):
    k += k
c = encrypt(k, m)
print('Закодированно: ', c)
rez = decrypt(k, c)
print('Раскодированно: ', rez)
