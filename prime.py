start=int(input("Enter the start range: "))
end=int(input("Enter the end range: "))
primes=[]
for num in range(start, end+1):
    if num>1:
        is_prime=True
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                is_prime=False
                break
        if is_prime:
            primes.append(num)
print(f"Prime numbers between {start} and {end} are {primes} ")