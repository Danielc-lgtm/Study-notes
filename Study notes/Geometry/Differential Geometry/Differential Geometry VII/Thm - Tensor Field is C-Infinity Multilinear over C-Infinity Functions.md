---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Tensor Field on a Manifold"
  - "Def - Covariant Tensor on a Vector Space"
  - "Def - Vector Field on a Manifold"
  - "Def - Bump Function and Smooth Cutoff"
  - "Def - The Smooth Functions Ring"
tags: [geometry, differential-geometry, tensor-characterization]
---

# Notation

$M$ is a smooth manifold. $\mathfrak{X}(M)$ is the space of smooth vector fields, a module over $C^\infty(M)$. $\Omega^1(M)$ is the space of smooth 1-forms, also a $C^\infty(M)$-module. A smooth covariant $k$-tensor field $A$ induces by pointwise evaluation a map $A : \mathfrak{X}(M)^k \to C^\infty(M)$, written $A(X_1, \dots, X_k)(p) = A_p(X_1|_p, \dots, X_k|_p)$. The theorem states this is precisely a $C^\infty(M)$-multilinear map and that every such map comes from a tensor field. Full notation registry: [[Differential Geometry VII — Tensors and Tensor Fields]].

---

# Statement

> **Lemma (Tensor Characterization, Lee Lemma 12.24).** Let $M$ be a smooth manifold and let $k \geq 1$. A map
> $$\mathcal{A} : \mathfrak{X}(M) \times \cdots \times \mathfrak{X}(M) \to C^\infty(M) \quad (k \text{ factors})$$
> is induced by pointwise evaluation by a smooth covariant $k$-tensor field $A$ on $M$ if and only if $\mathcal{A}$ is **multilinear over the [[Def - Ring|ring]] $C^\infty(M)$**: for $f, f' \in C^\infty(M)$, $X_i, X'_i \in \mathfrak{X}(M)$, and each slot $i$,
> $$\mathcal{A}(X_1, \dots, fX_i + f'X'_i, \dots, X_k) = f\,\mathcal{A}(X_1, \dots, X_i, \dots, X_k) + f'\,\mathcal{A}(X_1, \dots, X'_i, \dots, X_k).$$
> When this holds, $A$ is uniquely determined by $\mathcal{A}$.

> **Mixed-type version.** A map $\mathcal{A} : \Omega^1(M)^k \times \mathfrak{X}(M)^\ell \to C^\infty(M)$ is induced by a smooth $(k, \ell)$-tensor field if and only if it is $C^\infty(M)$-multilinear in all $k + \ell$ slots.

> **Corollary.** A smooth covariant $k$-tensor field $A$ is *pointwise*: its value $A_p(v_1, \dots, v_k)$ depends only on the values of $v_1, \dots, v_k$ at $p$, not on any extensions to vector fields in a neighbourhood.

---

# Motivation

The motivation is to characterize tensor fields by an *algebraic* property — multilinearity over the ring of smooth functions — rather than by the more cumbersome bundle-section definition. The bundle definition (a smooth section of $T^kT^*M$) is geometrically correct but operationally awkward: it asks the reader to verify smoothness of components in coordinates, which is a calculation rather than a structural statement. The lemma replaces this with a one-line algebraic test: substitute $fX$ for $X$ in a slot, check that $f$ pulls outside the slot, done.

Why is the $C^\infty(M)$-multilinearity the *right* characterization? Because **it captures the property of "living at a point" algebraically**. A tensor field at a point depends only on the values of its arguments at that point, not on how the arguments behave elsewhere. The bracket $[X, Y]$, by contrast, depends on the *derivatives* of $X$ and $Y$ — values at neighbouring points. The bracket fails the $C^\infty(M)$-multilinearity test ($[fX, Y] = f[X, Y] - (Yf)X$, with the term $(Yf)X$ proving non-locality), and this failure is what marks the bracket as non-tensorial. The lemma converts "tensorial" from a definition into a *testable algebraic condition*.

The lemma is also striking because the "only if" direction is easy — a tensor field obviously is $C^\infty(M)$-multilinear, since $f$ is just a scalar at each point — while the "if" direction is non-trivial: given an abstract $C^\infty(M)$-multilinear map, one must *construct* a smooth tensor field whose pointwise evaluation gives it. The construction uses smooth bump functions, partitions of unity, and the locality argument from extension lemmas.

