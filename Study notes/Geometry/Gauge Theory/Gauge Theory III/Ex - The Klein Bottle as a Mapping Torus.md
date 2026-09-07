---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle"
  - "Def - Sphere Bundles and Mapping Tori"
  - "Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\phi \colon S^1 \to S^1$ be the reflection $\phi(z) = \bar z$ (complex conjugation on the unit circle $S^1 = \{z \in \mathbb{C} : |z| = 1\}$), a diffeomorphism of $S^1$. Form its **mapping torus**
$$K := E_\phi = \mathbb{Z} \backslash (\mathbb{R} \times S^1), \qquad \pi \colon K \to \mathbb{Z} \backslash \mathbb{R} \cong S^1,$$
where $\mathbb{Z}$ acts on $\mathbb{R} \times S^1$ by $k \cdot (t, z) = (t + k, \phi^k(z))$ and $\pi$ is induced by the first projection. Prove:

1. $(K, \pi, S^1)$ is a fibre bundle with typical fibre $S^1$ — a **circle bundle over the circle**.
2. Its total space $K$ is **non-orientable**.
3. Consequently the bundle is **nontrivial**: it is not isomorphic to the product bundle $S^1 \times S^1 \to S^1$, because the total space of that product bundle is the orientable torus $S^1 \times S^1$, whereas $K$ (the Klein bottle) is not orientable, and orientability is a diffeomorphism invariant.

Prove the non-orientability directly, by showing that $K$ admits no nowhere-vanishing $2$-form: lift a hypothetical one to the cover $\mathbb{R} \times S^1$, write it in the global coordinates there, and derive a sign contradiction from invariance under the deck transformation.

**Recall:**

The objects in play are the mapping torus of a diffeomorphism, the fibre-bundle structure it carries over $S^1$, the covering map presenting it as a quotient, and the orientability criterion in terms of a nowhere-vanishing top form.

