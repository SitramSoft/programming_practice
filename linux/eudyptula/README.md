# My solutions to Eudyptula challenges

## **Task 1**
### **Challenge**
Write a Linux kernel module, and stand-alone Makefile, that when loaded
prints to the kernel debug log level, "Hello World!"  Be sure to make
the module be able to be unloaded as well.

The Makefile should build the kernel module against the source for the
currently running kernel, or, use an environment variable to specify
what kernel tree to build it against.

Please show proof of this module being built, and running, in your
kernel.  What this proof is is up to you, I'm sure you can come up with
something.  Also be sure to send the kernel module you wrote, along with
the Makefile you created to build the module.

Remember to use your ID assigned to you in the Subject: line when
responding to this task, so that I can figure out who to attribute it
to.  You can just respond to the task with the answers and all should be
fine.

If you forgot, your id is "7c1caf2f50d1".  But of course you have not
forgotten that yet, you are better than that.

### **Solution**
 - prepare the linux machine with the essential development tools and kernel headers
```
apt-get install build-essential linux-headers-`uname -r`
```
  - create empty file **Makefile** and **hello_world.c**
  - command line to build an external module using the kbuild system is below. 
    - **-C <path_to_kernel_source>** -> refers to the path of the kernel source directory. 
    - **M=$PWD** -> path of the directory where the external module is located. 
    - **Target** -> *modules*, *modules_install*, *clean*, *help*
```
make -C /lib/modules/`uname -r`/build M=$PWD [target]
```
  - module name and what files to use to build it is specified in either a "Kbuild" or "Makefile" using the syntax below:
```
obj-m := <module_name>.o
<module_name>-y := <src1>.o <src2>.o ...
```
  - MODULE_LICENSE can be set to a variety of values in the source code. A full list can be obtained running the command:
```
grep "MODULE_LICENSE" -B 27 /usr/src/linux-headers-`uname -r`/include/linux/module.h
```
  - **printk** is used instead of **printf** with a KERN_INFO parameter without a comma. The kernel sorts this out inside the printk function to save stack memory.
  - inserting the module in the kernel
```
sudo insmod <module_name>.ko
```
  - checking the kernel log for outputs from the module
```
  sudo dmesg
```
  - checking if the module is loaded in kernel
```
  lsmod | grep "<module_name>"
```
  - removing the module from the kernel
```
sudo rmmod <module_name>
```
  - in order to automate the testing of a kernel module, a make rule can be used
```
	sudo dmesg -C
	sudo insmod <module_name>.ko
	sudo rmmod <module_name>.ko
	sudo dmesg
```
  - passing the kernel version to the make file is done using one of the two [Override Directive](http://www.gnu.org/software/make/manual/make.html#Override-Directive) `override_variable = value` or `override_variable := value`. To append more text to a variable defined on the command line use `override_variable += text`
## **Task 2**
### **Challenge**
Now that you have written your first kernel module, it's time to take
off the training wheels and move on to building a custom kernel.  No
more distro kernels for you, for this task you must run your own kernel.
And use git!  Exciting isn't it!  No, oh, ok...

The tasks for this round is:
  - download Linus's latest git tree from git.kernel.org (you have to
    figure out which one is his, it's not that hard, just remember what
    his last name is and you should be fine.)
  - build it, install it, and boot it.  You can use whatever kernel
    configuration options you wish to use, but you must enable
    CONFIG_LOCALVERSION_AUTO=y.
  - show proof of booting this kernel.  Bonus points for you if you do
    it on a "real" machine, and not a virtual machine (virtual machines
    are acceptable, but come on, real kernel developers don't mess
    around with virtual machines, they are too slow.  Oh yeah, we aren't
    real kernel developers just yet.  Well, I'm not anyway, I'm just a
    script...)  Again, proof of running this kernel is up to you, I'm
    sure you can do well.

Hint, you should look into the 'make localmodconfig' option, and base
your kernel configuration on a working distro kernel configuration.
Don't sit there and answer all 1625 different kernel configuration
options by hand, even I, a foolish script, know better than to do that!

After doing this, don't throw away that kernel and git tree and
configuration file.  You'll be using it for later tasks, a working
kernel configuration file is a precious thing, all kernel developers
have one they have grown and tended to over the years.  This is the
start of a long journey with yours, don't discard it like was a broken
umbrella, it deserves better than that.

Remember to use your ID assigned to you in the Subject: line when
responding to this task, so that I can figure out who to attribute it
to.