The proof's strategy is in three stages: first show the map is **local** (depends only on $X_i$ in a neighbourhood), then show it is **pointwise** (depends only on $X_i$ at the point), and finally use the pointwise property to define a tensor field. Each step uses bump functions to localize.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem applies whenever you have a $\mathbb{R}$-multilinear map on vector fields that you suspect is a tensor field. The trick is recognizing when a candidate object is in this position. Each of the following is a property $B$ from which the precondition "$\mathcal{A}$ is $C^\infty(M)$-multilinear" can be verified, possibly with calculation.

**A candidate operation defined using only fibrewise data, no derivatives.** Example: given a connection $\nabla$ on $M$ and three vector fields $X, Y, Z$, the curvature operator $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z$ is *not* obviously fibrewise — it explicitly involves derivatives via $\nabla$ and the bracket $[X, Y]$. The bridge is to *compute* $R(fX, Y)Z, R(X, fY)Z, R(X, Y)(fZ)$ and verify the differential terms cancel pairwise (which they do, miraculously, because of the Leibniz rule). Once this is verified, the lemma certifies $R$ is a $(1, 3)$-tensor field, and the apparent dependence on $X, Y, Z$'s derivatives is illusory: the tensor lives at a point.

**A candidate operation that is the inner product of two tensorial inputs.** If $X, Y$ are vector fields and $g$ is a metric, then $\mathcal{A}(X, Y) := g(X, Y)$ is automatically $C^\infty(M)$-bilinear by the bilinearity of $g$ at each point: $g(fX, Y) = f g(X, Y)$ because $g_p$ is just a bilinear form on $T_pM$. The lemma certifies $g$ is a tensor field, which is consistent with the metric's *definition* as a tensor field. The interest is that this provides an *intrinsic* characterization: any candidate "inner product" on vector fields that satisfies the $C^\infty(M)$-bilinearity check is automatically a tensor field. So you can *define* the metric by giving its action on vector fields, without ever introducing components.

**A candidate operation defined by an integral or pairing with a fixed background.** If $\omega$ is a fixed 1-form on $M$, then $\mathcal{A}(X) := \omega(X)$ — the contraction of $X$ with $\omega$ — is $C^\infty(M)$-linear in $X$ because $\omega(fX) = f\omega(X)$ for each $p$. The lemma certifies $\mathcal{A}$ is a smooth 1-form (which is $\omega$ itself). This is degenerate-looking but is the prototype: a tensorial operation built from a fixed tensor by partial evaluation is itself tensorial.

**Sources where $C^\infty(M)$-multilinearity *fails* (so the theorem rules out tensoriality).** The Lie bracket $[X, Y]$, viewed as a map $\mathfrak{X}(M) \times \mathfrak{X}(M) \to \mathfrak{X}(M)$, satisfies $[fX, Y] = f[X, Y] - (Yf)X$, with the $-(Yf)X$ term breaking $C^\infty(M)$-linearity in the first slot. So the bracket is *not* a tensor field; the lemma is what makes this precise. The same holds for the covariant derivative $\nabla_X Y$ in the $X$ slot ($\nabla_{fX}Y = f\nabla_X Y$, this *is* $C^\infty(M)$-linear in $X$), but $\nabla_X(fY) = f\nabla_X Y + (Xf)Y$, *not* $C^\infty(M)$-linear in $Y$. So $\nabla$ is neither a tensor field nor a tensorial operation — it is a *connection*, a strictly more general object.

**Targets (Output Amplification)**

The conclusion gives you a tensor field. Each target is "tensor field $A$ + additional fact = downstream conclusion".

**Tensor field + chart computes components.** Once $\mathcal{A}$ is known to be a tensor field via the lemma, its components in a coordinate chart are $A^{i_1\cdots i_k}_{j_1\cdots j_\ell} = \mathcal{A}(dx^{i_1}, \dots, dx^{i_k}, \partial_{j_1}, \dots, \partial_{j_\ell})$. So the abstract algebraic object $\mathcal{A}$ has a fully explicit coordinate representation: $A$ is determined by its values on basis vectors and basis covectors.

**Tensor field + connection + Bianchi identities.** The Riemann curvature, certified as a tensor field by the lemma, satisfies the symmetry $R(X, Y)Z = -R(Y, X)Z$ (antisymmetry in $X, Y$), the first Bianchi identity $R(X, Y)Z + R(Y, Z)X + R(Z, X)Y = 0$ (when the connection is torsion-free), and the second Bianchi identity (a derivative-of-curvature identity). These structural properties are exactly the ones a tensor field can have, and they organize the geometry of Riemannian manifolds.

