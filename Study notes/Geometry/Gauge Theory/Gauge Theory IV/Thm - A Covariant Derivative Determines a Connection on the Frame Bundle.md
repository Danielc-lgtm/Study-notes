---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Connection on a Vector Bundle"
  - "Def - Connection Matrix and Local Form of a Connection"
  - "Def - Frame Bundle of a Vector Bundle"
  - "Def - Connection on a Principal Bundle"
  - "Def - Local Connection Form and Gauge Potential"
  - "Thm - Transformation of Local Connection and Curvature Forms"
  - "Thm - Gauge Transformation Law for Connection 1-Forms"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $E \to M$ is a smooth vector bundle of rank $k$ over the field $\mathbb{K} \in \{\mathbb{R}, \mathbb{C}\}$, and $M$ is a smooth manifold of dimension $n$. Its structure group is $G = GL(k; \mathbb{K})$, an open subset of the matrix space $\operatorname{Mat}(k \times k; \mathbb{K})$, with Lie algebra $\mathfrak{g} = \mathfrak{gl}(k; \mathbb{K}) = \operatorname{Mat}(k \times k; \mathbb{K})$ under the commutator bracket $[\xi, \eta] = \xi\eta - \eta\xi$. For a matrix group, $\operatorname{Ad}_g \xi = g \xi g^{-1}$ (this page uses only this case).

The **frame bundle** $\pi \colon \operatorname{Fr}(E) \to M$ (see [[Def - Frame Bundle of a Vector Bundle]]) has as its fibre over $m \in M$ the set of ordered bases of $E_m$; a point $p \in \operatorname{Fr}(E)_m$ is written as a row $p = (p_1, \dots, p_k)$ with each $p_i \in E_m$ and $(p_1, \dots, p_k)$ a basis, equivalently as the linear isomorphism $p \colon \mathbb{K}^k \to E_m$ sending the standard basis vector $\varepsilon_j$ to $p_j$. The group $G = GL(k;\mathbb{K})$ acts on $\operatorname{Fr}(E)$ on the **right** by change of basis: for $g = (g^i{}_j) \in G$,
$$(p \cdot g)_j = \sum_{i=1}^{k} p_i\, g^i{}_j, \qquad \text{equivalently } p \cdot g = p \circ g \text{ as maps } \mathbb{K}^k \to E_m,$$
which is a free and transitive right action on each fibre, $(p \cdot g) \cdot g' = p \cdot (gg')$. This makes $\operatorname{Fr}(E)$ a principal $G$-bundle ([[Def - Principal G-Bundle]]). A **local frame** $e = (e_1, \dots, e_k)$ of $E$ over an open set $U \subseteq M$, that is, a $k$-tuple of sections of $E|_U$ forming a basis at each point, is the same datum as a **local section** $e \colon U \to \operatorname{Fr}(E)|_U$ of the frame bundle ($\pi \circ e = \operatorname{id}_U$); the two viewpoints are used interchangeably.

The right translation by $g$ is $R_g \colon \operatorname{Fr}(E) \to \operatorname{Fr}(E)$, $R_g(p) = p \cdot g$. For $\xi \in \mathfrak{g}$ the **fundamental vector field** $\xi_P$ ([[Def - Fundamental Vector Field of a Group Action]]) is
$$\xi_P(p) = \frac{d}{dt}\Big|_{t=0}\, p \cdot \exp(t\xi), \qquad \text{so on } \operatorname{Fr}(E),\ \ \xi_P(p) = \frac{d}{dt}\Big|_{t=0}\, p \cdot \exp(t\xi) = p \cdot \xi \ \text{(the row } (\textstyle\sum_i p_i\, \xi^i{}_j)_j).$$
A **connection on the principal bundle** $\operatorname{Fr}(E)$ ([[Def - Connection on a Principal Bundle]]) is a $\mathfrak{g}$-valued $1$-form $\omega \in \Omega^1(\operatorname{Fr}(E); \mathfrak{g})$ satisfying

1. $R_g^* \omega = \operatorname{Ad}_{g^{-1}} \omega$ for all $g \in G$, that is, $\omega_{p \cdot g}(dR_g\, X) = g^{-1}\, \omega_p(X)\, g$ for $X \in T_p \operatorname{Fr}(E)$;
2. $\omega(\xi_P) = \xi$ for all $\xi \in \mathfrak{g}$.

The space of all such connections is $\mathcal{A}(\operatorname{Fr}(E))$. The space of connections (covariant derivatives) on the vector bundle $E$ is $\mathcal{A}(E)$; a **connection** $\nabla$ on $E$ ([[Def - Connection on a Vector Bundle]]) is a $\mathbb{K}$-linear map $\nabla \colon \Gamma(E) \to \Omega^1(M; E)$ with $\nabla(fs) = df \otimes s + f\, \nabla s$. In a local frame $e$ its **connection matrix** $A(\nabla, e) \in \Omega^1(U; \mathfrak{gl}_k)$ (throughout we abbreviate $\mathfrak{gl}_k := \mathfrak{gl}(k;\mathbb{K}) = \mathfrak{g}$) ([[Def - Connection Matrix and Local Form of a Connection]]) is defined by
$$\nabla e_j = \sum_{i=1}^{k} e_i \otimes A(\nabla,e)^i{}_j, \qquad \text{written compactly } \nabla e = e \cdot A(\nabla, e),$$
so that a section $s|_U = \sum_j e_j\, \sigma^j = e \cdot \sigma$ (with $\sigma \colon U \to \mathbb{K}^k$) has $\nabla s|_U = e \cdot (d\sigma + A(\nabla,e)\,\sigma)$, i.e. $\nabla = d + A$ in the frame $e$.

The symbol $\frac{\nabla}{dt}$ denotes the **covariant derivative along a curve** ([[Def - Covariant Derivative along a Curve]]): for a smooth curve $c \colon I \to M$ and a section $\sigma$ of $E$ along $c$ (that is, $\sigma(t) \in E_{c(t)}$), $\frac{\nabla}{dt}\sigma$ is the unique operation that is $\mathbb{K}$-linear, satisfies the Leibniz rule $\frac{\nabla}{dt}(f\sigma) = \dot f\, \sigma + f\, \frac{\nabla}{dt}\sigma$ for $f \colon I \to \mathbb{K}$, and agrees with $\nabla_{\dot c}$ on restrictions of ambient sections, $\frac{\nabla}{dt}(\tau \circ c) = \nabla_{\dot c}\tau$ for $\tau \in \Gamma(E)$. In a local frame $\tilde e$ with connection matrix $\tilde A = A(\nabla, \tilde e)$, writing $\sigma(t) = \sum_i a^i(t)\, \tilde e_i(c(t))$,
$$\frac{\nabla}{dt}\sigma = \sum_i \Big(\dot a^i + \sum_l \tilde A^i{}_l(\dot c)\, a^l\Big)\, \tilde e_i(c). \tag{$\ast$}$$

For a curve of frames $p(t) = (p_1(t), \dots, p_k(t))$, each component $p_j(t) \in E_{c(t)}$ is a section along $c = \pi \circ p$, and we write $\frac{\nabla}{dt}p := \big(\frac{\nabla}{dt}p_1, \dots, \frac{\nabla}{dt}p_k\big)$ for the row of covariant derivatives; for a matrix $B \in \operatorname{Mat}(k \times k; \mathbb{K})$ and a row $q = (q_1, \dots, q_k)$ of vectors of $E_m$ we write $(q \cdot B)_j = \sum_i q_i\, B^i{}_j$.

The **Maurer–Cartan form** $\theta \in \Omega^1(G; \mathfrak{g})$ ([[Def - The Maurer-Cartan Form]]) is $\theta_g(w) = dL_{g^{-1}}(w)$; for the matrix group $G = GL(k;\mathbb{K})$ it is $\theta = g^{-1}\, dg$, so that for a smooth map $g \colon U \to G$ the pullback is $(g^*\theta)(v) = g^{-1}\, dg(v)$.

