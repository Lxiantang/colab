import random
import string
import subprocess
import sys
import os
import concurrent.futures
import time
import shutil
params={}
for arg in sys.argv[1:]:
 if arg.startswith('--'):
  key_value=arg[len('--'):].split('=')
  if len(key_value)==2:
   key,value=key_value
   params[key]=value
subprocess.run(f'cd {params["dir"]}/',shell=True)
if params["ui"]=="anapnoe手机端完美适配":
 subprocess.run(f'git clone https://github.com/anapnoe/stable-diffusion-webui {params["dir"]}',shell=True)
elif params["ui"]=="V1.6SDXL":
 subprocess.run(f'git clone -b v1.6.0 --single-branch https://github.com/AUTOMATIC1111/stable-diffusion-webui {params["dir"]}',shell=True)
else:
 subprocess.run(f'git clone -b v1.5.1 --single-branch https://github.com/AUTOMATIC1111/stable-diffusion-webui {params["dir"]}',shell=True)
checkpoint_url={"Dark_sushi_mix.safetensors":"https://huggingface.co/mdl-mirror/dark-sushi-mix/resolve/main/darkSushiMixMix_brighter.safetensors","AnythingV5V3_v5PrtRE.safetensors":"https://huggingface.co/ckpt/anything-v5.0/resolve/main/AnythingV5V3_v5PrtRE.safetensors","chilloutmix_NiPrunedFp16Fix.safetensors":"https://huggingface.co/naonovn/chilloutmix_NiPrunedFp32Fix/resolve/main/chilloutmix_NiPrunedFp32Fix.safetensors","rpg_V4.safetensors":"https://huggingface.co/Anashel/rpg/resolve/main/RPG-V4-Model-Download/RPG-v4.safetensors","ProtoGen_X5.8-pruned-fp16.safetensors":"https://huggingface.co/darkstorm2150/Protogen_x5.8_Official_Release/resolve/main/ProtoGen_X5.8-pruned-fp16.safetensors","sd-xl.safetensors":"https://civitai.com/api/download/models/128078","none":""}
def run_git_download():
 start_time=time.time()
 subprocess.run(f'git clone https://github.com/Physton/sd-webui-prompt-all-in-one {params["dir"]}/extensions/sd-webui-prompt-all-in-one',shell=True)
 subprocess.run(f'git clone https://github.com/Mikubill/sd-webui-controlnet {params["dir"]}/extensions/sd-webui-controlnet',shell=True)
 subprocess.run(f'git clone https://github.com/dtlnor/stable-diffusion-webui-localization-zh_CN {params["dir"]}/extensions/stable-diffusion-webui-localization-zh_CN',shell=True)
 subprocess.run(f'git clone https://github.com/fkunn1326/openpose-editor {params["dir"]}/extensions/openpose-editor',shell=True)
 subprocess.run(f'git clone https://github.com/DominikDoom/a1111-sd-webui-tagcomplete {params["dir"]}/extensions/a1111-sd-webui-tagcomplete',shell=True)
 subprocess.run(f'git clone https://github.com/Coyote-A/ultimate-upscale-for-automatic1111 {params["dir"]}/extensions/ultimate-upscale',shell=True)
 subprocess.run(f'git clone https://github.com/toriato/stable-diffusion-webui-wd14-tagger {params["dir"]}/extensions/stable-diffusion-webui-wd14-tagger',shell=True)
 subprocess.run(f'git clone https://github.com/nonnonstop/sd-webui-3d-open-pose-editor {params["dir"]}/extensions/sd-webui-3d-open-pose-editor',shell=True)
 subprocess.run(f'git clone https://github.com/hako-mikan/sd-webui-lora-block-weight {params["dir"]}/extensions/sd-webui-lora-block-weight',shell=True)
 subprocess.run(f'git clone https://github.com/s9roll7/ebsynth_utility {params["dir"]}/extensions/ebsynth_utility',shell=True)
 if params["animatediff"]=="True":
  subprocess.run(f'git clone https://github.com/guoyww/animatediff {params["dir"]}/extensions/AnimateDiff-main', shell=True)
 end_time=time.time()
 print("已克隆git耗时：",end_time-start_time,"秒")
