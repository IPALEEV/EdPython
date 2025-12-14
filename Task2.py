salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
for month in range(months):
    money_capital += salary
    if month == 0:
        money_capital -= spend
    else:
        money_capital -= spend * (increase + 1)
        spend *= (increase + 1)
money_capital = int(abs(money_capital))
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
