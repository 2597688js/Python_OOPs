class Dad:
    basketball = 6

class Son(Dad):
    dance = 1
    basketball = 9
    def isdance(self):
        return f"Yes I can dance {self.dance} no of times"

class Grandson(Son):
    dance = 6
    def isdance(self):   # ami Son class r isdance function tuk override korisu
        return  f"Hell Yeah!! Yes I can incredibly dance {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())   # e harry r class ie., Grandson t bisaribo isdance() k, iyat nathakile Son t jabo.
print(harry.basketball)