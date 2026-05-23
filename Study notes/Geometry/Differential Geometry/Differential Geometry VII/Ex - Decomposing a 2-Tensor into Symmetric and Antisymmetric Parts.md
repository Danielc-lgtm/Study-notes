---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Covariant Tensor on a Vector Space"
  - "Def - Symmetric Tensor Field"
  - "Def - Alternating Tensor Field"
  - "Thm - Symmetrization and Alternation Projectors"
tags: [geometry, differential-geometry, decomposition]
---

# Problem Statement

Let $V$ be a finite-dimensional real vector space and $\beta \in T^2(V^*)$ a covariant 2-tensor on $V$.

**(a)** Show that $\beta$ decomposes uniquely as
$$\beta = \alpha + \omega, \qquad \alpha \in \Sigma^2(V^*),\ \omega \in \Lambda^2(V^*),$$
where $\alpha$ is symmetric and $\omega$ is alternating.

**(b)** Identify $\alpha$ and $\omega$ explicitly: $\alpha = \mathrm{Sym}\,\beta, \omega = \mathrm{Alt}\,\beta$.

**(c)** Verify the projector identities $\mathrm{Sym}^2 = \mathrm{Sym}, \mathrm{Alt}^2 = \mathrm{Alt}$, and $\mathrm{Sym} \circ \mathrm{Alt} = \mathrm{Alt} \circ \mathrm{Sym} = 0$.

**(d)** Show that the decomposition $T^k(V^*) = \Sigma^k(V^*) \oplus \Lambda^k(V^*)$ **fails** for $k = 3$: exhibit a tensor $\tau \in T^3(V^*)$ that is neither symmetric nor alternating, nor a sum of a symmetric tensor and an alternating one. (Take $V = \mathbb{R}^n$ with $n \geq 2$.)

**Recall:**

