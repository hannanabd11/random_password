import random


letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*/'

len_password=int(input('How many letters u want in your password:'))

password_random=random.choices(letters,k=len_password)

password=''.join(password_random)


print(password)
