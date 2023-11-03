"""
Uzrakstiet Python programmu, lai diviem sarakstiem noteikti atšķirību.
Izmantojiet funkciju map().
"""


saraksts1 = [1, 2, 3, 4, 5]
saraksts2 = [3, 1, 4, 2, 6]

def st(s1, s2):
    return s1 - s2

rez = list(map(st, saraksts1, saraksts2))

print(rez)  # Izvadīs [-2, 1, -1, 2, -1]
