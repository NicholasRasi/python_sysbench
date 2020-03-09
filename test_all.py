from sysbench import Sysbench

sysbench = Sysbench()
print("CPU: " + str(sysbench.cpu(2000)))
print("Memory: " + str(sysbench.memory("1M", "10G")))
print("Threads: " + str(sysbench.threads(10, 128)))
print("FileIO: " + str(sysbench.fileio("1GB", "rndrw", 5, 0)) + "ops/s & MiB/s")
