#Finger Game
def fing(no):
    di={1:[1,9],2:[2,8,10],3:[3,7,11],4:[4,6,12],5:[5,13]}
    for i in di:
        if no in di[i]:
            print(i)
            break
    
n=int(input("No.: "))
ans=fing(n)
