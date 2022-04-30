from sum_num import sum_
from multiplication import mult

if __name__=="__main__":
    x = input("Enter first Integer: ")
    y = input("Enter another Integer to be added: ")
    print("Summation Result: {}".format(sum_(x, y)))
    print("Multiplication Result: {}".format(mult(x, y)))
