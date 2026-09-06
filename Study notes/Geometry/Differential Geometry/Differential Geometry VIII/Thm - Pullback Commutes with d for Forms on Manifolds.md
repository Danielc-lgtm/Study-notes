---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Exterior Derivative on a Manifold"
  - "Def - Pullback of a Differential Form on a Manifold"
  - "Def - Differential k-Form on a Manifold"
  - "Thm - Uniqueness of the Exterior Derivative"
tags: [geometry, differential-geometry]
---

# Notation

$F : M \to N$ is a smooth map between smooth manifolds. $\Omega^k(N), \Omega^k(M)$ are the spaces of smooth $k$-forms. $d : \Omega^k \to \Omega^{k+1}$ is the exterior derivative; $F^* : \Omega^k(N) \to \Omega^k(M)$ is the pullback of forms. The full registry is on [[Differential Geometry VIII — Differential Forms]].

---

# Statement

> **Theorem (Naturality of $d$, Lee Proposition 14.26).** Let $F : M \to N$ be a smooth map between smooth manifolds. For every smooth $k$-form $\omega \in \Omega^k(N)$,
> $$F^*(d\omega) = d(F^*\omega).$$
> Equivalently, the diagram
> $$\Omega^k(N) \xrightarrow{d} \Omega^{k+1}(N), \qquad \Omega^k(M) \xrightarrow{d} \Omega^{k+1}(M)$$
> commutes when connected by $F^* : \Omega^\bullet(N) \to \Omega^\bullet(M)$ on both sides.

> **Corollary (functoriality of de Rham cohomology).** The pullback $F^*$ induces a well-defined linear map $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$ on de Rham cohomology. Composition is contravariant: $(F \circ G)^* = G^* \circ F^*$ on cohomology.

> **Corollary (chart-independence of $d$).** Two coordinate charts $\varphi : U \to \mathbb{R}^n$ and $\psi : V \to \mathbb{R}^n$ on $M$ that overlap give the same value of $d\omega$ at points of $U \cap V$. (This is the well-definedness of $d$ as a global operator on $M$, derived from naturality.)

---

# Motivation

The theorem says the exterior derivative is **intrinsic**: it does not depend on a chart, on a metric, on any auxiliary structure, only on the smooth structure of the manifold. The pullback $F^*$ is the universal way to compare forms on different manifolds; the commutation $F^* d = d F^*$ says $d$ is preserved by this comparison. The four-word description is "$d$ is natural".

The reason this matters in practice: it lets one *commute* $d$ and $F^*$ in any computation. The pullback is mechanical (substitute and apply chain rule); the exterior derivative is also mechanical (differentiate coefficients and wedge on $dx^j$); doing them in different orders sometimes simplifies a computation dramatically. Without the commutation, every change of variables or evaluation of a form on a parametrized submanifold would require re-doing the exterior derivative computation in the new coordinates.

The theorem is also what makes de Rham cohomology a *functor*. Without naturality, $F^*$ would not respect closedness and exactness, and the induced map on $H^k_{dR}$ would be ill-defined. With naturality, $H^k_{dR}$ becomes a contravariant functor from smooth manifolds to vector spaces — the calculus engine of algebraic topology.

There is also a deep reason naturality holds: the exterior derivative is *uniquely characterized* by its algebraic properties (linearity, agreement with $df$ on functions, graded Leibniz, $d^2 = 0$). The pullback $F^*$ commutes with all four of these, so the operator $F^* \circ d : \Omega^k(N) \to \Omega^{k+1}(M)$, when traced through the uniqueness, must equal $d \circ F^*$. This is the slick proof.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis "$F$ is a smooth map" is bare. The skill is recognizing the variety of computations that secretly invoke pullback.

The first disguised source is **a change of coordinates**. A coordinate change $\tilde x = F(x)$ on a manifold *is* a pullback along the inverse transition map. So computing the exterior derivative in new coordinates is the same as pulling back the exterior derivative computed in old coordinates. Naturality lets one choose the cheaper side.

The second disguised source is **integration over a parametrized submanifold**. To compute $\int_\Sigma\omega$ for a $k$-form $\omega$ on an ambient manifold $N$ and a parametrized $k$-submanifold $\Sigma$ given as the image of $F : M \to N$ (with $\dim M = k$), one pulls back $\omega$ along $F$ to a $k$-form on $M$, then integrates over $M$. The integration of $d\omega$ over $\Sigma$ similarly becomes integration of $F^*(d\omega) = d(F^*\omega)$ over $M$ — naturality lets one apply Stokes' theorem on $M$ instead of on $\Sigma$.

