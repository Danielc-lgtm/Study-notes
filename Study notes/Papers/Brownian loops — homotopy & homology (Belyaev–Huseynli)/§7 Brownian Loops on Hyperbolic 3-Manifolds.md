---
type: paper-section
paper: "BH26"
subject: brownian-loops
section: "7"
prereqs:
  - "Def - Kleinian Group and Loxodromic Complex Length"
  - "Constr - Loxodromic Standard Form and the H3 Fundamental Slab"
  - "Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds"
  - "Thm - The H3 Fundamental-Slab Heat-Kernel Identity"
  - "Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds"
tags: [paper, probability, hyperbolic-geometry, loop-measures]
---

# Notation

**Standing setting.** $X=\Gamma\backslash\mathbb{H}^3$ where $\mathbb{H}^3$ is hyperbolic $3$-space and $\Gamma\subset\mathrm{PSL}(2,\mathbb{C})$ is a torsion-free [[Def - Kleinian Group and Loxodromic Complex Length|Kleinian group]], so $X$ is a complete orientable hyperbolic $3$-manifold. Work in the upper half-space model $\mathbb{H}^3=\{(z,y) : z\in\mathbb{C},\ y>0\}$. The heat kernel $p^{\mathcal{E}}_{\mathbb{H}^3}$ is assumed to decay fast enough in its spatial variables that, with $\Gamma$ discrete, the periodisation converges absolutely.

- $L_\gamma = \ell_\gamma + i\theta_\gamma$ — the **complex length** of an oriented closed geodesic $\gamma$: $\ell_\gamma>0$ the translation length, $\theta_\gamma\in\mathbb{R}/2\pi\mathbb{Z}$ the holonomy rotation about the axis
- $L := mL_\gamma = m\ell_\gamma + im\theta_\gamma$ — the complex length of the $m$-fold iterate. **Warning:** in §3 the symbol $L$ denoted the *real* number $m\ell_\gamma$; here it is complex, and $|e^L-1|^2$ is a modulus squared
- $\tau : (z,y)\mapsto(e^{L_\gamma}z,\ e^{\ell_\gamma}y)$ — the [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab|loxodromic standard form]], with axis the vertical geodesic from $0$ to $\infty$
- $F_\tau=\{(z,y)\in\mathbb{H}^3 : 1\leq y<e^{\ell_\gamma}\}$ — the fundamental slab, a fundamental region for $\langle\tau\rangle$ acting on $\mathbb{H}^3$
- $p_{\mathbb{H}^3}(t,z,w)=\frac{1}{(4\pi t)^{3/2}}\frac{u}{\sinh u}e^{-t-u^2/4t}$ with $u=d(z,w)$ — the Brownian heat kernel on $\mathbb{H}^3$
- $\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}=y^{-3}\,\mathrm{d}A(z)\,\mathrm{d}y$, with $\mathrm{d}A$ Euclidean area measure on $\mathbb{C}$
- $\mathcal{P}_X$, $\mathcal{C}_X(\gamma^m)$, $[\tau^m]_{\mathrm{conj}}$, $C_\Gamma(\tau^m)=\langle\tau\rangle$, $V_\phi$ — as in §3, with $\mathbb{H}^3$ replacing $\mathbb{H}^2$

---

# What this section is for

The question this section answers is: **what actually tied the construction to surfaces?**

Almost nothing, is the answer. Definition 2.1 used $X$ only through four things — its heat kernel, its bridge measures, the multiplicative Haar measure $\mathrm{d}t/t$, and the Riemannian volume measure. Heat kernels exist on any complete Riemannian manifold; bridge measures are disintegrations of the path law by endpoint; the two weights are measures on $(0,\infty)$ and on the manifold. None of that is two-dimensional. The homotopy-class decomposition of §3 is likewise dimension-agnostic: it relied on the [[Constr - The Periodised Kernel|periodisation]] and on the unfolding over cosets of a cyclic centraliser, both of which are group theory.

