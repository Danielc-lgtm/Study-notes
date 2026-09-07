---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - The Maurer-Cartan Form"
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
  - "Thm - The Maurer-Cartan Equation"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Notation

We work with the **left Maurer–Cartan form** $\theta\in\Omega^1(G;\mathfrak{g})$ of a Lie group $G$, defined at $g\in G$ by
$$\theta_g:=d_gL_{g^{-1}}\colon T_gG\longrightarrow T_eG=\mathfrak{g},$$
where $L_h(g)=hg$ is left translation and $e$ is the identity. For a matrix Lie group this is the matrix-valued form $\theta=g^{-1}\,dg$. Its defining property is that it trivialises the tangent bundle by the *left*-invariant frame: if $\widetilde{\xi}$ is the left-invariant vector field with $\widetilde{\xi}(e)=\xi\in\mathfrak{g}$, then $\theta(\widetilde{\xi})=\xi$ as a constant $\mathfrak{g}$-valued function. The **Maurer–Cartan equation** is the identity $d\theta+\tfrac12[\theta\wedge\theta]=0$, where $[\,\cdot\wedge\cdot\,]$ is the bracket of $\mathfrak{g}$-valued forms, normalised so that $[\theta\wedge\theta](X,Y)=2[\theta(X),\theta(Y)]$ for vector fields $X,Y$.

We use the invariant coordinate-free formula for the exterior derivative of a $1$-form, in the sign convention of Bär (and of the whole series),
$$d\alpha(X,Y)=X\big(\alpha(Y)\big)-Y\big(\alpha(X)\big)-\alpha\big([X,Y]\big),$$
proved on [[Thm - Coordinate Expression for the Exterior Derivative]]; for a $\mathfrak{g}$-valued $1$-form the derivations act componentwise on the $\mathfrak{g}$-valued function $\alpha(Y)$.

For $U(1)=\{z\in\mathbb{C}:|z|=1\}$ we have $\mathfrak{u}(1)=i\mathbb{R}$. For $SU(2)$ we use the quaternion model of chapter I: identify $\mathbb{H}=\mathbb{R}^4$ with real basis $1,i,j,k$, quaternion multiplication $i^2=j^2=k^2=-1$, $ij=k=-ji$, $jk=i=-kj$, $ki=j=-ik$, conjugation $\overline{x_0+x_1i+x_2j+x_3k}=x_0-x_1i-x_2j-x_3k$, and norm $|q|^2=q\bar q=x_0^2+x_1^2+x_2^2+x_3^2$. Then $SU(2)\cong Sp(1)=\{q\in\mathbb{H}:|q|=1\}=S^3$ (see [[Ex - SU(2) is Diffeomorphic to S^3]]), the Lie algebra is the imaginary quaternions $\mathfrak{su}(2)\cong\operatorname{Im}\mathbb{H}=\operatorname{span}_{\mathbb{R}}\{i,j,k\}$, and for $q\in S^3$ a unit quaternion its inverse is $q^{-1}=\bar q$.

> [!warning] Convention: Bär's sign in Remark 2.5.9
> In computing the curvature of the product connection on $B\times G$ (Remark 2.5.9), Bär evaluates $d\phi$ on left-invariant fields $X,Y$ and writes $d\phi(X,Y)=\partial_X\phi(Y)-\partial_Y\phi(X)-\phi([X,Y])=[X,Y](e)$. The first two terms vanish because $\phi(Y)=Y(e)$ and $\phi(X)=X(e)$ are *constant* $\mathfrak{g}$-valued functions, so the remaining term is $-\phi([X,Y])=-[X,Y](e)$; the printed final value has the wrong sign. The corrected value $d\phi(X,Y)=-[X,Y](e)$ is what makes $d\phi+\tfrac12[\phi,\phi]=0$ hold, since $[\phi,\phi](X,Y)=2[X,Y](e)$; Bär's own conclusion "$d\phi+\tfrac12[\phi,\phi]=0$" is correct, only the intermediate sign is a slip. We use the corrected sign throughout.

# Problem Statement

Compute the left Maurer–Cartan form $\theta$ explicitly for the two smallest non-trivial compact groups and verify its defining equation:

1. For $G=U(1)$, writing $z=e^{i\varphi}$, show that $\theta=z^{-1}\,dz=i\,d\varphi$, that the Maurer–Cartan equation $d\theta+\tfrac12[\theta\wedge\theta]=0$ holds (indeed each term vanishes separately), and that $\theta$ is $i$ times the $1$-form dual to the left-invariant field $\partial_\varphi$.

2. For $G=SU(2)\cong S^3\subset\mathbb{H}$, in the quaternion coordinates $(x_0,x_1,x_2,x_3)$, show that $\theta=\bar q\,dq$, compute its three real components $\theta^1,\theta^2,\theta^3$ (the coefficients of $i,j,k$), verify the Maurer–Cartan equation directly by computing $d\theta$ and $\tfrac12[\theta\wedge\theta]$, and identify $\theta^1,\theta^2,\theta^3$ as the coframe dual to the left-invariant frame $e_1=qi,\ e_2=qj,\ e_3=qk$.

