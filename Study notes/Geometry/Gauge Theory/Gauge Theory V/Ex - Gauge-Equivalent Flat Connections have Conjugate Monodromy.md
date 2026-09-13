---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Thm - Flat Connections and Monodromy Representations of the Fundamental Group"
  - "Def - Gauge Transformation"
  - "Def - Holonomy Group of a Connection"
  - "Def - Parallel Transport in a Principal Bundle"
  - "Def - Flat Connection"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $M$ be a connected smooth manifold with base point $m$, and write $\Gamma:=\pi_1(M,m)$ for its fundamental group. Two flat connections that differ by a gauge transformation should describe "the same" flat bundle seen through a change of internal frame; the point of this exercise is to make that idea precise at the level of the monodromy representation, and to see that the change of frame acts on the representation by a single conjugation.

This is exercise 104 of Haydys, *Introduction to Gauge Theory* (§3.3.2), phrased there as: "Show that a gauge-equivalent connection yields a conjugate representation." We prove it in the two forms the series uses — for a connection on a principal bundle and for a connection on a vector bundle — and identify the conjugating element explicitly in each case.

**Problem (vector-bundle form).** Let $E\to M$ be a real vector bundle of rank $k$, let $\nabla$ be a flat connection on $E$, and let $g\in\mathcal G(E)$ be a gauge transformation acting on the right by
$$\nabla^{g}s \;=\; g^{-1}\,\nabla(g\,s),\qquad s\in\Gamma(E).$$
Prove that $\nabla^{g}$ is again flat and that its monodromy representation is conjugate to that of $\nabla$: writing $\rho_\nabla,\rho_{\nabla^{g}}\colon \Gamma\to GL(E_m)$ for the two monodromy representations at $m$,
$$\rho_{\nabla^{g}}([\gamma]) \;=\; g(m)^{-1}\,\rho_{\nabla}([\gamma])\,g(m)\qquad\text{for every }[\gamma]\in\Gamma,$$
so that $\rho_{\nabla^{g}}$ and $\rho_\nabla$ represent the same point of the representation variety $\mathcal R(M;GL_k(\mathbb R))$.

**Problem (principal-bundle form).** Let $P\to M$ be a principal $G$-bundle with a flat connection $\omega$, let $f\in\mathcal G(P)$ be a gauge transformation acting on the right by $\omega\cdot f:=f^{*}\omega$, and write $f(p)=p\cdot\hat g(p)$ for the associated equivariant function $\hat g\colon P\to G$. Fix $p\in P_m$ and let $u:=\hat g(p)\in G$. Prove that $f^{*}\omega$ is flat and that its monodromy representation at $p$ satisfies
$$\rho_{f^{*}\omega}([\gamma]) \;=\; u^{-1}\,\rho_{\omega}([\gamma])\,u\qquad\text{for every }[\gamma]\in\Gamma,$$
so $\rho_{f^{*}\omega}$ and $\rho_\omega$ represent the same point of $\mathcal R(M;G)$.

**Recall:**

The objects in play are a flat connection, its monodromy (holonomy) representation of the fundamental group, a gauge transformation and its action on connections, and parallel transport.

