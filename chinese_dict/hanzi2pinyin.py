from pypinyin import lazy_pinyin,Style;import sys

with open('dict.txt.big') as f:
    a = f.readlines()
with open('res',"a")as f:
    for w in a:
        w = w.strip()
        f.write(''.join(lazy_pinyin(w))+"\n")
        f.write('-'.join(lazy_pinyin(w))+"\n")
        f.write('_'.join(lazy_pinyin(w))+"\n")
        f.write(' '.join(lazy_pinyin(w))+"\n")
        f.write(''.join(lazy_pinyin(w,style=Style.FIRST_LETTER))+"\n")
        # style=Style.FIRST_LETTER

# print(''.join(lazy_pinyin(sys.stdin.read())),end='')