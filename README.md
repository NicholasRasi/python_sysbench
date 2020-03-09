# Python Sysbench 
A python module that wraps sysbench benchmarks. Note: sysbench has to be installed

## Benchmarks
### CPU
The cpu is one of the most simple benchmarks in SysBench. In this mode each request consists in calculation of prime numbers up to a value specified by the--cpu-max-primes option. All calculations are performed using 64-bit integers. Each thread executes the requests concurrently until either the total number of requests or the total execution time exceed the limits specified with the common command line options.

#### Signature
```
def cpu(cpu_max_prime)
```
#### Returned Values
Dict:
- total time [s]


### Threads
This test benchmarks the scheduler performance, more specifically the cases when a scheduler has a large number of threads competing for some set of mutexes.

#### Signature
```
def threads(max_time, num_threads)
```
#### Returned Values
Dict:
- average latency [ms]


### Memory
This test mode can be used to benchmark sequential memory reads or writes.

#### Signature
```
def memory(mem_block_size, mem_total_size)
```
#### Returned Values
Dict:
- throughput [ops/s]


### FileIO
This test mode can be used to produce various kinds of file I/O workloads.

#### Signature
```
def fileio(file_total_size, file_test_mode, max_time, max_requests)
```
#### Returned Values
Dict:
- read ops [ops/s]
- write ops [ops/s]
- fsync ops [ops/s]
- throughput read [MiB/s]
- throughput write [MiB/s]

### Sysbench Reference
- [manual](https://imysql.com/wp-content/uploads/2014/10/sysbench-manual.pdf)