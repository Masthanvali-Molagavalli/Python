print("FINDING TRIANGLE USING PYTHON LANGAUGE");

# Taking input from the user

p = float(input("Enter First Side Value:- "));
q = float(input("Enter Second Side Value:- "));
r = float(input("Enter Third Side Value:- "));

s = (p+q+r)/2;

area = (s*(s-p)*(s-q)*(s-r)) ** 0.5;

print("The area of the triangle is",area);