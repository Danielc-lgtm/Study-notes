---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - The Brouwer Degree is an Integer and a Homotopy Invariant"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Thm - Pull-Back Commutes with the Exterior Derivative"
  - "Def - Brouwer Degree of a Map"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $S^1=\{e^{it}:t\in\mathbb R\}$ is the circle, regarded as a closed, oriented, connected one-dimensional manifold; we orient it so that the coordinate $t$ increases in the positive direction (counter-clockwise), which is the same as declaring the angular form $d\theta$ below to be positive. The **circle group** is
$$U(1)=\{z\in\mathbb C:|z|=1\},$$
a compact abelian Lie group under multiplication of complex numbers, with identity $1$ and inverse $z^{-1}=\bar z$; it is diffeomorphic to $S^1$, and we give it the same orientation. We write $z$ for the standard complex coordinate of $\mathbb C$ restricted to $U(1)$, so that on $U(1)$ we have $z\bar z=|z|^2=1$.

The map $p\colon\mathbb R\to U(1)$, $p(t)=e^{it}$, is the universal covering homomorphism; it is a surjective local diffeomorphism and a group homomorphism, $p(t+s)=p(t)p(s)$.

The **angular form** $d\theta\in\Omega^1(U(1))$ is the unique smooth $1$-form with $p^*d\theta=dt$; it is established in Lemma 1 that
$$d\theta=\frac1i\,\bar z\,dz=-i\,\bar z\,dz\in\Omega^1(U(1)),\qquad \int_{U(1)}d\theta=2\pi .$$
There is no globally defined smooth angle function $\theta\colon U(1)\to\mathbb R$ (that is exactly what winding numbers measure), so the symbol $d\theta$ denotes this closed but non-exact $1$-form as a single object, not the differential of a function on $U(1)$.

For a smooth map $g\colon S^1\to U(1)$ we regard $g$ as a $\mathbb C$-valued function with $|g|\equiv1$; then $dg$ is its $\mathbb C$-valued differential (a $\mathbb C$-valued $1$-form on $S^1$), and since $g^{-1}=\bar g$ pointwise we write
$$g^{-1}dg=\bar g\,dg\in\Omega^1(S^1;i\mathbb R),$$
the pullback along $g$ of the Maurer–Cartan form of $U(1)$; it takes values in the imaginary axis $i\mathbb R=\operatorname{Lie}(U(1))$ because differentiating $g\bar g=1$ gives $\bar g\,dg+g\,d\bar g=0$, that is $\overline{\bar g\,dg}=-\bar g\,dg$. The **winding number** of $g$ is
$$w(g):=\frac1{2\pi}\int_{S^1}g^*d\theta=\frac1{2\pi i}\int_{S^1}g^{-1}dg,$$
the two expressions being equal because $g^*d\theta=g^*\!\left(\tfrac1i\bar z\,dz\right)=\tfrac1i\,\bar g\,dg=\tfrac1i\,g^{-1}dg$ (Lemma 1).

The **pointwise product** of two maps $g_1,g_2\colon S^1\to U(1)$ is $(g_1g_2)(x)=g_1(x)g_2(x)$, again a smooth map $S^1\to U(1)$; the **pointwise inverse** is $g^{-1}(x)=g(x)^{-1}=\overline{g(x)}$. These make $C^\infty(S^1,U(1))$ an abelian group with identity the constant map $\mathbf 1(x)\equiv1$. The closed unit disc is $D^2=\{z\in\mathbb C:|z|\le1\}$, a compact oriented $2$-manifold with boundary $\partial D^2=S^1$ carrying the induced (Stokes) boundary orientation. The degree of a smooth map between closed oriented equidimensional manifolds is denoted $\deg$; its meaning is fixed by [[Def - Brouwer Degree of a Map|the Brouwer degree]].

> [!warning] Convention: two sign conventions for the angular form, and two equivalent definitions of the winding number
> Some authors use $d\theta=+i\,z\,d\bar z$; on $U(1)$ this equals $-i\,\bar z\,dz$ because $\bar z\,dz+z\,d\bar z=0$, so the two agree, and both give $\int_{U(1)}d\theta=+2\pi$ with our orientation. The reversed orientation of $U(1)$ would flip the sign of every winding number; we fix the orientation once, by $\int_{U(1)}d\theta=+2\pi$. The literature also defines the winding number in two superficially different ways: analytically, by the integral $w(g)$ above, and topologically, as the net number of times $g$ circles the target, made precise by the monodromy of a lift (Lemma 3) or as the image of the homotopy class under $\pi_1(U(1))\cong\mathbb Z$ ([[Thm - Pi_1 of S^1 is Z]]). Part (a) of the theorem is precisely the statement that these definitions coincide with each other and with the Brouwer degree.

---

# Statement

> **Theorem (winding number of a map from the circle to $U(1)$).** For a smooth map $g\colon S^1\to U(1)$ define
> $$w(g)=\frac1{2\pi}\int_{S^1}g^*d\theta=\frac1{2\pi i}\int_{S^1}g^{-1}dg .$$
> Then:
> - **(a) Integrality and identification with the degree.** $w(g)\in\mathbb Z$, and $w(g)=\deg g$, the Brouwer degree of $g$ regarded as a map $S^1\to U(1)$ of closed oriented $1$-manifolds.
> - **(b) Homomorphism property.** For the pointwise product and pointwise inverse,
> $$w(g_1g_2)=w(g_1)+w(g_2),\qquad w(g^{-1})=-w(g),$$
> so $w\colon C^\infty(S^1,U(1))\to\mathbb Z$ is a group homomorphism.
> - **(c) Homotopy invariance.** If $g_0$ and $g_1$ are smoothly homotopic as maps $S^1\to U(1)$, then $w(g_0)=w(g_1)$.
> - **(d) The three characterisations of winding number zero.** The following are equivalent:
>   1. $w(g)=0$;
>   2. $g=e^{iu}$ for some smooth function $u\colon S^1\to\mathbb R$ (that is, $g$ admits a global smooth logarithm);
>   3. $g$ extends to a smooth map $G\colon D^2\to U(1)$ with $G|_{\partial D^2}=g$.
> - **(e) The power maps.** For each $k\in\mathbb Z$, the map $g_k\colon S^1\to U(1)$, $g_k(z)=z^k$, has $w(g_k)=k$.

---

# Motivation

