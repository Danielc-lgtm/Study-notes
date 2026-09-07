---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Parallel Transport in a Principal Bundle"
  - "Thm - The Standard Connection on the Hopf Bundle"
  - "Thm - Existence and Uniqueness of Horizontal Lifts"
  - "Def - The Hopf Bundle"
  - "Ex - Curvature of the Standard Hopf Connection"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Consider the **Hopf bundle** $\pi\colon S^3\to S^2$ with structure group $U(1)$, carrying its standard connection $a$. Realise $S^3=\{(w_1,w_2)\in\mathbb{C}^2:|w_1|^2+|w_2|^2=1\}$, let $U(1)$ act on the right by the diagonal scalar multiplication $(w_1,w_2)\cdot e^{i\alpha}=(w_1e^{i\alpha},w_2e^{i\alpha})$, and take the Hopf projection onto the unit sphere $S^2\subset\mathbb{C}\times\mathbb{R}$,
$$\pi(w_1,w_2)=\big(2w_1\bar w_2,\ |w_1|^2-|w_2|^2\big).$$
The standard Hopf connection is the $\mathfrak{u}(1)$-valued one-form $a\in\Omega^1(S^3;i\mathbb{R})$ given, in terms of the real inner product $\langle\cdot,\cdot\rangle$ on $\mathbb{C}^2\cong\mathbb{R}^4$ and the fundamental vector field $v(z)=z\cdot i=(iz_1,iz_2)$ of $i\in\mathfrak{u}(1)$, by
$$a_z(u)=i\,\langle u,\,z\cdot i\rangle,\qquad z\in S^3,\ u\in T_zS^3,$$
whose kernel is the horizontal subspace $H_z=(z\cdot i)^{\perp}$.

Let $c$ be the equatorial great circle of $S^2$, the loop
$$c(\phi)=\big(e^{i\phi},\,0\big)\in S^2,\qquad \phi\in[0,2\pi],$$
which lies in the equator $\{(z,t)\in S^2:t=0\}$ where the real coordinate vanishes.

1. **(Horizontal lift.)** Lift $c$ horizontally to $S^3$, starting from $\tilde c(0)=\big(\tfrac1{\sqrt2},\tfrac1{\sqrt2}\big)\in S^3$. Solve the horizontality equation explicitly and write $\tilde c(\phi)$ in closed form.
2. **(Holonomy.)** Show that the lift does not close up: $\tilde c(2\pi)=-\tilde c(0)$. Deduce that the holonomy of the equatorial great circle is the group element $-1=e^{-i\pi}\in U(1)$; that is, parallel transport once around the equator rotates each Hopf fibre by a half-turn.
3. **(Comparison with the curvature flux.)** Confirm that this agrees with the flux of the curvature $F_a$ through a hemisphere bounded by the equator: the equator encloses *half* of the sphere, and $\int_{S^2}F_a=2\pi i$, so the enclosed flux is $\pi i$ and $\exp(-\pi i)=-1$. Note that the *sign* of the exponent depends on the choice of bounding hemisphere (orientation), while the holonomy $-1$ does not.

**Recall:**

The computation uses the standard Hopf connection, the horizontal-lift theorem, and the definition of holonomy through parallel transport; the comparison in part 3 uses the curvature of the Hopf connection and the abelian holonomy formula of §5.2.

