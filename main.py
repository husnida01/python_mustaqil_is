
# total = 0

# for x in range(1, 11):
#     total += x

# print(total)
    


# for x in range(1, 10):
#      print(x ** 2)  


#functions vazifalar

# def car():
#     for x in range(1, 10+1):
#         print(x)


# car()


#mustakil qaytarish


# import math

# num = float(input("Enter a number: "))

# sqrt = math.sqrt(num)

# print("The square root of", num, "is", sqrt)


# item = "School"


# for x in range(0, len(item)):
#     print(item[x], end= ",")




# for x in range(1, 11):
#     square = 2 ** 4


# print(square)


# num = 0 

# for x in range(1, 11):
#     num += x
#     print(num)

# square = 2 ** 3

# print(square)


# uni = True
# ishga_kirish = True
# pul_topish = False
# boshqa_yol_qidiraman = True


# if uni:
#     print("Men universitetga kiraman")
#     if ishga_kirish:
#         print("Men ishda ishleyman")
#     if pul_topish:
#         print("Men pul topaman")
# else:
#     print("boshqa yol qidiraman")


# score = input("Eneter a score: ")

# if score >= 90: 
#     print("Your score A")
#     if score >= 70:
#         print("Your score B")
#         if score >= 50:
#             print("Your score C")

# else:
#     print("Your score C")



# number = int(input("enter a number: "))

# if number >= 70:
#     print("Your score A")
# elif number <= 60:
#         print("Your score B")
#         if number <= 30:
#              print("Your score C")
# else:
#     print("You failed the exam")


# docondan non olish kerak, nechta non olsa olgan noninga qancha tolov qilishini aytib berishi kerak dastur:


    # narh = 3500.60
    # soni = int(input("necta non olasiz?: "))

    # tolov = soni * narh

    # print("tolov", tolov)

# savollni sora?

# a = int(input("birinci sonni kiriting: "))
# b = int(input("ikkinci sonni kiriting: "))

# c = (b + a)

# print("natija", c) 


# print("operato + ", 25 + 5)
# print("operato - ", 25 - 5)
# print("operato * ", 25 * 5)
# print("operato / ", 25 / 5)
# print("operato ** ", 3 ** 2) ---> ikkinci qiymati bu kvadrati yoki darajasi boladi
# print("operato ** ", 3 ** 3) ---> uchinci qiymati bu kubi boladi


# misol

# a = int(input("som: "))
# b = int(input("tiyin: "))
# n = int(input("Kg: "))

# c = n * (a * 100) + b
# print("Umuiy tiyin: ", c)

# a = int(input("birinci sonni kiriting: "))
# b = int(input("ikkinci sonni kiriting: ")) 
# c = int(a % 10)
# d = int(a % 10)
# print("ohirgi soni: ", c)
# print("ohirgi soni: ", c)


# info = input("Enter: ")
# print("Salom", info)

# info = input("Enter: ")
# print("Salom {}". format(info))

# info = input("Enter: ")
# print("{:.10}" .format(info))

# info = input("Enter: ")
# input(info. capitalize()) ---> yozilgan kickina matindi bos harfini kattaytirib beradi capitalize

# info = input("Enter: ")
# input(info. casefold()) ---> barcha sozlarni hariflarini kicik hariflarga ozgartirib beradi


# info = input("Enter: ")
# print(info.count("oqish")) ---> bu count yordamci dasturda neci martta count ga olingan sozni kelganini aniqlab beradi

# info = "salom"
# print(len(info))  ---> stringdi icidagi sozni hariflari bilan hsoblab uzunligini donalab aytirib beradi va buni raqam saklida korsatib beradi


# masala
# bironbir kiritgan sozimizi avtomatik bizga teskarisiga kilib cikarib bersin

# info = input("Kiriting: ")
# print(info[::-1])



# yozgan infarmatsiyalarimiz coyini ozgartirish kerak
# info = input("Enter: ")
# info2 = input("Enter2: ")
# print(info[::-1] + info2[1]) 


# misol 2

# ikki hil voht kiritiladi 
# time1 = soat1, minut1, secund1
# time2 = soat2, minut2, secund2

time1 = int(input("1-time: "))
time1 = int(input("1-minut: "))
time1 = int(input("1-secund: "))

time2 = int(input("2-time: "))
time2 = int(input("2-minut: "))
time2 = int(input("2-secund: "))