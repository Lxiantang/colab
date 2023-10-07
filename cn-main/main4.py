import subprocess
import sys
import os
params={}
params2={}
paramArr=[]
for arg in sys.argv[1:]:
 if arg.startswith('--'):
  key_value=arg[len('--'):].split('=')
  if len(key_value)==2:
   key,value=key_value
   params[key]=value
  elif len(key_value)==1:
   paramArr+=key_value
params2=params.copy()
del params2["full"],params2["dark"],params2["token"],params2["dir"]
os.chdir(f'{params["dir"]}')
full_precision_str="--share --lowram --disable-safe-unpickle  --disable-console-progressbars --xformers --enable-insecure-extension-access --precision full --no-half --no-half-vae --opt-sub-quad-attention --opt-channelslast --api"
half_precision_str="--share --lowram  --disable-safe-unpickle  --disable-console-progressbars --xformers --enable-insecure-extension-access  --opt-sub-quad-attention --opt-channelslast --api"
for key,value in params2.items():
 full_precision_str+=" --{}={}".format(key,value)
 half_precision_str+=" --{}={}".format(key,value)
for item in paramArr:
 full_precision_str+=f" --{item}"
 half_precision_str+=f" --{item}"
if params["dark"]=="True":
 full_precision_str+=" --theme='dark'"
 half_precision_str+=" --theme='dark'"
else:
 full_precision_str+=" --theme='light'"
 half_precision_str+=" --theme='light'"
if params["token"] != "":
 full_precision_str+=f'  --ngrok={params["token"]} --ngrok-region="auto"'
 half_precision_str+=f'  --ngrok={params["token"]} --ngrok-region="auto"'
if params["full"]=="True":
 subprocess.run(f"python launch.py {full_precision_str}",shell=True)
else:
 subprocess.run(f"python launch.py {half_precision_str}",shell=True)

#import zlib, base64
#exec(zlib.decompress(base64.b64decode('eJy9VMGO2jAQvecrUl8StDjSckTyof/QG4qQCRNiYWzXdthFKP/eGRKyoSxltYeeMpl58/zGfrY6OOtjGtqN87aCEBI1ZE5jaEPipJeHIM7dEC3G8Kf3YlUmtfWp9LtUGeosMDyuXpflMklVTYUiROljeFOxyTPOsxlW0j2c1kepWxCIWGkwQ6ksgtMq5pnIZghDBqqN6JkQC2qn/nnfP9Yo3UtcYa4U1yToT1helyMcx3iZsFyn7L9FZd0pnyVb0AP5YsXqVmtWzsf/rfT76X+0ezA3AOVZmVhkazDM6+w8CO0rHc5KnGvnoVJBWbMO0QvGeWikh5Rzbd8Qj8FWBbnRwIOsgbfGqWqvIZ0UKmuCxS+e6c7joW6kD1h+x1M6wCUEcwEqE6BqPXB4j2BoUS4rsgFCRh0pycKEsbyRuv6I+FGSLusiRwPx363cchmRKFJXX6gaaQzooGWImJJOsYR6n475n+b8jn4y++g9svxwxoWKcAg5efv+JF8Ew/5zhzeHFSRQxnwkQZvfb8qTDlJBC44C0MMPVq4vRATu2Ocr3SDwqozWvLhaCPbLt8D+MVhs4AAiI3z2YI17GO4rPOfUatfEL5BecRP5wyVMf4iUPVJfZ2QCs/N2L85/NXbXCvewww7BZBstyx5s4neYJmr7J2Wy2R/PcuFbk9fMnWKD1tSyNVVTuFN6vp+oY/PQgNaCWGbXPf4C1f1It1R/ADLxJ0Q=')))
# Created by pyminifier (https://github.com/dzhuang/pyminifier3)
