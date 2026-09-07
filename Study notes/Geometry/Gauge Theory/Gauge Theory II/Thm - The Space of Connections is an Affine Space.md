---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Connection on a Vector Bundle"
  - "Def - Connection Matrix and Local Form of a Connection"
  - "Def - Bundle-Valued Differential Forms"
  - "Thm - Tensoriality Lemma for C-Infinity-Linear Maps"
  - "Thm - Existence of Smooth Partitions of Unity"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a smooth manifold — by our standing convention smooth, Hausdorff, and second countable, hence paracompact and equipped with smooth partitions of unity — and $\pi : E \to M$ is a smooth real [[Def - Vector Bundle|vector bundle]] of rank $k$. We write $\Gamma(E)$ for the space of smooth [[Def - Section of a Vector Bundle|sections]] of $E$, and $C^\infty(M)$ for the smooth real-valued functions on $M$; both are $\mathbb{R}$-vector spaces, and $\Gamma(E)$ is a module over $C^\infty(M)$ under pointwise multiplication $(f s)(m) = f(m)\, s(m)$.

For a vector bundle $F \to M$ we write, following our standing convention, $\Omega^p(M; F) = \Gamma(\Lambda^p T^*M \otimes F)$ for the space of [[Def - Bundle-Valued Differential Forms|$F$-valued differential $p$-forms]]; thus $\Omega^0(M; F) = \Gamma(F)$ and $\Omega^1(M; F) = \Gamma(T^*M \otimes F)$. The endomorphism bundle $\operatorname{End} E = E^* \otimes E$ has fibre $\operatorname{End}(E_m) = \operatorname{Hom}(E_m, E_m)$, the linear self-maps of the fibre $E_m$; its sections are the smooth fields of fibrewise endomorphisms.

A **connection** (covariant derivative) on $E$ is, by [[Def - Connection on a Vector Bundle|definition]], an $\mathbb{R}$-linear map
$$\nabla : \Gamma(E) \longrightarrow \Omega^1(M; E) = \Gamma(T^*M \otimes E)$$
satisfying the **Leibniz rule**
$$\nabla(f s) = df \otimes s + f\, \nabla s \qquad \text{for all } f \in C^\infty(M),\ s \in \Gamma(E),$$
where $df \in \Omega^1(M)$ is [[Def - The Differential of a Function as a 1-Form|the differential]] of $f$. We write $\mathcal{A}(E)$ for the set of all connections on $E$.

An element $a \in \Omega^1(M; \operatorname{End} E)$ **acts on sections** by contraction of the $\operatorname{End} E$-value against the section: $a \cdot s \in \Omega^1(M; E)$ is the $E$-valued $1$-form
$$(a \cdot s)(X) := a(X)\, s \qquad (X \text{ a tangent vector at a point of } M),$$
where $a(X) \in \operatorname{End}(E_m)$ is the endomorphism obtained by evaluating the $1$-form part of $a$ on $X$, applied to $s \in E_m$. In a local frame this is matrix-times-column with $1$-form entries; the operation is $C^\infty(M)$-bilinear in $(a, s)$.

> [!warning] Convention: source labelling
> This page proves Haydys, *Introduction to Gauge Theory*, Theorem 11 (p. 7), together with the reading of $\mathcal{A}(E)$ as an affine space "modelled on $\Omega^1(\operatorname{End} E)$" recorded there. Haydys leaves the tensoriality lemma (his Lemma 12) as an exercise, sews the local connections together only "just like in the proof of the existence of Riemannian metrics" ([BT03, Thm. 3.3.7]), and calls part (c) "straightforward". All three are written out in full below; the tensoriality lemma is proved on its own page [[Thm - Tensoriality Lemma for C-Infinity-Linear Maps]] and invoked here with its statement restated at the point of use.

We recall the notion the conclusion uses. A set $\mathcal{A}$ is an **affine space modelled on** a real vector space $V$ if it is non-empty and carries a map $\mathcal{A} \times V \to \mathcal{A}$, written $(\nabla, a) \mapsto \nabla + a$, which is a free and transitive action of the additive group $(V, +)$: it satisfies $\nabla + 0 = \nabla$ and $(\nabla + a) + b = \nabla + (a + b)$, and for every pair $\nabla, \hat\nabla \in \mathcal{A}$ there is a **unique** $a \in V$ with $\hat\nabla = \nabla + a$, denoted $a = \hat\nabla - \nabla$. Equivalently: $\mathcal{A}$ is a vector space that has forgotten where its origin is; choosing any one point $\nabla_0 \in \mathcal{A}$ identifies $\mathcal{A} \xrightarrow{\ \sim\ } V$, $\nabla \mapsto \nabla - \nabla_0$, but no such origin is distinguished. Here $V = \Omega^1(M; \operatorname{End} E)$.

---

# Statement

> **Theorem (the space of connections is an affine space).** Let $E \to M$ be a smooth real vector bundle over a smooth manifold. Then the set $\mathcal{A}(E)$ of all connections on $E$ is an affine space modelled on $\Omega^1(M; \operatorname{End} E) = \Gamma(T^*M \otimes \operatorname{End} E)$. Concretely, the three constituent statements hold:
> $$\textbf{(a)}\quad \mathcal{A}(E) \neq \varnothing;$$
> $$\textbf{(b)}\quad \text{for any two connections } \nabla, \hat\nabla \in \mathcal{A}(E), \text{ the difference } \nabla - \hat\nabla : \Gamma(E) \to \Omega^1(M; E) \text{ is } C^\infty(M)\text{-linear,}$$
> $$\qquad\quad\ \text{hence } \exists!\, a \in \Omega^1(M; \operatorname{End} E) \text{ with } (\nabla - \hat\nabla)s = a \cdot s \text{ for all } s \in \Gamma(E);$$
> $$\textbf{(c)}\quad \text{for any } \nabla \in \mathcal{A}(E) \text{ and any } a \in \Omega^1(M; \operatorname{End} E), \text{ the map } (\nabla + a)s := \nabla s + a \cdot s \text{ is a connection.}$$
> Assembling (a), (b), (c): the map $\Omega^1(M; \operatorname{End} E) \times \mathcal{A}(E) \to \mathcal{A}(E)$, $(a, \nabla) \mapsto \nabla + a$, is a free transitive action of the vector space $\Omega^1(M; \operatorname{End} E)$ on the non-empty set $\mathcal{A}(E)$.

