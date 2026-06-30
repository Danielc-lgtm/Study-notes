---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Tensors on Minkowski Space"
  - "Def - Metric Duality and Index Manipulation"
  - "Def - The Lorentz Group"
tags: [physics, special-relativity]
---

# Problem Statement

Work in mostly-minus signature, $c = 1$. Let $(e_\alpha)$ and $(e'_\alpha)$ be two bases of $E$ with change-of-basis matrix $P$ defined by $e'_\alpha = P^\beta{}_\alpha\,e_\beta$, and dual bases satisfying $e'^\alpha = (P^{-1})^\alpha{}_\beta\,e^\beta$.

1. Derive the transformation law of vector components, $v'^\alpha = (P^{-1})^\alpha{}_\beta\,v^\beta$, and of one-form components, $\omega'_\alpha = P^\beta{}_\alpha\,\omega_\beta$. Note they transform by *inverse* matrices.
2. Using these, show that the contraction $\omega_\mu v^\mu$ is invariant: $\omega'_\mu v'^\mu = \omega_\mu v^\mu$.
3. Hence show $X^\mu X_\mu$ is a Lorentz scalar (invariant), but the expression $X^\mu X^\mu$ (two upper indices) is *not* — it changes under a boost. Exhibit the change explicitly for a boost along $x$.
4. For two inertial frames, identify the change-of-basis matrix $P$ in terms of the [[Def - The Lorentz Group|Lorentz transformation]] $\Lambda$ relating them.

**Recall:**

A [[Def - Four-Vector|four-vector]] has components $v^\alpha = \langle e^\alpha, \vec v\rangle$ (contravariant, upper index); a one-form has $\omega_\alpha = \langle\omega, e_\alpha\rangle$ (covariant, lower index). Under a [[Def - Tensors on Minkowski Space|change of basis]] the two transform by mutually inverse matrices, which is exactly what makes their contraction invariant. The Lorentz boost along $x$ with rapidity $\varphi$ acts on components by $\Lambda^\mu{}_\nu$ with $\Lambda^0{}_0 = \Lambda^1{}_1 = \cosh\varphi$, $\Lambda^0{}_1 = \Lambda^1{}_0 = \sinh\varphi$.

---

# Convergent Strategy

**Problem class.** An *establish-an-invariant* problem combined with a *structural* derivation of the transformation laws. The [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality#Problem-Solving Strategy|topic strategy]] says: a quantity is frame-independent exactly when it is a legal up–down contraction, and the proof is that the $P$ and $P^{-1}$ cancel.

**Assumption pattern.** The defining relations $e'_\alpha = P^\beta{}_\alpha e_\beta$ and $e'^\alpha = (P^{-1})^\alpha{}_\beta e^\beta$ are the only inputs; everything follows by expanding components on the new basis and using $\langle e'^\alpha, e'_\beta\rangle = \delta^\alpha{}_\beta$. The contrast between the two contractions $X^\mu X_\mu$ and $X^\mu X^\mu$ is the whole point.

**Theorem routing.** Part 1: expand $v^\alpha = \langle e^\alpha, \vec v\rangle$ on the primed dual basis. Part 2: substitute the two laws into $\omega'_\mu v'^\mu$ and cancel $P P^{-1} = \mathbb{1}$. Part 3: $X^\mu X_\mu$ is the contraction of part 2 (invariant); $X^\mu X^\mu$ has both indices transforming by $P^{-1}$, leaving an uncancelled $(P^{-1})(P^{-1})$ that a boost makes visible. Part 4: match $P$ to $\Lambda$ via the inertial-frame transformation.

**Key decision point.** The crux is realising *why* one index up and one down is non-negotiable: contravariant components transform by $P^{-1}$, covariant by $P$, and only a product of one of each has the matrices cancel. The "illegal" $X^\mu X^\mu$ pairs two contravariant indices, so both bring a $P^{-1}$ and nothing cancels — the quantity is frame-dependent. Seeing the cancellation as the *reason* for the up–down rule, not merely a convention, is the lesson.

---

# Legal Operations Used

1. **Operation 1 from the topic page (raise/lower with the metric).** Implicit in forming $X_\mu = \eta_{\mu\nu}X^\nu$ for the legal contraction in part 3.

2. **Operation 2 from the topic page (contract an upper against a lower index).** Parts 2 and 3 hinge on this being the *only* invariant pairing; the illegal expression violates it.

---

# Hints

> [!note]- Hint 1
> Expand $\vec v = v^\alpha e_\alpha = v'^\alpha e'_\alpha$. Apply the primed dual form $e'^\beta$ to both sides: $v'^\beta = \langle e'^\beta, \vec v\rangle = \langle (P^{-1})^\beta{}_\gamma e^\gamma, v^\alpha e_\alpha\rangle = (P^{-1})^\beta{}_\gamma v^\alpha\delta^\gamma{}_\alpha = (P^{-1})^\beta{}_\alpha v^\alpha$.

> [!note]- Hint 2
> Substitute $\omega'_\mu = P^\alpha{}_\mu\omega_\alpha$ and $v'^\mu = (P^{-1})^\mu{}_\beta v^\beta$ into $\omega'_\mu v'^\mu$. The matrices meet as $P^\alpha{}_\mu(P^{-1})^\mu{}_\beta = \delta^\alpha{}_\beta$, leaving $\omega_\alpha v^\alpha$.

> [!note]- Hint 3
> $X^\mu X_\mu = X^\mu\eta_{\mu\nu}X^\nu$ is invariant (it is $\omega_\mu v^\mu$ with $\omega = X^\flat$, $v = X$). For $X^\mu X^\mu$, both factors transform by $P^{-1} = \Lambda$, so it becomes $\Lambda^\mu{}_\alpha\Lambda^\mu{}_\beta X^\alpha X^\beta$ — and $\Lambda^\mu{}_\alpha\Lambda^\mu{}_\beta \neq \delta_{\alpha\beta}$ (it would need $\Lambda^{\mathsf T}\Lambda = \mathbb{1}$, which fails; $\Lambda$ preserves $\eta$, not $\mathbb{1}$).

---

# Solution

The exercise makes precise why "indices up, indices down" is forced by invariance. The plan: derive the two transformation laws (Step 1), show their contraction is invariant by cancelling $PP^{-1}$ (Step 2), contrast the legal $X^\mu X_\mu$ with the illegal $X^\mu X^\mu$ and compute the latter's change under a boost (Step 3), and identify $P = \Lambda^{-1}$ for inertial frames (Step 4).

**Step 1: $v'^\alpha = (P^{-1})^\alpha{}_\beta v^\beta$ and $\omega'_\alpha = P^\beta{}_\alpha\omega_\beta$.**

> [!note]- Derivation
> *Vectors.* The vector $\vec v$ is basis-independent: $\vec v = v^\beta e_\beta = v'^\alpha e'_\alpha$. Apply the primed dual form $e'^\alpha$ and use $\langle e'^\alpha, e'_\gamma\rangle = \delta^\alpha{}_\gamma$ and $e'^\alpha = (P^{-1})^\alpha{}_\beta e^\beta$:
> $$v'^\alpha = \langle e'^\alpha, \vec v\rangle = \big\langle (P^{-1})^\alpha{}_\beta e^\beta,\, v^\gamma e_\gamma\big\rangle = (P^{-1})^\alpha{}_\beta\, v^\gamma\,\delta^\beta{}_\gamma = (P^{-1})^\alpha{}_\beta\, v^\beta.$$
> *Forms.* The form $\omega$ is basis-independent: evaluate it on the new basis vector $e'_\alpha = P^\beta{}_\alpha e_\beta$:
> $$\omega'_\alpha = \langle\omega, e'_\alpha\rangle = \big\langle\omega,\, P^\beta{}_\alpha e_\beta\big\rangle = P^\beta{}_\alpha\langle\omega, e_\beta\rangle = P^\beta{}_\alpha\,\omega_\beta.$$
> Vector components transform by $P^{-1}$ (contravariantly), form components by $P$ (covariantly) — by *inverse* matrices. This opposite behaviour is the origin of the up/down index distinction.

**Step 2: the contraction $\omega_\mu v^\mu$ is invariant.**

> [!note]- Derivation
> Substitute both laws:
> $$\omega'_\mu v'^\mu = \big(P^\alpha{}_\mu\omega_\alpha\big)\big((P^{-1})^\mu{}_\beta v^\beta\big) = \omega_\alpha v^\beta\,P^\alpha{}_\mu(P^{-1})^\mu{}_\beta = \omega_\alpha v^\beta\,\delta^\alpha{}_\beta = \omega_\alpha v^\alpha.$$
> The matrices cancel, $P^\alpha{}_\mu(P^{-1})^\mu{}_\beta = \delta^\alpha{}_\beta$, so $\omega'_\mu v'^\mu = \omega_\mu v^\mu$: the same number in every basis. **The up–down contraction is invariant precisely because the two index types transform by inverse matrices.**

**Step 3: $X^\mu X_\mu$ is invariant; $X^\mu X^\mu$ is not.**

> [!note]- Derivation
> *Legal.* $X^\mu X_\mu = X^\mu(\eta_{\mu\nu}X^\nu)$ is the contraction of part 2 with $\omega_\mu = X_\mu = \eta_{\mu\nu}X^\nu$ the [[Def - Metric Duality and Index Manipulation|lowered]] vector. Hence it is invariant, equal to $(X^0)^2 - |\mathbf X|^2$ in every frame.
>
> *Illegal.* The expression $X^\mu X^\mu$ has *both* indices upper, so both transform contravariantly. For inertial frames $P^{-1} = \Lambda$ (Step 4), so
> $$X'^\mu X'^\mu = \big(\Lambda^\mu{}_\alpha X^\alpha\big)\big(\Lambda^\mu{}_\beta X^\beta\big) = \big(\Lambda^\mu{}_\alpha\Lambda^\mu{}_\beta\big)X^\alpha X^\beta.$$
> This equals $X^\alpha X^\alpha$ only if $\Lambda^\mu{}_\alpha\Lambda^\mu{}_\beta = \delta_{\alpha\beta}$, i.e. $\Lambda^{\mathsf T}\Lambda = \mathbb{1}$ — but a Lorentz transformation satisfies $\Lambda^{\mathsf T}\eta\Lambda = \eta$, **not** $\Lambda^{\mathsf T}\Lambda = \mathbb{1}$. So $X'^\mu X'^\mu \neq X^\mu X^\mu$ in general. Explicitly, take $X^\mu = (1, 0, 0, 0)$ (so $X^\mu X^\mu = 1$) and boost along $x$ with rapidity $\varphi$: $X'^\mu = (\cosh\varphi, \sinh\varphi, 0, 0)$, giving
> $$X'^\mu X'^\mu = \cosh^2\varphi + \sinh^2\varphi = \cosh 2\varphi \neq 1$$
> for $\varphi \neq 0$. The "Euclidean norm" $X^\mu X^\mu$ grows under the boost — it is frame-dependent and meaningless. (By contrast the invariant $X^\mu X_\mu = \cosh^2\varphi - \sinh^2\varphi = 1$ is unchanged.) This is why Tong declares it "illegal to write $X^\mu X^\mu$."

**Step 4: for inertial frames, $P = \Lambda^{-1}$.**

> [!note]- Derivation
> The components of a vector transform between inertial frames by the [[Def - The Lorentz Group|Lorentz matrix]]: $X'^\mu = \Lambda^\mu{}_\nu X^\nu$. Comparing with the general law $v'^\alpha = (P^{-1})^\alpha{}_\beta v^\beta$ from Step 1, we read off $(P^{-1})^\mu{}_\nu = \Lambda^\mu{}_\nu$, i.e.
> $$P = \Lambda^{-1}.$$
> The change-of-*basis* matrix is the *inverse* of the change-of-*components* matrix — a standard but easily-confused fact: when the basis vectors transform by $P$, the components transform by $P^{-1}$. (This is Gourgoulhon's Example 14.4.)

> [!note]- Complete formal solution
> **(1)** From $\vec v = v'^\alpha e'_\alpha$ and $e'^\alpha = (P^{-1})^\alpha{}_\beta e^\beta$: $v'^\alpha = \langle e'^\alpha, \vec v\rangle = (P^{-1})^\alpha{}_\beta v^\beta$. From $\omega'_\alpha = \langle\omega, e'_\alpha\rangle$ and $e'_\alpha = P^\beta{}_\alpha e_\beta$: $\omega'_\alpha = P^\beta{}_\alpha\omega_\beta$.
> **(2)** $\omega'_\mu v'^\mu = P^\alpha{}_\mu\omega_\alpha(P^{-1})^\mu{}_\beta v^\beta = \delta^\alpha{}_\beta\omega_\alpha v^\beta = \omega_\mu v^\mu$.
> **(3)** $X^\mu X_\mu$ is invariant (part 2 with $\omega = X^\flat$). $X^\mu X^\mu$ has both indices contravariant; for $X^\mu = (1,0,0,0)$ boosted by rapidity $\varphi$, $X'^\mu X'^\mu = \cosh^2\varphi + \sinh^2\varphi = \cosh 2\varphi \neq 1$, so it is frame-dependent — illegal. (The invariant $X^\mu X_\mu = \cosh^2\varphi - \sinh^2\varphi = 1$ is unchanged.)
> **(4)** Matching $X'^\mu = \Lambda^\mu{}_\nu X^\nu$ to $v'^\alpha = (P^{-1})^\alpha{}_\beta v^\beta$ gives $P = \Lambda^{-1}$. $\blacksquare$

---

# Key Takeaways

**Covariant and contravariant components transform by inverse matrices — that is the whole content of the up/down distinction.** The single fact underlying the index calculus is that a [[Def - Four-Vector|four-vector]]'s components transform by $P^{-1}$ while a one-form's transform by $P$. Everything else follows: the contraction of one upper with one lower index is invariant because the two matrices cancel; the contraction of two upper (or two lower) indices is frame-dependent because two factors of $P^{-1}$ (or $P$) survive. The reusable mental model is that an upper index "carries a $P^{-1}$" and a lower index "carries a $P$," and a legal scalar is one in which all such factors pair off and cancel. When you write a tensor expression, count the loose $P$'s and $P^{-1}$'s: if they cancel, the quantity is invariant; if not, it is not a tensor and not physical.

**$X^\mu X^\mu$ fails because a Lorentz transformation preserves $\eta$, not the identity.** The boost computation $X'^\mu X'^\mu = \cosh 2\varphi \neq 1$ exposes the precise reason the "Euclidean norm" of a four-vector is illegal: it would be invariant only if $\Lambda^{\mathsf T}\Lambda = \mathbb{1}$, which characterises an *orthogonal* (rotation) matrix, whereas a Lorentz transformation satisfies $\Lambda^{\mathsf T}\eta\Lambda = \eta$ — it preserves the *indefinite* metric, not the Euclidean one. The invariant $X^\mu X_\mu$ works because the lowering with $\eta$ inserts exactly the metric that $\Lambda$ preserves. The transferable diagnostic: whenever a "norm" or "length" of a four-vector appears, make sure the metric $\eta$ is sandwiched between the two factors (i.e. one index is lowered); a sum of squares with no metric is the Euclidean norm and is wrong. This is the sharpest single test for a beginner's error in relativity.

**The change-of-basis matrix is the inverse of the change-of-components matrix.** A perennial source of confusion is whether the Lorentz matrix $\Lambda$ is $P$ or $P^{-1}$. The resolution: $\Lambda$ is the matrix that transforms *components* ($X'^\mu = \Lambda^\mu{}_\nu X^\nu$), so it is $P^{-1}$, and the *basis vectors* transform by $P = \Lambda^{-1}$. The reason is that a vector is fixed while its description changes: if the basis vectors get longer (transform by $P$), the components must get smaller (transform by $P^{-1}$) to describe the same vector. This inverse relationship is built into the definition of contravariance, and keeping it straight prevents sign and direction errors when boosting tensors. The rule of thumb: basis and components always transform oppositely, and "contravariant" literally means "transforms contrary to the basis."