![[Thm - Existence and Uniqueness of Horizontal Lifts#Statement]]

![[Def - Parallel Transport in a Principal Bundle#The Definition]]

For a loop $c$ based at $m\in S^2$ and a point $p\in P_m$, the horizontal lift closes up to $\tilde c(2\pi)=p\cdot g$ for a unique $g\in U(1)$, and this $g$ is the **holonomy** of $c$ at $p$; by equivariance of the lift it does not depend on which $p$ in the fibre is chosen (changing $p$ conjugates $g$, and $U(1)$ is abelian).

The **standard Hopf connection** (from [[Thm - The Standard Connection on the Hopf Bundle|the standard-connection theorem]]) is $a_z(u)=i\langle u,z\cdot i\rangle$ on $S^3\subset\mathbb{C}^2$, with $z\cdot i=(iz_1,iz_2)$ the fundamental field of $i\in\mathfrak{u}(1)=i\mathbb{R}$ and $\langle\cdot,\cdot\rangle$ the real inner product of $\mathbb{R}^4$; it is the unique connection whose horizontal space is $(z\cdot i)^{\perp}$, the orthogonal complement of the fibre direction. Concretely, writing $z=(x_0+ix_1,\,x_2+ix_3)\in\mathbb{C}^2\cong\mathbb{R}^4$, one has $z\cdot i=(-x_1,x_0,-x_3,x_2)$ and $a=i\,(-x_1\,dx_0+x_0\,dx_1-x_3\,dx_2+x_2\,dx_3)$.

The **curvature** of the Hopf connection (from [[Ex - Curvature of the Standard Hopf Connection|the Hopf-curvature exercise]]) is the two-form $F_a\in\Omega^2(S^2;i\mathbb{R})$ with $\pi^{*}F_a=da=2i\,(dx_0\wedge dx_1+dx_2\wedge dx_3)$; it is a constant positive multiple of the area form of the round base, and its total flux is
$$\int_{S^2}F_a=2\pi i.$$

> [!warning] Convention: normalisation of the base sphere
> This exercise uses the Hopf map $\pi(w_1,w_2)=(2w_1\bar w_2,|w_1|^2-|w_2|^2)$ onto the **unit** sphere $S^2\subset\mathbb{C}\times\mathbb{R}$. Haydys uses the map $z\mapsto(z_0\bar z_1,\tfrac12(|z_0|^2-|z_1|^2))$ onto the sphere of radius $\tfrac12$, and Bär uses a further rescaled stereographic normalisation. These choices differ only by a rescaling of the *base*; the connection $a$, the horizontal lift, and the holonomy all live on the total space $S^3$ and are computed there, so they are unaffected. Only the geometric statement "the equator bounds half the sphere" refers to the base, and that statement is invariant under rescaling. We take the loop orientation $\phi\colon0\to2\pi$ and orient a bounding surface by $\partial S=c$ (Stokes' convention).

---

# Convergent Strategy

**Problem class.** This is a *compute-a-holonomy-on-a-nontrivial-bundle* problem: the same machinery as the trivial-bundle drill, but on a bundle with no global section, where the interesting phenomenon — a contractible-looking loop with nontrivial holonomy — actually occurs. Its purpose is to exhibit the Hopf bundle's defining feature, that transport around a great circle is a half-turn ($-1$), and to connect the endpoint of a horizontal lift with the flux of curvature it encloses. The number $-1$ is the geometric origin of the double cover $S^3\to S^2$ and of the spin phenomenon "a $2\pi$ rotation acts by $-1$."

**Assumption pattern.** Two structural facts make the direct computation feasible. First, the fibres of the Hopf bundle are the $U(1)$-orbits $w\mapsto w\,e^{i\alpha}$, so *any* lift of a base curve is a chosen reference lift multiplied by a $U(1)$-valued function $e^{i\psi(\phi)}$; the unknown is the single scalar $\psi$. Second, the connection $a=i\langle\cdot,z\cdot i\rangle$ is written in ambient linear-algebra terms, so evaluating it on a velocity is a plain inner-product computation in $\mathbb{R}^4$. The recognisable trigger for "lift by solving one scalar equation" is again *abelian structure group*: for $U(1)$ the horizontality condition $a(\dot{\tilde c})=0$ becomes $\dot\psi=(\text{explicit function of }\phi)$.

**Theorem routing.** Choose a convenient (non-horizontal) reference lift $\sigma(\phi)$ of the equator; write the horizontal lift as $\tilde c(\phi)=\sigma(\phi)\cdot e^{i\psi(\phi)}$; impose $a(\dot{\tilde c})=0$ to get $\dot\psi=-\tfrac12$; integrate to $\psi(\phi)=-\phi/2$. Evaluate at $\phi=2\pi$: the vertical winding is $-\pi$, so the lift closes at $e^{-i\pi}\tilde c(0)=-\tilde c(0)$, and by the definition of [[Def - Parallel Transport in a Principal Bundle|holonomy]] the holonomy is $-1$. Independently, the abelian holonomy theorem of §5.2, [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|holonomy is the exponential of the enclosed curvature]], gives $\exp(-\int_S F_a)$; the enclosed flux is half of $\int_{S^2}F_a=2\pi i$, namely $\pi i$, and $\exp(-\pi i)=-1$ — the same answer, cross-checking the direct lift.

**Key decision point.** The one real choice is the *reference lift* $\sigma$. Picking $\sigma(\phi)=\big(\tfrac1{\sqrt2}e^{i\phi},\tfrac1{\sqrt2}\big)$ — a curve that manifestly projects to the equator and is easy to differentiate — turns the problem into solving $\dot\psi=-\tfrac12$. A poorer choice (say, an implicit section from a stereographic chart) would bury the computation in coordinate formulae. The subtle point to respect: the equator is a *closed geodesic* of the base and is contractible in $S^2$, yet its holonomy is nontrivial; this does *not* contradict the flat-connection theory because the Hopf connection is **not** flat — its curvature is nonzero, and a contractible loop sees the curvature it bounds.

---

# Legal Operations Used

The solution uses the following operations, corresponding on the §5.1 topic page to constructing and reading off horizontal lifts on a general principal bundle.

1. **Parametrise a lift on a $U(1)$-bundle as a reference lift times a phase.** Since fibres are $U(1)$-orbits, any lift of the base loop $c$ is $\tilde c(\phi)=\sigma(\phi)\cdot e^{i\psi(\phi)}$ for a fixed reference lift $\sigma$ and an unknown real function $\psi$; this reduces the vector unknown $\tilde c$ to the scalar $\psi$.

2. **Impose horizontality via the connection form and reduce to the fibre equation.** Evaluate $a(\dot{\tilde c})=0$; this is the reduction to equation $(2.9)$ of [[Thm - Existence and Uniqueness of Horizontal Lifts|the horizontal-lift theorem]], here yielding the scalar $\dot\psi=-\tfrac12$.

3. **Compute the connection on a velocity by the ambient inner product.** Because $a_z(u)=i\langle u,z\cdot i\rangle$, evaluating $a$ on $\dot{\tilde c}$ is an inner-product computation in $\mathbb{R}^4$; the terms combine to $i(\tfrac12+\dot\psi)$.

4. **Integrate the fibre equation and read the closing element.** Solve $\dot\psi=-\tfrac12$ with $\psi(0)=0$; evaluate at $\phi=2\pi$; the closing group element is the holonomy, by the definition of [[Def - Parallel Transport in a Principal Bundle|parallel transport]].

5. **Cross-check by the abelian holonomy–curvature formula.** Apply [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|the abelian holonomy theorem]] to the equator as the boundary of a hemisphere, using $\int_{S^2}F_a=2\pi i$ from [[Ex - Curvature of the Standard Hopf Connection|the Hopf-curvature exercise]].

---

# Hints

> [!note]- Hint 1
> The equator $c(\phi)=(e^{i\phi},0)$ is the image under the Hopf map of the curve $\sigma(\phi)=\big(\tfrac1{\sqrt2}e^{i\phi},\tfrac1{\sqrt2}\big)$ in $S^3$: check $\pi(\sigma(\phi))=(2\cdot\tfrac1{\sqrt2}e^{i\phi}\cdot\tfrac1{\sqrt2},\tfrac12-\tfrac12)=(e^{i\phi},0)$. But $\sigma$ is not horizontal. Write the horizontal lift as $\tilde c(\phi)=\sigma(\phi)\cdot e^{i\psi(\phi)}$ and find $\psi$.

> [!note]- Hint 2
> The horizontal condition is $a(\dot{\tilde c})=0$, i.e. $\langle\dot{\tilde c},\tilde c\cdot i\rangle=0$. Writing $\tilde c=(u_1,u_2)$ with $u_1=\tfrac1{\sqrt2}e^{i(\phi+\psi)}$, $u_2=\tfrac1{\sqrt2}e^{i\psi}$, use $\dot u_k=i(\cdots)u_k$ and $|u_k|^2=\tfrac12$. You should find $a(\dot{\tilde c})=i\,(\tfrac12+\dot\psi)$. What is $\psi$?

> [!note]- Hint 3
> $\dot\psi=-\tfrac12$, so $\psi(\phi)=-\phi/2$. Evaluate $\tilde c$ at $\phi=0$ and $\phi=2\pi$: the phase $e^{i\psi}$ has advanced by $e^{-i\pi}=-1$. What does $\tilde c(2\pi)=-\tilde c(0)$ say about the holonomy?

> [!note]- Hint 4
> For the curvature check: the equator bounds a hemisphere carrying half the total flux, and $\int_{S^2}F_a=2\pi i$, so the enclosed flux is $\pi i$. The abelian holonomy theorem gives $\exp(-\pi i)=-1$. Why does swapping to the other hemisphere (flux $-\pi i$) still give $-1$?

---

# Solution

The plan is a direct horizontal lift. The fibres of the Hopf bundle are the $U(1)$-orbits, so we write the lift of the equator as an explicit reference curve times a phase $e^{i\psi(\phi)}$, impose that the connection form annihilates its velocity, and find the single scalar equation $\dot\psi=-\tfrac12$. Integrating over the full loop advances the phase by $e^{-i\pi}=-1$, so the lift closes at the antipode and the holonomy is $-1$; the abelian holonomy theorem then confirms this is the exponential of the curvature flux through the enclosed hemisphere.

**Step 0: A reference lift of the equator and the phase ansatz.**

The equator is the image of $\sigma(\phi)=\big(\tfrac1{\sqrt2}e^{i\phi},\tfrac1{\sqrt2}\big)$, and every lift is $\sigma\cdot e^{i\psi}$.

> [!note]- Derivation
> Define $\sigma\colon[0,2\pi]\to S^3$ by $\sigma(\phi)=\big(\tfrac1{\sqrt2}e^{i\phi},\tfrac1{\sqrt2}\big)$; it lands in $S^3$ because $|\tfrac1{\sqrt2}e^{i\phi}|^2+|\tfrac1{\sqrt2}|^2=\tfrac12+\tfrac12=1$. Its Hopf projection is
> $$\pi(\sigma(\phi))=\Big(2\cdot\tfrac1{\sqrt2}e^{i\phi}\cdot\overline{\tfrac1{\sqrt2}},\ \big|\tfrac1{\sqrt2}e^{i\phi}\big|^2-\big|\tfrac1{\sqrt2}\big|^2\Big)=\big(e^{i\phi},\,0\big)=c(\phi)\qquad(\text{Hopf map on }\sigma),$$
> so $\sigma$ is a lift of the equator $c$. Because $\pi^{-1}(c(\phi))$ is the $U(1)$-orbit of $\sigma(\phi)$, **every** lift of $c$ has the form
> $$\tilde c(\phi)=\sigma(\phi)\cdot e^{i\psi(\phi)}=\Big(\tfrac1{\sqrt2}e^{i(\phi+\psi(\phi))},\ \tfrac1{\sqrt2}e^{i\psi(\phi)}\Big)\qquad(\text{lifts differ by a }U(1)\text{-valued phase}),$$
> for a smooth real function $\psi$ with, for our chosen starting point $\tilde c(0)=\big(\tfrac1{\sqrt2},\tfrac1{\sqrt2}\big)=\sigma(0)$, the initial value $\psi(0)=0$. It remains to pin down $\psi$ by horizontality.

**Step 1: Horizontality forces $\dot\psi=-\tfrac12$, hence $\psi(\phi)=-\phi/2$.**

Evaluating the connection form on $\dot{\tilde c}$ gives $a(\dot{\tilde c})=i(\tfrac12+\dot\psi)$, so horizontality is $\dot\psi=-\tfrac12$.

> [!note]- Derivation
> Write $\tilde c=(u_1,u_2)$ with $u_1=\tfrac1{\sqrt2}e^{i(\phi+\psi)}$ and $u_2=\tfrac1{\sqrt2}e^{i\psi}$; note $|u_1|^2=|u_2|^2=\tfrac12$. Differentiating in $\phi$,
> $$\dot u_1=i\,(1+\dot\psi)\,u_1,\qquad \dot u_2=i\,\dot\psi\,u_2\qquad(\text{chain rule on the exponentials}).$$
> The fundamental field at $\tilde c$ is $\tilde c\cdot i=(iu_1,iu_2)$. The standard Hopf connection is $a_z(u)=i\langle u,z\cdot i\rangle$ with $\langle\cdot,\cdot\rangle$ the real inner product on $\mathbb{C}^2\cong\mathbb{R}^4$, and for complex coordinates $\langle u,w\rangle=\operatorname{Re}\!\big(u_1\bar w_1+u_2\bar w_2\big)$. Hence
> $$a(\dot{\tilde c})=i\,\langle\dot{\tilde c},\,\tilde c\cdot i\rangle=i\,\operatorname{Re}\!\big(\dot u_1\,\overline{iu_1}+\dot u_2\,\overline{iu_2}\big)\qquad(\text{definition of }a\text{, real inner product}).$$
> Evaluate each term using $\overline{iu_k}=-i\,\bar u_k$:
> $$\dot u_1\,\overline{iu_1}=i(1+\dot\psi)u_1\cdot(-i)\bar u_1=(1+\dot\psi)\,|u_1|^2=\tfrac12(1+\dot\psi)\qquad(i\cdot(-i)=1,\ |u_1|^2=\tfrac12),$$
> $$\dot u_2\,\overline{iu_2}=i\,\dot\psi\,u_2\cdot(-i)\bar u_2=\dot\psi\,|u_2|^2=\tfrac12\,\dot\psi\qquad(\text{same computation}).$$
> Both are real, so the real part is their sum:
> $$a(\dot{\tilde c})=i\Big(\tfrac12(1+\dot\psi)+\tfrac12\dot\psi\Big)=i\Big(\tfrac12+\dot\psi\Big)\qquad(\text{adding the two terms}).$$
> By the definition of the [[Def - Horizontal Subspace and Horizontal Lift|horizontal subspace]], $\dot{\tilde c}(\phi)\in H_{\tilde c(\phi)}=\ker a$ if and only if $a(\dot{\tilde c})=0$, that is
> $$\dot\psi(\phi)=-\tfrac12\qquad(\text{horizontality}).$$
> This is precisely the reduction to the fibre equation $(2.9)$ guaranteed by [[Thm - Existence and Uniqueness of Horizontal Lifts|the horizontal-lift theorem]], now an explicit constant. With $\psi(0)=0$,
> $$\psi(\phi)=-\tfrac{\phi}{2}\qquad(\text{integrating }\dot\psi=-\tfrac12),$$
> so the horizontal lift is
> $$\boxed{\;\tilde c(\phi)=\Big(\tfrac1{\sqrt2}e^{i(\phi-\phi/2)},\ \tfrac1{\sqrt2}e^{-i\phi/2}\Big)=\Big(\tfrac1{\sqrt2}e^{i\phi/2},\ \tfrac1{\sqrt2}e^{-i\phi/2}\Big).\;}$$
> By uniqueness in [[Thm - Existence and Uniqueness of Horizontal Lifts|the lift theorem]], this is *the* horizontal lift through $\tilde c(0)$.

**Step 2: The lift closes at the antipode; the holonomy is $-1$.**

Evaluating at $\phi=2\pi$ gives $\tilde c(2\pi)=-\tilde c(0)=\tilde c(0)\cdot(-1)$, so the holonomy is $-1=e^{-i\pi}$.

> [!note]- Derivation
> At the endpoints of the loop,
> $$\tilde c(0)=\Big(\tfrac1{\sqrt2},\ \tfrac1{\sqrt2}\Big),\qquad \tilde c(2\pi)=\Big(\tfrac1{\sqrt2}e^{i\pi},\ \tfrac1{\sqrt2}e^{-i\pi}\Big)=\Big(-\tfrac1{\sqrt2},\ -\tfrac1{\sqrt2}\Big)\qquad(e^{\pm i\pi}=-1).$$
> Thus $\tilde c(2\pi)=-\tilde c(0)$. Writing this as an action of $U(1)$ on the fibre, $-\tilde c(0)=\tilde c(0)\cdot(-1)$ with $-1=e^{i\pi}=e^{-i\pi}\in U(1)$. By the definition of [[Def - Parallel Transport in a Principal Bundle|parallel transport]] and holonomy, the holonomy $g$ of the equator at $\tilde c(0)$ is the unique element with $\tilde c(2\pi)=\tilde c(0)\cdot g$, so
> $$\boxed{\;g=-1=e^{-i\pi}\in U(1).\;}$$
> Because $U(1)$ is abelian, the holonomy does not depend on the base point in the fibre (changing $\tilde c(0)$ to $\tilde c(0)\cdot e^{i\beta}$ conjugates $g$ by $e^{i\beta}$, which fixes it), so this is *the* holonomy of the equator. Geometrically: transporting a Hopf fibre once around the equatorial great circle returns it rotated by a half-turn. This is the concrete origin of the fact that $S^3\to S^2$ is a *nontrivial* $U(1)$-bundle: a trivial bundle has trivial holonomy on contractible loops, whereas here a contractible loop already transports by $-1$.

**Step 3: Agreement with the curvature flux through a hemisphere.**

The abelian holonomy theorem gives $g=\exp(-\int_S F_a)$ for a bounding hemisphere $S$; the enclosed flux is $\pi i$, and $\exp(-\pi i)=-1$.

> [!note]- Derivation
> The equator $c$ lies in the base and bounds a hemisphere $S$ (the surface with $\partial S=c$). By [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|the abelian holonomy theorem]] — *for an abelian structure group, the holonomy of a loop bounding a compact oriented surface $S$ with $\partial S=c$ in a trivialising set is $\operatorname{hol}(c)=\exp\!\big(-\int_S F\big)$, with $F$ the base curvature* — we have
> $$g=\exp\!\Big(-\int_S F_a\Big)\qquad(\text{abelian holonomy formula}).$$
> The curvature $F_a$ is, by [[Ex - Curvature of the Standard Hopf Connection|the Hopf-curvature exercise]], a constant positive multiple of the round area form, with total flux $\int_{S^2}F_a=2\pi i$. Since $F_a$ is proportional to the area form, its flux through a hemisphere is exactly half the total:
> $$\int_S F_a=\tfrac12\int_{S^2}F_a=\tfrac12\,(2\pi i)=\pi i\qquad(\text{uniform density, half the area}).$$
> Therefore
> $$g=\exp(-\pi i)=-1,$$
> in agreement with the direct computation of Step 2. **Sign and orientation.** If instead we bound the equator by the opposite hemisphere $S'$, then $\partial S'=c$ forces the opposite orientation on $S'$ relative to the outward normal, so $\int_{S'}F_a=-\pi i$ and $g=\exp(-(-\pi i))=\exp(\pi i)=-1$. The two hemispheres give exponents $\pm\pi i$ of opposite sign — consistent with the total flux $2\pi i$ splitting as $\pi i+(- \pi i)$ once boundary orientations are accounted for — yet both yield the holonomy $-1$, because $e^{i\pi}=e^{-i\pi}$. This is why the answer $-1$ is orientation-independent even though the sign of the exponent is not.

> [!note]- Complete formal solution
> **Setup.** The Hopf bundle is $\pi\colon S^3\to S^2$, $\pi(w_1,w_2)=(2w_1\bar w_2,|w_1|^2-|w_2|^2)$, with the standard connection $a_z(u)=i\langle u,z\cdot i\rangle$, $z\cdot i=(iz_1,iz_2)$. The equator is $c(\phi)=(e^{i\phi},0)$, $\phi\in[0,2\pi]$.
>
> **Lift.** The curve $\sigma(\phi)=\big(\tfrac1{\sqrt2}e^{i\phi},\tfrac1{\sqrt2}\big)$ lies in $S^3$ and satisfies $\pi\circ\sigma=c$, so every lift is $\tilde c(\phi)=\sigma(\phi)\,e^{i\psi(\phi)}=\big(\tfrac1{\sqrt2}e^{i(\phi+\psi)},\tfrac1{\sqrt2}e^{i\psi}\big)$, with $\psi(0)=0$ fixing $\tilde c(0)=\big(\tfrac1{\sqrt2},\tfrac1{\sqrt2}\big)$. Writing $u_1=\tfrac1{\sqrt2}e^{i(\phi+\psi)}$, $u_2=\tfrac1{\sqrt2}e^{i\psi}$, we have $\dot u_1=i(1+\dot\psi)u_1$, $\dot u_2=i\dot\psi u_2$, $|u_1|^2=|u_2|^2=\tfrac12$, and
> $$a(\dot{\tilde c})=i\operatorname{Re}\big(\dot u_1\overline{iu_1}+\dot u_2\overline{iu_2}\big)=i\big(\tfrac12(1+\dot\psi)+\tfrac12\dot\psi\big)=i\big(\tfrac12+\dot\psi\big).$$
> Horizontality $a(\dot{\tilde c})=0$ gives $\dot\psi=-\tfrac12$, so $\psi(\phi)=-\phi/2$ and
> $$\tilde c(\phi)=\Big(\tfrac1{\sqrt2}e^{i\phi/2},\ \tfrac1{\sqrt2}e^{-i\phi/2}\Big).$$
> By existence and uniqueness in [[Thm - Existence and Uniqueness of Horizontal Lifts|the horizontal-lift theorem]], this is the horizontal lift.
>
> **Holonomy.** $\tilde c(2\pi)=\big(\tfrac1{\sqrt2}e^{i\pi},\tfrac1{\sqrt2}e^{-i\pi}\big)=-\tilde c(0)=\tilde c(0)\cdot(-1)$, so the holonomy is $g=-1=e^{-i\pi}\in U(1)$; since $U(1)$ is abelian it is independent of the chosen base point in the fibre.
>
> **Curvature check.** By [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|the abelian holonomy theorem]], $g=\exp(-\int_S F_a)$ for a hemisphere $S$ with $\partial S=c$. As $F_a$ is a constant multiple of the round area form with $\int_{S^2}F_a=2\pi i$, the hemisphere flux is $\pi i$, so $g=\exp(-\pi i)=-1$, matching the direct computation. The opposite hemisphere gives exponent $+\pi i$ and the same value $-1$. $\blacksquare$

