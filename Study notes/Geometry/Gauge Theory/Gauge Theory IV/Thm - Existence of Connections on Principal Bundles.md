---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Connection on a Principal Bundle"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Thm - Existence of Smooth Partitions of Unity"
  - "Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space"
  - "Def - Adjoint Bundles ad P and Ad P"
  - "Thm - The Space of Connections is an Affine Space"
  - "Def - The Maurer-Cartan Form"
  - "Def - Fundamental Vector Field of a Group Action"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a Lie group with Lie algebra $\mathfrak{g} = T_eG$, and $\pi\colon P \to M$ is a smooth principal $G$-bundle over a smooth manifold $M$. The group acts on $P$ on the **right**, written $R_g(p) = p \cdot g$; this is the standing convention of the series, so that a representation acting on the left of a fibre never collides with the structural action. For $\xi \in \mathfrak{g}$ the **fundamental vector field** is $\xi_P(p) = \frac{d}{dt}\big|_{t=0}\, p\cdot\exp(t\xi)$, the velocity of the orbit through $p$ in the direction $\xi$; its values at $p$ sweep out the **vertical subspace** $V_p := \ker(d\pi_p) = \{\xi_P(p) : \xi \in \mathfrak{g}\}$, and $\xi \mapsto \xi_P(p)$ is a linear isomorphism $\mathfrak{g} \to V_p$ (this is the content of **[[Def - Fundamental Vector Field of a Group Action]]**). The **adjoint representation** is $\operatorname{Ad}\colon G \to GL(\mathfrak{g})$, $\operatorname{Ad}_g = d_e(h \mapsto ghg^{-1})$; for a matrix group $\operatorname{Ad}_g X = gXg^{-1}$.

We write $\Omega^p(M; E) = \Gamma(\Lambda^p T^*M \otimes E)$ for the smooth $E$-valued $p$-forms on $M$, where $E \to M$ is a vector bundle, and $\Omega^p(P; \mathfrak{g})$ for the smooth $\mathfrak{g}$-valued $p$-forms on the total space $P$, with $\mathfrak{g}$ regarded as a fixed vector space carrying the $G$-action $\operatorname{Ad}$. The **Maurer–Cartan form** $\theta \in \Omega^1(G; \mathfrak{g})$ is $\theta_g = d_g L_{g^{-1}}\colon T_gG \to T_eG = \mathfrak{g}$; it satisfies $R_h^*\theta = \operatorname{Ad}_{h^{-1}}\theta$ and $\theta(\tilde\xi) = \xi$ for the left-invariant field $\tilde\xi$, and for matrix groups $\theta = g^{-1}\,dg$ (all proved on **[[Def - The Maurer-Cartan Form]]**).

A **connection form** on $P$ is a form $\omega \in \Omega^1(P; \mathfrak{g})$ satisfying the two defining clauses

$$\text{(1)}\quad R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega \ \ \forall g \in G, \qquad\qquad \text{(2)}\quad \omega(\xi_P) = \xi \ \ \forall \xi \in \mathfrak{g},$$

restated in full from **[[Def - Connection on a Principal Bundle]]**. Clause (1) is equivariance of type $\operatorname{Ad}$; clause (2) reproduces $\xi$ from the vertical vector $\xi_P$, and in particular pins $\omega$ down on all of $V_p$. We denote the set of all connection forms on $P$ by $\mathcal{A}(P)$ (Bär writes $\mathcal{C}(P)$; Haydys writes $\mathcal{A}(P)$ but uses the letter $a$ for the connection form and $\operatorname{ad}$ for what we call $\operatorname{Ad}$).

A form $\beta \in \Omega^p(P; \mathfrak{g})$ is **horizontal** (Bär: **basic**) if it vanishes whenever one of its arguments is vertical, and **equivariant of type $\operatorname{Ad}$** if $R_g^*\beta = \operatorname{Ad}_{g^{-1}}\beta$ for all $g$. The space of forms that are both is written $\Omega^p_{\mathrm{bas}}(P; \mathfrak{g})^G$. The **adjoint bundle** is the associated vector bundle $\operatorname{ad}P := P \times_{\operatorname{Ad}} \mathfrak{g}$, whose fibre is $\mathfrak{g}$ and whose structure is that of **[[Def - Adjoint Bundles ad P and Ad P]]**; sections of $\operatorname{ad}P$ and, more generally, $\operatorname{ad}P$-valued forms on $M$ correspond bijectively to basic equivariant $\mathfrak{g}$-valued forms on $P$ by pull-back, which is the theorem **[[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space]]** restated at its point of use below.

We fix once and for all a **trivialising open cover** $\{U_\alpha\}_{\alpha \in I}$ of $M$ together with smooth **local sections** $s_\alpha\colon U_\alpha \to P$ (equivalently local trivialisations), whose existence over a trivialising set is **[[Thm - Sections of a Principal Bundle and Triviality]]**; on overlaps $U_{\alpha\beta} := U_\alpha \cap U_\beta$ the **transition functions** $g_{\alpha\beta}\colon U_{\alpha\beta} \to G$ are the unique smooth maps with $s_\beta = s_\alpha \cdot g_{\alpha\beta}$. Given $\omega \in \mathcal{A}(P)$, its **local connection forms** are $\omega_\alpha := s_\alpha^*\omega \in \Omega^1(U_\alpha; \mathfrak{g})$. Finally $\{\rho_\alpha\}_{\alpha \in I}$ denotes a smooth partition of unity subordinate to $\{U_\alpha\}$, i.e. $\rho_\alpha \in C^\infty(M)$, $\rho_\alpha \geq 0$, $\operatorname{supp}\rho_\alpha \subset U_\alpha$, the family $\{\operatorname{supp}\rho_\alpha\}$ locally finite, and $\sum_\alpha \rho_\alpha = 1$; its existence is **[[Thm - Existence of Smooth Partitions of Unity]]**.

> [!warning] Convention: "$G$-invariant" versus "$\operatorname{Ad}$-equivariant"
> In sketching this theorem Haydys (Theorem 41, Remark p. 16) says the difference $b = a - a'$ of two connections is "basic and $G$-invariant". By "$G$-invariant" he means precisely equivariant of type $\operatorname{Ad}$, that is $R_g^*b = \operatorname{Ad}_{g^{-1}}b$ — not $R_g^*b = b$. The series always writes **equivariant of type $\operatorname{Ad}$** for this, and reserves "$G$-invariant" for the honest invariance $R_g^*b = b$ (which holds for $\operatorname{ad}$-valued forms only when $G$ is abelian, since then $\operatorname{Ad}$ is trivial). Bär's Definition 2.3.1 as printed drops the form from clause (1), writing "$R_g^* = \operatorname{Ad}_{g^{-1}}\circ\omega$"; the intended statement is $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\circ\omega$, which is what we use.

---

# Statement

