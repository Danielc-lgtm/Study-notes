---
type: remark
subject: probability-geometry
prereqs:
  - "Def - Fuchsian Group and the Hyperbolic Quotient Surface"
  - "Def - Hyperbolic Plane"
  - "Def - Universal Cover"
  - "Def - Dirichlet Form and its Operator and Semigroup"
  - "Def - Heat Kernel and Heat Semigroup"
tags: [paper, brownian-loops, hyperbolic-geometry, potential-theory]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "unnumbered; §3.0 — descent of the heat kernel to the quotient by periodisation"
---

# Notation

- $\mathbb{H}^2 = \{x + iy : y > 0\}$ — the upper half-plane with hyperbolic metric $ds^2 = (dx^2 + dy^2)/y^2$; isometry group $\mathrm{PSL}(2, \mathbb{R})$.
- $\Gamma \subset \mathrm{PSL}(2, \mathbb{R})$ — a torsion-free, geometrically finite Fuchsian group.
- $X = \Gamma\backslash\mathbb{H}^2$ — the hyperbolic quotient surface; $\pi : \mathbb{H}^2 \to X$ the covering projection.
- $\rho_{\mathbb{H}^2}$, $\rho_X$ — hyperbolic area measures on $\mathbb{H}^2$ and $X$; $\rho_X = \pi_*(\rho_{\mathbb{H}^2}|_F)$ for any fundamental region $F$.
- $(\mathcal{E}, \mathcal{F})$ — a regular symmetric Dirichlet form on $L^2(\mathbb{H}^2, \rho_{\mathbb{H}^2})$.
- $p^E_{\mathbb{H}^2}(t, z, w)$ — its (jointly measurable) heat kernel: $(P^E_t f)(z) = \int p^E_{\mathbb{H}^2}(t, z, w) f(w)\,d\rho_{\mathbb{H}^2}(w)$.
- **$\Gamma$-invariance of the upstairs kernel.** $p^E_{\mathbb{H}^2}(t, h z, h w) = p^E_{\mathbb{H}^2}(t, z, w)$ for every $h \in \Gamma$, $t > 0$, $z, w \in \mathbb{H}^2$.
- $p^E_X(t, z, w)$ — the *downstairs* heat kernel on $X$, the object this remark builds.
- $[h]_{\mathrm{conj}} = \{q h q^{-1} : q \in \Gamma\}$ — conjugacy class of $h \in \Gamma$; corresponds to a free homotopy class of loops on $X$.

> [!recall]- Universal cover $\pi : \mathbb{H}^2 \to X$ and its lifts
> **Formally:** $\pi$ is a local isometry and a covering map: every point $x \in X$ has a neighbourhood $U$ such that $\pi^{-1}(U) = \sqcup_i U_i$ with each $U_i$ mapped isometrically to $U$. The fibre $\pi^{-1}(x)$ over any point $x \in X$ is exactly the $\Gamma$-orbit $\{h\tilde x : h \in \Gamma\}$ of any chosen lift $\tilde x$.
> **In words:** $\mathbb{H}^2$ is the "infinite unrolled" version of $X$: standing on $\mathbb{H}^2$ you walk forever without returning; standing on $X$ you come back. Every point on $X$ has infinitely many lifts on $\mathbb{H}^2$, one per element of $\Gamma$.
> **Concretely:** for the flat torus $T^2 = \mathbb{R}^2/\mathbb{Z}^2$, the universal cover is $\mathbb{R}^2 \to T^2$, $(x, y) \mapsto (x \bmod 1, y \bmod 1)$; the lifts of $(0.3, 0.7)$ are $\{(0.3 + m, 0.7 + n) : (m, n) \in \mathbb{Z}^2\}$. See [[Def - Universal Cover]].

