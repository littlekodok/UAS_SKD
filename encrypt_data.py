from cryptography.fernet import Fernet
import rsa
# membuka file symmetric.key
skey = open('symmetric.key','rb')
key = skey.read()

# membuat cipher
cipher = Fernet(key)

# mmebuka file yang akan di enkripsi
myfile = open('logobatik.png', 'rb') #membuka file gambar yang akan di enkripsi
myfiledata= myfile.read() #membaca file gambar

# fungsi enkripsi
encrypted_data = cipher.encrypt(myfiledata) #proses enkripsi dengan menggunakan fungsi cipher.encrypt
edata = open('logobatik_enkrip.png', 'wb') #membuka gambar yang di enkripsi
edata.write(encrypted_data) #mencetak gambar ke dalam bentuk yang sudah dienkripsi dengan format png

print(encrypted_data) #mencetak hasil enkripsi ke terminal

# membuka public key
pkey = open('publickey.key','rb') #mmebuka public key
pkdata = pkey.read() #membaca public key

# load file
pubkey = rsa.PublicKey.load_pkcs1(pkdata)

# enkripsi symmetric key  dengan public key
encrypted_key = rsa.encrypt(key,pubkey)

ekey = open('kunci_enskripsi.txt','wb')
ekey.write(encrypted_key) # mencetak kunci enkripsi ke dalam bentuk txt

print(encrypted_key)  # mencetak hasil enkripsi ke terminal
