---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Mixed Tensor"
  - "Def - Tensor Field on a Manifold"
  - "Thm - Transformation Rule for Tensor Components"
tags: [geometry, differential-geometry, kronecker-delta]
---

# Problem Statement

Let $V$ be a finite-dimensional real vector space, $\dim V = n$. Define the function

$$W_{\mathrm{id}} : V^* \times V \to \mathbb{R}, \quad W_{\mathrm{id}}(\omega, v) := \omega(v).$$

**(a)** Show that $W_{\mathrm{id}}$ is a mixed $(1, 1)$-tensor on $V$.

**(b)** Compute the components of $W_{\mathrm{id}}$ in any basis $(E_1, \dots, E_n)$ of $V$ with dual basis $(\varepsilon^1, \dots, \varepsilon^n)$ of $V^*$, and show they equal the Kronecker delta $\delta^i_j = 1$ if $i = j$, $0$ otherwise.

**(c)** Show that the components of $W_{\mathrm{id}}$ are the *same* in every basis — they remain $\delta^i_j$ regardless of the choice of basis. Verify this using the [[Thm - Transformation Rule for Tensor Components|transformation rule]] directly.

**(d)** Conclude that the identity endomorphism $\mathrm{id}_V : V \to V$ corresponds, under the isomorphism $T^{(1,1)}(V) \cong \mathcal{L}(V, V)$, to the tensor $W_{\mathrm{id}}$, and that the trace (contraction) of $W_{\mathrm{id}}$ equals $\delta^i_i = n$.

**Recall:**

A [[Def - Mixed Tensor|mixed tensor of type (1, 1)]] on $V$ is a multilinear function $W : V^* \times V \to \mathbb{R}$, with components $W^i_j = W(\varepsilon^i, E_j)$ in a basis. The space $T^{(1,1)}(V) \cong V \otimes V^* \cong \mathcal{L}(V, V)$.

A [[Def - Linear Map|linear map]] $A : V \to V$ corresponds to the $(1, 1)$-tensor $W_A(\omega, v) := \omega(Av)$, with components equal to the matrix of $A$.

Using coordinate bases fixes the convention cleanly. If $\tilde x^i=\tilde x^i(x)$ is a coordinate change, then the [[Thm - Transformation Rule for Tensor Components|transformation rule]] for a $(1,1)$-tensor is

$$\tilde W^i_j = \frac{\partial \tilde x^i}{\partial x^a}\, \frac{\partial x^b}{\partial \tilde x^j}\, W^a_b.$$

---

# Convergent Strategy

**Problem class.** This is a *check tensoriality and compute components* problem — the most basic recurring task in differential geometry. The Kronecker delta is the simplest non-trivial example: a $(1, 1)$-tensor whose components are the same in every basis.

**Assumption pattern.** Three hypotheses are in play. First, $V$ is a finite-dimensional vector space — needed for the $V \cong V^{**}$ identification and the [[Def - Dimension|dimension]] count. Second, a basis $(E_i)$ with dual basis $(\varepsilon^j)$ is given (or chosen). Third, the function $W_{\mathrm{id}}$ is defined by the *evaluation pairing* $\omega(v)$, which is bilinear in $(\omega, v)$ by the definition of the dual space.

**Theorem routing.** For part (a), verify multilinearity directly from the bilinearity of evaluation. For part (b), evaluate $W_{\mathrm{id}}(\varepsilon^i, E_j)$ using the dual basis identity $\varepsilon^i(E_j) = \delta^i_j$. For part (c), invoke the [[Thm - Transformation Rule for Tensor Components|transformation rule]] and verify the right-hand side equals $\delta^i_j$ after applying the chain rule for Jacobians. For part (d), recognize that the linear map associated to $W_{\mathrm{id}}$ via the isomorphism $W_A(\omega, v) = \omega(Av)$ is the identity, hence the matrix is the identity matrix, hence the trace is $n$.

