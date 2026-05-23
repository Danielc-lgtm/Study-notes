---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - The Tangent Space"
  - "Def - The Differential of a Smooth Map"
  - "Def - Direct Sum"
tags: [geometry, differential-geometry]
---

# Notation

$M_{1}, \dots, M_{k}$ are smooth manifolds. The product manifold $M = M_{1} \times \cdots \times M_{k}$ has dimension $\dim M = \sum \dim M_{i}$. The projection onto the $i$-th factor is $\pi_{i} : M \to M_{i}$, $\pi_{i}(p_{1}, \dots, p_{k}) = p_{i}$. The differential is $d(\pi_{i})_{p} : T_{p}M \to T_{p_{i}}M_{i}$. The direct sum of vector spaces is $V_{1} \oplus \cdots \oplus V_{k}$, see [[Def - Direct Sum]]. The full notation registry is on [[Differential Geometry III — Tangent Vectors and the Differential]].

---

# Statement

> **Theorem (Tangent Space of a Product Manifold).** Let $M_{1}, \dots, M_{k}$ be smooth manifolds and let $M = M_{1} \times \cdots \times M_{k}$ be their product manifold. For any point $p = (p_{1}, \dots, p_{k}) \in M$, the map
> $$\alpha : T_{p}M \to T_{p_{1}}M_{1} \oplus \cdots \oplus T_{p_{k}}M_{k}, \qquad \alpha(v) = (d(\pi_{1})_{p}(v), \dots, d(\pi_{k})_{p}(v))$$
> is a canonical vector-space isomorphism, where $\pi_{i} : M \to M_{i}$ is the projection onto the $i$-th factor.
>
> The same result holds if one of the $M_{i}$ is a smooth manifold with boundary.

> **Corollary 1 (Dimension).** $\dim T_{p}M = \sum_{i} \dim T_{p_{i}}M_{i} = \sum_{i} \dim M_{i} = \dim M$ — consistent with the dimension theorem.
>
> **Corollary 2 (Inverse).** The inverse of $\alpha$ sends a tuple $(v_{1}, \dots, v_{k})$ to the unique $v \in T_{p}M$ with $d(\pi_{i})_{p}(v) = v_{i}$ for all $i$. Explicitly, $v$ acts on a smooth function $f$ on $M$ by $v(f) = \sum_{i} v_{i}(f \circ \iota_{i,p})$, where $\iota_{i,p} : M_{i} \to M$ is the inclusion of the $i$-th factor fixing the other coordinates at $p_{j}$.
>
> **Corollary 3 (Global splitting).** The tangent bundle of a product manifold splits as $T(M_{1} \times M_{2}) \cong TM_{1} \oplus TM_{2}$ — but only over the base $M_{1} \times M_{2}$, not in a way that allows reduction to one factor.

---

# Motivation

The motivation is to compute tangent spaces of products of manifolds explicitly. This is needed everywhere: $\mathbb{R}^{n}$ is a product of $n$ copies of $\mathbb{R}$, the torus $T^{n}$ is a product of $n$ copies of $S^{1}$, the configuration space of $N$ particles in $\mathbb{R}^{3}$ is $(\mathbb{R}^{3})^{N}$, and the phase space of a Hamiltonian system is $T^{*}M$, which over a product base splits.

Without the theorem, computing tangent spaces of products would require building charts on the product manifold and verifying the tangent-space structure chart by chart — tedious and inelegant. With the theorem, tangent vectors on products split canonically into "components from each factor", and operations on products reduce to operations on each factor separately.

The result is also the foundational input for working with **product structures** in dynamical systems (separating variables, integrating Hamiltonian flows with conserved quantities), Lie group theory (the tangent space of a product Lie group is the direct sum of the tangent spaces of the factors, which gives the Lie algebra of the product as the direct sum of the factor Lie algebras), and physics (separating spatial and temporal components, or decomposing tensors).

---

# Sources and Targets

**Sources (Input Broadening).**

The first source is **a product manifold appearing in a problem**. Whenever a manifold $M$ is presented as $M_{1} \times M_{2}$ or some product, the theorem applies. The natural-isomorphism gives an explicit decomposition $T_{p}M = T_{p_{1}}M_{1} \oplus T_{p_{2}}M_{2}$ that respects the product structure.

The second source is **a Cartesian-product Lie group**. For Lie groups $G$ and $H$, the product $G \times H$ is a Lie group, and the tangent space at the identity $T_{(e,e)}(G \times H)$ is canonically $\mathfrak{g} \oplus \mathfrak{h}$ — the Lie algebra of the product is the direct sum of the Lie algebras. This is the basis for the structure theory of compact Lie groups (which split as products of simple Lie groups up to finite covers).

