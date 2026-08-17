---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds"
  - "Ext - Gaussian Reciprocal Integral Identity"
tags: [paper, loop-measures, kleinian-groups]
---

# Signature

| symbol | type |
|---|---|
| $X$ | $=\Gamma\backslash\mathbb{H}^3$ geometrically finite hyperbolic $3$-manifold |
| $\gamma,m$ | $\gamma\in\mathcal{P}_X$ primitive, $m\geq1$ |
| $L_\gamma$ | $=\ell_\gamma+i\theta_\gamma$; $mL_\gamma=m\ell_\gamma+im\theta_\gamma$ |
| $\mu_X$ | the **Brownian** loop measure, $\phi(\lambda)=\lambda$, $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$ |

---

# Type card

> [!abstract] Type card — Corollary 7.3
> **Given.** **(H1)** $X=\Gamma\backslash\mathbb{H}^3$ geometrically finite. **(H2)** $\gamma\in\mathcal{P}_X$, $m\geq1$. **(H3)** $\phi(\lambda)=\lambda$, so $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$.
>
> **Produces.**
> $$\boxed{\ \mu_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac1m\cdot\frac{1}{\big\lvert e^{mL_\gamma}-1\big\rvert^{2}}\ }\tag{91}$$
> with the equivalent forms
> $$=\frac{e^{-m\ell_\gamma}}{2m\big(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma)\big)}=\frac1m\Big[\big(e^{m\ell_\gamma}-1\big)^{2}+4e^{m\ell_\gamma}\sin^{2}\tfrac{m\theta_\gamma}{2}\Big]^{-1}.\tag{92}$$
> When $\theta_\gamma=0$ the denominator becomes $\big(e^{m\ell_\gamma}-1\big)^2$.
>
> **Lets you.** Read the entire $3$-dimensional theory off one formula — and see immediately why the §4 zeta machinery does **not** transfer.

---

# Statement

> **Corollary 7.3.** Assume (H1)–(H3). Then (91) holds, with the equivalent forms (92).

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds\|(90)]] | $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$ (Example 2.10) | $\frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{\lvert e^{L}-1\rvert^2}\cdot\frac{2}{(4\pi)^{3/2}}\int_0^\infty s^{-3/2}e^{-s-(m\ell_\gamma)^2/4s}\,\mathrm{d}s$ |
| [[Ext - Gaussian Reciprocal Integral Identity\|(GI)]] at $a=1$, $b=(m\ell_\gamma)^2/4$ | that integral | $\sqrt{\pi/b}\,e^{-2\sqrt{ab}}=\dfrac{2\sqrt\pi}{m\ell_\gamma}e^{-m\ell_\gamma}$ |
| cancellation | $\frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{\lvert e^{L}-1\rvert^2}\cdot\frac{2}{(4\pi)^{3/2}}\cdot\frac{2\sqrt\pi}{m\ell_\gamma}e^{-m\ell_\gamma}$ | $\frac{1}{m\lvert e^{L}-1\rvert^2}$, i.e. (91) |
| $\lvert e^{a+ib}-1\rvert^2=2e^{a}(\cosh a-\cos b)$ | (91) | the first form of (92) |
| $1-\cos(m\theta_\gamma)=2\sin^2(m\theta_\gamma/2)$ | the same | the second form of (92) |

---

# Proof

**Strategy.** One application of (GI), with $a=1$ (the $\mathbb{H}^3$ spectral bottom) instead of $a=\tfrac14+\kappa$; everything then cancels.

> [!note]- Proof (skippable)
> For pure Brownian motion $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$, so (90) becomes
> $$\mu_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{\lvert e^{L}-1\rvert^2}\cdot\frac{2}{(4\pi)^{3/2}}\int_0^\infty s^{-3/2}e^{-s-(m\ell_\gamma)^2/4s}\,\mathrm{d}s.$$
> By (GI), $\int_0^\infty s^{-3/2}e^{-as-b/s}\,\mathrm{d}s=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$ with $a=1$, $b=(m\ell_\gamma)^2/4$, which equals $\frac{2\sqrt\pi}{m\ell_\gamma}e^{-m\ell_\gamma}$. Substituting and cancelling — $\frac{2\pi\cdot2}{(4\pi)^{3/2}}\cdot2\sqrt\pi=1$, $e^{m\ell_\gamma}e^{-m\ell_\gamma}=1$, $\ell_\gamma/(m\ell_\gamma)=1/m$ — gives (91).
>
> The equivalent forms follow from $\lvert e^{mL_\gamma}-1\rvert^2=2e^{m\ell_\gamma}\big(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma)\big)$ and, using $1-\cos(m\theta_\gamma)=2\sin^2(m\theta_\gamma/2)$, from the expansion $\lvert e^{mL_\gamma}-1\rvert^2=\big(e^{m\ell_\gamma}-1\big)^2+4e^{m\ell_\gamma}\sin^2\frac{m\theta_\gamma}{2}$. $\;\square$

