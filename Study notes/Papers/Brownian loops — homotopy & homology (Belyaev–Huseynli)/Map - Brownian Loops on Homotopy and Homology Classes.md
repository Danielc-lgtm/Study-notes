---
type: paper-map
paper: "BH26"
subject: brownian-loops
title: "A Probability Measure on Homotopy & Homology Classes via Brownian Loops — Belyaev–Huseynli"
tags: [paper, map, loop-measures, self-contained]
---

> [!info] This note-set is a **self-contained** rewrite. To read the whole paper you open only this Map and the six section pages, in order — never a subpage. Every section page writes out every symbol, predicate, and imported result it uses as literal text, so you can typecheck it front-to-back without leaving it. The two reference pages at the foot ([[External Inputs and Gaps]], [[Anchors and Prerequisites]]) are optional.

# What the paper does

On a hyperbolic surface $X=\Gamma\backslash\mathbb H^2$, the **Brownian loop measure** (a natural $\sigma$-finite measure on loops) is split according to which **free-homotopy class** each loop belongs to. Each class turns out to carry an explicit finite mass; summing the masses over all non-trivial classes gives exactly $-\log Z_X(s)$ for the **Selberg zeta function**; dividing by that sum gives a canonical **probability measure on free-homotopy classes** whose moments are derivatives of $\log Z_X$. The same total mass is the regularised $\log\det\Delta_X$ (Polyakov). Grouping loops by **homology** and twisting by characters yields Selberg $L$-functions and the exact law of the total homology of the loop soup. A final section reruns everything on hyperbolic $3$-manifolds, where every step transfers **except** the zeta identity.

**Source.** `paper_source/` — Dmitry Belyaev & Farhad Huseynli, *A probability measure on homotopy & homology classes via Brownian loops* (2026).

---

# The one identity (the spine)

Everything is this identity, read in different directions:

$$\underbrace{\mu^\kappa_X\big(\mathcal C_X(\gamma^m)\big)=\frac1m\cdot\frac{e^{(1-s)L}}{e^{L}-1}}_{\substack{\text{§3: one number per class}\\ L=m\ell_\gamma,\ s=\frac12+\sqrt{\frac14+\kappa}}}\qquad\Longrightarrow\qquad\underbrace{\sum_{\gamma\in\mathcal P_X}\sum_{m\ge1}\mu^\kappa_X\big(\mathcal C_X(\gamma^m)\big)=-\log Z_X(s)}_{\text{§4: summed over all classes}}$$

The logical chain, each link tagged with the section that proves it:

