---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Pullback of a Covariant Tensor Field"
  - "Def - Tensor Field on a Manifold"
  - "Def - Smooth Map between Manifolds"
tags: [geometry, differential-geometry, pullback, functoriality]
---

# Notation

$F : M \to N$ is a smooth map of smooth manifolds; $G : N \to P$ another smooth map. $A, B$ are smooth covariant tensor fields on $N$ (of any rank). $f \in C^\infty(N)$ is a smooth function. $F^*$ denotes the [[Def - Pullback of a Covariant Tensor Field|pullback]] operation. Full notation registry: [[Differential Geometry VII — Tensors and Tensor Fields]].

---

# Statement

> **Theorem (Functoriality of Pullback).** Let $F : M \to N$ and $G : N \to P$ be smooth maps, $A \in \mathcal{T}^k(N)$ and $B \in \mathcal{T}^\ell(N)$ smooth covariant tensor fields, and $f \in C^\infty(N)$. The pullback operation satisfies:
>
> 1. **$\mathbb{R}$-linearity:** $F^*(aA + bA') = a F^*A + b F^*A'$ for $a, b \in \mathbb{R}, A, A' \in \mathcal{T}^k(N)$.
>
> 2. **Tensor product:** $F^*(A \otimes B) = F^*A \otimes F^*B$.
>
> 3. **Function:** $F^*(fB) = (f \circ F)\, F^*B$, and $F^*f = f \circ F$ for $f \in C^\infty(N) = \mathcal{T}^0(N)$.
>
> 4. **Functoriality (chain rule):** $(G \circ F)^* = F^* \circ G^*$.
>
> 5. **Identity:** $(\mathrm{id}_N)^*B = B$.
>
> 6. **Smoothness:** if $B$ is smooth, so is $F^*B$.

---

# Motivation

The motivation is to **certify pullback as a well-behaved functor**: it respects the entire algebraic structure on covariant tensor fields (sums, tensor products, scalar multiplication by functions), and it composes correctly under composition of smooth maps (reversing arrows, as a contravariant functor should).

Why does this matter? Because every concrete computation with pullback proceeds by applying these properties recursively until one reaches the base cases (pullback of a function, pullback of a 1-form). For instance:

- To compute $F^*(g)$ for a metric $g = g_{ij}(y)\, dy^i \otimes dy^j$, apply (3) to get $(g_{ij} \circ F)\, F^*(dy^i \otimes dy^j)$, then (2) to get $(g_{ij}\circ F)\, F^*dy^i \otimes F^*dy^j$, then the 1-form pullback identity $F^*dy^i = dF^i$ to get $(g_{ij}\circ F)\, dF^i \otimes dF^j$. The recursion terminates because every higher-rank tensor is built from functions and 1-forms by tensor products.

- To compute the pullback under a composed map $G \circ F$, apply (4) to break it into two pullbacks $F^* \circ G^*$, then handle each. This is the change-of-variables principle: working in coordinates is pulling back to a chart in $\mathbb{R}^n$, and the composition of two chart changes is the composition of two pullbacks.

The properties also serve as a **consistency check on the definition**. If pullback were defined badly — say, with a wrong sign or a missing Jacobian factor — these properties would fail, and the failure would be immediately diagnosable. The simultaneous satisfaction of all six properties is what makes pullback the "right" operation.

A meta-point: functoriality is *the* generalization of "well-behaved" in modern mathematics. A construction that is functorial in its inputs respects composition, identity, and (if it is a bifunctor) several variables, and these are exactly the properties that make it deployable in proofs. Pullback's functoriality is what makes it useful in the proofs of [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|Stokes's theorem]] and the change-of-variables formula.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem applies whenever you want to compute or manipulate a pullback of a complex tensor field. Each property has a typical source pattern.

**Computing pullback by recursion on tensor type.** Given a covariant tensor field, decompose it into a function times a tensor product of 1-forms (in coordinates), then apply (3) and (2). The 1-form pullback is then handled by the rule $F^*dy^i = dF^i$ from [[Def - Pullback of a Covector Field]], which is the base case. This recursive procedure is the standard recipe for any pullback computation.

**Verifying that a pullback formula in coordinates is correct.** Given a candidate formula, check (1), (2), (3), (4) on the formula in turn. If any fails, the formula is wrong.

**Establishing chain-rule identities.** Property (4) is the manifold-level chain rule: it converts a composed-map computation into two simpler pullback computations. Whenever you want to pull back via a composition, decompose it.

**Targets (Output Amplification)**

