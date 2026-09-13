---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map"
  - "Def - Discrete Group and Properly Discontinuous Action"
  - "Def - Free, Transitive, Effective, and Proper Group Actions"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let the group $(\mathbb{Z}, +)$, viewed as a $0$-dimensional Lie group with the discrete topology, act on the real line $\mathbb{R}$ by translation,
$$\mathbb{Z} \times \mathbb{R} \longrightarrow \mathbb{R}, \qquad (k, t) \longmapsto k \cdot t := k + t.$$

Prove the two claims that together identify the quotient of this action with the circle.

- **(A) Proper discontinuity.** The action is properly discontinuous, with the two conditions witnessed by the explicit neighbourhoods of Bär: condition (i) by $U := \left(t - \tfrac{1}{2}, t + \tfrac{1}{2}\right)$, and condition (ii), for points $s, t$ in different orbits (that is, with $t - s \notin \mathbb{Z}$), by $U := \left(s - \tfrac{\epsilon}{2}, s + \tfrac{\epsilon}{2}\right)$ and $V := \left(t - \tfrac{\epsilon}{2}, t + \tfrac{\epsilon}{2}\right)$ where $\epsilon := \min_{k \in \mathbb{Z}} |t - (s + k)|$.

- **(B) The quotient is the circle.** Writing $S^1 := \{(x, y) \in \mathbb{R}^2 : x^2 + y^2 = 1\}$ for the unit circle, the map
$$f : \mathbb{R} \longrightarrow S^1, \qquad f(t) := (\cos 2\pi t, \, \sin 2\pi t),$$
descends through the quotient projection $\pi : \mathbb{R} \to \mathbb{Z}\backslash\mathbb{R}$ to a unique smooth map $\tilde{f} : \mathbb{Z}\backslash\mathbb{R} \to S^1$ with $\tilde{f} \circ \pi = f$, and this $\tilde{f}$ is a **diffeomorphism**. In particular the argument uses only that $\tilde{f}$ is a bijective local diffeomorphism; the compactness of $\mathbb{Z}\backslash\mathbb{R}$ is not invoked.

This is Bär's Example 1.5.24. The source states part (B) in a single sentence — "$\tilde{f}$ is bijective and $d\tilde{f} \neq 0$, hence a diffeomorphism"; the task here is to supply every step of that reasoning, including the passage from "bijective local diffeomorphism" to "diffeomorphism", which the source leaves implicit.

**Recall:**

The objects in play are the properly-discontinuous condition, the smooth-covering-map structure on the quotient together with its universal property, and the notion of a local diffeomorphism.

