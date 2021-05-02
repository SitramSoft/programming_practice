# If KERNELRELEASE is defined, we've been invoked from the
# kernel build system and can use its language.
ifneq ($(KERNELRELEASE),)
	obj-m := hello_world.o

# Otherwise we were called directly from the command
# line; invoke the kernel build system.
else
	KERNELVER ?= $(shell uname -r)
	KERNELDIR ?= /lib/modules/$(KERNELVER)/build
    	PWD := $(shell pwd)
all:
	$(MAKE) -C $(KERNELDIR) M=$(PWD) modules

clean:
	$(MAKE) -C $(KERNELDIR) M=$(PWD) clean

test:
	sudo dmesg -C
	sudo insmod hello_world.ko
	sudo rmmod hello_world.ko
	sudo dmesg
endif