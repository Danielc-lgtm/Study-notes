---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Covariant Tensor on a Vector Space"
  - "Def - Symmetric Tensor Field"
  - "Def - Alternating Tensor Field"
tags: [geometry, differential-geometry, projectors]
---

# Notation

$V$ is a finite-dimensional real vector space, $\dim V = n$. $S_k$ is the symmetric group on $k$ elements; $\operatorname{sgn}\sigma$ is the sign of $\sigma \in S_k$. $T^k(V^*)$ is the space of covariant $k$-tensors on $V$; $\Sigma^k(V^*), \Lambda^k(V^*)$ are the symmetric and alternating subspaces. The projectors are $\mathrm{Sym}, \mathrm{Alt} : T^k(V^*) \to T^k(V^*)$. Full notation registry: [[Differential Geometry VII — Tensors and Tensor Fields]].

---

# Statement

> **Theorem (Symmetrization and Alternation Projectors).** Let $V$ be a finite-dimensional real vector space. The linear maps
> $$\mathrm{Sym} : T^k(V^*) \to T^k(V^*), \quad (\mathrm{Sym}\,\alpha)(v_1, \dots, v_k) = \frac{1}{k!}\sum_{\sigma \in S_k} \alpha(v_{\sigma(1)}, \dots, v_{\sigma(k)}),$$
> $$\mathrm{Alt} : T^k(V^*) \to T^k(V^*), \quad (\mathrm{Alt}\,\alpha)(v_1, \dots, v_k) = \frac{1}{k!}\sum_{\sigma \in S_k} (\operatorname{sgn}\sigma)\,\alpha(v_{\sigma(1)}, \dots, v_{\sigma(k)}),$$
> are **idempotent linear projections** onto $\Sigma^k(V^*)$ and $\Lambda^k(V^*)$ respectively:
>
> 1. $\mathrm{Sym}^2 = \mathrm{Sym}$, with image $\Sigma^k(V^*)$.
> 2. $\mathrm{Alt}^2 = \mathrm{Alt}$, with image $\Lambda^k(V^*)$.
> 3. $\mathrm{Sym}\,\alpha = \alpha \iff \alpha \in \Sigma^k(V^*)$; $\mathrm{Alt}\,\alpha = \alpha \iff \alpha \in \Lambda^k(V^*)$.
> 4. $\mathrm{Sym} \circ \mathrm{Alt} = 0 = \mathrm{Alt} \circ \mathrm{Sym}$ (the two projectors are *orthogonal* in a representation-theoretic sense).

> **Corollary (Decomposition for $k = 2$).** $T^2(V^*) = \Sigma^2(V^*) \oplus \Lambda^2(V^*)$, with the projections $\mathrm{Sym}$ and $\mathrm{Alt}$. Every covariant 2-tensor decomposes uniquely as $\beta = \mathrm{Sym}\,\beta + \mathrm{Alt}\,\beta$.

> **Counterexample for $k \geq 3$ and $\dim V\geq2$.** Under these hypotheses, $T^k(V^*) \supsetneq \Sigma^k(V^*) \oplus \Lambda^k(V^*)$ — there exist covariant $k$-tensors that are neither symmetric nor alternating nor a sum of one of each. They live in *mixed Young tableau* representations of $S_k$, beyond the trivial (symmetric) and sign (alternating) ones.

---

# Motivation

The motivation is **to extract the symmetric or antisymmetric part of a covariant tensor in a canonical way**. The symmetric part is needed when working with metrics or quadratic forms; the antisymmetric part is needed when working with forms or volume elements. Both projectors are *averages over the symmetric [[Def - Group|group]] action*, with signs in the antisymmetric case — and the averaging makes the result invariant (or sign-equivariant) under the action, which is what symmetry means.

The conceptual content: the symmetric group $S_k$ acts on $T^k(V^*)$ by permuting arguments, $(\sigma \cdot \alpha)(v_1, \dots, v_k) = \alpha(v_{\sigma(1)}, \dots, v_{\sigma(k)})$. The symmetric tensors are the *invariants* under this action; the alternating tensors are the *sign-equivariants*. The projectors $\mathrm{Sym}$ and $\mathrm{Alt}$ extract these [[Def - Subspace|subspaces]] via standard representation-theoretic averaging, in close parallel to the projector $\frac{1}{|G|}\sum_g g$ from finite group representation theory.