![[Def - Flat Connection#The Definition]]

A connection is **flat** when its curvature vanishes identically: $F_\nabla=0$ for a vector-bundle connection, $\Omega_\omega=0$ for a principal connection. Flatness is what makes parallel transport homotopy-invariant, and hence what makes the monodromy representation well defined.

![[Thm - Flat Connections and Monodromy Representations of the Fundamental Group#Statement]]

For a flat connection, parallel transport around a loop depends only on the homotopy class of the loop (proved on [[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|the homotopy-invariance page]]), so the assignment $[\gamma]\mapsto\operatorname{hol}(\gamma)$ is a well-defined representation of $\Gamma=\pi_1(M,m)$ — the **monodromy representation** $\rho_\nabla\colon\Gamma\to GL(E_m)$ (or $\rho_\omega\colon\Gamma\to G$). Throughout we write the monodromy through parallel transport; the conjugation identity we prove is insensitive to the convention (holonomy versus its inverse; homomorphism versus anti-homomorphism) fixed on that page, because conjugation by a fixed element commutes with inversion and with reindexing the group.

![[Def - Gauge Transformation#The Definition]]

A **gauge transformation** of a principal bundle $P$ is an equivariant diffeomorphism $f\colon P\to P$ covering the identity of $M$; equivalently (by [[Thm - The Gauge Group is the Space of Sections of the Adjoint Group Bundle|the adjoint-bundle description of the gauge group]]) it is given by $f(p)=p\cdot\hat g(p)$ for a function $\hat g\colon P\to G$ satisfying the equivariance $\hat g(p\cdot a)=a^{-1}\hat g(p)\,a$. A gauge transformation of a vector bundle $E$ is a section $g\in\mathcal G(E)\subset\Gamma(\operatorname{End}E)$ with $g(x)\in GL(E_x)$ for every $x$; it acts on connections by $\nabla^{g}s=g^{-1}\nabla(gs)$.

![[Thm - Gauge Transformations Act on Connections and Curvature#Statement]]

Under a gauge transformation the curvature transforms by conjugation: $F_{\nabla^{g}}=g^{-1}F_\nabla g$ for a vector bundle, and $\Omega_{f^{*}\omega}=f^{*}\Omega_\omega$ (locally $F_{f^{*}\omega,s}=\operatorname{Ad}_{g^{-1}}F_{\omega,s}$) for a principal bundle. In particular flatness is preserved.

![[Def - Parallel Transport in a Principal Bundle#The Definition]]

For a piecewise-smooth curve $c\colon[0,1]\to M$, **parallel transport** $\Gamma(c)\colon P_{c(0)}\to P_{c(1)}$ (on a principal bundle) sends $p$ to the endpoint of the horizontal lift of $c$ through $p$; on an associated vector bundle it induces the linear isomorphism $PT_c\colon E_{c(0)}\to E_{c(1)}$. Parallel transport is equivariant, $\Gamma(c)\circ R_a=R_a\circ\Gamma(c)$ (property (5) of [[Thm - Properties of Parallel Transport|the properties-of-parallel-transport theorem]]), and on a vector bundle a section $s$ along $c$ is parallel exactly when $(c^{*}\nabla)s=0$.

![[Def - Holonomy Group of a Connection#The Definition]]

The **holonomy** $\operatorname{hol}_p(c)\in G$ of a loop $c$ at $m$ is defined by $\Gamma(c)(p)=p\cdot\operatorname{hol}_p(c)$; on a vector bundle it is the linear map $PT_c\in GL(E_m)$. The monodromy representation is holonomy read as a function of the homotopy class.

---

# Convergent Strategy

**Problem class.** This is a *transformation-law* problem: an object (the monodromy representation) is attached to a connection, the connection is acted on by a group (the gauge group), and we must compute how the object transforms. The universal method for such problems is to trace the definition of the attached object through the group action step by step, never guessing the answer. The attached object here is built from parallel transport, so the whole problem reduces to one prior question — *how does parallel transport change when the connection is gauge-transformed?* — followed by bookkeeping.

**Assumption pattern.** Flatness is used in exactly one place: it is what licenses the phrase "monodromy representation" at all, because only for a flat connection does holonomy descend to a function of homotopy classes ([[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|homotopy-invariance theorem]]). The transformation law for parallel transport itself needs no flatness; it holds loop by loop. So the argument splits cleanly: first the flatness-free computation of how $PT$ (or $\Gamma(c)$) transforms, then the one invocation of flatness to say the result is a statement about representations rather than about individual loops. We also need flatness of $\nabla^{g}$ (respectively $f^{*}\omega$) so that $\rho_{\nabla^{g}}$ exists; that is immediate from the curvature transformation law.

**Theorem routing.** The route is: (1) [[Thm - Gauge Transformations Act on Connections and Curvature|curvature transforms by conjugation]] $\Rightarrow$ the gauge-transformed connection is flat, so its monodromy exists; (2) unwind $\nabla^{g}s=g^{-1}\nabla(gs)$ (respectively the horizontal distribution of $f^{*}\omega$) to see that a $\nabla^{g}$-parallel object becomes a $\nabla$-parallel object after applying $g$ (respectively $f$); (3) read off $PT^{\nabla^{g}}_c=g(c(1))^{-1}\,PT^{\nabla}_c\,g(c(0))$ (respectively $\Gamma^{f^{*}\omega}(c)=f^{-1}\circ\Gamma^{\omega}(c)\circ f$); (4) specialise to a loop at $m$ and use the equivariance of parallel transport plus the equivariance of $\hat g$ to collapse the endpoint factors into a single conjugation; (5) invoke flatness/homotopy-invariance to promote the loop identity to an identity of representations.

**Key decision point.** The one genuine decision is *which parallel object to transport*. For the vector bundle it is cleanest to observe that $\nabla^{g}$-parallelism of $s$ is literally $\nabla$-parallelism of $gs$ — a one-line rewrite of the defining formula — rather than to compute connection matrices in a frame. For the principal bundle the parallel object is the horizontal lift, and the decision is to characterise the horizontal distribution of $f^{*}\omega$ as $(df)^{-1}$ of that of $\omega$, so that lifts of $f^{*}\omega$ are $f^{-1}$ of lifts of $\omega$. Both decisions replace a computation with a naturality observation, which is why the exercise is short.

---

# Legal Operations Used

The topic page for Gauge Theory V is not yet assembled, so the operations are named descriptively; the orchestrator will reconcile the numbering.

1. **Rewrite the transformed connection's parallel condition as the original's parallel condition (pull the gauge through the derivative).** From $\nabla^{g}s=g^{-1}\nabla(gs)$ one reads that $(c^{*}\nabla^{g})s=0$ if and only if $(c^{*}\nabla)(gs)=0$: the section $s$ is $\nabla^{g}$-parallel exactly when $gs$ is $\nabla$-parallel. This is the whole engine of the vector-bundle case.

2. **Characterise the transformed horizontal distribution as the pre-image of the original under the differential.** For $f\in\mathcal G(P)$, $H^{f^{*}\omega}=\ker(f^{*}\omega)=(df)^{-1}\ker\omega=(df)^{-1}H^{\omega}$, so a curve is $f^{*}\omega$-horizontal precisely when its image under $f$ is $\omega$-horizontal. This is the principal-bundle analogue of operation 1.

3. **Use equivariance of parallel transport, $\Gamma(c)\circ R_a=R_a\circ\Gamma(c)$** (property (5) of [[Thm - Properties of Parallel Transport|the properties theorem]]), to move a group element through a parallel transport.

4. **Use the equivariance of the gauge function, $\hat g(p\cdot a)=a^{-1}\hat g(p)\,a$** (from [[Thm - The Gauge Group is the Space of Sections of the Adjoint Group Bundle|the adjoint-bundle description]]), to evaluate $\hat g$ at a transported point and collapse the two endpoint factors into a single conjugation.

5. **Invoke flatness through the curvature transformation law** ([[Thm - Gauge Transformations Act on Connections and Curvature|conjugation of curvature]]) to conclude that the gauge-transformed connection is flat, hence has a monodromy representation.

6. **Promote a loop-by-loop identity to a representation identity** by invoking [[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|homotopy-invariance of holonomy for flat connections]], which is what turns holonomy into the homomorphism $\rho$.

---

# Hints

> [!note]- Hint 1
> Do not try to compute in a frame or with connection matrices. Everything follows from the *defining formula* of the gauge action. For the vector bundle, stare at $\nabla^{g}s=g^{-1}\nabla(gs)$ and ask: if $s$ is parallel for $\nabla^{g}$ along a curve, what is parallel for $\nabla$?

> [!note]- Hint 2
> A section $s$ along $c$ is $\nabla^{g}$-parallel iff $g^{-1}\nabla(gs)=0$ along $c$ iff $\nabla(gs)=0$ along $c$ (since $g$ is invertible at every point) iff $gs$ is $\nabla$-parallel. So parallel transport for the two connections is related by conjugating with $g$ at the two endpoints. Write that relation down for a general curve $c$ from $x$ to $y$.

> [!note]- Hint 3
> You should obtain $PT^{\nabla^{g}}_{c}=g(y)^{-1}\circ PT^{\nabla}_{c}\circ g(x)$ for a curve from $x$ to $y$. Now take $c$ to be a loop at $m$: both endpoint factors are $g(m)$, and they no longer cancel — they conjugate. That is the answer. Only at the very end do you need flatness: to know that $\rho_{\nabla^{g}}$ is defined and that this loop identity is an identity of representations of $\pi_1$.

> [!note]- Hint 4
> For the principal bundle, replace "parallel section" by "horizontal lift". Because $f$ is a diffeomorphism of $P$ with $H^{f^{*}\omega}=(df)^{-1}H^{\omega}$, the $f^{*}\omega$-horizontal lift of $c$ through $p$ is $f^{-1}$ applied to the $\omega$-horizontal lift through $f(p)$. Hence $\Gamma^{f^{*}\omega}(c)=f^{-1}\circ\Gamma^{\omega}(c)\circ f$. To turn this into a conjugation of holonomies, write $f(p)=p\cdot\hat g(p)$, transport, and use the equivariance $\hat g(p\cdot a)=a^{-1}\hat g(p)a$ when you evaluate $\hat g$ at the transported point.

---

# Solution

The proof has the same shape in both settings and reduces to a single idea: *a gauge transformation intertwines the parallel transports of $\nabla$ and $\nabla^{g}$ pointwise along the curve*, so around a loop the two endpoint intertwiners become one conjugation. We treat the vector bundle first, where the algebra is transparent, then the principal bundle, where the same idea is carried by horizontal lifts. Flatness enters only to guarantee that the transformed connection has a monodromy representation and that the loop identity descends to homotopy classes.

## Part A — the vector-bundle case

**Step 1: $\nabla^{g}$ is flat, so $\rho_{\nabla^{g}}$ is defined.**

The curvature of the gauge-transformed connection is $F_{\nabla^{g}}=g^{-1}F_\nabla g$, which vanishes because $\nabla$ is flat; hence $\nabla^{g}$ is flat and has a monodromy representation.

> [!note]- Derivation
> By [[Thm - Gauge Transformations Act on Connections and Curvature|the gauge transformation law for curvature]], for $g\in\mathcal G(E)$ the curvature transforms by conjugation,
> $$F_{\nabla^{g}} \;=\; g^{-1}\,F_{\nabla}\,g \qquad \text{(gauge transformation law for the curvature of a vector-bundle connection).}$$
> By hypothesis $\nabla$ is [[Def - Flat Connection|flat]], so $F_\nabla=0$, and therefore
> $$F_{\nabla^{g}} \;=\; g^{-1}\cdot 0\cdot g \;=\; 0 \qquad \text{(substituting } F_\nabla=0\text{).}$$
> Thus $\nabla^{g}$ is flat. By [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the flat-connection/monodromy theorem]], a flat connection on $E$ has a well-defined monodromy representation $\rho_{\nabla^{g}}\colon\Gamma\to GL(E_m)$; the representation $\rho_\nabla$ exists for the same reason. Both objects we wish to compare therefore exist.

**Step 2: The two parallel-transport maps are intertwined by $g$.**

Along any piecewise-smooth curve $c$ from $x$ to $y$, parallel transport for $\nabla^{g}$ equals parallel transport for $\nabla$ conjugated by the values of $g$ at the endpoints:
$$PT^{\nabla^{g}}_{c} \;=\; g(y)^{-1}\circ PT^{\nabla}_{c}\circ g(x)\ \colon\ E_x\to E_y.$$

> [!note]- Derivation
> Fix a piecewise-smooth curve $c\colon[0,1]\to M$ with $c(0)=x$, $c(1)=y$, and let $s\in\Gamma(c^{*}E)$ be a section along $c$, viewed as $t\mapsto s(t)\in E_{c(t)}$. By the definition of parallel transport on a vector bundle, $s$ is **$\nabla^{g}$-parallel along $c$** means $(c^{*}\nabla^{g})s=0$.
>
> **Pull the gauge through the derivative.** By the defining formula of the gauge action, $\nabla^{g}\sigma=g^{-1}\nabla(g\sigma)$ for every section $\sigma$, and this is compatible with pull-back along $c$ (the gauge transformation $g$ pulls back to the fibrewise-invertible endomorphism $t\mapsto g(c(t))$, and $c^{*}\nabla^{g}=(c^{*}g)^{-1}\,(c^{*}\nabla)\,(c^{*}g)$ by naturality of the covariant derivative under pull-back). Writing $g$ for $c^{*}g$ to lighten notation,
> $$(c^{*}\nabla^{g})s \;=\; g^{-1}\,(c^{*}\nabla)(g\,s) \qquad \text{(defining formula } \nabla^{g}=g^{-1}\nabla g\text{, pulled back along } c\text{).}$$
> Since $g(c(t))\in GL(E_{c(t)})$ is invertible for every $t$, the left side vanishes if and only if $(c^{*}\nabla)(g s)=0$:
> $$(c^{*}\nabla^{g})s=0 \quad\Longleftrightarrow\quad (c^{*}\nabla)(g s)=0 \qquad \text{(multiplying by the invertible } g(c(t))\text{ pointwise).}$$
> In words: **$s$ is $\nabla^{g}$-parallel along $c$ if and only if $gs$ is $\nabla$-parallel along $c$** (operation 1).
>
> **Read off the transport maps.** Let $v\in E_x$ and let $s$ be the $\nabla^{g}$-parallel section along $c$ with $s(0)=v$; by definition $PT^{\nabla^{g}}_{c}(v)=s(1)$. Then $gs$ is the $\nabla$-parallel section along $c$ with initial value $(gs)(0)=g(x)v$, so by definition of $PT^{\nabla}_c$,
> $$(gs)(1) \;=\; PT^{\nabla}_{c}\big(g(x)v\big) \qquad \text{(} gs \text{ is } \nabla\text{-parallel with initial value } g(x)v\text{).}$$
> But $(gs)(1)=g(y)\,s(1)=g(y)\,PT^{\nabla^{g}}_{c}(v)$, hence
> $$g(y)\,PT^{\nabla^{g}}_{c}(v) \;=\; PT^{\nabla}_{c}\big(g(x)v\big) \qquad \text{(evaluating } gs \text{ at } t=1\text{).}$$
> Applying $g(y)^{-1}$ and letting $v\in E_x$ be arbitrary gives the claimed intertwining
> $$PT^{\nabla^{g}}_{c} \;=\; g(y)^{-1}\circ PT^{\nabla}_{c}\circ g(x). \qquad \text{(} g(y)\in GL(E_y)\text{ is invertible).}$$

**Step 3: Around a loop the two endpoint factors become one conjugation.**

Specialising to a loop at $m$ and passing to homotopy classes gives $\rho_{\nabla^{g}}([\gamma])=g(m)^{-1}\rho_\nabla([\gamma])g(m)$.

> [!note]- Derivation
> Let $\gamma\colon[0,1]\to M$ be a piecewise-smooth loop at $m$, so $x=y=m$. Substituting $x=y=m$ into the intertwining of Step 2,
> $$PT^{\nabla^{g}}_{\gamma} \;=\; g(m)^{-1}\circ PT^{\nabla}_{\gamma}\circ g(m) \qquad \text{(Step 2 with } c=\gamma,\ c(0)=c(1)=m\text{).}$$
> Both sides are elements of $GL(E_m)$, and the right side is the conjugate of $PT^{\nabla}_{\gamma}$ by the fixed invertible endomorphism $g(m)\in GL(E_m)$.
>
> **Promote to representations.** Because $\nabla$ and $\nabla^{g}$ are both flat (Step 1), [[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|homotopy-invariance of holonomy]] applies to each: parallel transport around a loop depends only on the loop's class in $\Gamma=\pi_1(M,m)$, and the resulting monodromy representations are
> $$\rho_\nabla([\gamma]) = PT^{\nabla}_{\gamma},\qquad \rho_{\nabla^{g}}([\gamma]) = PT^{\nabla^{g}}_{\gamma} \qquad \text{(definition of the monodromy representation, using the fixed convention of the theorem page).}$$
> Combining the last two displays,
> $$\rho_{\nabla^{g}}([\gamma]) \;=\; g(m)^{-1}\,\rho_\nabla([\gamma])\,g(m)\qquad\text{for every }[\gamma]\in\Gamma. \qquad \text{(conjugation by the fixed element } g(m)\text{).}$$
> The conjugating element $g(m)$ does not depend on $[\gamma]$, so $\rho_{\nabla^{g}}$ and $\rho_\nabla$ are conjugate as representations, i.e. equal in $\mathcal R(M;GL_k(\mathbb R))$. This proves the vector-bundle form.
>
> **Convention remark.** If the theorem page fixes the monodromy to be $\rho_\nabla([\gamma])=(PT^{\nabla}_\gamma)^{-1}$ (to make $\rho$ a homomorphism rather than an anti-homomorphism), the identity is unchanged: inverting $PT^{\nabla^{g}}_\gamma=g(m)^{-1}PT^{\nabla}_\gamma g(m)$ gives $(PT^{\nabla^{g}}_\gamma)^{-1}=g(m)^{-1}(PT^{\nabla}_\gamma)^{-1}g(m)$, the same conjugation. This is why the recall note above stresses that the result is convention-insensitive.

## Part B — the principal-bundle case

**Step 4: $f^{*}\omega$ is flat.**

The curvature satisfies $\Omega_{f^{*}\omega}=f^{*}\Omega_\omega=0$, so $f^{*}\omega$ is flat and has a monodromy representation at $p$.

> [!note]- Derivation
> By [[Thm - Gauge Transformations Act on Connections and Curvature|the gauge transformation law]], for $f\in\mathcal G(P)\subset\operatorname{Aut}(P)$ the curvature transforms naturally, $\Omega_{f^{*}\omega}=f^{*}\Omega_\omega$. Since $\omega$ is [[Def - Flat Connection|flat]], $\Omega_\omega=0$, and the pull-back of the zero form is zero:
> $$\Omega_{f^{*}\omega} \;=\; f^{*}\Omega_\omega \;=\; f^{*}0 \;=\; 0 \qquad \text{(curvature transformation law, then } \Omega_\omega=0\text{).}$$
> Thus $f^{*}\omega$ is flat and, by [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the flat-connection/monodromy theorem]], has a monodromy representation $\rho_{f^{*}\omega}\colon\Gamma\to G$ at the chosen $p\in P_m$.

**Step 5: The parallel transports are intertwined by $f$.**

For any piecewise-smooth curve $c$ from $x$ to $y$, the parallel-transport maps satisfy $\Gamma^{f^{*}\omega}(c)=f^{-1}\circ\Gamma^{\omega}(c)\circ f$ as maps $P_x\to P_y$.

> [!note]- Derivation
> The horizontal distribution of $f^{*}\omega$ is
> $$H^{f^{*}\omega}_q \;=\; \ker\big((f^{*}\omega)_q\big) \;=\; \ker\big(\omega_{f(q)}\circ d_qf\big) \;=\; (d_qf)^{-1}\big(\ker\omega_{f(q)}\big) \;=\; (d_qf)^{-1}\,H^{\omega}_{f(q)} \qquad \text{(definition of } f^{*}\omega\text{; } d_qf \text{ is a linear isomorphism, } f \text{ a diffeomorphism).}$$
> (operation 2). Consequently a curve $\tilde c$ in $P$ is $f^{*}\omega$-horizontal — meaning $\dot{\tilde c}(t)\in H^{f^{*}\omega}_{\tilde c(t)}$ for all $t$ — if and only if $\dot{(f\circ\tilde c)}(t)=d_{\tilde c(t)}f\big(\dot{\tilde c}(t)\big)\in H^{\omega}_{f(\tilde c(t))}$ for all $t$, that is, if and only if $f\circ\tilde c$ is $\omega$-horizontal:
> $$\tilde c\text{ is } f^{*}\omega\text{-horizontal}\quad\Longleftrightarrow\quad f\circ\tilde c\text{ is } \omega\text{-horizontal} \qquad \text{(} H^{f^{*}\omega}=(df)^{-1}H^{\omega}\text{, chain rule).}$$
> Now fix $p\in P_x$ and let $\tilde c$ be the $f^{*}\omega$-horizontal lift of $c$ through $p$ (unique, by [[Thm - Existence and Uniqueness of Horizontal Lifts|existence and uniqueness of horizontal lifts]]). Then $f\circ\tilde c$ is $\omega$-horizontal and starts at $f(\tilde c(0))=f(p)$, so $f\circ\tilde c$ is the $\omega$-horizontal lift of $c$ through $f(p)$; by definition of parallel transport its endpoint is $\Gamma^{\omega}(c)(f(p))$. Therefore
> $$f\big(\tilde c(1)\big) \;=\; \Gamma^{\omega}(c)\big(f(p)\big),\qquad\text{i.e.}\qquad \Gamma^{f^{*}\omega}(c)(p)=\tilde c(1)=f^{-1}\big(\Gamma^{\omega}(c)(f(p))\big) \qquad \text{(applying } f^{-1}\text{; } \Gamma^{f^{*}\omega}(c)(p):=\tilde c(1)\text{).}$$
> As $p\in P_x$ was arbitrary, $\Gamma^{f^{*}\omega}(c)=f^{-1}\circ\Gamma^{\omega}(c)\circ f$ on $P_x$.

**Step 6: Around a loop the intertwiner becomes conjugation by $u=\hat g(p)$.**

Evaluating Step 5 on a loop at $m$ and using the equivariances of $\Gamma$ and of $\hat g$ gives $\operatorname{hol}^{f^{*}\omega}_p(\gamma)=u^{-1}\operatorname{hol}^{\omega}_p(\gamma)\,u$, hence $\rho_{f^{*}\omega}([\gamma])=u^{-1}\rho_\omega([\gamma])u$.

> [!note]- Derivation
> Let $\gamma$ be a piecewise-smooth loop at $m$ and $p\in P_m$; set $u:=\hat g(p)\in G$, so $f(p)=p\cdot u$. Write $w:=\operatorname{hol}^{\omega}_p(\gamma)\in G$, the holonomy of $\omega$, defined by $\Gamma^{\omega}(\gamma)(p)=p\cdot w$.
>
> **Apply Step 5 at $p$.** By Step 5 with $c=\gamma$ (so $x=y=m$) and by the definition of holonomy for $f^{*}\omega$,
> $$p\cdot\operatorname{hol}^{f^{*}\omega}_p(\gamma) \;=\; \Gamma^{f^{*}\omega}(\gamma)(p) \;=\; f^{-1}\Big(\Gamma^{\omega}(\gamma)\big(f(p)\big)\Big) \qquad \text{(Step 5; definition } \Gamma^{f^{*}\omega}(\gamma)(p)=p\cdot\operatorname{hol}^{f^{*}\omega}_p(\gamma)\text{).}$$
>
> **Transport the shifted point using equivariance of $\Gamma$.** Since $f(p)=p\cdot u$ and parallel transport is equivariant (property (5), $\Gamma(\gamma)\circ R_u=R_u\circ\Gamma(\gamma)$, operation 3),
> $$\Gamma^{\omega}(\gamma)\big(f(p)\big) \;=\; \Gamma^{\omega}(\gamma)(p\cdot u) \;=\; \big(\Gamma^{\omega}(\gamma)(p)\big)\cdot u \;=\; (p\cdot w)\cdot u \;=\; p\cdot(w u) \qquad \text{(equivariance of parallel transport; } \Gamma^{\omega}(\gamma)(p)=p\cdot w\text{).}$$
>
> **Invert $f$ using equivariance of $\hat g$.** The inverse gauge transformation is $f^{-1}(q)=q\cdot\hat g(q)^{-1}$: indeed $f(q\cdot\hat g(q)^{-1})=f(q)\cdot\hat g(q)^{-1}=q\,\hat g(q)\,\hat g(q)^{-1}=q$ by equivariance of $f$. Apply this at $q=p\cdot(wu)$, and evaluate $\hat g$ there by its equivariance $\hat g(p\cdot a)=a^{-1}\hat g(p)\,a$ (operation 4) with $a=wu$:
> $$\hat g\big(p\cdot(wu)\big) \;=\; (wu)^{-1}\,\hat g(p)\,(wu) \;=\; (wu)^{-1}\,u\,(wu) \qquad \text{(equivariance of } \hat g\text{; } \hat g(p)=u\text{).}$$
> Therefore
> $$f^{-1}\big(p\cdot(wu)\big) \;=\; p\cdot(wu)\cdot\hat g\big(p\cdot(wu)\big)^{-1} \;=\; p\cdot(wu)\cdot\big[(wu)^{-1}u(wu)\big]^{-1} \qquad \text{(} f^{-1}(q)=q\cdot\hat g(q)^{-1}\text{).}$$
> Simplify the group word: $\big[(wu)^{-1}u(wu)\big]^{-1}=(wu)^{-1}u^{-1}(wu)$, so
> $$f^{-1}\big(p\cdot(wu)\big) \;=\; p\cdot(wu)(wu)^{-1}u^{-1}(wu) \;=\; p\cdot u^{-1}(wu) \;=\; p\cdot\big(u^{-1}w\,u\big) \qquad \text{(cancelling } (wu)(wu)^{-1}=e\text{).}$$
>
> **Read off the holonomy.** Combining the three displays,
> $$p\cdot\operatorname{hol}^{f^{*}\omega}_p(\gamma) \;=\; p\cdot\big(u^{-1}w\,u\big),$$
> and since the right $G$-action is free (a principal action), we may cancel $p$:
> $$\operatorname{hol}^{f^{*}\omega}_p(\gamma) \;=\; u^{-1}\,w\,u \;=\; u^{-1}\,\operatorname{hol}^{\omega}_p(\gamma)\,u \qquad \text{(freeness of the principal action).}$$
>
> **Promote to representations.** Both $\omega$ and $f^{*}\omega$ are flat (Step 4), so by [[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|homotopy-invariance]] the holonomies descend to representations $\rho_\omega,\rho_{f^{*}\omega}\colon\Gamma\to G$, and the last display reads
> $$\rho_{f^{*}\omega}([\gamma]) \;=\; u^{-1}\,\rho_\omega([\gamma])\,u\qquad\text{for every }[\gamma]\in\Gamma, \qquad \text{(conjugation by the fixed } u=\hat g(p)\in G\text{).}$$
> The conjugator $u$ is independent of $[\gamma]$, so the two monodromy representations are conjugate, i.e. equal in $\mathcal R(M;G)$. This proves the principal-bundle form.

> [!note]- Complete formal solution
> **Claim.** Gauge-equivalent flat connections have conjugate monodromy representations: for a vector bundle, $\rho_{\nabla^{g}}=g(m)^{-1}\rho_\nabla\,g(m)$; for a principal bundle, $\rho_{f^{*}\omega}=u^{-1}\rho_\omega\,u$ with $u=\hat g(p)$.
>
> *Vector bundle.* Since $F_{\nabla^{g}}=g^{-1}F_\nabla g=0$, the connection $\nabla^{g}$ is flat, so $\rho_{\nabla^{g}}$ exists. For a curve $c$ from $x$ to $y$ and a section $s$ along $c$, the formula $\nabla^{g}=g^{-1}\nabla g$ gives $c^{*}\nabla^{g}=(c^{*}g)^{-1}(c^{*}\nabla)(c^{*}g)$, so $s$ is $\nabla^{g}$-parallel iff $gs$ is $\nabla$-parallel (as $g$ is fibrewise invertible). Hence, for the $\nabla^{g}$-parallel $s$ with $s(0)=v$, the section $gs$ is $\nabla$-parallel with $(gs)(0)=g(x)v$, so $g(y)PT^{\nabla^{g}}_c(v)=(gs)(1)=PT^{\nabla}_c(g(x)v)$, giving $PT^{\nabla^{g}}_c=g(y)^{-1}PT^{\nabla}_c\,g(x)$. For a loop $\gamma$ at $m$, $x=y=m$, so $PT^{\nabla^{g}}_\gamma=g(m)^{-1}PT^{\nabla}_\gamma\,g(m)$. As both connections are flat, holonomy descends to $\pi_1(M,m)$ and $\rho_{\nabla^{g}}([\gamma])=g(m)^{-1}\rho_\nabla([\gamma])g(m)$ for all $[\gamma]$; the conjugator $g(m)$ is independent of $[\gamma]$.
>
> *Principal bundle.* Since $\Omega_{f^{*}\omega}=f^{*}\Omega_\omega=0$, the connection $f^{*}\omega$ is flat, so $\rho_{f^{*}\omega}$ exists. Because $H^{f^{*}\omega}=(df)^{-1}H^{\omega}$, a curve $\tilde c$ is $f^{*}\omega$-horizontal iff $f\circ\tilde c$ is $\omega$-horizontal; hence the $f^{*}\omega$-lift of $c$ through $p$ is $f^{-1}$ of the $\omega$-lift through $f(p)$, giving $\Gamma^{f^{*}\omega}(c)=f^{-1}\circ\Gamma^{\omega}(c)\circ f$. Fix a loop $\gamma$ at $m$, $p\in P_m$, $u=\hat g(p)$, $w=\operatorname{hol}^{\omega}_p(\gamma)$. Then $\Gamma^{\omega}(\gamma)(f(p))=\Gamma^{\omega}(\gamma)(pu)=(pw)u=p(wu)$ by equivariance of parallel transport, and $f^{-1}(p(wu))=p(wu)\hat g(p(wu))^{-1}=p(wu)\big[(wu)^{-1}u(wu)\big]^{-1}=p\,u^{-1}wu$ by equivariance of $\hat g$. Thus $p\cdot\operatorname{hol}^{f^{*}\omega}_p(\gamma)=p\cdot u^{-1}wu$, and freeness of the action gives $\operatorname{hol}^{f^{*}\omega}_p(\gamma)=u^{-1}wu$. Flatness of both connections makes holonomy homotopy-invariant, so $\rho_{f^{*}\omega}([\gamma])=u^{-1}\rho_\omega([\gamma])u$ for all $[\gamma]$, with $u=\hat g(p)$ independent of $[\gamma]$.
>
> In each case the monodromy representation of the gauge-transformed connection is the conjugate of the original by a single fixed group element, so the two determine the same point of the representation variety. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to argue "curvature transforms by conjugation, $F_{\nabla^{g}}=g^{-1}F_\nabla g$, so *of course* the holonomy transforms by conjugation." This is not a proof: the transformation law for curvature is a pointwise, infinitesimal statement, whereas holonomy is a *global* object built by integrating along the whole loop, and the conjugator in the curvature law is $g(x)$ at the point $x$, which *varies along the loop*. The reason the varying conjugator collapses to the single constant $g(m)$ is exactly the endpoint cancellation of Steps 2–3 (respectively 5–6): the interior values $g(c(t))$ never appear, only the value at the base point survives. The infinitesimal law makes the result *plausible* but does not establish that the conjugator is constant; that requires the parallel-transport computation.

---

# Key Takeaways

**A gauge transformation acts on all path-integrated data by conjugation at the base point, and the interior values wash out.** The reusable principle is that whenever an invariant is built by integrating a connection along paths — parallel transport, holonomy, the monodromy representation, a Wilson loop — a gauge transformation $g$ conjugates that invariant by $g$ evaluated *at the endpoints only*. For a loop the two endpoints coincide, so the endpoint values do not cancel but combine into a single conjugation $X\mapsto g(m)^{-1}Xg(m)$; for a path between distinct points they are two different intertwiners $g(y)^{-1}(\cdot)g(x)$. The trigger condition is "an object attached to a connection is defined by transporting along curves"; the reaction is "compute how a $\nabla^{g}$-parallel object relates to a $\nabla$-parallel object by pulling the gauge through the parallel equation," which for the right action $\nabla^{g}=g^{-1}\nabla g$ is the one-line rewrite "$s$ is $\nabla^{g}$-parallel iff $gs$ is $\nabla$-parallel." This is the same mechanism that makes Wilson loops $\operatorname{tr}\operatorname{hol}(\gamma)$ gauge invariant (the trace kills the conjugation) and makes the Chern–Simons functional's dependence on gauge controlled by base-point data.

**The principal and vector-bundle computations are the same computation carried by different parallel objects.** In the vector bundle the parallel object is a section and the gauge is pulled through the covariant derivative; in the principal bundle the parallel object is the horizontal lift and the gauge is pulled through the horizontal distribution via $H^{f^{*}\omega}=(df)^{-1}H^{\omega}$. The conjugators correspond under the associated-bundle dictionary: the vector-bundle conjugator $g(m)\in GL(E_m)$ is exactly $\rho(u)$ for $E=P\times_\rho V$, where $u=\hat g(p)\in G$ is the principal conjugator. The transferable diagnostic is: when a fact is stated for vector bundles, look for the principal statement obtained by replacing "parallel section" with "horizontal lift" and "$g\in\mathcal G(E)$" with "$\hat g\colon P\to G$"; the equivariance $\hat g(pa)=a^{-1}\hat g(p)a$ is what plays the role of the fibrewise linear action of $g$. Recognising this correspondence saves proving everything twice and is the organising idea behind the whole flat-connection/monodromy dictionary.

**This lemma is the well-definedness half of the correspondence between flat connections and representations.** The map "flat connection $\mapsto$ monodromy representation" is only useful as a map on *moduli* — flat connections modulo gauge, on one side, and representations modulo conjugation, on the other — and this exercise is precisely the statement that the map is well defined on those quotients: gauge-equivalent connections land in the same conjugacy class of representations. It is the companion of the converse observation (conjugate representations give isomorphic flat bundles), and together they make the assignment $\omega\mapsto[\rho_\omega]$ a genuine bijection $\mathcal M^\flat_G(M)\to\mathcal R(M;G)$ in [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the flat-connection/monodromy theorem]]. The general lesson for spaced practice: whenever you build an invariant of a geometric object and want it to be an invariant of the object *up to symmetry*, you owe exactly a computation like this one — trace the invariant through the symmetry and check the result lands in the correct quotient. Here the symmetry is the gauge group, the quotient on the target is conjugation, and the computation is the endpoint-cancellation argument above. A companion drill is [[Ex - A Flat Connection on the Möbius Line Bundle with Holonomy Minus One]], which exhibits a concrete flat bundle whose monodromy conjugacy class is nontrivial, so that the correspondence has something to detect.
