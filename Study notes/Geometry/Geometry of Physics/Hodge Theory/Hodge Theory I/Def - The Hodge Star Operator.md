---
type: definition
subject: hodge-theory
prereqs:
  - "Def - Differential k-Form on a Manifold"
  - "Def - Riemannian Metric"
  - "Def - Riemannian Volume Form"
  - "Def - Orientation of a Smooth Manifold"
  - "Def - The Wedge Product on a Manifold"
  - "Def - The L2 Inner Product on Differential Forms"
tags: [geometry, hodge-theory, riemannian-geometry, differential-forms]
---

# Notation

Let $(M, g)$ be a smooth oriented (pseudo-)Riemannian manifold of dimension $n$, with signature $(n - s, s)$ ($s = 0$ in the Riemannian case). The [[Def - Riemannian Volume Form|Riemannian volume form]] is $\operatorname{vol}_n$ (equivalently $\operatorname{vol}_g$, $\operatorname{vol}_M$); on an oriented orthonormal coframe $(\sigma^1, \dots, \sigma^n)$, $\operatorname{vol}_n = \sigma^1\wedge\cdots\wedge\sigma^n$. The Hodge star is $\star : \Omega^k(M) \to \Omega^{n-k}(M)$. We use the pointwise inner product $\langle\alpha,\beta\rangle_g$ on forms induced by $g$ (see [[Def - The L2 Inner Product on Differential Forms]]). For a multi-index $I = (i_1, \dots, i_k)$ with $i_1 < \cdots < i_k$, $\sigma^I = \sigma^{i_1}\wedge\cdots\wedge\sigma^{i_k}$; the **complementary multi-index** $J = I^c$ consists of the indices $\{1, \dots, n\} \setminus I$, arranged in increasing order.

> [!warning] Convention: orientation sign
> The sign of $\star\sigma^I$ depends on the parity of the permutation $(I, J)$ taking $(1, 2, \dots, n)$ to the concatenated tuple $(i_1, \dots, i_k, j_1, \dots, j_{n-k})$. Standard convention: this sign is $+1$ when $(I, J)$ is a positive permutation, $-1$ otherwise. Some sources (notably some physics texts) reverse the sign on the volume form, which propagates through every formula — fix one convention up-front. We use Frankel's convention: $\sigma^I \wedge \sigma^J = \mathrm{sgn}(I, J)\operatorname{vol}_n$, so $\star\sigma^I = \mathrm{sgn}(I, J)\sigma^J$ in the Riemannian case.

---

# Axiom Motivation

The Hodge star is the unique pointwise $\mathbb{R}$-linear isomorphism $\Omega^k(M) \to \Omega^{n-k}(M)$ that satisfies a single defining identity. Three structural pressures force the definition.

**Why pair up degrees $k$ and $n - k$?** On an $n$-dimensional vector space, $\dim\Lambda^k V^* = \binom{n}{k} = \binom{n}{n-k} = \dim\Lambda^{n-k}V^*$. So $\Lambda^k V^*$ and $\Lambda^{n-k}V^*$ have the same [[Def - Dimension|dimension]] and are abstractly isomorphic, but not canonically — the isomorphism depends on extra structure. The Hodge star is precisely the canonical isomorphism *given* a metric and an orientation: with the metric and orientation, we can pair every $k$-form with an $(n-k)$-form, and the pairing inherits the metric's structure. Without a metric, the natural object pairing degree $k$ with degree $n-k$ is the *densitized* $(n-k)$-form via integration $\alpha \wedge \beta = (\text{scalar density})\operatorname{vol}$ — but the "scalar density" depends on a volume form, and a volume form requires an orientation and a metric (or some other choice). So $\star$ is what makes the metric's information into a concrete isomorphism.

**Why the defining identity $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle\operatorname{vol}_n$?** The right side is a metric-dependent and orientation-dependent function on $M$ times the volume form; the left side is a wedge product of forms. The identity asks: which $(n-k)$-form $\star\beta$ makes the wedge product reproduce the inner product? Test the identity on the basis of $\Omega^k$: for $\alpha = \sigma^I$, $\langle\sigma^I, \beta\rangle = \beta_I$ (the $I$-component of $\beta$), and the identity becomes $\sigma^I \wedge \star\beta = \beta_I\operatorname{vol}_n$. This pins down $\star\beta$ component-by-component: the coefficient of $\sigma^J$ (complementary to $I$) in $\star\beta$ is exactly $\pm\beta_I$, with the sign determined by orientation. So the identity determines $\star\beta$ uniquely.

