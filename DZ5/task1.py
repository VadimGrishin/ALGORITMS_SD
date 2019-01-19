from collections import namedtuple

Company = namedtuple('Company', 'name q1 q2 q3 q4')
n = int(input('Введите количество предприятий '))
companies = []
s = 0
for i in range(n):
    a = input(f'Введите наименование предприятия ' 
        f'и прибыль по кварталам (разделенные запятыми): ').split(',')
    a = [int(v.strip()) if i else v for i, v in enumerate(a)]
    print(a)
    s += sum(a[1::1])
    companies.append(Company(*a))

avg = s / n

above = [c.name for c in companies if (c.q1 + c.q2 + c.q3 + c.q4) > avg]
below = [c.name for c in companies if (c.q1 + c.q2 + c.q3 + c.q4) < avg]

print(f'Прибыль выше среднего: {above}')
print(f'Прибыль ниже среднего: {below}')

# Gmbh RFS, 10,10,10,10
# ООО Рога, 15,15,15,15
# ООО Копыта, 20, 20, 20,20  
