users = {
    'admin': {'username': 'admin', 'password': 'admin'},
    'user': {'username': 'user', 'password': 'user'},
}

harga_sampah = {
    'organik': 0,
    'non organik': 0
}

def set_harga_sampah():
    print("\n===Pengelola Bank Sampah===")
    for jenis in harga_sampah.keys():
        harga = int(input(f"\nMasukkan harga per kilogram untuk sampah {jenis}: "))
        harga_sampah[jenis] = harga
        print(f"Harga untuk sampah {jenis} telah diatur menjadi {harga:.2f}per kg.")

    ecoscalc()

def hitung_harga_sampah():
    print("\n===Pengguna Bank Sampah===")
    while True:
        jenis_sampah = input("\nMasukkan jenis sampah (Organik / Non Organik): ").lower()
        if jenis_sampah not in harga_sampah:
            print("Jenis sampah tidak tersedia. Silakan masukkan jenis sampah yang valid.")
            continue

        berat = int(input("Masukkan berat sampah (dalam kg): "))
        total_harga = harga_sampah[jenis_sampah] * berat
        print(f"Total harga untuk {berat} kg sampah  {jenis_sampah} adalah Rp.{total_harga:.2f}. Silahkan pergi menuju bank sampah")

        lagi = input("Apakah anda ingin menghitung lagi? (ya/tidak): ").lower()
        if lagi == 'ya':
            hitung_harga_sampah
        else:
            choice2()
            break

def ecoscalc():
    print("=" * 30)
    ecoscalc = int(input('\n[1] Set Harga Sampah\n[2] Hitung Harga Sampah' + '\nSilakan pilih fitur berdasarkan angka: '))
    if (ecoscalc == 1):
        set_harga_sampah()
    elif(ecoscalc == 2):
        hitung_harga_sampah()

def choice2():
    print('=' * 30)
    choice2 = int(input('\n[1]EcosCalc\n[2]CRUD Bank Sampah\n[3]LogOut\n[4]Exit' + '\nSilakan pilih fitur berdasarkan angka: '))

    if(choice2 == 3):
        print('\nLogout berhasil!')
        choice1()
    elif(choice2 == 1):
        print("\nIni adalah halaman EcosCalc")
        ecoscalc()
    elif(choice2 == 4):
        pass


def login():
    print('=' * 30)
    print('\nSilakan masuk ke akun anda!\n')
    uname = input('Masukkan username: ')
    pw = input('Masukkan password: ')

    keyUser = list(users.keys())
    status_login = False
    
    for i in keyUser:
        if(uname == i):
            user_info = users[uname]
            if(pw == user_info['password']):
                status_login = True
                print(f'\nSelamat datang {uname}!!!')
                choice2()
                break
            else:
                print('Password salah, silakan coba lagi!')
                login()
                status_login = True
                break
        else:
            status_login = False
            
    if(status_login == False):
        print('Username atau password salah silakan coba lagi')
        login()

def register():
    print('=' * 30)
    print('\nSilakan daftarkan akun anda!\n')
    uname = input('Masukkan username: ')
    pw = input('Masukkan password: ')

    users[uname] = {'username': uname, 'password': pw}
    print('\nRegister berhasil, silakan login!')
    login()


def choice1():
    print('\n' + '=' * 30)
    choice1 = input('Silakan pilih Login atau Register terlebih dahulu (login / register): ')

    if(choice1.lower() == 'login'):
        login()
    elif(choice1.lower() == 'register'):
        register()
    else:
        print('Silakan ketik login atau register!')

choice1()
