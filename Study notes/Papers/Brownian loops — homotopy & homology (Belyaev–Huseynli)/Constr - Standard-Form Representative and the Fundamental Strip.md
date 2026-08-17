---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Primitive Hyperbolic Element and Translation Length"
  - "Def - Fundamental Region"
  - "Def - Centraliser and Coset Enumeration of a Conjugacy Class"
tags: [paper, hyperbolic-geometry]
---

# Signature

| symbol | type |
|---|---|
| $\gamma$ | $\in\mathcal{P}_X$; primitive oriented closed geodesic, length $\ell_\gamma>0$ |
| $\tau$ | $\in\mathrm{PSL}(2,\mathbb{R})$; the standard-form representative $\tau:z\mapsto e^{\ell_\gamma}z$ |
| $\tau^m$ | $z\mapsto e^{L}z$ with $L:=m\ell_\gamma$ |
| $F_\tau$ | $=\{z\in\mathbb{H}^2:1\leq\operatorname{Im}z<e^{\ell_\gamma}\}$; a [[Def - Fundamental Region\|fundamental region]] for $\langle\tau\rangle$; $\rho(F_\tau)=\infty$ |
| $\rho$ | $\mathrm{d}\rho=(\operatorname{Im}z)^{-2}\,\mathrm{d}x\,\mathrm{d}y$ |
| $F$ | a fundamental region for the whole of $\Gamma$ |
| $L$ | $=m\ell_\gamma\in(0,\infty)$ — **real** in §3–§6; complex in §7 |

---

# Construction

> **Construction (9) — standard form.** Fix a representative $\tau\in\Gamma$ of the primitive hyperbolic conjugacy class of $\gamma$. Conjugating **in $\mathrm{PSL}(2,\mathbb{R})$** (not merely in $\Gamma$), $\tau$ may be placed in the form
> $$\tau:\ z\longmapsto e^{\ell_\gamma}z,\tag{9}$$
> the hyperbolic isometry with $\operatorname{axis}(\tau)=i(0,\infty)$ (the imaginary half-line) and translation length $\ell_\gamma$.
>
> *Justification:* $\tau$ hyperbolic $\Rightarrow$ its lift to $\mathrm{SL}(2,\mathbb{R})$ has two real eigenvalues $e^{\pm\ell_\gamma/2}$; conjugating by the eigenvector matrix diagonalises it to $\operatorname{diag}(e^{\ell_\gamma/2},e^{-\ell_\gamma/2})$, acting as $z\mapsto e^{\ell_\gamma}z$.

> **Construction (12) — the fundamental strip.** In the form (9), $\operatorname{Im}(\tau z)=e^{\ell_\gamma}\operatorname{Im}(z)$, so $\tau$ acts on $\log\operatorname{Im}z$ by translation by $\ell_\gamma$. Set
> $$F_\tau:=\big\{z\in\mathbb{H}^2\ :\ 1\leq\operatorname{Im}z<e^{\ell_\gamma}\big\}.\tag{12}$$

**Well-definedness — $F_\tau$ satisfies [[Def - Fundamental Region|(D1),(D2)]].** The $\langle\tau\rangle$-orbit of $z$ has imaginary parts $\{e^{k\ell_\gamma}\operatorname{Im}z\}_{k\in\mathbb{Z}}$; exactly one lies in $[1,e^{\ell_\gamma})$, namely $k=-\lfloor\log\operatorname{Im}z/\ell_\gamma\rfloor$. So each orbit meets $F_\tau$ in exactly one point: (D1) holds, and (D2) holds with $\tau^kF_\tau\cap F_\tau=\emptyset$ for $k\neq0$. $\;\square$

