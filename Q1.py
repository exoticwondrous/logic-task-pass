#Q1/Write a method that will remove any given character from a String?

a=[]
print('Enter any text')
a = input()
print('enter any character would like to remove from the string')
b=[]
while b!='quit':
     b=input()
     if a.find(b)!=-1:
       c= a.index(b)
       a= a.replace(a[c],'')
       print('result: '+ a)
     else:
      print('Error: the given char is not contain in the string!')

print('Exit')      