For $k = 2$, the symmetric group $S_2$ has only two irreducible representations: the trivial (which gives the symmetric tensors) and the sign (which gives the antisymmetric ones). Their sum is the whole regular representation, so $T^2 = \Sigma^2 \oplus \Lambda^2$ — the decomposition is complete.

For $k \geq 3$, $S_k$ has more irreducible representations (corresponding to Young diagrams with non-trivial shapes), and these contribute *additional* subspaces of $T^k(V^*)$ that are neither symmetric nor alternating. The simplest example is $k = 3$: $S_3$ has *three* irreducibles (trivial, sign, and a 2-dimensional standard representation), and the tensor space $T^3(V^*)$ decomposes into pieces corresponding to each. The "mixed" pieces are crucial for representation theory but appear only as nuisance in pure differential geometry — where one usually works with either the fully symmetric or fully alternating subspaces, and discards the rest.

The reason for separating symmetric from alternating into separate definition pages (despite the formal parallel) is *exactly* this asymmetry of behavior: for $k \geq 3$, they do not jointly span the full tensor space, and they have different downstream uses. Symmetric tensors lead to metrics and Riemannian geometry; alternating tensors lead to forms and integration. The Young-tableau "leftover" representations matter in representation theory and in the analysis of higher-rank curvature tensors, but they are not first-class objects in elementary differential geometry.

The projectors are critical in computations:

- The metric in a non-orthogonal coordinate system has components $g_{ij}$, and the *symmetric part* is the metric. The antisymmetric part would correspond to a symplectic-like structure.
- The Christoffel symbols $\Gamma^k_{ij}$ are not a tensor, but their *symmetric part* in the lower indices is a tensor (it is the "symmetric connection"); the *antisymmetric part* in the lower indices is the *torsion tensor*.
- The decomposition $\beta = \mathrm{Sym}\,\beta + \mathrm{Alt}\,\beta$ for $k = 2$ tensors lets you separate the "metric-like" content from the "form-like" content of any bilinear form.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem applies in any context where you need to extract symmetric or alternating parts.

**A bilinear form with mixed symmetric/antisymmetric content.** Given a bilinear form $\beta(v, w) = v^\top M w$ with general $M$, the symmetric part is $\frac{1}{2}(M + M^\top)$ and the antisymmetric part is $\frac{1}{2}(M - M^\top)$ — the standard matrix decomposition. The projectors $\mathrm{Sym}$ and $\mathrm{Alt}$ are exactly these operations at the bilinear-form level.

**The Christoffel symbols of a non-symmetric connection.** The Christoffel symbols $\Gamma^k_{ij}$ have a symmetric and antisymmetric part in $(i, j)$. The antisymmetric part is the *torsion tensor* $T^k_{ij} = \Gamma^k_{ij} - \Gamma^k_{ji}$. For the Levi-Civita connection on a Riemannian manifold, $T = 0$ (the connection is symmetric); for connections with torsion, $T$ measures the failure of the parallel transport to commute with translations.

**The Riemann curvature in different index orderings.** The Riemann tensor $R_{ijk\ell}$ (after lowering the contravariant index with the metric) has multiple symmetry properties: $R_{ijk\ell} = -R_{jik\ell}$ (antisymmetric in first pair), $R_{ijk\ell} = -R_{ij\ell k}$ (antisymmetric in second pair), $R_{ijk\ell} = R_{k\ell ij}$ (symmetric in swapping the two pairs), and the first Bianchi identity $R_{i[jk\ell]} = 0$ (alternation in last three indices vanishes). These symmetries are read off using the projectors $\mathrm{Sym}, \mathrm{Alt}$ applied to various index subsets.

**Targets (Output Amplification)**

**The symmetric and exterior algebras.** $\Sigma^\bullet(V^*) = \bigoplus_k \Sigma^k(V^*)$ is the symmetric algebra (also called the polynomial algebra $S(V^*)$); $\Lambda^\bullet(V^*) = \bigoplus_k \Lambda^k(V^*)$ is the exterior algebra. Both are quotients of the tensor algebra $T^\bullet(V^*)$, obtained by enforcing commutativity or anticommutativity at the basis level — and the projectors $\mathrm{Sym}, \mathrm{Alt}$ are what enable the quotient.