![[Def - Discrete Group and Properly Discontinuous Action#The Definition]]

For the action of a discrete group $G$ on a manifold $M$, written $(g, p) \mapsto g \cdot p$, proper discontinuity is the conjunction of the two conditions of [[Def - Discrete Group and Properly Discontinuous Action|Bär]]:

- **(i)** for every $p \in M$ there is a neighbourhood $U$ of $p$ with $g \cdot U \cap U \neq \emptyset \Rightarrow g = e$;
- **(ii)** for every pair $p, q \in M$ lying in different orbits ($G \cdot p \neq G \cdot q$) there are neighbourhoods $U \ni p$ and $V \ni q$ with $g \cdot U \cap V = \emptyset$ for all $g \in G$.

![[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map#Statement]]

The single result this exercise routes through is the quotient theorem, restated here in the form used below: **if a discrete group $\Gamma$ acts smoothly and properly discontinuously on a manifold $M$, then the orbit space $\Gamma\backslash M$ carries a unique smooth structure for which the projection $\pi : M \to \Gamma\backslash M$ is a smooth covering map — in particular a surjective local diffeomorphism — and $\pi$ has the universal property that every smooth map $h : M \to N$ constant along the orbits of $\Gamma$ factors as $h = \bar{h} \circ \pi$ for a unique smooth $\bar{h} : \Gamma\backslash M \to N$.** See [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the quotient theorem]] for its proof. This exercise supplies the hypothesis of that theorem in part (A) and consumes its conclusion in part (B).

A **local diffeomorphism** is a smooth map $g : X \to Y$ of manifolds such that every point $x \in X$ has an open neighbourhood $W$ with $g(W)$ open in $Y$ and $g|_W : W \to g(W)$ a diffeomorphism. By the [[Thm - The Inverse Function Theorem|inverse function theorem]] — *if $g$ is smooth and the differential $d_x g : T_x X \to T_{g(x)} Y$ is a linear isomorphism at a point $x$, then $g$ restricts to a diffeomorphism between an open neighbourhood of $x$ and an open neighbourhood of $g(x)$* — a smooth map whose differential is an isomorphism at every point is a local diffeomorphism.

---

# Convergent Strategy

**Problem class.** This is a *quotient-identification* problem of the standard two-move shape: first certify that an explicit group action satisfies the hypothesis of a manifold-producing theorem (here, proper discontinuity), then identify the abstract quotient it produces with a concrete manifold one already knows (here, $S^1$) by exhibiting an explicit diffeomorphism. The abstract object $\mathbb{Z}\backslash\mathbb{R}$ is defined by a universal property and has no coordinates of its own; the entire content of "it is the circle" is the construction of a specific diffeomorphism to a space with coordinates.

**Assumption pattern.** Proper discontinuity is verified by *choosing radii that separate the relevant translates*. Both conditions reduce to the elementary geometric fact that two open intervals of prescribed half-widths, centred at points a known distance apart, are disjoint precisely when that distance exceeds the sum of the half-widths. Condition (i) uses intervals of length $1$ and the fact that distinct integer translates of a length-$1$ interval, centred a nonzero integer apart, cannot overlap; condition (ii) uses the *distance from a non-integer real to the nearest integer*, which is strictly positive, as the radius.

**Theorem routing.** The route is: verify (A) directly, feed it as the hypothesis of [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the quotient theorem]], and use two of that theorem's conclusions — *the universal property* to manufacture the smooth map $\tilde{f}$, and *the covering-map (local-diffeomorphism) property of $\pi$* to transport the non-vanishing of $df$ down to non-vanishing of $d\tilde{f}$. Then invoke the [[Thm - The Inverse Function Theorem|inverse function theorem]] to upgrade "$d\tilde{f}$ is an isomorphism everywhere" to "$\tilde{f}$ is a local diffeomorphism", and finish with the elementary lemma that a *bijective* local diffeomorphism is a diffeomorphism.

**Key decision point.** The one genuinely non-obvious move is how to prove $d\tilde{f} \neq 0$ when $\tilde{f}$ is a map out of a space with no explicit coordinates. The differential of $f$ is a direct computation, $f'(t) = 2\pi(-\sin 2\pi t, \cos 2\pi t) \neq 0$; the differential of $\tilde{f}$ is *not* directly computable, because $\mathbb{Z}\backslash\mathbb{R}$ carries no chosen chart. The device is the factorisation $f = \tilde{f} \circ \pi$: since $\pi$ is a local diffeomorphism its differential is an isomorphism, so $d_t f = d_{\pi(t)}\tilde{f} \circ d_t \pi$ forces $d_{\pi(t)}\tilde{f}$ to be nonzero. This is the recurring idea that *a covering projection lets one pull computations up to the total space, where coordinates exist*.

---

# Legal Operations Used

This solution deploys the following legal operations from the topic page's Legal Operations (referred to descriptively here; the orchestrator will reconcile numbering once the topic page is assembled).

1. **Certify a group action satisfies a manifold-producing hypothesis by separating translates with explicit radii.** For each of the two conditions of proper discontinuity, exhibit an explicit neighbourhood and compute, from the metric on $\mathbb{R}$, that the required translates are disjoint.

2. **Feed a verified hypothesis into the quotient theorem to obtain a smooth manifold and a covering projection.** Having established (A), invoke [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the quotient theorem]] to endow $\mathbb{Z}\backslash\mathbb{R}$ with its smooth structure and to make $\pi$ a smooth covering map.

3. **Descend a map constant along orbits through the quotient by the universal property.** The map $f$ is constant on $\mathbb{Z}$-orbits, so it factors uniquely and smoothly through $\pi$, producing $\tilde{f}$.

4. **Transport a differential across a covering projection.** Use $d_t f = d_{\pi(t)}\tilde{f} \circ d_t \pi$ together with the invertibility of $d_t \pi$ (operation 2) to move the computed non-vanishing of $df$ down onto $d\tilde{f}$.

5. **Upgrade an everywhere-invertible differential to a local diffeomorphism by the inverse function theorem.** From $d\tilde{f}$ an isomorphism at every point, conclude via the [[Thm - The Inverse Function Theorem|inverse function theorem]] that $\tilde{f}$ is a local diffeomorphism.

6. **Upgrade a bijective local diffeomorphism to a diffeomorphism by a locality-of-smoothness argument.** Bijectivity makes the set-theoretic inverse well defined; locality of smoothness makes it smooth, since near each point it coincides with the smooth inverse of a local restriction.

---

# Hints

> [!note]- Hint 1
> Split the problem cleanly. Part (A) is pure point-set computation on $\mathbb{R}$: it never mentions $S^1$. Two open intervals of half-widths $r_1, r_2$ centred at points $c_1, c_2$ meet if and only if $|c_1 - c_2| < r_1 + r_2$. Apply this once for condition (i) (translates of a single length-$1$ interval) and once for condition (ii) (a separating radius $\epsilon$). Do not try to do anything geometric with the circle yet.

> [!note]- Hint 2
> For condition (i) with $U = \left(t - \tfrac12, t + \tfrac12\right)$, the translate $k \cdot U$ is the interval of the same length centred at $t + k$. Its centre is at distance $|k|$ from the centre of $U$. When can two length-$1$ intervals whose centres are an *integer* distance apart overlap?

> [!note]- Hint 3
> For part (B), you cannot differentiate $\tilde{f}$ directly because $\mathbb{Z}\backslash\mathbb{R}$ has no chosen chart. Instead use the relation $f = \tilde{f} \circ \pi$ and the fact that $\pi$ is a *local diffeomorphism* (this is exactly what the quotient theorem gives you). The chain rule then reads $d_t f = d_{\pi(t)}\tilde{f} \circ d_t \pi$ with $d_t\pi$ invertible. Compute $d_t f$ by hand and read off $d_{\pi(t)}\tilde{f}$.

> [!note]- Hint 4
> Once $d\tilde{f}$ is an isomorphism at every point, the inverse function theorem makes $\tilde{f}$ a local diffeomorphism, and you already know $\tilde{f}$ is a bijection. To finish, show the inverse $\tilde{f}^{-1}$ is smooth: near any point $y = \tilde{f}(x)$ there is an open $W \ni x$ on which $\tilde{f}$ restricts to a diffeomorphism onto the open set $\tilde{f}(W)$; on $\tilde{f}(W)$ the global inverse $\tilde{f}^{-1}$ agrees with $(\tilde{f}|_W)^{-1}$. Smoothness is local, so this is enough — and note nowhere did you use compactness of the quotient.

---

# Solution

The plan is in two independent halves. In part (A) we verify proper discontinuity by the two interval computations, using at each step the elementary criterion that intervals of half-widths $r_1, r_2$ centred a distance $d$ apart are disjoint precisely when $d \geq r_1 + r_2$. In part (B) we obtain $\mathbb{Z}\backslash\mathbb{R}$ as a smooth manifold and $\pi$ as a covering map from the quotient theorem, descend $f$ to a smooth bijection $\tilde{f}$ through the universal property, prove $d\tilde{f} \neq 0$ by transporting the hand-computed differential of $f$ across the local diffeomorphism $\pi$, and finally upgrade the bijective local diffeomorphism $\tilde{f}$ to a diffeomorphism by a locality-of-smoothness argument that never touches compactness.

**Step 0: The map is a smooth action of the discrete group $\mathbb{Z}$.**

Before proper discontinuity is even a meaningful question we record that translation is a genuine smooth left action.

> [!note]- Derivation
> Write $\theta(k, t) = k + t$. The two axioms of a left action hold: $\theta(0, t) = 0 + t = t$ for every $t$, and for $k, l \in \mathbb{Z}$,
> $$\theta\big(k, \theta(l, t)\big) = k + (l + t) = (k + l) + t = \theta(k + l, t) \qquad \text{(associativity of addition in } \mathbb{R}\text{).}$$
> Since $\mathbb{Z}$ carries the discrete topology, it is a $0$-dimensional Lie group, and for each fixed $k$ the map $t \mapsto k + t$ is smooth on $\mathbb{R}$; hence $\theta$ is a smooth action in the sense of [[Def - Smooth Action of a Lie Group|a smooth Lie group action]]. Each orbit is the coset $\mathbb{Z} \cdot t = \{t + k : k \in \mathbb{Z}\} = t + \mathbb{Z}$, and two reals $s, t$ lie in the same orbit if and only if $t - s \in \mathbb{Z}$.

**Step 1 (Part A, condition (i)): Distinct integer translates of a length-$1$ interval are disjoint.**

For $t \in \mathbb{R}$ the neighbourhood $U := \left(t - \tfrac12, t + \tfrac12\right)$ satisfies $k \cdot U \cap U \neq \emptyset \Rightarrow k = 0$.

> [!note]- Derivation
> Fix $t \in \mathbb{R}$ and set $U := \left(t - \tfrac12, t + \tfrac12\right)$, an open interval of length $1$ centred at $t$. For $k \in \mathbb{Z}$,
> $$k \cdot U = k + U = \left(t + k - \tfrac12, \; t + k + \tfrac12\right) \qquad \text{(the action translates every point of } U \text{ by } k\text{),}$$
> an interval of length $1$ centred at $t + k$. The centres of $U$ and $k \cdot U$ are $t$ and $t + k$, at distance $|k|$. Two open intervals of half-widths $\tfrac12$ and $\tfrac12$ centred a distance $|k|$ apart intersect if and only if
> $$|k| < \tfrac12 + \tfrac12 = 1 \qquad \text{(the disjointness criterion for intervals).}$$
> Because $k$ is an integer, $|k| < 1$ forces $k = 0$. Contrapositively, if $k \cdot U \cap U \neq \emptyset$ then $|k| < 1$, hence $k = 0$. This is exactly condition (i) with the identity element $e = 0$ of $\mathbb{Z}$.

**Step 2 (Part A, condition (ii)): The nearest-integer distance separates points in different orbits.**

For $s, t$ in different orbits ($t - s \notin \mathbb{Z}$) put $\epsilon := \min_{k \in \mathbb{Z}} |t - (s + k)|$. Then $\epsilon > 0$, and $U := \left(s - \tfrac{\epsilon}{2}, s + \tfrac{\epsilon}{2}\right)$, $V := \left(t - \tfrac{\epsilon}{2}, t + \tfrac{\epsilon}{2}\right)$ satisfy $k \cdot U \cap V = \emptyset$ for all $k \in \mathbb{Z}$.

> [!note]- Derivation
> Suppose $s, t \in \mathbb{R}$ lie in different orbits, that is $t - s \notin \mathbb{Z}$ (Step 0). Consider
> $$\epsilon := \min_{k \in \mathbb{Z}} |t - (s + k)| = \min_{k \in \mathbb{Z}} |(t - s) - k|,$$
> the distance from the real number $t - s$ to the nearest integer.
>
> *The minimum exists and is positive.* Write $x := t - s$. The function $k \mapsto |x - k|$ on $\mathbb{Z}$ tends to $+\infty$ as $|k| \to \infty$, so its infimum over $\mathbb{Z}$ is attained at some integer $k_0$ (only finitely many $k$ satisfy $|x - k| \leq |x| + 1$, and the minimum over that finite set is the global minimum). Thus $\epsilon = |x - k_0|$ is attained. It is strictly positive: if $\epsilon = 0$ then $x = k_0 \in \mathbb{Z}$, contradicting $x = t - s \notin \mathbb{Z}$. Hence $\epsilon > 0$, and by definition of the minimum
> $$|t - (s + k)| \geq \epsilon \qquad \text{for every } k \in \mathbb{Z}. \tag{$\ast$}$$
>
> *The neighbourhoods separate all translates.* Set $U := \left(s - \tfrac{\epsilon}{2}, s + \tfrac{\epsilon}{2}\right)$ and $V := \left(t - \tfrac{\epsilon}{2}, t + \tfrac{\epsilon}{2}\right)$, open intervals of length $\epsilon$ centred at $s$ and $t$. For $k \in \mathbb{Z}$,
> $$k \cdot U = \left(s + k - \tfrac{\epsilon}{2}, \; s + k + \tfrac{\epsilon}{2}\right) \qquad \text{(translation by } k\text{),}$$
> an interval of length $\epsilon$ centred at $s + k$. The centres of $k \cdot U$ and $V$ are $s + k$ and $t$, at distance $|t - (s + k)| \geq \epsilon$ by $(\ast)$. Two open intervals of half-widths $\tfrac{\epsilon}{2}$ and $\tfrac{\epsilon}{2}$ centred a distance $\geq \epsilon = \tfrac{\epsilon}{2} + \tfrac{\epsilon}{2}$ apart are disjoint (the disjointness criterion, in the boundary case: the centre distance is at least the sum of the half-widths, so the open intervals do not meet). Therefore
> $$k \cdot U \cap V = \emptyset \qquad \text{for every } k \in \mathbb{Z},$$
> which is condition (ii).

Steps 1 and 2 together establish part (A): the translation action of $\mathbb{Z}$ on $\mathbb{R}$ is properly discontinuous.

**Step 3 (Part B): The quotient is a smooth manifold and $f$ descends to a smooth bijection.**

By part (A), the quotient theorem endows $\mathbb{Z}\backslash\mathbb{R}$ with a smooth structure making $\pi : \mathbb{R} \to \mathbb{Z}\backslash\mathbb{R}$ a smooth covering map, and the universal property produces a unique smooth $\tilde{f} : \mathbb{Z}\backslash\mathbb{R} \to S^1$ with $\tilde{f} \circ \pi = f$; this $\tilde{f}$ is a bijection.

> [!note]- Derivation
> By part (A) the action is smooth (Step 0) and properly discontinuous (Steps 1–2), so the hypotheses of [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the quotient theorem]] are met. It gives $\mathbb{Z}\backslash\mathbb{R}$ a unique smooth structure for which $\pi$ is a smooth covering map — in particular a surjective local diffeomorphism — and states that any smooth map constant along the $\mathbb{Z}$-orbits factors uniquely and smoothly through $\pi$.
>
> *The map $f$ is smooth and orbit-constant.* Its components $t \mapsto \cos 2\pi t$ and $t \mapsto \sin 2\pi t$ are smooth, and its image lies in $S^1$ since $\cos^2 2\pi t + \sin^2 2\pi t = 1$; so $f : \mathbb{R} \to S^1$ is smooth. It is constant along orbits because $\cos$ and $\sin$ have period $2\pi$:
> $$f(k + t) = \big(\cos 2\pi(k + t), \, \sin 2\pi(k + t)\big) = \big(\cos(2\pi t + 2\pi k), \, \sin(2\pi t + 2\pi k)\big) = (\cos 2\pi t, \, \sin 2\pi t) = f(t)$$
> for every $k \in \mathbb{Z}$ (since $2\pi k$ is an integer multiple of the period $2\pi$).
>
> *Descent.* By the universal property there is a unique smooth map
> $$\tilde{f} : \mathbb{Z}\backslash\mathbb{R} \longrightarrow S^1 \qquad \text{with} \qquad \tilde{f} \circ \pi = f.$$
>
> *$\tilde{f}$ is surjective.* Every point of $S^1$ has the form $(\cos \varphi, \sin \varphi)$ for some $\varphi \in \mathbb{R}$; taking $t = \varphi/(2\pi)$ gives $f(t) = (\cos \varphi, \sin \varphi)$, so $f$ is surjective. Since $f = \tilde{f} \circ \pi$ is surjective, $\tilde{f}$ is surjective (the last map of a surjective composite is surjective).
>
> *$\tilde{f}$ is injective.* Because $\pi$ is surjective, every element of $\mathbb{Z}\backslash\mathbb{R}$ is $\pi(t)$ for some $t$. Suppose $\tilde{f}(\pi(s)) = \tilde{f}(\pi(t))$; then $f(s) = f(t)$ (as $\tilde f\circ\pi = f$), that is
> $$\cos 2\pi s = \cos 2\pi t \quad \text{and} \quad \sin 2\pi s = \sin 2\pi t.$$
> Write $a := 2\pi t$ and $b := 2\pi s$. The angle-subtraction formula gives
> $$\cos(a - b) = \cos a \cos b + \sin a \sin b = \cos^2 b + \sin^2 b = 1 \qquad \text{(substituting } \cos a = \cos b \text{, } \sin a = \sin b \text{, then the Pythagorean identity),}$$
> and $\cos\vartheta = 1$ holds for a real $\vartheta$ if and only if $\vartheta \in 2\pi\mathbb{Z}$ (the zeros of $1 - \cos$ are exactly the integer multiples of $2\pi$). Hence $a - b = 2\pi(t - s) = 2\pi m$ for some $m \in \mathbb{Z}$, whence $t - s = m \in \mathbb{Z}$. By Step 0 this means $s$ and $t$ lie in the same orbit, so $\pi(s) = \pi(t)$. Thus $\tilde{f}$ is injective.
>
> Hence $\tilde{f}$ is a smooth bijection.

