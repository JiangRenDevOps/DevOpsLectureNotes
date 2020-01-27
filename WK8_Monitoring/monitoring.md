
### Problem Statement Approach
1. What makes you think there is a performance problem?
2. Has this system ever performed well?
3. What has changed recently? (Software? Hardware?
Load?)
4. Can the performance degradation be expressed in
terms of latency or run time?
5. Does the problem affect other people or applications (or
is it just you)?
6. What is the environment? Software, hardware,
instance types? Versions? Configuration?

### Workload Characterization Approach	
1. Who is causing the load? PID, UID, IP addr, ...
2. Why is the load called? code path, stack trace
3. What is the load? IOPS, tput, type, r/w
4. How is the load changing over time? 

### The USE Approach
1. Utilization: busy time
2. Saturation: queue length or queued time 
3. Error: error logs



Observability: Watch activity. Safe, usually, depending on
resource overhead.

Benchmarking: Load test. Caution: production tests can
cause issues due to contention.

Tuning Change:  Danger; changes could hurt
performance, now or later with load.

Static Check: configuration. Should be safe.

## Observability 
### 1. vmstat
vmstat reports describe the current state of a Linux system. Information regarding the running state of a system is useful when diagnosing performance related issues.
```
vmstat [interval] [count]
```

```
vagrant@linux:/home/vagrant$ vmstat 1 20
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0   1804 296112 132244 1207392    0    0    21   119   53  130  0  0 99  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   98  217  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0  106  243  0  1 99  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   70  220  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   66  215  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   66  221  0  1 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   62  230  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   73  235  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   65  244  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   73  241  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   80  243  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0  109  231  0  0 99  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   84  225  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   94  285  1  0 99  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   66  234  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   76  257  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   65  237  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   65  247  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0   75  250  0  0 100  0  0
 0  0   1804 296104 132244 1207392    0    0     0     0  114  327  0  0 100  0  0
```
more readable: convert the number to Megabytes e.g. 1M=1000KB=1000000B
```
vagrant@linux:/home/vagrant$ vmstat -S m 1 10
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0      1    303    135   1236    0    0    21   118   53  130  0  0 99  0  0
 0  0      1    303    135   1236    0    0     0     0  103  248  0  1 100  0  0
 0  0      1    303    135   1236    0    0     0     0   97  239  0  0 100  0  0
 0  0      1    303    135   1236    0    0     0     0   91  249  0  0 100  0  0
 0  0      1    303    135   1236    0    0     0     0  106  272  0  0 100  0  0
 0  0      1    303    135   1236    0    0     0     0  113  252  0  0 100  0  0
 0  0      1    303    135   1236    0    0     0     0   91  233  0  0 100  0  0
 0  0      1    303    135   1236    0    0     0     0   92  246  0  0 100  0  0
 0  0      1    303    135   1236    0    0     0     0   86  234  0  0 100  0  0
 0  0      1    303    135   1236    0    0     0     0   96  266  0  0 100  0  0
```
for 1M=1024KB, use `-S M` instead.


####Procs
Permalink
The procs data reports the number of processing jobs waiting to run and allows you to determine if there are processes “blocking” your system from running smoothly.
    
The `r` column displays the total number of processes waiting for access to the processor. 

The `b` column displays the total number of processes in a “sleep” state.
    
These values are often 0.

####MemoryPermalink
The information displayed in the memory section provides the same data about memory usage as the command `free -m`.

The `swpd` or “swapped” column reports how much memory has been swapped out to a swap file or disk. 

The `free` column reports the amount of unallocated memory. 

The `buff` or “buffers” column reports the amount of allocated memory in use. 

The `cache` column reports the amount of allocated memory that could be swapped to disk or unallocated if the resources are needed for another task.

####SwapPermalink
The swap section reports the rate that memory is sent to or retrieved from the swap system. By reporting “swapping” separately from total disk activity, vmstat allows you to determine how much disk activity is related to the swap system.

What is swap? see swap.md


The `si` column reports the amount of memory that is moved from swap to “real” memory per second. 

The `so` column reports the amount of memory that is moved to swap from “real” memory per second.

####I/OPermalink
The `io` section reports the amount of input and output activity per second in terms of blocks read and blocks written.

The `bi` column reports the number of blocks received, or “blocks in”, from a disk per second. The bo column reports the number of blocks sent, or “blocks out”, to a disk per second.

#### SystemPermalink
The system section reports data that reflects the number of system operations per second.

The `in` column reports the number of system interrupts per second, including interrupts from system clock. 

The `cs` column reports the number of context switches that the system makes in order to process all tasks.

CPUPermalink
The `cpu` section reports on the use of the system’s CPU resources. The columns in this section always add to 100 and reflect “percentage of available time”.


The `us` column reports the amount of time that the processor spends on userland tasks, or all non-kernel processes. 

The `sy` column reports the amount of time that the processor spends on kernel related tasks. 

The `id` column reports the amount of time that the processor spends idle. 

The `wa` column reports the amount of time that the processor spends waiting for IO operations to complete before being able to continue processing tasks.

### 2.uptime
```
vagrant@linux:/home/vagrant$ uptime
 15:22:38 up  5:26,  2 users,  load average: 0.00, 0.04, 0.06
```
uptime gives a one line display of the following information. The current time, how long the system has been running, how many users are currently logged on, and the system load averages for the past 1, 5, and 15 minutes.

Load > # of CPUs, may mean CPU saturation.

### 3.top (htop)
System and per-process interval summary: 
```
Tasks: 142 total,   1 running, 106 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.2 sy,  0.0 ni, 99.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem :  2041120 total,   295024 free,   406084 used,  1340012 buff/cache
KiB Swap:  2097148 total,  2095344 free,     1804 used.  1453912 avail Mem

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
17229 root      20   0  907880  44200  25148 S   0.7  2.2   0:18.58 containerd
19715 vagrant   20   0   41804   3696   3072 R   0.3  0.2   0:00.01 top
    1 root      20   0  159956   9080   6504 S   0.0  0.4   0:04.49 systemd
    2 root      20   0       0      0      0 S   0.0  0.0   0:00.00 kthreadd
    4 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 kworker/0:0H
    6 root       0 -20       0      0      0 I   0.0  0.0   0:00.00 mm_percpu_wq
    7 root      20   0       0      0      0 S   0.0  0.0   0:00.28 ksoftirqd/0
    8 root      20   0       0      0      0 I   0.0  0.0   0:00.58 rcu_sched
    ...
```
• %CPU is summed across all CPUs
• Can miss short-lived processes (atop won’t)
• Can consume noticeable CPU to read /proc

