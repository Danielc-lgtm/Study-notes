---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Reynolds Transport Theorem"
  - "Thm - Cartan's Magic Formula"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Def - Lie Derivative of a Differential Form"
  - "Def - Frankel Dictionary (Forms vs Vector Calculus)"
  - "Ex - Maxwell's Equations as Two Form Equations on Minkowski Space"
tags: [geometry, differential-geometry, electromagnetism, faraday]
---

# Problem Statement

In $\mathbb{R}^3$, let $\vec B(t, \vec x)$ be a smooth time-dependent magnetic field and let $S(t)$ be a smooth oriented surface that is being carried by a velocity field $\vec u(t, \vec x)$ — for instance, the moving surface bounded by a wire loop that is changing shape and position in time. The **magnetic flux** through $S(t)$ is
$$\Phi(t) := \int_{S(t)}\vec B\cdot d\vec A.$$
The **EMF** induced around the wire loop $\partial S(t)$ is $\mathcal{E}(t) := \oint_{\partial S(t)}\vec E\cdot d\vec\ell$ in the rest frame of the wire. The integral form of Faraday's law of induction asserts
$$\mathcal{E}(t) = -\frac{d\Phi}{dt}.$$

**(a)** Using the Reynolds Transport Theorem applied to the magnetic flux $2$-form $\beta = \star\vec B^\flat$, compute $\frac{d}{dt}\int_{S(t)}\beta$ and decompose it into the explicit-time-dependence term $\int_{S(t)}\partial_t\beta$ plus the Lie-derivative (flow) term $\int_{S(t)}\mathcal{L}_{\vec u}\beta$.

**(b)** Using the source-free Maxwell equation $dF = 0$ (where $F$ is the Faraday $2$-form on Minkowski space) and the spatial-decomposition identification $\partial_t\beta\,dt = $ ($\vec E$-related piece), show that $\partial_t\vec B + \nabla\times\vec E = 0$ — the differential form of Faraday's law — emerges from $dF = 0$.

**(c)** Combine (a) and (b), using Cartan's magic formula and Stokes's theorem, to derive the integral form
$$\frac{d\Phi}{dt} = -\oint_{\partial S(t)}\vec E_{\text{rest}}\cdot d\vec\ell,$$
where $\vec E_{\text{rest}} = \vec E + \vec u\times\vec B$ is the electric field in the rest frame of the wire (the so-called **motional EMF**).

**Recall:**

This exercise weaves together three structural tools.

