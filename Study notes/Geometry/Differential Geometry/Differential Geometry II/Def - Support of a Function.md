---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Function on a Manifold"
  - "Def - Topological Space"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a topological space (typically a smooth manifold for this topic, but the definition is purely topological). $f : M \to \mathbb{R}$ or $f : M \to \mathbb{R}^k$ is a function. $\operatorname{supp}(f)$ denotes the support of $f$. We write $\overline S$ for the topological closure of a subset $S \subseteq M$. The full registry is on [[Differential Geometry II — Smooth Maps and Partitions of Unity]].

---

# Axiom Motivation

The naive question: where is $f$ "actually doing something"? The naive answer: at the points where $f$ is nonzero. But this is wrong in a subtle way. Consider $f : \mathbb{R} \to \mathbb{R}$, the function that equals $1/n$ at $x = 1/n$ for $n \in \mathbb{N}$ and $0$ elsewhere. The set where $f$ is nonzero is $\{1/n : n \in \mathbb{N}\}$, a discrete subset of $\mathbb{R}$. But $f$ is *not continuous* at $0$, even though $f(0) = 0$, because the values $f(1/n) = 1/n$ converge to $0$ only because they themselves shrink. In any "where does $f$ matter" sense, the point $0$ should be included — it is a limit of points where $f$ is nonzero, and any continuous modification of $f$ in a neighbourhood of $0$ would have to behave consistently with that limit.

The fix is to take the *closure* of the set where $f$ is nonzero. The closure includes all limit points, and it is the smallest closed set outside of which $f$ vanishes identically. **The support of $f$ is the closure of the non-vanishing set** — and this is the correct topological notion of "where $f$ lives".

*Why the closure?* For three reasons. First, the closure ensures support is a *closed set*, which is the relevant kind of object for many topological operations (compactness, normality, separation). Second, the closure captures "limit-of-being-nonzero" — a point $p$ is in $\operatorname{supp}(f)$ iff every neighbourhood of $p$ contains a point where $f$ does not vanish, which is the right operational meaning. Third, the closure makes support behave correctly under continuity: a continuous function $f$ that vanishes on an open set $U$ has $\operatorname{supp}(f) \subseteq M \setminus U$, so $U$ is "outside the support", which matches intuition.

*Could we instead define support as the topological boundary of the non-vanishing set?* No — the boundary would consist only of limit points where $f$ vanishes, not the interior where $f$ is nonzero. The interior of the non-vanishing set is *also* part of the support.

*Could we define support as the complement of the largest open set on which $f$ vanishes?* Yes — this is equivalent. The largest open set on which $f$ vanishes is the interior of $\{p : f(p) = 0\}$ — its complement is $\overline{\{p : f(p) \neq 0\}} = \operatorname{supp}(f)$. The two characterizations agree.

The notion of *compactly supported* — meaning $\operatorname{supp}(f)$ is compact — is essential for many integration and analysis problems. A compactly supported function is "essentially finite": it vanishes outside a compact set, so it cannot escape to infinity. Smooth bump functions are by construction compactly supported, and they are the building blocks of every "local" construction in differential geometry. The set of all compactly supported smooth functions on $M$ is denoted $C^\infty_c(M)$.

The notion of *supported in $U$* — meaning $\operatorname{supp}(f) \subseteq U$ — is the precise statement of "$f$ lives in $U$". This is the condition appearing in the definition of partitions of unity ([[Def - Partition of Unity on a Manifold]]) and in the smooth extension lemma ([[Thm - Smooth Extension Lemma]]).

The definition makes sense for any function $f$ from a topological space to a topological vector space (where "zero" is a fixed element). We state it for $\mathbb{R}$- or $\mathbb{R}^k$-valued functions; the generalization is immediate.

---

# The Definition

Let $M$ be a topological space and $f : M \to \mathbb{R}$ (or $f : M \to \mathbb{R}^k$, or $f : M \to V$ for any topological vector space $V$). The **support** of $f$ is
$$\operatorname{supp}(f) = \overline{\{p \in M : f(p) \neq 0\}},$$
the topological closure of the set where $f$ does not vanish.

