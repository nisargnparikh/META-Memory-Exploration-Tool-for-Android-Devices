One block of trace is:

##########
CPU ID = 1
Reg 0 = 43471d2c 
Reg 1 = 553475f2 
Reg 2 = 1c96ad85 
Reg 3 = 5303ffed 
Reg 4 = 40008000 
Reg 5 = 400100a0 
Reg 6 = 40118060 
Reg 7 = ffffffff 
Reg 8 = 48138000 
Reg 9 = 406cc2c0 
Reg 10 = ea17f9d2 
Reg 11 = ec6f245b 
Reg 12 = 8453b40e 
Reg 13 = 0 
Reg 14 = 0 
0x40010150:  e9365c0f      ldmdb	r6!, {r0, r1, r2, r3, sl, fp, ip, lr}
0x40010154:  e1560005      cmp	r6, r5
0x40010158:  e9295c0f      stmdb	r9!, {r0, r1, r2, r3, sl, fp, ip, lr}
0x4001015c:  8afffffb      bhi	0x40010150

Every trace starts with 10 # signs.
Then the register values are printed as Reg XX.
Then we have the instructions using that register values.
Have to separate load store instructions and then use the register values given in that instruction to add as offset to the program counter( 1st column).

For ex:  In above trace:
Reg 6 = 40118060  
0x40010150:  e9365c0f      ldmdb	r6!, {r0, r1, r2, r3, sl, fp, ip, lr}  
First we have to get value of r6 as that is asked in this instruction.Similarly, need to get register value as asked in instruction.
Then We have to add pc ie 0x40010150 and r6 ie Reg 6 = 40118060 (both are hex).
Then, printing into a file in the predefined hex format.
load: R 0xabc0def0
store: W 0xabc0def0  
 