**Step 4 (Part B): The differential of $\tilde{f}$ is nowhere zero.**

Transporting the hand-computed differential of $f$ across the local diffeomorphism $\pi$ shows $d_{\pi(t)}\tilde{f} \neq 0$ for every $t$, and since $\dim(\mathbb{Z}\backslash\mathbb{R}) = \dim S^1 = 1$ this differential is a linear isomorphism at every point.

> [!note]- Derivation
> *Compute $d_t f$.* Differentiating componentwise,
> $$f'(t) = \frac{d}{dt}\big(\cos 2\pi t, \, \sin 2\pi t\big) = \big(-2\pi \sin 2\pi t, \; 2\pi \cos 2\pi t\big) \qquad \text{(chain rule on each component).}$$
> Its Euclidean norm is
> $$|f'(t)| = 2\pi\sqrt{\sin^2 2\pi t + \cos^2 2\pi t} = 2\pi \neq 0 \qquad \text{(Pythagorean identity),}$$
> so $f'(t) \neq 0$ for every $t$. As a linear map $d_t f : T_t\mathbb{R} \cong \mathbb{R} \to T_{f(t)}S^1$ out of a one-dimensional space, $d_t f$ sends the basis vector $\partial_t$ to the nonzero vector $f'(t)$, hence is injective — a linear isomorphism onto its image, and in particular nonzero.
>
> *Transport across $\pi$.* Differentiating $f = \tilde{f} \circ \pi$ at $t$ by the chain rule,
> $$d_t f = d_{\pi(t)}\tilde{f} \circ d_t \pi \qquad \text{(chain rule).} \tag{$\dagger$}$$
> The projection $\pi$ is a local diffeomorphism (Step 3), so its differential $d_t \pi : T_t \mathbb{R} \to T_{\pi(t)}(\mathbb{Z}\backslash\mathbb{R})$ is a linear isomorphism. If $d_{\pi(t)}\tilde{f}$ were the zero map, then by $(\dagger)$ the composite $d_t f$ would be zero, contradicting $d_t f \neq 0$. Therefore
> $$d_{\pi(t)}\tilde{f} \neq 0 \qquad \text{for every } t.$$
>
> *It is an isomorphism.* The manifold $\mathbb{Z}\backslash\mathbb{R}$ is one-dimensional (it is smoothly covered by the one-dimensional $\mathbb{R}$, and a covering map is a local diffeomorphism, hence preserves dimension), and $S^1$ is one-dimensional. A nonzero linear map between one-dimensional vector spaces is an isomorphism. Hence $d_{\pi(t)}\tilde{f}$ is a linear isomorphism at every point of $\mathbb{Z}\backslash\mathbb{R}$ (every such point is some $\pi(t)$ by surjectivity of $\pi$).

