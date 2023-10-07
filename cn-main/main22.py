import json
import re
import subprocess
import shutil
import os
from concurrent.futures import ThreadPoolExecutor
import sys
params={}
for arg in sys.argv[1:]:
 if arg.startswith('--'):
  key_value=arg[len('--'):].split('=')
  if len(key_value)==2:
   key,value=key_value
   params[key]=value
check_dir=f"{params['dir']}/models/Stable-diffusion"
lora_dir=f"{params['dir']}/models/Lora"
def swap(arr,l,r):
 temp=arr[l]
 arr[l]=arr[r]
 arr[r]=temp
def checkRelateMod(oldMod,newMod):
 try:
  return oldMod and newMod and oldMod['downloadLink']==newMod['downloadLink']
 except Exception as e:
  print(e)
def sanitize_filename(filename):
 pattern=r'[\\/:*?"<>|]'
 sanitized_filename=re.sub(pattern,'_',filename)
 return sanitized_filename
def compatibility(preContent):
 for item in preContent:
  if bool(item['path']):
   item['path']=re.sub(r'^(/[^/]+/[^/]+)',params['dir'],item['path'])
def dealRelateMod(oldRenameMod,newRenameMod):
 old_file_path=f"{oldRenameMod['path']}/{oldRenameMod['name']}"
 new_file_dir=(newRenameMod['path']if newRenameMod.get('path')and newRenameMod['path']!="" else oldRenameMod['path'])
 new_file_name=(sanitize_filename(newRenameMod['name'])+os.path.splitext(oldRenameMod['name'])[1]if newRenameMod['name']and newRenameMod['name']!="未命名" else oldRenameMod['name'])
 new_file_path=f"{new_file_dir}/{new_file_name}"
 if old_file_path!=new_file_path:
  try:
   if os.path.exists(old_file_path):
    os.rename(old_file_path,new_file_path)
    oldRenameMod['path']=new_file_dir
    oldRenameMod['name']=new_file_name
    print(f"{old_file_path}更改为{new_file_path}成功")
   else:
    print(f"{old_file_path}不存在，重命名失败")
  except OSError as e:
   print(f"更改{old_file_path}时发生错误: {e}")
 else:
  print(f"{newRenameMod['name']}已存在且无任何改变，将忽视")
def deleteMod(oldDeMod):
 file_path=f"{oldDeMod['path']}/{oldDeMod['name']}"
 try:
  if os.path.exists(file_path):
   os.remove(file_path)
   print(f"{oldDeMod['name']}删除成功")
  else:
   print(f"{oldDeMod['name']}不存在，删除失败")
 except OSError as e:
  print(f"删除{oldDeMod['name']}时发生错误: {e}")
