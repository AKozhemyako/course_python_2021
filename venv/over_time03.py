#Именованные константы
#мультипликатор сверхурочного времени
BASE_HOURS = 40 #базовое время в неделю
OT_MULTIPLIER = 1.5 #коэфициент умножения в случае переработки

#Получить отработанные часы
hours = float(input('Введите количество часов отработанных за неделю: '))
pay_rate = float(input('Введите почасовую ставку оплаты труда: '))
if hours > BASE_HOURS:
    overtime_hours = hours - BASE_HOURS #расчет зарплаты до удержания без переработки
    overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER # расчитать оплату за переработку
    gross_pay = BASE_HOURS * pay_rate + overtime_pay # расчт Зп до удержания
else:
    gross_pay = hours * pay_rate # рсчитать ЗП до удержагия без учета переработки
print('Зарплата до удержания составляет:  $',
      format (gross_pay, ',.2f'), sep ='' )