**Pullback computations become recursive.** Once the properties are established, pullback of any covariant tensor field reduces (via (3), (2)) to pullback of functions and 1-forms — both of which have explicit formulas. So a pullback computation that looks complex is just a recursion that terminates in base cases.

**The pullback functor.** Properties (4) and (5) make $F^*$ a contravariant functor $\mathcal{T}^\bullet(N) \to \mathcal{T}^\bullet(M)$. This functorial structure is the prerequisite for the manifold-level theory of integration: $\int_M F^*\omega$ is defined via pullback, and the change-of-variables formula $\int_M F^*\omega = \int_N \omega$ (when $F$ is a diffeomorphism) is the integral-level expression of functoriality.

**Pullback commutes with the exterior derivative on differential forms.** A deeper functoriality, proved in [[Differential Geometry VIII — Differential Forms]]: $F^*d = dF^*$. This is *not* a consequence of (1)–(6) alone — it requires that $d$ behave well under coordinate change — but the properties (1)–(6) are the prerequisite for stating it cleanly.

---

# Why Is It True

The intuition is **pullback is precomposition with the differential $dF_p$ at each point, and precomposition respects all the algebraic operations**.

**One-line mechanism: pullback evaluates a tensor field on $N$ on vectors *that have been pushed forward by $dF_p$*, and the pushforward is linear in each input — so all the algebraic operations on tensor fields commute with the precomposition.**

Concretely:

For (1) ($\mathbb{R}$-linearity), use the definition: $(F^*(aA + bA'))_p(v_1, \dots) = (aA + bA')_{F(p)}(dF_p v_1, \dots) = aA_{F(p)}(dF v_1, \dots) + bA'_{F(p)}(dF v_1, \dots) = a(F^*A)_p + b(F^*A')_p$ — by linearity of the operations on covariant tensors at the point.

For (2) (tensor product), the definition of the tensor product $(A \otimes B)$ at a point is $A_p \otimes B_p$ pointwise. Substituting $dF v_1, \dots$ into $A_p \otimes B_p$ gives the tensor product of the two evaluations $A_{F(p)}(dF v_1, \dots) \cdot B_{F(p)}(dF w_1, \dots)$, which is the tensor product of the pullbacks.

For (3), $(F^*(fB))_p = (fB)_{F(p)}(dF v_1, \dots) = f(F(p))\, B_{F(p)}(dF v_1, \dots) = (f \circ F)(p)\, (F^*B)_p$ — by the scalar-multiplication action on tensors.

For (4), apply the chain rule for differentials: $d(G \circ F)_p = dG_{F(p)} \circ dF_p$. Then $((G \circ F)^*B)_p(v_1, \dots) = B_{G(F(p))}(d(G\circ F)_p v_1, \dots) = B_{G(F(p))}(dG_{F(p)}\,dF_p v_1, \dots) = (G^*B)_{F(p)}(dF_p v_1, \dots) = F^*(G^*B)_p(v_1, \dots)$.

For (5), $d(\mathrm{id}_N)_p = \mathrm{id}_{T_pN}$, so $((\mathrm{id}_N)^*B)_p = B_p$.

For (6), smoothness is automatic: pullback of a smooth tensor field by a smooth map is smooth because all the ingredients are smooth and pullback is the composition of smooth operations.

The whole theorem is a **direct application of the definition**, leveraging the linearity and chain-rule properties of $dF_p$. There is no deeper content beyond the definition itself; what makes the theorem useful is that the six properties together are *sufficient* to determine $F^*$ on every covariant tensor field — they reduce the problem to base cases.

---

# What Makes This Hard

The properties are all straightforward to verify individually, but the theorem is *unified* in that all six together imply pullback is the unique functor with the given values on functions and 1-forms. The non-obvious part is realizing that pullback is not just an ad hoc collection of formulas but the *unique* extension of the function-pullback and 1-form-pullback to all covariant tensor fields. The properties enforce this uniqueness.

A subtle point: the converse — that any operation satisfying (1)–(5) and agreeing with $F^*f = f \circ F$ on functions and $F^*\omega = dF^*\omega$ on 1-forms equals the pullback — requires verifying that these data determine pullback on all higher-rank tensor fields. This follows because every covariant tensor field is a $C^\infty(N)$-linear combination of tensor products of 1-forms, and (1)–(3) handle these combinations.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Each property is a direct unwinding of the pullback definition, using the linearity of the differential $dF_p$ and the algebraic structure on covariant tensors at the point. The chain rule property (4) uses the chain rule for differentials of compositions.

**Subgoal decomposition:**