> **Theorem (existence and affine structure of the space of connections).** Let $\pi\colon P \to M$ be a smooth principal $G$-bundle over a smooth (Hausdorff, second countable) manifold $M$, and let $\operatorname{ad}P = P \times_{\operatorname{Ad}} \mathfrak{g}$ be its adjoint bundle. Then:
>
> **(a) Existence.** The set $\mathcal{A}(P)$ of connection forms on $P$ is non-empty; $\mathcal{A}(P) \neq \varnothing$.
>
> **(b) Differences are basic and equivariant.** For any two connection forms $\omega, \omega' \in \mathcal{A}(P)$, the difference $\omega - \omega' \in \Omega^1(P; \mathfrak{g})$ is horizontal and equivariant of type $\operatorname{Ad}$, so that $\omega - \omega' \in \Omega^1_{\mathrm{bas}}(P; \mathfrak{g})^G$; consequently there is a unique $b \in \Omega^1(M; \operatorname{ad}P)$ with $\pi^*b = \omega - \omega'$.
>
> **(c) Shifts by adjoint-valued forms are connections.** For any $\omega \in \mathcal{A}(P)$ and any $b \in \Omega^1(M; \operatorname{ad}P)$, with $\hat{b} := \pi^*b \in \Omega^1_{\mathrm{bas}}(P; \mathfrak{g})^G$ its basic equivariant lift, the form $\omega + \hat{b}$ is again a connection form.
>
> **(d) Local difference law.** For $\omega, \omega' \in \mathcal{A}(P)$ with local forms $\omega_\alpha = s_\alpha^*\omega$ and $\omega'_\alpha = s_\alpha^*\omega'$, the local differences transform on overlaps $U_{\alpha\beta}$ by
> $$\omega_\beta - \omega'_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}\big(\omega_\alpha - \omega'_\alpha\big),$$
> with no inhomogeneous term; hence the family $\big([s_\alpha,\, \omega_\alpha - \omega'_\alpha]\big)_\alpha$ is the local description of a single global form in $\Omega^1(M; \operatorname{ad}P)$, recovering the $b$ of part (b) from the ground.
>
> Taken together, (a)–(c) say that $\mathcal{A}(P)$ is a non-empty **affine space modelled on the vector space $\Omega^1(M; \operatorname{ad}P)$**: the difference of two connections is an element of $\Omega^1(M; \operatorname{ad}P)$, every such element is realised as a difference, and fixing one connection $\omega_0$ identifies $\mathcal{A}(P)$ with $\Omega^1(M; \operatorname{ad}P)$ via $b \mapsto \omega_0 + \pi^*b$.

The bundle $\operatorname{ad}P$ has rank $\dim \mathfrak{g}$, so $\Omega^1(M; \operatorname{ad}P)$ is an infinite-dimensional real vector space (a space of sections), and $\mathcal{A}(P)$ is an infinite-dimensional affine space. It has no distinguished origin: the zero form $0 \in \Omega^1(P; \mathfrak{g})$ fails clause (2), since $0(\xi_P) = 0 \neq \xi$ for $\xi \neq 0$, so $0 \notin \mathcal{A}(P)$ and $\mathcal{A}(P)$ is not a vector subspace of $\Omega^1(P; \mathfrak{g})$.

---

# Motivation

Everything that gauge theory does with a principal bundle — parallel transport, holonomy, curvature, the Yang–Mills functional, characteristic numbers — begins by *choosing a connection*. Before any of that can proceed we must know two things: that a connection exists at all on an arbitrary principal bundle, and that the collection of all connections has a usable structure. This theorem settles both. Part (a) is the licence to speak of "a connection on $P$" for any $P$; parts (b), (c), and the affine conclusion are the structure theorem for the configuration space of gauge theory.

The role of the affine structure is not decorative. In gauge theory one integrates and does variational calculus over $\mathcal{A}(P)$: the Yang–Mills action $\omega \mapsto \tfrac12\int_M |F_\omega|^2$ is a function on $\mathcal{A}(P)$ whose critical points are the Yang–Mills connections, and the Chern–Simons functional is a function on $\mathcal{A}(P)$ whose gradient is the curvature. To differentiate such a function one needs to add a small perturbation to a connection and stay inside $\mathcal{A}(P)$ — which is exactly what part (c) guarantees, with the perturbation living in the honest vector space $\Omega^1(M; \operatorname{ad}P)$ so that the tangent space to $\mathcal{A}(P)$ at every point is canonically this fixed vector space. The later homotopy argument for the Chern–Weil theorem interpolates linearly between two connections, $\omega_t = \omega_0 + t(\omega_1 - \omega_0)$, and is legitimate only because part (c) tells us every $\omega_t$ is a connection and part (b) tells us $\omega_1 - \omega_0$ is a genuine $\operatorname{ad}P$-valued form on the base along which to differentiate. The gauge group acts on $\mathcal{A}(P)$ by affine transformations, and the quotient — the space of gauge-equivalence classes — is the true configuration space of the theory; its analysis in chapter V rests on the affine picture established here.

The theorem is also the principal-bundle counterpart of the vector-bundle fact **[[Thm - The Space of Connections is an Affine Space|the space of connections on a vector bundle is affine over $\Omega^1(M; \operatorname{End}E)$]]**. There the difference of two covariant derivatives is a tensor because the derivation terms cancel; here the difference of two connection forms is horizontal because both reproduce $\xi$ on $\xi_P$, and equivariant because both are. The two statements are the same phenomenon read in two languages, and the frame-bundle correspondence of §4.4 turns one into the other precisely.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is only "a smooth principal bundle over a manifold"; the interesting sources are the properties that silently deliver such a bundle together with the ingredients the proof consumes.

The first disguised source is **a manifold carrying a free proper Lie group action**. If a Lie group $G$ acts freely and properly on a manifold $Q$, the quotient $Q \to Q/G$ is a principal $G$-bundle (this is the quotient-manifold theorem of chapter I applied in **[[Def - Principal G-Bundle]]**). The non-obvious bridge $B \Rightarrow A$ is that freeness and properness are exactly what make the orbit space a manifold and the projection a submersion with the local product structure the present theorem needs; once that is in hand, this theorem endows $Q/G$ with a connection with no further work. *Example problem:* the frame bundle of any Riemannian manifold arises this way, and this theorem gives it a connection — which the Levi-Civita connection then singles out.

The second disguised source is **paracompactness of the base**, hiding inside the phrase "smooth manifold". The proof's only global input is a partition of unity subordinate to a trivialising cover, and that is available precisely because a smooth (Hausdorff, second countable) manifold is paracompact. The bridge is that second countability plus local compactness forces paracompactness, hence partitions of unity, hence the gluing in part (a). *Example problem:* over a base that failed to be paracompact — a long line, say — the construction would break at exactly the gluing step, and connections need not exist; recognising that "manifold" already supplies paracompactness is what lets the proof go through unremarked.

The third disguised source is **any reduction of the structure group**. If $P$ reduces to a subgroup $H \leq G$ — an orthonormal frame bundle inside the full frame bundle, a spin structure over an oriented orthonormal frame bundle — then the reduced bundle $Q$ is itself a principal $H$-bundle, and this theorem produces an $H$-connection on $Q$, which extends to a $G$-connection on $P$ compatible with the reduction. The bridge $B \Rightarrow A$ is that a reduction *is* a principal subbundle, so the theorem applies to it verbatim. *Example problem:* a metric on a vector bundle reduces its frame bundle to $O(k)$; the theorem then yields a metric connection, the abstract source of the Levi-Civita construction.

**Targets (Output Amplification).** The bare outputs — "a connection exists" and "$\mathcal{A}(P)$ is affine" — combine with further ingredients to do much more.

Combine **existence** with a **compact structure group and an $\operatorname{Ad}$-invariant inner product on $\mathfrak{g}$**. A compact $G$ carries a bi-invariant metric, hence an $\operatorname{Ad}$-invariant inner product on $\mathfrak{g}$; feeding the connection from part (a) into this inner product produces the norm $|F_\omega|$ and thus the Yang–Mills functional $\tfrac12\int_M|F_\omega|^2$. The payoff is that the entire variational theory of chapter VII has a non-empty domain to vary over. The extra ingredient is the invariant inner product; the target is a well-posed functional on $\mathcal{A}(P)$.

Combine the **affine structure** with the **curvature map**. The assignment $\omega \mapsto F_\omega$ sends $\mathcal{A}(P)$ to $\Omega^2(M; \operatorname{ad}P)$, and along the affine line $\omega + t\hat b$ (legitimate by part (c)) its derivative is the exterior covariant derivative $d^\omega \hat b$. This is the linearisation that the Chern–Weil homotopy formula of chapter VI integrates to prove that the Chern–Weil form is closed and its cohomology class independent of the connection. The extra ingredient is the structure equation for the curvature; the target is topological invariance of characteristic classes.

Combine the **affine structure** with an **action of the gauge group**. The gauge group $\mathcal{G}(P)$ acts on $\mathcal{A}(P)$ by affine maps, and part (b) identifies the tangent space to every orbit inside the fixed vector space $\Omega^1(M; \operatorname{ad}P)$. The payoff, developed in chapter V and used decisively in Seiberg–Witten and Donaldson theory, is a slice theorem and a manifold structure on the quotient $\mathcal{A}(P)/\mathcal{G}(P)$: the affine model is what makes the orbit space amenable to the infinite-dimensional differential geometry the moduli theory requires.

---

# Why Is It True

Two clauses cut $\Omega^1(P; \mathfrak{g})$ down to $\mathcal{A}(P)$: clause (2) fixes a form's values on the vertical directions to be the tautological identification $\xi_P \mapsto \xi$, and clause (1) fixes how it must rotate under the group. Neither clause touches the *horizontal* directions — the directions transverse to the fibres — beyond the equivariance constraint (1). So a connection is a choice, made compatibly along each fibre, of how to read a Lie-algebra element off of every tangent vector, agreeing with the canonical reading on vertical vectors. The whole theorem is the geometry of that "choice on the horizontal part".

**Existence** is a soft, local-to-global argument. On a set where $P$ is a product $U_\alpha \times G$ there is an obvious connection — the Maurer–Cartan form on the $G$ factor, which reads off the vertical part in the only canonical way and ignores the base. Transporting it through the trivialisation gives a connection over $\pi^{-1}(U_\alpha)$. These local connections disagree on overlaps, but the two defining clauses are *affine* in $\omega$: clause (2) is preserved by any weighted average whose weights sum to one, and clause (1) is preserved by any weighted average with fibre-constant weights. A partition of unity supplies exactly such weights, so the average glues the local connections into a global one.

> The single mechanism behind existence is that a connection is a section of an *affine* constraint, and affine constraints are stable under partition-of-unity averaging, so local solutions always glue.

**The affine structure** is the observation that the two clauses are *inhomogeneous linear* in $\omega$: clause (1) is linear, and clause (2) is linear with the fixed right-hand side $\xi$. Subtracting two solutions kills the right-hand side — the difference reproduces $\xi - \xi = 0$ on $\xi_P$, so it is horizontal — while keeping the linear equivariance — so it is equivariant. Thus differences land in the *homogeneous* solution space, the basic equivariant forms, which by the fundamental correspondence between forms upstairs and forms downstairs is nothing but $\Omega^1(M; \operatorname{ad}P)$. Conversely, adding a homogeneous solution to an inhomogeneous one gives another inhomogeneous one. That is the entire content of "affine space modelled on $\Omega^1(M; \operatorname{ad}P)$": the solution set of an inhomogeneous linear condition is a coset of the solution set of its homogenisation.

---

# What Makes This Hard

The one genuine subtlety is that clause (2) is a condition about *vertical* vectors while a connection form is defined on *all* tangent vectors, and the two clauses interact through the fundamental-field identity $dR_g(\xi_P(p)) = (\operatorname{Ad}_{g^{-1}}\xi)_P(pg)$ — one must know that the equivariance clause (1) and the normalisation clause (2) are compatible rather than contradictory, which is why the sign is $\operatorname{Ad}_{g^{-1}}$ and not $\operatorname{Ad}_g$. The common error in the existence half is to forget that the locally defined forms are only defined over $\pi^{-1}(U_\alpha)$, so that $(\rho_\alpha\circ\pi)\,\omega^{(\alpha)}$ must be interpreted as extended by zero — legitimate only because $\operatorname{supp}\rho_\alpha \subset U_\alpha$. The common error in the affine half is to conflate "horizontal and equivariant" with "invariant" (see the Convention callout); the difference of two connections is equivariant of type $\operatorname{Ad}$, which is genuinely weaker than invariance whenever $G$ is non-abelian, and it is exactly this weaker condition that matches $\operatorname{ad}P$-valued rather than $\mathfrak{g}$-valued forms on the base.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build a connection locally by transporting the Maurer–Cartan form through each trivialisation, then average with a partition of unity, exploiting that the two connection clauses are affine. For the structure, subtract two connections to land in the horizontal-equivariant forms, identify those with $\Omega^1(M; \operatorname{ad}P)$ by the basic-forms correspondence, and check the affine-space axioms directly.

**Subgoal decomposition:**

1. **Differential of the right action.** Establish $d\hat{R}_{(p,g)}(v, w) = dR_g(v) + \big(\theta_g(w)\big)_P(p\cdot g)$ for the action map $\hat R(p,g) = p\cdot g$.
   - *Hint:* Split the curve $\hat R(p(t), g(t))$ into the two one-parameter motions and apply the product rule; the $g$-motion produces a fundamental vector field with parameter $\theta_g(w)$.
   - *Why needed:* It gives the canonical decomposition of every tangent vector to $P$ over a trivialising set, and reappears in the local difference law of part (d).

2. **Local connection from a section.** Over a trivialising $U_\alpha$ define $\omega^{(\alpha)}$ by declaring $\omega^{(\alpha)}\big(dR_g\,ds_\alpha(v) + \xi_P\big) = \xi$, and verify it is a smooth local connection form.
   - *Hint:* This is the pull-back of $\operatorname{pr}_2^*\theta$ through $\Psi_\alpha(x,g) = s_\alpha(x)\cdot g$; check clause (2) directly and clause (1) with $R_h^*\theta = \operatorname{Ad}_{h^{-1}}\theta$.
   - *Why needed:* It supplies the local solutions to be glued.

3. **Affine averaging.** Show that a fibre-constant convex combination $\sum_\alpha (\rho_\alpha\circ\pi)\,\omega^{(\alpha)}$, with $\sum_\alpha \rho_\alpha = 1$, again satisfies clauses (1) and (2).
   - *Hint:* Clause (2) uses $\sum \rho_\alpha = 1$; clause (1) uses that $\operatorname{Ad}_{h^{-1}}$ is linear and $\pi\circ R_h = \pi$.
   - *Why needed:* It produces the global connection, proving part (a).

4. **Difference and shift.** Show $\omega - \omega'$ is horizontal and equivariant, and that $\omega + \hat b$ is a connection for basic equivariant $\hat b$.
   - *Hint:* Both are one-line consequences of the linearity of clauses (1) and (2) in $\omega$.
   - *Why needed:* Parts (b) and (c).

5. **Affine-space axioms.** Using the basic-forms correspondence, verify the difference map $\mathcal{A}(P)\times\mathcal{A}(P) \to \Omega^1(M; \operatorname{ad}P)$ is regular and satisfies the Chasles relation.
   - *Hint:* Injectivity of $\pi^*$ turns every identity of forms on $M$ into a checkable identity of forms on $P$.
   - *Why needed:* It upgrades (a)–(c) into the precise statement "affine space modelled on $\Omega^1(M; \operatorname{ad}P)$".

6. **Local difference law.** Pull the horizontal equivariant $\omega - \omega'$ back by $s_\alpha$ and $s_\beta$ and use horizontality to kill the vertical part of $ds_\beta$.
   - *Hint:* $s_\beta = s_\alpha\cdot g_{\alpha\beta}$; apply subgoal 1 and then equivariance.
   - *Why needed:* Part (d), and a second, ground-level proof of part (b).

---

# Lemma Decomposition

> [!note]- Lemma 1: Differential of the right action map
> **Statement:** Let $\hat{R}\colon P \times G \to P$, $\hat{R}(p, g) = p\cdot g$, be the action map. For $(v, w) \in T_pP \oplus T_gG = T_{(p,g)}(P\times G)$,
> $$d\hat{R}_{(p,g)}(v, w) = dR_g(v) + \big(\theta_g(w)\big)_P(p\cdot g),$$
> where $\theta_g(w) = d_gL_{g^{-1}}(w) \in \mathfrak{g}$ is the Maurer–Cartan form and $R_g\colon P \to P$ is right translation by the fixed element $g$.
>
> **Hint:** Decompose a curve realising $(v,w)$ into a $P$-motion at fixed $g$ and a $G$-motion at fixed $p$, and read the $G$-motion as an orbit curve to produce a fundamental vector field.
>
> **Why needed:** It gives the exact decomposition of tangent vectors used to define the local connection forms (Lemma 2) and to prove the local difference law (part (d)).
>
> > [!note]- Full proof
> > **Reduce to a sum of two motions.** Choose smooth curves $p(t)$ in $P$ with $p(0) = p$, $\dot{p}(0) = v$, and $g(t)$ in $G$ with $g(0) = g$, $\dot{g}(0) = w$. Since $\hat{R}$ is bilinear-like in the sense that its differential is additive over the two factors, we may compute $d\hat R_{(p,g)}(v,w) = d\hat R_{(p,g)}(v, 0) + d\hat R_{(p,g)}(0, w)$ (the differential of a smooth map is linear on the tangent space $T_pP \oplus T_gG$).
> >
> > **First motion (base point moves, group element fixed).** With $g$ held fixed,
> > $$d\hat R_{(p,g)}(v, 0) = \frac{d}{dt}\Big|_{0} \hat R(p(t), g) = \frac{d}{dt}\Big|_{0} p(t)\cdot g = \frac{d}{dt}\Big|_{0} R_g(p(t)) = dR_g(v) \qquad \text{(definition of } R_g \text{ and of the differential).}$$
> >
> > **Second motion (group element moves, base point fixed).** With $p$ held fixed, write $g(t) = g\cdot\big(g^{-1}g(t)\big)$ and set $h(t) := g^{-1}g(t)$, a curve in $G$ with $h(0) = e$ and
> > $$\dot{h}(0) = \frac{d}{dt}\Big|_0 g^{-1}g(t) = d_gL_{g^{-1}}(w) = \theta_g(w) =: \eta \qquad \text{(definition of } \theta \text{ and of } L_{g^{-1}}\text{).}$$
> > Then
> > $$d\hat R_{(p,g)}(0, w) = \frac{d}{dt}\Big|_0 p\cdot g(t) = \frac{d}{dt}\Big|_0 (p\cdot g)\cdot h(t) \qquad \text{(associativity of the action, } p\cdot g(t) = (p\cdot g)\cdot(g^{-1}g(t))\text{).}$$
> > The curve $t \mapsto (p\cdot g)\cdot h(t)$ passes through $p\cdot g$ at $t = 0$ with $h(0) = e$ and $\dot h(0) = \eta$. Because the fundamental vector field of $\eta$ at a point $q$ is $\eta_P(q) = \frac{d}{dt}\big|_0 q\cdot\exp(t\eta)$ and the value $\frac{d}{dt}\big|_0 q\cdot h(t)$ depends only on $h(0) = e$ and $\dot h(0) = \eta$ (the velocity of the orbit map $g \mapsto q\cdot g$ at $e$ applied to $\dot h(0)$), we get
> > $$\frac{d}{dt}\Big|_0 (p\cdot g)\cdot h(t) = \eta_P(p\cdot g) = \big(\theta_g(w)\big)_P(p\cdot g) \qquad \text{(definition of the fundamental vector field; } \eta = \theta_g(w)\text{).}$$
> >
> > **Combine.** Adding the two motions,
> > $$d\hat R_{(p,g)}(v, w) = dR_g(v) + \big(\theta_g(w)\big)_P(p\cdot g),$$
> > as claimed. Note the second summand is vertical, being a fundamental vector field value, so this is the horizontal-transport-plus-vertical decomposition. $\blacksquare$

> [!note]- Lemma 2: A trivialising section transports the Maurer–Cartan form to a local connection
> **Statement:** Let $U_\alpha \subset M$ be a trivialising set with local section $s_\alpha\colon U_\alpha \to P$, and let $\Psi_\alpha\colon U_\alpha \times G \to \pi^{-1}(U_\alpha)$, $\Psi_\alpha(x, g) = s_\alpha(x)\cdot g$, be the induced $G$-equivariant diffeomorphism. Every $p \in \pi^{-1}(U_\alpha)$ is $p = s_\alpha(x)\cdot g$ for unique $x = \pi(p)$ and $g \in G$, and every $Y \in T_pP$ has a **unique** decomposition
> $$Y = dR_g\big(ds_\alpha(v)\big) + \xi_P(p), \qquad v \in T_xU_\alpha,\ \xi \in \mathfrak{g}.$$
> The form $\omega^{(\alpha)} \in \Omega^1(\pi^{-1}(U_\alpha); \mathfrak{g})$ defined by $\omega^{(\alpha)}_p(Y) := \xi$ is a smooth connection form on the restricted bundle $P|_{U_\alpha} \to U_\alpha$; equivalently $\omega^{(\alpha)} = (\Psi_\alpha^{-1})^*\big(\operatorname{pr}_2^*\theta\big)$, the transport of the product connection.
>
> **Hint:** Existence and uniqueness of the decomposition is Lemma 1 applied to $\Psi_\alpha$; clause (2) is immediate; clause (1) follows from $R_h^*\theta = \operatorname{Ad}_{h^{-1}}\theta$ and the equivariance of $\Psi_\alpha$.
>
> **Why needed:** It supplies, over each chart, the local connection that the partition of unity will glue.
>
> > [!note]- Full proof
> > **Step 0 — the decomposition exists and is unique.** The map $\Psi_\alpha(x, g) = s_\alpha(x)\cdot g = \hat R(s_\alpha(x), g)$ is a diffeomorphism onto $\pi^{-1}(U_\alpha)$ because $s_\alpha$ is a section over a trivialising set (by **[[Thm - Sections of a Principal Bundle and Triviality]]**: a local section over $U_\alpha$ is equivalent to a trivialisation $U_\alpha \times G \cong \pi^{-1}(U_\alpha)$, and this is that trivialisation). Fix $p = s_\alpha(x)\cdot g$. Applying Lemma 1 to the composite $\Psi_\alpha = \hat R \circ (s_\alpha \times \operatorname{id})$, a tangent vector $Y = d\Psi_\alpha(v, w)$ with $v \in T_xU_\alpha$, $w \in T_gG$ equals
> > $$Y = d\hat R_{(s_\alpha(x), g)}\big(ds_\alpha(v), w\big) = dR_g\big(ds_\alpha(v)\big) + \big(\theta_g(w)\big)_P(p) \qquad \text{(Lemma 1).}$$
> > Since $\Psi_\alpha$ is a diffeomorphism its differential is a linear isomorphism, so $(v, w) \mapsto Y$ is a bijection $T_xU_\alpha \oplus T_gG \to T_pP$; and since $\theta_g\colon T_gG \to \mathfrak{g}$ is a linear isomorphism (it is $d_gL_{g^{-1}}$, an isomorphism of vector spaces), $\xi := \theta_g(w)$ ranges over $\mathfrak{g}$ bijectively as $w$ ranges over $T_gG$. Hence every $Y$ is uniquely $Y = dR_g(ds_\alpha(v)) + \xi_P(p)$ with $v \in T_xU_\alpha$, $\xi \in \mathfrak{g}$ determined by $Y$. This makes $\omega^{(\alpha)}_p(Y) := \xi$ a well-defined linear map $T_pP \to \mathfrak{g}$, and $\omega^{(\alpha)}$ smooth because in the chart $\Psi_\alpha$ it is literally $\operatorname{pr}_2^*\theta$: indeed $\omega^{(\alpha)}(d\Psi_\alpha(v,w)) = \theta_g(w) = (\operatorname{pr}_2^*\theta)_{(x,g)}(v, w)$, so $\omega^{(\alpha)} = (\Psi_\alpha^{-1})^*(\operatorname{pr}_2^*\theta)$, a pull-back of a smooth form by a diffeomorphism.
> >
> > **Clause (2): $\omega^{(\alpha)}(\eta_P) = \eta$.** Take $Y = \eta_P(p)$, i.e. $v = 0$ and $\xi = \eta$ in the decomposition (setting the base motion to zero). Then by definition $\omega^{(\alpha)}_p(\eta_P(p)) = \eta$ for every $\eta \in \mathfrak{g}$. This is clause (2).
> >
> > **Clause (1): $R_h^*\omega^{(\alpha)} = \operatorname{Ad}_{h^{-1}}\omega^{(\alpha)}$.** Right translation $R_h$ corresponds under $\Psi_\alpha$ to $(x, g) \mapsto (x, gh)$, because $\Psi_\alpha(x, gh) = s_\alpha(x)\cdot(gh) = (s_\alpha(x)\cdot g)\cdot h = R_h(\Psi_\alpha(x, g))$ (associativity of the action). Denote by $\sigma_h\colon U_\alpha\times G \to U_\alpha\times G$, $\sigma_h(x,g) = (x, gh)$, so that $\Psi_\alpha \circ \sigma_h = R_h \circ \Psi_\alpha$. Then
> > $$\Psi_\alpha^* R_h^* \omega^{(\alpha)} = \sigma_h^* \Psi_\alpha^* \omega^{(\alpha)} = \sigma_h^*\big(\operatorname{pr}_2^*\theta\big) = \operatorname{pr}_2^*\big(R_h^*\theta\big) \qquad \text{(functoriality of pull-back; } \operatorname{pr}_2\circ\sigma_h = R_h\circ\operatorname{pr}_2\text{),}$$
> > where on the last step $\operatorname{pr}_2\circ\sigma_h(x,g) = gh = R_h(\operatorname{pr}_2(x,g))$ with $R_h$ now right translation on $G$. Using the Maurer–Cartan equivariance $R_h^*\theta = \operatorname{Ad}_{h^{-1}}\theta$ (proved on **[[Def - The Maurer-Cartan Form]]**),
> > $$\Psi_\alpha^* R_h^* \omega^{(\alpha)} = \operatorname{pr}_2^*\big(\operatorname{Ad}_{h^{-1}}\theta\big) = \operatorname{Ad}_{h^{-1}}\big(\operatorname{pr}_2^*\theta\big) = \operatorname{Ad}_{h^{-1}}\big(\Psi_\alpha^*\omega^{(\alpha)}\big) = \Psi_\alpha^*\big(\operatorname{Ad}_{h^{-1}}\omega^{(\alpha)}\big),$$
> > using that $\operatorname{Ad}_{h^{-1}}$ is a fixed linear map on $\mathfrak{g}$ and so commutes with pull-back of $\mathfrak{g}$-valued forms. Since $\Psi_\alpha^*$ is injective (as $\Psi_\alpha$ is a diffeomorphism), $R_h^*\omega^{(\alpha)} = \operatorname{Ad}_{h^{-1}}\omega^{(\alpha)}$, which is clause (1).
> >
> > Both clauses hold, so $\omega^{(\alpha)}$ is a connection form on $P|_{U_\alpha}$. $\blacksquare$

> [!note]- Lemma 3: Fibre-constant convex combinations of connection forms are connection forms
> **Statement:** Let $\{U_\alpha\}$ be an open cover of $M$ and, for each $\alpha$, let $\omega^{(\alpha)}$ be a connection form on $P|_{U_\alpha}$. Let $\{\rho_\alpha\}$ be a smooth partition of unity subordinate to $\{U_\alpha\}$ (so $\operatorname{supp}\rho_\alpha \subset U_\alpha$, the supports locally finite, $\sum_\alpha \rho_\alpha = 1$). Then
> $$\omega := \sum_{\alpha} (\rho_\alpha\circ\pi)\,\omega^{(\alpha)} \in \Omega^1(P; \mathfrak{g})$$
> — with each summand extended by zero off $\pi^{-1}(U_\alpha)$ — is a globally defined smooth connection form on $P$.
>
> **Hint:** Clause (2) collapses by $\sum \rho_\alpha = 1$; clause (1) survives because $\pi\circ R_g = \pi$ and $\operatorname{Ad}_{g^{-1}}$ is linear.
>
> **Why needed:** It is the gluing step of the existence proof (part (a)).
>
> > [!note]- Full proof
> > **Step 0 — $\omega$ is a well-defined smooth global form.** The product $(\rho_\alpha\circ\pi)\,\omega^{(\alpha)}$ is smooth on $\pi^{-1}(U_\alpha)$, where both factors are defined, and its support is contained in $\pi^{-1}(\operatorname{supp}\rho_\alpha) \subset \pi^{-1}(U_\alpha)$, a closed set of $P$ on which the product is smooth; extending it by zero on the open complement $P \setminus \pi^{-1}(\operatorname{supp}\rho_\alpha)$ therefore yields a smooth form on all of $P$ (the two definitions agree on the overlap, where both are zero). The family of supports $\{\pi^{-1}(\operatorname{supp}\rho_\alpha)\}$ is locally finite in $P$ because $\{\operatorname{supp}\rho_\alpha\}$ is locally finite in $M$ and $\pi$ is continuous, so the sum $\omega = \sum_\alpha (\rho_\alpha\circ\pi)\,\omega^{(\alpha)}$ is locally a finite sum of smooth forms and is smooth.
> >
> > **Clause (2): $\omega(\xi_P) = \xi$.** Fix $p \in P$, $x = \pi(p)$, and $\xi \in \mathfrak{g}$. For every $\alpha$ with $\rho_\alpha(x) \neq 0$ we have $x \in \operatorname{supp}\rho_\alpha \subset U_\alpha$, hence $p \in \pi^{-1}(U_\alpha)$ and $\omega^{(\alpha)}$ is defined at $p$ with $\omega^{(\alpha)}_p(\xi_P(p)) = \xi$ (clause (2) for $\omega^{(\alpha)}$). Therefore
> > $$\omega_p(\xi_P(p)) = \sum_\alpha \rho_\alpha(\pi(p))\,\omega^{(\alpha)}_p(\xi_P(p)) = \sum_\alpha \rho_\alpha(x)\,\xi = \Big(\sum_\alpha \rho_\alpha(x)\Big)\xi = 1\cdot\xi = \xi \qquad \text{(clause (2) for each } \omega^{(\alpha)}\text{; } \textstyle\sum_\alpha \rho_\alpha = 1\text{),}$$
> > where terms with $\rho_\alpha(x) = 0$ contribute nothing. This is clause (2) for $\omega$.
> >
> > **Clause (1): $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega$.** Pull back each summand. Since $\pi\circ R_g = \pi$ (right translation preserves fibres), the scalar factor is unchanged: $(\rho_\alpha\circ\pi)\circ R_g = \rho_\alpha\circ(\pi\circ R_g) = \rho_\alpha\circ\pi$. Hence
> > $$R_g^*\omega = \sum_\alpha R_g^*\big((\rho_\alpha\circ\pi)\,\omega^{(\alpha)}\big) = \sum_\alpha \big((\rho_\alpha\circ\pi)\circ R_g\big)\,R_g^*\omega^{(\alpha)} = \sum_\alpha (\rho_\alpha\circ\pi)\,\operatorname{Ad}_{g^{-1}}\omega^{(\alpha)} \qquad \text{(pull-back of a product; } \pi\circ R_g = \pi \text{; clause (1) for each } \omega^{(\alpha)}\text{).}$$
> > Because $\operatorname{Ad}_{g^{-1}}$ is a fixed linear map on $\mathfrak{g}$, it pulls out of the sum:
> > $$R_g^*\omega = \operatorname{Ad}_{g^{-1}}\Big(\sum_\alpha (\rho_\alpha\circ\pi)\,\omega^{(\alpha)}\Big) = \operatorname{Ad}_{g^{-1}}\omega \qquad \text{(linearity of } \operatorname{Ad}_{g^{-1}}\text{).}$$
> > This is clause (1) for $\omega$. Both clauses hold, so $\omega \in \mathcal{A}(P)$. $\blacksquare$

> [!note]- Lemma 4: Differences are horizontal-equivariant, and shifts by such forms are connections
> **Statement:** Let $\omega, \omega' \in \mathcal{A}(P)$ and $\beta \in \Omega^1_{\mathrm{bas}}(P; \mathfrak{g})^G$ (horizontal and equivariant of type $\operatorname{Ad}$). Then $\omega - \omega' \in \Omega^1_{\mathrm{bas}}(P; \mathfrak{g})^G$, and $\omega + \beta \in \mathcal{A}(P)$.
>
> **Hint:** Every claim is a one-line use of the linearity of clauses (1), (2) in $\omega$ together with $\beta(\xi_P) = 0$.
>
> **Why needed:** It is the algebraic heart of parts (b) and (c).
>
> > [!note]- Full proof
> > **The difference is horizontal.** Every vertical vector at $p$ is $\xi_P(p)$ for a unique $\xi \in \mathfrak{g}$ (isomorphism $\mathfrak{g}\to V_p$). For such a vector,
> > $$(\omega - \omega')(\xi_P) = \omega(\xi_P) - \omega'(\xi_P) = \xi - \xi = 0 \qquad \text{(clause (2) for } \omega \text{ and for } \omega'\text{).}$$
> > A $1$-form vanishing on every vertical vector is horizontal (for a $1$-form, "one argument vertical" is the only case), so $\omega - \omega'$ is horizontal.
> >
> > **The difference is equivariant.** For all $g \in G$,
> > $$R_g^*(\omega - \omega') = R_g^*\omega - R_g^*\omega' = \operatorname{Ad}_{g^{-1}}\omega - \operatorname{Ad}_{g^{-1}}\omega' = \operatorname{Ad}_{g^{-1}}(\omega - \omega') \qquad \text{(clause (1) for } \omega \text{ and for } \omega'\text{; linearity of } \operatorname{Ad}_{g^{-1}}\text{).}$$
> > Hence $\omega - \omega' \in \Omega^1_{\mathrm{bas}}(P; \mathfrak{g})^G$.
> >
> > **The shift satisfies clause (2).** Since $\beta$ is horizontal, $\beta(\xi_P) = 0$, so
> > $$(\omega + \beta)(\xi_P) = \omega(\xi_P) + \beta(\xi_P) = \xi + 0 = \xi \qquad \text{(clause (2) for } \omega \text{; } \beta \text{ horizontal).}$$
> >
> > **The shift satisfies clause (1).** Since $\beta$ is equivariant,
> > $$R_g^*(\omega + \beta) = R_g^*\omega + R_g^*\beta = \operatorname{Ad}_{g^{-1}}\omega + \operatorname{Ad}_{g^{-1}}\beta = \operatorname{Ad}_{g^{-1}}(\omega + \beta) \qquad \text{(clause (1) for } \omega \text{; equivariance of } \beta\text{; linearity of } \operatorname{Ad}_{g^{-1}}\text{).}$$
> > Both clauses hold, so $\omega + \beta \in \mathcal{A}(P)$. $\blacksquare$

> [!note]- Lemma 5: Local representatives of a basic equivariant form transform by $\operatorname{Ad}_{g_{\alpha\beta}^{-1}}$
> **Statement:** Let $\beta \in \Omega^1_{\mathrm{bas}}(P; \mathfrak{g})^G$ and set $\beta_\alpha := s_\alpha^*\beta \in \Omega^1(U_\alpha; \mathfrak{g})$. Then on every overlap $U_{\alpha\beta}$,
> $$\beta_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}\,\beta_\alpha .$$
>
> **Hint:** Differentiate $s_\beta = s_\alpha\cdot g_{\alpha\beta}$ by Lemma 1, discard the vertical part using horizontality of $\beta$, and apply equivariance.
>
> **Why needed:** It is part (d), and it re-proves part (b) from the ground: the local pieces glue by exactly the $\operatorname{ad}P$ cocycle law.
>
> > [!note]- Full proof
> > **Differentiate the section relation.** Fix $x \in U_{\alpha\beta}$ and $v \in T_xM$. Writing $s_\beta = \hat R\circ(s_\alpha, g_{\alpha\beta})$, Lemma 1 gives
> > $$ds_\beta(v) = d\hat R_{(s_\alpha(x),\, g_{\alpha\beta}(x))}\big(ds_\alpha(v),\, dg_{\alpha\beta}(v)\big) = dR_{g_{\alpha\beta}(x)}\big(ds_\alpha(v)\big) + \Big(\theta_{g_{\alpha\beta}(x)}\big(dg_{\alpha\beta}(v)\big)\Big)_P\big(s_\beta(x)\big) \qquad \text{(Lemma 1).}$$
> > The second summand is a fundamental vector field value at $s_\beta(x)$, hence vertical.
> >
> > **Discard the vertical part.** Since $\beta$ is horizontal it annihilates the vertical summand, so
> > $$\beta_\beta(v) = (s_\beta^*\beta)(v) = \beta_{s_\beta(x)}\big(ds_\beta(v)\big) = \beta_{s_\beta(x)}\Big(dR_{g_{\alpha\beta}(x)}\big(ds_\alpha(v)\big)\Big) \qquad \text{(} \beta \text{ horizontal, killing the vertical term).}$$
> >
> > **Apply equivariance.** Write $h := g_{\alpha\beta}(x)$, so $s_\beta(x) = s_\alpha(x)\cdot h$. Equivariance $R_h^*\beta = \operatorname{Ad}_{h^{-1}}\beta$ evaluated at $s_\alpha(x)$ on the vector $ds_\alpha(v)$ reads $\beta_{s_\alpha(x)\cdot h}\big(dR_h(ds_\alpha(v))\big) = \operatorname{Ad}_{h^{-1}}\,\beta_{s_\alpha(x)}\big(ds_\alpha(v)\big)$. Therefore
> > $$\beta_\beta(v) = \operatorname{Ad}_{h^{-1}}\,\beta_{s_\alpha(x)}\big(ds_\alpha(v)\big) = \operatorname{Ad}_{g_{\alpha\beta}(x)^{-1}}\big(s_\alpha^*\beta\big)(v) = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}\,\beta_\alpha(v) \qquad \text{(equivariance of } \beta \text{; definition of } \beta_\alpha\text{).}$$
> > As $x \in U_{\alpha\beta}$ and $v \in T_xM$ were arbitrary, $\beta_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}\beta_\alpha$ on $U_{\alpha\beta}$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\pi\colon P \to M$ be a smooth principal $G$-bundle with adjoint bundle $\operatorname{ad}P = P\times_{\operatorname{Ad}}\mathfrak{g}$.
>
> **Step 0 — the ingredients exist.** Since $M$ is a smooth (Hausdorff, second countable) manifold, it is paracompact and admits an open cover $\{U_\alpha\}$ over which $P$ trivialises, with local sections $s_\alpha\colon U_\alpha \to P$ (by **[[Thm - Sections of a Principal Bundle and Triviality]]**, a trivialisation over $U_\alpha$ is the same datum as a local section) and a subordinate smooth partition of unity $\{\rho_\alpha\}$, $\sum_\alpha \rho_\alpha = 1$ with $\operatorname{supp}\rho_\alpha \subset U_\alpha$ (by **[[Thm - Existence of Smooth Partitions of Unity]]**). Fix these once and for all.
>
> **Part (a) — existence.** For each $\alpha$, Lemma 2 produces a connection form $\omega^{(\alpha)}$ on $P|_{U_\alpha}$, defined by $\omega^{(\alpha)}(dR_g\,ds_\alpha(v) + \xi_P) = \xi$ (the transport of the product connection $\operatorname{pr}_2^*\theta$ through the trivialisation $\Psi_\alpha(x,g) = s_\alpha(x)\cdot g$). Applying Lemma 3 to the family $\{\omega^{(\alpha)}\}$ with the partition of unity $\{\rho_\alpha\}$,
> $$\omega := \sum_\alpha (\rho_\alpha\circ\pi)\,\omega^{(\alpha)} \in \Omega^1(P; \mathfrak{g})$$
> is a globally defined connection form on $P$. Hence $\omega \in \mathcal{A}(P)$ and $\mathcal{A}(P) \neq \varnothing$.
>
> **Part (b) — differences.** Let $\omega, \omega' \in \mathcal{A}(P)$. By the first two claims of Lemma 4, $\omega - \omega' \in \Omega^1_{\mathrm{bas}}(P; \mathfrak{g})^G$, that is, $\omega - \omega'$ is horizontal and equivariant of type $\operatorname{Ad}$. Now invoke the correspondence between forms on the base and basic equivariant forms upstairs:
> > **[[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|Basic-forms correspondence]].** For a $G$-representation $(V, \rho)$, the pull-back $a \mapsto \pi^*a$ is a linear bijection $\Omega^q(M; P\times_\rho V) \xrightarrow{\ \sim\ } \Omega^q_{\mathrm{bas}}(P; V)^G$.
>
> Applying it with $V = \mathfrak{g}$ and $\rho = \operatorname{Ad}$, so that $P\times_{\operatorname{Ad}}\mathfrak{g} = \operatorname{ad}P$, there is a **unique** $b \in \Omega^1(M; \operatorname{ad}P)$ with $\pi^*b = \omega - \omega'$. This is the assertion of part (b).
>
> **Part (c) — shifts.** Let $\omega \in \mathcal{A}(P)$ and $b \in \Omega^1(M; \operatorname{ad}P)$. By the basic-forms correspondence, $\hat b := \pi^*b \in \Omega^1_{\mathrm{bas}}(P; \mathfrak{g})^G$ is horizontal and equivariant. By the last two claims of Lemma 4, $\omega + \hat b \in \mathcal{A}(P)$. This is part (c).
>
> **The affine-space structure.** Define the **difference map**
> $$D\colon \mathcal{A}(P)\times\mathcal{A}(P) \longrightarrow \Omega^1(M; \operatorname{ad}P), \qquad D(\omega, \omega') := b \ \text{ where } \pi^*b = \omega - \omega',$$
> which is well-defined and single-valued by part (b) (existence of $b$) together with the injectivity of $\pi^*$ from the basic-forms correspondence (uniqueness of $b$). We verify the two axioms of an affine space modelled on the vector space $W := \Omega^1(M; \operatorname{ad}P)$.
>
> *Chasles (additivity) relation.* For $\omega, \omega', \omega'' \in \mathcal{A}(P)$,
> $$\pi^*\big(D(\omega,\omega') + D(\omega',\omega'')\big) = (\omega - \omega') + (\omega' - \omega'') = \omega - \omega'' = \pi^*\,D(\omega,\omega'') \qquad \text{(linearity of } \pi^* \text{; definition of } D\text{).}$$
> Since $\pi^*$ is injective, $D(\omega,\omega') + D(\omega',\omega'') = D(\omega,\omega'')$.
>
> *Regularity (free transitive translation).* Fix $\omega \in \mathcal{A}(P)$. The map $W \to \mathcal{A}(P)$, $b \mapsto \omega + \pi^*b$, is well-defined by part (c). It is **surjective**: given any $\omega'' \in \mathcal{A}(P)$, part (b) yields $b = D(\omega'', \omega)$ with $\pi^*b = \omega'' - \omega$, i.e. $\omega'' = \omega + \pi^*b$. It is **injective**: if $\omega + \pi^*b_1 = \omega + \pi^*b_2$ then $\pi^*b_1 = \pi^*b_2$, and injectivity of $\pi^*$ gives $b_1 = b_2$. Hence for every $\omega \in \mathcal{A}(P)$ the translation $b \mapsto \omega + \pi^*b$ is a bijection $W \to \mathcal{A}(P)$.
>
> The Chasles relation and the regularity of translation are exactly the axioms defining an **affine space modelled on $W$** (equivalently, $(W, +)$ acts freely and transitively on $\mathcal{A}(P)$ via $b\cdot\omega := \omega + \pi^*b$). Therefore $\mathcal{A}(P)$ is an affine space modelled on $\Omega^1(M; \operatorname{ad}P)$, and it is non-empty by part (a). This is the principal-bundle analogue of **[[Thm - The Space of Connections is an Affine Space|the affine structure of the space of vector-bundle connections]]**, which asserts the corresponding statement for covariant derivatives modelled on $\Omega^1(M; \operatorname{End}E)$; the frame-bundle correspondence of §4.4 identifies the two.
>
> **Part (d) — local difference law.** Apply Lemma 5 to $\beta := \omega - \omega'$, which is horizontal and equivariant by part (b). Its local representatives are $\beta_\alpha = s_\alpha^*(\omega - \omega') = s_\alpha^*\omega - s_\alpha^*\omega' = \omega_\alpha - \omega'_\alpha$. Lemma 5 gives, on each overlap $U_{\alpha\beta}$,
> $$\omega_\beta - \omega'_\beta = \beta_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}\,\beta_\alpha = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}\big(\omega_\alpha - \omega'_\alpha\big),$$
> which is the local difference law; there is no inhomogeneous Maurer–Cartan term precisely because $\beta$ is horizontal and so ignored the vertical part of $ds_\beta$. This is exactly the cocycle law $\beta_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}\beta_\alpha$ that an $\operatorname{ad}P$-valued $1$-form's local representatives satisfy, so the family $([s_\alpha,\, \omega_\alpha - \omega'_\alpha])_\alpha$ is the local description of the global $b \in \Omega^1(M; \operatorname{ad}P)$ of part (b), re-derived from the base.
>
> All four parts and the affine conclusion are proved. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Line bundles and the Picard group (complex geometry).** For a Hermitian line bundle $L \to M$ the associated principal bundle has abelian structure group $U(1)$, and here $\operatorname{Ad}$ is trivial, so $\operatorname{ad}P = M\times i\mathbb{R}$ and $\Omega^1(M; \operatorname{ad}P) = \Omega^1(M; i\mathbb{R})$. The theorem then says the space of $U(1)$-connections is affine over the ordinary imaginary-valued $1$-forms, so the difference of two connections is a global $1$-form $iA$. This is non-obvious because it makes the physicist's "gauge potential difference is a genuine $1$-form" a theorem rather than a coordinate accident, and it is the starting point for identifying the first Chern class with a curvature integral. The exercise is to specialise every step of the proof to abelian $G$ and watch "$\operatorname{ad}P$-valued" collapse to "$\mathfrak{g}$-valued".

