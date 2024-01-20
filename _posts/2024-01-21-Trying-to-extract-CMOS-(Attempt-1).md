---
layout: post
title:  "Trying to extract CMOS (Attempt 1)"
date:   2024-01-21 00:03:23 +0530
categories: Hardware and Reversing
---

I had this laptop lying around in my house with no internal fan, ACER SPIN 5. So I decided to take it apart,
find the CMOS chip and attempt to extract the boot sequence, BIOS settings and whatever is present in it.

There were three chips on the motherboard that looked like typical flash storage chips, I assumed one of them
to be the CMOS chip.

![Picture of the chips on board](https://github.com/azorfus/azorfus.github.io/blob/blog/_posts/2024-01-21-Trying-to-extract-CMOS-(Attempt-1)/3chips.jpeg?raw=true)

The chips in the top two pictures are the same.
Looking at common CMOS chips on the internet I saw that MXIC was a non-volatile chip solution provider, and I had 
one of their chips on my board, It must be the CMOS chip right?
So I look up the model of the chip and find the chip's [documentation][chip_documentation].

The chip uses the Serial Peripheral Interface (SPI) and the pins were labelled as such
![Picture of the pin diagram of the chip](https://github.com/azorfus/azorfus.github.io/_posts/2024-01-21-Trying-to-extract-CMOS-(Attempt-1)/pinconfig.jpeg)

[chip_documentation]: https://www.macronix.com/Lists/Datasheet/Attachments/8667/MX25L6473F,%203V,%2064Mb,%20v1.3.pdf

