---
type: definition
subject: special-relativity
prereqs:
  - "Def - Tensors on Minkowski Space"
  - "Def - Metric Duality and Index Manipulation"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use $\eta = \mathrm{diag}(1,-1,-1,-1)$. As on [[Def - Tensors on Minkowski Space]], $\mathscr{T}_{(k,\ell)}(E)$ is the space of type-$(k,\ell)$ tensors on the vector space $E$ underlying [[Def - Minkowski Space and the Metric|Minkowski space]]; a basis is $(e_\alpha)$ with dual basis $(e^\alpha)$, $\langle e^\alpha, e_\beta\rangle = \delta^\alpha{}_\beta$. The metric components are $g_{\alpha\beta}$ (orthonormal: $\eta_{\alpha\beta}$), with inverse $g^{\alpha\beta}$. The Einstein convention sums an index appearing once up, once down. Full registry on [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality]].

This is a compound page: it defines three interlocking operations — the **tensor product** $\otimes$, **contraction**, and **metric duality on tensors** (raising and lowering with $g$) — because together they generate the entire tensor algebra, and none is fully usable without the others.

---

# Axiom Motivation

A single tensor, no matter how clearly defined, is inert. What makes [[Def - Tensors on Minkowski Space|tensors]] the working language of physics is that they form a *closed algebra*: there are operations that build new tensors from old ones, and every relativistic manipulation — contracting a four-velocity with the metric, forming the field-strength from a potential, taking the trace of a Lorentz transformation — is some composite of three primitive moves. The motivation for this page is to isolate those three moves and explain why each is forced.

The first move answers "how do I combine two tensors into a bigger one?" The natural answer is the **tensor product**: given $A$ of type $(k,\ell)$ and $B$ of type $(m,n)$, feed the first batch of arguments to $A$, the second to $B$, and multiply the results. This is the unique way to combine them that stays multilinear in every slot and respects the slot structure. It is forced by the demand that the components multiply: $(A\otimes B)^{\dots}{}_{\dots} = A^{\dots}{}_{\dots}\,B^{\dots}{}_{\dots}$, which is what lets one *write down* tensors of any valence from low-valence pieces — the field-strength two-form is built this way from one-forms, the metric is built from dual-basis forms. Without a product there would be no way to ascend in valence, and the whole expansion $T = T^{\dots}{}_{\dots}\, e_{\alpha_1}\otimes\cdots\otimes e^{\beta_\ell}$ would be meaningless.

The second move answers "how do I go *down* in valence?" The tensor product only builds up. To collapse two slots one needs **contraction**: pick one upper slot and one lower slot, plug in a running basis vector and its dual form, and sum. The result is a tensor of valence two less. The reason it must be one upper and one lower — never two of the same kind — is invariance: an upper index transforms by $P^{-1}$ and a lower index by $P$, so a sum over an up–down pair has its $P^{-1}$ and $P$ cancel, leaving something basis-independent; a sum over two upper indices would carry an uncancelled $P^{-1}P^{-1}$ and depend on the frame, which is Tong's "illegal" $X^\mu X^\mu$. Contraction is precisely the operation whose well-definedness *requires* the up–down pairing, and that pairing is the syntactic rule of the entire calculus.

The third move answers "what if my indices are in the wrong position to contract?" Suppose I have $X^\mu$ and $Y^\mu$ and want their invariant inner product, but contraction needs one of them lowered. The metric supplies the conversion. Because $g$ is **non-degenerate**, [[Def - Metric Duality and Index Manipulation|metric duality]] gives a canonical isomorphism $E \cong E^*$, and in components it lowers an index, $X_\mu = g_{\mu\nu}X^\nu$, or raises one, $X^\mu = g^{\mu\nu}X_\nu$. The non-degeneracy is exactly what makes this an isomorphism rather than a lossy projection — a degenerate "metric" would have a kernel, the map $E \to E^*$ would fail to be injective, and there would be no clean raising and lowering (which is why Newtonian spacetime, with its degenerate temporal "metric," has no such calculus). With duality in hand, any two slots can be brought into up–down position, so contraction becomes universally applicable, and the inner product $X\cdot Y = g_{\mu\nu}X^\mu Y^\nu = X_\mu Y^\mu$ is just "lower then contract."