**Tensor field + smooth dependence + globalization.** A $C^\infty(M)$-multilinear gadget defined *locally* on each chart, agreeing on overlaps, automatically extends to a global tensor field. This is the partition-of-unity argument: every local tensorial operation glues to a global tensor field, and the lemma is what justifies the gluing.

**Tensor field + manifold curvature + characteristic classes.** Once you know that combinations of connections produce tensor fields (curvature, torsion), you can integrate them against suitable forms to get characteristic numbers (Chern, Pontryagin classes). The whole edifice of characteristic classes is built on the certification, via the lemma, that certain natural constructions yield tensor fields.

---

# Why Is It True

The intuition is **smoothness localizes everything, and locality at the function-ring level forces locality at the point-set level**.

**The dominator argument is the bump function.** Suppose $\mathcal{A}$ is $C^\infty(M)$-multilinear. Given any point $p \in M$ and a vector field $X_i$ that vanishes on a neighbourhood $U$ of $p$, choose a bump function $\psi$ supported in $U$ with $\psi(p) = 1$. Then $\psi X_i$ vanishes identically (since $X_i$ vanishes wherever $\psi$ is nonzero), so $\mathcal{A}(\dots, \psi X_i, \dots) = 0$. By $C^\infty(M)$-multilinearity in the $i$-th slot, $\mathcal{A}(\dots, \psi X_i, \dots)(p) = \psi(p)\, \mathcal{A}(\dots, X_i, \dots)(p) = \mathcal{A}(\dots, X_i, \dots)(p)$. Combining: $\mathcal{A}(\dots, X_i, \dots)(p) = 0$. So *vanishing on a neighbourhood of $p$ kills the contribution at $p$* — the operation is **local**.

**The pointwise refinement uses Taylor's theorem.** Once the operation is local, fix $p$ and choose a chart $(x^a)$ centered at $p$. Any vector field $X_i$ has, in coordinates near $p$, the form $X_i = X_i^a(x)\, \partial_a$, with $X_i^a(p)$ being the components of $X_i$ at $p$. The "pointwise dependence" claim is that $\mathcal{A}(X_1, \dots, X_k)(p)$ depends only on the values $X_i^a(p)$, not on the entire functions $X_i^a(x)$. Subtract a vector field that agrees with $X_i$ to first order at $p$ but vanishes elsewhere: $X_i$ minus its constant-coefficient first-order approximation is a vector field whose components vanish at $p$. Using the locality and $C^\infty(M)$-linearity, the operation can be made to depend only on the components at $p$. Multilinearity at the point of $\mathcal{A}_p(X_1|_p, \dots, X_k|_p)$ is then a finite-dimensional multilinear-algebra statement, and a $\mathbb{R}$-multilinear map on $T_pM^k$ is a covariant $k$-tensor at $p$ — by [[Def - Covariant Tensor on a Vector Space|definition]].

**The mechanism in one line: $\mathcal{A}$ is $C^\infty(M)$-multilinear, so $\mathcal{A}$ commutes with all multiplications by functions, including bump functions, which let us localize and pointwize the operation.**

**The reverse direction is immediate.** If $A$ is a smooth tensor field and $\mathcal{A}(X_1, \dots, X_k) := A(X_1, \dots, X_k)$, then at each point $p$,
$\mathcal{A}(X_1, \dots, fX_i, \dots, X_k)(p) = A_p(X_1|_p, \dots, f(p)X_i|_p, \dots, X_k|_p) = f(p)\, A_p(X_1|_p, \dots, X_i|_p, \dots, X_k|_p) = f(p)\,\mathcal{A}(X_1, \dots, X_k)(p)$,
which says $\mathcal{A}(\dots, fX_i, \dots) = f \cdot \mathcal{A}(\dots, X_i, \dots)$ globally. So tensor fields give $C^\infty(M)$-multilinear maps directly from the fibrewise multilinearity of $A_p$.

---

# What Makes This Hard

The non-trivial direction is the construction of $A$ from $\mathcal{A}$. The challenge is that $\mathcal{A}$ is defined on *global* vector fields, but a tensor at a point needs to be defined on tangent vectors at that point alone; the proof must extend a tangent vector to a global vector field, evaluate $\mathcal{A}$, and check the result is independent of the extension. Independence of extension is where bump functions and $C^\infty(M)$-linearity work together: if two extensions agree at $p$, their difference vanishes at $p$, so by the locality argument the difference contributes zero.

