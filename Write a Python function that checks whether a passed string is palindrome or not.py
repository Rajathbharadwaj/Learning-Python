Write a Python function that checks whether a passed string is palindrome or not.

#CODE

def palindrome(s):
    if s==s[::-1]:
        print "It's a palindrome"
        
    else:
        print "It's not a palindrome"
				
#OUTPUT				
palindrome("sssss")
It's a palindrome
