def removeanumber (number):
    for n in number:
        if (n == 5):
            number.remove(n)
    return number
    
    
    
    
    
    
a = [1,2,3,4,5]
print (removeanumber(a))