The common error is to skip the bump-function argument and "just evaluate" $\mathcal{A}$ on a tangent vector — but $\mathcal{A}$ does not act on tangent vectors at a point, it acts on vector fields. The subtlety is the extension issue and the verification of well-definedness.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Use bump functions to show $\mathcal{A}$ is local in each slot, then use coordinate vector fields and component functions to show $\mathcal{A}$ is *pointwise* in each slot. The pointwise restriction of $\mathcal{A}$ defines a multilinear map on each tangent space, hence a tensor at each point; the smoothness of the assignment $p \mapsto A_p$ comes from $\mathcal{A}$'s output being a smooth function.

**Subgoal decomposition:**

1. **Locality:** Show that if $X_i$ vanishes on a neighbourhood $U$ of $p$, then $\mathcal{A}(X_1, \dots, X_k)(p) = 0$.
   - *Hint:* Choose a bump function $\psi$ with $\psi(p) = 1$ and $\mathrm{supp}\,\psi \subset U$. Then $\psi X_i \equiv 0$, and $\mathcal{A}(\dots, \psi X_i, \dots) = 0$. Apply $C^\infty(M)$-linearity to extract $\psi(p) = 1$ and conclude.
   - *Why needed:* This is the first step — it says the operation only sees a vector field on an arbitrarily small neighbourhood.

2. **Pointwise dependence:** Show that if $X_i|_p = X'_i|_p$ (the two vector fields agree at $p$), then $\mathcal{A}(X_1, \dots, X_k)(p) = \mathcal{A}(\dots, X'_i, \dots, X_k)(p)$.
   - *Hint:* Their difference $X_i - X'_i$ vanishes at $p$. In a chart, $(X_i - X'_i) = (X_i - X'_i)^a \partial_a$ with $(X_i - X'_i)^a(p) = 0$. The component functions vanish at $p$, and after extending the chart-coordinate vector fields globally, $C^\infty(M)$-multilinearity gives a factor that vanishes at $p$.
   - *Why needed:* This converts the global operation into a fibrewise one — the value at $p$ depends only on the pointwise values of the inputs.

3. **Define the tensor:** For $v_1, \dots, v_k \in T_pM$, extend each $v_i$ to a smooth global vector field $X_i$ with $X_i|_p = v_i$, and set $A_p(v_1, \dots, v_k) := \mathcal{A}(X_1, \dots, X_k)(p)$.
   - *Hint:* The extensions exist by the extension lemma for vector fields. The value is independent of the extension by subgoal 2. $A_p$ is multilinear because $\mathcal{A}$ is (over $\mathbb{R}$, hence in particular pointwise).
   - *Why needed:* This is the tensor field, defined by pointwise evaluation of the $C^\infty(M)$-multilinear operation.

4. **Verify smoothness:** Show $p \mapsto A_p$ is a smooth section of $T^kT^*M$.
   - *Hint:* In a chart, the components $A^{i_1\cdots i_k}(x) = A_p(\partial_{i_1}|_p, \dots, \partial_{i_k}|_p) = \mathcal{A}(\partial_{i_1}, \dots, \partial_{i_k})(x)$ (with the coordinate vector fields used as inputs) are smooth functions of $x$ since $\mathcal{A}$ outputs a smooth function.
   - *Why needed:* Without smoothness, the construction gives only a rough section; the smoothness comes for free because $\mathcal{A}$ is $C^\infty$-valued.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\mathcal{A}$ acts locally
> **Statement:** If $X_i$ vanishes on a neighbourhood $U$ of $p$, then $\mathcal{A}(X_1, \dots, X_k)(p) = 0$.
>
> **Hint:** Multiply $X_i$ by a bump function $\psi$ with $\psi(p) = 1$ and $\mathrm{supp}\,\psi \subset U$. Then $\psi X_i \equiv 0$. Apply $C^\infty(M)$-linearity.
>
> **Why needed:** Establishes locality of $\mathcal{A}$ — the value at $p$ only depends on $X_i$ near $p$.
>
> > [!note]- Full proof
> > Choose a [[Def - Bump Function and Smooth Cutoff|bump function]] $\psi \in C^\infty(M)$ with $\psi(p) = 1$ and $\mathrm{supp}\,\psi \subset U$. Since $X_i$ vanishes on $U$, the product $\psi X_i$ vanishes wherever $\psi$ is nonzero, and trivially vanishes where $\psi$ is zero. Hence $\psi X_i \equiv 0$ on $M$, so $\mathcal{A}(X_1, \dots, \psi X_i, \dots, X_k) \equiv 0$. By $C^\infty(M)$-linearity in the $i$-th slot, $\mathcal{A}(X_1, \dots, \psi X_i, \dots, X_k) = \psi \cdot \mathcal{A}(X_1, \dots, X_i, \dots, X_k)$. Evaluating at $p$: $0 = \psi(p) \cdot \mathcal{A}(X_1, \dots, X_i, \dots, X_k)(p) = 1 \cdot \mathcal{A}(\dots)(p)$, so $\mathcal{A}(X_1, \dots, X_k)(p) = 0$. $\blacksquare$

