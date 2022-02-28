from audioop import avg
from statistics import mean

transaction_list = [250, 12, 45, 32, 23, 25, 250, 12]
moy = mean(transaction_list)
print(moy)

moy = sum(transaction_list) / len(transaction_list)
print(moy)