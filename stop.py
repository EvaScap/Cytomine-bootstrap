import os  
  
print('STOP CONTAINERS')
os.system('docker-compose stop') 

print('RM CONTAINERS')
os.system('docker-compose rm -f') 
