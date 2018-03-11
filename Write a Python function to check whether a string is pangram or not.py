Write a Python function to check whether a string is pangram or not.

#CODE
import string
def ispangram(str1, alphabet=string.ascii_lowercase):  
    alphaset = set(alphabet)  
    return alphaset <= set(str1.lower())  

#OUTPUT
ispangram("The quick brown fox jumps over the lazy dog")
True
ispangram("hello aim ad sdaosidijasd")
False