---

# Motivation

The theorem answers two questions at once, and it is worth separating them, because the proof answers them by quite different means.

The first question is existence: *does every vector bundle carry a connection at all?* This is not obvious. A connection is a global object — an operator defined on global sections, satisfying an identity that couples it to differentiation of functions — and there is no formula that produces one from the bundle data. On a trivial bundle $M \times \mathbb{R}^k$ the componentwise exterior derivative $d$ is a connection, but a general bundle is only *locally* trivial, and the local exterior derivatives attached to different trivialisations disagree on overlaps. The content of part (a) is that this disagreement can be averaged away: local connections always exist, and although they cannot simply be glued (the transition rule for a connection is inhomogeneous), a *partition of unity* combines them into a global connection. That this works at all is the same phenomenon that produces Riemannian metrics, volume forms, and every other object whose local existence is trivial and whose obstruction to gluing is affine rather than linear.

The second question is structural: *once connections exist, how are they related to one another?* Parts (b) and (c) answer that the set of all connections is not merely non-empty but has a rigid and useful shape. Two connections never differ by "an arbitrary operator"; their difference is always a **tensor** — a bundle-valued $1$-form, a pointwise-linear gadget, not a differential operator. Conversely, any tensor of the right type can be added to a connection to produce a new one. So $\mathcal{A}(E)$ is a copy of the vector space $\Omega^1(M; \operatorname{End} E)$ with the origin erased: an affine space. This is the structural fact on which the entire subject is built. It says that "the space of gauge fields" is flat and infinite-dimensional in a completely controlled way; that the difference of two gauge potentials is a physical field (a $1$-form with values in the adjoint bundle); that one may take convex combinations, straight-line paths, and derivatives of connections; and that the tangent space to $\mathcal{A}(E)$ at every point is canonically the single vector space $\Omega^1(M; \operatorname{End} E)$, which is what makes the linearised Yang–Mills, instanton, and Seiberg–Witten equations elliptic problems on a fixed Banach space.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is as weak as a hypothesis can be — "$E$ is a smooth vector bundle over a smooth manifold" — so the source question is really: *when does a problem secretly hand you such a bundle over such a base, so that the theorem silently applies and connections are available for free?*

The first disguised source is **a principal bundle together with a representation**. If $P \to M$ is a principal $G$-bundle and $\rho : G \to GL(V)$ a representation, the associated bundle $P \times_\rho V \to M$ is a smooth vector bundle even though no vector bundle was named; the bridge $B \Rightarrow A$ is the associated-bundle construction, which manufactures the fibrewise vector-space structure and the local trivialisations out of the principal data. The theorem then guarantees connections on $P \times_\rho V$; in fact these are exactly the covariant derivatives induced by principal connections, by [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|the induced-connection theorem]]. *Example problem:* show that the spinor bundle of a spin manifold — built as an associated bundle to the spin frame bundle — carries a covariant derivative, so that the Dirac operator can be written down at all.

The second disguised source is **a smooth map with a bundle downstairs**. Given a smooth map $f : N \to M$ and a vector bundle $E \to M$, the pull-back $f^* E \to N$ is again a smooth vector bundle over the smooth manifold $N$; the bridge is the pull-back construction, whose local trivialisations are the pre-images under $f$ of those of $E$. The theorem then supplies connections on $f^* E$ over $N$ with no further hypotheses on $f$. The non-obvious point is that even a map to a single point, or a highly degenerate $f$, still yields a genuine vector bundle whose affine space of connections is non-empty. *Example problem:* along a smooth curve $\gamma : [0,1] \to M$, the pull-back $\gamma^* TM$ carries connections, which is what allows one to speak of parallel transport as an ordinary differential equation.

The third disguised source is **the assertion that the base is a manifold**, invoked purely for the existence half. Existence of a connection rests on the existence of a partition of unity subordinate to any open cover, and *that* rests on paracompactness. A space is not obviously paracompact, but "smooth manifold" — Hausdorff and second countable in our convention — implies it. The bridge $B \Rightarrow A$ is the theorem that a second-countable, locally Euclidean Hausdorff space is paracompact, hence admits [[Thm - Existence of Smooth Partitions of Unity|smooth partitions of unity]]. *Example problem:* explain why the construction of part (a) would fail over a non-paracompact base such as the long line, even though local connections still exist there — the local pieces cannot be summed.

**Targets (Output Amplification)**

The bare conclusion is "$\mathcal{A}(E)$ is an affine space". Combined with other structures it does a great deal.

Combine the conclusion with **a group acting on connections**. The [[Def - Gauge Group of a Vector Bundle|gauge group]] $\mathcal{G}(E) = \{g \in \Gamma(\operatorname{End} E) : g(m) \in GL(E_m)\}$ acts on $\mathcal{A}(E)$ on the right by $\nabla^g s = g^{-1}\nabla(g s)$. Because $\mathcal{A}(E)$ is affine, one computes $\nabla^g = \nabla + g^{-1}(d^\nabla g)$, so the gauge action is an *affine* action: gauge orbits are affine subsets of an affine space, and the moduli space $\mathcal{A}(E)/\mathcal{G}(E)$ that carries all the invariants of the theory is a quotient of an affine space by an affine action. This is the extra ingredient — a group of symmetries — and the payoff is that the whole machinery of §2.4 has a linear model at every orbit.