> **(F1) $\rho(F_\tau)=\infty$.** $F_\tau$ is unbounded in the real direction — a band of height $\ell_\gamma$ in $\log\operatorname{Im}z$, infinite extent in $\operatorname{Re}z$. Not a problem: $p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,\tau^mz)$ decays as $z$ leaves the axis, since $d(z,\tau^mz)$ grows. The resulting integral is what [[Ext - Wang–Xue Strip Identity|(WX)]] evaluates.
>
> **(F2) $\langle\tau\rangle$-invariance of the integrand.** $\tau$ commutes with $\tau^m$ and $p^{\mathcal{E}}_{\mathbb{H}^2}$ is $\Gamma$-invariant, so $z\mapsto p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,\tau^mz)$ is $\langle\tau\rangle$-invariant. Hence by [[Def - Fundamental Region|(I)]] its integral over **any** fundamental region for $\langle\tau\rangle$ is the same.
>
> **(F3) Consistency of the two normalisations.** The conjugation in (9) moves $\Gamma$ to a conjugate group; harmless, since every quantity computed is conjugation-invariant. But the coset enumeration of [[Def - Centraliser and Coset Enumeration of a Conjugacy Class|(E)]] takes place inside $\Gamma$ (or its conjugate) and must be applied consistently.

---

# Type card

> [!abstract] Type card — standard form and strip
> **Given.** **(H1)** a primitive hyperbolic conjugacy class in $\Gamma$ with translation length $\ell_\gamma>0$. **(H2)** freedom to conjugate in $\mathrm{PSL}(2,\mathbb{R})$.
>
> **Produces.** $\tau:z\mapsto e^{\ell_\gamma}z$, acting by multiplication, with $\tau^mz=e^Lz$; and $F_\tau=\{1\leq\operatorname{Im}z<e^{\ell_\gamma}\}$, a fundamental region for $\langle\tau\rangle$ of infinite $\rho$-measure.
>
> **Lets you.** Turn the integral over an unmanageable fundamental region for $\Gamma$, with a conjugacy-class sum inside, into an explicit integral over a horizontal band with a single term inside — after which the hyperbolic heat kernel integrates in closed form.

---

# Depends on

- [[Def - Primitive Hyperbolic Element and Translation Length]] — the axis and $\ell_\gamma$; every hyperbolic is $\mathrm{PSL}(2,\mathbb{R})$-conjugate to a dilation
- [[Def - Fundamental Region]] — (D1),(D2) for $F_\tau$; (I) for (F2); (R) for the unfolding
- [[Def - Centraliser and Coset Enumeration of a Conjugacy Class]] — identifies $\langle\tau\rangle$ as the relevant subgroup
- 🟢 $\mathbb{H}^2$, $\mathrm{PSL}(2,\mathbb{R})$, hyperbolic area — [[Def - The Hyperbolic Space H^n]]

---

# Properties relied on later

**(P1) $\tau^mz=e^Lz$ literally.** This is why [[Ext - Wang–Xue Strip Identity|(WX)]] can be stated as an identity in one real parameter $L$ rather than as a statement about a group element.

**(P2) Any fundamental region will do.** By (F2)+(I), the strip may replace the reassembled $\bigsqcup_r r^{-1}F$ of [[Def - Fundamental Region|(R)]]. **This single step is what makes Theorem 3.2's right-hand side computable.**

**(P3) The $\mathbb{H}^3$ analogue.** $\tau:(z,y)\mapsto(e^{L_\gamma}z,e^{\ell_\gamma}y)$ and $F_\tau=\{1\leq y<e^{\ell_\gamma}\}$ — see [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab]]. The key point there: only the *height* is scaled, by the **real** factor $e^{\ell_\gamma}$, so the holonomy rotation acts within a slab and the one-point-per-orbit argument is unchanged.

---

# Consumed by

- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]] — as (H1); $F_\tau$ is the region in the conclusion
- [[Ext - Wang–Xue Strip Identity]] — stated for exactly this $\tau$ and $F_\tau$
- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] — inherits both
- [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab]] — the analogue

---

# Commentary

> [!note]- Commentary (skippable)
> Two normalisations that together turn an unmanageable integral into an explicit one. The standard form is a change of coordinates making $\tau^m$ a multiplication; the strip is the region where that multiplication is transparent.
>
> Why the pairing matters: [[Def - Centraliser and Coset Enumeration of a Conjugacy Class|(E)]] turns a $\Gamma$-sized class sum into a single term over a fundamental region for $\langle\tau\rangle$ — but the region it produces is $\bigsqcup_rr^{-1}F$, an unmanageable union. (F2)+(I) say any fundamental region gives the same answer, and $F_\tau$ is the one where the geometry is a band. **That freedom is the second half of the unfolding, and it is where all the explicitness comes from.**
