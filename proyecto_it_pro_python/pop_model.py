import math

alfa_start = 0.0001
x_0 = 0.961482
k = 500000

pop_values = {
        '1980':480741.00,
        '1990':407811.00,
        '2000':360478.00,
        '2005':355017.00,
        '2010':385439.00,
        '2015':417416.00,
        '2020':432259.00 
        }

alfas = []
#for pop_year in pop_values:
X_1 = 0
pop_year = 480741
while True:
    X_1 = alfa_start*x_0*(1-x_0)*k
    alfa_start+=0.001
    if X_1 < pop_year + 20000 and pop_year -20000 < X_1:
        alfas.append(alfa_start)
        break
print(alfas)

