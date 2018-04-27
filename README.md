# LiquidMetalBoundaryLayer

![BL Logo](https://github.com/CorbinFoucart/LiquidMetalBoundaryLayer/raw/master/img/BL_image.png)

Finite element solver for thermal boundary layer developement in flows with low Prandtl number, such
as flows of liquid metal. The solver takes advantage of the structure of the energy equation PDE in
order to solve a 2D problem as a series of 1D problems with pseudo-timestepping.  Such an approach,
along with a variable "timestep" in space, can provide a solution to the problem in a
computationally reasonable manner with the finite element method.

The governing energy equation in this regime reduces to:

<img src="https://github.com/CorbinFoucart/LiquidMetalBoundaryLayer/raw/master/img/eq.png" width="250">

- For problem formulation details and finite element considerations, see `summary.pdf`
- The solver code can be run interactively with `LiquidMetalBL_FEM.ipynb`
- The code was developed using Python 3.6 and the dependencies in `requirements.txt`