Combine the conclusion with **the curvature map $\nabla \mapsto F_\nabla$**. Since $\mathcal{A}(E)$ is affine, one may write any connection as $\nabla + a$ and expand the curvature. The extra ingredient is [[Def - Curvature of a Vector-Bundle Connection|the curvature]], and the payoff is [[Thm - Curvature of a Shifted Connection|the shift formula]] $F_{\nabla + a} = F_\nabla + d^\nabla a + a \wedge a$, whose linear part $a \mapsto d^\nabla a$ is the derivative of the curvature map at $\nabla$. This linearisation, living on the fixed vector space $\Omega^1(M; \operatorname{End} E)$, is precisely the operator whose ellipticity drives the deformation theory of Yang–Mills and Seiberg–Witten moduli spaces.

Combine the conclusion with **convexity and homotopy invariance**. Affine spaces are convex, so the straight-line path $A_t = (1-t)A_0 + t A_1$ joins any two connections through connections; the extra ingredient is a functional that is closed or invariant along such paths. The payoff is that Chern–Weil characteristic forms are independent of the connection: their cohomology class does not change as $A_t$ varies, because $\mathcal{A}(E)$ is contractible. The affine structure is what makes "the topology of $E$" extractable from any connection whatsoever.

Finally, the same statement has a **principal-bundle version**: the space $\mathcal{A}(P)$ of connections on a principal $G$-bundle is an affine space modelled on $\Omega^1(M; \operatorname{ad} P)$, proved as [[Thm - Existence of Connections on Principal Bundles|the existence theorem for principal connections]]. The vector-bundle case here is both the model for that proof and its special case through associated bundles.

---

# Why Is It True

Strip away the bundle language and look at what the Leibniz rule is as a condition on the unknown operator $\nabla$. It reads
$$\nabla(fs) = \underbrace{df \otimes s}_{\text{fixed, independent of } \nabla} + f\, \nabla s.$$
The right-hand side has an inhomogeneous term $df \otimes s$ that does not involve $\nabla$ at all, plus a term linear in $\nabla$. A condition of the form "(linear in the unknown) $=$ (fixed inhomogeneity)" is an **affine** condition, exactly like a system of linear equations $L x = b$ with $b \neq 0$. Its solution set, if non-empty, is a coset of the solution set of the *homogeneous* problem $L x = 0$. Here the homogeneous problem is "$A(fs) = f\, A s$", the condition that $A$ be $C^\infty(M)$-linear — and by the tensoriality lemma the $C^\infty(M)$-linear maps $\Gamma(E) \to \Omega^1(M; E)$ are exactly the tensors $a \in \Omega^1(M; \operatorname{End} E)$. So the solution set of the Leibniz condition, *provided it is non-empty*, is a coset of $\Omega^1(M; \operatorname{End} E)$: an affine space over it. That is parts (b) and (c) in a sentence.

Non-emptiness — part (a) — is the only genuinely geometric input, and its mechanism is averaging. Over a trivialising set the bundle looks like $U \times \mathbb{R}^k$ and the componentwise exterior derivative is a connection, so local connections always exist. They cannot be glued directly, because the "average of two connections" makes sense only as an *affine* average $t\nabla + (1-t)\hat\nabla$ with weights summing to one — and this is where the inhomogeneity re-enters helpfully: when the weights sum to $1$, the fixed term $df \otimes s$ is reproduced with coefficient $\sum_\alpha \rho_\alpha = 1$, so the affine combination again satisfies Leibniz, whereas a combination with weights summing to anything other than $1$ would scale $df \otimes s$ wrongly and fail. A partition of unity provides exactly weights summing to $1$, so it glues the local connections into a global one.

> **Mechanism, in one sentence:** the Leibniz rule is an inhomogeneous linear condition on $\nabla$, so its solution set is an affine space over the homogeneous solutions (the tensors $\Omega^1(\operatorname{End} E)$); local solutions exist because the bundle is locally trivial, and affine combinations of solutions — with weights summing to one, as a partition of unity supplies — are again solutions, so the local pieces glue.

---

# What Makes This Hard

The step that trips people is the interplay between "linear" and "affine". A beginner expects the space of connections to be a vector space and looks for a canonical zero connection; there is none on a non-trivial bundle, and the sum $\nabla + \hat\nabla$ of two connections is **not** a connection — its Leibniz defect is $2\, df \otimes s$, not $df \otimes s$. Only affine combinations, with coefficients summing to one, stay inside $\mathcal{A}(E)$; this is precisely why the partition of unity (whose functions sum to one) is the right gluing device and an arbitrary open-cover sum is not. The second subtlety is that the difference of two connections is a *tensor*: each connection is a first-order differential operator, yet the derivative terms cancel in the difference, leaving a pointwise-linear map — a fact that must be verified by the Leibniz computation and then converted to an actual bundle-valued form by the tensoriality lemma, not asserted. The third, quieter subtlety is the smoothness of the glued section: each local piece $\rho_\alpha \nabla^\alpha(s|_{U_\alpha})$ is defined only on $U_\alpha$, and one must justify — using $\operatorname{supp}\rho_\alpha \subset U_\alpha$ — that extending it by zero yields a *smooth* global section before summing.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove the three constituent statements in the order (c), (b), (a)-machinery, then assemble. Part (c) is a direct Leibniz check. Part (b) is a Leibniz check that the difference is $C^\infty(M)$-linear, followed by one invocation of the tensoriality lemma. Part (a) is the only construction: build local connections from trivialisations, then average them with a partition of unity, using that affine combinations preserve the Leibniz rule. Finally read off the affine-space axioms from (b) and (c).

**Subgoal decomposition:**

1. **Local connections exist.** On a trivialising set $U$ with trivialisation $\psi_U$, show $\nabla^U s := \psi_U^{-1}\, d(\psi_U s)$ is a connection on $E|_U$.
   - *Hint:* $\psi_U s : U \to \mathbb{R}^k$ is an ordinary vector-valued function; apply the ordinary Leibniz rule for $d$ componentwise and push it back through the fibrewise-linear isomorphism $\psi_U^{-1}$.
   - *Why needed:* Without a local supply of connections there is nothing for the partition of unity to average.

