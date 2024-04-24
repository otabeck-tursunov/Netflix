# # 2
#
# tub_sonlar = 0
# son = 1
# while tub_sonlar < 10:
#     count = 0
#     for i in range(1, son + 1):
#         if son % i == 0:
#             count += 1
#     if count == 2:
#         print(son, end=" ")
#         tub_sonlar += 1
#     son += 1
#
# # 5
# son = 26853
# yigindi = 0
#
# while son >= 1:
#     yigindi += son % 10
#     son //= 10
#
# print(yigindi)
#
#
# # 6
# son = int(input("Son kiriting: "))
#
# while son % 2 == 0:
#     son /= 2
#
# print(son)
#
# # 7
# soz = input("So'z kiriting: ")
# unlilar = ['a', 'e', 'i', 'o', 'u']
#
# while soz[0].lower() not in unlilar:
#     if not soz[0].isalpha():
#         print("Sizning 1-belgingiz harf bo'lishi kerak!")
#         break
#     soz = input("So'z kiriting: ")
#

# 9
# x = int(input("Enter the number: "))
# toplam = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# while toplam[-1] >= x:
#     toplam.pop()
# print(toplam)

# 10
# sonlar = [1, 3, 2, 9, 123, 23, 6, 9, 10]
#
# i = 0
# while i < len(sonlar):
#     if sonlar[i] < 10:
#         sonlar.remove(sonlar[i])
#         i -= 1
#     i += 1
#
# print(sonlar)

# soz = "Codial"
# soz = soz.upper()
# print(soz)

# 9
# familiya = input("Ismingizni kiriting: ")
# print(familiya.lower().endswith("a"))


# parol = input("Parol = ")
# print(parol.isdigit())
# print(parol.isnumeric())
# print(parol.isalpha())
# print(parol)

# import math
# x = 8
#
# a = math.sqrt(x) // 1
# print(a)

# address = "192.01.0.180"
# ad = "192[.]01[.]0[.]180"

# sonlar = [0, 1, 4, 5, 9, 10]
#
# a = int(input("a = "))
# b = int(input("b = "))
#
# try:
#     print(a / b)
#     print(sonlar[a])
# except ZeroDivisionError:
#     print("0 ga bo'lish mumkin emas!")
# except IndexError:
#     print("Kiritilgan indeksda element mavjud emas!")
# except:
#     print("Nimadir xato ketdi!")
# print("Dastur tugadi")

# ism = input("Ismingizni kiriting: ")
# yosh = int(input("Yoshingizni kiriting: "))
# kurs = int(input("Kursingizni kiriting: "))
#
# if yosh < 0:
#     raise Exception("Yosh 0 dan kichik bo'lishi mumkin emas!")
#
# if ism[-3:] != "xon" and ism[-3:] != 'bek' and ism[-3:] != 'jon' and ism[-4:] != 'bonu':
#     raise Exception("O'zbekcha ism kiriting!")
#
# if kurs < 1 or kurs > 4:
#     raise Exception("Bunday kurs mavjud emas!")


# ichimliklar = ["Pepsi", 'Fanta', 'Sprite', 'Moxito', 'Coca Cola']
#
# i = 4
# assert i < len(ichimliklar), f"{i} - indeksda ma'lumot yo'q"
#
# print(ichimliklar)

# mening_yoshim = 21
#
# f_yosh = int(input("Yoshingizni kiriting: "))
#
# if mening_yoshim != f_yosh:
#     print("Men bilan tengdosh emas ekansiz!")
# print("Dastur tugadi")

# kastyum = input("Kostyumingiz bormi: ")
# galstuk = input("Galstukingiz bormi: ")
#
# if kastyum == "bor" and galstuk == "bor":
#     print("Maktabga kirishingiz mumkin!")


# k = input("Koreys tilini bilasizmi: ")
# e = input("Ingliz tilini bilasizmi: ")
#
# if k == "ha" or e == "ha":
#     print("Koreaga borishingiz mumkin! Visangizni kuting!")


t = float(input("Yoshingizni kiriting: "))

# if 41 <= t < 44:
#     print("Tana haroratingiz juda baland, 103 ga qo’ng’iroq qiling")
# elif 37 <= t < 41:
#     print("Tana haroratingiz baland, dam oling va ko’p suyuqlik iching")
# elif 36.5 <= t < 37:
#     print("Tana haroratingiz normal, sog’ligingiz joyida")
# elif 32 <= t < 36.5:
#     print("Tana haroratingiz past, dam oling va issiqroq kiyining.")
# elif 24 <= t < 32:
#     print("Tana haroratingiz juda past, 103 ga qo’ng’iroq qiling")
# else:
#     print("Tana haroratingiz sezilarli darajada xavfli!")
