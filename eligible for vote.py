n=int(input("enter age"))
d=18-n
if n>=18:
    print("eligible for vote")
elif n!=18 and n<18:
    print("not eligible to vote and you are allowed to vote after",d)
