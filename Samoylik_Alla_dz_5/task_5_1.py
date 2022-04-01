from collections import namedtuple

Company = namedtuple('Company', ['name', 'quarterly_profit', 'annual_profit'])
n = int(input('Количество компаний: '))
companies = []
quarters = 4
total_profit = 0

for i in range(n):
    comp_name = input(f'\nНазвание {i + 1}-й компании: ')
    quart_profit = [int(input(f'Прибыль за {q + 1} квартал: ')) for q in range(quarters)]
    company = Company(comp_name, quart_profit, sum(quart_profit))
    companies.append(company)
    total_profit += company.annual_profit
average_profit = total_profit / n

above_average = []
below_average = []

for company in companies:
    if company.annual_profit > average_profit:
        above_average.append(company.name)
    elif company.annual_profit < average_profit:
        below_average.append(company.name)

print(f'\nСредняя прибыль за год (суммарно для компаний): {average_profit}\n')
print(
    f'Компании с прибылью выше среднего: {", ".join(above_average) if above_average else "нет"}')
print(
    f'Компании с прибылью выше среднего: {", ".join(below_average) if below_average else "нет"}')
