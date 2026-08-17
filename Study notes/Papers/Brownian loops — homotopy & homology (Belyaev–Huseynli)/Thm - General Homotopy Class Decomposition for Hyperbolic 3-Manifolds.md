---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - Loxodromic Standard Form and the H3 Fundamental Slab"
  - "Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces"
tags: [paper, loop-measures, kleinian-groups]
---

# Signature

| symbol | type |
|---|---|
| $X$ | $=\Gamma\backslash\mathbb{H}^3$, geometrically finite hyperbolic $3$-manifold |
| $\gamma$ | $\in\mathcal{P}_X$; $\tau\in\Gamma$ its loxodromic representative in standard form (82) |
| $m$ | $\geq1$, the winding number |
| $\mu^E_X$ | the [[Constr - The Dirichlet-Form Loop Measure\|Dirichlet-form loop measure]] on $X$ |
| $p^E_{\mathbb{H}^3}$ | the lifted kernel on $\mathbb{H}^3$ |
| $F_\tau$ | the fundamental slab $\{1\leq y<e^{\ell_\gamma}\}$ |

---

# Type card

> [!abstract] Type card — Theorem 7.1
> **Given.**
> **(H1)** $\Gamma\subset\mathrm{PSL}(2,\mathbb{C})$ discrete torsion-free; $X=\Gamma\backslash\mathbb{H}^3$.
> **(H2)** $\gamma\in\mathcal{P}_X$ with loxodromic $\tau$ in standard form (82); $m\geq1$.
> **(H3)** the periodisation of $p^E_{\mathbb{H}^3}$ converges absolutely — [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab|(P5)]], **assumed**.
>
> **Produces.**
> $$\mu^E_X\big(\mathcal{C}_X(\gamma^m)\big)=\int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau}p^E_{\mathbb{H}^3}\big(t,w,\tau^mw\big)\,\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}(w).\tag{85}$$
>
> **Lets you.** Compute a $3$-manifold class mass by a **single** integral over one fundamental slab in the universal cover — the sum over the conjugacy class having been unfolded away, exactly as in [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]].

---

# Statement

> **Theorem 7.1 (general homotopy class decomposition, dimension $3$).** Assume (H1)–(H3). Then (85) holds.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Def - Kleinian Group and Loxodromic Complex Length\|(D3)]] | non-trivial non-peripheral classes | class $\leftrightarrow$ loxodromic conjugacy class $[\tau^m]_{\mathrm{conj}}$ |
| [[Def - Kleinian Group and Loxodromic Complex Length\|(D4)]] | $C_\Gamma(\tau^m)=\langle\tau\rangle$ | $[\tau^m]_{\mathrm{conj}}=\bigsqcup_{r\in\Gamma/\langle\tau\rangle}\{r\tau^mr^{-1}\}$, eq. (83) |
| [[Constr - The Periodised Kernel]] descent (11) | the lifted kernel | $p^E_X(t,x,x)=\sum_{h\in\Gamma}p^E_{\mathbb{H}^3}(t,\tilde x,h\tilde x)$ |
| [[Def - Fundamental Region\|(U)]] unfolding | the coset decomposition | the $\Gamma$-sum over one class collapses to a $\langle\tau\rangle$-region integral |
| [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab\|(P1)]] | $F_\tau$ | a valid fundamental region for $\langle\tau\rangle$ |
| [[Constr - The Dirichlet-Form Loop Measure]] | the $\int_0^\infty\frac{\mathrm{d}t}{t}$ weight | the outer integral of (85) |

---

# Proof

**Strategy.** Identical in structure to Theorem 3.2, with the loxodromic standard form (82) in place of the hyperbolic one and the slab $F_\tau$ in place of the annular strip.

> [!note]- Proof (skippable)
> Lift the loop measure to $\mathbb{H}^3$ by the descent identity, so the diagonal kernel on $X$ is the periodisation $\sum_{h\in\Gamma}p^E_{\mathbb{H}^3}(t,\tilde x,h\tilde x)$. Restricting to the conjugacy class $[\tau^m]_{\mathrm{conj}}$ picks out the terms $h=r\tau^mr^{-1}$, one per coset $r\in\Gamma/\langle\tau\rangle$ by (83). Unfolding those cosets against a fundamental region for $\Gamma$ replaces "sum over cosets, integrate over a $\Gamma$-region" by "integrate over a $\langle\tau\rangle$-region", and by (P1) that region may be taken to be $F_\tau$. What remains is (85). $\;\square$

---

# What this assumes, and where to climb

- **The whole §3 unfolding apparatus** — [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]], [[Def - Fundamental Region|(U)]], [[Constr - The Periodised Kernel]]. **None of it uses dimension $2$.** The paper's opening remark is exactly this: §2.1's construction used $X$ only through its heat kernel, bridge measures, $\mathrm{d}t/t$ and $\mathrm{d}\mathrm{vol}_g$, all of which exist on any complete Riemannian manifold.
- **(H3) is a hypothesis, not a theorem** — the periodisation's absolute convergence is *assumed* in §7. See [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab|(P5)]].
- **Torsion-freeness** — [[Def - Kleinian Group and Loxodromic Complex Length|(D1),(D4)]]. Without it the centraliser need not be $\langle\tau\rangle$ and (83) fails.
- **Not assumed:** conformal invariance, or anything specific to $\phi$. (85) is stated for a **general** Dirichlet-form loop measure.

---

# Consumed by

- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]] — (85) with $p^E=p^\phi$
- [[§7 Brownian Loops on Hyperbolic 3-Manifolds]] §7.1

---

# Commentary

> [!note]- Commentary (skippable)
> The theorem's one-sentence proof is the section's thesis: **nothing in the homotopy-class decomposition was two-dimensional.** The heat kernel exists on any complete Riemannian manifold; bridge measures are disintegrations of the path law by endpoint; $\mathrm{d}t/t$ and $\mathrm{d}\mathrm{vol}_g$ are measures on $(0,\infty)$ and on the manifold; the descent identity and the coset unfolding are group theory.
>
> What *was* two-dimensional is named precisely in the paper: **conformal invariance**. The Polyakov anomaly formula and the Wang–Xue length-spectrum identity both rely on it, and it is what breaks in higher dimension. But — and this is the paper's point — conformal invariance already breaks in dimension $2$ as soon as one adds a killing rate or any nonlinear subordination, since $\phi(e^{-2\sigma}\Delta)\neq e^{-2\sigma}\phi(\Delta)$ unless $\phi$ is linear. So the results that survive subordination on surfaces are precisely the ones that survive the passage to $3$-manifolds. Section 7 is the systematic version of that observation.
