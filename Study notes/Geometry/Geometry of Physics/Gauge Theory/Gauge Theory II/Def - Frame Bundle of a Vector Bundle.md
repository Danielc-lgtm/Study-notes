---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Def - Vector Bundle"
tags: [gauge-theory, frame-bundle, principal-bundle]
---

# Notation

Let $E\to B$ be a rank-$r$ vector bundle over $\mathbb K=\mathbb R$ or $\mathbb C$.

# The Definition

> [!definition] Frame bundle
> The **frame bundle** $\operatorname{Fr}(E)$ has fibre
> $$
> \operatorname{Fr}(E)_x=\operatorname{Iso}_\mathbb K(\mathbb K^r,E_x).
> $$
> It is a right principal $\mathrm{GL}_r(\mathbb K)$-bundle under composition,
> $$u\cdot g=u\circ g.$$

A bundle frame $(e_1,\ldots,e_r)$ determines $u(a^1,\ldots,a^r)=a^je_j$. Changing the ordered basis of $\mathbb K^r$ on the right is free and transitive on the frames of $E_x$. A vector-bundle trivialization therefore gives a principal trivialization of $\operatorname{Fr}(E)$, proving smooth local triviality.

# Reconstruction

The defining representation recovers $E$:
$$
\operatorname{Fr}(E)\times_{\mathrm{GL}_r}\mathbb K^r\xrightarrow{\sim}E,
\qquad[u,v]\longmapsto u(v).
$$
The relation $[ug,v]=[u,gv]$ makes the map well defined. Thus rank-$r$ vector bundles and principal $\mathrm{GL}_r$-bundles encode the same data up to the corresponding notions of isomorphism.

# Examples / Corollaries

A global frame is a global section of $\operatorname{Fr}(E)$, so $E$ is trivial exactly when its frame bundle is. For $E=TB$, $\operatorname{Fr}(TB)$ is often abbreviated $\operatorname{Fr}(B)$.

# Unlocked by This

Additional fibre structure selects smaller classes of frames and hence reductions of the frame bundle: orthonormal, oriented, symplectic, complex, spin, and spin$^c$ frames.
