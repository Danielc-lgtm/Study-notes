---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
  - "Def - Domain in the Complex Plane"
tags: [analysis, complex-analysis]
---

# Notation

Throughout, $f$ is a complex-valued function, $a \in \mathbb{C}$ a point, $D(a, R) = \{z : |z - a| < R\}$ an open disc of radius $R > 0$ centred at $a$, and $D(a, R) \setminus \{a\}$ the punctured disc. The full registry lives on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Axiom Motivation

A holomorphic function $f$ might be defined and holomorphic everywhere on some open set *except* at one bad point $a$, where it either fails to be defined or fails to be holomorphic. The clean version of this situation — the one that admits a beautiful classification — is when $a$ is an *isolated* bad point: $f$ is holomorphic on a small punctured disc $D(a, R) \setminus \{a\}$, and the rest of the disc is just the single point $a$ where something goes wrong.

Why this specific form of "bad point"? Because the punctured disc is exactly where Laurent series live. A function holomorphic on a punctured disc has a Laurent expansion around the puncture, and the structure of that expansion — finitely or infinitely many negative-power terms — classifies the singularity. If the bad point were *not* isolated — if there were a sequence of bad points accumulating at $a$, or a whole curve of bad points through $a$ — then no Laurent expansion would exist near $a$ and the classification machinery would not apply.

Examples of non-isolated singularities: $1/\sin(1/z)$ has poles at $z = 1/(n\pi)$ for every integer $n$, accumulating at $z = 0$, so $z = 0$ is not isolated. The natural logarithm $\log z$ on the principal branch has a *branch cut* — a whole ray $(-\infty, 0]$ of bad points — so its bad set is not isolated either. These functions live outside the §3.3 framework; they require different techniques (branch cuts, Riemann surfaces, multi-valued function theory).

The isolated singularity assumption is precisely what makes the trichotomy "removable, pole, essential" exhaustive and clean: every isolated singularity falls into exactly one of these three buckets, classified by counting negative powers in the Laurent expansion. Without isolation, the buckets would not cover all cases — we would need additional bucket types for branch points, cluster points, natural boundaries, and other wild behaviours.

What would break with a stronger or weaker definition? A stronger definition requiring $f$ to *extend continuously* to $a$ would already exclude poles and essential singularities — too restrictive. A weaker definition allowing $f$ to be only defined "near" $a$ in some vague sense would lose the Laurent expansion. The "holomorphic on a punctured disc" formulation is the unique condition that simultaneously isolates the bad point and gives the Laurent expansion.

A subtle terminological point: some sources call $a$ an isolated singularity of $f$ even when $f$ extends holomorphically to $a$ (i.e., when the singularity is removable) — they are then using "singularity" to mean "point where the function is *not yet defined*", not "point where the function genuinely misbehaves". We adopt this convention, since the removable case is precisely the case where the singularity *can be removed*, and this terminological choice makes the trichotomy "removable / pole / essential" cleanly exhaustive.

---

# The Definition

A point $a \in \mathbb{C}$ is an **isolated singularity** of $f$ if there exists $R > 0$ such that $f$ is holomorphic on the punctured disc $D(a, R) \setminus \{a\}$ but is not defined (or not holomorphic) at $a$.

Equivalently, $f$ is holomorphic on some annulus $A(a; 0, R)$ for some $R > 0$.

By the [[Thm - Laurent Series Theorem|Laurent series theorem]], $f$ has a unique Laurent expansion
$$f(z) = \sum_{n=-\infty}^\infty c_n (z - a)^n$$
on $D(a, R) \setminus \{a\}$. The negative-power part $\sum_{n \geq 1} c_{-n}(z - a)^{-n}$ is called the **principal part** of $f$ at $a$, and it classifies the singularity into one of three types (see [[Def - Removable Singularity, Pole, Essential Singularity]]).

A function $f$ on an open $U \subseteq \mathbb{C}$ is **meromorphic** on $U$ if its only singularities in $U$ are poles (no essential singularities, and the set of poles is a discrete subset of $U$).

---

# Relate to Other Fields / Compression

In **algebraic geometry**, the analog is a **closed point** of a curve: a place on a smooth curve where one can take a local Laurent expansion of a rational function in a local parameter. The classification of singularities of meromorphic functions on a Riemann surface uses the same trichotomy, with the "essential singularity" case being the obstruction to meromorphicity.

