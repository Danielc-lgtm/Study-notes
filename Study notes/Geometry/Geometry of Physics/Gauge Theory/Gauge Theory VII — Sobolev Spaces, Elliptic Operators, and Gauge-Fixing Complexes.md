---
type: topic
subject: gauge-theory
chapter: "Gauge Theory VII"
title: "Gauge Theory VII — Sobolev Spaces, Elliptic Operators, and Gauge-Fixing Complexes"
tags: [gauge-theory, sobolev-spaces, elliptic-operators, fredholm, elliptic-complex]
---

# Notation Registry

$M^n$ is compact and without boundary unless stated otherwise; $E,F\to M$ are metric bundles. $W^{k,p}(E)$ controls weak covariant derivatives through order $k$ in $L^p$. For an order-$\ell$ differential operator $L$, $\sigma_L(x,\xi)$ is its principal symbol. Formal adjoints use the $L^2$ pairing.

# Motivation

Gauge equations are nonlinear PDEs on spaces of smooth fields, but smooth spaces are not complete and gauge symmetry destroys ellipticity before a slice is chosen. Sobolev completion repairs the first defect. Symbol exactness and adjoint gauge fixing repair the second. The reward is finite-dimensional behavior: kernels and cokernels become finite, weak solutions become smooth, and each linear gauge class acquires a canonical harmonic representative.

The analytic chain is
$$\text{Sobolev control}\Longrightarrow\text{compact embedding}\Longrightarrow
\text{elliptic estimate}\Longrightarrow\text{Fredholmness}\Longrightarrow
\text{finite-dimensional moduli data}.$$

# Concept Map

## §7.1 Sobolev spaces

- [[Def - Sobolev Space of Bundle Sections]] fixes bundle-valued norms, weak derivatives, equivalent choices, and boundary conventions.
- [[Thm - Sobolev Embedding, Compactness, and Multiplication]] organizes continuity, Rellich compactness, regularity, and nonlinear products by the index $k-n/p$.

![[Exercise Index - §7.1 Sobolev Spaces]]

## §7.2 Elliptic operators and Fredholm theory

- [[Def - Principal Symbol and Elliptic Differential Operator]] extracts the high-frequency operator and tests invertibility.
- [[Thm - Elliptic Estimate and Regularity]] proves derivative gain and smoothness of weak solutions.
- [[Def - Fredholm Operator and Index]] records the finite-dimensional defects and correct index sign.
- [[Thm - Elliptic Operators are Fredholm and the Fredholm Alternative]] proves closed range and the orthogonality solvability criterion.

## §7.3 Elliptic complexes and gauge fixing

- [[Def - Elliptic Complex and Associated Laplacian]] replaces invertibility of a single symbol by exactness of a symbol sequence.
- [[Thm - Hodge Theorem for an Elliptic Complex]] proves the orthogonal decomposition and harmonic-representative theorem.

![[Exercise Index - §7.2 Elliptic Operators and Complexes]]

# Sources and Targets

A minimizing sequence targets a convergent subsequence, so compare its bounded norm with a compact Sobolev embedding. A weak solution targets smoothness, so feed the equation into an elliptic estimate repeatedly. A linear equation targets solvability, so compute the adjoint kernel. A gauge-degenerate equation targets an elliptic system, so append the formal adjoint of the infinitesimal gauge action.

# Legal Operations

1. **Compare Sobolev indices $k-n/p$.** This predicts continuous embeddings before any estimate is attempted.
2. **Demand strict loss for compactness.** Equality permits scale-invariant concentrating sequences.
3. **Use multiplication only above the algebra threshold or with a verified product estimate.** Smooth multiplication does not automatically extend to every completion.
4. **Discard lower-order terms when computing symbols.** Derivatives of coordinate changes affect only lower order.
5. **Use the elliptic estimate with its kernel-controlling norm.** Remove that term only on a chosen complement of the kernel.
6. **Bootstrap weak solutions.** Each application gains the operator order in regularity.
7. **Test solvability against $\ker L^*$.** The source must be orthogonal to the adjoint kernel, not belong to it.
8. **Build the Laplacian of a complex.** $L^*L+LL^*$ converts symbol exactness into ordinary ellipticity.
9. **Impose the adjoint gauge condition.** $L_0^*a=0$ selects the orthogonal slice to infinitesimal gauge orbits.

## Illegal but tempting

Boundedness in a Sobolev space does not yield convergence in the same norm; a strict compact embedding is needed. Ellipticity is not invertibility: harmonic sections form a finite-dimensional kernel. The Fredholm alternative does not say $t\in\ker L^*$; it says $t\perp\ker L^*$. A nonlinear gauge quotient is not automatically a manifold merely because its linearized complex is elliptic; stabilizers and obstructions remain.

# Problem-Solving Strategy

First choose Sobolev exponents so every nonlinear product is continuous and gauge transformations have enough pointwise regularity. Then linearize, compute the entire symbol sequence, and add the adjoint gauge condition. Apply elliptic estimates for regularity and Rellich for compactness. Finally separate kernel, image, and cokernel rather than assuming an inverse. The unifying question is: **after completing and gauge-fixing, which infinite-dimensional directions remain genuinely finite-dimensional?**

# Most Reusable Properties

- Sobolev topology on a compact bundle is independent of auxiliary connections and metrics.
- Strict Sobolev-index improvement gives subsequential compactness, the engine of variational limits.
- Elliptic regularity says distributional kernel elements are smooth.
- Elliptic operators on closed manifolds are Fredholm; their cokernel is the adjoint kernel.
- Elliptic-complex cohomology is represented uniquely by harmonic sections and is finite dimensional.

# Insights

Gauge fixing is not an aesthetic normalization. The original linearized equation has symbol kernel exactly along gauge directions. Appending the adjoint infinitesimal action makes the combined symbol invertible transverse to those directions, allowing elliptic theory to see the quotient.

The lower-order norm in an elliptic estimate encodes topology: it is present because the operator may have a genuine global kernel even though its symbol is invertible at every nonzero frequency. Local analysis controls derivatives; finite-dimensional kernel data records the remaining global ambiguity.

# Bridges

Gauge Theory VIII uses Fredholm splittings to build Kuranishi models, transversality, determinant lines, and degree. Gauge Theory IX chooses Sobolev completions for the Seiberg–Witten configuration and gauge spaces and uses an elliptic deformation complex.

# Sources

- Andriy Haydys, *Introduction to Gauge Theory*, §§5.1–5.3.