> [!warning] Convention: symbols across the two sources
> Haydys writes $a$ for the principal connection form and states part (a) as $e^* a = A(\nabla, e)$; Bär writes $\omega$ (and $\omega_\alpha = s_\alpha^*\omega$ for local forms). This series writes $\omega$ for the connection form on $\operatorname{Fr}(E)$. Bär's account of the connection axioms silently corrects a misprint in the source, which prints condition 1 as "$R_g^* = \operatorname{Ad}_{g^{-1}} \circ \omega$"; the correct statement is $R_g^*\omega = \operatorname{Ad}_{g^{-1}} \circ \omega$, used above. Bär also writes $X$ both for a tangent vector to $\operatorname{Fr}(E)$ and for a Lie-algebra element; we keep these distinct, using $X, Y$ for tangent vectors and $\xi, \eta$ for elements of $\mathfrak{g}$. Finally, the Cartan connection $1$-forms $\omega^j{}_i$ of Riemannian geometry ([[Def - Connection 1-Forms (Cartan)]]) are exactly the matrix entries $(s^*\omega)^j{}_i$ of the pullback of the frame-bundle connection along a local frame $s$; part (c) below is this identification for the coordinate frame.

---

# Statement

> **Theorem (a covariant derivative determines a connection on the frame bundle).** Let $E \to M$ be a smooth vector bundle of rank $k$ over $\mathbb{K}$, with frame bundle $\operatorname{Fr}(E)$, structure group $G = GL(k;\mathbb{K})$ and $\mathfrak{g} = \mathfrak{gl}(k;\mathbb{K})$.
>
> **(a) Existence and uniqueness.** For every connection $\nabla$ on $E$ there is a unique connection $\omega = \omega(\nabla)$ on the principal bundle $\operatorname{Fr}(E)$ such that, for every local frame $e$ of $E$ (viewed as a local section of $\operatorname{Fr}(E)$),
> $$e^*\omega = A(\nabla, e).$$
>
> **(b) The covariant-derivative description.** This $\omega$ is given intrinsically as follows. For $p \in \operatorname{Fr}(E)$ and $X \in T_p \operatorname{Fr}(E)$, choose any curve $t \mapsto p(t) = (p_1(t), \dots, p_k(t))$ of frames with $p(0) = p$ and $\dot p(0) = X$. Then the matrix $\omega(X) \in \mathfrak{g}$ is the unique matrix satisfying
> $$\frac{\nabla}{dt}\Big|_{t=0} p_j \;=\; \big(p(0) \cdot \omega(X)\big)_j \;=\; \sum_{i=1}^{k} p_i(0)\, \omega(X)^i{}_j \qquad (j = 1, \dots, k),$$
> and this value is independent of the chosen curve.
>
> **(c) Christoffel symbols.** Let $E = TM$ and let $x^1, \dots, x^n$ be local coordinates on $U$, so that $s = \big(\tfrac{\partial}{\partial x^1}, \dots, \tfrac{\partial}{\partial x^n}\big)$ is a local section of $\operatorname{Fr}(TM)$. Then, with the Christoffel symbols $\Gamma^j_{ik}$ defined by $\nabla_{\partial_k}\partial_i = \sum_j \Gamma^j_{ik}\, \partial_j$,
> $$\big(s^*\omega(\partial_k)\big)^j{}_i = \Gamma^j_{ik}.$$
>
> **(d) Bijection.** The assignment $\nabla \mapsto \omega(\nabla)$ is a bijection $\mathcal{A}(E) \to \mathcal{A}(\operatorname{Fr}(E))$. Its inverse sends a connection $\omega$ on $\operatorname{Fr}(E)$ to the covariant derivative it induces on $E = \operatorname{Fr}(E) \times_\rho \mathbb{K}^k$ through the standard representation $\rho$ of $G$ on $\mathbb{K}^k$.

The two descriptions (a) and (b) are the two source constructions — Haydys builds $\omega$ from the local connection matrices and pastes the pieces together, Bär gives the intrinsic formula in (b) — and the content of part (a)–(b) is that they produce the same object. Part (d) closes the circle with the next theorem, [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles]], which constructs the induced covariant derivative; here we prove that $\nabla \mapsto \omega(\nabla)$ is injective and that the two maps are mutually inverse once that induced derivative is available.

---

# Motivation

The two chapters preceding this one develop two apparently unrelated notions of "connection." On a vector bundle a connection is a covariant derivative $\nabla$: a rule for differentiating sections, packaged as a first-order operator $\Gamma(E) \to \Omega^1(M;E)$ satisfying the Leibniz rule. On a principal bundle a connection is a $\mathfrak{g}$-valued $1$-form $\omega$ on the total space, or equivalently an equivariant choice of horizontal complement to the fibres. The definitions look nothing alike: one lives downstairs on $M$ and differentiates sections, the other lives upstairs on $\operatorname{Fr}(E)$ and splits tangent spaces. A reader is entitled to ask whether these are two names for one idea or two genuinely different structures.

This theorem is the bridge. It says that for the *frame bundle* $\operatorname{Fr}(E)$ — the principal $GL(k)$-bundle whose points are the bases of the fibres of $E$ — the two notions are in perfect, canonical correspondence: a covariant derivative on $E$ is *exactly the same thing* as a principal connection on $\operatorname{Fr}(E)$, with no loss and no auxiliary choices. The correspondence is forced by a single demand, that pulling the principal connection back along a frame $e$ reproduce the connection matrix $A(\nabla, e)$ of $\nabla$ in that frame. Because the connection matrices in different frames are already known to transform by the gauge rule $A' = g^{-1}Ag + g^{-1}dg$ (equation (14) of the vector-bundle chapter), and because that is precisely how the *local connection forms* $s^*\omega$ of a principal connection transform, the two data are interchangeable. The frame bundle is the object on which the transformation law of $\nabla$ becomes the equivariance of $\omega$.

The theorem matters because it is the gateway to everything that follows. Once a covariant derivative is a principal connection, the whole apparatus of the principal picture becomes available to ordinary differential geometry: curvature as a $\mathfrak{g}$-valued $2$-form, holonomy as a subgroup of $GL(k)$, characteristic classes through Chern–Weil theory, and reduction of the structure group when $\nabla$ preserves extra structure (a metric, an orientation, a complex structure). Conversely, the intrinsic description in part (b) — differentiate a moving frame and read off the resulting matrix — is what makes the abstract $\omega$ computable, and part (c) identifies its entries with the Christoffel symbols one already knows, so that the general machine specialises to the Levi-Civita connection of Riemannian geometry without any translation.

---

# Sources and Targets

**Sources (Input Broadening).** The stated hypothesis is a single connection $\nabla$ on a vector bundle. The interesting question is which problems secretly hand one such a connection, so that the theorem may be applied to lift it to the frame bundle.

The first disguised source is **a system of local matrix-valued $1$-forms that transform by the gauge law**. Suppose one is given, over the members $U_\alpha$ of a trivialising cover, a family of forms $A_\alpha \in \Omega^1(U_\alpha; \mathfrak{gl}_k)$ satisfying $A_\beta = g_{\alpha\beta}^{-1} A_\alpha g_{\alpha\beta} + g_{\alpha\beta}^{-1}\, dg_{\alpha\beta}$ on each overlap, where $g_{\alpha\beta}$ are the transition functions of $E$. The bridge $B \Rightarrow A$ is that any such family *is* the family of connection matrices of a unique covariant derivative $\nabla$ (define $\nabla = d + A_\alpha$ in each frame; the transformation law is exactly the condition that these local definitions agree), so the theorem applies and produces a principal connection with local forms $A_\alpha$. The non-obvious step is recognising that an inhomogeneous transformation law, and not an invariant one, is the signature of a connection. *Example problem:* the Yang–Mills gauge potentials $A_\mu$ of physics are presented only as local matrix fields with a prescribed behaviour under gauge transformations; this recognition is what turns them into a connection on a principal bundle.

