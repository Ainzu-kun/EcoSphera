users = {
    'admin': {'username': 'admin', 'password': 'admin'},
    'user': {'username': 'user', 'password': 'user'},
}

def choice2():
    print('=' * 30)
    choice2 = int(input('\n[1]EcosCalc\n[2]CRUD Bank Sampah\n[3]LogOut\n[4]Exit' + '\nSilakan pilih fitur berdasarkan angka: '))

    if(choice2 == 3):
        print('\nLogout berhasil!')
        choice1()
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
