#!/bin/bash


export WORKON_HOME=/www/zzy/workspace
source /usr/bin/virtualenvwrapper.sh
workon env1-stock
echo "python getfunddata.py "
python /www/wwwroot/zzydownload.com/downfunddata/getfunddata.py

deactivate