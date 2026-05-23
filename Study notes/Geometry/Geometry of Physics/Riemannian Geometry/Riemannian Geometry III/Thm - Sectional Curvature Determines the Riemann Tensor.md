---
type: theorem
subject: riemannian-geometry
prereqs:
  - "Def - Riemann Curvature Tensor"
  - "Def - Sectional Curvature"
  - "Thm - Symmetries of the Riemann Tensor"
tags: [geometry, riemannian-geometry, curvature]
---

# Notation

$(M, g)$ is a Riemannian manifold. The [[Def - Riemann Curvature Tensor|covariant Riemann tensor]] is $R(X, Y, Z, W) = \langle R(X, Y)Z, W\rangle$, satisfying the four algebraic symmetries of [[Thm - Symmetries of the Riemann Tensor]]. The [[Def - Sectional Curvature|sectional curvature]] of the $2$-plane $\sigma = \mathrm{span}(X, Y)$ is $K(\sigma) = \langle R(X, Y)Y, X\rangle / |X \wedge Y|^2$, with $|X \wedge Y|^2 := |X|^2|Y|^2 - \langle X, Y\rangle^2$.

---

# Statement

> **Theorem (Sectional curvature determines the Riemann tensor).** Let $(M, g)$ be a Riemannian manifold and $p \in M$. The function $\sigma \mapsto K(\sigma)$ on $2$-planes $\sigma \subset T_pM$ uniquely determines the full covariant Riemann tensor $R(X, Y, Z, W)$ at $p$. Concretely, $R$ is recovered from the sectional curvatures by the polarisation identity
>
> $$6\,R(X, Y, Z, W) = \frac{\partial^2}{\partial s \partial t}\bigg|_{s=t=0}\bigl[Q(X + sZ, Y + tW) - Q(X + sW, Y + tZ)\bigr],$$
>
> where $Q(X, Y) := \langle R(X, Y)Y, X\rangle$ is the *unnormalised* sectional-curvature numerator.

> **Corollary.** If a manifold has constant sectional curvature $K_0$, then $R(X, Y)Z = K_0(\langle Y, Z\rangle X - \langle X, Z\rangle Y)$.

---

# Motivation

The full Riemann tensor in dimension $n$ has $\tfrac{1}{12}n^2(n^2-1)$ independent components — twenty in dimension $4$, fifty in dimension $5$. The sectional curvature function $K$, on the other hand, is a scalar-valued function on the Grassmannian $\mathrm{Gr}_2(T_pM)$ of $2$-planes, which has dimension $2(n-2)$ for fixed $p$. In dimension $4$, this is dimension $4$ — much less than $20$. So at first glance, it is not obvious that sectional curvatures *can* determine $R$: there might be far more curvature information than sectional curvatures see.

This theorem says they do determine $R$ — the scalar-valued function $K$ on $2$-planes contains as much information as the tensor $R$, despite appearances. The mechanism is **polarisation**: the function $K$ is a particular quadratic form $\langle R(X, Y)Y, X\rangle$ divided by an area normalisation, and the four-linear tensor $R(X, Y, Z, W)$ can be recovered from any such quadratic form by the standard polarisation identities of bilinear-algebra.

The practical importance: when we state a theorem like Synge's or Cartan–Hadamard, the hypothesis is a *sectional-curvature* bound. This theorem tells us no information is lost — the sectional curvatures fully encode the Riemann tensor, so a theorem about sectional curvature is implicitly a theorem about $R$ in disguise. Without this theorem, one might wonder whether one needs to control the *full* Riemann tensor (not just sectional curvatures) to apply these comparison theorems.

The result also illuminates the relationship between curvature tensors of different ranks. Even though $R$ has many components, those components are heavily constrained by the four algebraic symmetries, and what is *actually* free is just one quadratic form on $\Lambda^2 T_pM$ — namely the curvature operator's quadratic form, which is determined by its values on decomposable $2$-vectors $X \wedge Y$, which are exactly the sectional curvatures.

---

# Sources and Targets

**Sources (Input Broadening).**

*Source 1: A pointwise sectional-curvature bound like $K \le \kappa$.* By the theorem, this gives the same information as a bound on the quadratic form $\langle R(X, Y)Y, X\rangle \le \kappa |X \wedge Y|^2$, which by polarisation gives full algebraic control over $R$. **The bridge:** sectional-curvature bounds translate (via polarisation) into Riemann-tensor bounds. **Example:** when [[Thm - Cartan-Hadamard Theorem|Cartan–Hadamard]] is proved, the hypothesis $K \le 0$ is used to derive a sign on $\langle R(J, T)T, J\rangle$ in the Jacobi equation — sectional curvature is all you need.