1. **Linearity in tensor argument.** Show $F^*(aA + bA') = a F^*A + b F^*A'$.
   - *Hint:* Unpack the definition; use the linearity of $A_p$ at each point.
   - *Why needed:* Establishes pullback as $\mathbb{R}$-linear.

2. **Tensor product.** Show $F^*(A \otimes B) = F^*A \otimes F^*B$.
   - *Hint:* Apply the definition to $A \otimes B$ at a point, using the pointwise definition of tensor product on tensor spaces.
   - *Why needed:* This is the key algebraic compatibility — pullback respects the tensor product structure.

3. **Function compatibility.** Show $F^*(fB) = (f \circ F)\, F^*B$.
   - *Hint:* Scalar multiplication on tensors is the special case of tensor product where one factor is a $(0, 0)$-tensor (a function).
   - *Why needed:* This handles the $C^\infty(M)$-module structure.

4. **Chain rule.** Show $(G \circ F)^* = F^* \circ G^*$.
   - *Hint:* The differential of a composition is the composition of differentials: $d(G \circ F)_p = dG_{F(p)} \circ dF_p$. Apply this in the definition.
   - *Why needed:* This is the functoriality, the heart of the theorem.

5. **Identity.** Show $(\mathrm{id}_N)^*B = B$.
   - *Hint:* The differential of the identity is the identity, so precomposition with the identity is the identity.
   - *Why needed:* Required for functoriality (a functor sends identities to identities).

6. **Smoothness preservation.** Show $F^*B$ is smooth if $F, B$ are smooth.
   - *Hint:* In coordinates, $F^*B$'s components are smooth combinations of $B$'s components composed with $F$ and the Jacobian of $F$ — all smooth ingredients.
   - *Why needed:* Without this, pullback would only produce continuous tensor fields, not smooth ones.

---

# Lemma Decomposition

> [!note]- Lemma 1: $F^*$ is $\mathbb{R}$-linear in tensor argument
> **Statement:** $F^*(aA + bA') = a F^*A + b F^*A'$.
>
> **Hint:** Apply the definition at a point, using linearity of $A_p$ on the right.
>
> **Why needed:** Foundational property for any tensor operation.
>
> > [!note]- Full proof
> > At any $p \in M$ and any $v_1, \dots, v_k \in T_pM$,
> > $$(F^*(aA + bA'))_p(v_1, \dots, v_k) = (aA + bA')_{F(p)}(dF_p v_1, \dots, dF_p v_k) = a A_{F(p)}(\dots) + b A'_{F(p)}(\dots),$$
> > by the linearity of pointwise evaluation on tensors. Recognizing the right side as $a (F^*A)_p(\dots) + b (F^*A')_p(\dots)$ completes the proof. $\blacksquare$

> [!note]- Lemma 2: $F^*$ respects tensor product
> **Statement:** $F^*(A \otimes B) = F^*A \otimes F^*B$.
>
> **Hint:** At a point, $(A \otimes B)_p = A_p \otimes B_p$ (pointwise tensor product). Evaluate on vectors $v_1, \dots, v_{k+\ell}$.
>
> **Why needed:** This is the key compatibility property of pullback with the algebraic structure.
>
> > [!note]- Full proof
> > For $A \in \mathcal{T}^k(N)$, $B \in \mathcal{T}^\ell(N)$, $v_1, \dots, v_{k+\ell} \in T_pM$:
> > $$(F^*(A \otimes B))_p(v_1, \dots, v_{k+\ell}) = (A \otimes B)_{F(p)}(dF_p v_1, \dots, dF_p v_{k+\ell})$$
> > $$= A_{F(p)}(dF_p v_1, \dots, dF_p v_k) \cdot B_{F(p)}(dF_p v_{k+1}, \dots, dF_p v_{k+\ell})$$
> > $$= (F^*A)_p(v_1, \dots, v_k) \cdot (F^*B)_p(v_{k+1}, \dots, v_{k+\ell})$$
> > $$= (F^*A \otimes F^*B)_p(v_1, \dots, v_{k+\ell}). \blacksquare$$

> [!note]- Lemma 3: Chain rule for pullback
> **Statement:** $(G \circ F)^* = F^* \circ G^*$ as operations on covariant tensor fields.
>
> **Hint:** Use the chain rule for differentials: $d(G \circ F)_p = dG_{F(p)} \circ dF_p$.
>
> **Why needed:** This is functoriality, the central compatibility property.
>
> > [!note]- Full proof
> > For any covariant $k$-tensor field $B$ on $P$, any $p \in M$, and any $v_1, \dots, v_k \in T_pM$:
> > $$((G \circ F)^*B)_p(v_1, \dots, v_k) = B_{(G \circ F)(p)}(d(G \circ F)_p v_1, \dots, d(G \circ F)_p v_k).$$
> > By the chain rule for differentials, $d(G \circ F)_p = dG_{F(p)} \circ dF_p$, so $d(G \circ F)_p v_i = dG_{F(p)}(dF_p v_i)$. Substituting:
> > $$= B_{G(F(p))}(dG_{F(p)}(dF_p v_1), \dots, dG_{F(p)}(dF_p v_k)) = (G^*B)_{F(p)}(dF_p v_1, \dots, dF_p v_k) = (F^*(G^*B))_p(v_1, \dots, v_k). \blacksquare$$

> [!note]- Lemma 4: Pullback preserves smoothness
> **Statement:** If $F$ and $B$ are smooth, then $F^*B$ is a smooth tensor field on $M$.
>
> **Hint:** Work in coordinates. The components of $F^*B$ are smooth combinations of $B$'s components evaluated at $F(x)$ and the partial derivatives of $F$.
>
> **Why needed:** Smoothness preservation is what makes pullback a well-defined operation on the category of *smooth* tensor fields.
>
> > [!note]- Full proof
> > In a chart on $M$ and a chart on $N$ with $F$ given by coordinate functions $F^i(x)$, the components of $F^*B$ are
> > $$(F^*B)_{a_1\cdots a_k}(x) = B_{i_1\cdots i_k}(F(x))\, \frac{\partial F^{i_1}}{\partial x^{a_1}}\cdots\frac{\partial F^{i_k}}{\partial x^{a_k}}.$$
> > Each factor is smooth: $B_{i_1\cdots i_k}$ is smooth on its chart, $F$ is smooth (so $B_{i_1\cdots i_k} \circ F$ is smooth), and the partial derivatives of the coordinate functions of $F$ are smooth. Products and compositions of smooth functions are smooth. So the components $(F^*B)_{a_1\cdots a_k}(x)$ are smooth, hence $F^*B$ is a smooth tensor field. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Pullback $F^*$ satisfies properties (1)–(6).
>
> *Proof of (1).* See Lemma 1.
>
> *Proof of (2).* See Lemma 2.
>
> *Proof of (3).* The function-pullback property is the special case of (2) with $f$ as a $(0, 0)$-tensor (a function): $F^*(fB) = F^*(f) \otimes F^*(B) = (f \circ F) \otimes F^*B$. Now $f \circ F$ is a function (a $(0, 0)$-tensor on $M$), and tensor product with a $(0, 0)$-tensor is scalar multiplication: $(f \circ F) \otimes F^*B = (f \circ F)\, F^*B$. Combining, $F^*(fB) = (f \circ F)\, F^*B$.
>
> *Proof of (4).* See Lemma 3.
>
> *Proof of (5).* For $\mathrm{id}_N : N \to N$, the differential is $d(\mathrm{id}_N)_p = \mathrm{id}_{T_pN}$ at every $p$. So $(F^*B)_p = B_p((\mathrm{id})v_1, \dots, (\mathrm{id})v_k) = B_p(v_1, \dots, v_k)$, hence $(\mathrm{id}_N)^*B = B$.
>
> *Proof of (6).* See Lemma 4. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian geometry: the induced metric on a submanifold and isometries.** For an embedded submanifold $M \hookrightarrow N$ with metric $g$ on $N$, the induced metric is $F^*g$. The chain rule (4) means: if $M' \hookrightarrow M \hookrightarrow N$ is a chain of submanifolds, the induced metric on $M'$ is *either* the induced metric of $M$'s induced metric, *or* the induced metric of $N$'s metric directly — by (4) they agree. This is the "transitivity of induced metric" property, used constantly when studying submanifolds of submanifolds (e.g., curves on surfaces in $\mathbb{R}^3$).

**Special relativity: Lorentz invariance of the metric in any inertial frame.** The Minkowski metric $\eta$ is invariant under Lorentz transformations $\Lambda : \mathbb{R}^4 \to \mathbb{R}^4$: $\Lambda^*\eta = \eta$. This says that the metric, viewed as a covariant tensor field, is *Lorentz-invariant*. The chain rule (4) ensures consistency: a composition of two Lorentz transformations gives another Lorentz transformation, and the pullback of $\eta$ remains $\eta$.

**General relativity: pullback of stress-energy under a diffeomorphism.** Under a diffeomorphism $\phi : M \to M$ of a spacetime $(M, g)$, the metric $\phi^*g$ is another metric. If we want to formulate diffeomorphism-invariant physics, we ask that all physical quantities transform by pullback consistently. The chain rule (4) is what makes "general covariance" consistent: composition of diffeomorphisms is again a diffeomorphism, and the relationships between tensor fields are preserved.

**Symplectic geometry: pullback under a canonical transformation.** A *symplectomorphism* $\phi : M \to M$ of a symplectic manifold satisfies $\phi^*\omega = \omega$. The theorem ensures that the algebra of pullback operations is consistent: composition of symplectomorphisms is again a symplectomorphism (chain rule), and tensor products and scalar multiplications by Hamiltonians transform consistently.

---

# Bridges

- **Pullback of differential forms.** The wedge product $\omega \wedge \eta$ is a particular alternation of $\omega \otimes \eta$. By property (2), $F^*(\omega \otimes \eta) = F^*\omega \otimes F^*\eta$, and alternation is a linear operation that commutes with pullback (in the sense that $\mathrm{Alt}(F^*A) = F^*(\mathrm{Alt}\, A)$ for alternation-projector applied first). So $F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$. This is the same theorem read for forms; see [[Differential Geometry VIII — Differential Forms]].

- **Pullback commutes with the exterior derivative on forms.** $F^*d = dF^*$ — a deeper functoriality, **not** a consequence of (1)–(6) alone. It requires the additional fact that $F$ is smooth and the exterior derivative is natural under chart change. Combined with (1)–(6), it makes the pullback a *cochain map* of de Rham complexes, hence induces a map on cohomology.

- **The category-theoretic statement.** $F^*$ is a contravariant functor from "tensor fields on $N$" to "tensor fields on $M$", with the tensor product as a monoidal structure. Property (4) says $F^*$ is functorial (composition); property (5) says it preserves identities; (1)–(3) say it preserves the linear, multilinear, and module structure. The theorem certifies pullback as a *monoidal contravariant functor*, the strongest functorial statement one could ask for.

- **The change-of-variables formula for integration.** If $F : M \to N$ is an orientation-preserving diffeomorphism and $\omega$ is a top form on $N$, then $\int_M F^*\omega = \int_N \omega$. The proof uses property (4) to reduce to a single chart, then property (3) and the standard change-of-variables formula in $\mathbb{R}^n$. The whole proof of the change-of-variables formula on manifolds is a careful application of this theorem's properties.

---

# Unlocked by This

> [!tip] Pullback of Differential Forms *(from [[Differential Geometry VIII — Differential Forms]])*
> The properties (1)–(6) apply to differential forms, with the wedge product replacing the tensor product. In particular, $F^*(\omega \wedge \eta) = F^*\omega \wedge F^*\eta$. The exterior derivative commutes with pullback ($F^*d = dF^*$) — a deeper functoriality not implied by (1)–(6) alone. These two together make pullback the standard tool of differential forms calculus on manifolds.

> [!tip] Integration on Manifolds and the Change-of-Variables Formula *(from [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]])*
> The integral $\int_M \omega$ of a top form on an oriented manifold is *defined* using pullback to a chart. The properties (1)–(6) ensure the definition is independent of the choice of chart (different charts give different pullbacks, but the integrals agree by property (4) and the standard change-of-variables formula). Stokes's theorem $\int_M d\omega = \int_{\partial M} \omega|_{\partial M}$ then uses the chain rule for boundary maps to relate the integrals on $M$ and $\partial M$.

> [!tip] The de Rham Complex and Cohomology *(from [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]])*
> The exterior derivative satisfies $d^2 = 0$, making $(\Omega^\bullet(M), d)$ a cochain complex. By the deeper functoriality $F^*d = dF^*$, pullback is a cochain map of de Rham complexes, hence induces a map on cohomology $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$. The de Rham theorem then identifies these with topological invariants (singular cohomology), and pullback respects the identification. This is the foundation of the algebraic-topological side of differential geometry.

> [!tip] Tensoriality of Constructions Built from Tensor Fields *(from Riemannian Geometry)*
> Whenever a construction on a manifold $N$ uses tensor fields and natural operations (sum, tensor product, contraction with the metric), the result is a tensor field, and it pulls back consistently along smooth maps. The properties (1)–(6) are the certificate that these constructions are *natural* in the categorical sense. This naturality is what makes general relativity's "tensorial" formulation work: physical laws are tensorial relations, and they pull back consistently under diffeomorphisms (general covariance).
