from datetime import date
s_date: date = date(2020, 7, 2)
e_date: date = date(2020, 7, 11)
delta = e_date - s_date
print(delta.days)
