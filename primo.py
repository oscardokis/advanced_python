def is_primo(number:int) -> bool:
    contador = 0
    for i in range(1, number+1):
        if i == 1 or i == number:
            continue
        elif number % i == 0:
            contador=+1
            break
    return contador == 0
    
def run():
    number = int(input("Write a number to know if is a primo: "))
    
    print(is_primo(number))

if __name__ == "__main__":
    run()
        
