

class student:
    def __init__(self, total):
        self.total = total

    def average(self):
        return self.total/ 5.0

        @property
        def total(self):
            return self._total

        @total.setter
        def total(self, t):
            if t<0 or t>500:
                print("Invalid Total And Can't change")    
            else:
                self._total = t    

o = student( 410 )
print("Total   : " , o.total)
print("Average : " , o.average())
o.total = 500
print("Total   : " , o.total)
print("Average : " , o.average())
