---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - The Induced Inner Product and Volume Form are Well-Defined"
  - "Thm - Riesz Representation Theorem (Finite-Dimensional)"
  - "Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms"
  - "Def - Alternating Tensor and Lambda k V Dual"
  - "Def - Orientation of a Vector Space"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $V$ is a real vector space of dimension $n$, equipped with a symmetric bilinear form $\langle\cdot,\cdot\rangle : V \times V \to \mathbb{R}$ that is **non-degenerate** — meaning that if $\langle v, w\rangle = 0$ for all $w \in V$ then $v = 0$ — but **not necessarily positive definite**. Such a form has an *index* $p \in \{0, 1, \dots, n\}$, the number of negative signs in any diagonalisation, which is well-defined by [[Thm - Sylvester's Law of Inertia|Sylvester's law of inertia]]; $p = 0$ is the Euclidean (Riemannian) case and $p = 1$ the Lorentzian case. We fix an orientation of $V$ in the sense of [[Def - Orientation of a Vector Space|orientation of a vector space]].

A **generalized orthonormal basis** $e_1, \dots, e_n$ of $V$ satisfies $\langle e_i, e_j\rangle = 0$ for $i \neq j$ and $\langle e_j, e_j\rangle = \epsilon_j = \pm 1$; its dual basis of $V^*$ is written $e_1^*, \dots, e_n^*$, with $e_i^*(e_j) = \delta_{ij}$. For $0 \le k \le n$, the space $\Lambda^k V^*$ of alternating $k$-linear forms on $V$ ([[Def - Alternating Tensor and Lambda k V Dual|alternating tensors]]) carries the **induced inner product**
$$\langle \omega, \eta\rangle := \sum_{i_1 < \dots < i_k} \epsilon_{i_1} \cdots \epsilon_{i_k}\, \omega(e_{i_1}, \dots, e_{i_k})\, \eta(e_{i_1}, \dots, e_{i_k}), \qquad \omega, \eta \in \Lambda^k V^*,$$
which is again a non-degenerate symmetric bilinear form and is independent of the chosen generalized orthonormal basis, both established on [[Thm - The Induced Inner Product and Volume Form are Well-Defined|the previous page]]. The top exterior power $\Lambda^n V^*$ is one-dimensional; the orientation fixes a distinguished generator, the **volume form** $\mathrm{vol} = e_1^* \wedge \dots \wedge e_n^*$ for any positively oriented generalized orthonormal basis, and $\langle \mathrm{vol}, \mathrm{vol}\rangle = (-1)^p$. The symbol $\wedge$ is the exterior product ([[Thm - Wedge Product Properties|wedge product]]); the full symbol registry for the chapter is on the topic page [[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory]].

The map produced by this theorem is the **Hodge star** $\star : \Lambda^k V^* \to \Lambda^{n-k} V^*$, defined on the following page [[Def - Hodge Star in Arbitrary Signature|Hodge star in arbitrary signature]] using the existence and uniqueness proved here.

> [!warning] Convention: which defining relation, and the competing sign
> The series adopts Bär's defining relation for the Hodge star,
> $$\omega \wedge \eta = \langle \star\omega, \eta\rangle\, \mathrm{vol} \qquad (\omega \in \Lambda^k V^*,\ \eta \in \Lambda^{n-k} V^*),$$
> in every signature. The other common convention defines a map $\star'$ by $\alpha \wedge \star'\beta = \langle \alpha, \beta\rangle\, \mathrm{vol}$ for $\alpha, \beta \in \Lambda^k V^*$; the two differ by the factor $(-1)^{k(n-k)}$, that is $\star' = (-1)^{k(n-k)}\star_V$ in the Riemannian case, and they agree in dimension $4$ on $2$-forms. The vault's Riemannian operator [[Def - The Hodge Star Operator|the Hodge star operator]] ($\star_V$) is built from the $\alpha \wedge \star'\beta$ relation. The full sign dictionary between the three operators — $\star_B = (-1)^p \star_V$ and $\star' = (-1)^{k(n-k)}\star_V$ — is worked out on [[Def - Hodge Star in Arbitrary Signature]]. **The present theorem asserts only existence, uniqueness, and linearity, and these are the same for any of the three conventions**; the signs enter only in the properties of $\star$, not in whether it exists.

---

# Statement

> **Theorem (Existence and uniqueness of the Hodge star).** Let $V$ be an oriented $n$-dimensional real vector space equipped with a non-degenerate symmetric bilinear form $\langle\cdot,\cdot\rangle$ of index $p$, and let $\mathrm{vol} \in \Lambda^n V^*$ be the associated volume form. Fix $k$ with $0 \le k \le n$. Then for every $\omega \in \Lambda^k V^*$ there exists a **unique** element $\star\omega \in \Lambda^{n-k} V^*$ such that
> $$\omega \wedge \eta = \langle \star\omega, \eta\rangle\, \mathrm{vol} \qquad \text{for all } \eta \in \Lambda^{n-k} V^*. \tag{$\ast$}$$
> Moreover, the resulting map $\star : \Lambda^k V^* \to \Lambda^{n-k} V^*$, $\omega \mapsto \star\omega$, is $\mathbb{R}$-linear.

