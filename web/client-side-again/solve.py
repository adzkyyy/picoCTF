flag = ['/'] * 32
s = 4

p = open('obfus.txt').read().split('\n')

for l in p:
    l = l.strip()
    if l == "":
        continue
    l = l.replace('if (checkpass["substring"](','flag [').replace(',',':').replace(') == ','] = ').replace(') {','')
    exec l

print ''.join(flag)
