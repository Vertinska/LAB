amount=float(input("Введите стоимость покупки: "))
if (amount>1000):
    discount=0.05
elif(amount>500):
    discount=0.03
else: 
    discount =0.00

final=amount*(1-discount)
print(f"Итоговая сумма с учетом скидки: {final:.2f} ")