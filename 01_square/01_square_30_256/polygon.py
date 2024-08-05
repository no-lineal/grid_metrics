import numpy as np
import math
from shapely.geometry import Polygon, Point, LineString, box
from shapely.affinity import scale, translate

def square( area, factor = 1 ):

    area = area * factor

    box_width = np.sqrt( area )
    box_height = box_width

    square = Polygon(
        [ 
            (- box_width/2, - box_height/2), 
            (- box_width/2, box_height/2), 
            (box_width/2, box_height/2),
            (box_width/2, - box_height/2) 
        ] 
    )
    
    return square

def rectangle( area, factor = 1 ):

    area = area * factor

    box_width = np.sqrt( area ) / 2
    box_height = np.sqrt( area ) * 2

    rectangle = Polygon(
        [ 
            (- box_width/2, - box_height/2), 
            (- box_width/2, box_height/2), 
            (box_width/2, box_height/2),
            (box_width/2, - box_height/2) 
        ] 
    )
    
    return rectangle

def circle( area, factor = 1 ):

    area = area * factor

    radius = np.sqrt( area / np.pi )

    center = Point(0, 0)

    circle = center.buffer( radius )

    return circle

def elipse( area, factor = 1 ):

    area = area * factor

    b = np.sqrt( area / ( np.pi * 2 ) )
    a = 2 * b

    c = Point(0, 0).buffer( 1 )
    e = scale( c, xfact=a, yfact=b )

    return e

def trapezoid( area, factor = 1 ):

    area = area * factor

    l = np.sqrt( area )

    h = l / 2
    b1 = l 
    b2 = 2*( area / h ) - b1

    tpz = Polygon(
        [
            (-b1/2, -h/2),
            (-b2/2, h/2),
            (b2/2, h/2),
            (b1/2, -h/2)
        ]
    )

    return tpz

def annulus( area, factor = 1 ):

    area = area * factor

    r = np.sqrt( area ) / 2
    R = np.sqrt( (area/np.pi) + r**2 )

    outer_circle = Point(0, 0).buffer( R )
    inner_circle = Point(0, 0).buffer( r )

    ann = outer_circle.difference( inner_circle )

    return ann

def polygon_hall( area, factor = 1 ):

    area = area * factor

    a_1 = area * 0.75
    a_2 = area * 0.25

    al = a_1 / 2
    ar = a_1 / 2

    l_al = np.sqrt( al )
    l_ar = np.sqrt( ar )

    l1_a2 = np.sqrt( a_2 ) + ( 0.75 * np.sqrt( a_2 ) )
    l2_a2 = 0.25 * np.sqrt( a_2 )

    left_bar = box( -l_al - l1_a2/2, -l_al/2, -l1_a2/2, l_al/2 ) 
    right_bar = box( l1_a2/2, -l_ar/2, l1_a2/2 + l_ar, l_ar/2 )
    middle_bar = box( -l1_a2/2, -l2_a2/2, l1_a2/2, l2_a2/2 )

    h_shape = left_bar.union(right_bar).union(middle_bar)

    return h_shape

def equilateral_triangle( area, factor = 1 ):

    area = area * factor

    a = np.sqrt( area * 4 / np.sqrt(3) )
    h = ( a * np.sqrt(3) ) / 2

    triangle = Polygon(
        [
            (-a/2, -h/3),
            (a/2, -h/3),
            (0, 2*h/3)
        ]
    )

    return triangle

def isoceles_triangle( area, factor = 1 ):

    area = area * factor

    h = np.sqrt( area )
    b = (2 * area) / h

    triangle = Polygon(
        [
            (-b/2, -h/2),
            (b/2, -h/2),
            (0, h/2)
        ]
    )

    return triangle

def triangle_area( v1, v2, v3 ):

    x1, y1 = v1
    x2, y2 = v2
    x3, y3 = v3

    # area given the vertices of a polygon
    return 0.5 * np.abs( x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2) )

def scalene_triangle( area, factor = 1 ):

    area = area * factor

    b = np.sqrt( area )
    hb = (2 * area) / b

    v1 = (0, hb/2)

    v2 = ( np.random.uniform(1, 10), np.random.uniform(1, 10) )
    v3 = ( np.random.uniform(1, 10), np.random.uniform(1, 10) )

    init_area = triangle_area( v1, v2, v3 ) 

    scale_factor = np.sqrt( area / init_area )

    v2 = ( v2[0] * scale_factor, v2[1] * scale_factor )
    v3 = ( v3[0] * scale_factor, v3[1] * scale_factor )

    triangle = Polygon( [ v1, v2, v3 ] )

    return triangle



def get_polygon( polygon, area, factor ):

    if polygon == 'square':

        return square( area, factor )
    
    elif polygon == 'rectangle':

        return rectangle( 2.2**2, factor )
    
    elif polygon == 'circle':

        return circle( 2.2**2, factor )
    
    elif polygon == 'elipse':

        return elipse( 2.2**2, factor )
    
    elif polygon == 'trapezoid':

        return trapezoid( 2.2**2, factor )
    
    elif polygon == 'annulus':

        return annulus( 2.2**2, factor )
    
    elif polygon == 'polygon_hall':

        return polygon_hall( 2.2**2, factor )
    
    elif polygon == 'equilateral_triangle':

        return equilateral_triangle( 2.2**2, factor )
    
    elif polygon == 'isoceles_triangle':

        return isoceles_triangle( 2.2**2, factor )
    
    elif polygon == 'scalene_triangle':

        return scalene_triangle( 2.2**2, factor )
    
    else:

        raise ValueError( 'Invalid polygon.' )
