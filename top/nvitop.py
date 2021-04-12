import pynvml as nvml
import psutil
import datetime 
## nvml 篇
# nvml.nvmlInit()
# device_count = nvml.nvmlDeviceGetCount()
# print(f'device count: {device_count}')
# index = 0
# handle = nvml.nvmlDeviceGetHandleByIndex(index)
# name = nvml.nvmlDeviceGetName(handle)
# print(f'device name: {name}')
# memory_total = nvml.nvmlDeviceGetMemoryInfo(handle).total
# print(f'memory_total: {memory_total>>20}')
# power = nvml.nvmlDeviceGetPowerManagementLimit(handle)
# print(f'power: {power}')
# display = nvml.nvmlDeviceGetDisplayActive(handle)
# print(f'display active: {display}')
# comp_processes = nvml.nvmlDeviceGetComputeRunningProcesses(handle)
# graph_processes = nvml.nvmlDeviceGetGraphicsRunningProcesses(handle)
# print(f'process: {comp_processes}')
# for p in comp_processes:
#     print(f'comp_proc: {p}')

# ##psutil篇 
# cmd = psutil.Process(44504).cmdline()
# print(f'cmd: {cmd}')
# name = psutil.Process(44504).username()
# print(f'name: {name}')
# create_time = psutil.Process(44504).create_time()
# create_time = datetime.datetime.fromtimestamp(create_time)#.strftime("%Y-%m-%d %H:%M:%S")
# print(f'create time: {create_time} {type(create_time)}')
# process_info = psutil.Process(44504).as_dict(attrs=['pid', 'name', 'create_time'])
# print(f'process_info: {process_info}')
# datetime_now = datetime.datetime.now()
# print(f'date_time now: {datetime_now}')
# print(f'running time: {datetime_now-create_time}')
# print(f'running time: {str(datetime_now-create_time)}')

def get_info():
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
            pid = item.pid
            cmd = ' '.join(psutil.Process(pid).cmdline())
            username = psutil.Process(pid).username()
            create_time = create_time = datetime.datetime.fromtimestamp(psutil.Process(pid).create_time())
            runtime = datetime.datetime.now() - create_time
            info.append((index,pid,username,memory_use>>20,str(runtime),cmd))
    return info
info = get_info()
print(info)