---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces"
  - "Constr - Loxodromic Standard Form and the H3 Fundamental Slab"
  - "Def - Kleinian Group and Loxodromic Complex Length"
tags: [paper, probability, hyperbolic-geometry, loop-measures]
---

# Notation

- $\Gamma\subset\mathrm{PSL}(2,\mathbb{C})$ — a torsion-free [[Def - Kleinian Group and Loxodromic Complex Length|Kleinian group]]; $X=\Gamma\backslash\mathbb{H}^3$
- $(\mathcal{E},\mathcal{F})$ — a $\Gamma$-invariant regular symmetric Dirichlet form whose kernel $p^{\mathcal{E}}_{\mathbb{H}^3}$ periodises; $\mu^{\mathcal{E}}_X$ the associated loop measure
- $\gamma\in\mathcal{P}_X$ — a primitive closed geodesic with complex length $L_\gamma=\ell_\gamma+i\theta_\gamma$; $\tau$ its [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab|standard-form representative]] (82)
- $F_\tau=\{(z,y)\in\mathbb{H}^3 : 1\leq y<e^{\ell_\gamma}\}$ — the fundamental slab (84)
- $m\geq1$ — the winding number; $\mathcal{C}_X(\gamma^m)$ the free non-peripheral homotopy class
- $\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}=y^{-3}\,\mathrm{d}A(z)\,\mathrm{d}y$

---

# Type card

> [!abstract] Type card — Theorem 7.1 (homotopy class decomposition, 3-manifolds)
> **Given.** A torsion-free [[Def - Kleinian Group and Loxodromic Complex Length|Kleinian group]] $\Gamma\subset\mathrm{PSL}(2,\mathbb{C})$ with $X=\Gamma\backslash\mathbb{H}^3$; a $\Gamma$-invariant regular symmetric Dirichlet form whose kernel periodises, with decay beating the orbit growth; a primitive closed geodesic $\gamma\in\mathcal{P}_X$ with loxodromic representative $\tau$ in [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab|standard form]] (82); a winding number $m\geq1$.
>
> **Produces.** An identity between numbers in $[0,\infty]$: the mass of the Dirichlet-form loop measure in the free non-peripheral homotopy class $\mathcal{C}_X(\gamma^m)$ equals an explicit double integral over $(0,\infty)\times F_\tau$ of the upstairs kernel against the single group element $\tau^m$.
>
> **Lets you.** Transport the entire §3 decomposition to three dimensions with **no new idea** — everything downstream in §7 is a computation of the right-hand side.

---

# Statement

> **Theorem 7.1 (general homotopy class decomposition for hyperbolic 3-manifolds).** Let $\gamma\in\mathcal{P}_X$ be a primitive closed geodesic with loxodromic representative $\tau\in\Gamma$, normalised as in (82), and let $m\geq1$ be the winding number. The mass of the Dirichlet form loop measure in the free non-peripheral homotopy class $\mathcal{C}_X(\gamma^m)$ is
> $$\mu^{\mathcal{E}}_X\big(\mathcal{C}_X(\gamma^m)\big) = \int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau}p^{\mathcal{E}}_{\mathbb{H}^3}\big(t,w,\tau^m w\big)\,\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}(w).\tag{85}$$

---

# Why it is true

It is [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]], and the interest is in *why* it is, since that is the substance of §7's opening claim.

The two-dimensional proof used four things: the loop measure's definition as $\int_0^\infty\frac{\mathrm{d}t}{t}\int(\cdots)$; the periodisation of the kernel over $\Gamma$; the correspondence between free homotopy classes and conjugacy classes; and the coset enumeration $[\tau^m]_{\mathrm{conj}}=\bigsqcup_r\{r\tau^mr^{-1}\}$ over $\Gamma/\langle\tau\rangle$, with $C_\Gamma(\tau^m)=\langle\tau\rangle$. **Not one of those is two-dimensional.** The loop measure needs a heat kernel, bridge measures and two weights, all of which exist on any complete Riemannian manifold. The periodisation needs a $\Gamma$-invariant kernel with enough decay. The correspondence needs a universal cover with deck group $\Gamma$. And the centraliser computation needs only that a torsion-free discrete group of orientation-preserving isometries preserving a geodesic is infinite cyclic — true in $\mathrm{PSL}(2,\mathbb{C})$ for the same reason as in $\mathrm{PSL}(2,\mathbb{R})$.

So the proof transfers word for word, with $\mathbb{H}^3$ for $\mathbb{H}^2$, "loxodromic" for "hyperbolic", the standard form (82) for (9), and the slab (84) for the strip (12). The one place the extra parameter could have intervened — the choice of fundamental region — it does not, because $\tau$ scales the **height** by the real factor $e^{\ell_\gamma}$ while the rotation $\theta_\gamma$ acts within each slab. **The holonomy is invisible to the slab.**

**The mechanism in one line: the §3 unfolding is group theory plus a change of fundamental region, and neither notices the dimension — the holonomy angle acts within a slab and so does not affect which slab a point lies in.**

**What genuinely was two-dimensional**, as §7 opens by observing, is [[Constr - The Brownian Loop Measure|conformal invariance]], used in exactly two results: the Polyakov anomaly formula of §5.1.1 and the length-spectrum identity of §3.4. And §3.4 already showed that conformal invariance dies under any killing rate or nonlinear subordination. So once $\kappa>0$, nothing at all ties the construction to surfaces.

---

# Strategy