> [!note]- Lemma 2: $\mathcal{A}$ acts pointwise
> **Statement:** If $X_i|_p = 0$ (the vector field vanishes at $p$), then $\mathcal{A}(X_1, \dots, X_i, \dots, X_k)(p) = 0$.
>
> **Hint:** In a chart around $p$, write $X_i = X_i^a(x)\, \partial_a$ with $X_i^a(p) = 0$ (since $X_i|_p = 0$). Use the extension lemma to extend $\partial_a$ from the chart to global vector fields $E_a$ and the component functions $X_i^a$ from the chart to global smooth functions $f^a_i$ that agree with $X_i^a$ near $p$.
>
> **Why needed:** Upgrades Lemma 1's locality to pointwise dependence — the value depends only on the values of the inputs at the point.
>
> > [!note]- Full proof
> > Choose a chart $(U, x^a)$ centered at $p$. In this chart, $X_i = X_i^a(x)\, \partial_a$, with the component functions $X_i^a \in C^\infty(U)$ and $X_i^a(p) = 0$ (since $X_i|_p = 0$ means $X_i = 0$ when expanded in the basis).
> >
> > Extend the local coordinate frame to global smooth vector fields: there exist $E_a \in \mathfrak{X}(M)$ with $E_a = \partial_a$ in some neighbourhood $V \subset U$ of $p$ (by multiplying by a bump function supported in $V$ and using the extension lemma to define them on all of $M$). Similarly extend the components $X_i^a$ on $V$ to global smooth functions $f_i^a \in C^\infty(M)$ with $f_i^a = X_i^a$ on $V$ and $f_i^a(p) = 0$.
> >
> > Define $\tilde X_i := f_i^a E_a$ (Einstein summation). On $V$, $\tilde X_i = X_i^a \partial_a = X_i$, so $\tilde X_i - X_i$ vanishes on the neighbourhood $V$ of $p$. By Lemma 1, $\mathcal{A}(\dots, \tilde X_i - X_i, \dots)(p) = 0$, so $\mathcal{A}(\dots, X_i, \dots)(p) = \mathcal{A}(\dots, \tilde X_i, \dots)(p)$.
> >
> > Now compute $\mathcal{A}(\dots, \tilde X_i, \dots) = \mathcal{A}(\dots, f_i^a E_a, \dots) = f_i^a \cdot \mathcal{A}(\dots, E_a, \dots)$ by $C^\infty(M)$-linearity. Evaluating at $p$: $f_i^a(p) \cdot \mathcal{A}(\dots, E_a, \dots)(p) = 0 \cdot \mathcal{A}(\dots, E_a, \dots)(p) = 0$, since $f_i^a(p) = X_i^a(p) = 0$. So $\mathcal{A}(\dots, X_i, \dots)(p) = 0$. $\blacksquare$