**Key decision point.** The non-obvious step is part (c): showing the components are basis-invariant. The trick is to write the transformation rule and recognize that the Jacobian factors precisely cancel, giving $\tilde\delta^i_j = \delta^i_j$. This invariance reflects the basis-free identity map. More generally, the endomorphisms whose matrices are unchanged under every basis change are precisely the scalar multiples of the identity.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Differential Geometry VII — Tensors and Tensor Fields#Legal Operations|the topic page's Legal Operations]]:

1. **Check tensoriality via $C^\infty(M)$-multilinearity** (operation 2). Verifying $W_{\mathrm{id}}$ is bilinear in its two slots — the linear-algebra version of the manifold-level $C^\infty$-multilinearity check.

2. **Compute components in a chart** (operation 3). Evaluating $W_{\mathrm{id}}(\varepsilon^i, E_j)$ to read off the components $\delta^i_j$.

3. **Change coordinates using the transformation rule** (operation 4). Used in part (c) to verify that the components transform correctly.

4. **Contract a covariant against a contravariant index** (operation 6). Part (d) involves the trace contraction, $\delta^i_i = n$.

---

# Hints

> [!note]- Hint 1
> For part (a), use bilinearity of the evaluation pairing $\omega(v)$. This pairing is linear in $\omega$ (by definition of the dual space) and linear in $v$ (since $\omega$ is a linear functional). That is exactly the (1, 1)-multilinearity required.

> [!note]- Hint 2
> For part (b), simply evaluate: $W_{\mathrm{id}}(\varepsilon^i, E_j) = \varepsilon^i(E_j) = \delta^i_j$ by definition of the dual basis.

> [!note]- Hint 3
> For part (c), apply the transformation rule with one upper and one lower index. The Jacobian factors are $\partial \tilde x^i / \partial x^a$ and $\partial x^b / \partial \tilde x^j$. Their product, summed over $a = b$, gives $(\partial \tilde x^i / \partial x^a)(\partial x^a / \partial \tilde x^j) = \delta^i_j$ by the chain rule.

> [!note]- Hint 4
> For part (d), the linear map $A$ satisfying $\omega(v) = \omega(Av)$ for all $\omega, v$ is the identity (set $v$ arbitrary, take $\omega$ to be any covector that detects the difference $v - Av$ — this is the standard "test on a separating family" argument).

---

# Solution

The proof breaks into four parts mirroring the problem statement. The thread linking them is that **the components $\delta^i_j$ uniquely identify $W_{\mathrm{id}}$**, and the components are basis-invariant because the Kronecker delta is the only tensor with this property.

**Step (a): $W_{\mathrm{id}}$ is a $(1, 1)$-tensor.**

$W_{\mathrm{id}}$ is bilinear in $(\omega, v)$, hence multilinear in its two slots, hence a $(1, 1)$-tensor.

> [!note]- Derivation
> *Linearity in $\omega$:* for $\omega, \omega' \in V^*$, $a, a' \in \mathbb{R}$, $v \in V$,
> $$W_{\mathrm{id}}(a\omega + a'\omega', v) = (a\omega + a'\omega')(v) = a\,\omega(v) + a'\,\omega'(v) = a\, W_{\mathrm{id}}(\omega, v) + a'\, W_{\mathrm{id}}(\omega', v),$$
> by the linearity of the operations on the dual space $V^*$ (vector space structure).
>
> *Linearity in $v$:* for $v, v' \in V$, $a, a' \in \mathbb{R}$, $\omega \in V^*$,
> $$W_{\mathrm{id}}(\omega, av + a'v') = \omega(av + a'v') = a\, \omega(v) + a'\, \omega(v') = a\, W_{\mathrm{id}}(\omega, v) + a'\, W_{\mathrm{id}}(\omega, v'),$$
> by the linearity of $\omega$ as a linear functional.
>
> So $W_{\mathrm{id}}$ is linear in each slot, hence a $(1, 1)$-tensor on $V$.

**Step (b): Components are $\delta^i_j$.**

By definition of components, $(W_{\mathrm{id}})^i_j = W_{\mathrm{id}}(\varepsilon^i, E_j) = \varepsilon^i(E_j) = \delta^i_j$.

