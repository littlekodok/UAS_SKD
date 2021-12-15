import rsa
from cryptography.fernet import Fernet

# load private key untuk mendekripsi public key
prkey = open('privkey.key','rb') # membuka file pivate key 
pkey = prkey.read() #file akan di baca
private_key = rsa.PrivateKey.load_pkcs1(pkey) #proses dej

e = open('kunci_enskripsi.txt', 'rb') #membuka file kunci_enskripsi.txt
ekey = e.read()  #file kunci_enskripsi.txt akan di read

dpubkey = rsa.decrypt(ekey,private_key) # proses memanggil algoritma rsa dengan private key

cipher = Fernet(dpubkey) # memanggil library fernet untuk melakukan dekripsi

encrypted_data = open('logobatik_enkrip.png', 'rb') # membuka gambar hasil yang di enkripsi
edata = encrypted_data.read()


decrypted_data = cipher.decrypt(edata) #proses dekripsi

# mmebuat file baru dari hasil dekripsi
edata = open('logobatik_dekrip.png', 'wb')  
edata.write(decrypted_data) # membuat file hasl dekripsi dengan format .png
edata.close()
#



