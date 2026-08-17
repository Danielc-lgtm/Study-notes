---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Free Homotopy Class and Conjugacy Class Correspondence"
tags: [paper, hyperbolic-geometry]
---

# Signature

| symbol | type |
|---|---|
| $(X,g)$ | a hyperbolic surface with its metric |
| $\ell_g$ | $\{\text{loops in }X\}\to[0,\infty)$; length in the metric $g$ |
| $\mathcal{C}_X(\gamma^m)$ | a non-trivial free homotopy class; $\gamma\in\mathcal{P}_X$, $m\geq1$ |
| $\mathrm{MLS}$ | $\{\text{non-trivial free homotopy classes}\}\to(0,\infty)$ — a **function**, not a multiset |
| $\ell_\gamma$ | length of the primitive closed geodesic $\gamma$ |

---

# Definition

> **Definition 3.10 (marked length spectrum).**
> $$\mathrm{MLS}:\ \mathcal{C}_X(\gamma^m)\ \longmapsto\ \inf_{\eta\in\mathcal{C}_X(\gamma^m)}\ell_g(\eta).$$
> On a hyperbolic surface the infimum is **attained**, by the unique closed geodesic in the class, so
> $$\mathrm{MLS}\big(\mathcal{C}_X(\gamma^m)\big)=m\ell_\gamma .$$

> **(F1) Determined by its primitive values.** Since $\mathrm{MLS}(\mathcal{C}_X(\gamma^m))=m\ell_\gamma$, the function $\mathrm{MLS}$ on $\mathcal{P}_X\times\mathbb{Z}_{\geq1}$ is determined by its restriction to $\mathcal{P}_X$.
>
> **(F2) Marked vs unmarked.** The **length spectrum** is the multiset $\{\mathrm{MLS}(\mathcal{C}):\mathcal{C}\}$ — it forgets the domain. **$\mathrm{MLS}$ is strictly stronger:** Vignéras constructed non-isometric hyperbolic surfaces whose length spectra agree as multisets. So the values alone do not determine $X$; the *assignment* value-to-class does.
>
> **(F3) The domain is metric-independent.** Free homotopy classes are topological, so two metrics $g_1,g_2$ on the same $X$ give two functions $\mathrm{MLS}_{g_1},\mathrm{MLS}_{g_2}$ on the **same** index set. This is what "with the identity marking" means, and it is what makes [[Thm - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]]'s hypothesis strong enough.

---

# Type card

> [!abstract] Type card — marked length spectrum
> **Given.** **(H1)** $(X,g)$ a hyperbolic surface. **(H2)** the standing convention: classes non-trivial, non-peripheral.
>
> **Produces.** A function $\mathrm{MLS}:\mathcal{P}_X\times\mathbb{Z}_{\geq1}\to(0,\infty)$, $(\gamma,m)\mapsto m\ell_\gamma$. **A function, not a multiset** — that distinction is the whole content.
>
> **Lets you.** State [[Thm - Loop Masses Determine the Marked Length Spectrum|Proposition 3.11]] (loop masses determine $\mathrm{MLS}$) and, via [[Ext - Otal–Croke Marked Length Spectrum Rigidity|(OC)]], upgrade it to a statement about the hyperbolic structure itself.

---

# Depends on

- [[Def - Free Homotopy Class and Conjugacy Class Correspondence]] — the domain, and (F3)
- [[Def - Primitive Hyperbolic Element and Translation Length]] — $\ell_\gamma$
- 🟢 existence and uniqueness of the closed geodesic in a non-trivial non-peripheral class — quoted (Buser, Katok)

---

# Checks

**Instance.** $X=\langle\tau\rangle\backslash\mathbb{H}^2$, $\tau:z\mapsto e^{\ell}z$. Classes indexed by $m\in\mathbb{Z}\setminus\{0\}$; $\mathrm{MLS}$ sends the class of winding number $m$ to $\lvert m\rvert\ell$. The multiset $\{\lvert m\rvert\ell:m\neq0\}$ has each value twice (once per orientation); $\mathrm{MLS}$ records which orientation and winding number produced each.

**Non-instance (fails F2 — the multiset is strictly weaker).** Vignéras's isospectral non-isometric pairs agree on every *value* of $\mathrm{MLS}$, with multiplicity, and are different surfaces. **Consequence:** [[Thm - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]]'s hypothesis is "$\mu^\kappa_{X,g_1}(\mathcal{C})=\mu^\kappa_{X,g_2}(\mathcal{C})$ **for every class $\mathcal{C}$**" — quantified over classes. Weakening it to equality of value multisets makes the corollary false.

**Non-instance (fails attainment).** A peripheral class — a loop around a cusp: $\inf_\eta\ell_g(\eta)=0$, **not attained**, no closed geodesic. $\mathrm{MLS}$ is either $0$ or undefined there; either way the class is excluded by the standing convention. See [[Def - Geometrically Finite Surfaces, Cusps and Funnels]].

---

# Used at

- [[Thm - Loop Masses Determine the Marked Length Spectrum]] — the target of the inversion
- [[Thm - Loop Masses Determine the Hyperbolic Surface]] — $\mathrm{MLS}$ with the identity marking, plus (OC)
- [[Ext - Otal–Croke Marked Length Spectrum Rigidity]] — its precondition is equality of $\mathrm{MLS}$
- [[§3 Decomposition over Homotopy Classes]] §3.4.1

---

# Commentary

> [!note]- Commentary (skippable)
> The word *marked* is carrying the whole statement, and (F2) is why: Burns and Katok conjectured that a negatively curved metric on a closed manifold is determined up to isometry by its **marked** length spectrum, and in two dimensions Otal and Croke proved it. The unmarked version is known to be false, by Vignéras.
>
> In this paper $\mathrm{MLS}$ is the intermediate object through which a probabilistic statement (masses) becomes a geometric one (isometry). §3.4.1 inverts the masses to get $\mathrm{MLS}$; (OC) takes $\mathrm{MLS}$ to the metric.