A [[Def - Covariant Tensor on a Vector Space|covariant k-tensor]] on $V$ is a $k$-multilinear map $V^k \to \mathbb{R}$. A [[Def - Symmetric Tensor Field|symmetric tensor]] satisfies $\alpha(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = \alpha(v_1, \dots, v_k)$ for all $\sigma \in S_k$; an [[Def - Alternating Tensor Field|alternating tensor]] satisfies $\omega(v_{\sigma(1)}, \dots, v_{\sigma(k)}) = (\operatorname{sgn}\sigma)\,\omega(v_1, \dots, v_k)$.

The [[Thm - Symmetrization and Alternation Projectors|symmetrization and alternation projectors]] are $\mathrm{Sym}, \mathrm{Alt} : T^k(V^*) \to T^k(V^*)$, with $\mathrm{Sym}\,\beta = \frac{1}{k!}\sum_\sigma \sigma \cdot \beta$ and $\mathrm{Alt}\,\beta = \frac{1}{k!}\sum_\sigma (\operatorname{sgn}\sigma) \cdot \sigma \cdot \beta$.

---

# Convergent Strategy

**Problem class.** This is a *direct application of the symmetrization and alternation projectors* problem. The chapter's [[Differential Geometry VII — Tensors and Tensor Fields#Problem-Solving Strategy|problem-solving strategy]] says: when working with symmetry classes, apply the appropriate projector and verify the projector identities. Here we additionally verify that the decomposition is *complete* for $k = 2$ and *fails* for $k = 3$.

**Assumption pattern.** Two hypotheses: $\beta$ is an arbitrary covariant 2-tensor on $V$ (so we cannot rely on any special symmetry of $\beta$); the symmetrization and alternation projectors are linear and idempotent (proved in [[Thm - Symmetrization and Alternation Projectors]]).

**Theorem routing.** For (a) and (b), apply [[Thm - Symmetrization and Alternation Projectors|Lemma 4]] (the decomposition for $k = 2$): $\beta = \mathrm{Sym}\,\beta + \mathrm{Alt}\,\beta$ uniquely. For (c), the projector identities are exactly [[Thm - Symmetrization and Alternation Projectors|Lemmas 1–3]] of that theorem. For (d), construct an explicit counterexample on $V = \mathbb{R}^2$ that demonstrates the failure of the decomposition for $k = 3$.

**Key decision point.** The non-obvious step is (d): constructing a tensor $\tau \in T^3(V^*)$ with $\mathrm{Sym}\,\tau = 0 = \mathrm{Alt}\,\tau$ but $\tau \neq 0$. The natural attempt is to take $\tau = \varepsilon^1 \otimes \varepsilon^2 \otimes \varepsilon^2$, but this has nontrivial $\mathrm{Sym}\,\tau$ (averaging over $S_3$ gives a symmetric tensor with components in all six positions). The trick is to use *antisymmetric pairs of indices*: consider $\tau = \varepsilon^1 \otimes \varepsilon^2 \otimes \varepsilon^2 - \varepsilon^2 \otimes \varepsilon^1 \otimes \varepsilon^2$, which is antisymmetric in slots 1 and 2 (the first $\varepsilon^1, \varepsilon^2$) but has $\varepsilon^2$ repeated in slots 2 and 3 (or 1 and 3), making it fail to be either fully symmetric or fully antisymmetric.

---

# Legal Operations Used

From [[Differential Geometry VII — Tensors and Tensor Fields#Legal Operations|the topic page's Legal Operations]]:

1. **Symmetrize or alternate a covariant tensor** (operation 7). The central operation: apply $\mathrm{Sym}$ and $\mathrm{Alt}$ to $\beta$, verify their image.

2. **Take the tensor product of two tensor fields** (operation 1). Used in constructing the counterexample in part (d).

3. **Compute components in a chart** (operation 3). Components of $\mathrm{Sym}\,\beta$ and $\mathrm{Alt}\,\beta$ are computed from those of $\beta$.

---

# Hints

> [!note]- Hint 1
> For (a) and (b), define $\alpha(v, w) = \frac{1}{2}(\beta(v, w) + \beta(w, v))$ and $\omega(v, w) = \frac{1}{2}(\beta(v, w) - \beta(w, v))$. Verify $\alpha$ is symmetric, $\omega$ is alternating, and $\alpha + \omega = \beta$. For uniqueness, use the [[Def - Dimension|dimension]] argument: $\dim T^2(V^*) = n^2 = \binom{n+1}{2} + \binom{n}{2} = \dim \Sigma^2(V^*) + \dim \Lambda^2(V^*)$.

> [!note]- Hint 2
> For (c), $\mathrm{Sym}^2 = \mathrm{Sym}$ because applying $\mathrm{Sym}$ to a symmetric tensor gives back the same tensor. $\mathrm{Sym} \circ \mathrm{Alt} = 0$ because applying $\mathrm{Sym}$ to an alternating tensor gives the *signed* average over $S_k$ of an alternating tensor — and the sum of signs of all permutations is zero.

> [!note]- Hint 3
> For (d), the key insight is that for $k \geq 3$, the symmetric [[Def - Group|group]] $S_k$ has irreducible representations beyond the trivial (giving symmetric) and the sign (giving alternating). Look for a tensor that lies in one of these *mixed* representations. A specific construction on $\mathbb{R}^2$: $\tau = \varepsilon^1 \otimes \varepsilon^2 \otimes \varepsilon^2 - \varepsilon^2 \otimes \varepsilon^1 \otimes \varepsilon^2$. Compute $\mathrm{Sym}\,\tau$ and $\mathrm{Alt}\,\tau$ explicitly and check both vanish.

---

# Solution

The proof breaks into four parts. (a), (b), (c) establish the decomposition for $k = 2$ via direct computation. (d) shows the failure for $k = 3$ via counterexample.

**Step (a) + (b): The decomposition for $k = 2$.**

Set $\alpha = \mathrm{Sym}\,\beta$ and $\omega = \mathrm{Alt}\,\beta$. Then $\alpha + \omega = \beta$, with $\alpha$ symmetric and $\omega$ alternating.

> [!note]- Derivation
> Define
> $$\alpha(v, w) := \mathrm{Sym}\,\beta(v, w) = \frac{1}{2}(\beta(v, w) + \beta(w, v)),$$
> $$\omega(v, w) := \mathrm{Alt}\,\beta(v, w) = \frac{1}{2}(\beta(v, w) - \beta(w, v)).$$
>
> *$\alpha$ is symmetric:* $\alpha(w, v) = \frac{1}{2}(\beta(w, v) + \beta(v, w)) = \alpha(v, w)$.
>
> *$\omega$ is alternating:* $\omega(w, v) = \frac{1}{2}(\beta(w, v) - \beta(v, w)) = -\omega(v, w)$.
>
> *$\alpha + \omega = \beta$:* $\alpha(v, w) + \omega(v, w) = \frac{1}{2}(\beta(v, w) + \beta(w, v)) + \frac{1}{2}(\beta(v, w) - \beta(w, v)) = \beta(v, w)$.
>
> *Uniqueness:* if $\beta = \alpha + \omega = \alpha' + \omega'$ with $\alpha, \alpha' \in \Sigma^2(V^*)$ and $\omega, \omega' \in \Lambda^2(V^*)$, then $\alpha - \alpha' = \omega' - \omega$. The left side is symmetric, the right side is alternating. A tensor that is both symmetric and alternating satisfies $\alpha(v, w) = \alpha(w, v) = -\alpha(v, w)$, hence $\alpha = 0$. So $\alpha = \alpha'$ and $\omega = \omega'$.
>
> Thus $T^2(V^*) = \Sigma^2(V^*) \oplus \Lambda^2(V^*)$, with the unique decomposition $\beta = \mathrm{Sym}\,\beta + \mathrm{Alt}\,\beta$. The dimension count agrees: $\dim T^2(V^*) = n^2$, $\dim \Sigma^2(V^*) = \binom{n+1}{2} = n(n+1)/2$, $\dim \Lambda^2(V^*) = \binom{n}{2} = n(n-1)/2$, sum $= n^2$. ✓

**Step (c): Projector identities.**

$\mathrm{Sym}^2 = \mathrm{Sym}, \mathrm{Alt}^2 = \mathrm{Alt}$, and $\mathrm{Sym} \circ \mathrm{Alt} = 0$.

> [!note]- Derivation
> *$\mathrm{Sym}^2 = \mathrm{Sym}$:* if $\alpha = \mathrm{Sym}\,\beta$, then $\alpha$ is symmetric. So $\mathrm{Sym}\,\alpha = \alpha$, hence $\mathrm{Sym}(\mathrm{Sym}\,\beta) = \mathrm{Sym}\,\beta$.
>
> *$\mathrm{Alt}^2 = \mathrm{Alt}$:* same argument with alternating in place of symmetric.
>
> *$\mathrm{Sym} \circ \mathrm{Alt} = 0$:* let $\omega = \mathrm{Alt}\,\beta$. Then $\omega$ is alternating, so $\omega(v, w) = -\omega(w, v)$. Compute $\mathrm{Sym}\,\omega(v, w) = \frac{1}{2}(\omega(v, w) + \omega(w, v)) = \frac{1}{2}(\omega(v, w) - \omega(v, w)) = 0$.
>
> *$\mathrm{Alt} \circ \mathrm{Sym} = 0$:* symmetric argument. Let $\alpha = \mathrm{Sym}\,\beta$, with $\alpha(v, w) = \alpha(w, v)$. Then $\mathrm{Alt}\,\alpha(v, w) = \frac{1}{2}(\alpha(v, w) - \alpha(w, v)) = 0$.

**Step (d): Failure of decomposition for $k = 3$.**

On $V = \mathbb{R}^2$ with dual basis $(\varepsilon^1, \varepsilon^2)$, the tensor $\tau = \varepsilon^1 \otimes \varepsilon^2 \otimes \varepsilon^2 - \varepsilon^2 \otimes \varepsilon^1 \otimes \varepsilon^2$ has $\mathrm{Sym}\,\tau = 0 = \mathrm{Alt}\,\tau$ but $\tau \neq 0$.

> [!note]- Derivation
> *Compute $\mathrm{Sym}\,\tau$.* The symmetrization averages $\tau$ over all $\sigma \in S_3 = \{\mathrm{id}, (12), (13), (23), (123), (132)\}$ (six permutations).
>
> Write $\tau$ with components $\tau_{i_1 i_2 i_3}$. The two terms of $\tau$ are:
> - $\varepsilon^1 \otimes \varepsilon^2 \otimes \varepsilon^2$: components $\tau_{122} = 1$, all others $0$.
> - $-\varepsilon^2 \otimes \varepsilon^1 \otimes \varepsilon^2$: components $\tau_{212} = -1$, all others $0$.
>
> So $\tau$ has non-zero components: $\tau_{122} = 1, \tau_{212} = -1$, with all six other component values $\tau_{111}, \tau_{222}, \tau_{112}, \tau_{121}, \tau_{211}, \tau_{221}$ being $0$.
>
> Symmetrization: $(\mathrm{Sym}\,\tau)_{i_1 i_2 i_3} = \frac{1}{6}\sum_\sigma \tau_{i_{\sigma(1)} i_{\sigma(2)} i_{\sigma(3)}}$. The result is symmetric in the indices, i.e., it depends only on the multiset $\{i_1, i_2, i_3\}$. The only multiset with one $1$ and two $2$'s contributes from $\tau_{122} = 1$ and $\tau_{212} = -1$ (and permutations that bring other index orderings to these two — six total permutations, of which exactly three give $\tau_{122}, \tau_{212}, \tau_{221}$; but $\tau_{221}$ is also a permutation of $(1, 2, 2)$, and $\tau$ has $\tau_{221} = 0$). Hmm, let me redo this carefully.
>
> $\mathrm{Sym}\,\tau$ evaluated on the multiset $\{1, 2, 2\}$ (any of $\tau_{122}, \tau_{212}, \tau_{221}$ in the symmetrized output): the sum over all six permutations of "$(\tau$ evaluated on $(\sigma(1), \sigma(2), \sigma(3))$ for the index multiset $\{1, 2, 2\})$" equals... wait this is getting tangled.
>
> Let me redo. The clean statement: $(\mathrm{Sym}\,\tau)_{i_1 i_2 i_3} = \frac{1}{6}\sum_\sigma \tau_{i_{\sigma(1)} i_{\sigma(2)} i_{\sigma(3)}}$. Computing for $(i_1, i_2, i_3) = (1, 2, 2)$:
> $(\mathrm{Sym}\,\tau)_{122} = \frac{1}{6}[\tau_{122} + \tau_{122} + \tau_{221} + \tau_{212} + \tau_{212} + \tau_{221}] = \frac{1}{6}[\tau_{122} + \tau_{122} + 0 + \tau_{212} + \tau_{212} + 0] = \frac{1}{6}[2 \cdot 1 + 0 + 2 \cdot (-1) + 0] = 0$.
>
> By the symmetry under permutation, $(\mathrm{Sym}\,\tau)_{212} = (\mathrm{Sym}\,\tau)_{221} = (\mathrm{Sym}\,\tau)_{122} = 0$. All other components of $\mathrm{Sym}\,\tau$ vanish because $\tau$ has zero entries on other multisets. So $\mathrm{Sym}\,\tau = 0$.
>
> *Compute $\mathrm{Alt}\,\tau$.* The antisymmetrization $\mathrm{Alt}\,\tau$ vanishes whenever any two indices coincide (by the alternation property). Since both terms of $\tau$ have $\varepsilon^2$ repeated (in slots 2,3 of the first term and slots 1,3 of the second), every component of $\mathrm{Alt}\,\tau$ corresponds to a multiset with a repeated index, hence vanishes.
>
> More carefully: $(\mathrm{Alt}\,\tau)_{i_1 i_2 i_3} = \frac{1}{6}\sum_\sigma (\operatorname{sgn}\sigma)\, \tau_{i_{\sigma(1)} i_{\sigma(2)} i_{\sigma(3)}}$. For this to be nonzero, we need at least one ordering of indices that gives a nonzero component of $\tau$. The only nonzero components of $\tau$ are $\tau_{122}$ and $\tau_{212}$, both having index multiset $\{1, 2, 2\}$ (with a repetition). So $(\mathrm{Alt}\,\tau)_{i_1 i_2 i_3}$ is potentially nonzero only when $(i_1, i_2, i_3)$ is a permutation of $(1, 2, 2)$. But $\mathrm{Alt}\,\tau$ is alternating, so if any two of $i_1, i_2, i_3$ are equal, the result is $0$. The multiset $\{1, 2, 2\}$ has $i_2 = i_3 = 2$ in any ordering, so $(\mathrm{Alt}\,\tau) = 0$ for all such index tuples. Hence $\mathrm{Alt}\,\tau = 0$.
>
> *But $\tau \neq 0$.* The component $\tau_{122} = 1 \neq 0$, so $\tau$ itself is a nonzero tensor.
>
> *Conclusion:* $\mathrm{Sym}\,\tau + \mathrm{Alt}\,\tau = 0 \neq \tau$, hence $\tau$ is **not** in $\Sigma^3 + \Lambda^3$, demonstrating that $T^3(V^*) \supsetneq \Sigma^3(V^*) \oplus \Lambda^3(V^*)$ for $V = \mathbb{R}^2$. The same example works for $V = \mathbb{R}^n$ with $n \geq 2$.

> [!note]- Complete formal solution
> *Steps (a) and (b).* Define $\alpha = \mathrm{Sym}\,\beta$ and $\omega = \mathrm{Alt}\,\beta$ via $\alpha(v, w) = \frac{1}{2}(\beta(v, w) + \beta(w, v))$ and $\omega(v, w) = \frac{1}{2}(\beta(v, w) - \beta(w, v))$. Direct verification: $\alpha$ is symmetric, $\omega$ is alternating, $\alpha + \omega = \beta$. Uniqueness: if $\beta = \alpha + \omega = \alpha' + \omega'$, then $\alpha - \alpha' = \omega' - \omega$ is both symmetric and alternating, hence zero.
>
> *Step (c).* $\mathrm{Sym}^2 = \mathrm{Sym}$ because $\mathrm{Sym}$ fixes symmetric tensors. Similarly $\mathrm{Alt}^2 = \mathrm{Alt}$. The mixed products $\mathrm{Sym} \circ \mathrm{Alt} = \mathrm{Alt} \circ \mathrm{Sym} = 0$ by direct computation: applying $\mathrm{Sym}$ to an alternating tensor symmetrizes it, and symmetrizing an alternating tensor cancels (each value gets paired with its negation under transposition, averaging to zero).
>
> *Step (d).* On $V = \mathbb{R}^2$, the tensor $\tau = \varepsilon^1 \otimes \varepsilon^2 \otimes \varepsilon^2 - \varepsilon^2 \otimes \varepsilon^1 \otimes \varepsilon^2$ has components $\tau_{122} = 1, \tau_{212} = -1$ (all others zero). $\mathrm{Sym}\,\tau = 0$ because the symmetrization of $\tau_{122} = 1$ and $\tau_{212} = -1$ contributes opposite signs that cancel. $\mathrm{Alt}\,\tau = 0$ because both nonzero components of $\tau$ have a repeated index $2$, and alternation kills repeated indices. But $\tau \neq 0$. Hence $T^3(\mathbb{R}^{2*}) \supsetneq \Sigma^3 \oplus \Lambda^3$. $\blacksquare$

---

# Key Takeaways

**The $k = 2$ decomposition is special — it does not generalize.** For $k = 2$, every covariant tensor decomposes uniquely as a sum of a symmetric and an alternating part. This is a *finite-dimensional miracle*: $S_2 = \{\mathrm{id}, \tau\}$ has only two irreducible representations (trivial and sign), and they are the only ones available. For $k \geq 3$, $S_k$ has additional irreducibles (the "standard" representation for $k = 3$, more for larger $k$), and tensors in those irreducible components are *neither* symmetric *nor* alternating. The general decomposition is the **Young decomposition**, with one summand for each partition of $k$ — and $\Sigma^k$ and $\Lambda^k$ are only two of the summands. The lesson: do not naively extend the $k = 2$ decomposition to higher rank.

**Symmetrization and alternation are orthogonal projections, not direct-sum complements (for $k \geq 3$).** The projectors $\mathrm{Sym}, \mathrm{Alt}$ are idempotent and satisfy $\mathrm{Sym} \circ \mathrm{Alt} = 0$ — they are projections whose images are mutually exclusive. But their *sum* $\mathrm{Sym} + \mathrm{Alt}$ is the identity only for $k \leq 2$; for $k \geq 3$, $\mathrm{Sym} + \mathrm{Alt}$ is a projection onto a *proper* [[Def - Subspace|subspace]] of $T^k(V^*)$. The complement contains the "mixed" Young-tableau tensors. This is the algebraic content of the assertion that $T^k = \Sigma^k \oplus \Lambda^k$ holds only for $k \leq 2$.

**The $k = 2$ decomposition has direct physical content.** Every covariant 2-tensor on a manifold (a "bilinear form field") decomposes into a symmetric part (a metric-like object) and an alternating part (a 2-form-like object). Examples: the gradient of a vector field (technically a $(1, 1)$-tensor, but the same decomposition applies via metric-lowering) decomposes into the *rate of strain* (symmetric part) and the *vorticity* (antisymmetric part) in fluid dynamics. A non-symmetric matrix decomposes into its symmetric part and its antisymmetric part. This decomposition is the algebraic basis of half of continuum mechanics. The fact that it generalizes only partially to higher rank is part of the reason higher-rank tensors are harder to interpret.

**Young decomposition is the right generalization.** For $k \geq 3$, the proper decomposition uses **Young symmetrizers** $c_\lambda$, one for each partition $\lambda$ of $k$. The result is $T^k(V^*) = \bigoplus_\lambda c_\lambda(T^k(V^*))$, with $\Sigma^k$ corresponding to $\lambda = (k)$ (the trivial representation), $\Lambda^k$ to $\lambda = (1^k)$ (the sign representation), and the "mixed" parts to other Young diagrams. This is the bridge to **Schur-Weyl duality** and the representation theory of $GL(V)$ — a deep area of representation theory crucial in the analysis of higher-rank curvature tensors (e.g., the Weyl tensor as the trace-free part of Riemann, sitting in a specific Young-diagram component of $T^4(V^*)$).
