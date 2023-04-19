# MonteCarlo_MiniProject

This repo is my assignment for GIST MonteCarlo class.

## 1. BuffonNeedle

### By simulating throwing needle and giving statistics about does needle touched the line or not, we can get the approximate pi's value.

```
related file: buffonTest.py main.py
```

## 2. Calculating pi via size/volume ratio

### By simulating throwing needle and giving statistics about to which space needle fell(square or circle), we can get the approximate pi's value. But since this method is basically ratio between circle and regular polygon, this calculate method can expand to circle and n-th regular polygon or hypersphere and hypercube in n-th dimension.

```
related file: hitOrMiss.py htmForMultiDim.py main.py
```

## 3. Analyzing integration and comparing with normal distribution

### Just analyzing integration equation and visualized it

```
related file: integratingHW.py
```

## 4. Importance Sampling

### By using importance sampling and inverse transform, we can get approximately same result with simply sampling.

```
related file: importanceSamplingHW.py
```

## 5. Metropolis Algorithm

### By using Metropolis Algorithm, I simulated closed system's charge distribution when magnetization and total energy are in equilibrium state.

```
related file: ClosedSystem.py ClosedSystemElement.py metropolis_energy_magnetization.py
```

## 6. Thermodynamic Function

### At same environment to 4th simulation, approximately calculate indicator from thermodynamics like specific heat and susceptibility.

```
related file: ClosedSystem.py ClosedSystemElement.py, thermodynamic_function.py
```

## 7. Wang Landau Algorithm

### simulating isolated system like 2d-ising model with Wang Landau Algorith. By doing this, we can know every entropy by energy and magnetization.

```
related file: ClosedSystem.py ClosedSystemElement.py, DensityOfStates.py, WangLandauAlgorithm.py
```

## 8. Walk on Spheres

### By using Walk on Spheres we can simulate diffusion process like brownian motion efficiently.

```
walk_on_spheres.py
```
