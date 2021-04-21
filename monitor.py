import top.nvitop as nvitop


def run():
    pre_processes = set()
    while True:
        resources = nvitop.nv_info()
        cur_processes = set(resources.keys())
        if pre_processes == cur_processes:
            continue
        else:
            finish_processes = pre_processes.difference(cur_processes)
            start_processes = cur_processes.difference(pre_processes)
            # 1）对于 finish_processes 更新数据库其运行时间

            # 2）对于 start_processes 插入到数据库

            # 3）同时将必要的信息输出到日志文件中

        # sleep 五分钟
        sleep(300)
        pre_processes = cur_processes
    


