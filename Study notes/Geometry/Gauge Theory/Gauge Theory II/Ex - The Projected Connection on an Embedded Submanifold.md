---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Connection on a Vector Bundle"
  - "Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)"
  - "Def - Metric-Compatible Connection"
  - "Def - Induced Metric on a Submanifold"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $M \subset \mathbb{R}^N$ be an embedded submanifold of dimension $n$, and let $\langle\cdot,\cdot\rangle$ be the standard inner product on $\mathbb{R}^N$. The tangent bundle $TM$ sits naturally as a subbundle of the **product bundle** $\underline{\mathbb{R}^N} := M \times \mathbb{R}^N$: at each point $m \in M$ the fibre $T_mM$ is a linear subspace of $\mathbb{R}^N$, so a section $s \in \Gamma(TM)$ is the same datum as a smooth map $s : M \to \mathbb{R}^N$ with $s(m) \in T_mM$ for every $m$. Write $\operatorname{pr}_m : \mathbb{R}^N \to T_mM$ for the orthogonal projection onto $T_mM$ (with respect to $\langle\cdot,\cdot\rangle$), and let $\operatorname{pr} \in \Gamma(\operatorname{End}\underline{\mathbb{R}^N})$ denote the resulting bundle endomorphism $m \mapsto \operatorname{pr}_m$. Let $d$ be the ordinary (componentwise) differential of an $\mathbb{R}^N$-valued map, so that $ds \in \Omega^1(M; \underline{\mathbb{R}^N})$.

Define
$$\nabla s := \operatorname{pr}(ds), \qquad \text{that is} \qquad (\nabla s)(v) := \operatorname{pr}_m\!\big(ds(v)\big) \quad \text{for } v \in T_mM.$$

Prove the following three assertions.

1. **($\nabla$ is a connection.)** The map $\nabla$ is $\mathbb{R}$-linear and satisfies the Leibniz rule $\nabla(fs) = df \otimes s + f\,\nabla s$ for all $f \in C^\infty(M)$ and $s \in \Gamma(TM)$; hence $\nabla$ is a covariant derivative on $TM$ (Haydys, *Introduction to Gauge Theory*, Example 10, p. 7).
2. **($\nabla_X Y$ is tangent.)** For vector fields $X, Y \in \mathfrak{X}(M)$, the value $\nabla_X Y(m)$ lies in $T_mM$; equivalently, $\nabla$ takes values in $\Omega^1(M; TM)$ rather than merely in $\Omega^1(M; \underline{\mathbb{R}^N})$. The complementary normal part $\operatorname{pr}^\perp(D_X Y)$, where $\operatorname{pr}^\perp := \mathrm{id} - \operatorname{pr}$ and $D = d$, is the second fundamental form.
3. **(Identification.)** Equip $M$ with the metric $g := \iota^*\langle\cdot,\cdot\rangle$ induced by the inclusion $\iota : M \hookrightarrow \mathbb{R}^N$. Then $\nabla$ is metric-compatible and torsion-free; consequently, by the uniqueness clause of the fundamental theorem of Riemannian geometry, $\nabla$ is the **Levi-Civita connection $\nabla^g$ of $(M, g)$**.

**Recall:**

The objects in play are a connection on a vector bundle, the flat product connection $d$ on $\underline{\mathbb{R}^N}$, the orthogonal projection onto $TM$, the induced metric, and the two axioms — metric-compatibility and torsion-freeness — that pin down the Levi-Civita connection.

