---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - First Chern Class via the Classifying Map"
  - "Def - The Hopf Bundle"
  - "Thm - Winding Number of a Map from the Circle to U(1)"
  - "Thm - Clutching Construction for Bundles over a Closed Manifold"
  - "Thm - Classification of Principal U(1)-Bundles by the First Chern Class"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\mathbb{CP}^1$ carry the **complex orientation** (the orientation for which $(\partial_x,\partial_y)$ is a positive frame in a holomorphic coordinate $w=x+iy$), and let $\mathcal O(-1)\to\mathbb{CP}^1$ be the **tautological line bundle**, whose fibre over a point $[z_0:z_1]$ is the complex line $\mathbb C\,(z_0,z_1)\subset\mathbb C^2$ that the point names. Regard $\mathcal O(-1)$ as a principal $U(1)$-bundle by choosing the Hermitian metric induced from the standard Hermitian product of $\mathbb C^2$; over the closed connected oriented surface $\mathbb{CP}^1$ this bundle has a well-defined **degree** $\deg\mathcal O(-1)\in\mathbb Z$, the winding number of a clutching function.

**Show that**
$$\deg\mathcal O(-1)=-1,$$
by computing the clutching function of $\mathcal O(-1)$ on the equatorial circle of $\mathbb{CP}^1$ explicitly and reading off its winding number. State precisely which of the two coordinate discs plays the role of the distinguished disc $D$ in the clutching convention, and confirm that the answer is consistent with the sign convention $c_1(\mathcal O(-1))=-[\omega_1]$ recorded in the first-Chern-class definition (equivalently with Haydys' normalisation $c(\mathcal O(-1))=1-a$).

**Recall.** The objects in play are the tautological bundle and its incarnation as the Hopf bundle, the degree of a line bundle over a surface as a clutching winding number, and the winding number of a circle map.

![[Def - The Hopf Bundle#The Definition]]

The **degree** of a principal $U(1)$-bundle (equivalently a complex line bundle) $P\to\Sigma$ over a closed connected oriented surface $\Sigma$ is defined on **[[Def - First Chern Class via the Classifying Map|the first-Chern-class page]]** as follows. Fix an embedded closed disc $D\subset\Sigma$, oriented by the orientation of $\Sigma$, with boundary circle $\partial D$ carrying the induced boundary orientation, and write $\Sigma'=\Sigma\setminus D^\circ$ for the complementary compact bordered surface. Both $D$ and $\Sigma'$ are homotopy equivalent to one-dimensional complexes, so $P$ is trivial over each; choosing trivialisations $P|_D\cong D\times U(1)$ and $P|_{\Sigma'}\cong\Sigma'\times U(1)$, the two agree on a collar of $\partial D$ up to a smooth **clutching function** $g\colon\partial D\to U(1)$, and the degree is
$$\deg(P):=w(g)\in\mathbb Z,$$
the [[Thm - Winding Number of a Map from the Circle to U(1)|winding number]] of $g$. That this does not depend on the trivialisations or on the disc is proved on [[Def - First Chern Class via the Classifying Map|that page]] using [[Thm - Clutching Construction for Bundles over a Closed Manifold|the clutching construction]] and the vanishing of the winding number of any circle map that extends over a bounding surface ([[Ex - A Map Extending over a Bounding Manifold has Degree Zero]]).

![[Thm - Winding Number of a Map from the Circle to U(1)#Statement]]

![[Def - First Chern Class via the Classifying Map#The Definition]]

The tautological bundle is the associated line bundle of the Hopf bundle for the standard representation, and its unit-circle subbundle is the Hopf principal bundle $S^3\to\mathbb{CP}^1$ ([[Ex - The Tautological Line Bundle over CP^n is Associated to the Hopf Bundle]]); its nontriviality is established in [[Ex - The Hopf Bundle is Nontrivial via the Winding Number of its Transition Function]]. The present exercise sharpens "$\deg=\pm1$" to the exact value $-1$ by fixing every orientation.

---

# Convergent Strategy

**Problem class.** This is a *pin-the-sign* computation: a topological invariant whose magnitude is already known ($|\deg\mathcal O(-1)|=1$, because the Hopf bundle is nontrivial) but whose sign is the whole content. Such problems are won or lost entirely on bookkeeping — which disc is $D$, which way $\partial D$ is oriented, which trivialisation the clutching function converts *into* which — and the discipline is to fix each of these choices in writing before computing, then let the winding-number integral produce the sign mechanically.

**Assumption pattern.** The hypotheses that carry the sign are the *complex orientation* of $\mathbb{CP}^1$ (it orients both coordinate discs and hence both boundary circles) and the *definition of the clutching function* as the map that expresses the $\Sigma'$-trivialisation in terms of the $D$-trivialisation. The recognisable trigger is that we are asked for a degree of a bundle *over a sphere*, presented by two charts whose overlap deformation-retracts to a circle: this is exactly the clutching situation, and the invariant is the winding number of one $U(1)$-valued function on that circle.

**Theorem routing.** The route is: exhibit $\mathcal O(-1)$ by its two natural holomorphic frames over the affine charts $U_0=\{z_0\neq0\}$ and $U_1=\{z_1\neq0\}$; normalise them by the Hermitian metric to unit frames; compute the unit-frame transition on the overlap and hence the clutching function $g$ on the equator; declare $D$ to be the coordinate disc around $[0:1]$ so that $\partial D$ inherits the counter-clockwise orientation of the holomorphic coordinate $\xi=z_0/z_1$; and apply the [[Thm - Winding Number of a Map from the Circle to U(1)|winding-number theorem]], parts (a) and (e), to read $w(g)=-1$. A second, independent route — [[Def - First Chern Class via the Classifying Map|the classifying-map definition]] $c_1(\mathcal O(-1))=-a|_{\mathbb{CP}^1}$ with $\langle a,[\mathbb{CP}^1]\rangle=1$ — is used as a cross-check.

**Key decision point.** The one genuinely load-bearing decision is the identification of the equatorial variable with the boundary orientation of $D$. The clutching function comes out as $g=\zeta/|\zeta|$ in the coordinate $\zeta=z_1/z_0$; whether this winds $+1$ or $-1$ turns on the fact that, in the coordinate $\xi=1/\zeta$ that positively orients $\partial D$, the equator is traversed so that $\zeta=e^{-i\psi}$ runs *clockwise*. Getting this one substitution right — and not the sign of $g$ in isolation — is what produces $-1$. Everything else is forced.

---

# Legal Operations Used

This solution deploys the following operations, in the numbering of the topic page's Legal Operations (to be reconciled with [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles]] when it is assembled); each is named descriptively here.

1. **Present a line bundle by holomorphic frames over the affine charts.** Take the two evident nowhere-zero sections $(1,\zeta)$ and $(\xi,1)$ of $\mathcal O(-1)$ over $U_0$ and $U_1$; these are the local frames from which every transition function is read.

2. **Normalise a holomorphic frame by the Hermitian metric to a unit frame.** Divide each frame by its norm to land in the $U(1)$-structure, so that transition functions become $U(1)$-valued and the clutching picture applies.

3. **Read the clutching function as the unit-frame transition on the collar of $\partial D$.** Express the $\Sigma'$-trivialisation in terms of the $D$-trivialisation on the equatorial overlap; the resulting $U(1)$-valued function is the clutching function $g$.

4. **Fix the distinguished disc and transport the orientation.** Declare which coordinate disc is $D$, and push the complex orientation of $\mathbb{CP}^1$ through the holomorphic coordinate that trivialises $D$ to orient $\partial D$; this is the step that determines the sign.

5. **Compute a winding number by the power-map rule.** Once $g$ is written as $e^{\pm i\psi}$ on the oriented boundary circle, apply the [[Thm - Winding Number of a Map from the Circle to U(1)|winding-number theorem]] part (e), $w(z\mapsto z^k)=k$, to read off the integer.

6. **Cross-check a computed invariant against an independent definition.** Recompute $\deg\mathcal O(-1)$ from the classifying-map definition of $c_1$ and from the dual bundle $\mathcal O(1)$, and confirm all three routes give $-1$.

---

# Hints

> [!note]- Hint 1
> The degree is defined as the winding number of the clutching function, and the clutching function is nothing but the transition function between two trivialisations of the bundle. So you first need two trivialisations of $\mathcal O(-1)$. The bundle sits inside $\mathbb{CP}^1\times\mathbb C^2$ as the family of lines $\mathbb C(z_0,z_1)$; over the chart where $z_0\neq0$ a line is spanned by the vector $(1,\zeta)$ with $\zeta=z_1/z_0$, and over the chart where $z_1\neq0$ by $(\xi,1)$ with $\xi=z_0/z_1$. Those two vectors are your two frames.

> [!note]- Hint 2
> To land in $U(1)$ you must use *unit* frames: divide each spanning vector by its norm. On the overlap the two spanning vectors are proportional — $(\xi,1)=\zeta^{-1}(1,\zeta)$ — so the unit frames differ by a *unit* complex scalar. Compute that scalar. It will be $\bar\zeta/|\zeta|$ or its inverse; keep track of which unit frame you are writing in terms of which.

> [!note]- Hint 3
> Now the orientation. Choose $D$ to be the closed coordinate disc around the point $[0:1]$, i.e. the set $\{|\xi|\le1\}$ in the chart $U_1$. The complex orientation of $\mathbb{CP}^1$ makes $\partial D$ counter-clockwise *in the coordinate $\xi$*. On the equator $|\xi|=1$, write $\xi=e^{i\psi}$ with $\psi$ increasing (positive boundary orientation). What is $\zeta=1/\xi$ in terms of $\psi$? That substitution is where the minus sign is born.

> [!note]- Hint 4
> With $\xi=e^{i\psi}$ you have $\zeta=e^{-i\psi}$. The clutching function, expressed as "$D$-trivialisation in terms of $\Sigma'$-trivialisation", comes out as $g=\zeta/|\zeta|=\zeta=e^{-i\psi}$ on the equator. As a map of the oriented boundary circle $\psi\in[0,2\pi]$ into $U(1)$ this is $\psi\mapsto e^{-i\psi}$, the power map with exponent $-1$. Apply part (e) of the winding-number theorem.

---

# Solution

The plan is to write $\mathcal O(-1)$ through its two natural unit frames, read the clutching function off their overlap as $\zeta/|\zeta|$, and then evaluate its winding number *in the coordinate that positively orients $\partial D$*. Choosing $D$ to be the disc around $[0:1]$ forces the equatorial coordinate to run clockwise in $\zeta$, turning $\zeta/|\zeta|$ into the power map $e^{-i\psi}$ of winding number $-1$. Two independent computations — the classifying-map definition of $c_1$ and the dual bundle $\mathcal O(1)$ — confirm the value.

**Notation for the computation.** Write points of $\mathbb{CP}^1$ as $[z_0:z_1]$. The affine charts are
$$U_0=\{[z_0:z_1]:z_0\neq0\},\quad\zeta:=z_1/z_0\in\mathbb C;\qquad U_1=\{z_1\neq0\},\quad\xi:=z_0/z_1\in\mathbb C,$$
with $\xi=1/\zeta$ on the overlap $U_0\cap U_1=\{z_0\neq0\neq z_1\}$. The chart $U_0$ omits the single point $[0:1]$; the chart $U_1$ omits $[1:0]$. The **equator** is the circle
$$E=\{[z_0:z_1]:|z_0|=|z_1|\}=\{|\zeta|=1\}=\{|\xi|=1\}.$$
Because the two charts are related by the holomorphic map $\xi=1/\zeta$, whose real Jacobian determinant is $|d\xi/d\zeta|^2>0$, they induce the *same* orientation on $\mathbb{CP}^1$; this common orientation is the complex orientation, and it is the one we use throughout.

**Step 1: The two unit frames of $\mathcal O(-1)$.**

Over $U_0$ the line $\mathbb C(z_0,z_1)$ is spanned by $(1,\zeta)$; over $U_1$ by $(\xi,1)$. Normalising by the Hermitian metric gives nowhere-zero unit sections
$$\hat e_0=\frac{(1,\zeta)}{\sqrt{1+|\zeta|^2}}\ \text{ over }U_0,\qquad
\hat e_1=\frac{(\xi,1)}{\sqrt{1+|\xi|^2}}\ \text{ over }U_1.$$

> [!note]- Derivation
> A point $[z_0:z_1]\in U_0$ has $z_0\neq0$, so scaling the representative by $z_0^{-1}\in\mathbb C^\times$ gives $[z_0:z_1]=[1:\zeta]$ with $\zeta=z_1/z_0$; the line it names is $\mathbb C(1,\zeta)$, and the assignment $[1:\zeta]\mapsto(1,\zeta)$ is a smooth nowhere-zero section of $\mathcal O(-1)$ over $U_0$ (its value is a nonzero vector in the fibre line). Its Hermitian norm is $\lVert(1,\zeta)\rVert=(1+|\zeta|^2)^{1/2}$, positive and smooth in $\zeta$, so $\hat e_0=(1,\zeta)/\sqrt{1+|\zeta|^2}$ is a smooth **unit** section of $\mathcal O(-1)$ over $U_0$. It trivialises $P|_{U_0}$: the unit vectors of each fibre over $U_0$ are exactly $\{\lambda\,\hat e_0:\lambda\in U(1)\}$. The same argument over $U_1$, scaling by $z_1^{-1}$ to write $[z_0:z_1]=[\xi:1]$, gives the unit section $\hat e_1=(\xi,1)/\sqrt{1+|\xi|^2}$. $\;\checkmark$

**Step 2: The unit-frame transition on the overlap.**

On $U_0\cap U_1$,
$$\hat e_1=\frac{\bar\zeta}{|\zeta|}\,\hat e_0.$$

> [!note]- Derivation
> On the overlap $[z_0:z_1]=[1:\zeta]=[\xi:1]$ with $\xi=1/\zeta$, and the two spanning vectors are proportional:
> $$(\xi,1)=\Big(\tfrac1\zeta,1\Big)=\tfrac1\zeta\,(1,\zeta)=\zeta^{-1}(1,\zeta)\qquad\text{(clearing the common factor }\zeta^{-1}\text{).}$$
> Taking Hermitian norms, and using $|\zeta^{-1}|=|\zeta|^{-1}$,
> $$\lVert(\xi,1)\rVert=|\zeta^{-1}|\,\lVert(1,\zeta)\rVert=|\zeta|^{-1}\sqrt{1+|\zeta|^2}\qquad\text{(norm is homogeneous of degree one under complex scaling).}$$
> Therefore
> $$\hat e_1=\frac{(\xi,1)}{\lVert(\xi,1)\rVert}=\frac{\zeta^{-1}(1,\zeta)}{|\zeta|^{-1}\sqrt{1+|\zeta|^2}}=\frac{\zeta^{-1}}{|\zeta|^{-1}}\cdot\frac{(1,\zeta)}{\sqrt{1+|\zeta|^2}}=\frac{|\zeta|}{\zeta}\,\hat e_0=\frac{\bar\zeta}{|\zeta|}\,\hat e_0,$$
> where the last equality uses $|\zeta|/\zeta=|\zeta|\,\bar\zeta/(\zeta\bar\zeta)=|\zeta|\,\bar\zeta/|\zeta|^2=\bar\zeta/|\zeta|$ (rationalising by $\bar\zeta$). $\;\checkmark$

**Step 3: The clutching function, with $D$ the disc around $[0:1]$.**

Choose the distinguished disc to be
$$D:=\{|\xi|\le1\}\subset U_1\quad(\text{the closed coordinate disc around }[0:1]),\qquad \Sigma':=\mathbb{CP}^1\setminus D^\circ=\{|\zeta|\le1\}\subset U_0.$$
Trivialise $P|_D$ by the unit frame $\hat e_1$ (defined on all of $U_1\supset D$) and $P|_{\Sigma'}$ by $\hat e_0$ (defined on all of $U_0\supset\Sigma'$). The clutching function $g\colon\partial D=E\to U(1)$ — the map expressing the $\Sigma'$-trivialisation coordinate in terms of the $D$-trivialisation coordinate — is
$$g=\frac{\zeta}{|\zeta|}\quad\text{on }E.$$

> [!note]- Derivation
> Both $D$ and $\Sigma'$ are closed round discs in a chart, hence contractible, so $\hat e_1$ trivialises $P$ over $D$ and $\hat e_0$ trivialises $P$ over $\Sigma'$; their common domain contains the collar of $E$, where Step 2 applies. Write a vector $v$ of the fibre over a point of $E$ in the two trivialisations: $v=c_0\,\hat e_0=c_1\,\hat e_1$, where $c_0$ is its coordinate in the $\Sigma'$-trivialisation and $c_1$ in the $D$-trivialisation. Substituting $\hat e_1=(\bar\zeta/|\zeta|)\hat e_0$ from Step 2,
> $$c_0\,\hat e_0=c_1\,\hat e_1=c_1\frac{\bar\zeta}{|\zeta|}\,\hat e_0\ \Longrightarrow\ c_0=\frac{\bar\zeta}{|\zeta|}\,c_1\ \Longrightarrow\ c_1=\frac{\zeta}{|\zeta|}\,c_0\qquad\text{(divide by the unit }\bar\zeta/|\zeta|\text{; its inverse is }\zeta/|\zeta|\text{).}$$
> The clutching function is the map $g$ with $c_1=g\,c_0$, converting the outer ($\Sigma'$) coordinate to the inner ($D$) coordinate — the normalisation "inner trivialisation is the outer one times $g$" fixed on [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds|the classification pages]] and on [[Def - First Chern Class via the Classifying Map|the degree definition]]. Hence
> $$g=\frac{\zeta}{|\zeta|}\colon E\longrightarrow U(1).$$
> (Had we instead chosen $D=\{|\zeta|\le1\}$, the roles of $\hat e_0,\hat e_1$ would swap and the clutching function would be $\bar\zeta/|\zeta|=g^{-1}$; Step 4 shows this gives the same degree, as the well-definedness of $\deg$ demands.) $\;\checkmark$

**Step 4: The winding number in the coordinate that orients $\partial D$.**

$$w(g)=-1,\qquad\text{hence}\qquad\deg\mathcal O(-1)=w(g)=-1.$$

> [!note]- Derivation
> The disc $D=\{|\xi|\le1\}$ is a round disc in the holomorphic coordinate $\xi$, and its orientation is the complex orientation of $\mathbb{CP}^1$, which in the coordinate $\xi=u+iv$ is $du\wedge dv$. The boundary orientation induced on $\partial D$ (outward normal first, the Stokes convention) is the **counter-clockwise** sense in $\xi$: parametrise
> $$\partial D=E:\quad \xi=e^{i\psi},\qquad \psi\in[0,2\pi]\ \text{increasing.}$$
> On $E$ we have $\zeta=1/\xi=e^{-i\psi}$, so $|\zeta|=1$ and the clutching function of Step 3 is
> $$g\big|_E=\frac{\zeta}{|\zeta|}=\zeta=e^{-i\psi}\qquad\text{(since }|\zeta|=1\text{ on the equator).}$$
> As a map of the positively oriented boundary circle $\psi\mapsto e^{-i\psi}$, this is the power map $z\mapsto z^{-1}$ under the identification $z=e^{i\psi}$ of $\partial D$ with the standard circle. By part (e) of the [[Thm - Winding Number of a Map from the Circle to U(1)|winding-number theorem]] — *for each $k\in\mathbb Z$ the map $z\mapsto z^k$ has $w=k$* — we get $w(g)=-1$. Directly from the integral definition, with $g^*d\theta=d(\arg g)=d(-\psi)=-d\psi$,
> $$w(g)=\frac1{2\pi}\int_{\partial D}g^*d\theta=\frac1{2\pi}\int_0^{2\pi}(-d\psi)=\frac{-2\pi}{2\pi}=-1,$$
> the boundary being traversed in the positive ($\psi$-increasing) sense. By the definition of degree recalled above, $\deg\mathcal O(-1)=w(g)=-1$. $\;\blacksquare$

> [!note]- Complete formal solution
> **Claim.** With the complex orientation of $\mathbb{CP}^1$, $\deg\mathcal O(-1)=-1$.
>
> Use the affine charts $U_0=\{z_0\neq0\}$, $\zeta=z_1/z_0$, and $U_1=\{z_1\neq0\}$, $\xi=z_0/z_1=1/\zeta$; they induce the same (complex) orientation because $\xi=1/\zeta$ is holomorphic. The line $\mathbb C(z_0,z_1)$ is spanned by $(1,\zeta)$ over $U_0$ and by $(\xi,1)$ over $U_1$; the corresponding unit sections of the Hermitian bundle $\mathcal O(-1)$ are
> $$\hat e_0=\frac{(1,\zeta)}{\sqrt{1+|\zeta|^2}},\qquad \hat e_1=\frac{(\xi,1)}{\sqrt{1+|\xi|^2}}.$$
> On the overlap $(\xi,1)=\zeta^{-1}(1,\zeta)$, so $\lVert(\xi,1)\rVert=|\zeta|^{-1}\lVert(1,\zeta)\rVert$ and hence $\hat e_1=(|\zeta|/\zeta)\hat e_0=(\bar\zeta/|\zeta|)\hat e_0$.
>
> Take $D=\{|\xi|\le1\}$ (the disc around $[0:1]$) as the distinguished disc, $\Sigma'=\{|\zeta|\le1\}$; trivialise $P|_D$ by $\hat e_1$ and $P|_{\Sigma'}$ by $\hat e_0$. Writing a fibre vector as $c_0\hat e_0=c_1\hat e_1$ and substituting the frame relation gives $c_1=(\zeta/|\zeta|)c_0$, so the clutching function (outer coordinate to inner coordinate) is $g=\zeta/|\zeta|$ on the equator $E=\{|\zeta|=1\}=\{|\xi|=1\}$.
>
> The complex orientation makes $\partial D$ counter-clockwise in $\xi$: parametrise $\xi=e^{i\psi}$, $\psi\in[0,2\pi]$ increasing. Then $\zeta=e^{-i\psi}$ on $E$, and $g=\zeta=e^{-i\psi}$, the power map of exponent $-1$. By the winding-number theorem (part (e), or directly $\int_0^{2\pi}(-d\psi)/2\pi=-1$), $w(g)=-1$. Therefore $\deg\mathcal O(-1)=w(g)=-1$.
>
> This agrees with the classifying-map definition: the tautological bundle is classified by the inclusion $\iota\colon\mathbb{CP}^1\hookrightarrow\mathbb{CP}^\infty$, so $c_1(\mathcal O(-1))=-\iota^*a=-a|_{\mathbb{CP}^1}$ with $\langle a,[\mathbb{CP}^1]\rangle=1$ (Haydys' normalisation, T3.1.2(iv): $c(\mathcal O(-1))=1-a$), whence $\deg\mathcal O(-1)=\langle c_1(\mathcal O(-1)),[\mathbb{CP}^1]\rangle=-1$; and with the dual bundle $\deg\mathcal O(-1)=-\deg\mathcal O(1)=-1$ because $\mathcal O(1)$ carries the linear forms as holomorphic sections, each vanishing once with positive index. $\;\blacksquare$

> [!warning] Illegal but tempting: reading the sign off $g=\zeta/|\zeta|$ without transporting the orientation
> It is tempting to see the clutching function $g=\zeta/|\zeta|$, note that on the circle $\zeta=e^{i\phi}$ it is $e^{i\phi}$, and conclude $w(g)=+1$, hence $\deg=+1$. This is wrong, and the error is instructive: the winding number must be computed along $\partial D$ *with its boundary orientation*, not along $\{|\zeta|=1\}$ with the orientation of the $\zeta$-plane. Because the distinguished disc $D=\{|\xi|\le1\}$ lives in the *reciprocal* coordinate $\xi=1/\zeta$, its positively oriented boundary runs clockwise in $\zeta$, i.e. $\zeta=e^{-i\psi}$; the honest winding number is $-1$. The extra condition that makes the naive reading legal is choosing $D=\{|\zeta|\le1\}$ instead — but then the clutching function is $g^{-1}=\bar\zeta/|\zeta|=e^{-i\phi}$ on $\partial D$ oriented counter-clockwise in $\zeta$, which again gives $-1$. Either way the sign is $-1$; what is illegal is mixing the disc of one choice with the equatorial orientation of the other.

> [!note]- Independent sanity check via the dual bundle $\mathcal O(1)$
> The hyperplane bundle $\mathcal O(1)=\mathcal O(-1)^\vee$ has global holomorphic sections: each linear form $\ell(z_0,z_1)=a z_0+b z_1$ with $(a,b)\neq0$ defines a section of $\mathcal O(1)$ vanishing exactly at the single point $[{-b}:a]$, and there transversally (the section is holomorphic, so its zero has local index $+1$ — a holomorphic map $\mathbb C\to\mathbb C$ with a simple zero is orientation-preserving of degree one at that zero). The signed count of zeros of a generic section equals the degree (this is the section-zero description of $\deg$ established in the proof of [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class|the U(1)-classification theorem]]), so $\deg\mathcal O(1)=+1$. By part (B) of that theorem, $\deg(L^\vee)=-\deg L$, whence $\deg\mathcal O(-1)=-\deg\mathcal O(1)=-1$, matching the clutching computation.

---

# Key Takeaways

**The magnitude of a bundle invariant over a sphere is topology; the sign is bookkeeping, and the bookkeeping is the orientation of the boundary of the distinguished disc.** That the tautological bundle is nontrivial — that $|\deg\mathcal O(-1)|=1$ — is the hairy-ball-level fact already secured by the winding of $z/|z|$. The extra work in this exercise is entirely the sign, and the sign lives in a single substitution: the distinguished disc $D$ was chosen in the coordinate $\xi$, so its positively oriented boundary is counter-clockwise *in $\xi$*, which is clockwise *in $\zeta$*, turning the clutching function $\zeta/|\zeta|$ into the power map $e^{-i\psi}$. The reusable discipline is to never read a winding number off the "obvious" parametrisation of a circle; always transport the ambient orientation to the boundary through the coordinate that trivialises the disc you called $D$. This is the same discipline that fixes the sign of a residue (orient the contour as the boundary of the region), the sign of a linking number, and the sign of the instanton number in the four-dimensional analogue on [[Ex - SU(2)-Bundles over S^4 of Every Chern Number]].

**A characteristic number can be computed by whichever of its definitions is cheapest, and the agreement of two computations is the proof that the conventions are consistent.** Here three routes met at $-1$: the clutching winding number, the classifying-map pairing $c_1(\mathcal O(-1))=-a|_{\mathbb{CP}^1}$ with $\langle a,[\mathbb{CP}^1]\rangle=1$, and the dual-bundle count $-\deg\mathcal O(1)=-1$. Each route uses a different convention — the sign in the clutching orientation, the minus sign in Haydys' $c_1:=-f^*a$, and the rule $\deg(L^\vee)=-\deg L$ — and the fact that they agree is exactly what certifies that the series' sign conventions ($c_1(\mathcal O(-1))=-[\omega_1]$, complex orientation, boundary-oriented clutching) form a coherent whole rather than a set of independently chosen minus signs. When you meet an invariant with a contested sign in the literature, the productive move is not to argue about one definition but to compute it two ways and let the consistency requirement pin the convention. Haydys' normalisation $c(\mathcal O(-1))=1-a$ (his T3.1.2(iv)) and the definitional minus sign in $c_1:=-f^*a$ (his D2.4.5) are precisely engineered so that the tautological bundle, the most concrete line bundle there is, has degree $-1$ rather than $+1$.

**Why $-1$ and not $+1$: the tautological bundle is a *sub*bundle, and subbundles of a trivial bundle have non-positive degree.** The line $\mathbb C(z_0,z_1)$ over $[z_0:z_1]$ is a genuine subspace of the fixed $\mathbb C^2$, so $\mathcal O(-1)$ embeds in the trivial bundle $\mathbb{CP}^1\times\mathbb C^2$; its "twisting" is that of a line rotating *inside* a fixed plane, and such a bundle can only lose sections, never gain them — it has no nonzero holomorphic section at all, which already forces $\deg\le0$, and the minimal nontrivial value is $-1$. The dual $\mathcal O(1)$, the quotient, is where the sections live (the linear forms), and it has degree $+1$. This dichotomy — sub-line-bundle of a trivial bundle has negative degree, quotient has positive degree — is the geometric content behind the sign and recurs throughout algebraic geometry as the statement that $\mathcal O(-1)$ is the *negative* generator of $\operatorname{Pic}(\mathbb{CP}^1)\cong\mathbb Z$; the exercise [[Ex - The Tautological Line Bundle over CP^n is Associated to the Hopf Bundle]] shows the same bundle as the associated bundle of the Hopf principal bundle, and [[Ex - Line Bundles of Every Degree on a Closed Oriented Surface]] shows that its powers $\mathcal O(-1)^{\otimes d}$ realise every degree $-d$.
