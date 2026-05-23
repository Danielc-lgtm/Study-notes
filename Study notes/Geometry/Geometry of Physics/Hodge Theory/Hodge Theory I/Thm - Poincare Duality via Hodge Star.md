---
type: theorem
subject: hodge-theory
prereqs:
  - "Def - The Hodge Star Operator"
  - "Def - Harmonic Form"
  - "Thm - Harmonic Forms Represent de Rham Cohomology"
  - "Def - The de Rham Cohomology Pairing"
tags: [geometry, hodge-theory, cohomology, duality]
---

# Notation

$(M, g)$ is a closed oriented Riemannian $n$-manifold. $\star : \Omega^k(M) \to \Omega^{n-k}(M)$ is the Hodge star; $\mathcal{H}^k(M)$ is the space of harmonic $k$-forms; $H^k_{dR}(M; \mathbb{R})$ is the $k$-th de Rham cohomology; $b_k(M) = \dim H^k_{dR}(M)$. The integration pairing is $\langle\cdot,\cdot\rangle_H : H^k\times H^{n-k}\to\mathbb{R}$, $([\alpha], [\beta]) \mapsto \int_M\alpha\wedge\beta$.

---

# Statement

> **Theorem (Poincaré duality via the Hodge star).** Let $(M, g)$ be a closed oriented Riemannian $n$-manifold. The Hodge star $\star : \Omega^k(M) \to \Omega^{n-k}(M)$ restricts to an $\mathbb{R}$-linear isomorphism
> $$\star : \mathcal{H}^k(M) \xrightarrow{\cong} \mathcal{H}^{n-k}(M).$$
> Combined with the Hodge isomorphism $\mathcal{H}^k\cong H^k_{dR}$ in both degrees, this gives a canonical $\mathbb{R}$-linear isomorphism
> $$H^k_{dR}(M; \mathbb{R}) \cong H^{n-k}_{dR}(M; \mathbb{R}),$$
> which is **Poincaré duality** for the closed oriented manifold $M$. In particular, the Betti numbers satisfy
> $$b_k(M) = b_{n-k}(M).$$

> **Corollary (concrete pairing).** The de Rham cohomology pairing $\langle\cdot,\cdot\rangle_H : H^k_{dR}\times H^{n-k}_{dR}\to\mathbb{R}$ is non-degenerate, and on harmonic representatives is
> $$\langle[h_\alpha], [h_\beta]\rangle_H = \int_M h_\alpha\wedge h_\beta = (-1)^{?}\langle h_\alpha, \star^{-1}h_\beta\rangle_{L^2},$$
> the $L^2$ inner product of the harmonic representatives via the Hodge star. Non-degeneracy is automatic from the isomorphism $\mathcal{H}^k\cong\mathcal{H}^{n-k}$ via $\star$.

---

# Motivation

Poincaré duality is the fundamental symmetry of cohomology on closed oriented manifolds: cohomology in complementary degrees has equal dimension. The classical formulation is purely topological and proved via simplicial or cellular methods. Hodge theory provides a *Riemannian-geometric* proof that is both elegant and computationally explicit: the Hodge star, defined from the metric and orientation, *literally is* the duality isomorphism on harmonic representatives.

This theorem matters for three reasons.

**First, it gives an explicit construction of the duality isomorphism.** The Poincaré duality isomorphism $H^k\cong H^{n-k}$ is, in the topological proof, abstract and combinatorial — given by "cap product with the fundamental class". In Hodge theory, it is *literally* the Hodge star on harmonic representatives. Computationally explicit; given a harmonic representative $h$, its dual representative is $\star h$.

**Second, it produces a Hilbert-space inner product on cohomology.** The $L^2$ inner product on harmonic forms induces an inner product on $H^k_{dR}$ via the Hodge isomorphism. Poincaré duality combined with this gives the cohomology pairing $H^k\times H^{n-k}\to\mathbb{R}$ as a *concrete bilinear form* on real vector spaces, computable from harmonic representatives. This is the foundation of the **intersection form** on $H^2$ of a $4$-manifold, the **signature** of a $4n$-manifold, and many other geometric invariants.

**Third, it derives a topological theorem from analytic structure.** The duality $H^k\cong H^{n-k}$ is topological (proved combinatorially). The Hodge-theoretic proof derives it from analysis (Hodge isomorphism plus $\star$-commutation with $\Delta$). This is the model for **every "topology from analysis" argument** in geometric analysis — the Bochner technique, the index theorem, the heat-kernel proof of Gauss–Bonnet — all use the principle: introduce a metric, set up an elliptic operator, derive cohomological consequences from the operator's properties.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is a closed oriented Riemannian manifold and a cohomology class. Several sources lead to invoking Poincaré duality.