The function $f$ is **supported in $U$** (for $U \subseteq M$) if $\operatorname{supp}(f) \subseteq U$. Equivalently, $f$ vanishes on $M \setminus \overline U$... no, more precisely, $f$ vanishes on $M \setminus U$ and the closure of $\{f \neq 0\}$ is in $U$ (which requires $U$ to contain that closure). When $U$ is open, "$f$ supported in $U$" is equivalent to "$f$ vanishes on $M \setminus U$" together with "$\operatorname{supp}(f) \subseteq U$" (the latter being automatic when $U$ is open and $\{f \neq 0\} \subseteq U$ is closed in $M$). For arbitrary $U$, the cleanest formulation is the displayed inclusion.

The function $f$ is **compactly supported** if $\operatorname{supp}(f)$ is a compact subset of $M$.

The set of compactly supported continuous functions $M \to \mathbb{R}$ is denoted $C_c(M)$; the set of compactly supported smooth functions on a smooth manifold $M$ is denoted $C^\infty_c(M)$ (this is an $\mathbb{R}$-vector subspace of $C^\infty(M)$, and an ideal of the ring $C^\infty(M)$ when $M$ is non-compact — though it lacks a multiplicative identity, since $1$ is not compactly supported on non-compact $M$).

**Equivalent characterization.** $p \in \operatorname{supp}(f)$ if and only if every open neighbourhood of $p$ contains a point where $f$ does not vanish.

**Equivalent characterization (alt).** $\operatorname{supp}(f) = M \setminus W$ where $W$ is the largest open set on which $f$ vanishes identically.

---

# Relate to Other Fields / Compression

The support of a function is **the smallest closed set outside of which the function vanishes identically**. This is the operational notion that makes support behave well under topological operations.

In **measure theory**, the *essential support* of a measurable function is a closely related notion: the smallest closed set outside of which $f = 0$ almost everywhere. For continuous functions on a "nice" space, essential support and support coincide.

In **distribution theory**, the support of a distribution $u$ on $\mathbb{R}^n$ is defined dually: $\operatorname{supp}(u)$ is the complement of the largest open set on which $u$ vanishes (where "vanishes" means $\langle u, \varphi \rangle = 0$ for every test function $\varphi$ supported in that open set). For a distribution arising from a continuous function, this matches the function-theoretic support.

In **sheaf theory**, support is internalized: the support of a section $s$ of a sheaf $\mathcal{F}$ is $\{p : s_p \neq 0\}$ in the stalk-wise sense — the locus where the germ is non-trivial.

**True name:** *the support is the smallest closed set on whose complement $f$ is identically zero*. The official definition (closure of the non-vanishing set) is a constructive way of writing this; the operational meaning is "where $f$ matters".

---

# Examples / Corollaries

**Is an instance: $f(x) = e^{-x^2}$ on $\mathbb{R}$.** The function is positive everywhere, so $\{f \neq 0\} = \mathbb{R}$, hence $\operatorname{supp}(f) = \mathbb{R}$ — the full real line. Not compactly supported, even though $f \to 0$ at infinity.

**Is an instance: a bump function.** The standard bump $H : \mathbb{R} \to [0, 1]$ with $H = 1$ on $[-1, 1]$ and $H = 0$ on $\mathbb{R} \setminus [-2, 2]$ has support $\operatorname{supp}(H) = [-2, 2]$ (closure of where $H > 0$, which is $(-2, 2)$). Compactly supported.

**Is an instance: $f(x) = x$ on $\mathbb{R}$.** $\{f \neq 0\} = \mathbb{R} \setminus \{0\}$, whose closure is $\mathbb{R}$. So $\operatorname{supp}(f) = \mathbb{R}$.

**Is an instance: the zero function.** $\operatorname{supp}(0) = \overline{\emptyset} = \emptyset$. The empty set is the support of the zero function.

**Is an instance: characteristic function of a non-closed set.** If $A \subseteq M$ is not closed and $\chi_A : M \to \mathbb{R}$ is its indicator, then $\operatorname{supp}(\chi_A) = \overline A$, which is strictly larger than $A$. (Note: $\chi_A$ is generally not continuous, but the support definition is purely topological.)

