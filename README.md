# LiquidMetalBoundaryLayer

Finite element solver for thermal boundary layer developement for liquid metals, or flows with low
Prandtl number. The solver takes advantage of the structure of the energy equation PDE in order to
solve a 2D problem as a series of 1D problems with pseudo-timestepping; an interesting idea that can
lead to solution of the problem in a computationally reasonable manner with the finite element
method, along with a variable "timestep" in space.

![BL Logo](https://github.com/CorbinFoucart/LiquidMetalBoundaryLayer/raw/master/img/BL_image.png)

The governing energy equation in this regime reduces to:
\begin{align}
  \left[u(y)\right]\frac{\partial T}{\partial x} 
  &= \frac{k}{\rho c_p} \frac{\partial^2 T}{\partial y^2} 
\end{align}

- For problem formulation details and finite element considerations, see `summary.pdf`
- The solver code can be run interactively with `LiquidMetalBL_FEM.ipynb`