The third disguised source is **a frame change or gauge transformation**. In gauge theory, transforming a connection $A$ by a gauge transformation $g : M \to G$ involves pullbacks of forms on $G$ to $M$. The naturality of $d$ ensures that the transformed connection's curvature is computed by pullback of the original curvature plus a known correction — a routine application of $F^* d = d F^*$.

A fourth source is **reduction to local algebra generators**. Every form is locally a sum of terms $u\,dy^{j_1}\wedge\cdots\wedge dy^{j_k}$. Pullback respects products, and the chain rule proves naturality on $u$ and each $dy^j$; graded Leibniz then forces the identity on every local term.

**Targets (Output Amplification)**

The conclusion $F^*d = dF^*$ is a single algebraic identity, but combined with other facts it unlocks structural results.

The first target combination is **$F^*d = dF^*$ + the structure of $F^*$ as an algebra map = pullback induces a graded ring homomorphism on $H^\bullet_{dR}$**. The pullback respects wedge ($F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$) and commutes with $d$, so it descends to a graded ring homomorphism $F^* : H^\bullet_{dR}(N) \to H^\bullet_{dR}(M)$. This is the structural backbone of de Rham theory as a functor: cohomology has both a vector space structure and a ring structure, and pullback respects both.

The second target combination is **$F^*d = dF^*$ + the de Rham theorem = pullback computes the topological induced map**. By de Rham's theorem $H^k_{dR}(M) \cong H^k(M; \mathbb{R})$, and the pullback on de Rham cohomology corresponds, under the isomorphism, to the pullback on singular cohomology. So computing $F^*[\omega]$ for a smooth $\omega$ gives the topological induced map $F^* : H^k(N; \mathbb{R}) \to H^k(M; \mathbb{R})$ — a way to compute topological invariants using calculus.

The third target combination is **$F^*d = dF^*$ + Stokes' theorem = compatibility of integration with change of variables on manifolds**. Stokes' theorem $\int_M d\omega = \int_{\partial M}\omega$ combined with naturality gives $\int_M F^*(d\omega) = \int_M d(F^*\omega) = \int_{\partial M} F^*\omega = \int_{F(\partial M)}\omega$ (under appropriate orientation conventions). The change-of-variables formula for integration on manifolds is then a direct consequence of pullback + Stokes.

The fourth target combination is **$F^*d = dF^*$ + homotopy invariance = pullback by homotopic maps gives equal cohomology maps**. The deeper statement (proved using the Poincaré-lemma-style homotopy formula) is that if $F, G : M \to N$ are smoothly homotopic, then $F^* = G^*$ on $H^k_{dR}$. The proof constructs an explicit chain homotopy using the homotopy between $F$ and $G$; the naturality $F^*d = dF^*$ is what makes the chain homotopy actually work at the cohomology level.

---

# Why Is It True

**The one-line mechanism:** **forms are locally generated by functions and their differentials; pullback respects wedge products, and the ordinary chain rule says $F^*(df)=d(f\circ F)$.**

Choose charts with $F(U)\subseteq V$ and write
$$\omega=\sum_J'\omega_J(y)\,dy^{j_1}\wedge\cdots\wedge dy^{j_k}.$$
Then
$$F^*\omega=\sum_J'(\omega_J\circ F)\,dF^{j_1}\wedge\cdots\wedge dF^{j_k}.$$
Applying $d_M$, every term in which $d$ lands on $dF^{j_r}$ vanishes by $d^2F^{j_r}=0$, leaving
$$d_M(F^*\omega)=\sum_J'd(\omega_J\circ F)\wedge dF^{j_1}\wedge\cdots\wedge dF^{j_k}.$$
The chain rule gives $d(\omega_J\circ F)=F^*(d_N\omega_J)$, and pullback respects wedge products, so this is exactly $F^*(d_N\omega)$. The calculation is local but the two sides are global forms, hence equality on such chart neighborhoods proves equality everywhere.

When $F$ is a diffeomorphism, the same result can also be recovered by conjugating $d_N$ with the algebra isomorphism $F^*$ and applying uniqueness of the exterior derivative. For a general smooth map $F^*$ need not be injective or surjective, so the generator proof above is the correct argument.

---

# What Makes This Hard

The proof is local and algebraic, but the bookkeeping can hide its load-bearing identity: the ordinary chain rule $d(\omega_J\circ F)=F^*(d\omega_J)$. The common error in the coordinate proof is to forget that $dF^{j_i}$ is *already* the differential of a smooth function, and to attempt to apply $d$ to it twice without recognizing that $d^2(F^{j_i}) = 0$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Work on local generators $u\,dy^J$: pullback the coefficient and basis differentials, apply graded Leibniz, use the chain rule on $u\circ F$, and use $d^2F^j=0$ to eliminate derivatives of the pulled-back basis factors.

