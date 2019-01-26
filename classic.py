import random as rn
import time
import os
from copy import deepcopy

class LIVE():
    def __init__(self,a=None,b=None,pol=None):
        if a!=None and b!=None:
            self.a,self.b = int(a),int(b)
            arr = []
            for _ in range(self.a):
                n = []
                for _ in range(self.b):
                    n.append(rn.randint(0,3))
                arr.append(n)
            self.pol = arr
        else:
            self.a,self.b = len(pol),len(pol[0])
            self.pol = pol
    def NumSum (self,num,cr):
        x = num[0]
        y = num[1]

        i = x - 1
        j = y - 1
        n=-1
        for _ in range(3):
            if i >= 0 and i < self.a:
                for __ in range(3):
                    if (j >= 0 and j < self.b):
                        if self.pol[i][j] == cr:
                            n += 1            
                    j += 1
            i += 1
            j = y - 1

        return n

    def printGraf(self,x):
        for i in range(self.a):
            for j in range(self.b):
                if x[i][j] == 0:
                    print (x[i][j],end =' ')
                elif x[i][j] == 1:
                    print (x[i][j],end =' ')
                elif x[i][j] == 2:
                    print (x[i][j],end =' ')
                else:
                    print (x[i][j],end =' ')
            print()


 
    def play(self):
        os.system('cls')
        self.pol_pred = None
        n = [-1 for _ in range(self.b)]
        self.pol_pred =  [n for _ in range(self.a)]      
        self.printGraf (self.pol)
        time.sleep(1)    
        os.system('cls')
        while self.pol_pred != self.pol:                   
            os.system('cls')     
            self.pol_pred = deepcopy(self.pol)
            pol_din = []    
            for i in range(self.a):
                for j in range(self.b):
                    if self.pol[i][j] == 1:
                        if (1<self.NumSum([i,j],1)<4) == False:
                            pol_din.append([[i,j],3])
                    elif self.pol[i][j] == 2:
                        if (1<self.NumSum([i,j],2)<4) == False:
                            pol_din.append([[i,j],3])
                    elif self.pol[i][j] == 3:
                        if self.NumSum([i,j],1) == 3:          
                            pol_din.append([[i,j],1])
                        elif self.NumSum([i,j],2) == 3:
                            pol_din.append([[i,j],2])
                    else:
                        continue
            for i in pol_din:
                self.pol[i[0][0]][i[0][1]] = i[1]
            self.printGraf (self.pol)
            time.sleep(1)


if __name__ == '__main__':    
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("params",help="two comma separated integers - the width and height or the name of the text file")
    parser.add_argument("--file",'-f', help="if you use file name",action="store_true")
    args = parser.parse_args()
    if args.file:
        a = []
        nums = list(map(str,list(range(4))))
        with open(args.params, 'r') as file:  
            for i in file.readlines():
                n = []
                for j in i:
                    if j in nums:
                        n.append(int(j))
                a.append(n)
                n=[]
        b = LIVE(pol=a)
    else:
        A,B = args.params.split(',')          
        b = LIVE(a=A,b=B)  

    b.play()