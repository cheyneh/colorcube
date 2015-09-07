# colorcube
A simple tool for visualizing a colormap by plotting it on the RGB color cube. 
Accepts any of the colormaps known to matplotlib.

Syntax:
    
    $./colorcube.py <cmap_name> <outfile>

If not given an outfile, will default to an interactive matplotlib plot, 
allowing you to rotate and zoom the 3D axes. 

## Example usage:

    $ ./colorcube.py cubehelix

produces:

![cubehelix](https://raw.github.com/cheyneh/colorcube/master/cubehelix.png)

    $ ./colorcube.py coolwarm

produces:

![coolwarm](https://raw.github.com/cheyneh/colorcube/master/coolwarm.png)

and 

    $ ./colorcube.py jet

produces:

![don't use jet](https://raw.github.com/cheyneh/colorcube/master/jet.png)