**Step 5 (Part B): A bijective local diffeomorphism is a diffeomorphism.**

Since $d\tilde{f}$ is an isomorphism everywhere, the inverse function theorem makes $\tilde{f}$ a local diffeomorphism; combined with the bijectivity from Step 3, its inverse is smooth, so $\tilde{f}$ is a diffeomorphism.

> [!note]- Derivation
> By Step 4 the differential of $\tilde{f}$ is a linear isomorphism at every point. By the [[Thm - The Inverse Function Theorem|inverse function theorem]] — *a smooth map whose differential at $x$ is invertible restricts to a diffeomorphism of an open neighbourhood of $x$ onto an open neighbourhood of its image* — the map $\tilde{f}$ is a **local diffeomorphism**: every $x \in \mathbb{Z}\backslash\mathbb{R}$ has an open neighbourhood $W$ with $\tilde{f}(W)$ open in $S^1$ and $\tilde{f}|_W : W \to \tilde{f}(W)$ a diffeomorphism.
>
> By Step 3, $\tilde{f}$ is a bijection, so the set-theoretic inverse $\tilde{f}^{-1} : S^1 \to \mathbb{Z}\backslash\mathbb{R}$ is well defined. It remains to show $\tilde{f}^{-1}$ is smooth, and smoothness is a local property, so it suffices to check smoothness near each point $y \in S^1$. Let $x := \tilde{f}^{-1}(y)$ and take an open $W \ni x$ as above, so $\tilde{f}|_W : W \to \tilde{f}(W)$ is a diffeomorphism onto the open set $\tilde{f}(W) \ni y$. On $\tilde{f}(W)$ the global inverse and the local inverse coincide:
> $$\tilde{f}^{-1}\big|_{\tilde{f}(W)} = \big(\tilde{f}|_W\big)^{-1} \qquad \text{(both send } \tilde f(w)\mapsto w \text{ for } w\in W \text{, using injectivity of the bijection } \tilde f\text{).}$$
> The right-hand side is smooth, being the inverse of a diffeomorphism; hence $\tilde{f}^{-1}$ is smooth on the open neighbourhood $\tilde{f}(W)$ of $y$. As $y \in S^1$ was arbitrary, $\tilde{f}^{-1}$ is smooth on all of $S^1$.
>
> Therefore $\tilde{f}$ is a smooth bijection with smooth inverse — a diffeomorphism. Observe that the only facts used were bijectivity and the local-diffeomorphism property; the compactness of $\mathbb{Z}\backslash\mathbb{R}$ played no role. (The familiar shortcut "a continuous bijection from a compact space to a Hausdorff space is a homeomorphism" would deliver only a homeomorphism, not the diffeomorphism required, and is therefore both unnecessary and insufficient here.)

