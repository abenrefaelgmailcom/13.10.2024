

#1 תנאים
number = float(input("הכנס מספר עשרוני: "))
if number > 10:
    print("ההפרש בין המספר ל-10 הוא:", number - 10)
else:
    print("המכפלה של המספר ב-10 היא:", number * 10)

#2
num1 = float(input("הכנס את המספר הראשון: "))
num2 = float(input("הכנס את המספר השני: "))
num3 = float(input("הכנס את המספר השלישי: "))

total = num1 + num2 + num3

if total > 100:
    print("הסכום הוא:", total)
else:
    print("הסכום קטן מ-100")

#3
num1 = float(input("הכנס את המספר הראשון: "))
num2 = float(input("הכנס את המספר השני: "))

frac1 = num1 - int(num1)
frac2 = num2 - int(num2)

if frac1 == frac2:
    print("שווים")
else:
    print("השבר הגדול יותר הוא:", max(frac1, frac2))

#4
age = int(input("הכנס את גילך: "))

if 0 < age < 120:
    print("הגיל הוא:", age)
else:
    print("גיל לא תקין")

#5
number = int(input("הכנס מספר תלת-ספרתי: "))

middle_digit = (number // 10) % 10
print("הספרה האמצעית היא:", middle_digit)

#6 לולאות
n = int(input("הכנס מספר טבעי: "))

for i in range(n, 0, -1):
    print(i, end=", ")

#7
num1 = int(input("הכנס את המספר הראשון: "))
num2 = int(input("הכנס את המספר השני: "))

for i in range(min(num1, num2), max(num1, num2) + 1):
    if i % 2 == 0:
        print(i, end=", ")

#8
n = int(input("הכנס מספר חיובי: "))

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        print(i, end=", ")

#9
n = int(input("הכנס מספר: "))

for i in range(7, n + 1, 7):
    print(i, end=", ")

#11 עיבוד נתונים
total_negative = 0

while True:
    num = int(input("הכנס מספר (0 לסיום): "))
    if num == 0:
        break
    if num < 0:
        total_negative += num

print("סכום המספרים השליליים הוא:", total_negative)

#12
numbers = [int(input("הכנס מספר: ")) for _ in range(10)]
print("הרשימה בסדר הפוך:", numbers[::-1])

#13
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

prime_count = 0

while True:
    num = int(input("הכנס מספר (0 לסיום): "))
    if num == 0:
        break

#14
numbers = []
for i in range(5):
    number = float(input(f"הכנס מספר {i+1}: "))
    numbers.append(number)

average = sum(numbers) / len(numbers)
print(f"הממוצע הוא: {average}")

greater_than_average = [num for num in numbers if num > average]
print(f"מספרים הגדולים מהממוצע: {greater_than_average}")
print(f"כמות המספרים הגדולים מהממוצע: {len(greater_than_average)}")

#15
numerator = int(input("הכנס את המספר הראשון (המונה): "))
denominator = int(input("הכנס את המספר השני (המכנה): "))

if denominator == 0:
    print("לא ניתן לחלק באפס.")
else:
    count = 0
    while numerator >= denominator:
        numerator -= denominator
        count += 1

    print(f"תוצאת החילוק היא: {count}")


#16 אתגרים
number = int(input("הכנס מספר תלת ספרתי: "))

sum_digits = (number // 100) + ((number // 10) % 10) + (number % 10)

if sum_digits % 3 == 0:
    print("מתחלק ב-3")
else:
    print("לא מתחלק ב-3")

#17
text = input("הכנס מחרוזת: ")

if text == text[::-1]:
    print("מהופכת")
else:
    print("לא מהופכת")




