"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

"""
class AAA:
    def __init__(self):
        self.rom_dict = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

    def uz_rom(self, num):
        result = ''
        for value in sorted(self.rom_dict.keys(), reverse=True):
            while num >= value:
                result += self.rom_dict[value]
                num -= value
        return result
    
# izveidojam objketu
kk=AAA()   
skaitlis=2023
# izsaucam klases iekšējo funkciju (metode)
rom_sks=kk.uz_rom(skaitlis)
print(f"{skaitlis} romiešu ciparos ir {rom_sks}.")