---
type: topic
subject: gauge-theory
chapter: "Gauge Theory VIII"
title: "Gauge Theory VIII — Fredholm Maps, Transversality, Determinant Lines, and Degree"
tags: [gauge-theory, fredholm, transversality, determinant-line, degree]
---

# Notation Registry

$X,Y$ are separable Banach manifolds, $f:X\to Y$ a smooth Fredholm map, and $s$ a Fredholm section. At a zero, $D$ denotes the linearization, $K=\ker D$, and $C=\operatorname{coker}D$. Proper means inverse images of compact sets are compact.

# Motivation

A nonlinear gauge equation has infinitely many variables, yet ellipticity confines local deformations and obstructions to finite-dimensional kernel and cokernel spaces. The Kuranishi model makes this reduction explicit. Transversality removes the obstruction generically; properness prevents solutions from escaping; determinant lines supply signs. These are the four ingredients behind a deformation-invariant solution count.

# Concept Map

- [[Def - Smooth Fredholm Map and Regular Value]] and [[Thm - Kuranishi Model for a Fredholm Map]] give the local finite-dimensional model.
- [[Thm - Sard-Smale and Parametric Transversality]] explains why regular perturbations are generic.
- [[Def - Mod-2 Degree of a Proper Fredholm Map]] counts without orientations.
- [[Def - Determinant Line and Orientation of a Fredholm Operator]] packages kernel/cokernel signs through jumping dimensions.
- [[Def - Integer Degree of an Oriented Fredholm Map]] gives signed counts and cobordism invariance.
- [[Def - Equivariant Fredholm Problem]] inserts slices, stabilizers, and gauge deformation complexes.

# Sources and Targets

A nonlinear equation targets a finite-dimensional local zero set: split its Fredholm derivative and form the Kuranishi obstruction map. A singular zero set targets a generic smooth one: enlarge by perturbation parameters and apply parametric transversality. A zero-dimensional compact moduli space targets an invariant: count modulo two, or orient the determinant line and count with signs.

# Legal Operations

1. Split domain and codomain by kernel, range, and cokernel before applying the implicit-function theorem.
2. Perturb in a parameter family whose universal section is transverse.
3. Use residual genericity only after checking separability and differentiability.
4. Use properness to turn zero-dimensional regular fibres into finite sets and one-parameter fibres into compact cobordisms.
5. Count modulo two when no coherent orientation is available.
6. Orient the determinant line, not kernels independently at each point.
7. Pass to a gauge slice before declaring an equivariant problem Fredholm.
8. Separate reducible stabilizers from failure of transversality.

## Illegal but tempting

Transversality does not imply compactness; sequences may escape. Properness does not imply regularity; singular solutions may persist. Kernel orientations alone do not orient a non-surjective family; the cokernel factor is required. Dividing by a gauge group without checking stabilizers can turn a smooth zero set into a singular quotient.

# Problem-Solving Strategy

Linearize, split, and identify deformation versus obstruction. Next construct enough perturbations for universal transversality. Prove compactness independently. Finally decide whether parity suffices or whether determinant-line orientations are coherent. The unifying question is: **which hypotheses turn a nonlinear infinite-dimensional zero set into a finite, deformation-invariant count?**

# Insights

The Kuranishi map is the exact nonlinear remainder left after solving every infinite-dimensional range direction. Its derivative vanishes because the original linearization already accounts for first order. Thus singularity is compressed into a finite-dimensional higher-order obstruction.

Degree invariance is fundamentally a boundary statement: a generic one-parameter family produces a one-manifold, whose boundary consists of endpoint solutions. Mod-two degree forgets boundary signs; integer degree remembers them through the determinant line.

# Bridges

Gauge Theory IX applies this framework to the Seiberg–Witten section. Gauge Theory X uses the resulting oriented zero-dimensional moduli space to define an invariant.

# Sources

- Andriy Haydys, *Introduction to Gauge Theory*, §§6.1–6.6.