A map $g\colon S^1\to U(1)$ is a loop in the circle group, and the single question one asks of such a loop is: how many times, net of direction, does it wind around the target? The winding number is the answer, and it is the first and simplest characteristic number in the whole of gauge theory. Every deeper invariant in this series — the degree of a line bundle over a surface, the first Chern number, the instanton number of an $SU(2)$-bundle, the gauge variation of the Chern–Simons functional — is, at the decisive step, a winding number of a transition function or of a gauge transformation restricted to a boundary sphere. Getting the one-dimensional case completely right, with every sign and every equivalence proved, is therefore not a warm-up but the foundation on which those computations rest.

There are three ways one naturally wants to *think about* winding number, and the content of the theorem is that they are the same. The **analytic** way is to integrate the pullback of the angular form: $\frac1{2\pi}\int_{S^1}g^*d\theta$. This is a real number, computable by an integral, and it is not obvious from the definition that it is an integer at all. The **counting** way is to pick a generic point $y\in U(1)$ and count the preimages $g^{-1}(y)$ with signs according to whether $g$ is locally orientation-preserving or -reversing there; this is manifestly an integer but requires choosing $y$ and knowing the count is independent of the choice. The **topological** way is to lift $g$ through the covering $p\colon\mathbb R\to U(1)$ to a path $\psi$ in $\mathbb R$ and read off how far it has travelled, $\psi(2\pi)-\psi(0)$, in units of $2\pi$; this is the definition that matches $\pi_1(U(1))\cong\mathbb Z$. The theorem welds the analytic definition to the counting one through the Brouwer degree (part (a)) and to the topological one through the lifting lemma (part (d) and its proof), so that one may compute whichever way is convenient and know the answer is the same.

The reason $U(1)$ deserves its own page, rather than being subsumed into the general degree theory, is its abelian group structure. Because $U(1)$ is a group, maps into it can be multiplied pointwise, and because it is *abelian*, the angular form is bi-invariant and pulls back additively under products. This turns the winding number into a group homomorphism (part (b)), which is exactly the property that later lets us say "the Chern number of a tensor product of line bundles is the sum of the Chern numbers" and "the winding number is unchanged when a clutching function is modified by boundary values of maps that extend over a disc". No such additivity is available for a general degree; it is a gift of the group structure, and part (b) is where we collect it.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is only that $g\colon S^1\to U(1)$ is smooth, so the question is: when does a problem hand you such a map without naming one?

The first disguised source is **a nowhere-vanishing complex-valued function on the circle**, or on any space carrying a distinguished loop. If $h\colon S^1\to\mathbb C\setminus\{0\}$ is smooth and nowhere zero, then $g:=h/|h|\colon S^1\to U(1)$ is smooth, and its winding number counts how many times $h$ encircles the origin. The bridge $B\Rightarrow A$ is the normalisation $h\mapsto h/|h|$, which is a smooth deformation retraction of $\mathbb C\setminus\{0\}$ onto $U(1)$ and hence does not change the homotopy class; by part (c) the winding number of $h/|h|$ is the classical winding number of $h$ about $0$. *Example problem:* show that a polynomial $p(z)$ of degree $n$ with no roots on the unit circle has $\frac1{2\pi i}\oint_{|z|=1}p'/p\,dz$ equal to the number of roots inside the disc, by recognising the integrand as $g^{-1}dg$ for $g=p/|p|$ restricted to the circle and using the argument principle together with part (a).

The second disguised source is **a transition function or clutching function of a $U(1)$-bundle over a surface, restricted to an equator or to the boundary of a coordinate disc**. A Hermitian line bundle over a closed surface is trivial off a disc, and the two trivialisations differ on the boundary circle by a smooth map $g\colon S^1\to U(1)$; this $g$ is not given as a loop in $U(1)$ but is manufactured from bundle data. The non-obvious step is that the isomorphism class of the bundle depends on $g$ only through $w(g)$, which is exactly what part (b) and part (d) deliver. *Example problem:* prove that the Hopf bundle over $S^2$ is nontrivial by exhibiting its clutching function $z\mapsto z/|z|$ on the equator and computing that its winding number is $1\ne0$ (done on [[Ex - The Hopf Bundle is Nontrivial via the Winding Number of its Transition Function|the Hopf-nontriviality exercise]]).

The third disguised source is **the holonomy of a flat connection on a line bundle over the circle, or a monodromy datum**. Parallel transport around $S^1$ for a $U(1)$-connection is an element of $U(1)$, and as the connection varies the holonomy traces a loop in $U(1)$; more directly, a gauge transformation of a $U(1)$-bundle over $S^1$ is precisely a map $S^1\to U(1)$, and its winding number is the topological quantity distinguishing gauge transformations that are, and are not, connected to the identity. The bridge is that "a based loop in $U(1)$" and "a map $S^1\to U(1)$" are the same object once a basepoint is chosen. *Example problem:* classify, up to homotopy, the gauge transformations of the trivial $U(1)$-bundle over $S^1$, showing that $w$ is a complete invariant (this is part (c) together with the surjectivity of $w$ from part (e)).

**Targets (Output Amplification)**

The bare conclusion is a homomorphism $w\colon C^\infty(S^1,U(1))\to\mathbb Z$ that computes the degree. Combined with other ingredients it does much more.

Combine $w$ with **the clutching construction and the degree theorem's bounding clause**. If $g$ and $g'$ are clutching functions of the same $U(1)$-bundle over a closed surface, they differ by $g'=(a|_{S^1})\,g\,(b|_{S^1})$ where $a$ and $b$ are defined on the two pieces of the surface, hence extend over discs; by part (d) the boundary values $a|_{S^1}$ and $b|_{S^1}$ have winding number zero, and by the homomorphism property (part (b)) $w(g')=w(g)$. The payoff is that the winding number of a clutching function is a bundle invariant — the **degree** of a line bundle over a surface — used throughout [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class|the $U(1)$-classification theorem]].

Combine $w$ with **Chern–Weil theory**. In chapter VI the first Chern number of a line bundle over a surface is computed as $\frac{i}{2\pi}\int_\Sigma F$, and matching it to the topological degree $w(g)$ of the clutching function requires exactly the identity $w(g)=\frac1{2\pi i}\int_{S^1}g^{-1}dg$ proved here, applied on the overlap where the two local connection forms differ by $g^{-1}dg$. The extra ingredient is Stokes' theorem on the two pieces; the payoff is the equality of the analytic and topological first Chern numbers.

