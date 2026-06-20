---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Simplicial Homotopy Group"
  - "Def - Kan Complex and the Nerve"
  - "Def - Kan Fibration and Anodyne Extension"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $X$ be a [[Def - Simplicial Set|simplicial set]] with basepoint $x \in X_0$. Recall the relation on spheroids (simplices with totally degenerate boundary): $\sigma \sim \tau$ if there is a simplex $H$ exhibiting a homotopy from $\sigma$ to $\tau$ rel basepoint. Prove that:

(a) the relation $\sim$ is always **reflexive**;
(b) when $X$ is a [[Def - Kan Complex and the Nerve|Kan complex]], $\sim$ is **transitive** (and symmetric), hence an equivalence relation, so $\pi_n(X, x)$ is well-defined;
(c) for the non-Kan simplicial set $\Delta^1$, the relation on vertices ($n = 0$ spheroids) fails to be symmetric, so the naive $\pi_0(\Delta^1)$ is not a set of equivalence classes.

Identify exactly where the [[Def - Kan Complex and the Nerve|Kan condition]] is used in (b).

**Recall:**

![[Def - Simplicial Homotopy Group#The Definition]]

A [[Def - Kan Complex and the Nerve|Kan complex]] is a [[Def - Simplicial Set|simplicial set]] in which every horn $\Lambda^n_k \to X$ fills to a simplex $\Delta^n \to X$.

---

# Convergent Strategy

**Problem class:** This is a *well-definedness* problem of the homotopy-group world (topic-page Problem-Solving Strategy): we must verify that the candidate quotient defining $\pi_n$ is legitimate, which reduces to checking an equivalence relation. The routine is to construct, for each property of the relation, a specific simplex (a degeneracy for reflexivity, a horn filler for transitivity) and read the property off its faces.

**Assumption pattern:** The recognisable feature in (a) is "reflexivity from a degeneracy" — degeneracies provide tautological homotopies for free, with no Kan condition. The feature in (b) is "two homotopies sharing a face assemble into a horn" — whenever you have several simplices agreeing on overlapping faces, they glue into a horn, and the Kan condition fills it. The feature in (c) is "directedness without inverses": $\Delta^1$ has an edge one way but not the other.

**Theorem routing:** Reflexivity routes through the degeneracy operator $s_n$. Transitivity routes through: two homotopies $H_1 : \sigma \sim \tau$, $H_2 : \tau \sim \rho$ $\to$ assemble with degenerate fillers into a horn $\Lambda^{n+2}_j$ $\to$ fill by the [[Def - Kan Complex and the Nerve|Kan condition]] $\to$ extract the missing face as a homotopy $\sigma \sim \rho$. The failure (c) routes through the explicit simplices of $\Delta^1$.

**Key decision point:** The non-obvious step in (b) is the *choice of which horn* to build from $H_1$ and $H_2$ — which face of the prospective $(n+2)$-simplex to leave empty so that the filler's missing face is exactly the desired homotopy. Picking the wrong index gives a filler whose missing face is not a homotopy rel basepoint. The standard choice uses the inner index that makes $H_1, H_2$ adjacent.

---

# Legal Operations Used

1. **Operation 1 from the topic page (fill a horn).** The entire transitivity argument is one horn-fill: assemble $H_1, H_2$ and degeneracies into a horn, fill it, read off the new homotopy.

2. **The degeneracy operators (from [[Def - Simplicial Set]]).** Reflexivity is provided by a degenerate simplex $s_n\sigma$, whose faces tautologically exhibit $\sigma \sim \sigma$.

3. **The structure of $\Delta^1$ (from [[Def - Simplicial Set]]).** The counterexample uses the explicit simplices of $\Delta^1$: two non-degenerate vertices and one non-degenerate edge, with no edge in the reverse direction.

---

# Hints

> [!note]- Hint 1
> Reflexivity needs no Kan condition. Look for a *degenerate* $(n+1)$-simplex whose relevant faces are $\sigma$ and $\sigma$.

> [!note]- Hint 2
> For transitivity, you are given two $(n+1)$-simplices $H_1$ (witnessing $\sigma \sim \tau$) and $H_2$ (witnessing $\tau \sim \rho$). They share the face $\tau$. Together with some degenerate simplices, they are the faces of a single $(n+2)$-dimensional horn.

> [!note]- Hint 3
> Build the horn $\Lambda^{n+2}_j$ so that $H_1$ and $H_2$ are two of its faces and the missing face $d_j$ is the homotopy you want, $\sigma \sim \rho$. The Kan condition fills the horn; read off $d_j$ of the filler.

> [!note]- Hint 4
> For (c): the vertices of $\Delta^1$ are $0$ and $1$. An edge $0 \to 1$ exists (the non-degenerate $1$-simplex), giving $0 \sim 1$. Is there an edge $1 \to 0$? List all $1$-simplices of $\Delta^1$ — they are monotone maps $[1] \to [1]$ — and check.

---

# Solution

Reflexivity is free from a degeneracy. Symmetry and transitivity both require the [[Def - Kan Complex and the Nerve|Kan condition]]: the two given homotopies, sharing a common face, assemble into a horn, and its filler supplies the composite homotopy. The failure for $\Delta^1$ is that it has the edge $0 \to 1$ but no edge $1 \to 0$, so the relation is not symmetric.

**Step 1: Reflexivity (no Kan condition).**

> [!note]- Derivation
> Let $\sigma$ be a spheroid in dimension $n$ (so $d_i\sigma = s_0^{(n-1)}x$ for all $i$). Consider the degenerate $(n+1)$-simplex $H = s_n\sigma \in X_{n+1}$. The simplicial identities give $d_n H = d_n s_n \sigma = \sigma$ and $d_{n+1}H = d_{n+1}s_n\sigma = \sigma$, while for $i \le n-1$, $d_i H = d_i s_n \sigma = s_{n-1}d_i\sigma = s_{n-1}s_0^{(n-1)}x$, a degenerate spheroid at $x$. So $H$ is a homotopy rel basepoint from $\sigma$ to $\sigma$, proving $\sigma \sim \sigma$. No horn-filling was used.

**Step 2: Transitivity (this is where the Kan condition enters).**

> [!note]- Derivation
> Suppose $\sigma \sim \tau$ via $H_1$ ($d_nH_1 = \sigma$, $d_{n+1}H_1 = \tau$, lower faces degenerate) and $\tau \sim \rho$ via $H_2$ ($d_nH_2 = \tau$, $d_{n+1}H_2 = \rho$, lower faces degenerate). We build an $(n+2)$-simplex of $X$. Define a horn $\Lambda^{n+2}_{n} \to X$ by prescribing its faces: place $H_2$ as the face $d_{n+2}$, $H_1$ as the face $d_{n+1}$, and degenerate spheroid-homotopies as the remaining faces $d_i$ for $i \le n-1$, leaving the face $d_n$ empty. One checks these prescribed faces agree on their common sub-faces (this is the compatibility condition for a horn, and it holds because $H_1, H_2$ share $\tau$ and the rest are degenerate). This assembles to a genuine horn $\Lambda^{n+2}_n \to X$. Since $X$ is a [[Def - Kan Complex and the Nerve|Kan complex]], it fills to a simplex $\Phi : \Delta^{n+2} \to X$. The missing face $d_n\Phi$ is then an $(n+1)$-simplex with $d_n(d_n\Phi) = \sigma$, $d_{n+1}(d_n\Phi) = \rho$ and lower faces degenerate — exactly a homotopy $\sigma \sim \rho$. (Symmetry is the same argument with $H_1$ and a reflexive $H_2 = s_n\tau$.) **The horn-filling is the only step that uses fibrancy.**

**Step 3: Failure for $\Delta^1$.**

> [!note]- Derivation
> The $1$-simplices of $\Delta^1 = \Delta(-,[1])$ are the monotone maps $[1] \to [1]$: the constant maps $c_0, c_1$ (degenerate edges at the vertices $0, 1$) and the identity $\mathrm{id}$ (the non-degenerate edge from $0$ to $1$). There is *no* monotone map $[1] \to [1]$ realising an edge from $1$ to $0$ — monotonicity forbids it. For $n = 0$ the spheroids are the vertices $\{0, 1\}$, and "$v \sim v'$" means there is an edge $v \to v'$. The edge $\mathrm{id} = (0 \to 1)$ gives $0 \sim 1$. But there is no edge $1 \to 0$, so we do *not* have $1 \sim 0$: the relation is **not symmetric**. Hence the naive quotient $X_0/\sim$ is ill-defined as a set of equivalence classes. The repair is to fibrantly replace $\Delta^1 \xrightarrow{\sim} \Delta^0$ (anodyne, since $\Delta^1$ is contractible) and set $\pi_0(\Delta^1) := \pi_0(\Delta^0) = *$.

> [!note]- Complete formal solution
> *(a) Reflexivity.* For a spheroid $\sigma \in X_n$, the degenerate simplex $H = s_n\sigma$ has $d_nH = d_{n+1}H = \sigma$ and lower faces degenerate (simplicial identities), so $\sigma \sim \sigma$ for any $X$.
>
> *(b) Transitivity/symmetry, $X$ Kan.* Given $H_1 : \sigma \sim \tau$ and $H_2 : \tau \sim \rho$, prescribe a horn $\Lambda^{n+2}_n \to X$ with $d_{n+1} = H_1$, $d_{n+2} = H_2$, lower faces degenerate. The faces are compatible (they share $\tau$ and degeneracies), so this is a horn; fill it by the [[Def - Kan Complex and the Nerve|Kan condition]] to $\Phi$, and $d_n\Phi$ is a homotopy $\sigma \sim \rho$. Symmetry: take $H_2 = s_n\tau$. So $\sim$ is an equivalence relation and $\pi_n(X,x) = Z_n/\sim$ is well-defined. The unique use of fibrancy is the horn-fill.
>
> *(c) $\Delta^1$.* Its $1$-simplices are $c_0, c_1, \mathrm{id}$; no edge runs $1 \to 0$. So $0 \sim 1$ (via $\mathrm{id}$) but not $1 \sim 0$: $\sim$ is not symmetric, and $X_0/\sim$ is not a quotient. $\quad\blacksquare$

---

# Key Takeaways

**The Kan condition is the transitivity of the homotopy relation — that is its operational meaning here.** It is easy to treat fibrancy as an opaque technical hypothesis, but this exercise shows precisely what it buys: the single horn-fill in Step 2 is the *only* place the Kan condition is used, and without it the homotopy relation is not transitive, so $\pi_n$ is not even a set. The trigger-reaction to install is: *whenever a "homotopy of homotopies" or a "compose two homotopies" step appears, it is a horn-fill, and it requires fibrancy.* This is why every homotopy-group construction in $\mathbf{sSet}$ begins by ensuring the objects are Kan, and why the first move on a non-fibrant object is fibrant replacement. The same pattern — "assemble several simplices sharing faces into a horn, fill it" — is the universal mechanism behind the group operation, associativity, inverses, and the long exact sequence.

**Degeneracies provide all the "free" homotopies, with no fibrancy needed.** Reflexivity came from a degenerate simplex, and this is general: degeneracies are the constant/identity homotopies of the theory, available in any simplicial set. The diagnostic is that any homotopy-theoretic fact provable "by a degeneracy" needs no Kan condition — it is structural, holding for all simplicial sets — whereas any fact needing a genuine (non-degenerate) filler needs fibrancy. Separating these two kinds of step is how one locates exactly where fibrancy is essential in a longer argument, and it explains why semi-simplicial sets (which lack degeneracies) have a worse homotopy theory: they cannot even express the reflexive homotopies for free.

**Directedness without invertibility is the precise obstruction in the non-Kan case.** The failure for $\Delta^1$ is not random: it is that $\Delta^1$ records a *directed* edge $0 \to 1$ with no inverse, exactly as the [[Def - Quasi-Category|quasi-category]] $\Delta^1$ models the arrow category, which is not a groupoid. The general lesson is that outer-horn filling is the combinatorial form of invertibility, and a simplicial set fails to be Kan precisely when it has non-invertible directed structure. The transferable insight: when a homotopy relation fails to be symmetric, look for a directed edge with no inverse; the repair is either to invert it (pass to a groupoid / Kan complex) or to fibrantly replace, which formally adds the missing inverses up to homotopy.