> [!note]- Alternative route through the local form $A_1$ (base-integral computation)
> The lift can also be run in the trivialisation given by the local section $s_1$ of the Hopf bundle over $U_1=S^2\setminus\{\text{south pole}\}$, which contains the equator. There the horizontal lift's fibre factor is $\exp\!\big(-\int_c A_1\big)$, where $A_1=s_1^{*}a$ is the local connection form computed in [[Ex - Connection Forms of the Hopf Connection in the Two Local Sections|the two-sections exercise]]. Since $dA_1=F_a$ on $U_1$ and the northern hemisphere cap lies in $U_1$, Stokes' theorem gives $\int_c A_1=\int_{\text{cap}}dA_1=\int_{\text{cap}}F_a=\pi i$, so the fibre factor is $e^{-\pi i}=-1$ — the same holonomy, now obtained by integrating the potential over the base rather than lifting on $S^3$. The two routes are the abelian holonomy theorem read in the two directions.

---

# Key Takeaways

**On a nontrivial bundle a horizontal lift is a reference lift times a phase, and the phase solves a single scalar equation.** The organising move here is to write $\tilde c=\sigma\cdot e^{i\psi}$ for a convenient reference lift $\sigma$ of the base curve, reducing the vector-valued unknown to the scalar $\psi$ and turning horizontality $a(\dot{\tilde c})=0$ into an ordinary differential equation for $\psi$. This works verbatim on any $U(1)$-bundle and, with $e^{i\psi}$ replaced by a $G$-valued curve, on any principal bundle; the only change for a non-abelian $G$ is that the equation becomes matrix-valued and its solution is a path-ordered exponential. The trigger to reach for this ansatz is a request to transport along a curve on a bundle where no global section is available: pick any local lift you can differentiate, absorb the failure of its velocity to be horizontal into the phase, and solve. The Hopf computation is the smallest example in which the bundle is genuinely nontrivial and the technique still gives a closed-form answer.

