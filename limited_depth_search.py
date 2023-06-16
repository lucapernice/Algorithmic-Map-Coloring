#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 21 10:15:05 2023

@author: lucapernice
"""

import game
import mcts

class lds_node(mcts.Node):
    
    def __init__(self, board,parent=None, list_of_child=[], value = 0,  visited_count = 0, player = 'o',depth = 0):
        super().__init__(board,parent,list_of_child,value,visited_count,player)
        self.depth = depth  #node depth
        
    def expand_node(self):
        
        c,p = self.get_actions()
        new_depth = self.depth + 1
        
        if self.player == 'o':
            next_player = 'x'
        else:
            next_player = 'o'
            
        for board in c:
            
            self.list_of_child.append(lds_node(board,parent = self, list_of_child=[],value = 0, visited_count= 0,player = next_player,depth=new_depth))
        
    def evaluate_leaf(self):
        '''Evaluation function
        Counts the lines in the grid where the computer player(o) can still win.'''      
        
        grid = self.board.matrix
        
        #check if the game is ended
        human_player_win = False
        computer_player_win = False
        
        for i in range(3):
            for j in range(3):
                if self.board.check_win((i,j)):
                    if self.player == 'x':
                        human_player_win = True
                        break
                    if self.player == 'o':
                        computer_player_win = True
        
        
        if human_player_win:
            return -10
        if computer_player_win:
            return 10
        
        
        else:
        
            counter = 0
            c,p = self.get_actions()
            visited_rows = []
            visited_columns = []
            
            for position in p:
                #ceck row
                row,column = position
                if row not in visited_rows:
                    if 'x' not in grid[row]:
                        counter = counter + 1
                    visited_rows.append(row)
                
                #check column
                if column not in visited_columns:
                    col = [None for k in range(3)]
                    for index in range(3):
                        col[index] = grid[index][column]
                    if 'x' not in col:
                        counter = counter + 1
                    visited_columns.append(column)
                    
            #check diagonals
            if (grid[0][0] != 'x') and (grid[1][1] != 'x') and (grid[2][2] != 'x'):
                counter = counter + 1
                
            if (grid[2][0] != 'x') and (grid[1][1] != 'x') and (grid[0][2] != 'x'):
                counter = counter + 1
            
            
            return counter
    
    
    def evaluate(self):
        if self.depth >= 2:
            return self.evaluate_leaf()
        else:
            if self.list_of_child == []:
                self.expand_node()
                
            
            max_value = float('-inf')
            
            for successor_node in self.list_of_child:
                val = successor_node.evaluate()
                if val > max_value:
                    max_value=val
            
            return max_value
            
            
                
    def best_move(self):
        max_value = float('-inf')
        best_board = None
        
        if self.list_of_child == []:
            self.expand_node()
        
        for child in self.list_of_child:
           value = child.evaluate()
           if value>max_value :
               max_value = value
               best_board = child.board
        
        return best_board,max_value
    
        
'''
b = game.Board()
b.matrix = [['x',None, 'x'],['o','x',None],['o','x','o']]    
root = lds_node(b)
best_board, max_value = root.best_move()


print(best_board.matrix[0])
print(best_board.matrix[1])
print(best_board.matrix[2])
'''
