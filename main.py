asistent="Ron"
print("Меня зовут", asistent)
name=input("Ведите ваше имя: ")     
print("Приятно познакомится,", name)
age=input("Скоко тебе лет?: ")
print("Вам", age, "лет")
print("А ты знал что через 10 лет тебе будет", int(age)+10, "лет")
height=input("Какой у вас рост? Например мой 0.53 метра: ")
print("Ого! Ты выше меня на",float(height)-0.53,)
print("Мне очень приятно познакомится:",name,age,"лет! С ростом",height,"метра!")
print("Я умею ,\n1 рассказывать анекдоты,\n2 я могу тебя подержать,\n3 рассказать что такое историю")
answer=input("Какое действие хочеш выполнить?")
if answer=="1":
    print("Экономия-это когда штопаеш носки нитками от чайных пакетиков")
    user_input=input("Хочеш ли ты услышать анекдот? тогда введи 1")
    if user_input=="1":
        print("Только глаз перестал дёргатся, а отпуск уже закончился.")
    else:
        print("ого спасибо что спросил!!!!!")
if answer=="2":
    print("Ты молодец!!!!")
if answer=="3":
    print("История-наука иследующая прошлое реальные факты и закономерности смены исторических событий")