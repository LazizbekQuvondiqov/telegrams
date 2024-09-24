faylnomi = 'new_file.txt'
son = input('sonni kriting: ')
with open(faylnomi, 'r') as fayl:
    a = fayl.read()

k = int(input('k = '))
if k < len(a):
    a = a.replace(a[0], son, 1)
    with open(faylnomi, 'w') as fayl:
        fayl.write(a)
else:
    print('\'k\' berilgan so\'z uzunligidan katta!!!')
