nums_0 = []
for i in range(10):
    if i % 2 == 0:
        nums_0.append(i**3)
print(nums_0)



nums_1 = [x**3 for x in range(10) if x % 2 == 0]
print(nums_1)

dict_1 = {'name': 'Bob', 'age': 30, 'adress': "Plehanova st."}
print(dict_1.get('name'))
print(dict_1.get('name1', 'нет такого значения'))

print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())
dict_1['name'] = 'Oleg'
print(dict_1)
dict_1['name1'] = 'Andrey'
print(dict_1)