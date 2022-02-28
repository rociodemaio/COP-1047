
gross_income=int(input('Enter your gross income'))
n_dependants=int(input('Enter your number of dependants'))
tax=(gross_income-10000-n_dependants*3000)*.2
print('The income tax is', tax)