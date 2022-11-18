# ДЗ к семинару 11

# Дана функция f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

# Определить корни

# Найти интервалы, на которых функция возрастает

# Найти интервалы, на которых функция убывает

# Построить график

# Вычислить вершину

# Определить промежутки, на котором f > 0

# Определить промежутки, на котором f < 0

import math
from sympy import *
# from sympy.plotting import plot as plt
import matplotlib.pyplot as plt
# from sympy import Symbol
init_printing()
start = -20.0
stop = 24.0
step = 0.1
def solve(x):
    y = -12*x**4*sin(cos(x)) - 18*x**3+5*x**2 + 10*x - 30
    return y
num_x = []
num_y = []
starts = start
while starts<stop:
    num_x.append(starts)
    starts+=step
for num in num_x:
    num_y.append(round(solve(num), 2))
    
# 5. Вершина

num_x_verch = []
num_y_verch = []
grafik_f = {}
for num in num_x:
    grafik_f[num] = round(solve(num), 2)
values_num = []
num_max = []
num_min = []
for key, values in grafik_f.items():
    values_num.append(values)
for k in range(1, len(values_num)-1):
    j = k-1
    l = k+1
    if(values_num[j] < values_num[k] > values_num[l]):
        num_max.append(values_num[k])
    if(values_num[j] > values_num[k] < values_num[l]):
        num_min.append(values_num[k])
values_verch = {}
for keys, value in grafik_f.items():
    for verch_max in num_max:
        if(value == verch_max):
            values_verch[keys] = value
            num_x_verch.append(keys)
            num_y_verch.append(value)
    for verch_min in num_min:
        if(value == verch_min):
            values_verch[keys] = value
            num_x_verch.append(keys)
            num_y_verch.append(value)
print(f'у бесконечно увеличивающейся амплитутды нет вершин, но есть точки изменения : {num_x_verch} , для промежутка {start} - {stop}')

# у бесконечно увеличивающейся амплитутды нет вершин, но есть точки изменения : [-19.099999999999987, -16.099999999999945, -12.899999999999956, -9.999999999999966, -6.799999999999978, -4.199999999999987, -0.3999999999999847, 0.5000000000000153, 1.700000000000016, 3.8000000000000176, 7.000000000000007, 9.899999999999997, 12.999999999999986, 15.999999999999975, 19.20000000000002, 22.200000000000063] , для промежутка -20.0 - 24.0

plt.grid()
p = plt.plot(num_x, num_y, num_x_verch, num_y_verch, 'o')

# 4. Построение графика

plt.grid()
p = plt.plot(num_x, num_y)

# 6. Определить промежутки, на котором f > 0

num_max_nol_x = []
count_max_nol = []
starts = start
while starts <=stop:
    if(starts == start):
        count_max_nol.append(0)
    temp = solve(starts)
    if(round(temp, 0) >= 0.0):
        num_max_nol_x.append(starts)
        count_max_nol.append(starts)
    else:
        count_max_nol.append(0)
    starts+=0.01
    if(starts==stop):
        count_max_nol.append(0)
interval_max_nol_nach_x = []
interval_max_nol_kon_x = []
for count_a in range(1, len(count_max_nol)-1):
    count_s = count_a-1
    count_d = count_a+1
    if(count_max_nol[count_s]==0 and count_max_nol[count_a]!=0 and count_max_nol[count_d]!=0):
        interval_max_nol_nach_x.append(count_max_nol[count_a])
    if(count_max_nol[count_s]!=0 and count_max_nol[count_a]!=0 and count_max_nol[count_d]==0):
        interval_max_nol_kon_x.append(count_max_nol[count_a])
interval_max_nol_nach_y = []
interval_max_nol_kon_y = []
for max_nach_nol_y in interval_max_nol_nach_x:
    interval_max_nol_nach_y.append(solve(max_nach_nol_y))
for max_nol_kon_y in interval_max_nol_kon_x:
    interval_max_nol_kon_y.append(solve(max_nol_kon_y))
for prt_max in range(0, len(interval_max_nol_nach_x)):
    print(f'промежуток от : {interval_max_nol_nach_x[prt_max]} <-> {interval_max_nol_kon_x[prt_max]}')
    
# промежуток от : -17.359999999999587 <-> -14.029999999999418
# промежуток от : -11.12999999999948 <-> -7.659999999999554
# промежуток от : -5.0199999999996106 <-> -1.3399999999996741
# промежуток от : 2.280000000000322 <-> 4.380000000000278
# промежуток от : 8.0400000000002 <-> 10.86000000000014
# промежуток от : 14.250000000000068 <-> 17.190000000000218
# промежуток от : 20.500000000000735 <-> 23.490000000001203

