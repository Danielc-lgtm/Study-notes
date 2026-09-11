---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral"
  - "Ex - Curvature of the Standard Hopf Connection"
  - "Thm - The Standard Connection on the Hopf Bundle"
  - "Def - Holonomy Group of a Connection"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles"
  - "Thm - Stokes' Theorem on Manifolds"
tags: [geometry, gauge-theory, holonomy, hopf-bundle]
---

# Problem Statement

Let $\pi\colon S^3\to S^2$ be the Hopf bundle with its standard $U(1)$-connection $a$, the connection whose horizontal space at each point is the orthogonal complement of the fibre direction. Work in the concrete model of the base used in the curvature computation: the quotient $S^3/U(1)$ is isometric to the round sphere $S^2_{1/2}$ of radius $\tfrac12$ sitting in $\mathbb{R}^3=\mathbb{C}\times\mathbb{R}$, and the curvature of the Hopf connection descends to the base as the two-form
$$F_a=2i\,\operatorname{vol}_{S^2_{1/2}}\in\Omega^2\!\big(S^2;\,i\mathbb{R}\big),\qquad \int_{S^2}F_a=2\pi i,$$
where $\operatorname{vol}_{S^2_{1/2}}$ is the area form of the round metric of radius $\tfrac12$ and $i\mathbb{R}=\mathfrak{u}(1)$ is the Lie algebra of $U(1)$. Parametrise the base by its **height** $t$ (the last coordinate in $\mathbb{R}^3$) and its **longitude** $\phi$, so that $t\in\big(-\tfrac12,\tfrac12\big)$ and $\phi\in\mathbb{R}/2\pi\mathbb{Z}$.

For a fixed height $t\in\big(-\tfrac12,\tfrac12\big)$ let $c_t$ be the **latitude circle at height $t$**,
$$c_t\colon[0,2\pi]\to S^2,\qquad c_t(\phi)=\text{the point of }S^2_{1/2}\text{ at height }t\text{ and longitude }\phi,$$
traversed once in the direction of increasing longitude. Fix a point $p\in S^3$ over $c_t(0)$.

**Compute the holonomy $\operatorname{hol}_p(c_t)\in U(1)$ of the Hopf connection around $c_t$.** Show that it equals $\exp\!\big(-\int_{S^-}F_a\big)$, where $S^-=\{h\le t\}$ is the spherical cap below the circle, evaluate the integral explicitly from the curvature form, and obtain
$$\operatorname{hol}_p(c_t)=\exp\!\Big(-2\pi i\big(t+\tfrac12\big)\Big)=-\,e^{-2\pi i t}.$$
Interpret the answer as $\exp\big(-i\cdot(\text{normalised area})\big)$, exhibit the two limiting cases (the loop shrinking to either pole), and compare the result both with the great-circle computation of §5.1 and with the Riemannian spherical-cap holonomy of the tangent bundle.

**Recall:**

The result we route the computation through is the abelian holonomy formula; its exact statement, transcluded from its own page, is:

