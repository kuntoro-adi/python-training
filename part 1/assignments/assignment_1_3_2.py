nama_nama_ikan = ["Ayam-ayam", "Alu-alu", "Bandeng", "Barakuda", "Baronang", "Belanak", "Buntal", "Cakalang", "Cucut", "Cupang", "Discus","Hiu", "Gatul", "Giru", "Guppy", "Gabus", "Haring", "Hilsa", "Injel", "Iwak pitik", "Iwak tempe", "Iwak peyek", "Julung-julung", "Kembung", "Kod", "Koki", "Koi", "Kepe-kepe", "Layur", "Lemadang", "Lepu",  "Lele", "Louhan", "Mas", "Makarel", "Mujahir", "Molly", "Nila", "Neon", "Platy", "Pari", "Pindang", "Sepat", "Salmon", "Sarden", "Kakap", "Kedukang", "Kerapu", "Terubuk", "Tenggiri", "Teri", "Tongkol", "Tuna"]

print('Sebutkan nama nama ikan (5)!')
nni = [x.lower() for x in nama_nama_ikan]

c = 0
while True:
    x = input()
    x = x.lower()
    if x in nni:
        print('Correct!')
        c = c + 1
    else:
        print('try again')
    if c >= 5:
        print('Horee')
        break