**Torsion-free splitting.** On a manifold with a connection $\nabla$, the *symmetric part* of $\nabla$ is itself a connection (the *torsion-free symmetric connection*), and the antisymmetric part is the torsion tensor $T$. So the projectors decompose any connection into a torsion-free piece and a tensor field. This is the conceptual root of the *existence* part of the [[Thm - Fundamental Theorem of Riemannian Geometry (Statement)|fundamental theorem of Riemannian geometry]]: a Riemannian metric determines a unique torsion-free, metric-compatible connection (the Levi-Civita connection), built by symmetrizing the connection that comes from the metric directly.

**Young decomposition for higher rank.** For $k \geq 3$, the projectors are the simplest cases of a wider family of *Young projectors*, one for each irreducible representation of $S_k$ (each Young tableau of shape $\lambda \vdash k$). The full decomposition $T^k(V^*) = \bigoplus_\lambda P_\lambda(T^k(V^*))$ is a Young decomposition, with $\Sigma^k$ corresponding to the partition $\lambda = (k)$ and $\Lambda^k$ to $\lambda = (1^k)$. This is the bridge to the *Schur-Weyl duality* and the representation theory of $GL(V)$.

---

# Why Is It True

The intuition is **averaging over the group action gives a projector onto the invariants; signed averaging gives a projector onto the sign-equivariants**.

**Mechanism in one line: $\frac{1}{|S_k|}\sum_\sigma \sigma$ is a projector onto $S_k$-invariants (since the sum is itself fixed by any element of $S_k$); $\frac{1}{|S_k|}\sum_\sigma (\operatorname{sgn}\sigma)\sigma$ is a projector onto sign-equivariants by the same argument with signs.**

For (1) and (3) ($\mathrm{Sym}$ projects onto $\Sigma^k$): If $\alpha \in \Sigma^k(V^*)$, then $\alpha(v_{\sigma(1)}, \dots) = \alpha(v_1, \dots)$ for every $\sigma$, so $\mathrm{Sym}\,\alpha = \frac{1}{k!}\sum_\sigma \alpha = \alpha$ ($k!$ terms each equal to $\alpha$, divided by $k!$). So $\mathrm{Sym}$ fixes $\Sigma^k$. For the converse, if $\beta = \mathrm{Sym}\,\alpha$, then for any $\tau \in S_k$,
$(\tau \cdot \beta)(v_1, \dots, v_k) = \beta(v_{\tau(1)}, \dots, v_{\tau(k)}) = \frac{1}{k!}\sum_\sigma \alpha(v_{\sigma\tau(1)}, \dots, v_{\sigma\tau(k)}) = \frac{1}{k!}\sum_{\sigma'} \alpha(v_{\sigma'(1)}, \dots) = \beta(v_1, \dots, v_k)$,
using the substitution $\sigma' = \sigma\tau$ (which runs over $S_k$ as $\sigma$ does). So $\beta$ is symmetric. Hence $\mathrm{Sym}(T^k(V^*)) \subseteq \Sigma^k(V^*)$, and we have $\mathrm{Sym}^2 = \mathrm{Sym}$ on $\Sigma^k$.

The argument for (2) and (3) for $\mathrm{Alt}$ is parallel, with signs tracked. The sign of the substitution $\sigma\tau$ is $(\operatorname{sgn}\sigma)(\operatorname{sgn}\tau)$, and one can check $(\tau \cdot \mathrm{Alt}\,\alpha) = (\operatorname{sgn}\tau)\,\mathrm{Alt}\,\alpha$ — making $\mathrm{Alt}\,\alpha$ sign-equivariant, hence alternating.

For (4) ($\mathrm{Sym} \circ \mathrm{Alt} = 0$): Symmetric and antisymmetric are *opposite* equivariances under $S_k$, and the sum/averaged combination of opposite equivariances vanishes. Concretely, $\mathrm{Sym}(\mathrm{Alt}\,\alpha) = \frac{1}{k!}\sum_\sigma (\sigma \cdot \mathrm{Alt}\,\alpha) = \frac{1}{k!}\sum_\sigma (\operatorname{sgn}\sigma) \mathrm{Alt}\,\alpha$. But $\sum_\sigma \operatorname{sgn}\sigma = 0$ for $k \geq 2$ (equally many even and odd permutations), so $\mathrm{Sym}(\mathrm{Alt}\,\alpha) = 0$.

