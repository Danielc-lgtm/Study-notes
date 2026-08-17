---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, hyperbolic-geometry, riemann-surfaces]
---

# Signature

| symbol | type |
|---|---|
| $X$ | complete hyperbolic surface without boundary |
| $P$ | $\subseteq X$ non-empty, closed, discrete (hence countable) |
| $X'$ | $:=X\setminus P$, a Riemann surface |
| $g$ | the ambient metric on $X$; $g\vert_{X'}$ its restriction — **not** complete on $X'$ |
| $g'$ | the complete hyperbolic metric on $X'$; $[g']=[g\vert_{X'}]$ as conformal classes |

---

# Statement

> **(UN) Uniformisation for a punctured hyperbolic surface.** *Precondition:*
> **(P1)** $X$ a complete hyperbolic surface without boundary;
> **(P2)** $P\subseteq X$ non-empty, closed, discrete;
> **(P3)** $X'=X\setminus P$ has non-abelian fundamental group (automatic once $X$ is hyperbolic and $P\neq\emptyset$).
>
> *Conclusion:* there is a **unique** complete hyperbolic metric $g'$ on $X'$ in the conformal class of $g\vert_{X'}$. It has a **cusp** at each point of $P$, and $g'\neq g\vert_{X'}$: the restricted ambient metric is not complete on $X'$.

---

# Type card

> [!abstract] Type card — (UN)
> **Given.** (P1),(P2),(P3).
>
> **Produces.** A metric $g'$ on $X'$ — existence and uniqueness — conformally equivalent to $g\vert_{X'}$, complete, of constant curvature $-1$, with a cusp at each puncture.
>
> **Lets you.** Apply [[Ext - Lawler–Werner Restriction and Conformal Invariance|(LW2)]] to swap $g\vert_{X'}$ for $g'$ inside the same conformal class, which is the second of the two moves in [[Ext - Wang–Xue Length-Spectrum Identity|(WXL)]].

---

# Status

- **Proved here:** no.
- **Source:** classical uniformisation; see Buser, or any Riemann-surfaces text.
- **DAG node that would close this:** *Riemann Surfaces* (🔵) — prereqs Complex Analysis, Topology, Algebraic Topology (basic).
- **What is safe to assume:** existence, uniqueness, conformal equivalence, and the cusp structure. Nothing else is used.
- **Scope of the dependency:** §3.4 only. Removing (UN) removes (WXL) and nothing else.

---

# Used at

- [[Ext - Wang–Xue Length-Spectrum Identity]] — (P3) there is exactly this conclusion
- [[§3 Decomposition over Homotopy Classes]] §3.4

---

# Commentary

> [!note]- Commentary (skippable)
> The clause doing the work is **conformal equivalence**: $g'$ and $g\vert_{X'}$ define the same conformal class, so (LW2) applies and the loop measure does not notice the swap. Without that, the swap would change $\mu$ and the identity would fail.
>
> The geometric content of the swap is that $g'$ has cusps where $g\vert_{X'}$ merely had punctures — so geodesics that must go around a puncture become **longer** in $g'$. That is why the two sides of (WXL) are a genuine constraint between different length spectra rather than a restatement.