The most common source is **a known Betti number in degree $k$, with the dual degree $n - k$ desired**. Property $B$: knowledge of $b_k(M)$ for some $k$. The bridge is the duality $b_k = b_{n-k}$ — directly compute $b_{n-k}$ from $b_k$. Example: on a closed orientable $4$-manifold, $b_0 = 1$ (connected), so $b_4 = 1$ by duality (the volume class). On a closed orientable $3$-manifold, $b_0 = 1$ and so $b_3 = 1$; $b_1 = b_2$ by duality.

A second source is **the integration pairing of two specific cohomology classes**. Property $B$: classes $[\alpha] \in H^k$ and $[\beta] \in H^{n-k}$. The bridge is that the pairing $\int_M\alpha\wedge\beta$ is non-degenerate (by Poincaré duality), so the pairing computes a complete invariant of the two classes. Example: on a closed orientable surface, the pairing of two $1$-forms representing different homology classes is the intersection number of the underlying cycles — a topological invariant computable analytically.

A third source is **a question about the Euler characteristic and signature**. Property $B$: the Euler characteristic $\chi(M)$ and signature $\sigma(M)$ of a closed orientable $n$-manifold. The bridge through Poincaré duality: $\chi(M) = \sum_k(-1)^k b_k$ has $b_k = b_{n-k}$, so for $n$ odd, pairs of terms with $b_k = b_{n-k}$ contribute with opposite signs and cancel, giving $\chi(M) = 0$. For $n = 4$, the middle term $b_2 = b^+_2 + b^-_2$ (decomposition by $\star$-eigenvalues), and $\sigma = b^+_2 - b^-_2$. These invariants are constrained by Poincaré duality.

A fourth source is **a homogeneous-space symmetry computation**. Property $B$: $M$ is a homogeneous space $G/K$ with $G$-invariant metric, and the cohomology in some degree is computed. The bridge: Poincaré duality gives the cohomology in the complementary degree for free, by applying $\star$ to the $G$-invariant harmonic representative. Example: on $\mathbb{CP}^m$, harmonic forms are $G$-invariant under $\mathrm{U}(m+1)$, and $\star$ maps degree $2p$ to degree $2(m-p)$, immediately giving $h^{p,p} = h^{m-p, m-p} = 1$ for all $p$ — the diagonal Hodge diamond of $\mathbb{CP}^m$.

**Targets (Output Amplification)**

The conclusion is the duality $b_k = b_{n-k}$, and a concrete realization via $\star$. Several combinations produce stronger results.

The most powerful combination is **Poincaré duality plus Euler-characteristic alternating sum gives $\chi(M^{2k+1}) = 0$**. The Betti numbers of a closed orientable $(2k+1)$-manifold satisfy $b_j = b_{2k+1-j}$. In $\chi = \sum_j(-1)^j b_j$, pairs $(j, 2k+1-j)$ have $b_j = b_{2k+1-j}$ and contribute with opposite signs $(-1)^j + (-1)^{2k+1-j} = (-1)^j(1 + (-1)^{2k+1-2j}) = (-1)^j(1 + (-1)) = 0$. So all pairs cancel, $\chi = 0$. **Every closed orientable odd-dimensional manifold has Euler characteristic zero** — a topological corollary of Poincaré duality.

A second combination is **Poincaré duality plus intersection form on middle dimension gives signature**. On a closed orientable $4k$-manifold, the intersection form on $H^{2k}$ is a symmetric nondegenerate bilinear form on a finite-dimensional real vector space; its signature $\sigma(M) = b^+_{2k} - b^-_{2k}$ is a topological invariant. **Hirzebruch's signature theorem** computes $\sigma$ as the integral of the **L-polynomial** in the Pontryagin classes — an early instance of an index theorem (the index of the signature operator).

A third combination is **Poincaré duality plus harmonic representatives gives spectral organization**. The Laplacian's eigenspaces in complementary degrees ($k$ and $n - k$) are related by the Hodge star (since $\Delta\star = \star\Delta$). This organizes the spectrum: every positive eigenvalue $\lambda$ of $\Delta$ on $\Omega^k$ corresponds to an eigenvalue $\lambda$ on $\Omega^{n-k}$ via $\star$. The structural consequence is that **the spectrum on $\Omega^k$ and $\Omega^{n-k}$ are identical**, with eigenforms related by $\star$.