The second disguised source is **a metric-compatible covariant derivative**. If $E$ carries a bundle metric $h$ and $\nabla$ satisfies $d\, h(s,t) = h(\nabla s, t) + h(s, \nabla t)$, then in an orthonormal frame the connection matrix $A$ takes values in the Lie algebra of the isometry group ($\mathfrak{o}(k)$ or $\mathfrak{u}(k)$), not all of $\mathfrak{gl}_k$. The bridge is that $\nabla$ then determines a connection on the *reduced* frame bundle of orthonormal frames, a principal $O(k)$- or $U(k)$-bundle. The non-obvious content is that a property of $\nabla$ (preserving $h$) becomes a reduction of the structure group of the associated principal connection. *Example problem:* the Levi-Civita connection of a Riemannian manifold produces a connection on the orthonormal frame bundle, the starting point of Cartan's method of moving frames.

The third disguised source is **a holomorphic structure together with a Hermitian metric on a complex vector bundle**. The Chern connection is the unique connection compatible with both; it is presented not as a covariant derivative directly but as the solution of a compatibility problem. The bridge is that solving that problem yields a genuine $\nabla$, to which the theorem applies, giving a connection on the frame bundle whose curvature is the object measured by the Chern classes. The non-obviousness is that an existence-and-uniqueness result upstream (the Chern connection exists) is what licenses the lift. *Example problem:* computing $c_1$ of a Hermitian holomorphic line bundle proceeds by lifting the Chern connection to the $U(1)$-frame bundle and integrating its curvature.

**Targets (Output Amplification).** The bare output is a principal connection $\omega$ on $\operatorname{Fr}(E)$. Combined with further ingredients it yields much more.

Combine $\omega$ with **the structure equation and Chern–Weil theory**. The curvature $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ of the frame-bundle connection is a $\mathfrak{g}$-valued $2$-form; feeding it into an $\operatorname{Ad}$-invariant polynomial produces closed forms on $M$ whose de Rham classes are the characteristic classes of $E$. The extra ingredient is invariant-polynomial theory, and the payoff is that topological invariants of $E$ become integrals of curvature. This is non-obvious because it converts a differential-geometric datum ($\nabla$) into topological invariants that do not depend on it.

Combine $\omega$ with **the induced-connection theorem for associated bundles**. A single $\omega$ on $\operatorname{Fr}(E)$ induces, through each representation $\rho$ of $GL(k)$, a covariant derivative on the corresponding associated bundle ([[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles]]). The extra ingredient is the list of representations; the payoff is that the connections on $E^*$, $\operatorname{End}(E)$, $\Lambda^p E$ and all tensor powers are produced simultaneously and consistently from one object, rather than defined separately and reconciled afterward.

Combine $\omega$ with **holonomy and the reduction theorem**. The horizontal distribution $\ker\omega$ has a holonomy group $\operatorname{Hol}(\omega) \subseteq GL(k)$, and the theorem that a connection reduces to a subbundle with structure group the holonomy turns geometric constraints on $\nabla$ into algebraic constraints on a subgroup. The extra ingredient is the holonomy principle; the payoff is the classification of special geometries (Kähler, hyperkähler, $G_2$) by holonomy subgroups, all of which begins with the passage from $\nabla$ to $\omega$ effected here.

---

# Why Is It True

Strip away the formalism and picture what a connection *does* to a moving frame. A covariant derivative $\nabla$ knows how to differentiate a frame $e = (e_1, \dots, e_k)$ of $E$ along a direction $v$: the result $\nabla_v e_j$ is again a vector in the fibre, so it expands in the basis $e$, and the coefficients form a matrix — this matrix is $A(\nabla, e)(v)$, the connection matrix. That is *all* a covariant derivative is, locally: a machine that eats a direction and returns the infinitesimal linear distortion of the frame, expressed as a matrix in $\mathfrak{gl}_k$.

Now stand on the frame bundle. A point of $\operatorname{Fr}(E)$ is a frame; a tangent vector $X$ to $\operatorname{Fr}(E)$ is an infinitesimal motion of a frame, which has two parts: the frame's base point moves (a horizontal-looking motion covering a tangent vector on $M$) and the frame itself twists within its fibre (a vertical motion, an element of $\mathfrak{gl}_k$ acting on the basis). The connection form $\omega$ must return, from this motion $X$, an element of $\mathfrak{g} = \mathfrak{gl}_k$. Bär's formula in part (b) says exactly what it returns: differentiate the moving frame covariantly, $\frac{\nabla}{dt}p_j$, and read the answer back in the frame $p$ itself as a matrix. If the motion is purely vertical — the base point is fixed and the frame spins by $\exp(t\xi)$ — then covariant differentiation is ordinary differentiation inside a single fibre, and it returns exactly the generator $\xi$; this is axiom 2. If the motion is a rigid right translation by $g$ of a given motion, the covariant derivative, being linear over the constant matrix $g$, gets conjugated, which is precisely the equivariance axiom 1.

> **The frame bundle turns the transformation law of the connection matrices into the equivariance law of a single global form:** $\omega$ is the one $\mathfrak{g}$-valued form on $\operatorname{Fr}(E)$ whose restriction to each frame $e$ is the connection matrix $A(\nabla, e)$, and it exists and is unique precisely because the matrices $A(\nabla, e)$ already transform, under change of frame $e' = e\cdot g$, by $A' = g^{-1}Ag + g^{-1}dg$ — the same law by which the pullbacks of any principal connection transform.

The deepest way to see the inevitability is dimensional. Over a trivialising set the frame bundle is $U \times GL(k)$, coordinatised by $(m, a)$ where $m \in U$ and $a$ records the frame relative to a reference frame $\tilde e$. In these coordinates the form is forced to be
$$\omega = a^{-1}\, da + a^{-1}\, (\pi^*\tilde A)\, a,$$
the first term supplying axiom 2 (the pure-fibre motion $da$ is read off by $a^{-1}da$, which is the Maurer–Cartan form of $GL(k)$) and the second term carrying the covariant derivative's information through the reference connection matrix $\tilde A = A(\nabla, \tilde e)$. There is no freedom left: once axioms 1 and 2 and the pullback condition are imposed, this formula is the only possibility, and one only has to check that the formulae built from different reference frames agree — which they do, by the transformation law.

---

# What Makes This Hard

The single non-obvious step is that the *well-definedness* is not automatic and must be earned twice, in two different guises: in Bär's description (b) one must show the matrix $\omega(X)$ does not depend on which curve $p(t)$ realises the tangent vector $X$, and in Haydys's description (a) one must show the connections reconstructed over different trivialising sets, from different reference frames, agree on the overlaps. Both reduce to the *same* fact — the gauge transformation law $A' = g^{-1}Ag + g^{-1}dg$ for connection matrices — but the reduction is not visible until one differentiates the right-action map $\hat R(p,g) = p\cdot g$ and separates its differential into a right-translation part and a fundamental-field part (Lemma 1). The common error is to check axiom 1 or 2 only at points of a single reference frame $e(m)$ and to assume equivariance propagates the check to the whole fibre $e(m)\cdot g$ for free; propagation is genuine content and uses the chapter I identity $(R_g)_*\xi_P = (\operatorname{Ad}_{g^{-1}}\xi)_P$. A second, subtler trap in part (b) is to forget that the covariant derivative along a *constant* curve (one that stays in a fixed fibre) reduces to the ordinary derivative in that fibre — the step that makes axiom 2 come out as an equality rather than an approximation.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build $\omega$ locally by the explicit formula $\omega = a^{-1}da + a^{-1}(\pi^*A)a$ in a trivialisation, so that the two connection axioms and the pullback condition are visible; then use the differential of the right-action map (Lemma 1) together with the gauge transformation law of connection matrices to show that the locally built forms agree on overlaps and glue to a global $\omega$, which is unique because its values are pinned by axioms 1–2 and the pullback condition on every tangent vector. Finally identify this $\omega$ with Bär's intrinsic covariant-derivative formula, unwind it in coordinates to see the Christoffel symbols, and record injectivity of $\nabla \mapsto \omega$.

**Subgoal decomposition:**

1. **Differentiate the action map.** Compute $d\hat R_{(p,g)}(v, w) = dR_g(v) + (\theta_g(w))_P(p\cdot g)$.
   - *Hint:* Split the differential into its two partial differentials, freeze one argument at a time, and recognise the second as a fundamental vector field via the orbit map.
   - *Why needed:* Every overlap and equivariance computation moves a tangent vector between the frames $e(m)$ and $e(m)\cdot g$; this is the only tool that does so.

