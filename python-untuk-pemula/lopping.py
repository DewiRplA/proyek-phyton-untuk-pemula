# Mencetak kata "Halo Python" sebanyak 5 kali
for x in range(5):
    print("Halo Python.")


# Mencetak semua item pada variabel fruits (lists)
fruits = ['Apple', 'Banana', 'Mango', 'Durian']
for fruit in fruits:
    print(fruit)

# Mencetak semua huruf satu per satu pada kata "Indonesia"
myCountry = "indonesia"
for x in myCountry:
    print(x)


# Mencetak angka, jika angka lebih kecil dari 5
counter = 0
while counter < 5:
    print(counter)
    counter += 1


# Menghentikan perulangan jika nilai x adalah 3
# Pada kode di bawah ini, jika nilai x sama dengan 3,
# maka perulangan akan dihentikan. Walaupun seharusnya
# perulangan akan berhenti setelah 5 kali berjalan.
for x in range(5):
    print(x)
    if x == 3:
        break


