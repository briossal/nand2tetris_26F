// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

(START)
@SCREEN
D=A
@R2
M=D

(KEYLOOP)
@KBD
D=M
@FILLBLACK
D;JNE
@FILLWHITE
0;JMP

(FILLBLACK)
@R3
M=-1
@DRAW
0;JMP

(FILLWHITE)
@R3
M=0

(DRAW)
@R3
D=M
@R2
A=M
M=D

@R2
M=M+1
D=M

@KBD
D=A-D
@DRAW
D;JGT

@START
0;JMP
