---
type: theorem
subject: hodge-theory
prereqs:
  - "Def - The Hodge Star Operator"
  - "Def - Riemannian Volume Form"
  - "Def - Orientation of a Smooth Manifold"
tags: [geometry, hodge-theory, differential-forms]
---

# Notation

$(M, g)$ is a smooth oriented (pseudo-)Riemannian $n$-manifold, signature $(n - s, s)$. The Hodge star is $\star : \Omega^k(M) \to \Omega^{n-k}(M)$; the volume form is $\operatorname{vol}_n$; the pointwise inner product on $k$-forms is $\langle\cdot,\cdot\rangle_g$. An orthonormal coframe is $(\sigma^1, \dots, \sigma^n)$ with $g(\sigma^i, \sigma^j) = \epsilon_i\delta^{ij}$, $\epsilon_i = \pm 1$ by signature. For a multi-index $I = (i_1 < \cdots < i_k)$, $\sigma^I = \sigma^{i_1}\wedge\cdots\wedge\sigma^{i_k}$. Full notation in [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

---

# Statement

> **Theorem (Properties of the Hodge Star).** Let $(M, g)$ be a smooth oriented (pseudo-)Riemannian $n$-manifold of signature $(n - s, s)$. The Hodge star $\star : \Omega^k(M) \to \Omega^{n-k}(M)$ satisfies:
> 1. **Pointwise $C^\infty(M)$-linearity**: $\star(f\omega) = f\star\omega$ for $f \in C^\infty(M)$ and $\omega \in \Omega^k(M)$.
> 2. **Double star**: $\star\star = (-1)^{k(n-k) + s}\,\mathrm{id}_{\Omega^k(M)}$.
> 3. **Isometry up to sign**: $\langle\star\alpha, \star\beta\rangle_g = (-1)^s\langle\alpha, \beta\rangle_g$ for $\alpha, \beta \in \Omega^k(M)$.
> 4. **On constants and the volume form**: $\star 1 = \operatorname{vol}_n$ and $\star\operatorname{vol}_n = (-1)^s$.
> 5. **Coordinate formula on orthonormal coframes**: $\star\sigma^I = \mathrm{sgn}(I, I^c)\,\epsilon_I\,\sigma^{I^c}$, where $I^c$ is the complementary multi-index in increasing order, $\mathrm{sgn}(I, I^c)$ is the sign of the permutation $(1, \dots, n) \mapsto (i_1, \dots, i_k, j_1, \dots, j_{n-k})$, and $\epsilon_I = \prod_{i \in I}\epsilon_i$.
> 6. **In Euclidean $\mathbb{R}^3$**: $\star dx = dy\wedge dz$, $\star dy = dz \wedge dx$, $\star dz = dx \wedge dy$, $\star(dy\wedge dz) = dx$, $\star(dz\wedge dx) = dy$, $\star(dx\wedge dy) = dz$, $\star(dx\wedge dy\wedge dz) = 1$, $\star 1 = dx \wedge dy \wedge dz$ — all signs positive. The cross product is recovered as $u \times v = (\star(u^\flat\wedge v^\flat))^\sharp$.

---

# Motivation

The Hodge star is defined abstractly via the identity $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle\operatorname{vol}_n$, which is conceptually clean but provides no immediate computational handle. The theorem collects the working properties of $\star$ — how to compute it on basis forms, how it interacts with itself, how it behaves under coordinate changes — so that all subsequent manipulations of $\star$ in proofs and exercises proceed mechanically.

The properties are all algebraic — none involves derivatives. So $\star$ is *purely algebraic*: it acts pointwise on the multilinear-algebra fibres $\Lambda^k T_p^*M$, using only the metric and the orientation at each point. This is in sharp contrast to the exterior derivative $d$ and the [[Def - The Codifferential|codifferential]] $\delta$, both of which are differential operators. The pointwise nature of $\star$ is what makes it amenable to direct computation and why the formulas below are simple.

The most-used property is the **double-star formula**, $\star\star = (-1)^{k(n-k)+s}\mathrm{id}$. It is the single algebraic identity that determines whether $\star$ behaves as an involution (eigenvalues $\pm 1$, as in Riemannian $4$D on $2$-forms), or as a *complex* structure (eigenvalues $\pm i$, as in Lorentzian $4$D on $2$-forms), or in between. The sign determines the geometric structure that emerges in various [[Def - Dimension|dimensions]] and signatures — and the entire theory of self-duality on $4$-manifolds hangs on $\star\star = +1$ in Riemannian $4$D.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is bare: an oriented (pseudo-)Riemannian manifold with the Hodge star defined. Each of the following is a property $B$ from which the theorem's properties are extracted in practice.

The most common source is **an orthonormal coframe being available**. Property $B$: the manifold has a local orthonormal coframe $(\sigma^1, \dots, \sigma^n)$, which is automatic on any (pseudo-)Riemannian manifold by Gram–Schmidt applied to a coordinate basis. The bridge is that the coordinate formula $\star\sigma^I = \pm\sigma^{I^c}$ on an orthonormal coframe lets us compute $\star\omega$ for any form $\omega$ by writing $\omega$ in the orthonormal basis and applying $\star$ termwise. The implication is non-obvious only because beginners forget that orthonormal coframes always exist; once you have one, all the formulas of the theorem become explicit. Example: on the round $S^2$ with the metric in spherical coordinates, the orthonormal coframe is $\sigma^1 = d\theta$, $\sigma^2 = \sin\theta\,d\varphi$, and $\star\sigma^1 = \sigma^2$, $\star\sigma^2 = -\sigma^1$ (with orientation $\sigma^1\wedge\sigma^2 = \operatorname{vol}_{S^2}$), giving immediately $\star d\theta = \sin\theta\,d\varphi$, $\star(\sin\theta\,d\varphi) = -d\theta$, etc.

A second source is **a chain of operations $\star A \star$ for some operator $A$**. Property $B$: a formula involving $\star A\star$ for some intermediate operator $A$ — typically $A = d$ giving $\star d\star = \pm\delta$, or $A = d^*$ giving $\star d^*\star = \pm d$. The bridge is the double-star formula: $\star\star = (-1)^{k(n-k)+s}$, which lets us collapse $\star\star$ wherever it appears. The implication is non-obvious because the sign depends on degree and signature, but mechanical to track. Example: $\delta = (-1)^{n(k+1)+1}\star d\star$ on $k$-forms in Riemannian signature — the derivation goes through computing the sign of the implicit $\star\star$ to undo.

A third source is **a Euclidean / Cartesian setting in low dimensions**. Property $B$: the manifold is $\mathbb{R}^n$ (or an open subset) with the standard Euclidean metric, in Cartesian coordinates. The bridge is property 6 in the theorem statement, which gives explicit formulas for $\star$ on every basis form. The implication is non-obvious only because there are many formulas to memorize; in practice one re-derives them as needed from the defining identity. The Euclidean $\mathbb{R}^3$ case is essential because it provides the bridge between Hodge theory and classical vector calculus (cross product, curl, divergence).

A fourth source is **a closed orientable surface ($n = 2$)**. Property $B$: $M$ is a $2$-dimensional Riemannian manifold (e.g., a Riemann surface). The bridge is that $\star$ on $1$-forms in $2$D is an isometry (and $\star\star = -1$ on $1$-forms in $2$D Riemannian since $k(n - k) = 1$ is odd), so $\star$ is a *complex structure* on $\Omega^1(M)$. The implication is non-obvious because the complex structure is hidden inside the Hodge star — but it is the structural reason that $2$-dimensional Riemannian geometry has an intimate connection with complex analysis (every Riemann surface is naturally a complex manifold via its Hodge star).

**Targets (Output Amplification)**

The conclusion of the theorem is a *toolkit* of algebraic identities for $\star$. Each combination with additional structure produces a useful result.

The most powerful combination is **$\star\star = +1$ plus middle dimension forces involution structure**. Take the double-star formula at $k = n/2$, $n = 2k$, Riemannian: $\star\star = (-1)^{k^2} = (-1)^k$, which is $+1$ when $k$ is even. Add the property $D$: $\star$ is self-adjoint with respect to the pointwise inner product. Then $\star$ is a self-adjoint involution on $\Omega^k$, giving an orthogonal eigenspace decomposition $\Omega^k = \Omega^k_+ \oplus \Omega^k_-$ into $\pm 1$ eigenspaces. The result $E$ is the **self-dual / anti-self-dual decomposition** in middle dimension, with $k$ even and $n = 2k$ — most famously $k = 2$, $n = 4$, the four-manifold case. This is non-obvious because it requires both the dimensional matching ($k$ even) and the self-adjointness of $\star$.

A second combination is **$\star$ commutes with $\Delta$ plus harmonic forms exist forces a Poincaré duality between cohomology in complementary degrees**. The bridge $\star\Delta = \Delta\star$ (from properties of $\star$ and the construction of $\Delta$) maps harmonic $k$-forms bijectively to harmonic $(n - k)$-forms. Combined with the Hodge isomorphism $\mathcal{H}^k \cong H^k_{dR}$, this gives $H^k_{dR} \cong H^{n-k}_{dR}$ — **Poincaré duality**. The combination is non-obvious because it requires both the algebraic fact ($\star$ commutes with $\Delta$) and the analytic fact (harmonic forms represent cohomology); together they produce a topological isomorphism.

A third combination is **$\star\sigma^I = \pm\sigma^{I^c}$ plus orthonormal frame gives explicit computation**. The coordinate formula on an orthonormal coframe combined with the existence of orthonormal coframes (by Gram–Schmidt) gives an explicit computational procedure for $\star$ on any form. The result is the algorithm: write the form in the orthonormal basis, apply $\star$ termwise via the complementary multi-index. This is non-obvious because the abstract definition of $\star$ is non-constructive; the orthonormal-frame formula makes it explicit. Used in essentially every coordinate computation in the chapter.

A fourth combination is **the cross-product / curl on $\mathbb{R}^3$**. The Euclidean $\mathbb{R}^3$ formulas $\star(dx \wedge dy) = dz$ etc. combined with the definitions of grad, curl, div on vector fields give the identities $\nabla\times \vec F = (\star d F^\flat)^\sharp$ and $\nabla\cdot\vec F = -\delta F^\flat$ (where $F^\flat$ is the $1$-form dual of $\vec F$). The result is that classical vector calculus on $\mathbb{R}^3$ is *literally* the form-calculus calculations in disguise, and identities like $\nabla\times(\nabla f) = 0$ and $\nabla\cdot(\nabla\times\vec F) = 0$ are just $d^2 = 0$ in different degrees.

---

# Why Is It True

The Hodge star is, structurally, the *isomorphism between $\Lambda^k V^*$ and $\Lambda^{n-k}V^*$ induced by the metric and the volume form*. **All the properties of $\star$ derive from this single structural fact, applied at each point.**

Why does the isomorphism exist? Because $\dim\Lambda^k V^* = \binom{n}{k} = \binom{n}{n-k} = \dim\Lambda^{n-k}V^*$. The two spaces are abstractly isomorphic, but the isomorphism requires extra data — the metric and the volume form — to be canonical. Both pieces are needed: the metric to identify $\Lambda^k V^*$ with $(\Lambda^k V^*)^*$ via the pointwise inner product; the volume form to identify $(\Lambda^k V^*)^*$ with $\Lambda^{n-k} V^*$ via the wedge pairing.

Concretely, on an orthonormal coframe $(\sigma^1, \dots, \sigma^n)$, the basis $\{\sigma^I\}_{|I|=k}$ for $\Lambda^k$ and the basis $\{\sigma^J\}_{|J|=n-k}$ for $\Lambda^{n-k}$ are both orthonormal. The natural isomorphism sends $\sigma^I$ to $\pm\sigma^{I^c}$ — to the complementary multi-index, with a sign determined by orientation. This is exactly the Hodge star formula.

**Why the double-star sign $(-1)^{k(n-k)+s}$?** Compute on a basis: $\star\star\sigma^I = \star(\mathrm{sgn}(I, I^c)\epsilon_I\sigma^{I^c}) = \mathrm{sgn}(I, I^c)\mathrm{sgn}(I^c, I)\epsilon_I\epsilon_{I^c}\sigma^I$. Now $\mathrm{sgn}(I, I^c)\cdot\mathrm{sgn}(I^c, I) =$ sign of the permutation taking $(1, \dots, n)$ to $(i_1, \dots, i_k, j_1, \dots, j_{n-k})$ times the sign taking it to $(j_1, \dots, j_{n-k}, i_1, \dots, i_k)$. These two permutations differ by a "rearrangement" of two blocks of sizes $k$ and $n - k$, which has sign $(-1)^{k(n-k)}$. So the combined product is $(-1)^{k(n-k)}$. And $\epsilon_I\epsilon_{I^c} = \prod_{i \in \{1,\dots,n\}}\epsilon_i = (-1)^s$ (the product over all indices is $(-1)^s$ by signature). Total: $\star\star\sigma^I = (-1)^{k(n-k)+s}\sigma^I$.

**Why $\star 1 = \operatorname{vol}_n$?** Direct from the defining identity with $\alpha = \beta = 1$: $1 \wedge \star 1 = \langle 1, 1\rangle\operatorname{vol}_n = \operatorname{vol}_n$. Since $1 \wedge \omega = \omega$, this gives $\star 1 = \operatorname{vol}_n$. **Why $\star\operatorname{vol}_n = (-1)^s$?** From the double-star formula at $k = n$: $\star\star 1 = (-1)^{n\cdot 0 + s}\cdot 1 = (-1)^s$, so $\star\operatorname{vol}_n = (-1)^s$.

**Why $\langle\star\alpha,\star\beta\rangle = (-1)^s\langle\alpha,\beta\rangle$?** Apply $\star$ to both sides of $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle\operatorname{vol}_n$ and use the double-star formula plus graded commutativity of wedge. This is a straightforward computation but the simplest path is to verify on basis forms: $\langle\star\sigma^I, \star\sigma^J\rangle = \langle\pm\sigma^{I^c}, \pm\sigma^{J^c}\rangle = \delta_{IJ}\cdot\epsilon_{I^c}\cdot(\text{sign squared}) = \epsilon_{I^c}\delta_{IJ}$, while $\langle\sigma^I, \sigma^J\rangle = \epsilon_I\delta_{IJ}$. The ratio is $\epsilon_{I^c}/\epsilon_I = \prod_i\epsilon_i = (-1)^s$.

**The one-line mechanism summary:** **the Hodge star is the metric-and-orientation-induced isomorphism between $\Lambda^k$ and $\Lambda^{n-k}$, and every property of $\star$ is a direct algebraic consequence of this isomorphism applied on an orthonormal coframe.**

---

# What Makes This Hard

The proofs are all explicit computations; nothing is conceptually difficult. The error mode is **sign tracking**. Three signs are interleaved: the orientation sign $\mathrm{sgn}(I, I^c)$, the signature sign $\epsilon_I$, and the rearrangement sign $(-1)^{k(n-k)}$ from swapping blocks in $\star\star$. When all three are correctly tracked, the formulas fall out; when one is missed, the resulting "theorem" is wrong by a sign and breaks downstream proofs (especially the codifferential and Hodge decomposition).

The most common error: **forgetting the $\epsilon_I$ factor in pseudo-Riemannian signature**. In Riemannian signature ($s = 0$), $\epsilon_i = 1$ for all $i$, so $\epsilon_I = 1$ and the formula simplifies to $\star\sigma^I = \mathrm{sgn}(I, I^c)\sigma^{I^c}$. In Lorentzian signature, $\epsilon_0 = -1$ (timelike) and $\epsilon_i = +1$ for spatial $i$, so $\epsilon_I$ depends on whether the multi-index $I$ includes the time index $0$. This is the source of many physics sign errors in electromagnetic field calculations.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
All properties are algebraic identities on the fibres $\Lambda^k T_p^*M$. Verify each property pointwise on a chosen orthonormal coframe, and extend by $C^\infty(M)$-linearity to all of $\Omega^k(M)$. The double-star formula is the key algebraic identity; everything else follows from it and the defining identity $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle\operatorname{vol}_n$.

**Subgoal decomposition:**

1. **$C^\infty(M)$-linearity** (property 1).
   - *Hint*: The defining identity $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle\operatorname{vol}_n$ is $C^\infty$-linear in $\beta$ (both sides are), so $\star$ is $C^\infty$-linear.
   - *Why needed*: To extend pointwise identities to global ones.

2. **Coordinate formula on orthonormal coframes** (property 5).
   - *Hint*: Use the defining identity with $\alpha = \sigma^I$, $\beta = \sigma^J$: $\sigma^I\wedge\star\sigma^J = \delta_{IJ}\epsilon_I\operatorname{vol}_n$. Match the coefficient of each basis element of $\Lambda^{n-k}$ in $\star\sigma^J$.
   - *Why needed*: Gives an explicit formula for $\star$ on basis forms, from which all other properties can be verified.

3. **Double-star formula** (property 2).
   - *Hint*: Apply the formula from step 2 twice. Track three signs: the orientation $\mathrm{sgn}(I, I^c)$ (twice), the signature $\epsilon_I$, and the rearrangement.
   - *Why needed*: The most-used algebraic identity; enables collapsing chains of $\star$ operators.

4. **On constants and the volume form** (property 4).
   - *Hint*: $\star 1$ is determined by $1\wedge\star 1 = 1\cdot\operatorname{vol}_n$. $\star\operatorname{vol}_n$ follows from the double-star formula at $k = 0$.
   - *Why needed*: Boundary cases that anchor the inductive verification on basis forms.

5. **Isometry up to sign** (property 3).
   - *Hint*: Verify on basis forms using step 2.
   - *Why needed*: Lets $\star$ be used in $L^2$-orthogonality arguments.

6. **Euclidean $\mathbb{R}^3$ formulas** (property 6).
   - *Hint*: Apply step 2 with $n = 3$, all $\epsilon_i = +1$, orientation $dx\wedge dy\wedge dz$. For example, $\star dx$ should be the unique $2$-form with $dx \wedge \star dx = \operatorname{vol}_3 = dx\wedge dy\wedge dz$, giving $\star dx = dy\wedge dz$.
   - *Why needed*: Bridges Hodge theory to classical vector calculus, the most physically familiar setting.

---

# Lemma Decomposition

> [!note]- Lemma 1: The defining identity uniquely determines $\star$
> **Statement:** Given the data $(g, \operatorname{vol}_n)$, the operator $\star : \Omega^k(M) \to \Omega^{n-k}(M)$ is uniquely determined by the identity $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle_g\operatorname{vol}_n$ for all $\alpha, \beta \in \Omega^k(M)$.
>
> **Hint:** The wedge product $\Lambda^k\otimes\Lambda^{n-k}\to\Lambda^n$ is a perfect pairing of one-dimensional spaces (over the function [[Def - Ring|ring]] $C^\infty(M)$), so any $\gamma \in \Lambda^{n-k}$ is determined by the function $\alpha \mapsto \alpha\wedge\gamma/\operatorname{vol}_n$.
>
> **Why needed:** Establishes that the abstract definition unambiguously specifies a single operator; subsequent properties just compute this operator on basis forms.
>
> > [!note]- Full proof
> > Suppose two operators $\star_1, \star_2$ both satisfy the defining identity. Then $\alpha\wedge\star_1\beta = \alpha\wedge\star_2\beta$ for all $\alpha$, hence $\alpha\wedge(\star_1\beta - \star_2\beta) = 0$ for all $\alpha$. The wedge product $\Lambda^k\otimes\Lambda^{n-k}\to\Lambda^n$ is a perfect pairing (pointwise, between two spaces of equal dimension $\binom{n}{k}$, with the bilinear form being a top-degree wedge, and non-degeneracy following from $\sigma^I\wedge\sigma^{I^c} = \pm\operatorname{vol}_n \neq 0$ for any multi-index $I$). Perfect pairings have trivial null space, so $\star_1\beta = \star_2\beta$. Pointwise uniqueness extends to smooth uniqueness.

> [!note]- Lemma 2: Coordinate formula on orthonormal coframes
> **Statement:** On a positively oriented orthonormal coframe $(\sigma^1, \dots, \sigma^n)$ with $g(\sigma^i, \sigma^j) = \epsilon_i\delta^{ij}$, $\star\sigma^I = \mathrm{sgn}(I, I^c)\,\epsilon_I\,\sigma^{I^c}$ for every increasing multi-index $I$.
>
> **Hint:** Test the defining identity with $\alpha = \sigma^I$: $\sigma^I\wedge\star\sigma^I = \langle\sigma^I, \sigma^I\rangle\operatorname{vol}_n = \epsilon_I\operatorname{vol}_n$.
>
> **Why needed:** This formula is the workhorse — every concrete computation of $\star$ uses it.
>
> > [!note]- Full proof
> > Write $\star\sigma^I = \sum'_J c_{IJ}\sigma^J$ for unknown coefficients $c_{IJ}$ (sum over increasing $J$ of degree $n - k$). The defining identity with $\alpha = \sigma^I$ gives $\sigma^I\wedge\sum'_J c_{IJ}\sigma^J = \epsilon_I\operatorname{vol}_n$. The wedge $\sigma^I\wedge\sigma^J$ is zero unless $J = I^c$ (the complementary multi-index), in which case $\sigma^I\wedge\sigma^{I^c} = \mathrm{sgn}(I, I^c)\operatorname{vol}_n$. So only the $J = I^c$ term survives: $c_{I, I^c}\mathrm{sgn}(I, I^c)\operatorname{vol}_n = \epsilon_I\operatorname{vol}_n$, giving $c_{I, I^c} = \epsilon_I/\mathrm{sgn}(I, I^c) = \epsilon_I\cdot\mathrm{sgn}(I, I^c)$ (since $\mathrm{sgn}(I, I^c) = \pm 1$).
> >
> > For $J \neq I^c$, taking $\alpha = \sigma^K$ with $K = \{1,\dots,n\}\setminus J$ (complement of $J$) gives $\sigma^K\wedge\star\sigma^I = \langle\sigma^K, \sigma^I\rangle\operatorname{vol}_n = 0$ (since $K \neq I$ as multi-indices). Expanding, $\sigma^K\wedge c_{IK^c}\sigma^{K^c} \neq 0$ would force $c_{IK^c} = 0$. So all off-complementary coefficients vanish, confirming $\star\sigma^I = \mathrm{sgn}(I, I^c)\epsilon_I\sigma^{I^c}$.

> [!note]- Lemma 3: Double-star formula
> **Statement:** $\star\star\sigma^I = (-1)^{k(n-k)+s}\sigma^I$ on $k$-forms, for any multi-index $I$ of length $k$.
>
> **Hint:** Apply Lemma 2 twice. The signs to track: $\mathrm{sgn}(I, I^c)$, $\mathrm{sgn}(I^c, I)$, $\epsilon_I$, $\epsilon_{I^c}$. Use $\mathrm{sgn}(I, I^c)\cdot\mathrm{sgn}(I^c, I) = (-1)^{k(n-k)}$ (rearrangement of blocks of sizes $k$ and $n-k$) and $\epsilon_I\epsilon_{I^c} = \epsilon_{\{1,\dots,n\}} = (-1)^s$ (product over all indices, equal to the determinant of the metric, $(-1)^s$ by signature).
>
> **Why needed:** The most-used algebraic identity; controls signs in every Hodge calculation.
>
> > [!note]- Full proof
> > $\star\sigma^I = \mathrm{sgn}(I, I^c)\epsilon_I\sigma^{I^c}$ by Lemma 2. Now $\sigma^{I^c}$ is itself a basis form indexed by $I^c$ of degree $n - k$, so applying Lemma 2 again:
> > $$\star\sigma^{I^c} = \mathrm{sgn}(I^c, (I^c)^c)\epsilon_{I^c}\sigma^{(I^c)^c} = \mathrm{sgn}(I^c, I)\epsilon_{I^c}\sigma^I,$$
> > where $(I^c)^c = I$. Combining,
> > $$\star\star\sigma^I = \mathrm{sgn}(I, I^c)\epsilon_I\cdot\mathrm{sgn}(I^c, I)\epsilon_{I^c}\sigma^I = \mathrm{sgn}(I, I^c)\mathrm{sgn}(I^c, I)\epsilon_I\epsilon_{I^c}\sigma^I.$$
> > Compute the signs: $\mathrm{sgn}(I, I^c)\cdot\mathrm{sgn}(I^c, I) = \mathrm{sgn}((I, I^c)\to(I^c, I))$ — the permutation taking the concatenation $(I, I^c)$ to $(I^c, I)$ is a cyclic block rearrangement of two blocks of sizes $k$ and $n - k$, which has sign $(-1)^{k(n-k)}$. And $\epsilon_I\epsilon_{I^c} = \prod_{i=1}^n\epsilon_i$. By signature, this product is the determinant of the signature matrix $\mathrm{diag}(\epsilon_1, \dots, \epsilon_n)$, which is $(-1)^s$. So $\star\star\sigma^I = (-1)^{k(n-k)+s}\sigma^I$.

> [!note]- Lemma 4: Euclidean $\mathbb{R}^3$ formulas
> **Statement:** On Euclidean $\mathbb{R}^3$ with coordinates $(x, y, z)$ and orientation $dx\wedge dy\wedge dz$: $\star 1 = dx\wedge dy\wedge dz$; $\star dx = dy\wedge dz$, $\star dy = dz\wedge dx$, $\star dz = dx\wedge dy$; $\star(dy\wedge dz) = dx$, $\star(dz\wedge dx) = dy$, $\star(dx\wedge dy) = dz$; $\star(dx\wedge dy\wedge dz) = 1$.
>
> **Hint:** Apply Lemma 2 with $n = 3$, all $\epsilon_i = +1$. The signs $\mathrm{sgn}(I, I^c)$ are $+1$ when $I$ is in the "canonical cyclic order" $\{1\}, \{2\}, \{3\}, \{1,2\}, \{2,3\}, \{1,3\}$ — i.e., when $(I, I^c)$ is even permutation of $(1, 2, 3)$.
>
> **Why needed:** Bridges Hodge theory to classical vector calculus on $\mathbb{R}^3$, the most familiar setting.
>
> > [!note]- Full proof
> > For $I = \emptyset$ ($k = 0$): $\sigma^\emptyset = 1$ and $I^c = \{1, 2, 3\}$. $\mathrm{sgn}(\emptyset, \{1,2,3\}) = +1$ (identity permutation). $\epsilon_\emptyset = 1$. So $\star 1 = +1\cdot dx\wedge dy\wedge dz$. Check.
> >
> > For $I = \{1\}$ ($k = 1$, so $\sigma^I = dx$): $I^c = \{2, 3\}$, $\mathrm{sgn}(\{1\}, \{2,3\}) = +1$. So $\star dx = dy\wedge dz$. Check.
> >
> > For $I = \{2\}$ ($k = 1$, so $\sigma^I = dy$): $I^c = \{1, 3\}$, $\mathrm{sgn}(\{2\}, \{1, 3\})$: the permutation $(1, 2, 3) \mapsto (2, 1, 3)$ has sign $-1$. So $\star dy = -dx\wedge dz = dz \wedge dx$. Check.
> >
> > For $I = \{3\}$: $I^c = \{1, 2\}$, $\mathrm{sgn}(\{3\}, \{1,2\}) = \mathrm{sgn}((1,2,3)\to(3,1,2)) = +1$ (cyclic permutation, even). So $\star dz = dx\wedge dy$. Check.
> >
> > The $2$-form cases follow similarly. The double-star formula at $k = 1, n = 3$ gives $\star\star = (-1)^{1\cdot 2 + 0} = +1$, consistent with $\star\star dx = \star(dy\wedge dz) = dx$. Check.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** As stated.
>
> *Proof.* All properties are pointwise on the fibres $\Lambda^k T_p^*M$, and extend smoothly because the metric $g$ and orientation are smooth. We verify each on a local orthonormal coframe.
>
> *Property 1 ($C^\infty$-linearity):* For $f \in C^\infty(M)$ and $\beta \in \Omega^k(M)$, the defining identity reads $\alpha\wedge\star(f\beta) = \langle\alpha, f\beta\rangle\operatorname{vol}_n = f\langle\alpha,\beta\rangle\operatorname{vol}_n = f\alpha\wedge\star\beta = \alpha\wedge(f\star\beta)$. By Lemma 1 (uniqueness), $\star(f\beta) = f\star\beta$.
>
> *Property 5 (coordinate formula):* By Lemma 2, $\star\sigma^I = \mathrm{sgn}(I, I^c)\epsilon_I\sigma^{I^c}$ on a positively oriented orthonormal coframe.
>
> *Property 2 (double-star):* By Lemma 3, $\star\star\sigma^I = (-1)^{k(n-k)+s}\sigma^I$ on basis forms. By $C^\infty$-linearity, $\star\star\omega = (-1)^{k(n-k)+s}\omega$ for all $\omega \in \Omega^k(M)$.
>
> *Property 4 (constants and volume):* $\star 1 = \operatorname{vol}_n$ by the defining identity with $\alpha = \beta = 1$. $\star\operatorname{vol}_n = \star\star 1 = (-1)^{0\cdot n + s}\cdot 1 = (-1)^s$ by the double-star formula.
>
> *Property 3 ([[Def - Isometry|isometry]] up to sign):* For basis forms, $\langle\star\sigma^I, \star\sigma^J\rangle = \langle\mathrm{sgn}(I, I^c)\epsilon_I\sigma^{I^c}, \mathrm{sgn}(J, J^c)\epsilon_J\sigma^{J^c}\rangle = \mathrm{sgn}(I, I^c)\mathrm{sgn}(J, J^c)\epsilon_I\epsilon_J\langle\sigma^{I^c}, \sigma^{J^c}\rangle = \mathrm{sgn}(I, I^c)\mathrm{sgn}(J, J^c)\epsilon_I\epsilon_J\delta_{IJ}\epsilon_{I^c}$ (since $\langle\sigma^K, \sigma^L\rangle = \delta_{KL}\epsilon_K$). When $I = J$: $\mathrm{sgn}(I, I^c)^2\epsilon_I\epsilon_J\epsilon_{I^c} = \epsilon_I^2\epsilon_{I^c} = \epsilon_{I^c}$. But $\epsilon_I\cdot\epsilon_{I^c} = (-1)^s$, so $\epsilon_{I^c} = (-1)^s/\epsilon_I = (-1)^s\epsilon_I$ (since $\epsilon_I^2 = 1$). So $\langle\star\sigma^I,\star\sigma^I\rangle = (-1)^s\epsilon_I = (-1)^s\langle\sigma^I,\sigma^I\rangle$. Extending by bilinearity gives the property for general forms.
>
> *Property 6 (Euclidean $\mathbb{R}^3$):* By Lemma 4. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Classical vector calculus:** Use the Hodge-star formulas in $\mathbb{R}^3$ to recover $\nabla\times(\nabla f) = 0$ and $\nabla\cdot(\nabla\times\vec F) = 0$ as instances of $d^2 = 0$ in different degrees. Concretely: $\nabla f$ as a $1$-form is $df$; $\nabla\times\vec F$ as a $1$-form is $\star dF^\flat$; so $\nabla\times(\nabla f) = \star d(df) = \star\cdot 0 = 0$. The "vector calculus identities" of textbooks are all consequences of $d^2 = 0$ via the Hodge star.

**Electromagnetic field tensor:** On Minkowski $\mathbb{R}^{3,1}$, write $F = E_i dx^i\wedge dt + B_{ij}dx^i\wedge dx^j$ as the electromagnetic $2$-form. Compute $\star F$ using the Lorentzian Hodge star (with signature $(- + + +)$): the result swaps the roles of $\vec E$ and $\vec B$ (with a sign). The duality $\vec E\leftrightarrow\vec B$ of source-free electromagnetism is exactly the Hodge star duality.

**Octonionic structures on $\mathbb{R}^8$:** Consider $\mathbb{R}^8$ with the standard Euclidean metric and an orientation. The Hodge star on $4$-forms satisfies $\star\star = +1$ (since $k(n-k) = 16$ is even and $s = 0$), so $\Omega^4(\mathbb{R}^8) = \Omega^4_+ \oplus \Omega^4_-$ splits into self-dual and anti-self-dual $4$-forms. Using the octonionic structure on $\mathbb{R}^8$, one can identify these eigenspaces with octonionic representations. This is the gateway to $\mathrm{Spin}(7)$ and $G_2$ holonomy in higher-dimensional geometry.

---

# Bridges

- **[[Def - The Codifferential|The codifferential]]** — the codifferential $\delta = \pm\star d\star$ is built directly from the Hodge star, with the sign determined by the double-star formula. Properties 2 and 5 of the theorem are exactly what is needed to compute $\delta$ explicitly. The combination "$\delta$ is defined using $\star d\star$, and $\star$ has property X" is the standard route from properties of $\star$ to properties of $\delta$.

- **[[Def - Hodge Laplacian|The Hodge Laplacian]]** — the Hodge Laplacian $\Delta = d\delta + \delta d$ commutes with $\star$ (since both $d$ and $\delta$ interact with $\star$ in compatible ways). The commutation is what makes $\star : \mathcal{H}^k \to \mathcal{H}^{n-k}$ an isomorphism on harmonic forms, ultimately giving Poincaré duality. The bridge "$\star$ commutes with $\Delta$ because $\delta = \pm\star d\star$ and double-star is scalar" is the link from $\star$'s algebraic properties to the topological invariance of Poincaré duality.

- **[[Def - Self-Dual and Anti-Self-Dual Forms|Self-dual / anti-self-dual decomposition]]** — in middle dimension and even $k$, $\star\star = +1$ on $\Omega^k$, making $\star$ a self-adjoint involution that splits $\Omega^k$ into $\pm 1$ eigenspaces. The bridge is that this decomposition exists exactly when $\star\star = +1$ on the middle degree, which is property 2 evaluated at $k = n/2$ with $k(n-k) + s$ even. For $n = 4$, $k = 2$, $s = 0$ this is $k(n-k) + s = 4 + 0 = 4$, even — so $\star\star = +1$ on $2$-forms in Riemannian $4$D, enabling the foundational decomposition of [[Gauge Theory V — Hodge Theory, Maxwell, Yang–Mills, and Instantons|Yang–Mills self-duality]].

- **Classical vector calculus on $\mathbb{R}^3$** — the cross product $u \times v$ is $\star(u^\flat\wedge v^\flat)$ followed by raising the index. The curl operator is $\star d$ on $1$-forms (with index manipulations). The divergence is $\delta = \star d\star$ on $1$-forms (with a sign). All classical vector calculus identities are Hodge-star identities translated through the musical isomorphism. The bridge between "form calculus on $\mathbb{R}^3$" and "vector calculus on $\mathbb{R}^3$" is property 6 of the theorem.

---

# Unlocked by This

> [!tip] Hodge Theory on Complex Manifolds *(from Complex Geometry)*
> On a complex Hermitian manifold, the Hodge star refines: it acts on $(p, q)$-forms as $\star : \Omega^{p,q} \to \Omega^{n-q, n-p}$ (where $n$ is the complex dimension), sending bidegree $(p, q)$ to bidegree $(n - q, n - p)$. This is the **conjugate-linear Hodge star** of complex Hodge theory, used to define **Dolbeault Laplacians** and the **Hodge decomposition** on a compact Kähler manifold. The structural property $\star^2 = +1$ or $-1$ generalizes to complex versions involving $i^{p-q}$.

> [!tip] Twistor Theory *(from Mathematical Physics)*
> On a self-dual Riemannian $4$-manifold (one whose anti-self-dual Weyl curvature vanishes), the algebraic identity $\star^2 = +1$ on $2$-forms is the key input to the **Penrose twistor construction**: the bundle of unit anti-self-dual $2$-forms is a $\mathbb{CP}^1$-bundle over the $4$-manifold, and the total space carries a natural complex structure. This **twistor space** encodes the conformal geometry of the original $4$-manifold complex-analytically, and is the foundation of **twistor methods** in conformal geometry and gauge theory.
