import sys,string
from math import ceil


### Get the user input on number of queens ###

N = input("Enter Number of Queens : ")
if N < 4:
  print "UNSATISFIABLE"
  exit()

### Initialize clause counter ###
count=0

### Create a file ###
file="converted.cnf"
file1= open(file,"w");


### row generating : At-least 1 queen in each row ###

lim = N * N + 1

for i in range(1, lim):
  file1.write("{0:d} ".format(i))
  if i % N == 0:
    file1.write("0\n")
    count+=1


### Algorithm to get the row number from square number i.e i ###

for i in range(1, lim):
  row = ceil(i / N)

### loop to print the clauses ###

  lastsquare_no = row * N
  for j in range(i, int(lastsquare_no + 1)):
    if j == i:
      continue
    file.write("-{0:d} -{1:d} 0\n".format(i, j))
    count+=1


# column

    # loop to go through all the squares of the board
for i in range(1, lim):

  # loop to print the clauses
 for j in range(i, lim, N):
      if j == i: 
        continue
      file1.write("-{0:d} -{1:d} 0\n".format(i, j))
      count+=1


### diagonal ###

#constraints on l->r diagonal
# part 1, upper bound triangle
for i in range(0,N-1):
 for j in range(i,N-1):
  number=j+1+N*i;
  for l in range(1,N-j):
   str0="-"+str(number)+" -"+str(number+l*(N+1))+" 0\n"
   file1.write(str0);
   count+=1

# part 2, lower bound triangle
for i in range(0,N-1):
 for j in range(0,i):
  number=j+1+N*i;
  for l in range(1,N-i):
   str0="-"+str(number)+" -"+str(number+l*(N+1))+" 0\n"
   file1.write(str0);
   count+=1

#constraints on r->l diagonal
# part 1, upper bound triangle
for i in range(0,N):
 for j in range(0,N-i):
  number=j+1+N*i;
  for l in range(1,j+1):
   str0="-"+str(number)+" -"+str(number+l*(N-1))+" 0\n"
   file1.write(str0);
   count+=1

# part 2, lower bound triangle
for i in range(0,N):
 for j in range(N-i,N):
  number=j+1+N*i;
  if (number != N*N ):
   for l in range(1,N-i):
    str0="-"+str(number)+" -"+str(number+l*(N-1))+" 0\n"
    file1.write(str0);
    count+=1

file1.close()


f = open('converted.cnf', 'r')
temp = f.read()
f.close();

f = open('converted.cnf', 'w')
f.write("c Aniruddh Chavda \n")
f.write("c CS5384 Project \n")
f.write("c Program to Convert N-queens into CNF for applying SAT Solver \n")
f.write("p cnf "+str(N*N) +" "+ str(count) + "\n")
f.write(temp)
f.close()
