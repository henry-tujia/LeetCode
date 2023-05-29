prob_temp = 1/365
i = 2
for i in range(1,365):
    prob_temp = 1
    for j in range(0,i):
        prob_temp *= (1/(365-j))
    prob_temp  *= (i-1)/365
    print(i,prob_temp)

# print(i)