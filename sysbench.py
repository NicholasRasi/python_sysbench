import multiprocessing
import subprocess
import re


class Sysbench:
    def __init__(self):
        self.num_threads = multiprocessing.cpu_count()

    def set_num_threads(self, num_threads):
        self.num_threads = num_threads

    def cpu(self, cpu_max_prime):
        try:
            output = str(subprocess.check_output(
                ["sysbench", "cpu", "--cpu-max-prime=" + str(cpu_max_prime),
                 "--threads=" + str(self.num_threads), "run"]))
        except Exception as e:
            print(str(e))
            return None

        regex_total_time = r"total time:[\s]*([0-9.]*)s"
        match_total_time = re.findall(regex_total_time, output, re.MULTILINE)

        total_time = None
        if match_total_time:
            total_time = match_total_time[0]
        return {"total_time [s]": total_time}

    def memory(self, mem_block_size, mem_total_size):
        try:
            output = str(subprocess.check_output(["sysbench", "memory", "--memory-block-size=" + str(mem_block_size),
                                                  "--memory-total-size=" + str(mem_total_size),
                                                  "--threads=" + str(self.num_threads), "run"]))
        except Exception as e:
            print(str(e))
            return None

        regex_throughput = r"([0-9.]*) per second"
        match_throughput = re.findall(regex_throughput, output, re.MULTILINE)

        throughput = None
        if match_throughput:
            throughput = match_throughput[0]
        return {"throughput [ops/s]": throughput}

    def threads(self, max_time, num_threads):
        try:
            output = str(subprocess.check_output(["sysbench", "threads", "--max-time=" + str(max_time),
                                                  "--threads=" + str(num_threads), "run"]))
        except Exception as e:
            print(str(e))
            return None

        regex_avg_lat = r"avg:\s*([0-9.]*)"
        match_avg_lat = re.findall(regex_avg_lat, output, re.MULTILINE)

        avg_lat = None
        if match_avg_lat:
            avg_lat = match_avg_lat[0]
        return {"avg_lat [ms]": avg_lat}

    def fileio(self, file_total_size, file_test_mode, max_time, max_requests):
        try:
            subprocess.check_output(["sysbench", "fileio", "--file-total-size=" + str(file_total_size), "prepare"])
            output = str(subprocess.check_output(["sysbench", "fileio", "--file-total-size=" + str(file_total_size),
                                                  "--file-test-mode=" + file_test_mode, "--max-time=" + str(max_time),
                                                  "--max-requests=" + str(max_requests), "run"]))
            subprocess.check_output(["sysbench", "fileio", "--file-total-size=" + str(file_total_size), "cleanup"])
        except Exception as e:
            print(str(e))
            return None

        regex_ops = r"reads/s:\s*([0-9.]*)\\n\s*writes/s:\s*([0-9.]*)\\n\s*fsyncs/s:\s*([0-9.]*)"
        match_ops = re.findall(regex_ops, output, re.MULTILINE)
        print(match_ops)
        regex_throughput = r"read, [a-zA-Z/]*:\s*([0-9.]*)\\n\s*written, [a-zA-Z/]*:\s*([0-9.]*)"
        match_throughput = re.findall(regex_throughput, output, re.MULTILINE)

        ops = throughput = None
        if match_ops:
            ops = match_ops[0]
        if match_throughput:
            throughput = match_throughput[0]
        return {"ops_read [ops/s]": ops[0], "ops_write [ops/s]": ops[1], "ops_fsync [ops/s]": ops[2],
                "t_read [MiB/s]": throughput[0], "t_write [MiB/s]": throughput[1]}