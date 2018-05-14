# Lovingly crafted by robots
   LOAD r1,const5_2
  STORE  r1,x_1
   LOAD r1,const1_4
  STORE  r1,fact_3
loop_5:  #While loop
   LOAD r1,x_1
  SUB  r0,r1,r0 
  JUMP/Z endloop_6
   LOAD r1,x_1
   LOAD r2,fact_3
   MUL  r1,r1,r2
  STORE  r1,fact_3
   LOAD r1,x_1
   LOAD r2,const1_4
   SUB  r1,r1,r2
  STORE  r1,x_1
  JUMP loop_5
endloop_6: 
   LOAD r1,fact_3
   STORE r1,r0,r0[511] # Print
   HALT  r0,r0,r0
x_1: DATA 0 #x
fact_3: DATA 0 #fact
const5_2:  DATA 5
const1_4:  DATA 1