2. **Affine combinations of connections are connections.** If $\{\nabla_\alpha\}$ are connections (each on the relevant domain) and $\{\rho_\alpha\} \subset C^\infty(M)$ satisfy $\sum_\alpha \rho_\alpha = 1$ locally finitely with $\operatorname{supp}\rho_\alpha$ inside the domain of $\nabla_\alpha$, then $\nabla s := \sum_\alpha \rho_\alpha \nabla_\alpha(s|_{U_\alpha})$ (extended by zero) is a connection.
   - *Hint:* $\mathbb{R}$-linearity is termwise; for Leibniz, the inhomogeneous term collects the coefficient $\sum_\alpha \rho_\alpha = 1$. Check smoothness of each extended term using the support condition.
   - *Why needed:* This is the gluing engine; convexity ($\alpha \in \{0,1\}$, two terms) is its simplest case and part (a) is its application to local connections.

3. **Assemble part (a).** Cover $M$ by trivialising sets, take a subordinate partition of unity, and feed the local connections of subgoal 1 into subgoal 2.
   - *Hint:* A smooth manifold admits partitions of unity subordinate to any open cover; the trivialising sets form such a cover.
   - *Why needed:* It produces one global connection, so $\mathcal{A}(E) \neq \varnothing$.

4. **Part (c).** For $\nabla \in \mathcal{A}(E)$ and $a \in \Omega^1(M; \operatorname{End} E)$, show $\nabla + a$ is a connection.
   - *Hint:* $a \cdot (fs) = f\,(a \cdot s)$ because $a$ acts fibrewise-linearly, so the extra term contributes nothing to the Leibniz defect.
   - *Why needed:* It gives the action of the model vector space on $\mathcal{A}(E)$ — that new connections lie a tensor away.

5. **Part (b).** For $\nabla, \hat\nabla \in \mathcal{A}(E)$, show $\nabla - \hat\nabla$ is $C^\infty(M)$-linear, then apply the tensoriality lemma to get the unique $a$.
   - *Hint:* Subtract the two Leibniz rules; the $df \otimes s$ terms cancel, leaving $C^\infty(M)$-linearity. Uniqueness of $a$ is because sections determine a bundle map.
   - *Why needed:* It gives that the action is free and transitive, completing the affine-space structure.

---

# Lemma Decomposition

