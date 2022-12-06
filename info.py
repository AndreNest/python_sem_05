nums_0 = []
for i in range(10):
    if i % 2 == 0:
        nums_0.append(i**3)
print(nums_0)



nums_1 = [x**3 for x in range(10) if x % 2 == 0]
print(nums_1)