The third source is **a manifold with a product structure on a neighbourhood**. Even if $M$ is not globally a product, the theorem applies *locally*: if $p$ has a neighbourhood $U \cong U_{1} \times U_{2}$ via a diffeomorphism, then $T_{p}M = T_{p_{1}}U_{1} \oplus T_{p_{2}}U_{2}$ at that point. This is the local product structure used in foliations and integrable distributions, see [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]].

**Targets (Output Amplification).**

The conclusion is $T_{p}M \cong T_{p_{1}}M_{1} \oplus T_{p_{2}}M_{2}$ canonically. Combined with various properties:

Target 1: **combined with the differential of a separable function, tangent splits give chain-rule splits**. If $f : M_{1} \times M_{2} \to \mathbb{R}$ separates as $f(p_{1}, p_{2}) = g(p_{1}) + h(p_{2})$ for smooth $g$ and $h$, then $df_{p} = dg_{p_{1}} + dh_{p_{2}}$ where the right side acts on $T_{p}M \cong T_{p_{1}}M_{1} \oplus T_{p_{2}}M_{2}$ by acting on each summand. This is a separation of variables at the tangent level.

Target 2: **combined with the cotangent splitting, tangent splits give the cotangent splitting**. The cotangent space of a product also splits: $T^{*}_{p}M \cong T^{*}_{p_{1}}M_{1} \oplus T^{*}_{p_{2}}M_{2}$. This makes the cotangent bundle of a product manifold a direct sum of the factor cotangent bundles, foundational for Hamiltonian mechanics with multiple degrees of freedom.

Target 3: **combined with iteration, tangent splits give the structure of $\mathbb{R}^{n}$**. Iterating the theorem with each factor being $\mathbb{R}$, we get $T_{a}\mathbb{R}^{n} = \bigoplus_{i=1}^{n} T_{a^{i}}\mathbb{R} = \bigoplus_{i=1}^{n} \mathbb{R} = \mathbb{R}^{n}$ canonically. This recovers the canonical identification $T_{a}\mathbb{R}^{n} \cong \mathbb{R}^{n}$ from the product structure rather than from coordinates.

Target 4: **combined with Lie group products, tangent splits give Lie algebra structure**. For Lie groups $G$ and $H$, the Lie algebra $\mathfrak{g} \oplus \mathfrak{h}$ of the product is the direct sum of the factor Lie algebras, with bracket $[(X_{1}, Y_{1}), (X_{2}, Y_{2})] = ([X_{1}, X_{2}]_{\mathfrak{g}}, [Y_{1}, Y_{2}]_{\mathfrak{h}})$. The brackets on factors do not mix.

---

# Why Is It True

The reason is structural: **the product manifold's atlas is the product of the factor atlases**, and the tangent-space splitting is the linearization of this product structure.

**The bolded one-liner mechanism summary: the canonical projections $\pi_{i} : M_{1} \times M_{2} \to M_{i}$ together with the canonical inclusions $\iota_{i} : M_{i} \to M_{1} \times M_{2}$ (fixing the other coordinate) give a direct-sum decomposition of $T_{p}M$ via $\alpha = (d\pi_{1}, d\pi_{2})$ and its inverse via insertion of the components into the inclusions.**

Here is the picture. The product manifold $M_{1} \times M_{2}$ has charts that are products of charts: a chart on $M$ at $p = (p_{1}, p_{2})$ is built from a chart $(U_{1}, \varphi_{1})$ on $M_{1}$ at $p_{1}$ and a chart $(U_{2}, \varphi_{2})$ on $M_{2}$ at $p_{2}$, with chart $(U_{1} \times U_{2}, \varphi_{1} \times \varphi_{2})$ on $M$. The coordinate functions are $x^{i}$ from the first factor and $y^{j}$ from the second, so a coordinate basis at $p$ is
$$\left\{\left.\frac{\partial}{\partial x^{i}}\right|_{p}\right\}_{i=1}^{m_{1}} \cup \left\{\left.\frac{\partial}{\partial y^{j}}\right|_{p}\right\}_{j=1}^{m_{2}}$$
where $m_{i} = \dim M_{i}$. The first subset spans an $m_{1}$-dimensional subspace; the second subset spans an $m_{2}$-dimensional subspace; they intersect only at $0$. So $T_{p}M$ splits as a direct sum of the two subspaces.