**Subgoal decomposition:**

1. **Verify $F^*(df) = d(F^*f)$ for functions $f \in C^\infty(N)$.**
   - *Hint:* This is the chain rule for the differential: $d(f \circ F)_p(v) = df_{F(p)}(dF_p(v))$.
   - *Why needed:* This is the base case; the general case propagates by Leibniz.

2. **Verify $F^*$ respects wedge products: $F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$.**
   - *Hint:* Direct from the pullback definition and the wedge definition.
   - *Why needed:* Combined with Subgoal 1 and graded Leibniz, propagates to general forms.

3. **Apply Leibniz: for $\omega = \omega_J\,dy^J$, expand both sides and verify they agree.**
   - *Hint:* Use the chain rule on $\omega_J \circ F$ and the fact that $d^2(F^j) = 0$.
   - *Why needed:* This is the inductive step from $0$-forms to general forms.

4. **Propagate by linearity to general forms.**
   - *Hint:* Every form is a sum of basic forms; both $F^*$ and $d$ are linear.
   - *Why needed:* Finishes the proof.

---

# Lemma Decomposition

> [!note]- Lemma 1: Pullback respects differential of functions ($k = 0$ case)
> **Statement:** For any smooth map $F : M \to N$ and any smooth function $f : N \to \mathbb{R}$,
> $$F^*(df) = d(F^*f) = d(f \circ F).$$
>
> **Hint:** This is exactly the chain rule: the differential of $f \circ F$ at $p$ is the composition $df_{F(p)} \circ dF_p$.
>
> **Why needed:** This is the base case of the inductive argument. Without it, the higher-degree cases have nothing to start from.
>
> > [!note]- Full proof
> > Both $F^*(df)$ and $d(F^*f)$ are $1$-forms on $M$. To show they are equal, evaluate on an arbitrary tangent vector $v \in T_pM$:
> > By the definition of pullback of a $1$-form,
> > $$(F^*(df))_p(v) = (df)_{F(p)}(dF_p(v)) = (dF_p(v))(f),$$
> > where the last equality uses that $df(w) = w(f)$ for a tangent vector $w$.
> >
> > On the other hand, $(d(F^*f))_p(v) = v(F^*f) = v(f \circ F)$. By the chain rule for tangent vectors, $v(f \circ F) = (dF_p(v))(f)$ — pushing $v$ forward by $dF$ to a vector at $F(p)$ and then evaluating $f$.
> >
> > So both sides equal $(dF_p(v))(f)$. Done.

> [!note]- Lemma 2: Pullback respects wedge products
> **Statement:** For smooth $F : M \to N$ and forms $\omega \in \Omega^k(N)$, $\eta \in \Omega^\ell(N)$,
> $$F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta.$$
>
> **Hint:** Evaluate both sides on tangent vectors and use the multilinearity and alternation properties of the wedge.
>
> **Why needed:** Combined with Lemma 1 and graded Leibniz, this propagates the naturality of $d$ from functions to all forms.
>
> > [!note]- Full proof
> > By definition, $(F^*(\omega \wedge \eta))_p(v_1, \dots, v_{k+\ell}) = (\omega \wedge \eta)_{F(p)}(dF_p(v_1), \dots, dF_p(v_{k+\ell}))$.
> >
> > The right side, using the formula $\omega \wedge \eta = \frac{(k+\ell)!}{k!\,\ell!}\operatorname{Alt}(\omega \otimes \eta)$:
> > $$= \frac{(k+\ell)!}{k!\,\ell!}\operatorname{Alt}(\omega \otimes \eta)_{F(p)}(dF_p(v_1), \dots, dF_p(v_{k+\ell})).$$
> > Expand the $\operatorname{Alt}$ as a sum over permutations; each summand is $\omega(dF\cdot v_{\sigma(1)}, \dots, dF\cdot v_{\sigma(k)}) \cdot \eta(dF\cdot v_{\sigma(k+1)}, \dots, dF\cdot v_{\sigma(k+\ell)})$, which equals $(F^*\omega)(v_{\sigma(1)}, \dots, v_{\sigma(k)}) \cdot (F^*\eta)(v_{\sigma(k+1)}, \dots, v_{\sigma(k+\ell)})$. Recombining gives $(F^*\omega \wedge F^*\eta)_p(v_1, \dots, v_{k+\ell})$ on the right.