Equivalently, the identity is the statement that the metric inner product $\langle\alpha,\beta\rangle$ and the integration pairing $\int_M \alpha\wedge\star\beta$ are the *same* operation expressed two ways. The Hodge star is what allows us to convert one into the other, and this is the operational meaning of "the metric and the volume form together determine $\star$."

**What if we strengthen — demand $\star$ commute with $d$?** Then we get an extra constraint: $d \star = \pm \star d$, which is *not* generally true. The Hodge star does not commute with the exterior derivative; the relationship is more subtle, mediated by the [[Def - The Codifferential|codifferential]] $\delta = \pm\star d\star$. If we demanded $d\star = \star d$, we would force a flat-metric condition. The actual relation between $d$ and $\star$ is captured by the codifferential and the [[Def - Hodge Laplacian|Hodge Laplacian]].

**What if we weaken — drop pointwise $C^\infty(M)$-linearity?** Then $\star$ could mix function coefficients in non-multiplicative ways (e.g., differentiate them), and the result would be a differential operator rather than an algebraic operation. The pointwise $C^\infty(M)$-linearity is the demand that $\star$ is an algebraic operation on forms, not a differential one — a tensor in the right sense. This is what makes $\star$ compositionally simple ($\star(f\omega) = f\star\omega$), and what lets $\star$ be defined without using any derivatives of $g$.

**What if we drop orientation?** The volume form $\operatorname{vol}_n$ requires an orientation to be well-defined (otherwise it is only defined up to sign). Without an orientation, $\star$ is only defined up to sign — equivalently, $\star\omega$ is a *pseudoform* (densitized form) rather than a true form. On a non-orientable manifold (e.g., the Möbius strip), the Hodge star produces [[Def - Pseudoform (Twisted Form)|pseudoforms]]; the Hodge Laplacian still makes sense and behaves the same way, but Poincaré duality has to be stated carefully. We assume orientation for everything in this chapter.

**What if we drop positivity?** In the pseudo-Riemannian case (Lorentzian signature), the inner product is indefinite, and the volume form is still well-defined (it requires only orientation and signature). The Hodge star is still defined by the same identity $\alpha\wedge\star\beta = \langle\alpha,\beta\rangle_g\operatorname{vol}_n$, and is still a pointwise isomorphism. The novelty is in the double star: $\star\star = (-1)^{k(n-k)+s}$ — the extra $(-1)^s$ comes from the timelike-spacelike split. In Lorentzian $4$D ($s = 1$), $\star\star = -1$ on $2$-forms, which is the key sign for self-duality.

---

# The Definition

Let $(M, g)$ be a smooth oriented (pseudo-)Riemannian $n$-manifold with volume form $\operatorname{vol}_n$. The **Hodge star operator** $\star : \Omega^k(M) \to \Omega^{n-k}(M)$ is the unique pointwise $C^\infty(M)$-linear map satisfying
$$\alpha \wedge \star\beta = \langle\alpha, \beta\rangle_g\,\operatorname{vol}_n \quad \text{for all } \alpha, \beta \in \Omega^k(M),$$
where $\langle\cdot,\cdot\rangle_g$ is the pointwise inner product on $k$-forms induced by $g$.

**Coordinate formula in an orthonormal coframe.** If $(\sigma^1, \dots, \sigma^n)$ is a positively oriented orthonormal coframe (so $g(\sigma^i, \sigma^j) = \epsilon_i\delta^{ij}$ with $\epsilon_i = \pm 1$ depending on signature, and $\operatorname{vol}_n = \sigma^1\wedge\cdots\wedge\sigma^n$), then for an increasing multi-index $I = (i_1, \dots, i_k)$,
$$\star\sigma^I = \mathrm{sgn}(I, J)\,\epsilon_I\,\sigma^J,$$
where $J = (j_1, \dots, j_{n-k})$ is the complementary increasing multi-index, $\epsilon_I = \prod_{i \in I}\epsilon_i$, and $\mathrm{sgn}(I, J) = \pm 1$ is the sign of the permutation $(1, 2, \dots, n) \mapsto (i_1, \dots, i_k, j_1, \dots, j_{n-k})$.