What is the identification with $T_{p_{1}}M_{1} \oplus T_{p_{2}}M_{2}$? The first subspace, spanned by $\partial/\partial x^{i}|_{p}$, is precisely the image of $T_{p_{1}}M_{1}$ under the inclusion $\iota_{1, p_{2}} : M_{1} \to M$, $\iota_{1, p_{2}}(q) = (q, p_{2})$. The differential $d(\iota_{1, p_{2}})_{p_{1}}$ sends $\partial/\partial x^{i}|_{p_{1}}$ to $\partial/\partial x^{i}|_{p}$. So the first subspace is naturally $T_{p_{1}}M_{1}$. Similarly the second subspace is $T_{p_{2}}M_{2}$.

The projection map $\alpha$ from the theorem is then easy: a tangent vector $v \in T_{p}M$ at the product has components in both subspaces, and $\alpha(v)$ extracts these components.

The proof of well-definedness is by the chain rule: $d\pi_{i, p}$ is linear, and the direct-sum target is the natural recipient of two linear maps. Bijectivity is by direct construction of the inverse.

---

# What Makes This Hard

The result is conceptually clean — the proof is essentially "the product of charts is a chart on the product, with coordinate basis the union of the factor coordinate bases". The technical step is showing the natural map $\alpha$ via projections matches the natural splitting via charts. This is one line: by linearity, it suffices to check on the basis $\partial/\partial x^{i}|_{p}, \partial/\partial y^{j}|_{p}$, and these are sent under $\alpha$ to the correct components by the chain rule applied to $\pi_{1}, \pi_{2}$.

A subtle point is that **the splitting at $p$ depends on $p$** — specifically on the "other factor"'s coordinates. The first-factor subspace is $d(\iota_{1, p_{2}})(T_{p_{1}}M_{1})$, where $\iota_{1, p_{2}}$ uses the *current* value $p_{2}$ of the second factor. This is fine because we are computing tangent spaces *at a specific point*; but for global vector fields, the splitting becomes a smooth-bundle-level statement: $T(M_{1} \times M_{2}) = \pi_{1}^{*}TM_{1} \oplus \pi_{2}^{*}TM_{2}$ — the pullbacks of the factor tangent bundles.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Define $\alpha = (d\pi_{1}, d\pi_{2}) : T_{p}M \to T_{p_{1}}M_{1} \oplus T_{p_{2}}M_{2}$. Construct the inverse using the inclusion maps $\iota_{i, p_{\bar i}}$. Verify the two maps are inverse to each other.

**Subgoal decomposition:**

1. **$\alpha$ is linear.** Each component $d\pi_{i, p}$ is linear, so $\alpha$ is linear into a direct sum.
   - *Hint:* Differentials are linear, direct sums of linear maps are linear.
   - *Why needed:* Establishes well-definedness as a linear map.

2. **Build the inverse $\beta$.** Define $\beta : T_{p_{1}}M_{1} \oplus T_{p_{2}}M_{2} \to T_{p}M$ by $\beta(v_{1}, v_{2}) = d(\iota_{1, p_{2}})_{p_{1}}(v_{1}) + d(\iota_{2, p_{1}})_{p_{2}}(v_{2})$, where $\iota_{i, p_{\bar i}}$ is the inclusion of $M_{i}$ into $M$ that fixes the other coordinate at $p_{\bar i}$.
   - *Hint:* This is the sum of two inclusion-pushforwards.
   - *Why needed:* Candidate inverse to $\alpha$.

3. **Verify $\alpha \circ \beta = \mathrm{id}$.** Compute $\alpha(\beta(v_{1}, v_{2}))$ using $\pi_{i} \circ \iota_{j, p_{\bar j}}$.
   - *Hint:* $\pi_{i} \circ \iota_{i, p_{\bar i}} = \mathrm{id}_{M_{i}}$ and $\pi_{i} \circ \iota_{j, p_{\bar j}}$ is constant for $i \neq j$.
   - *Why needed:* One half of inverse verification.

4. **Verify $\beta \circ \alpha = \mathrm{id}$.** Apply both maps to a coordinate basis vector of $T_{p}M$ and check the round trip is identity.
   - *Hint:* In the coordinate basis from a product chart, $\partial/\partial x^{i}|_{p}$ is in the first factor subspace, $\partial/\partial y^{j}|_{p}$ in the second. The round trip preserves each.
   - *Why needed:* Other half of inverse verification.

---

# Lemma Decomposition

