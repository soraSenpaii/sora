# Importar lib:
from tqdm import tqdm, trange
from time import sleep
import amino
import pyfiglet
import os

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# Feito por Luiz Eduardo.									   I
# Amino.py criada por Slimakoi™						 I
# Slimakoi™ todos os direitos reservados ® 	 I
#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Client responsável pela criação da conta:
client = amino.Client()

# Barra de progresso de inicialização:
os.system('clear')
print('\033[1;36m')
result = pyfiglet.figlet_format("Create\nAcc_sora", justify="center", width=60, font = "slant" )
print(result)
with tqdm(total = 100) as progressbar:
	for i in range(100):
		sleep(0.0)
		progressbar.update(1)
os.system('clear')

# Figlet/Banner inicial:
result = pyfiglet.figlet_format("Criador de contas", justify="center", width=60, font = "slant" )
print(result)
print('acc create by sora')
print('')

# Gerador de Deviceid:
device1 = amino.device.generate_device_info()['device_id']
client = amino.Client(deviceId=device1)
print(f'DeviceId Gerado >> {client.device_id}')
Device = input('DeviceId >> ')

# Sistema de mandar código para criar a conta:
email = input('Email  >> ')
client.request_verify_code(email=email)

# Sistema para criar as contas:
try:
	password = "ooo456ooo"
	verf = input('verification code >> ')
	client.register(nickname='Mr.X', email=email, password=password, verificationCode=verf, deviceId=Device)
except amino.exceptions.AccountLimitReached:
	print('هذا الديفايس ايدي قد بلغ الحد الاقصى لانشاء الحسابات قم باستبداله :)')

# Figlet de concluído:
os.system('clear')
result = pyfiglet.figlet_format("SORA", justify="center",width=60, font = "slant" )
print(result)
with tqdm(total = 100) as progressbar:
	for i in range(100):
		sleep(0.0)
		progressbar.update(1)
