"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score."""
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
if ((n>=2 and n<=10)):
    if len(arr) == n:
        for i in arr:
            if i ==' ':
                arr.remove(i)
            elif i == ',' in arr:
                arr.remove(i)
        l = []
        for i in arr:
            if (i>=-100 and i<=100):
                x = int(i)
                l.append(x)
        l.sort()
        m = []
        for i in l:
            if i not in m:
                m.append(i)
        m.sort()
print(m[-2])
            
