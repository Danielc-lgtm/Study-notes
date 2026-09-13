---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Ex - Curvature of the Standard Hopf Connection"
  - "Def - Isometry of Riemannian Manifolds"
  - "Thm - CP^1 is Diffeomorphic to S^2 via the Hopf Map"
  - "Thm - The Standard Connection on the Hopf Bundle"
  - "Def - Riemannian Volume Form"
  - "Ex - Volume of the n-Sphere via the Volume Form"
  - "Ex - The Round Metric on the Sphere via Restriction"
tags: [geometry, gauge-theory, characteristic-classes, hopf, riemannian-submersion]
---

# Problem Statement

Work on the round $3$-sphere $S^3=\{(z_0,z_1)\in\mathbb{C}^2:|z_0|^2+|z_1|^2=1\}$, carrying the diagonal right action $(z_0,z_1)\cdot\lambda=(z_0\lambda,z_1\lambda)$ of $U(1)=\{\lambda\in\mathbb{C}:|\lambda|=1\}$ and the Hopf projection $\pi\colon S^3\to\mathbb{CP}^1=S^3/U(1)$, $z\mapsto[z]$. Write $z_0=x_0+ix_1$ and $z_1=x_2+ix_3$, so that $S^3\subset\mathbb{R}^4$ is the unit sphere and $x=(x_0,x_1,x_2,x_3)$ has $|x|=1$. Let $a\in\Omega^1(S^3;i\mathbb{R})$ be the standard Hopf connection and $F_a\in\Omega^2(\mathbb{CP}^1;i\mathbb{R})$ its curvature.

Consider the map
$$\Phi\colon S^3\longrightarrow\mathbb{C}\times\mathbb{R}=\mathbb{R}^3,\qquad \Phi(z_0,z_1)=\Big(z_0\bar z_1,\ \tfrac12\big(|z_0|^2-|z_1|^2\big)\Big).$$

Prove the following, and thereby recover part (a) of [[Thm - First Chern Class of a Line Bundle from Curvature|the first-Chern-class theorem]] for the Hopf bundle by a route that never uses Stokes' theorem.

1. $\Phi$ takes values in the sphere $S^2_{1/2}=\{(w,t)\in\mathbb{C}\times\mathbb{R}:|w|^2+t^2=\tfrac14\}$ of radius $\tfrac12$, and $\Phi$ is constant on the Hopf fibres, so it descends to a smooth map $\bar\Phi\colon\mathbb{CP}^1\to S^2_{1/2}$ with $\bar\Phi\circ\pi=\Phi$.
2. $\bar\Phi$ is a bijection, with an explicit inverse.
3. On the horizontal orthonormal frame $v_2,v_3$ of the Hopf connection, the differentials $d\Phi(v_2),d\Phi(v_3)$ form an orthonormal pair in $\mathbb{R}^3$ tangent to $S^2_{1/2}$, while $d\Phi(v_1)=0$ on the vertical direction.
4. Consequently $\bar\Phi$ is a diffeomorphism, and $\Phi$ is a Riemannian submersion for the round metrics: the quotient metric on $\mathbb{CP}^1=S^3/U(1)$ is carried by $\bar\Phi$ to the round metric of radius $\tfrac12$, so $\bar\Phi$ is an isometry.
5. Therefore $F_a=2\,\mathrm{vol}_{S^2_{1/2}}\,i$, where $\mathrm{vol}_{S^2_{1/2}}$ is the round volume (area) form, and
$$\int_{\mathbb{CP}^1}F_a=2\,\operatorname{Vol}\!\big(S^2_{1/2}\big)\,i=2\pi i,\qquad\text{so}\qquad \frac{i}{2\pi}\int_{\mathbb{CP}^1}F_a=-1.$$

**Recall:**

The objects in play are the Hopf bundle and its standard connection, the horizontal frame and the curvature computed in chapter IV, the notions of Riemannian submersion and quotient metric, the round metric as a restriction of the ambient Euclidean metric, the Riemannian volume form, and the volume of a sphere.

*The Hopf connection, its horizontal frame, and its curvature (chapter IV).* By [[Thm - The Standard Connection on the Hopf Bundle|the standard-connection theorem]], the fundamental vector field of $i\in\mathfrak{u}(1)=i\mathbb{R}$ is $v(z)=iz$, and the connection form is $a_z(u)=\langle v(z),u\rangle\,i$ with $\langle\cdot,\cdot\rangle$ the Euclidean inner product of $\mathbb{R}^4$; its kernel $\ker a=v(z)^{\perp}\cap T_zS^3$ is the horizontal subspace. In real coordinates
$$a=\big(-x_1\,dx_0+x_0\,dx_1-x_3\,dx_2+x_2\,dx_3\big)\,i=\operatorname{Im}\big(\bar z_0\,dz_0+\bar z_1\,dz_1\big)\,i.$$
The three vector fields
$$v_1=(-x_1,x_0,-x_3,x_2),\qquad v_2=(-x_2,x_3,x_0,-x_1),\qquad v_3=(-x_3,-x_2,x_1,x_0)$$
form at each point of $S^3$ an oriented orthonormal basis of $T_zS^3$; here $v_1=v(z)=iz$ is the vertical (fundamental) field, and $v_2,v_3$ span the horizontal subspace $\ker a$. In complex notation $v_2\leftrightarrow(-\bar z_1,\bar z_0)$ and $v_3\leftrightarrow(-i\bar z_1,i\bar z_0)=iv_2$, so the complex structure $J$ (multiplication by $i$ in $\mathbb{C}^2$) sends $v_2$ to $v_3$. By [[Ex - Curvature of the Standard Hopf Connection|the chapter-IV curvature exercise]], the curvature satisfies
$$\pi^*F_a=da=2\big(dx_0\wedge dx_1+dx_2\wedge dx_3\big)\,i,\qquad F_a(\pi_*v_2,\pi_*v_3)=\pi^*F_a(v_2,v_3)=2i,$$
the value $2i$ being the same at every point of $S^3$; the curvature vanishes on any pair involving the vertical direction.

*Riemannian submersion and quotient metric.* A smooth surjective submersion $f\colon(M,g)\to(N,h)$ between Riemannian manifolds is a **Riemannian submersion** if, at each $p\in M$, the differential $df_p$ restricted to the horizontal subspace $H_p:=(\ker df_p)^{\perp}$ is a linear isometry onto $T_{f(p)}N$; equivalently, $df_p$ carries any orthonormal basis of $H_p$ to an orthonormal basis of $T_{f(p)}N$. When a compact Lie group $G$ acts on $(M,g)$ freely and by isometries with quotient manifold $M/G$, the **quotient metric** $h$ on $M/G$ is the unique metric for which the projection $M\to M/G$ is a Riemannian submersion: one sets $h(\pi_*X,\pi_*Y):=g(X^{\mathrm{hor}},Y^{\mathrm{hor}})$, and this is well defined precisely because the horizontal metric is $G$-invariant.