num_nol_y = []
for num_nol_0 in num_max_nol_x:
    num_nol_y.append(solve(num_nol_0))
plt.grid()
p = plt.plot(num_x, num_y, 
            num_max_nol_x, num_nol_y, 'o', 
            interval_max_nol_nach_x, interval_max_nol_nach_y, 'x', 
            interval_max_nol_kon_x, interval_max_nol_kon_y, 'x')

# 7. Определить промежутки, на котором f < 0

num_min_nol_x = []
count_min_nol = []
starts = start
while starts <=stop:
    if(starts == start):
        count_min_nol.append(0)
    temp = solve(starts)
    if(round(temp, 0) <= 0.0):
        num_min_nol_x.append(starts)
        count_min_nol.append(starts)
    else:
        count_min_nol.append(0)
    starts+=0.01
    if(round(starts, 3)==stop):
        count_min_nol.append(0)
interval_min_nol_nach_x = []
interval_min_nol_kon_x = []
for count_v in range(1, len(count_min_nol)-1):
    count_b = count_v-1
    count_n = count_v+1
    if(count_min_nol[count_b]==0 and count_min_nol[count_v]!=0 and count_min_nol[count_n]!=0):
        interval_min_nol_nach_x.append(count_min_nol[count_v])
    if(count_min_nol[count_b]!=0 and count_min_nol[count_v]!=0 and count_min_nol[count_n]==0):
        interval_min_nol_kon_x.append(count_min_nol[count_v])
interval_min_nol_nach_y = []
interval_min_nol_kon_y = []
for min_nach_nol_y in interval_min_nol_nach_x:
    interval_min_nol_nach_y.append(solve(min_nach_nol_y))
for min_nol_kon_y in interval_min_nol_kon_x:
    interval_min_nol_kon_y.append(solve(min_nol_kon_y))
for prt_min in range(0, len(interval_min_nol_nach_x)):
    print(f'промежуток от : {interval_min_nol_nach_x[prt_min]} <-> {interval_min_nol_kon_x[prt_min]}')
    
# промежуток от : -20.0 <-> -17.36999999999959
# промежуток от : -14.019999999999419 <-> -11.13999999999948
# промежуток от : -7.6499999999995545 <-> -5.02999999999961
# промежуток от : -1.3399999999996741 <-> 2.2700000000003224
# промежуток от : 4.390000000000278 <-> 8.0300000000002
# промежуток от : 10.87000000000014 <-> 14.240000000000068
# промежуток от : 17.20000000000022 <-> 20.490000000000734
# промежуток от : 23.500000000001204 <-> 23.99000000000128

num_min_nol_y = []
for num_min_0 in num_min_nol_x:
    num_min_nol_y.append(solve(num_min_0))
plt.grid()
p = plt.plot(num_x, num_y, 
            num_min_nol_x, num_min_nol_y, 'o', 
            interval_min_nol_nach_x, interval_min_nol_nach_y, 'x',
            interval_min_nol_kon_x, interval_min_nol_kon_y, 'x')

# 1. Определить корни

nach = -31
kon = 31
koren = []
while nach<kon:
    poisk_nol = round(solve(nach), 1)
    if(poisk_nol == 0.0):
        koren.append(nach)
    nach+=0.001
print(koren)
[-1.3389999999850604, 2.273000000014764]

# 2. Найти интервалы, на которых функция возрастает

num_vozrast = []
num_ubivan = []
index_vozrast = []
index_ubivan = []
count_vozrast=0
count_ubivan=0
for k in range(1, len(values_num)-1):
    if(k==1):
        index_vozrast.append(0)
        index_ubivan.append(0)
    j = k-1
    l = k+1
    if(values_num[j] < values_num[k] < values_num[l]):
        num_vozrast.append(values_num[k])
        count_vozrast+=1
        index_vozrast.append(count_vozrast)
    else:
        index_vozrast.append(0)
    if(values_num[j] > values_num[k] > values_num[l]):
        num_ubivan.append(values_num[k])
        count_ubivan+=1
        index_ubivan.append(count_ubivan)
    else:
        index_ubivan.append(0)
    if(k==len(values_num)-2):
        index_vozrast.append(0)
        index_ubivan.append(0)
