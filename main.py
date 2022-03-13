name= ("Cristina")
print(name)

age=("18")
print("Привет! Мне", age, "лет")

my_name= "Cris " + "Cris " + "Cris " + "Cris " + "Cris"
repeat = "Cris " * 5
print(my_name)
print(repeat)

user_name =input("Напишите Ваше имя...")
user_age =input("Напишите Ваш возраст...")
print("Здравствуйте,",user_name,".Вам", user_age, "? По вам и не скажешь...")
convert_age = int(user_age)
if convert_age<18:
    print("Ой, меньше 18? Да меня ж посадят, брысь отсюда")
if convert_age>18:
    print("Да, постарше мы определённо любим...")

s=user_name
text_1=s[2:]
text_2=s[::-1]
text_3=s[-3:]
text_4=s[:5]
print(text_1,text_2,text_3,text_4)

print(len(user_name))

number=int(user_age)
summa=0
mult=1

while number>0:
    digit = number % 10
    summa = summa + digit
    mult = mult * digit
    number = number//10

print("Сумма чисел возраста:", summa)
print("Произведение чисел возраста:",mult)

reg1 = str.lower(user_name)
reg2 = str.upper(user_name)
print(reg1, reg2)
reg3 =  str.title(user_name)
print(reg3)
















