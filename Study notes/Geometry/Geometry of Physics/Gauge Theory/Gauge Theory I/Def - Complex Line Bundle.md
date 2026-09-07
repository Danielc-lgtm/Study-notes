---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Vector Bundle"
  - "Def - Transition Function"
tags: [geometry, gauge-theory, line-bundle]
---

# Prerequisite Concepts

- [[Def - Vector Bundle]]
- [[Def - Transition Function]]

# Notation

Let $M$ be a smooth manifold. The multiplicative group of nonzero complex numbers is $\mathbb C^\times$; its unit circle is $U(1)$.

# The Definition

> [!definition] Complex line bundle
> A **complex line bundle** is a rank-one complex vector bundle $\pi:L\to M$. Equivalently, it is specified by an open cover $(U_\alpha)$ and smooth transition functions
> $$g_{\alpha\beta}:U_\alpha\cap U_\beta\to\mathbb C^\times$$
> satisfying
> $$g_{\alpha\alpha}=1,\qquad g_{\alpha\beta}=g_{\beta\alpha}^{-1},\qquad
> g_{\alpha\beta}g_{\beta\gamma}g_{\gamma\alpha}=1.$$

A nowhere-zero local section is a local frame. A global nowhere-zero section trivializes $L$: the map $(x,z)\mapsto z,s(x)$ is a bundle isomorphism $M\times\mathbb C\to L$. Conversely, a trivialization supplies such a section. Thus a line bundle's nontriviality is precisely the obstruction to choosing one nonvanishing frame globally.

# Legal Operations

Transition functions show immediately that
$$
g^{L\otimes K}_{\alpha\beta}=g^L_{\alpha\beta}g^K_{\alpha\beta},\qquad
 g^{L^*}_{\alpha\beta}=(g^L_{\alpha\beta})^{-1}.
$$
Hence tensor product adds and dualization negates the first Chern class. Pullback composes transition functions with the base map.

After choosing a Hermitian metric, unitary frames have $U(1)$-valued transition functions. A unitary connection is locally an imaginary-valued $1$-form, and its normalized curvature represents $c_1(L)$ in de Rham cohomology.

# Examples / Corollaries

- $M\times\mathbb C$ is the trivial line bundle.
- The tautological bundle over $\mathbb{CP}^n$ has fibre over $[v]$ equal to the line $\mathbb Cv\subset\mathbb C^{n+1}$.
- The Dirac monopole bundle $L_n\to S^2$ has transition function $e^{in\varphi}$ and first Chern number $n$.

A section of a line bundle is not intrinsically a complex-valued function. It becomes a function only after a local frame is chosen; on overlaps its coefficient transforms by the inverse transition function. This is why a charged field and a gauge potential must transform together.

# Unlocked by This

Hermitian line bundles are the geometric carriers of abelian gauge theory. Their connections describe electromagnetic potentials, their curvature describes field strength, and their Chern class records quantized flux.