> [!recall]- $\Gamma$-invariant Dirichlet form and $\Gamma$-invariant heat kernel
> **Formally:** the form $(\mathcal{E}, \mathcal{F})$ is $\Gamma$-invariant if $\mathcal{E}(f \circ h, g \circ h) = \mathcal{E}(f, g)$ for all $h \in \Gamma$ and all $f, g \in \mathcal{F}$. This is equivalent to $\Gamma$-invariance of the associated heat kernel: $p^E_{\mathbb{H}^2}(t, hz, hw) = p^E_{\mathbb{H}^2}(t, z, w)$.
> **In words:** the form treats $\Gamma$-related points identically; the process it generates has the same law under any deck move. This is what lets the form (and its process) *descend* to a form (and a process) on $X$.
> **Concretely:** the Laplace–Beltrami form $\mathcal{E}(f, g) = \int \langle \nabla f, \nabla g\rangle\,d\rho_{\mathbb{H}^2}$ is $\mathrm{Isom}(\mathbb{H}^2)$-invariant, hence in particular $\Gamma$-invariant for any Fuchsian $\Gamma$; the associated heat kernel $p_{\mathbb{H}^2}(t, z, w)$ depends only on the hyperbolic distance $d(z, w)$, which is $\mathrm{PSL}(2, \mathbb{R})$-invariant. See [[Def - Dirichlet Form and its Operator and Semigroup]].

> [!recall]- Free homotopy classes on $X$ ↔ conjugacy classes in $\Gamma$
> **Formally:** two oriented closed curves on $X$ are *freely homotopic* if one continuously deforms into the other with the basepoint allowed to move. The set of free homotopy classes is in bijection with the set of conjugacy classes of $\Gamma$: a loop $\omega$ rooted at $x$ lifts to an arc from a chosen lift $\tilde x$ to $h_\omega \tilde x$, and moving the basepoint by $q \in \Gamma$ carries the lift to its $q$-translate and changes the recorded element to $q h_\omega q^{-1}$.
> **In words:** each loop "goes around some holes in some pattern"; two loops in the same pattern (basepoint allowed to drift) are one class. Algebraically: forgetting the basepoint is exactly conjugation of the recorded deck element.
> **Concretely:** on $T^2 = \mathbb{R}^2/\mathbb{Z}^2$, $\Gamma = \mathbb{Z}^2$ is abelian, conjugacy classes are singletons, so free homotopy classes ↔ $\mathbb{Z}^2$, one per pair $(a, b)$ (winding $a$ times horizontally, $b$ times vertically).

> [!recall]- Geometrically finite Fuchsian group and orbit growth
> **Formally:** a torsion-free Fuchsian $\Gamma$ is *geometrically finite* if it admits a finite-sided fundamental polygon in $\mathbb{H}^2$; equivalently, $X = \Gamma\backslash\mathbb{H}^2$ has finitely generated $\pi_1$ and finitely many ends (cusps and funnels). The orbit-counting function $N(z, w; R) := \#\{h \in \Gamma : d(z, hw) \le R\}$ has polynomial-in-$e^R$ growth in $R$, with an exponent (the *critical exponent* $\delta_\Gamma$) strictly less than $1$ — the maximum growth rate of hyperbolic balls. See [[Def - Fuchsian Group and the Hyperbolic Quotient Surface]].
> **In words:** geometrically-finite $\Gamma$ has enough symmetries that orbits are dense, but its orbits grow *slower* than the exponential decay of the heat kernel — so any orbit-sum of the kernel converges.
> **Concretely:** for a compact hyperbolic surface, $\#\{h \in \Gamma : d(z, hw) \le R\} \sim c(z, w) e^R$ as $R \to \infty$ (Margulis–Selberg orbit counting); the Brownian heat kernel $p_{\mathbb{H}^2}(t, z, w)$ decays as $e^{-d^2/(4t)}$ in $d = d(z, w)$, which beats any $e^R$ for fixed $t > 0$, so the periodisation is (uniformly on compacts) absolutely convergent.

---

# Claim / Identity

