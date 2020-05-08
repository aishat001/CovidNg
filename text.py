file = open('text.txt', 'r')

f1 = file.read()

print(f1.strip('  '))

tab = list(f1)
print(tab)