**A contractible loop can have nontrivial holonomy exactly when the connection is not flat, and the holonomy is the curvature it encloses.** The equator is contractible in $S^2$, yet its holonomy is $-1$; this is not a paradox but the defining symptom of nonzero curvature. The abelian holonomy theorem makes the relationship exact: the holonomy is $\exp(-\int_S F_a)$ over any bounding surface, so a loop encircling flux transports nontrivially. Here the flux through a hemisphere is $\pi i$, half of the total Chern flux $2\pi i=2\pi i\cdot c_1$ of the Hopf line bundle, and the resulting holonomy $-1$ is the "half" of the full $2\pi$ phase that a complete sphere would accumulate. The diagnostic to remember: whenever a small or contractible loop transports nontrivially, look for the curvature it bounds; whenever it transports trivially for *every* contractible loop, the connection is flat and only the topology of the loop matters. The trivial-bundle companion [[Ex - Horizontal Lifts in the Trivial Bundle with a Constant Connection]] shows both faces of this — a flat potential with trivial holonomy and a curved one with holonomy $e^{-i}$.

**The half-turn $-1$ is the geometric seed of the double cover and of spin.** That transport once around a great circle returns the fibre rotated by $\pi$, not $2\pi$, is the same fact as the two-to-one nature of $S^3\to S^2$ and, one dimension up, of $\operatorname{Spin}(n)\to SO(n)$: a full $2\pi$ rotation in the base is realised upstairs by a path from a point to its antipode, and only a $4\pi$ rotation closes up. The Hopf holonomy $-1$ is where this first becomes a computation rather than a picture, and it recurs throughout gauge theory and quantum mechanics: it is the phase behind the Aharonov–Bohm effect for a flux of half a quantum, the sign in the spin-statistics connection, and the reason a spin-$\tfrac12$ state changes sign under a $2\pi$ rotation. When a later problem asks why some transport or monodromy is $-1$ rather than $+1$, the reflex should be to look for an enclosed half-flux or an antipodal lift of exactly this kind. The latitude-circle variant [[Ex - Holonomy of the Hopf Connection around a Latitude Circle]] interpolates between the two poles and recovers this equatorial case at the halfway height.
