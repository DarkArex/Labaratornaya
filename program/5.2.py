
res = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]
sort = sorted(res)
Good = sort[:3]
Bad = sort[-3:]
X = [result for result in res if result >= 10]
print(f"Лучшие 3: {Good}")
print(f"Худшие 3: {Bad}")
print(f"Все с 10: {X}")