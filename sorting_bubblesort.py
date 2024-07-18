#bubble sort 

a = [5,3,7,1,3,2,9,11,2]
n = len(a)
print("size: ",n)
for i in range(n-1):
    print("pass",i+1,": ",end = "")
    for j in range(n-1):
        if(a[j] > a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
    for j in range(n):
        print(a[j],end = " ")
    print()
    print("final sorted array")
for i in range(n):
    print(a[i],end = " ")

