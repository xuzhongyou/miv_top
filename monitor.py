import top.nvitop as nvitop
import utils.util as util
import logging
import time

def run():
    util.init_logging('global',logging.INFO,'./test_env.log',0)
    logger = logging.getLogger('global')
    pre_processes = set()
    pre_resources = None
    while True:
        cur_resources = nvitop.nv_info()
        cur_processes = set(cur_resources.keys())
        if pre_processes == cur_processes:
            continue
        else:
            finish_processes = pre_processes.difference(cur_processes)
            start_processes = cur_processes.difference(pre_processes)
            # 1）对于 finish_processes 更新数据库其运行时间

            # 2）对于 start_processes 插入到数据库

            # 3）同时将必要的信息输出到日志文件中  
            if finish_processes: 
                for process in finish_processes:
                    information = f"User-{pre_resources[process][1]} Pid-{process} G_ind-{pre_resources[process][0]} G_mem-{pre_resources[process][2]} Task-{pre_resources[process][-1]}. The process starts at {pre_resources[process][-4]} and finishes at {pre_resources[process][-3]}, the total runtime is {pre_resources[process][-2]}! "
                    logger.info(information)
            if start_processes:
                for process in start_processes:
                    information = f"User-{cur_resources[process][1]} Pid-{process} G_ind-{cur_resources[process][0]} Task-{cur_resources[process][-1]}. The process starts at {cur_resources[process][-4]}! "
                    logger.info(information)

        # sleep 五分钟
        time.sleep(10)
        pre_processes = cur_processes
        pre_resources = cur_resources

def Timer_send():
    #1) 查询数据库每人一周使用的总时长
    
    #2) 定时发送邮件
    schedule.every().wednesday.at("22:00").do(send_mail) 

if __name__ == "__main__":
    run()
