print("Half pyramid pattern of (numbers)")
n=int(input("Enter number of rows: "))
#usefullist=[]
#list=[]
count=0
#i=0
for i in range(n):
    for i in range (i+1):
        #i += 1
        count += 1 and count<n
        #usefullist.append(count)
        #list.append(usefullist) 
        print(count, end=" ")
    print()