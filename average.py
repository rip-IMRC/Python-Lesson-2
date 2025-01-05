s1=int(input("Enter the first speed: "))
s2=int(input("Enter the second speed: "))
s3=int(input("Enter the third speed: "))
average=(s1+s2+s3)/3
print("The average speed is", average)
if s1<average:
    print("First speed is slower than the average, and the difference is", average-s1)
else:
    print("First speed is faster than the average, and the difference is", s1-average)
if s2<average:
    print("Second speed is slower than the average, and the difference is", average-s2)
else:
    print("Second speed is faster than the average, and the difference is", s2-average)
if s3<average:
    print("Third speed is slower than the average, and the difference is", average-s3)
else:
    print("Third speed is faster than the average, and the difference is", s3-average)