![[Def - Connection on a Vector Bundle#The Definition]]

Thus a **connection** on a vector bundle $E \to M$ is an $\mathbb{R}$-linear map $\nabla : \Gamma(E) \to \Omega^1(M; E)$ obeying $\nabla(fs) = df \otimes s + f\,\nabla s$; its **directional derivative** is $\nabla_v s := \iota_v \nabla s = (\nabla s)(v)$ for $v \in T_mM$, and for a vector field $X$ we write $\nabla_X s$ for the section $m \mapsto \nabla_{X(m)}s$. The **flat product connection** on $\underline{\mathbb{R}^N} = M \times \mathbb{R}^N$ is $D = d$: writing a section as a map $s : M \to \mathbb{R}^N$, one sets $D_X s = ds(X)$, the componentwise directional derivative $\big(X s^1, \dots, X s^N\big)$. Its connection matrix in the constant standard frame is zero.

![[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)#Statement]]

We use only the **uniqueness** half of this theorem: on $(M, g)$ there is *at most one* connection on $TM$ that is simultaneously **torsion-free** — $\nabla_X Y - \nabla_Y X = [X, Y]$ for all $X, Y \in \mathfrak{X}(M)$ — and **metric-compatible** — $X\,g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$ for all $X, Y, Z \in \mathfrak{X}(M)$ (see [[Def - Metric-Compatible Connection|metric-compatible connection]]), and that connection is the Levi-Civita connection $\nabla^g$.

![[Def - Induced Metric on a Submanifold#The Definition]]

Concretely, the **induced metric** $g := \iota^*\langle\cdot,\cdot\rangle$ on $M \subset \mathbb{R}^N$ is $g_m(u, w) = \langle u, w\rangle$ for $u, w \in T_mM \subset \mathbb{R}^N$; it is simply the ambient inner product restricted to tangent vectors of $M$.

Two properties of the orthogonal projection are used repeatedly and recorded here. First, $\operatorname{pr}_m$ is a **linear** map $\mathbb{R}^N \to \mathbb{R}^N$ with image $T_mM$, and it is the identity on its image: $\operatorname{pr}_m(u) = u$ whenever $u \in T_mM$. Second, $\operatorname{pr}_m$ is **self-adjoint** and its kernel is the orthogonal complement $(T_mM)^\perp =: N_mM$, so that for any $w \in \mathbb{R}^N$ and any tangent $u \in T_mM$,
$$\langle w, u\rangle = \langle \operatorname{pr}_m w, u\rangle \qquad \text{(because } w - \operatorname{pr}_m w \in N_mM \perp u\text{).}$$
Smoothness of $\operatorname{pr}$ as a bundle endomorphism is the statement that $TM$ is a smooth subbundle of $\underline{\mathbb{R}^N}$; locally, if $\nu_{n+1}, \dots, \nu_N$ is a smooth orthonormal frame of the normal bundle, then $\operatorname{pr}^\perp = \sum_{\alpha} \nu_\alpha \nu_\alpha^{\mathsf t}$ is smooth, hence so is $\operatorname{pr} = \mathrm{id} - \operatorname{pr}^\perp$.

---

# Convergent Strategy

**Problem class.** This is a *verify-the-axioms-then-invoke-uniqueness* problem. Two separate things are asked: (i) that a concretely constructed operator satisfies the abstract definition of a connection, which is a direct Leibniz computation, and (ii) that this connection *coincides* with a connection defined by a universal property — the Levi-Civita connection. Problems of type (ii) are almost never solved by comparing formulas; they are solved by checking that the concrete object satisfies the two characterising axioms and then citing the uniqueness theorem. The submanifold connection $\nabla s = \operatorname{pr}(ds)$ is the founding example of gauge theory precisely because it exhibits, in the most tangible possible setting, the two ideas the abstract theory abstracts: covariant differentiation as "differentiate ambiently, then project back", and curvature as the failure of that projection to commute with a second differentiation (pursued in [[Ex - The Curvature of the Projected Connection on the Sphere]]).

**Assumption pattern.** Everything rests on a single structural fact about the ambient bundle: the flat connection $D = d$ on $\underline{\mathbb{R}^N}$ is both **metric** (for the *constant* inner product $\langle\cdot,\cdot\rangle$, differentiation obeys the product rule $X\langle Y, Z\rangle = \langle D_X Y, Z\rangle + \langle Y, D_X Z\rangle$) and **torsion-free** ($D_X Y - D_Y X = [X, Y]$). The construction $\nabla = \operatorname{pr}\circ D$ inherits both properties because the projection is chosen orthogonally: an orthogonal projection is *invisible* to inner products against vectors already in its image, and it kills exactly the normal directions that the two axioms are willing to discard.

**Theorem routing.** For part 1, route directly through the [[Def - Connection on a Vector Bundle|definition of a connection]]: use linearity of $d$ and of $\operatorname{pr}_m$ for $\mathbb{R}$-linearity, and the ordinary Leibniz rule $d(fs) = df\cdot s + f\,ds$ followed by the identity $\operatorname{pr}(s) = s$ for tangent $s$. For part 2, route through the defining property of an orthogonal projection: its image is $T_mM$. For part 3, route through the [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem of Riemannian geometry]]: verify metric-compatibility using self-adjointness of $\operatorname{pr}$, verify torsion-freeness using the torsion-freeness of $D$ together with the tangency of the Lie bracket of tangent fields, and then invoke *uniqueness* to conclude $\nabla = \nabla^g$.

**Key decision point.** The one move that is not mechanical is recognising, in part 3, that the two Levi-Civita axioms are exactly the two features of the flat ambient connection that *survive orthogonal projection*. Metric-compatibility survives because, when we pair $\nabla_X Y = \operatorname{pr}(D_X Y)$ against a *tangent* field $Z$, self-adjointness of $\operatorname{pr}$ lets us drop the projection: $g(\nabla_X Y, Z) = \langle \operatorname{pr}(D_X Y), Z\rangle = \langle D_X Y, Z\rangle$. Torsion-freeness survives because $D_X Y - D_Y X = [X, Y]$ is *already tangent*, so projecting it changes nothing. Seeing that these two cancellations are what the problem is really about turns a potentially long coordinate computation into two short lines.

---

# Legal Operations Used

This solution deploys the following operations; where the topic page for §2.2 exists, these are its Legal Operations, and the orchestrator will reconcile the numbering.

1. **Differentiate ambiently, then project (the projected connection).** Regard a section of the subbundle $TM \subset \underline{\mathbb{R}^N}$ as an $\mathbb{R}^N$-valued map, apply the flat connection $d$ that the trivial ambient bundle carries for free, and push the result back into $TM$ with the orthogonal projection. This manufactures a connection on a subbundle out of a connection on the ambient bundle.

2. **Use that an orthogonal projection is the identity on its image.** Since $s(m) \in T_mM = \operatorname{im}\operatorname{pr}_m$, we have $\operatorname{pr}_m(s(m)) = s(m)$; this is what turns the projected ordinary Leibniz rule into the connection Leibniz rule, and it is what makes the construction land in $TM$.

3. **Use self-adjointness of an orthogonal projection to drop it under a tangent pairing.** For $w \in \mathbb{R}^N$ and tangent $u \in T_mM$, $\langle \operatorname{pr}_m w, u\rangle = \langle w, u\rangle$. This converts $g(\nabla_X Y, Z)$ into the ambient pairing $\langle D_X Y, Z\rangle$, where the flat product rule is available.

4. **Inherit metric-compatibility from the flat product connection.** The constant ambient inner product makes $D = d$ metric; the product rule $X\langle Y, Z\rangle = \langle D_X Y, Z\rangle + \langle Y, D_X Z\rangle$ is then combined with operation 3.

5. **Inherit torsion-freeness from the flat product connection.** $D_X Y - D_Y X = [X, Y]$ in $\mathbb{R}^N$-components, and the bracket of two fields tangent to $M$ is again tangent to $M$, so projecting leaves it fixed.

6. **Pin down a connection by the two Levi-Civita axioms and cite uniqueness.** Having shown $\nabla$ is metric and torsion-free, invoke the uniqueness half of the [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem of Riemannian geometry]] to identify it with $\nabla^g$, with no formula comparison.

---

# Hints

> [!note]- Hint 1
> For part 1, do not think geometrically at all. Write $\nabla s = \operatorname{pr}(ds)$ and apply the *ordinary* Leibniz rule for the componentwise differential of the $\mathbb{R}^N$-valued map $fs$. Then you must move $\operatorname{pr}$ past a scalar $df$ and evaluate $\operatorname{pr}(s)$. What is $\operatorname{pr}_m$ applied to a vector that already lies in $T_mM$?

> [!note]- Hint 2
> For part 2, ask what the *image* of $\operatorname{pr}_m$ is by definition. The tangential–normal decomposition $D_X Y = \operatorname{pr}(D_X Y) + \operatorname{pr}^\perp(D_X Y)$ splits the ambient derivative into its tangent part (which is $\nabla_X Y$) and a normal part; the normal part is the second fundamental form and is the subject of a later exercise.

> [!note]- Hint 3
> For part 3, do not try to compute Christoffel symbols. The Levi-Civita connection is characterised by *two* axioms, and there is at most one connection satisfying both. So it suffices to check the two axioms for $\nabla = \operatorname{pr}\circ D$. For metric-compatibility, expand $X\,g(Y, Z) = X\langle Y, Z\rangle$ with the ordinary product rule for the constant inner product; you will meet $\langle D_X Y, Z\rangle$ with $Z$ tangent.

> [!note]- Hint 4
> To finish metric-compatibility, note $\langle D_X Y, Z\rangle = \langle \operatorname{pr}(D_X Y), Z\rangle$ because $Z$ is tangent and $D_X Y - \operatorname{pr}(D_X Y)$ is normal — this is self-adjointness of $\operatorname{pr}$. Hence $\langle D_X Y, Z\rangle = g(\nabla_X Y, Z)$. For torsion-freeness, use that $D$ itself is torsion-free ($D_X Y - D_Y X = [X, Y]$ componentwise) and that $[X, Y]$ is tangent to $M$, so $\operatorname{pr}[X, Y] = [X, Y]$.

---

# Solution

The three parts are, respectively, an application of the ordinary Leibniz rule, an appeal to the definition of "image of a projection", and a verification of the two Levi-Civita axioms followed by a uniqueness citation. The engine of part 3 is that the ambient flat connection $D = d$ is already metric and torsion-free, and orthogonal projection preserves exactly these two properties: metric-compatibility because $\operatorname{pr}$ is self-adjoint and disappears under a tangent pairing, torsion-freeness because the antisymmetric part $D_X Y - D_Y X = [X, Y]$ is already tangent and so is unchanged by projecting. We fix once and for all vector fields $X, Y, Z \in \mathfrak{X}(M)$, a section $s \in \Gamma(TM)$ regarded as a map $s : M \to \mathbb{R}^N$ with $s(m) \in T_mM$, and a function $f \in C^\infty(M)$.

**Step 1: $\nabla$ is well-defined and takes values in $\Omega^1(M; TM)$ (part 2).**

For each $m$, $(\nabla s)(v) = \operatorname{pr}_m(ds(v)) \in \operatorname{im}\operatorname{pr}_m = T_mM$; so $\nabla s$ is a $TM$-valued $1$-form and $\nabla_X Y(m) \in T_mM$.

> [!note]- Derivation
> By definition $\operatorname{pr}_m : \mathbb{R}^N \to \mathbb{R}^N$ is the orthogonal projection whose image is the linear subspace $T_mM \subseteq \mathbb{R}^N$. For any $v \in T_mM$ the vector $ds(v) \in \mathbb{R}^N$ is an ambient vector, and
> $$(\nabla s)(v) = \operatorname{pr}_m\big(ds(v)\big) \in \operatorname{im}\operatorname{pr}_m = T_mM \qquad \text{(definition of }\operatorname{pr}_m\text{).}$$
> Thus $\nabla s$ assigns to each $v \in T_mM$ a vector in $T_mM$, i.e. $\nabla s \in \Omega^1(M; TM)$; and $\operatorname{pr}$ is smooth (recorded in Notation: $TM$ is a smooth subbundle, so $\operatorname{pr} \in \Gamma(\operatorname{End}\underline{\mathbb{R}^N})$), so $\nabla s$ is smooth. In particular, taking $s = Y$ and $v = X(m)$, the value $\nabla_X Y(m) = \operatorname{pr}_m(D_X Y(m))$ lies in $T_mM$. **This is precisely part 2:** the projected derivative is tangent by construction. Writing $\operatorname{pr}^\perp := \mathrm{id} - \operatorname{pr}$ for the complementary projection onto the normal space $N_mM = (T_mM)^\perp$, we obtain the **tangential–normal decomposition of the ambient derivative**
> $$D_X Y = \underbrace{\operatorname{pr}(D_X Y)}_{= \nabla_X Y \in T_mM} + \underbrace{\operatorname{pr}^\perp(D_X Y)}_{=: \mathrm{II}(X, Y) \in N_mM},$$
> the **Gauss formula**; the normal part $\mathrm{II}(X, Y)$ is the [[Def - Second Fundamental Form|second fundamental form]], studied on its own page.

**Step 2: $\nabla$ is $\mathbb{R}$-linear and obeys the Leibniz rule (part 1).**

$\nabla$ is $\mathbb{R}$-linear because $d$ and each $\operatorname{pr}_m$ are; and $\nabla(fs) = df \otimes s + f\,\nabla s$.

> [!note]- Derivation
> **$\mathbb{R}$-linearity.** The componentwise differential $d : \Gamma(\underline{\mathbb{R}^N}) \to \Omega^1(M; \underline{\mathbb{R}^N})$ is $\mathbb{R}$-linear, and $\operatorname{pr}$ acts fibrewise by the linear maps $\operatorname{pr}_m$; the composite $\nabla = \operatorname{pr}\circ d$ is therefore $\mathbb{R}$-linear: for $s_1, s_2 \in \Gamma(TM)$ and $a, b \in \mathbb{R}$,
> $$\nabla(a s_1 + b s_2) = \operatorname{pr}\big(d(a s_1 + b s_2)\big) = \operatorname{pr}\big(a\,ds_1 + b\,ds_2\big) = a\,\operatorname{pr}(ds_1) + b\,\operatorname{pr}(ds_2) = a\,\nabla s_1 + b\,\nabla s_2 \quad \text{(linearity of } d \text{ and of }\operatorname{pr}_m\text{).}$$
>
> **Leibniz rule.** By the ordinary Leibniz rule for the differential of the $\mathbb{R}^N$-valued map $fs$ (which is componentwise the scalar Leibniz rule $d(f s^i) = df\,s^i + f\,ds^i$),
> $$d(fs) = df \otimes s + f\,ds \qquad \text{(ordinary product rule, componentwise).}$$
> Apply $\operatorname{pr}$ and use that it is $\mathbb{R}$-linear and $C^\infty(M)$-linear fibrewise (it commutes with multiplication by the scalar $f(m)$ and by the scalar $df(v)$):
> $$\nabla(fs) = \operatorname{pr}\big(df \otimes s\big) + \operatorname{pr}\big(f\,ds\big) = df \otimes \operatorname{pr}(s) + f\,\operatorname{pr}(ds) \qquad \text{(}\operatorname{pr}_m \text{ linear; scalars } df(v), f(m) \text{ pass through).}$$
> Now $s(m) \in T_mM$, and $\operatorname{pr}_m$ is the identity on $T_mM$, so $\operatorname{pr}(s) = s$ (operation 2). Hence
> $$\nabla(fs) = df \otimes s + f\,\nabla s \qquad \text{(since }\operatorname{pr}(s) = s \text{ and } \operatorname{pr}(ds) = \nabla s\text{).}$$
> Together with $\mathbb{R}$-linearity and the fact (Step 1) that the target is $\Omega^1(M; TM)$, this shows $\nabla$ is a connection on $TM$ in the sense of the [[Def - Connection on a Vector Bundle|definition]]. **This is part 1.**

**Step 3: $\nabla$ is metric-compatible for the induced metric $g$ (part 3, first axiom).**

For all $X, Y, Z \in \mathfrak{X}(M)$, $X\,g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$.

> [!note]- Derivation
> Recall $g(Y, Z) = \langle Y, Z\rangle$ as a function on $M$, where $Y, Z : M \to \mathbb{R}^N$ take tangent values and $\langle\cdot,\cdot\rangle$ is the *constant* ambient inner product. Differentiating this scalar function along $X$ with the ordinary product rule for a bilinear pairing of $\mathbb{R}^N$-valued maps — legitimate because $\langle\cdot,\cdot\rangle$ has constant coefficients, so the flat connection $D = d$ is compatible with it — gives
> $$X\,g(Y, Z) = X\langle Y, Z\rangle = \langle D_X Y, Z\rangle + \langle Y, D_X Z\rangle \qquad \text{(product rule for the constant inner product; } D_X Y = ds\text{-type derivative).}$$
> Consider the first term. Because $Z(m) \in T_mM$ is tangent and $\operatorname{pr}_m$ is the self-adjoint orthogonal projection with kernel $N_mM$, the normal part of $D_X Y$ pairs to zero against $Z$ (operation 3):
> $$\langle D_X Y, Z\rangle = \langle \operatorname{pr}(D_X Y), Z\rangle + \langle \operatorname{pr}^\perp(D_X Y), Z\rangle = \langle \operatorname{pr}(D_X Y), Z\rangle + 0 = \langle \nabla_X Y, Z\rangle \quad \text{(}\operatorname{pr}^\perp(D_X Y) \in N_mM \perp Z\text{; Step 1).}$$
> Since both $\nabla_X Y$ and $Z$ are tangent, $\langle \nabla_X Y, Z\rangle = g(\nabla_X Y, Z)$ by the definition of the induced metric. The same argument with $Y$ and $Z$ interchanged in their roles gives $\langle Y, D_X Z\rangle = \langle Y, \operatorname{pr}(D_X Z)\rangle = g(Y, \nabla_X Z)$, using that $Y$ is tangent and $\operatorname{pr}$ self-adjoint. Substituting both,
> $$X\,g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z),$$
> which is condition (1) of a [[Def - Metric-Compatible Connection|metric-compatible connection]]. Every hypothesis was used: constancy of $\langle\cdot,\cdot\rangle$ (product rule), self-adjointness of $\operatorname{pr}$ (dropping the projection), and tangency of $Y, Z$ (identifying $\langle\cdot,\cdot\rangle$ with $g$).

**Step 4: $\nabla$ is torsion-free (part 3, second axiom).**

For all $X, Y \in \mathfrak{X}(M)$, $\nabla_X Y - \nabla_Y X = [X, Y]$.

> [!note]- Derivation
> The ambient flat connection $D = d$ is **torsion-free**: writing $Y = (Y^1, \dots, Y^N)$ and $X = (X^1, \dots, X^N)$ in the standard coordinates of $\mathbb{R}^N$, one has $D_X Y = (X Y^1, \dots, X Y^N)$ and $D_Y X = (Y X^1, \dots, Y X^N)$, whence, componentwise,
> $$D_X Y - D_Y X = \big(X Y^i - Y X^i\big)_{i=1}^N = \big([X, Y]^i\big)_{i=1}^N = [X, Y] \qquad \text{(definition of the Lie bracket on each coordinate function).}$$
> Here $[X, Y]$ denotes the Lie bracket of the vector fields $X, Y$ *on the manifold* $M$, embedded into $\mathbb{R}^N$ via $\iota$; it is again a vector field on $M$, hence **tangent**: $[X, Y](m) \in T_mM$ for every $m$. (The bracket of two fields tangent to a submanifold is tangent to it — this is the tangency needed, and it holds because $[X,Y]f = X(Yf) - Y(Xf)$ acts as a derivation on functions on $M$, so it is a genuine element of $\mathfrak{X}(M)$.) Now project. Since $\operatorname{pr}$ is linear,
> $$\nabla_X Y - \nabla_Y X = \operatorname{pr}(D_X Y) - \operatorname{pr}(D_Y X) = \operatorname{pr}\big(D_X Y - D_Y X\big) = \operatorname{pr}\,[X, Y] \qquad \text{(linearity of }\operatorname{pr}\text{; the previous line).}$$
> Because $[X, Y]$ is already tangent, $\operatorname{pr}[X, Y] = [X, Y]$ (operation 2). Hence
> $$\nabla_X Y - \nabla_Y X = [X, Y],$$
> which is exactly torsion-freeness. The projection did no work here: the antisymmetric combination it was fed was already in its image.

**Step 5: Conclude $\nabla = \nabla^g$ (part 3, identification).**

$\nabla$ is a connection on $TM$ that is both metric-compatible and torsion-free for $g$; by uniqueness, $\nabla = \nabla^g$.

> [!note]- Derivation
> By Steps 1–2, $\nabla$ is a connection on $TM$; by Step 3 it is metric-compatible for the induced metric $g = \iota^*\langle\cdot,\cdot\rangle$; by Step 4 it is torsion-free. The [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem of Riemannian geometry]] asserts that on $(M, g)$ there is a *unique* connection on $TM$ satisfying both conditions, and names it the Levi-Civita connection $\nabla^g$. Since $\nabla$ satisfies both conditions, uniqueness forces
> $$\nabla = \nabla^g.$$
> No coordinate computation and no comparison of Christoffel symbols was needed: the identification is a corollary of a uniqueness theorem applied to two verified axioms. **This is part 3.** The concrete instance $M = S^2 \subset \mathbb{R}^3$, where one reads off the connection matrix in the coordinate frame and matches it against the Christoffel symbols of the round metric, is carried out in [[Ex - The Levi-Civita Connection of the Round Sphere as a Connection Matrix]] (and its curvature in [[Ex - The Curvature of the Projected Connection on the Sphere]]).

> [!note]- Complete formal solution
> **Claim.** Let $M \subset \mathbb{R}^N$ be an embedded submanifold with the induced metric $g = \iota^*\langle\cdot,\cdot\rangle$, and define $\nabla s = \operatorname{pr}(ds)$ on $\Gamma(TM)$, where $\operatorname{pr}_m : \mathbb{R}^N \to T_mM$ is orthogonal projection and $d$ is the componentwise differential. Then $\nabla$ is a connection on $TM$ taking values in $\Omega^1(M; TM)$, and $\nabla = \nabla^g$, the Levi-Civita connection of $(M, g)$.
>
> *Proof.* Fix $X, Y, Z \in \mathfrak{X}(M)$, $s \in \Gamma(TM)$ (a map $M \to \mathbb{R}^N$ with $s(m) \in T_mM$), and $f \in C^\infty(M)$. Throughout, $D = d$ denotes the flat product connection on $\underline{\mathbb{R}^N}$, and we use two facts about the orthogonal projection: $\operatorname{pr}_m$ is the identity on $T_mM$, and $\operatorname{pr}_m$ is self-adjoint with kernel $N_mM = (T_mM)^\perp$.
>
> *($\nabla$ is $TM$-valued.)* $(\nabla s)(v) = \operatorname{pr}_m(ds(v)) \in \operatorname{im}\operatorname{pr}_m = T_mM$; so $\nabla s \in \Omega^1(M; TM)$, and $\nabla_X Y(m) \in T_mM$.
>
> *($\nabla$ is a connection.)* $\nabla = \operatorname{pr}\circ d$ is $\mathbb{R}$-linear since $d$ and $\operatorname{pr}$ are. By the ordinary product rule $d(fs) = df\otimes s + f\,ds$, applying $\operatorname{pr}$ and using $\operatorname{pr}(s) = s$ (as $s$ is tangent),
> $$\nabla(fs) = df\otimes\operatorname{pr}(s) + f\,\operatorname{pr}(ds) = df\otimes s + f\,\nabla s.$$
> So $\nabla$ satisfies the Leibniz rule and is a connection on $TM$.
>
> *(Metric-compatible.)* Since $\langle\cdot,\cdot\rangle$ is constant, $X\langle Y, Z\rangle = \langle D_X Y, Z\rangle + \langle Y, D_X Z\rangle$. As $Z$ is tangent and $D_X Y - \operatorname{pr}(D_X Y) \in N_mM \perp Z$, we have $\langle D_X Y, Z\rangle = \langle\operatorname{pr}(D_X Y), Z\rangle = g(\nabla_X Y, Z)$; likewise $\langle Y, D_X Z\rangle = g(Y, \nabla_X Z)$. Hence $X g(Y, Z) = g(\nabla_X Y, Z) + g(Y, \nabla_X Z)$.
>
> *(Torsion-free.)* In $\mathbb{R}^N$-components, $D_X Y - D_Y X = (XY^i - YX^i)_i = [X, Y]$, which is tangent to $M$. Therefore $\nabla_X Y - \nabla_Y X = \operatorname{pr}(D_X Y - D_Y X) = \operatorname{pr}[X, Y] = [X, Y]$.
>
> *(Identification.)* $\nabla$ is a metric-compatible, torsion-free connection on $TM$ for $g$. By the uniqueness clause of the fundamental theorem of Riemannian geometry, the only such connection is $\nabla^g$. Hence $\nabla = \nabla^g$. $\blacksquare$

---

# Key Takeaways

**To prove a concretely built connection equals the Levi-Civita connection, verify the two characterising axioms and cite uniqueness — never compare Christoffel symbols.** The Levi-Civita connection is defined by a *universal property*: it is the unique connection on $TM$ that is both metric-compatible and torsion-free. Whenever a problem hands you some other connection — the projected connection here, a connection built from a moving frame, a connection pulled back from an ambient space — and asks whether it *is* the Levi-Civita connection, the efficient route is always the same: check metric-compatibility, check torsion-freeness, invoke the uniqueness half of the [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)|fundamental theorem]]. The alternative, computing both connections in coordinates and matching $\Gamma^k_{ij}$, is longer, chart-dependent, and obscures *why* the two agree. The trigger for this pattern is any sentence of the form "show that [this connection] is the Levi-Civita connection", and the diagnostic is: have I produced a coordinate formula (a warning sign), or have I verified two axioms (the intended path)?

