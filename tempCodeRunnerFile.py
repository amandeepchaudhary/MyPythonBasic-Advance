from datetime import date
dob=date(2000,8,22)

t=date.today()
print(t)
age=t.year - dob.year-((t.month, t.day)<(dob.month,dob.day))
print(age)

print(2-False)
print(2-True)