For the decomposition $T^2 = \Sigma^2 \oplus \Lambda^2$: any $\beta \in T^2$ satisfies $\beta = \frac{1}{2}(\beta + \beta) = \frac{1}{2}((\beta + \tau\beta) + (\beta - \tau\beta)) = \mathrm{Sym}\,\beta + \mathrm{Alt}\,\beta$, where $\tau$ is the swap. The decomposition is unique because $\mathrm{Sym} + \mathrm{Alt} = \mathrm{id}$ on $T^2$ and they are projectors.

For the counterexample at $k \geq 3$: take the tensor $\alpha = \varepsilon^1 \otimes \varepsilon^2 \otimes \varepsilon^2$ in $T^3(\mathbb{R}^{n*})$ with $n \geq 2$. Compute $\mathrm{Sym}\,\alpha$ and $\mathrm{Alt}\,\alpha$ and verify their sum is not $\alpha$ — there is a "mixed" residual.

---

# What Makes This Hard

The non-trivial part is **understanding why the decomposition fails for $k \geq 3$**. The intuition from $k = 2$ — that "every tensor decomposes into symmetric and antisymmetric parts" — generalizes only in modified form. The honest statement is that $T^k(V^*)$ decomposes as a direct sum of $S_k$-irreducible representations, and $\Sigma^k$ and $\Lambda^k$ are only two of the irreducibles (the trivial and the sign). For $k \geq 3$, there are *more* irreducibles, and they live in the complement of $\Sigma^k \oplus \Lambda^k$.

The common error: writing every tensor as a symmetric plus antisymmetric part for general $k$. This is wrong: for $k = 3$ on $\mathbb{R}^n$ with $n \geq 2$, there are tensors that are neither symmetric nor antisymmetric, and decompose into both *Sym* and *Alt* parts plus a residual. The residual is what makes the Young decomposition non-trivial.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Verify that $\mathrm{Sym}$ and $\mathrm{Alt}$ are linear, idempotent, and have the claimed images. Verify $\mathrm{Sym} \circ \mathrm{Alt} = 0$ using the vanishing of the signed sum over $S_k$ for $k \geq 2$. For the $k = 2$ decomposition, verify $\mathrm{Sym} + \mathrm{Alt} = \mathrm{id}$ on $T^2$.

**Subgoal decomposition:**

1. **$\mathrm{Sym}$ is linear and idempotent, with image $\Sigma^k$.** Show $\mathrm{Sym}(a\alpha + b\beta) = a\,\mathrm{Sym}\,\alpha + b\,\mathrm{Sym}\,\beta$, $\mathrm{Sym}(\mathrm{Sym}\,\alpha) = \mathrm{Sym}\,\alpha$, and $\mathrm{Sym}\,\alpha = \alpha$ iff $\alpha$ is symmetric.
   - *Hint:* Use the averaging-over-$S_k$ argument. Linearity from linearity of $\alpha$. Idempotence from the substitution $\sigma' = \sigma\tau$.
   - *Why needed:* Establishes $\mathrm{Sym}$ as a genuine projector.

2. **$\mathrm{Alt}$ is linear and idempotent, with image $\Lambda^k$.** Same as (1) with sign factors.
   - *Hint:* Track signs. $(\operatorname{sgn}\sigma)(\operatorname{sgn}\tau) = \operatorname{sgn}(\sigma\tau)$.
   - *Why needed:* Same role for $\mathrm{Alt}$.

3. **$\mathrm{Sym} \circ \mathrm{Alt} = 0$.** Show that the composite vanishes.
   - *Hint:* Apply $\mathrm{Sym}$ to $\mathrm{Alt}\,\alpha$, expand, and use $\sum_\sigma \operatorname{sgn}\sigma = 0$.
   - *Why needed:* Establishes the projectors as "orthogonal" in the representation-theoretic sense.

4. **Decomposition $T^2 = \Sigma^2 \oplus \Lambda^2$.** Show that $\mathrm{Sym} + \mathrm{Alt} = \mathrm{id}$ on $T^2$.
   - *Hint:* For $\beta \in T^2$, $\mathrm{Sym}\,\beta + \mathrm{Alt}\,\beta = \frac{1}{2}(\beta + \tau\beta) + \frac{1}{2}(\beta - \tau\beta) = \beta$, where $\tau$ is the swap.
   - *Why needed:* The most-used special case.