This is Lemma 3.1.5 in Bär's *Gauge Theory* (content-map item B-T3.1.4). The source proof is complete except that it invokes the non-degeneracy of the induced inner product on $\Lambda^{n-k}V^*$ without comment and appeals only to the definite Riesz lemma; we supply the general, indefinite statement and its proof below (Lemma 1) so that the argument is self-contained in Lorentzian and higher-index signatures.

---

# Motivation

The Hodge star is the single algebraic device that lets differential forms of complementary degree talk to each other: it converts a $k$-form into an $(n-k)$-form, and through that conversion it encodes the metric duality that underlies electromagnetism, the Yang–Mills functional, the codifferential, and the self-dual/anti-self-dual splitting on which four-dimensional gauge theory rests. Before any of that can be used, one owes a proof that the object exists at all and that the formula $(\ast)$ pins it down without ambiguity. That is the sole purpose of this theorem.

The reason the question is not trivial is that $(\ast)$ does not *construct* $\star\omega$; it *characterises* it, by demanding that a certain equation hold for every test form $\eta$. A characterisation of this kind is a promissory note: it is worth something only if exactly one element of $\Lambda^{n-k} V^*$ redeems it. If no element satisfied $(\ast)$, the Hodge star would be a fiction; if two different elements did, then "$\star\omega$" would be a symbol without a referent, and every later computation — the star table on Minkowski space, the identity $\star\star = (-1)^{k(n-k)+p}$, the equation $d\star F = 0$ — would be built on sand. The theorem removes both dangers at once.

The mechanism that redeems the note is a pairing argument, and it is worth naming the two ingredients now because they recur throughout the chapter. First, the exterior product furnishes a bilinear pairing $\Lambda^k V^* \times \Lambda^{n-k} V^* \to \Lambda^n V^* \cong \mathbb{R}$, $(\omega, \eta) \mapsto \omega \wedge \eta$, and this pairing is *perfect*: no nonzero $\omega$ wedges to zero against every $\eta$, and vice versa. Second, the induced inner product on $\Lambda^{n-k} V^*$ is *non-degenerate*, so it identifies $\Lambda^{n-k} V^*$ with its own dual. Composing these two identifications produces a well-defined isomorphism, and $\star\omega$ is simply the image of $\omega$ under it. The whole content of the theorem is that a perfect pairing followed by a non-degenerate inner product is an isomorphism — a statement of finite-dimensional linear algebra with no geometry in it beyond the choice of $\langle\cdot,\cdot\rangle$ and orientation.

The one genuine subtlety, and the reason the previous page had to prove that the induced form is non-degenerate, is that we are working in *arbitrary signature*. In the Euclidean case $p = 0$ the induced inner product is positive definite and one may quote the ordinary Riesz representation theorem for inner-product spaces. In Lorentzian signature it is indefinite — for instance $\langle dt \wedge dx, dt \wedge dx\rangle = -1$ on Minkowski space — so positivity is unavailable and the ordinary Riesz theorem does not apply verbatim. We therefore prove the representation statement for non-degenerate (not necessarily definite) forms directly, from injectivity and a dimension count, and it is that indefinite version that does the work.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is a non-degenerate symmetric bilinear form on a finite-dimensional space plus an orientation; the interesting question is which situations secretly provide those data and hence license a Hodge star.

The first disguised source is **a tangent space of a semi-Riemannian manifold**. A metric $g$ of any signature on a smooth manifold $M$ restricts, at each point $x$, to a non-degenerate symmetric bilinear form $g_x$ on $T_xM$, and an orientation of $M$ orients each $T_xM$ compatibly. The theorem then produces a Hodge star $\star_x$ on $\Lambda^\bullet T_x^*M$ at every point, and smoothness of $g$ makes the family $x \mapsto \star_x$ a bundle map. The non-obvious bridge is that nothing about the argument uses positivity, so the *same* theorem covers Riemannian manifolds, Lorentzian spacetimes, and split signatures without alteration; the index $p$ appears only later, in the properties. *Example problem:* on an oriented Lorentzian $4$-manifold, produce the operator sending the electromagnetic field strength $F \in \Omega^2(M)$ to $\star F \in \Omega^2(M)$ that appears in Maxwell's equation $d\star F + J = 0$.

The second disguised source is **any perfect bilinear pairing into a one-dimensional space**. Whenever a problem supplies a bilinear map $B : U \times W \to L$ with $\dim L = 1$ such that $B$ is non-degenerate in each slot, together with a non-degenerate form on $W$, the composite $U \to W^* \to W$ is an isomorphism of the same shape as $\star$. The wedge product into $\Lambda^n V^*$ is the archetype, but the pattern also appears in Poincaré duality (the cup-product pairing into the top cohomology) and in the pairing of a Lie algebra with itself by an invariant form. The non-obvious step is recognising that "wedge to the top degree" is *perfect*, which rests on the previous page's computation that the induced form on $\Lambda^{n-k}V^*$ is non-degenerate. *Example problem:* show that on an oriented closed surface the pairing $H^1 \times H^1 \to H^2 \cong \mathbb{R}$ given by cup product is perfect and therefore identifies $H^1$ with its dual.

