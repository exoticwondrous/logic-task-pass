#Q2/Write a program to find all prime numbers up to a given range of numbers?

a = int(input("Enter  minimum range from: "))
b = int(input("Enter  maximum range to: "))

print ("The prime Numbers in the range from "+str(a)+' to '+ str(b)+ ' are: ')  
for c in range (a, b + 1):  
    if c > 1:  
        for i in range (2, c):  
            if (c % i) == 0:  
                break  
        else:  
            print (c)  
