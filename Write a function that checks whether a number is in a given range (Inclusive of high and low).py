Write a function that checks whether a number is in a given range (Inclusive of high and low)

#CODE
def ran_check(num,low,high):
    if num in range(low,high+2):
        print "The num %s is in the range" %str(num)
    else:
        print "The num %s is not in the range" %str(num)
   
   #OUTPUT
   ran_check(10,40,99)
   The num 10 is not in the range
