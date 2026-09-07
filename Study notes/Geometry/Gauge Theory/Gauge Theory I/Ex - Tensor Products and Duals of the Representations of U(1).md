---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Constructions on Representations"
  - "Thm - Complex Representations of U(1) and SU(2)"
  - "Def - Representation of a Lie Group"
  - "Def - Tensor Product of Vector Spaces"
  - "Def - Dual Space"
tags: [geometry, gauge-theory]
---

# Problem Statement

We work with the circle group $U(1) = \{z \in \mathbb{C} : |z| = 1\}$ and, for each integer $k \in \mathbb{Z}$, its one-dimensional complex representation
$$\varrho_k : U(1) \to GL(1;\mathbb{C}) = \mathbb{C}^{\times}, \qquad \varrho_k(z) = z^k,$$
acting on the one-dimensional space $V = \mathbb{C}$ by scalar multiplication: $\varrho_k(z)v = z^k v$. Here $\mathbb{C}^{\times} = \mathbb{C}\setminus\{0\}$ is the multiplicative group of nonzero complex numbers, identified with $GL(1;\mathbb{C}) = \operatorname{Aut}(\mathbb{C})$ by letting a nonzero scalar act as multiplication.

**Part (a) — tensor products.** Exhibit the natural isomorphism $\mathbb{C} \otimes_{\mathbb{C}} \mathbb{C} \cong \mathbb{C}$ and use it to prove
$$\varrho_k \otimes \varrho_l \cong \varrho_{k+l} \qquad \text{for all } k, l \in \mathbb{Z},$$
verifying the equivariance (intertwining) condition in full.

**Part (b) — duals.** Exhibit the natural isomorphism $\mathbb{C}^{*} \cong \mathbb{C}$ (the dual space of the one-dimensional space $\mathbb{C}$) and use it to prove
$$\varrho_k^{*} \cong \varrho_{-k} \qquad \text{for all } k \in \mathbb{Z},$$
again verifying equivariance in full. Recall that the dual representation is defined by $\varrho_k^{*}(z) := \varrho_k(z^{-1})^{*}$, where $(\cdot)^{*}$ denotes the transpose (dual) map on functionals, $S^{*}(\lambda) = \lambda \circ S$ — not the Hermitian adjoint; the distinction matters here, since on $U(1)$ the Hermitian adjoint would conjugate the scalar and produce the wrong sign of the exponent.

**Recall:**

The objects in play are the representations $\varrho_k$ of $U(1)$, the tensor-product and dual constructions on representations, the equivalence of two representations, and the universal property that defines the tensor product of vector spaces.

