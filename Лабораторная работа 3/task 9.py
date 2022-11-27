salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

spend_all_months = spend

for i in range(2, months+1):
    spend = spend * 1.03
    spend_all_months = spend_all_months + spend

money_capital = spend_all_months - salary * months

print(round(money_capital))
