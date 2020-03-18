#stop and remove every docker containers 
#then remove all volumes to initialize and start the docker compose 

import os  
  
print('STOP CONTAINERS')
os.system('docker stop $(docker ps -a -q)') 

print('RM CONTAINERS')
os.system('docker rm $(docker ps -a -q)') 

print('RM VOLUMES')
os.system('docker volume prune -f')

print('INIT')
os.system('python3 initialisation.py')

print('START DOCKER COMPOSE')
os.system('docker-compose up -d')