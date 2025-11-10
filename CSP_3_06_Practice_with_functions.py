#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(a,b,c):
    # s = (a + b + c) /2
    return (a + b + c) /2


#Modify the below function such that it takes in 4 arguments. multiply the first
#argument by the difference between itself and each individual argument. Reference herons formula for more context.
def multiplyDifferences(s,a,b,c):
    return s * (s-a)*(s-b)*(s-c)

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def herons(a,b,c):
    s = semiPerimeter(a,b,c)
    product = multiplyDifferences(s,a,b,c)
    area = root(product)
    return area
#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(a):
    return 2*a

#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(b, discriminant_sqrt):
    solution1 = -b + discriminant_sqrt
    solution2 = -b - discriminant_sqrt
    return solution1,solution2
#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(a,b,c):
    b_squared = b**2
    four_ac = 4*a*c
    return b_squared - four_ac

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(a,b,c):
    discriminant = mainCalc(a,b,c)
    disc_sqrt = root(discriminant)
    numerator1,numerator2 = plusMinus(b,disc_sqrt)
    den = denominator(a)
    x1 = numerator1 / den
    x2 = numerator2 / den
    return x1,x2

