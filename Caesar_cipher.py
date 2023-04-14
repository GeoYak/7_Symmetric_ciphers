def encrypt(k, m):
    return ''.join(map(chr, [(x + k) % 65536 for x in map(ord, m)]))


def decrypt(k, c):
    return ''.join(map(chr, [(x - k) % 65536 for x in map(ord, c)]))


def decrypt_without_key(c):
    alph = {}
    for i in c:
        if i in alph:
            alph[i] += 1
        else:
            alph[i] = 1
    max_al = 0
    max_k = -1
    for i in alph:
        if alph[i] > max_al:
            max_al = alph[i]
            max_k = i
    k = ord(max_k) - ord(' ')
    return decrypt(k, c)


msg = input('Введите текст: ')
k = int(input('Введите ключ(число): '))
sh_msg = encrypt(k, msg)
print(sh_msg)
rez_msg = decrypt(k, sh_msg)
print(rez_msg)
rez = decrypt_without_key(sh_msg)
print('Расшифровка без ключа: ', rez)
