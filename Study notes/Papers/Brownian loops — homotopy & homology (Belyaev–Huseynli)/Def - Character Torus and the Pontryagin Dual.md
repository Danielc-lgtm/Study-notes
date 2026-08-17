---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Geometrically Finite Surfaces, Cusps and Funnels"
  - "Thm - Hurewicz Theorem (Statement)"
tags: [paper, algebra, topology, harmonic-analysis]
---

# Notation

- $H_1(X,\mathbb{Z})$ — the first homology group, the abelianisation of $\pi_1(X)\cong\Gamma$; $\Gamma\twoheadrightarrow H_1(X,\mathbb{Z})$ the abelianisation map ([[Def - Hurewicz Map]])
- $[\gamma]$ — the image in homology of an oriented primitive closed geodesic $\gamma$; note $[\gamma^m]=m[\gamma]$
- $r$ — the rank of $H_1(X,\mathbb{Z})$: $r=2g$ for a closed surface of genus $g$; $r=2g+b-1=2g+n_C+n_F-1$ when $X$ has $b\geq1$ ends
- $\chi : H_1(X,\mathbb{Z})\to\mathbb{C}^\times$ — a character; **unitary** when the image lies in $S^1$
- $\widehat{H_1(X,\mathbb{Z})}$ — the character torus, or Pontryagin dual; $\mathrm{d}\chi$ its normalised Haar measure
- $e_1,\dots,e_r$ — a $\mathbb{Z}$-basis; $\theta_1,\dots,\theta_r\in\mathbb{R}/\mathbb{Z}$ the corresponding phases

---

# In plain language

Homology is the abelianisation of the fundamental group: it remembers the net winding around each cycle and forgets the order in which handles are traversed. For a geometrically finite surface it is a free abelian group $\mathbb{Z}^r$, so it is completely described by a rank.

A **character** is a homomorphism $H_1(X,\mathbb{Z})\to\mathbb{C}^\times$; the **unitary** ones, landing in $S^1$, form the **character torus** or **Pontryagin dual** $\widehat{H_1(X,\mathbb{Z})}$. Since a homomorphism out of $\mathbb{Z}^r$ is determined by its values on a basis, and each value is a point of $S^1$,
$$\widehat{H_1(X,\mathbb{Z})}\cong(S^1)^r\cong(\mathbb{R}/\mathbb{Z})^r,$$
a compact $r$-dimensional torus.

**Why the paper needs it.** §6.2 wants the mass in a single homology class, which is an infinite sum over the free homotopy classes lying above it — no closed form is available directly. The device is Fourier analysis on the group $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$, whose dual is this compact torus: **the function $\beta\mapsto\mu^\kappa_X(\beta)$ and the function $\chi\mapsto-\log L_X(s,\chi)$ are a Fourier pair.** Fourier inversion then computes a single homology class's mass as one integral over a compact torus, and the tool that makes inversion work is orthogonality of characters,
$$\int_{\widehat{H_1(X,\mathbb{Z})}}\chi(\beta')\overline{\chi(\beta)}\,\mathrm{d}\chi = \begin{cases}1,&\beta'=\beta,\\0,&\text{otherwise},\end{cases}$$
with $\mathrm{d}\chi$ the normalised Haar measure. That single identity is the entire proof of [[Thm - Fourier Expansion and Inversion by Homology Class|Theorem 6.5]].

The compactness is what makes the construction useful: an infinite sum is traded for an integral over a *finite-dimensional compact* space, and Haar measure on it is just $\mathrm{d}\theta_1\cdots\mathrm{d}\theta_r$ on $(\mathbb{R}/\mathbb{Z})^r$.

---

# The definition

> **Definition (character and character torus).** A **character** of $H_1(X,\mathbb{Z})$ is a homomorphism $\chi:H_1(X,\mathbb{Z})\to\mathbb{C}^\times$. The **unitary** characters $\chi:H_1(X,\mathbb{Z})\to S^1$ form the **character torus**, or **Pontryagin dual**, $\widehat{H_1(X,\mathbb{Z})}$.

> **The rank and the torus.** For a closed surface of genus $g$, $H_1(X,\mathbb{Z})\cong\mathbb{Z}^{2g}$. For a geometrically finite non-compact surface with $b\geq1$ ends, of which $n_C$ are cusps and $n_F$ are funnels, the rank is $2g+b-1$, and since $b=n_C+n_F$ this gives $H_1(X,\mathbb{Z})\cong\mathbb{Z}^{2g+n_C+n_F-1}$. Writing $r$ for the rank, a unitary character is determined by its values on a $\mathbb{Z}$-basis: choosing $e_1,\dots,e_r$ and phases $\theta_1,\dots,\theta_r\in\mathbb{R}/\mathbb{Z}$ with $\chi(e_j)=e^{2\pi i\theta_j}$,
> $$\widehat{H_1(X,\mathbb{Z})}\cong(S^1)^r\cong(\mathbb{R}/\mathbb{Z})^r.$$

> **Orthogonality of characters.** With $\mathrm{d}\chi$ the normalised Haar measure on $\widehat{H_1(X,\mathbb{Z})}$, for $\beta,\beta'\in H_1(X,\mathbb{Z})$,
> $$\int_{\widehat{H_1(X,\mathbb{Z})}}\chi(\beta')\,\overline{\chi(\beta)}\,\mathrm{d}\chi = \delta_{\beta\beta'}.$$

---

# Types and signatures

- $H_1(X,\mathbb{Z})\cong\mathbb{Z}^r$ — a free abelian group of finite rank; $\beta$ a general element
- $\chi : H_1(X,\mathbb{Z})\to S^1$ — a group homomorphism; **not** a function on the surface
- $\widehat{H_1(X,\mathbb{Z})}$ — a compact abelian Lie group, isomorphic to $(S^1)^r$; **not canonically** so, the isomorphism depending on a choice of $\mathbb{Z}$-basis
- $\mathrm{d}\chi$ — the normalised Haar measure, total mass $1$; in coordinates $\mathrm{d}\theta_1\cdots\mathrm{d}\theta_r$
- $\mathbf{1}$ — the trivial character, $\chi\equiv1$; the identity element of the torus

**The composite that the paper actually uses** is $\Gamma\twoheadrightarrow H_1(X,\mathbb{Z})\xrightarrow{\chi}S^1$, a **one-dimensional unitary representation of $\Gamma$ that factors through the abelianisation.** That is exactly the abelian case of [[Def - Ruelle Zeta Function and its Twist|the twist]] by a representation $\rho$ of $\Gamma$, and it is why §6.2's identity is cleaner than §4's twisted Ruelle identity.

---

# Example

A closed surface of genus $2$: $r=4$, $H_1(X,\mathbb{Z})\cong\mathbb{Z}^4$, and $\widehat{H_1(X,\mathbb{Z})}\cong(S^1)^4$, a $4$-torus. A once-punctured torus: $g=1$, $b=1$, so $r=2\cdot1+1-1=2$ and the character torus is $(S^1)^2$. A three-funnelled sphere: $g=0$, $b=3$, so $r=2$ again.

The trivial character $\chi=\mathbf{1}$ gives $L_X(s,\mathbf{1})=Z_X(s)$, so [[Thm - Selberg L-Function Identity|Corollary 6.4]] contains [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]] as its value at one point of the torus. **The whole of §6.2 is §4.1 evaluated at every point of the torus at once, then Fourier-inverted.**