**Coordinate formula in a general coframe.** For $\beta = \beta_I\,dx^I$ in a general coordinate chart,
$$(\star\beta)^J = \sqrt{|g|}\,\beta_I \epsilon^{IJ}, \qquad \star\beta = \sum'_J (\star\beta)_J\,dx^J,$$
where indices are raised with $g$, $\epsilon^{IJ}$ is the Levi–Civita symbol, and the primed sum is over increasing $J$.

**Double star.** For $\omega \in \Omega^k(M)$ on an oriented (pseudo-)Riemannian $n$-manifold of signature $(n-s, s)$,
$$\star\star\omega = (-1)^{k(n-k)+s}\omega.$$
In the Riemannian case ($s = 0$) this is $(-1)^{k(n-k)}$; on Lorentzian $4$D and $2$-forms ($k = 2$, $n = 4$, $s = 1$), it is $(-1)^{4+1} = -1$.

---

# Categorical / Structural Definition

The Hodge star is the unique $C^\infty(M)$-linear map of bundles $\Lambda^k T^*M \to \Lambda^{n-k} T^*M$ extending fibrewise the linear map characterized by the following universal property: for each $p \in M$, the map $\star_p : \Lambda^k T_p^*M \to \Lambda^{n-k}T_p^*M$ is the unique linear map such that the diagram

$$\Lambda^k T_p^*M \otimes \Lambda^k T_p^*M \xrightarrow{\langle\cdot,\cdot\rangle\,\operatorname{vol}_n} \Lambda^n T_p^*M$$

factors as $\mathrm{id} \otimes \star_p$ followed by the wedge product $\Lambda^k \otimes \Lambda^{n-k} \to \Lambda^n$. In other words, the diagram

$$\begin{array}{ccc}
\Lambda^k \otimes \Lambda^k & \xrightarrow{\mathrm{id}\otimes \star} & \Lambda^k \otimes \Lambda^{n-k} \\
\downarrow{\langle,\rangle\,\operatorname{vol}_n} & & \downarrow{\wedge} \\
\Lambda^n & = & \Lambda^n
\end{array}$$

commutes. The right side, the wedge $\Lambda^k\otimes\Lambda^{n-k}\to\Lambda^n$, is a perfect pairing of one-dimensional spaces (after choosing a basis of $\Lambda^n$, i.e., choosing $\operatorname{vol}_n$ as a basis); this pairing gives an isomorphism $\Lambda^{n-k} \cong (\Lambda^k)^*$. The left side, the pointwise inner product, is also an isomorphism $\Lambda^k \cong (\Lambda^k)^*$ via $\alpha \mapsto \langle\alpha, \cdot\rangle$. Composing these two [[Def - Isomorphism|isomorphisms]] gives the Hodge star: $\Lambda^k \cong (\Lambda^k)^* \cong \Lambda^{n-k}$.

This categorical perspective makes clear that the Hodge star is essentially **the metric's identification of $\Lambda^k$ with $\Lambda^{n-k}$ via duality**. Two pieces of data — the metric (which dualizes $\Lambda^k$ with itself) and the volume form (which dualizes $\Lambda^k$ with $\Lambda^{n-k}$) — together fix the isomorphism. Neither alone suffices.

---

# Relate to Other Fields / Compression

**The cross product on $\mathbb{R}^3$ is the Hodge star.** For vectors $u, v \in \mathbb{R}^3$, take their metric duals $u^\flat, v^\flat \in \Omega^1(\mathbb{R}^3)$. The wedge $u^\flat \wedge v^\flat$ is a $2$-form, and $\star(u^\flat \wedge v^\flat) \in \Omega^1(\mathbb{R}^3)$ is a $1$-form whose metric dual is exactly $u \times v$. Component-wise: $\star(dx \wedge dy) = dz$, $\star(dy \wedge dz) = dx$, $\star(dz \wedge dx) = dy$ — these are exactly the components of $e_x \times e_y = e_z$ and cyclic permutations.

**The curl is $\star d$ in $\mathbb{R}^3$ on $1$-forms.** For a vector field $F = f_i e_i$ with dual $1$-form $F^\flat = f_i dx^i$, $dF^\flat$ is a $2$-form $\sum_{i<j}(\partial_i f_j - \partial_j f_i)dx^i\wedge dx^j$ whose $\star$ is the curl $\nabla\times F$ as a $1$-form. The divergence is $\delta = \star d\star$ on $1$-forms with a sign, recovering $\nabla\cdot F = \text{const}\cdot d^*F^\flat$.

