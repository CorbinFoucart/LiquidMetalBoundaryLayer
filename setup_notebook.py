import numpy as np
import sympy as sym
from sympy.tensor.array import Array, derive_by_array
import matplotlib.pyplot as plt
import matplotlib.tri as mtri               # delaunay triangulation
from mpl_toolkits.mplot3d import Axes3D     # surface plotting
import seaborn as sns
import pdb

# config
sym.init_printing(use_latex='mathjax')      # render latex for output

## plotting
sns.set()                                   # nice plotting defaults
%matplotlib inline
%config InlineBackend.figure_format = 'svg' # vectorized plots instead
