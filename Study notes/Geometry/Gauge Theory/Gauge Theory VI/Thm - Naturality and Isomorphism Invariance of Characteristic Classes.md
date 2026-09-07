---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Chern-Weil Theorem"
  - "Thm - Pull-Back of Connections and Curvature"
  - "Thm - Gauge Transformations Act on Connections and Curvature"
  - "Def - Ad-Invariant Polynomial"
  - "Def - Chern-Weil Form of an Invariant Polynomial"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a Lie group with Lie algebra $\mathfrak{g} = T_eG$ and [[Def - Adjoint Representation|adjoint representation]] $\operatorname{Ad} : G \to GL(\mathfrak{g})$; for a matrix group $\operatorname{Ad}_g X = gXg^{-1}$. We fix a ground field $\mathbb{K} \in \{\mathbb{R},\mathbb{C}\}$; the argument is identical for both, and we take $\mathbb{K} = \mathbb{C}$ when a choice is needed.

An **[[Def - Ad-Invariant Polynomial|$\operatorname{Ad}$-invariant polynomial]] of degree $d$** is a homogeneous degree-$d$ polynomial map $p : \mathfrak{g} \to \mathbb{K}$ with $p(\operatorname{Ad}_g\xi) = p(\xi)$ for all $g \in G$ and $\xi \in \mathfrak{g}$; the graded ring of all such is $I(G) = \bigoplus_{d\ge 0} I_d(G)$ under pointwise product, and $\tilde{p} : \mathfrak{g}^{\times d} \to \mathbb{K}$ denotes the polarisation of $p \in I_d(G)$, the unique symmetric $\operatorname{Ad}$-invariant $d$-linear form with $\tilde{p}(\xi,\dots,\xi) = p(\xi)$.

$P \xrightarrow{\ \pi\ } M$ and $P' \xrightarrow{\ \pi'\ } M$ are principal $G$-bundles over a smooth manifold $M$; the right action is written $R_g(p) = p\cdot g$. A [[Def - Connection on a Principal Bundle|connection]] on $P$ is a form $\omega \in \Omega^1(P;\mathfrak{g})$ with $\omega(\xi_P) = \xi$ and $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega$, where $\xi_P(p) = \tfrac{d}{dt}\big|_0\, p\cdot\exp(t\xi)$ is the [[Def - Fundamental Vector Field of a Group Action|fundamental vector field]] of $\xi \in \mathfrak{g}$; the set of connections is $\mathcal{A}(P)$. The [[Def - Curvature of a Principal Connection|curvature]] of $\omega$ is $\Omega = d\omega + \tfrac12[\omega\wedge\omega] \in \Omega^2(P;\mathfrak{g})$, horizontal and $\operatorname{Ad}$-equivariant ($R_g^*\Omega = \operatorname{Ad}_{g^{-1}}\Omega$).

For $p \in I_d(G)$ and $\omega \in \mathcal{A}(P)$, the **[[Def - Chern-Weil Form of an Invariant Polynomial|Chern–Weil form on the total space]]** is $p(\Omega) := \tilde{p}(\Omega,\dots,\Omega) \in \Omega^{2d}(P;\mathbb{K})$ ($d$ arguments); in a basis $Y_1,\dots,Y_N$ of $\mathfrak{g}$, writing $\Omega = \sum_a \Omega^a Y_a$ with ordinary $2$-forms $\Omega^a$,
$$p(\Omega) \;=\; \sum_{a_1,\dots,a_d=1}^N \Omega^{a_1}\wedge\cdots\wedge\Omega^{a_d}\ \tilde{p}(Y_{a_1},\dots,Y_{a_d}).$$
It is **basic** (horizontal and $G$-invariant), so it descends to a unique **Chern–Weil form** $p(F_\omega) \in \Omega^{2d}(M;\mathbb{K})$ with $\pi^*p(F_\omega) = p(\Omega)$. Writing this out through a local section $s_\alpha : U_\alpha \to P$ (so $\pi\circ s_\alpha = \operatorname{id}_{U_\alpha}$) with local curvature $\Omega_\alpha := s_\alpha^*\Omega \in \Omega^2(U_\alpha;\mathfrak{g})$, we have
$$p(F_\omega)\big|_{U_\alpha} \;=\; s_\alpha^*\,p(\Omega) \;=\; \tilde{p}(\Omega_\alpha,\dots,\Omega_\alpha) \;=:\; p(\Omega_\alpha),$$
because $s_\alpha^*\pi^* = (\pi\circ s_\alpha)^* = \operatorname{id}$ and pullback commutes with the wedge-and-constants formula above.

The **[[Thm - Chern-Weil Theorem|Chern–Weil theorem]]** proves that $p(F_\omega)$ is closed and that its de Rham class
$$c_p(P) \;:=\; [\,p(F_\omega)\,] \;\in\; H^{2d}_{dR}(M;\mathbb{K})$$
does not depend on the connection $\omega$; we call $c_p(P)$ the **characteristic class** of $P$ attached to $p$. Here $H^\bullet_{dR}(M) = H^\bullet_{dR}(M;\mathbb{K})$ is [[Def - de Rham Cohomology|de Rham cohomology]], with the induced pullback $f^* : H^\bullet_{dR}(M) \to H^\bullet_{dR}(N)$ for a smooth $f : N \to M$ (well defined because pullback of forms commutes with $d$, so it carries closed forms to closed forms and exact to exact).

For a smooth map $f : N \to M$, $f^*P \to N$ is the [[Thm - The Pull-Back of a Fibre Bundle is a Fibre Bundle|pull-back bundle]] $f^*P = \{(n,p) \in N\times P : f(n) = \pi(p)\}$, with canonical $G$-equivariant map $\hat{f} : f^*P \to P$, $\hat{f}(n,p) = p$, covering $f$ (that is, $\pi\circ\hat{f} = f\circ\pi'$, where $\pi' : f^*P \to N$ is projection to the first factor). An **isomorphism of principal $G$-bundles** $\phi : P \to P'$ over $M$ is a $G$-equivariant diffeomorphism ($\phi(p\cdot g) = \phi(p)\cdot g$) with $\pi'\circ\phi = \pi$ (it covers $\operatorname{id}_M$); we write $P \cong P'$. The group of $G$-equivariant diffeomorphisms $\phi : P \to P$ is $\operatorname{Aut}(P)$, and the **[[Def - Gauge Transformation|gauge group]]** is its subgroup $\mathcal{G}(P) = \{\phi\in\operatorname{Aut}(P) : \pi\circ\phi = \pi\}$ of those covering the identity.

> [!warning] Convention: standing sign and normalisation choices
> Right actions on principal bundles, the structure equation $\Omega = d\omega + \tfrac12[\omega\wedge\omega]$, and $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega$ are the series conventions. The statements and proofs on this page hold verbatim for **any** $\operatorname{Ad}$-invariant polynomial $p$ and involve no numerical normalisation, so they apply unchanged to the Chern normalisation $c(E) = \det(1 + \tfrac{i}{2\pi}F)$, to the Pontryagin and Euler normalisations, and to the raw forms $p = \operatorname{tr}(\xi^d)$ alike; the coefficient conventions enter only the *named* classes, on their own pages.

