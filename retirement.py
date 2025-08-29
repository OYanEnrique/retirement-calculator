from datetime import date
print('------Retirement------')
worker = {}

worker['name'] = input('Worker name:\n')
worker['birth_year'] = int(input('Birth year:\n'))
worker['age'] = date.today().year - worker['birth_year']
worker['ctps'] = int(input('CTPS:\n'))

if worker['ctps'] != 0:
	worker['hiring'] = int(input('Year of hire:\n'))
	worker['wage'] = float(input('Wage:\n'))
	
	worker['retirement'] = worker['age'] + ((worker['hiring'] + 35) - date.today().year)
	
for key, value in worker.items():
	print(f'  - {key.capitalize()}: {value}')