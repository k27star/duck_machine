# Lovingly crafted by robots
   LOAD r1,const5_2
   LOAD r2,const3_3
   ADD  r1,r1,r2
  STORE  r1,x_1
   LOAD r1,const4_5
   LOAD r2,x_1
   MUL  r1,r1,r2
  STORE  r1,y_4
loop_6:  #While loop
   LOAD r1,x_1
  SUB  r0,r1,r0 
  JUMP/Z endloop_7
   LOAD r1,x_1
   LOAD r2,const1_8
   SUB  r1,r1,r2
  STORE  r1,x_1
   LOAD r1,y_4
   LOAD r2,const1_8
   ADD  r1,r1,r2
  STORE  r1,y_4
  JUMP loop_6
endloop_7: 
   LOAD r1,y_4
STORE r1,r0,r0[511] # Print
  HALT  r0,r0,r0
x_1: DATA 0 #x
y_4: DATA 0 #y
const5_2:  DATA 5
const3_3:  DATA 3
const4_5:  DATA 4
const1_8:  DATA 1