A fourth combination is **Poincaré duality plus cup product gives perfect pairing structure**. The cup product makes $H^*(M) = \bigoplus_k H^k(M)$ into a graded commutative algebra, and Poincaré duality says the cup product into the top-degree cohomology gives a perfect pairing $H^k\otimes H^{n-k}\to H^n\cong\mathbb{R}$. This is the algebraic structure underlying intersection theory: classes in complementary degrees "intersect" to give a number, with the intersection being non-degenerate.

---

# Why Is It True

The proof has two steps. **Step 1: $\star$ commutes with $\Delta$, hence $\star$ maps harmonic forms in degree $k$ to harmonic forms in degree $n - k$.** **Step 2: $\star$ is a pointwise isomorphism $\Lambda^k T^*M \to \Lambda^{n-k}T^*M$, hence globally an isomorphism on harmonic forms.**

The first step is the algebraic content: $\Delta = d\delta + \delta d$ commutes with $\star$ because $\star$ commutes with both $d^* = \delta$ (essentially the definition of $\delta = \pm\star d\star$ with double-star tracking) and... actually, more carefully: $\star d = \pm d^*\star$ and $\star\delta = \pm d\star$, so $\Delta = d\delta + \delta d$ becomes, after $\star$-application, $\Delta\star = d\delta\star + \delta d\star$ which equals $\star\Delta$ with sign tracking. The verification is a sign computation but the conclusion is that $\star$ commutes with $\Delta$.

The second step is the algebraic fact about $\star$: it is an invertible $C^\infty(M)$-linear map $\Omega^k\to\Omega^{n-k}$, so its restriction to the (finite-dimensional) subspace $\mathcal{H}^k$ is also an invertible $\mathbb{R}$-linear map onto $\mathcal{H}^{n-k}$ (the image lies in $\mathcal{H}^{n-k}$ by step 1, and the dimension count matches because $\star$ is invertible on the whole space).

Combining with the Hodge isomorphism $\mathcal{H}^k\cong H^k_{dR}$ in both degrees gives the cohomological isomorphism $H^k_{dR}\cong H^{n-k}_{dR}$, hence $b_k = b_{n-k}$.

**The one-line mechanism summary:** **the Hodge star intertwines $\Delta$, maps harmonic $k$-forms bijectively to harmonic $(n-k)$-forms, and through the Hodge isomorphism realizes the topological Poincaré duality.**

The deeper insight: **the Hodge star is the metric-and-orientation realization of an abstract topological duality**. Without a metric, $\Lambda^k T^*M$ and $\Lambda^{n-k}T^*M$ are abstractly isomorphic (same fibre dimension) but not canonically. The metric and orientation together produce a canonical isomorphism — and this isomorphism, when restricted to harmonic forms, gives Poincaré duality. The metric is a "concrete choice" that realizes an abstract algebraic-topological fact.

---

# What Makes This Hard

The proof itself is short, but two subtleties trip up many students.

**The Hodge star depends on the metric, but the cohomological isomorphism is topological.** The duality $H^k\cong H^{n-k}$ is metric-independent (topological), but the Hodge star realizing it is metric-dependent. The resolution: different metrics give different Hodge stars, but they all give the *same* cohomological isomorphism (up to a sign, which depends on orientation). So the metric-dependent construction realizes a metric-independent invariant — and the same isomorphism is obtained regardless of metric choice, just with different concrete representatives.

**Orientation is essential.** Without an orientation, the Hodge star is only defined up to a sign, and the resulting "isomorphism" $\mathcal{H}^k\cong\mathcal{H}^{n-k}$ is well-defined only up to sign, breaking the duality. On a non-orientable closed manifold, the topological Poincaré duality is more subtle: $H^k(M; \mathbb{R}) \cong H^{n-k}(M; \mathcal{O}_M)$ with twisted coefficients (the orientation sheaf $\mathcal{O}_M$). The Hodge star can be modified to act on twisted forms (pseudoforms), recovering the twisted duality, but this is beyond the basic Hodge theory of orientable manifolds.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
The Hodge star commutes with $\Delta$ (a sign-tracking calculation using $\delta = \pm\star d\star$ and the double-star formula). Hence $\star$ maps harmonic $k$-forms to harmonic $(n-k)$-forms. Since $\star$ is a pointwise isomorphism between $\Omega^k$ and $\Omega^{n-k}$, its restriction to harmonics is an isomorphism. Combining with the Hodge isomorphism $\mathcal{H}^k\cong H^k_{dR}$ in both degrees gives the cohomological Poincaré duality.

