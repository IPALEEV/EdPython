money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month_count = 0
while salary + money_capital > spend:
    money_capital += salary
    if month_count == 0:
        money_capital -= spend
    else:
        money_capital -= spend * (increase + 1)
        spend *= (increase + 1)
    month_count += 1
print("Количество месяцев, которое можно протянуть без долгов:", month_count)
