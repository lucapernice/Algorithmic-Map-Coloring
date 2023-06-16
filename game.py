#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:23:08 2023

@author: lucapernice
"""

class Board:
    
    '''Board Class represent the game board of Tic Tac Toe Game.
       It consist of a 3x3 matrix and each element of the matrix 
       represent a cell of the grid.
    '''
    
    
    def __init__(self):
        self.matrix = [[None for c in range(3)] for i in range(3)]
    
    def clear_board(self):
        self.matrix =  [[None for c in range(3)] for i in range(3)]
        
        
    def empty_cells(self):
        #return list of free cells 
        free_cells_list = []
        
        for row in range(3):
            for column in range(3):
                if self.matrix[row][column] == None:
                    free_cells_list.append(tuple((row,column)))
        
        return free_cells_list
    
    def check_win(self,position):
        #given a position in the board, check if there is a winning combination in the row, in the column or in the diagonal
        x,y = position
        symbol = self.matrix[x][y]
        if symbol == None:
            return False
        
        #check row
        if self.matrix[x] == [symbol,symbol,symbol]:
            return True
       #check column
        col = [None for i in range(3)]
        for c in range(3):
            col[c] = self.matrix[c][y]
        if col == [symbol,symbol,symbol]:
            return True
        
        #check diagonal
        if (self.matrix[0][0] == symbol) and (self.matrix[1][1] == symbol) and (self.matrix[2][2] == symbol):
            return True
        
        if (self.matrix[2][0] == symbol) and (self.matrix[1][1] == symbol) and (self.matrix[0][2] == symbol):
            return True
        
        return False
    
    
    def insert(self,symbol,row,column, print_out = False):
        
        self.matrix[row][column] = symbol
        if self.check_win(tuple((row,column))) and print_out:
            print(f'{symbol} won')
        
        
    
    
    
                    
    
    