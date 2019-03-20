# Fraction-SImplifier
python3
fraction.py
This program consists of only one class named Fraction and no subclasses. This Fraction class
consists of a constructor and the following methods: getNum(), getDen(), setNum(), setDen(),
getReciprocal(), __simplify(), __str__(), __float__(), __int__(), __add__(), __sub__(), __mul__(),
__truediv__(), __eq__(), __ne__(), __lt__(), __le__(), __gt__(), and __ge__(). The whole purpose of this
class is to help us define a fraction object which we can use to perform mathematical operations and
comparison with other fractions of the same type.


At first I want to explain the __simplify() method. It makes the numerator a 0 if the
denominator is 0. If the numerator is 0 and the denominator is not, then it sets the denominator to 1.
Otherwise, it cancels out all the common factors between the 2 fractions. If both the numerator and the
denominator are negative, it cancels those negatives as well. If only the denominator is negative then it
makes it positive and assigns the numerator a negative sign.
getNum(), getDen(), setNum(), and setDen() are self-explanatory as far as their purpose is
concerned. setNum() and setDen() also call the __simplify() method at the end to make the new
resulting fractions a bit cleaner.


__str__(), __float__(), and __int__() return the fraction as strings, floats, or integers.__add__(), __sub__(), __mul__(), __truediv__() 
perform the following mathematical functionsbetween fraction objects: addition, subtraction, multiplication, and division. The results are returned as
fraction objects. __mul__() multiplies the integers with each other and does the same with the
denominators. __truediv__(), on the other hand, multiplies one fraction’s numerator with the other’s
denominator and vice versa. __add__() and __sub__() at first calculate the LCM for the combined new
fraction. Then it multiplies each fraction’s numerator with the quotient obtained by dividing the LCM
with the respective numerator’s denominator. Then addition or subtraction is done respectively.
getReciprocal() interchanges numerator’s and denominator’s positions. They are then returned
in a Fraction object.


__eq__(), __ne__(), __lt__(), __le__(), __gt__(), and __ge__() are comparison operations and
they determine the following respectively: Equal to, not equal to, less than, less than or equal to, greater
than, and greater than and equal to. A Boolean value of true or false is returned depending on the
circumstances. The code also accommodates for when there is a 0 in the denominator.