Combine $w$ with **the additivity of the three-dimensional analogue**. The identity $w(g_1g_2)=w(g_1)+w(g_2)$ has a direct sibling for maps $S^3\to SU(2)$, where the invariant is $\frac1{24\pi^2}\int_{S^3}\operatorname{tr}((g^{-1}dg)^{\wedge3})$; the proof that this is additive under pointwise products, and equals the degree, is modelled line for line on the proof of part (b) here, with the abelian cancellation replaced by a Stokes term. The payoff is the additivity of the instanton number under the group structure of gauge transformations, the engine of [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds|the $SU(2)$-classification theorem]].

---

# Why Is It True

Picture $g\colon S^1\to U(1)$ as a moving point on the target circle, traced out as the source point runs once around $S^1$. At each instant the point has an angular velocity, and the angular form $d\theta$ is precisely the instrument that reads off that velocity: $g^*d\theta$ is the $1$-form on the source whose integral over any arc is the net angle swept out on the target over that arc. Integrating over the whole source circle therefore gives the total angle swept, and dividing by $2\pi$ converts total angle into a number of full turns. That is the entire meaning of $w(g)$.

Why must the total number of turns be an integer? Because the moving point starts and ends at the same place. If we lift the motion to the real line — tracking not the point on the target circle but a real-valued angle $\psi(t)$ that increases continuously — then $\psi$ is free to run off to any real value, but the constraint that $g$ returns to its start forces $\psi(2\pi)-\psi(0)$ to be a whole number of $2\pi$'s, since two real angles give the same point on $U(1)$ exactly when they differ by a multiple of $2\pi$. The total swept angle is $\psi(2\pi)-\psi(0)$, so $w(g)$ is an integer. This is the same integer the Brouwer degree produces by counting signed preimages of a generic point, because sweeping through a generic angle $k$ full times means passing that angle exactly $k$ times, each time in the positive direction.

**The single mechanism: the winding number is the total angle the target point sweeps, measured in full turns, and it is an integer because the loop closes up.** The homomorphism property is then transparent: if two points move on the target circle with angular velocities that add — which is exactly what happens under pointwise multiplication, because the group $U(1)$ adds angles — then the total swept angles add, so the winding numbers add. The abelian-ness of $U(1)$ is what makes "the angular velocity of a product is the sum of the angular velocities" an exact identity of $1$-forms rather than a statement holding only up to a correction. Finally, a loop with total swept angle zero can be continuously unwound back to a constant, either by writing down a genuine real-valued angle function (a smooth logarithm $u$ with $g=e^{iu}$) or by filling in the disc; a loop with nonzero winding cannot, because the winding number is a homotopy invariant that the constant map does not share.

---

# What Makes This Hard

The subtle point is not any single computation but the coordination of three definitions that look different: the integral $\frac1{2\pi}\int g^*d\theta$, the signed preimage count, and the monodromy of a lift. Part (a) rests on recognising $\frac1{2\pi}d\theta$ as a *normalised volume form* on $U(1)$, so that the integral is literally the Brouwer degree; the common error is to try to prove integrality directly from the integral, without invoking the degree theorem, and to get lost. A second trap is in the additivity of part (b): the identity $(g_1g_2)^*d\theta=g_1^*d\theta+g_2^*d\theta$ is *exact*, with no leftover $d(\text{something})$ term, and this is true only because $U(1)$ is abelian — for a non-abelian group the corresponding pullback identity carries a correction, and forgetting this is the mistake that would break every downstream additivity claim. The third difficulty is the disc-extension direction of part (d): one must produce an *honestly smooth* map on the whole disc, including the origin, from boundary data, which is why the construction multiplies the angle function by a radial cutoff that is constant near the centre.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Establish the angular form and its normalisation (Lemma 1), then read (a) straight off the degree theorem with $\omega=\frac1{2\pi}d\theta$. Get (b) from the exact additivity of the angular form under products (Lemma 2). Get (c) from the degree theorem's homotopy invariance via (a). For (d), lift $g$ to the real line (Lemma 3) and run a cycle of three implications, using a radial-cutoff extension in one step and Stokes in another (Lemma 4). Get (e) by a one-line computation, cross-checked by (b).

**Subgoal decomposition:**

1. **The angular form is a normalised volume form.** Construct $d\theta$ with $p^*d\theta=dt$, show $d\theta=\frac1i\bar z\,dz$, and compute $\int_{U(1)}d\theta=2\pi$.
   - *Hint:* Differentiate $z\bar z=1$ to see $\frac1i\bar z\,dz$ is real; pull back along $p(t)=e^{it}$ to get $dt$; integrate over one period.
   - *Why needed:* Without $\int_{U(1)}\frac1{2\pi}d\theta=1$ the degree theorem does not apply and (a) is false.

2. **Pullback of the angular form is additive under products.** Show $m^*d\theta=\operatorname{pr}_1^*d\theta+\operatorname{pr}_2^*d\theta$ for the multiplication $m\colon U(1)\times U(1)\to U(1)$, hence $(g_1g_2)^*d\theta=g_1^*d\theta+g_2^*d\theta$.
   - *Hint:* $m^*(\bar\zeta\,d\zeta)=\bar z\bar w\,d(zw)=\bar z\,dz+\bar w\,dw$ using $|z|=|w|=1$.
   - *Why needed:* This is the exact identity behind the homomorphism property (b); its exactness uses abelian-ness.

3. **Every $g$ has a smooth real lift, whose monodromy is $2\pi w(g)$.** Produce $\psi\colon\mathbb R\to\mathbb R$ with $g(e^{it})=e^{i\psi(t)}$ and $\psi(t+2\pi)-\psi(t)=2\pi w(g)\in2\pi\mathbb Z$.
   - *Hint:* Set $\psi'=\frac1i\bar g\,g'$ and check $\frac{d}{dt}(g e^{-i\psi})=0$.
   - *Why needed:* It converts $w(g)=0$ into "$\psi$ is periodic", giving the smooth logarithm in (d); it also reproves integrality topologically.

4. **Stokes vanishing.** Show $\int_{S^1}du=0$ for smooth $u\colon S^1\to\mathbb R$, and $\int_{S^1}(G|_{S^1})^*d\theta=0$ for smooth $G\colon D^2\to U(1)$.
   - *Hint:* $S^1$ is a closed manifold; $d\theta$ is closed and pullback commutes with $d$; apply Stokes on $S^1$ and on $D^2$.
   - *Why needed:* It closes the equivalence cycle in (d) — the disc-extension forces winding number zero.

