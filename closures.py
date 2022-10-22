def make_repeater_of(n:int):

    def repeater(string:str):
        assert type(string) ==  str, "Solo puedes usar cadenas de texto"
        return string*n
    
    return repeater




def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola "))


if __name__ == "__main__":
    run()