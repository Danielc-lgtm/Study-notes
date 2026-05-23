---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Inner Product Space"
  - "Def - Linear Map"
  - "Thm - Riesz Representation Theorem (Finite-Dimensional)"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $V$ and $W$ are finite-dimensional [[Def - Inner Product Space|inner product spaces]] over $\mathbb{F} \in \{\mathbb{R}, \mathbb{C}\}$. The inner product on $V$ is $\langle \cdot, \cdot \rangle_V$, linear in the first slot and conjugate-linear in the second (Axler's convention); similarly for $W$. The space of linear maps $V \to W$ is $\mathcal{L}(V, W)$, and $\mathcal{L}(V) = \mathcal{L}(V, V)$. The adjoint of a linear map $T \in \mathcal{L}(V, W)$ is denoted $T^*$; with respect to orthonormal bases on $V$ and $W$, the matrix of $T^*$ is the **conjugate transpose** $A^*$ of the matrix $A$ of $T$, defined by $(A^*)_{jk} = \overline{A_{kj}}$. Over $\mathbb{R}$, the conjugate transpose is just the transpose $A^t$. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the full notation registry.

> [!warning] Convention: linearity slot of the inner product.
> Under Axler's convention $\langle \alpha v, w \rangle = \alpha \langle v, w \rangle$ — linear in the first argument. Under the physics convention (linear in the second), the defining relation of the adjoint flips conjugation: $\langle v, Tw \rangle = \langle T^* v, w \rangle$, with the same content but mirrored notation. The bilinear-form / sesquilinear-form distinction does not affect existence or uniqueness of the adjoint.

---

# Axiom Motivation

The right way to read the definition of the adjoint is to ask: *given* a linear map $T : V \to W$ and the inner products on $V$ and $W$, what is the most natural map $W \to V$ that the data forces upon us? There is exactly one, and it is the adjoint.

Imagine you have the inner product $\langle Tv, w \rangle_W$ — a number, depending on $v$ and $w$ — and you want to think of it as an inner product on $V$ instead, with one slot replaced. That is, you want a vector $T^* w \in V$ such that

$$\langle Tv, w \rangle_W = \langle v, T^* w \rangle_V \quad \text{for all } v \in V.$$

This rephrasing is not a luxury — it is the only way to *transfer* information about the action of $T$ on $V$ into a statement living in $W$, and vice versa. Without the adjoint, you cannot write "the orthogonal complement of the range of $T$" as the kernel of a map — yet that identification is one of the most useful tools in the chapter ($\operatorname{null} T^* = (\operatorname{range} T)^{\perp}$). The adjoint is the bridge between the "primal" world of $V$ and the "dual" world of $W$.

Why does the adjoint exist? Fix $w \in W$. The expression $\langle Tv, w \rangle_W$, viewed as a function of $v$, is *linear* in $v$ — composition of $T$ with the linear functional $\langle \cdot, w \rangle_W$ on $W$. So we have a linear functional $\varphi_w : V \to \mathbb{F}$ defined by $\varphi_w(v) = \langle Tv, w \rangle_W$. The [[Thm - Riesz Representation Theorem (Finite-Dimensional)|Riesz representation theorem]] says every linear functional on a finite-dimensional inner product space is uniquely of the form $v \mapsto \langle v, u \rangle$ for some $u \in V$. Apply Riesz to $\varphi_w$ and you get a unique $u \in V$ — call it $T^* w$ — such that $\varphi_w(v) = \langle v, T^* w \rangle_V$, that is, $\langle Tv, w \rangle_W = \langle v, T^* w \rangle_V$. This produces $T^* w$ for each $w \in W$, and a short check shows the assignment $w \mapsto T^* w$ is linear. The adjoint is thus *forced* upon us by Riesz applied slot-by-slot.

What if you tried to drop the linearity of $T$? Then $\varphi_w$ is no longer linear, Riesz does not apply, and no canonical $T^* w$ exists. What if you tried to drop the inner product structure and work with a general bilinear form? Then "linear functional" loses its meaning relative to that form unless the form is non-degenerate, and even then the resulting "adjoint" depends on the form — see the bridge to dual spaces below. Without the inner product, the adjoint reduces to the [[Def - Dual Map|dual map]] $T' : W' \to V'$ on dual spaces; the inner product is what lets us identify $V$ with $V'$ and so realise the dual map on $V$ itself rather than on $V'$.

A subtle but consequential consequence of the definition: conjugate-linearity in $T$. The relation $\langle Tv, w \rangle = \langle v, T^* w \rangle$ together with the conjugate-linearity of $\langle \cdot, \cdot \rangle$ in the second slot gives $(\alpha T)^* = \overline{\alpha} \, T^*$, *not* $\alpha T^*$. Over $\mathbb{R}$ the conjugation is invisible and the operation is linear; over $\mathbb{C}$ this is the first place students stumble. The conjugation is what makes "transpose conjugate" — the matrix expression of the adjoint — a sensible operation: under it, $(\alpha A)^* = \overline{\alpha} A^*$, exactly matching the operator-level statement.

Finally, a remark on why the relation $\langle Tv, w \rangle = \langle v, T^* w \rangle$, with $v$ free and $w$ free, is the right characterisation. One could imagine instead defining the adjoint by the relation with $v = w$ — but that under-determines the adjoint, because the inner product is determined by its values on the diagonal only up to a complex sign in general, and only via the polarisation identity (see [[Ex - Inner product determined by norm via the polarization identity]] in [[Linear Algebra VI — §6 Inner Product Spaces|Linear Algebra VI]]). So the right definition demands the relation hold for all $v$ and all $w$. The all-$v$-all-$w$ form is then equivalent (over $\mathbb{C}$, via polarisation; over $\mathbb{R}$, via the symmetric bilinear form) to the diagonal form $\langle Tv, v \rangle = \langle v, T^* v \rangle$, but the off-diagonal form is the right one to *state* the definition.

---

# The Definition

Let $T \in \mathcal{L}(V, W)$. The **adjoint** of $T$ is the unique linear map $T^* \in \mathcal{L}(W, V)$ satisfying

$$\langle Tv, w \rangle_W = \langle v, T^* w \rangle_V \quad \text{for all } v \in V, \ w \in W.$$

Existence and uniqueness follow from the [[Thm - Riesz Representation Theorem (Finite-Dimensional)|Riesz representation theorem]] applied to the linear functional $v \mapsto \langle Tv, w \rangle_W$ for each fixed $w$.

When $V = W$ and $T = T^*$, the operator $T$ is **[[Def - Self-Adjoint Operator|self-adjoint]]**. When $T T^* = T^* T$, $T$ is **[[Def - Normal Operator|normal]]**. When $T^* T = I$, $T$ is an **[[Def - Isometry|isometry]]**.

**Matrix description.** Let $e_1, \ldots, e_n$ be an orthonormal basis of $V$ and $f_1, \ldots, f_m$ be an orthonormal basis of $W$. If $A$ is the matrix of $T$ in these bases — so $A_{jk} = \langle T e_k, f_j \rangle$ — then the matrix of $T^*$ in the bases $f_1, \ldots, f_m$ (of $W$) and $e_1, \ldots, e_n$ (of $V$) is the **conjugate transpose**

$$(A^*)_{jk} = \overline{A_{kj}}.$$

Over $\mathbb{R}$ this is the transpose $A^t$. Over $\mathbb{C}$ it is also denoted $A^H$ or $\overline{A^t}$.

---

# Categorical / Structural Definition

The adjoint is an instance of a **dagger structure** on the category of finite-dimensional inner product spaces. A dagger is a contravariant functor $\dagger : \mathcal{C}^{\text{op}} \to \mathcal{C}$ that is the identity on objects and that is involutive, $\dagger \circ \dagger = \text{id}$. In our category, objects are finite-dimensional inner product spaces, morphisms are linear maps, and the dagger is $T \mapsto T^*$. The functoriality identities $(ST)^* = T^* S^*$ and $I^* = I$, together with the involution $T^{**} = T$, are the dagger axioms (see [[Thm - Properties of the Adjoint]]).

Equivalently, the adjoint is the *unique* linear map $T^* \in \mathcal{L}(W, V)$ that makes the diagram

$$\begin{array}{c} V \xrightarrow{T} W \\ \downarrow \cong \qquad \qquad \downarrow \cong \\ V' \xleftarrow{T'} W' \end{array}$$

