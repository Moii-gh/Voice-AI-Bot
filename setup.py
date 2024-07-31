import os

if os.name == 'nt':
  os.system('python.exe -m pip install --upgrade pip')
  os.system('python.exe -m pip install -r requirements.txt')
elif os.name == 'posix':
  os.system('pip install --upgrade pip')
  os.system('pip install -r requirements.txt')
 
print('\033c\033[HVoice Bot\nAuthor: @moii-gh\n')


#Навсякий случай

#if os.name == 'nt':
#os.system('python.exe -m pip install --telebot')
#os.system('python.exe -m pip install --requests')
#os.system('python.exe -m pip install --json')
#os.system('python.exe -m pip install --numpy')
#os.system('python.exe -m pip install --soundfile')
#os.system('python.exe -m pip install --speech_recognition


#elif os.name == 'posix':
#os.system('pip install --telebot)
#os.system('pip install --requests)
#os.system('pip install --json)
#os.system('pip install --numpy)
#os.system('pip install --soundfile)
#os.system('pip install --speech_recognition)