> [!note]- Lemma 1: The factor projections and inclusions
> **Statement:** Let $\pi_{i} : M_{1} \times M_{2} \to M_{i}$ be the projection and $\iota_{i, p_{\bar i}} : M_{i} \to M_{1} \times M_{2}$ the inclusion fixing the other coordinate at $p_{\bar i}$. Then:
> - $\pi_{i} \circ \iota_{i, p_{\bar i}} = \mathrm{id}_{M_{i}}$;
> - $\pi_{\bar i} \circ \iota_{i, p_{\bar i}}$ is the constant map at $p_{\bar i}$.
>
> **Hint:** Compute directly.
>
> **Why needed:** The key compositional facts that drive the proof.
>
> > [!note]- Full proof
> > For $q \in M_{i}$:
> > $(\pi_{i} \circ \iota_{i, p_{\bar i}})(q) = \pi_{i}(\iota_{i, p_{\bar i}}(q))$. The inclusion $\iota_{i, p_{\bar i}}$ sends $q$ to the element of $M$ with $i$-th component $q$ and other component $p_{\bar i}$. Projecting to the $i$-th factor returns $q$. So the composition is the identity.
> >
> > For the cross-composition: $(\pi_{\bar i} \circ \iota_{i, p_{\bar i}})(q) = \pi_{\bar i}(\iota_{i, p_{\bar i}}(q)) = p_{\bar i}$, the fixed value of the other coordinate.

> [!note]- Lemma 2: $\alpha$ is linear and well-defined
> **Statement:** The map $\alpha : T_{p}M \to T_{p_{1}}M_{1} \oplus T_{p_{2}}M_{2}$, $\alpha(v) = (d(\pi_{1})_{p}(v), d(\pi_{2})_{p}(v))$, is well-defined and linear.
>
> **Hint:** Each component is a differential, which is linear; direct sums of linear maps are linear.
>
> **Why needed:** Linearity is required to be the map of vector spaces in the theorem.
>
> > [!note]- Full proof
> > Each $d(\pi_{i})_{p}$ is a linear map $T_{p}M \to T_{p_{i}}M_{i}$. The tuple $(d\pi_{1}, d\pi_{2})$ is a map to the direct product $T_{p_{1}}M_{1} \times T_{p_{2}}M_{2}$, which is canonically the direct sum (as a vector space). For each $v \in T_{p}M$, both components are well-defined elements of the factor tangent spaces. Linearity: $\alpha(v + w) = (d\pi_{1}(v + w), d\pi_{2}(v + w)) = (d\pi_{1}(v) + d\pi_{1}(w), d\pi_{2}(v) + d\pi_{2}(w)) = \alpha(v) + \alpha(w)$, and similarly for scalar multiplication.

> [!note]- Lemma 3: $\beta$ is linear and a candidate inverse
> **Statement:** Define $\beta : T_{p_{1}}M_{1} \oplus T_{p_{2}}M_{2} \to T_{p}M$ by $\beta(v_{1}, v_{2}) = d(\iota_{1, p_{2}})_{p_{1}}(v_{1}) + d(\iota_{2, p_{1}})_{p_{2}}(v_{2})$. Then $\beta$ is linear.
>
> **Hint:** Each summand is a differential, hence linear; the sum is linear.
>
> **Why needed:** Establishes $\beta$ as a linear map; verification of inverse comes next.
>
> > [!note]- Full proof
> > Each summand $d(\iota_{i, p_{\bar i}})_{p_{i}}$ is a linear map from a factor tangent space to $T_{p}M$. The map $(v_{1}, v_{2}) \mapsto d\iota_{1}(v_{1}) + d\iota_{2}(v_{2})$ is linear in each argument and so linear from the direct sum.

