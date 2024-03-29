---
layout: post
title:  "s4r's Snake (Reverse Engineering)"
date:   2024-03-29 00:14:45 +0530
categories: Reverse Engineering and CTFs
---

This is a problem from Barbhack CTF 2023
We first decompressed the binary which was packed using the UPX executable
packer. I took many hints from another write-up as I'm completely new to packing
and the use of cryptographic algorithms in the binary, So I guess I can't say I
completely solved the problem on my own but, It was still a major learning experience.
I used the chacha20 library very conveniently provided in the write-up. It's the
only solution found at [the crackmes of the problem](https://crackmes.one/crackme/64f1f7afd931496abf909525) by [cnathansmith](https://crackmes.one/user/cnathansmith).

If you want any of the files associated with the blog then [click here](https://github.com/azorfus/azorfus.github.io/tree/blog/resources/barbhackctf20203_s4rssnake).

Its pointless to try reversing the rest of the binary except where
the flag is generated as we can't really do anything to 'bypass' them?
That is what I usually do :P
(New dimension of understanding unlocked xD)
I guess bruteforcing the flag with the constraints is the best bet.
We seem to be using currently unknown password and nonce for decrypting the
encrypted_flag. These two will be our constraints for replicating flag creation.

Figuring out how password is generated: (decompilation from ghidra)
```c
	password[password_idx] = (char)current_fruit_x + password[password_idx];
	password[password_idx] = password[password_idx] * (char)current_fruit_y;
	password_idx = (password_idx + 1) % 0x20;
```
password_idx starts out as 0
password is an empty array initially

If we look through the code although password creation is dependent on the
current fruit's x and y coordinated. These values are completely randomly
generated. We can simulate these values by using the same seed as the game.
We see that srand is seeded in gameplay():
```asm
	call    time
	mov     rcx, rax
	mov     rdx, 0x346dc5d63886594b
	mov     rax, rcx
	imul    rdx
	mov     rax, rdx
	sar     rax, 0xc
	mov     rdx, rcx
	sar     rdx, 0x3f
	sub     rax, rdx
	imul    rdx, rax, 0x4e20
	mov     rax, rcx
	sub     rax, rdx
	mov     edi, eax
	call    srand
```
Magic-number division optimizations...
I read more about magic-number division optimizations on a 
[reverseengineering.stackexchange.com](https://reverseengineering.stackexchange.com/questions/1397/how-can-i-reverse-optimized-integer-division-modulo-by-constant-operations) post, The question provided two instances
of modular operation and division and what we have is very similar to what was
given with the modular operation. Which makes it pretty clear that we are 
just doing this:
```c	
	seed = time(0) % 20000
```
Just to make sure once, I wrote some code in C that did the same and disassembled it.
Here's the dissassembly for the operation % 20000:
```asm
	0x0000000000001137 <+14>:	movsxd rdx,eax
	0x000000000000113a <+17>:	imul   rdx,rdx,0x68db8bad
	0x0000000000001141 <+24>:	shr    rdx,0x20
	0x0000000000001145 <+28>:	sar    edx,0xd
	0x0000000000001148 <+31>:	mov    ecx,eax
	0x000000000000114a <+33>:	sar    ecx,0x1f
	0x000000000000114d <+36>:	sub    edx,ecx
	0x000000000000114f <+38>:	imul   ecx,edx,0x4e20
	0x0000000000001155 <+44>:	sub    eax,ecx
	0x0000000000001157 <+46>:	mov    edx,eax
	0x0000000000001159 <+48>:	mov    eax,edx
```
So basically we are seeding srand like so:
```c
	srand(time(0) % 20000)
```
Either we figure out a way to get the time when this exact instruction is called or
we just bruteforce the seed since we know it lies between 0 and 19999.
The latter seems more plausible.

We find out how the coordinates for the new fruits are generated in add_fruit:
More magic-number division optimizations!
Due to ghidra being able to get rid of them and replace them with the
original operations we have: # These are the only places where rand() is being used.
```c	
	iVar1 = rand();
	iVar1 = iVar1 % 0x12 + 1; -> Y coordinate
	iVar2 = rand();
	iVar2 = iVar2 % 0x26 + 1; -> X coordinate
```
We should be able to simulate these values once we figure out a way to replicate
the seed value.

Needed variables to reverse flag:

	Password
	chacha_nonce?
	encrypted_flag
	
chacha_nonce just seems to be 0

The encrypted_flag: \xF4\xB8\xC0\x90\xCD\xF6\xCB\xF7\xC5\x42\x30\xF3\x75\x04\x2C
					\x4B\xFD\x9D\x96\x02\x57\x79\x9A\x7A\xEE\x75\xD9\xF0\x4C 

We can see in update_screen that the first 4 bytes of unencrypted_flag are "brb{"
so \xF4\xB8\xC0\x90 give "brb{" which gives us the necessary constraints to bruteforce the flag.

The initial score is 3, We need 550 to win. We need to simulate 547 fruits.
Inorder to stay on the same lane as the RNG given in the game.
We'll use the same rand() and srand() functions as them.
Ghidra conveniently has decompiled those for us:
```c
	void srand(uint __seed)
	{
		next = (ulong)__seed;
		return;
	}
	
	int rand(void)
	{
		next = next * 0x41c64e6d + 0x3039;
		return (uint)((ulong)next >> 0x10) & 0x7fff;
	}
```
Replicated all variables and writing a script [exploit.c](https://github.com/azorfus/azorfus.github.io/blob/blog/resources/barbhackctf20203_s4rssnake/exploit.c)
We successfully solve the problem:

	[!] Flag found at seed: 2c1c
	[!] Flag: brb{a_snake_and_20_chachas}


