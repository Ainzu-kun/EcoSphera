import pandas as pd
import re

auth = {'auth': 'user'}
user_login = {'username': ''}

def kelolaBank():
    bank_sampah = pd.read_csv('data_bank_sampah.csv', sep=';', dtype={'kontak pengelola': str})
    header = ['nama bank sampah', 'nama pengelola', 'lokasi', 'kontak pengelola', 'harga sampah organik', 'harga sampah non-organik', 'rating']
    bank_sampah_pengelola = bank_sampah[bank_sampah['nama pengelola'] == user_login['username']]

    if(bank_sampah_pengelola.empty):
        step = input('\n[1]Ya\n[2]Tidak\nAnda belum memiliki bank sampah yang dikelola! Apakah ingin membuat bank sampah sekarang? ')

        if(step.replace(' ', '') == ''):
            print('Inputan tidak boleh kosong!')
            kelolaBank()
        elif(not re.match(r'^\d{1}$', step)):
            print('Inputan hanya boleh mengandung angka! Maximal 1 angka!')
            kelolaBank()
        elif(step == '1'):
            nama_bank = input('\nMasukan nama bank sampah: ')
            nama_pengelola = user_login['username']
            lokasi = input('Masukkan lokasi bank sampah: ')
            kontak = input('Masukkan kontak pengelola bank sampah: ')
            organik = input('Masukkan harga sampah organik: ')
            non_organik = input('Masukkan harga sampah non organik: ')
            rating = 0

            if(str(nama_bank).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            elif(str(lokasi).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            elif(str(kontak).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            elif(str(organik).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            elif(str(non_organik).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            elif(not re.match(r'^[a-zA-Z\s]{3,20}$', nama_bank)):
                print('Nama bank sampah hanya boleh berisi huruf dan spasi! Minimal 3 huruf, maximal 20 huruf!')
                kelolaBank()
            elif(not re.match(r'^(?=(?:[^a-zA-Z]*[a-zA-Z]){3})[a-zA-Z0-9\s,\.(\)]{10,255}$', lokasi)):
                print('\nLokasi hanya boleh berisi huruf, spasi, angka, koma, spasi dan tanda kurung, setidaknya memiliki 3 huruf! Minimal 10 karakter!')
                kelolaBank()
            elif(not re.match(r'^\d{7,15}$', kontak)):
                print('\nKontak hanya boleh berisi angka, minimal berisi 7 angka dan maksimal 15 angka!')
                kelolaBank()
            elif(not re.match(r'^\d{4,7}$', organik)):
                print('\nHarga sampah organik hanya boleh berisi angka, minimal 4 angka!')
                kelolaBank()
            elif(not re.match(r'^\d{4,7}$', non_organik)):
                print('\nHarga sampah non organik hanya boleh berisi angka, minimal 4 angka!')
                kelolaBank()
            elif(not re.match(r'^[1-9][0-9]*$', organik)):
                print('\nHarga sampah organik tidak boleh didahului angka 0! Harap masukkan harga dengan benar!')
                kelolaBank()
            elif(not re.match(r'^[1-9][0-9]*$', non_organik)):
                print('\nHarga sampah non organik tidak boleh didahului angka 0! Harap masukkan harga dengan benar!')
                kelolaBank()

            data = [[nama_bank, nama_pengelola, lokasi, f'{kontak}', organik, non_organik, rating]]

            new_data =  pd.DataFrame(data, columns=header)
            new_data.to_csv('data_bank_sampah.csv', mode='a', sep=';', header=False, index=False)

            print('\nData bank sampah berhasil dibuat!')
            kelolaBank()
        elif(step == '2'):
            choicePengelola()
        else:
            print('\nSilakan pilih berdasarkan angka yang tersedia!')
            kelolaBank()
    else:
        print('\n' + 30 * '=')
        choice = input('\n[1]Tambah data bank sampah\n[2]Lihat data bank sampah\n[3]Update data bank sampah\n[4]Hapus data bank sampah\n[5]Kembali\nSilakan pilih fitur berdasarkan angka: ')

        # Validasi choice gaboleh kosong
        if(choice.replace(' ', '') == ''):
            print('\nInputan tidak boleh kosong!')
            kelolaBank()

        # Validasi choice harus angka dan 1 angka aja
        elif(not re.match(r'^\d{1}$', choice)):
            print('\nInput hanya boleh berisi angka! Maximal 1 angka!')
            kelolaBank()

        # Create data bank sampah pengelola
        elif(choice == '1'):
            nama_bank = input('\nMasukan nama bank sampah: ')
            nama_pengelola = user_login['username']
            lokasi = input('Masukkan lokasi bank sampah: ')
            kontak = input('Masukkan kontak pengelola bank sampah: ')
            organik = input('Masukkan harga sampah organik: ')
            non_organik = input('Masukkan harga sampah non organik: ')
            rating = 0

            if(str(nama_bank).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            elif(str(lokasi).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            elif(str(kontak).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            elif(str(organik).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            elif(str(non_organik).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            elif(not re.match(r'^[a-zA-Z\s]{3,20}$', nama_bank)):
                print('\nNama bank sampah hanya boleh berisi huruf dan spasi! Minimal 3 huruf, maximal 20 huruf!')
                kelolaBank()
            elif(not re.match(r'^(?=(?:[^a-zA-Z]*[a-zA-Z]){3})[a-zA-Z0-9\s,\.(\)]{10,255}$', lokasi)):
                print('\nLokasi hanya boleh berisi huruf, spasi, angka, koma, spasi dan tanda kurung, setidaknya memiliki 3 huruf! Minimal 10 karakter!')
                kelolaBank()
            elif(not re.match(r'^\d{7,15}$', kontak)):
                print('\nKontak hanya boleh berisi angka, minimal berisi 7 angka dan maksimal 15 angka!')
                kelolaBank()
            elif(not re.match(r'^\d{4,7}$', organik)):
                print('\nHarga sampah hanya boleh berisi angka, minimal 4 angka!')
                kelolaBank()
            elif(not re.match(r'^\d{4,7}$', non_organik)):
                print('\nHarga sampah hanya boleh berisi angka, minimal 4 angka!')
                kelolaBank()
            elif(not re.match(r'^[1-9][0-9]*$', organik or non_organik)):
                print('\nHarga sampah tidak boleh didahului angka 0! Harap masukkan harga dengan benar!')
                kelolaBank()

            data = [[nama_bank, nama_pengelola, lokasi, f'{kontak}', organik, non_organik, rating]]

            new_data =  pd.DataFrame(data, columns=header)
            new_data.to_csv('data_bank_sampah.csv', mode='a', sep=';', header=False, index=False)

            print('\nData bank sampah berhasil dibuat!')
            kelolaBank()

        # Lihat data bank sampah pengelola
        elif(choice == '2'):
            print('\n', bank_sampah_pengelola)
            kelolaBank()

        # Edit Pengelola
        elif(choice == '3'):
            print('\n', bank_sampah_pengelola)
            selected_bank = input('\nPilih bank sampah yang ingin di update berdasarkan nomor bank sampah (q jika tidak ada): ')

            if(selected_bank.replace(' ', '') == ''):
                print('\nInputan tidak boleh kosong!')
                kelolaBank()
            elif(not re.match(r'^\d+$', selected_bank)):
                print('\nInput hanya boleh berisi angka!')
                kelolaBank()
            elif(int(selected_bank) in bank_sampah_pengelola.index):
                data_dipilih = bank_sampah.iloc[int(selected_bank)]

                nama_bank = data_dipilih['nama bank sampah']
                nama_pengelola = data_dipilih['nama pengelola']
                lokasi = data_dipilih['lokasi']
                kontak = data_dipilih['kontak pengelola']
                harga_organik = data_dipilih['harga sampah organik']
                harga_non_organik = data_dipilih['harga sampah non-organik']
                rating = data_dipilih['rating']

                print('\nSilakan isi data terbaru, kosongkan jika tidak ada perubahan')
                new_nama_bank = input(f'Masukkan nama bank sampah baru ({nama_bank}): ') or nama_bank
                new_lokasi = input(f'Masukkan lokasi bank sampah baru ({lokasi}): ') or lokasi
                new_kontak = input(f'Masukkan kontak baru pengelola bank sampah ({kontak}): ') or kontak
                new_harga_organik = input(f'Masukkan harga baru sampah organik ({harga_organik}): ') or harga_organik
                new_harga_non_organik = input(f'Masukkan harga baru sampah non organik ({harga_non_organik}): ') or harga_non_organik


                if(str(new_nama_bank).replace(' ', '') == ''):
                    print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                    kelolaBank()
                elif(str(new_lokasi).replace(' ', '') == ''):
                    print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                    kelolaBank()
                elif(str(new_kontak).replace(' ', '') == ''):
                    print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                    kelolaBank()
                elif(str(new_harga_organik).replace(' ', '') == ''):
                    print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                    kelolaBank()
                elif(str(new_harga_non_organik).replace(' ', '') == ''):
                    print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                    kelolaBank()
                elif(not re.match(r'^[a-zA-Z\s]{3,20}$', new_nama_bank)):
                    print('\nNama bank sampah hanya boleh berisi huruf dan spasi! Minimal 3 huruf, maximal 20 huruf!')
                    kelolaBank()
                elif(not re.match(r'^(?=(?:[^a-zA-Z]*[a-zA-Z]){3})[a-zA-Z0-9\s,\.(\)]{10,255}$', new_lokasi)):
                    print('\nLokasi hanya boleh berisi huruf, spasi, angka, koma, spasi dan tanda kurung, setidaknya memiliki 3 huruf! Minimal 10 karakter!')
                    kelolaBank()
                elif(not re.match(r'^\d{7,15}$', str(new_kontak))):
                    print('\nKontak hanya boleh berisi angka, minimal berisi 7 angka dan maksimal 15 angka!')
                    kelolaBank()
                elif(not re.match(r'^\d{4,7}$', str(new_harga_organik))):
                    print('\nHarga sampah organik hanya boleh berisi angka, minimal 4 angka!')
                    kelolaBank()
                elif(not re.match(r'^\d{4,7}$', str(new_harga_non_organik))):
                    print('\nHarga sampah non organik hanya boleh berisi angka, minimal 4 angka!')
                    kelolaBank()
                elif(not re.match(r'^[1-9][0-9]*$', str(new_harga_organik))):
                    print('\nHarga sampah organik tidak boleh didahului angka 0! Harap masukkan harga dengan benar!')
                    kelolaBank()
                elif(not re.match(r'^[1-9][0-9]*$', str(new_harga_non_organik))):
                    print('\nHarga sampah non organik tidak boleh didahului angka 0! Harap masukkan harga dengan benar!')
                    kelolaBank()

                bank_sampah.loc[int(selected_bank), ['nama bank sampah', 'nama pengelola', 'lokasi', 'kontak pengelola', 'harga sampah organik', 'harga sampah non-organik', 'rating']] = [new_nama_bank, nama_pengelola, new_lokasi, int(f'{new_kontak}'), int(new_harga_organik), int(new_harga_non_organik), rating]
                bank_sampah.to_csv('data_bank_sampah.csv', index=False, sep=';')

                print('\nData bank sampah Anda berhasil diperbarui!')
                kelolaBank()
            else:
                print('\nSilakan pilih bank sampah yang tersedia!')
                kelolaBank()

        # Hapus data bank sampah pengelola
        elif(choice == '4'):
            print('\n', bank_sampah_pengelola)
            delete_index = input('\nPilih nomor bank sampah yang ingin dihapus (q jika tidak ada): ')

            if(delete_index.lower() == 'q'):
                kelolaBank()
            elif(delete_index.replace(' ', '') == ''):
                print('\nInput tidak boleh kosong!')
                kelolaBank()
            elif(not re.match(r'^\d+$', delete_index)):
                print('\nInput hanya boleh berisi angka!')
                kelolaBank()
            elif(int(delete_index) in bank_sampah_pengelola.index):
                delete_bank_sampah = bank_sampah.drop(index=int(delete_index))
                delete_bank_sampah.to_csv('data_bank_sampah.csv', sep=';', index=False)

                print('\nData bank sampah berhasil dihapus!')
                kelolaBank()
            else:
                print('\nData bank sampah tidak ada dalam pilihan!')
                kelolaBank()
        
        # Kembali
        elif(choice == '5'):
            choicePengelola()

        # Validasi angka <= 1 & >= 5
        else:
            print('\nSilakan pilih opsi sesuai angka yang ada!')
            kelolaBank()


def rating():
    header = ['uname_user', 'id_bank', 'rating']

    bank_sampah = pd.read_csv('data_bank_sampah.csv', sep=';', dtype={'kontak pengelola': str})
    data_rating = pd.read_csv('rating.csv', sep=';')

    print('\n')
    print(bank_sampah)
    print('\n')

    choice = input('Silakan nomor pilih bank sampah yang ingin diberi rating (q untuk quit): ')

    if(choice == 'q'):
        if(auth['auth'] == 'admin'):
            choiceAdmin()
        elif(auth['auth'] == 'user'):
            choiceUser()
        else:
            exit()
    elif(not re.match(r'^\d+$', choice)):
        print('\nSilakan isi berdasarkan angka, hanya boleh berisi 1 angka!')
        rating()
    elif(int(choice) in bank_sampah.index):
        # filter data rating
        filtered_data = data_rating[
            (data_rating['uname_user'] == user_login['username']) &
            (data_rating['id_bank'] == int(choice))
        ]

        if(not filtered_data.empty):
            rating_value = filtered_data['rating'].values[0]
            print(f'\nRating Anda untuk {bank_sampah['nama bank sampah'][int(choice)]} adalah {rating_value}!')

            if(auth['auth'] == 'admin'):
                choiceAdmin()
            elif(auth['auth'] == 'user'):
                choiceUser()
        else:
            user_rating = input(f'\nMasukkan rating untuk {bank_sampah['nama bank sampah'][int(choice)]}(1-5) (q untuk quit): ').strip()

            if(user_rating == 'q'):
                rating()
            elif(user_rating.replace(' ', '') == ''):
                print('\nRating tidak boleh kosong!')
                rating()
            elif(not re.match(r'^\d{1}$', user_rating)):
                print('\nSilakan rating menggunakan angka yang sudah ditentukan!')
                rating()
            elif(user_rating == '1' or user_rating == '2' or user_rating == '3' or user_rating == '4' or user_rating == '5'):
                data = [[user_login['username'], choice, int(user_rating)]]

                new_data = pd.DataFrame(data, columns=header)
                new_data.to_csv('rating.csv', mode='a', sep=';',header=False, index=False)

                new_data_rating = pd.read_csv('rating.csv', sep=';')

                # simpan data rating di data bank sampah
                data_dipilih = bank_sampah.iloc[int(choice)]
                
                filtered_rating = new_data_rating[new_data_rating['id_bank'] == int(choice)]

                if(not filtered_rating.empty):
                    avg_rating = filtered_rating['rating'].mean()
                    f_avg_rating = f'{avg_rating:,.1f}'

                bank_sampah.loc[int(choice), ['nama bank sampah', 'nama pengelola', 'lokasi', 'kontak pengelola', 'harga sampah organik', 'harga sampah non-organik', 'rating']] = [data_dipilih['nama bank sampah'],  data_dipilih['nama pengelola'], data_dipilih['lokasi'], data_dipilih['kontak pengelola'], data_dipilih['harga sampah organik'], data_dipilih['harga sampah non-organik'], float(f_avg_rating)]
                bank_sampah.to_csv('data_bank_sampah.csv', index=False, sep=';')

                print(f'Terimakasih telah memberi penilaian untuk {bank_sampah['nama bank sampah'][int(choice)]}!')
                if(auth['auth'] == 'admin'):
                    choiceAdmin()
                elif(auth['auth'] == 'user'):
                    choiceUser()
            else:
                print('\nSilakan rating bank sampah dari 1 sampai 5!')
                rating()

    else:
        print('\nSilakan pilih opsi yang tersedia!')
        rating()


def search():
    bank_sampah = pd.read_csv('data_bank_sampah.csv', sep=';', dtype={'kontak pengelola': str})

    print('\n' + 30 * '=')
    choice = input('\n[1]Nama Bank Sampah\n[2]Nama Pengelola Bank Sampah\n[3]Lokasi Bank Sampah\n[4]Harga Sampah Organik\n[5]Harga Sampah Non Organik\n[6]Kembali\nCari Bank Sampah berdasarkan kategori: ')

    if(choice == '1'):
        nama_bank = input('Masukkan nama bank sampah yang ingin dicari (q untuk quit): ')

        if(nama_bank == 'q'):
            if(auth['auth'] == 'admin'):
                choiceAdmin()
            elif(auth['auth'] == 'user'):
                choiceUser()
            elif(auth['auth'] == 'pengelola'):
                choicePengelola()
        elif(nama_bank.replace(' ', '') == ''):
            print('\nInput pencarian tidak boleh kosong!')
            search()
        else:
            data_bank = bank_sampah[bank_sampah['nama bank sampah'].str.contains(nama_bank, case=False, na=False)]

            if not data_bank.empty:
                print('\n')
                print(data_bank)
                search()
            else:
                print("\nTidak ada hasil yang mendekati nama bank sampah tersebut.")
                search()
    elif(choice == '2'):
        nama_pengelola = input('Masukkan nama pengelola bank sampah yang ingin dicari (q untuk quit): ')

        if(nama_pengelola == 'q'):
            if(auth['auth'] == 'admin'):
                choiceAdmin()
            elif(auth['auth'] == 'user'):
                choiceUser()
            elif(auth['auth'] == 'pengelola'):
                choicePengelola()
        elif(nama_pengelola.replace(' ', '') == ''):
            print('\nInput pencarian tidak boleh kosong!')
            search()
        else:
            data_bank = bank_sampah[bank_sampah['nama pengelola'].str.contains(nama_pengelola, case=False, na=False)]

            if not data_bank.empty:
                print('\n')
                print(data_bank)
                search()
            else:
                print("\nTidak ada hasil yang mendekati nama pengelola bank sampah tersebut.")
                search()
    elif(choice == '3'):
        lokasi = input('Masukkan lokasi bank sampah yang ingin dicari (q untuk quit): ')

        if(lokasi == 'q'):
            if(auth['auth'] == 'admin'):
                choiceAdmin()
            elif(auth['auth'] == 'user'):
                choiceUser()
            elif(auth['auth'] == 'pengelola'):
                choicePengelola()
        elif(lokasi.replace(' ', '') == ''):
            print('\nInput pencarian tidak boleh kosong!')
            search()
        else:
            data_bank = bank_sampah[bank_sampah['lokasi'].str.contains(lokasi, case=False, na=False)]

            if not data_bank.empty:
                print('\n')
                print(data_bank)
                search()
            else:
                print("\nTidak ada hasil yang mendekati lokasi bank sampah tersebut.")
                search()
    elif(choice == '4'):
        harga_organik = input('Masukkan harga sampah organik yang ingin dicari (q untuk quit): ')

        if(harga_organik == 'q'):
            if(auth['auth'] == 'admin'):
                choiceAdmin()
            elif(auth['auth'] == 'user'):
                choiceUser()
            elif(auth['auth'] == 'pengelola'):
                choicePengelola()
        elif(harga_organik.replace(' ', '') == ''):
            print('\nInput pencarian tidak boleh kosong!')
            search()
        elif(not re.match(r'^\d+$', harga_organik)):
            print('\nPencarian harga organik hanya boleh menginputkan angka saja!')
            search()
        else:
            data_bank = bank_sampah[bank_sampah['harga sampah organik'] <= int(harga_organik)]

            if not data_bank.empty:
                print('\n')
                print(data_bank)
                search()
            else:
                print("\nTidak ada hasil yang mendekati harga sampah tersebut.")
                search()
    elif(choice == '5'):
        harga_non_organik = input('Masukkan harga sampah non organik yang ingin dicari (q untuk quit): ')

        if(harga_non_organik == 'q'):
            if(auth['auth'] == 'admin'):
                choiceAdmin()
            elif(auth['auth'] == 'user'):
                choiceUser()
            elif(auth['auth'] == 'pengelola'):
                choicePengelola()
        elif(harga_non_organik.replace(' ', '') == ''):
            print('\nInput pencarian tidak boleh kosong!')
            search()
        elif(not re.match(r'^\d+$', harga_non_organik)):
            print('\nPencarian harga non organik hanya boleh menginputkan angka saja!')
            search()
        else:
            data_bank = bank_sampah[bank_sampah['harga sampah non-organik'] <= int(harga_non_organik)]
            
            if not data_bank.empty:
                print('\n')
                print(data_bank)
                search()
            else:
                print("\nTidak ada hasil yang mendekati harga sampah tersebut.")
                search()
    elif(choice == '6'):
        if(auth['auth'] == 'admin'):
            choiceAdmin()
        elif(auth['auth'] == 'user'):
            choiceUser()
        elif(auth['auth'] == 'pengelola'):
            choicePengelola()
    else:
        print('\nSilakan pilih kategori berdasarkan angka yang tersedia!')
        search()

def crud():
    bank_sampah = pd.read_csv('data_bank_sampah.csv', sep=';', dtype={'kontak pengelola': str})
    header = ['nama bank sampah', 'nama pengelola', 'lokasi', 'kontak pengelola', 'harga sampah organik', 'harga sampah non-organik', 'rating']

    print('\n' + 30 * '=')
    choice = input('\n[1]Tambah data bank sampah\n[2]Lihat data bank sampah\n[3]Update data bank sampah\n[4]Hapus data bank sampah\n[5]Kembali\nSilakan pilih fitur berdasarkan angka: ')

    if(choice == '1'):
        nama_bank = input('\nMasukan nama bank sampah: ')
        nama_pengelola = input('Masukkan nama pengelola: ')
        lokasi = input('Masukkan lokasi bank sampah: ')
        kontak = input('Masukkan kontak pengelola bank sampah: ')
        organik = input('Masukkan harga sampah organik: ')
        non_organik = input('Masukkan harga sampah non organik: ')
        rating = 0

        # regex docs : https://docs.python.org/3/howto/regex.html

        if(str(nama_bank).replace(' ', '') == ''):
            print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
            kelolaBank()
        elif(str(nama_pengelola).replace(' ', '' == '')):
            print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
            kelolaBank()
        elif(str(lokasi).replace(' ', '') == ''):
            print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
            kelolaBank()
        elif(str(kontak).replace(' ', '') == ''):
            print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
            kelolaBank()
        elif(str(organik).replace(' ', '') == ''):
            print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
            kelolaBank()
        elif(str(non_organik).replace(' ', '') == ''):
            print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
            kelolaBank()
        elif(not re.match(r'^[a-zA-Z\s]{3,20}$', nama_bank)):
            print('\nNama bank sampah hanya boleh berisi huruf dan spasi! Minimal 3 huruf, maximal 20 huruf!')
            crud()
        elif(not re.match(r'^[a-zA-Z\s]{3,20}$', nama_pengelola)):
            print('\nNama pengelola hanya boleh berisi huruf dan spasi! Minimal 3 huruf!, maximal 20 huruf')
            crud()
        elif(not re.match(r'^(?=(?:[^a-zA-Z]*[a-zA-Z]){3})[a-zA-Z0-9\s,\.(\)]{10,255}$', lokasi)):
            print('\nLokasi hanya boleh berisi huruf, spasi, angka, koma dan tanda kurung, setidaknya memiliki 3 huruf! Minimal 10 karakter!')
            crud()
        elif(not re.match(r'^\d{7,15}$', kontak)):
            print('\nKontak hanya boleh berisi angka, minimal berisi 7 angka dan maksimal 15 angka!')
            crud()
        elif(not re.match(r'^\d{4,7}$', organik)):
            print('\nHarga sampah hanya boleh berisi angka, minimal 4 angka!')
            crud()
        elif(not re.match(r'^\d{4,7}$', non_organik)):
            print('\nHarga sampah hanya boleh berisi angka, minimal 4 angka!')
            crud()
        elif(not re.match(r'^[1-9][0-9]*$', organik)):
            print('\nHarga sampah tidak boleh didahului angka 0! Harap masukkan harga dengan benar!')
            crud()
        elif(not re.match(r'^[1-9][0-9]*$', non_organik)):
            print('\nHarga sampah tidak boleh didahului angka 0! Harap masukkan harga dengan benar!')
            crud()

        data = [[nama_bank, nama_pengelola, lokasi, f'{kontak}', organik, non_organik, rating]]

        new_data =  pd.DataFrame(data, columns=header)
        new_data.to_csv('data_bank_sampah.csv', mode='a', sep=';', header=False, index=False)

        print('\nData bank sampah berhasil dibuat!!!')
        crud()
    elif(choice == '2'):
        print(bank_sampah)
        crud()
    elif(choice == '3'):
        print('\n')
        print(bank_sampah)
        selected_bank = input('\nPilih bank sampah yang ingin di update berdasarkan nomor bank sampah (q jika tidak ada): ')

        if(selected_bank.lower() == 'q'):
            crud()
        elif(selected_bank.replace(' ', '') == ''):
            print('\nNomor bank sampah tidak boleh kosong!')
            crud()
        elif(not re.match(r'^\d+$', selected_bank)):
            print('\nSilakan isi menggunakan angka!')
            crud()
        elif(int(selected_bank) in bank_sampah.index):
            data_dipilih = bank_sampah.iloc[int(selected_bank)]

            nama_bank = data_dipilih['nama bank sampah']
            nama_pengelola = data_dipilih['nama pengelola']
            lokasi = data_dipilih['lokasi']
            kontak = data_dipilih['kontak pengelola']
            harga_organik = data_dipilih['harga sampah organik']
            harga_non_organik = data_dipilih['harga sampah non-organik']
            rating = data_dipilih['rating']

            print('\nSilakan isi data terbaru, kosongkan jika tidak ada perubahan')
            new_nama_bank = input(f'Masukkan nama bank sampah baru ({nama_bank}): ') or nama_bank
            new_nama_pengelola = input(f'Masukkan nama pengelola baru ({nama_pengelola}): ') or nama_pengelola
            new_lokasi = input(f'Masukkan lokasi bank sampah baru ({lokasi}): ') or lokasi
            new_kontak = input(f'Masukkan kontak baru pengelola bank sampah ({kontak}): ') or kontak
            new_harga_organik = input(f'Masukkan harga baru sampah organik ({harga_organik}): ') or harga_organik
            new_harga_non_organik = input(f'Masukkan harga baru sampah non organik ({harga_non_organik}): ') or harga_non_organik

            if(str(new_nama_bank).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            if(str(new_nama_pengelola).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            elif(str(new_lokasi).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            elif(str(new_kontak).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            elif(str(new_harga_organik).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            elif(str(new_harga_non_organik).replace(' ', '') == ''):
                print('\nInput tidak boleh kosong atau spasi saja! Mohon input data dengan benar!')
                kelolaBank()
            elif(not re.match(r'^[a-zA-Z\s]{3,20}$', new_nama_bank)):
                print('\nNama bank sampah hanya boleh berisi huruf dan spasi! Minimal 3 huruf, maximal 20 huruf!')
                crud()
            elif(not re.match(r'^[a-zA-Z\s]{3,20}$', new_nama_pengelola)):
                print('\nNama pengelola hanya boleh berisi huruf dan spasi! Minimal 3 huruf, maximal 20 huruf!')
                crud()
            elif(not re.match(r'^(?=(?:[^a-zA-Z]*[a-zA-Z]){3})[a-zA-Z0-9\s,\.(\)]{10,255}$', new_lokasi)):
                print('\nLokasi hanya boleh berisi huruf, spasi, angka, koma, spasi dan tanda kurung, setidaknya memiliki 3 huruf! Minimal 10 karakter!')
                crud()
            elif(not re.match(r'^\d{7,15}$', str(new_kontak))):
                print('\nKontak hanya boleh berisi angka, minimal berisi 7 angka dan maksimal 15 angka!')
                crud()
            elif(not re.match(r'^\d{4,7}$', str(new_harga_organik))):
                print('\nHarga sampah hanya boleh berisi angka, minimal 4 angka!')
                crud()
            elif(not re.match(r'^\d{4,7}$', str(new_harga_non_organik))):
                print('\nHarga sampah hanya boleh berisi angka, minimal 4 angka!')
                crud()
            elif(not re.match(r'^[1-9][0-9]*$', str(new_harga_organik))):
                print('\nHarga sampah tidak boleh didahului angka 0! Harap masukkan harga dengan benar!')
                crud()
            elif(not re.match(r'^[1-9][0-9]*$', str(new_harga_non_organik))):
                print('\nHarga sampah tidak boleh didahului angka 0! Harap masukkan harga dengan benar!')
                crud()

            bank_sampah.loc[int(selected_bank), ['nama bank sampah', 'nama pengelola', 'lokasi', 'kontak pengelola', 'harga sampah organik', 'harga sampah non-organik', 'rating']] = [new_nama_bank, new_nama_pengelola, new_lokasi, new_kontak, new_harga_organik, new_harga_non_organik, rating]

            bank_sampah.to_csv('data_bank_sampah.csv', index=False, sep=';')

            print('\nData bank sampah berhasil diperbarui!!!')
            crud()
        else:
            print('\nData belum ada, silakan masukkan data dengan benar!')
            crud()
    elif(choice == '4'):
        print('\n')
        print(bank_sampah)
        print('\n')
        delete_index = input('Pilih nomor bank sampah yang ingin dihapus (q jika tidak ada): ')

        if(delete_index.lower() == 'q'):
            crud()
        elif(delete_index.replace(' ', '') == ''):
            print('Nomor bank sampah tidak boleh kosong!')
            crud()
        elif(not re.match(r'^\d+$', delete_index)):
            print('Silakan isi menggunakan angka!')
            crud()
        elif(int(delete_index) in bank_sampah):
            delete_bank_sampah = bank_sampah.drop(index=int(delete_index))
            delete_bank_sampah.to_csv('data_bank_sampah.csv', sep=';', index=False)
            print('\n' + 'Data bank sampah berhasil dihapus!!!')
            crud()
        else:
            print('Tidak ada data bank sampah! Silakan pilih nomor bank sampah yang sesuai!')
            crud()
    elif(choice == '5'):
        if(auth['auth'] == 'admin'):
            choiceAdmin()
        elif(auth['auth'] == 'pengelola'):
            choicePengelola()


def ecoscalc():
    bank_sampah = pd.read_csv('data_bank_sampah.csv', sep=';', dtype={'kontak pengelola': str})

    print('\n' + 30 * '=')
    print(bank_sampah)
    selected_bank = input('\nPilih bank sampah berdasarkan nomor bank sampah (q jika tidak ada): ')

    if(selected_bank.lower() == 'q'):
        if(auth['auth'] == 'admin'):
            choiceAdmin()
        elif(auth['auth'] == 'user'):
            choiceUser()
        elif(auth['auth'] == 'pengelola'):
            choicePengelola()
    elif(selected_bank.replace(' ', '') == ''):
        print('Nomor bank sampah tidak boleh kosong!')
        ecoscalc()
    elif(not re.match(r'^\d+$', selected_bank)):
        print('\nSilakan pilih bank sampah menggunakan angka!')
        ecoscalc()
    elif(int(selected_bank) in bank_sampah.index):
        data_dipilih = bank_sampah.iloc[int(selected_bank)]
        
        harga_organik = data_dipilih['harga sampah organik']
        harga_non_organik = data_dipilih['harga sampah non-organik']

        input_organik = input('\nMasukkan berat sampah organik(kg): ')
        input_non_organik = input('Masukkan berat sampah non-organik(kg): ')

        if(input_organik.replace(' ', '') == ''):
            print('\nBerat sampah organik tidak boleh kosong!')
            ecoscalc()
        elif(input_non_organik.replace(' ', '') == ''):
            print('\nBerat sampah non organik tidak boleh kosong!')
            ecoscalc()
        elif(not re.match(r'^\d{1,3}$', input_organik)):
            print('\nHarga sampah organik hanya boleh berisi angka! Maximal 3 digit!')
            ecoscalc()
        elif(not re.match(r'^\d{1,3}$', input_non_organik)):
            print('\nHarga sampah non organik hanya boleh berisi angka! Maximal 3 digit!')
            ecoscalc()
        elif(not re.match(r'^[1-9][0-9]*$', input_organik)):
            print('Harga sampah tidak boleh didahului angka 0! Harap masukkan harga dengan benar!')
            ecoscalc()
        elif(not re.match(r'^[1-9][0-9]*$', input_non_organik)):
            print('Harga sampah tidak boleh didahului angka 0! Harap masukkan harga dengan benar!')
            ecoscalc()

        print(f'\nTotal harga sampah organik anda adalah Rp.{int(harga_organik) * int(input_organik):,.0f}')
        print(f'Total harga sampah non-organik anda adalah Rp.{int(harga_non_organik) * int(input_non_organik):,.0f}')

        next_step = input('\n[1]Ya\n[2]Tidak\nApakah anda ingin menghitung lagi? ')

        if(next_step.replace(' ', '') == ''):
            print('\nInput tidak boleh kosong!')
            ecoscalc()
        elif(next_step == '1'):
            ecoscalc()
        elif(next_step == '2'):
            if(auth['auth'] == 'admin'):
                choiceAdmin()
            elif(auth['auth'] == 'user'):
                choiceUser()
            elif(auth['auth'] == 'pengelola'):
                choicePengelola()
        else:
            print('\nSilakan pilih berdasarkan pilihan yang tersedia!')

    else:
        print('\nData bank sampah belum ada, silakan masukkan data dengan benar!')
        ecoscalc()


# ! CHOICE START


def choiceAdmin():
    print('\n' + 30 * '=')
    choice = input('\n[1]EcosCalc\n[2]CRUD Bank Sampah\n[3]Search Bank Sampah\n[4]Rating Bank Sampah\n[5]Logout\n[6]Exit\nSilakan pilih fitur berdasarkan angka: ')

    if(choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6'):
        if(int(choice) == 1):
            ecoscalc()
        elif(int(choice) == 2):
            crud()
        elif(int(choice) == 3):
            search()
        elif(int(choice) == 4):
            rating()
        elif(int(choice) == 5):
            print('\nLogout berhasil!!!')
            login()
        elif(int(choice) == 6):
            print('\n' + 30 * '=')
            print('\nTerimakasih telah menggunakan EcoSphera!\n')
            exit()
    else:
        print('\nSilakan pilih berdasarkan angka atau pilihan yang tersedia')
        choiceAdmin()


def choiceUser():
    bank_sampah = pd.read_csv('data_bank_sampah.csv', sep=';')

    print('\n' + 30 * '=')
    choice = input('\n[1]EcosCalc\n[2]Lihat Bank Sampah\n[3]Search Bank Sampah\n[4]Rating Bank Sampah\n[5]Logout\n[6]Exit\nSilakan pilih fitur berdasarkan angka: ')

    if(choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6'):
        if(int(choice) == 1):
            ecoscalc()
        elif(int(choice) == 2):
            print('\n', bank_sampah)
            choiceUser()
        elif(int(choice) == 3):
            search()
        elif(int(choice) == 4):
            rating()
        elif(int(choice) == 5):
            login()
        elif(int(choice) == 6):
            print('\n' + 30 * '=')
            print('\nTerimakasih telah menggunakan EcoSphera!\n')
            exit()
    else:
        print('\nSilakan pilih berdasarkan angka atau pilihan yang tersedia')
        choiceUser()


def choicePengelola():
    bank_sampah = pd.read_csv('data_bank_sampah.csv', sep=';')

    print('\n' + 30 * '=')
    choice = input('\n[1]EcosCalc\n[2]Kelola Bank Sampah\n[3]Lihat Bank Sampah\n[4]Search Bank Sampah\n[5]Logout\n[6]Exit\nSilakan pilih fitur berdasarkan angka: ')

    if(choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6'):
        if(int(choice) == 1):
            ecoscalc()
        elif(int(choice) == 2):
            kelolaBank()
        elif(int(choice) == 3):
            print('\n', bank_sampah)
            choicePengelola()
        elif(int(choice) == 4):
            search()
        elif(int(choice) == 5):
            print('\nLogout berhasil!!!')
            login()
        elif(int(choice) == 6):
            print('\n' + 30 * '=')
            print('\nTerimakasih telah menggunakan EcoSphera!\n')
            exit()
    else:
        print('\nSilakan pilih berdasarkan angka atau pilihan yang tersedia')
        choiceAdmin()


# ! CHOICE END

chance = {'chance': 2}


def login():
    users = pd.read_csv('users.csv', sep=';')

    print('\n' + 30 * '=')

    print('\nSilakan masuk ke akun anda!\n')
    uname = input('Masukkan username: ')
    pw = input('Masukkan password: ')

    validate = users[(users['username'] == uname) & (users['password'] == pw)]

    if(chance['chance'] == 0):
        chance['chance'] = 2
        choice1()
    elif(uname.replace(' ', '') == '' or pw.replace(' ', '') == ''):
        print(f'\nUsername atau password tidak boleh kosong! Silakan coba lagi! Kesempatan anda {chance['chance']}x lagi!')
        chance['chance'] -= 1
        login()
    else:
        if(not validate.empty):
            print('\n' + 30 * '=')
            print('\nLogin berhasil!!!')

            chance['chance'] = 2
            role = validate.iloc[0]['role']

            user_login['username'] = uname

            if(role == 'admin'):
                auth['auth'] = 'admin'
                choiceAdmin()
            elif(role == 'user'):
                auth['auth'] = 'user'
                choiceUser()
            elif(role == 'pengelola'):
                auth['auth'] = 'pengelola'
                choicePengelola()
            else:
                print('laahh siapa dong ini')
        else:
            print(f'\nUsername atau password salah! Silakan coba lagi! Kesempatan anda {chance['chance']}x lagi!')
            chance['chance'] -= 1
            login()


def register():
    users = pd.read_csv('users.csv', sep=';')

    print('\n' + 30 * '=')

    regisChoice = input('\n[1]User\n[2]Pengelola\n[3]Kembali\n[4]Exit\nSilakan pilih register sebagai: ')

    if(regisChoice == '1' or regisChoice == '2'):
        def regis2():
            uname = input('\nMasukkan username: ')
            pw = input('Masukkan password: ')
            
            notUnique = users[(users['username'] == uname)]
            if(chance['chance'] == 0):
                chance['chance'] = 2
                choice1()
            elif(not notUnique.empty):
                print('\nUsername sudah terdaftar! Silakan pakai username baru!')
                chance['chance'] -= 1
                regis2()
            elif(uname.replace(' ', '') == '' or pw.replace(' ', '') == ''):
                print('\nUsername atau password tidak boleh kosong!')
                chance['chance'] -= 1
                regis2()
            elif(not re.match(r'^\w{3,20}$', uname)):
                print('\nUsername hanya boleh mengandung huruf, angka dan garis bawah! Minimal 3 karakter, Maximal 20 karakter!')
                chance['chance'] -= 1
                regis2()
            elif(not re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}', pw)):
                print('Password setidaknya mengandung huruf besar, huruf kecil dan angka! Minimal 8 karakter!')
                chance['chance'] -= 1
                regis2()
            else:
                header = ['username', 'password', 'role']

                if(int(regisChoice) == 1):
                    user = [[uname, pw, 'user']]
                elif(int(regisChoice) == 2):
                    user = [[uname, pw, 'pengelola']]

                new_user = pd.DataFrame(user, columns=header)
                new_user.to_csv('users.csv', mode='a', sep=';', header=False, index=False)

                print('\nSelamat akun anda telah berhasil dibuat!!! Silakan login terlebih dahulu!')
                chance['chance'] = 2
                login()
        regis2()
    elif(regisChoice == '3'):
        choice1()
    elif(regisChoice == '4'):
        print('\nTerimakasih telah menggunakan EcoSphera!\n')
        exit()
    else:
        print('\nSilakan pilih berdasarkan angka yang tersedia!!!')
        register()


def choice1():
    print('\n' + 30 * '=')
    print('Selamat Datang di EcoSphera!!!')
    
    choice = input('\n[1]Register\n[2]Login\n[3]Exit\nSilakan pilih Login atau Register: ')

    if(choice == '1' or choice == '2' or choice == '3'):
        if(int(choice) == 1):
            register()
        elif(int(choice) == 2):
            login()
        elif(int(choice) == 3):
            print('\nTerimakasih telah menggunakan EcoSphera!\n')
            exit()
    else:
        print('\nSilakan pilih opsi yang tersedia!')
        choice1()


choice1()