a=[10,2,3,14,5]
target=int(input("enter target: "))
for i in a:
    if i==target:
        print("found")
        break
else:
    print("not found")