---
type: definition
subject: gauge-theory
prereqs: ["Thm - Kuranishi Model for a Fredholm Map"]
tags: [gauge-theory, equivariant, fredholm-map, moduli]
---

# Prerequisite Concepts

- [[Thm - Kuranishi Model for a Fredholm Map]]

# The Definition

> [!definition] Equivariant Fredholm problem
> A Lie group $G$ acts smoothly on a Banach manifold $X$ and bundle $E\to X$, and a section $s$ is equivariant when $s(gx)=g,s(x)$. The moduli problem is $s^{-1}(0)/G$.

The derivative kills infinitesimal orbit directions at a zero, so it cannot be elliptic/Fredholm until one either passes to a slice or forms a deformation complex
$$\operatorname{Lie}(G)\xrightarrow{d_0}T_xX\xrightarrow{D_xs}E_x.$$
A gauge-fixing operator $d_0^*$ produces the combined operator $D_xs\oplus d_0^*$ transverse to the orbit.

# Stabilizers

If the stabilizer of $x$ is nontrivial, the quotient need not be a manifold even when the slice equation is transverse. A finite stabilizer yields an orbifold model; a positive-dimensional stabilizer produces a more singular quotient. Framing often removes constant stabilizers.

**True name:** an equivariant Fredholm problem is a finite-dimensional obstruction problem after separating symmetry directions.