---

# Statement

> **Theorem (naturality and isomorphism invariance of characteristic classes).** Let $G$ be a Lie group and $p \in I_d(G)$ an $\operatorname{Ad}$-invariant polynomial of degree $d$. Let $P \to M$ be a principal $G$-bundle. Then:
>
> **(a) Naturality.** For every smooth map $f : N \to M$ of manifolds,
> $$c_p(f^*P) \;=\; f^*c_p(P) \qquad\text{in } H^{2d}_{dR}(N).$$
>
> **(b) Isomorphism invariance.** If $\phi : P \to P'$ is an isomorphism of principal $G$-bundles over $M$, then
> $$c_p(P) \;=\; c_p(P') \qquad\text{in } H^{2d}_{dR}(M).$$
>
> **(c) Invariant of the isomorphism class.** Consequently $c_p(P)$ depends only on the isomorphism class of $P$. In particular, for every gauge transformation $\phi \in \mathcal{G}(P)$ and every connection $\omega \in \mathcal{A}(P)$ the Chern–Weil form itself is gauge invariant,
> $$p\big(F_{\phi^*\omega}\big) \;=\; p(F_\omega) \qquad\text{in } \Omega^{2d}(M;\mathbb{K}),$$
> so $c_p$ descends to a function on $\mathcal{A}(P)/\mathcal{G}(P)$; and for a general automorphism $\phi \in \operatorname{Aut}(P)$ covering the base diffeomorphism $\bar\phi : M \to M$ one has $\bar\phi^*c_p(P) = c_p(P)$.
>
> **(d) Homotopy invariance.** If $f_0, f_1 : N \to M$ are smoothly homotopic, then
> $$c_p(f_0^*P) \;=\; c_p(f_1^*P) \qquad\text{in } H^{2d}_{dR}(N).$$

The four parts are the four senses in which the Chern–Weil class deserves the name **characteristic class**: it transforms correctly under maps, it cannot tell isomorphic bundles apart, it is blind to the gauge freedom, and it factors through the homotopy category on the base.

---

# Motivation

The [[Thm - Chern-Weil Theorem|Chern–Weil theorem]] produces, from a principal $G$-bundle $P \to M$ with *any* connection $\omega$, a de Rham class $c_p(P) = [p(F_\omega)] \in H^{2d}_{dR}(M)$ that is independent of $\omega$. That independence is the first and hardest step, but it is not yet enough to make $c_p(P)$ a topological invariant of the bundle. The class is built from a differential-geometric datum — a curvature form — and a priori it could still depend on incidental features: the way $P$ is presented, the identification of $P$ with an isomorphic bundle, the choice of a map used to construct $P$ by pullback. A number that changed when we merely renamed the fibres would be useless as an invariant.

This page removes exactly those residual dependencies, and it is worth naming the question each part answers.

Part (a) asks how $c_p$ interacts with the single universal operation on bundles, pullback along a map $f : N \to M$. Every construction of new bundles from old — restriction to a submanifold, the bundle over a product, the bundle classified by a map into a Grassmannian or projective space — is a pullback, so naturality is what lets a characteristic class be *computed* by transporting a known model to the situation at hand. Concretely, the way one finds $c_p$ of a complicated bundle is to exhibit it as $f^*(\text{a standard bundle})$ and read off $c_p = f^*(\text{a standard class})$; without naturality this move would be illegitimate.

Part (b) asks whether $c_p$ is an invariant of the bundle or only of a chosen presentation of it. A principal bundle carries no canonical connection and no canonical trivialisation; two constructions that produce isomorphic bundles must be shown to produce the *same* class, or the class is an artefact. Isomorphism invariance is the precise statement that $c_p$ is a function on the set of isomorphism classes — the object the classification of bundles is actually about.

Part (c) is the gauge-theoretic reading of (b) and the reason characteristic classes matter for physics. The gauge group $\mathcal{G}(P)$ acts on the infinite-dimensional space of connections $\mathcal{A}(P)$, and the physically meaningful objects live on the quotient $\mathcal{A}(P)/\mathcal{G}(P)$. A functional of the connection can descend to that quotient only if it is gauge invariant. We prove more than the invariance of the *class*: the Chern–Weil *form* $p(F_\omega)$ is already unchanged by a gauge transformation, pointwise on $M$. This is what makes the Chern–Weil forms the natural integrands for gauge-invariant action functionals and topological charges, and it is the fact behind the well-definedness of the second Chern number and the Chern–Simons functional later in this chapter.

Part (d) is the bridge to the classifying-space picture. Once (a) is available, homotopy invariance says $c_p(f^*P)$ depends only on the homotopy class of $f$. In the axiomatic language of a [[Def - Characteristic Class|characteristic class]], where a bundle over $M$ is classified by a homotopy class of maps $M \to BG$ and a characteristic class is the pullback of a fixed cohomology class of $BG$, part (d) is precisely the compatibility that makes the Chern–Weil class agree with the topological one. It is also what shows that the class cannot separate a bundle from its pullback along a homotopy equivalence — in particular, every bundle over a contractible base has vanishing characteristic classes, the first hint of the next theorem, [[Thm - Trivial Bundles Have Vanishing Characteristic Classes|that trivial bundles have vanishing characteristic classes]].

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypotheses are mild — a smooth map, or an isomorphism, or a homotopy — so the skill is to recognise when a problem is secretly one of these.

The first disguised source is **a bundle presented as living over a subspace or a product**. A restriction $P|_A$ of a bundle to a submanifold $A \subseteq M$ is the pullback $\iota^*P$ along the inclusion $\iota : A \hookrightarrow M$; a bundle over $M\times[0,1]$ restricted to a slice $M\times\{t\}$ is a pullback along $m\mapsto(m,t)$. The bridge $B \Rightarrow A$ is "restriction is pullback", and it is non-obvious only because restriction is rarely written with a map. *Example problem:* show that the first Chern class of a line bundle over $\mathbb{CP}^n$, restricted to a projective line $\mathbb{CP}^1 \subset \mathbb{CP}^n$, equals the pullback of $c_1$ along the inclusion, so that the integral over $\mathbb{CP}^1$ computes a single integer independent of which line is chosen.

The second disguised source is **a bundle built by a clutching or gluing construction, or classified by a map**. A bundle over a base $X$ obtained from a map $g : X \to Y$ (a clutching function into $G$, a Gauss map into a Grassmannian, a classifying map into projective space) is a pullback of a universal model along $g$. The bridge is "classified by $g$" $\Rightarrow$ "equal to $g^*(\text{model})$", and naturality then reduces the class to the model's class transported by $g^*$. *Example problem:* compute the second Chern number of the clutching bundle of $q\mapsto q^k$ over $S^4$ by recognising it as a pullback and reducing to the degree of the clutching map.

The third disguised source is **two descriptions of one bundle that must be reconciled**. When the same bundle arises two ways — as an associated bundle and as a frame bundle, as a quotient and as a subbundle, with two different Hermitian or Euclidean structures — an isomorphism between the descriptions is exactly the input for part (b), and it forces the two computed classes to agree. The bridge is "any isomorphism suffices; one need not be canonical". *Example problem:* show that the Chern classes of a complex vector bundle do not depend on the choice of Hermitian metric, by exhibiting an isomorphism of unitary frame bundles for two metrics and applying isomorphism invariance.

**Targets (Output Amplification).** The bare conclusions combine with three further ingredients into the working tools of the subject.

Combine part (a) with **a computation on a model space**. If $c_p$ is known on a standard bundle over a standard base — say $c_1(\mathcal{O}(-1)) = -[\omega_1]$ on $\mathbb{CP}^1$ — then naturality delivers $c_p$ on *every* bundle pulled back from that model, with no further curvature computation: $c_p(f^*\mathcal{O}(-1)) = f^*c_1(\mathcal{O}(-1))$. The payoff is that a single geometric integral, done once, computes an entire family of characteristic numbers.

Combine parts (b) and (d) with **the existence of a homotopy or an isomorphism obstruction, read backwards**. The contrapositive of invariance is a non-triviality test: if $c_p(P) \neq c_p(P')$ then $P \not\cong P'$, and if $c_p(P) \neq 0$ while every trivial bundle has $c_p = 0$, then $P$ is non-trivial. The extra ingredient is the vanishing theorem for trivial bundles; the payoff is that characteristic classes become obstructions to triviality, which is their principal use in four-manifold topology.

Combine part (c) with **an action functional on connections**. Gauge invariance of the Chern–Weil form means that any integral $\int_M \eta\wedge p(F_\omega)$, or $\int_M p(F_\omega)$ when $2d = \dim M$, descends to the moduli space $\mathcal{A}(P)/\mathcal{G}(P)$. The extra ingredient is a base of the right dimension (or a fixed background form $\eta$); the payoff is the topological term in the Yang–Mills energy identity and the second Chern number as a gauge-invariant instanton charge, both in chapter VII.

---

# Why Is It True

Strip away the cohomology and look at the Chern–Weil form itself. In a chart, $p(F_\omega)$ is a fixed universal polynomial expression in the entries of the **local curvature form** $\Omega_\alpha = s_\alpha^*\Omega$: a sum of wedge products of the scalar $2$-forms $\Omega_\alpha^a$, weighted by the constants $\tilde{p}(Y_{a_1},\dots,Y_{a_d})$. Everything on this page follows from a single observation about that expression and the two ways the local curvature can change.

> **The mechanism in one sentence: the Chern–Weil form is a natural, $\operatorname{Ad}$-invariant expression in the curvature, so pulling back the bundle pulls back the form, changing the fibre identification by an isomorphism leaves the local curvature untouched, and a gauge transformation only conjugates the curvature by an element of $G$ — which the $\operatorname{Ad}$-invariance of $p$ absorbs.**

Take naturality first. Pulling $P$ back along $f : N \to M$ pulls back the connection: the [[Thm - Pull-Back of Connections and Curvature|pull-back connection]] $\hat{f}^*\omega$ has curvature $\hat{f}^*\Omega$, and in a chart its local curvature is literally $f^*\Omega_\alpha$. Since $p(F_\omega)$ is built from $\Omega_\alpha$ by wedges and fixed constants, and pullback of forms commutes with the wedge product and passes through constants, the Chern–Weil form of the pulled-back connection is the pullback of the Chern–Weil form: $p(F_{\hat{f}^*\omega}) = f^*p(F_\omega)$. Taking classes, and using that the class does not care which connection computed it, gives $c_p(f^*P) = f^*c_p(P)$. Naturality of the *class* is naturality of the *form*, which is naturality of the curvature.

Isomorphism invariance is even more immediate. An isomorphism $\phi : P \to P'$ carries a connection $\omega$ on $P$ to a connection $\phi_*\omega$ on $P'$ and carries the local sections $s_\alpha$ of $P$ to local sections $\phi\circ s_\alpha$ of $P'$ over the *same* open cover of $M$. Computed through these matched sections, the local curvature of $\phi_*\omega$ is exactly the local curvature of $\omega$: $\phi$ moves the total spaces but not the base, and the local curvature lives on the base. Equal local curvatures give equal Chern–Weil forms, hence equal classes. An isomorphism of bundles is a relabelling of fibres, and the curvature two-form on the base does not see relabellings.

Gauge invariance is the same statement read once more, now for a self-isomorphism. A [[Thm - Gauge Transformations Act on Connections and Curvature|gauge transformation]] $\phi \in \mathcal{G}(P)$ changes the connection but transforms its curvature by conjugation: locally $F_{\phi^*\omega} = \operatorname{Ad}_{g^{-1}}F_\omega$, with no derivative term, because curvature is tensorial. The polynomial $p$ was chosen $\operatorname{Ad}$-invariant precisely so that it cannot see this conjugation: $p(\operatorname{Ad}_{g^{-1}}F) = p(F)$. So the Chern–Weil form is unchanged on the nose. This is why the *invariance* of $p$ under $\operatorname{Ad}$ is not a technical convenience but the whole point — it is the property that makes $p(F)$ gauge invariant.

Homotopy invariance needs nothing new. By naturality, $c_p(f_i^*P) = f_i^*c_p(P)$, and homotopic maps induce equal pullbacks on de Rham cohomology. So the two classes coincide the moment (a) is in hand.

---

# What Makes This Hard

The mathematics is short; the difficulty is entirely in bookkeeping that is easy to get backwards. First, the direction of every pullback must be tracked: for $f : N \to M$ the bundle map $\hat{f} : f^*P \to P$ goes *from* the pullback, and to move a connection *onto* $P'$ under $\phi : P \to P'$ one must pull back along $\phi^{-1}$, so the correct object is $\phi_*\omega = (\phi^{-1})^*\omega$, not $\phi^*\omega$. Bär's text prints two sign-of-the-arrow misprints here (see the note in the proof), and reproducing them makes the local sections and forms fail to typecheck. Second, one must resist proving isomorphism invariance by pushing forward *forms on the total space* and worrying about the descent; the clean route keeps everything downstairs, on the base, through matched local sections, where the curvatures are literally equal. Third, the leverage in the whole page is that $c_p(P)$ is connection-independent (the Chern–Weil theorem): this is what lets us compute the class of the transformed bundle with the *transformed* connection rather than an arbitrary one, and every part silently uses it at the last step.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove each invariance first at the level of the Chern–Weil *form*, by tracking the local curvature form through the relevant operation, then pass to cohomology using the connection-independence of $c_p(P)$ from the Chern–Weil theorem. Naturality and gauge invariance are the two substantive form-level computations; isomorphism invariance is a matched-section identity; homotopy invariance is a corollary of naturality.

**Subgoal decomposition:**

1. **Pull-back of the Chern–Weil form.** Show $p(F_{\hat{f}^*\omega}) = f^*p(F_\omega)$ as forms on $N$.
   - *Hint:* Use the pull-back-connection theorem: $\hat{f}^*\omega$ is a connection with curvature $\hat{f}^*\Omega$; either compute in a chart with $\Omega'_\alpha = f^*\Omega_\alpha$, or work on total spaces and cancel $\pi'^*$ using its injectivity.
   - *Why needed:* This is naturality of the class once you take $[\ \cdot\ ]$ and invoke connection-independence.

2. **Push-forward of a connection under an isomorphism.** For $\phi : P \to P'$, show $\phi_*\omega := (\phi^{-1})^*\omega$ is a connection on $P'$ with curvature $(\phi^{-1})^*\Omega$.
   - *Hint:* Check the two connection axioms using $G$-equivariance of $\phi$ (so $\phi$ commutes with $R_g$ and sends $\xi_P$ to $\xi_{P'}$); get the curvature from the structure equation and the fact that pullback commutes with $d$ and with the bracket-wedge.
   - *Why needed:* It supplies a connection on $P'$ whose local curvature you can compare with that of $\omega$.

3. **Matched local sections give equal local curvature.** With $s'_\alpha := \phi\circ s_\alpha$, show $(s'_\alpha)^*(\phi^{-1})^*\Omega = s_\alpha^*\Omega$, hence $p(F_{\phi_*\omega}) = p(F_\omega)$.
   - *Hint:* $(\phi\circ s_\alpha)^*(\phi^{-1})^* = s_\alpha^*(\phi^{-1}\circ\phi)^* = s_\alpha^*$; and $\pi'\circ s'_\alpha = \operatorname{id}$ because $\phi$ covers the identity.
   - *Why needed:* Equal forms give equal classes: this is isomorphism invariance.

4. **Gauge conjugation is invisible to $p$.** For $\phi \in \mathcal{G}(P)$ with local representation $g : U \to G$, use $F_{\phi^*\omega} = \operatorname{Ad}_{g^{-1}}F_\omega$ locally and $p(\operatorname{Ad}_{g^{-1}}\xi) = p(\xi)$ to get $p(F_{\phi^*\omega}) = p(F_\omega)$.
   - *Hint:* $\operatorname{Ad}$-invariance of $p$ passes to $\mathfrak{g}$-valued $2$-forms because it is a pointwise algebraic identity in the values.
   - *Why needed:* This is the pointwise gauge invariance of the form in part (c).

5. **Assemble the four parts.** Take classes in (1) and (3)–(4), invoking connection-independence to evaluate $c_p$ of the transformed bundle with the transformed connection; deduce (d) from (a) and homotopy invariance of de Rham cohomology.
   - *Hint:* For (d), $c_p(f_i^*P) = f_i^*c_p(P)$ and $f_0^* = f_1^*$ on $H^\bullet_{dR}$.
   - *Why needed:* It turns the form-level facts into the cohomological statements (a)–(d).

---

# Lemma Decomposition

> [!note]- Lemma 1: The projection pullback $\pi^*$ is injective on forms
> **Statement:** Let $\pi : P \to M$ be a principal $G$-bundle (or any surjective submersion admitting local sections). Then $\pi^* : \Omega^k(M;\mathbb{K}) \to \Omega^k(P;\mathbb{K})$ is injective: if $\pi^*\eta = 0$ then $\eta = 0$.
>
> **Hint:** Precompose with a local section.
>
> **Why needed:** It lets the total-space identity $\pi'^*\alpha = \pi'^*\beta$ be cancelled to $\alpha = \beta$ in the clean proof of naturality (Lemma 2), where the descended forms are compared through their pullbacks.
>
> > [!note]- Full proof
> > Let $\eta \in \Omega^k(M;\mathbb{K})$ with $\pi^*\eta = 0$. Fix $m \in M$. A principal bundle admits a local section near every point: choose a trivialising open set $U \ni m$ and a local section $s : U \to P$ with $\pi\circ s = \operatorname{id}_U$ (for instance $s(x) = \Phi^{-1}(x,e)$ for a local trivialisation $\Phi : \pi^{-1}(U) \to U\times G$ and the identity $e \in G$). Then
> > $$\eta\big|_U = (\pi\circ s)^*\eta = s^*(\pi^*\eta) = s^*(0) = 0 \qquad \text{(functoriality of pullback; } \pi^*\eta = 0\text{).}$$
> > So $\eta$ vanishes on a neighbourhood of each point, hence $\eta = 0$. Therefore $\pi^*$ is injective. $\blacksquare$

> [!note]- Lemma 2: The Chern–Weil form is natural under pullback of the connection
> **Statement:** Let $f : N \to M$ be smooth, $P \to M$ a principal $G$-bundle with connection $\omega$, and $\hat{f} : f^*P \to P$ the canonical equivariant map covering $f$. Let $\hat{f}^*\omega$ be the pull-back connection on $f^*P$. Then for every $p \in I_d(G)$,
> $$p\big(F_{\hat{f}^*\omega}\big) \;=\; f^*\,p(F_\omega) \qquad \text{in } \Omega^{2d}(N;\mathbb{K}).$$
>
> **Hint:** The pull-back connection has curvature $\hat{f}^*\Omega$; evaluate the total-space Chern–Weil form and cancel $\pi'^*$ with Lemma 1, or compute in a chart with $\Omega'_\alpha = f^*\Omega_\alpha$.
>
> **Why needed:** Passing to cohomology classes and invoking the connection-independence of $c_p$ turns this into part (a).
>
> > [!note]- Full proof
> > We use the [[Thm - Pull-Back of Connections and Curvature|pull-back-connection theorem]], restated here: *for $f : N\to M$ and the canonical equivariant map $\hat{f} : f^*P \to P$ covering $f$, the form $\hat{f}^*\omega \in \Omega^1(f^*P;\mathfrak{g})$ is a connection on $f^*P$, and its curvature is $\Omega' = \hat{f}^*\Omega$.* Write $\pi' : f^*P \to N$ for the projection, so that $\pi\circ\hat{f} = f\circ\pi'$.
> >
> > **Step 1 — the total-space forms pull back.** The Chern–Weil form on the total space is $p(\Omega) = \tilde{p}(\Omega,\dots,\Omega)$, a sum of wedge products of the scalar components of $\Omega$ weighted by the constants $\tilde{p}(Y_{a_1},\dots,Y_{a_d})$. Pullback of forms commutes with the wedge product and is $\mathbb{K}$-linear, so it commutes with this expression:
> > $$p(\Omega') \;=\; \tilde{p}\big(\hat{f}^*\Omega,\dots,\hat{f}^*\Omega\big) \;=\; \hat{f}^*\,\tilde{p}(\Omega,\dots,\Omega) \;=\; \hat{f}^*\,p(\Omega) \qquad \text{(pullback commutes with wedge and passes through constants; } \Omega' = \hat{f}^*\Omega\text{).}$$
> >
> > **Step 2 — rewrite both sides through the base forms.** By the definition of the descended Chern–Weil form, $p(\Omega) = \pi^*p(F_\omega)$ on $P$ and $p(\Omega') = \pi'^*p(F_{\hat{f}^*\omega})$ on $f^*P$. Substituting into Step 1,
> > $$\pi'^*\,p\big(F_{\hat{f}^*\omega}\big) \;=\; \hat{f}^*\,\pi^*\,p(F_\omega) \;=\; (\pi\circ\hat{f})^*\,p(F_\omega) \;=\; (f\circ\pi')^*\,p(F_\omega) \;=\; \pi'^*\,f^*\,p(F_\omega) \qquad \text{(functoriality of pullback; } \pi\circ\hat{f} = f\circ\pi'\text{).}$$
> >
> > **Step 3 — cancel $\pi'^*$.** Both sides are $\pi'^*$ of a form on $N$. By Lemma 1 applied to the bundle $\pi' : f^*P \to N$, the map $\pi'^*$ is injective, so
> > $$p\big(F_{\hat{f}^*\omega}\big) \;=\; f^*\,p(F_\omega).$$
> >
> > **Chart check (independent verification).** The same identity follows locally. Let $s_\alpha : U_\alpha \to P$ be local sections over an open cover of $M$; the pull-back-connection theorem also gives that, with $V_\alpha := f^{-1}(U_\alpha)$ and $s'_\alpha := \hat{f}^{-1}\circ s_\alpha\circ f : V_\alpha \to f^*P$, the local curvature forms satisfy $\Omega'_\alpha = (s'_\alpha)^*\Omega' = f^*\Omega_\alpha$. Then, on $V_\alpha$,
> > $$p\big(F_{\hat{f}^*\omega}\big)\big|_{V_\alpha} = \tilde{p}(\Omega'_\alpha,\dots,\Omega'_\alpha) = \tilde{p}(f^*\Omega_\alpha,\dots,f^*\Omega_\alpha) = f^*\,\tilde{p}(\Omega_\alpha,\dots,\Omega_\alpha) = f^*\big(p(F_\omega)\big|_{U_\alpha}\big) = \big(f^*p(F_\omega)\big)\big|_{V_\alpha},$$
> > each equality by, in turn, the local formula for the descended form, $\Omega'_\alpha = f^*\Omega_\alpha$, commutation of pullback with wedge and constants, the local formula again, and $f(V_\alpha)\subseteq U_\alpha$. Since the $V_\alpha$ cover $N$, the two forms agree globally, confirming Step 3. $\blacksquare$

> [!note]- Lemma 3: An isomorphism carries a connection to a connection with matched local curvature
> **Statement:** Let $\phi : P \to P'$ be an isomorphism of principal $G$-bundles over $M$ and $\omega$ a connection on $P$. Then $\phi_*\omega := (\phi^{-1})^*\omega \in \Omega^1(P';\mathfrak{g})$ is a connection on $P'$, its curvature is $\Omega' = (\phi^{-1})^*\Omega$, and for any local section $s_\alpha : U_\alpha \to P$ the section $s'_\alpha := \phi\circ s_\alpha : U_\alpha \to P'$ satisfies $(s'_\alpha)^*\Omega' = s_\alpha^*\Omega = \Omega_\alpha$. Consequently $p(F_{\phi_*\omega}) = p(F_\omega)$ for every $p \in I_d(G)$.
>
> **Hint:** Use $G$-equivariance of $\phi$ for the two connection axioms, the structure equation for the curvature, and $(\phi\circ s_\alpha)^*(\phi^{-1})^* = s_\alpha^*$ for the local curvature.
>
> **Why needed:** Equal Chern–Weil forms give equal classes, which is part (b).
>
> > [!note]- Full proof
> > Because $\phi : P \to P'$ is a $G$-equivariant diffeomorphism, $\phi^{-1} : P' \to P$ is one as well; in particular $\phi^{-1}\circ R_g = R_g\circ\phi^{-1}$ for all $g \in G$ (equivariance of $\phi^{-1}$), and $\phi^{-1}$ maps the fundamental field $\xi_{P'}$ to $\xi_P$, that is $d\phi^{-1}\circ\xi_{P'} = \xi_P\circ\phi^{-1}$ (differentiate $\phi^{-1}(p'\cdot\exp(t\xi)) = \phi^{-1}(p')\cdot\exp(t\xi)$ at $t = 0$).
> >
> > **Step 0 — $\phi_*\omega$ is a connection on $P'$.** We verify the two defining axioms of a connection for $\omega' := (\phi^{-1})^*\omega$.
> >
> > *Equivariance.* For $g \in G$,
> > $$R_g^*\omega' = R_g^*(\phi^{-1})^*\omega = (\phi^{-1}\circ R_g)^*\omega = (R_g\circ\phi^{-1})^*\omega = (\phi^{-1})^*R_g^*\omega = (\phi^{-1})^*\operatorname{Ad}_{g^{-1}}\omega = \operatorname{Ad}_{g^{-1}}(\phi^{-1})^*\omega = \operatorname{Ad}_{g^{-1}}\omega',$$
> > using in order: the definition of $\omega'$; functoriality of pullback; equivariance of $\phi^{-1}$ ($\phi^{-1}\circ R_g = R_g\circ\phi^{-1}$); functoriality again; the connection axiom $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega$ for $\omega$; and that $\operatorname{Ad}_{g^{-1}}$ acts pointwise on the $\mathfrak{g}$-values and so commutes with pullback of forms.
> >
> > *Fundamental fields.* Fix $\xi \in \mathfrak{g}$ and $p' \in P'$; write $p = \phi^{-1}(p')$. Then
> > $$\omega'_{p'}(\xi_{P'}(p')) = \big((\phi^{-1})^*\omega\big)_{p'}(\xi_{P'}(p')) = \omega_{p}\big(d\phi^{-1}(\xi_{P'}(p'))\big) = \omega_p(\xi_P(p)) = \xi,$$
> > using the definition of pullback of a $1$-form, then $d\phi^{-1}(\xi_{P'}(p')) = \xi_P(\phi^{-1}(p')) = \xi_P(p)$ (that $\phi^{-1}$ sends $\xi_{P'}$ to $\xi_P$), then the connection axiom $\omega(\xi_P) = \xi$ for $\omega$. Both axioms hold, so $\omega'$ is a connection on $P'$.
> >
> > **Step 1 — the curvature is $(\phi^{-1})^*\Omega$.** By the structure equation and the naturality of $d$ and of the bracket-wedge under pullback,
> > $$\Omega' = d\omega' + \tfrac12[\omega'\wedge\omega'] = d(\phi^{-1})^*\omega + \tfrac12\big[(\phi^{-1})^*\omega\wedge(\phi^{-1})^*\omega\big] = (\phi^{-1})^*\big(d\omega + \tfrac12[\omega\wedge\omega]\big) = (\phi^{-1})^*\Omega,$$
> > using that pullback commutes with the exterior derivative ($d\circ(\phi^{-1})^* = (\phi^{-1})^*\circ d$) and with the bracket-wedge ($[(\phi^{-1})^*\alpha\wedge(\phi^{-1})^*\beta] = (\phi^{-1})^*[\alpha\wedge\beta]$, since the bracket-wedge is built pointwise from the wedge of forms and the Lie bracket of values).
> >
> > **Step 2 — matched local sections give equal local curvature.** Because $\phi$ covers the identity, $\pi'\circ\phi = \pi$; hence $s'_\alpha := \phi\circ s_\alpha$ satisfies $\pi'\circ s'_\alpha = \pi'\circ\phi\circ s_\alpha = \pi\circ s_\alpha = \operatorname{id}_{U_\alpha}$, so $s'_\alpha$ is a local section of $P'$ over the same open set $U_\alpha$. Its local curvature form is
> > $$(s'_\alpha)^*\Omega' = (\phi\circ s_\alpha)^*(\phi^{-1})^*\Omega = s_\alpha^*\,\phi^*(\phi^{-1})^*\Omega = s_\alpha^*(\phi^{-1}\circ\phi)^*\Omega = s_\alpha^*\,\operatorname{id}^*\Omega = s_\alpha^*\Omega = \Omega_\alpha,$$
> > using the definition of $s'_\alpha$ and of $\Omega'$, functoriality of pullback, $\phi^{-1}\circ\phi = \operatorname{id}_P$, and the definition of $\Omega_\alpha$.
> >
> > **Step 3 — equal Chern–Weil forms.** The descended Chern–Weil form is computed chart by chart from the local curvature: $p(F_{\phi_*\omega})|_{U_\alpha} = \tilde{p}((s'_\alpha)^*\Omega',\dots) = \tilde{p}(\Omega_\alpha,\dots,\Omega_\alpha) = p(F_\omega)|_{U_\alpha}$ by Step 2. As the $U_\alpha$ cover $M$, we conclude $p(F_{\phi_*\omega}) = p(F_\omega)$ on $M$. $\blacksquare$
>
> > [!note]- Remark: two misprints in Bär's Remark 2.5.8, corrected here
> > Bär's source (Remark 2.5.8) writes the pushed connection as "$\omega' := \phi^*\omega$" and the sections as "$s'_\alpha := \phi^{-1}\circ s_\alpha$". Both are typographical slips of the direction of the arrow: for $\phi : P \to P'$ and $\omega \in \Omega^1(P;\mathfrak{g})$, the form $\phi^*\omega$ would live on $P$, not $P'$, and $\phi^{-1}\circ s_\alpha$ would require $s_\alpha$ to map into $P'$. The correct objects, used above, are $\omega' = \phi_*\omega = (\phi^{-1})^*\omega \in \Omega^1(P';\mathfrak{g})$ and $s'_\alpha = \phi\circ s_\alpha : U_\alpha \to P'$; with these, the computation $(s'_\alpha)^*\Omega' = \Omega_\alpha$ closes exactly as Bär intends.

> [!note]- Lemma 4: The Chern–Weil form is gauge invariant
> **Statement:** Let $\omega \in \mathcal{A}(P)$ and $\phi \in \mathcal{G}(P)$ a gauge transformation. Then for every $p \in I_d(G)$,
> $$p\big(F_{\phi^*\omega}\big) \;=\; p(F_\omega) \qquad \text{in } \Omega^{2d}(M;\mathbb{K}).$$
>
> **Hint:** A gauge transformation acts on curvature by $\operatorname{Ad}$-conjugation, with no derivative term, and $p$ is $\operatorname{Ad}$-invariant.
>
> **Why needed:** It is the pointwise gauge-invariance statement in part (c), and the form-level fact that lets $c_p$ descend to the moduli space.
>
> > [!note]- Full proof
> > We use the [[Thm - Gauge Transformations Act on Connections and Curvature|gauge-action theorem]], restated here in its local form: *for $\phi \in \mathcal{G}(P)$ and a local section $s : U \to P$, writing $g := \hat{g}\circ s : U \to G$ for the local representation of $\phi$ (where $\phi(p) = p\cdot\hat{g}(p)$), the local connection and curvature forms of the gauge-transformed connection $\phi^*\omega$ are*
> > $$A_{\phi^*\omega,\,s} = \operatorname{Ad}_{g^{-1}}A_{\omega,\,s} + g^*\theta, \qquad F_{\phi^*\omega,\,s} = \operatorname{Ad}_{g^{-1}}F_{\omega,\,s},$$
> > *with $\theta$ the [[Def - The Maurer-Cartan Form|Maurer–Cartan form]].* Only the curvature relation is needed: crucially it carries **no** derivative term, so a gauge transformation conjugates the local curvature by the $G$-valued function $g$.
> >
> > **Step 1 — $\operatorname{Ad}$-invariance passes to $\mathfrak{g}$-valued forms.** The polarisation $\tilde{p}$ is $\operatorname{Ad}$-invariant: $\tilde{p}(\operatorname{Ad}_h\xi_1,\dots,\operatorname{Ad}_h\xi_d) = \tilde{p}(\xi_1,\dots,\xi_d)$ for all $h \in G$ and $\xi_i \in \mathfrak{g}$ ([[Def - Ad-Invariant Polynomial|invariance of the polarisation]]). This is an algebraic identity in the values, so it holds after tensoring with ordinary forms: for $\mathfrak{g}$-valued forms $\Phi_1,\dots,\Phi_d$ and a fixed $h \in G$, writing $\Phi_i = \sum_a \Phi_i^a Y_a$,
> > $$\tilde{p}(\operatorname{Ad}_h\Phi_1,\dots,\operatorname{Ad}_h\Phi_d) = \sum_{a_1,\dots,a_d}\Phi_1^{a_1}\wedge\cdots\wedge\Phi_d^{a_d}\ \tilde{p}(\operatorname{Ad}_hY_{a_1},\dots,\operatorname{Ad}_hY_{a_d}) = \sum \Phi_1^{a_1}\wedge\cdots\wedge\Phi_d^{a_d}\ \tilde{p}(Y_{a_1},\dots,Y_{a_d}) = \tilde{p}(\Phi_1,\dots,\Phi_d),$$
> > where the middle equality is the $\operatorname{Ad}$-invariance of $\tilde{p}$ applied to the constant coefficients (the forms $\Phi_i^a$ are untouched by $\operatorname{Ad}_h$). The same holds with a $G$-valued *function* $g$ in place of the constant $h$, pointwise on $U$, since the identity is applied at each point $x \in U$ with $h = g(x)$. In particular, taking $\Phi_i = F_{\omega,s}$ (the local curvature) and $g = g$,
> > $$\tilde{p}\big(\operatorname{Ad}_{g^{-1}}F_{\omega,s},\dots,\operatorname{Ad}_{g^{-1}}F_{\omega,s}\big) = \tilde{p}\big(F_{\omega,s},\dots,F_{\omega,s}\big). \tag{$\dagger$}$$
> >
> > **Step 2 — compute the Chern–Weil form of $\phi^*\omega$.** On the chart $U$, using the local formula for the descended Chern–Weil form and then the gauge-action relation $F_{\phi^*\omega,s} = \operatorname{Ad}_{g^{-1}}F_{\omega,s}$,
> > $$p\big(F_{\phi^*\omega}\big)\big|_U = \tilde{p}\big(F_{\phi^*\omega,s},\dots,F_{\phi^*\omega,s}\big) = \tilde{p}\big(\operatorname{Ad}_{g^{-1}}F_{\omega,s},\dots,\operatorname{Ad}_{g^{-1}}F_{\omega,s}\big) \overset{(\dagger)}{=} \tilde{p}\big(F_{\omega,s},\dots,F_{\omega,s}\big) = p(F_\omega)\big|_U.$$
> > The equalities are, in order: the local formula for $p(F_{\phi^*\omega})$; the gauge-action curvature relation; the invariance identity $(\dagger)$; and the local formula for $p(F_\omega)$.
> >
> > **Step 3 — globalise.** The base $M$ is covered by such trivialising charts $U$, and on each the two forms agree. A form determined chart by chart is determined; hence $p(F_{\phi^*\omega}) = p(F_\omega)$ on all of $M$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix a Lie group $G$, a principal $G$-bundle $P \to M$, and $p \in I_d(G)$. Throughout we use the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]] in the form: *for every connection $\eta$ on a principal $G$-bundle $Q$, the Chern–Weil form $p(F_\eta)$ is closed and its class $c_p(Q) = [p(F_\eta)] \in H^{2d}_{dR}(\text{base})$ is independent of $\eta$.* This independence is what allows us, on each transformed bundle, to compute $c_p$ with any convenient connection.
>
> **Step 0 — the classes are defined.** The Chern–Weil theorem guarantees that $c_p(P)$, $c_p(P')$, $c_p(f^*P)$, $c_p(f_i^*P)$ are all well-defined de Rham classes, each independent of the connection used to compute it. The pullback maps $f^*, f_i^* : H^\bullet_{dR}(M) \to H^\bullet_{dR}(N)$ are defined because pullback of forms commutes with $d$, sending closed forms to closed forms and exact forms to exact forms.
>
> **Part (a) — naturality.** Let $f : N \to M$ be smooth and choose any connection $\omega$ on $P$. By the [[Thm - Pull-Back of Connections and Curvature|pull-back-connection theorem]], $\hat{f}^*\omega$ is a connection on $f^*P$. By Lemma 2,
> $$p\big(F_{\hat{f}^*\omega}\big) = f^*\,p(F_\omega) \qquad \text{as forms on } N.$$
> Taking de Rham classes and using that $f^*$ on cohomology is $[f^*(\ \cdot\ )]$ of the form-level pullback,
> $$c_p(f^*P) = \big[\,p(F_{\hat{f}^*\omega})\,\big] = \big[\,f^*p(F_\omega)\,\big] = f^*\big[\,p(F_\omega)\,\big] = f^*c_p(P),$$
> where the first equality evaluates $c_p(f^*P)$ with the connection $\hat{f}^*\omega$ (legitimate by connection-independence, Step 0), and the last evaluates $c_p(P)$ with $\omega$. This proves (a).
>
> **Part (b) — isomorphism invariance.** Let $\phi : P \to P'$ be an isomorphism of principal $G$-bundles over $M$ and choose any connection $\omega$ on $P$. By Lemma 3, $\phi_*\omega = (\phi^{-1})^*\omega$ is a connection on $P'$ and $p(F_{\phi_*\omega}) = p(F_\omega)$ as forms on $M$. Taking classes and using connection-independence to evaluate $c_p(P')$ with the connection $\phi_*\omega$,
> $$c_p(P') = \big[\,p(F_{\phi_*\omega})\,\big] = \big[\,p(F_\omega)\,\big] = c_p(P).$$
> This proves (b).
>
> **Part (c) — invariant of the isomorphism class.** Part (b) says that any two isomorphic bundles have the same characteristic class; hence $P \mapsto c_p(P)$ is constant on each isomorphism class, i.e. it is a function on the set of isomorphism classes of principal $G$-bundles over $M$. For the gauge statement, let $\phi \in \mathcal{G}(P)$ and $\omega \in \mathcal{A}(P)$. By Lemma 4,
> $$p\big(F_{\phi^*\omega}\big) = p(F_\omega) \qquad \text{as forms on } M,$$
> so the Chern–Weil form is fixed pointwise by the gauge action; a fortiori $[p(F_{\phi^*\omega})] = [p(F_\omega)]$, so the map $\omega \mapsto [p(F_\omega)]$ is constant on each gauge orbit and descends to a function on $\mathcal{A}(P)/\mathcal{G}(P)$ (which by connection-independence is the single value $c_p(P)$). Finally, let $\phi \in \operatorname{Aut}(P)$ cover the base diffeomorphism $\bar\phi : M \to M$. Then $\phi : P \to \bar\phi^*P$ is an isomorphism of principal $G$-bundles over $M$ — it is $G$-equivariant and, by construction of $\bar\phi^*P$ and the universal property of the pullback, covers $\operatorname{id}_M$ once its target is taken to be $\bar\phi^*P$ — so part (b) gives $c_p(P) = c_p(\bar\phi^*P)$, and part (a) gives $c_p(\bar\phi^*P) = \bar\phi^*c_p(P)$; combining, $c_p(P) = \bar\phi^*c_p(P)$. This proves (c).
>
> **Part (d) — homotopy invariance.** Let $f_0, f_1 : N \to M$ be smoothly homotopic. By part (a), $c_p(f_i^*P) = f_i^*c_p(P)$ for $i = 0, 1$. By the [[Thm - Homotopy Invariance of de Rham Cohomology|homotopy invariance of de Rham cohomology]] — *smoothly homotopic maps induce the same homomorphism on de Rham cohomology, $f_0^* = f_1^* : H^\bullet_{dR}(M) \to H^\bullet_{dR}(N)$* — we have $f_0^*c_p(P) = f_1^*c_p(P)$. Combining,
> $$c_p(f_0^*P) = f_0^*c_p(P) = f_1^*c_p(P) = c_p(f_1^*P).$$
> This proves (d).
>
> **Conclusion.** All four statements hold. The characteristic class $c_p$ is natural under smooth maps, invariant under isomorphism of bundles, blind to the gauge freedom at the level of the form, and homotopy invariant on the base. $\blacksquare$

> [!note]- Alternative proof of (d) via the bundle homotopy theorem
> One may bypass de Rham homotopy invariance and instead use the bundle-level theorem [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|that homotopic maps pull back isomorphic principal bundles]]: *if $f_0 \simeq f_1 : N \to M$ are smoothly homotopic, then $f_0^*P \cong f_1^*P$ as principal $G$-bundles over $N$.* Given this, part (b) applied to the isomorphism $f_0^*P \cong f_1^*P$ yields $c_p(f_0^*P) = c_p(f_1^*P)$ directly. The two proofs are genuinely the same fact seen upstairs and downstairs: the bundle isomorphism of the second route is constructed from a connection on the homotopy bundle over $N\times[0,1]$, whose curvature descends to the transgression underlying de Rham homotopy invariance in the first route.

---

# Cross-Field Exercise Suggestions

**Restriction of a bundle to a submanifold (differential topology).** Let $E \to M$ be a complex vector bundle and $\Sigma \subseteq M$ a closed embedded surface with inclusion $\iota : \Sigma \hookrightarrow M$. The restricted bundle $E|_\Sigma$ is $\iota^*E$, so naturality gives $c_1(E|_\Sigma) = \iota^*c_1(E)$ and the characteristic number $\int_\Sigma c_1(E|_\Sigma) = \int_\Sigma \iota^*c_1(E) = \langle c_1(E), [\Sigma]\rangle$. The theorem applies because restriction *is* pullback along an inclusion; the non-obvious content is that a purely local restriction is computed by a global cohomological pairing, which is how characteristic numbers of subvarieties are read off from ambient classes.

**Metric-independence of Chern classes (Riemannian and Hermitian geometry).** Two Hermitian metrics $h_0, h_1$ on a complex vector bundle $E$ produce two unitary frame bundles $\operatorname{Fr}_{U,h_0}(E)$ and $\operatorname{Fr}_{U,h_1}(E)$. These are isomorphic principal $U(r)$-bundles (the identity of $E$ is unitary once one measures with the appropriate metric on the two sides), so isomorphism invariance forces the Chern classes computed from the two metrics to agree. The theorem applies because a change of metric is an isomorphism of frame bundles; it is non-obvious because the two curvature forms are genuinely different differential forms, equal only in cohomology.

**Gauge-invariance of the instanton charge (mathematical physics).** On a closed oriented $4$-manifold $X$ with a principal $SU(2)$-bundle $P$, the second Chern number is $\tfrac{1}{8\pi^2}\int_X\operatorname{tr}(F_\omega\wedge F_\omega)$, the integral of a Chern–Weil form for the invariant polynomial $\xi\mapsto -\operatorname{tr}(\xi^2)$. Part (c) shows the integrand is unchanged by a gauge transformation, so the charge is a functional on the moduli space $\mathcal{A}(P)/\mathcal{G}(P)$ rather than on connections. The theorem applies because $-\operatorname{tr}(\xi^2)$ is $\operatorname{Ad}$-invariant; the subtlety is that the connection form $\omega$ transforms with a derivative term, yet the curvature — and hence the charge — does not.

---

# Bridges

- **[[Thm - Chern-Weil Theorem|Chern–Weil theorem]]** — the indispensable input. That theorem establishes the connection-independence of $c_p(P)$; this page uses it at the last step of every part to evaluate $c_p$ of the transformed bundle with the transformed connection. Together they say: the Chern–Weil construction produces a class that depends on neither the connection (Chern–Weil) nor the presentation of the bundle (this page).

- **[[Thm - Pull-Back of Connections and Curvature|Pull-back of connections and curvature]]** — supplies the geometric half of naturality. Its content is that pulling back a bundle pulls back its connection and curvature, with $\Omega' = \hat{f}^*\Omega$ and, in charts, $\Omega'_\alpha = f^*\Omega_\alpha$; the passage from this to naturality of the class is entirely the wedge-and-constants bookkeeping of Lemma 2.

- **[[Thm - Gauge Transformations Act on Connections and Curvature|Gauge transformations act on connections and curvature]]** — supplies the conjugation formula $F_{\phi^*\omega} = \operatorname{Ad}_{g^{-1}}F_\omega$ that, married to the $\operatorname{Ad}$-invariance of $p$, gives gauge invariance of the form. The absence of a derivative term in the curvature transformation (present in the connection transformation) is exactly what makes the Chern–Weil form, and not merely its class, gauge invariant.

- **[[Def - Characteristic Class|Characteristic class]] (Algebraic Topology III)** — the axiomatic notion. There a characteristic class of a bundle over $M$ is defined as the pullback $f^*c$ of a fixed cohomology class $c$ of the classifying space along a classifying map $f : M \to BG$, and one *postulates* that it depends only on the isomorphism class. Parts (a), (b), and (d) of this page are the differential-geometric proof that the Chern–Weil class satisfies those axioms: naturality is the pullback compatibility, isomorphism invariance is the well-definedness on isomorphism classes, and homotopy invariance is the independence of the classifying map within its homotopy class.

- **[[Thm - Trivial Bundles Have Vanishing Characteristic Classes|Trivial bundles have vanishing characteristic classes]]** — the immediate sequel. Once $c_p$ is an isomorphism invariant, one computes it on the product bundle $M\times G$ with its flat product connection, whose curvature vanishes, so $c_p(M\times G) = 0$ in positive degree; isomorphism invariance (part (b)) then gives $c_p(P) = 0$ for every trivial $P$. That theorem is the source of all the non-triviality obstructions this chapter builds.

---

# Unlocked by This

> [!tip] Characteristic classes as obstructions to triviality *(from Algebraic Topology)*
> Combining this page with the vanishing theorem, a non-zero characteristic class certifies that a bundle is non-trivial: $c_p(P)\neq 0 \Rightarrow P\not\cong M\times G$. This is the engine behind the non-triviality of the tangent bundle $TS^2$, of the tautological bundle $\mathcal{O}(-1)$ over $\mathbb{CP}^1$, and of the instanton bundles over $S^4$. See **Thm - Trivial Bundles Have Vanishing Characteristic Classes** and [[Def - Chern Classes]].

> [!tip] Characteristic numbers of moduli spaces *(from Gauge Theory)*
> Gauge invariance of the Chern–Weil form (part (c)) is the reason the second Chern number and the Chern–Simons integrand descend to the quotient $\mathcal{A}(P)/\mathcal{G}(P)$, where the gauge-theoretic moduli spaces of chapters VII, XI, and XIII live. Without it the topological charges of instantons would not be well defined. See **Thm - Second Chern Number of an SU(2)-Bundle over a Closed Four-Manifold is the Clutching Degree**.
