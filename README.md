# NQueen_CNF_to_SAT


Date : 4th dec , 20

N-Queen Problem : 
The N Queen is the problem of placing N chess queens on an N×N chessboard so that no two queens attack each other.
Rules : 
1) Only 1 queen in one row.
2) Only 1 queen in 1 column.
3) Only one queen in a diagonal (Pls note there are two diagonals , one : right to left , two : left to right)

It can be seen that for n =1, the problem has a trivial solution, and no solution exists for n =2 and n =3.

The Python program will take the input N (Number of queens) , and will print the output in a file having format as CNF , that file will contain the list of variables and their clauses. That file can directly be used in miniSAT to get the output or you can copy paste the output in any of the SAT solvers available.

The SAT solver will give you the solution in which if the variable is negative then a queen is not present there and if the variable is positive then a queen is present there.

Once you get the output from SAT , Start writing the output in NxN board from left to right and then you'll get the chess board with correct N queens placement.

 x ------- x ------- x ------- x ------- x ------- x ------- x ------- x ------- x ------- x ------- x ------- x ------- x ------- x ------- x

More advancements will soon be available : 
-Manual effort of executing the miniSAT would be replaced by automation.
-Instead of Command Line Interface , A good UI would be implemented.