5. **Counterexample for $k \geq 3$.** Construct a $\alpha \in T^3$ with $\mathrm{Sym}\,\alpha + \mathrm{Alt}\,\alpha \neq \alpha$.
   - *Hint:* Try $\alpha = \varepsilon^1 \otimes \varepsilon^2 \otimes \varepsilon^2 - \varepsilon^2 \otimes \varepsilon^1 \otimes \varepsilon^2$ on $\mathbb{R}^{n \geq 2}$. Compute $\mathrm{Sym}$ and $\mathrm{Alt}$ explicitly and check the sum differs from $\alpha$.
   - *Why needed:* Shows that the decomposition does not generalize.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\mathrm{Sym}$ is an idempotent projection onto $\Sigma^k(V^*)$
> **Statement:** (1a) $\mathrm{Sym}$ is linear. (1b) For every $\alpha \in T^k(V^*)$, $\mathrm{Sym}\,\alpha \in \Sigma^k(V^*)$. (1c) $\mathrm{Sym}^2 = \mathrm{Sym}$. (1d) $\mathrm{Sym}\,\alpha = \alpha \iff \alpha \in \Sigma^k(V^*)$.
>
> **Hint:** Average-over-group-action argument. The key identity is the substitution $\sigma' = \sigma\tau$ running over $S_k$ as $\sigma$ does.
>
> **Why needed:** Establishes $\mathrm{Sym}$ as a projector onto the symmetric subspace.
>
> > [!note]- Full proof
> > (1a) Linearity is immediate: $(\mathrm{Sym}(a\alpha + b\beta))(v_1, \dots) = \frac{1}{k!}\sum_\sigma (a\alpha + b\beta)(v_{\sigma(1)}, \dots) = a (\mathrm{Sym}\,\alpha)(v_1, \dots) + b (\mathrm{Sym}\,\beta)(v_1, \dots)$.
> >
> > (1b) For $\tau \in S_k$,
> > $$(\tau \cdot \mathrm{Sym}\,\alpha)(v_1, \dots) = (\mathrm{Sym}\,\alpha)(v_{\tau(1)}, \dots) = \frac{1}{k!}\sum_\sigma \alpha(v_{\sigma\tau(1)}, \dots) = \frac{1}{k!}\sum_{\sigma'} \alpha(v_{\sigma'(1)}, \dots) = (\mathrm{Sym}\,\alpha)(v_1, \dots),$$
> > with $\sigma' := \sigma\tau$. So $\mathrm{Sym}\,\alpha$ is fixed by every $\tau$, i.e. symmetric.
> >
> > (1c) For $\alpha \in \Sigma^k$, every $\sigma \in S_k$ gives $\sigma \cdot \alpha = \alpha$, so $\mathrm{Sym}\,\alpha = \frac{1}{k!}\sum_\sigma \alpha = \alpha$. Hence $\mathrm{Sym}^2 = \mathrm{Sym}$ on the image, which is all of $\Sigma^k$ by (1b).
> >
> > (1d) ($\Leftarrow$): if $\alpha$ is symmetric, $\mathrm{Sym}\,\alpha = \alpha$ by (1c). ($\Rightarrow$): if $\mathrm{Sym}\,\alpha = \alpha$, then by (1b), $\alpha$ is symmetric. $\blacksquare$

