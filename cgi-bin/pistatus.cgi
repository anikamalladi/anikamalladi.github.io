<html>
<head>
</head>
<body>
<h1>Raspberry Pi Status: rpi01</h1>
<h2>Host Info</h2>
<li>Host name : rpi01</li>
<li>IP Address: 172.19.193.252 </li>
<li>OS name:    Raspbian GNU/Linux 9 (stretch)</li>
<h2>Who is logged in</h2>
<pre>           system boot  Dec 31 16:00
           run-level 5  Jun  4 10:59
LOGIN      tty1         Jun  4 10:59               416 id=tty1
student4 + pts/0        Jun 11 12:03 00:05        6289 (172.19.217.19)
           pts/1        Jun  8 17:07             24522 id=ts/1  term=0 exit=0
           pts/2        Jun  8 16:10             24992 id=ts/2  term=0 exit=0
           tty7         Jun 11 09:30                 0 id=:0    term=0 exit=0</pre>
<h2>Performance Summary</h2>
<pre>top - 12:24:06 up 7 days,  1:24,  1 user,  load average: 0.31, 0.39, 0.42
Tasks: 150 total,   1 running, 107 sleeping,   0 stopped,   0 zombie
%Cpu(s):  3.2 us,  0.3 sy,  0.1 ni, 96.3 id,  0.0 wa,  0.0 hi,  0.1 si,  0.0 st
KiB Mem :   945392 total,   483744 free,   125432 used,   336216 buff/cache
KiB Swap:   102396 total,    79100 free,    23296 used.   745560 avail Mem </pre>
<h2>Top 5 Processes by CPU</h2>
<pre>USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
avahi      314 11.2  0.6   9344  5816 ?        Ss   Jun04 1139:37 avahi-daemon: running [r
www-data  6468  1.0  0.2   3412  2484 ?        S    12:24   0:00 /bin/bash /usr/lib/cgi-bi
root      5587  0.9  0.0      0     0 ?        I    08:57   1:54 [kworker/u8:2]
root      6330  0.4  0.0      0     0 ?        I    12:05   0:04 [kworker/u8:3]
root      5753  0.3  4.7 199416 45260 tty7     Ssl+ 09:30   0:40 /usr/lib/xorg/Xorg :0 -se</pre>
<h2>Top 5 Processes by Memory</h2>
<pre>USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
lightdm   5776  0.3  6.4 178120 60584 ?        Ssl  09:30   0:35 /usr/sbin/pi-greeter
root      5753  0.3  4.7 199416 45260 tty7     Ssl+ 09:30   0:40 /usr/lib/xorg/Xorg :0 -se
root       448  0.0  2.0 119924 19524 ?        Ss   Jun04   0:29 /usr/sbin/apache2 -k star
student2 18549  0.0  1.1  91940 10728 ?        Ssl  Jun07   0:00 /usr/lib/gvfs/gvfs-udisks
student1 10527  0.0  1.0  92964  9720 ?        Ssl  Jun06   0:00 /usr/lib/gvfs/gvfs-udisks</pre>
</body>
</html>