**The Hodge star is the "musical isomorphism" extended from rank $1$ to rank $k$.** The musical isomorphism $\flat : T M \to T^*M$ ($v \mapsto g(v, \cdot)$) is the rank-$1$ version: it uses the metric to identify $TM$ with $T^*M$. The Hodge star uses the metric *together with* the volume form (orientation) to identify $\Lambda^k T^*M$ with $\Lambda^{n-k}T^*M$. Both are "the metric's identifications", but $\star$ requires the extra orientation choice because $\Lambda^k$ and $\Lambda^{n-k}$ are not the same space (only of the same dimension), whereas $TM$ and $T^*M$ are dual.

**True name:** the Hodge star is the *concrete realization* of the abstract duality $\Lambda^k V^* \cong (\Lambda^k V^*)^* \cong \Lambda^{n-k}V^*$ provided by a positive-definite inner product and an orientation on $V$. When you see "$\star$ in coordinates," you are seeing the metric's pairing $\alpha \leftrightarrow \langle\alpha,\cdot\rangle$ composed with the wedge perfect-pairing $\Lambda^k \otimes \Lambda^{n-k} \to \Lambda^n$.

---

# Examples / Corollaries

**Is an instance: $\star$ on $\mathbb{R}^3$.** With the standard Euclidean metric and orientation:
- $\star 1 = dx \wedge dy \wedge dz = \operatorname{vol}_3$
- $\star(dx) = dy \wedge dz$, $\star(dy) = dz \wedge dx$, $\star(dz) = dx \wedge dy$
- $\star(dx \wedge dy) = dz$, $\star(dy \wedge dz) = dx$, $\star(dz \wedge dx) = dy$
- $\star(dx \wedge dy \wedge dz) = 1$
All signs $+1$ because $k(n-k) + s = k(3-k) + 0$ is even for all $k$.

**Is an instance: $\star$ on $\mathbb{R}^4$ (Euclidean).** For a $2$-form $\omega = \omega_{ij}dx^i\wedge dx^j$ (with $i < j$), $\star\omega$ is also a $2$-form with components $(\star\omega)_{kl} = \frac{1}{2}\epsilon_{ijkl}\omega^{ij}$. Self-dual ($\star\omega = \omega$) and anti-self-dual ($\star\omega = -\omega$) $2$-forms decompose $\Omega^2(\mathbb{R}^4) = \Omega^2_+ \oplus \Omega^2_-$, each $3$-dimensional at each point.

**Is an instance: $\star$ on Minkowski $\mathbb{R}^{3,1}$.** With metric $g = -dt^2 + dx^2 + dy^2 + dz^2$:
- $\star 1 = -dt \wedge dx \wedge dy \wedge dz$ (timelike orientation conventionally gives a sign)
- $\star(dx \wedge dt) = -dy \wedge dz$ (the timelike index $0$ gives a factor of $\epsilon_0 = -1$)
- $\star(dx\wedge dy) = dz \wedge dt$
The signs reflect $s = 1$ in the signature; $\star\star = -1$ on $2$-forms.

**Is NOT an instance: $\star$ on a non-orientable manifold.** The Möbius strip $M$ admits a metric (any Riemannian metric on $\mathbb{R}^2$ descending to the strip) but no global orientation. The "$\star$" cannot be well-defined as a true form: locally, in one trivialization of the orientation, $\star\omega$ is one form; in the other trivialization (after going around the strip once), it is the opposite. The output is a **pseudoform**, transforming under change of orientation by an extra sign. Hodge theory on non-orientable manifolds is built using pseudoforms and twisted bundles.