> [!note]- Lemma 4: $\alpha$ and $\beta$ are mutual inverses
> **Statement:** $\alpha \circ \beta = \mathrm{id}_{T_{p_{1}}M_{1} \oplus T_{p_{2}}M_{2}}$ and $\beta \circ \alpha = \mathrm{id}_{T_{p}M}$.
>
> **Hint:** For $\alpha \circ \beta$, apply $\pi_{i}$ to each summand of $\beta(v_{1}, v_{2})$ using the chain rule and Lemma 1. For $\beta \circ \alpha$, work in a product chart's coordinate basis.
>
> **Why needed:** Establishes the bijection.
>
> > [!note]- Full proof
> > $(\alpha \circ \beta)(v_{1}, v_{2}) = \alpha(d\iota_{1}(v_{1}) + d\iota_{2}(v_{2}))$
> > $= (d\pi_{1}(d\iota_{1}(v_{1}) + d\iota_{2}(v_{2})), d\pi_{2}(d\iota_{1}(v_{1}) + d\iota_{2}(v_{2})))$
> > $= (d\pi_{1} \circ d\iota_{1}(v_{1}) + d\pi_{1} \circ d\iota_{2}(v_{2}), d\pi_{2} \circ d\iota_{1}(v_{1}) + d\pi_{2} \circ d\iota_{2}(v_{2}))$
> > $= (d(\pi_{1} \circ \iota_{1, p_{2}})_{p_{1}}(v_{1}) + d(\pi_{1} \circ \iota_{2, p_{1}})_{p_{2}}(v_{2}),\; d(\pi_{2} \circ \iota_{1, p_{2}})_{p_{1}}(v_{1}) + d(\pi_{2} \circ \iota_{2, p_{1}})_{p_{2}}(v_{2}))$ by the chain rule.
> >
> > By Lemma 1: $\pi_{1} \circ \iota_{1, p_{2}} = \mathrm{id}_{M_{1}}$, so its differential is $\mathrm{id}_{T_{p_{1}}M_{1}}$. And $\pi_{1} \circ \iota_{2, p_{1}}$ is constant at $p_{1}$, so its differential is zero. Similarly for the other pair. So the tuple becomes $(v_{1} + 0, 0 + v_{2}) = (v_{1}, v_{2})$.
> >
> > For $\beta \circ \alpha$: pick a product chart $(U_{1} \times U_{2}, \varphi_{1} \times \varphi_{2})$ at $p$, with coordinate basis $\{\partial/\partial x^{i}|_{p}\} \cup \{\partial/\partial y^{j}|_{p}\}$ of $T_{p}M$. It suffices to verify $\beta \circ \alpha$ on this basis. By the chain rule applied to $\iota_{1, p_{2}}$ in the chart, $d(\iota_{1, p_{2}})_{p_{1}}(\partial/\partial x^{i}|_{p_{1}}) = \partial/\partial x^{i}|_{p}$. And $d(\pi_{1})_{p}(\partial/\partial x^{i}|_{p}) = \partial/\partial x^{i}|_{p_{1}}$, while $d(\pi_{2})_{p}(\partial/\partial x^{i}|_{p}) = 0$. So $\alpha(\partial/\partial x^{i}|_{p}) = (\partial/\partial x^{i}|_{p_{1}}, 0)$ and $\beta(\partial/\partial x^{i}|_{p_{1}}, 0) = \partial/\partial x^{i}|_{p}$. Hence $\beta \circ \alpha(\partial/\partial x^{i}|_{p}) = \partial/\partial x^{i}|_{p}$. Similarly for $\partial/\partial y^{j}|_{p}$. Linearity extends to the whole space, so $\beta \circ \alpha = \mathrm{id}_{T_{p}M}$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $M = M_{1} \times \cdots \times M_{k}$ be a product manifold and $p \in M$. The map $\alpha : T_{p}M \to \bigoplus_{i} T_{p_{i}}M_{i}$ is a vector-space isomorphism.
>
> *Proof.* For simplicity we treat $k = 2$; the general case follows by induction.
>
> By Lemma 2, $\alpha$ is well-defined and linear.
>
> By Lemma 3, $\beta : T_{p_{1}}M_{1} \oplus T_{p_{2}}M_{2} \to T_{p}M$ defined by $\beta(v_{1}, v_{2}) = d(\iota_{1, p_{2}})_{p_{1}}(v_{1}) + d(\iota_{2, p_{1}})_{p_{2}}(v_{2})$ is linear.
>
> By Lemma 4, $\alpha$ and $\beta$ are mutual inverses.
>
> Hence $\alpha$ is a bijection, and since both $\alpha$ and $\beta$ are linear, $\alpha$ is a vector-space isomorphism. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Classical mechanics — separation of variables.** For a Lagrangian system on a product configuration manifold $Q_{1} \times Q_{2}$ with Lagrangian $L(q_{1}, q_{2}, \dot q_{1}, \dot q_{2})$ that separates as $L = L_{1}(q_{1}, \dot q_{1}) + L_{2}(q_{2}, \dot q_{2})$, the dynamics on $T(Q_{1} \times Q_{2}) = TQ_{1} \oplus TQ_{2}$ also separate — the velocity on each factor evolves independently. The tangent-space splitting is the basis for this separation.

