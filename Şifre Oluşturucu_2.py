import random
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
karaktersecim = int(input("Şifre kaç karakterli?: "))

sifre = ""


for i in range(karaktersecim):
    sifre = sifre + random.choice(karakter)

print("Oluşturulan parola:", sifre,".")