> [!note]- Lemma 3: $F^* d_N = d_M F^*$ on basic forms $\omega = u\,dy^J$
> **Statement:** For a smooth function $u$ on $N$ and an increasing multi-index $J$ on $N$,
> $$F^*(d_N(u\,dy^J)) = d_M(F^*(u\,dy^J)).$$
>
> **Hint:** Compute both sides using the chart formulas plus Lemma 1 and Lemma 2; cancel the $d^2(F^{j_i}) = 0$ terms.
>
> **Why needed:** Inductive step propagating from $0$-forms to general forms in a chart.
>
> > [!note]- Full proof
> > $d_N(u\,dy^J) = du \wedge dy^J$ (since $d_N(dy^J) = 0$).
> >
> > Pullback: $F^*(du \wedge dy^J) = F^*(du) \wedge F^*(dy^J)$ by Lemma 2 $= d(F^*u) \wedge F^*(dy^J)$ by Lemma 1 $= d(u \circ F) \wedge dF^{j_1} \wedge \cdots \wedge dF^{j_k}$.
> >
> > On the other side: $F^*(u\,dy^J) = (u \circ F)\,dF^{j_1} \wedge \cdots \wedge dF^{j_k}$. Apply $d_M$, using graded Leibniz: $d_M((u\circ F)\,dF^{j_1} \wedge \cdots \wedge dF^{j_k}) = d(u \circ F) \wedge dF^{j_1} \wedge \cdots \wedge dF^{j_k} + (u\circ F) \wedge d(dF^{j_1} \wedge \cdots \wedge dF^{j_k})$. The second term is zero because $d_M(dF^{j_i}) = 0$ (Lemma 2 applied iteratively: $dF^{j_i}$ is the differential of a function, so $d(dF^{j_i}) = d^2(F^{j_i}) = 0$). The first term equals the pullback side computed above.

> [!note]- Lemma 4: $F^* d_N = d_M F^*$ on any form
> **Statement:** For any $\omega \in \Omega^k(N)$, $F^*(d_N\omega) = d_M(F^*\omega)$.
>
> **Hint:** In a chart, write $\omega$ as a sum of basic forms times functions, and apply Lemma 3 plus linearity.
>
> **Why needed:** Finishes the proof.
>
> > [!note]- Full proof
> > In a chart $(V, y^j)$ on $N$, $\omega = \sum'_J u_J\,dy^J$. Applying $F^*$ and $d_M$ to both sides and using the linearity of $F^*$ and $d$, plus Lemma 3 on each basic term, gives equality.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** $F^*(d_N\omega) = d_M(F^*\omega)$ for any smooth $F : M \to N$ and any $\omega \in \Omega^k(N)$.
>
> *Proof.*
>
In any chart $(V, y^j)$ on $N$ and $(U, x^i)$ on $M$ with $F(U) \subseteq V$, by linearity reduce to $\omega = u\,dy^J$ for a single increasing multi-index $J$. Then by Lemma 3,
> $$F^*(d_N(u\,dy^J)) = F^*(du \wedge dy^J) = F^*(du) \wedge F^*(dy^J) = d(u\circ F) \wedge dF^{j_1} \wedge \cdots \wedge dF^{j_k},$$
> $$d_M(F^*(u\,dy^J)) = d_M((u\circ F)\,dF^{j_1} \wedge \cdots \wedge dF^{j_k}) = d(u\circ F) \wedge dF^{j_1} \wedge \cdots \wedge dF^{j_k}.$$
> The two sides agree. Linearity propagates to all forms; chart-independence makes the identity global.
>
> $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Change of variables on Riemannian manifolds.** Given a Riemannian metric $g$ on $M$ and a diffeomorphism $F : M \to N$, the volume form transforms as $F^*(\text{vol}_h) = (\sqrt{\det g/h \circ F^{-1}})\,\text{vol}_g$ for the appropriate metrics. The compatibility with $d$ — naturality — is what makes the change of variables consistent across overlapping coordinate patches on an oriented manifold.

**Gauge transformations in Yang–Mills theory.** A gauge transformation $g : M \to G$ pulls back the Maurer–Cartan form on $G$ to a $\mathfrak{g}$-valued $1$-form on $M$, and the connection $A$ transforms by addition of this pullback. The curvature $F = dA + \tfrac12[A, A]$ then transforms as $F \mapsto g^{-1} F g$, with the naturality of $d$ underlying the computation $d(g^{-1}Ag) = g^{-1}(dA)g + \cdots$.

