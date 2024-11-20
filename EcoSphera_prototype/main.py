import pandas as pd

auth = 'user'

def crud():
    bank_sampah = pd.read_csv('./data/data_bank_sampah.csv', sep=';')
    header = ['nama bank sampah', 'nama pengelola', 'lokasi', 'kontak pengelola', 'harga sampah organik', 'harga sampah non-organik']

    print('\n' + 30 * '=')
    choice = int(input('\n[1]Tambah data bank sampah\n[2]Lihat data bank sampah\n[3]Update data bank sampah\n[4]Hapus data bank sampah\n[5]Kembali\nSilakan pilih fitur berdasarkan angka: '))

    if(choice == 1):
        nama_bank = input('\nMasukan nama bank sampah: ')
        nama_pengelola = input('Masukkan nama pengelola: ')
        lokasi = input('Masukkan lokasi bank sampah: ')
        kontak = int(input('Masukkan nomor pengelola bank sampah: '))
        organik = int(input('Masukkan harga sampah organik: '))
        non_organik = int(input('Masukkan harga sampah non organik: '))

        data = [[nama_bank, nama_pengelola, lokasi, kontak, organik, non_organik]]

        new_data =  pd.DataFrame(data, columns=header)
        new_data.to_csv('./data/data_bank_sampah.csv', mode='a', sep=';', header=False, index=False)

        print('\nData bank sampah berhasil dibuat!!!')
        crud()
    elif(choice == 2):
        print(bank_sampah)
        crud()
    elif(choice == 3):
        print('\nFitur ini masih dalam pengembangan!!!')
        crud()
        # print('\n')
        # print(bank_sampah)
        # print('\n')
        # update_index = input('Pilih nomor bank sampah yang ingin di update (q jika tidak ada): ')

        # if(update_index.lower() == 'q'):
        #     crud()
        # else:
        #     update_bank_sampah = bank_sampah.loc[int(update_index), []]
    elif(choice == 4):
        print('\n')
        print(bank_sampah)
        print('\n')
        delete_index = input('Pilih nomor bank sampah yang ingin dihapus (q jika tidak ada): ')

        if(delete_index.lower() == 'q'):
            crud()
        else:
            delete_bank_sampah = bank_sampah.drop(index=int(delete_index))
            delete_bank_sampah.to_csv('./data/data_bank_sampah.csv', sep=';', index=False)
            print('\n' + 'Data bank sampah berhasil dihapus!!!')
            crud()
    elif(choice == 5):
        choiceAdmin()


def ecoscalc():
    bank_sampah = pd.read_csv('./data/data_bank_sampah.csv', sep=';')

    print('\n' + 30 * '=')
    print(bank_sampah)
    selected_bank = input('\nPilih bank sampah berdasarkan nomor bank sampah (q jika tidak ada): ')

    if(selected_bank == 'q'):
        choiceAdmin()
    elif int(selected_bank) in bank_sampah.index:
        data_dipilih = bank_sampah.iloc[int(selected_bank)]
        
        harga_organik = data_dipilih['harga sampah organik']
        harga_non_organik = data_dipilih['harga sampah non-organik']

        input_organik = int(input('\nMasukkan berat sampah organik(kg): '))
        input_non_organik = int(input('Masukkan berat sampah non-organik(kg): '))

        print(f'\nTotal harga sampah organik anda adalah Rp.{harga_organik * input_organik}')
        print(f'Total harga sampah non-organik anda adalah Rp.{harga_non_organik * input_non_organik}')

        next_step = int(input('\n[1]Ya\n[2]Tidak\nApakah anda ingin menghitung lagi? '))

        if(next_step == 1):
            ecoscalc()
        elif(next_step == 2):
            if(auth == 'admin'):
                choiceAdmin()
            elif(auth == 'user'):
                choiceUser()
        else:
            print('Silakan pilih berdasarkan pilihan yang tersedia!')

    else:
        print('\nData belum ada, silakan data dengan benar!')
        ecoscalc()


def choiceAdmin():
    print('\n' + 30 * '=')
    choice = int(input('\n[1]EcosCalc\n[2]CRUD Bank Sampah\n[3]Search Bank Sampah\n[4]Rating Bank Sampah\n[5]Logout\n[6]Exit\nSilakan pilih fitur berdasarkan angka: '))

    if(choice == 1):
        ecoscalc()
    elif(choice == 2):
        crud()
    elif(choice == 5):
        print('\nLogout berhasil!!!')
        login()
    elif(choice == 6):
        pass
    else:
        print('Silakan pilih berdasarkan angka atau pilihan yang tersedia')


def choiceUser():
    print('\n' + 30 * '=')
    choice = int(input('\n[1]EcosCalc\n[2]Search Bank Sampah\n[3]Rating Bank Sampah\n[4]Logout\n[5]Exit\nSilakan pilih fitur berdasarkan angka: '))

    if(choice == 1):
        ecoscalc()
    elif(choice == 4):
        login()
    elif(choice == 5):
        pass
    else:
        print('Silakan pilih berdasarkan angka atau pilihan yang tersedia')


def choicePengelola():
    pass


def login():
    users = pd.read_csv('./data/users.csv', sep=';')

    print('\n' + 30 * '=')

    print('\nSilakan masuk ke akun anda!\n')
    uname = input('Masukkan username: ')
    pw = input('Masukkan password: ')

    validate = users[(users['username'] == uname) & (users['password'] == pw)]

    if(not validate.empty):
        print('\n' + 30 * '=')
        print('Login berhasil!!!')
        role = validate.iloc[0]['role']
        if(role == 'admin'):
            auth = 'admin'
            choiceAdmin()
        elif(role == 'user'):
            auth = 'user'
            choiceUser()
        elif(role == 'pengelola'):
            auth = 'pengelola'
            print('Fitur ini masih dalam pengembangan!')
            choicePengelola()
        else:
            print('laahh siapa dong ini')
    else:
        print('Username atau password salah! Silakan coba lagi!')
        login()


def register():
    users = pd.read_csv('./data/users.csv', sep=';')

    print('\n' + 30 * '=')

    regisChoice = int(input('\n[1]User\n[2]Pengelola\nSilakan pilih register sebagai: '))

    if(regisChoice == 1 or regisChoice == 2):
        def regis2():
            uname = input('\nMasukkan username: ')
            pw = input('Masukkan password: ')
            
            notUnique = users[(users['username'] == uname)]
            if(not notUnique.empty):
                print('\nUsername sudah terdaftar! Silakan pakai username baru!')
                regis2()
            else:
                header = ['username', 'password', 'role']

                if(regisChoice == 1):
                    user = [[uname, pw, 'user']]
                elif(regisChoice == 2):
                    user = [[uname, pw, 'pengelola']]

                new_user = pd.DataFrame(user, columns=header)
                new_user.to_csv('./data/users.csv', mode='a', sep=';', header=False, index=False)

                print('\nSelamat akun anda telah berhasil dibuat!!! Silakan login terlebih dahulu!')
                login()
        regis2()
    else:
        print('Silakan pilih 1 atau 2!!!')


def choice1():
    print('\n' + 30 * '=')
    print('Selamat Datang di EcoSphera!!!')
    
    choice = int(input('\n[1]Register\n[2]Login\nSilakan pilih Login atau Register: '))

    if(choice == 1):
        register()
    elif(choice == 2):
        login()
    else:
        print('Silakan pilih 1 atau 2!!!')


choice1()