5. **Assemble (a)–(e).** Feed Lemma 1 into the degree theorem for (a); Lemma 2 for (b); (a) plus the degree theorem for (c); Lemmas 3 and 4 for the cycle in (d); a direct computation for (e).
   - *Hint:* For (d) prove $1\Rightarrow2\Rightarrow3\Rightarrow1$; each arrow is one lemma or one construction.
   - *Why needed:* The parts are independent claims that must each be discharged.

---

# Lemma Decomposition

> [!note]- Lemma 1: The angular form is a normalised volume form on $U(1)$
> **Statement:** There is a unique $1$-form $d\theta\in\Omega^1(U(1))$ with $p^*d\theta=dt$, where $p\colon\mathbb R\to U(1)$, $p(t)=e^{it}$. It equals $d\theta=\frac1i\bar z\,dz=-i\,\bar z\,dz$, is real-valued and left- and right-invariant, and satisfies $\int_{U(1)}d\theta=2\pi$. Consequently $\omega_0:=\frac1{2\pi}d\theta$ is a smooth $1$-form on $U(1)$ with $\int_{U(1)}\omega_0=1$, and for every smooth $g\colon S^1\to U(1)$ one has $g^*d\theta=\frac1i g^{-1}dg$.
>
> **Hint:** Differentiate the defining relation $z\bar z=1$; pull back along $p$; integrate over one period.
>
> **Why needed:** Part (a) applies the degree theorem with $\omega=\omega_0$, which requires $\int_{U(1)}\omega_0=1$; the closed-form expression is what lets every later page compute with $g^{-1}dg$.
>
> > [!note]- Full proof
> > **Step 1 — the candidate form is real.** On $U(1)$ the coordinate satisfies $z\bar z=|z|^2=1$. Taking the exterior derivative (the exterior derivative of the constant function $1$ is zero, and by the Leibniz rule $d(z\bar z)=\bar z\,dz+z\,d\bar z$),
> > $$\bar z\,dz+z\,d\bar z=0,\qquad\text{hence}\qquad z\,d\bar z=-\bar z\,dz\quad\text{on }U(1). \tag{1}$$
> > Set $\alpha:=\frac1i\bar z\,dz$. Its complex conjugate is
> > $$\bar\alpha=\overline{\tfrac1i\bar z\,dz}=-\tfrac1i\,z\,d\bar z=-\tfrac1i(-\bar z\,dz)=\tfrac1i\bar z\,dz=\alpha \qquad(\text{by }(1)),$$
> > so $\alpha$ is a real-valued $1$-form on $U(1)$.
> >
> > **Step 2 — the pullback along $p$ is $dt$.** Compose with $p(t)=e^{it}$: then $z\circ p=e^{it}$, so $p^*dz=d(e^{it})=ie^{it}\,dt$, and $\bar z\circ p=e^{-it}$. Therefore
> > $$p^*\alpha=\tfrac1i\,(e^{-it})(ie^{it}\,dt)=\tfrac1i\cdot i\,dt=dt \qquad(\text{since }e^{-it}e^{it}=1).$$
> > Define $d\theta:=\alpha=\frac1i\bar z\,dz$; then $p^*d\theta=dt$, as required.
> >
> > **Step 3 — uniqueness.** The map $p$ is a surjective local diffeomorphism, so its differential is everywhere an isomorphism, and $p^*\colon\Omega^1(U(1))\to\Omega^1(\mathbb R)$ is injective: if $p^*\beta=0$ then $\beta_{p(t)}\circ d_tp=0$ for all $t$, and since $d_tp$ is an isomorphism onto $T_{p(t)}U(1)$ and $p$ is surjective, $\beta=0$. Hence a form with prescribed pullback $dt$ is unique.
> >
> > **Step 4 — invariance.** For $a\in U(1)$ let $L_a(z)=az$ be left translation. Then $z\circ L_a=az$ and $\bar z\circ L_a=\bar a\bar z$, so
> > $$L_a^*d\theta=\tfrac1i(\bar a\bar z)\,d(az)=\tfrac1i\,\bar a\bar z\,a\,dz=\tfrac1i\,|a|^2\,\bar z\,dz=\tfrac1i\bar z\,dz=d\theta \qquad(\text{since }|a|^2=1).$$
> > Because $U(1)$ is abelian, right translation equals left translation, so $d\theta$ is bi-invariant. In particular $d\theta$ is nowhere zero (its pullback $dt$ is nowhere zero and $p$ is a local diffeomorphism), hence a volume form on the oriented $1$-manifold $U(1)$; with our orientation it is positive.
> >
> > **Step 5 — the integral.** The restriction $p|_{[0,2\pi)}\colon[0,2\pi)\to U(1)$ is an orientation-preserving diffeomorphism onto $U(1)$ minus one point (a set of measure zero, which does not affect the integral). By the definition of integration of a top form and the change-of-variables/pullback formula,
> > $$\int_{U(1)}d\theta=\int_{[0,2\pi]}p^*d\theta=\int_0^{2\pi}dt=2\pi.$$
> > Hence $\omega_0=\frac1{2\pi}d\theta$ has $\int_{U(1)}\omega_0=1$.
> >
> > **Step 6 — the expression $g^*d\theta=\frac1i g^{-1}dg$.** For smooth $g\colon S^1\to U(1)$, pullback is natural in the coordinate: $g^*z=g$ and $g^*\bar z=\bar g=g^{-1}$ (as $|g|=1$), and $g^*dz=dg$. Therefore
> > $$g^*d\theta=g^*\!\left(\tfrac1i\bar z\,dz\right)=\tfrac1i\,\bar g\,dg=\tfrac1i\,g^{-1}dg,$$
> > and multiplying by $\frac1{2\pi}$ gives the two stated forms of $w(g)$. This is a smooth real $1$-form on $S^1$ because $g^{-1}dg$ is imaginary-valued (differentiate $g\bar g=1$: $\bar g\,dg+g\,d\bar g=0$, so $\overline{\bar g\,dg}=-\bar g\,dg$). $\blacksquare$

