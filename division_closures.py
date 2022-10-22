
def make_division_by(d):
    def numerator(n):
        return n/d
    return numerator



def run():
    make_division_by_3 = make_division_by(3)
    print(make_division_by_3(18))
    make_division_by_5 = make_division_by(5)
    print(make_division_by_5(100))
    make_division_by_18 = make_division_by(18)
    print(make_division_by_18(54))


if __name__ == "__main__":
    run()