If you forgot, your id is "7c1caf2f50d1".  But why do I repeat myself?
Of course you know your id, you made it through the first task just fine
with it.
### **Solution**
 - [Requirements for building and using a Kernel](http://files.kroah.com/lkn/lkn_pdf/ch02.pdf)
    - checking **compiler** version is done with `gcc --version`
    - checking **linker** version is done with `ld -v`
    - checking **make** version is done with `make --version`
    - **util-linux** package is a collection of small utilities that do a whole range of tasks. Checking the version is done with `fdformat --version`
    - **module-init-tools** package is needed for Linux kernel modules. Checking the version is done with `depmod -V`
    To work with any of the ext2/ext3/ext4 filesystems, **e2fsprogrs** package must be installed. Checking the version is done with `tune2fs`
    - For managing and monitoring processes, **procps** package has to be installed. Checking the version is done with `ps --version`
  - [Git repositories](https://git.kernel.org/)
     - [torvalds/linux.git](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/): the main tree with the latest Linux releases. Used to define Release Candidate version (-rc). This tree changes only when a new release (or Release Candidate) is created each 7 to 10 days approximately. Maintained by Linus Torvalds
     - [stable/linux.git](https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/): Linux's stable tree repository. Used to store and update stable releases over time. The main difference between this repository and the main Linux tree is that this repository's releases will be updated (mainly security updates and bugfixes) over time if the related release is supported.
      - [next/linux-next.git](https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git/): All the different subsystem trees and their modifications are merged into it each day. It contains the latest, most complete Linux kernel tree.
      - [gregkh/staging.git](https://git.kernel.org/pub/scm/linux/kernel/git/gregkh/staging.git/): This tree stores all the modifications applied to the staging drivers (released drivers but isolated from the others as they are not finished yet). This tree is a nice source of contributions as all these drivers need to be cleaned up and adapted to the latest kernel's API. Maintained by Greg Kroah-Hartman.
  - Linux Kernel configuration
    - `make defconfig`: create a default .config file with all the options that suits your current architecture.
    - `make config` / `make nconfig` / `make menuconfig`: used to interactively change kernel's options.
    - `make oldconfig`: create a .config file using the one currently available. Useful if you want to build a new kernel with all the options used in an older one.
    - `make randconfig`: randomly enable / disable options. Used to test purposes.
    - `make tinyconfig`: create the tiniest kernel possible.
    - `make kvmconfig`: update the current configuration with KVM support
    - `make olddefconfig`: Use old `.config` and will answer default values to all new options, making `.config` applicable to new kernel
    - `make localmodconfig`: Disable in `.config` all modules that are not currently loaded on the machine, using `lsmod` output
  - Building the Linux Kernel
    - `make`: build the kernel using the configuration selected
    - `make -jx`:build the kernel in a multithreaded way for every subdirectory in the kernel tree. It is best to use a number that matches twice the number of processors in the system.
    - Building only a portion of the Kernel
      - `make <directory_or_file>`: build a specific subdirectory or a single file
      - `make M=<directory_or_file>`: Build all the needed files in that directory and link the file module images.
      - Final kernel image is not build using either of the building ways above. `make` command needs to be executed at the end.
    - `make O=<path>`: control where the output of the kernel build
    - `make ARCH=<architecture> defconfig`: Get the default kernel configuration for a specific architecture
    - `make ARCH=<architecture> CROSS_COMPILE=<cross_compile_toolchain>`: Build the Linux Kernel with for a specific architecture with it's associated toolchain
    - `make CC=<compiler>`: Change what the build system uses as a compiler. Example `distcc` or `ccache` to reduce the time it takes to build the kernel
  - [Install and Boot from a build Kernel](http://files.kroah.com/lkn/lkn_pdf/ch05.pdf)
    - `sudo make modules_install`: install all the modules build and place them in */lib/modules/kernel_version* for the new kernel to find them.
    - `make install`
      - Automatic installation using `installkernel` script from package `mkinitrd`
        - check that the kernel is successfully built
        - install the static kernel portion into the /boot directory, renaming the file based on the kernel version
        - create initial ramdisk images with the modules that have been installed 
        - notify bootloader program about the new kernel to be added in the booting menu. Older kernel images are not overwritten and can be selected from booting menu.
        - reboot the system
      - Manual installation
        - `make kernelversion`: Obtain the version of the built kernel
        - `cp arch/<arch>/boot/bzImage /boot/bzImage-KERNEL_VERSION`: copy kernel image 
        - `cp System.map /boot/System.map-KERNEL_VERSION` copy System.map file
        - Modify the bootloader for the new kernel
          - LILO
            - `ls /etc/lilo.conf`: check if LILO bootloader is installed
            - TODO: add steps for introducing a new kernel in the bootloader
          - GRUB
            - `ls -F /boot | grep grub`: check if GRUB bootloader is installed
            - GRUB configuration can be edited in `/etc/default/grub` on Debian. Make sure to run `sudo update-grub` afterwards to update `/boot/grub/grub.cfg`
            - TODO: add steps for introducing a new kernel in the bootloader
      - Remove compiled kernel from locations below on Ubuntu and update grub configuration with `sudo update-grub2`

            /boot/vmlinuz*KERNEL-VERSION*
            /boot/initrd.img*KERNEL-VERSION*
            /boot/System.map*KERNEL-VERSION*
            /boot/config-*KERNEL-VERSION*
            /lib/modules/*KERNEL-VERSION*/
            /var/lib/initramfs-tools/*KERNEL-VERSION*/
      - `dpkg --list | egrep -i --color 'linux-image|linux-headers|linux-modules' | awk '{ print $2 }'`: List Ubuntu kernels installed 
      - `sudo apt purge linux-*-5.8.0-48-*`: example of removing all packages related to a certain kernel version. Review the packages before confirming to be removed.

## **Task 3**
### **Challenge**
Now that you have your custom kernel up and running, it's time to modify
it!

The tasks for this round is:
  - take the kernel git tree from Task 02 and modify the Makefile to
    and modify the EXTRAVERSION field.  Do this in a way that the
    running kernel (after modifying the Makefile, rebuilding, and
    rebooting) has the characters "-eudyptula" in the version string.
  - show proof of booting this kernel.  Extra cookies for you by
    providing creative examples, especially if done in intrepretive
    dance at your local pub.
  - Send a patch that shows the Makefile modified.  Do this in a manner
    that would be acceptable for merging in the kernel source tree.
    (Hint, read the file Documentation/SubmittingPatches and follow the
    steps there.)

Remember to use your ID assigned to you in the Subject: line when
responding to this task, so that I can figure out who to attribute it
to.

If you forgot, your id is "7c1caf2f50d1".  Surely I don't need to keep
saying this right?  I know, _you_ wouldn't forget, but someone else, of
course they would, so I'll just leave it here for those "others".
### **Solution**
  - If Linux kernel images are being built with "-dirty" on the end of the version string, this simply means that modifications in the source directory have not been committed. Use git status to check for uncommitted files
  - The steps needed to find the driver for a device that has a working driver already bound to it:
    - Find the proper sysfs class device that the device is bound to.Network
devices are listed in /sys/class/net and tty devices in /sys/class/tty.Other types of devices are listed in other directories in /sys/class, depending on the type of device.
    - Trace through the sysfs tree to find the module name that controls this
device.It will be found in the /sys/class/class_name/device_name/device/driver/module, and can be displayed using the readlink and basename applications:

          $ basename `readlink /sys/class/class_name/device_name/device/driver/module`
    - Search the kernel Makefiles for the CONFIG_ rule that builds this module name by using find and grep:

          $ find -type f -name Makefile | xargs grep module_name
    - Search in the kernel configuration system for that configuration value and go to the location in the menu that it specifies to enable that driver to be built.

## **Task 4**
### **Challenge**
Wonderful job in making it this far, I hope you have been having fun.
Oh, you're getting bored, just booting and installing kernels?  Well,
time for some pedantic things to make you feel that those kernel builds
are actually fun!

Part of the job of being a kernel developer is recognizing the proper
Linux kernel coding style.  The full description of this coding style
can be found in the kernel itself, in the Documentation/CodingStyle
file.  I'd recommend going and reading that right now, it's pretty
simple stuff, and something that you are going to need to know and
understand.  There is also a tool in the kernel source tree in the
scripts/ directory called checkpatch.pl that can be used to test for
adhering to the coding style rules, as kernel programmers are lazy and
prefer to let scripts do their work for them...

And why a coding standard at all?  That's because of your brain (yes,
yours, not mine, remember, I'm just some dumb shell scripts).  Once your
brain learns the patterns, the information contained really starts to
sink in better.  So it's important that everyone follow the same
standard so that the patterns become consistent.  In other words, you
want to make it really easy for other people to find the bugs in your
code, and not be confused and distracted by the fact that you happen to
prefer 5 spaces instead of tabs for indentation.  Of course you would
never prefer such a thing, I'd never accuse you of that, it was just an
example, please forgive my impertinence!

Anyway, the tasks for this round all deal with the Linux kernel coding
style.  Attached to this message are two kernel modules that do not
follow the proper Linux kernel coding style rules.  Please fix both of
them up, and send it back to me in such a way that does follow the
rules.

What, you recognize one of these modules?  Imagine that, perhaps I was
right to accuse you of the using a "wrong" coding style :)

Yes, the logic in the second module is crazy, and probably wrong, but
don't focus on that, just look at the patterns here, and fix up the
coding style, do not remove lines of code.

As always, please remember to use your ID assigned to you in the
Subject: line when responding to this task, so that I can figure out who
to attribute it to.  And if you forgot (which of course you have not,
we've been through all of this before), your id is "7c1caf2f50d1".
### **Solution**

## **Task 5**
### **Challenge**
Yeah, you survived the coding style mess!  Now, on to some "real"
things, as I know you are getting bored by these so far.

So, simple task this time around:
  - take the kernel module you wrote for task 01, and modify it so that
    when a USB keyboard is plugged in, the module will be automatically
    loaded by the correct userspace hotplug tools (which are implemented
    by depmod / kmod / udev / mdev / systemd, depending on what distro
    you are using.)

Yes, so simple, and yet, it's a bit tricky.  As a hint, go read chapter
14 of the book, "Linux Device Drivers, 3rd edition."  Don't worry, it's
free, and online, no need to go buy anything.

As always, please remember to use your ID assigned to you, yadda yadda
yadda...  It's "7c1caf2f50d1" of course.
### **Solution**

## **Task 6**
### **Challenge**
Nice job with the module loading macros, those are tricky, but a very
valuable skill to know about, especially when running across them in
real kernel code.

Speaking of real kernel code, let's write some!

The task this time is this:
  - Take the kernel module you wrote for task 01, and modify it to be a
    misc char device driver.  The misc interface is a very simple way to
    be able to create a character device, without having to worry about
    all of the sysfs and character device registration mess.  And what a
    mess it is, so stick to the simple interfaces wherever possible.
  - The misc device should be created with a dynamic minor number, no
    need running off and trying to reserve a real minor number for your
    test module, that would be crazy.
  - The misc device should implement the read and write functions.
  - The misc device node should show up in /dev/eudyptula.
  - When the character device node is read from, your assigned id is
    returned to the caller.
  - When the character device node is written to, the data sent to the
    kernel needs to be checked.  If it matches your assigned id, then
    return a correct write return value.  If the value does not match
    your assigned id, return the "invalid value" error value.
  - The misc device should be registered when your module is loaded, and
    unregistered when it is unloaded.
  - Provide some "proof" this all works properly.

As you will be putting your id into the kernel module, of course you
haven't forgotten it, but just to be safe, it's "7c1caf2f50d1".
### **Solution**

## **Task 7**
### **Challenge**
Great work with that misc device driver.  Isn't that a nice and simple
way to write a character driver?

Just when you think this challenge is all about writing kernel code,
this task is a throwback to your second one.  Yes, that's right,
building kernels.  Turns out that's what most developers end up doing,
tons and tons of rebuilds, not writing new code.  Sad, but it is a good
skill to know.

The tasks this round are:
  - Download the linux-next kernel for today.  Or tomorrow, just use
    the latest one.  It changes every day so there is no specific one
    you need to pick.  Build it.  Boot it.  Provide proof that you built
    and booted it.

What is the linux-next kernel?  Ah, that's part of the challenge.

For a hint, you should read the excellent documentation about how the
Linux kernel is developed in Documentation/development-process/ in the
kernel source itself.  It's a great read, and should tell you all you
never wanted to know about what Linux kernel developers do and how they
do it.

As always, please respond to this challenge with your id.  I know you
know what it is.  I'll not even include it this time, I trust you.
Don't make me feel that is a mistake.
### **Solution**

## **Task 8**
### **Challenge**
We will come back to the linux-next kernel in a later exercise, so don't
go and delete that directory, you'll want it around.  But enough of
building kernels, let's write more code!

This task is much like the 06 task with the misc device, but this time
we are going to focus on another user/kernel interface, debugfs.  It is
rumored that the creator of debugfs said that there is only one rule for
debugfs use, "There are no rules when using debugfs."  So let's take
them up on that offer and see how to use it.

debugfs should be mounted by your distro in /sys/kernel/debug/, if it
isn't, then you can mount it with the line:
        mount -t debugfs none /sys/kernel/debug/

Make sure it is enabled in your kernel, with the CONFIG_DEBUG_FS option,
you will need it for this task.

The task, in specifics is:

  - Take the kernel module you wrote for task 01, and modify it to be
    create a debugfs subdirectory called "eudyptula".  In that
    directory, create 3 virtual files called "id", "jiffies", and "foo".
  - The file "id" operates just like it did for example 06, use the same
    logic there, the file must be readable and writable by any user.
  - The file "jiffies" is to be read only by any user, and when read,
    should return the current value of the jiffies kernel timer.
  - The file "foo" needs to be writable only by root, but readable by
    anyone.  When writing to it, the value must be stored, up to one
    page of data.  When read, which can be done by any user, the value
    must be returned that is stored it it.  Properly handle the fact
    that someone could be reading from the file while someone else is
    writing to it (oh, a locking hint!)
  - When the module is unloaded, all of the debugfs files are cleaned
    up, and any memory allocated is freed.
  - Provide some "proof" this all works.

Again, you are using your id in the code, so you know what it is by now,
no need to repeat it again.

### **Solution**

## Task 9**
### Challenge**
Nice job with debugfs, that is a handy thing to remember when wanting to
print out some debugging information.  Never use /proc/ that is only for
processes, use debugfs instead.

Along with debugfs, sysfs is a common place to put information that
needs to move from the user to the kernel.  So let us focus on sysfs for
this task.

The task this time:

  - Take the code you wrote in task 08, and move it to sysfs.  Put the
    "eudyptula" directory under the /sys/kernel/ location in sysfs.
  - Provide some "proof" this works.

That's it!  Simple, right?  No, you are right, it's more complex, sysfs
is complicated.  I'd recommend reading Documentation/kobject.txt as a
primer on how to use kobjects and sysfs.

Feel free to ask for hints and help with this one if you have questions
by sending in code to review if you get stuck, many people have dropped
out in the challenge at this point in time, so don't feel bad about
asking, we don't want to see you go away just because sysfs is so damn
complicated.
### Solution**

## **Task 10**
### **Challenge**
Yeah, you conquered the sysfs monster, great job!

Now you know to never want to mess with a kobject again, right?  Trust
me, there are easier ways to create sysfs files, and we will get into
that for a future task, but for now, let's make it a bit more simple
after all of that coding.

For this task, go back to the linux-next tree you used for task 07.
Update it, and then do the following:
  - Create a patch that fixes one coding style problem in any of the
    files in drivers/staging/
  - Make sure the patch is correct by running it through
    scripts/checkpatch.pl
  - Submit the code to the maintainer of the driver/subsystem, finding
    the proper name and mailing lists to send it to by running the tool,
    scripts/get_maintainer.pl on your patch.
  - Send a web link back to me of your patch on the public mailing list
    archive (don't cc: me on the patch, that will only confuse me and
    everyone in the kernel development community.)
  - If you want to mention the Eudyptula Challenge as the reason for
    writing the patch, feel free to do so in the body of the patch, but
    it's not necessary at all.

Hopefully this patch will be accepted into the kernel tree, and all of a
sudden, you are an "official" kernel developer!

Don't worry, there's plenty more tasks coming, but a little breather
every now and again for something simple is always nice to have.
### **Solution**

## **Task 11**
### **Challenge**
You made a successful patch to the kernel source tree, that's a great
step!

But, let's not rest, time to get back to code.

Remember that mess of kobject and sysfs code back in task 09?  Let's
move one level up the tree and start to mess with devices and not raw
kobjects.

For this task:
  - Write a patch against any driver that you are currently using on
    your machine.  So first you have to figure out which drivers you are
    using, and where the source code in the kernel tree is for that
    driver.
  - In that driver, add a sysfs file to show up in the /sys/devices/
    tree for the device that is called "id".  As you might expect, this
    file follows the same rules as task 09 as for what you can read and
    write to it.
  - The file is to show up only for devices that are controlled by a
    single driver, not for all devices of a single type (like all USB
    devices.  But all USB maibox LEDs would be acceptable, if you happen
    to have the device that that driver controls.)

Submit both the patch, in proper kernel commit form, and "proof" of it
working properly on your machine.

And as always, please use your id in the subject line.  If you happened
to forget it, as it has been a while since I reminded you of it, it is
"7c1caf2f50d1".
### **Solution**

## **Task 12**
### **Challenge**
Nice job with the driver patch.  That took some work in finding the
proper place to modify, and demonstrates a great skill in tracking down
issues when you can't get a specific piece of hardware working.

Now let's step back from drivers (they are boring things), and focus on
the kernel core.  To do that, we need to go way back to the basics --
stuff you would learn in your "intro to data structures" class, if you
happened to take one.

Yes, I'm talking about linked lists.

The kernel has a unique way of creating and handling linked lists, that
is quite different than the "textbook" way of doing so.  But, it turns
out to be faster, and simpler, than a "textbook" would describe, so
that's a good thing.

For this task, write a kernel module, based on your cleaned up one from
task 04, that does the following:
  - You have a structure that has 3 fields:
        char  name[20];
        int   id;
        bool  busy;
    name this structure "identity".
  - Your module has a static variable that points to a list of these
    "identity" structures.
  - Write a function that looks like:
        int identity_create(char *name, int id)
    that creates the structure "identity", copies in the 'name' and 'id'
    fields and sets 'busy' to false.  Proper error checking for out of
    memory issues is required.  Return 0 if everything went ok; an error
    value if something went wrong.
  - Write a function that looks like:
        struct identity *identity_find(int id);
    that takes a given id, iterates over the list of all ids, and
    returns the proper 'struct identity' associated with it.  If the
    identity is not found, return NULL.
  - Write a function that looks like:
        void identity_destroy(int id);
    that given an id, finds the proper 'struct identity' and removes it
    from the system.
  - Your module_init() function will look much like the following:

        struct identity *temp;

        identity_create("Alice", 1);
        identity_create("Bob", 2);
        identity_create("Dave", 3);
        identity_create("Gena", 10);

        temp = identity_find(3);
        pr_debug("id 3 = %s\n", temp->name);

        temp = identity_find(42);
        if (temp == NULL)
                pr_debug("id 42 not found\n");

        identity_destroy(2);
        identity_destroy(1);
        identity_destroy(10);
        identity_destroy(42);
        identity_destroy(3);

   Bonus points for properly checking return values of the above
   functions.

As always, please send the full module (following the proper kernel
coding style rules), and "proof" of it working properly.  And remember
to use your id of "7c1caf2f50d1" in the Subject line properly.
### **Solution**

## **Task 13**
### **Challenge**
Weren't those lists fun to play with?  You should get used to them, they
are used all over the kernel in lots of different places.

Now that we are allocating a structure that we want to use a lot of, we
might want to start caring about the speed of the allocation, and not
have to worry about the creation of those objects from the "general"
memory pools of the kernel.

This task is to take the code written in task 12, and cause all memory
allocated from the 'struct identity' to come from a private slab cache
just for the fun of it.

Instead of using **kmalloc()** and **kfree()** in the module, use
**kmem_cache_alloc()** and **kmem_cache_free()** instead.  Of course this means
you will have to initialize your memory cache properly when the module
starts up.  Don't forget to do that.  You are free to name your memory
cache whatever you wish, but it should show up in the **/proc/slabinfo**
file.

Don't send the full module for this task, only a patch with the diff
from task 12 showing the lines changed.  This means you will have to
keep a copy of your 12 task results somewhere to make sure you don't
overwrite them.

Also show the output of **/proc/slabinfo** with your module loaded.
### **Solution**

## **Task 14**
### **Challenge**
Now that you have the basics of lists, and we glossed over the custom
allocators (the first cut at that task was much harder, you got off
easy), it's time to move on to something a bit more old-school: tasks.

For this task:
  - Add a new field to the core kernel task structure called, wait for
    it, "id".
  - When the task is created, set the id to your id.  Imaginative, I
    know.  You try writing these tasks.
  - Add a new proc file for every task called, "id", located in the
    /proc/${PID}/ directory for that task.
  - When the proc file is read from, have it print out the value of
    your id, and then increment it by one, allowing different tasks to
    have different values for the "id" file over time as they are read
    from.
  - Provide some "proof" it all works properly.

As you are touching files all over the kernel tree, a patch is the
required result to be sent in here.  Please specify which kernel version
you make this patch against, to give my virtual machines a chance to
figure out how to apply it.

Also provide some kind of proof that you tested the patch.

And, in case you happened to forget it, your id is "7c1caf2f50d1".
### **Solution**

## **Task 15**
### **Challenge**
That process task turned out to not be all that complex, but digging
through the core kernel was a tough task, nice work with that.

Speaking of "core kernel" tasks, let's do another one.  It's one of the
most common undergraduate tasks there is: create a new syscall!
Yeah, loads of fun, but it's good to know the basics of how to do this,
and, how to call it from userspace.

For this task:
  - Add a new syscall to the kernel called "sys_eudyptula", so this is
    all going to be changes to the kernel tree itself, no stand-alone
    module needed for this task (unless you want to do it that way
    without hacking around the syscall table, if so, bonus points for
    you...)
  - The syscall number needs to be the next syscall number for the
    architecture you test it on (some of you all are doing this on ARM
    systems, showoffs, and syscall numbers are not the same across all
    architectures).  Document the arch you are using and why you picked
    this number in the module.
  - The syscall should take two parameters: int high_id, int low_id.
  - The syscall will take the two values, mush them together into one
    64bit value (low_id being the lower 32bits of the id, high_id being
    the upper 32bits of the id).
  - If the id value matches your id (which of course you know as
    "7c1caf2f50d1", then the syscall returns success.  Otherwise it
    returns a return code signifying an invalid value was passed to it.
  - Write a userspace C program that calls the syscall and properly
    exercises it (valid and invalid calls need to be made).
  - "Proof" of running the code needs to be provided.

So you need to send in a .c userspace program, a kernel patch, and
"proof" that it all works, as a response.
### **Solution**

## **Task 16**
### **Challenge**
Good job with the new syscall.  The odds of you ever having to write a
new syscall is pretty rare, but now you know where to look them up, and
what the code involved in creating one looks like, which is useful when
you try to debug things.

Let's take a breather after all of that code, and go back to doing a bit
of reading, and learn some more about some common kernel tools.

Go install the tool 'sparse'.  It was started by Linus as a
static-analysis tool that acts much like a compiler.  The kernel build
system is set up to have it run if you ask it to, and it will report a
bunch of issues in C code that are really specific to the kernel.

When you build the kernel, pass the "C=1" option to the build, to have
sparse run on the .c file before gcc is run.  Depending on the file,
nothing might be printed out, or something might.  Here's an example of
it being run on the ext4 code:

    $ make C=1 M=fs/ext4
    CHECK   fs/ext4/balloc.c
    CC      fs/ext4/balloc.o
    CHECK   fs/ext4/bitmap.c
    CC      fs/ext4/bitmap.o
    CHECK   fs/ext4/dir.c
    CC      fs/ext4/dir.o
    CHECK   fs/ext4/file.c
    CC      fs/ext4/file.o
    CHECK   fs/ext4/fsync.c
    CC      fs/ext4/fsync.o
    CHECK   fs/ext4/ialloc.c
    CC      fs/ext4/ialloc.o
    CHECK   fs/ext4/inode.c
    CC      fs/ext4/inode.o
    CHECK   fs/ext4/page-io.c
    CC      fs/ext4/page-io.o
    CHECK   fs/ext4/ioctl.c
    CC      fs/ext4/ioctl.o
    CHECK   fs/ext4/namei.c
    CC      fs/ext4/namei.o
    CHECK   fs/ext4/super.c
    CC      fs/ext4/super.o
    CHECK   fs/ext4/symlink.c
    CC      fs/ext4/symlink.o
    CHECK   fs/ext4/hash.c
    CC      fs/ext4/hash.o
    CHECK   fs/ext4/resize.c
    CC      fs/ext4/resize.o
    CHECK   fs/ext4/extents.c
    CC      fs/ext4/extents.o
    CHECK   fs/ext4/ext4_jbd2.c
    CC      fs/ext4/ext4_jbd2.o
    CHECK   fs/ext4/migrate.c
    CC      fs/ext4/migrate.o
    CHECK   fs/ext4/mballoc.c
    fs/ext4/mballoc.c:5018:9: warning: context imbalance in 'ext4_trim_extent' - unexpected unlock
    CC      fs/ext4/mballoc.o
    CHECK   fs/ext4/block_validity.c
    CC      fs/ext4/block_validity.o
    CHECK   fs/ext4/move_extent.c
    CC      fs/ext4/move_extent.o
    CHECK   fs/ext4/mmp.c
    CC      fs/ext4/mmp.o
    CHECK   fs/ext4/indirect.c
    CC      fs/ext4/indirect.o
    CHECK   fs/ext4/extents_status.c
    CC      fs/ext4/extents_status.o
    CHECK   fs/ext4/xattr.c
    CC      fs/ext4/xattr.o
    CHECK   fs/ext4/xattr_user.c
    CC      fs/ext4/xattr_user.o
    CHECK   fs/ext4/xattr_trusted.c
    CC      fs/ext4/xattr_trusted.o
    CHECK   fs/ext4/inline.c
    CC      fs/ext4/inline.o
    CHECK   fs/ext4/acl.c
    CC      fs/ext4/acl.o
    CHECK   fs/ext4/xattr_security.c
    CC      fs/ext4/xattr_security.o
    LD      fs/ext4/ext4.o
    LD      fs/ext4/built-in.o
    Building modules, stage 2.
    MODPOST 0 modules

As you can see, only one warning was found here, and odds are, it is a
false-positive, as I'm sure those ext4 developers know what they are
doing with their locking functions, right?

Anyway the task this time is:
  - Run sparse on the drivers/staging/ directory, yes, that horrible
    code again, sorry.
  - Find one warning that looks interesting.
  - Write a patch that resolves the issue.
  - Make sure the patch is correct by running it through
    scripts/checkpatch.pl
  - Submit the code to the maintainer of the driver/subsystem, finding
    the proper name and mailing lists to send it to by running the tool,
    scripts/get_maintainer.pl on your patch.
  - Send a web link back to me of your patch in the public mailing list
    archive (don't cc: me on the patch, that will only confuse me and
    everyone in the kernel development community.)
  - If you want to mention the Eudyptula Challenge as the reason for
    writing the patch, feel free to do so in the body of the patch, but
    it's not necessary at all.

That's it, much like task 10 was, but this time you are fixing logical
issues, not just pesky coding style issues.  You are a real developer
now, fixing real bugs!
### **Solution**

## **Task 17**
### **Challenge**
Another patch made and sent in.  See, that wasn't so hard.  Keep sending
in kernel patches outside of this challenge, those lazy kernel
developers need all the help they can get in cleaning up their code.

It is time to start putting the different pieces of what we have done in
the past together, into a much larger module, doing more complex things.
Much more like what a "real" kernel module has to do.

Go dig up your code from task 06, the misc char device driver, and make
the following changes:

 - Delete the read function.  You don't need that anymore, so make it a
   write-only misc device and be sure to set the mode of the device to
   be write-only, by anyone.  If you do this right, udev will set up the
   node automatically with the correct permissions.
 - Create a wait queue, name it "wee_wait".
 - In your module init function, create a kernel thread, named of course
   "eudyptula".
 - The thread's main function should not do anything at this point in
   time, except make sure to shutdown if asked to, and wait on the
   "wee_wait" waitqueue.
 - In your module exit function, shut down the kernel thread you started
   up.

Load and unload the module and "prove" that it works properly (that the
thread is created, it can be found in the process list, and that the
device node is created with the correct permission value.)  Send in the
proof and the .c file for the module.

Be sure to keep this code around, as we will be doing more with it next
time.
### **Solution**

## **Task 18**
### **Challenge**
Nice job with the kernel thread.  It really doesn't take much code at
all to create a new thread.  So now let us get some data into the module
to give the thread something to do.

Base all of this work on your task 17 codebase.

Go back and dig up task 12's source code, the one with the list
handling. Copy the structure into this module, and the
**identity_create()**, **identity_find()**, and **identity_destroy()** functions
into this module as well.

Write a new function, **identity_get()**, that looks like:

    struct identity identity_get(void);

and returns the next "identity" structure that is on the list, and
removes it from the list.  If nothing is on the list, return NULL.

Then, hook up the misc char device "write" function to do the following:
  - If a write is larger than 19 characters, truncate it at 19.
  - Take the write data and pass it to identity_create() as the string,
    and use an incrementing counter as the "id" value.
  - Wake up the "wee_wait" queue.

In the kernel thread function:
  - If the "wee_wait" queue wakes us up, get the next identity in the
    system with a call to **identity_get()**.
  - Sleep (in an interruptable state, don't go increasing the system
    load in a bad way) for 5 seconds.
  - Write out the identity name, and id to the debug kernel log and then
    free the memory.

When the module exits, clean up the whole list by using the functions
given, no fair mucking around with the list variables directly.

Yes, it's a bit clunky, but it shows the basics of taking work from
userspace, and then quickly returning to the user, and then going off
and doing something else with the data and cleaning everything up.  It's
a common pattern for a kernel, as it's really all that a kernel ends up
doing most of the time (get a disk block, write a disk block, handle a
mouse event, etc.)

Load and unload the module and "prove" that it works properly by writing
and looking at the debug log, and that everything cleans up properly
when the module is unloaded.

Send in the proof and the .c file for the module.

A good test script would be the following:

    echo "Alice" > /dev/eudyptula
    echo "Bob" > /dev/eudyptula
    sleep 15
    echo "Dave" > /dev/eudyptula
    echo "Gena" > /dev/eudyptula
    rmmod task18

Removing the module while there is pending work is always a good stress
test.

### **Solution**

## **Task 19
### **Challenge**
Handling delayed work is easy now, right?  So, time to move on to
something totally different.  How about networking?  We have been
ignoring that part of the kernel, so let us now focus on the network
side of the kernel, as that is a huge reason for why Linux has taken
over the world.

For this task, write a netfilter kernel module that does the following:
  - monitors all IPv4 network traffic that is coming into the machine
  - prints the id to the kernel debug log if the network traffic stream
    contains your id.
  - properly unregisters you from the netfilter core when the module
    unloads.

Test this by sending yourself an email with your id in the subject, much
like the email you need to send back to me.

Send in the proof and the .c file for the module.
### **Solution**

## **Task 20**
### **Challenge**
Networking filters turned out to be not all that complex in the end,
great work with that.

So, here's the final task.

There might be other tasks that get created and sent out later on, but
the original challenge had 20 tasks, so after finishing this one, you
can consider yourself done!

Let's try something a bit harder.  Something that might cause some data
loss on a filesystem, always a fun thing to play with, if for no other
reason than to not be afraid of things like that in the future.

This task requires you to work on the fat filesystem code:
  - Add an ioctl to modify the volume label of a mounted fat filesystem.
    Be sure to handle both 16 and 32 bit fat filesystems {hint!}
  - Provide a userspace .c program to test this new ioctl.

That's it!  Seems so simple, right?  I wonder why that option isn't in
the kernel tree already...

Anyway, provide a patch to the kernel, and the .c file used to test the
new ioctl, as well as "proof" of this working.  Make sure you don't run
into 32/64bit kernel issues with the ioctl, if you do things correctly,
you shouldn't have any problems.

I recommend doing this work on either a loop-back fat filesystem on your
"normal" filesystem, or on a USB stick.  Either will work just as well,
and make things easier to debug and test.

Watch out for locking issues, as well as dirty filesystem state
problems.

Best of luck!
### **Solution**