> [!note]- Lemma 2: The angular form pulls back additively under multiplication
> **Statement:** Let $m\colon U(1)\times U(1)\to U(1)$, $m(z,w)=zw$, be the multiplication, and $\operatorname{pr}_1,\operatorname{pr}_2\colon U(1)\times U(1)\to U(1)$ the two projections. Then
> $$m^*d\theta=\operatorname{pr}_1^*d\theta+\operatorname{pr}_2^*d\theta .$$
> Consequently, for smooth $g_1,g_2\colon S^1\to U(1)$ with pointwise product $g_1g_2$,
> $$(g_1g_2)^*d\theta=g_1^*d\theta+g_2^*d\theta .$$
>
> **Hint:** Compute $m^*(\bar\zeta\,d\zeta)$ directly, using $|z|=|w|=1$; then use functoriality $(m\circ(g_1,g_2))^*=(g_1,g_2)^*m^*$.
>
> **Why needed:** This exact identity is the whole of the homomorphism property (b); its exactness (no correction term) is where abelian-ness of $U(1)$ enters.
>
> > [!note]- Full proof
> > **Step 1 — the identity on $U(1)\times U(1)$.** Write $z,w$ for the two complex coordinates on $U(1)\times U(1)$ (the pullbacks of the single coordinate along $\operatorname{pr}_1,\operatorname{pr}_2$), and $\zeta$ for the coordinate on the target. Then $\zeta\circ m=zw$ and $\bar\zeta\circ m=\bar z\bar w$, and by the Leibniz rule $m^*d\zeta=d(zw)=w\,dz+z\,dw$. Using the expression $d\theta=\frac1i\bar\zeta\,d\zeta$ from Lemma 1,
> > $$m^*d\theta=\tfrac1i\,(\bar z\bar w)\,(w\,dz+z\,dw)=\tfrac1i\big(\bar z\,(\bar w w)\,dz+(\bar z z)\,\bar w\,dw\big)=\tfrac1i\big(\bar z\,dz+\bar w\,dw\big),$$
> > where we used $\bar w w=|w|^2=1$ and $\bar z z=|z|^2=1$ on $U(1)\times U(1)$. The right-hand side is $\frac1i\bar z\,dz+\frac1i\bar w\,dw=\operatorname{pr}_1^*d\theta+\operatorname{pr}_2^*d\theta$, since $\frac1i\bar z\,dz$ is the pullback of $d\theta$ along $\operatorname{pr}_1$ and likewise for $w$. (This step used $U(1)$'s abelian-ness only implicitly, in that no ordering of $z$ and $w$ matters; for a non-abelian matrix group the parallel computation of $(zw)^{-1}d(zw)=w^{-1}(z^{-1}dz)w+w^{-1}dw$ carries the conjugation $w^{-1}(\cdot)w$, which does not simplify.)
> >
> > **Step 2 — descent to maps from $S^1$.** Let $(g_1,g_2)\colon S^1\to U(1)\times U(1)$, $x\mapsto(g_1(x),g_2(x))$, so that the pointwise product is the composite $g_1g_2=m\circ(g_1,g_2)$. Pullback is contravariantly functorial, $(m\circ(g_1,g_2))^*=(g_1,g_2)^*\circ m^*$, and $\operatorname{pr}_j\circ(g_1,g_2)=g_j$ gives $(g_1,g_2)^*\operatorname{pr}_j^*=g_j^*$. Therefore
> > $$(g_1g_2)^*d\theta=(g_1,g_2)^*m^*d\theta=(g_1,g_2)^*\big(\operatorname{pr}_1^*d\theta+\operatorname{pr}_2^*d\theta\big)=g_1^*d\theta+g_2^*d\theta,$$
> > using in the last step that $(g_1,g_2)^*$ is linear. This is the claimed identity. $\blacksquare$

> [!note]- Lemma 3: Every smooth map $S^1\to U(1)$ has a smooth real lift with integer monodromy
> **Statement:** For every smooth $g\colon S^1\to U(1)$, regarded as a smooth $2\pi$-periodic map $g\colon\mathbb R\to U(1)$ via $t\mapsto g(e^{it})$, there is a smooth function $\psi\colon\mathbb R\to\mathbb R$ with
> $$g(e^{it})=e^{i\psi(t)}\qquad(t\in\mathbb R),$$
> unique up to adding a constant in $2\pi\mathbb Z$, and
> $$\psi(t+2\pi)-\psi(t)=\int_{S^1}g^*d\theta=2\pi\,w(g)\in2\pi\mathbb Z\qquad\text{for all }t .$$
> In particular $w(g)\in\mathbb Z$, computed independently of the degree theorem.
>
> **Hint:** Define $\psi$ by integrating $\frac1i\bar g\,g'$; check $g e^{-i\psi}$ has zero derivative; use that $g$ is $2\pi$-periodic to force the monodromy into $2\pi\mathbb Z$.
>
> **Why needed:** It turns "$w(g)=0$" into "the lift is periodic", producing the smooth logarithm in part (d); it also gives the topological proof of integrality matching $\pi_1(U(1))\cong\mathbb Z$.
>
> > [!note]- Full proof
> > **Step 1 — a smooth antiderivative of the angular density.** Since $g\colon\mathbb R\to U(1)\subset\mathbb C$ is smooth with $|g|\equiv1$, the function $\beta(t):=\frac1i\,\overline{g(t)}\,g'(t)$ is smooth and real-valued: differentiating $g\bar g=1$ gives $\bar g g'+g\bar g'=0$, so $\overline{\bar g g'}=g\bar g'=-\bar g g'$, i.e. $\bar g g'\in i\mathbb R$ and $\beta=\frac1i\bar g g'\in\mathbb R$. By construction $g^*d\theta=\frac1i g^{-1}dg=\beta(t)\,dt$ (Lemma 1). Define
> > $$\phi(t):=\int_0^t\beta(\tau)\,d\tau,$$
> > a smooth function with $\phi(0)=0$ and $\phi'=\beta$ (fundamental theorem of calculus, $\beta$ continuous).
> >
> > **Step 2 — the lift.** Choose $c\in\mathbb R$ with $g(0)=e^{ic}$ (possible since $g(0)\in U(1)$), and set $\psi(t):=c+\phi(t)$, smooth. We claim $g(t)=e^{i\psi(t)}$. Consider $F(t):=g(t)e^{-i\psi(t)}$; then
> > $$F'(t)=g'(t)e^{-i\psi}-i\psi'(t)\,g(t)e^{-i\psi}=e^{-i\psi}\big(g'-i\psi'g\big).$$
> > Now $i\psi'g=i\beta g=i\cdot\tfrac1i\bar g g'\cdot g=(\bar g g)\,g'=g'$ (since $\bar g g=|g|^2=1$), so $g'-i\psi'g=0$ and $F'\equiv0$. Hence $F(t)=F(0)=g(0)e^{-ic}=e^{ic}e^{-ic}=1$, giving $g(t)=e^{i\psi(t)}$.
> >
> > **Step 3 — the monodromy is $2\pi w(g)$.** The map $g$ is $2\pi$-periodic, $g(t+2\pi)=g(t)$, so $e^{i\psi(t+2\pi)}=e^{i\psi(t)}$ for all $t$, which means $\psi(t+2\pi)-\psi(t)\in2\pi\mathbb Z$. The left-hand side is a continuous function of $t$ taking values in the discrete set $2\pi\mathbb Z$, hence is a constant $2\pi n$ with $n\in\mathbb Z$. Evaluating with $\psi(t)=c+\phi(t)$,
> > $$2\pi n=\psi(2\pi)-\psi(0)=\phi(2\pi)-\phi(0)=\int_0^{2\pi}\beta(\tau)\,d\tau=\int_{S^1}g^*d\theta=2\pi\,w(g),$$
> > where the fourth equality is the definition of $\int_{S^1}$ via the parametrisation $t\mapsto e^{it}$ (Lemma 1, Step 5). Therefore $w(g)=n\in\mathbb Z$.
> >
> > **Step 4 — uniqueness up to $2\pi\mathbb Z$.** If $\psi,\tilde\psi$ are two smooth lifts, then $e^{i(\psi-\tilde\psi)}\equiv1$, so $\psi-\tilde\psi$ is a continuous $2\pi\mathbb Z$-valued function on $\mathbb R$, hence a constant in $2\pi\mathbb Z$. $\blacksquare$