**What was genuinely two-dimensional is conformal invariance** — and only two results used it: the Polyakov anomaly formula of §5.1.1 and the length-spectrum identity of §3.4. But §3.4 already showed that conformal invariance dies the moment a killing rate or any nonlinear subordination is introduced. So once one works with $\kappa>0$, nothing at all ties the construction to surfaces, and the extension to three dimensions is free.

Free, except for one thing. §3 discharged its spatial integral by quoting the Wang–Xue identity, Lemma 3.4, which is an identity for the $\mathbb{H}^2$ heat kernel. There is no such quotable identity on $\mathbb{H}^3$, so the paper derives one. That derivation — equations (88)–(89) — is **the one genuinely new computation of §7**, and it is short and worth reading.

The other change is geometric. In $\mathrm{PSL}(2,\mathbb{R})$ the non-parabolic non-elliptic elements are *hyperbolic*: they translate along an axis, full stop. In $\mathrm{PSL}(2,\mathbb{C})$ they are **loxodromic**: they translate along an axis *and may rotate about it*. So an oriented closed geodesic carries a complex length $L_\gamma=\ell_\gamma+i\theta_\gamma$, and the extra parameter $\theta_\gamma$ — the holonomy angle — has to show up somewhere in the answer. It shows up as a modulus squared: the 2D denominator $e^{m\ell_\gamma}-1$ becomes $|e^{mL_\gamma}-1|^2$, which reduces to $(e^{m\ell_\gamma}-1)^2$ when $\theta_\gamma=0$. Notice that even in the no-rotation case the exponent is $2$ rather than $1$; the squaring is a genuine dimensional effect, not a holonomy effect.

---

# The setup, verbatim from §3

The structural material transfers with the words changed and nothing else. Free homotopy classes of oriented closed curves on $X$ correspond to conjugacy classes in $\Gamma$; the non-trivial non-peripheral classes correspond to loxodromic conjugacy classes, and each contains a unique oriented closed geodesic representative. Since $\Gamma$ is torsion-free and discrete, anything commuting with $\tau^m$ preserves the axis of $\tau$, and the elements of $\Gamma$ preserving that axis form an infinite cyclic subgroup generated by the primitive $\tau$, so $C_\Gamma(\tau^m)=\langle\tau\rangle$ and
$$[\tau^m]_{\mathrm{conj}} = \bigsqcup_{r\in\Gamma/\langle\tau\rangle}\{r\tau^m r^{-1}\},$$
one distinct conjugate per coset. This is [[Def - Centraliser and Coset Enumeration of a Conjugacy Class]] with $\mathrm{PSL}(2,\mathbb{C})$ substituted; the argument does not notice the change.

**The fundamental region.** In the standard form $\tau$ scales the height by the real factor $e^{\ell_\gamma}$ and rotates the horizontal coordinate by $\theta_\gamma$. Because only the height is scaled, each orbit of $\langle\tau\rangle$ meets the slab $F_\tau=\{(z,y) : 1\leq y<e^{\ell_\gamma}\}$ in exactly one point — the rotation acts *within* each slab and does not affect which slab a point lies in. So $F_\tau$ is a fundamental region for $\langle\tau\rangle$, exactly as the strip was in §3. See [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab]].

---

# Results

## Theorem 7.1 — the decomposition in three dimensions

> [!abstract] Type card — Theorem 7.1 (homotopy class decomposition, 3-manifolds)
> **Given.** A torsion-free [[Def - Kleinian Group and Loxodromic Complex Length|Kleinian group]] $\Gamma\subset\mathrm{PSL}(2,\mathbb{C})$ with $X=\Gamma\backslash\mathbb{H}^3$; a $\Gamma$-invariant Dirichlet form whose kernel periodises; a primitive closed geodesic $\gamma\in\mathcal{P}_X$ with loxodromic representative $\tau$ in [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab|standard form]]; a winding number $m\geq1$.
>
> **Produces.** The identity
> $$\mu^{\mathcal{E}}_X\big(\mathcal{C}_X(\gamma^m)\big) = \int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau}p^{\mathcal{E}}_{\mathbb{H}^3}(t,w,\tau^m w)\,\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}(w).$$
>
> **Lets you.** Transport the entire §3 decomposition to three dimensions with no new idea — everything downstream in §7 is a computation of the right-hand side.