These three together are not an arbitrary toolkit; they are a generating set. The reason there are exactly three is structural: $\otimes$ raises valence, contraction lowers it, and duality moves indices between the up and down positions without changing valence — between them they reach every position in the lattice of tensor types from any starting point. Anything you can legally write with indices — Tong's whole "indices up, indices down" discipline — is a composite of these three.

---

# The Definition

**Tensor product.** Given $A \in \mathscr{T}_{(k,\ell)}(E)$ and $B \in \mathscr{T}_{(m,n)}(E)$, their **tensor product** $A \otimes B \in \mathscr{T}_{(k+m,\,\ell+n)}(E)$ is
$$
(A\otimes B)(\omega_1, \dots, \omega_{k+m}, \vec v_1, \dots, \vec v_{\ell+n}) = A(\omega_1, \dots, \omega_k, \vec v_1, \dots, \vec v_\ell)\cdot B(\omega_{k+1}, \dots, \omega_{k+m}, \vec v_{\ell+1}, \dots, \vec v_{\ell+n}),
$$
where $\cdot$ is multiplication in $\mathbb{R}$. It is **associative**, $A\otimes(B\otimes C) = (A\otimes B)\otimes C$, but **not commutative** in general. In components it multiplies components: e.g. for two linear forms, $(\omega_1\otimes\omega_2)(\vec v, \vec w) = \langle\omega_1, \vec v\rangle\langle\omega_2, \vec w\rangle$, with components $(\omega_1\otimes\omega_2)_{\alpha\beta} = (\omega_1)_\alpha(\omega_2)_\beta$.

**Contraction.** For $T \in \mathscr{T}_{(k,\ell)}(E)$ with $k \geq 1$ and $\ell \geq 1$, and integers $p \in \{1,\dots,k\}$, $q \in \{1,\dots,\ell\}$, the **contraction on the indices of rank $p$ and $q$** is the tensor $C^p_q T \in \mathscr{T}_{(k-1,\ell-1)}(E)$ defined by inserting a running dual-basis form $e^\alpha$ in the $p$-th upper slot, the matching basis vector $e_\alpha$ in the $q$-th lower slot, and summing over $\alpha$:
$$
(C^p_q T)(\omega_1, \dots, \omega_{k-1}, \vec v_1, \dots, \vec v_{\ell-1}) = T(\omega_1, \dots, \underset{p}{e^\alpha}, \dots, \omega_{k-1}, \vec v_1, \dots, \underset{q}{e_\alpha}, \dots, \vec v_{\ell-1}).
$$
The definition is **independent of the basis** $(e_\alpha)$ (the $P^{-1}$ from the up-slot and $P$ from the down-slot cancel). In components it sets the two chosen indices equal and sums:
$$
(C^p_q T)^{\alpha_1\dots\alpha_{k-1}}{}_{\beta_1\dots\beta_{\ell-1}} = T^{\alpha_1\dots\,\mu\,\dots\alpha_{k-1}}{}_{\beta_1\dots\,\mu\,\dots\beta_{\ell-1}},
$$
the summation index $\mu$ sitting in the $p$-th upper and $q$-th lower position. For a type $(1,1)$ tensor the only contraction is the **trace**: $C^1_1 T = T^\mu{}_\mu$; in particular $C^1_1(\vec v\otimes\omega) = v^\mu\omega_\mu = \langle\omega, \vec v\rangle$.