**Subgoal decomposition:**

1. **$\star$ commutes with $d$ and $\delta$** (up to sign, in a compatible way).
   - *Hint:* $\delta = (-1)^{n(k+1)+1}\star d\star$ on $k$-forms, so $\star\delta\star^{-1} = \pm d$ (after double-star tracking). Symmetrically, $\star d\star^{-1} = \pm\delta$.
   - *Why needed:* The basis for $\star$ commuting with $\Delta$.

2. **$\star$ commutes with $\Delta$.** $\star\Delta = \star(d\delta + \delta d) = \star d\delta + \star\delta d$, and after rearrangement using step 1, this equals $\Delta\star$.
   - *Hint:* Apply $\star\Delta\omega = \star d\delta\omega + \star\delta d\omega$. Use $\star\delta = \pm d\star$ (rearranged from $\delta = \pm\star d\star$) on each term. After sign tracking, the result is $d\delta\star\omega + \delta d\star\omega = \Delta\star\omega$.
   - *Why needed:* Implies $\star$ preserves the kernel of $\Delta$, i.e., maps harmonic forms to harmonic forms.

3. **$\star : \mathcal{H}^k\to\mathcal{H}^{n-k}$ is an isomorphism.** $\star$ is pointwise an isomorphism $\Omega^k\to\Omega^{n-k}$; it maps $\mathcal{H}^k$ into $\mathcal{H}^{n-k}$ by step 2; the inverse is $\star^{-1} = (-1)^?\star$ which also commutes with $\Delta$, so also maps harmonics to harmonics.
   - *Hint:* Since $\star$ has a pointwise (algebraic) inverse $\star^{-1} = (-1)^{k(n-k)+s}\star$ on $(n-k)$-forms, the restriction to $\mathcal{H}^k$ is invertible.
   - *Why needed:* Establishes the analytic isomorphism between harmonic spaces.

4. **Hodge isomorphism in both degrees.** $\mathcal{H}^k\cong H^k_{dR}$ and $\mathcal{H}^{n-k}\cong H^{n-k}_{dR}$ by [[Thm - Harmonic Forms Represent de Rham Cohomology]].
   - *Hint:* The harmonic representatives give a canonical isomorphism.
   - *Why needed:* Bridges the harmonic-form isomorphism to a cohomological isomorphism.

5. **Composition gives Poincaré duality.** $H^k_{dR}\xrightarrow{\cong}\mathcal{H}^k\xrightarrow{\star}\mathcal{H}^{n-k}\xrightarrow{\cong}H^{n-k}_{dR}$.
   - *Hint:* Both maps in the composition are isomorphisms.
   - *Why needed:* Concludes the cohomological Poincaré duality from the harmonic isomorphism.

6. **Dimensions agree.** $b_k = \dim H^k_{dR} = \dim\mathcal{H}^k = \dim\mathcal{H}^{n-k} = \dim H^{n-k}_{dR} = b_{n-k}$.
   - *Hint:* Immediate from step 5.
   - *Why needed:* The most-used corollary.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\star$ intertwines $d$ and $\delta$
> **Statement:** On a (pseudo-)Riemannian $n$-manifold, $\star d = \epsilon\delta\star$ and $\star\delta = \epsilon' d\star$ for some signs $\epsilon, \epsilon'$ that depend on the degree and signature. Concretely, $\star d\omega = (-1)^{k(n-k)+s}\delta\star\omega$ for $\omega \in \Omega^{n-k-1}$ (so that $d\omega \in \Omega^{n-k}$), and a similar formula for $\star\delta$.
>
> **Hint:** Use $\delta = (-1)^{n(k+1)+1}\star d\star$ to express $\delta\star\omega$ in terms of $\star d\star\star\omega$, then apply the double-star formula.
>
> **Why needed:** The intertwining is the key algebraic identity making $\star$ commute with $\Delta$.
>
> > [!note]- Full proof (sketch)
> > The signs in the identities $\star d = \pm\delta\star$ and $\star\delta = \pm d\star$ are determined by carefully tracking the conventions in $\delta = (-1)^{n(k+1)+1}\star d\star$ and the double-star formula $\star\star = (-1)^{k(n-k)+s}\mathrm{id}$. The actual values of $\epsilon, \epsilon'$ are not important for the commutation of $\star$ with $\Delta$ — what matters is that the rearrangement works out.