commute, where the vertical [[Def - Isomorphism|isomorphisms]] are the **Riesz [[Def - Isomorphism|isomorphisms]]** $v \mapsto \langle \cdot, v \rangle$ (a conjugate-linear isomorphism from $V$ to its dual $V'$), and $T'$ is the [[Def - Dual Map|dual map]]. In other words, *the adjoint is the dual map transported across the Riesz isomorphism.* This is the precise way in which the adjoint is "the dual map made concrete in $V$".

---

# Relate to Other Fields / Compression

The adjoint is the inner-product realisation of the **[[Def - Dual Map|dual map]]** from [[Linear Algebra IV — §3E–F Products, Quotients, Duality]]. The dual map $T' : W' \to V'$ between dual spaces is canonically associated to any linear map and requires no inner product; the adjoint $T^* : W \to V$ "pulls $T'$ back" along the Riesz isomorphism. Over $\mathbb{R}$ the Riesz isomorphism is a genuine linear isomorphism and the dual map and the adjoint look identical (both are realised by the transpose matrix). Over $\mathbb{C}$ the Riesz isomorphism is conjugate-linear, which is why the adjoint involves complex conjugation while the dual map does not.

In **infinite-dimensional functional analysis**, the same definition works for *bounded* linear operators between Hilbert spaces — Riesz still applies to bounded linear functionals. For *unbounded* operators, the adjoint is much more delicate: it has a domain of definition $\operatorname{dom}(T^*)$ which can be smaller than the codomain, and operators self-adjoint as bounded operators are not the same thing as self-adjoint unbounded operators. The momentum operator $\hat p = -i \hbar \frac{d}{dx}$ in quantum mechanics is unbounded, and its self-adjointness depends critically on choosing the correct domain of definition.

In **physics**, the adjoint in Dirac bra-ket notation is $\langle \psi | A^\dagger | \phi \rangle = \overline{\langle \phi | A | \psi \rangle}$ — the bar-and-flip relation, which under Axler's convention reads $\langle A^\dagger \psi, \phi \rangle = \overline{\langle \phi, A \psi \rangle}$. The physics community uniformly writes $A^\dagger$ for what mathematicians write as $A^*$, freeing the $*$ for complex conjugation of scalars.

**True name:** The adjoint is the **swap operator for the inner product slot**. The defining relation $\langle Tv, w \rangle = \langle v, T^* w \rangle$ literally says "moving $T$ from the first slot to the second slot turns it into $T^*$". Whenever in a computation you have an inner product involving $T$ and want to push $T$ to the other side of the comma, the rule is "becomes $T^*$". This is the working characterisation, and it is what one reaches for in proofs.

---

# Examples / Corollaries

The simplest example: the identity operator. $\langle Iv, w \rangle = \langle v, w \rangle = \langle v, Iw \rangle$, so $I^* = I$. The identity is its own adjoint, as one would expect of "doing nothing".

A second example: scalar multiplication. If $T = \alpha I$ for $\alpha \in \mathbb{F}$, then $\langle \alpha v, w \rangle = \alpha \langle v, w \rangle = \langle v, \overline{\alpha} w \rangle$ (using conjugate-linearity in the second slot), so $T^* = \overline{\alpha} I$. Over $\mathbb{R}$ scalars equal their adjoints; over $\mathbb{C}$ they conjugate.

A third example: a $2 \times 2$ matrix. Let $T : \mathbb{C}^2 \to \mathbb{C}^2$ have matrix $A = \begin{pmatrix} 1 & i \\ 0 & 2 \end{pmatrix}$ in the standard basis. Then $T^*$ has matrix $A^* = \begin{pmatrix} 1 & 0 \\ -i & 2 \end{pmatrix}$ — transpose, then conjugate every entry. Note that $T \neq T^*$, so $T$ is not self-adjoint; but $T T^* = \begin{pmatrix} 1 + 1 & -2i \\ 2i & 4 \end{pmatrix}$ and $T^* T = \begin{pmatrix} 1 & i \\ -i & 5 \end{pmatrix}$ are different, so $T$ is also not normal.

A subtle non-example: the unilateral shift on $\ell^2(\mathbb{N})$ (infinite-dimensional). The shift $S(x_1, x_2, x_3, \ldots) = (0, x_1, x_2, \ldots)$ has adjoint $S^*(x_1, x_2, x_3, \ldots) = (x_2, x_3, \ldots)$ — the backward shift. Then $S^* S = I$ (so $S$ is an [[Def - Isometry|isometry]]) but $S S^* \neq I$ (the projection onto the orthogonal complement of $e_1$). This shows that **in infinite [[Def - Dimension|dimensions]], $S^*S = I$ does not imply $S S^* = I$**; one needs to check both for unitary. This phenomenon does not occur in finite [[Def - Dimension|dimensions]] because an [[Def - Isometry|isometry]] $V \to V$ on a finite-dimensional space is automatically surjective.

A geometric example: orthogonal projection. The [[Def - Orthogonal Projection|orthogonal projection]] $P_U$ onto a [[Def - Subspace|subspace]] $U$ of $V$ satisfies $P_U^* = P_U$ (it is self-adjoint) and $P_U^2 = P_U$ (it is idempotent). In fact, **a projection is orthogonal if and only if it is self-adjoint** — the two characterisations of orthogonal projection coincide.

A corollary on dimensions: $\dim \operatorname{range} T = \dim \operatorname{range} T^*$. Combined with the rank-nullity theorem (which is the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]] from [[Linear Algebra III — §3A–D Linear Maps]]), this gives $\dim \operatorname{null} T - \dim V = \dim \operatorname{null} T^* - \dim W$, the **row-rank-equals-column-rank theorem** in clean form.