**Metric duality on tensors.** Because $g$ is non-degenerate, indices are **lowered** with $g_{\alpha\beta}$ and **raised** with the inverse $g^{\alpha\beta}$ (where $g^{\alpha\rho}g_{\rho\beta} = \delta^\alpha{}_\beta$):
$$
v_\alpha = g_{\alpha\beta}\, v^\beta, \qquad \omega^\alpha = g^{\alpha\beta}\,\omega_\beta,
$$
and the same rule applies one $g$ per index to a tensor of any rank — for example $T^\mu{}_\nu = g_{\nu\rho}T^{\mu\rho} = g^{\mu\sigma}T_\sigma{}^\rho g_{\rho\nu}$. Raising then lowering the same index returns the original tensor. The operation **commutes with contraction**, so all index manipulations may be performed in any order. The inverse metric $g^{-1} = g^{\alpha\beta}\, e_\alpha\otimes e_\beta$ is itself the type-$(2,0)$ tensor that performs the raising.

---

# Categorical / Structural Definition

The tensor product on tensors is the bilinear map $\mathscr{T}_{(k,\ell)} \times \mathscr{T}_{(m,n)} \to \mathscr{T}_{(k+m,\ell+n)}$ induced by the [[Thm - Universal Property of the Tensor Product|universal property]]: it is the unique bilinear operation making $\bigoplus_{k,\ell}\mathscr{T}_{(k,\ell)}(E)$ into an associative graded algebra (the **tensor algebra** of $E \oplus E^*$, with grading by valence). Under the identification $\mathscr{T}_{(k,\ell)}(E) \cong E^{\otimes k}\otimes (E^*)^{\otimes \ell}$, the operation $\otimes$ is literally the tensor product of vector spaces concatenating factors, which is why it is associative and bilinear by construction.

Contraction is the **evaluation pairing** $E \otimes E^* \to \mathbb{R}$, $\vec v\otimes\omega \mapsto \langle\omega, \vec v\rangle$, applied to a chosen pair of factors and tensored with the identity on the rest. This pairing is the canonical map exhibiting $E^*$ as the dual of $E$; its basis-independence is the basis-independence of "evaluate a form on a vector." The general contraction $C^p_q$ is this single evaluation, threaded through the $p$-th $E$-factor and $q$-th $E^*$-factor of the tensor-product space.

Metric duality is the isomorphism $\Phi_g : E \xrightarrow{\sim} E^*$, $\Phi_g(\vec v) = g(\vec v, \cdot)$, extended factor-by-factor to all of $\mathscr{T}_{(k,\ell)}(E)$. In representation-theoretic terms, $\Phi_g$ is the intertwiner realising the equivalence between the defining and dual representations of the [[Def - The Lorentz Group|Lorentz group]] that the invariant form $g$ provides; raising and lowering are the action of this intertwiner on individual factors, which is why they preserve the abstract tensor while relabelling its index positions. The three operations are thus, structurally: concatenation of factors ($\otimes$), the evaluation counit ($E\otimes E^* \to \mathbb{R}$, contraction), and the metric intertwiner ($E \cong E^*$, duality).

---

# Relate to Other Fields / Compression

These are the three operations of **multilinear algebra** specialised to a space with a non-degenerate form. In a general (non-metric) vector space only $\otimes$ and contraction exist; the metric is what adds raising and lowering, which is exactly the extra structure that distinguishes a *geometry* from a bare vector space. In quantum mechanics the same trio appears as: tensor product of Hilbert spaces (composite systems), partial trace (contraction over a subsystem), and the Riesz isomorphism $|\psi\rangle \leftrightarrow \langle\psi|$ (metric duality via the inner product). The relativistic calculus and the bra–ket calculus are the same multilinear algebra wearing different notation.

**True name:** the three operations are *concatenate (⊗), evaluate-and-sum (contract), and convert (raise/lower with $g$)*. The reflex each installs: when you need a higher-valence object, build it with $\otimes$; when an expression has a repeated up–down index, that is a contraction and it lowers valence by two; when free indices do not match up-and-down across an equation, raise or lower with $g$ until they do. Tong's entire "indices up, indices down" discipline is the statement that legal expressions are exactly the ones assembled from these three moves with every summed index appearing once up and once down.

---

# Examples / Corollaries