2. **Reconstruct locally and check the axioms.** Over a trivialising $U$ with reference frame $e$, show the formula $\omega = a^{-1}da + a^{-1}(\pi^*A)a$ defines the unique smooth connection with $e^*\omega = A$.
   - *Hint:* In the coordinates $(m,a)$, evaluate $\omega$ on a purely vertical vector and on $de$; check $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega$ directly from $a \mapsto ag$.
   - *Why needed:* It supplies existence over each trivialising set and the uniqueness that forces the gluing.

3. **Glue across frames.** For two frames $e' = e\cdot g$ over the same $U$, show $e'^*\omega = g^{-1}(e^*\omega)g + g^{-1}dg$, so the reconstructed forms agree wherever two trivialisations overlap.
   - *Hint:* Write $e' = \hat R \circ (e, g)$, apply Lemma 1, then use axioms 1 and 2 of the already-built $\omega$.
   - *Why needed:* This is the compatibility that turns the local forms into one global form and simultaneously proves $e^*\omega = A(\nabla,e)$ for *every* frame.

4. **Match Bär's formula and specialise.** Show the intrinsic value $\frac{\nabla}{dt}|_0 p_j = (p\cdot\omega(X))_j$ depends only on $(p, X)$ and defines the same $\omega$; then unwind in coordinates to get the Christoffel symbols.
   - *Hint:* Use the frame expansion $(\ast)$ of the covariant derivative along a curve; for a fixed-fibre curve $\dot c = 0$ and for a right-translated curve use $\mathbb{K}$-linearity over constants.
   - *Why needed:* It identifies the two source constructions and delivers parts (b) and (c).

5. **Record injectivity.** Show $\nabla$ is recovered from the family of pullbacks $e^*\omega$, so $\nabla \mapsto \omega$ is injective; cite the next theorem for surjectivity and the inverse.
   - *Hint:* $\nabla = d + A(\nabla, e)$ in each frame, and $A(\nabla,e) = e^*\omega$.
   - *Why needed:* It is part (d).

---

# Lemma Decomposition

