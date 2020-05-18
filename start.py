import os  
import time


FILES=[
'configs/core/cytomineconfig.groovy', 
'configs/ims/ims-config.groovy',
'configs/iipCyto/nginx.conf',
'configs/iipCyto/iip-configuration.sh', 
'configs/iipJP2/nginx.conf', 
'configs/iris/iris-config.groovy',
'configs/iris/iris-production-config.groovy',
'configs/nginx/nginx.conf' ,
'configs/nginx/server-core.conf' ,
'configs/nginx/server-iipjp2.conf',
'configs/nginx/server-ims.conf',
'configs/nginx/server-iris.conf',
'configs/nginx/server-retrieval.conf',
'configs/software_router/config.groovy',
'configs/web-ui/configuration.json',
'hosts/core/addHosts.sh',
'hosts/ims/addHosts.sh',
'hosts/retrieval/addHosts.sh',
'hosts/iris/addHosts.sh',
'hosts/software_router/addHosts.sh',
'hosts/slurm/addHosts.sh', 
'hosts/project_migrator/addHosts.sh',
'docker-compose.yml']

for file in FILES:
	if os.path.exists(file)!= True :
		print(file +"n'existe pas, initialisation des fichiers")
		
		print('RM VOLUMES')
		os.system('docker volume prune -f')

		print('INIT')
		os.system('python3 initialisation.py')

		break


os.system('docker-compose up -d')