def LCS(oldCo,newCo):
 oldStartIdx=0
 newStartIdx=0
 oldEndIdx=len(oldCo)-1
 newEndIdx=len(newCo)-1
 oldStartMod=oldCo[oldStartIdx]
 oldEndMod=oldCo[oldEndIdx]
 newStartMod=newCo[newStartIdx]
 newEndMod=newCo[newEndIdx]
 linkMap={}
 while oldStartIdx<=oldEndIdx and newStartIdx<=newEndIdx:
  if checkRelateMod(oldStartMod,newStartMod):
   dealRelateMod(oldStartMod,newStartMod)
   oldStartIdx+=1
   newStartIdx+=1
   if newStartIdx>newEndIdx or oldStartIdx>oldEndIdx:
    break
   oldStartMod=oldCo[oldStartIdx]
   newStartMod=newCo[newStartIdx]
  elif checkRelateMod(oldEndMod,newEndMod):
   dealRelateMod(oldEndMod,newEndMod)
   oldEndIdx-=1
   newEndIdx-=1
   if newStartIdx>newEndIdx or oldStartIdx>oldEndIdx:
    break
   oldEndMod=oldCo[oldEndIdx]
   newEndMod=newCo[newEndIdx]
  elif checkRelateMod(oldStartMod,newEndMod):
   dealRelateMod(oldStartMod,newEndMod)
   oldStartIdx+=1
   newEndIdx-=1
   if newStartIdx>newEndIdx or oldStartIdx>oldEndIdx:
    break
   oldStartMod=oldCo[oldStartIdx]
   newEndMod=newCo[newEndIdx]
  elif checkRelateMod(oldEndMod,newStartMod):
   dealRelateMod(oldEndMod,newStartMod)
   oldEndIdx-=1
   newStartIdx+=1
   if newStartIdx>newEndIdx or oldStartIdx>oldEndIdx:
    break
   oldEndMod=oldCo[oldEndIdx]
   newStartMod=newCo[newStartIdx]
  else:
   linkMap={}
   for i in range(oldStartIdx,oldEndIdx+1):
    downloadLink=oldCo[i]['downloadLink']
    if downloadLink is not None:
     linkMap[downloadLink]=i
   idxInOld=linkMap.get(newStartMod['downloadLink'],None)
   if idxInOld is None:
    print(f"{newStartMod['name']}不存在于旧mod,{newStartMod['downloadLink']}将添加到下载任务队列")
    content.append(newStartMod)
   else:
    dealRelateMod(oldCo[idxInOld],newStartMod)
    swap(oldCo,idxInOld,oldEndIdx)
    oldEndIdx-=1
   newStartIdx+=1
   if newStartIdx>newEndIdx:
    break
   newStartMod=newCo[newStartIdx]
   oldEndMod=oldCo[oldEndIdx]
 print('new',newStartIdx,newEndIdx)
 print('old',oldStartIdx,oldEndIdx)
 if newStartIdx<=newEndIdx:
  for i in range(newStartIdx,newEndIdx+1):
   print(f"{newCo[i]['name']}为新且不重复mod，将添加到下载任务队列")
   content.append(newCo[i])
 elif oldStartIdx<=oldEndIdx:
  i=oldStartIdx
  while i<=oldEndIdx:
   if i<len(oldCo):
    print(f"{oldCo[i]['name']}为旧不重复mod，将删除")
    deleteMod(oldCo[i])
    del oldCo[i]
    oldEndIdx-=1
   else:
    break
with open(params["json_dir"],'r')as modelFile:
 preContent=json.loads(modelFile.read())
 compatibility(preContent)
oldCo=json.loads(os.environ["oldCo"])
if 'oldCo' and len(oldCo)>0:
 content=[]
 print(oldCo)
 print(preContent)
 LCS(oldCo,preContent)
 print(content)
else:
 oldCo=[]
 content=preContent
selected_mods=[x.strip()for x in params["name"].split('与')if x.strip()]
def get_file_size(file_path):
 try:
  file_size_bytes=os.path.getsize(file_path)
  for unit in['B','KB','MB','GB','TB']:
   if file_size_bytes<1024.0:
    break
   file_size_bytes/=1024.0
  return f"{file_size_bytes:.2f} {unit}"
 except OSError as e:
  print(f"Error: {e}")
  return None
def get_civitai_file(str):
 match=re.search(r'[^/]+$',str.decode())
 if match:
  return match.group(0).split('\n')[0]
 else:
  print("无法从输出中提取文件名")
def move_model(source_path,target_path):
 try:
  shutil.move(source_path,target_path)
 except OSError as e:
  print(f"Error: {e}")
