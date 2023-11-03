"""
Doti divi saraksti.
Izmantojot funkciju map(), izdrukāt abu sarakstu vienādo( sakrīt elementi un to index) elementu summu.
"""
saraksts1 = [1, 2, 3, 4, 5]
saraksts2 = [1, 2, 5, 4, 7]
 
# Funkcija, kas pārbauda, vai elementi un indeksi sakrīt un sasummē tos
def saskaitit_vienados_elementus(skaitlis1, skaitlis2, indekss):
    if skaitlis1 == skaitlis2 and saraksts1.index(skaitlis1) == indekss:
        return skaitlis1 + skaitlis2
    else:
        return 0  # 0, ja elementi nesakrīt
 
# Izmantot map() funkciju, lai iegūtu vienādo elementu summas
sasummetie_elementi = list(map(saskaitit_vienados_elementus, saraksts1, saraksts2, range(len(saraksts1))))
 
# Saskaitīt summu
summa = sum(sasummetie_elementi)
 
print("Vienādo elementu summa:", summa)