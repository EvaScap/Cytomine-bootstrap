import json
import yaml 
from deepmerge import always_merger 
import re
import os.path
import shutil
import uuid



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
'docker-compose.yml']



# ------------------------------------------------
# ---------------FILES LIST & VAR-----------------
# ------------------------------------------------

KEY= 'Key.yml.sample'
LISTDICT=['configurationBase.yml', 'version.yml', 'Key.yml']



# -----------------------------------------
# -------------FONCTIONS-------------------
# -----------------------------------------

#opens the .yml file and saves it in a dictionary. 
#Return this dict
def OpenAndSave(file):
    with open(file) as yml_data:
        data_dict = yaml.load(yml_data,Loader=yaml.FullLoader)
    return(data_dict)
   

#replaces the keys with their respective value in a file
def replaceVar(dictFinal, fichier):
	string_server_list= ""
	for i in range (0,int(dictFinal['NB_IIP_PROCESS'])):
		string_server_list += '			server 127.0.0.1:900' +str(i) +';\n'
	with open(fichier) as temp:
		change = temp.read()
		for key in dictFinal: 

			change= re.sub('\\$'+key,dictFinal[key],change)
		change=re.sub('\\$IIP_PROCESS',string_server_list,change)
	temp.close()
	with open(fichier, 'w') as temp:
	    temp.write(change)


#creation of a dictionary based on the list of yml files
def CreateDict(LISTDICT):
	cmp=0
	for i in LISTDICT:
		dict1= OpenAndSave(i)
		if cmp==0:
			dictFinal=dict1

		dictFinal=always_merger.merge(dictFinal,dict1) 
		cmp+=1
	return dictFinal


#generates random keys for variables in a .sample file and creates the corresponding yml file
def GenerateKey(fileKey):
	dictKey= OpenAndSave(fileKey)
	for i in dictKey:
		dictKey[i] = str(uuid.uuid4())

	with open(fileKey[:-7] , 'w') as file:
		documents = yaml.dump(dictKey,file)




# --------------------------------------------------------------
# --------------------CREATION FINAL DICT-----------------------
# ------------------------ + SAVE ------------------------------
#---------------------------------------------------------------
print("INITIALIZATION")
print("Generating random keys")
GenerateKey(KEY)

dictFinal=CreateDict(LISTDICT) 
print("Saving variables in the file configuration.env")
with open('configuration.env' , 'w') as file:
	documents = yaml.dump(dictFinal,file) 

	

# --------------------------------------------------------------
# ---------------------LOOP TO REPLACE--------------------------
# --------------------------------------------------------------
print("Starting to generate the various files")
for i in FILES:
	if os.path.isfile(i+'.sample'):
		#copies the .sample file to create a filled file without losing the .sample
		shutil.copy(i+'.sample',i)
		replaceVar(dictFinal,i)
		

