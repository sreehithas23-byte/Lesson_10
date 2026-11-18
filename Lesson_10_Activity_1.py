string=input("Enter a lovely string: ")
char=input("Enter a character to count: ")
i=0
count=0
while i<len(string):
    if string[i]==char:
        count+=1
    i+=1
print("The total number of times, ",char," appears in the string is: ",count)