> [!note]- Complete formal solution
> **Claim.** The translation action of $(\mathbb{Z}, +)$ on $\mathbb{R}$, $(k, t) \mapsto k + t$, is properly discontinuous, and the map $f(t) = (\cos 2\pi t, \sin 2\pi t)$ descends to a diffeomorphism $\tilde{f} : \mathbb{Z}\backslash\mathbb{R} \xrightarrow{\ \sim\ } S^1$.
>
> **(A) Proper discontinuity.** Translation is a smooth left action of the $0$-dimensional Lie group $\mathbb{Z}$, with orbits $t + \mathbb{Z}$; $s, t$ share an orbit iff $t - s \in \mathbb{Z}$.
>
> *(i)* For $t \in \mathbb{R}$ let $U = \left(t - \tfrac12, t + \tfrac12\right)$. Then $k \cdot U = \left(t + k - \tfrac12, t + k + \tfrac12\right)$ has centre $t + k$, at distance $|k|$ from the centre of $U$; two length-$1$ intervals meet iff $|k| < 1$, and for $k \in \mathbb{Z}$ this forces $k = 0$. So $k \cdot U \cap U \neq \emptyset \Rightarrow k = 0$.
>
> *(ii)* For $s, t$ with $t - s \notin \mathbb{Z}$ let $\epsilon = \min_{k \in \mathbb{Z}} |t - (s + k)|$, the distance from $t - s$ to the nearest integer; the minimum is attained (the map $k \mapsto |t - s - k|$ is proper on $\mathbb{Z}$) and positive (else $t - s \in \mathbb{Z}$). With $U = \left(s - \tfrac{\epsilon}{2}, s + \tfrac{\epsilon}{2}\right)$, $V = \left(t - \tfrac{\epsilon}{2}, t + \tfrac{\epsilon}{2}\right)$, the interval $k \cdot U$ has centre $s + k$ at distance $|t - (s + k)| \geq \epsilon$ from the centre $t$ of $V$; two intervals of half-width $\tfrac{\epsilon}{2}$ whose centres are $\geq \epsilon$ apart are disjoint, so $k \cdot U \cap V = \emptyset$ for all $k$. Hence the action is properly discontinuous.
>
> **(B) The quotient is $S^1$.** By (A) and [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the quotient theorem]], $\mathbb{Z}\backslash\mathbb{R}$ is a smooth $1$-manifold, $\pi : \mathbb{R} \to \mathbb{Z}\backslash\mathbb{R}$ is a smooth covering map (a surjective local diffeomorphism), and its universal property applies. The map $f : \mathbb{R} \to S^1$ is smooth (its image satisfies $\cos^2 + \sin^2 = 1$) and orbit-constant ($f(k + t) = f(t)$ by periodicity), so it descends to a unique smooth $\tilde{f} : \mathbb{Z}\backslash\mathbb{R} \to S^1$ with $\tilde{f} \circ \pi = f$. It is surjective ($f$ is) and injective ($f(s) = f(t) \Rightarrow 2\pi(t - s) \in 2\pi\mathbb{Z} \Rightarrow t - s \in \mathbb{Z} \Rightarrow \pi(s) = \pi(t)$), hence bijective.
>
> Differentiating $f$: $f'(t) = 2\pi(-\sin 2\pi t, \cos 2\pi t)$ has norm $2\pi \neq 0$, so $d_t f$ is injective. From $f = \tilde{f} \circ \pi$, $d_t f = d_{\pi(t)}\tilde{f} \circ d_t\pi$ with $d_t\pi$ invertible (local diffeomorphism), so $d_{\pi(t)}\tilde{f} \neq 0$; between $1$-dimensional tangent spaces this makes it a linear isomorphism at every point. By the [[Thm - The Inverse Function Theorem|inverse function theorem]], $\tilde{f}$ is a local diffeomorphism. A bijective local diffeomorphism has a smooth inverse — near each $y = \tilde{f}(x)$ the global inverse agrees with the inverse of a local diffeomorphic restriction $\tilde{f}|_W$, hence is smooth, and smoothness is local — so $\tilde{f}$ is a diffeomorphism. No compactness of the quotient was used. $\blacksquare$