The third disguised source is **a symmetric matrix with nonzero determinant**, presented without any mention of "inner product". If a bilinear form is written in coordinates by a symmetric Gram matrix $G$ with $\det G \neq 0$, then it is non-degenerate — the map $v \mapsto \langle v, \cdot\rangle$ has matrix $G$, which is invertible — and the theorem applies even though the form may be indefinite. The non-obvious bridge is that non-degeneracy is exactly $\det G \neq 0$, not positivity ($G$ positive definite); many students reflexively check the wrong condition. *Example problem:* given the Minkowski Gram matrix $\operatorname{diag}(-1, 1, 1, 1)$, whose determinant is $-1 \neq 0$, conclude that a Hodge star exists on $\Lambda^\bullet(\mathbb{R}^{1,3})^*$ despite the form being indefinite.

**Targets (Output Amplification)**

The bare conclusion is a linear map $\star$ characterised by $(\ast)$. Combined with further ingredients it becomes the engine of the chapter.

Combine the existence of $\star$ with **a computation of $\star\star$**. Applying the theorem in each degree gives operators $\Lambda^k \to \Lambda^{n-k} \to \Lambda^k$, and the composite is $\star\star = (-1)^{k(n-k)+p}\,\mathrm{id}$ ([[Thm - Properties of the Hodge Star in Arbitrary Signature|properties of the Hodge star]]). In dimension $4$, index $0$, on $2$-forms this reads $\star\star = \mathrm{id}$, an involution, so $\Lambda^2$ splits into $\pm 1$ eigenspaces $\Lambda^2_+ \oplus \Lambda^2_-$. The extra ingredient is the sign computation; the payoff is the self-dual/anti-self-dual decomposition that defines instantons. This is non-obvious because the mere existence of $\star$ says nothing about whether it squares to $\pm 1$; that is a separate, signature-dependent fact.

Combine the existence of $\star$ with **integration and Stokes' theorem on an oriented manifold**. Fibrewise $\star$ together with $\int_M$ produces the global $L^2$ inner product $\langle\!\langle \alpha, \beta\rangle\!\rangle = \int_M \alpha \wedge \star\beta$ on forms, and integration by parts then exhibits the codifferential $\delta = \pm \star d \star$ as the formal adjoint of the exterior derivative $d$. The extra ingredients are Stokes' theorem and compactness (or compact support); the payoff is Hodge theory and the elliptic operator $d + \delta$. This amplification is non-obvious because it converts a pointwise algebraic gadget into an analytic adjointness statement.

Combine the existence of $\star$ with **the calculus of variations**. The Yang–Mills functional $\tfrac12\int_M \langle F_A, F_A\rangle\,\mathrm{vol}$ and the Maxwell action $\tfrac12\int F \wedge \star F$ are built from $\star$, and their Euler–Lagrange equations are $d_A \star F_A = 0$ and $d\star F + J = 0$. The extra ingredient is a variational argument (perturb the connection, integrate by parts); the payoff is the field equations of physics. This is non-obvious because the star, defined by a purely algebraic characterisation, turns out to encode precisely the metric information that makes the action functional physically meaningful.

---

# Why Is It True

Set the geometry aside and look only at the linear algebra. We are given two structures on a finite-dimensional space. On one hand, the exterior product provides a way to pair a $k$-form $\omega$ with an $(n-k)$-form $\eta$ and land in the one-dimensional space $\Lambda^n V^*$; dividing by the fixed generator $\mathrm{vol}$ turns this into an ordinary number $(\omega \wedge \eta)/\mathrm{vol}$. So each fixed $\omega$ defines a *linear functional* $T_\omega$ on $\Lambda^{n-k} V^*$: feed it an $\eta$, get a number. On the other hand, $\Lambda^{n-k} V^*$ carries the induced inner product, which is non-degenerate.

Now recall what a non-degenerate inner product does for you: it lets you represent *every* linear functional as "inner product with a fixed vector". This is the Riesz representation idea, and it holds for any non-degenerate symmetric form on a finite-dimensional space, not only for positive-definite ones — the proof is just that $w \mapsto \langle w, \cdot\rangle$ is an injective linear map from the space to its dual, and injective plus equal dimensions forces bijective. Applying this to the functional $T_\omega$ gives exactly one vector $\star\omega \in \Lambda^{n-k} V^*$ with $T_\omega(\eta) = \langle \star\omega, \eta\rangle$ for all $\eta$, which is the defining relation $(\ast)$ once you multiply back through by $\mathrm{vol}$.

> **The wedge pairing $\Lambda^k V^* \times \Lambda^{n-k} V^* \to \Lambda^n V^* \cong \mathbb{R}$ is perfect, and a perfect pairing composed with a non-degenerate inner product is an isomorphism; the Hodge star is that isomorphism, and Riesz representation is what makes it exist and be unique.**