> [!note]- Lemma 4: Stokes vanishing on the circle and over the disc
> **Statement:** (i) For every smooth $u\colon S^1\to\mathbb R$, $\int_{S^1}du=0$. (ii) If $G\colon D^2\to U(1)$ is smooth and $g=G|_{S^1}$, then $\int_{S^1}g^*d\theta=0$; equivalently $w(g)=0$.
>
> **Hint:** $S^1$ is a closed manifold (empty boundary); $d\theta$ is closed and pullback commutes with the exterior derivative; apply Stokes on $S^1$ for (i) and on $D^2$ for (ii).
>
> **Why needed:** It supplies the implication "extends over the disc $\Rightarrow$ winding number zero" that closes the equivalence cycle in part (d).
>
> > [!note]- Full proof
> > **Part (i).** The circle $S^1$ is a compact oriented $1$-manifold without boundary, $\partial S^1=\varnothing$. By [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] — for a smooth $(n-1)$-form $\eta$ on a compact oriented $n$-manifold $M$ with boundary, $\int_M d\eta=\int_{\partial M}\eta$ — applied to $\eta=u$ (a $0$-form) on $M=S^1$ (so $n=1$),
> > $$\int_{S^1}du=\int_{\partial S^1}u=\int_{\varnothing}u=0,$$
> > since the integral over the empty set is zero.
> >
> > **Part (ii).** Let $\iota\colon S^1=\partial D^2\hookrightarrow D^2$ be the boundary inclusion, so that $g=G\circ\iota$ and hence $g^*d\theta=\iota^*(G^*d\theta)$ by functoriality of pullback. The form $G^*d\theta$ is a smooth $1$-form on the compact oriented $2$-manifold-with-boundary $D^2$. Because [[Thm - Pull-Back Commutes with the Exterior Derivative|pullback commutes with the exterior derivative]] — for a smooth map $G$ and a form $\eta$, $d(G^*\eta)=G^*(d\eta)$ — its exterior derivative is
> > $$d(G^*d\theta)=G^*(d\,d\theta),$$
> > and $d\,d\theta=0$ because $d\theta$ is a $1$-form on the $1$-manifold $U(1)$, so $d\,d\theta\in\Omega^2(U(1))=\{0\}$ (there are no nonzero $2$-forms on a $1$-manifold). Hence $G^*d\theta$ is closed. Now [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] on $D^2$, with $\partial D^2=S^1$ carrying the induced boundary orientation, gives
> > $$\int_{S^1}g^*d\theta=\int_{\partial D^2}\iota^*(G^*d\theta)=\int_{D^2}d(G^*d\theta)=\int_{D^2}0=0.$$
> > Dividing by $2\pi$, $w(g)=0$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We prove the five parts in turn. Throughout, $S^1$ and $U(1)$ are closed, oriented, connected $1$-manifolds oriented so that $\int_{U(1)}d\theta=+2\pi$ (Lemma 1), and $g,g_1,g_2\colon S^1\to U(1)$ are smooth.
>
> **Step 0 — well-posedness.** By Lemma 1, $d\theta$ is a genuine smooth $1$-form on $U(1)$, $\omega_0:=\frac1{2\pi}d\theta$ satisfies $\int_{U(1)}\omega_0=1$, and for every smooth $g$ the pullback $g^*d\theta=\frac1i g^{-1}dg$ is a smooth real $1$-form on $S^1$. Hence $w(g)=\frac1{2\pi}\int_{S^1}g^*d\theta=\frac1{2\pi i}\int_{S^1}g^{-1}dg$ is a well-defined real number, and the two displayed expressions agree. All integrals below are over the compact manifold $S^1$ and so are finite.
>
> **Part (a) — integrality and $w=\deg$.** We invoke [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the Brouwer degree theorem]]: *for closed oriented $n$-manifolds $M,N$ with $N$ connected and $f\colon M\to N$ smooth, the number $\deg f=\int_M f^*\omega$ for any $\omega\in\Omega^n(N)$ with $\int_N\omega=1$ is independent of the normalised $\omega$ (part (a) of that theorem) and equals $\sum_{x\in f^{-1}(y)}\operatorname{sign}\det df_x$ for every regular value $y$, hence is an integer (part (b)).* Here $M=S^1$ and $N=U(1)$ are closed oriented connected $1$-manifolds, $f=g$, and $\omega=\omega_0=\frac1{2\pi}d\theta$, which is normalised, $\int_{U(1)}\omega_0=1$ (Step 0). Therefore
> $$w(g)=\frac1{2\pi}\int_{S^1}g^*d\theta=\int_{S^1}g^*\omega_0=\deg g\in\mathbb Z,$$
> the middle equality being the linearity of the integral. Thus $w(g)=\deg g$ and $w(g)$ is an integer. (An independent proof of integrality, not using the degree theorem, is given in Lemma 3: $w(g)=n$ where $2\pi n$ is the monodromy of a smooth lift.)
>
> **Part (b) — homomorphism property.** By Lemma 2, $(g_1g_2)^*d\theta=g_1^*d\theta+g_2^*d\theta$ exactly. Integrating over $S^1$ and dividing by $2\pi$,
> $$w(g_1g_2)=\frac1{2\pi}\int_{S^1}(g_1g_2)^*d\theta=\frac1{2\pi}\int_{S^1}g_1^*d\theta+\frac1{2\pi}\int_{S^1}g_2^*d\theta=w(g_1)+w(g_2),$$
> using linearity of the integral. For the constant map $\mathbf1(x)\equiv1$ we have $\mathbf1^*d\theta=0$ (the differential of a constant map is zero), so $w(\mathbf1)=0$. Since the pointwise inverse satisfies $g\cdot g^{-1}=\mathbf1$, the additivity just proved gives
> $$0=w(\mathbf1)=w(g\cdot g^{-1})=w(g)+w(g^{-1}),\qquad\text{hence}\qquad w(g^{-1})=-w(g).$$
> Therefore $w\colon C^\infty(S^1,U(1))\to\mathbb Z$ is a group homomorphism from the pointwise-multiplication group to $(\mathbb Z,+)$.
>
> **Part (c) — homotopy invariance.** Suppose $g_0$ and $g_1$ are smoothly homotopic maps $S^1\to U(1)$. By part (a), $w(g_j)=\deg g_j$ for $j=0,1$. By [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the Brouwer degree theorem]], part (c) — *smoothly homotopic maps between closed oriented equidimensional manifolds have equal degree* — we get $\deg g_0=\deg g_1$. Combining, $w(g_0)=\deg g_0=\deg g_1=w(g_1)$. (Equivalently, one may argue directly: a smooth homotopy $H\colon S^1\times[0,1]\to U(1)$ makes $g_0^*d\theta$ and $g_1^*d\theta$ cohomologous in $H^1_{dR}(S^1)$ by [[Thm - Homotopy Invariance of de Rham Cohomology|homotopy invariance of de Rham cohomology]], and $\frac1{2\pi}\int_{S^1}$ depends only on the cohomology class since it vanishes on exact forms by Lemma 4(i); this reproves $w(g_0)=w(g_1)$ without the degree theorem.)
>
> **Part (d) — the three characterisations of winding number zero.** We prove the cycle of implications $1\Rightarrow2\Rightarrow3\Rightarrow1$, which establishes the mutual equivalence of statements 1 ($w(g)=0$), 2 ($g=e^{iu}$ for smooth $u\colon S^1\to\mathbb R$), and 3 ($g$ extends smoothly over $D^2$).
>
> *Direction $1\Rightarrow2$.* Assume $w(g)=0$. By Lemma 3 there is a smooth lift $\psi\colon\mathbb R\to\mathbb R$ with $g(e^{it})=e^{i\psi(t)}$ and monodromy $\psi(t+2\pi)-\psi(t)=2\pi w(g)=0$ for all $t$. Thus $\psi$ is $2\pi$-periodic and descends to a well-defined function $u\colon S^1\to\mathbb R$ by $u(e^{it}):=\psi(t)$. It is smooth: near any point $e^{it_0}$ the covering $p$ has a smooth local inverse $q$ with $q(e^{it})=t$ (a local branch), and $u=\psi\circ q$ is a composite of smooth maps there. By construction $g=e^{iu}$.
>
> *Direction $2\Rightarrow3$.* Assume $g=e^{iu}$ with $u\colon S^1\to\mathbb R$ smooth; write $\hat u(t):=u(e^{it})$, a smooth $2\pi$-periodic function. Fix a smooth cutoff $\chi\colon[0,1]\to[0,1]$ with $\chi\equiv0$ on $[0,\tfrac12]$ and $\chi\equiv1$ on $[\tfrac34,1]$. Define $G\colon D^2\to U(1)$ in polar coordinates $z=re^{it}$ ($0\le r\le1$) by
> $$G(re^{it}):=e^{\,i\,\chi(r)\,\hat u(t)},\qquad G(0):=1 .$$
> This is smooth on all of $D^2$: on the disc $\{r\le\tfrac12\}$ we have $\chi(r)=0$, so $G\equiv1$ there (in particular $G$ is smooth across the origin, where polar coordinates degenerate); on the annulus $\{r>0\}$ the polar coordinates $(r,t)$ are smooth and $G$ is a composite of the smooth maps $(r,t)\mapsto\chi(r)\hat u(t)\mapsto e^{i(\cdot)}$, well-defined because $\hat u$ is $2\pi$-periodic in $t$. On the boundary $r=1$, $\chi(1)=1$ gives $G(e^{it})=e^{i\hat u(t)}=g(e^{it})$, so $G|_{\partial D^2}=g$. Hence $g$ extends smoothly over $D^2$.
>
> *Direction $3\Rightarrow1$.* Assume $g=G|_{\partial D^2}$ for a smooth $G\colon D^2\to U(1)$. By Lemma 4(ii), $\int_{S^1}g^*d\theta=0$, so $w(g)=0$.
>
> The three implications form a cycle, so statements 1, 2, and 3 are equivalent.
>
> **Part (e) — the power maps.** Fix $k\in\mathbb Z$ and $g_k(z)=z^k$. On the source, $g_k(e^{it})=e^{ikt}$, so $g_k^{-1}dg_k=e^{-ikt}\,d(e^{ikt})=e^{-ikt}(ik\,e^{ikt})\,dt=ik\,dt$, and by Lemma 1,
> $$g_k^*d\theta=\tfrac1i g_k^{-1}dg_k=\tfrac1i(ik\,dt)=k\,dt .$$
> Therefore
> $$w(g_k)=\frac1{2\pi}\int_{S^1}g_k^*d\theta=\frac1{2\pi}\int_0^{2\pi}k\,dt=\frac1{2\pi}\cdot k\cdot2\pi=k .$$
> As a cross-check consistent with parts (a) and (b): the identity map $g_1(z)=z$ has $w(g_1)=\frac1{2\pi}\int_{S^1}d\theta=1$ (Lemma 1), and since $g_k=g_1\cdots g_1$ ($k$ factors) for $k\ge1$ under pointwise product, part (b) gives $w(g_k)=k\,w(g_1)=k$; the case $k\le0$ follows from $w(g^{-1})=-w(g)$ and $g_0\equiv1$ with $w(g_0)=0$. This also matches the regular-value formula of part (a): a generic value $y=e^{is}\in U(1)$ has exactly $k$ preimages under $z\mapsto z^k$ for $k>0$, at each of which $g_k$ is orientation-preserving (its derivative in the coordinate $t$ is $+k>0$), so the signed count is $+k$.
>
> This proves all five parts. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The argument principle in complex analysis.** Let $h$ be holomorphic and nowhere zero on an annulus containing $S^1$. Then $g:=h/|h|\colon S^1\to U(1)$ is smooth, and $w(g)=\frac1{2\pi i}\oint_{S^1}g^{-1}dg=\frac1{2\pi i}\oint_{S^1}h^{-1}\,dh$ (the modulus $|h|$ contributes an exact real form $d\log|h|$ that integrates to zero over the closed contour). By the argument principle this equals the number of zeros of $h$ inside the disc. The application is non-obvious because the winding number, defined by a real integral of an angular form, turns out to *count zeros* — the theorem is the bridge that makes "how many times the image circles the origin" and "how many roots lie inside" the same integer.

