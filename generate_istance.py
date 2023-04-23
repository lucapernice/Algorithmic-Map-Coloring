import numpy as np
from numpy import random

from scipy.spatial import distance

from shapely.geometry import LineString
import matplotlib.pyplot as plt


"""
Exercise 2 : Algorithmic map coloring - Performance analysis

Generate random istances of map-coloring problems as follow:

    -scatter n points on the unit square;
    -select a point X at random;
    -connect X by a straight line to the nearest point Y such that X is not 
     already connected to Y and the line crosses no other line;
    -repeat the previous step until no more connections are possible.


"""


def scatter_points(n):
    """n: number of points"""
    
    points = np.random.rand(n,2)
        
    return points.tolist()

class Segment:
    """Segment between points p1 and p2"""
    
    def __init__(self,p1,p2):
        
        self.p1 = p1
        self.p2 = p2
        
    def intersect(self,other_segment):
        """return True if there is an intersection between segments"""
        
        
        
        line = LineString([self.p1, self.p2])
        other = LineString([other_segment.p1,other_segment.p2])
        
        return line.intersects(other)
        
        
        
        
        
def connections(points) :
    """
    Select a random point X from the points list. Then search Y, the nearest point from X that is not in adj_list of X. Add Y to the adj_list of X and vice 
    versa. 
    Then add the segment from X to Y in the seg_list (if there aren't intersections).
    The function iterate this process in a while loop. 
    When a point has every other points in its adj_list, it's removed from the expandable_node list so that it can't be extracted anymore. 
    When the expandable_nodes list is empty, the while loop ends.
    
    """
    
    n = len(points)     #total number of points
    adj_list = [ [] for _ in range(n) ] #for each point there is a list containig the visited nearest points in the while loop below
    seg_list = []   #store the segments    
    expandable_nodes = list(points) #list of points that still can be expanded in the while loop below
    

    while len(expandable_nodes) > 0 : #while loop stops when there is no more expandable nodes
    
        remaining_n = len(expandable_nodes)
        if remaining_n == 1:
            i = 0
        else:
            i = random.randint(0, remaining_n - 1) #select random X from expandable_nodes
        
        if len(adj_list[points.index(expandable_nodes[i])])==n-1 :  #if the point can't be expanded it is removed from expandable_nodes list
        
            expandable_nodes.remove(expandable_nodes[i])
         
        else:                   
                
            min_dist = 999999
            min_index=0
            for j in range(n):
                
                dist = distance.euclidean(expandable_nodes[i],points[j])
                if ( dist>0 ) and (points[j] not in adj_list[points.index(expandable_nodes[i])]) :
                    
                    if dist < min_dist:
                        min_dist = dist
                        min_index = j #index of Y
            
            adj_list[points.index(expandable_nodes[i])] = adj_list[points.index(expandable_nodes[i])] + [points[min_index]]#add Y to adj_list of X
            adj_list[min_index] = adj_list[min_index] + [points[points.index(expandable_nodes[i])]] #add X to adj_list of Y
            
            s = Segment(expandable_nodes[i], points[min_index]) #create the segment from X to Y
            
            cond = False
            
            
            for segment in seg_list:
                if s.p1 != segment.p1 and s.p1 != segment.p2 and s.p2 != segment.p1 and s.p2 != segment.p2:
                    cond = s.intersect(segment) #check for intersections
                    if cond == True: break
                
            if cond == False: seg_list.append(s) #if there are no intersections add the segment to the seg_list
    
    
    return seg_list
        

def generate(n_points):
    points = scatter_points(n_points)
    seg = connections(points)
    
    return points,seg

        
    
#points, seg5 = generate(5)

#for h in range(len(seg5)):
     
   #plt.plot([seg5[h].p1[0],seg5[h].p2[0]],[seg5[h].p1[1],seg5[h].p2[1]])     
        
                
        
        
    
    
        
    


    
    


