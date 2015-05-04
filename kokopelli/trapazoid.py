from koko.lib.shapes import *


def trapazoid(length, height, left_offset, right_offset):
    """ Create a 2D Trapazoid. It will be the union of two triangles and a rectangle
    @param length The length of the base of the trapazoid
    @param height The height of the trapazoid
    @param left_offset The offset from the end of the base to the end of the top of the trapazoid on the left
    @param right_offset The offset from the end of the base to the end of the top of the trapazoid on the right
    The trapazoid will be a triangle joined with a rectangle and another triangle.
    The base of the trapazoid will be in the positive x direction. With the height in the y direction.
    """
    assert left_offset + right_offset < length
    assert left_offset >= 0
    assert right_offset >= 0
    net_shape = None
    if left_offset > 0:
        # triangle seems to require clockwise
        net_shape += triangle(0, 0, left_offset, height, left_offset, 0)
    net_shape += rectangle(left_offset, length - right_offset, 0, height)
    if right_offset > 0:
       net_shape += triangle(length-right_offset, 0, length-right_offset, height, length, 0)
    return net_shape
    
def make_foam_trapazoid(length, height, left_offset, right_offset, color=None):
    t = trapazoid(length, height, left_offset, right_offset)
    obj = extrusion(t, 0, 2 * 0.0254)
    if color:
        obj.color = color
    return obj

def make_foam_sheet(length, width, color):
    hc_base = rectangle(0, length, 0, width)
    #hc_base = rotate_z(hc_base, 0)
    hc_base = extrusion(hc_base, 0, 2*0.0254)
    hc_base.color = color
    return hc_base

#shapes = {}
#shapes['main1'] = make_foam_sheet(8, 4, 'green')# render all shapes
#shapes['trap'] = make_foam_trapazoid(4,2,1,1, 'green')
#cad.shapes =[s for s in shapes.values()]
