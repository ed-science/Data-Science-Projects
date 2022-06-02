## Aim :
## You are given two strings, A and B. 
## Find if there is a substring that appears in both A and B.

# Input:
# The first line of the input will contain a single integer , tthe number of test cases.
# Then there will be t descriptions of the test cases. Each description contains two lines. 
# The first line contains the string A and the second line contains the string B.

# Output:
# For each test case, display YES (in a newline), if there is a common substring. 
# Otherwise, display NO

n = int(input().strip())
a = []
for _ in range(2*n):
   a_t = list(input().strip().split(' '))[0]
   a.append(a_t)

for i in range(2*n):
   if (i%2==0):
      s1=set(a[i])
      s2=set(a[i+1])
      S=s1.intersection(s2) #intersection of subset -> return the same characters !!
      if not S:
         print("NO")
      else:
         print("YES")
