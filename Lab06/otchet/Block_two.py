num1 = int(input("Введите количество учеников в первом классе: "))
class1 = []
print(f"Введите {num1} оценок для первого класса:")
for i in range(num1):
    score = int(input(f"Оценка ученика {i+1}: "))
    class1.append(score)

average1 = sum(class1) / num1
print(f"Средняя оценка в первом классе: {average1:.2f}")


num2 = int(input("Введите количество учеников во втором классе: "))
class2 = []
print(f"Введите {num2} оценок для второго класса:")
for i in range(num2):
    score = int(input(f"Оценка ученика {i+1}: "))
    class2.append(score)

average2 = sum(class2) / num2
print(f"Средняя оценка во втором классе: {average2:.2f}")

two = 2
power = 0

while power<=20:
    result= two**power
    print(f"2^{power} = {result}")
    power+=1