---

# Dimension 2 versus dimension 3

| | surface ($\mathbb{H}^2$) | $3$-manifold ($\mathbb{H}^3$) |
|---|---|---|
| class invariant | $\ell_\gamma\in(0,\infty)$ | $L_\gamma=\ell_\gamma+i\theta_\gamma\in\mathbb{C}$ |
| Brownian mass | $\dfrac1m\dfrac{1}{e^{m\ell_\gamma}-1}$ | $\dfrac1m\dfrac{1}{\lvert e^{mL_\gamma}-1\rvert^{2}}$ |
| spectral bottom, $(\frac{n-1}{2})^2$ | $\tfrac14$ | $1$ |
| $(GI)$ applied at | $a=\tfrac14+\kappa$ | $a=1$ (Brownian) |
| slab identity | imported, [[Ext - Wang–Xue Strip Identity\|(WX)]] | proved here, [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity\|(88)]] |
| total mass | $-\log Z_X(s)$ | **no closed form known** |

---

# What this assumes, and where to climb

- **Theorem 7.2** — hence (88), Theorem 7.1, Lemma 2.11, and the assumed periodisation convergence.
- **(GI) at $a=1$** — [[Ext - Gaussian Reciprocal Integral Identity]]. This is the sixth and last use of that identity in the paper.
- **Not assumed:** any zeta identity. §7 stops here.

> [!warning] The Selberg zeta criterion does **not** apply
> [[Thm - Selberg Zeta Criterion|Lemma 4.2]] requires the mass to have the shape $\dfrac{C}{m}\dfrac{e^{(1-s)L}}{e^{L}-1}$ with $C,s$ independent of $L$. The $3$-dimensional mass $\dfrac1m\lvert e^{mL_\gamma}-1\rvert^{-2}$ is **not** of that shape: the denominator is a squared modulus, and $L_\gamma$ is complex. **The paper's most concrete open question is what replaces $-\log Z_X(s)$ as the total mass on a hyperbolic $3$-manifold.**

---

# Consumed by

- [[§7 Brownian Loops on Hyperbolic 3-Manifolds]] §7.2
- Nothing else. This is the last result of the paper.

---

# Commentary

> [!note]- Commentary (skippable)
> The formula is clean enough to be worth memorising: **the Brownian loop mass of a free homotopy class on a hyperbolic $3$-manifold is $\frac1m\lvert e^{mL_\gamma}-1\rvert^{-2}$.** The surface answer was $\frac1m(e^{m\ell_\gamma}-1)^{-1}$. Two changes: the length is complex, and the power is $2$ instead of $1$. The first is geometry — closed geodesics in dimension $3$ rotate as well as translate — and the second is dimension, entering through the $\mathbb{H}^3$ volume element and the $s^{-3/2}$ in (GI).
>
> The second form of (92) is the one that shows what the holonomy does: $\big(e^{m\ell_\gamma}-1\big)^2+4e^{m\ell_\gamma}\sin^2\frac{m\theta_\gamma}{2}$. The rotation adds a strictly positive term, so **holonomy always reduces the mass**, most sharply when $m\theta_\gamma\equiv\pi$. Geometrically: a loop must close up in the rotational direction as well as in the translational one, and the extra constraint costs measure. The effect is oscillatory in $m$ and vanishes exactly when $m\theta_\gamma\in2\pi\mathbb{Z}$, where the $m$-th iterate returns to the same rotational position.
>
> The open question is worth stating as the paper leaves it. In dimension $2$, summing $\frac1m\frac{e^{(1-s)L}}{e^L-1}$ over $(\gamma,m)$ gave $-\log Z_X(s)$ because that summand is exactly a Selberg Euler factor's logarithmic expansion. Here the summand $\frac1m\lvert e^{mL_\gamma}-1\rvert^{-2}$ is not, and no zeta function is known to produce it. One might hope for a $3$-dimensional Selberg-type zeta twisted by holonomy — objects of that kind exist in the Kleinian literature — but the paper does not identify one, and §7 therefore ends without a total-mass identity, a probability measure, or a determinant formula. Everything §4–§6 built rests on a coincidence of shape that dimension $3$ breaks.
