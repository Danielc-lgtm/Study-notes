---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Free Homotopy Class and Conjugacy Class Correspondence"
tags: [paper, hyperbolic-geometry]
---

# Notation

- $(X,g)$ — a hyperbolic surface with its metric; $\ell_g(\eta)$ the length of a loop $\eta$ measured in $g$
- $\mathcal{C}_X(\gamma^m)$ — a non-trivial free homotopy class; $\gamma\in\mathcal{P}_X$, $m\geq1$
- $\mathrm{MLS}$ — the marked length spectrum, a function on the set of non-trivial free homotopy classes
- $\ell_\gamma$ — the length of the primitive closed geodesic $\gamma$

---

# In plain language

The **length spectrum** of a hyperbolic surface is the multiset of lengths of its closed geodesics. The **marked** length spectrum is more: it is the *function* assigning to each free homotopy class the length of its geodesic representative. The marking is the record of which class realises which length.

That extra record is not decoration. Vignéras produced non-isometric hyperbolic surfaces whose geodesic lengths agree **as a set** — isospectral but not isometric. So the values of $\mathrm{MLS}$ alone do not determine $X$; the pairing of value with class is what carries the geometry. Burns and Katok conjectured that a negatively curved metric on a closed manifold is determined up to isometry by its marked length spectrum, and in two dimensions this was proved by Otal and by Croke.

Why the paper cares: [[Thm - Loop Masses Determine the Marked Length Spectrum|Proposition 3.11]] shows the loop masses determine $\mathrm{MLS}$, and [[Thm - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]] then invokes Otal–Croke to conclude that the loop masses determine the hyperbolic structure itself. So $\mathrm{MLS}$ is the intermediate object through which a probabilistic statement (masses) becomes a geometric one (isometry).

---

# The definition

> **Definition 3.10 (marked length spectrum).** The **marked length spectrum** of $(X,g)$ is the function defined on the set of non-trivial free homotopy classes of closed curves on $X$,
> $$\mathrm{MLS} : \mathcal{C}_X(\gamma^m)\longmapsto \inf_{\eta\in\mathcal{C}_X(\gamma^m)}\ell_g(\eta),$$
> assigning to each free homotopy class the infimum of the lengths of loops in the class.

On a hyperbolic surface the infimum is attained by the unique closed geodesic in the class, so
$$\mathrm{MLS}\big(\mathcal{C}_X(\gamma^m)\big) = m\ell_\gamma.$$

Recall from [[Def - Free Homotopy Class and Conjugacy Class Correspondence]] that every non-trivial non-peripheral free homotopy class is $\mathcal{C}_X(\gamma^m)$ for a unique $\gamma\in\mathcal{P}_X$ and $m\geq1$, so $\mathrm{MLS}$ is a function on $\mathcal{P}_X\times\mathbb{Z}_{\geq1}$ determined by its values on $\mathcal{P}_X$.

---

# Types and signatures

- $\ell_g : \{\text{loops in }X\}\to[0,\infty)$ — length in the metric $g$
- $\mathrm{MLS} : \{\text{non-trivial free homotopy classes}\}\to(0,\infty)$ — a function, not a multiset; the domain is the marking
- the underlying **length spectrum** — the multiset $\{\mathrm{MLS}(\mathcal{C}) : \mathcal{C}\}$, which forgets the domain and is a strictly weaker invariant
- $\mathrm{MLS}(\mathcal{C}_X(\gamma^m))=m\ell_\gamma$ — so $\mathrm{MLS}$ is determined by its restriction to primitive classes

---

# Example

The hyperbolic cylinder $\langle\tau\rangle\backslash\mathbb{H}^2$ with $\tau : z\mapsto e^\ell z$. Its non-trivial classes are indexed by $m\in\mathbb{Z}\setminus\{0\}$, and $\mathrm{MLS}$ sends the class of winding number $m$ to $|m|\ell$. The length spectrum as a multiset is $\{|m|\ell : m\neq0\}$ with each value occurring twice (once per orientation); the marked version records which orientation and which winding number produced each value.

**Near-miss non-example — the length spectrum without the marking.** Vignéras's construction gives pairs of non-isometric hyperbolic surfaces with the same length spectrum as a multiset. So two surfaces can agree on every *value* of $\mathrm{MLS}$, with multiplicity, and still be different surfaces. What differs is the assignment: which class carries which length. This is exactly why [[Thm - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]] is stated as "$\mu^\kappa_{X,g_1}(\mathcal{C}_X(\gamma^m))=\mu^\kappa_{X,g_2}(\mathcal{C}_X(\gamma^m))$ **for every class**" — the hypothesis is a statement about a function on classes, and weakening it to equality of the value multisets would make the corollary false.

**Second near-miss.** A peripheral class — a loop around a cusp — has $\inf_\eta\ell_g(\eta)=0$, **not attained**. So $\mathrm{MLS}$ takes the value $0$ there, or is simply not defined; either way the class carries no geodesic and is excluded by the standing convention. See [[Def - Geometrically Finite Surfaces, Cusps and Funnels]].

---

# Used in this paper at

- [[Thm - Loop Masses Determine the Marked Length Spectrum|Proposition 3.11]] — the loop masses determine $\mathrm{MLS}$, by explicit inversion in the Brownian case and by strict monotonicity in the killing case
- [[Thm - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]] — $\mathrm{MLS}$ with the identity marking, plus Otal–Croke, gives an isometry isotopic to the identity
- [[§3 Decomposition over Homotopy Classes]] §3.4.1 — where the marked length spectrum is introduced as what the loop masses recover

---

# Where this sits in my DAG

Reduces to [[Def - Free Homotopy Class and Conjugacy Class Correspondence]] for the domain, and to the existence of a unique closed geodesic in each non-trivial non-peripheral class for the value — the latter standard hyperbolic geometry, quoted from Buser or Katok.

Two things are quoted rather than derived and are recorded as gaps on [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes]]: **Vignéras's isospectral non-isometric surfaces** (which motivate the marking) and the **Otal–Croke theorem** (which is what makes the marking sufficient). The latter is genuinely outside the vault — it belongs to a hyperbolic-geometry / Teichmüller-theory strand with no DAG node yet — and it is used only in Corollary 3.12.