In **partial differential equations**, the analog is a **singular point** of a solution to an elliptic or parabolic equation. A solution to Laplace's equation $\Delta u = 0$ on a punctured neighborhood of a point in $\mathbb{R}^n$ either extends harmonically (removable), or blows up like a fundamental solution (pole-like), or has wilder behaviour. The analog of Laurent's theorem is the Bôcher characterization of singularities of harmonic functions; the analog of Riemann's removable singularity theorem is the Kelvin transform.

In **dynamical systems**, the analog is a **fixed point** of a holomorphic map or a **critical point** of a Hamiltonian flow. The local classification of such fixed points (attracting, repelling, parabolic, irrationally indifferent) uses Laurent-like expansions of the map's iterates and is the starting point of complex dynamics.

---

# Examples / Corollaries

**Is an instance — $f(z) = 1/z$ at $z = 0$.** Holomorphic on $\mathbb{C}^\times = \mathbb{C} \setminus \{0\}$, not defined at $z = 0$. The punctured disc $D(0, R) \setminus \{0\}$ is contained in the domain of holomorphicity for every $R > 0$, so $z = 0$ is an isolated singularity. The Laurent expansion is $1/z$ (a single $c_{-1} = 1$ term), so it is a *simple pole*.

**Is an instance — $f(z) = e^{1/z}$ at $z = 0$.** Holomorphic on $\mathbb{C}^\times$, not defined at $0$. The Laurent expansion is $\sum_{n=0}^\infty z^{-n}/n! = 1 + 1/z + 1/(2z^2) + \ldots$, infinitely many negative-power terms, so it is an *essential singularity*.

**Is an instance — $f(z) = (\sin z)/z$ at $z = 0$.** Holomorphic on $\mathbb{C}^\times$ (the formula is undefined at $0$ where the denominator vanishes). However, $\sin z = z - z^3/6 + \ldots$, so $(\sin z)/z = 1 - z^2/6 + \ldots$ has a Laurent expansion with no negative-power terms — it is a *removable singularity*. The function extends holomorphically to $z = 0$ by defining $f(0) = 1$.

**Is NOT an instance — $f(z) = 1/\sin(1/z)$ at $z = 0$.** This function has poles at $z = 1/(n\pi)$ for every integer $n$, accumulating at $z = 0$. So $z = 0$ is *not* isolated — every punctured disc around $0$ contains other singularities. The function is not even defined on any punctured disc $D(0, R) \setminus \{0\}$.

**Is NOT an instance — $f(z) = \log z$ on the principal branch, at any point of $(-\infty, 0]$.** The principal branch of $\log z$ has a branch cut along $(-\infty, 0]$ — a whole ray of "bad" points. No point on the ray is isolated (every neighborhood of such a point contains a whole arc of the ray), so the §3.3 framework does not apply. Treating branch points requires Riemann surface theory.

**Is NOT an instance — $f(z) = 1/(z^2 + 1)$ at $z = 0$.** This function is *holomorphic* at $0$ (the function value is $1$, and a neighborhood of $0$ avoids the singularities at $\pm i$). The "singularity at $0$" is not a singularity at all — $0$ is a regular point.

**Corollary — discreteness of singular set.** The set of isolated singularities of a function holomorphic on an open $U$ minus a set $S$ is automatically discrete in $U$ (since each singularity has a punctured-disc neighborhood disjoint from other singularities). A meromorphic function on $U$ thus has a discrete (locally finite) set of poles, with no accumulation points in $U$.

**Corollary — the punctured-disc condition is exactly what gives a Laurent series.** $f$ holomorphic on $D(a, R) \setminus \{a\}$ ⟺ $f$ admits a Laurent expansion around $a$ converging on that punctured disc. This is the *true name* of the isolated singularity assumption: it is exactly the regularity needed for the Laurent expansion to exist.

---

# Unlocked by This

> [!tip] Classification of Singularities *(from §3.3)*
> The [[Def - Removable Singularity, Pole, Essential Singularity|trichotomy]] classifying isolated singularities by their principal part: zero, finite, or infinite. Every isolated singularity falls into exactly one bucket.

> [!tip] Residue Theory and Contour Integration *(from §3.3, §3.4)*
> All of [[Thm - Residue Theorem|residue theory]] applies only to isolated singularities. The residue is the single Laurent coefficient $c_{-1}$, which is well-defined only when a Laurent expansion exists, which is exactly the isolated case.

> [!tip] Meromorphic Functions and the Riemann Sphere *(from §3.5+)*
> A function with only pole singularities, all isolated, is **meromorphic** — equivalently, a holomorphic map to the Riemann sphere $\hat{\mathbb{C}} = \mathbb{C} \cup \{\infty\}$. Meromorphic functions on $\mathbb{C}$ form a field, the foundation of algebraic function theory and Riemann surface theory.
