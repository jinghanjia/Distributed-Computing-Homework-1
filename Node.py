import random
import math
mini_num= 1.0e-8
class Node:
    def __init__(self,id,X_axis,Y_axis,N,k):
        self.id=id
        self.X_axis=X_axis
        self.Y_axis=Y_axis
        self.neighbors=[]
        self.N=N
        self.k=k
    def add_neighbors(self,n):
        self.neighbors.append(n)

    def get_id(self):
        return self.id
    def get_X(self):
        return self.X_axis
    def get_Y(self):
        return self.Y_axis
    def set_X(self,x):
        self.X_axis=x
    def set_Y(self,y):
        self.Y_axis=y
    def pickNeighbor(self):
        n=random.randint(0,self.k-1)
        return self.neighbors[n]
    def get_neighbors(self):
        return self.neighbors
    def get_distance(self,n2,topology):
        #function to compute distance between self and n2
        if topology == 'R':
            #x1=self.get_X()
            #y1=self.get_Y()
            #x2=n2.get_X()
            #y2=n2.get_Y()
            #result=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
            result1=abs(self.id-n2.id)
            result2=self.N-abs(self.id-n2.id)    
            if result1>result2:
                result= result2
            else:
                result= result1            
        elif topology == 'P': 
            if self.id == self.N-1 and (n2.id==0 or n2.id==self.N-2):
                result=1
            elif n2.id == self.N-1 and (self.id==0 or self.id==self.N-2):
                result=1
            else:
                #x1=self.get_X()
                #y1=self.get_Y()
                #x2=n2.get_X()
                #y2=n2.get_Y()
                #result=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
                result=abs(self.id-n2.id)
        elif topology == 'S':
            x1=self.get_X()
            N=self.N
            y1=self.get_Y()
            x2=n2.get_X()
            y2=n2.get_Y()
            id1=self.id
            id2=n2.get_id()

            if id1 >=0 and id1 <= math.ceil(N/7):
                if id2>=0 and id2<=math.ceil(N/7):
                    result=mini_num*math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
                else :
                    result=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
            elif    id1 >= math.ceil(N/7)+1 and id1 <= math.ceil(2*N/7)  :
                if  id2 >= math.ceil(N/7)+1 and id2 <= math.ceil(2*N/7):
                    result=mini_num*math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
                else:
                     result=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
            elif    id1 >= math.ceil(2*N/7)+1 and id1 <= math.ceil(3*N/7)  :
                if  id2 >= math.ceil(2*N/7)+1 and id2 <= math.ceil(3*N/7):
                    result=mini_num*math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
                else:
                     result=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
            elif    id1 >= math.ceil(3*N/7)+1 and id1 <= N-1  :
                if  id2 >= math.ceil(3*N/7)+1 and id2 <= N-1:
                    result=mini_num*math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
                else:
                     result=math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
        return result
    def UpdateNeighbors(self,l1):
        #function to update neighbor list
        self.neighbors.clear()
        self.neighbors=l1
    def rearrange(self,neighbors_list,topology):
        #Both update their neighbor list.
        merged_list=self.neighbors+neighbors_list
        merged_list=list(set(merged_list))
        final_list=[]
        for node in merged_list:
            if node.get_id() != self.id:
                final_list.append(node)
        dists=[]
        for node in final_list:
            dist=self.get_distance(node,topology)
            dists.append(dist)
        index=sorted(range(len(dists)),key=lambda t:dists[t])
        new_neighbors=[]
        for count in range(self.k):
            new_neighbors.append(final_list[index[count]])
        self.UpdateNeighbors(new_neighbors)



    