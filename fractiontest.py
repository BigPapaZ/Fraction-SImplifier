#######################
# fractiontest.py
# Zaigham
# Tests whether the program fraction.py is working
#######################


import fraction

def main():

    frac=fraction.Fraction(5,4)
    print(frac.getNum(), frac.getDen(),frac)

    frac.setNum(8)
    print(frac.getNum(), frac.getDen(),frac)

    frac.setDen(10)
    print(frac.getNum(), frac.getDen(),frac)

    frac.setDen(0)
    print(frac.getNum(), frac.getDen(),frac)

    frac.setNum(10)
    print(frac.getNum(), frac.getDen(),frac)

    frac=fraction.Fraction(5,-4)
    print(frac.getNum(), frac.getDen())
    frac.getReciprocal()
    print(frac.getNum(), frac.getDen(),frac)


    frac=fraction.Fraction(-5,4)
    print(frac.getNum(), frac.getDen(),frac)
    frac.getReciprocal()
    print(frac.getNum(), frac.getDen(),frac)


    frac1=fraction.Fraction(-5,-4)
    print(frac1.getNum(), frac1.getDen(),frac1)
    frac.getReciprocal()
    print(frac1.getNum(), frac1.getDen(), frac1)

    frac2=fraction.Fraction(7, 6)
    frac3 = fraction.Fraction(6, 7)
    print(frac2/frac3,frac2-frac3,frac2+frac3,frac2*frac3)

    frac6=fraction.Fraction(61,70)
    frac7 = fraction.Fraction(10, 0)
    print(frac6/frac7, "Division")
    print(frac6*frac7, "Multiplication")
    print(frac6-frac7, "Subtraction")
    print(frac6+frac7, "Addition")

    print("61/70>6/7?",frac6>frac3)
    print("61/70<6/7?",frac6<frac3)
    print("61/70=6/7?", frac6 == frac3)
    print("61/70<=6/7?", frac6 <= frac3)
    print("61/70>=6/7?", frac6 >= frac3)
    print("61/70 not = 6/7?", frac6 != frac3)


    print(frac2, float(frac2), int(frac2))


main()
