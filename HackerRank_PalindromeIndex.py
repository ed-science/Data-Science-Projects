## Given a string of lowercase letters, determine the index of the character 
## whose removal will make the string a palindrome. 
## If the string is already a palindrome, then print -1 . There will always be a valid solution.

## Input:
## The first line contains n (the number of test cases). 
## The n subsequent lines of test cases each contain a single string to be checked.

## Output :
## int the zero-indexed position (integer) of a character whose deletion will result in a palindrome; 
## if there is no such character (i.e.: the string is already a palindrome), print -1.

n = int(input().strip())
a = []
for _ in range(n):
   a_t = list(input().strip().split(' '))[0]
   a.append(a_t)
        
def isPal(s):
   return all(s[i] == s[len(s)-i-1] for i in range(len(s) // 2))
 
def solve(s):
   return next(
       (i if isPal(s[:i] + s[i + 1:]) else len(s) - i - 1
        for i in range(int((len(s) + 1) / 2)) if s[i] != s[len(s) - i - 1]),
       -1,
   )
for i in range(n):
    x=a[i]
    print(solve(x))