> [!note]- Lemma 3: Define $A_p$ and verify smoothness
> **Statement:** For $v_1, \dots, v_k \in T_pM$, define $A_p(v_1, \dots, v_k) := \mathcal{A}(X_1, \dots, X_k)(p)$, where $X_i$ is any smooth vector field on $M$ with $X_i|_p = v_i$. This is well-defined, multilinear, and smooth in $p$.
>
> **Hint:** Well-definedness follows from Lemma 2 (the answer only depends on $X_i|_p = v_i$). Multilinearity is inherited from the $\mathbb{R}$-multilinearity of $\mathcal{A}$. Smoothness comes from $\mathcal{A}$ outputting smooth functions.
>
> **Why needed:** This actually constructs the tensor field. The previous lemmas guarantee well-definedness; this lemma assembles them into the conclusion.
>
> > [!note]- Full proof
> > **Existence of extensions.** Given $v_i \in T_pM$, the extension lemma for vector fields produces $X_i \in \mathfrak{X}(M)$ with $X_i|_p = v_i$. (Sketch: pick coordinates $(x^a)$ around $p$, set $X_i = \sum_a v_i^a \partial_a$ in the chart, multiply by a bump function $\psi$ with $\psi(p) = 1$, and extend by $0$ outside the chart's support.)
> >
> > **Well-definedness.** If $X_i$ and $X'_i$ are two such extensions, with $X_i|_p = X'_i|_p = v_i$, then $(X_i - X'_i)|_p = 0$, so by Lemma 2, $\mathcal{A}(X_1, \dots, X_i - X'_i, \dots, X_k)(p) = 0$, hence $\mathcal{A}(X_1, \dots, X_i, \dots, X_k)(p) = \mathcal{A}(X_1, \dots, X'_i, \dots, X_k)(p)$. So $A_p(v_1, \dots, v_k)$ is independent of the choice of extension.
> >
> > **Multilinearity.** $\mathcal{A}$ is multilinear over $\mathbb{R}$ (since $C^\infty(M)$-multilinearity includes constant functions), so $A_p(\dots, av_i + bv'_i, \dots) = a A_p(\dots, v_i, \dots) + b A_p(\dots, v'_i, \dots)$ for $a, b \in \mathbb{R}$.
> >
> > **Smoothness.** Pick a chart $(x^a)$. The components $A^{i_1\cdots i_k}(x) := A_p(\partial_{i_1}|_p, \dots, \partial_{i_k}|_p) = \mathcal{A}(\partial_{i_1}, \dots, \partial_{i_k})(p)$ (with the coordinate frames extended to global vector fields by bump functions, but the result is independent of that extension by Lemma 2) are smooth functions because $\mathcal{A}$ outputs smooth functions. Smoothness of components implies smoothness of $A$ as a section. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Lemma (Tensor Characterization, Lee 12.24).** A map $\mathcal{A} : \mathfrak{X}(M)^k \to C^\infty(M)$ is induced by a smooth covariant $k$-tensor field $A$ on $M$ if and only if $\mathcal{A}$ is multilinear over $C^\infty(M)$.
>
> *Proof.* ($\Leftarrow$, the easy direction.) If $A$ is a smooth covariant $k$-tensor field and $\mathcal{A}(X_1, \dots, X_k) := A(X_1, \dots, X_k)$, then at each $p$, $\mathcal{A}(\dots, fX_i, \dots)(p) = A_p(\dots, f(p)X_i|_p, \dots) = f(p)\,A_p(\dots, X_i|_p, \dots) = (f\,\mathcal{A}(\dots, X_i, \dots))(p)$, by the multilinearity of $A_p$ at the point. So $\mathcal{A}$ is $C^\infty(M)$-multilinear.
>
> ($\Rightarrow$, the substantive direction.) Suppose $\mathcal{A} : \mathfrak{X}(M)^k \to C^\infty(M)$ is $C^\infty(M)$-multilinear. We construct $A$ in three steps.
>
> **Step 1: Locality.** Suppose $X_i$ vanishes on a neighbourhood $U$ of $p$. Choose a bump function $\psi$ with $\psi(p) = 1$ and $\mathrm{supp}\,\psi \subset U$. Then $\psi X_i \equiv 0$ on $M$ (since on $U$ both $\psi$ and $X_i$ can be nonzero but $X_i = 0$ on $U$, while on $M \setminus U$, $\psi = 0$). By $C^\infty(M)$-linearity in the $i$-th slot, $\mathcal{A}(\dots, \psi X_i, \dots) = \psi \cdot \mathcal{A}(\dots, X_i, \dots) \equiv 0$ (the left side is $\mathcal{A}$ of zero, by multilinearity). Evaluating at $p$ with $\psi(p) = 1$: $\mathcal{A}(\dots, X_i, \dots)(p) = 0$.
>
> **Step 2: Pointwise dependence.** Suppose $X_i|_p = 0$. Pick a chart $(U, x^a)$ centred at $p$. On $U$, write $X_i = X_i^a \partial_a$ with $X_i^a(p) = 0$. Extend $\partial_a$ and $X_i^a$ to globally defined $E_a \in \mathfrak{X}(M)$ and $f_i^a \in C^\infty(M)$, agreeing with the original on a smaller neighbourhood $V \ni p$. Set $\tilde X_i := f_i^a E_a$. Then $X_i - \tilde X_i$ vanishes on $V$, so by Step 1, $\mathcal{A}(\dots, X_i - \tilde X_i, \dots)(p) = 0$. By $C^\infty(M)$-linearity, $\mathcal{A}(\dots, \tilde X_i, \dots) = f_i^a \cdot \mathcal{A}(\dots, E_a, \dots)$, which evaluated at $p$ gives $f_i^a(p) \cdot \mathcal{A}(\dots, E_a, \dots)(p) = 0$ since $f_i^a(p) = X_i^a(p) = 0$.
>
> **Step 3: Construct $A$.** For $p \in M$ and $v_1, \dots, v_k \in T_pM$, choose smooth global extensions $X_i \in \mathfrak{X}(M)$ with $X_i|_p = v_i$ (extension lemma). Define $A_p(v_1, \dots, v_k) := \mathcal{A}(X_1, \dots, X_k)(p)$.
>
> **Well-definedness:** If $X'_i|_p = v_i$ also, then $X_i - X'_i$ vanishes at $p$, so by Step 2, $\mathcal{A}(\dots, X_i - X'_i, \dots)(p) = 0$, hence $\mathcal{A}(\dots, X_i, \dots)(p) = \mathcal{A}(\dots, X'_i, \dots)(p)$.
>
> **Multilinearity of $A_p$:** Inherited from $\mathbb{R}$-multilinearity of $\mathcal{A}$.
>
> **Smoothness:** In a chart, the components $A_{i_1\cdots i_k}(x) = A_p(\partial_{i_1}, \dots, \partial_{i_k})$ are smooth functions of $x$ since $\mathcal{A}(\partial_{i_1}, \dots, \partial_{i_k}) \in C^\infty(M)$.
>
> Thus $A$ is a smooth covariant $k$-tensor field, and by construction $\mathcal{A}(X_1, \dots, X_k)(p) = A_p(X_1|_p, \dots, X_k|_p)$. $\qquad\blacksquare$
>
> *Uniqueness* of $A$: if $A, A'$ both induce $\mathcal{A}$, then at every $p$ and every $v_1, \dots, v_k$, $A_p(v_1, \dots, v_k) = A'_p(v_1, \dots, v_k)$ — they agree pointwise on global extensions of basis vectors, hence everywhere.
>
> *Mixed-type version.* The same proof works with covector field slots: 1-forms behave like vector fields under multiplication by smooth functions, and Steps 1–3 apply equally well to slots accepting 1-forms.

---

# Cross-Field Exercise Suggestions

The aim here is to find settings where this lemma applies but is not advertised — to battle-test recognition of "is this a tensor?".

**Riemannian geometry: the curvature tensor of a connection.** Given a connection $\nabla$ on $M$ and vector fields $X, Y, Z$, the operator $R(X, Y)Z := \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z$ looks like it depends on derivatives of $X, Y, Z$. Yet it is **$C^\infty(M)$-multilinear in all three slots**, hence (by the lemma) it is a $(1, 3)$-tensor field. The verification is one of the standard "miraculous cancellation" calculations of Riemannian geometry: the Leibniz rule terms cancel between the two double derivatives and the bracket term. The lemma is the abstract tool that turns this calculation into a structural theorem.

**Continuum mechanics: tensoriality of the stress.** The Cauchy stress tensor $\sigma$ is *defined* by the requirement that for any surface element with unit normal $n$, the traction (force per unit area) be $t = \sigma(n, \cdot)$ — a *linear* function of $n$. By the lemma, the map $n \mapsto t$ (linear over $\mathbb{R}$ and smooth in $n$) extends to a $C^\infty(M)$-linear map of vector fields, hence a $(1, 1)$-tensor field (or $(0, 2)$ after lowering an index with the spatial metric). The lemma is what justifies treating $\sigma$ as a single tensor object, independent of the choice of surface.

**Special relativity: the electromagnetic field strength.** The 4-current $J^\mu$ on Minkowski space and the field strength $F^{\mu\nu}$ are related by $\partial_\mu F^{\mu\nu} = J^\nu$ (one of Maxwell's equations). If we try to verify that $F$ is a tensor by checking $C^\infty(\mathbb{R}^4)$-multilinearity of the antisymmetric form $F(X, Y) = X^\mu Y^\nu F_{\mu\nu}$ in $X, Y \in \mathfrak{X}(\mathbb{R}^4)$, the verification is immediate ($F(fX, Y) = f F(X, Y)$ since $F_{\mu\nu}$ are *functions* of position, and $f$ just multiplies the result). So the lemma confirms $F$ is a tensor field — not surprising in special relativity (where everything is global Cartesian), but the lemma is what makes the *generalization* to general relativity rigorous.

**Algebraic geometry: invariants of the Lie bracket.** A natural question: the Jacobiator $J(X, Y, Z) = [X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]]$. By the Jacobi identity, $J \equiv 0$. But what if we worked in a system where the Jacobi identity might fail (e.g., a Loday algebra)? Then $J$ would be a candidate tensor. Checking $C^\infty(M)$-multilinearity reveals that $J$ is *not* tensorial in general — the bracket's non-tensoriality propagates. So the lemma is what rules out the non-tensoriality of bracket-derived operations.

---

# Bridges

- **[[Def - Vector Field on a Manifold|Vector fields]] and the Lie bracket.** The Lie bracket $[X, Y]$ is the prototypical *non-tensorial* operation: it has the form of a $(1, 2)$-operation but the $C^\infty(M)$-multilinearity test fails ($[fX, Y] = f[X, Y] - (Yf)X$). This failure marks the bracket as a *differential* operator, not a tensor. The tensor characterization lemma is what makes this dichotomy precise: differential operators are precisely the failures of $C^\infty(M)$-multilinearity.

- **The Riemann curvature tensor.** The curvature of a connection is constructed from non-tensorial pieces (the connection itself, the Lie bracket), but their combination $R(X, Y)Z$ is tensorial *because* the non-tensorial pieces cancel. The lemma is the certificate of this cancellation. This is the prototype of "non-tensorial parts assembling into a tensorial whole" — a pattern that recurs whenever curvature, torsion, or higher-order invariants are defined.

- **Pullback of covariant tensor fields.** Pullback is the canonical functorial operation on covariant tensor fields. The tensor characterization lemma says that to define a covariant tensor field on $M$, it suffices to specify the corresponding $C^\infty(M)$-multilinear map on vector fields. So pullback can be specified by saying what it does at the vector-field level, $\big(F^*A\big)(X_1, \dots, X_k) := A(F_*X_1, \dots, F_*X_k)$ when applicable — and the lemma certifies this defines a tensor field.

- **The Serre-Swan theorem.** A deeper bridge to commutative algebra: the lemma is one step in establishing that smooth vector bundles over $M$ correspond to finitely-generated projective $C^\infty(M)$-modules — the Serre-Swan theorem. Tensor fields, as sections of tensor bundles, are precisely the iterated tensor products of these modules over $C^\infty(M)$.

---

# Unlocked by This

> [!tip] Curvature Tensor as a $C^\infty(M)$-Multilinear Object *(from Riemannian Geometry)*
> The Riemann curvature tensor $R(X, Y, Z) := \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z$ is a $(1, 3)$-tensor field on $M$. **The lemma is the entire proof of this fact**: it suffices to verify $C^\infty(M)$-multilinearity in each slot, which is a finite calculation. Without the lemma, one would have to construct $R$ as a section of $T^{(1,3)}M$ and verify smoothness of components — much more work.

> [!tip] Tensoriality of Composite Operations *(from Differential Geometry)*
> The lemma is the universal test for whether a candidate construction yields a tensor field. Whenever you write down a multilinear-looking map on vector fields and 1-forms, the lemma is your diagnostic. The discipline this enforces in differential geometry — *always check $C^\infty(M)$-multilinearity before claiming an object is a tensor* — is the entry point to careful manifold-level calculation. Once internalized, it converts the question "is this a tensor?" from an obscure structural worry to a one-line check.

> [!tip] Module-Theoretic Formulation of Tensor Fields *(from Algebra)*
> The lemma is the geometric instance of the algebraic principle "tensorial = multilinear over the base ring". For a commutative ring $R$ with modules $M_1, \dots, M_k$ and $N$, the space of $R$-multilinear maps $M_1 \times \cdots \times M_k \to N$ is the **tensor product of modules** $M_1 \otimes_R \cdots \otimes_R M_k$ via its universal property. The geometric tensor field characterization is this algebraic fact applied with $R = C^\infty(M)$, $M_i = \mathfrak{X}(M)$, $N = C^\infty(M)$. The lemma is what makes the algebraic and geometric formulations agree.
