###What is swap?

Swap is a space on a disk that is used when the amount of physical RAM memory is full. When a Linux system runs out of RAM, inactive pages are moved from the RAM to the swap space. Swap space can take the form of either a dedicated swap partition or a swap file.


### A little background

Your system uses Random Access Memory (aka RAM) when it runs an application. When there are only a few applications running your system manages with the available RAM.

But if there are too many applications running or if the applications need a lot of RAM, then your system gets into trouble. If an application needs more memory but entire RAM is already in use, the application will crash.

Swap acts as a breather to your system when the RAM is exhausted. What happens here is that when the RAM is exhausted, your Linux system uses part of the hard disk memory and allocates it to the running application.

That sounds cool. This means if you allocate like 50GB of swap size, your system can run hundreds or perhaps thousands of applications at the same time? WRONG!

You see, the speed matters here. RAM access data in the order of nanoseconds. An SSD access data in microseconds while as a normal hard disk accesses the data in milliseconds. This means that RAM is 1000 times faster than SSD and 100,000 times faster than the usual HDD.

If an application relies too much on the swap, its performance will degrade as it cannot access the data at the same speed as it would have in RAM. So instead of taking 1 second for a task, it may take several minutes to complete the same task. It will leave the application almost useless. This is known as thrashing in computing terms.

In other words, a little swap is helpful. A lot of it will be of no good use.

###Do we need swap?

If your system has RAM less than 1 GB, you must use swap as most applications would exhaust the RAM soon.

If your system uses resource heavy applications like video editors, it would be a good idea to use some swap space as your RAM may be exhausted here.

If you use hibernation, then you must add swap because the content of the RAM will be written to the swap partition. This also means that the swap size should be at least the size of RAM.
Avoid strange events like a program going nuts and eating RAM.



###Do you need swap if you have lots of RAM?

This is a good question indeed. If you have 32GB or 64 GB of RAM, chances are that your system would perhaps never use the entire RAM and hence it would never use the swap partition.

But will you take the chance? I am guessing if your system has 32GB of RAM, it should also be having a hard disk of 100s of GB. Allocating a couple of GB of swap won’t hurt. It will provide an extra layer of ‘stability’ if a faulty program starts misusing RAM.

###How much should I allocate?
Different os has different suggestions. For Ubuntu:

If RAM is less than 1 GB, swap size should be at least the size of RAM and at most double the size of RAM

If RAM is more than 1 GB, swap size should be at least equal to the square root of the RAM size and at most double the size of RAM

If hibernation is used, swap size should be equal to size of RAM plus the square root of the RAM size