Uniqueness is the same non-degeneracy read the other way: if two candidates $\alpha, \alpha'$ both represented $T_\omega$, their difference would pair to zero against every $\eta$, and non-degeneracy forces $\alpha = \alpha'$. Linearity in $\omega$ is automatic and costs nothing: the assignment $\omega \mapsto T_\omega$ is linear because the wedge product is linear in its first slot, and Riesz representation is a linear isomorphism, so the composite $\omega \mapsto \star\omega$ is linear. There is no cleverness anywhere; the theorem is the statement that two non-degeneracies (of the wedge pairing and of the inner product) compose to an isomorphism.

---

# What Makes This Hard

The single point where a careless proof breaks is **signature**. In the Euclidean case the induced inner product on $\Lambda^{n-k}V^*$ is positive definite and one may cite the standard Riesz representation theorem for inner-product spaces; in Lorentzian or higher index it is genuinely indefinite (already $\langle dt\wedge dx, dt\wedge dx\rangle = -1$ on Minkowski $2$-forms), so positivity is gone and the standard theorem does not apply as stated. The fix is to notice that Riesz representation needs only *non-degeneracy*, not positivity, and to prove that version — but this requires knowing that the induced form is non-degenerate, which is precisely the content the previous page established and which Bär's proof uses silently. The second, smaller trap is the phrase "$(\omega \wedge \eta)/\mathrm{vol}$": division is only meaningful because $\Lambda^n V^*$ is one-dimensional and $\mathrm{vol}$ is a *nonzero* generator, so the well-definedness of the coefficient must be checked before the functional $T_\omega$ can be written down.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** For each fixed $\omega$, turn the desired relation $(\ast)$ into "$T_\omega(\eta) = \langle \star\omega, \eta\rangle$ for all $\eta$" by dividing through by $\mathrm{vol}$, so that $\star\omega$ is exactly the vector representing the functional $T_\omega$ under the induced inner product. Existence and uniqueness of that vector is Riesz representation for a non-degenerate (possibly indefinite) form; linearity in $\omega$ falls out because everything in sight is linear in $\omega$.

**Subgoal decomposition:**

1. **Indefinite Riesz representation.** Prove that a non-degenerate symmetric bilinear form $b$ on a finite-dimensional real space $W$ makes $w \mapsto b(w, \cdot)$ an isomorphism $W \to W^*$; hence every functional is $b(w, \cdot)$ for a unique $w$.
   - *Hint:* Non-degeneracy is exactly "trivial kernel"; then use rank–nullity and $\dim W^* = \dim W$.
   - *Why needed:* This is the only place existence and uniqueness of $\star\omega$ come from, and it must work without positivity because the induced form is indefinite in Lorentzian signature.

2. **The wedge functional.** For fixed $\omega \in \Lambda^k V^*$, show that $T_\omega : \eta \mapsto (\omega \wedge \eta)/\mathrm{vol}$ is a well-defined linear functional on $\Lambda^{n-k} V^*$.
   - *Hint:* $\Lambda^n V^*$ is one-dimensional with basis $\mathrm{vol}$, so "divide by $\mathrm{vol}$" is a genuine linear map $\Lambda^n V^* \to \mathbb{R}$; precompose with $\eta \mapsto \omega \wedge \eta$.
   - *Why needed:* It is the functional to which Riesz representation is applied.

3. **Represent $T_\omega$.** Apply subgoal 1 with $W = \Lambda^{n-k} V^*$ and $b = \langle\cdot,\cdot\rangle$ (non-degenerate by the previous page) to get a unique $\star\omega$ with $T_\omega(\eta) = \langle \star\omega, \eta\rangle$; multiply back by $\mathrm{vol}$ to recover $(\ast)$.
   - *Hint:* The representing vector *is* $\star\omega$, by definition.
   - *Why needed:* This produces the map and gives uniqueness in one stroke.

4. **Linearity in $\omega$.** Show $\star(a\omega_1 + b\omega_2) = a\star\omega_1 + b\star\omega_2$.
   - *Hint:* $T_{a\omega_1 + b\omega_2} = aT_{\omega_1} + bT_{\omega_2}$ because wedge is linear in the first slot; then invoke uniqueness from subgoal 3.
   - *Why needed:* The theorem asserts $\star$ is linear, and this is where that is verified.

---

# Lemma Decomposition