num_vozrast_x = []
num_vozrast_y = []
for keys, value in grafik_f.items():
    for vozrastan in num_vozrast:
        if(value == vozrastan):
            num_vozrast_x.append(keys)
            num_vozrast_y.append(value)
interval_vozrast_nach_x = []
interval_vozrast_kon_x = []
for a in range(1, len(index_vozrast)-1):
    s = a-1
    d = a+1
    if(index_vozrast[s]==0 and index_vozrast[a]!=0 and index_vozrast[d]!=0):
        interval_vozrast_nach_x.append(num_vozrast_x[index_vozrast[a]-1])
    if(index_vozrast[s]!=0 and index_vozrast[a]!=0 and index_vozrast[d]==0):
        interval_vozrast_kon_x.append(num_vozrast_x[index_vozrast[a]-1])
for prt_vozr in range(0, len(interval_vozrast_nach_x)):
    print(f'промежуток от : {interval_vozrast_nach_x[prt_vozr]} <-> {interval_vozrast_kon_x[prt_vozr]}')
    
# промежуток от : -18.999999999999986 <-> -16.199999999999946
# промежуток от : -12.799999999999956 <-> -10.099999999999966
# промежуток от : -6.699999999999978 <-> -4.2999999999999865
# промежуток от : -0.2999999999999847 <-> 0.40000000000001534
# промежуток от : 1.800000000000016 <-> 3.7000000000000175
# промежуток от : 7.100000000000007 <-> 9.799999999999997
# промежуток от : 13.099999999999985 <-> 15.899999999999975
# промежуток от : 19.300000000000022 <-> 22.100000000000062

interval_vozrast_nach_y = []
interval_vozrast_kon_y = []
for v in interval_vozrast_nach_x:
    interval_vozrast_nach_y.append(solve(v))
for c in interval_vozrast_kon_x:
    interval_vozrast_kon_y.append(solve(c))
plt.grid()
p = plt.plot(num_x, num_y, 
            num_vozrast_x, num_vozrast_y, 'o', 
            interval_vozrast_nach_x,interval_vozrast_nach_y, 'x', 
            interval_vozrast_kon_x, interval_vozrast_kon_y, 'x')

# 3. Найти интервалы, на которых функция убывает

num_ubivan_x = []
num_ubivan_y = []
for keys, value in grafik_f.items():
    for ubivan in num_ubivan:
        if(value == ubivan):
            num_ubivan_x.append(keys)
            num_ubivan_y.append(value)
interval_ubivan_nach_x = []
interval_ubivan_kon_x = []
for w in range(1, len(index_ubivan)-1):
    e = w-1
    r = w+1
    if(index_ubivan[e]==0 and index_ubivan[w]!=0 and index_ubivan[r]!=0):
        interval_ubivan_nach_x.append(num_ubivan_x[index_ubivan[w]-1])
    if(index_ubivan[e]!=0 and index_ubivan[w]!=0 and index_ubivan[r]==0):
        interval_ubivan_kon_x.append(num_ubivan_x[index_ubivan[w]-1])
for prt_ubv in range(0, len(interval_ubivan_nach_x)):
    print(f'промежуток от : {interval_ubivan_nach_x[prt_ubv]} <-> {interval_ubivan_kon_x[prt_ubv]}')

# промежуток от : -19.9 <-> -19.19999999999999
# промежуток от : -15.999999999999945 <-> -12.999999999999956
# промежуток от : -9.899999999999967 <-> -6.899999999999977
# промежуток от : -4.099999999999987 <-> -0.4999999999999847
# промежуток от : 0.6000000000000153 <-> 1.6000000000000159
# промежуток от : 3.9000000000000177 <-> 6.9000000000000075
# промежуток от : 9.999999999999996 <-> 12.899999999999986
# промежуток от : 16.099999999999977 <-> 19.10000000000002
# промежуток от : 22.300000000000065 <-> 23.800000000000086

interval_ubivan_nach_y = []
interval_ubivan_kon_y = []
for v in interval_ubivan_nach_x:
    interval_ubivan_nach_y.append(solve(v))
for c in interval_ubivan_kon_x:
    interval_ubivan_kon_y.append(solve(c))
plt.grid()
p = plt.plot(num_x, num_y, 
            num_ubivan_x, num_ubivan_y, 'o', 
            interval_ubivan_nach_x, interval_ubivan_nach_y, 'x', 
            interval_ubivan_kon_x, interval_ubivan_kon_y, 'x')