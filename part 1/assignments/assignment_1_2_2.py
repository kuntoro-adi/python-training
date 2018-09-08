import datetime

y = input('birthday year: ')
m = input('birthday month: ')
d = input('birthday date: ')

bd = datetime.date(int(y), int(m), int(d))

now = datetime.date.today()

delta = now - bd

print('You are ', delta.days / 365.25, ' years old.')