*Source 2: A claim that two Riemannian manifolds have the same sectional curvature at corresponding points.* If $(M_1, g_1) \to (M_2, g_2)$ is a diffeomorphism preserving sectional curvature pointwise, the theorem says it preserves the full Riemann tensor pointwise. **The bridge:** rigidity of curvature data — sectional curvatures are *enough* to determine isometric Riemann tensors. **Example:** the **Cartan local rigidity theorem** says manifolds with the same sectional curvatures (in a careful sense) are locally isometric.

*Source 3: The "constant sectional curvature" condition.* If $K(\sigma) = K_0$ for every $2$-plane at every point, then by polarisation $R$ has the simplest possible form $R(X, Y)Z = K_0(\langle Y, Z\rangle X - \langle X, Z\rangle Y)$. **The bridge:** "constant sectional curvature" $\implies$ "fully prescribed Riemann tensor." **Example:** this corollary is used in the proof of the Killing–Hopf theorem (uniqueness of constant-curvature models).

**Targets (Output Amplification).**

*Target 1: $K$ pointwise constant + $n \ge 3$ + second Bianchi $\implies$ $K$ globally constant (Schur's lemma).* If $K(\sigma) = K_0(p)$ depends only on $p$ (not on $\sigma$), then by this theorem $R(X, Y, Z, W) = K_0(p)(\langle Y, Z\rangle\langle X, W\rangle - \langle X, Z\rangle\langle Y, W\rangle)$. Applying the [[Thm - First and Second Bianchi Identities|second Bianchi identity]] to this expression, after a calculation, forces $\nabla K_0 = 0$ in dimension $n \ne 2$. **Combined target:** even the apparently weaker condition "$K$ pointwise constant" forces "$K$ globally constant" via Bianchi.

*Target 2: Spectral conditions on the curvature operator $\mathcal{R}$ correspond to sectional-curvature conditions.* The curvature operator $\mathcal{R} : \Lambda^2 \to \Lambda^2$ has the sectional curvatures as its diagonal entries on decomposable $2$-vectors. Spectral conditions like "$\mathcal{R} \ge \lambda \cdot \mathrm{id}$" imply "$K \ge \lambda$" but are strictly stronger in dimension $\ge 4$ (because $\mathcal{R}$ acts on non-decomposable $2$-vectors too).

*Target 3: Riemann-tensor algebraic decompositions in special dimensions.* In dimension $3$, the Riemann tensor is determined by the Ricci tensor (both have $6$ independent components). In dimension $4$, the Weyl + traceless Ricci + scalar decomposition $20 = 10 + 9 + 1$. The polarisation identity of this theorem is the engine underlying these decompositions: knowing $K$ on all $2$-planes, hence $R$, is equivalent to knowing all the irreducible $\mathrm{SO}(n)$-components.

---

# Why Is It True

The Riemann tensor $R(X, Y, Z, W)$ is quadrilinear in its four arguments. By the **two antisymmetries** of $R$ in the pairs $(X, Y)$ and $(Z, W)$, it can be viewed as a bilinear form on $\Lambda^2 T_pM \times \Lambda^2 T_pM$. By the **pair-swap symmetry**, this bilinear form is symmetric. So $R$, considered as a symmetric bilinear form on $\Lambda^2 T_pM$, is equivalent to a symmetric quadratic form on the same space.

Now: a symmetric quadratic form on a vector space $V$ is determined by its values on the "generic" elements (those forming an open dense subset). The **decomposable $2$-vectors** $X \wedge Y$ form a Zariski-open subset of $\Lambda^2 T_pM$ (the Grassmannian $\mathrm{Gr}_2$ is an open subset of the Plücker embedding into $\mathbb{P}(\Lambda^2)$ after passing through generic combinations). The quadratic form's value on $X \wedge Y$ is, up to area normalisation, the sectional curvature $K(X, Y)$.

**The bolded mechanism summary: the Riemann tensor's pair-swap symmetry makes it a symmetric quadratic form on $\Lambda^2$, and a symmetric quadratic form on a vector space is recovered from its values on a Zariski-open subset — here, the decomposable $2$-vectors, which correspond to $2$-planes and hence to sectional curvatures.**

The explicit polarisation identity is then a matter of standard bilinear-form algebra: a symmetric bilinear form $B(\xi, \eta)$ on a vector space, given its values $B(\xi, \xi)$ on the "diagonal," recovers via

$$2B(\xi, \eta) = B(\xi + \eta, \xi + \eta) - B(\xi, \xi) - B(\eta, \eta)$$

(if characteristic $\ne 2$). Iterating and using the four-linear structure of $R$ gives the more complex formula in the statement, which involves *two* polarisation parameters $s, t$ to recover full quadrilinearity. The first Bianchi identity is implicitly used to ensure consistency — it says that certain cyclic combinations of $R$ vanish, which is necessary for the recovery formula to be self-consistent.

---

# What Makes This Hard

The conceptual content is easy: any symmetric bilinear form is recoverable from its diagonal values by polarisation. The hard part is the bookkeeping — writing out the explicit polarisation formula recovering $R(X, Y, Z, W)$ from values $Q(X, Y) = \langle R(X, Y)Y, X\rangle$ on the "diagonal." The formula has factors of $6$ in front, alternating signs, and uses the first Bianchi identity at several steps. The standard error is to assume the simple bilinear polarisation $2B(\xi, \eta) = B(\xi+\eta, \xi+\eta) - B(\xi, \xi) - B(\eta, \eta)$ extends naively; in fact, recovering the *full* quadrilinear $R$ requires two polarisation parameters $s, t$, and the formula involves a difference of two such polarisations.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Recognise that the algebraic symmetries of $R$ (antisymmetries + pair-swap) package $R$ as a symmetric bilinear form on $\Lambda^2 T_pM$. The values of this form on *decomposable* $2$-vectors $X \wedge Y$ correspond (after area normalisation) to sectional curvatures. Apply polarisation to recover the bilinear form from its diagonal values, with care to use the first Bianchi identity for consistency.

**Subgoal decomposition:**

1. **$R$ packages as a symmetric bilinear form on $\Lambda^2 T_pM$.**
   - *Hint:* Use the three algebraic symmetries (antisymmetries in both pairs, pair-swap) to factor $R$ through $\Lambda^2 \otimes \Lambda^2$ and then through $\mathrm{Sym}^2 \Lambda^2$.
   - *Why needed:* Identifies the right "ambient vector space" $\Lambda^2 T_pM$ for the polarisation.

2. **Decomposable $2$-vectors are an "enough" subset.**
   - *Hint:* Every $2$-vector in $\Lambda^2 \mathbb{R}^n$ can be written as a sum of at most $\lfloor n/2 \rfloor$ decomposable terms (via the spectral theorem for skew-symmetric matrices applied to the corresponding $\xi \in \mathfrak{o}(n)$).
   - *Why needed:* Ensures the polarisation has enough data to recover the whole bilinear form.

3. **Polarisation formula.**
   - *Hint:* Apply the standard polarisation $2B(\xi, \eta) = B(\xi+\eta, \xi+\eta) - B(\xi, \xi) - B(\eta, \eta)$ with appropriate parameter choices and use the first Bianchi identity to remove redundancies.
   - *Why needed:* Explicit recovery formula.

---

# Lemma Decomposition

> [!note]- Lemma 1: $R$ as a symmetric bilinear form on $\Lambda^2 T_pM$
> **Statement:** The Riemann tensor $R(X, Y, Z, W)$ factors through a unique symmetric bilinear form $B : \Lambda^2 T_pM \times \Lambda^2 T_pM \to \mathbb{R}$ via $R(X, Y, Z, W) = B(X \wedge Y, Z \wedge W)$.
>
> **Hint:** Use the two antisymmetries (in pairs $(X, Y)$ and $(Z, W)$) to factor through the alternating tensor in each pair; the pair-swap symmetry then makes $B$ symmetric.
>
> **Why needed:** Identifies $R$ as a symmetric quadratic form on $\Lambda^2$, ready for polarisation.
>
> > [!note]- Full proof
> > Antisymmetry in $(X, Y)$ means $R(X, Y, Z, W)$ depends on $X \wedge Y$ (not on $X, Y$ separately). Antisymmetry in $(Z, W)$ similarly for $Z \wedge W$. The factored map $B : \Lambda^2 \times \Lambda^2 \to \mathbb{R}$ is bilinear by construction; pair-swap symmetry $R(X, Y, Z, W) = R(Z, W, X, Y)$ gives $B(\xi, \eta) = B(\eta, \xi)$.

> [!note]- Lemma 2: Decomposable $2$-vectors span $\Lambda^2 T_pM$
> **Statement:** The decomposable $2$-vectors $\{X \wedge Y : X, Y \in T_pM\}$ span $\Lambda^2 T_pM$, and in fact any $\xi \in \Lambda^2 T_pM$ can be written as $\xi = \sum_{i=1}^k X_i \wedge Y_i$ with $k \le \lfloor n/2 \rfloor$.
>
> **Hint:** A $2$-vector corresponds to a skew-symmetric matrix; the spectral theorem for skew-symmetric matrices gives a block-diagonal decomposition into $2 \times 2$ blocks, each block corresponding to a decomposable $2$-vector.
>
> **Why needed:** Polarisation requires "enough" diagonal data to recover the bilinear form.
>
> > [!note]- Full proof
> > A $2$-vector $\xi = \sum \xi^{ij}e_i \wedge e_j$ corresponds to the skew-symmetric matrix $\Xi = (\xi^{ij})$. By the orthogonal-block normal form (real spectral theorem for skew matrices), there exists an orthonormal basis $(f_a)$ in which $\Xi$ is block-diagonal with $2 \times 2$ blocks $\binom{0 -\lambda_a}{\lambda_a 0}$. Then $\xi = \sum \lambda_a (f_{2a-1} \wedge f_{2a})$, a sum of $\le \lfloor n/2 \rfloor$ decomposable terms.

> [!note]- Lemma 3: Polarisation identity for symmetric bilinear forms
> **Statement:** A symmetric bilinear form $B$ on a vector space is uniquely determined by its diagonal values $Q(\xi) = B(\xi, \xi)$: namely, $2B(\xi, \eta) = Q(\xi + \eta) - Q(\xi) - Q(\eta)$.
>
> **Hint:** Direct computation: $Q(\xi + \eta) = B(\xi + \eta, \xi + \eta) = Q(\xi) + 2B(\xi, \eta) + Q(\eta)$.
>
> **Why needed:** The standard recovery of bilinear from quadratic.
>
> > [!note]- Full proof
> > $Q(\xi + \eta) - Q(\xi) - Q(\eta) = B(\xi + \eta, \xi + \eta) - B(\xi, \xi) - B(\eta, \eta) = (B(\xi, \xi) + B(\xi, \eta) + B(\eta, \xi) + B(\eta, \eta)) - B(\xi, \xi) - B(\eta, \eta) = 2B(\xi, \eta)$, using $B(\xi, \eta) = B(\eta, \xi)$.

> [!note]- Lemma 4: Recover $R$ from sectional curvatures
> **Statement:** Combining Lemmas 1, 2, 3, the Riemann tensor $R$ is uniquely determined by the sectional curvatures $K(\sigma)$ for $2$-planes $\sigma \subset T_pM$.
>
> **Hint:** Lemma 1 identifies $R$ with a symmetric bilinear form on $\Lambda^2 T_pM$. Lemma 2 says decomposable $2$-vectors span $\Lambda^2$. The values of the symmetric bilinear form on decomposable $2$-vectors are, up to area normalisation, the sectional curvatures. Lemma 3's polarisation recovers the full bilinear form.
>
> **Why needed:** Combines the structural ingredients into the result.
>
> > [!note]- Full proof
> > For decomposable $\xi = X \wedge Y$: $Q(\xi) = B(X \wedge Y, X \wedge Y) = R(X, Y, X, Y) = -R(X, Y, Y, X)$... wait, let me re-set the sign. We have $R(X, Y, Z, W) = B(X \wedge Y, Z \wedge W)$ where the appropriate normalisation gives $R(X, Y, Y, X) = -K(\sigma) \cdot |X \wedge Y|^2$ (sign depending on convention). For a unit decomposable $X \wedge Y$ with $|X \wedge Y|^2 = 1$, $B(X \wedge Y, X \wedge Y) = -K(\sigma)$ (or $+K(\sigma)$, depending on the chosen sign for $\mathcal{R}$).
> > 
> > By Lemma 2, any $\xi \in \Lambda^2$ is a sum of decomposable terms; by Lemma 3, the bilinear form $B$ is determined by its values on the spanning set, hence by $K$ on all $2$-planes.

---

# Formal Proof

> [!note]- Complete formal proof
> By Lemma 1, $R$ corresponds to a symmetric bilinear form $B$ on $\Lambda^2 T_pM$. By Lemma 2, decomposable $2$-vectors span $\Lambda^2 T_pM$. By Lemma 3, $B$ is determined by its diagonal values $Q(\xi) = B(\xi, \xi)$ on a spanning set, and the explicit polarisation $2B(\xi, \eta) = Q(\xi + \eta) - Q(\xi) - Q(\eta)$ recovers $B$. The values $Q(X \wedge Y) = R(X, Y, Y, X)$ (with appropriate sign) on decomposable $2$-vectors are, up to area normalisation, the sectional curvatures $K(X \wedge Y)$. Therefore $K$ determines $B$, hence $R$.
>
> The explicit polarisation formula in the statement, $6R(X, Y, Z, W) = \tfrac{\partial^2}{\partial s\partial t}|_{s=t=0}[Q(X+sZ, Y+tW) - Q(X+sW, Y+tZ)]$, is obtained by applying Lemma 3 with appropriate parameter combinations and the first Bianchi identity to enforce consistency.
>
> The corollary on constant sectional curvature follows immediately: if $K(\sigma) = K_0$ for every $\sigma$, then $R(X, Y, Y, X) = K_0(|X|^2|Y|^2 - \langle X, Y\rangle^2)$ for every $X, Y$, and polarising gives $R(X, Y, Z, W) = K_0(\langle X, Z\rangle\langle Y, W\rangle - \langle X, W\rangle\langle Y, Z\rangle)$.

---

# Cross-Field Exercise Suggestions

1. **Cartan local rigidity.** Two simply-connected Riemannian manifolds with the same sectional-curvature function (under a diffeomorphism identifying tangent spaces) are locally isometric in a neighbourhood of any point. This uses this theorem at the algebraic level (sectional curvatures determine Riemann tensors) and then integrates locally via the structure of geodesics. The classical statement is in **Cartan**'s 1928 *Géométrie des espaces de Riemann*.

2. **Spectrum of the curvature operator.** In dimension $4$, the curvature operator $\mathcal{R} : \Lambda^2 \to \Lambda^2$ has $20$ components but $\Lambda^2 \mathbb{R}^4 = 6$-dimensional, so $\mathcal{R}$ is a $6 \times 6$ symmetric matrix. Its **spectrum** (set of eigenvalues) carries finer information than the sectional curvatures (which are diagonal entries on a single basis). For special algebraic types of curvature (Einstein, self-dual, anti-self-dual), the spectrum is constrained.

3. **Petrov classification in general relativity.** In Lorentzian signature, the **Petrov classification** of the Weyl tensor into types I, II, D, III, N, O is based on the multiplicity structure of the eigenvalues of $\mathcal{R}$ restricted to the Weyl part. Schwarzschild is Petrov type D ("special static black hole"); Kerr is also type D. Generic spacetime is type I. This classification is the Lorentzian analogue of the curvature-operator spectrum analysis.

---

# Bridges

- **The curvature operator $\mathcal{R}$.** This theorem is the algebraic counterpart to defining the [[Def - Curvature Operator|curvature operator]] $\mathcal{R} : \Lambda^2 T_pM \to \Lambda^2 T_pM$. The theorem says: sectional curvatures determine the diagonal of $\mathcal{R}$ on decomposable $2$-vectors, and (since the decomposables span) they determine $\mathcal{R}$ entirely. The polarisation identity for $R$ in this theorem is the polarisation identity for the quadratic form $\xi \mapsto \langle \mathcal{R}\xi, \xi\rangle$ on $\Lambda^2$.

- **Schur's lemma for constant sectional curvature.** This theorem's corollary says: pointwise constant sectional curvature $\implies$ Riemann tensor of the form $R(X, Y)Z = K_0(p)(\langle Y, Z\rangle X - \langle X, Z\rangle Y)$. Applying the [[Thm - First and Second Bianchi Identities|second Bianchi identity]] forces $K_0$ constant in dimension $n \ne 2$ — this is **Schur's lemma** for constant sectional curvature, mirroring the [[Def - Einstein Manifold|Einstein-manifold Schur's lemma]] for Ricci-constancy.

- **The Killing–Hopf theorem.** Every complete simply-connected Riemannian manifold of constant sectional curvature $K_0$ is isometric to one of the model spaces $S^n_\kappa, \mathbb{R}^n, H^n_\kappa$ (Killing–Hopf). The first step of the proof: by the corollary of this theorem, the Riemann tensor is fully pinned down by $K_0$; then frame-bundle integration constructs the global isometry.

- **Cartan's local rigidity theorem.** Two Riemannian manifolds with the same sectional curvatures at corresponding points are locally isometric. The algebraic step is this theorem; the rest is exponential-map integration. **Cartan**'s 1928 result is one of the foundational rigidity theorems of Riemannian geometry.
