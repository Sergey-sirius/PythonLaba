


symbols_count = dict()
symbols_count = {'a': 2, 's': 8, 'd': 8, 'f': 7, 'g': 1, '1': 3, '2': 3, '3': 3}

#symbols_count[s] = symbols_count.get(s, 0) + 1
print(symbols_count)
print(symbols_count.items())
print("---------------------")
print(symbols_count.get('z', 1))
print(symbols_count)
print("---------------------")
d = dict.fromkeys(['a', 'b'])
print(d)
d = dict.fromkeys(['a', 'b'], 100)
print(d)
d = dict.fromkeys(['a', 'b'])
print(d)
print("---------------------")

dic1 = {1: 10, 2: 20}
dic2 = {1: 30, 4: 40}
dic1.update(dic2)
print(dic1)
print("---------------------")
