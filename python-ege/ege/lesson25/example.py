from fnmatch import fnmatchcase
for n in range(37,10001,37):
    if fnmatchcase(str(n),"1?2*"):
        print(n,n//37)
