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
LISTDICT=['configurationBase.yml', 'version.yml', KEY]



# -----------------------------------------
# -------------FONCTIONS-------------------
# -----------------------------------------

#saves a dict of dicts in env files. 
#These files have a name equals to the name of  a key (that is one dict too) and contain the dict associated.
def SaveDicoFileEnv(dico):
    for key in dico:
        print(key)
        f=open(key+".env", "w+")
        for key2 in dico[key]:
            f.write(str(key2)+'='+str(dico[key][key2])+'\n')
            print('\t'+str(key2)+'='+str(dico[key][key2]))
        f.close()


#opens the .yml file and saves it in a dictionary. 
#Return this dict
def OpenAndSave(file):
    with open(file) as yml_data:
        data_dict = yaml.load(yml_data,Loader=yaml.FullLoader)
    return(data_dict)
   


#replace the keys with their respective value in a file
def replaceVar(dictFinal, fichier):
	print(fichier +'TEEEEST')
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
		#dictKey[i]=dictKey[i].hex
		print(dictKey[i])

	with open(fileKey[:-7] , 'w') as file:
		documents = yaml.dump(dictKey,file)




# --------------------------------------------------------------
# --------------------CREATION FINAL DICT-----------------------
# ------------------------ + SAVE ------------------------------
#---------------------------------------------------------------

GenerateKey(KEY)

dictFinal=CreateDict(LISTDICT) 

with open('configuration.env' , 'w') as file:
	documents = yaml.dump(dictFinal,file) #on pourrait le faire un peu plus propre --> a voir

	

# --------------------------------------------------------------
# ---------------------LOOP TO REPLACE--------------------------
# --------------------------------------------------------------
for i in FILES:
	print("'"+i+".sample'") 
	if os.path.isfile(i+'.sample'):
		print('je retire le sample du fichier')

		#delete the file if it exists
		# if os.path.isfile(i):
		# 	os.remove(i)
		#--> pas besoin pcq si il existe je l'ecrase juste après

		#copy the .sample file to create a filled file without losing the .sample
		shutil.copy(i+'.sample',i)
		replaceVar(dictFinal,i)
		

