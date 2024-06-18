"""
@file geometry.py
@brief Basic geometry computation functions
"""
import math

def rectangle_area(length, width):
    """
    Compute the area of a rectangle
    
    @param length One dimension of the rectangle
    @param width The other dimension of the rectangle
    @return The area of the rectangle
    """
    return (length * width)

def rectangle_perimeter(length, width):
    """
    Compute the perimeter of a rectangle
    
    @param length One dimension of the rectangle
    @param width The other dimension of the rectangle
    @return The perimeter of the rectangle
    """
    return ((length + width)*2)

def circle_area(radius):
    """
    Compute the area of a circle
    
    @param radius The radius of the circle
    @return The area of the circle
    """
    return (radius * radius * math.pi) 

def circle_circumference(radius):
    """
    Compute the circumference of a circle
    
    @param radius The radius of the circle
    @return The circumference of the circle
    """
    return (2 * radius * math.pi)