---

# Key Takeaways

**Proper discontinuity is verified by choosing radii that separate the relevant translates, and the correct radius is a distance the hypotheses guarantee to be positive.** Both conditions of proper discontinuity are, at bottom, the single elementary statement that two open balls (here intervals) are disjoint once their centres are at least the sum of their radii apart. The art is only in *which* distance to use as the radius. For condition (i) the discreteness of the group does the work: distinct group elements move a point by at least the minimal orbit gap (here, $1$), so a ball of radius half that gap cannot meet its own nonzero translates. For condition (ii) the *separation of orbits* is the input: two points in different orbits are a positive distance from each other's entire orbit, and that distance — here the nearest-integer distance $\epsilon$, positive exactly because $t - s \notin \mathbb{Z}$ — is the radius that works. The recurring diagnostic: when asked to verify proper discontinuity of a discrete action, look for the quantity the hypotheses force to be strictly positive (a minimal displacement, an orbit-to-orbit distance) and build the neighbourhoods with half that quantity as radius. The same template certifies the deck action of $\mathbb{Z}^n$ on $\mathbb{R}^n$ that produces the torus, and it is exactly the computation that *fails* for the dense $\mathbb{Q}$-action of the companion exercise, [[Ex - The Rationals Acting on R are Not Properly Discontinuous]], where no such positive separation exists.

