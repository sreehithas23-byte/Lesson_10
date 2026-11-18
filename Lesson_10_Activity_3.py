num= int(input("Enter a number : "))
t=num
numLen=0
while  t>0:
    numLen = numLen + 1
    t = int(t/10)

if numLen>=4:
    numlen =  int(numLen/2)
    chk = 0
    while num>0:
        rem = num % 10
        if chk ==numlen:
            mid = remOne = rem
        elif chk == (numLen - 1) :
            midTwo = rem 
        num = int(num/10)
        chk = chk + 1
        prod = midOne * midTwo
        print("/nProduct of Mid digits ("+str(midOne)+ " * "+ str(midTwo)+") = "+ str(prod))

    else: print ("The number is less than 4 digits, please enter a number with 4 or more digits.")