![[Def - Representation of a Lie Group#The Definition]]

Two representations $\varrho : G \to GL(V)$ and $\tilde\varrho : G \to GL(\tilde V)$ are **equivalent** (Bär's Definition 1.3.12) when there is a linear isomorphism $T : V \to \tilde V$ that **intertwines** them, meaning
$$T \circ \varrho(g) = \tilde\varrho(g) \circ T \qquad \text{for every } g \in G;$$
we write $\varrho \cong \tilde\varrho$. Verifying $\varrho \cong \tilde\varrho$ therefore has two obligations: produce a linear isomorphism $T$, and check the boxed identity for all $g$.

![[Def - Constructions on Representations#The Definition]]

For representations $\varrho_1 : G \to GL(V_1)$ and $\varrho_2 : G \to GL(V_2)$, the **tensor product representation** $\varrho_1 \otimes \varrho_2 : G \to GL(V_1 \otimes V_2)$ is defined on simple tensors by
$$(\varrho_1 \otimes \varrho_2)(g)(v_1 \otimes v_2) = \varrho_1(g)v_1 \otimes \varrho_2(g)v_2$$
and extended linearly. For a representation $\varrho : G \to GL(V)$, the **dual representation** $\varrho^{*} : G \to GL(V^{*})$ on the dual space $V^{*} = \{\lambda : V \to \mathbb{C} \text{ linear}\}$ is
$$\varrho^{*}(g) = \varrho(g^{-1})^{*}, \qquad \text{that is} \qquad \big(\varrho^{*}(g)\lambda\big)(v) = \lambda\big(\varrho(g^{-1})v\big),$$
where for a linear map $S : V \to V$ the dual (transpose) map $S^{*} : V^{*} \to V^{*}$ is $S^{*}(\lambda) = \lambda \circ S$. The inverse $g^{-1}$ is present precisely so that $\varrho^{*}$ is a homomorphism rather than an anti-homomorphism; without it, $g \mapsto \varrho(g)^{*}$ reverses the order of products.

![[Thm - Complex Representations of U(1) and SU(2)#Statement]]

The only facts from that classification used here are the definition $\varrho_k(z) = z^k$ and the two isomorphisms this exercise proves; we do not use complete reducibility.

The tensor product $V_1 \otimes_{\mathbb{C}} V_2$ and its defining universal property are recalled from linear algebra:

A [[Def - Tensor Product of Vector Spaces|tensor product]] of complex vector spaces $V_1, V_2$ is a complex vector space $V_1 \otimes V_2$ together with a bilinear map $\otimes : V_1 \times V_2 \to V_1 \otimes V_2$, $(v_1, v_2) \mapsto v_1 \otimes v_2$, such that for every complex vector space $W$ and every bilinear map $\beta : V_1 \times V_2 \to W$ there is a *unique* linear map $\tilde\beta : V_1 \otimes V_2 \to W$ with $\tilde\beta(v_1 \otimes v_2) = \beta(v_1, v_2)$; this is the [[Thm - Universal Property of the Tensor Product|universal property]]. Two consequences we use: scalars pull through a simple tensor, $(a v_1) \otimes (b v_2) = ab\,(v_1 \otimes v_2)$ for $a, b \in \mathbb{C}$ (bilinearity), and $\dim_{\mathbb{C}}(V_1 \otimes V_2) = (\dim V_1)(\dim V_2)$, so $\mathbb{C} \otimes_{\mathbb{C}} \mathbb{C}$ is one-dimensional.

The [[Def - Dual Space|dual space]] $V^{*}$ of an $n$-dimensional space $V$ is the space of linear functionals $\lambda : V \to \mathbb{C}$; it has dimension $n$, and for $V = \mathbb{C}$ (basis $\{1\}$) it is one-dimensional with dual basis $\{\varepsilon\}$, where $\varepsilon(v) = v$ is the identity functional.

---

# Convergent Strategy

**Problem class.** This is a *verify-an-equivalence-of-representations* problem: for each part we must produce an explicit intertwiner and check the commuting-square condition on the nose. Because the underlying vector spaces are one-dimensional, "produce an isomorphism" reduces to writing down a single nonzero linear map, and "check equivariance" reduces to comparing two scalars. The whole exercise is a template for the general pattern — build $T$ from the natural linear-algebra isomorphism, then push a general group element through both sides.

**Assumption pattern.** The structural feature exploited throughout is that $U(1)$ acts by *scalars*: $\varrho_k(z)$ is multiplication by $z^k$. Scalars commute with everything and pull through both tensor products and functionals, so the intertwining condition never involves genuinely non-commutative operators — it collapses to an identity between powers of $z$. The recognisable trigger is "one-dimensional representation of an abelian group": every such representation is a character $z \mapsto (\text{scalar})$, and tensoring adds exponents while dualising negates them, mirroring $z^k \cdot z^l = z^{k+l}$ and $(z^k)^{-1} = z^{-k}$.

**Theorem routing.** For part (a) the route is: take the multiplication map $\mu : \mathbb{C} \otimes \mathbb{C} \to \mathbb{C}$, $u \otimes w \mapsto uw$, which is well defined and linear by [[Thm - Universal Property of the Tensor Product|the universal property of the tensor product]] and is an isomorphism because both spaces are one-dimensional and $\mu(1 \otimes 1) = 1 \neq 0$; then verify $\mu \circ (\varrho_k \otimes \varrho_l)(z) = \varrho_{k+l}(z) \circ \mu$ on simple tensors, which suffices since simple tensors span. For part (b) the route is: take the evaluation-at-$1$ map $S : \mathbb{C}^{*} \to \mathbb{C}$, $\lambda \mapsto \lambda(1)$, an isomorphism because $\dim \mathbb{C}^{*} = 1$ and $S(\varepsilon) = 1$; then compute $\varrho_k^{*}(z)$ from the definition $\varrho_k^{*}(z)\lambda = \lambda \circ \varrho_k(z^{-1})$ and verify $S \circ \varrho_k^{*}(z) = \varrho_{-k}(z) \circ S$.

**Key decision point.** The one place where care is required is the *direction of the exponent in the dual*. The naive guess $\varrho_k^{*} \cong \varrho_k$ is wrong: because the dual representation is built from $\varrho_k(z^{-1})$, the functional $\lambda$ is precomposed with multiplication by $z^{-k}$, which acts as multiplication by $z^{-k}$ on the scalar output. The exponent flips sign, giving $\varrho_{-k}$. Recognising that the inverse $g^{-1}$ in the definition of $\varrho^{*}$ is exactly what produces this sign flip — and is exactly what makes $\varrho^{*}$ a homomorphism — is the conceptual content of part (b).

---

# Legal Operations Used

The topic page for §1.3 is not yet assembled; the operations below are named descriptively and the chapter's Legal Operations list will absorb them.

1. **Build an intertwiner from the canonical linear-algebra isomorphism.** For the tensor product use the multiplication map $\mu(u \otimes w) = uw$; for the dual use evaluation at the basis vector, $S(\lambda) = \lambda(1)$. In each case the map exists and is linear before any group action is considered.

2. **Certify well-definedness on a tensor product through the universal property.** The map $\mu : \mathbb{C} \otimes \mathbb{C} \to \mathbb{C}$ is induced by the bilinear map $(u, w) \mapsto uw$, so [[Thm - Universal Property of the Tensor Product|the universal property]] guarantees it is a single well-defined linear map on the whole tensor product, not merely a rule on simple tensors.

3. **Reduce an equivariance check on a tensor product to simple tensors.** Since simple tensors $u \otimes w$ span $V_1 \otimes V_2$ and both sides of the intertwining identity are linear, it suffices to verify the identity on simple tensors.

4. **Pull scalars through a simple tensor.** Use bilinearity $(z^k u) \otimes (z^l w) = z^{k+l}(u \otimes w)$ to collapse the tensor-product action to a single scalar factor.

5. **Compute a dual operator by precomposition.** From $\varrho_k^{*}(z)\lambda = \lambda \circ \varrho_k(z^{-1})$ and $\varrho_k(z^{-1}) = (\text{multiplication by } z^{-k})$, obtain $\varrho_k^{*}(z)\lambda = z^{-k}\lambda$ by linearity of $\lambda$.

---

# Hints

> [!note]- Hint 1
> Both representation spaces are one-dimensional, so an "isomorphism" is just any nonzero linear map. For the tensor product, the obvious candidate is multiplication $u \otimes w \mapsto uw$; for the dual, the obvious candidate is "evaluate the functional at $1 \in \mathbb{C}$". Write these down first; the group action comes afterward.

> [!note]- Hint 2
> To check equivariance you must compare $T \circ (\text{source action})$ with $(\text{target action}) \circ T$. For the tensor product, apply $\varrho_k \otimes \varrho_l$ to a simple tensor $u \otimes w$ and *then* multiply the two factors; separately, multiply first and *then* apply $\varrho_{k+l}$. The two must agree for all $z$.

> [!note]- Hint 3
> The scalar rule $z^k u \otimes z^l w = z^{k+l}(u \otimes w)$ is the whole computation for part (a): the exponents add. This is why tensoring characters of $U(1)$ mirrors multiplying powers of $z$.

> [!note]- Hint 4
> For the dual, start from the definition $\big(\varrho_k^{*}(z)\lambda\big)(v) = \lambda\big(\varrho_k(z^{-1})v\big)$. Since $\varrho_k(z^{-1})v = z^{-k}v$ and $\lambda$ is linear, $\lambda(z^{-k}v) = z^{-k}\lambda(v)$. So $\varrho_k^{*}(z)$ is multiplication by $z^{-k}$ — that is $\varrho_{-k}$. The inverse in the definition is exactly what flips $k$ to $-k$.

---

# Solution

The plan is uniform across both parts: identify the natural one-dimensional isomorphism ($\mu$ for the tensor product, $S$ for the dual), confirm it is a linear isomorphism, and then verify the intertwining identity by pushing a general $z \in U(1)$ through both routes of the commuting square. Because $U(1)$ acts by scalars, each verification collapses to the arithmetic of exponents: $z^k z^l = z^{k+l}$ for the tensor product and $(z^k)^{-1} = z^{-k}$ for the dual.

**Step 1 (part a): The multiplication map $\mu : \mathbb{C} \otimes \mathbb{C} \to \mathbb{C}$ is a well-defined linear isomorphism.**

The map $\mu(u \otimes w) = uw$ exists as a linear map by the universal property and is bijective because both spaces are one-dimensional.

> [!note]- Derivation
> Consider the map $\beta : \mathbb{C} \times \mathbb{C} \to \mathbb{C}$, $\beta(u, w) = uw$. It is $\mathbb{C}$-bilinear: in the first slot $\beta(au + a'u', w) = (au + a'u')w = a(uw) + a'(u'w) = a\beta(u,w) + a'\beta(u',w)$ (distributivity of complex multiplication), and in the second slot $\beta(u, bw + b'w') = u(bw + b'w') = b(uw) + b'(uw') = b\beta(u,w) + b'\beta(u,w')$ for $b, b' \in \mathbb{C}$ (distributivity again). By [[Thm - Universal Property of the Tensor Product|the universal property of the tensor product]], there is a **unique** linear map
> $$\mu : \mathbb{C} \otimes_{\mathbb{C}} \mathbb{C} \to \mathbb{C}, \qquad \mu(u \otimes w) = uw,$$
> defined on all of $\mathbb{C} \otimes \mathbb{C}$, not just on simple tensors. It is surjective because $\mu(u \otimes 1) = u$ realises every $u \in \mathbb{C}$; and since $\dim_{\mathbb{C}}(\mathbb{C} \otimes \mathbb{C}) = 1\cdot 1 = 1 = \dim_{\mathbb{C}}\mathbb{C}$, a surjective linear map between spaces of equal finite dimension is an isomorphism. (Concretely, $1 \otimes 1$ is a basis of $\mathbb{C} \otimes \mathbb{C}$ and $\mu(1 \otimes 1) = 1 \neq 0$, so $\mu$ carries a basis to a basis.) Thus $\mu$ is the required isomorphism $\mathbb{C} \otimes \mathbb{C} \cong \mathbb{C}$.

**Step 2 (part a): $\mu$ intertwines $\varrho_k \otimes \varrho_l$ with $\varrho_{k+l}$.**

For every $z \in U(1)$ and every simple tensor, $\mu \circ (\varrho_k \otimes \varrho_l)(z) = \varrho_{k+l}(z) \circ \mu$.

> [!note]- Derivation
> Fix $z \in U(1)$ and a simple tensor $u \otimes w \in \mathbb{C} \otimes \mathbb{C}$. We must show the two composites agree; by operation 3 checking simple tensors suffices, since they span and both composites are linear.
>
> **Left route — act, then multiply.** By the definition of the tensor-product representation, then bilinearity, then $\mu$:
> $$\mu\big((\varrho_k \otimes \varrho_l)(z)(u \otimes w)\big) = \mu\big(\varrho_k(z)u \otimes \varrho_l(z)w\big) \qquad \text{(definition of } \varrho_k \otimes \varrho_l\text{)}$$
> $$= \mu\big(z^k u \otimes z^l w\big) \qquad \text{(} \varrho_k(z)u = z^k u,\ \varrho_l(z)w = z^l w\text{)}$$
> $$= \mu\big(z^{k+l}(u \otimes w)\big) \qquad \text{(pulling scalars through the tensor: } z^k u \otimes z^l w = z^{k+l}(u \otimes w)\text{)}$$
> $$= z^{k+l}\,\mu(u \otimes w) = z^{k+l}\,uw \qquad \text{(linearity of } \mu\text{, then } \mu(u \otimes w) = uw\text{).}$$
>
> **Right route — multiply, then act.** By $\mu$, then the definition of $\varrho_{k+l}$:
> $$\varrho_{k+l}(z)\big(\mu(u \otimes w)\big) = \varrho_{k+l}(z)(uw) = z^{k+l}\,uw \qquad \text{(} \mu(u \otimes w) = uw,\ \varrho_{k+l}(z)v = z^{k+l}v\text{).}$$
>
> **Combine.** Both routes yield $z^{k+l}uw$, so $\mu \circ (\varrho_k \otimes \varrho_l)(z) = \varrho_{k+l}(z) \circ \mu$ on simple tensors, hence everywhere. As $z \in U(1)$ was arbitrary, $\mu$ intertwines the two representations. Together with Step 1 ($\mu$ an isomorphism), this is the definition of equivalence, so $\varrho_k \otimes \varrho_l \cong \varrho_{k+l}$.

**Step 3 (part b): The evaluation map $S : \mathbb{C}^{*} \to \mathbb{C}$ is a linear isomorphism, and $\varrho_k^{*}(z)$ is multiplication by $z^{-k}$.**

The map $S(\lambda) = \lambda(1)$ is a linear isomorphism, and $\varrho_k^{*}(z)\lambda = z^{-k}\lambda$.

> [!note]- Derivation
> **The isomorphism.** Evaluation at the basis vector $1 \in \mathbb{C}$,
> $$S : \mathbb{C}^{*} \to \mathbb{C}, \qquad S(\lambda) = \lambda(1),$$
> is linear: $S(\lambda + a\lambda') = (\lambda + a\lambda')(1) = \lambda(1) + a\lambda'(1) = S(\lambda) + aS(\lambda')$ (definition of the vector-space operations on $\mathbb{C}^{*}$). It is an isomorphism because $\dim_{\mathbb{C}}\mathbb{C}^{*} = \dim_{\mathbb{C}}\mathbb{C} = 1$ and $S$ is nonzero: on the dual basis vector $\varepsilon$ (the functional $\varepsilon(v) = v$) it gives $S(\varepsilon) = \varepsilon(1) = 1 \neq 0$, so $S$ carries the basis $\{\varepsilon\}$ to the basis $\{1\}$.
>
> **The dual operator.** By operation 5, for $\lambda \in \mathbb{C}^{*}$ and $v \in \mathbb{C}$,
> $$\big(\varrho_k^{*}(z)\lambda\big)(v) = \lambda\big(\varrho_k(z^{-1})v\big) \qquad \text{(definition } \varrho_k^{*}(z) = \varrho_k(z^{-1})^{*}, \text{ i.e. precompose with } \varrho_k(z^{-1})\text{)}$$
> $$= \lambda\big(z^{-k}v\big) \qquad \text{(} \varrho_k(z^{-1})v = (z^{-1})^k v = z^{-k}v\text{)}$$
> $$= z^{-k}\lambda(v) \qquad \text{(linearity of the functional } \lambda\text{).}$$
> Since this holds for all $v$, the functional $\varrho_k^{*}(z)\lambda$ equals $z^{-k}\lambda$; that is, $\varrho_k^{*}(z)$ is multiplication by the scalar $z^{-k}$ on $\mathbb{C}^{*}$.

**Step 4 (part b): $S$ intertwines $\varrho_k^{*}$ with $\varrho_{-k}$.**

For every $z \in U(1)$, $S \circ \varrho_k^{*}(z) = \varrho_{-k}(z) \circ S$.

> [!note]- Derivation
> Fix $z \in U(1)$ and $\lambda \in \mathbb{C}^{*}$.
>
> **Left route — dualise, then evaluate.** By Step 3, $\varrho_k^{*}(z)\lambda = z^{-k}\lambda$, so
> $$S\big(\varrho_k^{*}(z)\lambda\big) = S\big(z^{-k}\lambda\big) = \big(z^{-k}\lambda\big)(1) = z^{-k}\,\lambda(1) = z^{-k}\,S(\lambda) \qquad \text{(} S \text{ evaluates at } 1; \text{ scalars pull out of the functional}\text{).}$$
>
> **Right route — evaluate, then act.** Since $\varrho_{-k}(z)$ is multiplication by $z^{-k}$ (as $(-k)$ is the exponent),
> $$\varrho_{-k}(z)\big(S(\lambda)\big) = z^{-k}\,S(\lambda) \qquad \text{(} \varrho_{-k}(z)v = z^{-k}v,\ v = S(\lambda)\text{).}$$
>
> **Combine.** Both routes yield $z^{-k}S(\lambda)$, so $S \circ \varrho_k^{*}(z) = \varrho_{-k}(z) \circ S$ for every $z \in U(1)$. With Step 3 ($S$ an isomorphism), this is the definition of equivalence, so $\varrho_k^{*} \cong \varrho_{-k}$.

> [!note]- Complete formal solution
> **Claim.** For all $k, l \in \mathbb{Z}$, the representations $\varrho_k(z) = z^k$ of $U(1)$ satisfy $\varrho_k \otimes \varrho_l \cong \varrho_{k+l}$ and $\varrho_k^{*} \cong \varrho_{-k}$.
>
> *Tensor product.* The bilinear map $(u, w) \mapsto uw$ induces, by [[Thm - Universal Property of the Tensor Product|the universal property]], a linear map $\mu : \mathbb{C} \otimes_{\mathbb{C}} \mathbb{C} \to \mathbb{C}$, $\mu(u \otimes w) = uw$. It is an isomorphism: $\dim(\mathbb{C} \otimes \mathbb{C}) = 1 = \dim \mathbb{C}$ and $\mu(1 \otimes 1) = 1 \neq 0$. For $z \in U(1)$ and a simple tensor $u \otimes w$,
> $$\mu\big((\varrho_k \otimes \varrho_l)(z)(u \otimes w)\big) = \mu(z^k u \otimes z^l w) = z^{k+l}uw = \varrho_{k+l}(z)\big(\mu(u \otimes w)\big),$$
> using bilinearity $z^k u \otimes z^l w = z^{k+l}(u \otimes w)$. Simple tensors span and both sides are linear, so $\mu$ intertwines $\varrho_k \otimes \varrho_l$ and $\varrho_{k+l}$; being also an isomorphism, it witnesses $\varrho_k \otimes \varrho_l \cong \varrho_{k+l}$.
>
> *Dual.* Evaluation at $1$, $S : \mathbb{C}^{*} \to \mathbb{C}$, $S(\lambda) = \lambda(1)$, is linear and an isomorphism (equal dimensions; $S(\varepsilon) = 1 \neq 0$ for the dual basis vector $\varepsilon(v) = v$). From the definition $\varrho_k^{*}(z)\lambda = \lambda \circ \varrho_k(z^{-1})$ and $\varrho_k(z^{-1})v = z^{-k}v$, linearity of $\lambda$ gives $\varrho_k^{*}(z)\lambda = z^{-k}\lambda$. Hence for all $z \in U(1)$ and $\lambda \in \mathbb{C}^{*}$,
> $$S\big(\varrho_k^{*}(z)\lambda\big) = z^{-k}\lambda(1) = z^{-k}S(\lambda) = \varrho_{-k}(z)\big(S(\lambda)\big),$$
> so $S$ intertwines $\varrho_k^{*}$ and $\varrho_{-k}$, and $\varrho_k^{*} \cong \varrho_{-k}$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: omitting the inverse in the dual and getting the sign wrong
> A frequent error is to define the dual representation as $g \mapsto \varrho(g)^{*}$, without the inverse, and thereby to "prove" $\varrho_k^{*} \cong \varrho_k$. This is illegitimate on two counts. First, $g \mapsto \varrho(g)^{*}$ is *not a representation*: because $(\varrho(g_1)\varrho(g_2))^{*} = \varrho(g_2)^{*}\varrho(g_1)^{*}$ (the transpose reverses composition), the map $g \mapsto \varrho(g)^{*}$ is an anti-homomorphism, satisfying $(\ )^{*}(g_1 g_2) = (\ )^{*}(g_2)(\ )^{*}(g_1)$ instead of the homomorphism law. Second, the correct definition $\varrho^{*}(g) = \varrho(g^{-1})^{*}$ inserts the inverse precisely to repair this — $\varrho^{*}(g_1 g_2) = \varrho((g_1 g_2)^{-1})^{*} = \varrho(g_2^{-1}g_1^{-1})^{*} = (\varrho(g_2^{-1})\varrho(g_1^{-1}))^{*} = \varrho(g_1^{-1})^{*}\varrho(g_2^{-1})^{*} = \varrho^{*}(g_1)\varrho^{*}(g_2)$ — and it is exactly this inverse that turns $z^k$ into $z^{-k}$. For the *abelian* group $U(1)$ the order reversal is invisible, so the anti-homomorphism happens to still be a homomorphism; but the sign of the exponent is governed by the inverse, and dropping it produces the wrong answer $\varrho_k$ in place of $\varrho_{-k}$. The condition that would make "no inverse" harmless is never met for the exponent: it is the inverse, not the transpose, that carries the sign.

> [!note]- Independent sanity check: the character viewpoint
> Every one-dimensional representation is its own character $\chi(z) = \varrho(z)$ (the trace of a $1\times 1$ matrix is its single entry), and equivalence of one-dimensional representations is equality of characters. The character of $\varrho_k \otimes \varrho_l$ is the product of characters, $z^k \cdot z^l = z^{k+l}$, matching $\varrho_{k+l}$; the character of $\varrho_k^{*}$ is $\overline{\chi(z)} = \overline{z^k} = z^{-k}$ (for $|z| = 1$, $\bar z = z^{-1}$), matching $\varrho_{-k}$. Both isomorphisms are thus confirmed by the elementary arithmetic of characters, exactly as the explicit intertwiners show.

---

# Key Takeaways

**To prove two representations equivalent, name the natural linear isomorphism of the underlying spaces first, then verify it intertwines — never conflate the two obligations.** An equivalence $\varrho \cong \tilde\varrho$ is a single linear isomorphism $T$ subject to the commuting-square law $T\varrho(g) = \tilde\varrho(g)T$ for all $g$. This exercise trains the discipline of producing $T$ from the canonical construction — the multiplication map on a tensor product, evaluation at a basis vector on a dual — and then discharging the intertwining check as a separate, explicit computation on a spanning set. The trigger for this pattern is any claim of the form "this constructed representation *is* that one"; the transferable diagnostic is that on a tensor product it always suffices to test simple tensors (they span and everything is linear), so the check reduces to one line of the defining formulas. The same template governs the far less trivial equivalence $\varrho_2 \cong (\operatorname{Ad}_{SU(2)})_{\mathbb{C}}$ proved in [[Thm - Complex Representations of U(1) and SU(2)|the classification theorem]], where the intertwiner is Bär's explicit $3 \times 3$ matrix $T$ rather than a scalar map, but the two obligations — isomorphism, then intertwining — are identical.

**On tensor products the group action adds exponents; on duals it negates them — and the inverse in the dual definition is the source of the sign.** For one-dimensional representations of $U(1)$ the arithmetic is transparent: $\varrho_k \otimes \varrho_l = \varrho_{k+l}$ mirrors $z^k z^l = z^{k+l}$, and $\varrho_k^{*} = \varrho_{-k}$ mirrors $(z^k)^{-1} = z^{-k}$. The deeper point is *why* the dual flips the sign: the dual representation is $\varrho(g^{-1})^{*}$, and the inverse — inserted to make $g \mapsto \varrho^{*}(g)$ a homomorphism rather than the order-reversing anti-homomorphism $g \mapsto \varrho(g)^{*}$ — is exactly what converts the exponent $k$ into $-k$. The reusable principle is that duality and inversion are the same operation seen on the two sides of a pairing, so a dual always carries the inverse of whatever the original carried; forgetting the inverse both breaks the homomorphism law and produces the wrong sign. This is the abelian, one-dimensional shadow of the general fact that the character of a dual representation is the complex conjugate (equivalently, the inverse-argument) of the original character.

**The additive group of exponents $\mathbb{Z}$ is the representation ring of $U(1)$ in miniature, and these two isomorphisms are its multiplication and inversion.** Assembling the results: the isomorphism classes of the $\varrho_k$ are indexed by $k \in \mathbb{Z}$, tensor product corresponds to addition ($k + l$), the trivial representation $\varrho_0$ is the additive identity, and duality corresponds to negation ($-k$). This makes the set $\{[\varrho_k] : k \in \mathbb{Z}\}$, under $\otimes$, a group isomorphic to $(\mathbb{Z}, +)$ — the character group of $U(1)$, which is $\mathbb{Z}$. This structural payoff is what makes the classification of $U(1)$-representations so clean and is the algebraic engine behind the geometry to come: when $U(1)$ is the structure group of a line bundle, the associated bundle built from $\varrho_k$ is the $k$-th tensor power $L^{\otimes k}$ of the fundamental line bundle, so "tensoring representations adds exponents" becomes "tensoring line bundles adds first Chern numbers". Returning to this exercise later, the reconstruction hinges on the two one-line facts "$z^k z^l = z^{k+l}$" and "the dual carries $z^{-1}$, hence $z^{-k}$", and on remembering that each must be dressed as an *explicit intertwiner* to count as a proof of equivalence.