> **Claim (descent of the heat kernel by periodisation).** Let $(\mathcal{E}, \mathcal{F})$ be a $\Gamma$-invariant regular symmetric Dirichlet form on $L^2(\mathbb{H}^2, \rho_{\mathbb{H}^2})$ with $\Gamma$-invariant heat kernel $p^E_{\mathbb{H}^2}$ decaying fast enough in $d(z, w)$ to beat the $\Gamma$-orbit growth. Then for any $z, w \in X$ and any choice of lifts $\tilde z, \tilde w \in \mathbb{H}^2$ with $\pi(\tilde z) = z$, $\pi(\tilde w) = w$, the series
> $$p^E_X(t, z, w) \;:=\; \sum_{h \in \Gamma} p^E_{\mathbb{H}^2}(t, \tilde z, h \tilde w) \tag{$\heartsuit$}$$
> converges, is **independent of the choice of lifts**, and is the heat kernel of the descended regular symmetric Dirichlet form on $L^2(X, \rho_X)$. Moreover, the sum is *pre-sorted by homotopy class*: for a fixed conjugacy class $[\tau]_{\mathrm{conj}} \subset \Gamma$, the sub-sum $\sum_{h \in [\tau]_{\mathrm{conj}}} p^E_{\mathbb{H}^2}(t, \tilde z, h \tilde z)$ is the total mass of the downstairs bridge measure restricted to loops of type $C_X(\gamma)$.

---

# In One Line

The downstairs kernel is the sum of the upstairs kernel over the deck group; this is the standard way a $\Gamma$-invariant object on $\mathbb{H}^2$ becomes one on $X$, and it is what lets the whole homotopy decomposition of §3 work — each summand carries one deck transformation, which is one topological type of loop.

---

# Why It's True

**Mechanism (one sentence).** *A downstairs bridge from $z$ to $w$ over time $t$ decomposes, once lifted, as a countable disjoint union of upstairs bridges from $\tilde z$ to each lift $h \tilde w$ of $w$; summing their total masses gives the downstairs kernel.*

The picture: a Brownian (or diffusion) path on $X$ from $z$ to $w$ lifts uniquely to a path on $\mathbb{H}^2$ from a chosen $\tilde z$; its endpoint is some lift $h \tilde w$, and $h$ is the loop's monodromy. The downstairs law of the whole path is the pushforward of the upstairs law. Summing over $h$ over the full group $\Gamma$ enumerates *all* possible lift-endpoints, i.e. *all* homotopy classes, exactly once — so the downstairs kernel is the group-sum of the upstairs kernel. Restricting the sum to one conjugacy class picks out one topological type of downstairs loop.

The convergence claim is where **geometric finiteness** enters: the number of $\Gamma$-orbits of $w$ within hyperbolic distance $R$ of $z$ grows like $e^{\delta_\Gamma R}$ with $\delta_\Gamma < 1$, but the heat kernel decays like $e^{-d^2/(4t)}$ (Brownian) or faster; the two combine to give absolute convergence, uniformly on compact subsets.

---

# Derivation

