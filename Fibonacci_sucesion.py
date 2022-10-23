import time
class FiboIter():
    def __init__(self, max=None):
        self.max = max
    def __iter__(self):
        self.n1 = 0
        self.n2 = 0
        return self
    def __next__(self):

        if self.n2 == 0:
            self.n2 += 1
            return self.n2
        elif self.n2 == 1 and self.n1==0:
            self.n1 += 1
            return self.n2
        else:
            self.fibo = self.n1 + self.n2
            self.n1 = self.n2
            self.n2 = self.fibo
            if not self.max or self.fibo <= int(self.max):
                return self.fibo
            else:
                raise StopIteration


if __name__ =="__main__":
    
    fibo_max = input("Escriba el numero maximo en la secuencia fibonacci: ")
    fibonacci = FiboIter(fibo_max)
    for element in fibonacci:
        print(element)
        time.sleep(0.1)


        

        
