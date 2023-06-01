first_name = 'John'
last_name = 'Smith'
age = 20
returning = False

if not returning:
    returning = 'New patient'

print('Patient:',last_name.upper()+',',first_name.upper())
print('Age:',age)
print(returning)