**To differentiate a map out of a coordinate-free quotient, pull the computation up to the covering space through the projection's invertible differential.** The abstract quotient $\mathbb{Z}\backslash\mathbb{R}$ has no chosen chart, so $d\tilde{f}$ cannot be written down directly; but the covering projection $\pi$ is a local diffeomorphism, and the factorisation $f = \tilde{f} \circ \pi$ turns the chain rule $d_t f = d_{\pi(t)}\tilde{f} \circ d_t\pi$ into a device that reads properties of $\tilde{f}$ off the concrete, computable map $f$. The trigger condition is precisely this configuration — a map defined on a quotient (or any base of a covering or submersion) that factors through a projection whose differential is known to be invertible. The transferable principle is that *a local diffeomorphism is transparent to first-order information*: injectivity, surjectivity, rank, and non-vanishing of a differential all pass across it in whichever direction the factorisation allows. This is the same manoeuvre used to compute the differential of the induced diffeomorphism $\mathbb{CP}^1 \to S^2$ in [[Thm - CP^1 is Diffeomorphic to S^2 via the Hopf Map|the Hopf identification]], and it is the reason quotient constructions in gauge theory remain computable despite having no canonical coordinates.

**"Bijective local diffeomorphism $\Rightarrow$ diffeomorphism" is the right finishing move, and it is strictly stronger and cheaper than the compactness shortcut.** Once a smooth map is known to be a bijection whose differential is everywhere invertible, it is a diffeomorphism: the inverse is smooth because, near each point, it coincides with the smooth inverse of a local diffeomorphic restriction, and smoothness is a local property. This argument uses no global topology of the domain or codomain — in particular no compactness, no connectedness, no Hausdorffness beyond what makes the objects manifolds. It is worth contrasting with the point-set reflex "continuous bijection from compact to Hausdorff is a homeomorphism": that statement is about homeomorphisms, not diffeomorphisms, so even when its hypotheses hold it delivers the wrong conclusion for a smooth-category problem. The lesson for spaced practice is to keep the smooth-category upgrade lemma separate from its topological cousin, and to reach for it whenever a quotient- or covering-identification has already produced a smooth bijection with invertible differential; the diffeomorphism then costs nothing further. This is why the exercise can, and does, avoid ever asking whether $\mathbb{Z}\backslash\mathbb{R}$ is compact.