*The round metric and its volume form.* By [[Ex - The Round Metric on the Sphere via Restriction|the round-metric exercise]], the round metric on a sphere in Euclidean space is the restriction of the ambient Euclidean metric; the tangent space $T_pS^2_{1/2}$ is the Euclidean orthogonal complement of the position vector $p$, and lengths and angles of tangent vectors are the Euclidean ones. By [[Def - Riemannian Volume Form|the Riemannian volume form]], on an oriented Riemannian surface the volume (area) form $\mathrm{vol}$ is the unique $2$-form assigning $+1$ to every oriented orthonormal frame; a $2$-form $\omega$ on a surface equals $\omega(e_1,e_2)\,\mathrm{vol}$ for any oriented orthonormal frame $(e_1,e_2)$. By [[Ex - Volume of the n-Sphere via the Volume Form|the sphere-volume exercise]], the unit $2$-sphere has $\operatorname{Vol}(S^2)=4\pi$, and a homothety by the factor $r$ multiplies the area form by $r^2$, so $\operatorname{Vol}(S^2_r)=4\pi r^2$.

*The theorem being recovered (chapter VI).* The convention $c(E)=\det\big(1+\tfrac{i}{2\pi}F\big)$ (see [[Def - Chern Classes|the Chern-class definition]]) gives $c_1(L)=[\tfrac{i}{2\pi}F_A]$ for a Hermitian line bundle $L$ with unitary connection $A$; part (a) below is exactly the value of this class on the tautological bundle.

