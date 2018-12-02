import requests
import numpy as np
import random
import time
import os
import re
#*************************************************************************************************
kv={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0'}
ips=[]
path=os.getcwd().replace('\\','/')+'/ip.txt'
with open(path,'r') as f:
    for ip in f:
        ips.append(ip.strip('\n'))
f.close()
#------------------------------------------------------------------------------------------------
stru=[]
path=os.getcwd().replace('\\','/')+'/pdblist'
with open(path,'r') as f:
    for structure in f:
        stru.append(structure.strip('\n'))
f.close()
#------------------------------------------------------------------------------------------------
i=0
for structure in stru:
    try:
        pdbUrl = 'https://files.rcsb.org/download/'+structure[:4]+'.pdb'
        try:
            r0=requests.get(pdbUrl,headers=kv,proxies={'http':'http://'+ips[i]},timeout=60)
        except:
            r0=requests.get(pdbUrl,headers=kv,proxies={'https':'https://'+ips[i]},timeout=60)
        r0.raise_for_status()
        data = r0.content
        with open(structure+'.pdb','wb') as f:
            f.write(data)
            f.close()                
            print('Downloading {} as {}.'.format(structure[:4], structure))
        if i >= len(ips):
            i=0
        else:
            i+=1
    except:
        print(structure+'error')
        pass
print('*****over*****')