> [!note]- Gap-free derivation
> **Setup.** Fix a $\Gamma$-invariant regular symmetric Dirichlet form $(\mathcal{E}, \mathcal{F})$ on $L^2(\mathbb{H}^2, \rho_{\mathbb{H}^2})$ with $\Gamma$-invariant jointly-measurable heat kernel $p^E_{\mathbb{H}^2}(t, z, w)$. Fix $z, w \in X$ and choose lifts $\tilde z, \tilde w \in \mathbb{H}^2$.
>
> **Step 1 — the series converges.** The number of lattice points $\#\{h \in \Gamma : d(\tilde z, h\tilde w) \le R\}$ is bounded by $C e^{\delta R}$ for some $C = C(\tilde z, \tilde w)$ and some $\delta = \delta_\Gamma \le 1$ (geometrically finite Fuchsian $\Gamma$; this is the Poincaré-series exponent of $\Gamma$; for a cocompact $\Gamma$, $\delta_\Gamma = 1$ but the kernel decay still wins, and for cusped or funnel-ended $\Gamma$, $\delta_\Gamma < 1$). The heat kernel $p^E_{\mathbb{H}^2}(t, z, w)$ decays faster than any polynomial in $d(z, w)$ (in fact Gaussian-type in the Brownian case, and dominated by the Brownian kernel in the subordinate cases); in particular for fixed $t > 0$,
> $$p^E_{\mathbb{H}^2}(t, \tilde z, h\tilde w) \;\le\; C_t\,e^{-c_t\,d(\tilde z, h\tilde w)^2}$$
> for some $c_t > 0$. Summing dyadically over annuli $R \le d(\tilde z, h\tilde w) < R + 1$ gives
> $$\sum_{h \in \Gamma} p^E_{\mathbb{H}^2}(t, \tilde z, h\tilde w) \;\le\; C_t \sum_{R \ge 0} e^{\delta R}\,e^{-c_t R^2} \;<\; \infty,$$
> convergent because a Gaussian tail beats an exponential envelope.
>
> **Step 2 — independence of the lifts.** Suppose we make different choices of lifts $\tilde z' = q_1 \tilde z$ and $\tilde w' = q_2 \tilde w$ with $q_1, q_2 \in \Gamma$. Then
> $$\sum_{h \in \Gamma} p^E_{\mathbb{H}^2}(t, \tilde z', h\tilde w') \;=\; \sum_{h \in \Gamma} p^E_{\mathbb{H}^2}(t, q_1 \tilde z, h q_2 \tilde w).$$
> Applying $\Gamma$-invariance with $q_1^{-1}$ (acting on both arguments simultaneously),
> $$p^E_{\mathbb{H}^2}(t, q_1\tilde z, hq_2\tilde w) \;=\; p^E_{\mathbb{H}^2}(t, \tilde z, q_1^{-1}hq_2\tilde w).$$
> As $h$ ranges over $\Gamma$, the substitution $h' := q_1^{-1} h q_2$ ranges over $\Gamma$ as well (a bijection of $\Gamma$ with itself); so relabelling the summation index,
> $$\sum_{h \in \Gamma} p^E_{\mathbb{H}^2}(t, \tilde z', h\tilde w') \;=\; \sum_{h' \in \Gamma} p^E_{\mathbb{H}^2}(t, \tilde z, h'\tilde w).$$
> The sum is the same regardless of the lifts, so $p^E_X(t, z, w)$ is well-defined on $X \times X$.
>
> **Step 3 — the sum is the heat kernel of the descended form.** The descended form $(\mathcal{E}_X, \mathcal{F}_X)$ on $L^2(X, \rho_X)$ is defined by identifying $L^2(X, \rho_X)$ with the $\Gamma$-invariant part of $L^2(\mathbb{H}^2, \rho_{\mathbb{H}^2})_{\mathrm{loc}}$: a function $f \in L^2(X, \rho_X)$ lifts to a $\Gamma$-periodic $\tilde f : \mathbb{H}^2 \to \mathbb{R}$, and $\mathcal{E}_X(f, g) := \mathcal{E}(\tilde f, \tilde g)$ (computed on any single fundamental region $F$). The semigroup $P^X_t$ on $L^2(X, \rho_X)$ is the restriction of $P^E_t$ to $\Gamma$-invariant functions, viewed downstairs. For $f \in L^2(X, \rho_X)$ and $z \in X$,
> $$(P^X_t f)(z) \;=\; \int_{\mathbb{H}^2} p^E_{\mathbb{H}^2}(t, \tilde z, \tilde w)\,\tilde f(\tilde w)\,d\rho_{\mathbb{H}^2}(\tilde w)$$
> (right-hand side computed for one lift $\tilde z$). Split the $\mathbb{H}^2$-integral into a sum over $\Gamma$-translates of one fundamental region $F$: since $\mathbb{H}^2 = \bigsqcup_{h \in \Gamma} h F$ (up to null boundaries) and $\tilde f$ is $\Gamma$-periodic,
> $$(P^X_t f)(z) \;=\; \sum_{h \in \Gamma} \int_{hF} p^E_{\mathbb{H}^2}(t, \tilde z, \tilde w)\,\tilde f(\tilde w)\,d\rho_{\mathbb{H}^2}(\tilde w).$$
> Substitute $\tilde w = h w'$ in the $h$-th integral (isometry, Jacobian $1$; $\tilde f(h w') = \tilde f(w') = f(\pi(w'))$ by periodicity):
> $$(P^X_t f)(z) \;=\; \sum_{h \in \Gamma} \int_F p^E_{\mathbb{H}^2}(t, \tilde z, h w')\,f(\pi(w'))\,d\rho_{\mathbb{H}^2}(w') \;=\; \int_F \Big[\sum_{h \in \Gamma} p^E_{\mathbb{H}^2}(t, \tilde z, h w')\Big] f(\pi(w'))\,d\rho_{\mathbb{H}^2}(w').$$
> The pushforward $\pi_*(\rho_{\mathbb{H}^2}|_F) = \rho_X$, so
> $$(P^X_t f)(z) \;=\; \int_X p^E_X(t, z, w)\,f(w)\,d\rho_X(w), \qquad p^E_X(t, z, w) := \sum_{h \in \Gamma} p^E_{\mathbb{H}^2}(t, \tilde z, h\tilde w).$$
> That identifies $p^E_X$ as the heat kernel of the descended semigroup.
>
> **Step 4 — the sum is pre-sorted by homotopy class.** Consider the bridge decomposition of the downstairs process at a base point $z$ (endpoint = $z$ too, so a loop). Each downstairs loop $\omega : [0, t] \to X$ rooted at $z$ lifts uniquely to an $\mathbb{H}^2$-arc from a chosen $\tilde z$ to some $h_\omega \tilde z$; $h_\omega \in \Gamma$ is the loop's monodromy. The pushforward-of-upstairs-bridge decomposition
> $$\mathbb{W}^{t, E}_{z \to z,\, X} \;=\; \sum_{h \in \Gamma} \pi_* \mathbb{W}^{t, E}_{\tilde z \to h\tilde z,\, \mathbb{H}^2}$$
> partitions the downstairs bridge into disjoint pieces, indexed by monodromy $h$, with total masses summing correctly to $p^E_X(t, z, z) = \sum_h p^E_{\mathbb{H}^2}(t, \tilde z, h\tilde z)$. Loops of free homotopy class $C_X(\gamma)$ correspond to $h \in [\tau]_{\mathrm{conj}}$, where $\tau$ is a primitive hyperbolic representative of $C_X(\gamma)$. So restricting the sum to $h \in [\tau]_{\mathrm{conj}}$ gives the total mass of the downstairs bridge restricted to loops of class $C_X(\gamma)$ — the class-mass integrand of [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]].
>
> This is the mechanism the whole homotopy decomposition rests on. $\blacksquare$

