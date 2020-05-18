

import os  
os.system('microk8s start')  

os.system('microk8s.kubectl delete -f persistant_volume.yaml -f db-postgres11-persistentvolumeclaim.yaml -f  postgresql-deployment.yaml -f postgresql_service.yaml -f persistant_volume2.yaml -f db-mongo-persistentvolumeclaim.yaml -f  mongodb-deployment.yaml -f mongodb_service.yaml -f rabbitmq-deployment.yaml -f rabbitmq_service.yaml -f webui-deployment.yaml -f webui_service.yaml -f nginx-deployment.yaml -f nginx_service.yaml -f core-deployment.yaml -f core_service.yaml -f localhost-core_service.yaml -f ims-deployment.yaml -f ims_service.yaml -f iipcyto-deployment.yaml -f iipcyto_service.yaml -f iipjp2-deployment.yaml -f iipjp2_service.yaml -f bioformat-deployment.yaml -f bioformat_service.yaml -f memcached-deployment.yaml -f memcached_service.yaml -f localhost_ims.yaml -f localhost_upload.yaml -f nginx-ingress.yaml') 


os.system('python3 initialisation.py')


os.system('microk8s.kubectl apply -f persistant_volume.yaml -f db-postgres11-persistentvolumeclaim.yaml -f  postgresql-deployment.yaml -f postgresql_service.yaml -f persistant_volume2.yaml -f db-mongo-persistentvolumeclaim.yaml -f  mongodb-deployment.yaml -f mongodb_service.yaml -f rabbitmq-deployment.yaml -f rabbitmq_service.yaml -f webui-deployment.yaml -f webui_service.yaml -f nginx-deployment.yaml -f nginx_service.yaml -f core-deployment.yaml -f core_service.yaml -f localhost-core_service.yaml -f ims-deployment.yaml -f ims_service.yaml -f iipcyto-deployment.yaml -f iipcyto_service.yaml -f iipjp2-deployment.yaml -f iipjp2_service.yaml -f bioformat-deployment.yaml -f bioformat_service.yaml -f memcached-deployment.yaml -f memcached_service.yaml -f localhost_ims.yaml -f localhost_upload.yaml -f nginx-ingress.yaml')
