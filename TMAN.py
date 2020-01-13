import math
import random
import Node
import matplotlib.pyplot as plt
import networkx as nx
CYCLE=40
def Write_Distance_Sum(nodes_list,cycle,N,k,topology):
    # write distance sum
    distance = 0
    for node in nodes_list:
        for neighbor_node in node.get_neighbors():
            distance+=node.get_distance(neighbor_node,topology)
    path=topology+'_N'+str(N)+'_k'+str(k) +'.txt'
    fo=open(path,'a+')
    #print(str(cycle))
    fo.write('cycle'+str(cycle+1)+':'+str(distance)+'\r\n')
def Write_Neighbors(nodes_list,cycle,N,k,topology):
    #write neighbors' id
    merged_output=''
    for node in nodes_list:
        id1=str(node.get_id())
        neighbors_list=node.get_neighbors()
        merged_output+=id1+'---->'
        neighbors_id=[]
        for neighbor in neighbors_list:
            neighbors_id.append(neighbor.get_id())
            neighbors_id.sort()
        id2=''
        for i in range(k-1):
            id2+=str(neighbors_id[i])+','
        id2+=str(neighbors_id[k-1])+'\r\n'
        merged_output+=id2
    path=topology+'_N'+str(N)+'_k'+str(k)+'_'+str(cycle+1)+'.txt'
    fo=open(path,'a+')
    fo.write(merged_output)
def plot_picture(nodes_list,cycle,N,k,topology):
    # plot nodes' picture
    node_id_list=[]
    for node in nodes_list:
        neighbors_list=node.get_neighbors()
        x1=node.get_X()
        y1=node.get_Y()
        node_id_list.append(node.get_id())
        for neighbor in neighbors_list:
            if neighbor.get_id() not in node_id_list:
                x2=neighbor.get_X()
                y2=neighbor.get_Y()
                plt.plot([x1,x2],[y1,y2])
    path=topology+'_N'+str(N)+'_k'+str(k)+'_'+str(cycle+1)+'.png' 
    plt.show()
    plt.savefig(path)
    plt.close()
####
#### ring topology
def Ring(N,k,topology):
    angle_diff=2*math.pi/N
    nodes_list=[]
    angle=0
    #initialize N nodes
    for i in range(N):
        x=math.cos(angle)
        y=math.sin(angle)
        node=Node.Node(i,x,y,N,k)
        nodes_list.append(node)
        angle+=angle_diff
    #initialize our network random select neighbors for nodes
    for node in nodes_list:
        list1=[*range(N)]
        list1.remove(node.get_id())
        list1_slice=random.sample(list1,k)
        for index in list1_slice:
            node.add_neighbors(nodes_list[index])           
    # iterations 
    for cycle in range(CYCLE):
        for node in nodes_list:
            neighbor_node=node.pickNeighbor()
            node.rearrange(neighbor_node.get_neighbors(),topology)
            neighbor_node.rearrange(node.get_neighbors(),topology)
        Write_Distance_Sum(nodes_list,cycle,N,k,topology)
        if(cycle==0 or cycle==4 or cycle==9 or cycle==14 or cycle==39):
            Write_Neighbors(nodes_list,cycle,N,k,topology)
            plot_picture(nodes_list,cycle,N,k,topology)

##### P topology
def P_topology(N,k,topology):
    angle_diff=math.pi/(N-1)
    nodes_list=[]
    angle=0
    #initialize N nodes
    for i in range(N):
        if i<N-1:
            x=math.sin(angle)
            y=math.cos(angle)
            node=Node.Node(i,x,y,N,k)
            nodes_list.append(node)
            angle+=angle_diff
        else :
            x=0
            y=-2
            node=Node.Node(i,x,y,N,k)
            nodes_list.append(node)
    print(nodes_list[N-1].get_Y())
    #initialize our network random select neighbors for nodes
    for node in nodes_list:
        list1=[*range(N)]
        list1.remove(node.get_id())
        list1_slice=random.sample(list1,k)
        for index in list1_slice:
            node.add_neighbors(nodes_list[index])           
    # iterations 
    for cycle in range(CYCLE):
        for node in nodes_list:
            neighbor_node=node.pickNeighbor()
            node.rearrange(neighbor_node.get_neighbors(),topology)
            neighbor_node.rearrange(node.get_neighbors(),topology)
        Write_Distance_Sum(nodes_list,cycle,N,k,topology)
        if(cycle==0 or cycle==4 or cycle==9 or cycle==14 or cycle==39):
            Write_Neighbors(nodes_list,cycle,N,k,topology)
            plot_picture(nodes_list,cycle,N,k,topology)
def S_topology(N,k,topology):
    nodes_list=[]
    angle1=0
    angle2=0
    angle3=0
    angle4=0
    angle1_diff=2*math.pi/(math.ceil(N/7)+1)
    angle2_diff=2*math.pi/(math.ceil(2*N/7)-math.ceil(N/7))
    angle3_diff=math.pi/(math.ceil(3*N/7)-math.ceil(2*N/7))
    angle4_diff=2*math.pi/(N-1-math.ceil(3*N/7))
    #initialize N nodes
    for id1 in range(N):
            if id1 >=0 and id1 <= math.ceil(N/7):
                x=2+math.cos(angle1)
                y=2+math.sin(angle1)
                node=Node.Node(id1,x,y,N,k)
                nodes_list.append(node)
                angle1+=angle1_diff
            elif    id1 >= math.ceil(N/7)+1 and id1 <= math.ceil(2*N/7)  :
                x=-2+math.cos(angle2)
                y=2+math.sin(angle2)
                node=Node.Node(id1,x,y,N,k)
                nodes_list.append(node)
                angle2+=angle2_diff
            elif    id1 >= math.ceil(2*N/7)+1 and id1 <= math.ceil(3*N/7)  :
                x=2*math.cos(angle3)
                y=-1-2*math.sin(angle3)
                node=Node.Node(id1,x,y,N,k)
                nodes_list.append(node)
                angle3+=angle3_diff
            elif    id1 >= math.ceil(3*N/7)+1 and id1 <= N-1  :
                x=4*math.sin(angle4)
                y=4*math.cos(angle4)
                node=Node.Node(id1,x,y,N,k)
                nodes_list.append(node)
                angle4+=angle4_diff
    print(nodes_list[N-1].get_Y())
    #initialize our network random select neighbors for nodes
    for node in nodes_list:
        list1=[*range(N)]
        list1.remove(node.get_id())
        list1_slice=random.sample(list1,k)
        for index in list1_slice:
            node.add_neighbors(nodes_list[index])           
    # iterations 
    for cycle in range(CYCLE):
        for node in nodes_list:
            neighbor_node=node.pickNeighbor()
            node.rearrange(neighbor_node.get_neighbors(),topology)
            neighbor_node.rearrange(node.get_neighbors(),topology)
        Write_Distance_Sum(nodes_list,cycle,N,k,topology)
        if(cycle==0 or cycle==4 or cycle==9 or cycle==14 or cycle==39):
            Write_Neighbors(nodes_list,cycle,N,k,topology)
            plot_picture(nodes_list,cycle,N,k,topology)

#Ring(1000,30,'R')
#P_topology(1000,30,'P')
S_topology(1000,30,'S')