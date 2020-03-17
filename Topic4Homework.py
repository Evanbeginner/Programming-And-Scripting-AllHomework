A=int(input("Enter number"))
#creating variable int A to store user input number
L=[]
#creating a list to store calculated numbers from control flow below
while A != 1 :
 if A % 2 ==0:
    A = A/2
    L.append(A)
 else:
     A = (A*3)+1
     L.append(A)
print(L)
#above shows an if statement within a while statement
#while the user input number is not equal to 1(program terminates on 1)
#if the number is even ie no remainder after 2 it is divided by 2 and new value is appended to L
#if number is odd(else) is is multiploed by 3 and 1 is added and then appended
#the control flow(while loop) keeps checking A's value and will continue to run aslong as A is not equal to 1
#Finally the list L is printed