**Strategy.** Identical in structure to [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]]: unfold the conjugacy-class sum over cosets of $\langle\tau\rangle$, then replace the reassembled fundamental region by the slab, using the loxodromic standard form (82) in place of the hyperbolic one (9).

Full statement: [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds]].

## The $\mathbb{H}^3$ slab identity — the new computation

> [!abstract] Type card — equations (88)–(89)
> **Given.** The explicit Brownian heat kernel $p_{\mathbb{H}^3}(t,z,w)=(4\pi t)^{-3/2}\frac{u}{\sinh u}e^{-t-u^2/4t}$ with $u=d(z,w)$; $\tau$ in loxodromic standard form; $t>0$, $m\geq1$; $L=mL_\gamma$.
>
> **Produces.** The closed form, a positive real number:
> $$\int_{F_\tau}p_{\mathbb{H}^3}(t,w,\tau^m w)\,\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}(w) = \frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{|e^L-1|^2}\cdot\frac{2te^{-t}}{(4\pi t)^{3/2}}e^{-(m\ell_\gamma)^2/4t} = \frac{\ell_\gamma}{2\big(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma)\big)}\cdot\frac{e^{-t-(m\ell_\gamma)^2/4t}}{\sqrt{4\pi t}}.$$
>
> **Lets you.** Play the role Lemma 3.4 plays in §3. This is what §7 has to supply itself, because Wang–Xue's identity is two-dimensional.

**Strategy.** Compute $\cosh u$ for $u=d(w,\tau^m w)$ in the upper half-space model; use polar coordinates in $z$ so that the angular integral contributes $2\pi$; then change variables from the radius $r$ to $u$, at which point $\sinh u\,\mathrm{d}u$ produced by the substitution **cancels the $1/\sinh u$ in the kernel** — that cancellation is the whole trick — leaving an elementary Gaussian integral in $u$ over $[m\ell_\gamma,\infty)$.

Full derivation: [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity]]. The factorisation to notice is the same one as in §3: a purely geometric prefactor, here $\ell_\gamma/2(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma))$, multiplied by a purely analytic factor in $(t,m\ell_\gamma)$. The holonomy angle $\theta_\gamma$ sits **only in the geometric prefactor** and never touches the analytic factor — which is why the subordination machinery goes through unchanged.

## Theorem 7.2 — the mass in three dimensions

> [!abstract] Type card — Theorem 7.2 (mass of the subordinate loop measure, 3-manifolds)
> **Given.** Any of the paper's Bernstein functions $\phi$; a primitive closed geodesic $\gamma\in\mathcal{P}_X$ with complex length $L_\gamma=\ell_\gamma+i\theta_\gamma$; $m\geq1$; write $L=mL_\gamma$.
>
> **Produces.** The closed form
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{|e^L-1|^2}\int_{(0,\infty)}\frac{2se^{-s}}{(4\pi s)^{3/2}}e^{-(m\ell_\gamma)^2/4s}\,V_\phi(\mathrm{d}s).$$
>
> **Lets you.** Specialise to any subordination in three dimensions exactly as in §3 — the choice of process still enters only through $V_\phi$.

**Strategy.** The §3.5 strategy verbatim: evaluate the spatial integral by the slab identity (88), then collapse the $\mathrm{d}t/t$ integral into $V_\phi$ by [[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11]], applied with $h(s)=\frac{2se^{-s}}{(4\pi s)^{3/2}}e^{-(m\ell_\gamma)^2/4s}$.

Full proof: [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]].

## Corollary 7.3 — the Brownian case

