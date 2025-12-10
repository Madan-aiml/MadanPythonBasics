numbers = list(map(int,input("Enter numbers seperated by specs").split()))
               
mean = sum(numbers) / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

print("mean:",mean)
print("Maximum:",maximum)
print("minimum:",minimum)