A non-example: the matrix of $T^*$ is *not* the conjugate transpose of the matrix of $T$ in a non-orthonormal basis. If the basis $b_1, \ldots, b_n$ has Gram matrix $G_{jk} = \langle b_j, b_k \rangle$, then the matrix of $T^*$ is $G^{-1} M^* G$, not $M^*$. Working in orthonormal bases is essential for the "conjugate transpose" shortcut.

**Calibration check.** Verify these three facts about the adjoint:
1. The adjoint reverses composition: $(ST)^* = T^* S^*$, not $S^* T^*$ — this comes from pushing both maps to the other slot of the inner product one at a time.
2. The adjoint is an involution: $T^{**} = T$. (Set $S = T^*$ in the defining relation, take the conjugate of both sides.)
3. The adjoint is conjugate-linear: $(\alpha T + \beta S)^* = \overline{\alpha} T^* + \overline{\beta} S^*$, over $\mathbb{C}$. Over $\mathbb{R}$ it is linear.

If these three identities feel mechanical to you, you have understood the definition. The full theorem stating all properties is [[Thm - Properties of the Adjoint]].

---

# Unlocked by This

> [!tip] Adjoint Functor *(from Category Theory)*
> The defining relation $\langle Tv, w \rangle = \langle v, T^* w \rangle$ has the exact shape of an adjunction between hom-functors: there is a natural isomorphism between $\operatorname{Hom}(V, W)$ pairings and $\operatorname{Hom}(W, V)$ pairings mediated by the inner product. More formally, the assignment $T \mapsto T^*$ is a **dagger structure** on the category of finite-dimensional Hilbert spaces, and the entire chapter is the theory of operators with respect to this dagger. Operators with special relations to their dagger have categorical names: self-adjoint operators ($T = T^\dagger$), unitary operators ($T T^\dagger = T^\dagger T = I$), positive operators ($T = S^\dagger S$ for some $S$). Each of these is a categorical specification, not a linear-algebraic one — they generalise to any dagger category.

