#The spider steps
import sys
sys.setrecursionlimit(999999)
def spiderr(height,climb,fall):
    steps=1
    steps+=((height-climb)/(climb-fall))
    return int(steps)+1
H=int(input("Height: "))
U=int(input("U: "))
D=int(input("D: "))
ans=spiderr(H,U,D)
print(ans)
