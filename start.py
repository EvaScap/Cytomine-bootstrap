import os  
import time
#faire un verife de si le init pas fait --> lle faire (verif des  fichier sans .sample)

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
'configs/nginx/server-iipjp2.conf ',
'configs/nginx/server-ims.conf ',
'configs/nginx/server-iris.conf ',
'configs/nginx/server-retrieval.conf ',
'configs/software_router/config.groovy ',
'configs/web-ui/configuration.json ',
'utils/start.sh hosts/core/addHosts.sh ',
'hosts/ims/addHosts.sh ',
'hosts/retrieval/addHosts.sh ',
'hosts/iris/addHosts.sh ',
'hosts/software_router/addHosts.sh ',
'hosts/slurm/addHosts.sh', 
'hosts/project_migrator/addHosts.sh',
'docker-compose.yml',
'bioformat-deployment.yaml',
'core-deployment.yaml',
'iipcyto-deployment.yaml',
'iipjp2-deployment.yaml',
'ims-deployment.yaml',
'memcached-deployment.yaml',
'mongodb-deployment.yaml',
'nginx-deployment.yaml',
'postgresql-deployment.yaml',
'rabbitmq-deployment.yaml',
'webui-deployment.yaml',
'persistent_volume.yaml',
'persistent_volume2.yaml',
]

#start microk8s
os.system('sudo microk8s start')
#enable plugins
os.system(' microk8s enable dns storage ingress')
for file in FILES:
	if os.path.exists(file)!= True :
		print(file +"doesn't exist, files initialisation")
		#delete old files
		os.system('microk8s.kubectl delete -f persistant_volume.yaml -f db-postgres11-persistentvolumeclaim.yaml -f  postgresql-deployment.yaml -f postgresql_service.yaml -f persistant_volume2.yaml -f db-mongo-persistentvolumeclaim.yaml -f  mongodb-deployment.yaml -f mongodb_service.yaml -f rabbitmq-deployment.yaml -f rabbitmq_service.yaml -f webui-deployment.yaml -f webui_service.yaml -f nginx-deployment.yaml -f nginx_service.yaml -f core-deployment.yaml -f core_service.yaml -f localhost-core_service.yaml -f ims-deployment.yaml -f ims_service.yaml -f iipcyto-deployment.yaml -f iipcyto_service.yaml -f iipjp2-deployment.yaml -f iipjp2_service.yaml -f bioformat-deployment.yaml -f bioformat_service.yaml -f memcached-deployment.yaml -f memcached_service.yaml -f localhost_ims.yaml -f localhost_upload.yaml -f nginx-ingress.yaml')

		print('INIT')
		os.system('python3 initialisation.py')
		break
#Apply new files
os.system('microk8s.kubectl apply -f persistant_volume.yaml -f db-postgres11-persistentvolumeclaim.yaml -f  postgresql-deployment.yaml -f postgresql_service.yaml -f persistant_volume2.yaml -f db-mongo-persistentvolumeclaim.yaml -f  mongodb-deployment.yaml -f mongodb_service.yaml -f rabbitmq-deployment.yaml -f rabbitmq_service.yaml -f webui-deployment.yaml -f webui_service.yaml -f nginx-deployment.yaml -f nginx_service.yaml -f core-deployment.yaml -f core_service.yaml -f localhost-core_service.yaml -f ims-deployment.yaml -f ims_service.yaml -f iipcyto-deployment.yaml -f iipcyto_service.yaml -f iipjp2-deployment.yaml -f iipjp2_service.yaml -f bioformat-deployment.yaml -f bioformat_service.yaml -f memcached-deployment.yaml -f memcached_service.yaml -f localhost_ims.yaml -f localhost_upload.yaml -f nginx-ingress.yaml')
		


