import os

os.system("sudo ip link set can0 down")
os.system("sudo ip link set can0 type can bitrate 500000")
os.system("sudo ip link set can0 up")


