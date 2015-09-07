from sys import argv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3DCollection
from matplotlib import cm
import seaborn as sns
sns.set_style('dark')


# get the color palette, default to cubehelix
try:
    cmap_name = argv[1]
except IndexError:
    cmap_name = 'cubehelix'
pal = cm.get_cmap(cmap_name)



pts = np.array([ pal(i)[:3] for i in range(256)])
pts = pts.reshape(-1, 1,  3)
segs = np.concatenate([pts[:-1], pts[1:]], axis = 1)

lc = Line3DCollection(segs, cmap = pal)
lc.set_array(np.array(range(256)))


fig = plt.figure(figsize = (8, 6))
ax = plt.subplot2grid((1,4), (0,0), colspan = 3, projection = '3d', aspect = 1)
ax.set_xlabel('Red')
ax.set_ylabel('Green')
ax.set_zlabel('Blue')
ax.set_title('{} Palette in RGB Space'.format(cmap_name))
ax.add_collection(lc)


# make the gradient
grad_width = 20
gradient = np.linspace(0, 1, 256)
pal_image = np.outer(gradient, np.ones(grad_width))
ax2 = plt.subplot2grid( (1,4), (0,3) )
ax2.imshow(pal_image, cmap = pal)
ax2.set_axis_off()

# fig.tight_layout()


plt.show()
