# break 

while True:
    try:
        hitung = int(input("Hitung sampai berapa??\njawab: "))
        print("\n")

        angka = 0
        while True:
            angka += 1
            print(f"count {angka}")

            if angka == hitung:
                print("Enough....\n")
                break  # Keluar dari loop menghitung

        # Menanyakan apakah pengguna ingin mengulangi program
        ulang = input("do you want to repeat the program? (yes/no): ").strip().lower()
        if ulang != 'yes':
            print("Thanks! Program completed.")
            break  # Keluar dari loop utama jika tidak ingin mengulangi

    except ValueError:
        print("Input is invalid, enter a valid integer")
