---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Free, Transitive, Effective, and Proper Group Actions"
  - "Def - Complex Projective Space as a Quotient"
  - "Def - Smooth Action of a Lie Group"
tags: [geometry, gauge-theory]
---

# Problem Statement

Regard $\mathbb{C}^n$ as $\mathbb{R}^{2n}$ with its Hermitian inner product $\langle v, w \rangle = \sum_{j=1}^n v_j \overline{w_j}$ and Euclidean norm $|w|^2 = \sum_{j=1}^n |w_j|^2$, and let
$$S^{2n-1} := \{w = (w_1, \dots, w_n) \in \mathbb{C}^n : |w| = 1\}$$
be the odd-dimensional unit sphere. Let $U(1) = \{z \in \mathbb{C} : |z| = 1\}$ act on $S^{2n-1}$ by scalar multiplication on the complex coordinates,
$$z \cdot w := (z w_1, \dots, z w_n), \qquad z \in U(1), \ w \in S^{2n-1}.$$

Prove the following.

1. The action is well defined and is a smooth left action.
2. The action is **free** (hence also effective).
3. The action is **transitive if and only if $n = 1$**.
4. Two points $w, w' \in S^{2n-1}$ lie in the same orbit if and only if they span the same complex line in $\mathbb{C}^n$; consequently the orbit space is the set of complex lines in $\mathbb{C}^n$, that is, the complex projective space
$$U(1) \backslash S^{2n-1} \;=\; \mathbb{CP}^{n-1},$$
a smooth manifold of real dimension $2(n-1)$.

**Recall:**

The objects in play are a smooth left action of a Lie group, the properties free, effective, and transitive, the orbit space of an action, and complex projective space as a quotient.

