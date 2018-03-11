Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24


#CODE
def multiply(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total  
    
#OUTPUT

multiply([1,2,3,-4])
-24