Throughout, $dq=dx_0+dx_1\,i+dx_2\,j+dx_3\,k$ denotes the $\mathbb{H}$-valued differential of the identity map, and products such as $\bar q\,dq$ are quaternion products of a quaternion-valued function with a quaternion-valued $1$-form.

**Recall:**

The objects in play are the left Maurer–Cartan form, the bracket of $\mathfrak{g}$-valued $1$-forms, the invariant formula for $d$, and the quaternion model of $SU(2)$.

![[Def - The Maurer-Cartan Form#The Definition]]

The **[[Def - The Maurer-Cartan Form|Maurer–Cartan form]]** $\theta$ satisfies $\theta(\widetilde{\xi})=\xi$ for every left-invariant field $\widetilde{\xi}$, is left-invariant ($L_h^*\theta=\theta$), transforms under right translation as $R_h^*\theta=\operatorname{Ad}_{h^{-1}}\theta$, and equals $g^{-1}\,dg$ for a matrix group. Its value on a smooth curve $g(t)$ is $\theta(\dot g(t))=g(t)^{-1}\dot g(t)$.

![[Def - Lie-Algebra-Valued Differential Forms and Their Bracket#The Definition]]

For $\mathfrak{g}$-valued $1$-forms $\alpha,\beta$ the **bracket** evaluates as $[\alpha\wedge\beta](X,Y)=[\alpha(X),\beta(Y)]-[\alpha(Y),\beta(X)]$, so on the diagonal $[\alpha\wedge\alpha](X,Y)=2[\alpha(X),\alpha(Y)]$; this factor of $2$ is why the Maurer–Cartan equation carries a $\tfrac12$. In components, if $\alpha=\sum_c\alpha^c E_c$ and $\beta=\sum_c\beta^c E_c$ for a basis $\{E_c\}$ of $\mathfrak{g}$, then $[\alpha\wedge\beta]=\sum_{a,b}(\alpha^a\wedge\beta^b)\,[E_a,E_b]$.

The identity that closes the Maurer–Cartan equation on $\mathfrak{su}(2)=\operatorname{Im}\mathbb{H}$ is the commutator table of the imaginary quaternions,
$$[i,j]=ij-ji=k-(-k)=2k,\qquad [j,k]=2i,\qquad [k,i]=2j,$$
computed from the quaternion multiplication rules; here the bracket is the commutator of the associative product of $\mathbb{H}$. The bracket of left-invariant vector fields realises the Lie-algebra bracket, $[\,\widetilde{\xi},\widetilde{\eta}\,]=\widetilde{[\xi,\eta]}$, by [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]].

The theorem this exercise instantiates is:

![[Thm - The Maurer-Cartan Equation#Statement]]

---

# Convergent Strategy

**Problem class.** This is a *compute-and-verify* problem: produce a closed formula for a canonical object on a specific group and check the structural equation it must satisfy. The verification can be done two ways — intrinsically, by evaluating both sides of $d\theta+\tfrac12[\theta\wedge\theta]=0$ on the left-invariant frame where everything is constant, or extrinsically, by writing $\theta$ in ambient coordinates and differentiating. We do both, because they illuminate different things: the intrinsic route shows *why* the equation holds (it is the structure-constant identity of the Lie algebra), and the coordinate route shows *that* it holds by an explicit computation of $2$-forms.

**Assumption pattern.** Two features are exploited repeatedly. First, both $U(1)$ and $SU(2)$ are *matrix groups*, so $\theta=g^{-1}\,dg$ and the Maurer–Cartan equation can also be checked by the one-line matrix calculation $d(g^{-1}\,dg)=-g^{-1}\,dg\wedge g^{-1}\,dg$. Second, on the left-invariant frame $\theta(\widetilde{\xi})=\xi$ is *constant*, which annihilates the two derivative terms in the invariant formula for $d\theta$ and reduces $d\theta(\widetilde{\xi},\widetilde{\eta})$ to $-\theta([\widetilde{\xi},\widetilde{\eta}])=-[\xi,\eta]$, a pure Lie-algebra quantity.

**Theorem routing.** For $U(1)$ the route is immediate: substitute $z=e^{i\varphi}$ into $\theta=\bar z\,dz$ and read off $i\,d\varphi$; the equation holds because $\mathfrak{u}(1)$ is abelian so $[\theta\wedge\theta]=0$, and $d(i\,d\varphi)=0$. For $SU(2)$ the route is: compute $\theta=\bar q\,dq$ by quaternion multiplication and separate real and imaginary parts (the real part vanishes on $S^3$, confirming $\theta\in\mathfrak{su}(2)$); read off $\theta^1,\theta^2,\theta^3$; verify $\theta(e_a)=E_a$ so that $\{\theta^a\}$ is the dual coframe; then verify $d\theta+\tfrac12[\theta\wedge\theta]=0$ intrinsically via the invariant $d$-formula plus [[Thm - Left-Invariant Vector Fields Form a Lie Algebra|the left-invariant bracket]], and confirm it by the coordinate computation $d\theta^1=2\,dx_0\wedge dx_1-2\,dx_2\wedge dx_3=-2\,\theta^2\wedge\theta^3$ on $S^3$.

**Key decision point.** The subtle move on $SU(2)$ is to pass between the ambient $\mathbb{R}^4=\mathbb{H}$ and the hypersurface $S^3$. Off the sphere the coordinate identities carry an extra term proportional to the radial form $\rho=x_0\,dx_0+x_1\,dx_1+x_2\,dx_2+x_3\,dx_3=\tfrac12\,d|q|^2$; on $S^3$ this form pulls back to zero (since $|q|^2\equiv 1$ there), and only then do the identities take their clean form. Keeping track of when $\rho$ may be discarded — precisely after restricting to $S^3$ — is the whole discipline of the coordinate verification.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory IV — Connections and Curvature on Principal Bundles#Legal Operations|the topic page's Legal Operations]]:

1. **Evaluate the Maurer–Cartan form on a curve.** For a matrix (or quaternion) group, $\theta(\dot g)=g^{-1}\dot g$; this turns "compute $\theta$" into "left-multiply the differential by the inverse", giving $\theta=\bar z\,dz$ on $U(1)$ and $\theta=\bar q\,dq$ on $SU(2)$.

2. **Separate a quaternion product into real and imaginary parts.** Compute $\bar q\,dq$ with the quaternion product formula $(p_0+\mathbf p)(r_0+\mathbf r)=(p_0r_0-\mathbf p\cdot\mathbf r)+(p_0\mathbf r+r_0\mathbf p+\mathbf p\times\mathbf r)$; the scalar part is $\tfrac12\,d|q|^2$, which vanishes on $S^3$, so $\theta$ is imaginary-quaternion valued.

3. **Reduce $d$ of an invariant form to a bracket.** Apply the invariant formula $d\alpha(X,Y)=X(\alpha(Y))-Y(\alpha(X))-\alpha([X,Y])$ on the left-invariant frame, where $\alpha(\text{frame field})$ is constant, so $d\theta(\widetilde\xi,\widetilde\eta)=-\theta([\widetilde\xi,\widetilde\eta])=-[\xi,\eta]$.

4. **Realise the bracket of frame fields by the algebra bracket.** Use $[\widetilde\xi,\widetilde\eta]=\widetilde{[\xi,\eta]}$ from [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]] to replace geometry by the commutator table $[i,j]=2k$, etc.

5. **Expand the bracket of a $\mathfrak{g}$-valued form in components.** Compute $\tfrac12[\theta\wedge\theta]$ from $[\theta\wedge\theta]=\sum_{a,b}(\theta^a\wedge\theta^b)[E_a,E_b]$ and the structure constants.

6. **Discard a form after restriction to a hypersurface.** On $S^3$, drop the radial form $\rho=\tfrac12\,d|q|^2$, which pulls back to zero because $|q|^2\equiv 1$ on the sphere.

---

# Hints

> [!note]- Hint 1
> For a matrix group $\theta=g^{-1}\,dg$. On $U(1)$ the group elements are $z$ with $z^{-1}=\bar z$, so $\theta=\bar z\,dz$; put $z=e^{i\varphi}$ and differentiate. On $SU(2)=S^3$ the elements are unit quaternions $q$ with $q^{-1}=\bar q$, so $\theta=\bar q\,dq$; multiply out.

> [!note]- Hint 2
> To multiply $\bar q\,dq$, use the scalar/vector form of quaternion multiplication. The scalar (real) part comes out as $x_0\,dx_0+x_1\,dx_1+x_2\,dx_2+x_3\,dx_3=\tfrac12\,d(|q|^2)$, which vanishes on the unit sphere — so $\theta$ has values in the imaginary quaternions $\operatorname{Im}\mathbb{H}=\mathfrak{su}(2)$, as it must.

> [!note]- Hint 3
> To identify $\theta$ with a dual coframe, evaluate it on the left-invariant frame $e_a(q)=q\cdot E_a$ (right multiplication by $E_1=i$, $E_2=j$, $E_3=k$). Because $q$ is a unit quaternion, $\theta(e_a)=\bar q\,(qE_a)=(\bar q q)E_a=E_a$ is constant. So $\theta=\theta^1 i+\theta^2 j+\theta^3 k$ where $\{\theta^a\}$ is dual to $\{e_a\}$: $\theta^a(e_b)=\delta^a_b$.

> [!note]- Hint 4
> For the equation, the fastest verification uses the invariant $d$-formula on the frame: since $\theta^a(e_b)=\delta^a_b$ is constant, $d\theta^a(e_b,e_c)=-\theta^a([e_b,e_c])$, and $[e_b,e_c]=\widetilde{[E_b,E_c]}$ has value $2\varepsilon_{bca}E_a$. Compare with $\tfrac12[\theta\wedge\theta]$, whose $E_a$-component evaluated on $(e_b,e_c)$ is $[E_b,E_c]$'s $E_a$-part. For the coordinate check, differentiate $\theta^1$ directly and use $|q|^2\equiv1$ to simplify $\theta^2\wedge\theta^3$.

---

# Solution

We treat the two groups in turn. The plan is to obtain $\theta$ from $\theta=g^{-1}\,dg$, read off components, identify the dual frame, and then verify $d\theta+\tfrac12[\theta\wedge\theta]=0$ — trivially for the abelian $U(1)$, and by both an intrinsic and a coordinate computation for $SU(2)$. All computations use only the group structure and the invariant formula for $d$ recalled above.

## Part A — the group $U(1)$

**Step A1: Compute $\theta=i\,d\varphi$.**

Left multiplication by $\bar z$ on the differential of the identity yields $\theta=\bar z\,dz$, which in the angular coordinate is $i\,d\varphi$.

> [!note]- Derivation
> An element of $U(1)$ is $z=e^{i\varphi}$ with $|z|=1$, so $z^{-1}=\bar z=e^{-i\varphi}$. The Lie algebra is $\mathfrak{u}(1)=T_1U(1)=i\mathbb{R}$. For the matrix (here $1\times 1$ complex) group,
> $$\theta=z^{-1}\,dz=\bar z\,dz.$$
> Writing $z=e^{i\varphi}$, we have $dz=i\,e^{i\varphi}\,d\varphi$, and therefore
> $$\theta=e^{-i\varphi}\cdot i\,e^{i\varphi}\,d\varphi=i\,d\varphi\qquad\text{(the exponentials cancel).}$$
> Note that although $\varphi$ is only defined locally on $U(1)$ (it is multivalued as a global function), its differential $d\varphi$ is a genuine, globally defined $1$-form on the circle — the angular form — so $\theta=i\,d\varphi\in\Omega^1(U(1);i\mathbb{R})$ is a well-defined global $\mathfrak{u}(1)$-valued $1$-form.

**Step A2: $\theta$ is $i$ times the coframe dual to $\partial_\varphi$, and the Maurer–Cartan equation holds.**

The left-invariant field is $\partial_\varphi$; $\theta(\partial_\varphi)=i$; and both terms of the Maurer–Cartan equation vanish.

> [!note]- Derivation
> The left-invariant vector field with value $i\in\mathfrak{u}(1)$ at $z=1$ is $\partial_\varphi$: under left translation $L_w(z)=wz$, the field $\partial_\varphi$ is carried to itself because $L_w$ acts on the angle by $\varphi\mapsto\varphi+\arg w$, a translation whose differential is the identity on $\partial_\varphi$. Evaluating,
> $$\theta(\partial_\varphi)=i\,d\varphi(\partial_\varphi)=i,$$
> so $\theta=i\,d\varphi$ exhibits $\theta$ as $i$ times the $1$-form $d\varphi$ dual to $\partial_\varphi$, confirming $\theta(\widetilde\xi)=\xi$ for the single generator $\xi=i$.
>
> For the Maurer–Cartan equation, first $[\theta\wedge\theta]=0$: the Lie algebra $\mathfrak{u}(1)=i\mathbb{R}$ is abelian, so every bracket $[\xi,\eta]=0$, and by the component formula $[\theta\wedge\theta]=\sum_{a,b}(\theta^a\wedge\theta^b)[E_a,E_b]=0$. Second,
> $$d\theta=d(i\,d\varphi)=i\,d(d\varphi)=0\qquad\text{(}d\circ d=0\text{, see [[Thm - d-Squared-is-Zero]]).}$$
> Hence $d\theta+\tfrac12[\theta\wedge\theta]=0+0=0$, and each term vanishes on its own, as claimed.

## Part B — the group $SU(2)\cong S^3$

**Step B1: Compute $\theta=\bar q\,dq$ and its components.**

Left multiplication by $\bar q$ gives $\theta=\bar q\,dq$; the scalar part vanishes on $S^3$ and the three imaginary parts are $\theta^1,\theta^2,\theta^3$ below.

> [!note]- Derivation
> A unit quaternion $q=x_0+x_1i+x_2j+x_3k$ has $q^{-1}=\bar q$, so
> $$\theta=q^{-1}\,dq=\bar q\,dq,\qquad \bar q=x_0-x_1i-x_2j-x_3k,\quad dq=dx_0+dx_1\,i+dx_2\,j+dx_3\,k.$$
> Multiply using the scalar/vector form of the quaternion product: for $p=p_0+\mathbf p$ and $r=r_0+\mathbf r$ (bold denotes the $(i,j,k)$-vector part),
> $$pr=(p_0r_0-\mathbf p\cdot\mathbf r)+\big(p_0\mathbf r+r_0\mathbf p+\mathbf p\times\mathbf r\big).$$
> Here $p=\bar q$ has $p_0=x_0$, $\mathbf p=(-x_1,-x_2,-x_3)$, and $r=dq$ has $r_0=dx_0$, $\mathbf r=(dx_1,dx_2,dx_3)$.
>
> *Scalar part:* $p_0r_0-\mathbf p\cdot\mathbf r=x_0\,dx_0-(-x_1\,dx_1-x_2\,dx_2-x_3\,dx_3)=x_0\,dx_0+x_1\,dx_1+x_2\,dx_2+x_3\,dx_3=\tfrac12\,d(|q|^2)$. On $S^3$, $|q|^2\equiv 1$, so $d(|q|^2)=0$ and the scalar part of $\theta$ vanishes: $\theta$ takes values in $\operatorname{Im}\mathbb{H}=\mathfrak{su}(2)$, exactly as required of a $\mathfrak{g}$-valued form.
>
> *Vector part:* $p_0\mathbf r+r_0\mathbf p+\mathbf p\times\mathbf r$. Computing the cross product $\mathbf p\times\mathbf r$ with $\mathbf p=(-x_1,-x_2,-x_3)$, $\mathbf r=(dx_1,dx_2,dx_3)$ componentwise, and adding $x_0(dx_1,dx_2,dx_3)$ and $dx_0(-x_1,-x_2,-x_3)$, gives the three imaginary components
> $$\theta^1=-x_1\,dx_0+x_0\,dx_1+x_3\,dx_2-x_2\,dx_3,$$
> $$\theta^2=-x_2\,dx_0+x_0\,dx_2+x_1\,dx_3-x_3\,dx_1,$$
> $$\theta^3=-x_3\,dx_0+x_0\,dx_3+x_2\,dx_1-x_1\,dx_2,$$
> so that $\theta=\theta^1\,i+\theta^2\,j+\theta^3\,k$. (The three are cyclic in $(i,j,k)\leftrightarrow(x_1,x_2,x_3)$: applying the substitution $x_1\to x_2\to x_3\to x_1$ sends $\theta^1\to\theta^2\to\theta^3\to\theta^1$, a symmetry we use below.)

**Step B2: Identify $\{\theta^a\}$ as the coframe dual to the left-invariant frame.**

Right multiplication by $i,j,k$ produces the left-invariant frame $e_1,e_2,e_3$, and $\theta^a(e_b)=\delta^a_b$.

> [!note]- Derivation
> The left-invariant vector field with value $E_a\in\mathfrak{su}(2)$ at $q=1$ is $e_a(q)=d_1L_q(E_a)=q\cdot E_a$ (right quaternion multiplication), because $L_q$ acts on $\mathbb{H}$ by left multiplication by $q$, whose differential is again left multiplication by $q$. Concretely, with $E_1=i,E_2=j,E_3=k$,
> $$e_1=qi=(-x_1,x_0,x_3,-x_2),\quad e_2=qj=(-x_2,-x_3,x_0,x_1),\quad e_3=qk=(-x_3,x_2,-x_1,x_0),$$
> the components being taken in the frame $(\partial_{x_0},\partial_{x_1},\partial_{x_2},\partial_{x_3})$. Now evaluate $\theta$ on $e_a$: since $q$ is a unit quaternion,
> $$\theta(e_a)=\bar q\,(q E_a)=(\bar q q)E_a=E_a\qquad\text{(associativity of }\mathbb{H}\text{ and }\bar q q=|q|^2=1\text{),}$$
> a *constant* element of $\mathfrak{su}(2)$. Reading off components, $\theta^a(e_b)=\delta^a_b$. As a direct check on $\theta^1$: with $e_1=(-x_1,x_0,x_3,-x_2)$,
> $$\theta^1(e_1)=(-x_1)(-x_1)+x_0(x_0)+x_3(x_3)-x_2(-x_2)=x_0^2+x_1^2+x_2^2+x_3^2=1,$$
> while $\theta^1(e_2)=(-x_1)(-x_2)+x_0(-x_3)+x_3(x_0)-x_2(x_1)=x_1x_2-x_0x_3+x_0x_3-x_1x_2=0$ and similarly $\theta^1(e_3)=0$. Hence $\{\theta^1,\theta^2,\theta^3\}$ is exactly the coframe dual to the left-invariant frame $\{e_1,e_2,e_3\}$, which is the coordinate statement of $\theta(\widetilde\xi)=\xi$.

**Step B3: Verify the Maurer–Cartan equation intrinsically.**

On the left-invariant frame the derivative terms of $d\theta^a$ vanish, leaving $d\theta^a(e_b,e_c)=-\theta^a([e_b,e_c])$; the structure constants of $\mathfrak{su}(2)$ then match $\tfrac12[\theta\wedge\theta]$ term by term.

> [!note]- Derivation
> By [[Thm - Left-Invariant Vector Fields Form a Lie Algebra|the left-invariant bracket identity]], $[e_b,e_c]=\widetilde{[E_b,E_c]}$; with the quaternion commutator table $[i,j]=2k$, $[j,k]=2i$, $[k,i]=2j$ this reads
> $$[e_1,e_2]=2e_3,\qquad [e_2,e_3]=2e_1,\qquad [e_3,e_1]=2e_2.$$
> Apply the invariant formula for $d$ on the frame. Since $\theta^a(e_c)=\delta^a_c$ is constant, $e_b(\theta^a(e_c))=0$ and $e_c(\theta^a(e_b))=0$, so
> $$d\theta^a(e_b,e_c)=e_b(\theta^a(e_c))-e_c(\theta^a(e_b))-\theta^a([e_b,e_c])=-\theta^a([e_b,e_c])\qquad\text{(constancy of }\theta^a(e_\bullet)\text{).}$$
> For $a=1$ this gives, using the bracket table,
> $$d\theta^1(e_2,e_3)=-\theta^1(2e_1)=-2,\qquad d\theta^1(e_1,e_2)=-\theta^1(2e_3)=0,\qquad d\theta^1(e_3,e_1)=-\theta^1(2e_2)=0.$$
> Now the bracket term. By the component formula, the $i$-component ($E_1=i$) of $[\theta\wedge\theta]$ receives contributions only from $[E_2,E_3]=[j,k]=2i$ and $[E_3,E_2]=-2i$, so
> $$[\theta\wedge\theta]^1=2\,\theta^2\wedge\theta^3-2\,\theta^3\wedge\theta^2=4\,\theta^2\wedge\theta^3,\qquad\text{hence}\qquad \tfrac12[\theta\wedge\theta]^1=2\,\theta^2\wedge\theta^3.$$
> Evaluating $2\,\theta^2\wedge\theta^3$ on the frame with $\theta^a(e_b)=\delta^a_b$: $(\theta^2\wedge\theta^3)(e_2,e_3)=\theta^2(e_2)\theta^3(e_3)-\theta^2(e_3)\theta^3(e_2)=1$, and it vanishes on $(e_1,e_2)$ and $(e_3,e_1)$. Thus $\tfrac12[\theta\wedge\theta]^1$ takes the values $2,0,0$ on $(e_2,e_3),(e_1,e_2),(e_3,e_1)$, which are the negatives of the values of $d\theta^1$. Therefore
> $$\big(d\theta+\tfrac12[\theta\wedge\theta]\big)^1=0\qquad\text{on every pair of frame fields, hence identically (the frame spans }TS^3\text{).}$$
> By the cyclic symmetry $i\to j\to k\to i$, $x_1\to x_2\to x_3\to x_1$ noted in Step B1 — which permutes $(\theta^1,\theta^2,\theta^3)$ and $(e_1,e_2,e_3)$ cyclically and preserves the commutator table — the same identity holds for the $j$- and $k$-components. Hence $d\theta+\tfrac12[\theta\wedge\theta]=0$.

**Step B4: Confirm the equation by a direct coordinate computation.**

Differentiating $\theta^1$ in the ambient coordinates and simplifying $\theta^2\wedge\theta^3$ on $S^3$ reproduces $d\theta^1=-2\,\theta^2\wedge\theta^3$.

> [!note]- Derivation
> Differentiate $\theta^1=-x_1\,dx_0+x_0\,dx_1+x_3\,dx_2-x_2\,dx_3$ term by term:
> $$d\theta^1=-dx_1\wedge dx_0+dx_0\wedge dx_1+dx_3\wedge dx_2-dx_2\wedge dx_3=2\,dx_0\wedge dx_1-2\,dx_2\wedge dx_3,$$
> using $-dx_1\wedge dx_0=dx_0\wedge dx_1$ and $dx_3\wedge dx_2=-dx_2\wedge dx_3$.
>
> Next compute $\theta^2\wedge\theta^3$. Writing the coefficient of each basic $2$-form $dx_\mu\wedge dx_\nu$ ($\mu<\nu$) as $\theta^2_\mu\theta^3_\nu-\theta^2_\nu\theta^3_\mu$ from the coefficient vectors $\theta^2=(-x_2,-x_3,x_0,x_1)$ and $\theta^3=(-x_3,x_2,-x_1,x_0)$ (indexed by $dx_0,dx_1,dx_2,dx_3$), one finds
> $$\theta^2\wedge\theta^3=(-x_2^2-x_3^2)\,dx_0\wedge dx_1+(x_0^2+x_1^2)\,dx_2\wedge dx_3+\rho\wedge\theta^1,$$
> where $\rho=x_0\,dx_0+x_1\,dx_1+x_2\,dx_2+x_3\,dx_3=\tfrac12\,d(|q|^2)$ collects the remaining four coefficients; this last claim is the identity $\big(\theta^2\wedge\theta^3\big)-\big(-dx_0\wedge dx_1+dx_2\wedge dx_3\big)=\rho\wedge\theta^1+(|q|^2-1)\,dx_2\wedge dx_3$, verified coefficient by coefficient (the six coefficients of $\rho\wedge\theta^1$ are computed from $\rho=(x_0,x_1,x_2,x_3)$ and $\theta^1=(-x_1,x_0,x_3,-x_2)$ and match the six differences exactly, the $dx_2\wedge dx_3$ coefficient using $x_0^2+x_1^2=1-x_2^2-x_3^2$).
>
> Now restrict to $S^3$, i.e. pull back along the inclusion $\iota\colon S^3\hookrightarrow\mathbb{R}^4$. There $|q|^2\equiv 1$, so $\iota^*\rho=\tfrac12\,\iota^*d(|q|^2)=0$ and $\iota^*(|q|^2-1)=0$. Hence on $S^3$,
> $$\theta^2\wedge\theta^3=-dx_0\wedge dx_1+dx_2\wedge dx_3.$$
> Comparing with $d\theta^1=2\,dx_0\wedge dx_1-2\,dx_2\wedge dx_3$ gives $d\theta^1=-2\big(-dx_0\wedge dx_1+dx_2\wedge dx_3\big)=-2\,\theta^2\wedge\theta^3$ on $S^3$, i.e. $d\theta^1+2\,\theta^2\wedge\theta^3=0$, which is $\big(d\theta+\tfrac12[\theta\wedge\theta]\big)^1=0$ from Step B3. This confirms the intrinsic computation.

> [!note]- Complete formal solution
> **Claim.** The left Maurer–Cartan form of $U(1)$ is $\theta=z^{-1}\,dz=i\,d\varphi$, and of $SU(2)\cong S^3$ is $\theta=\bar q\,dq=\theta^1 i+\theta^2 j+\theta^3 k$ with $\theta^1,\theta^2,\theta^3$ as above; both satisfy $d\theta+\tfrac12[\theta\wedge\theta]=0$, and in each case the components of $\theta$ form the coframe dual (up to the identification $\xi\leftrightarrow$ its component) to the left-invariant frame.
>
> *$U(1)$.* Since $z^{-1}=\bar z$ and $z=e^{i\varphi}$, $\theta=\bar z\,dz=e^{-i\varphi}(ie^{i\varphi}\,d\varphi)=i\,d\varphi$. The left-invariant field is $\partial_\varphi$ and $\theta(\partial_\varphi)=i$, so $\theta=i\,d\varphi$ is $i$ times the coframe dual to $\partial_\varphi$. As $\mathfrak{u}(1)$ is abelian, $[\theta\wedge\theta]=0$; and $d\theta=i\,d(d\varphi)=0$. Hence $d\theta+\tfrac12[\theta\wedge\theta]=0$.
>
> *$SU(2)$.* For $q\in S^3$, $q^{-1}=\bar q$, so $\theta=\bar q\,dq$. The quaternion product $\bar q\,dq$ has scalar part $\tfrac12\,d(|q|^2)$, which vanishes on $S^3$, and imaginary part $\theta^1 i+\theta^2 j+\theta^3 k$ with $\theta^1=-x_1\,dx_0+x_0\,dx_1+x_3\,dx_2-x_2\,dx_3$ and its two cyclic images. The left-invariant frame is $e_a=qE_a$ ($E_1,E_2,E_3=i,j,k$), and $\theta(e_a)=\bar q\,qE_a=E_a$, so $\theta^a(e_b)=\delta^a_b$: the $\theta^a$ are the dual coframe.
>
> To verify the equation, on the frame $d\theta^a(e_b,e_c)=-\theta^a([e_b,e_c])$ because $\theta^a(e_\bullet)$ is constant; with $[e_b,e_c]=\widetilde{[E_b,E_c]}$ and $[i,j]=2k,[j,k]=2i,[k,i]=2j$, the values of $d\theta^1$ on $(e_2,e_3),(e_1,e_2),(e_3,e_1)$ are $-2,0,0$. The component $\tfrac12[\theta\wedge\theta]^1=2\,\theta^2\wedge\theta^3$ takes values $+2,0,0$ on the same pairs, so $(d\theta+\tfrac12[\theta\wedge\theta])^1=0$; cyclic symmetry gives the other two components. Independently, $d\theta^1=2\,dx_0\wedge dx_1-2\,dx_2\wedge dx_3$ and, on $S^3$ (where the radial form $\rho=\tfrac12 d|q|^2$ vanishes), $\theta^2\wedge\theta^3=-dx_0\wedge dx_1+dx_2\wedge dx_3$, so $d\theta^1=-2\,\theta^2\wedge\theta^3$. In both computations $d\theta+\tfrac12[\theta\wedge\theta]=0$. $\blacksquare$

> [!warning] Illegal but tempting: dropping the $\tfrac12$ or the bracket sign for $SU(2)$
> Because $SU(2)$ is non-abelian, one may *not* discard $[\theta\wedge\theta]$: it is $4\,\theta^2\wedge\theta^3$ in the $i$-slot and is exactly what cancels $d\theta$. It is equally tempting to reuse Bär's printed $d\phi=+[X,Y](e)$; doing so gives $d\theta+\tfrac12[\theta\wedge\theta]=2\,[X,Y](e)\neq0$, a contradiction with the closed matrix computation $d(\bar q\,dq)=-\bar q\,dq\wedge\bar q\,dq$. The resolution is the corrected sign $d\phi=-[X,Y](e)$ recorded in the Notation callout; the matrix identity $d(g^{-1}dg)=-g^{-1}dg\wedge g^{-1}dg=-\tfrac12[g^{-1}dg\wedge g^{-1}dg]$ is an independent, sign-safe route to the same conclusion.

**Independent sanity check (matrix route).** Regard $SU(2)$ as $2\times 2$ matrices, so $\theta=g^{-1}\,dg$. Differentiating $g^{-1}g=1$ gives $d(g^{-1})=-g^{-1}(dg)g^{-1}$, hence
$$d\theta=d(g^{-1})\wedge dg=-g^{-1}(dg)g^{-1}\wedge dg=-\big(g^{-1}dg\big)\wedge\big(g^{-1}dg\big)=-\theta\wedge\theta.$$
By the companion exercise [[Ex - The Bracket of Matrix-Valued 1-Forms is Twice the Wedge Square|the bracket-versus-wedge identity]], $\theta\wedge\theta=\tfrac12[\theta\wedge\theta]$ for a matrix-valued $1$-form, so $d\theta=-\tfrac12[\theta\wedge\theta]$, i.e. $d\theta+\tfrac12[\theta\wedge\theta]=0$. This one-line argument is valid for every matrix group at once and reproduces the coordinate result for $SU(2)$.

---

# Key Takeaways

**The Maurer–Cartan form is the tautological trivialisation of the tangent bundle of a Lie group, and its equation is the structure-constant table read as a differential identity.** The single most reusable idea here is that $\theta(\widetilde\xi)=\xi$ turns every geometric question about a Lie group into a question about its Lie algebra: on the left-invariant frame the components $\theta^a$ are constants, so $d\theta$ is computed purely from the bracket $[e_b,e_c]=\widetilde{[E_b,E_c]}$, and the Maurer–Cartan equation $d\theta^a=-\tfrac12 c^a_{bc}\,\theta^b\wedge\theta^c$ (with $c^a_{bc}$ the structure constants, here $c^1_{23}=2$ and cyclic) is nothing but the multiplication table of $\mathfrak{g}$ in differential-form dress. The trigger to reach for this: whenever you must differentiate an invariant object on a group, evaluate on the invariant frame first and let constancy kill the derivative terms. The diagnostic that you have done it right is that only brackets remain.

**Restricting a computation to a level set means discarding the radial form; keep it visible until the restriction is taken.** The $SU(2)$ calculation lived on $S^3=\{|q|=1\}$, and every clean identity — the vanishing of the scalar part of $\bar q\,dq$, the simplification of $\theta^2\wedge\theta^3$ — held only after dropping the radial $1$-form $\rho=\tfrac12\,d(|q|^2)$, which pulls back to zero on the sphere. Off the sphere those identities carry $\rho$-dependent correction terms, and conflating "true on $\mathbb{R}^4$" with "true on $S^3$" is the standard error in this kind of computation. The transferable rule: when computing forms on a hypersurface $\{f=\text{const}\}$ embedded in a larger coordinate space, carry the ambient formula in full, isolate the multiples of $df$, and discard them only at the moment you pull back. This same bookkeeping governs, for instance, the Hopf connection computations of §4.2–§4.3, where the curvature is read off on $S^3$ from an ambient form on $\mathbb{R}^4$.

**Two verifications of one structural equation are worth more than one, because they cross-check the conventions.** The exercise proved $d\theta+\tfrac12[\theta\wedge\theta]=0$ three ways — intrinsically on the frame, in ambient coordinates, and by the matrix identity $d(g^{-1}dg)=-g^{-1}dg\wedge g^{-1}dg$ — and the agreement is what pins down the sign that Bär's Remark 2.5.9 misprints. This is a general research habit: when a normalisation-sensitive identity (a factor of $\tfrac12$, a bracket sign, an orientation) can be checked by an independent route, the independent route is the arbiter, and a discrepancy localises the error rather than hiding it. Here the sign-safe matrix computation is the arbiter, and it certifies the corrected $d\phi=-[X,Y](e)$. The pattern recurs whenever the abelian and matrix wedge conventions of [[Ex - The Bracket of Matrix-Valued 1-Forms is Twice the Wedge Square]] feed into a structure equation: compute once with the bracket, once with the bare wedge, and demand they agree.