![[Thm - First Chern Class of a Line Bundle from Curvature#Statement]]

> [!warning] Convention: orientation of $\mathbb{CP}^1$
> Throughout, $\mathbb{CP}^1$ carries the **complex orientation**, the one for which $(X,JX)$ is a positively oriented real basis of any tangent plane, where $J$ is multiplication by $i$; since $v_3=Jv_2$, the frame $(\pi_*v_2,\pi_*v_3)$ is positively oriented. All integrals over $\mathbb{CP}^1$ are taken in this orientation, in agreement with the sign ledger on [[Def - The Hopf Bundle|the Hopf-bundle page]]. The map $\bar\Phi$ then transports this orientation to a definite orientation of $S^2_{1/2}$; the *area* $\operatorname{Vol}(S^2_{1/2})=\pi$ is independent of that choice, and only the orientation of $\mathbb{CP}^1$ enters the sign of $\int_{\mathbb{CP}^1}F_a$.

---

# Convergent Strategy

**Problem class.** This is a *geometric identification* problem that converts an integral into an area. The chapter-IV exercise already computed the curvature *pointwise* as the constant $F_a(\pi_*v_2,\pi_*v_3)=2i$ on an orthonormal frame; what is missing to get the *total* $\int_{\mathbb{CP}^1}F_a$ is a metric on the base with a known volume. The whole task is to supply that metric — the round metric of radius $\tfrac12$ — by exhibiting an explicit isometry $\bar\Phi$, and then read off the integral as (constant curvature density) $\times$ (area). The problem is a ⭐⭐⭐ because the isometry claim is a genuine multi-part computation: fibre-constancy, bijectivity, and the orthonormality of the pushed-forward frame must each be proved, and the last is a nontrivial identity in the four real coordinates.

**Assumption pattern.** The single hypothesis that does all the work is that $U(1)$ acts on $S^3$ *by isometries* (it acts by unit-modulus scalar multiplication, which preserves the Euclidean metric of $\mathbb{C}^2=\mathbb{R}^4$). This is what makes the quotient metric well defined, and it is what makes a Riemannian submersion the right notion: the metric on $\mathbb{CP}^1$ is *forced* once we demand that $\pi$ be a Riemannian submersion. The recognisable trigger is the phrase "quotient by an isometric group action": whenever it appears, the horizontal part of the upstairs metric descends, and any explicit map to a model space that is orthonormal-on-horizontal-frames is automatically an isometry.

**Theorem routing.** The route is: (i) show $\Phi$ lands in $S^2_{1/2}$ and is fibrewise constant, so it descends to $\bar\Phi$ (universal property of the quotient, [[Def - Complex Projective Space as a Quotient|CP^1 as a quotient]]); (ii) invert $\bar\Phi$ explicitly to get bijectivity; (iii) compute $d\Phi(v_2),d\Phi(v_3)$ and verify $\lVert d\Phi(v_2)\rVert=\lVert d\Phi(v_3)\rVert=1$ and $\langle d\Phi(v_2),d\Phi(v_3)\rangle=0$ in $\mathbb{R}^3$ (this is the Riemannian-submersion condition, using [[Ex - The Round Metric on the Sphere via Restriction|round metric = restriction]]); (iv) conclude $\bar\Phi$ is an isometry, so the quotient volume form is $\bar\Phi^*\mathrm{vol}_{S^2_{1/2}}$; (v) expand $F_a=F_a(\pi_*v_2,\pi_*v_3)\,\mathrm{vol}=2i\,\mathrm{vol}$ ([[Def - Riemannian Volume Form|volume form]]) and integrate using $\operatorname{Vol}(S^2_{1/2})=\pi$ ([[Ex - Volume of the n-Sphere via the Volume Form|sphere volume]]). The output $\frac{i}{2\pi}\int F_a=-1$ then reproduces [[Thm - First Chern Class of a Line Bundle from Curvature|part (a)]].

**Key decision point.** The one non-obvious move is *doing the differential computation in complex notation*. Written in the four real coordinates, $d\Phi(v_2)$ and $d\Phi(v_3)$ are messy quadratic vectors and the orthonormality identities look opaque. Rewriting the horizontal fields as $v_2\leftrightarrow(-\bar z_1,\bar z_0)$, $v_3=iv_2$, and $\Phi=(z_0\bar z_1,\tfrac12(|z_0|^2-|z_1|^2))$, the differentials collapse to $d\Phi(v_2)=(z_0^2-\bar z_1^2,\,-2\operatorname{Re}(z_0z_1))$ and $d\Phi(v_3)=(-i(z_0^2+\bar z_1^2),\,-2\operatorname{Im}(z_0z_1))$, and the three identities each reduce, via $\operatorname{Re}(W)^2\pm\operatorname{Im}(W)^2$ manipulations, to the single relation $|z_0|^2+|z_1|^2=1$. Recognising that complex bookkeeping linearises the whole computation is the crux.

---

# Legal Operations Used

This solution deploys the following operations (numbered as on [[Gauge Theory VI — Chern–Weil Theory, Characteristic Classes, and the Chern–Simons Functional#Legal Operations|the topic page's Legal Operations]]; where the topic page is not yet assembled the operation is named descriptively and the orchestrator will reconcile numbers).

1. **Descend a fibrewise-constant map through a quotient.** Show a map on the total space is constant on orbits and invoke the universal property of the smooth quotient $S^3\to\mathbb{CP}^1$ to obtain a smooth map on the base.

2. **Certify a diffeomorphism by an explicit inverse plus full rank.** Produce the inverse map in closed form to get bijectivity, and use the rank of the differential on the horizontal frame to get the local-diffeomorphism property; combine into "bijective local diffeomorphism, hence diffeomorphism".

3. **Verify a Riemannian submersion on an orthonormal horizontal frame.** Reduce the isometry claim to checking that the differential sends the horizontal orthonormal pair to an orthonormal pair in the target, using that the round metric is the restriction of the ambient Euclidean metric.

4. **Read a top-degree form off its value on an oriented orthonormal frame.** On a surface, expand a $2$-form as (its value on an oriented orthonormal frame) times the volume form; here this turns the pointwise curvature value $2i$ into $F_a=2i\,\mathrm{vol}$.

5. **Convert a total integral into a curvature density times an area.** Integrate a constant multiple of the volume form by multiplying the constant by the total volume, computed from the sphere-volume formula and the homothety scaling of the area form.

6. **Transport an orientation through an isometry to fix a sign.** Use that $\bar\Phi$ carries the complex orientation of $\mathbb{CP}^1$ to a definite orientation of $S^2_{1/2}$, keeping the sign of the integral tied to the complex orientation.

---

# Hints

> [!note]- Hint 1
> Do not try to integrate a $2$-form on $\mathbb{CP}^1$ directly. The chapter-IV exercise already gives you the curvature as the *constant* value $F_a(\pi_*v_2,\pi_*v_3)=2i$ on an orthonormal frame. If you knew that $\mathbb{CP}^1$ with its quotient metric were a round sphere of a known radius, the integral would just be $2i$ times the area. So the real task is: identify the quotient metric.

> [!note]- Hint 2
> The candidate identification is the map $\Phi(z_0,z_1)=(z_0\bar z_1,\tfrac12(|z_0|^2-|z_1|^2))$. First check the two easy structural facts: that $|\Phi(z)|=\tfrac12$ for every $z\in S^3$ (set $a=|z_0|^2$, $b=|z_1|^2$, $a+b=1$, and expand), and that $\Phi(z\lambda)=\Phi(z)$ for $|\lambda|=1$. The first puts $\Phi$ on $S^2_{1/2}$; the second lets it descend to the quotient.

> [!note]- Hint 3
> To show $\bar\Phi$ is an isometry, you only need the Riemannian-submersion condition: $d\Phi$ sends the horizontal orthonormal pair $v_2,v_3$ to an orthonormal pair on $S^2_{1/2}$ (the round metric there is just the Euclidean metric restricted). Rewrite everything in complex notation: $v_2\leftrightarrow(-\bar z_1,\bar z_0)$, $v_3=iv_2$. For a tangent $\dot z=(\dot z_0,\dot z_1)$, differentiate the two components of $\Phi$: $\frac{d}{dt}(z_0\bar z_1)=\dot z_0\bar z_1+z_0\overline{\dot z_1}$ and $\frac{d}{dt}\tfrac12(|z_0|^2-|z_1|^2)=\operatorname{Re}(\dot z_0\bar z_0-\dot z_1\bar z_1)$.

> [!note]- Hint 4
> You should find $d\Phi(v_2)=(z_0^2-\bar z_1^2,\,-2\operatorname{Re}(z_0z_1))$ and $d\Phi(v_3)=(-i(z_0^2+\bar z_1^2),\,-2\operatorname{Im}(z_0z_1))$. For the norms use $4\operatorname{Re}(W)^2=2|W|^2+2\operatorname{Re}(W^2)$ and $4\operatorname{Im}(W)^2=2|W|^2-2\operatorname{Re}(W^2)$ with $W=z_0z_1$; everything telescopes to $(|z_0|^2+|z_1|^2)^2=1$. For the inner product in $\mathbb{C}\times\mathbb{R}$, use $\langle(A,s),(B,t)\rangle=\operatorname{Re}(A\bar B)+st$ and watch the two $\operatorname{Im}(z_0^2z_1^2)$ terms cancel.

> [!note]- Hint 5
> Once $\bar\Phi$ is an isometry, $F_a=F_a(\pi_*v_2,\pi_*v_3)\,\mathrm{vol}_{S^2_{1/2}}=2i\,\mathrm{vol}$, because $(\pi_*v_2,\pi_*v_3)$ is an oriented orthonormal frame. Then $\int_{\mathbb{CP}^1}F_a=2i\operatorname{Vol}(S^2_{1/2})$ and $\operatorname{Vol}(S^2_{1/2})=4\pi(\tfrac12)^2=\pi$. Finish with $\frac{i}{2\pi}\cdot2\pi i=i^2=-1$.

---

# Solution

The plan is to build the isometry $\bar\Phi$ in four passes — descent, bijectivity, the differential computation, and the isometry conclusion — and then convert the pointwise curvature into a total integral. The engine is that $U(1)$ acts by isometries, so the quotient metric is forced and any explicit orthonormal-on-horizontal map is automatically an isometry; the arithmetic engine is complex notation, which turns three real-coordinate identities into the single relation $|z_0|^2+|z_1|^2=1$. The final integral is (constant curvature density $2i$) $\times$ (area $\pi$) $=2\pi i$, and dividing by $2\pi/i$ gives the Chern number $-1$.

**Step 1: $\Phi$ lands in $S^2_{1/2}$, is constant on Hopf fibres, and descends to a smooth $\bar\Phi$.**

$\Phi$ maps $S^3$ into the radius-$\tfrac12$ sphere and satisfies $\Phi(z\lambda)=\Phi(z)$ for $\lambda\in U(1)$, so it factors as $\bar\Phi\circ\pi$ for a smooth $\bar\Phi\colon\mathbb{CP}^1\to S^2_{1/2}$.

> [!note]- Derivation
> Write $a=|z_0|^2$ and $b=|z_1|^2$, so $a,b\ge0$ and $a+b=1$ on $S^3$. The image point $\Phi(z)=(z_0\bar z_1,\tfrac12(a-b))$ has squared Euclidean norm in $\mathbb{C}\times\mathbb{R}$
> $$|z_0\bar z_1|^2+\tfrac14(a-b)^2=ab+\tfrac14(a-b)^2 \qquad\text{(since }|z_0\bar z_1|^2=|z_0|^2|z_1|^2=ab\text{)}$$
> $$=\tfrac14\big(4ab+a^2-2ab+b^2\big)=\tfrac14\big(a^2+2ab+b^2\big)=\tfrac14(a+b)^2=\tfrac14 \qquad\text{(since }a+b=1\text{).}$$
> Hence $\lVert\Phi(z)\rVert=\tfrac12$, so $\Phi(S^3)\subseteq S^2_{1/2}$.
>
> For fibre-constancy, take $\lambda\in U(1)$, so $|\lambda|=1$. Then
> $$\Phi(z_0\lambda,z_1\lambda)=\Big((z_0\lambda)\overline{(z_1\lambda)},\ \tfrac12\big(|z_0\lambda|^2-|z_1\lambda|^2\big)\Big)=\Big(z_0\bar z_1\,|\lambda|^2,\ \tfrac12\big(|z_0|^2-|z_1|^2\big)\Big)=\Phi(z) \qquad\text{(since }|\lambda|^2=1\text{),}$$
> so $\Phi$ is constant on each Hopf fibre $\pi^{-1}([z])=z\cdot U(1)$.
>
> The Hopf projection $\pi\colon S^3\to\mathbb{CP}^1=S^3/U(1)$ is a smooth surjective submersion ([[Def - Complex Projective Space as a Quotient|complex projective space as a quotient]]). A smooth map that is constant on the fibres of a surjective submersion factors uniquely through the quotient as a smooth map: define $\bar\Phi([z]):=\Phi(z)$, well defined by fibre-constancy, and smooth because $\pi$ admits local smooth sections $s$ and $\bar\Phi=\Phi\circ s$ locally. Thus $\bar\Phi\circ\pi=\Phi$.

**Step 2: $\bar\Phi$ is a bijection, with explicit inverse.**

Every point of $S^2_{1/2}$ has exactly one preimage class in $\mathbb{CP}^1$; the correspondence is $(w,t)\mapsto[z_0:z_1]$ with $|z_0|^2=\tfrac12+t$, $|z_1|^2=\tfrac12-t$, $z_0\bar z_1=w$.

> [!note]- Derivation
> Fix $(w,t)\in S^2_{1/2}$, so $w\in\mathbb{C}$, $t\in\mathbb{R}$ and $|w|^2+t^2=\tfrac14$; in particular $-\tfrac12\le t\le\tfrac12$. We solve $\Phi(z)=(w,t)$ for $[z]\in\mathbb{CP}^1$.
>
> The equation $\tfrac12(|z_0|^2-|z_1|^2)=t$ together with $|z_0|^2+|z_1|^2=1$ forces
> $$|z_0|^2=\tfrac12+t,\qquad |z_1|^2=\tfrac12-t,$$
> both non-negative because $|t|\le\tfrac12$. These fix the moduli of $z_0,z_1$ for any preimage.
>
> *Existence.* Consider first $-\tfrac12<t<\tfrac12$, so both moduli are positive. Choose the representative with $z_0=\sqrt{\tfrac12+t}>0$ real (using the phase freedom of $[z]$), and set $z_1:=\bar w/z_0$. Then $z_0\bar z_1=z_0\cdot(w/z_0)=w$ (as $z_0$ is real, $\bar z_1=w/z_0$), and
> $$|z_1|^2=\frac{|w|^2}{z_0^2}=\frac{|w|^2}{\tfrac12+t}=\frac{(\tfrac12-t)(\tfrac12+t)}{\tfrac12+t}=\tfrac12-t \qquad\text{(since }|w|^2=\tfrac14-t^2=(\tfrac12-t)(\tfrac12+t)\text{),}$$
> so $(z_0,z_1)\in S^3$ and $\Phi(z)=(w,t)$. At the poles $t=\tfrac12$ (then $|z_1|=0$, giving $z=(1,0)$, i.e. $[1:0]$, and $w=z_0\bar z_1=0$) and $t=-\tfrac12$ (then $z=(0,1)$, i.e. $[0:1]$, and $w=0$) the preimage is again the stated point; these are the only points of $S^2_{1/2}$ with $w=0$ and $t=\pm\tfrac12$.
>
> *Uniqueness.* Suppose $\Phi(z)=\Phi(z')=(w,t)$. The moduli of both coordinates are fixed by $t$ as above. If both are nonzero, write $z_0=|z_0|e^{i\alpha_0}$, $z_1=|z_1|e^{i\alpha_1}$; then $z_0\bar z_1=|z_0||z_1|e^{i(\alpha_0-\alpha_1)}=w$ fixes the phase difference $\alpha_0-\alpha_1$, and the individual phases are free only through the common factor $e^{i\alpha_1}$, which is exactly the $U(1)$-action. Hence $z'=z\cdot\lambda$ for some $\lambda\in U(1)$, so $[z]=[z']$. If one modulus vanishes the class is a pole and is determined outright. Thus $\bar\Phi$ is injective, and with existence it is a bijection whose inverse is $(w,t)\mapsto\big[\sqrt{\tfrac12+t}:\bar w/\sqrt{\tfrac12+t}\big]$ away from the pole $t=-\tfrac12$ (and symmetrically near it).

**Step 3: the differential on the frame — $d\Phi(v_1)=0$ and $d\Phi(v_2),d\Phi(v_3)$ are orthonormal in $\mathbb{R}^3$.**

Writing $d\Phi$ in complex notation, the vertical field is annihilated and the horizontal pair maps to an orthonormal pair.

> [!note]- Derivation
> Identify a tangent vector to $S^3$ at $z$ with a pair $\dot z=(\dot z_0,\dot z_1)\in\mathbb{C}^2$ satisfying $\operatorname{Re}\langle\dot z,z\rangle_{\mathbb{C}}=0$, where $\langle a,b\rangle_{\mathbb{C}}=a_0\bar b_0+a_1\bar b_1$; the ambient real inner product is $\langle a,b\rangle=\operatorname{Re}\langle a,b\rangle_{\mathbb{C}}$. Differentiating the two components of $\Phi$ along a curve $z(s)$ with $\dot z=\tfrac{d}{ds}z$,
> $$d\Phi_{\mathbb{C}}(\dot z)=\frac{d}{ds}\big(z_0\bar z_1\big)=\dot z_0\,\bar z_1+z_0\,\overline{\dot z_1},\qquad d\Phi_{\mathbb{R}}(\dot z)=\frac{d}{ds}\,\tfrac12\big(z_0\bar z_0-z_1\bar z_1\big)=\operatorname{Re}\big(\dot z_0\,\bar z_0-\dot z_1\,\bar z_1\big),$$
> the second because $\tfrac12\tfrac{d}{ds}(z_j\bar z_j)=\operatorname{Re}(\dot z_j\bar z_j)$. Here $d\Phi(\dot z)=(d\Phi_{\mathbb{C}}(\dot z),d\Phi_{\mathbb{R}}(\dot z))\in\mathbb{C}\times\mathbb{R}$.
>
> **Vertical direction.** The vertical field is $v_1=v(z)=iz$, that is $\dot z=(iz_0,iz_1)$. Then
> $$d\Phi_{\mathbb{C}}(v_1)=(iz_0)\bar z_1+z_0\overline{(iz_1)}=iz_0\bar z_1-iz_0\bar z_1=0 \qquad\text{(since }\overline{iz_1}=-i\bar z_1\text{),}$$
> $$d\Phi_{\mathbb{R}}(v_1)=\operatorname{Re}\big(iz_0\bar z_0-iz_1\bar z_1\big)=\operatorname{Re}\big(i(|z_0|^2-|z_1|^2)\big)=0 \qquad\text{(a purely imaginary quantity).}$$
> Hence $d\Phi(v_1)=0$: the differential annihilates the fibre direction, as it must for a map that is constant on fibres.
>
> **Horizontal fields.** In complex notation $v_2\leftrightarrow(-\bar z_1,\bar z_0)$ and $v_3=iv_2\leftrightarrow(-i\bar z_1,i\bar z_0)$. For $v_2$ (so $\dot z_0=-\bar z_1$, $\dot z_1=\bar z_0$):
> $$d\Phi_{\mathbb{C}}(v_2)=(-\bar z_1)\bar z_1+z_0\,\overline{\bar z_0}=-\bar z_1^{\,2}+z_0^{\,2}=z_0^{\,2}-\bar z_1^{\,2} \qquad\text{(since }\overline{\bar z_0}=z_0\text{),}$$
> $$d\Phi_{\mathbb{R}}(v_2)=\operatorname{Re}\big((-\bar z_1)\bar z_0-\bar z_0\bar z_1\big)=\operatorname{Re}\big(-2\bar z_0\bar z_1\big)=-2\operatorname{Re}(z_0z_1) \qquad\text{(since }\operatorname{Re}(\bar z_0\bar z_1)=\operatorname{Re}(\overline{z_0z_1})=\operatorname{Re}(z_0z_1)\text{).}$$
> For $v_3$ (so $\dot z_0=-i\bar z_1$, $\dot z_1=i\bar z_0$):
> $$d\Phi_{\mathbb{C}}(v_3)=(-i\bar z_1)\bar z_1+z_0\,\overline{(i\bar z_0)}=-i\bar z_1^{\,2}+z_0(-i)z_0=-i\big(z_0^{\,2}+\bar z_1^{\,2}\big) \qquad\text{(since }\overline{i\bar z_0}=-iz_0\text{),}$$
> $$d\Phi_{\mathbb{R}}(v_3)=\operatorname{Re}\big((-i\bar z_1)\bar z_0-(i\bar z_0)\bar z_1\big)=\operatorname{Re}\big(-2i\,\bar z_0\bar z_1\big)=2\operatorname{Im}(\bar z_0\bar z_1)=-2\operatorname{Im}(z_0z_1),$$
> using $\operatorname{Re}(-2i\,W)=2\operatorname{Im}(W)$ and $\operatorname{Im}(\bar z_0\bar z_1)=\operatorname{Im}(\overline{z_0z_1})=-\operatorname{Im}(z_0z_1)$. Summarising,
> $$d\Phi(v_2)=\big(z_0^{\,2}-\bar z_1^{\,2},\ -2\operatorname{Re}(z_0z_1)\big),\qquad d\Phi(v_3)=\big(-i(z_0^{\,2}+\bar z_1^{\,2}),\ -2\operatorname{Im}(z_0z_1)\big).$$
>
> **First norm.** With $W:=z_0z_1$, so $|W|^2=|z_0|^2|z_1|^2$ and $W^2=z_0^{\,2}z_1^{\,2}$, and using $4\operatorname{Re}(W)^2=2|W|^2+2\operatorname{Re}(W^2)$,
> $$\lVert d\Phi(v_2)\rVert^2=\big|z_0^{\,2}-\bar z_1^{\,2}\big|^2+4\operatorname{Re}(z_0z_1)^2.$$
> Now $\big|z_0^{\,2}-\bar z_1^{\,2}\big|^2=|z_0|^4+|z_1|^4-2\operatorname{Re}\big(z_0^{\,2}\,\overline{\bar z_1^{\,2}}\big)=|z_0|^4+|z_1|^4-2\operatorname{Re}(z_0^{\,2}z_1^{\,2})$ (since $\overline{\bar z_1^{\,2}}=z_1^{\,2}$), and $4\operatorname{Re}(z_0z_1)^2=2|z_0|^2|z_1|^2+2\operatorname{Re}(z_0^{\,2}z_1^{\,2})$. Adding, the $\pm2\operatorname{Re}(z_0^{\,2}z_1^{\,2})$ terms cancel:
> $$\lVert d\Phi(v_2)\rVert^2=|z_0|^4+2|z_0|^2|z_1|^2+|z_1|^4=\big(|z_0|^2+|z_1|^2\big)^2=1 \qquad\text{(since }|z_0|^2+|z_1|^2=1\text{).}$$
>
> **Second norm.** Symmetrically, using $4\operatorname{Im}(W)^2=2|W|^2-2\operatorname{Re}(W^2)$,
> $$\lVert d\Phi(v_3)\rVert^2=\big|z_0^{\,2}+\bar z_1^{\,2}\big|^2+4\operatorname{Im}(z_0z_1)^2=\big(|z_0|^4+|z_1|^4+2\operatorname{Re}(z_0^{\,2}z_1^{\,2})\big)+\big(2|z_0|^2|z_1|^2-2\operatorname{Re}(z_0^{\,2}z_1^{\,2})\big)=1,$$
> again by $\big(|z_0|^2+|z_1|^2\big)^2=1$. (The factor $|-i|=1$ leaves the complex part's modulus unchanged.)
>
> **Orthogonality.** The inner product on $\mathbb{C}\times\mathbb{R}$ is $\langle(A,s),(B,t)\rangle=\operatorname{Re}(A\bar B)+st$. With $A=z_0^{\,2}-\bar z_1^{\,2}$, $B=-i(z_0^{\,2}+\bar z_1^{\,2})$, so $\bar B=i(\bar z_0^{\,2}+z_1^{\,2})$,
> $$A\bar B=i\big(z_0^{\,2}-\bar z_1^{\,2}\big)\big(\bar z_0^{\,2}+z_1^{\,2}\big)=i\big(|z_0|^4-|z_1|^4+z_0^{\,2}z_1^{\,2}-\bar z_0^{\,2}\bar z_1^{\,2}\big)=i\big(|z_0|^4-|z_1|^4\big)-2\operatorname{Im}(z_0^{\,2}z_1^{\,2}),$$
> where $z_0^{\,2}z_1^{\,2}-\bar z_0^{\,2}\bar z_1^{\,2}=z_0^{\,2}z_1^{\,2}-\overline{z_0^{\,2}z_1^{\,2}}=2i\operatorname{Im}(z_0^{\,2}z_1^{\,2})$ and $i\cdot2i=-2$. Hence $\operatorname{Re}(A\bar B)=-2\operatorname{Im}(z_0^{\,2}z_1^{\,2})$. For the real parts, with $s=-2\operatorname{Re}(z_0z_1)$ and $t=-2\operatorname{Im}(z_0z_1)$,
> $$st=4\operatorname{Re}(z_0z_1)\operatorname{Im}(z_0z_1)=2\operatorname{Im}\big((z_0z_1)^2\big)=2\operatorname{Im}(z_0^{\,2}z_1^{\,2}) \qquad\text{(since }2\operatorname{Re}(W)\operatorname{Im}(W)=\operatorname{Im}(W^2)\text{).}$$
> Therefore
> $$\big\langle d\Phi(v_2),d\Phi(v_3)\big\rangle=\operatorname{Re}(A\bar B)+st=-2\operatorname{Im}(z_0^{\,2}z_1^{\,2})+2\operatorname{Im}(z_0^{\,2}z_1^{\,2})=0.$$
> Both differentials are tangent to $S^2_{1/2}$ at $\Phi(z)$ automatically, since $\Phi(S^3)\subseteq S^2_{1/2}$ and hence $d\Phi_z$ maps $T_zS^3$ into $T_{\Phi(z)}S^2_{1/2}$. Thus $\big(d\Phi(v_2),d\Phi(v_3)\big)$ is an orthonormal pair in $T_{\Phi(z)}S^2_{1/2}$ for the round metric (= restriction of the Euclidean metric, [[Ex - The Round Metric on the Sphere via Restriction|round metric via restriction]]).
>
> *Concrete instance.* At $z=(1,0)$, i.e. $x=(1,0,0,0)$, one has $v_2=(0,0,1,0)$, $v_3=(0,0,0,1)$ and $\Phi=(0,\tfrac12)$ (the north pole $(0,0,\tfrac12)$). The formulae give $d\Phi(v_2)=(1,0,0)$ and $d\Phi(v_3)=(0,-1,0)$: unit length, orthogonal, and both tangent to $S^2_{1/2}$ at the north pole (whose tangent plane is $\{w\in\mathbb{C}\}\times\{0\}$), matching the general result.

**Step 4: $\bar\Phi$ is a diffeomorphism and an isometry.**

The rank-$2$ differential on the horizontal frame together with bijectivity makes $\bar\Phi$ a diffeomorphism, and orthonormality makes $\Phi$ a Riemannian submersion, so $\bar\Phi$ is an isometry onto $S^2_{1/2}$.

> [!note]- Derivation
> At each $z$, $\ker d\Phi_z\supseteq\mathbb{R}v_1$ (Step 3), and $d\Phi_z$ restricted to the horizontal plane $H_z=\operatorname{span}(v_2,v_3)$ is injective, since it sends the orthonormal pair $(v_2,v_3)$ to the orthonormal — hence linearly independent — pair $(d\Phi(v_2),d\Phi(v_3))$. As $T_zS^3=\mathbb{R}v_1\oplus H_z$, the rank of $d\Phi_z$ is exactly $2=\dim S^2_{1/2}$, so $\Phi$ is a submersion and $d\bar\Phi_{[z]}$ is a linear isomorphism $T_{[z]}\mathbb{CP}^1\to T_{\Phi(z)}S^2_{1/2}$. Thus $\bar\Phi$ is a local diffeomorphism; being also a bijection (Step 2), it is a diffeomorphism. (This reproves, with the concrete target $S^2_{1/2}$, that $\mathbb{CP}^1$ is diffeomorphic to a round $2$-sphere; compare [[Thm - CP^1 is Diffeomorphic to S^2 via the Hopf Map|the diffeomorphism theorem]], which gives the same statement for the unit sphere, related to $S^2_{1/2}$ by the homothety $x\mapsto\tfrac12 x$.)
>
> The quotient metric on $\mathbb{CP}^1$ is defined by $g_{\mathbb{CP}^1}(\pi_*X,\pi_*Y)=g_{S^3}(X^{\mathrm{hor}},Y^{\mathrm{hor}})$, which is well defined because $U(1)$ acts by isometries; in particular $(\pi_*v_2,\pi_*v_3)$ is an orthonormal frame of $T_{[z]}\mathbb{CP}^1$, since $(v_2,v_3)$ is an orthonormal frame of $H_z$. By Step 3, $d\bar\Phi$ sends this orthonormal frame to the orthonormal frame $(d\Phi(v_2),d\Phi(v_3))$ of $T_{\Phi(z)}S^2_{1/2}$. A linear map sending an orthonormal basis to an orthonormal basis is a linear isometry; hence $d\bar\Phi_{[z]}$ is a linear isometry at every point, so $\bar\Phi$ is a Riemannian isometry ([[Def - Isometry of Riemannian Manifolds|isometry of Riemannian manifolds]]) from $\mathbb{CP}^1$ with the quotient metric onto $S^2_{1/2}$ with the round metric. Equivalently, $\Phi=\bar\Phi\circ\pi$ is a Riemannian submersion. In particular the quotient metric *is* the round metric of radius $\tfrac12$, transported by $\bar\Phi^{-1}$.

**Step 5: $F_a=2\,\mathrm{vol}_{S^2_{1/2}}\,i$ and $\int_{\mathbb{CP}^1}F_a=2\pi i$.**

Because the curvature has the constant value $2i$ on the oriented orthonormal frame, it equals $2i$ times the round volume form; integrating gives $2i$ times the area of $S^2_{1/2}$.

> [!note]- Derivation
> Identify $\mathbb{CP}^1$ with $S^2_{1/2}$ via the isometry $\bar\Phi$, and give it the complex orientation, for which $(\pi_*v_2,\pi_*v_3)=(\pi_*v_2,J\pi_*v_2)$ is a *positively* oriented orthonormal frame (Convention callout above). The curvature $F_a$ is a $2$-form on the surface $\mathbb{CP}^1$; a $2$-form on an oriented surface equals its value on any oriented orthonormal frame times the volume form ([[Def - Riemannian Volume Form|Riemannian volume form]]):
> $$F_a=F_a(\pi_*v_2,\pi_*v_3)\,\mathrm{vol}_{S^2_{1/2}}=2i\,\mathrm{vol}_{S^2_{1/2}},$$
> using $F_a(\pi_*v_2,\pi_*v_3)=2i$ from [[Ex - Curvature of the Standard Hopf Connection|the chapter-IV curvature exercise]] and $\mathrm{vol}_{S^2_{1/2}}(\pi_*v_2,\pi_*v_3)=1$; the value $2i$ is the same constant at every point, so the identity holds globally.
>
> The area of $S^2_{1/2}$ is, by the sphere-volume computation and the scaling of the area form under the homothety $x\mapsto\tfrac12 x$ (which multiplies the area form by $(\tfrac12)^2$),
> $$\operatorname{Vol}\!\big(S^2_{1/2}\big)=\Big(\tfrac12\Big)^2\operatorname{Vol}(S^2)=\tfrac14\cdot4\pi=\pi,$$
> using $\operatorname{Vol}(S^2)=4\pi$ from [[Ex - Volume of the n-Sphere via the Volume Form|the sphere-volume exercise]].
> Therefore
> $$\int_{\mathbb{CP}^1}F_a=\int_{\mathbb{CP}^1}2i\,\mathrm{vol}_{S^2_{1/2}}=2i\int_{S^2_{1/2}}\mathrm{vol}_{S^2_{1/2}}=2i\operatorname{Vol}\!\big(S^2_{1/2}\big)=2i\cdot\pi=2\pi i,$$
> the middle equality because $\bar\Phi$ is an orientation-compatible isometry, hence preserves the integral of the volume form ([[Thm - Change of Variables for Integration on Manifolds|change of variables]]).

**Step 6: read off the Chern number and recover part (a).**

The normalisation $c_1(L)=[\tfrac{i}{2\pi}F_A]$ turns the integral into $-1$.

> [!note]- Derivation
> With the series convention $c_1(L)=\big[\tfrac{i}{2\pi}F_A\big]$ ([[Def - Chern Classes|Chern classes]]) applied to the tautological bundle $\mathcal{O}(-1)\to\mathbb{CP}^1$, whose induced connection has curvature $F_a$,
> $$\int_{\mathbb{CP}^1}c_1(\mathcal{O}(-1))=\frac{i}{2\pi}\int_{\mathbb{CP}^1}F_a=\frac{i}{2\pi}\cdot2\pi i=i^2=-1.$$
> This is exactly the value asserted in part (a) of [[Thm - First Chern Class of a Line Bundle from Curvature|the first-Chern-class theorem]]. The present derivation reached it *geometrically* — by identifying the base with a round sphere of known area — rather than by the Stokes/winding-number computation used in the theorem's proof and in [[Ex - The Chern Number of the Hopf Line Bundle over CP^1 is Minus One|the companion exercise]]; the two independent routes give the same integer, which pins the orientation and the sign.

> [!note]- Complete formal solution
> **Claim.** The map $\Phi(z_0,z_1)=(z_0\bar z_1,\tfrac12(|z_0|^2-|z_1|^2))$ descends to an isometry $\bar\Phi\colon\mathbb{CP}^1\to S^2_{1/2}$ from the quotient metric to the round metric of radius $\tfrac12$; consequently $F_a=2\,\mathrm{vol}_{S^2_{1/2}}\,i$ and $\frac{i}{2\pi}\int_{\mathbb{CP}^1}F_a=-1$.
>
> Set $a=|z_0|^2$, $b=|z_1|^2$; on $S^3$, $a+b=1$. Then $|z_0\bar z_1|^2+\tfrac14(a-b)^2=ab+\tfrac14(a-b)^2=\tfrac14(a+b)^2=\tfrac14$, so $\Phi(S^3)\subseteq S^2_{1/2}$; and $\Phi(z\lambda)=(z_0\bar z_1|\lambda|^2,\tfrac12(a-b))=\Phi(z)$ for $|\lambda|=1$. Hence $\Phi$ factors through the submersion $\pi$ as a smooth $\bar\Phi\colon\mathbb{CP}^1\to S^2_{1/2}$.
>
> Given $(w,t)\in S^2_{1/2}$ ($|w|^2+t^2=\tfrac14$, $|t|\le\tfrac12$), the equations $\tfrac12(|z_0|^2-|z_1|^2)=t$ and $|z_0|^2+|z_1|^2=1$ force $|z_0|^2=\tfrac12+t$, $|z_1|^2=\tfrac12-t$; choosing $z_0=\sqrt{\tfrac12+t}>0$ and $z_1=\bar w/z_0$ gives $z_0\bar z_1=w$ and $|z_1|^2=|w|^2/(\tfrac12+t)=\tfrac12-t$, so $\bar\Phi$ is onto, and the class $[z]$ is determined by $(w,t)$ up to the phase absorbed by $U(1)$, so $\bar\Phi$ is a bijection.
>
> Identify $T_zS^3\ni\dot z=(\dot z_0,\dot z_1)$; then $d\Phi_{\mathbb{C}}(\dot z)=\dot z_0\bar z_1+z_0\overline{\dot z_1}$, $d\Phi_{\mathbb{R}}(\dot z)=\operatorname{Re}(\dot z_0\bar z_0-\dot z_1\bar z_1)$. For $v_1=iz$: $d\Phi(v_1)=0$. For $v_2\leftrightarrow(-\bar z_1,\bar z_0)$ and $v_3=iv_2\leftrightarrow(-i\bar z_1,i\bar z_0)$:
> $$d\Phi(v_2)=\big(z_0^{\,2}-\bar z_1^{\,2},\,-2\operatorname{Re}(z_0z_1)\big),\qquad d\Phi(v_3)=\big(-i(z_0^{\,2}+\bar z_1^{\,2}),\,-2\operatorname{Im}(z_0z_1)\big).$$
> Using $4\operatorname{Re}(W)^2=2|W|^2+2\operatorname{Re}(W^2)$ and $4\operatorname{Im}(W)^2=2|W|^2-2\operatorname{Re}(W^2)$ with $W=z_0z_1$, both norms equal $(|z_0|^2+|z_1|^2)^2=1$; and $\langle d\Phi(v_2),d\Phi(v_3)\rangle=\operatorname{Re}(A\bar B)+st=-2\operatorname{Im}(z_0^{\,2}z_1^{\,2})+2\operatorname{Im}(z_0^{\,2}z_1^{\,2})=0$. Since $\Phi(S^3)\subseteq S^2_{1/2}$, these lie in $T_{\Phi(z)}S^2_{1/2}$, where the round metric is the Euclidean restriction. Thus $d\Phi_z$ has rank $2$ (so $\bar\Phi$ is a local diffeomorphism, hence a diffeomorphism) and sends the horizontal orthonormal frame $(v_2,v_3)$ to an orthonormal frame; as $U(1)$ acts by isometries, $(\pi_*v_2,\pi_*v_3)$ is orthonormal for the quotient metric, so $d\bar\Phi$ is a linear isometry everywhere and $\bar\Phi$ is a Riemannian isometry: the quotient metric is the round metric of radius $\tfrac12$.
>
> Orient $\mathbb{CP}^1$ by the complex orientation, so $(\pi_*v_2,\pi_*v_3)=(\pi_*v_2,J\pi_*v_2)$ is positive and $\mathrm{vol}_{S^2_{1/2}}(\pi_*v_2,\pi_*v_3)=1$. Then $F_a=F_a(\pi_*v_2,\pi_*v_3)\,\mathrm{vol}_{S^2_{1/2}}=2i\,\mathrm{vol}_{S^2_{1/2}}$. With $\operatorname{Vol}(S^2_{1/2})=(\tfrac12)^2\cdot4\pi=\pi$,
> $$\int_{\mathbb{CP}^1}F_a=2i\operatorname{Vol}\!\big(S^2_{1/2}\big)=2\pi i,\qquad \frac{i}{2\pi}\int_{\mathbb{CP}^1}F_a=i^2=-1,$$
> which is part (a) of the first-Chern-class theorem. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to argue "$F_a=2\,\mathrm{vol}$ on any orthonormal frame, so $\int F_a=2\operatorname{Vol}$" *before* verifying that $(\pi_*v_2,\pi_*v_3)$ is an orthonormal frame **of the base metric that one is integrating against**. The value $F_a(\pi_*v_2,\pi_*v_3)=2i$ alone does not give $F_a=2i\,\mathrm{vol}$: it does so only once the metric making $(\pi_*v_2,\pi_*v_3)$ orthonormal has been identified with the metric whose volume form is $\mathrm{vol}$. That identification is the entire content of Steps 1–4; skipping it hides the fact that $\int F_a$ depends on the area of the base, which is why the radius $\tfrac12$ (not $1$) matters — a radius-$1$ sphere would give area $4\pi$ and the wrong answer $\tfrac{i}{2\pi}\cdot8\pi i=-4$.

> [!note]- Independent sanity check
> The direct integral confirms the area route. In the affine coordinate $\zeta=z_1/z_0$ on the chart $\{z_0\ne0\}$, the induced curvature on $\mathcal{O}(-1)$ is $F_a=\dfrac{2i}{(1+|\zeta|^2)^2}\,d\xi\wedge d\eta$ ($\zeta=\xi+i\eta$), so with the complex orientation
> $$\frac{i}{2\pi}\int F_a=\frac{i}{2\pi}\int_{\mathbb{R}^2}\frac{2i}{(1+r^2)^2}\,d\xi\,d\eta=\frac{-2}{2\pi}\cdot2\pi\int_0^\infty\frac{r\,dr}{(1+r^2)^2}=-2\cdot\tfrac12=-1,$$
> the excluded point $[0:1]$ having measure zero and the improper integral converging. This direct integration of the curvature density is a third route to the same integer, distinct both from the area computation carried out here and from the two-disc winding-number argument of [[Ex - The Chern Number of the Hopf Line Bundle over CP^1 is Minus One|the Stokes-route companion]] (which never integrates the density but localises the integral onto the equator); all three agree on $-1$.

---

# Key Takeaways

**When a $2$-form on a surface is known only through its value on one frame, an integral becomes an area — provided the frame is orthonormal for the metric you integrate against.** The chapter-IV exercise handed over the curvature as a single pointwise number, $F_a(\pi_*v_2,\pi_*v_3)=2i$, constant across the base. That number is not yet the integrand of a total curvature until it is paired with a volume form, and a volume form needs a metric and an orientation. The decisive step here was recognising that the pointwise datum plus a *metric identification* determines the whole integral: $F_a=2i\,\mathrm{vol}$ and $\int=2i\cdot\operatorname{area}$. The general principle, worth carrying into every characteristic-number computation on a surface, is that a top-degree form is completely pinned by its value on one oriented orthonormal frame, so the outstanding work is always to find the metric — and the radius, which fixes the area — not to integrate a complicated density. The recurring trap, made explicit in the warning callout, is to forget that the answer scales with the base area: the same curvature density over a sphere of a different radius gives a different integral, and only the geometrically correct radius $\tfrac12$ produces the topologically correct $-1$.

**A quotient by an isometric group action carries a forced metric, and any explicit orthonormal-on-horizontal map to a model space is automatically an isometry.** The trigger to reach for a Riemannian submersion is the phrase "quotient by a group acting by isometries": the quotient metric is then not a choice but a consequence, defined by declaring the horizontal part of the upstairs metric to descend. This turns the isometry problem into a purely linear-algebraic check on one frame — does the differential send a horizontal orthonormal basis to an orthonormal basis of the target? — which is far cheaper than comparing metric tensors coordinate by coordinate. The transferable diagnostic: to prove that a homogeneous or quotient space is a familiar model (here, that $\mathbb{CP}^1$ is a round $2$-sphere), do not chase Christoffel symbols; exhibit a concrete map to the model and verify orthonormality on the natural frame, letting the isometric action supply the rest. The same manoeuvre identifies $\mathbb{HP}^1$ with $S^4$, and Berger spheres with squashed $S^3$'s, from their defining submersions.

**Complex bookkeeping linearises real quadratic identities; the modulus constraint $|z_0|^2+|z_1|^2=1$ does the rest.** The orthonormality of $d\Phi(v_2),d\Phi(v_3)$, written in the four real coordinates $x_0,\dots,x_3$, is three unpleasant quartic identities in eight terms each. Rewriting the horizontal fields as $(-\bar z_1,\bar z_0)$ and its $i$-multiple, and $\Phi$ in terms of $z_0\bar z_1$ and $|z_0|^2-|z_1|^2$, collapses each identity to an application of $4\operatorname{Re}(W)^2=2|W|^2+2\operatorname{Re}(W^2)$ (and its $\operatorname{Im}$-analogue) followed by $(|z_0|^2+|z_1|^2)^2=1$. The reusable heuristic: when a computation on $S^{2n+1}\subset\mathbb{C}^{n+1}$ or on $\mathbb{CP}^n$ produces symmetric real polynomials, convert to Hermitian quantities ($z\bar z$, $z^2$, $\operatorname{Re}$, $\operatorname{Im}$) before expanding — the single normalisation $\sum|z_j|^2=1$ then absorbs almost every cross term, and the vertical direction $iz$ drops out for free because $\Phi$ is built from $U(1)$-invariants. This is the same reason the Hopf map has such clean formulas: it is assembled entirely from the invariants $z_0\bar z_1$ and $|z_0|^2-|z_1|^2$, and every derivative respects that invariance.

**Two independent routes to the same Chern number are a proof that the sign and normalisation are self-consistent.** This exercise and [[Ex - The Chern Number of the Hopf Line Bundle over CP^1 is Minus One|its Stokes-route companion]] compute the same integer by disjoint machinery — one through the area of a model sphere, the other through the winding number of a transition function via Stokes. Their agreement is not redundancy: it is what fixes the orientation convention and confirms that $c_1(L)=[\tfrac{i}{2\pi}F]$ with the complex orientation of $\mathbb{CP}^1$ yields $-1$ rather than $+1$. Whenever a normalisation-sensitive invariant can be computed two ways, doing so is the cheapest available guard against a dropped $i$ or a reversed orientation; the habit pays off acutely in gauge theory, where the sign of $c_1$, of $c_2$, and of the Chern–Simons variation must all be mutually consistent (see the sign ledger on [[Def - The Hopf Bundle|the Hopf-bundle page]]).