**Riemannian geometry via the orthonormal frame bundle.** The orthonormal frame bundle $O(TM) \to M$ of a Riemannian manifold is a principal $O(n)$-bundle; the theorem furnishes a connection, and among all connections the metric-compatible torsion-free one is the Levi-Civita connection. The application is non-obvious because it decouples *existence* of a connection (soft, this theorem) from *uniqueness* of a distinguished one (rigid, the fundamental theorem of Riemannian geometry): the affine space of $O(n)$-connections is where the Levi-Civita connection is then pinned down by two further linear conditions. The exercise is to show that metric compatibility and vanishing torsion each cut out an affine subspace and that their intersection is a single point.

**Configuration spaces in lattice-free gauge theory (mathematical physics).** In Yang–Mills theory the fields are connections and the theorem's affine structure is what makes the path integral and the perturbative expansion even formulatable: one expands $\omega = \omega_0 + \hat a$ around a background connection $\omega_0$, with the fluctuation $\hat a \in \Omega^1(M; \operatorname{ad}P)$ a field in a fixed vector space. The application is non-obvious because it explains why gauge fixing and the Faddeev–Popov procedure live on an affine space with a linear group of translations rather than on a curved manifold. The exercise is to identify the tangent space $T_\omega\mathcal{A}(P)$ with $\Omega^1(M; \operatorname{ad}P)$ for every $\omega$ and to write the gauge-group action as an affine action.