> [!note]- Lemma 2: $\mathrm{Alt}$ is an idempotent projection onto $\Lambda^k(V^*)$
> **Statement:** Same as Lemma 1 with $\mathrm{Sym} \mapsto \mathrm{Alt}, \Sigma^k \mapsto \Lambda^k$, and a sign change tracking $\operatorname{sgn}\sigma$.
>
> **Hint:** Same argument with signs. Use $\operatorname{sgn}(\sigma\tau) = \operatorname{sgn}\sigma \cdot \operatorname{sgn}\tau$.
>
> **Why needed:** Establishes $\mathrm{Alt}$ as a projector onto the alternating subspace.
>
> > [!note]- Full proof
> > (2a) Linearity: immediate as in (1a).
> >
> > (2b) For $\tau \in S_k$,
> > $$(\tau \cdot \mathrm{Alt}\,\alpha)(v_1, \dots) = \frac{1}{k!}\sum_\sigma (\operatorname{sgn}\sigma)\,\alpha(v_{\sigma\tau(1)}, \dots) = \frac{1}{k!}\sum_{\sigma'} (\operatorname{sgn}(\sigma'\tau^{-1}))\,\alpha(v_{\sigma'(1)}, \dots)$$
> > $$= (\operatorname{sgn}\tau^{-1}) \cdot \frac{1}{k!}\sum_{\sigma'} (\operatorname{sgn}\sigma')\,\alpha(v_{\sigma'(1)}, \dots) = (\operatorname{sgn}\tau)\, (\mathrm{Alt}\,\alpha)(v_1, \dots),$$
> > using $\operatorname{sgn}\tau^{-1} = \operatorname{sgn}\tau$. So $\mathrm{Alt}\,\alpha$ is sign-equivariant under $S_k$, hence alternating.
> >
> > (2c) For alternating $\alpha$, $\sigma \cdot \alpha = (\operatorname{sgn}\sigma)\,\alpha$, so $\mathrm{Alt}\,\alpha = \frac{1}{k!}\sum_\sigma (\operatorname{sgn}\sigma)^2\,\alpha = \alpha$. Hence $\mathrm{Alt}^2 = \mathrm{Alt}$.
> >
> > (2d) By (2b) and (2c). $\blacksquare$

> [!note]- Lemma 3: $\mathrm{Sym} \circ \mathrm{Alt} = 0$
> **Statement:** For every $\alpha \in T^k(V^*)$ with $k \geq 2$, $\mathrm{Sym}(\mathrm{Alt}\,\alpha) = 0 = \mathrm{Alt}(\mathrm{Sym}\,\alpha)$.
>
> **Hint:** Expand and use $\sum_\sigma \operatorname{sgn}\sigma = 0$ for $k \geq 2$.
>
> **Why needed:** Establishes that $\mathrm{Sym}$ and $\mathrm{Alt}$ are mutually annihilating.
>
> > [!note]- Full proof
> > $\mathrm{Sym}(\mathrm{Alt}\,\alpha)(v_1, \dots) = \frac{1}{k!}\sum_\tau (\mathrm{Alt}\,\alpha)(v_{\tau(1)}, \dots) = \frac{1}{k!}\sum_\tau (\operatorname{sgn}\tau)(\mathrm{Alt}\,\alpha)(v_1, \dots)$ (since $\mathrm{Alt}\,\alpha$ is sign-equivariant) $= (\mathrm{Alt}\,\alpha)(v_1, \dots) \cdot \frac{1}{k!}\sum_\tau \operatorname{sgn}\tau = 0$, using $\sum_\tau \operatorname{sgn}\tau = 0$ for $k \geq 2$. The other identity is symmetric. $\blacksquare$

> [!note]- Lemma 4: Decomposition $T^2(V^*) = \Sigma^2(V^*) \oplus \Lambda^2(V^*)$
> **Statement:** $T^2(V^*) = \Sigma^2(V^*) \oplus \Lambda^2(V^*)$, and every $\beta \in T^2(V^*)$ decomposes uniquely as $\beta = \mathrm{Sym}\,\beta + \mathrm{Alt}\,\beta$.
>
> **Hint:** For $\beta \in T^2$, $\mathrm{Sym}\,\beta(v, w) = \frac{1}{2}(\beta(v, w) + \beta(w, v))$ and $\mathrm{Alt}\,\beta(v, w) = \frac{1}{2}(\beta(v, w) - \beta(w, v))$. Their sum is $\beta$.
>
> **Why needed:** The most-used decomposition in the chapter.
>
> > [!note]- Full proof
> > For $k = 2$, $S_2 = \{\mathrm{id}, \tau\}$ where $\tau$ is the swap. So
> > $$\mathrm{Sym}\,\beta(v, w) = \frac{1}{2}(\beta(v, w) + \beta(w, v)), \qquad \mathrm{Alt}\,\beta(v, w) = \frac{1}{2}(\beta(v, w) - \beta(w, v)).$$
> > Adding: $\mathrm{Sym}\,\beta + \mathrm{Alt}\,\beta = \beta$. So $T^2 = \Sigma^2 + \Lambda^2$. The sum is direct because $\Sigma^2 \cap \Lambda^2 = 0$ (a tensor both symmetric and alternating vanishes by $\alpha(v, w) = \alpha(w, v) = -\alpha(w, v) \Rightarrow \alpha(v, w) = 0$). So $T^2 = \Sigma^2 \oplus \Lambda^2$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** The maps $\mathrm{Sym}, \mathrm{Alt}$ are idempotent linear projections of $T^k(V^*)$ onto $\Sigma^k(V^*), \Lambda^k(V^*)$, with $\mathrm{Sym} \circ \mathrm{Alt} = 0$.
>
> *Proof.* See Lemmas 1, 2, 3.
>
> **Corollary (Decomposition for $k = 2$).** $T^2(V^*) = \Sigma^2(V^*) \oplus \Lambda^2(V^*)$.
>
> *Proof.* See Lemma 4.
>
> **Counterexample for $k = 3$ on $\mathbb{R}^2$.** Take $\alpha = \varepsilon^1 \otimes \varepsilon^2 \otimes \varepsilon^2 - \varepsilon^2 \otimes \varepsilon^1 \otimes \varepsilon^2$ on $V = \mathbb{R}^2$.
>
> Direct computation: $\mathrm{Sym}\,\alpha$ averages $\alpha$ over $S_3$. The result is the sum over all permutations of the index tuple $(1, 2, 2)$ minus the sum over all permutations of $(2, 1, 2)$, divided by $6$. But these two sums are actually the same up to relabeling: $(1, 2, 2)$ and $(2, 1, 2)$ give the same multiset $\{1, 2, 2\}$ under any permutation of the slot positions. So $\mathrm{Sym}\,\alpha = 0$.
>
> Similarly, $\mathrm{Alt}\,\alpha$ involves signed averaging. By antisymmetry, any tensor with a repeated index ($2$ appears twice in both terms of $\alpha$) is killed by $\mathrm{Alt}$: $\mathrm{Alt}(\varepsilon^1 \otimes \varepsilon^2 \otimes \varepsilon^2) = 0$ because the result must be antisymmetric in the last two slots, but it has a repeated index $2$. Same for the other term. So $\mathrm{Alt}\,\alpha = 0$.
>
> But $\alpha \neq 0$: it is the nonzero $T^3$ element $\varepsilon^1 \otimes \varepsilon^2 \otimes \varepsilon^2 - \varepsilon^2 \otimes \varepsilon^1 \otimes \varepsilon^2$. So $\mathrm{Sym}\,\alpha + \mathrm{Alt}\,\alpha = 0 \neq \alpha$, and $T^3 \supsetneq \Sigma^3 \oplus \Lambda^3$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Continuum mechanics: decomposition of the velocity gradient.** On Euclidean space with its standard flat connection, the velocity gradient $\nabla_i v^j$ of a fluid is a $(1,1)$-tensor (or a $(0,2)$-tensor after lowering an index). Bare partial derivatives $\partial_i v^j$ do not define tensor components in arbitrary coordinates. Its symmetric part is the *rate of strain* $D_{ij} = \frac{1}{2}(\partial_i v_j + \partial_j v_i)$ — describing local stretching and shearing. Its antisymmetric part is the *vorticity* $\omega_{ij} = \frac{1}{2}(\partial_i v_j - \partial_j v_i)$ — describing local rotation. The decomposition into symmetric and antisymmetric parts is *physically* the decomposition into stretching and rotation, and is foundational in fluid mechanics. Lee's projectors are exactly these classical operations.

**General relativity: the Weyl tensor as a "traceless" Riemann.** The Riemann curvature has 20 independent components in 4D. Subtracting the Ricci part (the "trace" of Riemann) gives the *Weyl tensor*, which has the same symmetries as Riemann but with all traces vanishing. The construction uses projectors of the kind discussed here: the Riemann tensor is decomposed into Weyl + Ricci-trace pieces using a specific Young projector arrangement.

**Representation theory: Young symmetrizers.** The Sym and Alt projectors are the simplest cases of *Young symmetrizers*, one for each partition $\lambda$ of $k$. The Young symmetrizer $c_\lambda$ projects $T^k(V^*)$ onto the irreducible $S_k$-representation of shape $\lambda$. For $\lambda = (k)$, $c_\lambda = \mathrm{Sym}$; for $\lambda = (1^k)$, $c_\lambda = \mathrm{Alt}$. For intermediate $\lambda$, the projector is a more complex combination. This is the algebraic origin of the *Schur-Weyl duality* relating $GL(V)$ representations to $S_k$ representations.

**Algebraic topology: the Hochschild-Serre splitting.** In the Hochschild-Serre spectral sequence for the homology of a group extension, the symmetric and alternating parts of bilinear forms on the cyclic group give the basic splitting. The same symmetrization/alternation projectors appear in the algebraic setting, with the symmetric part giving the "symmetric homology" and the alternating part giving the "antisymmetric" piece (related to the second cohomology).

---

# Bridges

- **The symmetric algebra $S^\bullet(V^*)$.** The graded direct sum $\bigoplus_k \Sigma^k(V^*)$ with the symmetric product is the symmetric algebra. The symmetric product $\alpha\beta = \mathrm{Sym}(\alpha \otimes \beta)$ uses the projector. The symmetric algebra is *the* polynomial algebra on $V$, with the symmetric power $\Sigma^k(V^*)$ being the degree-$k$ homogeneous polynomials. So the projector $\mathrm{Sym}$ is the algebraic projector onto polynomials of fixed degree.

- **The exterior algebra $\Lambda^\bullet(V^*)$.** The graded direct sum $\bigoplus_k \Lambda^k(V^*)$ with the wedge product is the exterior algebra. The wedge product $\omega \wedge \eta = \binom{k+\ell}{k}\,\mathrm{Alt}(\omega \otimes \eta)$ uses the projector $\mathrm{Alt}$ (up to a normalization factor). So the projector $\mathrm{Alt}$ is the algebraic projector onto multivectors of fixed degree.

- **Torsion of a connection.** The torsion tensor $T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y]$ is the *antisymmetric part* of the connection's lower indices. The fact that this is a *tensor* (despite $\nabla$ not being one) follows from the alternation killing the non-tensorial parts. Defining $\nabla^0_XY:=\nabla_XY-\tfrac12T(X,Y)$ gives a torsion-free connection and the precise decomposition $\nabla=\nabla^0+\tfrac12T$ separates a connection into a tensor and a symmetric connection.

- **Riemann curvature symmetries.** The Riemann tensor $R_{ijk\ell}$ has antisymmetric pairs (anti)symmetrization properties read using the projectors. The first Bianchi identity is the vanishing of $\mathrm{Alt}_{[jk\ell]}\, R_{ijk\ell}$ (alternation in the last three indices), and the symmetry under pair exchange is $\mathrm{Sym}_{(ij)\leftrightarrow(k\ell)}\, R_{ijk\ell} = R_{ijk\ell}$. So the structure of the Riemann tensor is described by a battery of projector identities.

---

# Unlocked by This

> [!tip] The Wedge Product *(from [[Differential Geometry VIII — Differential Forms]])*
> The wedge product $\omega \wedge \eta = \binom{k+\ell}{k}\,\mathrm{Alt}(\omega \otimes \eta)$ uses the $\mathrm{Alt}$ projector with a combinatorial normalization. Computing wedge products in coordinates is exactly applying $\mathrm{Alt}$ to a tensor product and remembering the factorial factor.

> [!tip] The Torsion-Free Symmetric Connection *(from Riemannian Geometry)*
> Every connection $\nabla$ determines a torsion-free connection $\nabla^0_XY=\nabla_XY-\tfrac12T(X,Y)$. Thus $\nabla=\nabla^0+\tfrac12T$; the difference of the two connections is tensorial even though neither connection is itself a tensor. The Levi-Civita connection is the unique torsion-free, metric-compatible connection — built using the metric and projecting away the antisymmetric (torsion) part.

> [!tip] Young Symmetrizers and the Schur-Weyl Duality *(from Representation Theory)*
> For $k \geq 3$, the projectors generalize to **Young symmetrizers** $c_\lambda$, one for each partition $\lambda \vdash k$. These project $T^k(V^*)$ onto the $\lambda$-isotypic component. The Schur-Weyl duality relates the resulting decomposition to representations of $GL(V)$: each $c_\lambda(T^k(V^*))$ is an irreducible $GL(V) \times S_k$ representation. This is the foundation of the *Schur functor* construction in representation theory.

> [!tip] Decomposition of the Riemann Curvature *(from Riemannian Geometry)*
> The Riemann tensor on a 4D manifold has 20 independent components (after accounting for symmetries). These decompose into: 1 scalar (the scalar curvature $R$), 9 components of the traceless Ricci (Einstein) tensor, and 10 components of the Weyl tensor. The projectors used in this decomposition are higher-order Young symmetrizers acting on $T^4(V^*)$. The result is one of the foundational structural decompositions of differential geometry.
