---
type: section
paper: "BH26"
subject: brownian-loops
prereqs:
  - "§3 Decomposition over Homotopy Classes"
tags: [paper, section, kleinian-groups]
---

# Signature

| symbol | type |
|---|---|
| $\mathbb{H}^3$ | $\{(z,y):z\in\mathbb{C},y>0\}$; $\mathrm{d}\mathrm{vol}=y^{-3}\mathrm{d}A(z)\mathrm{d}y$ |
| $\Gamma$ | $\subset\mathrm{PSL}(2,\mathbb{C})$ discrete torsion-free; $X=\Gamma\backslash\mathbb{H}^3$ |
| $L_\gamma$ | $=\ell_\gamma+i\theta_\gamma$, complex length; $L:=mL_\gamma$ |
| $\tau$ | standard form $(z,y)\mapsto(e^{L_\gamma}z,e^{\ell_\gamma}y)$ |
| $F_\tau$ | $\{1\leq y<e^{\ell_\gamma}\}$, the fundamental slab |
| $p_{\mathbb{H}^3}$ | $\frac{1}{(4\pi t)^{3/2}}\frac{u}{\sinh u}e^{-t-u^2/4t}$, $u=d(z,w)$ |
| $V_\phi$ | the weighted potential measure of Definition 2.9, unchanged |

> **Convention.** $s$ denotes the **subordination time** throughout §7, as in §2. The spectral parameter of §4–§6 does not appear: §7 proves no zeta identity.

---

# What transfers and what does not

| ingredient of §2–§3 | transfers to $\mathbb{H}^3$? | why |
|---|---|---|
| heat kernel, bridge measures | **yes** | exist on any complete Riemannian manifold |
| $\mathrm{d}t/t$ and $\mathrm{d}\mathrm{vol}_g$ weights | **yes** | measures on $(0,\infty)$ and on the manifold |
| descent (11), periodised kernel | **yes** | covering-space identity, no dimension |
| coset unfolding over $C_\Gamma(\tau^m)=\langle\tau\rangle$ | **yes** | group theory; needs torsion-freeness only |
| Lemma 2.11 collapse into $V_\phi$ | **yes** | a statement about $(0,\infty)$ |
| the strip/slab identity | **rederived** | $\mathbb{H}^3$ kernel is elementary; §3 had to import (WX) |
| **conformal invariance** | **no** | and it already fails on surfaces under killing or nonlinear $\phi$ |
| Polyakov anomaly, (WX) length-spectrum identity | **no** | both rest on conformal invariance |
| Selberg zeta identity, §4–§6 | **no** | the mass is not of the shape Lemma 4.2 requires |

> [!warning] Conformal invariance was the only two-dimensional ingredient
> $\Delta_{X,e^{2\sigma}g}=e^{-2\sigma}\Delta_{X,g}$ in dimension $2$, but $\phi(e^{-2\sigma}\Delta)\neq e^{-2\sigma}\phi(\Delta)$ unless $\phi(\lambda)=c\lambda$. **So conformal invariance is already lost on surfaces the moment a killing rate or any nonlinear subordination is introduced** — the results that survive subordination in §3 are exactly the ones that survive the change of dimension here.

---

# Exports

> **(E1) Complex length.** Non-parabolic non-elliptic elements are **loxodromic**: they translate by $\ell_\gamma$ and rotate by $\theta_\gamma$ about an axis, so an oriented closed geodesic carries $L_\gamma=\ell_\gamma+i\theta_\gamma\in\mathbb{C}$. Non-trivial non-peripheral classes $\leftrightarrow$ loxodromic conjugacy classes, each with a unique geodesic representative. *([[Def - Kleinian Group and Loxodromic Complex Length]].)*
>
> **(E2) Standard form and slab.** $\tau:(z,y)\mapsto(e^{L_\gamma}z,e^{\ell_\gamma}y)$, and $F_\tau=\{1\leq y<e^{\ell_\gamma}\}$ is a fundamental region for $\langle\tau\rangle$ — the height scales **really**, so the rotation acts within slabs. *([[Constr - Loxodromic Standard Form and the H3 Fundamental Slab|(82),(84)]].)*
>
> **(E3) Decomposition.** $\mu^E_X(\mathcal{C}_X(\gamma^m))=\int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau}p^E_{\mathbb{H}^3}(t,w,\tau^mw)\,\mathrm{d}\mathrm{vol}$. *([[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds|Thm 7.1]], eq. (85).)*
>
> **(E4) Slab identity.** $\displaystyle\int_{F_\tau}p_{\mathbb{H}^3}(t,w,\tau^mw)\,\mathrm{d}\mathrm{vol}=\frac{\ell_\gamma}{2(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma))}\cdot\frac{e^{-t-(m\ell_\gamma)^2/4t}}{\sqrt{4\pi t}}$. *([[Thm - The H3 Fundamental-Slab Heat-Kernel Identity|(88),(89)]] — **derived here**, not imported.)*
>
> **(E5) Subordinate mass.** $\mu^\phi_X(\mathcal{C}_X(\gamma^m))=\dfrac{2\pi e^{m\ell_\gamma}\ell_\gamma}{\lvert e^{L}-1\rvert^2}\displaystyle\int_{(0,\infty)}\frac{2se^{-s}}{(4\pi s)^{3/2}}e^{-(m\ell_\gamma)^2/4s}\,V_\phi(\mathrm{d}s)$. *([[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds|Thm 7.2]], eq. (90).)*
>
> **(E6) Brownian mass.** $\mu_X(\mathcal{C}_X(\gamma^m))=\dfrac1m\dfrac{1}{\lvert e^{mL_\gamma}-1\rvert^{2}}=\dfrac1m\Big[(e^{m\ell_\gamma}-1)^2+4e^{m\ell_\gamma}\sin^2\tfrac{m\theta_\gamma}{2}\Big]^{-1}$. *([[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds|Cor 7.3]], eqs. (91),(92).)*
>
> **(E7) Standing assumption.** $p^E_{\mathbb{H}^3}$ is **assumed** to decay fast enough that the periodisation converges absolutely. Not proved.

