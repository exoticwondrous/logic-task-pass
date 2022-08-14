#Q3/write a function that count how many the given character repeated in a given string?

def find_freq(s,c):  
    r = 0     
    for i in range(len(s)):
        if s[i]== c:
            r = r + 1
    return r

a= input('Enter any text, try to type the characters has some repeating char: ')
b=input('now type the char would like to count its repentance: ')

print('The number of occurrence of '+b + ' is ' + str(find_freq(a,b)))