def run_aria2c_download():
 start_time=time.time()
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M {checkpoint_url[params["model"]]} -d {params["dir"]}/models/Stable-diffusion -o {params["model"]}',shell=True)
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11e_sd15_ip2p_fp16.safetensors -d {params["dir"]}/models/ControlNet -o control_v11e_sd15_ip2p.safetensors',shell=True)
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11f1p_sd15_depth_fp16.safetensors -d {params["dir"]}/models/ControlNet -o control_v11f1p_sd15_depth.safetensors',shell=True)
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_canny_fp16.safetensors -d {params["dir"]}/models/ControlNet -o control_v11p_sd15_canny.safetensors',shell=True)
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_inpaint_fp16.safetensors -d {params["dir"]}/models/ControlNet -o control_v11p_sd15_inpaint.safetensors',shell=True)
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_lineart_fp16.safetensors -d {params["dir"]}/models/ControlNet -o control_v11f1p_sd15_depth.safetensors',shell=True)
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_mlsd_fp16.safetensors -d {params["dir"]}/models/ControlNet -o control_v11p_sd15_mlsd.safetensors',shell=True)
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_normalbae_fp16.safetensors -d {params["dir"]}/models/ControlNet -o control_v11p_sd15_normalbae.safetensors',shell=True)
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_openpose_fp16.safetensors -d {params["dir"]}/models/ControlNet -o control_v11p_sd15_openpose.safetensors',shell=True)
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_scribble_fp16.safetensors -d {params["dir"]}/models/ControlNet -o control_v11p_sd15_scribble.safetensors',shell=True)
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_seg_fp16.safetensors -d {params["dir"]}/models/ControlNet -o control_v11p_sd15_seg.safetensors',shell=True)
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15_softedge_fp16.safetensors -d {params["dir"]}/models/ControlNet -o control_v11p_sd15_softedge.safetensors',shell=True)
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11p_sd15s2_lineart_anime_fp16.safetensors -d {params["dir"]}/models/ControlNet -o control_v11p_sd15s2_lineart_anime.safetensors',shell=True)
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/comfyanonymous/ControlNet-v1-1_fp16_safetensors/resolve/main/control_v11f1e_sd15_tile_fp16.safetensors -d {params["dir"]}/models/ControlNet -o control_v11f1e_sd15_tile_fp16.safetensors',shell=True)
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/lokCX/4x-Ultrasharp/resolve/main/4x-UltraSharp.pth -d {params["dir"]}/models/ESRGAN/ -o 4x-UltraSharp.pth',shell=True)
 subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/datasets/daasd/CN.csv/resolve/main/CN.csv -d {params["dir"]}/extensions/a1111-sd-webui-tagcomplete/tags -o CN.csv',shell=True)
 if params["animatediff"]=="True":
  subprocess.run(f'aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://huggingface.co/guoyww/animatediff/resolve/main/mm_sd_v15_v2.ckpt -d {params["dir"]}/extensions/AnimateDiff-main/models/StableDiffusion -o mm_sd_v15_v2.ckpt',shell=True)
 end_time=time.time()
 print("aria2c完成下载耗时：",end_time-start_time,"秒")
 
def curl_download():
 start_time=time.time()
 subprocess.run(f"curl -Lo '{params['dir']}/models/VAE/vae-ft-mse-840000-ema-pruned.safetensors' https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors",shell=True)
 subprocess.run(f"curl -Lo '{params['dir']}/models/VAE/kl-f8-anime2.ckpt' https://huggingface.co/hakurei/waifu-diffusion-v1-4/resolve/4c4f05104055c029ad577c18ac176462f0d1d7c1/vae/kl-f8-anime2.ckpt",shell=True)
 subprocess.run(f"curl -Lo '{params['dir']}/models/VAE/animevae.pt' https://huggingface.co/swl-models/animvae/resolve/main/animevae.pt",shell=True)
 end_time=time.time()
 print("curl完成下载耗时：",end_time-start_time,"秒")
def wget_download():
 start_time=time.time()
 subprocess.run("apt install libunwind8-dev -yqq",shell=True)
 os.environ["LD_PRELOAD"]="libtcmalloc.so.4"
 os.environ["TF_CPP_MIN_LOG_LEVEL"]="3"
 subprocess.run("sudo apt-get install sox ffmpeg libcairo2 libcairo2-dev",shell=True)
 end_time=time.time()
 print("wget完成下载耗时：",end_time-start_time,"秒")
def pip_download():
 start_time=time.time()
 subprocess.run("pip install xformers xformers==0.0.20",shell=True)
 end_time=time.time()
 print("pip完成下载耗时：",end_time-start_time,"秒")