def download_file(item):
 if selected_mods and item['name']not in selected_mods:
  return
 download_url=item['downloadLink']
 match=re.search(r'/([^/]*)$',download_url)
 file_name=match.group(1)
 cmd=f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {download_url} -d {lora_dir}" if '.' not in match.group(1)else f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {download_url} -d {lora_dir} -o {file_name}"
 result=subprocess.run(cmd,shell=True,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
 if result.returncode==0:
  if '.' not in file_name:
   file_name=get_civitai_file(result.stdout)
  if item['name']!='未命名':
   temp_name=sanitize_filename(item['name'])+os.path.splitext(file_name)[1]
   os.rename(f"{lora_dir}/{file_name}",f"{lora_dir}/{temp_name}")
   final_name=temp_name
  else:
   final_name=file_name
  source_path=f"{lora_dir}/{final_name}"
  file_size=get_file_size(source_path)
  if item.get('path')and item['path']!="":
   target_path=item['path']
   move_model(source_path,target_path)
   item['path']=target_path
   print(file_name+'已下载，重命名为：'+final_name)
   print('移动--',final_name,f'到{target_path}')
  elif file_size and 'GB' in file_size:
   move_model(source_path,check_dir)
   item['path']=check_dir
   print(file_name+'已下载，重命名为：'+final_name)
   print('移动checkpoint--',final_name,f'到{check_dir}文件夹')
  else:
   item['path']=lora_dir
   print(file_name+'已下载，重命名为：'+final_name)
  item['name']=final_name
  oldCo.append(item)
 else:
  print(f"{item['name']}下载失败,请检查{item['downloadLink']}")
with ThreadPoolExecutor(max_workers=5)as executor:
 for item in content:
  executor.submit(download_file,item)

#import zlib, base64
#exec(zlib.decompress(base64.b64decode('eJy1WVtvG8cVfuevGBMFdjdaUpLR9oHwukBstTBqJ0bsN3ojrLhDaavlLjG7lKiyBPoUG259CapYThvALurAQYHAaRrEihW1f4Zk5Kf8hZ4zszM7u0tKTeq+kJw5lzmXb2bOHAa9fsxS8pskjmqB+M2o/JUMNvos7tAkUTNbgzQI5ShOal0W90gnjjoDxmiUNruDdMBoQjKOm1uMev71OA7XhrQzSGOmNO0ltb7HvF7ijMa1bsyIxzZJECGhCT932qstt1UjQRcJzST1WJrsBumWaTQahgUUsk331ne8cEAd4GiHNMpIbjPph0FqGo5hARtoQJrithznPIqjvC3kFQ2nhVVtmHMdMdnZop3tdT9gTrc+ysgGDA13vNyLfRomyzdSbyOkDT/odgdJEEf1Whgz73SZq8BRr/m0S5Jdr296jNmhzdC1lPb64BRrh26NiG8+ZNmQuQ6ycFlu3Hs09FJ6LfbNOPThy47oLnxxXWwPvWUUEhMRQSZe5BPBwn+KWbAv3o3C2POvBtG24TqOYCnP1wgddmg/JWv8C7wlXkIortJnQZSa1BJeeVGQBr+l690AEuD1qCl/oF19L00pixxmtG/dWm699Yv6hYu/c42aEvOVnMNoE7BoZiK2sW7YSlVNulaVE/GJeyAXbAQAiT2zz+ilOEoBqmgDwi6ASCLuckpLgGYDUGsitW2Agi3D5aAj+ow0jBnvm8vt95fdJfFpGXYh5XZBDTfLp15YyNp73OQsd2qAawKRu7SO8ggnnVtqHS+XpvEHTNdrmGghj2g0de1SGLzVp5ubFHYPJ1kZUioi55x6nQCKKZlnjaWtyjNoVsFQ1CrMtZbipIkqxBamw9Sc55XVXi3bLElVe8U82Dv75O/TD4+nD+/NNTzTrBkuw63HD8JccAzjC5YUUnTOKahA1GSbkLNmDtJhkKSJWZAUCEMWJmJUoNoFtZZgnRN8Rzd4Dpfw1Cn4wdnE7hUAyxcaz/7y1Wz/m8nhq1HBgPHszsPp3Sd1bggGtHWaksnhvennj6effPb9t398ffueSMT02T9OvvqUa8iOlHdvrDGGl0F2oCh1woiyZQdfTx98+N3+k9f7H5+8eNEiI0gIaJPWKFvmIWI8ffmlMGlyuD87eDo5OpocfwSLTB88BiOnX3ww/ffxyfMP6nLDhlRt1styb5b35eXqnrxc3o8ZGKpYKOGAw6AX71CzmHQ9wkXl0ztPX3/8TMuLSstiGT0xQj7PyoKkSGWCvapyQVowilcv3cD4XYoRzJfi7Hi7gbf7FX/orPDtpw+Buhb5OMBLnItajVXOps0LZTgvtYE9Dudua/pdqa9AFXrcfGmkco1tzRhXrlmgKtkQrsZrXh+LGbK7BfnS/brgqGXk1ZuTlJYMFNULXRplawYKiFRukbmsNXEEyCWXnFWc0YzIZsSRKicvKsMI5F6Tv6icETt+A2q8bX2NRbEnZ0YYADs3AiLstkrAAu8rbJlVwtqG8rswfgNeL0QUORUzi7zVk3iqv3MYF+b6Tft8dqZ/sN95+s5A+RzGBZl+8wg/PddnoTs7jvXTgogyFGtQ5kWb1NQMsdUCS6tZcaDX4pkVgVst0YWz+iwJEhLFKXknjrKrWprR1tlcJ+CR8odXondD38l4eE2oOVhe0Ua1VhZjKYxL5svpt3GupnwNTV7dnx08hyeSPTpluTFcz7OXR9O7T6d3vpgc/uHk+Bju7+ndv75+/GR650AUJfgwxYK+6fX7NPLNMl7yoqWCMIxq5oRbwZl4r4lrTHLlmVKF2Y/EYglyZ4LqVFCKmBsgYtianK1WsxQPiBn2XOxZtZKxpUurhN+560j86iDIoKsQ8Gr2CHK5D1DACvHZPQCBKMTOzHQ10Vw3LwVFeT7nKub3raPRYCyu7qDExTF9IS9AqpVu1ZWD51U/RMGUgbNQUEpzxTyRM3OhlMNWgAS7IiQGx83s0VnHdg4W/3XXNhi84RLCWw6/BN/w5a1eug4yNnFXJabiaGLLxrTAmIVP5xq3T5eGWpVGOwGLo3adE+vgDUTN4AODVz15/C6utGoyZ05bwVQQ5UhfT6sbC9OCsyPHWWSEdahXrpEL1RIIeyel/jo4nDjtYTNJWdA3LQTxkDcCsiBiLuuqlzQ5vG9Y4JDid3k9C6eieI8k8LYtFvBZma+o6xt7KU0cWfODZEkm20kDeCiDHW3jbcM2fo0f1/DjV/hx823DlYAsKb6wunL+p82V0ulRYlp2BFfeEAL4lnhazfPdMRmhGfhaOeMNwGfVw0tqxUNfxacT7ASpF/A4mRA9DE7PSztbvH1CPdbZMpnBGyc/MWxgaPq0A2jkGARHOa/Ww+Lj5iaLB31zxZIJuhUZVnvFLT/+6vCym/3zo8nR/ZN//Wl6+9Xk8PPZg4fTB49mj25Pjr7GboB4meBDa51vAjOJB6yTvbnhaEAfSkkVfdAmf5wt4v5hoeNPzOyKE5HCnpElOqAFzPK9JBpK4rjBSx0bpzpTHq5arnbAQkcIlquFajqWTUzIWxZkRJe3sicvb+roiVjF86LnwzPYY4F3vkMaDdh8SRzSRhhvNkK6Q0OH8jg0gDgkqz8njYR/bpPVa2SkrzImDZ+MZAd1XMcYGE2DZJ4W1+W9nP/HsqQRk1Gh08NoMghTJ++LN9kgMsFtO9miYejcZAMKAPZhQZ3p+pXrazgdD9LytEC40NsUCUPoO85K9hrU3FamtNTO5mmo7LFMnVgxa4HrgDnnGKoXZnBl2E0Wyqp9Ol1yTn9O2YFNOdW2EO3eeh7MZT2SdpGiVhdnCLgWeaEwR5H06lmj6w0sbSM65aWlAGYxPxSd4vGtKdCiVu6G6r1c7IKKAOYb39EZkPZfnCyVxrJG1Kom6eySMX35paiF9HYalB3ff/tnYyl3V+sXGd89h6rps0YDe+eSbncNqKpG2mpjw5IPNBUYfuLgBaRQiLOtU3xT/5hUPVOkN+sXV9uPYWauh2rVcXbuP/vGKDTICjZK6PyvJupbx8lJNSJKFFmu8pN+TtdSFx+LNUVvzj558XL2t9/Pnnw6mnee4zbiRWH17zez5w3Xd2O2TVni/AwrQ5pRSn+HdPL/QiQH/tXRg6u2cE3Zwvj/AAMNW9s=')))
# Created by pyminifier (https://github.com/dzhuang/pyminifier3)