**Gauge transformations of a bundle over the circle.** A gauge transformation of the trivial $U(1)$-bundle over $S^1$ is exactly a smooth map $g\colon S^1\to U(1)$, and part (c) together with the surjectivity from part (e) shows that $w$ is a complete homotopy invariant: two gauge transformations are homotopic if and only if they have the same winding number, and every integer is realised. This is the one-dimensional prototype of the statement that the group of gauge transformations of a bundle has connected components indexed by a characteristic number, which governs large gauge transformations and the periodicity of the Chern–Simons functional; the theorem applies because the relevant invariant is literally a winding number of $g$ on a circle.

**Holonomy of a flat connection on the circle.** A flat $U(1)$-connection on the trivial bundle over $S^1$ is $A=a\,dt$ for a constant $a$, and its holonomy around the loop is $e^{-i\oint A}=e^{-2\pi i a}\in U(1)$. Deforming the connection through a loop of flat connections traces a map $S^1\to U(1)$ whose winding number measures the spectral flow of the associated family. The theorem applies because the holonomy assembles into a map into $U(1)$, and it is non-obvious that a purely spectral count (how many eigenvalues cross) equals the topological winding of the holonomy — the identification $w=\deg$ is what makes the two agree.

---

# Bridges

- **[[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|The Brouwer degree theorem]].** This page is the one-dimensional, group-valued specialisation. Part (a) is the observation that $\frac1{2\pi}d\theta$ is a normalised volume form on $U(1)$, so that $w=\deg$; parts (a)–(c) then inherit integrality, the regular-value count, and homotopy invariance directly. What the degree theorem cannot see is the group structure of $U(1)$; part (b) is the genuinely new content that the abelian target contributes.

