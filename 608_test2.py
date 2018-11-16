import sys
import numpy as np #extract airport_ID 
import csv
import re

with open('delay.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    ori=[row['ORIGIN_AIRPORT_ID'] for row in reader]

with open('delay.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    destination=[row['DEST_AIRPORT_ID'] for row in reader]

with open('delay.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    distance=[row['DISTANCE'] for row in reader]

with open('delay.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    flight_number=[row['FL_NUM'] for row in reader]

with open('delay.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    arrival_delay=[row['ARR_DELAY'] for row in reader]

with open('airport.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    airport=[row['AIRPORT'] for row in reader]

with open('airport.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    airport_ID=[row['AIRPORT_ID'] for row in reader]
    
with open('distance.csv')as csvfile:
    reader=csv.DictReader(csvfile)
    source=[row['ORIGIN_AIRPORT_ID'] for row in reader]
    
    
with open('distance.csv')as csvfile:
    reader=csv.DictReader(csvfile)
    target=[row['DEST_AIRPORT_ID'] for row in reader]

    
with open('distance.csv')as csvfile:
    reader=csv.DictReader(csvfile)
    weight=[row['DISTANCE'] for row in reader]

with open('delay.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    dep=[row['ORIGIN_AIRPORT_ID'] for row in reader]

with open('delay.csv') as csvfile:
    reader=csv.DictReader(csvfile)
    arr=[row['DEST_AIRPORT_ID'] for row in reader]
    
    
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start, target):
    #print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                #print 'updated : current = %s next = %s new_dist = %s' \
                        #%(current.get_id(), next.get_id(), next.get_distance())
            #else:
                #print 'not updated : current = %s next = %s new_dist = %s' \
                        #%(current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
def unique_index(L,e):
    lst=[]
    for index,item in enumerate(L):
        if item ==e:
            lst=np.append(lst,int(index))
    return lst
indexm=0
def find_min_delay(x,y):
    a=unique_index(dep,x)
    b=unique_index(arr,y)
    c=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]==b[j]:
                c=np.append(c,a[i])
    common=np.empty(len(c),dtype=object)
    for i in range(len(c)):
        common[i]=int(c[i])
    arr_d=1000000
    for i in range(len(common)):    
        if int(arrival_delay[common[i]]) < arr_d:
            arr_d=int(arrival_delay[common[i]])
            indexm=common[i]
    return arr_d

air_delay=np.empty(len(arrival_delay),dtype=object)
for i in range(len(arrival_delay)):
    air_delay[i]=arrival_delay[i]
    
def find_flight(x,y):
    find_min_delay(x,y)
    print flight_number[indexm]
    
    

    
if __name__ == '__main__':

    
        
    g = Graph()

    for i in range(len(airport_ID)):
        g.add_vertex(airport_ID[i])

    for i in range(len(source)):
        g.add_edge(source[i],target[i],int(weight[i]))

    #print 'Graph data:'
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            #print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

    dijkstra(g, g.get_vertex('12478'), g.get_vertex('14771')) 

    target = g.get_vertex('14771')
    path = [target.get_id()]
    shortest(target, path)
    print 'The shortest path : %s' %(path[::-1])
    delay=0
    print 'Recommended flights : ' 
    for i in range(len(path)-1):
        delay=delay+find_min_delay(path[i],path[i+1])
        find_flight(path[i],path[i+1])
    print 'Estimated delay : '
    print delay
