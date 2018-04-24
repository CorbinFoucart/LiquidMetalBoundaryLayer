# LiquidMetalBoundaryLayer

Finite element solver for thermal boundary layer developement for liquid metals, or flows with low
Prandtl number. The solver takes advantage of the structure of the energy equation PDE in order to
solve a 2D problem as a series of 1D problems with pseudo-timestepping.

![BL Logo](https://github.com/CorbinFoucart/LiquidMetalBoundaryLayer/raw/master/img/BL_image.png)

- For problem details and finite element considerations, see `summary.pdf`
- The solver code can be run interactively with `LiquidMetalBL_FEM.ipynb`
