import ftplib
import telegram_send
import datetime 


ftp = ftplib.FTP("kscftpserv.ksc.local")
ftp.login("1csynctvzkscuser", "Gb43#gbw2")

ftp.cwd('TVZ_KCK')
files = []
with open("/home/abonin/ftp/file_list.txt", "r") as myfile:
    file_list =myfile.read() 
date = datetime.datetime.now().strftime("%y%m%d")
#date = '211022'
#print(date)
try:
    files = ftp.nlst()
except ftplib.error_perm as resp:
    if str(resp) == "550 No files found":
        print ("No files in this directory")
    else:
        raise

for f in files:
    if (f.find(date)>=0 and file_list.find(f)<0):
       with open("/home/abonin/ftp/file_list.txt", "a") as myfile:
           myfile.write(f'{f} \n')
       text = [f'Найден новый файл {f}']
       telegram_send.send(messages=text)
       # print (f)