> [!tip] Spectral Measure *(from Functional Analysis)*
> The adjoint of an *unbounded* operator on a Hilbert space is a subtler object than the finite-dimensional adjoint. It has its own domain of definition, $\operatorname{dom}(T^*) \subseteq W$, which can be strictly smaller than $W$ and even strictly smaller than $\operatorname{dom}(T)$. An operator is **self-adjoint as an unbounded operator** when not only $T = T^*$ on the overlap but also $\operatorname{dom}(T) = \operatorname{dom}(T^*)$ — this domain equality is a genuinely new condition. Only self-adjoint operators (in this strict sense) admit a **spectral measure** on $\mathbb{R}$, the projection-valued generalisation of an eigenbasis. The momentum and position operators in quantum mechanics are self-adjoint exactly because their domains can be chosen so that the domain equality holds; without this, the spectral theorem fails and the operator does not correspond to a physical observable.

> [!tip] Hodge Star *(from Differential Geometry)*
> On an oriented Riemannian manifold the **Hodge star** $\star : \Omega^k \to \Omega^{n - k}$ on differential forms gives rise to a codifferential $d^* = \pm \star d \star$ which is the formal adjoint of the exterior derivative $d$ with respect to the $L^2$ inner product on forms. The combination $\Delta = dd^* + d^*d$ is the **Hodge Laplacian**, and Hodge theory — the identification of cohomology classes with harmonic forms — rests entirely on the adjoint relation between $d$ and $d^*$. Self-adjointness of the Laplacian is what allows spectral decomposition of forms by eigenvalue, the infinite-dimensional analogue of the spectral theorem proved in this chapter.
