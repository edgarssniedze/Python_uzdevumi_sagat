"""
Uzdevumā izmantot funkciju map(), kura  komandu izpilda 
katram saraksta(virknes) loceklim.
"""

def juris(skaitlis):
    return skaitlis ** 2
saraksts = [1, 2, 3, 4, 5]
rezultats = map(juris, saraksts)
rezultats = list(rezultats)
print(rezultats)