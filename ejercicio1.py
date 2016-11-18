class romano():	
    global result
    keys = []
    
    def Roman_Number(self,number):
        def reverse_numeric(x, y):
            return y - x
        Roman_Table = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
               100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 
               10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        self.result = ""
        keys = Roman_Table.keys()
        keys = sorted(keys, cmp=reverse_numeric)
        while number > 0:
            for i in keys:
                if number >= i:
                    self.result += str(Roman_Table.get(i, 0))
                    number -= i
                    break
        return self.result
    def mostrar(self):
        print self.result
miromano = romano()
miromano.Roman_Number(1000)
miromano.mostrar()


