import time

def fibo_gen(x):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter +=1
            yield n1
        elif counter ==1:
            counter +=1
            yield n2
        else:
            aux =n1+n2
            n1, n2 = n2, aux
            if aux <= int(x):
                yield aux
            else:
                break




if __name__ == "__main__":
    x = input("Escriba hasta cual numero quieres Fibonacci: ")
    fibo = fibo_gen(x)
    for element in fibo:
        print(element)
        time.sleep(0.1)