> [!note]- Lemma 1: the differential of the right-action map
> **Statement:** Let $P \to M$ be a principal $G$-bundle with right action $\hat R \colon P \times G \to P$, $\hat R(p, g) = p \cdot g$. For $v \in T_p P$ and $w \in T_g G$,
> $$d\hat R_{(p,g)}(v, w) = dR_g(v) + \big(\theta_g(w)\big)_P(p \cdot g),$$
> where $\theta$ is the left Maurer–Cartan form ($\theta_g(w) = dL_{g^{-1}}(w) \in \mathfrak{g}$) and $\zeta_P$ denotes the fundamental vector field of $\zeta \in \mathfrak{g}$. For $P = \operatorname{Fr}(E)$ and the matrix group $G = GL(k;\mathbb{K})$, $\theta_g(w) = g^{-1}w$.
>
> **Hint:** The differential of a two-variable map is the sum of its partial differentials; freeze $g$, then freeze $p$, and recognise the second contribution through the orbit map.
>
> **Why needed:** It is the sole device that relates tangent vectors at $p$ and at $p\cdot g$, hence the engine of every equivariance and overlap computation below.
>
> > [!note]- Full proof
> > Because $\hat R$ is smooth on the product $P \times G$, its differential at $(p, g)$ is additive over the two factors of $T_{(p,g)}(P \times G) = T_p P \oplus T_g G$:
> > $$d\hat R_{(p,g)}(v, w) = d\hat R_{(p,g)}(v, 0) + d\hat R_{(p,g)}(0, w). \qquad \text{(differential is linear on the direct sum)}$$
> >
> > **First term (vary $p$, freeze $g$).** Choose a curve $p(t)$ in $P$ with $p(0) = p$, $\dot p(0) = v$. Then $\hat R(p(t), g) = p(t) \cdot g = R_g(p(t))$, so
> > $$d\hat R_{(p,g)}(v, 0) = \frac{d}{dt}\Big|_{0} R_g(p(t)) = dR_g(v). \qquad \text{(definition of } R_g \text{ and of the differential)}$$
> >
> > **Second term (vary $g$, freeze $p$).** Choose a curve $g(t)$ in $G$ with $g(0) = g$, $\dot g(0) = w$. Set $h(t) := g^{-1} g(t)$, so that $h(0) = e$ and
> > $$\dot h(0) = \frac{d}{dt}\Big|_0 g^{-1} g(t) = dL_{g^{-1}}(w) = \theta_g(w) =: \zeta \in \mathfrak{g}. \qquad \text{(chain rule; definition of } \theta\text{)}$$
> > Since $p \cdot g(t) = p \cdot \big(g \cdot h(t)\big) = (p \cdot g) \cdot h(t)$, and writing $\ell_q \colon G \to P$, $\ell_q(g') = q \cdot g'$ for the orbit map through a point $q$,
> > $$d\hat R_{(p,g)}(0, w) = \frac{d}{dt}\Big|_0 (p\cdot g) \cdot h(t) = d(\ell_{p \cdot g})_e\big(\dot h(0)\big) = d(\ell_{p \cdot g})_e(\zeta). \qquad \text{(} h(0) = e \text{; chain rule)}$$
> > By the definition of the fundamental vector field, $\zeta_P(q) = \frac{d}{dt}\big|_0 q \cdot \exp(t\zeta) = d(\ell_q)_e(\zeta)$, because $t \mapsto \exp(t\zeta)$ is a curve through $e$ with velocity $\zeta$ and the value depends only on that velocity. Hence $d(\ell_{p\cdot g})_e(\zeta) = \zeta_P(p\cdot g) = (\theta_g(w))_P(p\cdot g)$.
> >
> > **Combine.** Adding the two terms gives $d\hat R_{(p,g)}(v,w) = dR_g(v) + (\theta_g(w))_P(p\cdot g)$. For the matrix group $G = GL(k;\mathbb{K})$ we have $L_{g^{-1}}(h) = g^{-1}h$ linear in $h$, so $\theta_g(w) = dL_{g^{-1}}(w) = g^{-1}w$. $\blacksquare$

> [!note]- Lemma 2: local reconstruction, its axioms, and its uniqueness
> **Statement:** Let $U \subseteq M$ be a trivialising open set with a local frame $e$ of $E$, and let $A \in \Omega^1(U; \mathfrak{gl}_k)$. Trivialise $\operatorname{Fr}(E)|_U \cong U \times GL(k;\mathbb{K})$ by $e(m) \cdot a \leftrightarrow (m, a)$. Then the formula
> $$\omega_{(m,a)} := a^{-1}\, da + a^{-1}\, \big(\pi^*A\big)\, a \tag{L2}$$
> (where $da$ is the Maurer–Cartan form of the $GL(k)$-factor and $\pi^*A$ is the pullback of $A$ to $U \times GL(k)$) defines a smooth connection $\omega$ on $\operatorname{Fr}(E)|_U$ satisfying axioms 1 and 2 and $e^*\omega = A$; and it is the *only* connection on $\operatorname{Fr}(E)|_U$ with $e^*\omega = A$.
>
> **Hint:** Read off the value of (L2) on a vertical vector and on $de(v)$; for equivariance use that right translation is $a \mapsto ag$; for uniqueness use that axioms 1–2 pin $\omega$ on all of $T_{e(m)a}\operatorname{Fr}(E)$.
>
> **Why needed:** It supplies existence of the connection over each trivialising set and the uniqueness that makes the overlap check (Lemma 1 plus the transformation law) force a global gluing.
>
> > [!note]- Full proof
> > Throughout, points of $\operatorname{Fr}(E)|_U$ are written $(m, a)$ with $m \in U$, $a \in GL(k;\mathbb{K})$, meaning the frame $e(m)\cdot a$; the reference frame $e$ is $a \equiv \mathbf{1}$. A tangent vector at $(m, a)$ has the form $(v, \dot a)$ with $v \in T_m U$ and $\dot a \in T_a GL(k) = \operatorname{Mat}(k\times k)$. The right translation is $R_g(m, a) = (m, ag)$.
> >
> > **$\omega$ satisfies axiom 2.** The fundamental vector field of $\xi \in \mathfrak{gl}_k$ at $(m, a)$ is $\xi_P(m,a) = \frac{d}{dt}\big|_0 (m, a\exp(t\xi)) = (0, a\xi)$ (the base point is fixed, the fibre coordinate moves by $a\exp(t\xi)$). Evaluating (L2):
> > $$\omega_{(m,a)}(\xi_P) = a^{-1}(a\xi) + a^{-1}A(0)\,a = \xi, \qquad \text{(} da \text{ applied to } (0, a\xi) \text{ is } a\xi \text{; } \pi^*A \text{ kills the vertical vector } (0,a\xi)\text{)}$$
> > so $\omega(\xi_P) = \xi$ for every $\xi$, which is axiom 2.
> >
> > **$\omega$ satisfies axiom 1.** For $g \in GL(k)$, compute $R_g^*\omega$ at $(m, a)$ on a vector $(v, \dot a)$. Under $R_g$ the point $(m,a)$ goes to $(m, ag)$ and $(v, \dot a) \mapsto (v, \dot a\, g)$. The Maurer–Cartan term of (L2) at $(m, ag)$ evaluated on $(v, \dot a\, g)$ is $(ag)^{-1}(\dot a\, g) = g^{-1}(a^{-1}\dot a)g$, and the second term is $(ag)^{-1}A(v)(ag) = g^{-1}\big(a^{-1}A(v)a\big)g$. Hence
> > $$(R_g^*\omega)_{(m,a)}(v,\dot a) = g^{-1}\Big(a^{-1}\dot a + a^{-1}A(v)a\Big)g = g^{-1}\, \omega_{(m,a)}(v,\dot a)\, g = \operatorname{Ad}_{g^{-1}}\big(\omega_{(m,a)}(v,\dot a)\big),$$
> > which is axiom 1.
> >
> > **Pullback along $e$.** The frame $e$ is the slice $a \equiv \mathbf{1}$, so $de(v) = (v, 0)$ and $a^{-1}da$ vanishes on it while $a^{-1}(\pi^*A)a = A$ there:
> > $$(e^*\omega)(v) = \omega_{(m,\mathbf 1)}(v, 0) = \mathbf 1^{-1}\cdot 0 + \mathbf 1^{-1}A(v)\mathbf 1 = A(v). \qquad \text{(evaluate (L2) at } a = \mathbf 1\text{)}$$
> > Thus $e^*\omega = A$. The form (L2) is a smooth $\mathfrak{gl}_k$-valued $1$-form because $a \mapsto a^{-1}$ and matrix multiplication are smooth on $GL(k)$ and $A$ is smooth; so $\omega$ is a smooth connection.
> >
> > **Uniqueness.** Suppose $\omega'$ is any connection on $\operatorname{Fr}(E)|_U$ with $e^*\omega' = A$. Fix a point $q = e(m) \cdot a = (m, a)$ and a tangent vector $Y \in T_q \operatorname{Fr}(E)$. Because $q = R_a(e(m))$ and $R_a$ is a diffeomorphism, $Y = dR_a(Z)$ for a unique $Z \in T_{e(m)}\operatorname{Fr}(E)$. At $e(m)$ we have the direct-sum decomposition $T_{e(m)}\operatorname{Fr}(E) = V_{e(m)} \oplus de(T_m U)$, where $V_{e(m)} = \ker d\pi_{e(m)}$ is the vertical space (of dimension $k^2$) and $de(T_m U)$ is the $n$-dimensional image of the injective $de$ (injective since $\pi \circ e = \operatorname{id}$); the sum is direct and exhausts $T_{e(m)}\operatorname{Fr}(E)$ by dimension count, $k^2 + n = \dim \operatorname{Fr}(E)$. Write $Z = \xi_P(e(m)) + de(v)$ with $\xi \in \mathfrak{g}$, $v \in T_m U$; this is possible because $V_{e(m)} = \{\xi_P(e(m)) : \xi \in \mathfrak{g}\}$, the fundamental fields spanning the vertical space: each $\xi_P(e(m))$ is vertical because the curve $t \mapsto e(m)\cdot\exp(t\xi)$ stays in the single fibre $\operatorname{Fr}(E)_m$, so $d\pi\big(\xi_P(e(m))\big) = \frac{d}{dt}\big|_0 \pi\big(e(m)\cdot\exp(t\xi)\big) = 0$; the map $\xi \mapsto \xi_P(e(m))$ is injective because axiom 2 for any connection $\varpi$ gives $\xi = \varpi(\xi_P)$, so $\xi_P(e(m)) = 0$ forces $\xi = 0$; and since $\dim \mathfrak{g} = k^2 = \dim V_{e(m)}$ this injective map into $V_{e(m)}$ is an isomorphism onto $V_{e(m)}$. Then, for *any* connection $\varpi$ with $e^*\varpi = A$,
> > $$\varpi_q(Y) = \varpi_{q}\big(dR_a(Z)\big) = \operatorname{Ad}_{a^{-1}}\varpi_{e(m)}(Z) \qquad \text{(axiom 1 for } \varpi\text{)}$$
> > $$= \operatorname{Ad}_{a^{-1}}\Big(\varpi_{e(m)}(\xi_P) + \varpi_{e(m)}(de(v))\Big) = \operatorname{Ad}_{a^{-1}}\big(\xi + (e^*\varpi)(v)\big) = \operatorname{Ad}_{a^{-1}}\big(\xi + A(v)\big). \qquad \text{(axiom 2; } e^*\varpi = A\text{)}$$
> > The right-hand side depends only on $A$, on $q = (m,a)$, and on the decomposition of $Z$, not on the particular connection. Applying this to both $\omega$ and $\omega'$ gives $\omega_q(Y) = \omega'_q(Y)$ for all $q, Y$, so $\omega = \omega'$. $\blacksquare$

> [!note]- Lemma 3: the covariant-derivative datum depends only on $(p(0), \dot p(0))$
> **Statement:** Let $\nabla$ be a connection on $E$ and $p(t) = (p_1(t), \dots, p_k(t))$ a smooth curve of frames of $E$, with $c := \pi \circ p$. Then for each $j$ the vector $\frac{\nabla}{dt}\big|_{0} p_j \in E_{c(0)}$ depends only on the point $p(0)$ and the velocity $\dot p(0)$, and not on the rest of the curve. Moreover, for a constant matrix $g \in GL(k;\mathbb{K})$,
> $$\frac{\nabla}{dt}\Big|_0 (p \cdot g)_j = \Big(\Big(\tfrac{\nabla}{dt}\big|_0 p\Big) \cdot g\Big)_j, \tag{L3}$$
> and if $c$ is constant (the curve stays in one fibre) then $\frac{\nabla}{dt}\big|_0 p_j = \frac{d}{dt}\big|_0 p_j(t)$, the ordinary derivative in the fixed vector space $E_{c(0)}$.
>
> **Hint:** Expand $p_j(t)$ in a fixed reference frame using $(\ast)$; the constant-coefficient and constant-base cases fall out of that formula.
>
> **Why needed:** It is exactly what Bär's part (b) needs: well-definedness of $\omega(X)$, and the two computations that produce axioms 1 and 2.
>
> > [!note]- Full proof
> > Fix a local reference frame $\tilde e = (\tilde e_1, \dots, \tilde e_k)$ of $E$ over a neighbourhood of $m = c(0)$, with connection matrix $\tilde A = A(\nabla, \tilde e)$. Expand each frame vector in the reference frame along the curve: $p_j(t) = \sum_i a^i{}_j(t)\, \tilde e_i(c(t))$ with $a(t) = (a^i{}_j(t)) \in GL(k;\mathbb{K})$ smooth. By the frame formula $(\ast)$ for the covariant derivative along $c$,
> > $$\frac{\nabla}{dt}\Big|_0 p_j = \sum_i\Big(\dot a^i{}_j(0) + \sum_l \tilde A^i{}_l(\dot c(0))\, a^l{}_j(0)\Big)\, \tilde e_i(m). \qquad \text{(apply } (\ast) \text{ to } p_j\text{)} \tag{L3a}$$
> > The right-hand side involves only $a(0)$, $\dot a(0)$ and $\dot c(0)$. But $a(0)$ and $c(0)$ together record the point $p(0)$ in the trivialisation induced by $\tilde e$, and $\dot a(0)$ and $\dot c(0)$ together record $\dot p(0)$; hence $\frac{\nabla}{dt}\big|_0 p_j$ depends only on $p(0)$ and $\dot p(0)$, proving the first claim.
> >
> > **Constant right multiplication.** For a constant $g$, the curve $p(t) \cdot g$ has reference-frame coefficients $a(t) g$, so $\frac{d}{dt}(a g) = \dot a\, g$ and $(ag)(0) = a(0)g$. Substituting into (L3a) (with $c$ unchanged, so $\dot c(0)$ is the same),
> > $$\frac{\nabla}{dt}\Big|_0 (p\cdot g)_j = \sum_i\Big((\dot a\, g)^i{}_j(0) + \sum_l \tilde A^i{}_l(\dot c(0))\,(a g)^l{}_j(0)\Big)\tilde e_i(m) = \Big(\Big(\tfrac{\nabla}{dt}\big|_0 p\Big)\cdot g\Big)_j,$$
> > because $g$ has constant entries and factors out of both terms on the right of (L3a); this is (L3). (Equivalently, $\frac{\nabla}{dt}$ is $\mathbb{K}$-linear over constant coefficients.)
> >
> > **Constant base curve.** If $c(t) \equiv m$, then $\dot c(0) = 0$ and the reference frame is evaluated at the fixed point $m$, so $(\ast)$/(L3a) reduces to $\frac{\nabla}{dt}\big|_0 p_j = \sum_i \dot a^i{}_j(0)\, \tilde e_i(m) = \frac{d}{dt}\big|_0 \big(\sum_i a^i{}_j(t)\tilde e_i(m)\big) = \frac{d}{dt}\big|_0 p_j(t)$, the ordinary derivative of the $E_m$-valued curve $p_j$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix a connection $\nabla$ on $E$. We prove parts (a)–(d) in turn.
>
> **Step 0 — the frame bundle and its trivialisations.** By [[Def - Frame Bundle of a Vector Bundle]], $\operatorname{Fr}(E) \to M$ is a principal $G$-bundle with $G = GL(k;\mathbb{K})$, and a local frame $e$ of $E$ over $U$ is the same as a local section $e \colon U \to \operatorname{Fr}(E)|_U$; such a section induces the trivialisation $U \times G \xrightarrow{\ \cong\ } \operatorname{Fr}(E)|_U$, $(m, a) \mapsto e(m)\cdot a$. Choose an open cover $\{U_\alpha\}$ of $M$ over which $E$ admits local frames $e_\alpha$, with connection matrices $A_\alpha := A(\nabla, e_\alpha) \in \Omega^1(U_\alpha; \mathfrak{gl}_k)$. On an overlap $U_\alpha \cap U_\beta$ the frames are related by $e_\beta = e_\alpha \cdot g_{\alpha\beta}$ for a smooth transition function $g_{\alpha\beta} \colon U_\alpha \cap U_\beta \to G$, and by the gauge transformation law of connection matrices — the matrix case of [[Thm - Transformation of Local Connection and Curvature Forms]], equivalently [[Thm - Gauge Transformation Law for Connection 1-Forms]], which states that under $e' = e\cdot g$ one has $A(\nabla, e') = g^{-1}A(\nabla, e)\,g + g^{-1}dg$ — we have
> $$A_\beta = g_{\alpha\beta}^{-1}\, A_\alpha\, g_{\alpha\beta} + g_{\alpha\beta}^{-1}\, dg_{\alpha\beta} \qquad \text{on } U_\alpha \cap U_\beta. \tag{14}$$
>
> **Part (a) — existence.** By Lemma 2 applied to each $\alpha$, there is a unique connection $\omega_\alpha$ on $\operatorname{Fr}(E)|_{U_\alpha}$ with $e_\alpha^*\omega_\alpha = A_\alpha$. We show the $\omega_\alpha$ agree on overlaps. Fix $\alpha, \beta$ and abbreviate $g := g_{\alpha\beta}$, so $e_\beta = e_\alpha \cdot g = \hat R \circ (e_\alpha, g)$ over $U_\alpha \cap U_\beta$. For $v \in T_m U$ with $m \in U_\alpha \cap U_\beta$,
> $$e_\beta^*\omega_\alpha(v) = \omega_\alpha\big(de_\beta(v)\big) = \omega_\alpha\Big(d\hat R_{(e_\alpha(m),\, g(m))}\big(de_\alpha(v),\, dg(v)\big)\Big). \qquad \text{(} e_\beta = \hat R\circ(e_\alpha,g)\text{, chain rule)}$$
> By **Lemma 1** with $p = e_\alpha(m)$ and this $g = g(m)$, and writing $\eta := \theta_{g(m)}(dg(v)) = g(m)^{-1}dg(v) = (g^{-1}dg)(v) \in \mathfrak{g}$,
> $$d\hat R_{(e_\alpha(m),\,g(m))}\big(de_\alpha(v), dg(v)\big) = dR_{g(m)}\big(de_\alpha(v)\big) + \eta_P\big(e_\beta(m)\big).$$
> Apply $\omega_\alpha$ and use its axioms:
> $$\omega_\alpha\Big(dR_{g(m)}\big(de_\alpha(v)\big)\Big) = \operatorname{Ad}_{g(m)^{-1}}\,\omega_\alpha\big(de_\alpha(v)\big) = g^{-1}\, A_\alpha(v)\, g \qquad \text{(axiom 1 for } \omega_\alpha\text{; } \omega_\alpha(de_\alpha(v)) = e_\alpha^*\omega_\alpha(v) = A_\alpha(v)\text{)},$$
> $$\omega_\alpha\big(\eta_P(e_\beta(m))\big) = \eta = (g^{-1}dg)(v). \qquad \text{(axiom 2 for } \omega_\alpha\text{)}$$
> Adding, $e_\beta^*\omega_\alpha(v) = g^{-1}A_\alpha(v)\,g + (g^{-1}dg)(v) = A_\beta(v)$ by (14). Thus $e_\beta^*\omega_\alpha = A_\beta = e_\beta^*\omega_\beta$, and by the **uniqueness** clause of Lemma 2 (a connection over $U_\alpha \cap U_\beta$ is determined by its pullback along the single frame $e_\beta$) we conclude $\omega_\alpha = \omega_\beta$ on $\pi^{-1}(U_\alpha \cap U_\beta)$. Hence the local forms glue to a single smooth $1$-form $\omega \in \Omega^1(\operatorname{Fr}(E); \mathfrak{g})$ with $\omega|_{\pi^{-1}(U_\alpha)} = \omega_\alpha$. It satisfies axioms 1 and 2 because each $\omega_\alpha$ does and the axioms are pointwise conditions; so $\omega \in \mathcal{A}(\operatorname{Fr}(E))$.
>
> It remains to check $e^*\omega = A(\nabla, e)$ for *every* local frame $e$, not only the $e_\alpha$. Given such an $e$ over $V$ and a point $m \in V$, pick $\alpha$ with $m \in U_\alpha$; on a neighbourhood of $m$ we have $e = e_\alpha \cdot h$ for a smooth $h \colon V \cap U_\alpha \to G$, and the computation just performed (with $e_\alpha, e, h$ in place of $e_\alpha, e_\beta, g$) gives $e^*\omega(v) = h^{-1}A_\alpha(v)h + (h^{-1}dh)(v) = A(\nabla, e)(v)$, the last equality again by the transformation law (14) applied to $e = e_\alpha \cdot h$. As $m$ was arbitrary, $e^*\omega = A(\nabla, e)$.
>
> **Part (a) — uniqueness.** Suppose $\omega'$ is another connection on $\operatorname{Fr}(E)$ with $e^*\omega' = A(\nabla, e)$ for every frame $e$. Over each $U_\alpha$, $\omega'$ is a connection with $e_\alpha^*\omega' = A_\alpha$, so by the uniqueness clause of Lemma 2, $\omega' = \omega_\alpha = \omega$ on $\pi^{-1}(U_\alpha)$. As the $U_\alpha$ cover $M$, $\omega' = \omega$. This proves part (a).
>
> **Part (b) — the covariant-derivative description.** Define, for $p \in \operatorname{Fr}(E)$ and $X \in T_p\operatorname{Fr}(E)$, a curve of frames $p(t)$ with $p(0) = p$, $\dot p(0) = X$ (such a curve exists: choose any smooth curve realising $X$ in the manifold $\operatorname{Fr}(E)$). By **Lemma 3**, the vectors $\frac{\nabla}{dt}\big|_0 p_j \in E_{\pi(p)}$ depend only on $(p, X)$; since $p = (p_1, \dots, p_k)$ is a basis of $E_{\pi(p)}$, there is a unique matrix, which we *name* $\tilde\omega(X) \in \mathfrak{gl}_k$, with
> $$\frac{\nabla}{dt}\Big|_0 p_j = \big(p \cdot \tilde\omega(X)\big)_j = \sum_i p_i\, \tilde\omega(X)^i{}_j. \tag{b}$$
> Curve-independence of the left side (Lemma 3) makes $\tilde\omega(X)$ well-defined, so (b) defines a map $\tilde\omega \colon T\operatorname{Fr}(E) \to \mathfrak{g}$; it is fibrewise linear because $X \mapsto \frac{\nabla}{dt}\big|_0 p_j$ is linear in $X$ (visible from (L3a), which is linear in $(\dot a(0), \dot c(0))$). We verify $\tilde\omega$ equals the $\omega$ of part (a), and along the way that it is a connection.
>
> *Axiom 2 for $\tilde\omega$.* Fix $\xi \in \mathfrak{g}$ and take the fibre curve $p(t) = p \cdot \exp(t\xi)$, which has $\dot p(0) = \xi_P(p)$ and constant base $c(t) \equiv \pi(p)$. By the constant-base clause of Lemma 3, $\frac{\nabla}{dt}\big|_0 p_j = \frac{d}{dt}\big|_0 p_j(t)$. Now $p_j(t) = (p\cdot \exp(t\xi))_j = \sum_i p_i \exp(t\xi)^i{}_j$, whose ordinary derivative at $0$ is $\sum_i p_i\, \xi^i{}_j = (p\cdot \xi)_j$. Comparing with (b), $p \cdot \xi = p \cdot \tilde\omega(\xi_P(p))$, and as $p$ is a basis, $\tilde\omega(\xi_P(p)) = \xi$. This is axiom 2.
>
> *Axiom 1 for $\tilde\omega$.* Fix $g \in G$ and $X \in T_p\operatorname{Fr}(E)$ with realising curve $p(t)$. Then $R_g(p(t)) = p(t)\cdot g$ realises $dR_g(X)$ at the point $p\cdot g$. By the constant-right-multiplication clause (L3) of Lemma 3,
> $$\frac{\nabla}{dt}\Big|_0 (p(t)\cdot g)_j = \Big(\Big(\tfrac{\nabla}{dt}\big|_0 p\Big)\cdot g\Big)_j = \big((p\cdot\tilde\omega(X))\cdot g\big)_j = \big(p\cdot (\tilde\omega(X)g)\big)_j. \qquad \text{(L3, then (b))}$$
> On the other hand, applying the definition (b) at the base frame $p\cdot g$,
> $$\frac{\nabla}{dt}\Big|_0 (p(t)\cdot g)_j = \big((p\cdot g)\cdot \tilde\omega(dR_g X)\big)_j = \big(p\cdot (g\,\tilde\omega(dR_g X))\big)_j. \qquad \text{(} (p\cdot g)\cdot B = p\cdot(gB)\text{)}$$
> Equating and using that $p$ is a basis, $\tilde\omega(X)g = g\,\tilde\omega(dR_g X)$, hence $\tilde\omega(dR_g X) = g^{-1}\tilde\omega(X)g = \operatorname{Ad}_{g^{-1}}\tilde\omega(X)$. This is axiom 1. (Smoothness of $\tilde\omega$ follows from formula (L3a), which is smooth in the trivialisation; so $\tilde\omega \in \mathcal{A}(\operatorname{Fr}(E))$.)
>
> *$\tilde\omega = \omega$.* We show $e^*\tilde\omega = A(\nabla, e)$ for every frame $e$; then uniqueness in part (a) forces $\tilde\omega = \omega$. Fix a frame $e$ over $U$, a point $m \in U$, and $v \in T_m U$. Take the curve $p(t) = e(c(t))$ where $c$ is a curve in $U$ with $c(0) = m$, $\dot c(0) = v$; then $\dot p(0) = de(v) =: X$ and $p_j(t) = e_j(c(t))$, so
> $$\frac{\nabla}{dt}\Big|_0 p_j = \frac{\nabla}{dt}\Big|_0 e_j(c(t)) = \nabla_{\dot c(0)} e_j = \nabla_v e_j = \sum_i e_i(m)\, A(\nabla,e)^i{}_j(v), \qquad \text{(ambient-section clause of } \tfrac{\nabla}{dt}\text{; definition of } A(\nabla,e)\text{)}$$
> while (b) gives $\frac{\nabla}{dt}\big|_0 p_j = (e(m)\cdot\tilde\omega(X))_j = \sum_i e_i(m)\,\tilde\omega(X)^i{}_j$. Comparing coefficients of the basis $e(m)$, $\tilde\omega(de(v)) = A(\nabla,e)(v)$, i.e. $(e^*\tilde\omega)(v) = A(\nabla,e)(v)$. Hence $e^*\tilde\omega = A(\nabla,e)$ for every $e$, and by part (a) uniqueness $\tilde\omega = \omega$. This proves part (b).
>
> **Part (c) — Christoffel symbols.** Let $E = TM$, let $x^1,\dots,x^n$ be coordinates on $U$, and let $s = (\partial_1,\dots,\partial_n)$ be the associated coordinate frame, a section of $\operatorname{Fr}(TM)|_U$. By part (a), $s^*\omega = A(\nabla, s)$, the connection matrix of $\nabla$ in the coordinate frame. By definition of the [[Def - Christoffel Symbols|Christoffel symbols]], $\nabla_{\partial_k}\partial_i = \sum_j \Gamma^j_{ik}\,\partial_j$, so in the compact notation $\nabla \partial_i = \sum_j \partial_j \otimes A(\nabla,s)^j{}_i$ we read off $A(\nabla,s)^j{}_i = \sum_k \Gamma^j_{ik}\, dx^k$. Evaluating on the coordinate vector field $\partial_k$,
> $$\big(s^*\omega(\partial_k)\big)^j{}_i = A(\nabla,s)^j{}_i(\partial_k) = \Big(\sum_l \Gamma^j_{il}\, dx^l\Big)(\partial_k) = \Gamma^j_{ik}, \qquad \text{(} dx^l(\partial_k) = \delta^l_k\text{)}$$
> which is part (c). In particular the Cartan connection $1$-forms $\omega^j{}_i := (s^*\omega)^j{}_i = \sum_k \Gamma^j_{ik}\,dx^k$ ([[Def - Connection 1-Forms (Cartan)]]) are the matrix entries of the frame-bundle connection form pulled back along $s$.
>
> **Part (d) — bijection.** We first show $\nabla \mapsto \omega(\nabla)$ is injective. If $\omega(\nabla) = \omega(\nabla')$, then for every local frame $e$, $A(\nabla, e) = e^*\omega(\nabla) = e^*\omega(\nabla') = A(\nabla', e)$. A connection on $E$ is determined by its connection matrices in local frames: over a trivialising $U$ with frame $e$, any section $s|_U = e\cdot\sigma$ has $\nabla s|_U = e\cdot(d\sigma + A(\nabla,e)\sigma)$ ([[Def - Connection Matrix and Local Form of a Connection]]), so $\nabla$ and $\nabla'$ agree on $\Gamma(E|_U)$ for every member of a trivialising cover, hence $\nabla = \nabla'$. Thus $\nabla \mapsto \omega(\nabla)$ is injective.
>
> For surjectivity and the description of the inverse we invoke the next theorem, [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles]]: it states that any connection $\omega$ on a principal $G$-bundle $P$ and any representation $\rho$ of $G$ induce a unique connection $\nabla^\omega$ on the associated bundle $P \times_\rho V$, and that when $P = \operatorname{Fr}(E)$ with the standard representation $\rho$ of $GL(k;\mathbb{K})$ on $\mathbb{K}^k$ (so that $\operatorname{Fr}(E)\times_\rho \mathbb{K}^k \cong E$ canonically, [[Thm - Vector Bundles are Associated to Their Frame Bundles]]) the connection matrices of $\nabla^\omega$ are $A(\nabla^\omega, e) = e^*\omega$ for every frame $e$. Granting this, take any $\omega \in \mathcal{A}(\operatorname{Fr}(E))$ and set $\nabla := \nabla^\omega$. Then $A(\nabla^\omega, e) = e^*\omega$ for every $e$, so $\omega(\nabla^\omega)$ and $\omega$ are two connections on $\operatorname{Fr}(E)$ with the same pullback along every frame; by the uniqueness of part (a), $\omega(\nabla^\omega) = \omega$. Hence $\nabla \mapsto \omega(\nabla)$ is surjective. Conversely, for a connection $\nabla$ on $E$, both $\nabla$ and $\nabla^{\omega(\nabla)}$ have connection matrices $A(\nabla, e) = e^*\omega(\nabla)$ in every frame, so $\nabla^{\omega(\nabla)} = \nabla$ by the injectivity argument's determinacy. Therefore $\nabla \mapsto \omega(\nabla)$ and $\omega \mapsto \nabla^\omega$ are mutually inverse bijections $\mathcal{A}(E) \leftrightarrow \mathcal{A}(\operatorname{Fr}(E))$. This proves part (d) and completes the theorem. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian geometry: the Levi-Civita connection as an $O(n)$-connection.** On a Riemannian manifold $(M, g)$ the Levi-Civita covariant derivative $\nabla$ is metric and torsion-free. Applying this theorem to $\nabla$ on $E = TM$ yields a connection $\omega$ on $\operatorname{Fr}(TM)$; because $\nabla$ preserves $g$, it restricts to a connection on the *orthonormal* frame bundle, a principal $O(n)$-bundle. The exercise is to verify that in an orthonormal frame the connection matrix $A(\nabla, e)$ is antisymmetric, so that $\omega$ takes values in $\mathfrak{o}(n)$, and to identify the resulting $\mathfrak{o}(n)$-valued forms with Cartan's connection forms. This is non-obvious because the reduction of the structure group from $GL(n)$ to $O(n)$ is invisible in the covariant-derivative language and becomes transparent only in the frame-bundle picture.

