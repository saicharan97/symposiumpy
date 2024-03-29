#There are N people P1, P2, P3, …, PN having F1, F2, F3, …, FN Facebook friends, respectively. The solution to this problem is finding k = Fi%Fj such that it is maximum over all valid i,j. 
#Constraints:
#2 <= N <= 105
#1 <= Ai <= 109 for each i
#Input Format:

#The first line contains an integer N
#The second line contains N space-separated integers F1, F2, F3, …, FN
#Output Format:

#Print in a single line the output which is k, the solution to this problem.
#Example:

#Input:
#5
#1 2 3 4 5

#Output:
#4

N=int(input())
F=[int(i) for i in input().split()]
UB=0
for i in range(N):
    for j in range(N):
        k=F[i]%F[j]
        if(k>UB):
            UB=k
print(UB)