**Cohomology of fibre bundles.** For a fibre bundle $\pi : E \to B$ with fibre $F$, the pullback $\pi^* : H^k_{dR}(B) \to H^k_{dR}(E)$ is the start of the **Leray–Serre spectral sequence**, which computes $H^k_{dR}(E)$ from $H^k_{dR}(B)$ and $H^k_{dR}(F)$. The naturality of $d$ is what makes $\pi^*$ well-defined on cohomology, and is the starting input to the spectral sequence.

**Index theorems.** The Atiyah–Singer index theorem expresses the index of an elliptic operator on a compact manifold as an integral of a polynomial in the curvature of the underlying bundles. The naturality of $d$ (and the analogous naturality of covariant exterior derivatives) is what makes the index a topological invariant — pullbacks under [[Def - Diffeomorphism|diffeomorphisms]] preserve the index, with the integrand being a closed form.

---

# Bridges

- **[[Thm - Uniqueness of the Exterior Derivative]]** — The proof of naturality is dramatically cleaner via uniqueness: the four-axiom characterization of $d$ lets one identify $F^* \circ d$ with $d \circ F^*$ by showing both satisfy the axioms. This is the *modern* approach to naturality, replacing the coordinate-bashing of older texts.

- **[[Thm - Pullback Commutes with d for 1-Forms]]** in DG VI — The present theorem is the higher-degree generalization. The $k = 1$ case was proved separately in DG VI for $1$-forms (covector fields); the present version extends to all degrees, with the same mechanism (chain rule on functions, plus Leibniz to propagate).

- **[[Def - Pullback of a Differential Form on a Manifold]]** — The naturality of $d$ is what makes the pullback functor compatible with the differential. Combined with the algebra-homomorphism property ($F^*$ respects wedge), naturality makes $F^*$ a DGA homomorphism.

- **[[Thm - The General Stokes Theorem]]** — Stokes' theorem on a parametrized submanifold $F : M \to N$ becomes a statement about $\int_M F^*(d\omega) = \int_M d(F^*\omega) = \int_{\partial M}F^*\omega$. The naturality of $d$ is what makes the change-of-variables compatible with Stokes; without it, integration on a manifold via parametrizations would not have a consistent pullback formulation.

- **Maxwell's equations under coordinate change** — Under a change of coordinates on spacetime, the field strength $F$ pulls back to its expression in the new coordinates, and Maxwell's equations $dF = 0$, $d\star F = J$ transform compatibly because $d$ commutes with pullback. This is the source of "covariance" of Maxwell's equations under coordinate changes.

---

# Unlocked by This

> [!tip] de Rham Cohomology as a Contravariant Functor *(from Algebraic Topology)*
> Because $F^* d = d F^*$, the pullback $F^*$ sends closed forms to closed forms and exact forms to exact forms, so it descends to $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$. Combined with the algebra structure (pullback respects $\wedge$), this makes $H^\bullet_{dR}$ a contravariant functor from smooth manifolds to graded-commutative $\mathbb{R}$-algebras.

> [!tip] Homotopy Invariance of de Rham Cohomology *(from DG X)*
> If $F, G : M \to N$ are smoothly homotopic, then $F^* = G^*$ on $H^k_{dR}$. The proof constructs an explicit chain homotopy, and naturality is the starting input. This is the key technical step in proving the de Rham theorem (identifying $H^k_{dR}$ with singular cohomology) and in computing $H^k_{dR}$ of complicated spaces via cellular decompositions.

> [!tip] Pullback in Sheaf Cohomology *(from Algebraic Geometry)*
> The naturality of $d$ is the prototype for naturality of all sheaf-theoretic cohomology theories. For a morphism of schemes $f : X \to Y$, the pullback $f^*$ commutes with the differentials of the de Rham, Dolbeault, and crystalline cohomologies, making each one a contravariant functor and a topological invariant.

> [!tip] Equivariant Cohomology *(from Differential Geometry)*
> For a Lie group $G$ acting on a manifold $M$, the **equivariant de Rham cohomology** $H^k_G(M)$ is the cohomology of $G$-invariant forms; naturality of $d$ under the pullback by $G$-action is what makes invariant forms a subcomplex. The Cartan model and the Mathai–Quillen formalism build on this base structure.

> [!tip] Gauge Transformations *(from Gauge Theory / General Relativity)*
> Under a gauge transformation (or a diffeomorphism in GR), the connection $1$-form and curvature $2$-form transform by pullback, and the consistency of the transformation laws — including the Bianchi identity $d_A F = 0$ — uses the naturality of $d$ throughout. The gauge-invariance of physical quantities like the action $\int F \wedge \star F$ is what makes the theory well-defined.
