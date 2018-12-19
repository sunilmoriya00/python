max = None
min = None

while True :
    num = input("Enter a number: ")
    if num == "done" :
        break
    try :
        num = int(num)
    except :
        print ("Invalid input")
        continue
	#check for maximum number 	
    if max is None :
        max = num
    elif max < num :
        max = num
	#check for minimum number 	
    if min is None :
        min = num
    elif num < min :
        min = num

print ("Maximum is", max)
print ("Minimum is", min)
