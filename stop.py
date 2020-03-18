import os  
  
print('STOP CONTAINERS')
os.system('docker stop $(docker ps -a -q)') 

print('RM CONTAINERS')
os.system('docker rm $(docker ps -a -q)') 