---

# Bridges

- **The vector-bundle affine theorem.** The statement here is the exact principal-bundle mirror of **[[Thm - The Space of Connections is an Affine Space]]**: there, two covariant derivatives $\nabla, \nabla'$ on a vector bundle $E$ differ by a tensor $\nabla - \nabla' \in \Omega^1(M; \operatorname{End}E)$ because the two Leibniz terms cancel; here, two connection forms differ by a horizontal equivariant form because both reproduce $\xi$ on $\xi_P$. Under the frame-bundle correspondence $\nabla \leftrightarrow \omega$ of §4.4, with $\operatorname{End}E = \operatorname{Fr}(E)\times_{\operatorname{Ad}}\mathfrak{gl}_k$ playing the role of $\operatorname{ad}P$, the two affine structures are identified, and the difference tensor of vector-bundle connections is the same object as the difference form of frame-bundle connections read through the standard representation.

- **The basic-forms dictionary.** The step from "$\omega - \omega'$ is horizontal and equivariant" to "$\omega - \omega'$ is a form on the base valued in $\operatorname{ad}P$" is a single application of **[[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space]]**. That dictionary is used again and again in this chapter — for the curvature (which descends from the horizontal equivariant $\Omega$ on $P$ to $F_\omega \in \Omega^2(M; \operatorname{ad}P)$ on the base) and for the exterior covariant derivative — so the present theorem is a first, clean instance of the principle that geometry compatible with the group descends to the quotient.