**Corollary (double star).** $\star\star\omega = (-1)^{k(n-k) + s}\omega$. In Riemannian signature ($s = 0$): on $0$-forms ($k = 0$, $n - k = n$), $\star\star = 1$; on $1$-forms in $3$D ($k = 1$, $n - k = 2$), $\star\star = 1$; on $2$-forms in $4$D ($k = 2$, $n - k = 2$), $\star\star = 1$. In Lorentzian $4$D ($s = 1$): on $2$-forms, $\star\star = -1$. Verification on an orthonormal basis: $\star\star\sigma^I = \star(\mathrm{sgn}(I, J)\epsilon_I\sigma^J) = \mathrm{sgn}(I, J)\mathrm{sgn}(J, I)\epsilon_I\epsilon_J\sigma^I = \mathrm{sgn}(I,J)^2\epsilon_{\{1,\dots,n\}}\sigma^I/\epsilon_I\cdot\epsilon_I = \mathrm{sgn}(I,J)^2(-1)^s\sigma^I$. But $\mathrm{sgn}(I, J) = (-1)^{k(n-k)}\mathrm{sgn}(J, I)$ (rearranging $k$ and $n - k$ blocks), so we get $(-1)^{k(n-k)+s}\sigma^I$.

**Corollary ($\star$ is a pointwise isometry).** $\langle\star\alpha, \star\beta\rangle_g = \langle\alpha,\beta\rangle_g$ in the Riemannian case (with a sign $(-1)^s$ in the pseudo-Riemannian case). This follows from $\star\alpha\wedge\star\star\beta = \langle\star\alpha,\star\beta\rangle\operatorname{vol}_n$ combined with $\star\star\beta = \pm\beta$ and the symmetry of the wedge product. So $\star$ preserves $L^2$ norms (up to a sign): $\|\star\omega\|_{L^2} = \|\omega\|_{L^2}$.

**Corollary ($\star$ commutes with [[Def - Isometry|isometries]]).** If $F : (M, g) \to (M, g)$ is an orientation-preserving isometry, then $F^*\star = \star F^*$. This is because both sides preserve the defining identity. The corollary is used in symmetry-averaging arguments for computing harmonic forms.

**Calibration check.** If you can verify (i) $\star(dx \wedge dy) = dz$ in $\mathbb{R}^3$ (from the defining identity applied to $\alpha = dx \wedge dy$), (ii) the double-star formula $\star\star = (-1)^{k(n-k) + s}$ on $2$-forms in $4$D Riemannian (gives $+1$) and $4$D Lorentzian (gives $-1$), and (iii) the formula $\star\sigma^I = \pm\sigma^J$ with $J$ the complementary multi-index on an orthonormal coframe, you have understood the operator correctly.

---

# Unlocked by This

> [!tip] Self-Duality in 4D *(from Gauge Theory and Differential Topology)*
> The double-star formula $\star\star = +1$ on $2$-forms in $4$D Riemannian splits $\Omega^2 = \Omega^2_+ \oplus \Omega^2_-$ into the self-dual and anti-self-dual eigenspaces of $\star$, each of rank $3$ at every point. This decomposition is the entire algebraic substrate of the **self-dual / anti-self-dual instanton equations** $F_+ = 0$ or $F_- = 0$ in [[Gauge Theory IV — Yang–Mills Fields and Instantons|Yang–Mills theory]], and is what makes $4$D special in gauge theory. In other dimensions $\star$ on $2$-forms is not an involution, and no analogous decomposition exists.

> [!tip] Hodge Operators on Spinor Bundles *(from Spin Geometry)*
> On a [[Spinors and the Dirac Equation|spin manifold]], there is a parallel "spinor Hodge star" mapping spinor fields $S^+ \to S^-$ between chirality components, with analogous properties to the Hodge star on forms. The Dirac operator $D = \gamma^i\nabla_i$ acts as the spinor analogue of $d + \delta$, and the spinor Laplacian $D^2$ admits a Weitzenböck-type decomposition (the **Lichnerowicz formula**) into a rough Laplacian plus a scalar-curvature term. The structural parallel — form Hodge star and form Laplacian on one side, spinor Hodge star and Dirac operator squared on the other — is the gateway to spin geometry.

> [!tip] Hodge Theory in Lp and Sobolev Spaces *(from Functional Analysis)*
> The Hodge star extends from smooth forms to $L^p$ forms, Sobolev spaces of forms $W^{s,p}\Omega^k$, and distributional forms. The Hodge theorem in these settings becomes a statement about closed-range Fredholm operators on Hilbert spaces, with the kernel of $\Delta$ being a closed subspace and the cokernel being its orthogonal complement. This is the natural home for the analytic side of Hodge theory; the smooth-forms version is the conclusion of an elliptic-regularity argument applied to the Hilbert-space version.