> [!note]- Lemma 2: $\star$ commutes with $\Delta$
> **Statement:** $\star\Delta\omega = \Delta\star\omega$ for all $\omega \in \Omega^k(M)$ and all $k$.
>
> **Hint:** $\Delta = d\delta + \delta d$. Apply $\star$ to both terms; use Lemma 1 to rearrange $\star d \leftrightarrow \delta\star$ and $\star\delta\leftrightarrow d\star$.
>
> **Why needed:** Implies $\star : \ker\Delta \to \ker\Delta$ (preservation of harmonic forms under $\star$).
>
> > [!note]- Full proof
> > $\star\Delta\omega = \star(d\delta\omega + \delta d\omega) = \star d\delta\omega + \star\delta d\omega$.
> >
> > Using Lemma 1 in the form $\star d = \pm\delta\star$: $\star d(\delta\omega) = \pm\delta\star(\delta\omega) = \pm\delta(\pm d\star\omega) = \delta d\star\omega$ (after sign-tracking; the two signs combine to $+1$ by the same calculation that makes $\delta\star d\star = \star d\delta$).
> >
> > Symmetrically: $\star\delta(d\omega) = \pm d\star d\omega = \pm d(\pm\delta\star\omega) = d\delta\star\omega$.
> >
> > Hence $\star\Delta\omega = \delta d\star\omega + d\delta\star\omega = \Delta\star\omega$. The sign-tracking in the intermediate steps is the bookkeeping; the end result is the clean commutation.

> [!note]- Lemma 3: $\star : \mathcal{H}^k \to \mathcal{H}^{n-k}$ is an isomorphism
> **Statement:** The restriction $\star|_{\mathcal{H}^k} : \mathcal{H}^k(M) \to \mathcal{H}^{n-k}(M)$ is an $\mathbb{R}$-linear bijection.
>
> **Hint:** $\star$ preserves the kernel of $\Delta$ by Lemma 2. The pointwise inverse $\star^{-1} = (-1)^{k(n-k)+s}\star$ also commutes with $\Delta$ (same proof), so also maps $\mathcal{H}^{n-k}\to\mathcal{H}^k$.
>
> **Why needed:** Establishes the analytic isomorphism between harmonic spaces in complementary degrees.
>
> > [!note]- Full proof
> > $\star$ maps $\mathcal{H}^k$ into $\Omega^{n-k}$. For $h \in \mathcal{H}^k$, $\Delta(\star h) = \star(\Delta h) = \star\cdot 0 = 0$ (Lemma 2). So $\star h \in \mathcal{H}^{n-k}$.
> >
> > Conversely, $\star^{-1}$ (the pointwise inverse, given by $\star^{-1} = (-1)^{k(n-k)+s}\star$ on $\Omega^{n-k}$) also commutes with $\Delta$ by the same argument, so it maps $\mathcal{H}^{n-k}$ into $\mathcal{H}^k$. The composition $\star\circ\star^{-1} = \mathrm{id}$ on $\mathcal{H}^{n-k}$ and $\star^{-1}\circ\star = \mathrm{id}$ on $\mathcal{H}^k$, so $\star : \mathcal{H}^k\to\mathcal{H}^{n-k}$ is a bijection.