executor=concurrent.futures.ThreadPoolExecutor(max_workers=5)
task1=executor.submit(run_git_download)
task2=executor.submit(run_aria2c_download)
task3=executor.submit(curl_download)
task4=executor.submit(wget_download)
task5=executor.submit(pip_download)
concurrent.futures.wait([task1,task2,task3,task4,task5])
if os.path.exists(f'{params["dir"]}/embeddings'):
 shutil.rmtree(f'{params["dir"]}/embeddings')
subprocess.run(f'git clone https://huggingface.co/nolanaatama/embeddings {params["dir"]}/embeddings',shell=True)
if params["extensions"]=="True":
 if os.path.exists("/content/drive/MyDrive/extensions"):
  subprocess.run(f'rsync -a /content/drive/MyDrive/extensions/* {params["dir"]}/extensions',shell=True)
  print('已加载云盘里的插件')
 if os.path.exists("/content/drive/MyDrive/VAE"):
  subprocess.run(f'rsync -a /content/drive/MyDrive/VAE/* {params["dir"]}/models/VAE',shell=True)
  print('已加载云盘里的VAE')
 if os.path.exists("/content/drive/MyDrive/embeddings"):
  subprocess.run(f'rsync -a /content/drive/MyDrive/embeddings/* {params["dir"]}/embeddings',shell=True)
  print('已加载云盘里的embeddings')
 if os.path.exists("/content/drive/MyDrive/lora"):
  subprocess.run(f'mkdir -p {params["dir"]}/models/Lora',shell=True)
  subprocess.run(f'rsync -a /content/drive/MyDrive/lora/* {params["dir"]}/models/Lora',shell=True)
  print('已加载云盘里的lora')
 if os.path.exists("/content/drive/MyDrive/checkpoint"):
  subprocess.run(f'rsync -a /content/drive/MyDrive/checkpoint/* {params["dir"]}/models/Stable-diffusion',shell=True)
  print('已加载云盘里的Stable-diffusion')

