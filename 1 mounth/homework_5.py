Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

del Geeks['bag']
Geeks['address'] = 'Ibraimova 103'
Geeks['phone'] = '0507052018'
Geeks['instagram'] = '@geeks_edu'
new_courses = ['База данных', 'Тестировщик', 'UX/UI']
Geeks['courses'].extend(new_courses)
Geeks['courses'] = set(Geeks['courses'])
Geeks['establishment_date'] = '2018.11.08'

print(f"Количество курсов: {len(Geeks['courses'])}")
for key, value in Geeks.items():
    print(f"{key}: {value}")