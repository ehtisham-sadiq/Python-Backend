def Calculator(num1, num2):
    print(f"Sum of {num1} and {num2} is : {num1+num2}")
    print(f"Subtraction of {num1} and {num2} is : {num1-num2}")
    print(f"Multiplication of {num1} and {num2} is : {num1*num2}")
    if num2==0:
    	print("Division is not possible")
    else:
    	print(f"Division of {num1} and {num2} is : {format(num1/num2, '.2f')}")
    	
def main():
    number1 = int(input("Enter First Number : "))
    number2 = int(input("Enter Second Number : "))
    Calculator(number1,number2)
    
if __name__== '__main__':
    print("This piece of code must be executed! When we run this file as a python Script")
    main()
