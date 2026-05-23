---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Orientation of a Smooth Manifold"
  - "Def - Volume Form"
  - "Def - Oriented Atlas"
  - "Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form"
tags: [geometry, differential-geometry, orientation, sphere, mobius]
---

# Problem Statement

(a) Prove that the unit sphere $S^n \subseteq \mathbb{R}^{n+1}$ is orientable for every $n \geq 1$, by exhibiting an explicit nowhere-vanishing smooth $n$-form on $S^n$.

(b) Prove that the open Möbius strip $E$ — defined as the quotient of $\mathbb{R} \times (-1, 1)$ by the equivalence $(x, y) \sim (x + 1, -y)$ — is *not* orientable, by showing that any candidate smooth nowhere-vanishing 2-form on $E$, when transported once around the core circle, must change sign and so must vanish somewhere.

**Recall:**

A smooth manifold $M$ is **orientable** iff it admits a smooth nowhere-vanishing top-degree form:

![[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form#Statement]]

A **volume form** is a smooth nowhere-vanishing top-degree differential form:

![[Def - Volume Form#The Definition]]

An [[Def - Oriented Atlas|oriented atlas]] is a smooth atlas in which every transition map has positive Jacobian determinant.

---

# Convergent Strategy

**Problem class:** Orientability-or-refutation problem. Establishing or refuting orientability is one of the five recurring targets of [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem|the topic]], with two opposite routes: *exhibit* a nowhere-vanishing top-form to prove orientability, or show *every candidate must vanish* to refute it.

**Assumption pattern:** Part (a) gives the sphere as a hypersurface of $\mathbb{R}^{n+1}$ — the ambient Euclidean structure plus an outward-normal vector field (the position vector $x$) are all we need. Part (b) gives the Möbius strip as a quotient of $\mathbb{R} \times (-1, 1)$ by an orientation-reversing involution — the negative sign in the identification $(x, y) \sim (x + 1, -y)$ is the obstruction we will exploit. The quotient picture is the cleanest way to see the holonomy.

**Theorem routing:** For (a), the orientability criterion [[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form]] says it suffices to exhibit a nowhere-vanishing top-form. The construction uses contraction: contract the ambient volume form $dx^1\wedge\cdots\wedge dx^{n+1}$ with the outward normal $\nu = x^i\partial_i$, then restrict to $S^n$. For (b), we use the same criterion contrapositively: assume a global volume form exists, transport it via the deck transformation, and derive a contradiction (the transport multiplies by $-1$, forcing a sign-change on a connected manifold, which is impossible without a zero).

**Key decision point:** For (a), the choice of the position vector $x$ as outward normal is the natural one — but any nowhere-vanishing normal vector field would work; the position vector is just the simplest. For (b), the *quotient picture* is the key choice: working with the universal cover $\mathbb{R} \times (-1, 1)$ and analyzing how the deck transformation acts on the top-form makes the obstruction visible, whereas trying to work directly on $E$ obscures the topological argument.

---

# Legal Operations Used

1. **Operation 6 (exhibit a nowhere-vanishing top-form to prove orientability)** from the [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem#Legal Operations|topic page]]. In part (a), we apply this directly via the contraction trick — contract the ambient volume form with an outward normal, then restrict.

2. **Operation 10 (read the boundary/normal orientation off "outward-first")** from the topic page. The outward normal $\nu$ on $S^n$ is the position vector; "outward-first" means $(\nu, E_1, \ldots, E_n)$ is positively oriented in $\mathbb{R}^{n+1}$ iff $(E_1, \ldots, E_n)$ is positively oriented in $S^n$. This is the linear-algebra source of the contraction formula.

3. **Operation 8 (verify orientation-preservation via the sign of $\det DF$)** from the topic page. In part (b), we check that the deck transformation $\tau(x, y) = (x + 1, -y)$ has $\det D\tau = -1 < 0$, hence is orientation-*reversing*. This is the sign that creates the obstruction.

4. **The contrapositive use of operation 6.** To refute orientability, we suppose a global volume form exists and derive a contradiction. This requires verifying that *any* candidate form must change sign upon transport around the obstruction-loop.

---

# Hints

> [!note]- Hint 1
> For (a), think of $S^n$ as the level set $\{|x|^2 = 1\}$ of a smooth function $f(x) = |x|^2$ on $\mathbb{R}^{n+1}$. The gradient $\nabla f = 2x$ is normal to the level set. Use this to "convert" the ambient volume form into a top-form on $S^n$.

> [!note]- Hint 2
> For (a), specifically: define $\omega := \iota_\nu(dx^1\wedge\cdots\wedge dx^{n+1})$ on $\mathbb{R}^{n+1}$, where $\nu = \sum_i x^i\partial_i$ is the position vector. Restrict $\omega$ to $S^n$. Show it is nowhere zero by computing $\omega$ on an orthonormal basis of $T_pS^n$.

> [!note]- Hint 3
> For (b), parametrize $E$ as $\mathbb{R} \times (-1, 1) / \sim$ where $\sim$ identifies $(x, y) \sim (x + 1, -y)$. A 2-form on $E$ pulls back to a 2-form on $\mathbb{R} \times (-1, 1)$ that is *invariant* under the deck transformation $\tau(x, y) = (x + 1, -y)$. Compute $\tau^*(dx\wedge dy)$ and observe the sign.

> [!note]- Hint 4
> For (b), the contradiction: if $\omega = f(x, y)\,dx\wedge dy$ is a $\tau$-invariant 2-form on $\mathbb{R} \times (-1, 1)$ (the lift of a 2-form on $E$), then $\tau^*\omega = f(x+1, -y)(-dx\wedge dy) = \omega$. So $f(x+1, -y) = -f(x, y)$. Set $y = 0$ to derive a sign-flipping condition on $f$ along the line $y = 0$, forcing $f$ to vanish somewhere.

---

# Solution

The proof breaks into two parts, each a single substantive computation. **Part (a)** constructs a nowhere-vanishing $n$-form on $S^n$ by contracting the ambient volume form with the outward normal — the form is nowhere zero because the outward normal is everywhere transverse to $S^n$. **Part (b)** shows that any candidate $\tau$-invariant 2-form on the universal cover $\mathbb{R}\times(-1,1)$ must satisfy a functional equation $f(x+1, -y) = -f(x, y)$, which forces a sign-flipping condition along the line $y = 0$ and hence a zero somewhere — meaning no global volume form on the Möbius strip exists.

**Part (a): $S^n$ is orientable.**

**Step 1: Define the candidate form $\omega$ on $S^n$ via contraction.** On $\mathbb{R}^{n+1}$, take the standard volume form $\Omega := dx^1\wedge\cdots\wedge dx^{n+1}$ and the position vector field $\nu := \sum_{i=1}^{n+1}x^i\partial_i$. Define
$$\omega := \iota_\nu\Omega = \sum_{i=1}^{n+1}(-1)^{i-1}x^i\,dx^1\wedge\cdots\wedge\widehat{dx^i}\wedge\cdots\wedge dx^{n+1},$$
where $\iota_\nu$ is the interior product / contraction with $\nu$ and the hat indicates the omitted differential. This is a smooth $n$-form on $\mathbb{R}^{n+1}$, and its restriction to $S^n$ is denoted again $\omega$.

> [!note]- Derivation
> The interior product of a top-form $dx^1\wedge\cdots\wedge dx^{n+1}$ with a vector $\nu = \sum_i\nu^i\partial_i$ is the $n$-form
> $$\iota_\nu(dx^1\wedge\cdots\wedge dx^{n+1}) = \sum_{i=1}^{n+1}(-1)^{i-1}\nu^i\,dx^1\wedge\cdots\wedge\widehat{dx^i}\wedge\cdots\wedge dx^{n+1}.$$
> With $\nu = \sum_i x^i\partial_i$, $\nu^i = x^i$, giving the displayed formula. The form is smooth (polynomial coefficients) on $\mathbb{R}^{n+1}$; its restriction to $S^n$ is smooth.

**Step 2: Show $\omega|_{S^n}$ is nowhere zero.** At any $p \in S^n$, choose an orthonormal basis $(E_1, \ldots, E_n)$ of $T_pS^n$. Then $(\nu_p, E_1, \ldots, E_n)$ is a basis of $T_p\mathbb{R}^{n+1}$ (the normal $\nu_p = p$ is transverse to $S^n$), and orthonormal (since $|\nu_p| = |p| = 1$ on $S^n$ and $\nu_p$ is orthogonal to $T_pS^n$). So
$$\omega_p(E_1, \ldots, E_n) = (\iota_\nu\Omega)_p(E_1, \ldots, E_n) = \Omega_p(\nu_p, E_1, \ldots, E_n) = \pm 1 \neq 0,$$
the sign being $+1$ if $(\nu_p, E_1, \ldots, E_n)$ is positively oriented in $\mathbb{R}^{n+1}$ and $-1$ otherwise.

> [!note]- Derivation
> The interior product satisfies $(\iota_\nu\alpha)(v_1, \ldots, v_n) = \alpha(\nu, v_1, \ldots, v_n)$ for any $(n+1)$-form $\alpha$ and any vectors $v_1, \ldots, v_n$. Applied to $\Omega = dx^1\wedge\cdots\wedge dx^{n+1}$ at $p$:
> $$\omega_p(E_1, \ldots, E_n) = \Omega_p(\nu_p, E_1, \ldots, E_n) = \det[\nu_p\ |\ E_1\ |\ \cdots\ |\ E_n],$$
> the determinant of the matrix with columns $\nu_p, E_1, \ldots, E_n$. Since these are $n+1$ orthonormal vectors in $\mathbb{R}^{n+1}$, the determinant is $\pm 1$.
>
> Choosing the orthonormal basis $(E_1, \ldots, E_n)$ of $T_pS^n$ in a particular way determines the sign; both choices are possible, but for *any* choice the value is nonzero. So $\omega_p \neq 0$ at every $p$.

**Step 3: Conclude $S^n$ is orientable.** $\omega$ is a smooth nowhere-vanishing $n$-form on $S^n$. By [[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form|the orientability criterion]], $S^n$ is orientable.

**Part (b): The Möbius strip $E$ is not orientable.**

**Plan.** Lift $E$ to its universal cover $\widetilde E := \mathbb{R}\times(-1,1)$. A 2-form on $E$ corresponds to a $\tau$-invariant 2-form on $\widetilde E$, where $\tau(x, y) = (x + 1, -y)$ is the deck transformation. Compute the action of $\tau$ on $dx\wedge dy$: it gives $-dx\wedge dy$. So $\tau$-invariance of $\omega = f(x, y)\,dx\wedge dy$ forces $f(x+1, -y) = -f(x, y)$, a functional equation that forces $f$ to vanish somewhere.

**Step 1: Lift to the universal cover and compute $\tau^*(dx \wedge dy)$.** Let $q : \widetilde E = \mathbb{R}\times(-1,1) \to E$ be the quotient map. A smooth 2-form $\omega \in \Omega^2(E)$ pulls back to $q^*\omega \in \Omega^2(\widetilde E)$ which is $\tau$-invariant: $\tau^*(q^*\omega) = (q\circ\tau)^*\omega = q^*\omega$.

Compute: $\tau^*(dx\wedge dy) = d(\tau^*x)\wedge d(\tau^*y) = d(x+1)\wedge d(-y) = dx\wedge(-dy) = -dx\wedge dy$.

> [!note]- Derivation
> By the chain rule, $\tau^*(dx) = d(x\circ\tau) = d(x + 1) = dx$ and $\tau^*(dy) = d(y\circ\tau) = d(-y) = -dy$. Wedging,
> $$\tau^*(dx\wedge dy) = \tau^*(dx)\wedge\tau^*(dy) = dx\wedge(-dy) = -dx\wedge dy. \qquad\square$$
> This is the sign that creates the obstruction: pulling back $dx\wedge dy$ via $\tau$ reverses the form's sign.

**Step 2: Derive the functional equation for the lift.** Write $q^*\omega = f(x, y)\,dx\wedge dy$ for some smooth $f : \widetilde E \to \mathbb{R}$ (this is the general form of a 2-form on $\widetilde E$, which is a planar region). Then
$$\tau^*(q^*\omega) = \tau^*(f\,dx\wedge dy) = f(\tau(x, y))\cdot\tau^*(dx\wedge dy) = f(x+1, -y)\cdot(-dx\wedge dy).$$
Setting $\tau^*(q^*\omega) = q^*\omega$ (the $\tau$-invariance condition),
$$f(x+1, -y)\cdot(-dx\wedge dy) = f(x, y)\,dx\wedge dy,$$
hence $f(x+1, -y) = -f(x, y)$ for all $(x, y) \in \widetilde E$.

> [!note]- Derivation
> The pullback action of a smooth map on a 2-form $\omega = f\,dx\wedge dy$ is $\tau^*\omega = (f\circ\tau)\,\tau^*(dx\wedge dy)$, by the multiplicativity of the pullback over the product structure. Setting this equal to $\omega$ (the invariance condition) gives the functional equation.

**Step 3: The functional equation forces a zero.** Suppose, for contradiction, that $f$ is nowhere zero on $\widetilde E$. Then $f$ has constant sign on the connected $\widetilde E$ — without loss of generality $f > 0$ everywhere. But $f(x+1, 0) = -f(x, 0)$ from the functional equation at $y = 0$. The left side is positive (by the positivity assumption), the right side is negative — contradiction. Hence $f$ vanishes somewhere.

> [!note]- Derivation
> Set $y = 0$ in the functional equation: $f(x + 1, 0) = -f(x, 0)$ for all $x \in \mathbb{R}$. The line $\{y = 0\}$ in $\widetilde E$ is connected, and $f$ restricted to this line is a smooth real-valued function. If $f$ never vanished, $f|_{y=0}$ would have constant sign. But $f(x+1, 0)$ has the opposite sign from $f(x, 0)$, contradiction. So $f$ vanishes on the line $y = 0$ — in particular, there exists at least one $(x_0, 0)$ with $f(x_0, 0) = 0$.

**Step 4: Conclude $E$ is not orientable.** If $E$ had a smooth nowhere-vanishing 2-form $\omega$, its lift $q^*\omega = f\,dx\wedge dy$ would also be nowhere-vanishing (since $q$ is a local [[Def - Diffeomorphism|diffeomorphism]], $q^*\omega(p) = 0$ iff $\omega(q(p)) = 0$). But Step 3 shows $f$ must vanish somewhere on $\widetilde E$, contradicting nowhere-vanishing. By [[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form|the orientability criterion]], $E$ is not orientable.

> [!note]- Complete formal solution
> **Part (a).** Let $\nu = \sum_i x^i\partial_i \in \mathfrak{X}(\mathbb{R}^{n+1})$ be the position vector field, and let $\Omega = dx^1\wedge\cdots\wedge dx^{n+1}$ be the standard volume form on $\mathbb{R}^{n+1}$. Define
> $$\omega := \iota_\nu\Omega = \sum_{i=1}^{n+1}(-1)^{i-1}x^i\,dx^1\wedge\cdots\wedge\widehat{dx^i}\wedge\cdots\wedge dx^{n+1}.$$
> This is a smooth $n$-form on $\mathbb{R}^{n+1}$; we show its restriction $\omega|_{S^n}$ is nowhere-vanishing.
>
> At any $p \in S^n$, $\nu_p = p$ has $|\nu_p| = 1$ and is orthogonal to $T_pS^n$. Choose an orthonormal basis $(E_1, \ldots, E_n)$ of $T_pS^n$. Then $(\nu_p, E_1, \ldots, E_n)$ is an orthonormal basis of $T_p\mathbb{R}^{n+1}$, so
> $$\omega_p(E_1, \ldots, E_n) = \Omega_p(\nu_p, E_1, \ldots, E_n) = \pm 1 \neq 0,$$
> the sign being the orientation of $(\nu_p, E_1, \ldots, E_n)$ in $\mathbb{R}^{n+1}$. Hence $\omega|_{S^n}$ is nowhere zero. By the orientability criterion [[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form]], $S^n$ is orientable. The orientation $\omega$ determines is the **standard orientation** of $S^n$ (outward-normal first).
>
> **Part (b).** Let $q : \widetilde E = \mathbb{R}\times(-1, 1) \to E$ be the quotient map by the equivalence $(x, y) \sim (x + 1, -y)$, and $\tau(x, y) := (x + 1, -y)$ the deck transformation. Any smooth 2-form $\omega$ on $E$ pulls back to a $\tau$-invariant smooth 2-form $q^*\omega$ on $\widetilde E$.
>
> Write $q^*\omega = f(x, y)\,dx\wedge dy$ for some smooth $f : \widetilde E \to \mathbb{R}$. Compute
> $$\tau^*(dx\wedge dy) = dx\wedge d(-y) = -dx\wedge dy,$$
> using $\tau^*(dx) = dx$ and $\tau^*(dy) = -dy$. Hence
> $$\tau^*(q^*\omega) = f(x+1, -y)(-dx\wedge dy) \stackrel{!}{=} f(x, y)\,dx\wedge dy,$$
> so $f(x+1, -y) = -f(x, y)$ for all $(x, y) \in \widetilde E$.
>
> Set $y = 0$: $f(x+1, 0) = -f(x, 0)$, so $f$ restricted to the line $\{y = 0\}$ alternates sign in steps of $x = 1$. On the connected line $\{y = 0\}$, $f$ cannot have constant sign while satisfying this alternation, so $f$ vanishes at some $(x_0, 0) \in \widetilde E$. Since $q$ is a local [[Def - Diffeomorphism|diffeomorphism]], $\omega = q^{-1*}(q^*\omega)$ vanishes at $q(x_0, 0) \in E$.
>
> Therefore, $E$ admits no nowhere-vanishing smooth 2-form. By the orientability criterion, $E$ is not orientable. $\blacksquare$

> [!warning] Illegal but tempting: trying to prove non-orientability by computing transition Jacobians
> One might try to refute orientability of $E$ by finding two charts whose transition has negative Jacobian. This *would* show that *that particular atlas* is not oriented — but it might be possible to repair by negating coordinates. The correct refutation is global: show that *no* atlas can be oriented, which we do by exhibiting an obstruction to the existence of a global top-form (the universal-cover argument). The Möbius strip is non-orientable not because some specific transition has negative Jacobian, but because no choice of transition signs can be made coherent across the underlying $\mathbb{Z}/2$ holonomy.

---

# Key Takeaways

**Outward-normal contraction gives orientation for hypersurfaces.** Whenever a manifold $M$ embeds as a hypersurface in an oriented ambient manifold $N$ and has a nowhere-vanishing transverse vector field $\nu$ (a "normal"), the contraction $\iota_\nu\omega_N$ gives a nowhere-vanishing top-form on $M$ via [[Def - Orientation of a Vector Space|the outward-first convention]]. This is the universal recipe for orientations on submanifolds of Euclidean space and works for spheres, level sets of regular functions, surfaces in 3-space, and any embedded hypersurface. The construction is so reusable that it deserves to be memorized as a one-line technique: "to orient a hypersurface, contract the ambient volume form with the outward normal".

**The trigger condition for orientability via this technique is a nowhere-vanishing normal vector field.** A hypersurface has such a field iff its **normal bundle is trivial** — a topological condition. For embedded hypersurfaces of $\mathbb{R}^{n+1}$ this is automatic (the normal bundle is line-bundle, and the position vector or any other choice gives a nowhere-zero section). For more general ambient manifolds, the normal-bundle question is more subtle. The Möbius strip is *embedded* in $\mathbb{R}^3$ but has *non-trivial normal bundle* — exactly the obstruction to a nowhere-vanishing normal. Part (b) of this exercise shows this is the same obstruction as non-orientability.

**Non-orientability is a holonomy obstruction; the universal cover exposes it.** The Möbius strip's non-orientability is best seen by lifting to its universal cover and analyzing how the deck transformation acts on candidate volume forms. The deck transformation reverses orientation (its Jacobian determinant is $-1$), so a deck-invariant volume form must satisfy a sign-reversal functional equation, which forces a zero. This pattern is universal: every non-orientable manifold's non-orientability can be detected by an analysis of orientation-reversing deck transformations on its orientation double cover. For $\mathbb{RP}^{2k}$ the deck transformation is the antipodal map of $S^{2k}$, of degree $-1$; for the Klein bottle it is a glide reflection; the underlying mechanism is the same.

**Companion exercise.** [[Ex - The Tangent Bundle of the Circle is Trivial]] and [[Ex - The Möbius Bundle is Nontrivial]] in [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]] are the bundle-theoretic versions of this exercise: the question "is $TM$ trivial as a vector bundle?" is closely related to "is $M$ orientable?" but they are not the same — $S^2$ has trivial *orientation* line bundle but nontrivial $TM$ (parallelizability is strictly stronger than orientability). The bundle-theoretic / topological view brings these subtle distinctions into focus.
