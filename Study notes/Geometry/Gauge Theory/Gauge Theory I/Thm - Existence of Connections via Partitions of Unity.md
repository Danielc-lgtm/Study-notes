---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Connection on a Vector Bundle"
  - "Def - Vector Bundle"
  - "Def - Local Trivialization"
tags: [geometry, gauge-theory, existence, partitions-of-unity]
---

# Notation

$E \to M$ is a smooth vector bundle of rank $K$ over a paracompact Hausdorff smooth manifold $M$. A **connection** on $E$ is a Koszul connection in the sense of [[Def - Connection on a Vector Bundle]]. A **partition of unity** subordinate to an open cover $\{U_\alpha\}$ is a collection of smooth functions $\{\rho_\alpha : M \to [0, 1]\}$ with $\mathrm{supp}(\rho_\alpha) \subset U_\alpha$, the supports forming a locally finite family, and $\sum_\alpha \rho_\alpha \equiv 1$ on $M$. For the parent symbol registry see [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

---

# Statement

> **Theorem.** Every smooth vector bundle $E \to M$ over a paracompact smooth manifold admits a connection. Moreover, the **space of connections** on $E$ is an affine space modelled on the vector space $\Omega^1(M, \mathrm{End}(E))$ of $\mathrm{End}(E)$-valued 1-forms: any two connections $\nabla_1, \nabla_2$ differ by such a 1-form, $\nabla_2 = \nabla_1 + D$ for some $D \in \Omega^1(M, \mathrm{End}(E))$, and conversely any such $D$ added to a connection yields a new connection.

---

# Motivation

The theorem says two things, both useful:

(1) **Existence is automatic.** You do not need any special structure on $E$ — not a metric, not a complex structure, not anything beyond the bundle data — to define a connection. Every smooth vector bundle has connections.

(2) **The space of connections is affine.** This is a structural fact with substantial consequences. The set $\mathcal{A}(E)$ of all connections on $E$ is *not* a vector space — there is no zero connection, since connections involve the Leibniz rule which is inhomogeneous. But the *difference* of two connections is well-behaved: it is an $\mathrm{End}(E)$-valued 1-form. So $\mathcal{A}(E)$ is an affine space modelled on $\Omega^1(M, \mathrm{End}(E))$, with the tangent space at any point being precisely this vector space.

The proof is by **partition of unity** — a standard manifold-theoretic gluing technique. The strategy: in each trivializing patch the trivial connection works; glue locally trivial connections via a partition of unity. The non-obvious technical point is that this gluing *preserves the Leibniz rule* — the partition-of-unity sum $\sum\rho_\alpha\nabla^\alpha$ is a connection precisely because $\sum\rho_\alpha = 1$, killing the inhomogeneous correction terms from the gluing.

This result has the same flavour as "every smooth manifold has a Riemannian metric" and "every smooth manifold has a partition of unity" — generic existence theorems where paracompactness of $M$ is essential. The proof reduces a global question (existence of connection) to a local one (existence in each patch — trivial since the patch is a product) plus a gluing argument.

The affine-space structure is critical for *moduli problems* in gauge theory. The **Yang-Mills moduli space** is $\mathcal{A}(P)/\mathcal{G}$, the affine space of connections modulo the gauge group — a finite-dimensional quotient with rich topology. The **affineness** of $\mathcal{A}(P)$ is what makes the linearization (and hence the analytic theory of moduli spaces) clean.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is bare: a smooth vector bundle on a paracompact manifold. Examples include all the basic geometric and physical bundles.

**Tangent bundle of any smooth manifold.** $E = TM$ for any smooth $M$. The theorem gives existence of a connection — the special connection (Levi-Civita) requires a metric, but *some* connection always exists.

**Wave-function bundles in physics.** Hermitian line bundles for electromagnetism, hermitian rank-$K$ bundles for non-abelian gauge theory. The theorem ensures the gauge fields exist as a matter of bundle theory, before any equations of motion are imposed.

**Trivial bundles.** $E = M \times \mathbb{R}^K$ trivially has the canonical trivial connection $\nabla\sigma = d\sigma$; the theorem confirms this and also notes that *other* connections exist (any 1-form $A \in \Omega^1(M, \mathrm{gl}(K))$ added to the trivial one gives another connection).

**Pullback bundles.** For $f : M \to N$ and a bundle $E \to N$ with connection $\nabla$, the pullback bundle $f^*E \to M$ has the canonical *pullback connection* $f^*\nabla$. The theorem applied to $f^*E$ confirms its existence — and in fact gives an *explicit* construction via the pullback.

**Targets (Output Amplification)**

The conclusion (existence + affine space) combined with other ingredients:

**Combined with metric structure:** existence of metric-compatible connections (Riemannian connections on $TM$, hermitian connections on hermitian bundles). The space of metric-compatible connections is a non-empty *affine subspace* of $\mathcal{A}(E)$, with the difference of any two metric-compatible connections being an $\mathfrak{o}(E)$ (or $\mathfrak{u}(E)$)-valued 1-form.

**Combined with torsion-freeness:** the **Levi-Civita connection** is uniquely characterised among connections on $TM$ as the metric-compatible, torsion-free one. The Koszul formula gives an explicit construction; the theorem ensures connections exist before uniqueness is even considered.

**Combined with gauge group action:** the space of connections modulo the gauge group, $\mathcal{A}(E)/\mathcal{G}(E)$, has a well-defined affine quotient structure. This is the foundation of moduli-space constructions in gauge theory.

**Combined with Chern-Weil theory:** the *Chern classes* of $E$ are independent of which connection is chosen (a key result in characteristic class theory). The existence of *some* connection lets you compute Chern classes via curvature; the *independence* uses the affine-space structure and Bianchi identity to vary the connection continuously.

---

# Why Is It True

**One-line mechanism summary:** **Trivial connections exist on each patch (just use componentwise $d$), and a partition of unity $\{\rho_\alpha\}$ with $\sum\rho_\alpha = 1$ allows weighted averaging that preserves the Leibniz rule.**

The intuition: a connection is a *local* concept (it asks how to differentiate sections, an inherently local question), and locally — on a single trivializing patch $U \times \mathbb{R}^K$ — there is an obvious connection: differentiate components in the trivialization, $\nabla\sigma = d\sigma$ where $\sigma$ is identified with its component vector. So *locally* connections are not a problem; the only issue is gluing.

A partition of unity gives a smooth interpolation between local data. For a smooth function $f$ defined locally as $f^{(\alpha)}$ on each $U_\alpha$, the global expression $f = \sum_\alpha\rho_\alpha f^{(\alpha)}$ is smooth and equals $f^{(\alpha)}$ on patches where $\rho_\alpha = 1$. The same idea applied to connections: $\nabla = \sum_\alpha\rho_\alpha\nabla^{(\alpha)}$, where $\nabla^{(\alpha)}$ is the trivial connection on $U_\alpha$ extended trivially.

The non-trivial verification: does this preserve the Leibniz rule? Check $\nabla(f\sigma) = \sum_\alpha\rho_\alpha\nabla^{(\alpha)}(f\sigma) = \sum_\alpha\rho_\alpha[(df)\sigma + f\nabla^{(\alpha)}\sigma] = (df)\sigma\sum_\alpha\rho_\alpha + f\sum_\alpha\rho_\alpha\nabla^{(\alpha)}\sigma = (df)\sigma \cdot 1 + f\nabla\sigma$. ✓

The key step: $\sum_\alpha\rho_\alpha = 1$ converts $\sum\rho_\alpha(df)\sigma$ into just $(df)\sigma$ — the partition of unity normalization is exactly what is needed for Leibniz to survive averaging.

The affine-space structure: if $\nabla_1, \nabla_2$ are both connections and $D := \nabla_2 - \nabla_1$, compute $D(f\sigma) = \nabla_2(f\sigma) - \nabla_1(f\sigma) = [f\nabla_2\sigma + (df)\sigma] - [f\nabla_1\sigma + (df)\sigma] = f(\nabla_2\sigma - \nabla_1\sigma) = fD\sigma$. So $D$ is $C^\infty$-linear in $\sigma$ — a *tensor*, specifically a section of $\mathrm{End}(E) \otimes T^*M$. Conversely, $\nabla_1 + D$ for any such tensorial $D$ satisfies Leibniz (the constant-in-$f$ pieces cancel).

---

# What Makes This Hard

The proof is straightforward once you know it, but two technical hurdles can trip people up:

(1) **Why does the partition-of-unity average preserve Leibniz?** Because $\sum\rho_\alpha = 1$, the inhomogeneous $(df)\sigma$ piece appears with coefficient $\sum\rho_\alpha = 1$, not some smaller weighted average that would mess things up. This is the *key calculation*.

(2) **Paracompactness is essential.** Partitions of unity exist for *paracompact* manifolds; for non-paracompact manifolds (rare in geometric settings but possible in abstract topology) the existence of connections fails.

Common errors: (i) Trying to average frames or trivializations directly rather than averaging the *connection operators*. (ii) Forgetting that the trivial connection in a patch depends on the choice of trivialization — the *trivial-connection-in-one-trivialization* and the *trivial-connection-in-a-different-trivialization* are different connections, related by the change-of-frame law. (iii) Confusing the affine-space structure for connections with a vector-space structure — connections do not form a vector space because of Leibniz.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Existence — choose a trivializing cover $\{U_\alpha\}$, a partition of unity $\{\rho_\alpha\}$ subordinate to it, define trivial connections $\nabla^{(\alpha)}$ on each patch, and set $\nabla = \sum_\alpha\rho_\alpha\nabla^{(\alpha)}$. Verify Leibniz. Affineness — compute $\nabla_2 - \nabla_1$ for any two connections, observe it is $C^\infty$-linear in the section.

**Subgoal decomposition:**

1. **Choose a trivializing cover and partition of unity.** $\{U_\alpha\}$ an open cover with trivializations $\Phi_\alpha : E|_{U_\alpha} \cong U_\alpha \times \mathbb{R}^K$, and $\{\rho_\alpha\}$ a smooth partition of unity subordinate to this cover. Existence of $\{\rho_\alpha\}$ uses paracompactness.
   - *Hint:* Standard manifold theory; not specific to bundles.
   - *Why needed:* Sets up the local-to-global machinery.

2. **Define local trivial connections.** On each $U_\alpha$, the trivialization $\Phi_\alpha$ identifies $E|_{U_\alpha}$ with $U_\alpha \times \mathbb{R}^K$; in this product the trivial connection is $\nabla^{(\alpha)}\sigma = d(\Phi_\alpha\sigma)$, where the right side differentiates the components in $\mathbb{R}^K$. Extend $\nabla^{(\alpha)}$ to all of $\Gamma(E)$ by restriction (or by setting it to "zero" outside the patch — the partition of unity will localize).
   - *Hint:* Local triviality is exactly the structure that lets you define a "componentwise $d$" inside each patch.
   - *Why needed:* Local connections are the input to gluing.

3. **Glue via the partition of unity.** Set $\nabla = \sum_\alpha\rho_\alpha\nabla^{(\alpha)}$, the partition-of-unity average. This is well-defined globally because the support condition makes the sum locally finite.
   - *Hint:* For each section $\sigma$, evaluate $\nabla\sigma$ at $p$: only finitely many $\rho_\alpha(p) \ne 0$, so the sum reduces to a finite sum at each point.
   - *Why needed:* Provides the candidate global connection.

4. **Verify Leibniz for $\nabla$.** Compute $\nabla(f\sigma) = \sum\rho_\alpha\nabla^{(\alpha)}(f\sigma) = \sum\rho_\alpha[(df)\sigma + f\nabla^{(\alpha)}\sigma] = (df)\sigma\sum\rho_\alpha + f\sum\rho_\alpha\nabla^{(\alpha)}\sigma = (df)\sigma + f\nabla\sigma$, using $\sum\rho_\alpha = 1$.
   - *Hint:* The key step is the cancellation $\sum\rho_\alpha = 1$.
   - *Why needed:* Confirms the candidate is genuinely a connection.

5. **Verify affineness.** For any two connections $\nabla_1, \nabla_2$, define $D = \nabla_2 - \nabla_1$ as the difference operator on sections. Compute $D(f\sigma) = \nabla_2(f\sigma) - \nabla_1(f\sigma) = f\nabla_2\sigma + (df)\sigma - f\nabla_1\sigma - (df)\sigma = fD\sigma$. So $D$ is $C^\infty$-linear, hence tensorial, hence a section of $\mathrm{End}(E) \otimes T^*M = \Omega^1(M, \mathrm{End}(E))$.
   - *Hint:* The inhomogeneous Leibniz pieces cancel in the difference, leaving a tensorial operator.
   - *Why needed:* Establishes the affine-space structure.

---

# Lemma Decomposition

> [!note]- Lemma 1: Existence of partitions of unity
> **Statement:** Every paracompact smooth manifold $M$ admits a smooth partition of unity subordinate to any given open cover.
>
> **Hint:** Standard result from manifold theory; combines smooth bump functions with paracompactness.
>
> **Why needed:** The basic technical tool for gluing local constructions on a manifold.
>
> > [!note]- Full proof
> > See standard references (e.g., Lee's *Smooth Manifolds*, Chapter 2). The construction proceeds: (i) refine the given cover to a locally finite cover by precompact coordinate charts (using paracompactness); (ii) for each chart in the locally finite cover, build a smooth bump function supported in it; (iii) sum the bumps and normalize. Details omitted.

> [!note]- Lemma 2: Trivial connection on a trivial bundle
> **Statement:** On the trivial bundle $E = M \times \mathbb{R}^K$, the operator $\nabla\sigma := d\sigma$ (componentwise exterior derivative of the $\mathbb{R}^K$-valued function $\sigma$) is a connection.
>
> **Hint:** $\mathbb{R}$-linearity is clear; Leibniz follows from the Leibniz rule for $d$ on each component.
>
> **Why needed:** Provides the local input for the gluing construction.
>
> > [!note]- Full proof
> > For $\sigma : M \to \mathbb{R}^K$ a smooth section, $d\sigma : M \to \mathbb{R}^K \otimes T^*M$ is the standard differential, taking values in $E \otimes T^*M = (M \times \mathbb{R}^K) \otimes T^*M$. $\mathbb{R}$-linearity is the linearity of $d$ in $\sigma$ on the level of functions. Leibniz: $\nabla(f\sigma) = d(f\sigma) = (df)\sigma + f\,d\sigma = (df)\sigma + f\nabla\sigma$ in the bundle setting (the wedge convention $\sigma \otimes df$ vs $(df)\sigma$ is a matter of notation). ✓

> [!note]- Lemma 3: Difference of connections is tensorial
> **Statement:** If $\nabla_1, \nabla_2$ are two connections on $E$, then $D := \nabla_2 - \nabla_1 : \Gamma(E) \to \Gamma(E \otimes T^*M)$ is $C^\infty(M)$-linear, hence a tensor in $\Gamma(\mathrm{End}(E) \otimes T^*M)$.
>
> **Hint:** Compute $D(f\sigma)$ using Leibniz on each connection.
>
> **Why needed:** Establishes that the space of connections is an affine space (the *difference* lies in a vector space).
>
> > [!note]- Full proof
> > $D(f\sigma) = \nabla_2(f\sigma) - \nabla_1(f\sigma) = [f\nabla_2\sigma + \sigma \otimes df] - [f\nabla_1\sigma + \sigma \otimes df] = f\nabla_2\sigma - f\nabla_1\sigma = f(\nabla_2 - \nabla_1)\sigma = fD\sigma$. So $D$ is $C^\infty(M)$-linear in $\sigma$. By the standard correspondence between $C^\infty(M)$-linear maps $\Gamma(E) \to \Gamma(E \otimes T^*M)$ and sections of $\mathrm{End}(E) \otimes T^*M$, $D$ corresponds to such a tensor.

---

# Formal Proof

> [!note]- Complete formal proof
> **Existence.** Let $E \to M$ be a smooth vector bundle over a paracompact manifold.
>
> *Step 1.* Choose an open cover $\{U_\alpha\}$ of $M$ trivializing $E$, with trivializations $\Phi_\alpha : E|_{U_\alpha} \to U_\alpha \times \mathbb{R}^K$.
>
> *Step 2.* By Lemma 1, choose a smooth partition of unity $\{\rho_\alpha\}$ subordinate to $\{U_\alpha\}$: $\rho_\alpha \in C^\infty(M, [0, 1])$ with $\mathrm{supp}(\rho_\alpha) \subset U_\alpha$, the supports forming a locally finite family, and $\sum_\alpha\rho_\alpha \equiv 1$ on $M$.
>
> *Step 3.* On each $U_\alpha$, define the trivial connection $\nabla^{(\alpha)} : \Gamma(E|_{U_\alpha}) \to \Gamma((E \otimes T^*M)|_{U_\alpha})$ via the trivialization $\Phi_\alpha$, by Lemma 2: $\nabla^{(\alpha)}\sigma = \Phi_\alpha^{-1}(d(\Phi_\alpha\sigma))$ for $\sigma \in \Gamma(E|_{U_\alpha})$, where $d$ is componentwise exterior derivative in $\mathbb{R}^K$.
>
> *Step 4.* Define $\nabla : \Gamma(E) \to \Gamma(E \otimes T^*M)$ by
> $$\nabla\sigma := \sum_\alpha\rho_\alpha\nabla^{(\alpha)}\sigma,$$
> where the convention is that $\rho_\alpha\nabla^{(\alpha)}\sigma$ is interpreted as $\rho_\alpha$ times the *restriction* $\nabla^{(\alpha)}(\sigma|_{U_\alpha})$, extended by zero outside $U_\alpha$ (zero because $\rho_\alpha = 0$ there, so the product is zero). The sum is locally finite (only finitely many $\rho_\alpha(p) \ne 0$ for each $p$), so $\nabla\sigma$ is smooth.
>
> *Step 5.* Verify Leibniz. For $f \in C^\infty(M)$:
> $$\nabla(f\sigma) = \sum_\alpha\rho_\alpha\nabla^{(\alpha)}(f\sigma) = \sum_\alpha\rho_\alpha[\sigma \otimes df + f\nabla^{(\alpha)}\sigma] = \sigma \otimes df \cdot \sum_\alpha\rho_\alpha + f\sum_\alpha\rho_\alpha\nabla^{(\alpha)}\sigma = \sigma \otimes df + f\nabla\sigma,$$
> using $\sum_\alpha\rho_\alpha = 1$ in the last step. ✓
>
> *Step 6.* $\mathbb{R}$-linearity is immediate from $\mathbb{R}$-linearity of each $\nabla^{(\alpha)}$.
>
> Hence $\nabla$ is a connection on $E$, and connections exist.
>
> **Affine-space structure.** Let $\nabla_1, \nabla_2$ be two connections on $E$. By Lemma 3, $D := \nabla_2 - \nabla_1 \in \Gamma(\mathrm{End}(E) \otimes T^*M) = \Omega^1(M, \mathrm{End}(E))$.
>
> Conversely, given any $D \in \Omega^1(M, \mathrm{End}(E))$ and any connection $\nabla_1$, the operator $\nabla_1 + D : \sigma \mapsto \nabla_1\sigma + D\sigma$ satisfies Leibniz: $(\nabla_1 + D)(f\sigma) = \nabla_1(f\sigma) + D(f\sigma) = f\nabla_1\sigma + \sigma \otimes df + fD\sigma = f(\nabla_1 + D)\sigma + \sigma \otimes df$. ✓
>
> Hence the space $\mathcal{A}(E)$ of connections is an affine space modelled on $\Omega^1(M, \mathrm{End}(E))$. ▪

---

# Cross-Field Exercise Suggestions

**Riemannian geometry: existence of Riemannian metrics.** The same partition-of-unity technique proves: every paracompact smooth manifold admits a Riemannian metric. Locally in each chart use the standard Euclidean metric, glue via a partition of unity. The averaged metric is positive-definite because each summand is positive semi-definite and at every point at least one summand is strictly positive. This is the "metric version" of the present theorem.

**Hermitian-bundle existence.** Same technique gives: every complex vector bundle on a paracompact manifold admits a hermitian metric. The partition-of-unity average of trivial hermitian metrics on patches is again hermitian (positivity is preserved). Hence the structure-group reduction $\mathrm{GL}(K, \mathbb{C}) \to U(K)$ is *always* possible — the *non-existence* would require a bundle on a non-paracompact base.

**Existence of orientations and spin structures.** Orientations are global sections of a $\mathbb{Z}/2$-bundle over $M$ — they exist iff the bundle is trivial, which is an obstruction-theoretic condition (the first Stiefel-Whitney class). Spin structures exist iff the second Stiefel-Whitney class vanishes. The partition-of-unity machinery does *not* prove the existence of these structures unconditionally — they have *real* topological obstructions, unlike connections and metrics.

**Yang-Mills moduli space.** The fact that $\mathcal{A}(E)$ is an affine space (rather than just a topological space) makes the *moduli space* $\mathcal{M}(E) = \mathcal{A}(E)/\mathcal{G}(E)$ amenable to analytic study. The tangent space at a point $[\nabla]$ in the moduli space is the quotient of $\Omega^1(M, \mathrm{End}(E))$ (deformations of $\nabla$) by the image of the gauge-group action — a finite-dimensional vector space in good cases. This is the foundation of all moduli-space constructions in gauge theory: instanton moduli spaces (Donaldson), Seiberg-Witten moduli spaces, etc.

---

# Bridges

- **[[Def - Connection on a Vector Bundle|Connection on a Vector Bundle]]** — This theorem is the fundamental existence result for the very object defined there: every vector bundle admits a connection. Without this theorem, one might wonder whether connections are a generic feature of geometry or a special structure requiring extra hypotheses; the answer is that they are generic.

- **Existence of Riemannian Metrics** *(from [[Riemannian Geometry I — Connections and Covariant Differentiation]])* — A parallel result with the same proof technique. Every paracompact manifold has a Riemannian metric. The proof: trivial metric on each chart (Euclidean), glue via partition of unity, verify positivity is preserved. The two existence theorems sit naturally side by side.

- **[[Riemannian Geometry I — Connections and Covariant Differentiation|Levi-Civita connection]]** — Once a metric is chosen on $TM$, the *Levi-Civita connection* is *uniquely* characterised among connections by metric-compatibility and torsion-freeness. The present theorem gives existence in general; the Koszul formula gives the unique metric-compatible torsion-free connection in particular.

- **Moduli space of connections** *(from Gauge Theory)* — The affine-space structure of $\mathcal{A}(E)$ is what makes the moduli space $\mathcal{M}(E) = \mathcal{A}(E)/\mathcal{G}(E)$ tractable. The gauge group $\mathcal{G}(E)$ acts on $\mathcal{A}(E)$ by translation (in the affine sense), and the quotient — when well-defined (e.g., when restricted to irreducible connections) — has the structure of a smooth finite-dimensional manifold in many important cases. This is the technical foundation of **Donaldson theory** (instanton moduli on 4-manifolds), **Seiberg-Witten theory**, and all of moduli-space-based gauge theory.

---

# Unlocked by This

> [!tip] Chern-Weil Theory and Connection-Independence of Characteristic Classes *(from Algebraic Topology)*
> The existence of connections lets you *compute* Chern classes via curvature. The affine-space structure (plus the Bianchi identity) lets you prove that the resulting cohomology classes are *independent of which connection you chose* — the cornerstone of Chern-Weil theory. Specifically, if $\nabla_t = \nabla_0 + tD$ is a one-parameter family of connections, the curvature $F_t$ varies smoothly, and $\int\mathrm{tr}(F_t^k)$ is constant in $t$ modulo exact forms — by an explicit transgression formula. The existence and affineness theorems combine to give the connection-independence of characteristic classes.

> [!tip] Moduli of Yang-Mills Connections *(from Gauge Theory)*
> The Yang-Mills moduli space $\mathcal{M}_{\mathrm{YM}}(P) = \{\nabla : d_\nabla\star F_\nabla = 0\}/\mathcal{G}(P)$ — connections satisfying the Yang-Mills equations modulo gauge equivalence — is a finite-dimensional manifold (with singularities at reducible connections) on closed 4-manifolds. Its topology encodes deep information about the underlying 4-manifold: **Donaldson invariants** of 4-manifolds are constructed by integrating over the Yang-Mills moduli space, and they detect smooth structures invisible to topology. The affine structure of $\mathcal{A}(P)$ from the present theorem is what makes the moduli space's local analysis tractable.
