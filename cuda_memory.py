# "pip install nvidia-ml-py3"
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "nvidia-ml-py3"])

# Import modules
import nvidia_smi
import numpy as np

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

