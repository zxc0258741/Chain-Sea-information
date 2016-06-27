 #-*- coding: UTF-8 -*- 
import numpy as np
import scipy.io
import scipy.misc
import os

finaldic={}

def get_imlist(path):
  return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.npy')]
folder1=get_imlist('/home/lcw/下載/tensorflow/gabstractscene/')
folder2=get_imlist('/home/lcw/下載/tensorflow/gabstractman/')
folder3=get_imlist('/home/lcw/下載/tensorflow/photopool5/')
folder4=get_imlist('/home/lcw/下載/tensorflow/photomanpool5/')
pic=get_imlist('/home/lcw/下載/tensorflow/wikiartpool5/')


def build_style_loss(A, G):
  loss = np.sum((A-G)**2)
  #print loss
  #print  '---------'
  return loss

def get_classification(folder):
  dic={}
  for path in pic:
	cpool = np.load(path)#一次拿一張圖片
        a=path.split('/')[6].split('.')[0]
	for npypath in folder:
	  rh = np.load(npypath)
	  if a in dic:
	  	dic.update({a:dic[a]+build_style_loss(cpool,rh)})
	  else:
		dic.update({a:build_style_loss(cpool,rh)})
   
	     
  return dic		

a=get_classification(folder1)
b=get_classification(folder2)
c=get_classification(folder3)
d=get_classification(folder4)
#print a

for path in pic:
      name=path.split('/')[6].split('.')[0]
      finaldic.setdefault(name,[]).append(a[name]/10.5)#small
      finaldic.setdefault(name,[]).append(b[name]/7.4)
      finaldic.setdefault(name,[]).append(c[name]/18)
      finaldic.setdefault(name,[]).append(d[name]/24.8)#big
asortdict={}
bsortdict={}
csortdict={}
dsortdict={}

for item in pic:
  name=item.split('/')[6].split('.')[0]
  if finaldic[name].index(min(finaldic[name]))==0:
     asortdict.update({name:finaldic[name][finaldic[name].index(min(finaldic[name]))]})
  elif finaldic[name].index(min(finaldic[name]))==1:
     bsortdict.update({name:finaldic[name][finaldic[name].index(min(finaldic[name]))]})
  elif finaldic[name].index(min(finaldic[name]))==2:
     csortdict.update({name:finaldic[name][finaldic[name].index(min(finaldic[name]))]})
  else:
     dsortdict.update({name:finaldic[name][finaldic[name].index(min(finaldic[name]))]})

adict= sorted(asortdict.iteritems(), key=lambda d:d[1], reverse = True)
bdict= sorted(bsortdict.iteritems(), key=lambda d:d[1], reverse = True)
cdict= sorted(csortdict.iteritems(), key=lambda d:d[1], reverse = True)
ddict= sorted(dsortdict.iteritems(), key=lambda d:d[1], reverse = True)

writetext=''
for i,a in enumerate(adict):
 writetext+=a[0]+'|'+'AS'+'|'+str(a[1])+'\n'
writetext+='----------------abstractscene-----------------'+'\n'
for i,a in enumerate(bdict):
 writetext+=a[0]+'|'+'AM'+'|'+str(a[1])+'\n'
writetext+='----------------abstractman-------------------'+'\n'
for i,a in enumerate(cdict):
 writetext+=a[0]+'|'+'RS'+'|'+str(a[1])+'\n'
writetext+='----------------realscene---------------------'+'\n'
for i,a in enumerate(ddict):
 writetext+=a[0]+'|'+'RM'+'|'+str(a[1])+'\n'
writetext+='----------------realman-----------------------'+'\n'

with open('/home/lcw/下載/tensorflow/rank12.txt','w') as f:
  f.write(writetext)

#for item in pic:
 # name=item.split('/')[6].split('.')[0]
  #print name,finaldic[name]

#for item in pic:
 #  name=item.split('/')[6].split('.')[0]
  # sortdic.update({name:str(finaldic[name].index(min(finaldic[name])))+'.'+str(finaldic[name][finaldic[name].index(min(finaldic[name]))])})
   #print name,finaldic[name].index(min(finaldic[name])),finaldic[name][finaldic[name].index(min(finaldic[name]))]


#writetext=''
#dict= sorted(sortdic.iteritems(), key=lambda d:d[1], reverse = True)
#for a in dict:
#  writetext+=a[0]+','+a[1]+'\n'
#with open('/home/lcw/下載/tensorflow/classification.text','w') as f:
#  f.write(writetext)

  

    
#build_style_loss(c,d)
