# OpenFOAM Airfoil Verification Study

**Tool:** OpenFOAM

## Objective

2D incompressible airfoil CFD workflow with mesh refinement, y+ tracking, force coefficient extraction, and validation-style reporting.

## Why this project matters

This project is designed to show aerospace-relevant simulation judgement rather than only tool familiarity. The expected output should demonstrate setup discipline, convergence checking, post-processing automation and clear engineering interpretation.

## Planned workflow

1. Define the physical problem and assumptions.
2. Create the baseline numerical setup.
3. Run a coarse, medium and fine study where appropriate.
4. Extract key engineering metrics.
5. Compare with an analytical, benchmark or literature reference where available.
6. Summarise limitations and next improvements.

## Skills demonstrated

- OpenFOAM
- snappyHexMesh/blockMesh
- ParaView
- Python post-processing
- mesh convergence

## Target deliverables

- Mesh independence report
- CL/CD polar plot
- residual and force convergence dashboard

## Suggested folder structure

```text
.
├── case/
├── scripts/
├── results/
├── figures/
└── README.md
```

## Summary

Built a reproducible OpenFOAM simulation workflow for aerospace-relevant numerical analysis, including setup automation, convergence checks, post-processing and engineering interpretation.