- **The local transformation law.** Part (d) is the difference of the full inhomogeneous transformation law $\omega_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}}\omega_\alpha + g_{\alpha\beta}^*\theta$ proved on **[[Thm - Transformation of Local Connection and Curvature Forms]]**: the Maurer–Cartan term $g_{\alpha\beta}^*\theta$ is the same for $\omega$ and $\omega'$ and cancels, leaving the homogeneous $\operatorname{Ad}$-cocycle law. The present page derives the difference law directly from horizontality (Lemma 5), which is why it can precede the transformation-law page in logical order without circularity.

- **Partitions of unity as the soft-analysis engine.** The existence half is a template that recurs throughout the series: any structure defined by an *affine* local condition (connections, Riemannian metrics, Hermitian structures, splittings) exists globally on a paracompact base because local solutions average. The same **[[Thm - Existence of Smooth Partitions of Unity]]** underwrites the existence of Riemannian metrics and of metric connections; recognising the shared mechanism is more valuable than any single instance of it.

---

# Unlocked by This

> [!tip] The configuration space of gauge theory *(from Yang–Mills theory)*
> With $\mathcal{A}(P)$ known to be a non-empty affine space modelled on $\Omega^1(M; \operatorname{ad}P)$, the Yang–Mills functional becomes a genuine function on a genuine (infinite-dimensional affine) space, its first variation is taken by translating along $\Omega^1(M; \operatorname{ad}P)$, and its critical points are the Yang–Mills connections. See **Def - Yang-Mills Lagrangian and Action Functional**.

> [!tip] The gauge-orbit space *(from moduli theory)*
> The gauge group acts on the affine space $\mathcal{A}(P)$, and the quotient $\mathcal{A}(P)/\mathcal{G}(P)$ is the configuration space whose geometry Donaldson and Seiberg–Witten theory study; the affine model established here is what gives the orbit space its slice charts and (generically) its manifold structure. See **Thm - Gauge Transformations Act on Connections and Curvature**.

> [!tip] Connection-independence of characteristic classes *(from Chern–Weil theory)*
> Because any two connections are joined by the affine segment $\omega_t = \omega_0 + t(\omega_1 - \omega_0)$ of connections (part (c)), the Chern–Weil form's cohomology class can be shown independent of the connection by differentiating along $t$; the difference $\omega_1 - \omega_0 \in \Omega^1(M; \operatorname{ad}P)$ (part (b)) is the object one differentiates against. See **Thm - Chern-Weil Theorem**.
