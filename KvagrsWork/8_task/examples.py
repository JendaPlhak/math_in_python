#!usr/bin/env python

from affine_transformation import *
from numpy                 import array

if __name__ == '__main__':

    points = array([[0,0,1],[50,0,1],[50,50,1],[0,50,1]])
        
    # First example from http://www.fi.muni.cz/~xpelanek/IV122/slidy/lingebra.pdf
    operator = combine(rotation(20), scaling(1.1, 1.1), translation(5, 10))
    operator = combine(translation(5, 10), scaling(1.1, 1.1), rotation(20))
    lines = line_transformation(points, iteration=10, matrix=operator)   
    plot_and_save('1_example', lines)
    

    points = array([[-50, -50,1],[50,-50,1],[50,50,1],[-50,50,1]])
    # Second example from http://www.fi.muni.cz/~xpelanek/IV122/slidy/lingebra.pdf
    operator = combine(rotation(10), scaling(1.1,0.8))
    lines = line_transformation(points, iteration=15, matrix=operator)   
    plot_and_save('2_example', lines)
    
    # Third example from http://www.fi.muni.cz/~xpelanek/IV122/slidy/lingebra.pdf
    operator = combine(translation(50, 50), scaling(0.9, 0.9), rotation(10), shear(1.3))
    lines = line_transformation(points, iteration=25, matrix=operator)   
    plot_and_save('3_example', lines)