> [!note]- Derivation
> The components of a $(1, 1)$-tensor $W$ in a basis $(E_i)$ with dual basis $(\varepsilon^j)$ are $W^i_j := W(\varepsilon^i, E_j)$. Applying to $W_{\mathrm{id}}$:
> $$(W_{\mathrm{id}})^i_j = W_{\mathrm{id}}(\varepsilon^i, E_j) = \varepsilon^i(E_j).$$
> By the definition of the dual basis, $\varepsilon^i(E_j) = \delta^i_j$, where $\delta^i_j = 1$ if $i = j$ and $0$ otherwise. Hence $(W_{\mathrm{id}})^i_j = \delta^i_j$.

**Step (c): Components are basis-invariant.**

Under any change of basis, the components of $W_{\mathrm{id}}$ remain $\delta^i_j$ — verified via the transformation rule for a $(1, 1)$-tensor.

> [!note]- Derivation
> Consider a change of basis from $(E_i)$ to $(\tilde E_i)$, with associated dual-basis change from $(\varepsilon^j)$ to $(\tilde\varepsilon^j)$. The transformation rule for a $(1, 1)$-tensor (specializing [[Thm - Transformation Rule for Tensor Components]] to $k = \ell = 1$) is
> $$\tilde W^i_j = \frac{\partial \tilde x^i}{\partial x^a}\, \frac{\partial x^b}{\partial \tilde x^j}\, W^a_b,$$
> where the Jacobian factors come from the basis change. Applying to $W = W_{\mathrm{id}}$ with components $W^a_b = \delta^a_b$:
> $$\tilde W^i_j = \frac{\partial \tilde x^i}{\partial x^a}\, \frac{\partial x^b}{\partial \tilde x^j}\, \delta^a_b = \frac{\partial \tilde x^i}{\partial x^a}\, \frac{\partial x^a}{\partial \tilde x^j}$$
> (the $\delta^a_b$ collapses $b$ to $a$). By the chain rule,
> $$\frac{\partial \tilde x^i}{\partial x^a}\, \frac{\partial x^a}{\partial \tilde x^j} = \frac{\partial \tilde x^i}{\partial \tilde x^j} = \delta^i_j,$$
> since the partial derivative of one coordinate with respect to another in the *same* chart is $1$ for equal indices and $0$ otherwise.
>
> Hence $\tilde W^i_j = \delta^i_j$, i.e., the components of $W_{\mathrm{id}}$ in the new basis are the same Kronecker delta as in the old basis. This is the *uniqueness* property: the only $(1, 1)$-tensor with chart-independent components is the Kronecker delta (up to scaling).

**Step (d): $W_{\mathrm{id}}$ corresponds to the identity map; trace is $n$.**

Under the isomorphism $W_A(\omega, v) = \omega(Av) \leftrightarrow A \in \mathcal{L}(V, V)$, the tensor $W_{\mathrm{id}}$ corresponds to the linear map satisfying $\omega(v) = \omega(Av)$ for all $\omega, v$ — which is the identity. The trace is the contraction $W_{\mathrm{id}}{}^i_i = \delta^i_i = n$.

> [!note]- Derivation
> *Identifying the linear map.* Under the isomorphism $T^{(1, 1)}(V) \cong \mathcal{L}(V, V)$, a $(1, 1)$-tensor $W$ corresponds to the unique linear map $A : V \to V$ with $W(\omega, v) = \omega(Av)$ for all $\omega \in V^*, v \in V$. Applied to $W_{\mathrm{id}}$:
> $$\omega(v) = W_{\mathrm{id}}(\omega, v) = \omega(Av) \quad \text{for all } \omega, v.$$
> This forces $Av = v$ for all $v$, by the following argument: $\omega(v - Av) = 0$ for every $\omega \in V^*$, and since $V^*$ separates points of $V$ (any nonzero $v - Av$ is detected by some $\omega$, e.g., a covector dual to a basis containing $v - Av$ as a basis vector), $v - Av = 0$. So $A = \mathrm{id}_V$.
>
> *Computing the trace.* The trace (contraction) of $W_{\mathrm{id}}$ is
> $$\mathrm{tr}\, W_{\mathrm{id}} = (W_{\mathrm{id}})^i_i = \sum_i \delta^i_i = \underbrace{1 + 1 + \cdots + 1}_{n \text{ terms}} = n.$$
> This agrees with the trace of the identity matrix in dimension $n$, which is also $n$.