> [!note]- Lemma 1: Every trivialisation defines a local connection
> **Statement:** Let $U \subseteq M$ be open and $\psi_U : E|_U \xrightarrow{\ \sim\ } U \times \mathbb{R}^k$ a [[Def - Local Trivialization|local trivialisation]], a fibrewise-linear diffeomorphism over $U$. For $s \in \Gamma(E|_U)$ let $\psi_U s : U \to \mathbb{R}^k$ denote the smooth principal part (so $\psi_U(s(m)) = (m, (\psi_U s)(m))$). Then
> $$\nabla^U s := \psi_U^{-1}\big(d(\psi_U s)\big)$$
> is a connection on $E|_U$, where $d$ is the componentwise exterior derivative of an $\mathbb{R}^k$-valued function and $\psi_U^{-1}$ is applied to the $E$-value.
>
> **Hint:** Reduce to the componentwise ordinary product rule $d(f\, \sigma) = df \otimes \sigma + f\, d\sigma$ for $\sigma : U \to \mathbb{R}^k$, and use that $\psi_U^{-1}$ is fibrewise linear, so it commutes with tensoring by a covector.
>
> **Why needed:** It is the local supply of connections that the partition of unity averages in part (a); without it $\mathcal{A}(E)$ could be empty.
>
> > [!note]- Full proof
> > **Goal.** We must show $\nabla^U : \Gamma(E|_U) \to \Omega^1(U; E|_U)$ is $\mathbb{R}$-linear and satisfies $\nabla^U(fs) = df \otimes s + f\,\nabla^U s$ for all $f \in C^\infty(U)$, $s \in \Gamma(E|_U)$.
> >
> > **Step 0 — the map is well defined and lands in the right space.** Since $\psi_U$ is a fibrewise-linear diffeomorphism over $U$, its principal part sends a smooth section $s$ to a smooth map $\psi_U s : U \to \mathbb{R}^k$; the componentwise exterior derivative $d(\psi_U s)$ is then a smooth $\mathbb{R}^k$-valued $1$-form, that is, an element of $\Omega^1(U; \underline{\mathbb{R}^k})$ with $\underline{\mathbb{R}^k} = U \times \mathbb{R}^k$. Applying the bundle isomorphism $\psi_U^{-1}$ to the $\mathbb{R}^k$-value (leaving the covector slot untouched) produces $\nabla^U s \in \Omega^1(U; E|_U)$. This uses only that $\psi_U^{-1}$ is smooth and fibrewise linear.
> >
> > **$\mathbb{R}$-linearity.** For $s, s' \in \Gamma(E|_U)$ and $\lambda, \mu \in \mathbb{R}$, the principal part is $\mathbb{R}$-linear, $\psi_U(\lambda s + \mu s') = \lambda\,\psi_U s + \mu\,\psi_U s'$ (since $\psi_U$ is linear on fibres); the exterior derivative $d$ is $\mathbb{R}$-linear; and $\psi_U^{-1}$ is $\mathbb{R}$-linear on fibres. Composing,
> > $$\nabla^U(\lambda s + \mu s') = \psi_U^{-1} d\big(\lambda\, \psi_U s + \mu\, \psi_U s'\big) = \lambda\, \psi_U^{-1} d(\psi_U s) + \mu\, \psi_U^{-1} d(\psi_U s') = \lambda\, \nabla^U s + \mu\, \nabla^U s' \qquad (\text{by linearity of } \psi_U,\ d,\ \psi_U^{-1}).$$
> >
> > **Leibniz rule.** Let $f \in C^\infty(U)$ and $s \in \Gamma(E|_U)$. The principal part of $fs$ is the pointwise scalar multiple $\psi_U(fs) = f\, (\psi_U s)$, because $\psi_U$ is linear on each fibre. Applying the componentwise ordinary product rule to the $\mathbb{R}^k$-valued function $\psi_U s$,
> > $$d\big(\psi_U(fs)\big) = d\big(f\, \psi_U s\big) = df \otimes (\psi_U s) + f\, d(\psi_U s) \qquad (\text{ordinary Leibniz rule for } d \text{ on each of the } k \text{ components}).$$
> > Now apply $\psi_U^{-1}$ to the $\mathbb{R}^k$-value. Since $\psi_U^{-1}$ acts fibrewise-linearly and the covector $df$ is a scalar factor on each component, it commutes with tensoring by $df$ and with multiplication by the scalar function $f$:
> > $$\nabla^U(fs) = \psi_U^{-1}\big(df \otimes (\psi_U s) + f\, d(\psi_U s)\big) = df \otimes \psi_U^{-1}(\psi_U s) + f\, \psi_U^{-1} d(\psi_U s) = df \otimes s + f\, \nabla^U s \qquad (\text{fibrewise linearity of } \psi_U^{-1};\ \psi_U^{-1}\psi_U = \mathrm{id}).$$
> >
> > **Conclusion.** $\nabla^U$ is an $\mathbb{R}$-linear map satisfying the Leibniz rule, hence a connection on $E|_U$. $\blacksquare$

> [!note]- Lemma 2: Affine combinations of connections, glued by a partition of unity, are connections
> **Statement:** Let $\{U_\alpha\}_{\alpha \in I}$ be an open cover of $M$, let $\nabla^\alpha$ be a connection on $E|_{U_\alpha}$ for each $\alpha$, and let $\{\rho_\alpha\}_{\alpha \in I} \subset C^\infty(M)$ be a partition of unity with $\operatorname{supp}\rho_\alpha \subseteq U_\alpha$, the family $\{\operatorname{supp}\rho_\alpha\}$ locally finite, and $\sum_\alpha \rho_\alpha \equiv 1$. For $s \in \Gamma(E)$ and each $\alpha$, let $\rho_\alpha \nabla^\alpha(s|_{U_\alpha})$ be extended by zero from $U_\alpha$ to a global section of $T^*M \otimes E$. Then
> $$\nabla s := \sum_{\alpha \in I} \rho_\alpha\, \nabla^\alpha(s|_{U_\alpha}) \in \Omega^1(M; E)$$
> is a well-defined connection on $E$.
>
> **Hint:** For smoothness of each summand use $\operatorname{supp}\rho_\alpha \subseteq U_\alpha$: the term is $0$ on $M \setminus \operatorname{supp}\rho_\alpha$ and given on $U_\alpha$, and these two open sets cover $M$ and agree on the overlap. For the Leibniz rule, the inhomogeneous term picks up the factor $\sum_\alpha \rho_\alpha = 1$.
>
> **Why needed:** It is the gluing engine of part (a); the two-term case with $\rho_0 = t$, $\rho_1 = 1-t$ constant is exactly the convexity of $\mathcal{A}(E)$.
>
> > [!note]- Full proof
> > **Goal.** We must show (i) each summand extends to a smooth global section, (ii) the sum is locally finite hence smooth, and (iii) the resulting $\nabla$ is $\mathbb{R}$-linear and satisfies the Leibniz rule.
> >
> > **Step 0 — extension by zero is smooth.** Fix $\alpha$. The section $\rho_\alpha\, \nabla^\alpha(s|_{U_\alpha})$ is a smooth section of $T^*M \otimes E$ over the open set $U_\alpha$. Set $Z_\alpha := M \setminus \operatorname{supp}\rho_\alpha$, which is open because $\operatorname{supp}\rho_\alpha$ is closed. On $U_\alpha \cap Z_\alpha$ we have $\rho_\alpha = 0$ (indeed $\rho_\alpha$ vanishes on all of $Z_\alpha$), so the section $\rho_\alpha\, \nabla^\alpha(s|_{U_\alpha})$ equals $0$ there; and $0$ is the constant zero section on $Z_\alpha$. Thus the two smooth sections — the given one on $U_\alpha$ and the zero section on $Z_\alpha$ — agree on the overlap $U_\alpha \cap Z_\alpha$. Since $U_\alpha \cup Z_\alpha = M$ (a point outside $U_\alpha$ lies outside $\operatorname{supp}\rho_\alpha \subseteq U_\alpha$, hence in $Z_\alpha$), they patch to a smooth global section, which we still denote $\rho_\alpha\, \nabla^\alpha(s|_{U_\alpha}) \in \Omega^1(M; E)$. This is the only place the hypothesis $\operatorname{supp}\rho_\alpha \subseteq U_\alpha$ is used.
> >
> > **Step 1 — the sum is locally finite, hence a smooth section.** Since $\{\operatorname{supp}\rho_\alpha\}$ is locally finite, each $m \in M$ has a neighbourhood $W$ meeting only finitely many $\operatorname{supp}\rho_\alpha$; on $W$ all but finitely many summands vanish identically, so $\nabla s = \sum_\alpha \rho_\alpha \nabla^\alpha(s|_{U_\alpha})$ is a finite sum of smooth sections on $W$ and therefore smooth on $W$. As smoothness is local, $\nabla s \in \Omega^1(M; E)$.
> >
> > **$\mathbb{R}$-linearity.** For $s, s' \in \Gamma(E)$ and $\lambda, \mu \in \mathbb{R}$, restriction $s \mapsto s|_{U_\alpha}$ is $\mathbb{R}$-linear, each $\nabla^\alpha$ is $\mathbb{R}$-linear (it is a connection), and multiplication by the fixed function $\rho_\alpha$ is $\mathbb{R}$-linear, so termwise
> > $$\nabla(\lambda s + \mu s') = \sum_\alpha \rho_\alpha\, \nabla^\alpha\big((\lambda s + \mu s')|_{U_\alpha}\big) = \sum_\alpha \rho_\alpha\big(\lambda\, \nabla^\alpha(s|_{U_\alpha}) + \mu\, \nabla^\alpha(s'|_{U_\alpha})\big) = \lambda\, \nabla s + \mu\, \nabla s' \qquad (\text{each } \nabla^\alpha \ \mathbb{R}\text{-linear; the sum converges locally finitely}).$$
> >
> > **Leibniz rule.** Let $f \in C^\infty(M)$ and $s \in \Gamma(E)$. Restriction is a ring homomorphism, $(fs)|_{U_\alpha} = (f|_{U_\alpha})(s|_{U_\alpha})$, and each $\nabla^\alpha$ obeys the Leibniz rule on $U_\alpha$, so
> > $$\rho_\alpha\, \nabla^\alpha\big((fs)|_{U_\alpha}\big) = \rho_\alpha\Big(d(f|_{U_\alpha}) \otimes (s|_{U_\alpha}) + (f|_{U_\alpha})\, \nabla^\alpha(s|_{U_\alpha})\Big) = \rho_\alpha\, df \otimes s + f\,\rho_\alpha\, \nabla^\alpha(s|_{U_\alpha}) \qquad (\text{Leibniz for } \nabla^\alpha;\ d(f|_{U_\alpha}) = (df)|_{U_\alpha}),$$
> > where each term is understood extended by zero as in Step 0. Summing over $\alpha$ (a locally finite sum, so the interchange with the two-term split is legitimate at each point),
> > $$\nabla(fs) = \sum_\alpha \rho_\alpha\, df \otimes s + \sum_\alpha f\, \rho_\alpha\, \nabla^\alpha(s|_{U_\alpha}) = \Big(\sum_\alpha \rho_\alpha\Big)\, df \otimes s + f \sum_\alpha \rho_\alpha\, \nabla^\alpha(s|_{U_\alpha}) = df \otimes s + f\, \nabla s \qquad (\text{using } \textstyle\sum_\alpha \rho_\alpha \equiv 1).$$
> > The decisive step is the last equality: the inhomogeneous term $df \otimes s$ survives with coefficient $\sum_\alpha \rho_\alpha = 1$. Had the weights summed to any other value, this term would be mis-scaled and $\nabla$ would fail the Leibniz rule.
> >
> > **Conclusion.** $\nabla$ is a well-defined, $\mathbb{R}$-linear, Leibniz-obeying map $\Gamma(E) \to \Omega^1(M; E)$, hence a connection on $E$. $\blacksquare$

> [!note]- Lemma 3: Adding a bundle-valued 1-form to a connection yields a connection
> **Statement:** Let $\nabla \in \mathcal{A}(E)$ and $a \in \Omega^1(M; \operatorname{End} E)$. Then $\nabla + a$, defined by $(\nabla + a)s := \nabla s + a \cdot s$ with $(a \cdot s)(X) = a(X)\,s$, is a connection on $E$.
>
> **Hint:** The only thing to check beyond $\mathbb{R}$-linearity is that $a \cdot (fs) = f\,(a \cdot s)$, because $a$ acts fibrewise-linearly on the section slot; so the added term contributes nothing to the Leibniz inhomogeneity.
>
> **Why needed:** It is part (c) of the theorem and provides the action of the model vector space $\Omega^1(M; \operatorname{End} E)$ on $\mathcal{A}(E)$.
>
> > [!note]- Full proof
> > **Goal.** Show $\nabla + a$ is $\mathbb{R}$-linear and satisfies $(\nabla + a)(fs) = df \otimes s + f\,(\nabla + a)s$.
> >
> > **Step 0 — the action is $C^\infty(M)$-linear in the section.** For $f \in C^\infty(M)$, $s \in \Gamma(E)$, and a tangent vector $X$ at $m \in M$, the value $a(X) \in \operatorname{End}(E_m)$ is a *linear* map of the fibre, so
> > $$\big(a \cdot (fs)\big)(X) = a(X)\big(f(m)\, s(m)\big) = f(m)\, a(X)\big(s(m)\big) = f(m)\,(a \cdot s)(X) \qquad (\text{fibrewise linearity of } a(X)).$$
> > As $X$ was arbitrary, $a \cdot (fs) = f\,(a \cdot s)$; in particular $a \cdot (\lambda s + \mu s') = \lambda\,(a \cdot s) + \mu\,(a \cdot s')$ for scalars, so $s \mapsto a \cdot s$ is $\mathbb{R}$-linear.
> >
> > **$\mathbb{R}$-linearity.** Both $\nabla$ (a connection) and $s \mapsto a \cdot s$ (Step 0) are $\mathbb{R}$-linear, so their sum $\nabla + a$ is $\mathbb{R}$-linear.
> >
> > **Leibniz rule.** For $f \in C^\infty(M)$ and $s \in \Gamma(E)$,
> > $$(\nabla + a)(fs) = \nabla(fs) + a \cdot (fs) = \big(df \otimes s + f\,\nabla s\big) + f\,(a \cdot s) \qquad (\text{Leibniz for } \nabla;\ a\cdot(fs) = f\,(a\cdot s) \text{ by Step 0})$$
> > $$= df \otimes s + f\big(\nabla s + a \cdot s\big) = df \otimes s + f\,(\nabla + a)s \qquad (\text{collecting the factor } f).$$
> > The added term $a \cdot s$ enters only through $f\,(a \cdot s)$; it produces no new inhomogeneous term, which is exactly why $\nabla + a$ remains a connection.
> >
> > **Conclusion.** $\nabla + a$ is a connection on $E$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $E \to M$ be a smooth real vector bundle of rank $k$ over a smooth manifold, and let $\mathcal{A}(E)$ be its set of connections and $V := \Omega^1(M; \operatorname{End} E)$ the candidate model space.
>
> **Step 0 — the action map is defined.** By Lemma 3, for every $\nabla \in \mathcal{A}(E)$ and $a \in V$ the map $\nabla + a := \big(s \mapsto \nabla s + a \cdot s\big)$ lies in $\mathcal{A}(E)$. Hence $(a, \nabla) \mapsto \nabla + a$ is a genuine map $V \times \mathcal{A}(E) \to \mathcal{A}(E)$; this is part **(c)**. We now show it is a free transitive action and that $\mathcal{A}(E)$ is non-empty.
>
> **Part (a) — $\mathcal{A}(E) \neq \varnothing$.**
> By local triviality of $E$ (part of the [[Def - Vector Bundle|definition of a vector bundle]]), each point of $M$ has a trivialising neighbourhood; choose an open cover $\{U_\alpha\}_{\alpha \in I}$ of $M$ by such sets, with [[Def - Local Trivialization|trivialisations]] $\psi_{U_\alpha} : E|_{U_\alpha} \xrightarrow{\sim} U_\alpha \times \mathbb{R}^k$. **Build local connections:** by **Lemma 1**, each $\nabla^\alpha := \nabla^{U_\alpha}$, $\nabla^\alpha s = \psi_{U_\alpha}^{-1}\, d(\psi_{U_\alpha} s)$, is a connection on $E|_{U_\alpha}$. **Choose a partition of unity:** because $M$ is a smooth manifold — Hausdorff and second countable, hence paracompact — the [[Thm - Existence of Smooth Partitions of Unity|partition-of-unity theorem]] (*for any open cover $\{U_\alpha\}$ of a smooth manifold there is a smooth partition of unity $\{\rho_\alpha\}$ subordinate to it: $0 \le \rho_\alpha \le 1$, $\operatorname{supp}\rho_\alpha \subseteq U_\alpha$, the family $\{\operatorname{supp}\rho_\alpha\}$ locally finite, and $\sum_\alpha \rho_\alpha \equiv 1$*) supplies such a $\{\rho_\alpha\}_{\alpha \in I}$ indexed by the same $I$. **Glue:** by **Lemma 2** applied to $\{\nabla^\alpha\}$ and $\{\rho_\alpha\}$, the map
> $$\nabla := \sum_{\alpha \in I} \rho_\alpha\, \nabla^\alpha(\,\cdot\,|_{U_\alpha}) : \Gamma(E) \to \Omega^1(M; E)$$
> is a connection on $E$. Hence $\mathcal{A}(E) \neq \varnothing$.
>
> **Part (b) — the difference of two connections is a bundle-valued $1$-form.**
> Let $\nabla, \hat\nabla \in \mathcal{A}(E)$ and set $A := \nabla - \hat\nabla : \Gamma(E) \to \Omega^1(M; E)$, $A s = \nabla s - \hat\nabla s$. **$A$ is $\mathbb{R}$-linear** as the difference of two $\mathbb{R}$-linear maps. **$A$ is $C^\infty(M)$-linear:** for $f \in C^\infty(M)$ and $s \in \Gamma(E)$, subtract the two Leibniz rules,
> $$A(fs) = \nabla(fs) - \hat\nabla(fs) = \big(df \otimes s + f\,\nabla s\big) - \big(df \otimes s + f\,\hat\nabla s\big) = f\big(\nabla s - \hat\nabla s\big) = f\, A s \qquad (\text{the } df \otimes s \text{ terms cancel}).$$
> Thus $A : \Gamma(E) \to \Omega^1(M; E)$ is an $\mathbb{R}$-linear, $C^\infty(M)$-linear map. **Invoke tensoriality:** by [[Thm - Tensoriality Lemma for C-Infinity-Linear Maps|the tensoriality lemma]] — *an $\mathbb{R}$-linear map $A : \Gamma(E) \to \Omega^p(M; F)$ that is $C^\infty(M)$-linear, $A(fs) = f\,A(s)$, is given by a unique bundle-valued form $a \in \Omega^p(M; \operatorname{Hom}(E, F))$ via $A(s) = a \cdot s$* — applied with $p = 1$ and $F = E$ (so $\operatorname{Hom}(E, E) = \operatorname{End} E$), there is a unique $a \in \Omega^1(M; \operatorname{End} E) = V$ with
> $$(\nabla - \hat\nabla)s = a \cdot s \qquad \text{for all } s \in \Gamma(E).$$
> This proves **(b)**, and exhibits $a = \nabla - \hat\nabla \in V$.
>
> **Step 1 — the action is transitive.** Given $\nabla, \hat\nabla \in \mathcal{A}(E)$, part (b) produces $a \in V$ with $\nabla - \hat\nabla = a \cdot (\,\cdot\,)$, i.e. $\nabla = \hat\nabla + a$. So any connection is reached from any other by adding an element of $V$: the action is transitive.
>
> **Step 2 — the action is free (uniqueness of the difference).** Suppose $\nabla + a = \nabla + a'$ for some $\nabla \in \mathcal{A}(E)$ and $a, a' \in V$. Then $a \cdot s = a' \cdot s$ for every $s \in \Gamma(E)$, so $(a - a') \cdot s = 0$ for all $s$. We show a bundle-valued $1$-form annihilating every section is zero. Fix $m \in M$ and $v \in E_m$; since [[Thm - Local Frames Span Sections|local frames span sections]], there is $s \in \Gamma(E)$ with $s(m) = v$. For any tangent vector $X$ at $m$, $\big((a - a')(X)\big) v = \big((a-a')\cdot s\big)(X)\big|_m = 0$; as $v \in E_m$ and $X$ were arbitrary, the endomorphism-valued form $a - a'$ vanishes at $m$, and as $m$ was arbitrary, $a = a'$. Equivalently, the uniqueness clause of the tensoriality lemma already gives this. Hence for each ordered pair $(\nabla, \hat\nabla)$ the $a$ with $\hat\nabla = \nabla + a$ is unique, so the action is free.
>
> **Step 3 — the action axioms.** For $\nabla \in \mathcal{A}(E)$ and $a, b \in V$ and any $s \in \Gamma(E)$,
> $$(\nabla + 0)s = \nabla s + 0 \cdot s = \nabla s, \qquad \big((\nabla + a) + b\big)s = (\nabla s + a\cdot s) + b \cdot s = \nabla s + (a + b)\cdot s = \big(\nabla + (a + b)\big)s \qquad (\text{additivity of } a \mapsto a\cdot s \text{ in the form slot}),$$
> so $\nabla + 0 = \nabla$ and $(\nabla + a) + b = \nabla + (a + b)$: the map $V \times \mathcal{A}(E) \to \mathcal{A}(E)$ is an action of the additive group $(V, +)$.
>
> **Conclusion.** By Part (a) the set $\mathcal{A}(E)$ is non-empty; by Step 3 the map $(a, \nabla) \mapsto \nabla + a$ is an action of $V = \Omega^1(M; \operatorname{End} E)$; by Steps 1 and 2 it is transitive and free. Therefore $\mathcal{A}(E)$ is an affine space modelled on $\Omega^1(M; \operatorname{End} E)$, with $\hat\nabla - \nabla$ the unique bundle-valued $1$-form furnished by part (b). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The configuration space of a gauge theory (mathematical physics).** In Yang–Mills theory the field is a "gauge potential" $A$, and physicists routinely add a $1$-form to it, take differences $A_1 - A_0$ as physical objects, and integrate functionals along paths $A_t = (1-t)A_0 + tA_1$. The affine-space theorem is what licenses every one of these operations: the potentials are the connections on a bundle, their differences are $\operatorname{ad}$-bundle-valued $1$-forms, and the straight-line homotopy stays inside the configuration space because $\mathcal{A}(E)$ is convex. The application is non-obvious because the physics literature never mentions bundles or the Leibniz rule; recognising that "the space of potentials is affine, not linear" is what explains why there is no canonical zero potential and why only *differences* of potentials are gauge-covariant.

**Splittings of a short exact sequence of vector bundles (homological algebra in geometry).** Given a short exact sequence $0 \to E' \to E \to E'' \to 0$ of vector bundles, the set of smooth splittings (right inverses of $E \to E''$) is either empty or an affine space modelled on $\operatorname{Hom}(E'', E')$-valued objects — by exactly the mechanism of this page: the splitting condition is an inhomogeneous linear condition, its homogeneous version is a $\operatorname{Hom}$-bundle, local splittings exist by local triviality, and a partition of unity averages them. The theorem here is the prototype; recognising the shared "inhomogeneous-linear-condition" pattern is the transferable step, and it is non-obvious because splittings and connections look unrelated until one writes both conditions as $L x = b$.

