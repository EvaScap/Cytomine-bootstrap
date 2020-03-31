import json
import yaml #pip3 install pyYaml
from deepmerge import always_merger #pip3 install deepmerge
import re
import os.path
import shutil
import uuid


#ce sont les fichiers a remplir avec le dictionnaire


FILES=[
'configs/core/cytomineconfig.groovy', 
'configs/ims/ims-config.groovy',
'configs/iipCyto/nginx.conf.sample',
'configs/iipCyto/iip-configuration.sh', 
'configs/iipJP2/nginx.conf.sample', 
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

#meme liste qu'avant + le docker-compose qu'il faut remplir a la place du start






# ------------------------------------------------
# ---------------FILES LIST & VAR-----------------
# ------------------------------------------------

KEY= 'Key.yml.sample'
#FILES=['coucou.conf', 'cirque.yml', 'docker-compose.yml']
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
   


#replace the keys with their respective value in a file
def replaceVar(dictFinal, fichier):
	with open(fichier) as temp:
		change = temp.read()
		for key in dictFinal: 

			change= re.sub('\\$'+key,dictFinal[key],change)
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

		dictFinal=always_merger.merge(dictFinal,dict1) #si on a qu'un dico il va merger deux les meme on s'en fout
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
		#copy the .sample file to create a filled file without losing the .sample
		shutil.copy(i+'.sample',i)
		replaceVar(dictFinal,i)
		