The two $\Gamma$-invariance uses are: (i) independence of the sum from lift choices (Step 2), and (ii) equivariance of the whole downstairs-vs-upstairs formalism (Step 3, in identifying $\mathcal{F}_X$ with the $\Gamma$-invariant part). Geometric finiteness is used exactly once, in Step 1, and there only to ensure absolute convergence.

---

# Where the paper uses this

Establishes the object $p^E_X$ that [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] decomposes. Every homotopy-class mass in §3.1 ([[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] and its four special cases §3.1.1–§3.1.4) starts from the pre-sorted sub-sum $\sum_{h \in [\tau^m]_{\mathrm{conj}}}$ of this periodisation. The definition of the class-mass for **jump processes** ([[Remark - Homotopy Classes for Jump Processes|Remark 3.1]]) is *by fiat* the restriction of this same periodisation to the target conjugacy class — so the whole decomposition of §3 is a story about restricting ($\heartsuit$) to conjugacy sub-classes and then unfolding the coset sum via [[Remark - Collapsing the Conjugacy Sum via the Centraliser|the centraliser identification]] in [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3]]. The same descent construction is redeployed in [[Paper - Brownian Loops — Homotopy and Homology — §7 Hyperbolic 3-Manifolds|§7]] for hyperbolic 3-manifolds ([[Thm - Homotopy Decomposition for 3-Manifolds|Theorem 7.1]]).