**Time-dependent covariant derivatives along a curve (ordinary differential equations).** Pulling a bundle back along a curve $\gamma : [0,1] \to M$ produces $\gamma^* E \to [0,1]$, to which the theorem applies, giving a non-empty affine space of connections; a choice of connection turns "parallel transport" into a linear ODE $\dot\sigma + A(t)\sigma = 0$. The exercise is to see that the affine ambiguity in the connection is exactly the freedom to conjugate the transport by a time-dependent gauge, and that this is why holonomy — the transport around a loop up to conjugacy — is the invariant content. It is non-obvious because the base is now one-dimensional, where every bundle is trivial, so the whole subtlety migrates into the choice of connection.

---

# Bridges

- **[[Def - Gauge Group of a Vector Bundle|The gauge group and its action]].** The affine structure is the setting in which the gauge group $\mathcal{G}(E)$ acts. Writing any connection as $\nabla_0 + a$ turns the nonlinear-looking action $\nabla \mapsto g^{-1}\nabla(g\,\cdot\,)$ into an affine motion of $a$, so gauge orbits are affine subsets and the quotient $\mathcal{A}(E)/\mathcal{G}(E)$ — the object every moduli problem studies — is a quotient of an affine space; §2.4 develops this.

- **[[Thm - Curvature of a Shifted Connection|The curvature of a shifted connection]].** Because $\mathcal{A}(E)$ is affine, one expands curvature along the model directions: $F_{\nabla + a} = F_\nabla + d^\nabla a + a \wedge a$. The linear term $d^\nabla a$ is the derivative of the curvature map at $\nabla$, defined on the fixed vector space $\Omega^1(M; \operatorname{End} E)$; this is the construction that makes the deformation theory of connections a problem in linear elliptic analysis.