#import zlib, base64
#exec(zlib.decompress(base64.b64decode('eJztWltv3LgVfvevEPRiuzCl0XjGyQaYB8N2ggVsx0iyRgDDEDgSNSKGIrUkNZ7ZIMCi6PaW9LYvW6R96FsfCmyBPmyLbbe/ZpNsnvoXeqi5ay6eGQ8CxFjDkGXynMPvfDw8h5JIk1RIbUnMQ5Fs0O5/SkvKG4P/snoqRUCUGrR0BrdicBcIHmRSEq6dKNOZJIMeTRMyUI0zTdlGiiVOVO3Z841ISAvLhkW5MevAbevCu3d5b8OikelwlMZSqyuq461NhDa3ocdqko7fwiwjNZC4YIT3ui4dlTKqtzZrm9sgBhZM30B6u1YrG3Wjv9PVH/SZ5i6qC2i7rHUbh747MuNb0WYQWs96YnZIpX353N3cUTFhrPZEwggbMGa/P6P2Za1mY45TLsibX7148+dv3/7t76+/fvn2v7999/lP333xGxvgTIzRoMAmE5xYsdapuue60BJndScQiduz5gItdUZQSKMoU1RwdEXqGS2CG8dG2CS6c8/Ze3z49PgaJKhutUDSKVkIKQgOGLoOQRPE0zDuf/Lk4cn+k48PPPhZEakiiwCqOt77ARTEJGimgnLtZ5LVntmHWDZ9lamY+gltOwpHRBOuhFT2PbsPIc4aDcAW4YAADjcJGUqolEK6IaijXB1a2i6sFsFaxE0w5XnfY9N1Qtvw69clbcSayLFBdux93tExWD+vnu/6reqZ1I+OFsMBnmgIpK46alWd0jiAay3v2EFMGROZBvD+KT2D2SHh/dTbu78oFxwLLlrcnW5ot3y/yMocwQI2mTb888piMPY5NtPsgs74cI/OHqDzCjoRIWHoUFxxJnCYt7YqhfHOpNDiAeH+06pzF6U5MhQBGYtBMNOttJBJ2auW3NxYA4y1wZj/MIpoQDHzHxFGsCLjGBcbeMfmsGBgfPv5RkgiC8R8WBt+2HNqy6TUPMv6JlPXzMUxl63tZZPTWdwBT7irwu6aAkwiSTXCjCHKkdEqZk/SNjhhFao5WuNrcUlQJ7SZ1SF2hvahVGkpGCd6IThD8RvhCDXjsPKnZx/ERIAZ/Qxr0/RZ7B+czsW2qJEbIY6aGefebnnPFSnhqVAEkZBCqM6DVhC9EYBDkVBOm4fCFD6Tu9FgUjRugETKIMznoZmtdSNgB6IjNEH7bsZgpWC4zVIF3BME+xmEMy2gkQZm8Hnoito3wgRkU6zFrNi4Cr2K8b9B5k7f9do3AgmpCH4hSaTD9bUbIhM0aMEAm6d3I2wxbgqoxk08ksCYkBjVYV01ocGU4YWQTWjdCJf6CLIPu+OSuupwHftmB011Zx6SguiNhic6JpJg1m67dayDmFHeVNP3TKMQirIFDISHU8pNCg8eest+/c9/vP7ixbtXPwcYP3z+1Zuvvvnff17ZO30dNKxWO/bbv35pbw8KG4Y1UA5WrG1dZdhQQsaHMktgHhuIkRZhNWJ2bRaCzrbl7VlI5dem5Z1Yz8b3hhd9ShKzdbAvL59baPKhIe9U7uPCarOQGIr2DDy/bvZWgz1rbyiSqINhjXYSkSlIdHntOyUatTzk+WZ34Y/sLgp7tK603/I84qvQq/o0Lad+cUsyh5DheIaK6fZGTX2Q3ERe2vUmJCks0nXQM27yg2eo50yAOe+shZ9Rg7eFHcpTbJLOGvnpmbwtDEH5ISb3/7jCZjGUMBWuM4CMvdvCDTytJZjVMVknQQOjt4Wl/vPeOknq27wtHKlA0jps9NbJUd/mreGINNZKD2ncGmZEpEnYWG/09GzeEo5UeVDrMYfHuzVSVTT9wTMW9Z+lNF1TRppv8b2SxETz4KlbaaNPmJZYxVim40T0ux6bLgd2cnMcPnr86MH+qWu8nVB7r16FWGNFtIIbrEL34NQJVGvcr27bNGcWehvqwr0yjnbtLPOypuvp669fvvnl77//14sfvvtu8Vc2QSbZai9rbKNqoWNhbfYd3gSHN4ezd75/5LYwQZFGiSLobqUEP4gkuPelZCxGZzFvXofmr9AwNa/3RuwJSUEQs/FpWHRAe374LOZdk6HoLsqzUtkxH/VmuhHjZiYJda8wjbKRl7uQOSoDBypBJSpVvVKlVK0GpfJHOKzeuRN4d3Hg3dmr7JWjUuiF0GCcnBx7LR7l9sC8M8cXdcVQT8WIGzBjUzBiw14ijA2+1YL4qkFW+5pm41RblIM0Yxaj9YxfUR7eRSGBhdz59NMCfKEcwltUCn5hHx/6Z4+Ojh/uH9qXNRt0dQCPFUwEjhJOxR4XfnLfPzg7808+PvWPHz7wj4/Oj46N2q49CUllobAAFwKnBtiUaFtRlKSkYWAGGMyWh3cG7zJMG75WYzql6WpEg+LAmXYEj2AEKl3/plYrOSWnXFrGBzC4vAukTYJMC1mbPCvjPIklweGZEOyoJ7WV4LZ/JWTTQKxub0AJaHq1vg0HXEyo3ip+ze3KlafKFV6Od0V3J0THknJXqDIhNBb0XaHqhNDofG1vTPEa8pHeusg928lx59fd/FrJr9XL/EwNhHOKdeyQNlVaQX2dqHJJnYQhpAmVHxHqnjNyZKIlIdeIT57ymfweUjy9IBjmGKpygkdMTZbe4SizDgkNq3N+HMf0293DTwWX7XwPB+S5oaSQ6046h/nfEQP52agJZ6TqcNhrYOtaA+5P5mweCluC3kLYNJ9qfv0XWALff/uHt3/647tfvHz76mdvfvfl9//+xpzBWtwPSP8rOmAKxyTyYVVZBrkRXwr2cIpXpX9gYBr9MwJovhNjwb2EL+az5QwvkiYgslA6i+ZjUC1CXJoKM/7smZw2xDwWjLXl/B9+yFtxLocGZrtR/OS3jEsTutv/B+msQ10=')))
# Created by pyminifier (https://github.com/dzhuang/pyminifier3)
