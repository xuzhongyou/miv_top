import pynvml as nvml
import psutil
import datetime 

# 只针对使用GPU的进程，所以cpu为空，且内存使用情况只代表
# 当前进程，不代表整个任务。
def nv_info():
    info = []
    nvml.nvmlInit()
    device_count = nvml.nvmlDeviceGetCount()
    for index in range(device_count):
        handle = nvml.nvmlDeviceGetHandleByIndex(index)
        name = nvml.nvmlDeviceGetName(handle)
        memory_total = nvml.nvmlDeviceGetMemoryInfo(handle).total
        comp_processes = nvml.nvmlDeviceGetComputeRunningProcesses(handle)
        for item in comp_processes:
            memory_use = item.usedGpuMemory
            pid = psutil.Process(item.pid)
            pid_num = item.pid
            cmd = ' '.join(pid.cmdline())
            username = pid.username()
            cpu_percent =  pid.cpu_percent()
            mem_percent = pid.memory_percent()
            create_time = datetime.datetime.fromtimestamp(pid.create_time())
            cur_time = datetime.datetime.now()
            runtime = cur_time - create_time
            info.append((index,username,pid_num,memory_use>>20,cpu_percent,format(mem_percent,'.2f'),
                create_time.strftime('%Y-%m-%d %H:%M:%S'),cur_time.strftime('%Y-%m-%d %H:%M:%S'),
                format(runtime.total_seconds()/3600,'.2f'),cmd[:30]))
    return info
