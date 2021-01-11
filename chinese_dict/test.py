with open('test.txt') as f:
    r = f.readlines()
for l in r:
    v= l.strip().split(' ')
    word = []
    for x in v:
        word.append(x[0])
    print(''.join(word))