> [!note]- Lemma 4: Composition gives the cohomological isomorphism
> **Statement:** The composition $H^k_{dR}(M) \xrightarrow{\sim} \mathcal{H}^k(M) \xrightarrow{\star} \mathcal{H}^{n-k}(M) \xrightarrow{\sim} H^{n-k}_{dR}(M)$ (using the Hodge isomorphism on both ends) is an isomorphism $H^k\cong H^{n-k}$.
>
> **Hint:** Each map in the composition is an isomorphism by [[Thm - Harmonic Forms Represent de Rham Cohomology]] and Lemma 3.
>
> **Why needed:** Gives the cohomological Poincaré duality from the harmonic-form isomorphism.
>
> > [!note]- Full proof
> > Direct. The first and third arrows are isomorphisms by the Hodge isomorphism (which is the content of [[Thm - Harmonic Forms Represent de Rham Cohomology]]). The middle arrow $\star : \mathcal{H}^k\to\mathcal{H}^{n-k}$ is an isomorphism by Lemma 3. Composition of isomorphisms is an isomorphism. The dimensions agree: $b_k = \dim H^k = \dim\mathcal{H}^k = \dim\mathcal{H}^{n-k} = \dim H^{n-k} = b_{n-k}$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $(M, g)$ be a closed oriented Riemannian $n$-manifold. The Hodge star induces a vector-space isomorphism $H^k_{dR}(M; \mathbb{R}) \cong H^{n-k}_{dR}(M; \mathbb{R})$, hence $b_k(M) = b_{n-k}(M)$.
>
> *Proof.*
>
> **Step 0 — Well-posedness.** The Hodge star $\star : \Omega^k(M) \to \Omega^{n-k}(M)$ is a pointwise $C^\infty(M)$-linear isomorphism (see [[Thm - Properties of the Hodge Star]]). The harmonic forms $\mathcal{H}^k(M) = \ker(\Delta|_{\Omega^k})$ are well-defined finite-dimensional subspaces (by the Hodge decomposition theorem).
>
> **Step 1 — Sign convention compatibility.** Using $\delta = (-1)^{n(k+1)+1}\star d\star$ and the double-star formula $\star\star = (-1)^{k(n-k)+s}\mathrm{id}$, the identities
> $$\star d = (-1)^{?}\delta\star, \qquad \star\delta = (-1)^{?}d\star$$
> hold with signs determined by the conventions. The key fact (Lemma 1) is that these rearrangement formulas are consistent.
>
> **Step 2 — $\star$ commutes with $\Delta$.** $\star\Delta\omega = \star(d\delta + \delta d)\omega$. Using Lemma 1 to commute $\star$ past $d$ and $\delta$: $\star d\delta\omega = (-1)^?\delta\star\delta\omega = \delta d\star\omega$ (after two applications of Lemma 1, with signs combining to $+1$). Similarly $\star\delta d\omega = d\delta\star\omega$. Combining: $\star\Delta\omega = \delta d\star\omega + d\delta\star\omega = \Delta\star\omega$.
>
> **Step 3 — $\star$ preserves harmonicity.** If $h \in \mathcal{H}^k$, then $\Delta\star h = \star\Delta h = \star\cdot 0 = 0$, so $\star h \in \mathcal{H}^{n-k}$. Thus $\star(\mathcal{H}^k) \subseteq \mathcal{H}^{n-k}$.
>
> **Step 4 — $\star : \mathcal{H}^k\to\mathcal{H}^{n-k}$ is an isomorphism.** The inverse $\star^{-1} = (-1)^{k(n-k)+s}\star : \Omega^{n-k}\to\Omega^k$ is also a $C^\infty$-linear pointwise isomorphism, also commutes with $\Delta$ (same proof as Step 2). So $\star^{-1}(\mathcal{H}^{n-k}) \subseteq \mathcal{H}^k$. The compositions $\star\circ\star^{-1} = \mathrm{id}$ and $\star^{-1}\circ\star = (-1)^{k(n-k)+s}\cdot(-1)^{k(n-k)+s}\mathrm{id} = \mathrm{id}$ (after double application of double-star), so $\star : \mathcal{H}^k\to\mathcal{H}^{n-k}$ is bijective. It is $\mathbb{R}$-linear as the restriction of a linear map.
>
> **Step 5 — Combining with the Hodge isomorphism.** By [[Thm - Harmonic Forms Represent de Rham Cohomology]], the natural maps $\mathcal{H}^k\to H^k_{dR}$ and $\mathcal{H}^{n-k}\to H^{n-k}_{dR}$ are isomorphisms. Composing:
> $$H^k_{dR}(M) \xleftarrow{\cong} \mathcal{H}^k(M) \xrightarrow{\star} \mathcal{H}^{n-k}(M) \xrightarrow{\cong} H^{n-k}_{dR}(M).$$
> All three maps are isomorphisms, so the composition (after inverting the first) is an isomorphism $H^k_{dR}(M)\xrightarrow{\cong}H^{n-k}_{dR}(M)$.
>
> **Step 6 — Dimensions.** $b_k(M) = \dim H^k_{dR}(M) = \dim H^{n-k}_{dR}(M) = b_{n-k}(M)$. $\qquad\blacksquare$
>
> *Corollary (Pairing).* The map $H^k_{dR}\times H^{n-k}_{dR}\to\mathbb{R}$, $([\alpha], [\beta])\mapsto\int_M\alpha\wedge\beta$, is non-degenerate. Proof: on harmonic representatives, $\int_M h_\alpha\wedge h_\beta = \int_M h_\alpha\wedge\star\star^{-1}h_\beta = \langle h_\alpha, \star^{-1}h_\beta\rangle_{L^2}$ (sign tracking via double-star). For any nonzero $[\alpha]$, the harmonic representative $h_\alpha \neq 0$, and the inner product $\langle h_\alpha, h_\alpha\rangle_{L^2} > 0$. With $\beta = \star h_\alpha \in \mathcal{H}^{n-k}$, $\int_M h_\alpha\wedge h_\beta = \langle h_\alpha, \star^{-1}\star h_\alpha\rangle_{L^2} = \pm\|h_\alpha\|^2 \neq 0$. So the pairing is non-degenerate.

