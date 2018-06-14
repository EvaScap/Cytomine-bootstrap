#
# Copyright (c) 2009-2017. Authors: see NOTICE file.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#URLs
CORE_URL=localhost-core
IMS_URLS="[localhost-ims,localhost-ims2]"
UPLOAD_URL=localhost-upload

#Backups
# BACKUP_BOOL : backup active or not
BACKUP_BOOL=false
# SENDER_EMAIL, SENDER_EMAIL_PASS, SENDER_EMAIL_SMTP : email params of the sending account
SENDER_EMAIL='your.email@gmail.com'
SENDER_EMAIL_PASS='passwd'
SENDER_EMAIL_SMTP_HOST='smtp.gmail.com'
SENDER_EMAIL_SMTP_PORT='587'
# RECEIVER_EMAIL : email adress of the receiver
RECEIVER_EMAIL='receiver@XXX.com'

#Paths
IMS_STORAGE_PATH=/data
IMS_BUFFER_PATH=/data/_buffer
BACKUP_PATH=/data/backup
ALGO_PATH=/data/algo/
RETRIEVAL_PATH=/data/thumb
FAST_DATA_PATH=/data

#middlewares
RETRIEVAL_PASSWD='retrieval_default'
RABBITMQ_LOGIN="router"
RABBITMQ_PASSWORD="router"


#IRIS
IRIS_ENABLED=true
IRIS_URL=localhost-iris
IRIS_ID="LOCAL_CYTOMINE_IRIS"
IRIS_ADMIN_NAME="Ian Admin"
IRIS_ADMIN_ORGANIZATION_NAME="University of Somewhere, Department of Whatever"
IRIS_ADMIN_EMAIL="ian.admin@somewhere.edu"


# You don't to change the datas below this line instead of advanced customization
# ---------------------------

IS_LOCAL=true

#IIP_OFF_URL=localhost-iip-base
IIP_CYTO_URL=localhost-iip-cyto
IIP_JP2_URL=localhost-iip-jp2000
NB_IIP_PROCESS=20

RETRIEVAL_URL=localhost-retrieval

BIOFORMAT_ENABLED="true"

#possible values : memory, redis
RETRIEVAL_ENGINE=redis

MEMCACHED_PASS="mypass"

BIOFORMAT_ALIAS="bioformat"
BIOFORMAT_PORT="4321"


# DO NOT USE DATA BELOW EXCEPT YOU WANT TO INSTALL A DEVELOPMENT ENV.
DEV_CORE=true
DEV_IMS=false
# Complete the keys by running, for example $(cat /proc/sys/kernel/random/uuid) for each.
# For a production deployment, these keys are automatically generated !
IMS_PUB_KEY="DEF"
IMS_PRIV_KEY="ABC"
ADMIN_PUB_KEY="JKL"
ADMIN_PRIV_KEY="GHI"
SUPERADMIN_PUB_KEY="PQR"
SUPERADMIN_PRIV_KEY="MNO"
RABBITMQ_PUB_KEY="VWX"
RABBITMQ_PRIV_KEY="STU"