**Complex geometry: the Chern connection and $c_1$.** On a Hermitian holomorphic line bundle $L \to X$ over a complex manifold, the Chern connection $\nabla$ is the unique connection compatible with the metric and the holomorphic structure. Applying the theorem gives a connection $\omega$ on the $U(1)$-frame bundle, and its curvature computes the first Chern class $c_1(L) = [\tfrac{i}{2\pi}F]$. The exercise is to write $\nabla$ in a local holomorphic frame, read off $A = \partial \log h$ for the Hermitian metric $h$, and produce $\omega$ and its curvature. The non-obvious content is that a topological invariant is extracted from a connection whose very definition is analytic.

**Mathematical physics: gauge potentials as connections.** In a gauge theory one is handed local $\mathfrak{g}$-valued potentials $A_\mu$ over patches of spacetime, with a prescribed transformation law $A' = g^{-1}Ag + g^{-1}dg$ under gauge changes $g$. The exercise is to recognise that this family satisfies the hypotheses of the theorem's disguised-source form: it is precisely the family of connection matrices of a covariant derivative on an associated vector bundle, hence the frame-bundle connection form of a principal connection. This turns the physicist's potential into the mathematician's $\omega$, and the field strength $F_{\mu\nu}$ into its curvature; the non-obviousness is that the inhomogeneous gauge law is exactly the well-definedness condition (14) that the theorem consumes.

