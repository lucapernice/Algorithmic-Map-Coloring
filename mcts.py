#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:15:19 2023

@author: lucapernice

Implementation of Monte Carlo Tree Search for solving Tic Tac Toe game.
This program finds the best move given a certain state of the Tic Tac Toe board.
"""

import game  #game.py
import copy  #necessary for deep copy 
import math
import random



class Node():
    '''Node of the search tree representing a state of the game.
       For each state one of the two players has to take an action.
       Human player is  "x", computer player is "o".
       
    '''
    
    def __init__(self, board, parent=None, list_of_child=[], value = 0,  visited_count = 0, player = 'o'):
        self.parent = parent
        self.list_of_child=list_of_child
        self.value = value   #count of wins
        self.board = board
        self.visited_count = visited_count
        self.player = player
        
    
    def get_actions(self):
        '''return possible actions for the actual state of the game'''
        empty_cells = self.board.empty_cells()
        reachable_states = []
        positions = []
                
        for cell in empty_cells:
            row,column = cell
            new_board = copy.deepcopy(self.board)
            new_board.insert(self.player,row,column)
            reachable_states.append(new_board)
            positions.append(tuple((row,column)))
        
        return reachable_states,positions
    
    def ucb(self, c = math.sqrt(2)):
        
        if self.visited_count == 0:
            return float('inf')
        
        ratio = self.value / self.visited_count
        N_parent = self.parent.visited_count
        log_N_parent = math.log(N_parent)
        h = log_N_parent/self.visited_count
        
        return ratio + c*math.sqrt(h)
    
    def select(self):
        if self.player == 'o':
            next_player = 'x'
        else:
            next_player = 'o'
         
            
        a = self.list_of_child
        if self.list_of_child == []:
            return self
        else:
            
        
            max_ucb_score = float('-inf')
            
            next_state = None
            for state in self.list_of_child:
                
                
                ucb_score = state.ucb()
                if ucb_score >= max_ucb_score:
                    max_ucb_score=ucb_score
                    next_state = state
            
            return next_state.select()
    
    
    def rollout(self):
        tie = False
        human_player_win = False
        computer_player_win = False
        
        current_state = self
        
        current_player = self.player
        
        while(not tie and not human_player_win and not computer_player_win):
            
            if self.player == 'o':
                next_player = 'x'
            else:
                next_player = 'o'
            
            c,p= current_state.get_actions()
            if c == []:
                tie = True
            else:
                random_next_state_index = random.randint(0,len(c)-1)
                random_next_state = c[random_next_state_index]
                position = p[random_next_state_index]
                next_node = Node(board = random_next_state,player = next_player)
                current_player = next_player
               
                if random_next_state.check_win(position):
                    if current_player == 'o':
                        computer_player_win = True
                    if current_player == 'x':
                        human_player_win = True
                
            
                current_state = next_node
        
        return tie,human_player_win,computer_player_win
    
    
        
    def expand_simulate(self):
        #self will be a leaf node and this function is called after select
        
        
        #expansion
        c,p = self.get_actions()
        
        if self.player == 'o':
            next_player = 'x'
        else:
            next_player = 'o'
            
        for board in c:
            
            self.list_of_child.append(Node(board,parent = self, list_of_child=[],value = 0, visited_count= 0,player = next_player))
        
        
        if self.list_of_child == []:
            for i in range(3):
                for j in range(3):
                    if self.board.check_win((i,j)):
                        if self.player == 'x':
                            human_player_win = True
                            break
                        if self.player == 'o':
                            computer_player_win = True
            tie = True
         
        else:    
        #simulation
            starting_simulation_node = self.list_of_child[0]
            tie,human_player_win,computer_player_win = starting_simulation_node.rollout()
        
        if tie:
            return 0
        if human_player_win:
            return -1
        if computer_player_win:
            return 1
        
        
    def single_iteration(self):
        #A single iteration of Montecarlo Tree Search Algorithm
        
        x = self.select()  #selection
        result = x.expand_simulate() #simulation
        
        #backpropagation
        current_node = x
        while current_node != None:
            current_node.value = current_node.value + result
            current_node.visited_count = current_node.visited_count + 1 
            current_node = current_node.parent
            


def best_move(node, max_iterations = 1000):
    '''The function take in input a state of the game as a Node object and return the best move to do next'''
    
    it = 0
    while it < max_iterations:
        node.single_iteration()
        it = it + 1
    
    max_value = float('-inf')
    best_board = None
    for child in node.list_of_child:
        mean_value = child.value/child.visited_count
        if mean_value>max_value :
            max_value = mean_value
            best_board = child.board
    
    return best_board,max_value
            
    
      
    
#test
'''
b = game.Board()
b.matrix = [['x',None, 'x'],['o','x',None],['o','x','o']]    
root = Node(b)
best_board, max_value = best_move(root)
print(best_board.matrix[0])
print(best_board.matrix[1])
print(best_board.matrix[2])

 '''               
    
        
                
                    
            
        
        
        
        
           


    
    
    
        