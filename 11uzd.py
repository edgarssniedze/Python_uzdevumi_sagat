"""
Uzrakstiet Python programmu, lai trīskāršotu visus dotā veselo skaitļu saraksta skaitļus.
Izmantojiet Python map() funkciju.
"""

def je(skaitlis):
    return skaitlis * 3
saraksts = [1, 2, 3, 4, 5]
rez = list(map(je, saraksts))
print(rez)