![[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral#Statement]]

In words: for an **abelian** structure group $G$ (here $G=U(1)$), and a piecewise smooth loop $c$ that lies inside one trivialising open set $U_\alpha$ on which a local section defines the local connection form $A_\alpha=s_\alpha^*\omega$, the holonomy is the exponential of minus the line integral of the potential, $\operatorname{hol}(c)=\exp\!\big(-\oint_c A_\alpha\big)$; and when in addition $c$ bounds a compact oriented surface $S\subset U_\alpha$ with $\partial S=c$, Stokes' theorem converts this to $\operatorname{hol}(c)=\exp\!\big(-\int_S F\big)$ with $F=dA_\alpha$ the (globally defined) curvature. The mechanism is that for a commuting-valued potential the path-ordered exponential collapses to an ordinary exponential of the integral, because there is no ordering obstruction.

![[Def - Holonomy Group of a Connection#The Definition]]

The curvature form we use is computed on its own page; its result, which we take as given here, is:

The standard Hopf connection $a=\big(-x_1\,dx_0+x_0\,dx_1-x_3\,dx_2+x_2\,dx_3\big)i$ on $S^3\subset\mathbb{R}^4$ has $\pi^*F_a=da=2i\,(dx_0\wedge dx_1+dx_2\wedge dx_3)$, and under the isometry $S^3/U(1)\cong S^2_{1/2}$ this descends to $F_a=2i\,\operatorname{vol}_{S^2_{1/2}}$ with $\int_{S^2}F_a=2\pi i$ (see [[Ex - Curvature of the Standard Hopf Connection]] and [[Thm - The Standard Connection on the Hopf Bundle]]).

> [!warning] Convention: sign of the holonomy formula and orientation of the base
> We use the series conventions ($\mathfrak{u}(1)=i\mathbb{R}$; a $U(1)$-connection form is $\mathfrak{u}(1)$-valued; curvature of a Hermitian line bundle is $i$-real-valued). The abelian holonomy formula carries a minus sign, $\operatorname{hol}(c)=\exp(-\int_S F)$, inherited from the parallel-transport equation $\dot v=-A(\dot c)\,v$. The base $S^2$ carries the orientation for which $\int_{S^2}F_a=+2\pi i$; equivalently, in the height–longitude chart the pair $(\partial_t,\partial_\phi)$ is positively oriented, so that Stokes' theorem sends the boundary of the lower cap $S^-=\{h\le t\}$ to the latitude circle traversed with **increasing** longitude, which is exactly the orientation of $c_t$ fixed above.

---

# Convergent Strategy

**Problem class.** This is a *compute-a-holonomy-of-a-line-bundle* problem: a loop is given on the base of a principal $U(1)$-bundle carrying a specified connection, and we want the single group element in $U(1)$ by which parallel transport around the loop fails to return the fibre to itself. The defining feature of the class is that the structure group is abelian, so the entire ordered-transport machinery collapses and the answer is an exponential of an integral. The only real work is turning the abstract $\int_S F$ into an honest number using the explicit curvature form and the geometry of the region the loop bounds.

**Assumption pattern.** Two hypotheses do all the work. First, $U(1)$ is **abelian**: this is what licenses replacing the path-ordered exponential by $\exp$ of the ordinary integral, and hence what makes [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|the abelian holonomy formula]] applicable. Second, the latitude circle $c_t$ **bounds a cap** inside a single trivialising set: the base minus one pole is diffeomorphic to a disc, a trivialising set for the Hopf bundle, and it contains both $c_t$ and the cap $S^-$ below it, so the surface-integral form of the formula applies. Without a bounding surface inside a trivialising set — for instance for a non-contractible loop on a torus — one would have to fall back on the line-integral $\oint_c A_\alpha$ directly, which is the situation of the companion exercise [[Ex - Holonomy of a Constant Connection on the Trivial Bundle over the Torus]].

**Theorem routing.** The route is short and forced: (i) recall from [[Ex - Curvature of the Standard Hopf Connection|the Hopf curvature exercise]] that $F_a=2i\,\operatorname{vol}_{S^2_{1/2}}$; (ii) express $\operatorname{vol}_{S^2_{1/2}}$ in the height–longitude chart, where Archimedes' theorem gives the clean form $\operatorname{vol}_{S^2_{1/2}}=\tfrac12\,dt\wedge d\phi$, so that $F_a=i\,dt\wedge d\phi$; (iii) apply [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|the abelian holonomy formula]] with $S=S^-$ the cap below $c_t$; (iv) integrate $F_a$ over $S^-$ and exponentiate. A second, independent evaluation through the line integral $\oint_{c_t}A_S$ of an explicit local potential $A_S$ with $dA_S=F_a$ serves as the consistency check.

**Key decision point.** The one genuinely non-obvious move is the choice of which cap to integrate over, and the recognition that the choice does not affect the answer. The circle $c_t$ bounds *two* caps, the northern $S^+=\{h\ge t\}$ and the southern $S^-=\{h\le t\}$, with opposite induced orientations; the abelian formula applied to each must give the same holonomy, and it does precisely because the two integrals differ by $\int_{S^2}F_a=2\pi i$, and $\exp(-2\pi i)=1$. Seeing that the total flux $2\pi i$ is exactly a full period of $\exp\colon i\mathbb{R}\to U(1)$ is the conceptual content: it is the integrality of the first Chern number of the Hopf bundle, read off as the well-definedness of the holonomy.

---

# Legal Operations Used

1. **Reduce an abelian holonomy to a curvature flux (the operation "for a commuting connection, transport is the exponential of the integral").** Because $U(1)$ is abelian, parallel transport around $c_t$ is $\exp\big(-\oint_{c_t}A\big)$, and Stokes converts the line integral of the potential over the boundary into the surface integral of the curvature over the cap. This is the operation applied on [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|the abelian holonomy page]]; here the connection is the Hopf connection and the surface is the spherical cap $S^-$.

2. **Trivialise over the base minus a pole.** The base $S^2$ minus the north pole is diffeomorphic to a plane, hence contractible, hence a trivialising set for the bundle; the section over it defines the local potential $A_S$ and makes both $c_t$ and $S^-$ live inside one $U_\alpha$, which is the hypothesis the abelian formula requires.

3. **Convert an area form on a sphere to Cartesian height–longitude coordinates (Archimedes' projection).** The round area form of $S^2_{1/2}$ is $\tfrac12\,dt\wedge d\phi$ because the radial projection of a sphere onto its circumscribing cylinder preserves area; this turns the flux integral into an elementary double integral.

4. **Use the exponential's periodicity to check consistency across the two caps.** The northern and southern evaluations agree because they differ by the total flux $\int_{S^2}F_a=2\pi i$, and $2\pi i$ lies in the kernel $2\pi i\mathbb{Z}$ of $\exp\colon i\mathbb{R}\to U(1)$; this is the operation "read a curvature integral modulo the period lattice", used throughout the abelian theory.

---

# Hints

> [!note]- Hint 1
> The structure group is $U(1)$, which is abelian. Do not attempt to solve the transport ODE directly or to compute a path-ordered exponential. Instead reach for the one theorem that trivialises abelian holonomy: the holonomy of a loop bounding a surface is $\exp$ of minus the flux of the curvature through that surface. What surface does the latitude circle bound, and does it lie inside a single trivialising set?

> [!note]- Hint 2
> Recall the curvature from [[Ex - Curvature of the Standard Hopf Connection]]: on the base $S^2_{1/2}$ it is $F_a=2i\,\operatorname{vol}$, where $\operatorname{vol}$ is the round area form of the radius-$\tfrac12$ sphere. You now need $\operatorname{vol}$ in coordinates. On a sphere of radius $R$, height $z$ and longitude $\phi$, the area form is $\operatorname{vol}=R\,dz\wedge d\phi$ — this is Archimedes' hat-box theorem (the projection to the circumscribing cylinder is area-preserving). Substitute $R=\tfrac12$.

> [!note]- Hint 3
> With $F_a=i\,dt\wedge d\phi$, integrate over the cap $S^-=\{h\le t\}$: this is $\{(t',\phi):-\tfrac12\le t'\le t,\ 0\le\phi<2\pi\}$. The integral is elementary. Then the holonomy is $\exp$ of minus that integral. Do not forget the minus sign in the abelian formula.

> [!note]- Hint 4
> You should find $\int_{S^-}F_a=2\pi i\big(t+\tfrac12\big)$, hence $\operatorname{hol}(c_t)=\exp\big(-2\pi i(t+\tfrac12)\big)=-e^{-2\pi it}$. Check it two ways: (a) as $t\to\pm\tfrac12$ the loop shrinks to a pole and the holonomy must become $1$; (b) at $t=0$ (the equator, a great circle) you must recover the value $-1$ of the §5.1 great-circle exercise. Both hold.

---

# Solution

The plan is to reduce the holonomy to a curvature flux by the abelian formula, then to evaluate that flux by writing the curvature in height–longitude coordinates where it is simply $i\,dt\wedge d\phi$. The whole computation happens inside the trivialising set $S^2\setminus\{N\}$ (the base minus the north pole), which contains both the loop $c_t$ and the cap $S^-$ it bounds. After the main derivation we verify the answer independently through a local potential, and by the two shrinking-loop limits and the equatorial case.

**Step 1: Set up the trivialising chart and the height–longitude coordinates.**

The base minus the north pole is a trivialising set carrying a section $s$, and in the height–longitude coordinates $(t,\phi)$ the Hopf curvature is $F_a=i\,dt\wedge d\phi$.

> [!note]- Derivation
> Let $N\in S^2_{1/2}$ be the north pole (height $t=\tfrac12$) and $U=S^2\setminus\{N\}$. The stereographic projection from $N$ is a diffeomorphism $U\to\mathbb{R}^2$, so $U$ is contractible; by [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|the homotopy-invariance theorem]] — every principal bundle over a contractible manifold is trivial — the restriction $\pi^{-1}(U)\to U$ is trivial, and hence by [[Thm - Sections of a Principal Bundle and Triviality|the triviality criterion]] (a principal bundle is trivial if and only if it admits a global section) $U$ is a trivialising set carrying a global section $s\colon U\to S^3$. The latitude circle $c_t$ (for $t<\tfrac12$) and the closed southern cap $S^-=\{h\le t\}$ both lie in $U$; this is what the abelian holonomy formula will require.
>
> On $U\setminus\{S\}$ (also removing the south pole $S$, height $t=-\tfrac12$, so that longitude is defined) use as coordinates the height $t\in(-\tfrac12,\tfrac12)$ and the longitude $\phi\in\mathbb{R}/2\pi\mathbb{Z}$. Concretely a point of $S^2_{1/2}\subset\mathbb{R}^3$ with these coordinates is
> $$\Big(\sqrt{\tfrac14-t^2}\,\cos\phi,\ \sqrt{\tfrac14-t^2}\,\sin\phi,\ t\Big).$$
> The two tangent vectors $\partial_\phi$ and $\partial_t$ are orthogonal, with
> $$\lvert\partial_\phi\rvert=\sqrt{\tfrac14-t^2},\qquad \lvert\partial_t\rvert=\frac{1/2}{\sqrt{\tfrac14-t^2}}\qquad(\text{by differentiating the parametrisation and using }|\partial_t|^2=\tfrac{t^2}{\tfrac14-t^2}+1),$$
> so the round area form is
> $$\operatorname{vol}_{S^2_{1/2}}=\lvert\partial_t\rvert\,\lvert\partial_\phi\rvert\;dt\wedge d\phi=\sqrt{\tfrac14-t^2}\cdot\frac{1/2}{\sqrt{\tfrac14-t^2}}\;dt\wedge d\phi=\tfrac12\,dt\wedge d\phi\qquad(\text{the radius-}R\text{ area form is }R\,dz\wedge d\phi,\ R=\tfrac12).$$
> This is Archimedes' hat-box theorem: on a sphere of radius $R$ the area between two horizontal planes depends only on their separation, because the projection to the circumscribing cylinder preserves area. Consequently, using the recalled curvature $F_a=2i\,\operatorname{vol}_{S^2_{1/2}}$,
> $$F_a=2i\cdot\tfrac12\,dt\wedge d\phi=i\,dt\wedge d\phi\qquad(\text{substituting the area form}).$$
> As a check on the orientation and the constant, $\int_{S^2}F_a=i\int_{-1/2}^{1/2}\!\!\int_0^{2\pi}dt\,d\phi=i\cdot 1\cdot 2\pi=2\pi i$, which is the value recorded on the curvature page; so the pair $(\partial_t,\partial_\phi)$ is positively oriented, consistent with the convention callout.

**Step 2: Reduce the holonomy to the flux of $F_a$ through the southern cap.**

Because $U(1)$ is abelian and $c_t=\partial S^-$ with $S^-\subset U$, the abelian holonomy formula gives $\operatorname{hol}_p(c_t)=\exp\big(-\int_{S^-}F_a\big)$.

> [!note]- Derivation
> The structure group $U(1)$ is abelian, and by Step 1 the loop $c_t$ lies in the trivialising set $U=S^2\setminus\{N\}$ and bounds the compact oriented surface $S^-=\{h\le t\}\subset U$ with $\partial S^-=c_t$ (with the boundary orientation induced by the outward-normal-first convention: the outward normal of $S^-$ at its rim points in the $+\partial_t$ direction, and since $(\partial_t,\partial_\phi)$ is positive the induced rim orientation is $+\partial_\phi$, i.e. increasing longitude — exactly the orientation of $c_t$). All hypotheses of [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|the abelian holonomy formula]] are therefore met: $G$ abelian, $c_t$ a loop in $U_\alpha$, $S^-\subset U_\alpha$ a surface with $\partial S^-=c_t$. The formula yields
> $$\operatorname{hol}_p(c_t)=\exp\!\Big(-\int_{S^-}F_a\Big)\qquad(\text{abelian holonomy formula, surface form, }F_a=dA_\alpha).$$
> The base point $p\in S^3$ does not appear on the right: for an abelian group conjugation is trivial, so by the corollary $\operatorname{hol}_{pg}(c)=g^{-1}\operatorname{hol}_p(c)g=\operatorname{hol}_p(c)$ on [[Def - Holonomy Group of a Connection|the holonomy page]], the holonomy is independent of the chosen point in the fibre. We therefore write $\operatorname{hol}(c_t)$ from now on.

**Step 3: Evaluate the flux and exponentiate.**

The integral is elementary in the height–longitude coordinates, giving $\int_{S^-}F_a=2\pi i\big(t+\tfrac12\big)$ and hence $\operatorname{hol}(c_t)=-e^{-2\pi it}$.

> [!note]- Derivation
> In the coordinates of Step 1 the southern cap is $S^-=\{(t',\phi):-\tfrac12\le t'\le t,\ 0\le\phi<2\pi\}$, and $F_a=i\,dt\wedge d\phi$, so
> $$\int_{S^-}F_a=i\int_{-1/2}^{\,t}\!\!\int_0^{2\pi}d\phi\,dt'=i\int_{-1/2}^{\,t}2\pi\,dt'=2\pi i\Big(t-\big(-\tfrac12\big)\Big)=2\pi i\big(t+\tfrac12\big)\qquad(\text{Fubini; the integrand is a constant multiple of }dt\wedge d\phi).$$
> Substituting into Step 2,
> $$\operatorname{hol}(c_t)=\exp\!\Big(-2\pi i\big(t+\tfrac12\big)\Big)=\exp\big(-2\pi i t-\pi i\big)=e^{-\pi i}\,e^{-2\pi it}=-\,e^{-2\pi it}\qquad(\text{since }e^{-\pi i}=-1).$$
> This is the required holonomy. Writing $\int_{S^-}F_a=i\,\mathcal{A}$ with the **normalised area** $\mathcal{A}:=2\pi\big(t+\tfrac12\big)$ (the geometric cap area $\pi(t+\tfrac12)$ weighted by the curvature density $2$, equivalently $2\pi$ times the fraction $\big(t+\tfrac12\big)$ of the total flux carried by the cap), the answer takes the announced form $\operatorname{hol}(c_t)=\exp(-i\,\mathcal{A})$.

**Step 4: Independent check through an explicit local potential.**

A local potential $A_S=i\big(t+\tfrac12\big)\,d\phi$ on $U=S^2\setminus\{N\}$ has $dA_S=F_a$, and $\oint_{c_t}A_S=2\pi i\big(t+\tfrac12\big)$, reproducing Step 3 without invoking Stokes.

> [!note]- Derivation
> Define $A_S:=i\big(t+\tfrac12\big)\,d\phi$ on $U\setminus\{S\}$. Then
> $$dA_S=i\,dt\wedge d\phi=F_a\qquad(\text{differentiating; the coefficient }i(t+\tfrac12)\text{ depends only on }t).$$
> Moreover $A_S$ extends smoothly across the south pole $S$: there its coefficient $i\big(t+\tfrac12\big)$ vanishes ($t=-\tfrac12$) exactly as the longitude one-form $d\phi$ degenerates, so $A_S$ is a genuine smooth potential on all of $U=S^2\setminus\{N\}$, the very trivialising set used above. (It does *not* extend across $N$, where the coefficient tends to $i$ while $d\phi$ degenerates; this is why the north pole is removed, and it is the coordinate shadow of the bundle's nontriviality.) The line integral over $c_t$, parametrised by $\phi\in[0,2\pi]$ at fixed height $t$, is
> $$\oint_{c_t}A_S=\int_0^{2\pi}i\big(t+\tfrac12\big)\,d\phi=2\pi i\big(t+\tfrac12\big)\qquad(t\text{ constant along }c_t),$$
> in agreement with $\int_{S^-}F_a$ from Step 3 (as [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] — $\int_{\partial S}\eta=\int_S d\eta$ for a smooth form $\eta$ on a compact oriented surface-with-boundary $S$ — demands, applied to $\eta=A_S$, $S=S^-$). By the line-integral form of the abelian holonomy formula, $\operatorname{hol}(c_t)=\exp\big(-\oint_{c_t}A_S\big)=\exp\big(-2\pi i(t+\tfrac12)\big)=-e^{-2\pi it}$, exactly as before.

**Step 5: Consistency across the two caps and the shrinking-loop limits.**

The northern cap gives the same holonomy, and the loop-to-pole limits and the equatorial case all agree with the expected values.

> [!note]- Derivation
> *Both caps agree.* The circle $c_t$ also bounds the northern cap $S^+=\{h\ge t\}$, but with the opposite induced orientation: $c_t=-\partial S^+$. Applying the abelian formula through $S^+$ gives
> $$\operatorname{hol}(c_t)=\exp\!\Big(+\int_{S^+}F_a\Big),\qquad \int_{S^+}F_a=i\int_{t}^{1/2}\!\!\int_0^{2\pi}d\phi\,dt'=2\pi i\big(\tfrac12-t\big),$$
> so this route yields $\exp\big(2\pi i(\tfrac12-t)\big)=\exp\big(\pi i-2\pi it\big)=-e^{-2\pi it}$, the same value. The two evaluations are forced to agree because their exponents differ by
> $$\Big(-\int_{S^-}F_a\Big)-\Big(+\int_{S^+}F_a\Big)=-\int_{S^2}F_a=-2\pi i\in 2\pi i\mathbb{Z}=\ker\big(\exp\colon i\mathbb{R}\to U(1)\big),$$
> which is the integrality of the Hopf bundle's flux: the total curvature is exactly one full period of the exponential.
>
> *Shrinking-loop limits.* As $t\to\tfrac12^-$ the circle $c_t$ shrinks to the north pole and the enclosed southern cap fills the whole sphere; $\operatorname{hol}(c_t)=-e^{-2\pi it}\to -e^{-\pi i}=-(-1)=1$, the identity, as it must for a loop contracting to a point. As $t\to-\tfrac12^+$ the circle shrinks to the south pole and $S^-$ collapses; $\operatorname{hol}(c_t)\to -e^{\pi i}=-(-1)=1$, again the identity.
>
> *Equator.* At $t=0$ the latitude circle is a great circle, and $\operatorname{hol}(c_0)=-e^{0}=-1$. This matches the value $e^{-i\pi}=-1$ obtained by direct horizontal lifting of the equator in [[Ex - Parallel Transport in the Hopf Bundle along a Great Circle|the §5.1 great-circle exercise]]; there the enclosed hemisphere carries half of the total flux $2\pi i$, i.e. $\pi i$, and $\exp(-\pi i)=-1$.

> [!note]- Complete formal solution
> Let $\pi\colon S^3\to S^2$ be the Hopf bundle with its standard $U(1)$-connection $a$, whose curvature descends to the base $S^2\cong S^2_{1/2}$ as $F_a=2i\,\operatorname{vol}_{S^2_{1/2}}$ with $\int_{S^2}F_a=2\pi i$ (from [[Ex - Curvature of the Standard Hopf Connection]]). Coordinatise the base off the poles by height $t\in(-\tfrac12,\tfrac12)$ and longitude $\phi\in\mathbb{R}/2\pi\mathbb{Z}$, with $(\partial_t,\partial_\phi)$ positively oriented.
>
> On a sphere of radius $R$ the round area form in height–longitude coordinates is $R\,dz\wedge d\phi$ (Archimedes' hat-box theorem). With $R=\tfrac12$ this is $\operatorname{vol}_{S^2_{1/2}}=\tfrac12\,dt\wedge d\phi$, hence
> $$F_a=2i\cdot\tfrac12\,dt\wedge d\phi=i\,dt\wedge d\phi,\qquad \int_{S^2}F_a=i\!\int_{-1/2}^{1/2}\!\!\int_0^{2\pi}\!d\phi\,dt=2\pi i.$$
>
> Let $U=S^2\setminus\{N\}$ (north pole removed). Being diffeomorphic to $\mathbb{R}^2$, $U$ is contractible, so by [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|the homotopy-invariance theorem]] the Hopf bundle is trivial over $U$, and hence by [[Thm - Sections of a Principal Bundle and Triviality|the triviality criterion]] $U$ is a trivialising set. For $t<\tfrac12$ the latitude circle $c_t$ and the southern cap $S^-=\{h\le t\}$ both lie in $U$, and with $U$'s orientation the boundary $\partial S^-$ carries the increasing-longitude orientation, which is that of $c_t$.
>
> The group $U(1)$ is abelian, $c_t$ is a loop in the trivialising set $U$, and $S^-\subset U$ is a compact oriented surface with $\partial S^-=c_t$. By [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|the abelian holonomy formula]] (surface form),
> $$\operatorname{hol}(c_t)=\exp\!\Big(-\int_{S^-}F_a\Big),\qquad \int_{S^-}F_a=i\!\int_{-1/2}^{\,t}\!\!\int_0^{2\pi}\!d\phi\,dt'=2\pi i\big(t+\tfrac12\big).$$
> Since $U(1)$ is abelian the value is independent of the point in the fibre. Therefore
> $$\boxed{\ \operatorname{hol}(c_t)=\exp\!\Big(-2\pi i\big(t+\tfrac12\big)\Big)=-\,e^{-2\pi i t}\ }$$
> equivalently $\operatorname{hol}(c_t)=\exp(-i\,\mathcal{A})$ with normalised area $\mathcal{A}=2\pi\big(t+\tfrac12\big)$.
>
> The result is confirmed by three independent checks. (1) The northern cap $S^+=\{h\ge t\}$, with $c_t=-\partial S^+$, gives $\exp\big(+\int_{S^+}F_a\big)=\exp\big(2\pi i(\tfrac12-t)\big)=-e^{-2\pi it}$; the two agree because their exponents differ by $-\int_{S^2}F_a=-2\pi i\in\ker\exp$. (2) The limits $t\to\pm\tfrac12$ give $\operatorname{hol}\to 1$, as required for a loop contracting to a pole. (3) At $t=0$, $\operatorname{hol}(c_0)=-1$, matching [[Ex - Parallel Transport in the Hopf Bundle along a Great Circle|the great-circle computation]]. $\blacksquare$

> [!warning] Illegal but tempting route: integrating $A_S$ over the "obvious" disc through the north pole
> It is tempting to fill $c_t$ with the northern cap and use the *same* potential $A_S=i(t+\tfrac12)\,d\phi$ to write $\operatorname{hol}=\exp\big(-\int_{S^+}dA_S\big)$. This is illegal: $A_S$ is **not** smooth on $S^+$, because $S^+$ contains the north pole $N$, where $A_S$ has the nonzero coefficient $i$ against the degenerating form $d\phi$. Stokes' theorem requires the potential to be smooth on the whole surface, and here it fails at $N$; the defect is exactly $\oint$ of the transition function around a small loop about $N$, i.e. one unit of winding, which is the bundle's Chern number. The correct northern-cap computation uses the *other* local potential $A_N=i(t-\tfrac12)\,d\phi$, which is smooth across $N$ (its coefficient vanishes there) but singular at $S$; then, since $c_t$ lies in the trivialising set $S^2\setminus\{S\}$ on which $A_N$ is the local potential, the line-integral formula (with its standing minus sign) gives $\operatorname{hol}=\exp\big(-\oint_{c_t}A_N\big)=\exp\big(-2\pi i(t-\tfrac12)\big)=\exp\big(2\pi i(\tfrac12-t)\big)$, agreeing with Step 5. The lesson: each spherical cap must be integrated with the potential regular on *that* cap, and the two potentials differ by the transition one-form $A_N-A_S=-i\,d\phi=g^{-1}dg$ with $g=e^{-i\phi}$.

---

# Key Takeaways

**For an abelian connection, holonomy is flux, and the base point drops out.** The single most reusable fact in this exercise is that a $U(1)$- (or any abelian-) connection has $\operatorname{hol}(c)=\exp\big(-\int_S F\big)$ for a loop $c$ bounding a surface $S$ inside a trivialising set, with no ordering and no conjugation to track. The trigger to reach for this is the appearance of an abelian structure group together with a loop that bounds; the diagnostic that it is the right tool is that the answer will be a pure exponential of a curvature integral, so all one must do is compute one number. This is what makes electromagnetism and Berry-phase computations tractable: the Aharonov–Bohm phase, the Dirac quantisation condition, and the geometric phase of an adiabatically transported quantum state are all instances of $\exp\big(-\int_S F\big)$ for a $U(1)$-connection, and each is computed by exactly the method above. The non-abelian analogue is genuinely harder precisely because the ordered exponential does not collapse; the small-loop expansion [[Thm - Curvature is the Infinitesimal Holonomy|"holonomy is one minus the curvature flux to leading order"]] is the residue of this abelian identity in the non-abelian world.

**Integrality of the total flux is the well-definedness of the holonomy.** The two caps bounded by the same latitude circle give the same holonomy only because $\int_{S^2}F_a=2\pi i$ lies in the kernel $2\pi i\mathbb{Z}$ of the exponential. Read forwards, this is a *consistency requirement*: for the holonomy to be well defined independently of the filling surface, the total curvature over any closed surface must be an integer multiple of $2\pi i$. That integer is the first Chern number of the line bundle, and here it is $\tfrac{i}{2\pi}\int_{S^2}F_a=\tfrac{i}{2\pi}\cdot 2\pi i=-1$, the Chern number of the tautological bundle $\mathcal{O}(-1)$ associated to the Hopf bundle. The recurring lesson for spaced practice: whenever a geometric quantity is defined by "choose a filling and integrate", its well-definedness modulo the ambiguity is a quantisation statement, and the ambiguity is a characteristic number. This same reasoning underlies the Dirac quantisation of magnetic charge in chapter VII.

**The Hopf phase is exactly half the Riemannian solid-angle rotation — the arithmetic signature of the spin double cover.** Compare this computation with [[Ex - Holonomy around a Spherical Cap is the Solid Angle|the Riemannian spherical-cap exercise]], where parallel transport of a *tangent* vector around the same latitude circle rotates it by the solid angle $\Omega=2\pi(1-\cos\theta_0)$ subtended by the cap. Writing the height as $t=\tfrac12\cos\theta_0$, our southern-cap flux is $\int_{S^-}F_a=2\pi i(t+\tfrac12)=\pi i(1+\cos\theta_0)=i\cdot\tfrac12\,\Omega_{S^-}$, so the Hopf holonomy phase is *half* the solid angle of the enclosed cap. The factor of two is not an accident of normalisation: the tangent bundle $TS^2$ has Euler number $2$, while the Hopf line bundle $\mathcal{O}(-1)$ has Chern number $-1$, exactly half in magnitude, so its curvature carries half the flux. Geometrically, the Hopf bundle is the "square root" of the tangent framing — the same relation that makes $SU(2)\to SO(3)$ a double cover and makes a spin-$\tfrac12$ state acquire the phase $-1$ under a $2\pi$ rotation. The equatorial value $\operatorname{hol}(c_0)=-1$ is precisely this: transporting a fibre around a great circle, which encloses half the sphere, returns it multiplied by $-1$, the half-turn phase that a spinor sees where a vector would already have returned to itself.

**The pole limits diagnose the coordinate singularity, not a geometric one.** As the loop shrinks to either pole the holonomy tends to $1$, confirming that the connection is smooth at the poles even though the height–longitude chart and the local potentials $A_S,A_N$ are singular there. The two potentials, each regular on the complement of one pole and differing by the transition one-form $g^{-1}dg$, are the coordinate expression of the bundle's nontriviality: no single global potential exists, and the obstruction is exactly the winding of $g=e^{\pm i\phi}$ about a pole, i.e. the Chern number. The transferable diagnostic is to distrust any computation that fills a loop with a cap through the pole where the chosen potential blows up; the correct move is to switch to the potential regular on that cap, and the mismatch between the two potentials is where the topology lives. This is the same bookkeeping that reappears in the clutching construction and in the proof that $c_1$ is the winding number of the transition function on [[Thm - First Chern Class of a Line Bundle from Curvature|the first-Chern-class page]].

**Companion exercises.** Read this alongside [[Ex - Parallel Transport in the Hopf Bundle along a Great Circle]] (the equatorial special case, done by direct horizontal lifting rather than by the flux formula) and [[Ex - Holonomy of a Constant Connection on the Trivial Bundle over the Torus]] (the flat case, where loops do not bound and one must use the line-integral form of the formula). Together the three exercises span the abelian holonomy formula's whole range of use: a bounding loop with nonzero curvature (here), a bounding loop computed by lifting (the great circle), and a non-bounding loop on a flat bundle (the torus).