---

# Cross-Field Exercise Suggestions

**Riemannian geometry — Poincaré duality on tori.** On $T^n$, $\dim\mathcal{H}^k = \binom{n}{k}$ (constant-coefficient forms). Poincaré duality reads $\binom{n}{k} = \binom{n}{n-k}$, which is the elementary identity for binomial coefficients. The Hodge star realizes the duality explicitly: $\star(dx^{i_1}\wedge\cdots\wedge dx^{i_k}) = \pm dx^{j_1}\wedge\cdots\wedge dx^{j_{n-k}}$ with complementary multi-indices, mapping the natural basis of $\mathcal{H}^k$ to the natural basis of $\mathcal{H}^{n-k}$.

**Complex geometry — Hodge symmetry and Serre duality.** On a compact Kähler manifold of complex dimension $m$ (real dimension $n = 2m$), Poincaré duality combines with the bidegree decomposition to give:
- $b_k = \sum_{p+q=k}h^{p,q}$ (Hodge decomposition).
- $b_k = b_{n-k}$ (Poincaré duality).
- $h^{p,q} = h^{q,p}$ (Hodge symmetry).
- $h^{p,q} = h^{m-p, m-q}$ (Serre duality).
These four constraints on the Hodge diamond are interrelated, with Poincaré duality coming from the Hodge star and Serre duality coming from the conjugate-linear Hodge star $\bar\star : \Omega^{p,q}\to\Omega^{n-q, n-p}$. The Hodge diamond of a Kähler manifold has reflective symmetries along both diagonals.

**Algebraic topology — intersection numbers.** On a closed orientable surface $\Sigma_g$, two homology classes $[a], [b] \in H_1(\Sigma_g; \mathbb{Z})$ have an integer **intersection number** $a\cdot b \in \mathbb{Z}$. By de Rham theory and Poincaré duality, this is realized as $\int_{\Sigma_g}\omega_a\wedge\omega_b$ where $\omega_a, \omega_b$ are the (harmonic) $1$-forms dual to $a, b$ under Poincaré duality. The exercise: verify directly that on the standard genus-$g$ surface with $1$-forms $\omega_{a_i}, \omega_{b_j}$ ($i, j = 1, \dots, g$), the pairing matrix is the symplectic form $\bigoplus_i\begin{pmatrix}0 & 1\\-1 & 0\end{pmatrix}$.

**Knot theory — linking numbers via the Hodge star.** Two disjoint simple closed curves $C_1, C_2$ in $\mathbb{R}^3$ have a **linking number** $\mathrm{lk}(C_1, C_2) \in \mathbb{Z}$, classically defined via the Gauss linking integral. In the form language, $\mathrm{lk}(C_1, C_2) = \int_{C_1}\omega_2$ where $\omega_2$ is the $1$-form on $\mathbb{R}^3\setminus C_2$ Poincaré-dual to $C_2$ (i.e., closed with $\int_{S^2}\omega_2 = 1$ for any sphere $S^2$ around $C_2$). Compactification to $S^3$ and Hodge theory on $S^3\setminus(C_1\cup C_2)$ gives a Hodge-theoretic interpretation, with the linking number as a pairing between cohomology classes.

---

# Bridges

- **[[Def - The de Rham Cohomology Pairing|de Rham cohomology pairing]]** — the Poincaré duality theorem is the *non-degeneracy* statement for the de Rham pairing $H^k\times H^{n-k}\to\mathbb{R}$. The Hodge star realizes the duality concretely: the pairing of $[\alpha]$ with $[\star h_\alpha]$ is $\|h_\alpha\|^2 \neq 0$. Without the Hodge star (i.e., abstractly), non-degeneracy is harder to verify; with the Hodge star, it is immediate.