- **[[Ex - Convex Combinations of Connections are Connections|Convexity in isolation]].** The two-term, constant-weight case of Lemma 2 — that $t\nabla + (1-t)\hat\nabla$ is a connection for $t \in [0,1]$ — is worth isolating: it is the fact that $\mathcal{A}(E)$ is convex, hence contractible, hence that any characteristic form computed from a connection has a connection-independent cohomology class. The Chern–Weil theory of chapter VI runs on this convexity.

- **[[Thm - Existence of Connections on Principal Bundles|The principal-bundle version]].** The same statement holds for a principal $G$-bundle $P$: $\mathcal{A}(P)$ is an affine space modelled on $\Omega^1(M; \operatorname{ad} P)$. Its proof mirrors this one — local connection forms from local sections, glued by a partition of unity — and the vector-bundle case is recovered from it through associated bundles. The model gluing argument for both is the one used to build [[Thm - Existence of Riemannian Metrics via Partitions of Unity|Riemannian metrics]], where the object glued is a positive-definite form rather than a connection but the affine/convex mechanism is identical.

---

# Unlocked by This

> [!tip] The Space of Gauge Potentials as an Affine Banach Space *(from Global Analysis)*
> Completing $\Omega^1(M; \operatorname{End} E)$ in a Sobolev norm $W^{k,p}$ turns $\mathcal{A}(E)$ into an affine Banach space $\mathcal{A}^{k,p} = \nabla_0 + W^{k,p}(T^*M \otimes \operatorname{End} E)$, whose structure is independent of the base-point $\nabla_0$ precisely because the underlying set was affine. This is the arena for the Fredholm and transversality theory of moduli spaces. See **Def - Sobolev Completion of the Space of Connections**.

> [!tip] Contractibility and Characteristic Classes *(from Algebraic Topology)*
> Because an affine space is convex, $\mathcal{A}(E)$ is contractible, so any construction that assigns a cohomology class to a connection and varies continuously must give a class independent of the connection — the topological invariant of the bundle. This is the structural reason Chern–Weil forms represent characteristic classes. See [[Def - Curvature of a Vector-Bundle Connection]].
