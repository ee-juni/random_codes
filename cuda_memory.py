# "pip install nvidia-ml-py3"
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "nvidia-ml-py3"])

# Import modules
import nvidia_smi
import numpy as np
import os

def get_free():
    '''
    Return list of percentage of free memory of all available CUDA devices.
    '''
    nvidia_smi.nvmlInit()
    freem = []

    for i in range(nvidia_smi.nvmlDeviceGetCount()):
        info = nvidia_smi.nvmlDeviceGetMemoryInfo(nvidia_smi.nvmlDeviceGetHandleByIndex(i))
        freem.append(100*info.free/info.total)
    nvidia_smi.nvmlShutdown()

    return freem

def get_sorted():
    '''
    Return list of CUDA device numbers sorted from highest to lowest percentage of free memory
    '''
    freem = get_free()
    l = []
    for i in range(len(freem)):
        max_idx = np.argmax(freem).item()
        l.append(max_idx)
        freem[max_idx]=-1
    return l

def set_device(num: int = 1):
    '''
    Set CUDA_VISIBLE_DEVICES to the most free CUDA device
    '''
    if num<1 or not isinstance(num ,int):
        raise TypeError("Number of devices must be a positive integer")
    devices_string = ",".join([str(i) for i in get_sorted()][:num])
    os.environ['CUDA_VISIBLE_DEVICES'] = devices_string
    print("CUDA_VISBLE_DEVICES set to",devices_string)
    