![[Def - Sphere Bundles and Mapping Tori#The Definition]]

The [[Def - Sphere Bundles and Mapping Tori|mapping torus]] of a diffeomorphism $\phi \colon F \to F$ is $E_\phi = \mathbb{Z} \backslash (\mathbb{R} \times F)$, the quotient of $\mathbb{R} \times F$ by the properly discontinuous free $\mathbb{Z}$-action $k \cdot (t, f) = (t + k, \phi^k(f))$; the generator $T$ of $\mathbb{Z}$ acts as $T(t, f) = (t + 1, \phi(f))$. The quotient map $q \colon \mathbb{R} \times F \to E_\phi$ is a smooth covering map (the quotient of a manifold by a free properly discontinuous action, [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map]]), hence a local diffeomorphism, and satisfies $q \circ T = q$. The first projection descends to $\pi \colon E_\phi \to \mathbb{Z} \backslash \mathbb{R} \cong S^1$.

![[Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle#Statement]]

The [[Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle|mapping-torus theorem]] states that for any diffeomorphism $\phi$ of a manifold $F$, the triple $(E_\phi, \pi, S^1)$ is a fibre bundle with typical fibre $F$, with local trivialisations over the two arcs $S^1 \setminus \{[0]\}$ and $S^1 \setminus \{[1/2]\}$ coming from the global triviality of $\mathbb{R} \times F \to \mathbb{R}$.

![[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form#Statement]]

A smooth manifold $M^n$ is [[Def - Orientation of a Smooth Manifold|orientable]] if and only if it admits a nowhere-vanishing top-degree form $\omega \in \Omega^n(M)$ (a **volume form**). Orientability is preserved by diffeomorphisms: if $\Phi \colon M \to N$ is a diffeomorphism and $\omega$ a nowhere-vanishing $n$-form on $N$, then $\Phi^* \omega$ is a nowhere-vanishing $n$-form on $M$, since $d\Phi_x$ is a linear isomorphism at every $x$ and hence $(\Phi^* \omega)_x = (d\Phi_x)^* \omega_{\Phi(x)} \neq 0$.

> [!warning] Convention: the angle form $d\theta$
> On $S^1$ the symbol $\theta$ denotes the angular coordinate $z = e^{i\theta}$. It is not a globally defined smooth function (it is multivalued modulo $2\pi$), but its differential $d\theta$ **is** a globally defined, nowhere-vanishing smooth $1$-form on $S^1$ — the standard angle form, characterised by $\int_{S^1} d\theta = 2\pi$. We use $d\theta$ (and $dt$ on the $\mathbb{R}$ factor) as honest global $1$-forms throughout; no step relies on $\theta$ itself being single-valued. Under the reflection $z \mapsto \bar z$, i.e. $\theta \mapsto -\theta$, the angle form pulls back to $-d\theta$.

---

# Convergent Strategy

**Problem class.** This is a *prove-a-bundle-is-nontrivial* problem, and it belongs to the family whose universal method is: find a diffeomorphism invariant of the total space that the trivial bundle's total space does not share. The trivial circle bundle over $S^1$ has total space the torus $S^1 \times S^1$, which is orientable; so if we can show the mapping torus $K$ is non-orientable, triviality is impossible. The entire creative content is the choice of *orientability* as the separating invariant, together with the mechanism that produces non-orientability — the orientation-reversing twist $\phi(z) = \bar z$ glued into the fibre as we go once around the base circle.

**Assumption pattern.** The decisive hypothesis is that $\phi$ is **orientation-reversing** on the fibre $S^1$: $\phi^* d\theta = -d\theta$. This single sign is what forces the deck transformation $T(t, \theta) = (t + 1, -\theta)$ to reverse the orientation of $\mathbb{R} \times S^1$, and a manifold that carries a fixed-point-free orientation-reversing self-diffeomorphism generating the deck group of a cover cannot have an orientation downstairs. The recognisable trigger is exactly this: a mapping torus (or any quotient by a properly discontinuous group) is non-orientable precisely when some deck transformation reverses orientation of the orientable cover.

**Theorem routing.** The route is: (i) invoke the [[Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle|mapping-torus theorem]] to get the circle-bundle structure; (ii) assume for contradiction $K$ is orientable and use the [[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form|orientability criterion]] to get a nowhere-vanishing $2$-form $\omega$ on $K$; (iii) pull $\omega$ back along the covering map $q$ (a local diffeomorphism, so the pull-back stays nowhere-vanishing) to a $T$-invariant nowhere-vanishing $2$-form $\tilde\omega$ on $\mathbb{R} \times S^1$; (iv) write $\tilde\omega = g\, dt \wedge d\theta$ and turn $T$-invariance into the functional equation $g \circ T = -g$; (v) contradict it with the fact that a continuous nowhere-vanishing function on the connected space $\mathbb{R} \times S^1$ has constant sign; (vi) conclude non-orientability, hence — via the diffeomorphism-invariance of orientability and the orientability of $S^1 \times S^1$ — nontriviality.

**Key decision point.** Two moves carry the argument. The first is *lifting to the cover*: orientability is hard to contradict directly on $K$ because $K$ has no global coordinates, but its cover $\mathbb{R} \times S^1$ has the global nowhere-vanishing $2$-form $dt \wedge d\theta$, and the covering map lets a hypothetical orientation of $K$ descend to a $T$-invariant one upstairs, where computation is possible. The second is *reading the sign off the deck transformation*: the whole obstruction is compressed into the single computation $T^*(dt \wedge d\theta) = -\,dt \wedge d\theta$, coming from $T^* d\theta = -d\theta$; everything else is bookkeeping. The genuine insight is that non-orientability is not a statement about $K$'s intrinsic curvature or shape but about a *sign* — whether the gluing diffeomorphism preserves or reverses the fibre's orientation.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles#Legal Operations|the topic page's Legal Operations]]:

1. **Present the bundle as a quotient by a deck group, and use the covering map.** Realise $K = \mathbb{Z} \backslash (\mathbb{R} \times S^1)$ with covering map $q$, a local diffeomorphism intertwining the deck transformation $T$ with the identity, $q \circ T = q$.

2. **Read off the fibre-bundle structure from the mapping-torus theorem.** Apply [[Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle]] to the reflection $\phi(z) = \bar z$ to obtain a circle bundle over $S^1$.

3. **Convert an orientability question into the existence of a nowhere-vanishing top form.** Use the criterion [[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form]] in both directions: to name a volume form on a supposedly orientable $K$, and to certify the orientability of the torus $S^1 \times S^1$.

4. **Pull a top form back along a local diffeomorphism, preserving nowhere-vanishing.** Since $dq_x$ is an isomorphism at every point, $q^*$ carries a nowhere-vanishing $2$-form on $K$ to a nowhere-vanishing $2$-form on $\mathbb{R} \times S^1$.

5. **Turn deck invariance into a functional equation and compute the twist sign.** From $q \circ T = q$ deduce $T^* \tilde\omega = \tilde\omega$, and evaluate $T^*(dt \wedge d\theta) = -\,dt \wedge d\theta$ from $T^* d\theta = -d\theta$, yielding $g \circ T = -g$.

6. **Use constancy of sign of a nowhere-vanishing continuous function on a connected space.** Contradict $g \circ T = -g$ with the intermediate value theorem applied on the connected manifold $\mathbb{R} \times S^1$.

7. **Separate two bundles by a diffeomorphism invariant of their total spaces.** Conclude nontriviality because orientability distinguishes $K$ from the total space $S^1 \times S^1$ of the trivial bundle.

---

# Hints

> [!note]- Hint 1
> Part 1 is immediate from a theorem already in the chapter — which one takes a diffeomorphism of a manifold $F$ and produces a fibre bundle over $S^1$ with fibre $F$? Here $F = S^1$ and $\phi(z) = \bar z$; check only that $\phi$ is a diffeomorphism of $S^1$.

> [!note]- Hint 2
> For nontriviality, do not try to compare $K$ with $S^1 \times S^1$ by exhibiting or ruling out an explicit isomorphism. Instead find a property of the *total space* that a trivial circle bundle over $S^1$ must have but $K$ lacks. The trivial bundle's total space is the torus. What is the simplest global property the torus has that a "twisted" surface might not?

> [!note]- Hint 3
> Aim to show $K$ is non-orientable. By the orientability criterion, this means $K$ has no nowhere-vanishing $2$-form. Suppose it had one, $\omega$; pull it back by the covering map $q \colon \mathbb{R} \times S^1 \to K$ to a $2$-form $\tilde\omega = q^* \omega$ on the cover. Two facts to establish: $\tilde\omega$ is still nowhere-vanishing (because $q$ is a local diffeomorphism), and $\tilde\omega$ is invariant under the deck transformation $T(t, \theta) = (t + 1, -\theta)$ (because $q \circ T = q$).

> [!note]- Hint 4
> Write $\tilde\omega = g(t, \theta)\, dt \wedge d\theta$ with $g$ smooth and nowhere-zero. Compute $T^*(dt \wedge d\theta)$: since $t \circ T = t + 1$ and $\theta \circ T = -\theta$, you get $dt \wedge (-d\theta) = -\,dt \wedge d\theta$. Invariance $T^* \tilde\omega = \tilde\omega$ then forces $g(t + 1, -\theta) = -g(t, \theta)$. Now use that $\mathbb{R} \times S^1$ is connected and $g$ is continuous and never zero: $g$ cannot change sign, but the equation says it must. Contradiction.

---

# Solution

The bundle structure is a one-line appeal to the mapping-torus theorem with fibre $S^1$. Nontriviality is an orientability argument: the trivial circle bundle over $S^1$ has orientable total space (the torus), so it suffices to show the mapping torus of the reflection is non-orientable. We prove that by lifting a hypothetical volume form to the cover $\mathbb{R} \times S^1$, where the global form $dt \wedge d\theta$ lets us compute, and extracting a sign contradiction from the fact that the deck transformation $T(t, \theta) = (t + 1, -\theta)$ reverses orientation.

**Step 1: $(K, \pi, S^1)$ is a circle bundle over $S^1$.**

The reflection $\phi(z) = \bar z$ is a diffeomorphism of $S^1$, so its mapping torus is a fibre bundle over $S^1$ with fibre $S^1$.

> [!note]- Derivation
> The map $\phi \colon S^1 \to S^1$, $\phi(z) = \bar z$, is smooth (complex conjugation is smooth on $\mathbb{C}$, hence on the embedded submanifold $S^1$) and is its own inverse, $\phi \circ \phi = \operatorname{id}$ (since $\bar{\bar z} = z$), so it is a diffeomorphism of $S^1$. Its mapping torus $E_\phi = \mathbb{Z} \backslash (\mathbb{R} \times S^1)$, with the $\mathbb{Z}$-action $k \cdot (t, z) = (t + k, \phi^k(z))$, is defined exactly as in [[Def - Sphere Bundles and Mapping Tori]] with $F = S^1$.
>
> By the [[Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle|mapping-torus theorem]] — restated: for any diffeomorphism $\phi$ of a manifold $F$, $(E_\phi, \pi, S^1)$ is a fibre bundle with typical fibre $F$ — the triple $(K, \pi, S^1)$ is a fibre bundle with typical fibre $F = S^1$. Since $\dim S^1 = 1$ for both base and fibre, the total space $K$ is a smooth surface, $\dim K = 2$. This proves part 1.

**Step 2: Set up the cover and the deck transformation in global coordinates.**

The quotient map $q \colon \mathbb{R} \times S^1 \to K$ is a local diffeomorphism with $q \circ T = q$, where $T(t, \theta) = (t + 1, -\theta)$; the cover carries the global nowhere-vanishing $2$-form $dt \wedge d\theta$.

> [!note]- Derivation
> The $\mathbb{Z}$-action on $\mathbb{R} \times S^1$ is free and properly discontinuous (this is verified when the mapping torus is defined, [[Def - Sphere Bundles and Mapping Tori]]). By [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the quotient theorem]] — the quotient of a manifold by a free properly discontinuous group action is a manifold and the quotient map is a covering map — the projection
> $$q \colon \mathbb{R} \times S^1 \longrightarrow K = \mathbb{Z} \backslash (\mathbb{R} \times S^1)$$
> is a smooth covering map, in particular a **local diffeomorphism**: every point has a neighbourhood mapped diffeomorphically onto its image, so $dq_x$ is a linear isomorphism for every $x$.
>
> The generator of the $\mathbb{Z}$-action is the diffeomorphism
> $$T \colon \mathbb{R} \times S^1 \to \mathbb{R} \times S^1, \qquad T(t, z) = (t + 1, \phi(z)) = (t + 1, \bar z),$$
> which in the angular coordinate $z = e^{i\theta}$ reads $T(t, \theta) = (t + 1, -\theta)$ (because $\bar z = e^{-i\theta}$). As $T$ is the deck transformation of the cover, $q$ is constant on $\mathbb{Z}$-orbits, so
> $$q \circ T = q.$$
> Finally, $dt$ (from the $\mathbb{R}$ factor) and $d\theta$ (the global angle form on $S^1$, see the Convention callout) are global nowhere-vanishing $1$-forms on $\mathbb{R} \times S^1$, so $dt \wedge d\theta$ is a global nowhere-vanishing $2$-form there, and every $2$-form on the surface $\mathbb{R} \times S^1$ is $g\, dt \wedge d\theta$ for a unique smooth $g$.

**Step 3: A volume form on $K$ would lift to a $T$-invariant nowhere-vanishing $2$-form upstairs.**

Assuming $K$ orientable produces a nowhere-vanishing $2$-form $\omega$ on $K$; its pull-back $\tilde\omega = q^* \omega$ is nowhere-vanishing and $T$-invariant.

> [!note]- Derivation
> Suppose, for contradiction, that $K$ is **orientable**. Since $\dim K = 2$, the [[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form|orientability criterion]] gives a nowhere-vanishing $2$-form $\omega \in \Omega^2(K)$. Define
> $$\tilde\omega := q^* \omega \in \Omega^2(\mathbb{R} \times S^1).$$
>
> *$\tilde\omega$ is nowhere-vanishing.* At any point $x \in \mathbb{R} \times S^1$, $(\tilde\omega)_x = (dq_x)^* \omega_{q(x)}$, the pull-back of the nonzero alternating $2$-form $\omega_{q(x)}$ by the linear isomorphism $dq_x$ (Step 2). The pull-back of a nonzero top form by a linear isomorphism is again nonzero — explicitly, $(dq_x)^*\omega_{q(x)}(u, v) = \omega_{q(x)}(dq_x u, dq_x v)$, and choosing $u, v$ with $dq_x u, dq_x v$ a basis on which $\omega_{q(x)} \neq 0$ (possible as $dq_x$ is onto) makes it nonzero. Hence $(\tilde\omega)_x \neq 0$ for every $x$.
>
> *$\tilde\omega$ is $T$-invariant.* Using $q \circ T = q$ from Step 2 and functoriality of pull-back,
> $$T^* \tilde\omega = T^* (q^* \omega) = (q \circ T)^* \omega = q^* \omega = \tilde\omega \qquad (\text{since } q \circ T = q).$$

**Step 4: Invariance forces a sign-reversing functional equation on the coefficient.**

Writing $\tilde\omega = g\, dt \wedge d\theta$, the invariance $T^* \tilde\omega = \tilde\omega$ becomes $g \circ T = -g$, that is $g(t + 1, -\theta) = -g(t, \theta)$.

> [!note]- Derivation
> By Step 2 write $\tilde\omega = g\, dt \wedge d\theta$ with $g \in C^\infty(\mathbb{R} \times S^1)$; by Step 3, $g$ is nowhere zero. Compute the pull-back of the basic $2$-form under $T(t, \theta) = (t + 1, -\theta)$. The two component pull-backs are
> $$T^* dt = d(t \circ T) = d(t + 1) = dt \qquad (\text{the } t\text{-coordinate shifts by the constant } 1),$$
> $$T^* d\theta = d(\theta \circ T) = d(-\theta) = -d\theta \qquad (\text{the reflection } \phi(z) = \bar z \text{ acts as } \theta \mapsto -\theta).$$
> Since pull-back is an algebra homomorphism on forms,
> $$T^*(dt \wedge d\theta) = (T^* dt) \wedge (T^* d\theta) = dt \wedge (-d\theta) = -\,dt \wedge d\theta \qquad (\text{by the two lines above}).$$
> Also $T^* g = g \circ T$. Therefore
> $$T^* \tilde\omega = (g \circ T)\, T^*(dt \wedge d\theta) = -(g \circ T)\, dt \wedge d\theta \qquad (\text{pull-back of a product; previous display}).$$
> The invariance $T^* \tilde\omega = \tilde\omega$ from Step 3 reads $-(g \circ T)\, dt \wedge d\theta = g\, dt \wedge d\theta$. As $dt \wedge d\theta$ is nowhere-vanishing, the coefficients agree:
> $$g \circ T = -g, \qquad \text{i.e.} \qquad g(t + 1, -\theta) = -g(t, \theta) \quad \text{for all } (t, \theta) \in \mathbb{R} \times S^1.$$

**Step 5: The sign equation contradicts constancy of sign, so $K$ is non-orientable.**

A continuous nowhere-vanishing function on the connected space $\mathbb{R} \times S^1$ has constant sign, which is incompatible with $g \circ T = -g$; the contradiction shows no volume form exists.

> [!note]- Derivation
> The space $\mathbb{R} \times S^1$ is connected (a product of connected spaces). The function $g$ is continuous and nowhere zero, so by the intermediate value theorem it cannot take both a positive and a negative value: if it did, its value would have to pass through $0$ somewhere along a path joining the two points, contradicting $g \neq 0$ everywhere. Hence $g$ has **constant sign**: either $g > 0$ everywhere or $g < 0$ everywhere.
>
> Fix any point $(t, \theta)$. The image point $T(t, \theta) = (t + 1, -\theta)$ lies in the same connected space, so $g(t + 1, -\theta)$ and $g(t, \theta)$ have the **same** sign. But Step 4 gives $g(t + 1, -\theta) = -g(t, \theta)$, and since $g(t, \theta) \neq 0$ this forces $g(t + 1, -\theta)$ and $g(t, \theta)$ to have **opposite** signs. Same sign and opposite sign, with both values nonzero, is a contradiction.
>
> The contradiction was reached from the sole extra assumption that $K$ is orientable (Step 3). Therefore $K$ admits no nowhere-vanishing $2$-form, and by the [[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form|orientability criterion]], $K$ is **non-orientable**. This proves part 2.

**Step 6: Non-orientability forces nontriviality.**

The trivial circle bundle over $S^1$ has the orientable torus as total space; since orientability is a diffeomorphism invariant and $K$ is non-orientable, $K$ is not that total space, so the bundle is nontrivial.

> [!note]- Derivation
> Suppose, for contradiction, that the bundle $(K, \pi, S^1)$ were **trivial**. By the [[Def - Fibre Bundle|definition of triviality]], its total space would be diffeomorphic to the total space of the product bundle $S^1 \times S^1 \to S^1$, namely the torus $\mathbb{T}^2 = S^1 \times S^1$; call the diffeomorphism $\Phi \colon K \to \mathbb{T}^2$.
>
> The torus is orientable: $d\theta_1 \wedge d\theta_2$, the wedge of the two global angle forms on the two circle factors, is a global nowhere-vanishing $2$-form on $S^1 \times S^1$, so by the orientability criterion $\mathbb{T}^2$ is orientable. Then $\Phi^*(d\theta_1 \wedge d\theta_2)$ is a nowhere-vanishing $2$-form on $K$ (the diffeomorphism $\Phi$ has $d\Phi_x$ an isomorphism at each point, so it pulls a volume form back to a volume form, exactly as recorded in the orientability criterion's invariance clause). This makes $K$ orientable, contradicting Step 5.
>
> Therefore $(K, \pi, S^1)$ is **not** trivial. The mapping torus of the reflection $z \mapsto \bar z$ — the Klein bottle — is a nontrivial circle bundle over $S^1$. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** The mapping torus $K = E_\phi$ of the reflection $\phi(z) = \bar z$ of $S^1$ is a nontrivial circle bundle over $S^1$.
>
> *Proof.* The reflection $\phi(z) = \bar z$ is a diffeomorphism of $S^1$ (smooth, with $\phi \circ \phi = \operatorname{id}$), so by [[Thm - The Mapping Torus of a Diffeomorphism is a Fibre Bundle over the Circle|the mapping-torus theorem]], $(K, \pi, S^1)$ is a fibre bundle with typical fibre $S^1$; its total space is a surface.
>
> Present $K = \mathbb{Z} \backslash (\mathbb{R} \times S^1)$ via the covering map $q \colon \mathbb{R} \times S^1 \to K$ (a local diffeomorphism, by [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map]]), with deck transformation $T(t, \theta) = (t + 1, -\theta)$ satisfying $q \circ T = q$.
>
> Suppose $K$ were orientable. Then it has a nowhere-vanishing $2$-form $\omega$ ([[Thm - A Manifold is Orientable iff it Admits a Nowhere-Vanishing Top Form|orientability criterion]]). Its pull-back $\tilde\omega = q^* \omega$ is nowhere-vanishing (as $q$ is a local diffeomorphism) and $T$-invariant, since $T^* \tilde\omega = (q \circ T)^* \omega = q^* \omega = \tilde\omega$. Writing $\tilde\omega = g\, dt \wedge d\theta$ with $g$ smooth and nowhere zero, and using $T^* dt = dt$, $T^* d\theta = -d\theta$, we get $T^*(dt \wedge d\theta) = -\,dt \wedge d\theta$, so invariance yields $g \circ T = -g$, i.e. $g(t + 1, -\theta) = -g(t, \theta)$. But $\mathbb{R} \times S^1$ is connected and $g$ is continuous and nowhere zero, so $g$ has constant sign; then $g(t + 1, -\theta)$ and $g(t, \theta)$ share a sign, contradicting $g(t + 1, -\theta) = -g(t, \theta)$ with $g \neq 0$. Hence $K$ is non-orientable.
>
> If the bundle were trivial, its total space would be diffeomorphic to $S^1 \times S^1$, which is orientable ($d\theta_1 \wedge d\theta_2$ is a volume form); a diffeomorphism pulls this volume form back to one on $K$, making $K$ orientable — contradiction. Therefore the bundle is nontrivial. $\blacksquare$

> [!warning] Illegal but tempting route: "the fibre $S^1$ is orientable and the base $S^1$ is orientable, so the total space is orientable"
> It is tempting to conclude orientability of the total space from orientability of base and fibre, as though orientations simply multiply. This is false in general: the Möbius strip has orientable base $S^1$ and orientable fibre (an interval), yet is non-orientable, and the Klein bottle here is the same phenomenon with a circle fibre. A fibre bundle's total space is orientable when base and fibre are oriented **and the transition (or gluing) diffeomorphisms preserve the fibre orientation** — the missing hypothesis. Here the single gluing map is $\phi(z) = \bar z$, which *reverses* the orientation of the fibre $S^1$ ($\phi^* d\theta = -d\theta$), and that reversal is exactly the obstruction. The correct statement — orientable total space when the structure group can be reduced to orientation-preserving diffeomorphisms — is what the sign computation in Step 4 tests. Compare [[Ex - The Sphere is Orientable but the Möbius Strip is Not]], where the identical mechanism appears with an interval fibre.

---

# Key Takeaways

**A mapping torus is orientable exactly when its gluing diffeomorphism preserves the fibre's orientation, and non-orientability is read off a single sign.** The mapping torus $E_\phi$ is built by taking $\mathbb{R} \times F$ and identifying $(t, f)$ with $(t + 1, \phi(f))$; going once around the base circle applies $\phi$ to the fibre. If $\phi$ preserves orientation, the two ends of the strip $[0, 1] \times F$ glue up consistently and the total space is orientable (for $F = S^1$ one gets the torus); if $\phi$ reverses orientation, the ends glue with a flip and the total space cannot be coherently oriented (for $F = S^1$ one gets the Klein bottle). The reusable principle is that *the orientability of a quotient by a group of diffeomorphisms is governed by whether the group acts by orientation-preserving maps on the orientable cover*: a fixed-point-free orientation-reversing deck transformation obstructs any invariant volume form. The trigger to apply this is any manifold presented as a mapping torus, or more generally as $\Gamma \backslash \widetilde{M}$ for a properly discontinuous $\Gamma$ acting on an orientable $\widetilde{M}$; the diagnostic is to compute the sign of each generator's action on a top form, here condensed to $\phi^* d\theta = -d\theta$.

**To contradict a global property of a quotient, lift it to the cover where global coordinates exist, and let invariance carry the contradiction.** The obstacle to arguing directly on $K$ is that $K$ has no single coordinate chart and no obvious global $2$-form to test. The covering space $\mathbb{R} \times S^1$ repairs both: it is a product with the global nowhere-vanishing form $dt \wedge d\theta$, and a hypothetical orientation of $K$ descends to a *deck-invariant* orientation upstairs via pull-back along the covering map. Because the covering map is a local diffeomorphism, pull-back neither creates nor destroys zeros of a top form, so "nowhere-vanishing on $K$" transfers faithfully to "nowhere-vanishing and $T$-invariant on the cover", where it becomes a concrete functional equation $g \circ T = -g$ that a connectedness argument can refute. The transferable diagnostic: whenever a manifold is a quotient $\Gamma \backslash \widetilde{M}$ and you must prove it lacks some invariant structure (an orientation, a nowhere-zero section, a flat metric of a given type), lift the structure to $\widetilde{M}$, record its $\Gamma$-invariance, and look for an equation invariance forces that the geometry of $\widetilde{M}$ cannot satisfy — here, sign-reversal against constant-sign.

**Nontriviality of a bundle is most cheaply proved by separating total spaces with a diffeomorphism invariant, not by chasing trivialisations.** A direct attack on "$K \not\cong S^1 \times S^1$ as bundles" would wade through transition functions or attempt to rule out every possible global section-frame; the economical route is to notice that the trivial circle bundle over $S^1$ has an orientable total space and then to defeat triviality by defeating orientability of $K$. This is an instance of the general pattern that *a bundle invariant is often best detected through a topological invariant of the total space* — here orientability, elsewhere the Euler characteristic, the fundamental group, or a characteristic number. The method is robust because it needs only one property that the model trivial bundle's total space has and the candidate lacks, and both orientability and its diffeomorphism-invariance are easy to certify. The companion exercises that calibrate this technique are [[Ex - The Möbius Strip as a Mapping Torus is a Nontrivial Bundle]], where the separating invariant is the non-existence of a nowhere-vanishing section, and [[Ex - Pull-Back of a Fibre Bundle along a Constant Map is Trivial]], which sits at the opposite pole, exhibiting the maximally trivial case for contrast.
