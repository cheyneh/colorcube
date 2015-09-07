from sys import argv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib import cm
import seaborn as sns
sns.set_style('white')


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



# get the rgb values as a numpy array, and create segments
pts = np.array([ pal(i)[:3] for i in range(256)])
pts = pts.reshape(-1, 1,  3)
segs = np.concatenate([pts[:-1], pts[1:]], axis = 1)

# color each segment based on the cmap, and create a collection
lc = Line3DCollection(segs, cmap = pal)
lc.set_array(np.array(range(256)))


# create the figure
fig = plt.figure(figsize = (8, 6))


# create the path
# add_axes([left, bottom, width, height], ...
ax = fig.add_axes([0,0, .8, 1], projection = '3d', aspect = 1)
ax.set_xlabel('Red')
ax.set_ylabel('Green')
ax.set_zlabel('Blue')
ax.set_title('{} palette in RGB space'.format(cmap_name))
line = ax.add_collection(lc)


# create the color bar
grad_width = 20
gradient = np.linspace(1, 0, 256)
pal_image = np.outer(gradient, np.ones(grad_width))
cbar = fig.add_axes([0.8,0,.2,1])
im = cbar.imshow(pal_image, cmap = pal)
cbar.set_yticks([])


if outfile:
    fig.savefig(outfile, dpi = 120)
else:
    plt.show()
