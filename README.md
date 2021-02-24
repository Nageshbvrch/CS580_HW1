# CS580_HW1
24-Puzzle



Initial Test : 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0,24

Solvable : 2,11,0,4,5,6,1,3,9,12,8,19,13,7,10,18,17,14,15,20,16,21,22,23,24

Final Test : 9,24,3,5,17,6,0,13,19,10,11,21,12,1,20,16,4,14,12,15,8,18,23,2,7

#---- 24 puzzle :

#----#-- BFS - Breadth First Search --#----#

Sno	|	board									| number of moves |		Time Taken (Seconds)|				solution (s) |
----|-----------------------|-----------------|-----------------------|--------------------|
1		1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0,24		1			0.00000000					R
2		1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,0,23,24		2			0.00097060					RR
3		1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,0,21,22,23,24		4			0.00000000					RRRR
4		1,2,3,4,0,6,7,8,9,5,11,12,13,14,10,16,17,18,19,15,21,22,23,24,20		4			0.00099707					DDDD
5		1,2,3,0,4,6,7,8,9,5,11,12,13,14,10,16,17,18,19,15,21,22,23,24,20		5			0.00498605					RDDDD
6		0,1,2,3,4,6,7,8,9,5,11,12,13,14,10,16,17,18,19,15,21,22,23,24,20		8			0.05382967					RRRRDDDD
7		6,1,2,3,4,11,7,8,9,5,16,12,13,14,10,21,17,18,19,15,0,22,23,24,20		12			1.33746266					UUUURRRRDDDD
8		6,1,2,3,4,11,7,8,9,5,16,12,13,14,10,21,17,18,19,15,22,23,24,20,0		16			16.48596382					LLLLUUUURRRRDDDD
9		6,1,2,3,4,11,7,13,8,9,16,12,0,14,5,21,17,18,19,10,22,23,24,20,15		Programs Crashes as the memory is full

#----#-- DFS - Depth First Search --#----#

Sno	|	board									| number of moves |		Time Taken (Seconds)|				solution (s)

1		1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,0,24		1			0.00000000					R
2		1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,0,23,24		Program executes forever as there are many branches because of the depth.





Reference : 

1. https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/what-is-modular-arithmetic