**Lie theory — product Lie group.** For Lie groups $G$ and $H$, the product $G \times H$ is a Lie group, and the tangent space at the identity $T_{(e, e)}(G \times H) = T_{e}G \oplus T_{e}H = \mathfrak{g} \oplus \mathfrak{h}$. The Lie bracket on the product algebra is the componentwise bracket, with no mixing between $\mathfrak{g}$ and $\mathfrak{h}$ — the two factors commute. This is the trivial case of the structure theory of Lie algebras.

**Hamiltonian mechanics — product phase space.** For Hamiltonian systems with multiple particles, the phase space is a product of single-particle phase spaces (or a quotient thereof for indistinguishable particles). The tangent-space splitting gives the natural decomposition of "position-momentum pairs" into per-particle pieces, foundational for many-body classical mechanics.

**Algebraic topology — Künneth formula for $TM \otimes TN$.** The tangent bundle of $M \times N$ splits as $\pi_{M}^{*}TM \oplus \pi_{N}^{*}TN$, where $\pi_{M}, \pi_{N}$ are the projections. This is the Künneth-type splitting at the level of vector bundles, and it underlies computations of characteristic classes of products.

---

# Bridges

- **Direct sum is the categorical product in $\mathrm{Vec}$.** The direct sum $V \oplus W$ is the categorical product in the category of vector spaces — it is the unique vector space equipped with linear projections to $V$ and $W$ that any pair of linear maps into $V$ and $W$ factor through. The theorem says the tangent functor $T_{p}$ takes the categorical product on $\mathrm{Diff}_{*}$ (which is the manifold product) to the categorical product on $\mathrm{Vec}$ (which is the direct sum). So $T_{p}$ is a *product-preserving* functor.

- **Lie algebras of products.** For Lie groups $G$ and $H$, $\mathrm{Lie}(G \times H) = \mathrm{Lie}(G) \oplus \mathrm{Lie}(H)$, with the product Lie algebra having pieces that commute. The same direct-sum splitting appears whenever Lie groups (or other algebraic objects) are products. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

- **Global splitting of $T(M_{1} \times M_{2})$.** The tangent bundle of a product is the direct sum of the pullback bundles: $T(M_{1} \times M_{2}) = \pi_{1}^{*}TM_{1} \oplus \pi_{2}^{*}TM_{2}$. This is the bundle-level statement of the tangent-space splitting and is the basis for working with products at the global level.

- **The theorem is the foundation for foliations.** A **foliation** of $M$ is a smooth decomposition of $M$ into leaves $L_{\alpha}$ such that locally, near each point, $M \cong L \times T$ for a leaf $L$ and a transversal $T$. At a point of intersection, the tangent space splits via this local product: $T_{p}M = T_{p}L \oplus T_{p}T$. This is exactly the product-tangent-space splitting in the local product chart. See [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]].

---

# Unlocked by This

> [!tip] Lie Algebra of a Product Lie Group *(from Lie Theory)*
> For Lie groups $G$ and $H$, the Lie algebra $\mathfrak{g} \oplus \mathfrak{h}$ of $G \times H$ has bracket $[(X_{1}, Y_{1}), (X_{2}, Y_{2})] = ([X_{1}, X_{2}], [Y_{1}, Y_{2}])$. The two factors do not mix, so $\mathfrak{g}$ and $\mathfrak{h}$ commute inside the product. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

> [!tip] Cotangent Bundle of a Product *(from Differential Geometry)*
> $T^{*}(M_{1} \times M_{2}) = T^{*}M_{1} \oplus T^{*}M_{2}$, with covectors splitting in parallel to vectors. This is the basis for "position-momentum" splitting in Hamiltonian mechanics for multi-particle systems. See [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]].

> [!tip] Foliations and Distributions *(from Differential Geometry)*
> A **foliation** decomposes $M$ locally as a product of a leaf and a transversal. The tangent-space splitting at each point reflects this local product structure: $T_{p}M = T_{p}L \oplus T_{p}T$. The integrability of a distribution (the Frobenius condition) is closely related. See [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]].

> [!tip] Phase Space of Many-Body Systems *(from Classical Mechanics)*
> For a system of $N$ particles in $\mathbb{R}^{3}$, the configuration manifold is $(\mathbb{R}^{3})^{N}$ and the tangent space at any configuration splits as a direct sum of $N$ copies of $\mathbb{R}^{3}$ — one per particle's velocity. The Lagrangian, Hamiltonian, and momentum maps all respect this splitting.
