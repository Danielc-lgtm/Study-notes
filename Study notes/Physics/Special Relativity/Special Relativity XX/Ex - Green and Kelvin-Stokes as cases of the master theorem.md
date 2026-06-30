---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Stokes Theorem on Spacetime"
  - "Def - The Exterior Derivative"
  - "Def - Alternate Forms and the Exterior Product"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$ and signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$.

1. **Fundamental theorem of calculus ($p=1$).** For a curve $\mathscr{V}$ along the $z$-axis ($t=x=y=0$, $a\le z\le b$) and a scalar field $A = f$, apply Stokes' theorem $\int_{\mathscr{V}}\mathrm{d}A = \int_{\partial\mathscr{V}} A$ and show it reduces to $\int_a^b\frac{\partial f}{\partial z}\,\mathrm{d}z = f(B) - f(A)$.
2. **Green–Riemann formula ($p=2$).** For a planar region $\mathscr{V}$ in the $t=z=0$ plane and the 1-form $A = P(x,y)\,\mathrm{d}x + Q(x,y)\,\mathrm{d}y$, compute $\mathrm{d}A$ and apply Stokes to recover $\int_{\mathscr{V}}\left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\mathrm{d}x\,\mathrm{d}y = \oint_{\partial\mathscr{V}} P\,\mathrm{d}x + Q\,\mathrm{d}y$.
3. **Kelvin–Stokes curl theorem ($p=2$).** For a spacelike 2-surface $\mathscr{V}$ in a slice and a 1-form $A$ dual to a spatial vector field $\vec{A}$, identify the surviving component of $\mathrm{d}A$ as a component of $\mathrm{curl}\,\vec{A}$ and recover $\int_{\mathscr{V}}\mathrm{curl}\,\vec{A}\cdot\mathrm{d}\vec{S} = \oint_{\partial\mathscr{V}}\vec{A}\cdot\mathrm{d}\vec{\ell}$.
4. State which component of $\mathrm{d}A$ each classical theorem "reads off", and explain how div, grad, curl are the exterior derivative in disguise.

**Recall:**

Stokes' theorem and the exterior derivative are as follows.

