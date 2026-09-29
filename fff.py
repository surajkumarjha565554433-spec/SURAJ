a=int(input("Enter the no:"))
b=int(input("Enter the no:"))
c=int(input("Enter the no:"))
d=int(input("Enter the no:"))
e=int(input("Enter the no:"))

#if(a>b):
#        if(a>c):
#           if(a>d):
#                print("A is greater ")
#           else:
#               print("D is greater ")
#        elif(c>d):
#            print("C is greater ")
#        else:
#            print("D is greater ")
else:
#   if(b>c):
#     if(b>d):
#        print("B is greater ")
#    else:
#        print("D is greater ")
#elif(c>d):
#    print("C is greater ")
#else:
#    print("D is greater ")

if(a>b):
    if(a>c):
        if(a>d):
            if(a>e):
                print("A is greater :")
            else:
                print("E is greater :")
        elif(d>e):
            print("D is greater :")
        else:
            print("E is greater :")
    elif(c>d):
        if(c>e):
            print("C is greater :")
        else:
            print("E is greater :")
    elif(d>e):
        print("D is greater :")
    else:
        print("E is greater :")
elif(b>c):
    if(b>d):
        if(b>e):
            print("B is greater :")
        else:
            print("E is greater :")
    elif(c>e):
        print("C is greater :")
    else:
        print("E is greater :")
elif(c>d):
    if(c>e):
        print("c is greater :")
    else:
        print("E is greater :")
elif(d>e):
    print("d is greater :")
else:
    print("E is greater :")