> [!note]- Complete formal solution
> *Parts (a) and (b).* $W_{\mathrm{id}}(\omega, v) := \omega(v)$ is bilinear (linear in each slot by linearity of evaluation), hence a $(1, 1)$-tensor. Components: $W_{\mathrm{id}}(\varepsilon^i, E_j) = \varepsilon^i(E_j) = \delta^i_j$.
>
> *Part (c).* Under any change of basis,
> $$\tilde W_{\mathrm{id}}{}^i_j = \frac{\partial \tilde x^i}{\partial x^a}\,\frac{\partial x^b}{\partial \tilde x^j}\,\delta^a_b = \frac{\partial \tilde x^i}{\partial x^a}\,\frac{\partial x^a}{\partial \tilde x^j} = \frac{\partial \tilde x^i}{\partial \tilde x^j} = \delta^i_j.$$
> So the components are basis-invariant.
>
> *Part (d).* The linear map $A : V \to V$ corresponding to $W_{\mathrm{id}}$ satisfies $\omega(v) = \omega(Av)$ for all $\omega \in V^*, v \in V$. Since $V^*$ separates points, $A = \mathrm{id}_V$. The trace is $\delta^i_i = n$. $\blacksquare$

---

# Key Takeaways

**The Kronecker delta is the universal $(1, 1)$-tensor.** Among all $(1, 1)$-tensors, the Kronecker delta is uniquely characterized by having basis-independent components. The reason is the cancellation $(\partial \tilde x^i / \partial x^a)(\partial x^a / \partial \tilde x^j) = \delta^i_j$, which is the chain rule applied to the same chart change in both directions. Every other $(1, 1)$-tensor has components that depend on the basis. This makes $\delta^i_j$ the "identity in the tensor algebra" — the unique tensor that does nothing to a tensor when contracted with it: $T^i_j = \delta^i_a T^a_j = T^i_j$. The trick of inserting $\delta^i_a$ into a product is the standard manipulation in index gymnastics.

**The matrix of a linear map *is* the components of its associated $(1, 1)$-tensor.** The classical "matrix" $A^i_j$ of a linear map and the "tensor components" $W_A{}^i_j$ are the *same* set of numbers under the canonical isomorphism $\mathcal{L}(V, V) \cong V \otimes V^* \cong T^{(1, 1)}(V)$. This is why linear maps appear as $(1, 1)$-tensors everywhere in differential geometry: the matrix and the tensor are two names for the same object. The Jacobian $\partial F^i / \partial x^j$ is a $(1, 1)$-tensor (the differential of $F$ in components), and its trace is the divergence of $F$.

**The trace is the simplest nontrivial coordinate-invariant scalar.** The trace $\delta^i_i = n$ may seem too trivial to matter, but it is the prototype of how *contraction* produces basis-independent quantities. The general principle: a contracted upper-lower index pair gives a basis-independent scalar; without contraction, no basis-independent scalar can be extracted from $W^i_j$ alone (the matrix entries are basis-dependent). This is the algebraic foundation of the trace, the determinant, the characteristic polynomial coefficients, and ultimately the scalar curvature of a Riemannian manifold — all of which are contractions of various tensorial constructions.

**Verifying tensoriality of an algebraic-looking object is usually a one-line check.** For $W_{\mathrm{id}}$, the bilinearity of $\omega(v)$ in its two arguments is immediate from the definition of "$\omega$ is a linear functional on $V$". For more complex objects, the same logic applies: write the candidate as a function of vectors and covectors, check linearity in each, done. The lemma converts every "is this a tensor?" question into a one-line check — the simplest application being the present exercise.