> [!abstract] Type card — Corollary 7.3 (Brownian mass in a class, 3-manifolds)
> **Given.** $X=\Gamma\backslash\mathbb{H}^3$ geometrically finite; pure Brownian motion, so $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$; $\gamma\in\mathcal{P}_X$ and $m\geq1$.
>
> **Produces.** The mass
> $$\mu_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac1m\cdot\frac{1}{\big|e^{mL_\gamma}-1\big|^2},\qquad mL_\gamma=m\ell_\gamma+im\theta_\gamma,$$
> with the two equivalent forms
> $$\mu_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac{e^{-m\ell_\gamma}}{2m\big(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma)\big)} = \frac1m\Big[\big(e^{m\ell_\gamma}-1\big)^2+4e^{m\ell_\gamma}\sin^2\tfrac{m\theta_\gamma}{2}\Big]^{-1}.$$
> When $\theta_\gamma=0$ the holonomy term drops and the denominator is $(e^{m\ell_\gamma}-1)^2$.
>
> **Lets you.** See the two-dimensional formula $\frac1m\frac{1}{e^L-1}$ as a specialisation: three dimensions square the denominator, and holonomy enters through a modulus.

**Strategy.** Substitute $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$ into Theorem 7.2 and apply the same integral identity $\int_0^\infty s^{-3/2}e^{-as-b/s}\,\mathrm{d}s=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$ that discharged every case in §3.1, now with $a=1$ and $b=(m\ell_\gamma)^2/4$.

> [!note]- Calculation (skippable)
> With $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$,
> $$\mu_X(\mathcal{C}_X(\gamma^m)) = \frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{|e^L-1|^2}\cdot\frac{2}{(4\pi)^{3/2}}\int_0^\infty s^{-3/2}e^{-s-(m\ell_\gamma)^2/4s}\,\mathrm{d}s.$$
> The identity with $a=1$, $b=(m\ell_\gamma)^2/4$ gives $\sqrt{\pi/b}\,e^{-2\sqrt{ab}}=\sqrt\pi\cdot\frac{2}{m\ell_\gamma}e^{-m\ell_\gamma}$. Cancelling $e^{m\ell_\gamma}$ against $e^{-m\ell_\gamma}$ and $\ell_\gamma$ against $m\ell_\gamma$ leaves $\frac1m\frac{1}{|e^{mL_\gamma}-1|^2}$. The equivalent forms follow from $|e^{a+ib}-1|^2=2e^a(\cosh a-\cos b)$ and, using $1-\cos(m\theta_\gamma)=2\sin^2(m\theta_\gamma/2)$, from $|e^{mL_\gamma}-1|^2=(e^{m\ell_\gamma}-1)^2+4e^{m\ell_\gamma}\sin^2(m\theta_\gamma/2)$.

Full statement: [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds]].

---

# What to carry forward

**That §7 costs one computation.** Everything except the slab identity is §3 with $\mathbb{H}^2$ replaced by $\mathbb{H}^3$. If you have understood the coset unfolding once, you have understood it twice.

**The complex length.** $L_\gamma=\ell_\gamma+i\theta_\gamma$; the holonomy angle sits only in the geometric prefactor; and the mass formula $\frac1m|e^{mL_\gamma}-1|^{-2}$ specialises to $(e^{m\ell_\gamma}-1)^{-2}$ when there is no rotation. **The exponent $2$ is dimensional and survives $\theta_\gamma=0$** — a fact easy to misremember as "holonomy squares the denominator".

**Why §4–§6 do not follow.** [[Thm - Selberg Zeta Criterion|Lemma 4.2]] demands a mass of the form $\frac{C}{m}\frac{e^{(1-s)L}}{e^L-1}$, and $\frac1m|e^{mL_\gamma}-1|^{-2}$ is not of that form. So there is no Selberg zeta identity here as stated, no finiteness criterion, and no probability measure on homotopy classes of a hyperbolic $3$-manifold. The natural next object is a Selberg zeta function for $\Gamma\subset\mathrm{PSL}(2,\mathbb{C})$ built from complex lengths, and the natural next question is which functional equation replaces (33). This is recorded as the paper's most concrete unfinished business on [[Map - Brownian Loops on Homotopy and Homology Classes]].

Back to the overview: [[Map - Brownian Loops on Homotopy and Homology Classes]].
