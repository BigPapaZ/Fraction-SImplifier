#######################
# fraction.py
# Zaigham
# Defines a Fraction Class
#######################



class Fraction:

    #Constructor
    def __init__(self, numerator, denominator):
        self.__numerator=numerator
        self.__denominator=denominator
        self.__simplify()

    def getNum(self):
        '''
        Returns Numerator's value
        Input: Self
        Output: Numeraotr
        '''
        return int(self.__numerator)

    def getDen(self):
        '''
        Returns Denominator's value
        Input: Self
        Output: Denominator
        '''
        return int(self.__denominator)

    def setNum(self, Num):
        '''
        Changes numerator's Value
        Input: Self, New Numerator
        Output: None (Nothing is returned)
        '''
        self.__numerator=Num
        self.__simplify()

    def setDen(self, Den):
        '''
        Changes denominator's Value
        Input: Self, New denominator
        Output: None (Nothing is returned)
                '''
        self.__denominator=Den
        self.__simplify()

    def getReciprocal(self):
        '''
        Interchanging numerator and the denominator
        Input: Self
        Output: None (Nothing is returned)
        '''


        #Defining some variables to be used later with interchanging
        y=self.getDen()
        x=self.getNum()

        self.setDen(x)
        if x<0: self.setNum(-1*y)   #If the numerator is negative
        else:self.setNum(y) #If the numerator is positive

    def __simplify(self):
        '''
        Editing the Fraction to make look a bit cleaner
        Input: Self
        Output: None (Nothing is returned)
        '''

        #If Denominator is 0, then denominator is 0
        if self.getDen()==0:
            self.__numerator=0

        #If numerator is and the denominator is not 0, then denominator is 1
        elif self.getNum()==0 and self.getDen()!=0:
            self.__denominator=1

        #Deleting the common factors out of the fraction
        else:
            if abs(self.getDen())>abs(self.getNum()):
                bigger=abs(int(self.getDen()))
                smaller=abs(int(self.getNum()))

            elif abs(self.getDen())<abs(self.getNum()):
                bigger=abs(int(self.getNum()))
                smaller=abs(int(self.getDen()))

            else:
                bigger = abs(int(self.getDen()))
                smaller = abs(int(self.getNum()))

            for afactor in list(reversed((list(range(1,bigger))))):

                if bigger%afactor==0 and smaller%afactor==0:
                    Thefactor=afactor
                    break

            self.__denominator=self.getDen()/Thefactor
            self.__numerator=self.getNum() / Thefactor

        #If both the umerator and denominator are negative
        if self.getNum()<0 and self.getDen()<0:

            self.__numerator=self.getNum()*-1
            self.__denominator=self.getDen()*-1

        #If only the denominator is negative
        elif self.getDen()<0:

            self.__numerator=self.getNum()*-1
            self.__denominator=self.getDen()*-1

    def __str__(self):
        '''
        Returns a given fraction as a string
        Input: The Fraction
        Output: The fraction as a string
        '''
        return (str(self.getNum())+"/"+str(self.getDen()))

    def __float__(self):
        '''
        Returns a given fraction as a floating point number
        Input: The Fraction
        Output: A float
        '''
        return (self.getNum()/self.getDen())

    def __int__(self):
        '''
        Returns a given fraction as an Integer
        Input: The Fraction
        Output: An integer
        '''
        return (int(self.getNum() / self.getDen()))

    def __add__(self, otherFraction):
        '''
        Adds 2 given fractions
        Input: The 2 fractions
        return: The resulting fraction
        '''


        if self.getDen()==0:
            return Fraction(otherFraction.getNum(), otherFraction.getDen())
        elif otherFraction.getDen()==0:
            return Fraction(self.getNum(), self.getDen())

        #Calculating LCM
        if self.getDen()>otherFraction.getDen():
            LargerDen=self.getDen()
            LargerNum=self.getNum()
            SmallerDen=otherFraction.getDen()
            SmallerNum=otherFraction.getNum()

        elif self.getDen()<=otherFraction.getDen():
            SmallerDen=self.getDen()
            SmallerNum=self.getNum()
            LargerDen=otherFraction.getDen()
            LargerNum=otherFraction.getNum()
        #Determining the numerator of the combined fraction
        if LargerDen%SmallerDen==0:#If the denominators are multiples of each other
            L_C_M=LargerDen
            b=0
        else:                      #If the denominators have nothing in common
            L_C_M=LargerDen*SmallerDen
            b=1
        if b==0:
            UpperPart=(L_C_M/self.getDen())*self.getNum()+(L_C_M/otherFraction.getDen())*otherFraction.getNum()
        elif b==1:
            UpperPart = self.getDen() * otherFraction.getNum()+self.getNum()*otherFraction.getDen()
        return Fraction(UpperPart,L_C_M)

    def __sub__(self, otherFraction):
        '''
        Subtracts 2 given fractions
        Input: The 2 fractions
        return: The resulting fraction
        '''

        if self.getDen()==0:
            return Fraction(otherFraction.getNum(), otherFraction.getDen())
        elif otherFraction.getDen()==0:
            return Fraction(self.getNum(), self.getDen())


        #The same method as in Add. Except the upper part is obtained by subtraction of numerators
        if self.getDen() > otherFraction.getDen():
            LargerDen = self.getDen()
            LargerNum = self.getNum()
            SmallerDen = otherFraction.getDen()
            SmallerNum = otherFraction.getNum()

        elif self.getDen() <= otherFraction.getDen():
            SmallerDen = self.getDen()
            SmallerNum = self.getNum()
            LargerDen = otherFraction.getDen()
            LargerNum = otherFraction.getNum()

        if LargerDen % SmallerDen == 0:
            L_C_M = LargerDen
            b = 0

        else:
            L_C_M = LargerDen * SmallerDen
            b = 1

        if b == 0:
            UpperPart = (L_C_M / self.getDen()) * self.getNum() - (
                                                                  L_C_M / otherFraction.getDen()) * otherFraction.getNum()
        elif b == 1:
            UpperPart = self.getDen() * otherFraction.getNum() - self.getNum() * otherFraction.getDen()
        return Fraction(UpperPart, L_C_M)

    def __mul__(self, otherFraction):
        #Just simple multiplication of Numerators
        return Fraction((self.getNum()*otherFraction.getNum()),(self.getDen()*otherFraction.getDen()))

    def __truediv__(self, otherFraction):
        #One fraction's numerator is divided by the other's denominator. And the latter's denominator is divided by
        #the former's numerator
        return Fraction(self.getNum() * otherFraction.getDen(),self.getDen() * otherFraction.getNum())

    def __eq__(self, other):
        '''
        Determines whether the fractions are equal
        Input: The 2 fractions
        return: A boolean value
        '''
        if self.getDen() == 0:
            return False
        elif other.getDen() == 0:
            return False
        else:
            if (self.getNum()/self.getDen())==(other.getNum()/other.getDen()):
                return True
            else: return False

    def __ne__(self, other):
        '''
        Determines whether the fractions are not equal
        Input: The 2 fractions
        return: A boolean value
        '''
        if self.getDen() == 0:
            return False
        elif other.getDen() == 0:
            return False
        else:
            if (self.getNum()/self.getDen())!=(other.getNum()/other.getDen()):
                return True
            else: return False

    def __lt__(self, other):
        '''
        Determines whether one fraction is less than the other
        Input: The 2 fractions
        return: A boolean value
        '''
        if self.getDen()==0:
            return False
        elif other.getDen()==0:
            return True
        else:
            if (self.getNum()/self.getDen())<(other.getNum()/other.getDen()):
                return True
            else: return False

    def __le__(self, other):
        '''
        Determines whether one fraction is less than or equal to the other
        Input: The 2 fractions
        return: A boolean value
        '''
        if self.getDen()==0:
            return False
        elif other.getDen()==0:
            return True
        else:
            if (self.getNum()/self.getDen())<=(other.getNum()/other.getDen()):
                return True
            else: return False

    def __gt__(self, other):
        '''
        Determines whether one fraction is greater than the other
        Input: The 2 fractions
        return: A boolean value
        '''
        if self.getDen()==0:
            return True
        elif other.getDen()==0:
            return False
        else:
            if (self.getNum()/self.getDen())>(other.getNum()/other.getDen()):
                return True
            else:
                return False

    def __ge__(self, other):
        '''
        Determines whether one fraction is greater than or equal to the other
        Input: The 2 fractions
        return: A boolean value
        '''
        if self.getDen() == 0:
            return True
        elif other.getDen() == 0:
            return False
        else:
            if (self.getNum()/self.getDen())>=(other.getNum()/other.getDen()):
                return True
            else: return False