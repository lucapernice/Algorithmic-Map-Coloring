import generate_istance as gen
import numpy as np
import random


    
class Problem:
    
    ''' Problem Class 
    --------------------------------------------------------------------------------
    
        list_of_regions : list containing points/region 
        seg_list : list containing object of gen.segment class type --> neighbors
        k: int representing number of colours
        colours : array with colour (integers from 0 to k-1) for each region        
        
    --------------------------------------------------------------------------------     
    '''
    def __init__(self,list_of_regions,seg_list,k):
        self.regions = list_of_regions
        self.costraints = seg_list
        self.k = k
        self.colours = np.zeros(len(self.regions))  #colours[i] is the colour of regions[i]
        
        
    def search_conflicts(self):
        '''Return list of neighbors in conflict'''
        
        conf_list = []
        
        for seg in self.costraints:
            
            p1_index = self.regions.index(seg.p1)
            p2_index = self.regions.index(seg.p2)
            
            if self.colours[p1_index] == self.colours[p2_index]:
                conf_list = conf_list + [seg]
        
        return conf_list
    
    
    def min_conflict(self, max_iterations=10000):
        '''Implementation of min-conflict algorithm'''
        
        col_list = [] #list of all k possible colours
        for i in range(self.k):
            col_list = col_list + [i]
            
            
        conf_list = self.search_conflicts()
        if conf_list==[]:
            print('Already solved')
        t = 0
        while conf_list != [] and t<= max_iterations:
            conflict = random.choice(conf_list)
            var = random.choice([conflict.p1,conflict.p2]) #random variable in conflict
            var_index = self.regions.index(var)
            min_conf_numb = 999999
            min_conf_col = self.colours[var_index]
            new_conf_list = list(conf_list)
            
            for col in col_list:
                self.colours[var_index] = col
                c = self.search_conflicts()
                l = len(c)
                if l<min_conf_numb:
                    min_conf_numb = l
                    min_conf_col = col
                    new_conf_list = c
                    
                
            self.colours[var_index]=min_conf_col
            
            conf_list = new_conf_list
            if conf_list == []:
                print(f'Solved in {t} iterations')
            t = t + 1
        
        if conf_list != [] :
            print('Not solved')
   
    
    def consistence(self,assignment,var, color):
        for seg in self.costraints:
            
            if (seg.p1 == var):
                if tuple(seg.p2) in assignment:
                    if color == assignment[tuple(seg.p2)]:
                        return False
            if (seg.p2==var):
                if tuple(seg.p1) in assignment:
                    if color == assignment[tuple(seg.p1)]:
                        return False            
        return True
        
   
    def backtrack(self,assignment, unassigned_variables, domain_values):
        '''Implemenation of backtract algorithm in figure 6.5 of chapter 6.3
           from the book " Artificial Intelligence. A Modern Approach Fourth"
           by Stuart Russel and Peter Norvig.
        '''
        #print(f'unassigned variables : {unassigned_variables}, len = {len(unassigned_variables)}')
        if unassigned_variables == []:  #if assignment is complete
            return assignment  
    
        var =  unassigned_variables[0]
        #print(f'var: {var} , assignment --> {assignment}')
        
        for color in domain_values:
            if self.consistence(assignment, var, color) :
                #print(f'color : {color}')
                assignment[tuple(var)]=color
                new_unassigned_variables = list(unassigned_variables)
                new_unassigned_variables.remove(var)
                res = self.backtrack(assignment, new_unassigned_variables, domain_values)
                if res != {}: 
                    return res
        return {}  #empty dictionary represent FALSE
    
    def forward_domain(self,var,color,domain):
        for seg in self.costraints:            
            
            if (seg.p1 == var):
                ind = self.regions.index(seg.p2)
               
                if color in domain[ind]:
                    
                    c =list(domain[ind])
                    c.remove(color)
                    domain[ind] = c
            
            if (seg.p2==var):
                ind = self.regions.index(seg.p1)
                
                if color in domain[ind]:
                    c =list(domain[ind])
                    c.remove(color)
                    domain[ind] = c
                    
        return domain
        
    
    def backtrack_f(self,assignment, unassigned_variables,domain):
        '''Adaptation of backtrack for forward checking'''
        #print(f'unassigned variables : {unassigned_variables}, len = {len(unassigned_variables)}')
        if unassigned_variables == []:  #if assignment is complete
            return assignment
        
        var =  unassigned_variables[0]
        
        
        for color in domain[self.regions.index(var)]:
            if self.consistence(assignment, var, color) :
               
                
                assignment[tuple(var)]=color
                new_unassigned_variables = list(unassigned_variables)
                new_unassigned_variables.remove(var)
                new_domain = list(domain)
                new_domain = self.forward_domain(var, color, new_domain)
                res = self.backtrack_f(assignment, new_unassigned_variables, new_domain)
                if res != {}: 
                    return res
        return {}  #empty dictionary represent FALSE
    
    
    def revise(self,arc,domain):
        
        revised = False
        
        xj = arc.p2
        
        for col in domain[self.regions.index(arc.p1)]:
            if domain[self.regions.index(xj)]==[col]:
                
                c =list(domain[self.regions.index(arc.p1)])
                c.remove(col)
                domain[self.regions.index(arc.p1)] = c
                
                revised = True
                
            
        return revised
    
    
    
    def ac3(self,var,color,domain):
        domain[self.regions.index(var)] = [color]
        queue = []
        arcs = list(self.costraints)
        
        for seg in self.costraints:                  #each costraint(segment object) is duplicated
            arcs.append(gen.Segment(seg.p2,seg.p1))  #with swapped vertex.
        
        for seg in arcs:
            if (seg.p2 == var) :  #forcing var to be the second vertex of the arc. 
                queue.append(seg)
        
        while queue != []:
            arc = queue.pop(0)
            xi = arc.p1
            if self.revise(arc,domain):
                if domain[self.regions.index(xi)]==[]:
                    return False
                for seg in arcs:
                    if (seg.p2 == xi) :  #forcing Xi to be the second vertex of the arc. 
                        queue.append(seg)
                    
            
        return True
    
    
    
    
            
    def backtrack_mac(self,assignment, unassigned_variables,domain):
        '''Adaptation of backtrack with MAC'''
        #print(f'unassigned variables : {unassigned_variables}, len = {len(unassigned_variables)}')
        if unassigned_variables == []:  #if assignment is complete
            return assignment
        
        var =  unassigned_variables[0]
        
        
        for color in domain[self.regions.index(var)]:
            if self.consistence(assignment, var, color) :
               
                
                assignment[tuple(var)]=color
                new_unassigned_variables = list(unassigned_variables)
                new_unassigned_variables.remove(var)
                new_domain = list(domain)
                if self.ac3(var, color, new_domain):
                    res = self.backtrack_mac(assignment, new_unassigned_variables, new_domain)
                    if res != {}: 
                        return res
        return {}  #empty dictionary represent FALSE






    def backtracking_search(self, type = 'normal'):
        
        col_list = [] #list of all k possible colours
        for i in range(self.k):
            col_list = col_list + [i]
            
        if type == 'normal':
            
                
            res = self.backtrack({},list(self.regions),col_list)
            
            if res != {}:
                for i in range(len(self.regions)):
                    self.colours[i]=res[tuple(self.regions[i])]
                print('Solved')
            else: 
                print('Not Solved')
        
        if type == 'forward_checking':
            
            domain = [0]*len(self.regions)
            for i in range(len(self.regions)):
                domain[i]=col_list
            
            res = self.backtrack_f({},list(self.regions),domain)
            
            if res != {}:
                for i in range(len(self.regions)):
                    self.colours[i]=res[tuple(self.regions[i])]
                print('Solved')
            else: 
                print('Not Solved')
        
        if type == 'mac':
            domain = [0]*len(self.regions)
            for i in range(len(self.regions)):
                domain[i]=col_list
                
            
            res = self.backtrack_mac({},list(self.regions),domain)
            
            if res != {}:
                for i in range(len(self.regions)):
                    self.colours[i]=res[tuple(self.regions[i])]
                print('Solved')
            else: 
                print('Not Solved')  
                
                
                    
                
                
        
        
            
            
      