> [!note]- Lemma 1: Indefinite Riesz representation
> **Statement:** Let $W$ be a finite-dimensional real vector space and $b : W \times W \to \mathbb{R}$ a non-degenerate symmetric bilinear form (non-degenerate: $b(w, w') = 0$ for all $w' \in W$ implies $w = 0$). Then the map $\flat : W \to W^*$, $\flat(w) = b(w, \cdot)$, is a linear isomorphism. Consequently, for every linear functional $\varphi \in W^*$ there is a unique $w \in W$ with $\varphi(w') = b(w, w')$ for all $w' \in W$.
>
> **Hint:** Non-degeneracy says $\ker\flat = \{0\}$; combine injectivity with $\dim W^* = \dim W$ and rank–nullity.
>
> **Why needed:** The ordinary [[Thm - Riesz Representation Theorem (Finite-Dimensional)|Riesz representation theorem]] is proved only for positive-definite inner products, whereas the induced form on $\Lambda^{n-k}V^*$ is indefinite whenever $p > 0$; this lemma extends the representation statement to every non-degenerate form and is the sole source of the existence and uniqueness of $\star\omega$.
>
> > [!note]- Full proof
> > We must show $\flat$ is linear, injective, and surjective, and then deduce the representation statement.
> >
> > **$\flat$ is linear.** Fix $w_1, w_2 \in W$ and $a_1, a_2 \in \mathbb{R}$. For every $w' \in W$,
> > $$\flat(a_1 w_1 + a_2 w_2)(w') = b(a_1 w_1 + a_2 w_2,\, w') = a_1\, b(w_1, w') + a_2\, b(w_2, w') = \big(a_1 \flat(w_1) + a_2 \flat(w_2)\big)(w')$$
> > (by linearity of $b$ in its first argument). As this holds for all $w'$, we have $\flat(a_1 w_1 + a_2 w_2) = a_1\flat(w_1) + a_2\flat(w_2)$, so $\flat$ is linear.
> >
> > **$\flat$ is injective.** Suppose $\flat(w) = 0$ in $W^*$, that is, $b(w, w') = 0$ for all $w' \in W$. By the non-degeneracy hypothesis on $b$, this forces $w = 0$. Hence $\ker\flat = \{0\}$, so $\flat$ is injective.
> >
> > **$\flat$ is surjective.** The dual space of a finite-dimensional space has the same dimension: if $w_1, \dots, w_m$ is a basis of $W$, the dual functionals $w_1^*, \dots, w_m^*$ (defined by $w_i^*(w_j) = \delta_{ij}$) form a basis of $W^*$, so $\dim W^* = m = \dim W$. By the rank–nullity theorem applied to $\flat : W \to W^*$,
> > $$\dim \operatorname{im}\flat = \dim W - \dim\ker\flat = m - 0 = m = \dim W^*$$
> > (using injectivity, $\dim\ker\flat = 0$). Thus $\operatorname{im}\flat$ is a subspace of $W^*$ of full dimension $m$, and a subspace of a finite-dimensional space whose dimension equals that of the whole space is the whole space; therefore $\operatorname{im}\flat = W^*$ and $\flat$ is surjective.
> >
> > **Representation.** Since $\flat$ is a linear bijection, for each $\varphi \in W^*$ there is a unique $w \in W$ with $\flat(w) = \varphi$, that is, $b(w, w') = \varphi(w')$ for all $w'$; existence is surjectivity and uniqueness is injectivity of $\flat$. (By symmetry of $b$, one also has $\varphi(w') = b(w', w)$, so it does not matter in which slot the representing vector is placed.) $\blacksquare$

> [!note]- Lemma 2: The wedge pairing gives a well-defined linear functional
> **Statement:** Let $\mathrm{vol} \in \Lambda^n V^*$ be nonzero. There is a unique linear map $c : \Lambda^n V^* \to \mathbb{R}$ with $c(\mathrm{vol}) = 1$, namely $c(\sigma) = a$ where $\sigma = a\,\mathrm{vol}$. For each fixed $\omega \in \Lambda^k V^*$, the map
> $$T_\omega : \Lambda^{n-k} V^* \to \mathbb{R}, \qquad T_\omega(\eta) := c(\omega \wedge \eta) = \frac{\omega \wedge \eta}{\mathrm{vol}},$$
> is a well-defined linear functional on $\Lambda^{n-k} V^*$.
>
> **Hint:** $\Lambda^n V^*$ is one-dimensional, so $\mathrm{vol}$ is a basis and "coefficient with respect to $\mathrm{vol}$" is a linear isomorphism onto $\mathbb{R}$; precompose with the linear map $\eta \mapsto \omega \wedge \eta$.
>
> **Why needed:** It manufactures, from the exterior product, the linear functional whose Riesz representative is $\star\omega$; without one-dimensionality of $\Lambda^n V^*$ the symbol $(\omega\wedge\eta)/\mathrm{vol}$ would be meaningless.
>
> > [!note]- Full proof
> > **The coefficient map $c$ is well-defined and linear.** The top exterior power has dimension $\dim \Lambda^n V^* = \binom{n}{n} = 1$ ([[Def - Alternating Tensor and Lambda k V Dual|dimension of $\Lambda^k V^*$]]). Since $\mathrm{vol} \neq 0$, the singleton $\{\mathrm{vol}\}$ is a basis of $\Lambda^n V^*$, so every $\sigma \in \Lambda^n V^*$ can be written $\sigma = a\,\mathrm{vol}$ for one and only one scalar $a \in \mathbb{R}$; set $c(\sigma) := a$. This is exactly the coordinate map with respect to the basis $\{\mathrm{vol}\}$, hence linear: if $\sigma_1 = a_1\,\mathrm{vol}$ and $\sigma_2 = a_2\,\mathrm{vol}$ then $\lambda_1\sigma_1 + \lambda_2\sigma_2 = (\lambda_1 a_1 + \lambda_2 a_2)\,\mathrm{vol}$, so $c(\lambda_1\sigma_1 + \lambda_2\sigma_2) = \lambda_1 a_1 + \lambda_2 a_2 = \lambda_1 c(\sigma_1) + \lambda_2 c(\sigma_2)$. Uniqueness of $c$ with $c(\mathrm{vol}) = 1$ holds because a linear map out of a one-dimensional space is determined by its value on a basis vector, and $c(\mathrm{vol}) = 1$ fixes that value.
> >
> > **$T_\omega$ is well-defined and linear.** The exterior product is bilinear ([[Thm - Wedge Product Properties|wedge product properties]]), so for fixed $\omega$ the map $L_\omega : \Lambda^{n-k}V^* \to \Lambda^n V^*$, $L_\omega(\eta) = \omega \wedge \eta$, is linear. Then $T_\omega = c \circ L_\omega$ is a composition of linear maps and is therefore a well-defined linear functional $\Lambda^{n-k}V^* \to \mathbb{R}$. Concretely, for $\eta_1, \eta_2 \in \Lambda^{n-k}V^*$ and $\lambda_1, \lambda_2 \in \mathbb{R}$,
> > $$T_\omega(\lambda_1\eta_1 + \lambda_2\eta_2) = c\big(\omega \wedge (\lambda_1\eta_1 + \lambda_2\eta_2)\big) = c\big(\lambda_1(\omega\wedge\eta_1) + \lambda_2(\omega\wedge\eta_2)\big) = \lambda_1 T_\omega(\eta_1) + \lambda_2 T_\omega(\eta_2),$$
> > using bilinearity of $\wedge$ in the middle step and linearity of $c$ in the last. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $V$ be oriented, $n$-dimensional, with a non-degenerate symmetric bilinear form $\langle\cdot,\cdot\rangle$ of index $p$, volume form $\mathrm{vol}$, and fix $k$ with $0 \le k \le n$. We produce, for each $\omega \in \Lambda^k V^*$, a unique $\star\omega \in \Lambda^{n-k}V^*$ satisfying $(\ast)$, and show $\omega \mapsto \star\omega$ is linear.
>
> **Step 0 — the preconditions hold.** Two facts from earlier pages are needed and we record them explicitly.
> *(a) The volume form is a nonzero generator of the one-dimensional space $\Lambda^n V^*$.* We have $\dim\Lambda^n V^* = \binom{n}{n} = 1$, and for a positively oriented generalized orthonormal basis $e_1, \dots, e_n$ the element $\mathrm{vol} = e_1^* \wedge \dots \wedge e_n^*$ is nonzero because $e_1^*, \dots, e_n^*$ are linearly independent; that $\mathrm{vol}$ is independent of the chosen positively oriented basis is part (iii) of [[Thm - The Induced Inner Product and Volume Form are Well-Defined|the well-definedness theorem]].
> *(b) The induced inner product on $\Lambda^{n-k}V^*$ is non-degenerate.* By part (ii) of the same theorem, restated here: for a generalized orthonormal basis $e_1,\dots,e_n$ of $V$, the wedge monomials $\{e^*_{j_1}\wedge\dots\wedge e^*_{j_{n-k}}\}_{j_1<\dots<j_{n-k}}$ form a generalized orthonormal basis of $\Lambda^{n-k}V^*$ with $\langle e^*_J, e^*_J\rangle = \epsilon_{j_1}\cdots\epsilon_{j_{n-k}} = \pm 1$; a bilinear form that is diagonal with entries $\pm 1$ in some basis has an invertible (indeed $\pm 1$-determinant) Gram matrix and is therefore non-degenerate. Hence $\langle\cdot,\cdot\rangle$ restricted to $\Lambda^{n-k}V^*$ satisfies the hypothesis of Lemma 1.
>
> **Step 1 — construct the wedge functional.** Fix $\omega \in \Lambda^k V^*$. By Step 0(a), $\mathrm{vol}$ is a nonzero generator of $\Lambda^n V^*$, so by Lemma 2 the map
> $$T_\omega : \Lambda^{n-k} V^* \to \mathbb{R}, \qquad T_\omega(\eta) = \frac{\omega\wedge\eta}{\mathrm{vol}},$$
> is a well-defined linear functional, that is, $T_\omega \in (\Lambda^{n-k}V^*)^*$.
>
> **Step 2 — existence of $\star\omega$.** Apply Lemma 1 with $W = \Lambda^{n-k} V^*$, with $b = \langle\cdot,\cdot\rangle$ the induced inner product (non-degenerate by Step 0(b)), and with $\varphi = T_\omega \in W^*$. Lemma 1 yields a **unique** element $\star\omega \in \Lambda^{n-k} V^*$ such that
> $$T_\omega(\eta) = \langle \star\omega, \eta\rangle \qquad \text{for all } \eta \in \Lambda^{n-k}V^*.$$
> Unwinding the definition of $T_\omega$, this says $(\omega\wedge\eta)/\mathrm{vol} = \langle\star\omega,\eta\rangle$, and multiplying both sides by the generator $\mathrm{vol}$ of $\Lambda^n V^*$ gives
> $$\omega\wedge\eta = \langle\star\omega,\eta\rangle\,\mathrm{vol} \qquad \text{for all } \eta \in \Lambda^{n-k}V^*,$$
> which is exactly $(\ast)$. This proves existence.
>
> **Step 3 — uniqueness of $\star\omega$.** Suppose $\alpha, \alpha' \in \Lambda^{n-k}V^*$ both satisfy $(\ast)$ for the given $\omega$, so that for every $\eta \in \Lambda^{n-k}V^*$,
> $$\langle\alpha,\eta\rangle\,\mathrm{vol} = \omega\wedge\eta = \langle\alpha',\eta\rangle\,\mathrm{vol}.$$
> Since $\mathrm{vol} \neq 0$ spans the one-dimensional $\Lambda^n V^*$, equality of these two multiples of $\mathrm{vol}$ forces equality of the scalar coefficients: $\langle\alpha,\eta\rangle = \langle\alpha',\eta\rangle$, hence $\langle\alpha - \alpha', \eta\rangle = 0$, for all $\eta$ (using bilinearity of $\langle\cdot,\cdot\rangle$ in its first slot). By non-degeneracy of $\langle\cdot,\cdot\rangle$ on $\Lambda^{n-k}V^*$ (Step 0(b)), this forces $\alpha - \alpha' = 0$, that is $\alpha = \alpha'$. (This is the same conclusion already delivered by the uniqueness clause of Lemma 1; we spell it out to show it is exactly non-degeneracy read in the reverse direction.) Thus $\star\omega$ is uniquely determined by $\omega$.
>
> **Step 4 — linearity of $\omega \mapsto \star\omega$.** Let $\omega_1, \omega_2 \in \Lambda^k V^*$ and $a_1, a_2 \in \mathbb{R}$. Because the exterior product is linear in its first argument ([[Thm - Wedge Product Properties|wedge product properties]]) and the coefficient map $c$ of Lemma 2 is linear, for every $\eta \in \Lambda^{n-k}V^*$,
> $$T_{a_1\omega_1 + a_2\omega_2}(\eta) = \frac{(a_1\omega_1 + a_2\omega_2)\wedge\eta}{\mathrm{vol}} = a_1\frac{\omega_1\wedge\eta}{\mathrm{vol}} + a_2\frac{\omega_2\wedge\eta}{\mathrm{vol}} = a_1 T_{\omega_1}(\eta) + a_2 T_{\omega_2}(\eta).$$
> Therefore, for all $\eta$,
> $$\langle \star(a_1\omega_1 + a_2\omega_2),\, \eta\rangle = T_{a_1\omega_1 + a_2\omega_2}(\eta) = a_1 T_{\omega_1}(\eta) + a_2 T_{\omega_2}(\eta) = a_1\langle\star\omega_1, \eta\rangle + a_2\langle\star\omega_2, \eta\rangle = \langle a_1\star\omega_1 + a_2\star\omega_2,\, \eta\rangle,$$
> where the first and third equalities are the defining relation of $\star$ from Step 2 (applied to $a_1\omega_1 + a_2\omega_2$, and to $\omega_1, \omega_2$ respectively) and the last uses bilinearity of $\langle\cdot,\cdot\rangle$. Both $\star(a_1\omega_1 + a_2\omega_2)$ and $a_1\star\omega_1 + a_2\star\omega_2$ therefore represent the same functional $T_{a_1\omega_1 + a_2\omega_2}$, so by the uniqueness established in Step 3 they are equal:
> $$\star(a_1\omega_1 + a_2\omega_2) = a_1\star\omega_1 + a_2\star\omega_2.$$
> Hence $\star : \Lambda^k V^* \to \Lambda^{n-k}V^*$ is $\mathbb{R}$-linear.
>
> **Conclusion.** For every $\omega \in \Lambda^k V^*$ there exists a unique $\star\omega \in \Lambda^{n-k}V^*$ satisfying $\omega\wedge\eta = \langle\star\omega,\eta\rangle\,\mathrm{vol}$ for all $\eta$ (Steps 2 and 3), and the map $\omega \mapsto \star\omega$ is linear (Step 4). Therefore the Hodge star operator exists and is unique. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Musical isomorphisms as the degree-one case.** On a semi-Riemannian vector space, the flat map $\flat : V \to V^*$, $v \mapsto \langle v, \cdot\rangle$, and its inverse the sharp map $\sharp$, are exactly Lemma 1 applied with $W = V$ and $b = \langle\cdot,\cdot\rangle$. Reprove that $\flat$ is an isomorphism in Lorentzian signature — where it is not an isometry but is still bijective — and identify how $\star$ on $\Lambda^{n-1}$ combines with $\sharp$ to send a top-codimension form to a vector. The theorem applies because $V$ with a non-degenerate metric is precisely the hypothesis of Lemma 1; the point that is non-obvious to students is that indefiniteness does not obstruct the isomorphism, only the metric's positivity.

**Poincaré duality by a perfect pairing.** On a closed oriented $n$-manifold, cup product gives a pairing $H^k(M;\mathbb{R}) \times H^{n-k}(M;\mathbb{R}) \to H^n(M;\mathbb{R}) \cong \mathbb{R}$. Show that this pairing is perfect and conclude $H^k \cong (H^{n-k})^*$, mirroring the structure of the present proof (a bilinear map into a one-dimensional space, made into an isomorphism). The Hodge-star theorem is the pointwise, linear-algebraic prototype of this global statement, and the exercise makes the analogy precise; it is non-obvious because the manifold version needs Stokes' theorem and Hodge theory to supply the non-degeneracy that the linear-algebra version gets for free from $\langle\cdot,\cdot\rangle$.

**Adjoints from non-degenerate pairings in indefinite spaces.** In a Krein space or a space with an indefinite metric (as in relativistic quantum mechanics, where the Minkowski or Gupta–Bleuler inner product is indefinite), the adjoint of an operator is defined by $\langle Tv, w\rangle = \langle v, T^\dagger w\rangle$. Prove that $T^\dagger$ exists and is unique for every $T$ on a finite-dimensional indefinite inner-product space, using Lemma 1 in place of the usual positive-definite Riesz argument. The relevance is that the existence of the adjoint is the same representation statement as the existence of $\star$; the non-obvious part is that the standard textbook proof, which quotes the definite Riesz theorem, must be replaced by the non-degenerate version proved here.

---

# Bridges

- **The previous page supplies the non-degeneracy this proof consumes.** [[Thm - The Induced Inner Product and Volume Form are Well-Defined|The induced inner product and volume form are well-defined]] proves three things: the induced form does not depend on the generalized orthonormal basis; the wedge monomials form a generalized orthonormal basis of $\Lambda^k V^*$ so the induced form is non-degenerate; and $\Lambda^n V^*$ is one-dimensional with $\langle\mathrm{vol},\mathrm{vol}\rangle = (-1)^p$. The present theorem uses exactly the second and third of these — non-degeneracy of the induced form (Step 0(b)) and one-dimensionality of $\Lambda^n V^*$ (Step 0(a)) — and nothing else about the metric. This is why the existence and uniqueness of $\star$ are logically prior to, and independent of, all of its properties.

- **The definite Riesz theorem is a special case of Lemma 1.** The vault's [[Thm - Riesz Representation Theorem (Finite-Dimensional)|Riesz representation theorem]] proves the representation statement for positive-definite inner products (and, over $\mathbb{C}$, up to conjugation). Lemma 1 here drops positivity and keeps only non-degeneracy, which is the property actually used; the definite theorem is recovered by observing that a positive-definite form is in particular non-degenerate. The construction of the adjoint operator on an ordinary inner-product space and the construction of $\star$ on a semi-Riemannian one are then the *same* representation argument, differing only in whether positivity is available.

- **The next page turns this abstract map into a computable operator.** [[Def - Hodge Star in Arbitrary Signature|The Hodge star in arbitrary signature]] takes the existence and uniqueness proved here as a black box and computes $\star$ on basis monomials, producing the explicit star table on Euclidean $\mathbb{R}^3$ and Minkowski space; the properties page [[Thm - Properties of the Hodge Star in Arbitrary Signature|properties of the Hodge star]] then derives $\star\star = (-1)^{k(n-k)+p}$ and the pairing identities. Every one of those computations presupposes that "$\star\omega$" denotes a single well-defined form, which is precisely what this theorem guarantees.

---

# Unlocked by This

> [!tip] The Codifferential and the L2 Adjoint of d *(from Hodge Theory)*
> Once $\star$ exists fibrewise on an oriented semi-Riemannian manifold, the codifferential $\delta = \pm\star d\star$ and the $L^2$ inner product $\langle\!\langle\alpha,\beta\rangle\!\rangle = \int_M \alpha\wedge\star\beta$ can be defined, and integration by parts shows $\delta$ is the formal adjoint of $d$. See [[Def - The Codifferential]] and [[Thm - Codifferential is the Adjoint of d]] for the Riemannian version, and §7.2–7.4 of this chapter for the arbitrary-signature use in electrodynamics and Yang–Mills theory.

> [!tip] Self-Dual and Anti-Self-Dual 2-Forms *(from Four-Dimensional Gauge Theory)*
> In dimension $4$ and index $0$, the operator $\star$ produced here restricts to an involution on $\Lambda^2$, whose $\pm 1$ eigenspaces give the self-dual/anti-self-dual decomposition underlying instantons. See [[Thm - Self-Dual Decomposition of 2-Forms in Four Dimensions]] and [[Def - Self-Dual and Anti-Self-Dual Forms]].
