import random

def gen_pass():
    source = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    password_length = 10
    password = " "

    for i in range(password_length):
        password += random.choice(source)

    return password

def flip_coins():
    coins = random.randint(1, 2)
    if coins == 1:
        return 'koin bagia nominal'
    else:
        return 'koin bagian wajah pahlawan'

sampah_organik = ['daun', 'makanan sisa', 'kotoran hewan', 'ranting', 'cangkang telur', 'sisa sayuran', 'buah busuk', 'tulang']

sampah_anorganik = ['kresek', 'kertas', 'kardus', 'ban/karet', 'kaca', 'kaleng', 'botol plastik', 'baterai', 'kabel']