---

# Bridges

- **The gauge transformation law of connection matrices.** The theorem is possible only because the matrices $A(\nabla, e)$ transform under change of frame $e' = e\cdot g$ by $A' = g^{-1}Ag + g^{-1}dg$. This is the matrix ($GL_k$) case of [[Thm - Transformation of Local Connection and Curvature Forms]], and in the Riemannian-geometry stream it is [[Thm - Gauge Transformation Law for Connection 1-Forms]]. That inhomogeneous law is *both* the compatibility condition that makes the local reconstructions of Lemma 2 glue and the transformation law obeyed by the local connection forms $s^*\omega$ of any principal connection; the two coincide, which is the whole content of the correspondence.

- **The differential of the right-action map.** Lemma 1, $d\hat R_{(p,g)}(v,w) = dR_g(v) + (\theta_g(w))_P(p\cdot g)$, is the universal device for moving a tangent vector along a fibre. It reappears in [[Thm - Transformation of Local Connection and Curvature Forms]] (differentiating $s_\beta = s_\alpha g_{\alpha\beta}$) and is drilled independently in [[Ex - The Differential of the Right Action Map]]. Its ingredients are the fundamental vector field [[Def - Fundamental Vector Field of a Group Action]] and the Maurer–Cartan form [[Def - The Maurer-Cartan Form]].

