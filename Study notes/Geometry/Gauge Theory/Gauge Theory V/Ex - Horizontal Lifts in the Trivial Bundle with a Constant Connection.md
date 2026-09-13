---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Existence and Uniqueness of Horizontal Lifts"
  - "Def - Connection on a Principal Bundle"
  - "Def - Horizontal Subspace and Horizontal Lift"
  - "Def - Local Connection Form and Gauge Potential"
  - "Def - The Maurer-Cartan Form"
  - "Def - Parallel Transport in a Principal Bundle"
  - "Def - Flat Connection"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $P=\mathbb{R}^2\times U(1)$ be the trivial principal $U(1)$-bundle over the plane, with projection $\pi(x,y,g)=(x,y)$ and the right action $R_g(x,y,h)=(x,y,hg)$. Write the Lie algebra of $U(1)$ as $\mathfrak{u}(1)=i\mathbb{R}$, and let $s_0\colon\mathbb{R}^2\to P$, $s_0(x,y)=((x,y),1)$, be the constant unit section. Fix two real constants $a,b\in\mathbb{R}$ and give $P$ the connection $\omega$ whose local connection form in the gauge $s_0$ is the constant $\mathfrak{u}(1)$-valued one-form
$$A:=s_0^{*}\omega=i\,(a\,dx+b\,dy)\in\Omega^1(\mathbb{R}^2;\mathfrak{u}(1)).$$

1. **(Straight segment.)** For a target point $(x_1,y_1)\in\mathbb{R}^2$, let $c(t)=(t\,x_1,\,t\,y_1)$, $t\in[0,1]$, be the segment from the origin to $(x_1,y_1)$. Compute the horizontal lift $\tilde c$ of $c$ starting at $\tilde c(0)=((0,0),1)$, and read off the parallel transport $\Gamma_c\colon P_{(0,0)}\to P_{(x_1,y_1)}$. Show that, expressed as multiplication in the trivialising gauge $s_0$, it is the group element $e^{-i(ax_1+by_1)}\in U(1)$.
2. **(Unit square loop.)** Let $\square$ be the boundary of the unit square, the loop based at the origin running $0\to(1,0)\to(1,1)\to(0,1)\to0$ along the four edges. Compute the holonomy of $\omega$ around $\square$ — the group element $g\in U(1)$ for which the horizontal lift through $((0,0),1)$ closes up at $((0,0),g)$ — and show it is $g=1$. Explain this by showing that $\omega$ is flat.
3. **(A non-flat variant.)** Replace $A$ by $A'=i\,x\,dy$ (that is, $a$ and $b$ are no longer constant: the coefficient of $dy$ is the coordinate function $x$, and the coefficient of $dx$ is zero). Recompute the holonomy of the resulting connection $\omega'$ around the same unit square loop $\square$, and show it is $e^{-i}$. Confirm that $\omega'$ is not flat, and that the answer agrees with the flux of the curvature through the square.

**Recall:**

The only substantial tool is the existence-and-uniqueness theorem for horizontal lifts, together with the first-order ordinary differential equation it reduces horizontality to. Everything else is the definition of the connection form on a trivial bundle and the definition of parallel transport.