**Is NOT an instance of "where $f$ is nonzero": the support.** A common confusion is to identify $\operatorname{supp}(f)$ with $\{p : f(p) \neq 0\}$. The two agree if and only if the latter is already closed. The latter is *not* closed for most functions: even the smooth bump $H$ above has $\{H \neq 0\} = (-2, 2)$, not closed, while $\operatorname{supp}(H) = [-2, 2]$.

**Corollary (support of a sum).** $\operatorname{supp}(f + g) \subseteq \operatorname{supp}(f) \cup \operatorname{supp}(g)$. *Proof:* if $p \notin \operatorname{supp}(f) \cup \operatorname{supp}(g)$, then $p$ has a neighbourhood disjoint from both supports, hence on which both $f$ and $g$ vanish, hence on which $f + g$ vanishes, hence $p \notin \operatorname{supp}(f + g)$. The inclusion can be strict: $f$ and $-f$ both have the same support, but $f + (-f) = 0$ has empty support.

**Corollary (support of a product).** $\operatorname{supp}(fg) \subseteq \operatorname{supp}(f) \cap \operatorname{supp}(g)$. *Proof:* if $f$ or $g$ vanishes at $p$, so does $fg$; closures of intersections may strictly contain, but supports of products are inside the intersection of supports.

**Corollary (support of $\lambda f$ for $\lambda \neq 0$).** $\operatorname{supp}(\lambda f) = \operatorname{supp}(f)$ for nonzero $\lambda \in \mathbb{R}$. The non-vanishing set is the same.

**Corollary (support is closed).** $\operatorname{supp}(f)$ is closed in $M$ by definition (it is a closure). This is one of the key structural properties — supports are objects of the closed-set lattice of $M$.

**Corollary (smoothness on the complement of support).** If $f$ is continuous (or smooth) and $\operatorname{supp}(f) \subseteq U$, then $f$ vanishes identically on $M \setminus U$. So in any chart contained in $M \setminus U$, the coordinate representation of $f$ is the zero function.

**Calibration check.** Verify the following: (i) the support of the function $\sin x$ on $\mathbb{R}$ is all of $\mathbb{R}$ (not the complement of $\{n\pi\}$). (ii) The support of a sum of bump functions, each supported in a small ball, is the union of their supports (assume the balls are disjoint or check the inclusion). (iii) For $f$ continuous on a compact space $M$, $\operatorname{supp}(f)$ is automatically compact (every subset of a compact space is compact only if closed; supports are always closed, hence compact). (iv) If $f \in C^\infty_c(\mathbb{R}^n)$ has $\operatorname{supp}(f) \subseteq B(0, R)$, then $f \equiv 0$ on $\{|x| > R\}$.

---

# Unlocked by This

> [!tip] Compactly Supported Smooth Functions $C^\infty_c(M)$ *(from Differential Geometry / Distribution Theory)*
> The space $C^\infty_c(M)$ of compactly supported smooth functions is the standard space of **test functions** in distribution theory. It is dense in $C^\infty(M)$ in suitable topologies, and the **dual space** $C^\infty_c(M)^*$ is the space of distributions on $M$. The richness of $C^\infty_c(M)$ — which depends on the existence of smooth bump functions and partitions of unity — is what makes distribution theory work on manifolds.

> [!tip] Integration on Non-Compact Manifolds *(from Differential Geometry)*
> Integration of a differential form on a non-compact manifold requires compact support (or rapid decay) to converge. Defining $\int_M \omega$ for general $\omega$ requires either restricting to $\omega \in \Omega^n_c(M)$ (compactly supported forms) or imposing decay conditions. The mechanism that gives compact support is multiplication by a bump function from a partition of unity. See [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|DG IX]].

> [!tip] Sheaves with Support *(from Sheaf Theory)*
> The notion of support generalizes from functions to **sections of sheaves**. For a sheaf $\mathcal{F}$, the support of a section $s$ is $\{p : s_p \neq 0\}$ (the stalk-wise vanishing locus). For "soft" sheaves (such as the sheaf of smooth functions), every section can be modified to have arbitrary support without changing its restriction to any open set — this is the mechanism behind the acyclicity of soft sheaves.
