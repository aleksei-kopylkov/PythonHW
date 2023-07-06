name = ["John", "Mike", "Adam", "Sam"]
rate = [40000, 35000, 87500, 104000]
bonus = ["12.5%", "10.3%", "12.25", "11.8"]
result = {name[i]: round((rate[i] * float(bonus[i].strip("%")) / 100), 2) for i in range(len(name))}
print(result)