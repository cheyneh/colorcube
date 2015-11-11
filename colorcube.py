#! /usr/bin/env python3
# Tool to visualize a colormap by plotting it on the RGB cube
# cheyne.homberger@gmail.com

from sys import argv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib import cm
import seaborn as sns

sns.set_style('white')


def make_cube(pal):
    # get the rgb values as a numpy array, and create segments
    pts = np.array([ pal(i)[:3] for i in range(256)])
    pts = pts.reshape(-1, 1,  3)
    segs = np.concatenate([pts[:-1], pts[1:]], axis = 1)

    # color each segment based on the cmap, and create a collection
    lc = Line3DCollection(segs, cmap = pal)
    lc.set_array(np.arange(256))

    # create the figure
    fig = plt.figure(figsize = (8, 6))

    # create the path
    ax = fig.add_axes([0,0, .8, 1], projection = '3d', aspect = 1)
    ax.set_xlabel('Red')
    ax.set_ylabel('Green')
    ax.set_zlabel('Blue')
    ax.set_title('{} palette in RGB space'.format(cmap_name))
    ax.add_collection(lc)
    ax.set_xlim3d(0,1)
    ax.set_ylim3d(0,1)
    ax.set_zlim3d(0,1)

    # create the color bar
    grad_width = 20
    gradient = np.linspace(0, 1, 256)
    pal_image = np.outer(gradient, np.ones(grad_width))
    cbar = fig.add_axes([0.8,.1,.2,.8])
    cbar.imshow(pal_image, cmap = pal)
    cbar.set_xticks([])
    cbar.set_yticks([])

    return fig


if __name__ == '__main__':
    # TODO: use argparse to make this less awful
    # get the color palette, default to cubehelix
    try:
        cmap_name = argv[1]
    except IndexError:
        cmap_name = 'cubehelix'
    try:
        outfile = argv[2]
    except IndexError:
        outfile = None

    pal = cm.get_cmap(cmap_name)

    cube = make_cube(pal)


    if outfile:
        cube.savefig(outfile, dpi = 144)
    else:
        plt.show()