![[Thm - Reynolds Transport Theorem#Statement]]

Cartan's magic formula relates the Lie derivative, exterior derivative, and interior product:
$$\mathcal{L}_X\omega = d(\iota_X\omega) + \iota_X(d\omega).$$
See [[Thm - Cartan's Magic Formula]] for the derivation and the structural reason this identity holds.

The Faraday $2$-form on Minkowski $\mathbb{R}^{1,3}$ packages $\vec E$ and $\vec B$ into a single $2$-form:
$$F = -E_i\,dt\wedge dx^i + \tfrac{1}{2}\epsilon_{ijk}B^k\,dx^i\wedge dx^j.$$
The two homogeneous Maxwell equations ($\nabla\cdot\vec B = 0$ and $\partial_t\vec B + \nabla\times\vec E = 0$) are exactly the components of $dF = 0$. See [[Ex - Maxwell's Equations as Two Form Equations on Minkowski Space]] for the full unpacking.

On $\mathbb{R}^3$, the magnetic field $\vec B$ has two equivalent form-language representations from the [[Def - Frankel Dictionary (Forms vs Vector Calculus)|Frankel dictionary]]: the **circulation** $1$-form $\vec B^\flat = B^1\,dx + B^2\,dy + B^3\,dz$ and the **flux** $2$-form $\beta = \star\vec B^\flat = B^1\,dy\wedge dz + B^2\,dz\wedge dx + B^3\,dx\wedge dy$. For magnetic flux through a surface, $\beta$ is the right form: $\int_S\beta = \int_S\vec B\cdot d\vec A$.

---

# Convergent Strategy

**Problem class.** This is a *derive an integral conservation law from a differential one, accounting for moving regions* problem. It is the most important application of Reynolds's theorem in classical physics: a moving region forces a correction to the naive "differentiate inside the integral" that recovers the universally-known motional EMF term.

**Assumption pattern.** The hypotheses are: (i) a smooth time-dependent vector field $\vec u(t, \vec x)$ that flows the surface, (ii) a smooth magnetic field $\vec B(t, \vec x)$ satisfying $\nabla\cdot\vec B = 0$ (no monopoles), (iii) the differential Faraday equation $\partial_t\vec B = -\nabla\times\vec E$ which is one component of $dF = 0$. The first two together let us apply Reynolds; the third lets us identify the explicit-time-dependence term as $-\nabla\times\vec E$, which when integrated over a surface (via Stokes) becomes a boundary line integral of $\vec E$. The combination is what produces the right answer for moving conductors.

**Theorem routing.** The route runs: Reynolds Transport Theorem ($\to$ split into $\partial_t\beta$ term + $\mathcal{L}_{\vec u}\beta$ term) $\to$ Cartan's magic formula on $\mathcal{L}_{\vec u}\beta$ ($\to$ $d\iota_{\vec u}\beta + \iota_{\vec u}d\beta$, with the second term being a $3$-form on a surface, which vanishes for a different reason than one might expect) $\to$ Stokes's theorem ($\to$ converts both $d$-terms into boundary integrals) $\to$ Faraday law $dF = 0$ unpacked, identifying $\partial_t\beta = $ $-(\text{curl}\,\vec E)$-related-$2$-form $\to$ collect terms.

**Key decision point.** The non-obvious step is recognizing that the $\iota_{\vec u}$ contraction with the magnetic flux $2$-form $\beta = \star\vec B^\flat$ is, by the form-language identity $\iota_{\vec u}(\star\vec B^\flat) = -\star(\vec u^\flat\wedge\vec B^\flat) = -(\vec u\times\vec B)^\flat$, exactly the motional EMF contribution. This algebra is the precise reason the rest-frame electric field in moving conductors is $\vec E + \vec u\times\vec B$: the $\vec u\times\vec B$ piece does not come from a separate physical mechanism, it comes from the geometric fact that flowing surfaces pick up a Lie-derivative correction that translates to $-d\iota_{\vec u}\beta = d((\vec u\times\vec B)^\flat)$, which integrates by Stokes to a $\oint(\vec u\times\vec B)\cdot d\vec\ell$ line integral. A reader who treats $\frac{d\Phi}{dt} = \int\partial_t\vec B\cdot d\vec A$ and forgets the moving-surface correction will miss the motional EMF entirely.

---

# Legal Operations Used

This solution deploys the following legal operations:

1. **Apply Reynolds Transport** (the central operation of this topic, see [[Thm - Reynolds Transport Theorem]]). The full statement separates the rate of change of a moving integral into the explicit time derivative of the integrand and the Lie-derivative correction; both contribute non-trivially here.

2. **Apply Cartan's magic formula** to convert $\mathcal{L}_{\vec u}\beta$ into $d\iota_{\vec u}\beta + \iota_{\vec u}d\beta$. The trigger is the appearance of a Lie derivative whose action we need to compute and convert into something integrable.

3. **Apply Stokes's theorem** ([[Thm - Stokes' Theorem on Manifolds]]) to turn $\int_S d\eta$ into $\int_{\partial S}\eta$ for any $1$-form $\eta$. The trigger is the appearance of $d$ acting on a $1$-form inside a surface integral.

4. **Apply the Frankel dictionary** to convert between form-language identities and vector-calculus identities. The non-trivial computations are: $\beta = \star\vec B^\flat$ (flux $2$-form), $\iota_{\vec u}(\star\vec B^\flat) = -\star(\vec u^\flat\wedge\vec B^\flat) = -(\vec u\times\vec B)^\flat$ (cross product as interior contraction with $\star$), and $d\beta = \nabla\cdot\vec B\,dV$ (divergence as $d$ of $2$-form, which vanishes by $\nabla\cdot\vec B = 0$).

---

# Hints

> [!note]- Hint 1
> Reynolds's theorem applied to a *time-dependent* form on a moving surface has *two* terms: the explicit time derivative $\partial_t\beta$ and the Lie-derivative-along-the-flow $\mathcal{L}_{\vec u}\beta$. Write both down, and remember that we are integrating a $2$-form over a $2$-surface, so the result has the right dimensions to compare to a flux.

> [!note]- Hint 2
> Apply Cartan's magic formula to $\mathcal{L}_{\vec u}\beta$: $\mathcal{L}_{\vec u}\beta = d\iota_{\vec u}\beta + \iota_{\vec u}d\beta$. What is $d\beta$? In $\mathbb{R}^3$, $d\beta = d(\star\vec B^\flat) = (\nabla\cdot\vec B)\,dV$. Since $\nabla\cdot\vec B = 0$ (no magnetic monopoles), $d\beta = 0$, and the Lie derivative reduces to $\mathcal{L}_{\vec u}\beta = d\iota_{\vec u}\beta$. Then Stokes converts $\int_S d\iota_{\vec u}\beta$ into $\oint_{\partial S}\iota_{\vec u}\beta$.

> [!note]- Hint 3
> Compute $\iota_{\vec u}\beta = \iota_{\vec u}(\star\vec B^\flat)$ explicitly. The general identity from the Frankel dictionary is $\iota_X(\star\omega) = -\star(X^\flat\wedge\omega)$ for $X$ a vector field and $\omega$ a $1$-form (in $\mathbb{R}^3$ with positive signature). So $\iota_{\vec u}(\star\vec B^\flat) = -\star(\vec u^\flat\wedge\vec B^\flat) = -(\vec u\times\vec B)^\flat$ by the cross-product identity $(\vec u\times\vec B)^\flat = \star(\vec u^\flat\wedge\vec B^\flat)$.

> [!note]- Hint 4
> For part (b), recall that $F = -E_i\,dt\wedge dx^i + \tfrac{1}{2}\epsilon_{ijk}B^k\,dx^i\wedge dx^j$, and decompose $dF$ into terms with $dt\wedge\cdots$ and terms without. The $dt$-free terms of $dF$ are $\frac{1}{2}\epsilon_{ijk}\partial_l B^k\,dx^l\wedge dx^i\wedge dx^j$, which sum to $\nabla\cdot\vec B\,dx\wedge dy\wedge dz$. The $dt$-containing terms include the time derivative of $\vec B$ and the spatial derivative of $\vec E$, and they sum to $(\partial_t\vec B + \nabla\times\vec E)$-related.

> [!note]- Hint 5
> Combine (a) and (b). The explicit-time-derivative term is $\int_{S(t)}\partial_t\beta\,dt$, which by Faraday's differential law equals $-\int_{S(t)}\nabla\times\vec E\cdot d\vec A$, and by Stokes this is $-\oint_{\partial S(t)}\vec E\cdot d\vec\ell$. The Lie-derivative term is $\oint_{\partial S(t)}\iota_{\vec u}\beta = -\oint_{\partial S(t)}(\vec u\times\vec B)\cdot d\vec\ell$. Combining and rearranging gives $\frac{d\Phi}{dt} = -\oint_{\partial S(t)}(\vec E + \vec u\times\vec B)\cdot d\vec\ell$, identifying $\vec E_{\text{rest}} = \vec E + \vec u\times\vec B$ as the field measured in the wire's rest frame.

---

# Solution

The proof breaks into three steps. Step 1 applies Reynolds's theorem to the magnetic flux $2$-form $\beta = \star\vec B^\flat$, separating the rate of change of flux into a "stationary $\vec B$" term and a "moving surface" term. Step 2 uses the differential Faraday law (a component of $dF = 0$) to identify the first term as a line integral of $\vec E$. Step 3 uses Cartan's formula plus Stokes to convert the second term into a line integral of $\vec u\times\vec B$. The non-obvious move is in Step 3, where the algebraic identity $\iota_{\vec u}(\star\vec B^\flat) = -(\vec u\times\vec B)^\flat$ recognizes the motional EMF as the geometric Lie-derivative correction.

**Step 1: Reynolds's theorem decomposes $d\Phi/dt$.**

Apply the time-dependent Reynolds Transport Theorem to $\omega_t = \beta(t) = \star\vec B(t,\cdot)^\flat$ and the moving surface $S(t)$:
$$\frac{d\Phi}{dt} = \frac{d}{dt}\int_{S(t)}\beta(t) = \int_{S(t)}\frac{\partial\beta}{\partial t} + \int_{S(t)}\mathcal{L}_{\vec u}\beta.$$

> [!note]- Derivation
> Reynolds's theorem in the time-dependent form (see [[Thm - Reynolds Transport Theorem]]) states
> $$\frac{d}{dt}\int_{\phi_t(D)}\omega_t = \int_{\phi_t(D)}\left(\frac{\partial\omega_t}{\partial t} + \mathcal{L}_{X(t,\cdot)}\omega_t\right).$$
> Here $\omega_t = \beta(t)$, $X(t,\cdot) = \vec u(t,\cdot)$, $D = S(0)$, and $\phi_t(D) = S(t)$. Substituting,
> $$\frac{d}{dt}\int_{S(t)}\beta = \int_{S(t)}\frac{\partial\beta}{\partial t} + \int_{S(t)}\mathcal{L}_{\vec u}\beta.$$

**Step 2: Identify the explicit-time-derivative term as $-\oint_{\partial S(t)}\vec E\cdot d\vec\ell$.**

The differential Faraday law $\partial_t\vec B = -\nabla\times\vec E$, which is one component of the source-free Maxwell equation $dF = 0$, gives $\partial_t\beta = -\star(\nabla\times\vec E)^\flat$. Then by Stokes's theorem applied to the $1$-form $\vec E^\flat$,
$$\int_{S(t)}\frac{\partial\beta}{\partial t} = -\int_{S(t)}\nabla\times\vec E\cdot d\vec A = -\oint_{\partial S(t)}\vec E\cdot d\vec\ell.$$

> [!note]- Derivation
> The Faraday $2$-form on Minkowski $\mathbb{R}^{1,3}$ is $F = -E_i\,dt\wedge dx^i + \tfrac{1}{2}\epsilon_{ijk}B^k\,dx^i\wedge dx^j$ ([[Ex - Maxwell's Equations as Two Form Equations on Minkowski Space]]). Compute $dF$:
> $$dF = -\partial_jE_i\,dx^j\wedge dt\wedge dx^i + \tfrac{1}{2}\epsilon_{ijk}\partial_t B^k\,dt\wedge dx^i\wedge dx^j + \tfrac{1}{2}\epsilon_{ijk}\partial_l B^k\,dx^l\wedge dx^i\wedge dx^j.$$
> Separating into $dt$-free and $dt$-containing parts:
>
> *$dt$-free part* (spatial-only): $\tfrac{1}{2}\epsilon_{ijk}\partial_l B^k\,dx^l\wedge dx^i\wedge dx^j$. The sum $\sum_l\epsilon_{ijk}\partial_l B^k\,dx^l\wedge dx^i\wedge dx^j$ when $\{l, i, j\} = \{1, 2, 3\}$ becomes $(\partial_1 B^1 + \partial_2 B^2 + \partial_3 B^3)\,dx^1\wedge dx^2\wedge dx^3 = (\nabla\cdot\vec B)\,dV$. The $dt$-free part of $dF = 0$ gives $\nabla\cdot\vec B = 0$.
>
> *$dt$-containing part*: $-\partial_jE_i\,dx^j\wedge dt\wedge dx^i + \tfrac{1}{2}\epsilon_{ijk}\partial_t B^k\,dt\wedge dx^i\wedge dx^j$. Rearranging the wedge to put $dt$ first: $\partial_jE_i\,dt\wedge dx^j\wedge dx^i + \tfrac{1}{2}\epsilon_{ijk}\partial_t B^k\,dt\wedge dx^i\wedge dx^j$. The factor on $dt\wedge dx^i\wedge dx^j$ becomes $\partial_jE_i - \partial_iE_j + \epsilon_{ijk}\partial_t B^k = -\epsilon_{ijl}(\nabla\times\vec E)^l + \epsilon_{ijk}\partial_t B^k = \epsilon_{ijk}(\partial_t B^k + (\nabla\times\vec E)^k)$. Setting this to zero (since $dF = 0$) gives $\partial_t\vec B + \nabla\times\vec E = 0$, the differential Faraday law.
>
> Now translate $\partial_t\beta$ via $\beta = \star\vec B^\flat$. Differentiating, $\partial_t\beta = \star(\partial_t\vec B)^\flat$. Using $\partial_t\vec B = -\nabla\times\vec E$, this is $\partial_t\beta = -\star(\nabla\times\vec E)^\flat$. Integrating over $S(t)$ and using the dictionary $\int_S\star\vec F^\flat = \int_S\vec F\cdot d\vec A$,
> $$\int_{S(t)}\partial_t\beta = -\int_{S(t)}\nabla\times\vec E\cdot d\vec A.$$
> By Stokes's theorem ($\int_S\nabla\times\vec E\cdot d\vec A = \oint_{\partial S}\vec E\cdot d\vec\ell$, which is Kelvin–Stokes applied to $\omega = \vec E^\flat$),
> $$\int_{S(t)}\partial_t\beta = -\oint_{\partial S(t)}\vec E\cdot d\vec\ell.$$

**Step 3: Identify the Lie-derivative term as $-\oint_{\partial S(t)}(\vec u\times\vec B)\cdot d\vec\ell$.**

Cartan's magic formula: $\mathcal{L}_{\vec u}\beta = d\iota_{\vec u}\beta + \iota_{\vec u}d\beta$. The second term vanishes because $d\beta = \nabla\cdot\vec B\,dV = 0$. The first term integrates via Stokes:
$$\int_{S(t)}\mathcal{L}_{\vec u}\beta = \int_{S(t)}d\iota_{\vec u}\beta = \oint_{\partial S(t)}\iota_{\vec u}\beta = -\oint_{\partial S(t)}(\vec u\times\vec B)\cdot d\vec\ell.$$

> [!note]- Derivation
> By Cartan's magic formula ([[Thm - Cartan's Magic Formula]]),
> $$\mathcal{L}_{\vec u}\beta = d(\iota_{\vec u}\beta) + \iota_{\vec u}(d\beta).$$
> The second term: $d\beta = d(\star\vec B^\flat) = (\nabla\cdot\vec B)\,dV$ by the Frankel dictionary's divergence-as-$d$-of-$2$-form identity. By the source-free Maxwell equation $\nabla\cdot\vec B = 0$, $d\beta = 0$, so $\iota_{\vec u}(d\beta) = 0$.
>
> The first term: $\iota_{\vec u}\beta = \iota_{\vec u}(\star\vec B^\flat)$. The key identity is $\iota_X(\star\omega) = -\star(X^\flat\wedge\omega)$ for $X$ a vector field and $\omega$ a $1$-form on oriented Riemannian $\mathbb{R}^3$ (a standard identity in oriented Riemannian geometry; in dimension $3$, the sign is $-$). So
> $$\iota_{\vec u}\beta = -\star(\vec u^\flat\wedge\vec B^\flat) = -(\vec u\times\vec B)^\flat,$$
> using the dictionary identity $(\vec u\times\vec B)^\flat = \star(\vec u^\flat\wedge\vec B^\flat)$.
>
> Now by Stokes's theorem applied to the $1$-form $\iota_{\vec u}\beta = -(\vec u\times\vec B)^\flat$,
> $$\int_{S(t)}d(\iota_{\vec u}\beta) = \oint_{\partial S(t)}\iota_{\vec u}\beta = -\oint_{\partial S(t)}(\vec u\times\vec B)\cdot d\vec\ell.$$
> Combining,
> $$\int_{S(t)}\mathcal{L}_{\vec u}\beta = -\oint_{\partial S(t)}(\vec u\times\vec B)\cdot d\vec\ell.$$

**Step 4: Collect into the integral Faraday law with motional EMF.**

Adding the two contributions from Steps 2 and 3 and substituting into Step 1's Reynolds decomposition,
$$\frac{d\Phi}{dt} = -\oint_{\partial S(t)}\vec E\cdot d\vec\ell - \oint_{\partial S(t)}(\vec u\times\vec B)\cdot d\vec\ell = -\oint_{\partial S(t)}(\vec E + \vec u\times\vec B)\cdot d\vec\ell = -\oint_{\partial S(t)}\vec E_{\text{rest}}\cdot d\vec\ell.$$

The combination $\vec E_{\text{rest}} = \vec E + \vec u\times\vec B$ is the electric field measured by an observer comoving with the wire — this is the **rest-frame** electric field of the conductor. The integral Faraday law of induction is recovered exactly.

> [!note]- Derivation
> Substituting Steps 2 and 3 into Step 1:
> \begin{align*}
> \frac{d\Phi}{dt} &= \int_{S(t)}\partial_t\beta + \int_{S(t)}\mathcal{L}_{\vec u}\beta \\
> &= \left(-\oint_{\partial S(t)}\vec E\cdot d\vec\ell\right) + \left(-\oint_{\partial S(t)}(\vec u\times\vec B)\cdot d\vec\ell\right) \\
> &= -\oint_{\partial S(t)}\big(\vec E + \vec u\times\vec B\big)\cdot d\vec\ell.
> \end{align*}
> The motional EMF $\vec u\times\vec B$ emerged purely from the Lie-derivative term — i.e., from the fact that the surface itself is moving. Identifying $\vec E_{\text{rest}} = \vec E + \vec u\times\vec B$ as the rest-frame electric field (the field seen by a charge comoving with the wire), the integral Faraday law is
> $$\mathcal{E}(t) := \oint_{\partial S(t)}\vec E_{\text{rest}}\cdot d\vec\ell = -\frac{d\Phi}{dt}.$$

> [!note]- Complete formal solution
> Let $\vec B(t, \vec x)$ be a smooth magnetic field on $\mathbb{R}^3$ with $\nabla\cdot\vec B = 0$, and let $\vec E(t, \vec x)$ satisfy the source-free Maxwell equation $\partial_t\vec B + \nabla\times\vec E = 0$. Let $\vec u(t, \vec x)$ be a smooth velocity field and $S(t) = \phi_t(S_0)$ the surface transported by its flow.
>
> *Reynolds decomposition.* By the time-dependent Reynolds Transport Theorem applied to the magnetic flux $2$-form $\beta = \star\vec B^\flat$,
> $$\frac{d\Phi}{dt} = \frac{d}{dt}\int_{S(t)}\beta = \int_{S(t)}\partial_t\beta + \int_{S(t)}\mathcal{L}_{\vec u}\beta.$$
>
> *Explicit-time-derivative term.* The differential Faraday law gives $\partial_t\beta = -\star(\nabla\times\vec E)^\flat$. Integrating and applying Kelvin–Stokes,
> $$\int_{S(t)}\partial_t\beta = -\int_{S(t)}\nabla\times\vec E\cdot d\vec A = -\oint_{\partial S(t)}\vec E\cdot d\vec\ell.$$
>
> *Lie-derivative term.* By Cartan's magic formula, $\mathcal{L}_{\vec u}\beta = d\iota_{\vec u}\beta + \iota_{\vec u}d\beta$. The second term vanishes because $d\beta = (\nabla\cdot\vec B)\,dV = 0$. The first term uses the form-language identity $\iota_{\vec u}(\star\vec B^\flat) = -(\vec u\times\vec B)^\flat$, so by Stokes's theorem,
> $$\int_{S(t)}\mathcal{L}_{\vec u}\beta = \int_{S(t)}d\iota_{\vec u}\beta = \oint_{\partial S(t)}\iota_{\vec u}\beta = -\oint_{\partial S(t)}(\vec u\times\vec B)\cdot d\vec\ell.$$
>
> *Collection.* Adding the two contributions,
> $$\frac{d\Phi}{dt} = -\oint_{\partial S(t)}\vec E\cdot d\vec\ell - \oint_{\partial S(t)}(\vec u\times\vec B)\cdot d\vec\ell = -\oint_{\partial S(t)}(\vec E + \vec u\times\vec B)\cdot d\vec\ell = -\mathcal{E}(t).$$
> The rest-frame electric field $\vec E_{\text{rest}} = \vec E + \vec u\times\vec B$ is recognized as the contribution to the EMF, including the motional component. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> A common error is to write $\frac{d\Phi}{dt} = \int_{S(t)}\partial_t\vec B\cdot d\vec A$ and conclude $\frac{d\Phi}{dt} = -\oint_{\partial S(t)}\vec E\cdot d\vec\ell$ via Stokes alone, ignoring the motional EMF. This is *incorrect* whenever $S(t)$ is moving — the moving boundary contributes the Lie-derivative term, which produces the motional $\vec u\times\vec B$ contribution. The error appears in elementary treatments where the surface is assumed stationary; for moving conductors (rotating loops, sliding bars on rails, induction motors), the motional EMF is essential and must come from the Lie-derivative term.

> [!note]- Sanity check via independent route
> Consider a square loop of wire in a uniform stationary magnetic field $\vec B = B_0\hat z$, with one side sliding at velocity $\vec u = u_0\hat x$ along the $x$-axis. The enclosed flux is $\Phi(t) = B_0\,L\,u_0 t$ (with $L$ the loop width in the $y$-direction), so $d\Phi/dt = B_0 L u_0$. The motional EMF in the sliding bar is $\mathcal{E} = -\oint(\vec u\times\vec B)\cdot d\vec\ell$. On the sliding bar, $\vec u\times\vec B = u_0 B_0(\hat x\times\hat z) = -u_0 B_0\hat y$, and $d\vec\ell$ on the bar is $\hat y\,L$, so the contribution is $-(-u_0 B_0)\cdot L = u_0 B_0 L$. The other three sides have either $\vec u = 0$ or $\vec u\parallel d\vec\ell$, so they contribute $0$. The total motional EMF is $\mathcal{E} = -u_0 B_0 L$, and indeed $\mathcal{E} = -d\Phi/dt$. The two methods agree, confirming the form-language derivation. The relativistic interpretation: in the rest frame of the bar, the electric field $\vec E' = \vec u\times\vec B$ produces a force on charges in the wire, driving the current.

---

# Key Takeaways

**The motional EMF $\vec u\times\vec B$ is the Lie-derivative term in Reynolds's theorem.** Faraday's law is one of the simplest physics applications of Reynolds's theorem, but the deep lesson is structural: the motional contribution to the EMF in a moving conductor is *not* a separate physical mechanism, it is the geometric correction Reynolds's theorem demands whenever the surface of integration is itself in motion. The trigger for recognizing this pattern is the phrase "moving boundary" or "moving conductor" combined with an integral conservation law — any time you see this combination, the Lie-derivative term will produce a "$\vec u\times($field$)$" line integral over the boundary that has the structural form of a motional correction. The reusable insight: whenever you derive a flux equation from a closed-form physical law, expect a moving-boundary correction proportional to $\vec u\times$(the dual field), and identify it geometrically via Cartan's formula before reaching for physical heuristics.

**Cartan's formula plus a closed form simplifies Reynolds dramatically.** The full Reynolds Transport Theorem has the Lie-derivative term $\mathcal{L}_{\vec u}\beta$, which is in general a complicated expression. But Cartan's formula $\mathcal{L}_X = d\iota_X + \iota_X d$ decomposes it into two pieces, and when $\beta$ is closed ($d\beta = 0$), the second piece vanishes and what remains is $d\iota_X\beta$ — which by Stokes is automatically a boundary integral. This is the pattern: *closed form + moving region $\to$ Lie-derivative term becomes a clean boundary flux*. This is exactly the situation for Faraday's law, where $d\beta = (\nabla\cdot\vec B)\,dV = 0$ kills the second term. The same pattern explains why Maxwell's equations in form language separate into one closed-form equation ($dF = 0$, which forces flux conservation under moving boundaries) and one source equation ($d\star F = J$, which is not as well-behaved). The trigger: a Bianchi identity (a closed-form equation $d\omega = 0$) combined with a Reynolds-type question always simplifies via this Cartan-plus-Stokes route.

**$dF = 0$ as a Bianchi identity unifies four classical laws.** The single statement $dF = 0$ in Minkowski $\mathbb{R}^{1,3}$ packages both $\nabla\cdot\vec B = 0$ (the $dt$-free part) and $\partial_t\vec B + \nabla\times\vec E = 0$ (the $dt$-containing part). These are two of the four Maxwell equations — the two that are *kinematic* (topological), in the sense that they encode the geometric fact that $F$ is the curvature of a connection $A$ ($F = dA$) on the electromagnetic $U(1)$-bundle, and any curvature automatically satisfies $dF = ddA = 0$ — the *Bianchi identity*. So the homogeneous Maxwell equations are not separate physical laws to be discovered; they are a single geometric identity. This is the central insight that unifies electromagnetism with gauge theory and that promotes electromagnetism from "two messy vector fields" to "the simplest example of a $U(1)$ connection." See **Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection** for the principal-bundle formulation.

**The form-language derivation is shorter than the classical one — and more general.** Compare the form-language derivation above (three steps: Reynolds, Cartan, Stokes) with the classical derivation in an undergraduate E&M textbook (separate cases for stationary and moving conductors, several pages of vector-calculus identities, ad-hoc motivation of the motional EMF). The form-language version is shorter because the geometric structure encoded in $\mathcal{L}_X$ — namely, "rate of change of integrated quantity under a flow" — is already the right object for the question. Spending effort to learn the form language pays back here as a 5-line proof of a result that takes 50 lines classically. More importantly, the form-language proof generalizes immediately to (i) Lorentzian manifolds, where it gives the *general-relativistic* version of Faraday's law in curved spacetime, (ii) non-abelian gauge groups, where it gives Yang–Mills Bianchi identities and their integral consequences, and (iii) higher-dimensional or more exotic settings (e.g. magnetic monopoles, instanton number conservation). Whenever the classical version of an electromagnetism identity feels ad hoc, recast it in form language and the right structure usually appears.