![[Thm - Stokes Theorem on Spacetime#Statement]]

The exterior derivative of a $0$-form (scalar) $f$ is the 1-form $\mathrm{d}f = \partial_\mu f\,\mathrm{d}x^\mu$. The exterior derivative of a 1-form $A = A_\mu\,\mathrm{d}x^\mu$ is the 2-form $\mathrm{d}A = \partial_\mu A_\nu\,\mathrm{d}x^\mu\wedge\mathrm{d}x^\nu = \sum_{\mu<\nu}(\partial_\mu A_\nu - \partial_\nu A_\mu)\,\mathrm{d}x^\mu\wedge\mathrm{d}x^\nu$. See [[Def - The Exterior Derivative]].

---

# Convergent Strategy

**Problem class.** A *recover-a-classical-theorem* problem: specialise the master identity $\int_{\mathscr{V}}\mathrm{d}A = \int_{\partial\mathscr{V}} A$ to low dimensions and particular forms to obtain the named theorems of vector calculus. It demonstrates the unifying claim of [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem#Bridges|the chapter]] that div, grad, curl, and their integral theorems are one theorem.

**Assumption pattern.** A low-dimensional region and a form of a specified type. The signpost is the dimension $p$ and the degree of $A$: $p=1$ with a scalar gives FTC, $p=2$ with a 1-form gives Green or Kelvin–Stokes. The work is computing $\mathrm{d}A$ and recognising the classical "derivative" inside it.

**Theorem routing.** Each part applies [[Thm - Stokes Theorem on Spacetime]] with a particular $A$, then computes $\mathrm{d}A$ via [[Def - The Exterior Derivative]] and reads off the classical operator (gradient component, the combination $\partial_x Q - \partial_y P$, a curl component).

**Key decision point.** The instructive choice is to see that the *same* Stokes theorem produces all three classical theorems, distinguished only by the dimension and the form's degree. The recognition step — identifying $\partial_x Q - \partial_y P$ as the relevant curl/Green combination and $\partial_2 A_3 - \partial_3 A_2$ as a Cartesian curl component — is where the classical operators emerge from the exterior derivative.

---

# Legal Operations Used

1. **Operation 5 from the topic page (apply Stokes' theorem to trade $\mathrm{d}$ for $\partial$).** Each part is a direct application of Stokes' theorem to a particular form on a particular region.

2. **Operation 2 from the topic page (integrate a $p$-form by reading off its single tangential component).** The boundary integrals $\int_{\partial\mathscr{V}} A$ and the bulk integrals $\int_{\mathscr{V}}\mathrm{d}A$ are evaluated by extracting the appropriate component of $A$ and $\mathrm{d}A$.

---

# Hints

> [!note]- Hint 1
> For $p=1$ with $A = f$: $\mathrm{d}f = \partial_z f\,\mathrm{d}z$ along the curve, so $\int_{\mathscr{V}}\mathrm{d}f = \int_a^b\partial_z f\,\mathrm{d}z$. The boundary $\partial\mathscr{V} = \{B\} - \{A\}$ (endpoint $B$ positive, $A$ negative by the induced orientation), so $\int_{\partial\mathscr{V}} f = f(B) - f(A)$.

> [!note]- Hint 2
> For $A = P\,\mathrm{d}x + Q\,\mathrm{d}y$: $\mathrm{d}A = (\partial_x Q - \partial_y P)\,\mathrm{d}x\wedge\mathrm{d}y$ (the $\partial_x P\,\mathrm{d}x\wedge\mathrm{d}x$ and $\partial_y Q\,\mathrm{d}y\wedge\mathrm{d}y$ terms vanish). Stokes gives $\int_{\mathscr{V}}(\partial_x Q - \partial_y P)\,\mathrm{d}x\,\mathrm{d}y = \oint_{\partial\mathscr{V}} P\,\mathrm{d}x + Q\,\mathrm{d}y$.

> [!note]- Hint 3
> For the curl theorem on a surface in a slice with $A = A_i\,\mathrm{d}x^i$: the surviving component of $\mathrm{d}A$ on the surface is $\partial_2 A_3 - \partial_3 A_2$, which is the $x^1$-component of $\mathrm{curl}\,\vec{A}$. With $\mathrm{d}x^2\wedge\mathrm{d}x^3$ the area element, this is $\mathrm{curl}\,\vec{A}\cdot\mathrm{d}\vec{S}$, and the boundary integral is $\oint\vec{A}\cdot\mathrm{d}\vec{\ell}$.

> [!note]- Hint 4
> Each theorem reads off one piece of $\mathrm{d}A$: FTC reads the gradient $\partial_z f$ (the $z$-component of $\mathrm{d}f$); Green reads $\partial_x Q - \partial_y P$; Kelvin–Stokes reads the curl component. So gradient = $\mathrm{d}$ on a $0$-form, curl = $\mathrm{d}$ on a 1-form (dualised), divergence = $\mathrm{d}$ on a 2-form (dualised).

---

# Solution

All three classical theorems are the single identity $\int_{\mathscr{V}}\mathrm{d}A = \int_{\partial\mathscr{V}} A$ specialised by dimension and form-degree. The plan: $p=1$ with a scalar gives FTC; $p=2$ with a 1-form on a plane gives Green; $p=2$ with a 1-form on a surface gives Kelvin–Stokes; then read off which derivative each extracts.

**Step 1: The fundamental theorem of calculus.**

> [!note]- Derivation
> Take the curve $\mathscr{V}$ along the $z$-axis, $t=x=y=0$, $a\le z\le b$, with $A = f$ a scalar ($0$-form). Its exterior derivative is the 1-form $\mathrm{d}f = \partial_\mu f\,\mathrm{d}x^\mu$, and along the curve (where only $z$ varies) the integral picks out the $z$-component: $\int_{\mathscr{V}}\mathrm{d}f = \int_a^b(\mathrm{d}f)_z\,\mathrm{d}z = \int_a^b\partial_z f\,\mathrm{d}z$. The boundary $\partial\mathscr{V}$ is the two-point set $\{B\} - \{A\}$, where $B = (0,0,0,b)$ carries $+$ and $A = (0,0,0,a)$ carries $-$ (the induced outward-normal-first orientation: at the upper endpoint the outward direction is $+z$, at the lower it is $-z$). So $\int_{\partial\mathscr{V}} f = f(B) - f(A)$. Stokes' theorem gives
> $$\int_a^b\frac{\partial f}{\partial z}\,\mathrm{d}z = f(B) - f(A),$$
> the fundamental theorem of calculus.

**Step 2: The Green–Riemann formula.**

> [!note]- Derivation
> Take a planar region $\mathscr{V}$ in the $t=z=0$ plane, with coordinates $(x,y)$, and the 1-form $A = P(x,y)\,\mathrm{d}x + Q(x,y)\,\mathrm{d}y$. Its exterior derivative is
> $$\mathrm{d}A = \partial_x P\,\mathrm{d}x\wedge\mathrm{d}x + \partial_y P\,\mathrm{d}y\wedge\mathrm{d}x + \partial_x Q\,\mathrm{d}x\wedge\mathrm{d}y + \partial_y Q\,\mathrm{d}y\wedge\mathrm{d}y .$$
> The first and last terms vanish ($\mathrm{d}x\wedge\mathrm{d}x = \mathrm{d}y\wedge\mathrm{d}y = 0$), and $\mathrm{d}y\wedge\mathrm{d}x = -\mathrm{d}x\wedge\mathrm{d}y$, so
> $$\mathrm{d}A = \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\mathrm{d}x\wedge\mathrm{d}y .$$
> Stokes' theorem $\int_{\mathscr{V}}\mathrm{d}A = \int_{\partial\mathscr{V}} A$ then reads
> $$\int_{\mathscr{V}}\left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\mathrm{d}x\,\mathrm{d}y = \oint_{\partial\mathscr{V}} P\,\mathrm{d}x + Q\,\mathrm{d}y ,$$
> the Green–Riemann formula. The combination $\partial_x Q - \partial_y P$ — the "scalar curl" of the planar field $(P,Q)$ — is exactly the single component of $\mathrm{d}A$.

**Step 3: The Kelvin–Stokes curl theorem.**

> [!note]- Derivation
> Take a spacelike 2-surface $\mathscr{V}$ in a constant-time slice, and a spatial vector field $\vec{A} = (A^1, A^2, A^3)$ with associated 1-form $A = A_i\,\mathrm{d}x^i$ (lower the index; on the slice the spatial metric is Euclidean up to sign). In a neighbourhood of a point of $\mathscr{V}$, choose Cartesian coordinates with $(x^2, x^3)$ the tangent directions and $x^1$ the normal. The exterior derivative is the 2-form $\mathrm{d}A = \sum_{i<j}(\partial_i A_j - \partial_j A_i)\,\mathrm{d}x^i\wedge\mathrm{d}x^j$, and the only component that survives integration over the surface (whose area element is $\mathrm{d}x^2\wedge\mathrm{d}x^3$) is
> $$(\mathrm{d}A)_{23} = \partial_2 A_3 - \partial_3 A_2 = (\mathrm{curl}\,\vec{A})^1 ,$$
> the $x^1$-component of the curl — i.e. the component *along the normal* to the surface. With $\mathrm{d}x^2\wedge\mathrm{d}x^3$ the area element $\mathrm{d}S$ and the normal $\vec{e}_1$, this is $(\mathrm{curl}\,\vec{A})\cdot\mathrm{d}\vec{S}$. The boundary integral $\int_{\partial\mathscr{V}} A = \oint_{\partial\mathscr{V}} A_i\,\mathrm{d}x^i = \oint_{\partial\mathscr{V}}\vec{A}\cdot\mathrm{d}\vec{\ell}$. Stokes' theorem gives
> $$\int_{\mathscr{V}}\mathrm{curl}\,\vec{A}\cdot\mathrm{d}\vec{S} = \oint_{\partial\mathscr{V}}\vec{A}\cdot\mathrm{d}\vec{\ell} ,$$
> the Kelvin–Stokes curl theorem.

**Step 4: Which component each reads off, and div/grad/curl as $\mathrm{d}$.**

> [!note]- Derivation
> Each classical theorem extracts a particular piece of the exterior derivative:
> - *FTC* reads the **gradient**: $\mathrm{d}f = \partial_\mu f\,\mathrm{d}x^\mu$ is the gradient 1-form, and FTC integrates its component along the curve.
> - *Green/Kelvin–Stokes* read the **curl**: $\mathrm{d}A$ of a 1-form $A$ is the 2-form whose components $\partial_i A_j - \partial_j A_i$ are the curl, and the surface integral picks out the component normal to the surface.
> - The **divergence theorem** (treated in [[Ex - Stokes' theorem for a three-form gives the four-dimensional Gauss theorem]]) reads the **divergence**: $\mathrm{d}$ of a 2-form (the Hodge dual of a vector) has the divergence as its top component.
>
> So gradient, curl, and divergence are *the same operation* — the exterior derivative $\mathrm{d}$ — applied to forms of degree $0$, $1$, and $2$ respectively, with the Hodge star translating between forms and vector fields. Correspondingly, the fundamental theorem of calculus, the Green/Kelvin–Stokes theorems, and the divergence theorem are *the same theorem* — Stokes — applied in dimensions $1$, $2$, and $3$. The miscellaneous "vector identities" of calculus are organised by a single $\mathrm{d}$ and a single $\int_{\mathscr{V}}\mathrm{d}A = \int_{\partial\mathscr{V}} A$.

> [!note]- Complete formal solution
> *FTC ($p=1$, $A=f$):* $\mathrm{d}f = \partial_z f\,\mathrm{d}z$ along the $z$-axis curve, $\partial\mathscr{V}=\{B\}-\{A\}$, so Stokes gives $\int_a^b\partial_z f\,\mathrm{d}z = f(B)-f(A)$. *Green ($p=2$, $A=P\mathrm{d}x+Q\mathrm{d}y$):* $\mathrm{d}A = (\partial_x Q - \partial_y P)\mathrm{d}x\wedge\mathrm{d}y$, so Stokes gives $\int_{\mathscr{V}}(\partial_x Q-\partial_y P)\mathrm{d}x\,\mathrm{d}y = \oint_{\partial\mathscr{V}} P\mathrm{d}x+Q\mathrm{d}y$. *Kelvin–Stokes ($p=2$, $A=A_i\mathrm{d}x^i$ on a surface):* $(\mathrm{d}A)_{23}=\partial_2 A_3-\partial_3 A_2 = (\mathrm{curl}\,\vec{A})^1$, so Stokes gives $\int_{\mathscr{V}}\mathrm{curl}\,\vec{A}\cdot\mathrm{d}\vec{S} = \oint_{\partial\mathscr{V}}\vec{A}\cdot\mathrm{d}\vec{\ell}$. Each reads off a piece of $\mathrm{d}A$: gradient ($\mathrm{d}$ on $0$-forms), curl ($\mathrm{d}$ on 1-forms), divergence ($\mathrm{d}$ on 2-forms); so div/grad/curl are one operation and FTC/Green/Stokes/divergence are one theorem. $\blacksquare$

---

# Key Takeaways

**The classical integral theorems are one theorem in different dimensions.** The fundamental theorem of calculus, Green's theorem, the Kelvin–Stokes curl theorem, and the divergence theorem are not four results to be separately memorised — they are the single identity $\int_{\mathscr{V}}\mathrm{d}A = \int_{\partial\mathscr{V}} A$ specialised by the dimension $p$ of the region and the degree of the form $A$. Recognising this collapses a large chunk of vector calculus into one statement, and it tells you immediately how to generalise: the four-dimensional version (the 4D Gauss theorem) is just the $p=4$ case, which ordinary vector calculus cannot even state. The trigger is any "integral of a derivative over a region = integral of the original over the boundary" identity; it is always Stokes. The transferable payoff is that you never need to re-derive or look up the individual theorems — you write down $\int_{\mathscr{V}}\mathrm{d}A = \int_{\partial\mathscr{V}} A$, choose $A$, and compute $\mathrm{d}A$.

**Gradient, curl, and divergence are the exterior derivative on forms of degree 0, 1, and 2.** The three differential operators of vector calculus, which look unrelated when written in components, are the *same* operation — the exterior derivative $\mathrm{d}$ — applied to forms of different degree, with the Hodge star converting between forms and vector fields. The gradient is $\mathrm{d}$ on a scalar ($0$-form); the curl is $\mathrm{d}$ on a 1-form (then Hodge-dualised back to a vector); the divergence is $\mathrm{d}$ on a 2-form (the Hodge dual of a vector). This unification explains the otherwise mysterious identities $\mathrm{curl}\,\mathrm{grad} = 0$ and $\mathrm{div}\,\mathrm{curl} = 0$ — both are instances of $\mathrm{d}\circ\mathrm{d} = 0$ — and it is why the exterior calculus, not vector calculus, is the right language in four dimensions and on curved spaces. Recognising "div/grad/curl = $\mathrm{d}$ at different degrees" is the portable insight that makes the exterior derivative feel inevitable rather than abstract.

**Which component survives is dictated by the dimension and the surface's orientation.** A practical subtlety worth internalising: when you integrate $\mathrm{d}A$ over a $p$-region, only the single component of $\mathrm{d}A$ tangent to the region survives, and *which* component that is depends on how the region sits in space. For the curl theorem, the surviving component is the curl *along the normal* to the surface — a surface in the $yz$-plane picks out $(\mathrm{curl}\,\vec{A})^x$ — so the "circulation = flux of curl" statement automatically selects the right curl component. The diagnostic lesson is that the exterior-derivative formalism handles this selection automatically: you do not choose which component of the curl to use, the geometry of the surface does it for you through the area element. This is why the form-based statement is cleaner than the component-based one — it is coordinate-free and the orientation bookkeeping is built in — and the companion exercise [[Ex - Stokes' theorem for a three-form gives the four-dimensional Gauss theorem]] shows the same automatic selection producing the divergence in the $p=3$ and $p=4$ cases.