**Is an instance — the inner product as lower-then-contract.** $X\cdot Y = g(X,Y) = g_{\mu\nu}X^\mu Y^\nu = X_\nu Y^\nu$: lower one index of $X$ with $g$, then contract against $Y$. This is the canonical composite of duality and contraction.

**Is an instance — the trace of a Lorentz transformation.** $\Lambda^\mu{}_\mu = C^1_1\Lambda$ is the trace, a Lorentz scalar (invariant). For the identity, $\delta^\mu{}_\mu = 4$ (the dimension of spacetime).

**Is an instance — building the metric from forms.** $g = g_{\alpha\beta}\, e^\alpha\otimes e^\beta$ exhibits the type-$(0,2)$ metric as a tensor-product combination of dual-basis one-forms — the simplest nontrivial use of $\otimes$.

**Is NOT an instance — contracting two upper indices.** $T^{\mu\mu}$ (sum over a repeated *upper* index) is **not** a contraction and **not** a tensor: it carries an uncancelled $(P^{-1})(P^{-1})$ under a change of basis and so is frame-dependent. The legal trace-like object is $T^\mu{}_\mu$ (one up, one down) or, if both indices are genuinely upper, first lower one with $g$: $g_{\mu\nu}T^{\mu\nu}$.

**Is NOT an instance — copying components when lowering.** Setting $X_\mu = X^\mu$ (same four numbers) is wrong in mostly-minus signature: lowering gives $X_0 = X^0$ but $X_i = -X^i$. The check is $X_\mu X^\mu = (X^0)^2 - |\mathbf X|^2$, not $(X^0)^2 + |\mathbf X|^2$.

**Corollary — raise-then-lower is the identity.** $g_{\mu\nu}g^{\nu\rho}X_\rho = \delta_\mu{}^\rho X_\rho = X_\mu$. The two operations are mutually inverse because $g$ and $g^{-1}$ are inverse matrices.

**Corollary — contraction is a scalar when it removes all indices.** Contracting a type $(1,1)$ tensor to type $(0,0)$ yields a real number, frame-independent: $T^\mu{}_\mu$ is the same in every basis, which is the special case $k=\ell=1$ of the invariance built into every contraction.

**Calibration check.** If you have understood the operations you can: (i) write $X\cdot Y$ as a composite of one lowering and one contraction; (ii) explain why $T^\mu{}_\mu$ is a scalar but $T^{\mu\mu}$ is not even a tensor; (iii) compute $\delta^\mu{}_\mu = 4$ and $g_{\mu\nu}g^{\mu\nu} = 4$.

---

# Unlocked by This

> [!tip] The Exterior Product as Antisymmetrised Tensor Product *(from §18.2)*
> The [[Def - Alternate Forms and the Exterior Product|wedge product]] $\wedge$ of forms is the antisymmetrisation of $\otimes$: for one-forms $a\wedge b = a\otimes b - b\otimes a$. The whole exterior algebra sits inside the tensor algebra as the fully antisymmetric part, with $\wedge$ the operation $\otimes$ followed by antisymmetrisation.

> [!tip] The Hodge Star Built from $\varepsilon$ and $g^{-1}$ *(from §18.3)*
> The [[Def - The Hodge Star|Hodge star]] $\star$ is constructed entirely from these operations: it contracts a $p$-form against the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]] $\varepsilon$ after raising the $p$-form's indices with $g^{-1}$. It is "contract a form into $\varepsilon$ using metric duality," and nothing more.

> [!tip] Covariant Differentiation Preserves the Tensor Operations *(from General Relativity)*
> On a manifold the [[Def - The Covariant Derivative|covariant derivative]] $\nabla$ is the unique differentiation that commutes with contraction and (for the metric connection) annihilates $g$, so that $\nabla$ commutes with raising and lowering. This compatibility, $\nabla g = 0$, is what lets index gymnastics pass freely through derivatives — the cornerstone of tensor calculus on curved spacetime; see [[Special Relativity XIX — Fields on Spacetime and the Covariant Derivative]].
