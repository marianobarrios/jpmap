# JPMAP

Jpmap is an alternative to Linux's pmap command by Albert Cahalan, augmented for Java Virtual Machine processes. Besides the usual pmap output, jpmap adds information about stack segments. It uses stack pointers from the Java thread dump to map threads with their stack segments, and to show additional information about them.

## Installation

`pip install git+https://github.com/marianobarrios/jpmap.git`

## Sample output

	$ jpmap <pid>
	START ADDRESS          PSS       RSS     DIRTY      VSIZE PERMS  TYPE       FILE/THREAD
	00000000a9bb0000     53888     53888     53888      53888 rw-p   [anon]     
	0000000094650000     11676     11676     11676      16832 rw-p   [anon]     
	000000009064f000     11468     11468     11468      16388 rw-p   [anon]     
	0000000000ef1000      3432      3432       916       7608 r-xp   [vmlib]    /usr/lib/jvm/java-7-oracle/jre/lib/i386/server/libjvm.so
	00000000b4710000      1640      1640      1632       2304 rwxp   [anon]     
	000000008dc00000      1004      1004      1004       1004 rw-p   [anon]     
	000000008db00000       996       996       996        996 rw-p   [anon]     
	000000000165f000       240       240       236        316 rw-p   [vmlib]    /usr/lib/jvm/java-7-oracle/jre/lib/i386/server/libjvm.so
	000000009054f000        36        36        36         36 rw-p   [anon]     
	000000009052f000        32        32        32         32 rw-p   [anon]     
	000000008e51a000        28        28        28        312 rw-p   [stack]    "DMORcvW-sId...3489" lwp=3139 jvm_id=0x9a0fc00
	000000008e6af000        28        28        28        312 rw-p   [stack]    "Sel-Peer-R" lwp=3021 jvm_id=0x8ed3dc00
	000000008ec10000        28        28        28        312 rw-p   [stack]    "W15955619_ScanWrkr" lwp=2943 jvm_id=0x9b34400
	000000000028c000        24        48         0        140 r-xp   [vmlib]    /usr/lib/jvm/java-7-oracle/jre/lib/i386/libjava.so
	00000000003a8000        24        48         0         92 r-xp   [vmlib]    /usr/lib/jvm/java-7-oracle/jre/lib/i386/libzip.so
	000000008f07b000        24        24        24        312 rw-p   [stack]    "QPub-BackupMgr" lwp=2900 jvm_id=0x8f391800
	000000008f410000        24        24        24        312 rw-p   [stack]    "W2193463_SystemWatcher" lwp=2865 jvm_id=0x8f67ec00
	000000008e56b000        20        20        20        312 rw-p   [stack]    "RPConnWrk-DefaultGroup" lwp=3025 jvm_id=0x8f87cc00
	000000008e60d000        20        20        20        312 rw-p   [stack]    "W14725577_RPCtdWrk-DefaultGroup" lwp=3023 jvm_id=0x8ed41000
	000000008e65e000        20        20        20        312 rw-p   [stack]    "Sel-Peer-W" lwp=3022 jvm_id=0x8ed3f800
	...

	$ jpmap <pid> -s
	TYPE             PSS       RSS     DIRTY      VSIZE
	[anon]         90744     90744     90728     662100
	[heap]          5776      5776      5776       6124
	[vmlib]         3934      4924      1244      11164
	[stack]          788       788       784      19656
	[file]            20        36         8       2412
	[exec]             4         4         4          8
	[vdso]             0         4         0          4
	[jlib]             0         0         0       2844
	TOTALS:       101266    102276     98544     704312

## `/proc` implementation

In previous version of this tool, stack pointers were also obtained for the `stat` file in the `proc` filesystem. That had the advantage of also providing pointers for native threads. However [that functionality was removed](https://lore.kernel.org/lkml/20160912152203.052491949@linuxfoundation.org/) from recent kernels because it was not reliable in the end.