**Orthogonal projection is metric-compatibility- and torsion-preserving; that is the entire content of the Gauss picture of submanifold geometry.** The ambient flat connection $D = d$ on $\underline{\mathbb{R}^N}$ is metric (the inner product is constant) and torsion-free (mixed partials commute). The projected connection $\nabla = \operatorname{pr}\circ D$ keeps both properties, and the reason is structural rather than computational. Metric-compatibility is kept because we only ever pair $\nabla_X Y$ against tangent fields, and *self-adjointness of the orthogonal projection lets the projection be dropped under a tangent pairing* — the normal part is annihilated. Torsion-freeness is kept because the torsion of $D$, namely $D_X Y - D_Y X - [X, Y]$, vanishes, and the surviving antisymmetric part $D_X Y - D_Y X = [X, Y]$ is *already tangent*, so projecting it is the identity. The normal information that projection discards — collected in the second fundamental form $\mathrm{II}(X, Y) = \operatorname{pr}^\perp(D_X Y)$ — is exactly the data of how $M$ curves inside $\mathbb{R}^N$, and it is precisely the data that the two Levi-Civita axioms are indifferent to. By **Nash's isometric embedding theorem** — which this series neither proves nor uses, and which is recorded here only as background — every Riemannian manifold can be realised isometrically as such a submanifold, so the picture just described, in which the intrinsic Levi-Civita connection is the tangential shadow of flat ambient differentiation, is in principle universal.

**"Differentiate ambiently, then project back" is the prototype of every covariant derivative, and the failure of projection to commute with a second differentiation is the prototype of curvature.** This exercise is the concrete seed from which the abstract theory of connections grows. A section of an abstract bundle cannot be differenced across fibres, so the covariant derivative is imposed axiomatically through the Leibniz rule; but here, in a submanifold of $\mathbb{R}^N$, the covariant derivative is *visibly* the honest derivative followed by a projection, and the Leibniz rule is *inherited* rather than postulated. The transferable diagnostic is that whenever a bundle sits inside a trivial (or flat) bundle — a subbundle, a bundle with a fixed background connection, an associated bundle built from a principal connection — the induced covariant derivative is "background-differentiate, then correct", and its curvature measures how far the correction is from being integrable. The next exercise, [[Ex - The Curvature of the Projected Connection on the Sphere]], differentiates the projection $\operatorname{pr} = \mathrm{id} - \nu\nu^{\mathsf t}$ a second time on $S^2$ and reads the round-sphere curvature $F(X, Y)Z = \langle Y, Z\rangle X - \langle X, Z\rangle Y$ straight out of the two normal terms, with no Gauss equation invoked — the same "project, then re-differentiate" mechanism, one order higher.