![[Thm - Existence and Uniqueness of Horizontal Lifts#Statement]]

We use this in the shape it takes for the structure group $U(1)$. Since $U(1)$ is abelian, its adjoint representation is trivial and the reduction equation $(2.9)$ above simplifies: writing the fibre coordinate of the lift as $h(t)=e^{i\psi(t)}\in U(1)$ and the local form as $A_\alpha=i\,\alpha$ with $\alpha$ a real one-form, horizontality becomes $\dot\psi(t)=-\alpha(\dot c(t))$, a scalar equation solved by direct integration.

![[Def - Local Connection Form and Gauge Potential#The Definition]]

The local connection form of $\omega$ in a local section $s$ is $A_s:=s^{*}\omega\in\Omega^1(U;\mathfrak{g})$, the pullback of the connection one-form along the section; it is the "gauge potential" of the physics literature. On a trivial bundle a global section exists, so a single global $A$ determines $\omega$.

![[Def - The Maurer-Cartan Form#The Definition]]

The **[[Def - The Maurer-Cartan Form|Maurer–Cartan form]]** $\theta\in\Omega^1(G;\mathfrak{g})$ is $\theta_g=(dL_{g^{-1}})_g$, the left-translation of tangent vectors back to the identity; for the matrix group $U(1)$ it is $\theta=g^{-1}dg$, and in the angle coordinate $g=e^{i\psi}$ it is $\theta=i\,d\psi$.

![[Def - Parallel Transport in a Principal Bundle#The Definition]]

**Parallel transport** along a curve $c$ from $c(t_0)$ to $c(t_1)$ is the map $\Gamma_c\colon P_{c(t_0)}\to P_{c(t_1)}$, $\Gamma_c(p)=\tilde c(t_1)$, where $\tilde c$ is the horizontal lift of $c$ through $p$. For a loop it is an endomorphism of a single fibre, and because the lift is equivariant ($\widetilde{c}\cdot g$ is the lift through $p\cdot g$) it commutes with the right action, so on a fibre $P_m\cong U(1)$ it is right multiplication by a fixed group element — the holonomy.

![[Def - Flat Connection#The Definition]]

A connection is **[[Def - Flat Connection|flat]]** when its curvature vanishes, $F=0$. For a $U(1)$-connection with global potential $A=i\alpha$ the curvature is the global two-form $F=dA=i\,d\alpha$, so flatness is exactly $d\alpha=0$: the real one-form $\alpha$ is closed.

---

# Convergent Strategy

**Problem class.** This is the most basic *compute-a-horizontal-lift* problem: a trivial bundle, an explicitly given constant potential, and curves for which the reduction equation can be integrated in closed form. Its purpose is to make the abstract statement of [[Thm - Existence and Uniqueness of Horizontal Lifts|the horizontal-lift theorem]] concrete and to expose, in the simplest possible arena, the single mechanism that governs all of parallel transport: *horizontality is a first-order ordinary differential equation for the fibre coordinate, driven by the value of the local connection form along the curve.* The three parts move from an open path (nontrivial transport, no invariant), to a loop with a closed potential (trivial holonomy, flatness), to a loop with a non-closed potential (nontrivial holonomy measuring an enclosed flux).

**Assumption pattern.** Two features make the computation trivial to carry out and are worth naming because their *failure* is what makes the general theory hard. First, the bundle is trivial, so there is a global gauge $s_0$ and a single global potential $A$; no patching of local forms is needed. Second, the structure group $U(1)$ is abelian, so the reduction equation is scalar and its solution is a plain integral $\psi(t)=\psi(0)-\int_0^t\alpha(\dot c)\,d\tau$ with no ordering of non-commuting factors. The recognisable trigger for "the lift is an ordinary integral of the potential" is precisely *abelian structure group on a trivial bundle*; the moment either hypothesis is dropped one needs the path-ordered exponential instead.

**Theorem routing.** The route is uniform across all three parts. Set up the connection one-form on the trivial bundle as $\omega=\pi^{*}A+\operatorname{pr}_2^{*}\theta$; write a lift as $\tilde c(t)=(c(t),e^{i\psi(t)})$; impose $\omega(\dot{\tilde c})=0$ to obtain $\dot\psi=-\alpha(\dot c)$ — this is the $U(1)$ form of equation $(2.9)$ from [[Thm - Existence and Uniqueness of Horizontal Lifts|the lift theorem]]; integrate. For the open segment the integral is $ax_1+by_1$; for a loop it is the line integral $\oint_\square\alpha$, which [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] rewrites as the flux $\int_S d\alpha$ of the curvature through any bounding surface $S$. Flatness ($d\alpha=0$) makes the loop integral vanish; a nonzero curvature makes it the enclosed area.

**Key decision point.** The one genuine decision is *how to package the lift*. Writing the fibre coordinate multiplicatively as $h(t)\in U(1)$ and then in the angle chart as $h=e^{i\psi}$ turns the equivariant reduction equation $\dot h=-A(\dot c)\,h$ into the additive scalar equation $\dot\psi=-\alpha(\dot c)$, which integrates immediately. The temptation to avoid is treating the loop integral as automatically zero "because $A$ is a total derivative": that is true for a constant potential (part 2) and false for $A'=i\,x\,dy$ (part 3), and the discriminating quantity is not whether $A$ looks like a differential of something but whether $d\alpha=0$ — that is, whether the connection is flat.

---

# Legal Operations Used

The solution uses the following operations; where the section-§5.1 topic page numbers them, these correspond to the operations on constructing and integrating horizontal lifts.

1. **Write the connection one-form of a trivial bundle from its global potential.** On $P=M\times G$ with global section $s_0$ and potential $A=s_0^{*}\omega$, the connection is $\omega=\operatorname{Ad}_{g^{-1}}\pi^{*}A+\operatorname{pr}_2^{*}\theta$; for abelian $G$ this is $\omega=\pi^{*}A+\operatorname{pr}_2^{*}\theta$. This turns "a connection" into a one-line formula that can be evaluated on tangent vectors.

2. **Reduce horizontality to the fibre ordinary differential equation.** Parametrise a lift as $\tilde c(t)=(c(t),h(t))$ and impose $\omega(\dot{\tilde c})=0$; this is operation "reduce a lift to equation $(2.9)$" from [[Thm - Existence and Uniqueness of Horizontal Lifts|the lift theorem]]. For $U(1)$ in the angle chart the equation is $\dot\psi=-\alpha(\dot c)$.

3. **Integrate the fibre equation along an explicit curve.** With the potential and the curve both given explicitly, solve $\dot\psi=-\alpha(\dot c)$ by direct integration, using $\psi(0)$ from the prescribed starting fibre point.

4. **Concatenate lifts over a piecewise curve.** For the square loop, lift each of the four edges in turn, using the endpoint of one edge's lift as the starting point of the next; this is the concatenation clause of [[Thm - Existence and Uniqueness of Horizontal Lifts|the lift theorem]] (its part on piecewise smooth curves).

5. **Read parallel transport and holonomy off the lift.** By the definition of [[Def - Parallel Transport in a Principal Bundle|parallel transport]], the endpoint of the lift *is* the transported point; for a loop the closing group element is the holonomy.

6. **Convert a loop integral of the potential into a curvature flux by Stokes.** For a loop $\square=\partial S$, rewrite $\oint_\square\alpha=\int_S d\alpha$ using [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]]; the integrand $d\alpha$ is the (real part of the) curvature, so the holonomy sees the enclosed flux.

---

# Hints

> [!note]- Hint 1
> On the trivial bundle the connection has a single global formula. If $g=e^{i\psi}$ is the fibre coordinate and $\theta=i\,d\psi$ is the Maurer–Cartan form, then $\omega=\pi^{*}A+\operatorname{pr}_2^{*}\theta$. Evaluate $\omega$ on the velocity of a candidate lift $\tilde c(t)=(c(t),e^{i\psi(t)})$ and set it to zero. What ordinary differential equation for $\psi$ do you get?

> [!note]- Hint 2
> You should have found $\dot\psi(t)=-\alpha(\dot c(t))$, where $A=i\alpha$. For the segment this is a constant, so $\psi$ is linear in $t$. For a loop, integrate edge by edge; the total change in $\psi$ is $-\oint_\square\alpha$. Remember the fibre coordinate starts at $\psi(0)=0$ because the lift starts at $((0,0),1)$.

> [!note]- Hint 3
> For part 2 the potential is $A=i(a\,dx+b\,dy)$ with $a,b$ constant, so $\alpha=a\,dx+b\,dy=d(ax+by)$ is closed: $\oint_\square\alpha=0$. For part 3, $A'=i\,x\,dy$ gives $\alpha'=x\,dy$ with $d\alpha'=dx\wedge dy\neq0$. Do not expect the loop integral to vanish; compute it directly (only the two vertical edges contribute), or use Stokes: $\oint_\square x\,dy=\int_{[0,1]^2}dx\wedge dy=1$.

---

# Solution

The whole computation rests on one reduction: on the trivial $U(1)$-bundle the connection one-form is $\omega=\pi^{*}A+\operatorname{pr}_2^{*}\theta$, and a curve $\tilde c(t)=(c(t),e^{i\psi(t)})$ is horizontal exactly when $\dot\psi=-\alpha(\dot c)$, where $A=i\alpha$. Once this scalar equation is in hand, each part is an integral: the segment gives the linear accumulation $ax_1+by_1$; the square with a closed potential gives zero (flatness); the square with the potential $x\,dy$ gives the enclosed area, $1$.

**Step 0: The connection one-form on the trivial bundle, and the reduction to a scalar equation.**

We record the global formula for $\omega$ and reduce horizontality to $\dot\psi=-\alpha(\dot c)$.

> [!note]- Derivation
> A connection on the trivial bundle $P=\mathbb{R}^2\times U(1)$ is determined by its potential $A=s_0^{*}\omega$ in the global gauge $s_0(x,y)=((x,y),1)$, through the reconstruction formula for a trivial bundle (the local-form definition, [[Def - Local Connection Form and Gauge Potential|local connection form]]):
> $$\omega_{(x,y,g)}=\operatorname{Ad}_{g^{-1}}\big(\pi^{*}A\big)+\operatorname{pr}_2^{*}\theta\qquad\text{(reconstruction of }\omega\text{ from }A\text{ on a trivial bundle)}.$$
> Here $\theta$ is the [[Def - The Maurer-Cartan Form|Maurer–Cartan form]] of $U(1)$ and $\operatorname{pr}_2\colon P\to U(1)$ the second projection. Because $U(1)$ is **abelian**, its adjoint representation is trivial, $\operatorname{Ad}_{g^{-1}}=\operatorname{id}$, so
> $$\omega=\pi^{*}A+\operatorname{pr}_2^{*}\theta\qquad(\text{triviality of }\operatorname{Ad}\text{ for abelian }U(1)).$$
> Write the fibre coordinate as $g=e^{i\psi}$; then $\theta=g^{-1}dg=i\,d\psi$ (Maurer–Cartan form of $U(1)$ in the angle chart), and with $A=i\alpha$ for the real one-form $\alpha$,
> $$\omega=i\big(\pi^{*}\alpha+d\psi\big)\qquad(\text{substituting }A=i\alpha,\ \theta=i\,d\psi).$$
> Now take any lift $\tilde c(t)=(c(t),e^{i\psi(t)})$ of a curve $c$ in the base; its velocity has base part $\dot c(t)$ and fibre part $\dot\psi(t)\,\partial_\psi$. Evaluate:
> $$\omega(\dot{\tilde c}(t))=i\big(\alpha(\dot c(t))+\dot\psi(t)\big)\qquad(\text{applying }\omega\text{ to }\dot{\tilde c},\ \pi^{*}\alpha(\dot{\tilde c})=\alpha(\dot c)).$$
> By definition of the [[Def - Horizontal Subspace and Horizontal Lift|horizontal subspace]], $\dot{\tilde c}(t)\in H_{\tilde c(t)}=\ker\omega_{\tilde c(t)}$ if and only if this vanishes, that is
> $$\dot\psi(t)=-\alpha(\dot c(t))\qquad(\text{horizontality condition}).\tag{$\ast$}$$
> This is exactly equation $(2.9)$ of [[Thm - Existence and Uniqueness of Horizontal Lifts|the horizontal-lift theorem]] in the $U(1)$ case: there the matrix form is $\dot h=-A(\dot c)\,h$, and with $h=e^{i\psi}$, $\dot h=i\dot\psi\,e^{i\psi}$, while $A(\dot c)\,h=i\,\alpha(\dot c)\,e^{i\psi}$, so $i\dot\psi=-i\,\alpha(\dot c)$, which is $(\ast)$. The theorem guarantees that the solution of $(\ast)$ with a prescribed initial value exists and is unique on the whole parameter interval, so the lifts we now write down are *the* horizontal lifts.

**Step 1: Horizontal lift of the segment and the parallel transport $\Gamma_c$.**

For $c(t)=(t\,x_1,\,t\,y_1)$ and $A=i(a\,dx+b\,dy)$, equation $(\ast)$ integrates to $\psi(t)=-t(ax_1+by_1)$, giving parallel transport by the element $e^{-i(ax_1+by_1)}$.

> [!note]- Derivation
> Here $\alpha=a\,dx+b\,dy$ with $a,b$ constant, and $\dot c(t)=(x_1,y_1)$ is the constant velocity of the segment. Hence
> $$\alpha(\dot c(t))=a\,x_1+b\,y_1\qquad(\text{evaluating }a\,dx+b\,dy\text{ on }(x_1,y_1)),$$
> a constant in $t$. Equation $(\ast)$ becomes $\dot\psi(t)=-(a x_1+b y_1)$. The lift starts at $\tilde c(0)=((0,0),1)$, so $\psi(0)=0$; integrating the constant right-hand side,
> $$\psi(t)=\psi(0)-\int_0^{t}(a x_1+b y_1)\,d\tau=-\,t\,(a x_1+b y_1)\qquad(\text{integration of a constant, }\psi(0)=0).$$
> Therefore the horizontal lift is
> $$\tilde c(t)=\Big((t x_1,\,t y_1),\ e^{-\,i\,t\,(a x_1+b y_1)}\Big),\qquad t\in[0,1],$$
> and at the endpoint $t=1$,
> $$\tilde c(1)=\Big((x_1,y_1),\ e^{-\,i\,(a x_1+b y_1)}\Big).$$
> By the definition of [[Def - Parallel Transport in a Principal Bundle|parallel transport]], $\Gamma_c\colon P_{(0,0)}\to P_{(x_1,y_1)}$ sends the starting fibre point to this endpoint: $\Gamma_c\big((0,0),1\big)=\big((x_1,y_1),e^{-i(a x_1+b y_1)}\big)$. To see it as a group element, use equivariance (part 3 of the lift theorem): for any $g\in U(1)$ the lift through $((0,0),g)$ is $\tilde c\cdot g$, so
> $$\Gamma_c\big((0,0),g\big)=\big((x_1,y_1),\ e^{-i(a x_1+b y_1)}\,g\big)\qquad(\text{equivariance of the lift}).$$
> Reading both fibres off through the global gauge $s_0$ (identify $P_{(0,0)}\cong U(1)\cong P_{(x_1,y_1)}$ by the second coordinate), $\Gamma_c$ is left multiplication by the fixed element
> $$\boxed{\;\Gamma_c=e^{-i(a x_1+b y_1)}\in U(1).\;}$$
> The transport is nontrivial and depends on the endpoint through the linear form $a x_1+b y_1$, as expected for a nonzero constant potential.

**Step 2: Holonomy around the unit square is $1$; the connection is flat.**

Lifting the four edges in turn and accumulating $\psi$, the changes cancel and the lift closes up, giving holonomy $1$; this reflects $d\alpha=0$.

> [!note]- Derivation
> By the concatenation clause of [[Thm - Existence and Uniqueness of Horizontal Lifts|the lift theorem]], the lift of the piecewise smooth loop $\square$ is obtained edge by edge, each edge starting where the previous ended. The total change in $\psi$ over the loop is
> $$\Delta\psi=-\oint_{\square}\alpha=-\oint_{\square}(a\,dx+b\,dy)\qquad(\text{integrating }(\ast)\text{ over }\square).$$
> Compute the four edge integrals of $\alpha=a\,dx+b\,dy$ (parametrise each edge on $[0,1]$):
> $$\text{edge }0\to(1,0)\colon\ \dot c=(1,0),\ \textstyle\int_0^1 a\,d\tau=a;\qquad (1,0)\to(1,1)\colon\ \dot c=(0,1),\ \int_0^1 b\,d\tau=b;$$
> $$(1,1)\to(0,1)\colon\ \dot c=(-1,0),\ \textstyle\int_0^1(-a)\,d\tau=-a;\qquad (0,1)\to0\colon\ \dot c=(0,-1),\ \int_0^1(-b)\,d\tau=-b.$$
> Adding, $\oint_\square\alpha=a+b-a-b=0$, so $\Delta\psi=0$ and $\psi$ returns to its starting value. Hence the horizontal lift through $((0,0),1)$ closes at $((0,0),e^{i\cdot0})=((0,0),1)$, and the holonomy is
> $$\boxed{\;g=1\in U(1).\;}$$
> This is forced by **flatness**. The curvature of $\omega$ is the global two-form $F=dA=i\,d(a\,dx+b\,dy)=0$ because $a,b$ are constant (the exterior derivative of a constant-coefficient one-form vanishes). So $\omega$ is a [[Def - Flat Connection|flat connection]]. Equivalently $\alpha=d(ax+by)$ is exact, so its integral around any loop vanishes: the holonomy of *every* loop, not just the square, is trivial for this connection.

**Step 3: With $A'=i\,x\,dy$ the holonomy is $e^{-i}$, matching the curvature flux.**

Now only the two vertical edges contribute to $\oint\square\alpha'$, giving total $1$; the holonomy is $e^{-i}$, and Stokes identifies it with the flux of the non-vanishing curvature through the square.

> [!note]- Derivation
> With $A'=i\,x\,dy$ we have $\alpha'=x\,dy$, so $\alpha'(\dot c)=x(t)\,\dot y(t)$ along a curve. Equation $(\ast)$ reads $\dot\psi=-x\,\dot y$. Integrate edge by edge over $\square$:
> $$\text{edge }0\to(1,0)\colon\ \dot y=0,\ \textstyle\int_0^1 x\,\dot y\,d\tau=0;\qquad (1,0)\to(1,1)\colon\ x\equiv1,\ \dot y=1,\ \int_0^1 1\cdot1\,d\tau=1;$$
> $$(1,1)\to(0,1)\colon\ \dot y=0,\ \textstyle\int_0^1 x\,\dot y\,d\tau=0;\qquad (0,1)\to0\colon\ x\equiv0,\ \int_0^1 0\cdot(-1)\,d\tau=0.$$
> Hence $\oint_\square\alpha'=0+1+0+0=1$, so $\Delta\psi=-\oint_\square\alpha'=-1$, and the lift through $((0,0),1)$ closes at $((0,0),e^{-i})$. The holonomy is
> $$\boxed{\;g=e^{-i}\in U(1).\;}$$
> This connection is **not flat**: its curvature is
> $$F'=dA'=i\,d(x\,dy)=i\,dx\wedge dy\neq0\qquad(\text{exterior derivative of }x\,dy).$$
> The holonomy is exactly the flux of $F'$ through the square, by [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] — *if $S$ is a compact oriented surface with boundary $\partial S$, then $\int_S d\eta=\oint_{\partial S}\eta$ for every one-form $\eta$*:
> $$\oint_\square\alpha'=\int_{[0,1]^2}d\alpha'=\int_{[0,1]^2}dx\wedge dy=1\qquad(\text{Stokes, then }\textstyle\int_{[0,1]^2}dx\wedge dy=\text{area}=1),$$
> and correspondingly $g=\exp\!\big(-\!\oint_\square\alpha'\big)=\exp\!\big(-\!\int_{[0,1]^2}\tfrac1i F'\big)=e^{-i}$. The nonzero holonomy of the small loop is precisely the curvature it encloses; this is the abelian case of the general fact that curvature is the infinitesimal holonomy, and it is why a constant potential (part 2) transports trivially while $x\,dy$ (part 3) does not.

> [!note]- Complete formal solution
> **Setup.** On $P=\mathbb{R}^2\times U(1)$ with global gauge $s_0(x,y)=((x,y),1)$ and potential $A=s_0^{*}\omega=i\alpha$ ($\alpha$ a real one-form), triviality of $\operatorname{Ad}$ for abelian $U(1)$ gives the connection one-form $\omega=\pi^{*}A+\operatorname{pr}_2^{*}\theta=i(\pi^{*}\alpha+d\psi)$ in the angle coordinate $g=e^{i\psi}$. A lift $\tilde c(t)=(c(t),e^{i\psi(t)})$ satisfies $\omega(\dot{\tilde c})=i(\alpha(\dot c)+\dot\psi)$, so it is horizontal if and only if
> $$\dot\psi(t)=-\alpha(\dot c(t)),$$
> which is the $U(1)$ form of the reduction equation $(2.9)$ of [[Thm - Existence and Uniqueness of Horizontal Lifts|the horizontal-lift theorem]]; that theorem gives existence and uniqueness of the solution on the whole interval.
>
> **Part 1.** For $A=i(a\,dx+b\,dy)$ ($a,b$ constant) and the segment $c(t)=(tx_1,ty_1)$, $\alpha(\dot c)=ax_1+by_1$ is constant, so with $\psi(0)=0$, $\psi(t)=-t(ax_1+by_1)$ and $\tilde c(t)=((tx_1,ty_1),e^{-it(ax_1+by_1)})$. Thus $\Gamma_c((0,0),g)=((x_1,y_1),e^{-i(ax_1+by_1)}g)$, i.e. parallel transport is the group element
> $$\Gamma_c=e^{-i(ax_1+by_1)}\in U(1).$$
>
> **Part 2.** For the unit square loop $\square$, the total change is $\Delta\psi=-\oint_\square(a\,dx+b\,dy)$. The four edge integrals are $a,\,b,\,-a,\,-b$, summing to $0$, so $\Delta\psi=0$ and the holonomy is $g=1$. This is flatness: $F=dA=i\,d(a\,dx+b\,dy)=0$ since $a,b$ are constant; equivalently $\alpha=d(ax+by)$ is exact, so every loop has trivial holonomy.
>
> **Part 3.** For $A'=i\,x\,dy$, the equation is $\dot\psi=-x\dot y$. Over $\square$ only the edge $(1,0)\to(1,1)$ (where $x\equiv1$, $\dot y=1$) contributes, giving $\oint_\square x\,dy=1$; hence $\Delta\psi=-1$ and the holonomy is
> $$g=e^{-i}\in U(1).$$
> The connection is not flat: $F'=dA'=i\,dx\wedge dy\neq0$. By [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]], $\oint_\square x\,dy=\int_{[0,1]^2}dx\wedge dy=1$, so the holonomy equals the flux of the curvature through the square, $g=\exp(-\int_{[0,1]^2}\tfrac1i F')=e^{-i}$. $\blacksquare$

> [!warning] Illegal but tempting: "the potential is a total derivative, so every loop integral is zero."
> In part 2 this reasoning happens to give the right answer, and it is tempting to carry it over to part 3 by writing $x\,dy=d(xy)-y\,dx$ and hoping the loop integral vanishes. It does not: $d(xy)$ integrates to zero around a loop, but the *remaining* piece $-y\,dx$ does not, and $\oint_\square x\,dy=-\oint_\square y\,dx=1$. The discriminating condition is not whether $\alpha$ can be written with a $d(\cdot)$ term but whether $\alpha$ is **closed** ($d\alpha=0$), equivalently whether the connection is flat. A constant potential is closed; $x\,dy$ is not, since $d(x\,dy)=dx\wedge dy\neq0$.

---

# Key Takeaways

**Horizontality is a first-order ordinary differential equation for the fibre coordinate, driven by the local connection form along the curve.** This is the single mechanism behind every parallel-transport computation, and this exercise is its cleanest instance. On any principal bundle the reduction is $\dot h=-\,dR_h(A_\alpha(\dot c))$; for a matrix group it linearises to $\dot h=-A_\alpha(\dot c)\,h$, and for the abelian group $U(1)$ in the angle chart it collapses to the scalar $\dot\psi=-\alpha(\dot c)$, an equation one integrates by inspection. The trigger to reach for this reduction is any request to "transport" a frame, a fibre point, or a section along a given curve: convert the geometry into the local potential $A_\alpha$, evaluate it on the velocity, and solve the resulting ordinary differential equation with the prescribed initial fibre point. Everything downstream — parallel transport, holonomy, the monodromy of a flat connection — is a corollary of solving this one equation and reading off its endpoint.

**On an abelian bundle the transport is the ordinary exponential of the line integral of the potential, and around a loop that line integral is a curvature flux.** Because $U(1)$ is commutative there is no ordering to worry about, so the solution of $\dot\psi=-\alpha(\dot c)$ is the plain integral $\psi(t)=\psi(0)-\int_0^t\alpha(\dot c)\,d\tau$, and the holonomy of a loop is $\exp(-\oint\alpha)$. Stokes' theorem then turns the loop integral into $\int_S d\alpha=\int_S(\tfrac1i F)$, the flux of the curvature through any bounding surface. The two loops in this exercise are the two ends of that dictionary: a constant potential is closed, so its curvature is zero and every loop transports trivially (flatness); the potential $x\,dy$ has curvature $dx\wedge dy$, so the unit square transports by $e^{-i}=\exp(-\text{area})$. This is the abelian shadow of the general theorem that *curvature is the infinitesimal holonomy*, and it is the computation that underlies Dirac's quantisation condition and the Aharonov–Bohm phase, where the "area" is replaced by a magnetic flux.

**Flatness, not the surface appearance of the potential, decides whether transport sees only endpoints.** The pedagogically important contrast is parts 2 and 3: both potentials are genuine one-forms on the same trivial bundle, both loops are the same unit square, yet one has trivial and the other nontrivial holonomy. The invariant that separates them is closedness of $\alpha$, equivalently $F=0$. When the connection is flat, the line integral of the potential depends only on the endpoints of the path (it is path-independent on a simply connected base), so parallel transport factors through the endpoints and, on a simply connected base, is entirely trivial; the holonomy then measures only the topology of the loop, which is the content of the monodromy correspondence for flat connections. When the connection is not flat, the holonomy of a contractible loop is already nonzero and equals the enclosed curvature, so transport genuinely depends on the whole path. The diagnostic to carry away: before computing any loop holonomy, check whether $d\alpha=0$; if it is, expect endpoints to be all that matter, and if it is not, expect an area. The companion exercise [[Ex - Parallel Transport in the Hopf Bundle along a Great Circle]] runs the same machinery on a genuinely non-trivial bundle, where even a great circle bounding half the sphere transports by $-1$.