- **Christoffel symbols and the coordinate frame.** Part (c) identifies $\Gamma^j_{ik}$ with the entries of $s^*\omega$ in the coordinate frame $s = (\partial_1, \dots, \partial_n)$; the same identification, now used to compute rather than to define, is the subject of [[Ex - Christoffel Symbols are the Local Connection Form of the Frame Bundle]]. Through it the curvature of $\omega$ pulled back along $s$ becomes the matrix of Cartan's curvature $2$-forms of [[Thm - Cartan's Second Structural Equation]], the frame-bundle avatar of the Riemann tensor.

- **The inverse construction on associated bundles.** Part (d)'s inverse is the induced-connection construction of [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles]]: a single connection $\omega$ on $\operatorname{Fr}(E)$ produces covariant derivatives on $E$ and all its tensor and endomorphism bundles at once, through the corresponding representations of $GL(k)$. This theorem and that one together establish that "covariant derivative on $E$" and "principal connection on $\operatorname{Fr}(E)$" are two faces of one object.

- **The equivariance of fundamental vector fields.** The propagation of the connection axioms from a reference frame $e(m)$ across its fibre $e(m)\cdot g$ rests on $(R_g)_*\xi_P = (\operatorname{Ad}_{g^{-1}}\xi)_P$, proved in [[Thm - The Fundamental Vector Field Map is a Lie Algebra Homomorphism for Right Actions]]; it is the identity Haydys writes as $(R_g)_* K_\xi = K_{\operatorname{Ad}_{g^{-1}}\xi}$ in his Step 2. Its role here is to guarantee that a form defined equivariantly from its values at one frame is genuinely a global, axiom-satisfying connection.

---

# Unlocked by This

> [!tip] Reduction of the structure group *(from Differential Geometry)*
> When a covariant derivative preserves an extra fibrewise structure (a metric, orientation, symplectic or complex structure), the corresponding principal connection lives on a reduced frame bundle with structure group the symmetry group of that structure. This is the mechanism behind **special holonomy** and the classification of geometric structures by holonomy subgroups.

> [!tip] Curvature as a Lie-algebra-valued 2-form *(from Gauge Theory)*
> Once $\nabla$ is the principal connection $\omega$, its curvature is the $\mathfrak{g}$-valued $2$-form $\Omega = d\omega + \tfrac12[\omega\wedge\omega]$ of the **structure equation**, feeding directly into Chern–Weil theory and the construction of characteristic classes from invariant polynomials of the curvature.