---

# Imported results

| import | used for | gap? |
|---|---|---|
| [[Ext - Explicit Heat Kernel on Hyperbolic 3-Space\|(HK3)]] | (E4) | no — elementary, inside *Analysis of PDEs* |
| [[Ext - Gaussian Reciprocal Integral Identity\|(GI)]] at $a=1$ | (E6) | no |
| [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms\|(C5)]] | (E5) | no |

Everything else in §7 is proved from §2–§3 material.

---

# Subpages

- [[Def - Kleinian Group and Loxodromic Complex Length]] — (E1)
- [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab]] — (E2), and the displacement computation
- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds]] — (E3), Theorem 7.1
- [[Ext - Explicit Heat Kernel on Hyperbolic 3-Space]] — the one substantive import
- [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity]] — (E4)
- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]] — (E5), Theorem 7.2
- [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds]] — (E6), Corollary 7.3

---

# Open question

> [!warning] What replaces the Selberg zeta identity in dimension 3?
> [[Thm - Selberg Zeta Criterion|Lemma 4.2]] requires the shape $\dfrac{C}{m}\dfrac{e^{(1-s)L}}{e^{L}-1}$ with $C,s$ independent of $L$. The $3$-dimensional mass $\dfrac1m\lvert e^{mL_\gamma}-1\rvert^{-2}$ has a **squared modulus** in the denominator and a **complex** $L_\gamma$; it is not of that shape, and no zeta function is identified in the paper whose logarithmic expansion produces it.
>
> Consequently §7 has **no** total-mass identity, **no** probability measure on classes, and **no** determinant formula. A holonomy-twisted Selberg-type zeta for Kleinian groups is the natural candidate, and the paper does not pursue it. This is the most concrete open problem the paper leaves.

---

# Commentary

> [!note]- Commentary (skippable)
> §7 is the paper's structural audit, and it is short because the audit passes. The construction of §2 used the surface only through objects that exist on any complete Riemannian manifold, and the decomposition of §3 used only the covering-space descent and a coset unfolding over a cyclic centraliser. Neither is two-dimensional. Theorem 7.1's proof is one sentence for that reason.
>
> The single new computation is the slab identity, and the reason it can be done at all is a parity accident: the hyperbolic heat kernel is elementary in odd dimensions and not in even ones. So §3 had to import Wang–Xue for the $\mathbb{H}^2$ strip identity while §7 derives its $\mathbb{H}^3$ counterpart in half a page — the harder-sounding setting is the easier computation.
>
> What the section really isolates is that **conformal invariance, not dimension, is the load-bearing hypothesis** of §4–§6. And conformal invariance is already lost on surfaces as soon as one kills or subordinates nonlinearly, since $\phi$ does not commute with the conformal rescaling of the Laplacian. The reader who has followed §3's careful separation of the "restriction and conformal invariance" results from the rest will find §7 predictable — which is the point.
>
> The formula (E6) is a satisfying place to stop, and the open question is a real one. Everything that made §4–§6 possible was the coincidence that the surface mass formula is exactly a Selberg Euler factor's logarithmic expansion. In dimension $3$ the mass has a different shape, and the arithmetic half of the paper has no analogue. Whether a holonomy-twisted zeta closes that gap is unanswered here.