1. **[§2]** The Brownian loop measure $\mu_X$ (and its subordinate versions $\mu^\phi_X$) is a well-defined $\sigma$-finite measure on unrooted unparametrised loops; a collapse lemma reduces its class masses to one integral against a measure $V_\phi$ on $(0,\infty)$.
2. **[§3]** The mass of the class of $\gamma^m$ is $\frac{\ell_\gamma}{2\sinh(L/2)}I_\phi(L)$; for killing $\kappa$ it is $\frac1m\frac{e^{(1-s)L}}{e^L-1}$ — a function of the single number $L=m\ell_\gamma$.
3. **[§4]** Summed over all non-trivial classes, this equals $-\log Z_X(s)$; the sum is finite iff $s>\delta$ (the geodesic growth rate). On a finite-area surface with $\kappa=0$ it diverges.
4. **[§5]** That divergent total, renormalised, is $\log\det\Delta_X$ (Polyakov's formula), read off the length spectrum.
5. **[§6]** Dividing the class masses by $-\log Z_X(s)$ gives a probability measure $\mathbb P_s$ on classes; grouping by homology and twisting by a character $\chi$ gives Selberg $L$-functions, and the loop soup's total homology $\beta(\lambda)$ has characteristic function $(Z_X(s)/L_X(s,\chi))^\lambda$.
6. **[§7]** On $X=\Gamma\backslash\mathbb H^3$ the class mass becomes $\frac1m|e^{mL_\gamma}-1|^{-2}$ with complex length $L_\gamma=\ell_\gamma+i\theta_\gamma$; every step of §2–§3 transfers, but this shape is **not** a Selberg Euler factor, so §4's zeta identity has no analogue — the paper's main open question.

---

# Global signature

Every symbol used across the note-set, typed. Each section page restates the ones it uses, so this table is a convenience, not a prerequisite.

| symbol | type |
|---|---|
| $X=\Gamma\backslash\mathbb H^2$ | geometrically finite hyperbolic surface; $\Gamma\subset\mathrm{PSL}(2,\mathbb R)$ discrete, torsion-free. §7: $X=\Gamma\backslash\mathbb H^3$, $\Gamma\subset\mathrm{PSL}(2,\mathbb C)$ |
| $\Delta_X$ | positive Laplacian, $\operatorname{spec}\subseteq[0,\infty)$; BM at speed $2$, generator $-\Delta_X$ |
| $\mathcal P_X$ | primitive oriented closed geodesics $\gamma$; $\ell_\gamma\in(0,\infty)$ their lengths |
| $m,\,L$ | $m\in\mathbb Z_{\ge1}$; $L:=m\ell_\gamma$ **real** in §2–§6, **complex** $=mL_\gamma$ in §7 |
| $\mathcal C_X(\gamma^m)$ | free-homotopy class of $\gamma^m$ $=$ conjugacy class $[\tau^m]$ in $\Gamma$; a measurable set of loops |
| $\mu^\phi_X$ | $\sigma$-finite loop measure on the class space $\mathcal C_X$, total mass $\infty$; class mass $\mu^\phi_X(\mathcal C_X(\gamma^m))\in(0,\infty)$ |
| $\phi$ | a Bernstein function (Laplace exponent of a subordinator); the four instances $\lambda,\lambda+\kappa,\lambda^{\alpha/2},(\lambda+\kappa)^{\alpha/2}$ |
| $V_\phi,\ I_\phi$ | weighted potential measure ($\sigma$-finite on $(0,\infty)$, not finite); heat-kernel integral $(0,\infty)\to(0,\infty)$ |
| $\kappa,\ s$ | killing $\ge-\tfrac14$; spectral parameter $=\tfrac12+\sqrt{\tfrac14+\kappa}$; $\kappa=s(s-1)$ |
| $u,\ t$ | subordination / proper-time variable; loop duration (integrated $\mathrm dt/t$) — the paper writes both, and $s$, as one letter "$s$" |
| $\delta$ | critical exponent $\in(0,1]$; geodesic growth rate; $\delta=1\iff\operatorname{area}(X)<\infty$ |
| $Z_X,\ L_X(\cdot,\chi)$ | Selberg zeta; Selberg $L$-function twisted by a unitary character $\chi$; $L_X(\cdot,1)=Z_X$ |
| $\mathbb P_s,\ \mathbb E_s$ | probability measure on classes; expectation under it |
| $H_1(X,\mathbb Z),\ \widehat{H_1}$ | first homology $\cong\mathbb Z^r$; its character torus $\cong(S^1)^r$ |
| $\mathcal L_\lambda,\ \beta(\lambda)$ | loop soup of intensity $\lambda$; its total homology |
| $\det\!{}_\zeta,\ \det_0$ | zeta-regularised determinant (closed); renormalised determinant (cusped/infinite-area) |

**Conventions & collisions.** $\Delta_X\ge0$ (geometer's sign). Three time-like variables kept distinct — spectral $s$, subordination $u$, loop duration $t$ — where the paper overloads "$s$". $L$ is real on surfaces, complex on $3$-manifolds. **Total mass** always = sum over non-trivial, non-peripheral classes.

---

# Section-level dependency table

| section | consumes | produces | page |
|---|---|---|---|
| §2 loop measure & subordination | anchors only | $\mu^\phi_X$, $V_\phi$, Lemma 2.11 (the collapse) | [[§2 The Loop Measure and Subordination]] |
| §3 mass of a class | §2 | class mass $\frac1m\frac{e^{(1-s)L}}{e^L-1}$; loop soup; masses↦length spectrum | [[§3 Mass of a Homotopy Class]] |
| §4 zeta identities & finiteness | §3 | $\sum=-\log Z_X(s)$; finite iff $s>\delta$ | [[§4 Zeta Identities and Finiteness]] |
| §5 determinants & Polyakov | §3, §4 | $\log\det\Delta_X=\text{Area}\cdot E+\log Z_X'(1)$ | [[§5 Determinants and the Polyakov Anomaly]] |
| §6 probability & homology | §3, §4 | $\mathbb P_s$; Selberg $L$; law of $\beta(\lambda)$ | [[§6 Probability on Homotopy and Homology Classes]] |
| §7 hyperbolic $3$-manifolds | §2, §3 (not §4) | mass $\frac1m|e^{mL_\gamma}-1|^{-2}$; open question | [[§7 Hyperbolic 3-Manifolds]] |

**Shortest chain to the headline** ($\sum$ mass $=-\log Z_X(s)$): §2 (Lemma 2.11) → §3 (Theorem 3.5, on faith of the Wang–Xue strip identity) → §4 (the criterion + the killing verification). Four results, one import.

---

# Reading orders

- **Cover to cover (fast, rigorous):** the six section pages in order. Each is self-contained; open folds only when you want the proof.
- **Just the main theorem:** §3 §C (skim to Theorem 3.5) → §4 in full. Two pages.
- **Probabilist:** §2 → §3 (including §3.3 loop soup) → §6. Skip §4.2, §5.
- **Spectral geometer:** §4 → §5. Take §3's class mass as given.
- **Skippable with no loss:** §3.2 (the Euclidean-QM digression — a dictionary, cited by nothing) and Remark 6.6 (the Jacobian reformulation — closed surfaces only, decorative).

---

# The honest floor

Everything the paper takes on faith is listed with exact precondition→conclusion, source, and gap-depth on **[[External Inputs and Gaps]]**. The backchain of every term down to the reader's anchor set, and the ranked list of what would close each gap, is on **[[Anchors and Prerequisites]]**. The deepest genuine gaps: the Wang–Xue strip identity (§3, underlies everything), Naud's formula and Borthwick–Judge–Perry (§5), and the Selberg trace formula / prime geodesic theorem (§4–§5).

---

# Open questions the paper leaves

1. **Dimension 3 has no zeta identity.** The class mass $\frac1m|e^{mL_\gamma}-1|^{-2}$ (complex $L_\gamma$, squared modulus) is not a Selberg Euler factor, so §7 has no total-mass identity, no probability measure, no determinant. A holonomy-twisted Selberg zeta for Kleinian groups is the natural candidate; the paper does not pursue it. **The most concrete gap.**
2. **Which functions on classes arise as loop masses?** Corollary 3.12 shows the map (metric)↦(mass function) is injective; its image is not characterised.
3. **Geodesic intersections.** The stated motivation for $\mathbb P_s$ — computing intersection probabilities of random classes — is not carried out.
4. **General Bernstein $\phi$.** Only four $\phi$ satisfy the §4 criterion; for a general one the total mass is simply not a zeta value, and nothing is said about what it is.
