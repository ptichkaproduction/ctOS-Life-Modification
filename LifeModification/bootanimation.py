#OPERATING SYSTEM
import os
import time
from datetime import datetime
import platform
com = str("")
buffer = ""
buffer2 = ""
start = "true"
clean = ""
if platform.system() == "Windows":
    clean = "cls"
    syst = "| base system: WINDOWS |"
elif platform.system() == "Linux" or platform.system() == "Darwin":
    clean = "clear"
    syst = "| base system: LINUX   |"
os.system(clean)
print("[        ]")
print("Please, wait... (0%)")
time.sleep(0.085)
os.system(clean)
print("[//      ]")
print("Please, wait... (20%)")
time.sleep(0.085)
os.system(clean)
print("[////    ]")
print("Please, wait... (50%)")
time.sleep(0.085)
os.system(clean)
print("[//////  ]")
print("Please, wait... (75%)")
time.sleep(0.085)
os.system(clean)
print("[////////]")
print("Complete! (^^) (100%)")
time.sleep(0.1)
os.system(clean)