![[Def - Free, Transitive, Effective, and Proper Group Actions#The Definition]]

A smooth left action of a Lie group $G$ on a manifold $M$ is a smooth map $G \times M \to M$, $(g, x) \mapsto g \cdot x$, with $(gh) \cdot x = g \cdot (h \cdot x)$ and $e \cdot x = x$. The action is **effective** if $g \cdot x = x$ for all $x$ forces $g = e$; it is **free** if $g \cdot x = x$ for even a single $x$ forces $g = e$; it is **transitive** if for all $x, y \in M$ there is a $g$ with $g \cdot x = y$. Every free action is effective (provided $M \neq \varnothing$). The **orbit** of $x$ is $G \cdot x = \{g \cdot x : g \in G\}$ and the **orbit space** is $G \backslash M = \{G \cdot x : x \in M\}$ with the quotient topology. A Lie group action is **proper** if $(g, x) \mapsto (g \cdot x, x)$ is a proper map; every action of a **compact** Lie group is proper.

![[Def - Complex Projective Space as a Quotient#The Definition]]

Complex projective space $\mathbb{CP}^{n-1}$ is the set of one-dimensional complex-linear subspaces (complex lines through the origin) of $\mathbb{C}^n$; equivalently it is the orbit space $S^{2n-1} / U(1)$ of the scalar action defined above, and equivalently the quotient $(\mathbb{C}^n \setminus \{0\}) / \mathbb{C}^{\ast}$. It is a compact, connected smooth manifold of real dimension $2(n-1)$.

> [!warning] Convention: side of the action and the notation for the quotient
> Bär writes group actions on the left and denotes the orbit space $U(1) \backslash S^{2n-1}$ (Example 1.5.7.2, 1.5.12). Because $U(1)$ is abelian, the scalar action $z \cdot w = zw$ is at the same time a left and a right action — $z_1 \cdot (z_2 \cdot w) = z_1 z_2 w = (z_1 z_2) \cdot w$ with $z_1 z_2 = z_2 z_1$ — so the distinction is immaterial here, and we write $U(1) \backslash S^{2n-1}$ and $S^{2n-1}/U(1)$ interchangeably, both equal to $\mathbb{CP}^{n-1}$.

---

# Convergent Strategy

**Problem class.** This is a *classify-an-action* problem together with an *orbit-space identification*: decide freeness, effectiveness, and transitivity of an explicit action, then recognise the quotient as a named manifold. Freeness is settled by a one-line cancellation in the field $\mathbb{C}$; transitivity is settled by a linear-dependence invariant; the orbit space is recognised by translating "same orbit" into "same complex line".

**Assumption pattern.** The recognisable trigger is that the group is the *unit scalars* $U(1) \subset \mathbb{C}^{\ast}$ acting *linearly* on a complex vector space and restricted to the unit sphere. Two features of this setup are decisive. First, on any non-zero coordinate the equation $z w_j = w_j$ can be *cancelled* because $\mathbb{C}$ is a field, giving $z = 1$ — this is the source of freeness, and it is exactly what fails for the fixed points of a rotation action, where the moved subspace can be zero. Second, a scalar multiple $zw$ is *complex-linearly dependent* on $w$; so orbits never leave a complex line, and this both blocks transitivity in dimension $\geq 2$ and identifies the quotient with the space of complex lines.

**Theorem routing.** For part 2 we use the definition of freeness directly: a point of $S^{2n-1}$ is a *unit* vector, hence non-zero, so it has a non-zero coordinate on which we cancel. For part 3 we split into $n = 1$ (where the action is left multiplication on the group $U(1)$, transitive by solving $z w = y$) and $n \geq 2$ (where two independent unit vectors, such as the first two standard basis vectors, cannot be scalar multiples of each other). For part 4 we prove "same orbit $\iff$ same complex line" and then invoke the quotient-manifold theorem for free proper actions — the action is free (part 2) and proper ($U(1)$ compact) — to conclude that $U(1) \backslash S^{2n-1}$ is a smooth manifold of dimension $(2n - 1) - 1 = 2(n-1)$, which is $\mathbb{CP}^{n-1}$ by the line identification. The routing is recorded on **[[Def - Complex Projective Space as a Quotient]]** and **[[Thm - Quotient Manifold Theorem for Free Proper Actions]]**.

**Key decision point.** The one decision that makes everything short is to *read a point of the sphere as a non-zero vector on which cancellation is legal*. Freeness is not a statement about the sphere's geometry; it is the algebraic fact that in a field, $z w_j = w_j$ with $w_j \neq 0$ forces $z = 1$, and a unit vector always has such a coordinate. The complementary decision, for the orbit space, is to notice that "differ by a unit scalar" and "span the same complex line" are the *same relation* on unit vectors — the containment is immediate one way, and the reverse uses that a scalar relating two *unit* vectors automatically has modulus one.

---

# Legal Operations Used

This solution deploys the following operations, to be reconciled with the numbered Legal Operations of the (not-yet-written) topic page for §1.5.

1. **Confirm an action is well defined by checking the target constraint.** Verify $|z \cdot w| = 1$ so that $z \cdot w \in S^{2n-1}$, then check the two action axioms and smoothness.

2. **Prove freeness by field cancellation on a non-zero coordinate.** From $z \cdot w = w$ with $w$ a unit vector, pick a coordinate $w_j \neq 0$ and cancel it in $z w_j = w_j$ to force $z = 1$.

3. **Descend from freeness to effectiveness.** Invoke that a free action on a non-empty manifold is automatically effective.

4. **Split transitivity by dimension.** Treat $n = 1$ (transitive: the action is left multiplication on $U(1)$) and $n \geq 2$ (not transitive: exhibit two orbits) separately.

5. **Refute transitivity by a linear-dependence invariant.** Show $z \cdot w$ is a complex-scalar multiple of $w$; two complex-independent unit vectors then lie in different orbits.

6. **Translate "same orbit" into "same complex line".** Prove $w' \in U(1) \cdot w \iff \mathbb{C} w = \mathbb{C} w'$, using that a scalar relating two unit vectors has modulus one.

7. **Identify the quotient as a manifold via the quotient-manifold theorem.** Since the action is free and proper, conclude the orbit space is a smooth manifold of dimension $\dim S^{2n-1} - \dim U(1) = 2(n-1)$, namely $\mathbb{CP}^{n-1}$.

---

# Hints

> [!note]- Hint 1
> A point $w$ of the sphere is a *unit* vector, so it cannot be zero: at least one coordinate $w_j$ is non-zero. If $z \cdot w = w$, what does the $j$-th coordinate equation $z w_j = w_j$ tell you, given that you are allowed to divide by $w_j$ in $\mathbb{C}$?

> [!note]- Hint 2
> For transitivity when $n = 1$: the sphere $S^1$ *is* the group $U(1)$, and the action is $z \cdot w = z w$ — plain group multiplication. Solve $z w = y$ for $z$. For $n \geq 2$: any point in the orbit of $w$ is a scalar multiple of $w$; can $(1, 0, \dots, 0)$ and $(0, 1, 0, \dots, 0)$ be scalar multiples of each other?

> [!note]- Hint 3
> For the orbit space: $w$ and $w'$ are in the same orbit iff $w' = z w$ for some $|z| = 1$. If instead you only know $w' = \lambda w$ for some $\lambda \in \mathbb{C}^{\ast}$ (that is, $w, w'$ span the same complex line), take norms of both sides — what must $|\lambda|$ be, since $|w| = |w'| = 1$?

> [!note]- Hint 4
> Once "same orbit $\iff$ same complex line" is established, the orbit space is the set of complex lines in $\mathbb{C}^n$, which is $\mathbb{CP}^{n-1}$. To know it is a genuine smooth manifold, note the action is free (part 2) and proper (the group $U(1)$ is compact) and apply the quotient-manifold theorem; the dimension is $(2n - 1) - 1$.

---

# Solution

The action is free for a purely algebraic reason: a point of the sphere is a non-zero vector, and on any non-zero coordinate the equation $z w_j = w_j$ cancels to $z = 1$ because $\mathbb{C}$ is a field. Transitivity holds only in the degenerate case $n = 1$, where the sphere coincides with the group and the action is left multiplication; for $n \geq 2$ the orbit of $w$ consists only of scalar multiples of $w$, so two independent unit vectors are unreachable from each other. Finally, two unit vectors are in the same orbit exactly when they differ by a unit scalar, which is the same as spanning the same complex line, so the orbit space is the space of complex lines, $\mathbb{CP}^{n-1}$; freeness and properness make it a smooth manifold of dimension $2(n-1)$.

**Step 1: The action is well defined and smooth.**

Scalar multiplication by a unit complex number sends $S^{2n-1}$ to itself and satisfies the action axioms smoothly.

> [!note]- Derivation
> **Target constraint.** For $z \in U(1)$ and $w \in S^{2n-1}$,
> $$|z \cdot w|^2 = \sum_{j=1}^n |z w_j|^2 = |z|^2 \sum_{j=1}^n |w_j|^2 = 1 \cdot |w|^2 = 1 \qquad \text{(since $|z| = 1$ and $|w| = 1$),}$$
> so $z \cdot w \in S^{2n-1}$; the map $U(1) \times S^{2n-1} \to S^{2n-1}$ is well defined.
>
> **Action axioms.** For $z_1, z_2 \in U(1)$ and $w \in S^{2n-1}$, $(z_1 z_2) \cdot w = ((z_1 z_2) w_j)_j = (z_1 (z_2 w_j))_j = z_1 \cdot (z_2 \cdot w)$ by associativity of multiplication in $\mathbb{C}$, and $1 \cdot w = (1 \cdot w_j)_j = w$. Hence the two axioms of a left action hold.
>
> **Smoothness.** Componentwise the map is $(z, w) \mapsto (z w_1, \dots, z w_n)$, each entry a polynomial (indeed bilinear) function of the real and imaginary parts of $z$ and the $w_j$; the restriction of a smooth map on $U(1) \times \mathbb{C}^n$ to the embedded submanifolds $U(1) \times S^{2n-1}$ and $S^{2n-1}$ is smooth. Thus this is a smooth left action in the sense of **[[Def - Smooth Action of a Lie Group]]**.

**Step 2: The action is free.**

If $z \cdot w = w$ for some $w \in S^{2n-1}$, then $z = 1$.

> [!note]- Derivation
> Suppose $z \in U(1)$ and $w \in S^{2n-1}$ satisfy $z \cdot w = w$, that is, $z w_j = w_j$ for every $j$. Because $|w| = 1 \neq 0$, the vector $w$ is not the zero vector, so there exists an index $k$ with $w_k \neq 0$. For that index,
> $$z w_k = w_k \quad\Longrightarrow\quad (z - 1) w_k = 0 \quad\Longrightarrow\quad z - 1 = 0 \qquad \text{(dividing by $w_k \neq 0$ in the field $\mathbb{C}$),}$$
> hence $z = 1$. Therefore the only group element with any fixed point is the identity: the action is **free** by the definition on **[[Def - Free, Transitive, Effective, and Proper Group Actions|the free/effective/transitive definition]]**.
>
> **Effectiveness.** Since $S^{2n-1} \neq \varnothing$ and every free action on a non-empty space is effective — a $z$ fixing all points fixes one point, so $z = 1$ — the action is also **effective**.

**Step 3: The action is transitive if and only if $n = 1$.**

For $n = 1$ the action is transitive; for $n \geq 2$ it is not.

> [!note]- Derivation
> **Case $n = 1$ (transitive).** Here $\mathbb{C}^1 = \mathbb{C}$ and $S^{1} = \{w \in \mathbb{C} : |w| = 1\} = U(1)$, and the action is $z \cdot w = z w$, ordinary multiplication in the group $U(1)$. Given $w, y \in S^1 = U(1)$, set $z := y w^{-1} = y \overline{w}$ (using $w^{-1} = \overline{w}$ for $|w| = 1$); then $z \in U(1)$ because $|z| = |y||w|^{-1} = 1$, and $z \cdot w = y w^{-1} w = y$. Hence every point is reachable from every other, and the action is **transitive** (it is the left multiplication action of $U(1)$ on itself).
>
> **Case $n \geq 2$ (not transitive).** For any $w \in S^{2n-1}$, every point of its orbit is a complex-scalar multiple of $w$: $z \cdot w = z w \in \mathbb{C} w$. Consider the two standard unit vectors
> $$e_1 = (1, 0, 0, \dots, 0), \qquad e_2 = (0, 1, 0, \dots, 0),$$
> which lie in $S^{2n-1}$ because $n \geq 2$ (both have norm $1$). They are complex-linearly independent, so $e_2$ is *not* a complex-scalar multiple of $e_1$; in particular there is no $z$ with $z e_1 = e_2$. Thus $e_2 \notin U(1) \cdot e_1$, and the action is **not transitive**.
>
> Combining the two cases, the action is transitive precisely when $n = 1$.

**Step 4: The orbit space is $\mathbb{CP}^{n-1}$.**

Two unit vectors are in the same orbit exactly when they span the same complex line; hence $U(1) \backslash S^{2n-1}$ is the space of complex lines, a smooth manifold of dimension $2(n-1)$.

> [!note]- Derivation
> **Same orbit $\Rightarrow$ same complex line.** If $w' \in U(1) \cdot w$, then $w' = z w$ for some $z \in U(1) \subseteq \mathbb{C}^{\ast}$, so $w'$ is a non-zero scalar multiple of $w$ and $\mathbb{C} w' = \mathbb{C} w$ — the two vectors span the same complex line.
>
> **Same complex line $\Rightarrow$ same orbit.** Suppose $\mathbb{C} w = \mathbb{C} w'$ with $w, w' \in S^{2n-1}$. Since $w \neq 0$ spans the line and $w'$ lies on it, $w' = \lambda w$ for some $\lambda \in \mathbb{C}$; and $\lambda \neq 0$ because $w' \neq 0$. Taking norms,
> $$1 = |w'| = |\lambda w| = |\lambda|\,|w| = |\lambda| \qquad \text{(since $|w| = |w'| = 1$),}$$
> so $|\lambda| = 1$, that is, $\lambda \in U(1)$. Then $w' = \lambda \cdot w \in U(1) \cdot w$: the two points are in the same orbit.
>
> Therefore the orbits are in bijection with the complex lines of $\mathbb{C}^n$, and
> $$U(1) \backslash S^{2n-1} = \{\text{complex lines in } \mathbb{C}^n\} = \mathbb{CP}^{n-1}$$
> as a set, matching the description on **[[Def - Complex Projective Space as a Quotient]]**.
>
> **Smooth-manifold structure.** By Step 2 the action is free, and it is proper because $U(1)$ is compact (every action of a compact Lie group is proper). The quotient-manifold theorem then applies: for a smooth, free, and proper action of $G$ on $M$, the orbit space $G \backslash M$ carries a unique smooth manifold structure of dimension $\dim M - \dim G$ for which the projection is a submersion (see **[[Thm - Quotient Manifold Theorem for Free Proper Actions]]**). Here $\dim M = \dim S^{2n-1} = 2n - 1$ and $\dim G = \dim U(1) = 1$, so
> $$\dim_{\mathbb{R}} \big(U(1) \backslash S^{2n-1}\big) = (2n - 1) - 1 = 2(n - 1),$$
> and the orbit space is the smooth manifold $\mathbb{CP}^{n-1}$ of real dimension $2(n-1)$.

> [!note]- Complete formal solution
> **Claim.** The scalar action of $U(1)$ on $S^{2n-1} \subseteq \mathbb{C}^n$ is a smooth, free (hence effective) action; it is transitive if and only if $n = 1$; and its orbit space is $\mathbb{CP}^{n-1}$, a smooth manifold of real dimension $2(n-1)$.
>
> *Well defined and smooth.* For $z \in U(1)$, $|z \cdot w| = |z|\,|w| = 1$, so $z \cdot w \in S^{2n-1}$; associativity of complex multiplication gives $(z_1 z_2)\cdot w = z_1 \cdot(z_2 \cdot w)$ and $1 \cdot w = w$; the coordinate maps $(z, w) \mapsto z w_j$ are bilinear, hence smooth.
>
> *Free.* If $z \cdot w = w$ with $w \in S^{2n-1}$, then $w \neq 0$, so some $w_k \neq 0$; from $z w_k = w_k$ and cancellation in $\mathbb{C}$, $z = 1$. A free action on a non-empty manifold is effective, so the action is effective as well.
>
> *Transitivity.* If $n = 1$, then $S^1 = U(1)$ and $z \cdot w = zw$; given $w, y$, the element $z = y\overline{w} \in U(1)$ satisfies $z \cdot w = y$, so the action is transitive. If $n \geq 2$, every orbit point $z \cdot w = zw$ lies on $\mathbb{C} w$, and $e_1, e_2 \in S^{2n-1}$ are complex-independent, so $e_2 \notin U(1) \cdot e_1$; the action is not transitive.
>
> *Orbit space.* Points $w, w' \in S^{2n-1}$ satisfy $w' \in U(1) \cdot w \iff w' = zw$ with $|z| = 1 \iff \mathbb{C} w = \mathbb{C} w'$; the forward direction is clear, and conversely $w' = \lambda w$ with $|w| = |w'| = 1$ forces $|\lambda| = 1$. Hence the orbits are the complex lines and $U(1) \backslash S^{2n-1} = \mathbb{CP}^{n-1}$ as a set. The action is free and proper ($U(1)$ compact), so by the quotient-manifold theorem the orbit space is a smooth manifold of dimension $(2n - 1) - 1 = 2(n-1)$, namely $\mathbb{CP}^{n-1}$. $\blacksquare$

> [!warning] Illegal but tempting: cancelling before checking the coordinate is non-zero
> The freeness argument cancels $w_k$ in $z w_k = w_k$. This step is legal *only* after producing an index $k$ with $w_k \neq 0$, which is why the hypothesis $w \in S^{2n-1}$ (a unit, hence non-zero, vector) is essential. If one allowed $w = 0$ — as one could on all of $\mathbb{C}^n$ rather than the sphere — every $z$ would fix $w$, the origin would be a fixed point, and the action on $\mathbb{C}^n$ would not be free. The restriction to the sphere (equivalently, to $\mathbb{C}^n \setminus \{0\}$ before normalising) is exactly what removes the origin and makes the field-cancellation argument valid everywhere.

---

# Key Takeaways

**Freeness of a linear scalar action is field cancellation, and it needs the zero vector removed.** The heart of this exercise is one implication: in a field, $z w_k = w_k$ with $w_k \neq 0$ gives $z = 1$. The geometry of the sphere enters only to guarantee a non-zero coordinate exists — a unit vector is never zero. The reusable principle is that a group of scalars acts freely on a vector space *with the origin deleted* precisely because the origin is the unique common fixed point of all scalars; deleting it (or passing to the unit sphere) is the standard device that turns a linear representation into a free action. Recognise the trigger whenever a group acts by an invertible scalar or by a representation and you are asked about freeness: the fixed points are exactly the vectors killed by $(g - \operatorname{id})$, and freeness is the statement that no non-identity element leaves any non-zero vector fixed. This is the free counterpart of the non-free rotation action of the companion exercise **[[Ex - Rotation of the Sphere about an Axis]]**, where the fixed axis meets the sphere in genuine fixed points.

**Transitivity of a scalar action collapses in dimension two and above because scalars cannot change direction.** Every point of an orbit is a scalar multiple of its neighbours, so an orbit is confined to a single line; when the space has complex dimension at least two, there are independent directions no scalar can connect, and transitivity fails. Transitivity survives only in the borderline case $n = 1$, and there for a structural reason worth remembering: the sphere $S^1$ *is* the group $U(1)$, and a group always acts transitively on itself by translation. The transferable diagnostic: an action whose orbits are constrained to lie in proper subspaces (lines, level sets, leaves) can only be transitive if the whole space is a single such subspace. When you must decide transitivity, look for an invariant subspace or an invariant function through each orbit; if one exists non-trivially, transitivity is impossible above the borderline dimension.

**"Same orbit" and "same complex line" are the same relation on unit vectors, and this is what makes the quotient a projective space.** The identification $U(1) \backslash S^{2n-1} = \mathbb{CP}^{n-1}$ rests on the observation that on *unit* vectors, differing by a general non-zero scalar is no more general than differing by a unit scalar — taking norms forces the scalar to have modulus one. This is the mechanism by which two apparently different quotients coincide: normalising to the sphere and quotienting by $U(1)$ gives the same result as quotienting $\mathbb{C}^n \setminus \{0\}$ by all of $\mathbb{C}^{\ast}$. Once the set-level identification is in hand, the smooth structure is not extra work but a citation: the action is free (the algebraic cancellation) and proper (compactness of $U(1)$), so the quotient-manifold theorem delivers a boundaryless smooth manifold of the predicted dimension $2(n-1)$. Carry away that projective spaces are the archetype of "free circle quotient of an odd sphere", the total spaces of the Hopf-type fibrations $U(1) \to S^{2n-1} \to \mathbb{CP}^{n-1}$ that reappear throughout gauge theory as the simplest non-trivial principal $U(1)$-bundles.