**Near-miss non-example — a non-unitary character.** A homomorphism $H_1(X,\mathbb{Z})\to\mathbb{C}^\times$ with $|\chi(\beta)|\neq1$ is a perfectly good character but is not in $\widehat{H_1(X,\mathbb{Z})}$. Two things break. The Euler product for $L_X(s,\chi)$ no longer converges for $\operatorname{Re}(s)>\delta$ — the expansion in [[Def - Selberg L-Function|Corollary 6.4's derivation]] needs $|z|=|\chi([\gamma])|e^{-(\operatorname{Re}(s)+k)\ell_\gamma}<1$, which uses $|\chi|=1$. And there is no compact group to integrate over, so no Fourier inversion. This is the same phenomenon as the abscissa $c_\rho>\delta$ for a non-unitary $\rho$ on [[Def - Ruelle Zeta Function and its Twist]].

**Second near-miss — conjugacy classes are not homology classes.** For genus $g\geq2$ the fundamental group $\pi_1(X)\cong\Gamma$ is **non-abelian**. A free homotopy class corresponds to a conjugacy class in $\Gamma$ and retains non-abelian information — such as the order in which different handles are traversed, up to conjugation. Passing to homology discards this and gives a much coarser equivalence relation: **a fixed homology class $\beta$ has contributions from infinitely many distinct free homotopy classes.** That is precisely why $\mu^\kappa_X(\beta)$ has no direct closed form and needs the $L$-function.

---

# Used in this paper at

- [[Def - Selberg L-Function]] — $L_X(s,\chi)$ is indexed by $\chi\in\widehat{H_1(X,\mathbb{Z})}$
- [[Constr - The Mass in a Homology Class]] — $\mu^\kappa_X(\beta)$ is the Fourier coefficient
- [[Thm - Selberg L-Function Identity|Corollary 6.4]] — the twisted identity, one point of the torus at a time
- [[Thm - Fourier Expansion and Inversion by Homology Class|Theorem 6.5]] — the Fourier pair and the inversion formula, whose proof is orthogonality
- [[Thm - Distribution of the Total Homology of the Loop Soup|Proposition 6.7]] — $\mathbb{E}[\chi(\beta(\lambda))]$ is a characteristic function on the torus, and the pointwise law is its inverse transform
- [[Def - The Jacobian as a Principally Polarised Abelian Variety]] — for a closed surface the torus **is** the Jacobian, via Hodge theory

---

# Where this sits in my DAG

Two rungs, both shallow. The homology side is *Algebraic Topology* (🔵): the abelianisation of $\pi_1$ is [[Def - Hurewicz Map]] and [[Thm - Hurewicz Theorem (Statement)]] in the vault, and the computation $H_1\cong\mathbb{Z}^{2g}$ for a closed surface of genus $g$, $\mathbb{Z}^{2g+b-1}$ with $b$ ends, is standard surface topology. The rank formula is quoted.

The duality side — characters of a finitely generated abelian group, Haar measure on a compact torus, orthogonality — is elementary harmonic analysis, and reduces to *Advanced Probability / Measure-Theoretic* (🟢) for the measure theory plus the observation that a homomorphism out of $\mathbb{Z}^r$ is a choice of $r$ points of $S^1$. **Pontryagin duality in general is a theorem; here it is a computation**, because the group is free abelian of finite rank and its dual can be written down.