**Strategy.** Identical in structure to [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]]: unfold the conjugacy-class sum over cosets of $\langle\tau\rangle$ using $\Gamma$-invariance of the kernel, then replace the reassembled fundamental region by the slab, using the loxodromic standard form (82) in place of the hyperbolic one (9).

> [!note]- Proof (skippable)
> The paper's proof reads in full: "Identical in structure to the proof of Theorem 3.2, using the loxodromic standard form (82)."
>
> Spelled out, the two steps are:
>
> **Step 1 — isolating the conjugacy class.** The lifting picture gives the bridge decomposition $W^{t,\mathcal{E}}_{w\to w,X}=\sum_{h\in\Gamma}\pi_*W^{t,\mathcal{E}}_{\tilde w\to h\tilde w,\mathbb{H}^3}$, so restricting to loops in $\mathcal{C}_X(\gamma^m)$ restricts the periodisation to $h\in[\tau^m]_{\mathrm{conj}}$, and
> $$\mu^{\mathcal{E}}_X\big(\mathcal{C}_X(\gamma^m)\big) = \int_0^\infty\frac{\mathrm{d}t}{t}\int_X\sum_{h\in[\tau^m]_{\mathrm{conj}}}p^{\mathcal{E}}_{\mathbb{H}^3}(t,\tilde w,h\tilde w)\,\mathrm{d}\mathrm{vol}_X(w).$$
>
> **Step 2 — unfolding to the slab.** Let $F$ be a fundamental region for $\Gamma$ in $\mathbb{H}^3$, so $\int_X(\cdot)\,\mathrm{d}\mathrm{vol}_X=\int_F(\cdot)\,\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}$. Unfold the sum using the coset enumeration (83): for each $r\in\Gamma/\langle\tau\rangle$, $\Gamma$-invariance gives $p^{\mathcal{E}}_{\mathbb{H}^3}(t,w,r\tau^mr^{-1}w)=p^{\mathcal{E}}_{\mathbb{H}^3}(t,r^{-1}w,\tau^mr^{-1}w)$, and the isometric substitution $w'=r^{-1}w$ moves the integral to $r^{-1}F$. Summing over cosets, $\bigsqcup_r r^{-1}F$ is a fundamental region for $\langle\tau\rangle$. Since the integrand $w\mapsto p^{\mathcal{E}}_{\mathbb{H}^3}(t,w,\tau^mw)$ is $\langle\tau\rangle$-invariant, its integral over any fundamental region of $\langle\tau\rangle$ is the same, so replace the union by the slab $F_\tau$ of (84). This gives (85). $\;\square$

---

# What this assumes, and where to climb

**The standard form, the slab, and the coset enumeration** — [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab]]. Note that the centraliser argument there is *the same argument* as in two dimensions, and [[Def - Centraliser and Coset Enumeration of a Conjugacy Class]] covers both.

**The periodisation with $\Gamma$-invariance** — the three-dimensional version of [[Constr - The Periodised Kernel]]. Two jobs, as in §3: the downstairs kernel is a $\Gamma$-indexed sum, and $\Gamma$-invariance is what moves a coset representative onto the integration region in Step 2. The paper assumes explicitly that $p^{\mathcal{E}}_{\mathbb{H}^3}$ decays fast enough in its spatial variables that, with $\Gamma$ discrete, the periodisation converges absolutely.

**The free-homotopy/conjugacy correspondence in three dimensions** — [[Def - Kleinian Group and Loxodromic Complex Length]]. Non-trivial non-peripheral classes correspond to loxodromic conjugacy classes, each containing a unique closed geodesic.

**Torsion-freeness**, for the centraliser computation and for the quotient to be a manifold.

**The loop measure at Dirichlet-form generality** — [[Constr - The Dirichlet-Form Loop Measure]]. The theorem is stated at exactly the level of §3.2, so it covers jump processes too, read through [[Constr - Loop Mass in a Homotopy Class for Jump Processes|Remark 3.1]].

**Not assumed: any finiteness, any hyperbolic-surface-specific geometry, and no conformal invariance.**

---

# What consumes this

- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds|Theorem 7.2]] — starts from (85) with $p^{\mathcal{E}}_{\mathbb{H}^3}=p^\phi_{\mathbb{H}^3}$, discharges the spatial integral by the slab identity and the time integral by Lemma 2.11
- [[§7 Brownian Loops on Hyperbolic 3-Manifolds]]

---

# Reading it against the rest of the paper

The theorem's content is negative and structural: **it shows how little of §3 was about surfaces.** Reading it alongside §7's opening paragraph is the efficient way to see what the paper's framework actually requires — a heat kernel, bridge measures, the weights $\mathrm{d}t/t$ and $\mathrm{d}\mathrm{vol}_g$, a universal cover with a discrete torsion-free deck group, and enough kernel decay. That list has no dimension in it.

What §7 must supply itself is the *computation*, since §3 discharged its spatial integral by quoting Wang–Xue's $\mathbb{H}^2$ identity and no such citation exists for $\mathbb{H}^3$. That derivation, [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity|equations (88)–(89)]], is the one genuinely new piece of work in the section — which is why §7 reads as short despite covering the same ground as §3.

And what §7 does **not** supply is §4–§6: no Selberg-zeta identity, no finiteness criterion, no probability measure. The obstruction is visible in [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds|Corollary 7.3]]'s answer, which is not of the shape [[Thm - Selberg Zeta Criterion|Lemma 4.2]] demands. See [[Map - Brownian Loops on Homotopy and Homology Classes]] for that as the paper's most concrete open question.