- **[[Thm - Pi_1 of S^1 is Z|The fundamental group of the circle]].** Lemma 3 constructs a lift $\psi\colon\mathbb R\to\mathbb R$ of $g$ through the universal covering $p\colon\mathbb R\to U(1)$, and the monodromy $\psi(2\pi)-\psi(0)\in2\pi\mathbb Z$ is precisely the image of the based homotopy class $[g]$ under the isomorphism $\pi_1(U(1))\cong\mathbb Z$. Thus the analytic winding number, the Brouwer degree, and the fundamental-group invariant are one and the same integer; the covering-space route ([[Thm - Path Lifting and Homotopy Lifting|path and homotopy lifting]]) gives the topological definition, and this page proves it equals the integral.

- **[[Def - The Maurer-Cartan Form|The Maurer–Cartan form]].** The imaginary-valued $1$-form $g^{-1}dg$ appearing in the definition of $w$ is the pullback along $g$ of the (left-invariant) Maurer–Cartan form of $U(1)$, which for the abelian circle group is exactly the angular form $\frac1i\,z^{-1}dz=d\theta$ up to the factor $i$. The additivity of Lemma 2 is the abelian instance of the general transformation law of the Maurer–Cartan form under a product of maps; the correction term that appears for non-abelian groups is what makes the three-dimensional invariant $\frac1{24\pi^2}\int_{S^3}\operatorname{tr}((g^{-1}dg)^{\wedge3})$ additive only after a Stokes argument, rather than exactly.

- **[[Ex - The de Rham Cohomology of S^1 is R|The first de Rham cohomology of the circle]].** The class $[d\theta]$ generates $H^1_{dR}(U(1))\cong\mathbb R$, and $\frac1{2\pi}\int_{U(1)}$ is the isomorphism $H^1_{dR}(U(1))\to\mathbb R$ normalised so that $[d\theta]\mapsto1$. The winding number $w(g)$ is the image of the pulled-back class $[g^*d\theta]=\deg g\cdot[d\theta]$ under this isomorphism, which is why it is a homotopy invariant: pullback on cohomology sees only the homotopy class of $g$.

---

# Unlocked by This

> [!tip] Degree of a line bundle over a surface *(from Gauge Theory III §3.6)*
> A Hermitian line bundle over a closed oriented surface is trivial off a coordinate disc, and its clutching function $g\colon\partial D\to U(1)$ has a winding number $w(g)$ that, by parts (b) and (d), is independent of all choices; this integer is the **degree** of the line bundle, the topological first Chern number. See [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class]].

> [!tip] The Hopf bundle is nontrivial *(from Gauge Theory III §3.5)*
> The Hopf bundle over $S^2$ has clutching function $z\mapsto z/|z|$ on the equator, whose winding number is $1$; since a trivial bundle would force winding number $0$ by part (d), the Hopf bundle is nontrivial. See [[Ex - The Hopf Bundle is Nontrivial via the Winding Number of its Transition Function]].

> [!tip] Abelian holonomy and flat $U(1)$-connections *(from Gauge Theory V)*
> For a flat connection on a $U(1)$-bundle over a surface, the holonomies around loops assemble into a homomorphism $\pi_1\to U(1)$, and the winding numbers computed here are the local model for the monodromy representation; the additivity of part (b) is what makes the holonomy a homomorphism.