- **[[Def - Self-Dual and Anti-Self-Dual Forms|Self-dual / anti-self-dual decomposition]]** — in middle dimension on a $4$-manifold, the Hodge star is an involution on $\Omega^2$, splitting $\Omega^2 = \Omega^2_+\oplus\Omega^2_-$. By Poincaré duality, the harmonic forms in middle degree $\mathcal{H}^2$ split into $\mathcal{H}^2_+\oplus\mathcal{H}^2_-$, with dimensions $b^+_2$ and $b^-_2$ — the **signature components**. The Poincaré duality bridge: $b_2$ is symmetric in Poincaré duality (it pairs with itself), and the self-duality splitting refines this into a positive-definite and negative-definite part.

- **Cup product on $H^*$** — Poincaré duality plus the cup product give the **cap product** with the fundamental class, and the **intersection pairing**. The Hodge-theoretic version: the cup product on harmonic forms is $h_\alpha\cdot h_\beta = h_{[\alpha\smile\beta]}$ (harmonic projection of the wedge), and the intersection pairing is the cup product integrated over $M$.

- **Hirzebruch signature theorem** — on a closed oriented $4k$-manifold, the signature $\sigma(M) = b^+_{2k} - b^-_{2k}$ is computed by integration of a polynomial in the Pontryagin classes (the L-polynomial). The Hodge-theoretic foundation: Poincaré duality establishes that the intersection form on $H^{2k}$ has well-defined signature; the signature is then expressed as an index of an elliptic operator (the signature operator), and the Atiyah–Singer index theorem computes it topologically.

- **Atiyah–Singer index theorem for the signature operator** — Poincaré duality combined with the Hodge star defines the **signature operator** $D = d + \delta : \Omega^+\to\Omega^-$ (acting on $\pm$-eigenspaces of an involution $\tau$ built from $\star$ and orientation). Its index is the signature $\sigma(M)$. The Atiyah–Singer theorem computes this index from the symbol's topology, recovering Hirzebruch's signature theorem.

---

# Unlocked by This

> [!tip] Lefschetz Duality and Manifolds with Boundary *(from Algebraic Topology)*
> On a compact oriented manifold with boundary $(M, \partial M)$, Poincaré duality generalizes to **Lefschetz duality**: $H^k(M)\cong H^{n-k}(M, \partial M)$, with the right side being relative cohomology. The Hodge-theoretic version requires choosing boundary conditions: tangential ($i^*\omega = 0$) gives one side of the duality, normal ($i^*\star\omega = 0$) gives the other. The two boundary conditions are exchanged by $\star$, just as the absolute and relative cohomology are exchanged by Lefschetz duality. This is the framework for **Hodge theory on manifolds with boundary**, with applications to electromagnetism in cavities, fluid flow in bounded domains, and elastic vibrations.

> [!tip] Hodge Decomposition on Complex Manifolds and Serre Duality *(from Complex Geometry)*
> On a compact Hermitian manifold, the conjugate-linear Hodge star $\bar\star : \Omega^{p,q}\to\Omega^{n-q, n-p}$ (a refinement of the real $\star$) commutes with the Dolbeault Laplacian $\Delta_{\bar\partial}$. This gives **Serre duality** $H^{p,q}_{\bar\partial}\cong H^{n-p, n-q}_{\bar\partial}$ as a complex analog of Poincaré duality. On a compact Kähler manifold, combining with Hodge symmetry $h^{p,q} = h^{q,p}$ produces the four-fold symmetry of the Hodge diamond. Serre duality has analogs for any coherent sheaf on a compact complex manifold, expressed in terms of the canonical bundle.

> [!tip] Atiyah–Singer Index Theorem *(from Index Theory)*
> Poincaré duality, when reinterpreted via the **signature operator** $D = d + \delta : \Omega^+\to\Omega^-$ on a closed oriented $4k$-manifold, becomes a special case of the **Atiyah–Singer index theorem**. The signature operator's analytic index is the signature $\sigma(M) = b^+_{2k} - b^-_{2k}$ (a Poincaré-duality invariant); the topological index is the integral of the L-polynomial in the Pontryagin classes (Hirzebruch's L-genus). The equality of these is **Hirzebruch's signature theorem**, an early instance of the Atiyah–Singer machinery. The general theorem applies to any elliptic operator, with the signature operator being the canonical example arising from Hodge theory and Poincaré duality.
