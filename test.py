import yaml
import pynvml as nvml
import psutil
import datetime 
import mail.email as email 
import top.nvi as nvi
import utils.util as util
import logging
from tabulate import tabulate
'''
1.  测试nvml 篇
nvml.nvmlInit()
device_count = nvml.nvmlDeviceGetCount()
print(f'device count: {device_count}')
index = 0
handle = nvml.nvmlDeviceGetHandleByIndex(index)
name = nvml.nvmlDeviceGetName(handle)
print(f'device name: {name}')
memory_total = nvml.nvmlDeviceGetMemoryInfo(handle).total
print(f'memory_total: {memory_total>>20}')
power = nvml.nvmlDeviceGetPowerManagementLimit(handle)
print(f'power: {power}')
display = nvml.nvmlDeviceGetDisplayActive(handle)
print(f'display active: {display}')
comp_processes = nvml.nvmlDeviceGetComputeRunningProcesses(handle)
graph_processes = nvml.nvmlDeviceGetGraphicsRunningProcesses(handle)
print(f'process: {comp_processes}')
for p in comp_processes:
    print(f'comp_proc: {p}')
'''

'''
2.  测试psutil篇 
cmd = psutil.Process(44504).cmdline()
print(f'cmd: {cmd}')
name = psutil.Process(44504).username()
print(f'name: {name}')
create_time = psutil.Process(44504).create_time()
create_time = datetime.datetime.fromtimestamp(create_time)#.strftime("%Y-%m-%d %H:%M:%S")
print(f'create time: {create_time} {type(create_time)}')
process_info = psutil.Process(44504).as_dict(attrs=['pid', 'name', 'create_time'])
print(f'process_info: {process_info}')
datetime_now = datetime.datetime.now()
print(f'date_time now: {datetime_now}')
print(f'running time: {datetime_now-create_time}')
print(f'running time: {str(datetime_now-create_time)}')
'''

'''
3.  测试yaml 模块
with open('./config.yaml','r',encoding='utf-8') as f:
    data = f.read()
config = yaml.load(data,Loader=yaml.FullLoader)
'''

'''
4.  发送邮件  
sender = '936214756@qq.com'
receiver = ['936214756@qq.com','542327823@qq.com']
pwd = 'nwiciwqhsfssbddg'
host_server = 'smtp.qq.com'
mail_content = 'This is for test!'
email_title = 'GPU usage!'
email.send_mail(mail_content,email_title,sender,receiver,pwd,host_server)
'''

'''
5.  测试nvi
results = nvitop.nv_info()
print(results)
'''

'''
6.  测试日志文件 
util.init_logging('global',logging.INFO,'./test_env.log',0)
logger = logging.getLogger('global')
logger.info('test the log script!')
'''

'''
7.  测试表格
table_header = ['Name', 'Chinese', 'Math', 'English']
table_data = [('Tom', '90', '80', '85'),('Jim', '70', '90', '80'),
              ('Lucy', '90', '70', '90')]
print(tabulate(table_data, headers=table_header, tablefmt='grid'))
'''

'''
8.  测试表格和邮件

table_header = ['Name','Server_name','GPUs','Time','Running_time']
table_data = [('lpy','csffm3','4','2020.01.25','1000')]
text = """
Hello, Friend.
Here is your data:
{}
Regards,
Me"""

html = """
<html>
<head>
<style> 
  table, th, td {{ border: 1px solid black; border-collapse: collapse; }}
  th, td {{ padding: 5px; }}
</style>
</head>
<body><p>Hello, Friend.</p>
<p>Here is your data:</p>
{}
<p>Regards,</p>
<p>Me</p>
</body></html>
"""

sender = '936214756@qq.com'
receiver = ['936214756@qq.com','542327823@qq.com']
# receiver = ['936214756@qq.com']
pwd = 'nwiciwqhsfssbddg'
host_server = 'smtp.qq.com'
mail_content = email.write_table(table_header,table_data,fmt)
text = text.format(tabulate(table_data,table_header,'grid'))
html = html.format(tabulate(table_data,table_header,'html'))
email_title = 'GPU usage!'
email.send_mail(text,html,email_title,sender,receiver,pwd,host_server)
'''