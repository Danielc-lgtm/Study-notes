---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds"
  - "Def - The Hopf Bundle"
  - "Ex - SU(2) is the Group of Unit Quaternions"
  - "Ex - Degree of the Power Maps on the Circle and on SU(2)"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Write $\mathbb H$ for the quaternions, $Sp(1)=\{q\in\mathbb H:|q|=1\}$ for the unit quaternions (isomorphic to $SU(2)$ by [[Ex - SU(2) is the Group of Unit Quaternions]]), and $\mathbb{HP}^1$ for the quaternionic projective line, the space of right $\mathbb H$-lines in $\mathbb H^2$. The **quaternionic Hopf bundle** is the principal $Sp(1)$-bundle
$$\pi\colon S^7\longrightarrow\mathbb{HP}^1,\qquad \pi(h_0,h_1)=[h_0:h_1],\qquad (h_0,h_1)\cdot q=(h_0q,h_1q),$$
of [[Def - The Hopf Bundle|the Hopf-bundle page]]. Establish the following.

1. **The base is a four-sphere.** The map
$$\Phi\colon\mathbb{HP}^1\longrightarrow S^4=\{(x,t)\in\mathbb H\times\mathbb R:|x|^2+t^2=1\},\qquad
\Phi([h_0:h_1])=\frac{\big(2h_1\bar h_0,\ |h_1|^2-|h_0|^2\big)}{|h_0|^2+|h_1|^2},$$
is a diffeomorphism (the quaternionic analogue of the identification $\mathbb{CP}^1\cong S^2$ of [[Thm - CP^1 is Diffeomorphic to S^2 via the Hopf Map|chapter I]]).

2. **The Hopf bundle is a clutching bundle of degree $\pm1$.** Under $\Phi$, the quaternionic Hopf bundle is $P_g$ for a clutching map $g\colon S^3\to Sp(1)$ on the boundary of a coordinate disc, with $g(q)=\bar q$ (equivalently $g(q)=q$ for the opposite choice of disc), so its Chern number is $k=\pm1$: it is a generator of the $SU(2)$-bundles over $S^4$.

3. **Every Chern number is realised.** For each $k\in\mathbb Z$ there is a principal $SU(2)$-bundle $P_{q^k}\to S^4$ with Chern number $k(P_{q^k})=k$, namely the clutching bundle of the power map $q\mapsto q^k$.

**Recall.** The objects in play are the quaternionic Hopf bundle, the classification of $SU(2)$-bundles over a four-manifold by the clutching degree, and the degree of the power maps on $S^3$.

![[Def - The Hopf Bundle#The Definition]]

![[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds#Statement]]

The clutching degree of the power map is computed in [[Ex - Degree of the Power Maps on the Circle and on SU(2)|the power-map exercise]]: the self-map $q\mapsto q^k$ of $S^3=Sp(1)$ has [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|Brouwer degree]] $k$. The one-point-triviality and clutching mechanism is the [[Thm - Clutching Construction for Bundles over a Closed Manifold|clutching construction]], as invoked inside the classification theorem above.

---

# Convergent Strategy

**Problem class.** This is a *realisation* problem: exhibit, concretely, a bundle attaining each value of an integer invariant, and identify a distinguished geometric bundle (the quaternionic Hopf bundle) as one of the generators. The classification theorem has already reduced the isomorphism theory of $SU(2)$-bundles over a closed oriented four-manifold to a single integer, the clutching degree $k(P)=\deg g$; the work here is entirely constructive — build the clutching maps and compute their degrees.

**Assumption pattern.** Two facts do all the lifting. First, over the four-sphere every $SU(2)$-bundle is a clutching bundle $P_g$ with $g\colon S^3\to SU(2)$, and $k(P_g)=\deg g$ (classification theorem, part (B)); this converts "find a bundle with Chern number $k$" into "find a self-map of $S^3$ of degree $k$". Second, the group $SU(2)\cong Sp(1)$ *is* a three-sphere, so its own power maps $q\mapsto q^k$ are self-maps of $S^3$ of degree $k$ ([[Ex - Degree of the Power Maps on the Circle and on SU(2)|the power-map exercise]]) — the target of a clutching map coincides with the sphere being mapped, and the group structure supplies maps of every degree for free. This coincidence is special to $SU(2)$ and is exactly why the four-dimensional theory is as clean as it is.

**Theorem routing.** The route is: (i) identify $\mathbb{HP}^1$ with $S^4$ by an explicit quaternionic stereographic diffeomorphism $\Phi$, so that the classification theorem for four-manifolds applies to the Hopf bundle's base; (ii) compute the transition function of the quaternionic Hopf bundle between the two affine charts and restrict it to the equatorial $S^3$, obtaining the clutching map $g(q)=\bar q$; (iii) evaluate $\deg(q\mapsto\bar q)=-1$ from the determinant of quaternionic conjugation, so $k=\pm1$ and the Hopf bundle is a generator; (iv) invoke the power maps $q\mapsto q^k$ with $\deg=k$, and the additivity $k(P_{g_1g_2})=k(P_{g_1})+k(P_{g_2})$ of part (C), to realise every integer.

**Key decision point.** The one subtlety is the sign of the Chern number of the Hopf bundle, which is genuinely a matter of the orientation chosen on $S^4=\mathbb{HP}^1$: the clutching map is quaternionic conjugation, of degree $-1$, but whether $k(P)=\deg g$ equals $-1$ or $+1$ depends on orienting the equatorial $S^3$ and the target $SU(2)$ consistently (the ledger convention on [[Def - The Hopf Bundle|the Hopf-bundle page]]). What is convention-free, and all that the realisation statement needs, is that $|k|=1$ for the Hopf bundle and that the power maps span every degree.

---

# Legal Operations Used

Named descriptively; to be reconciled with the numbering of [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles]] when the topic page is assembled.

1. **Coordinatise a projective line by two affine charts and a quotient coordinate.** Cover $\mathbb{HP}^1$ by $V_0=\{h_0\neq0\}$ and $V_1=\{h_1\neq0\}$ with right-quotient coordinates $u=h_1h_0^{-1}$ and $v=h_0h_1^{-1}$, so $v=u^{-1}$ on the overlap.

2. **Identify a projective line with a sphere by stereographic projection.** Match the two affine coordinates to inverse stereographic projections from the two poles, exhibiting $\Phi\colon\mathbb{HP}^1\to S^4$ as a diffeomorphism.

3. **Read a principal-bundle transition function from explicit local sections.** Build unit sections $s_0,s_1$ of $S^7\to\mathbb{HP}^1$ over the two charts and solve $s_1=s_0\cdot g_{01}$ for the $Sp(1)$-valued transition $g_{01}$.

4. **Restrict a transition function to the equatorial sphere to obtain a clutching map.** Take $D$ to be a coordinate disc around a pole; the transition function restricted to $\partial D=S^3$ is the clutching map $g$, and $k(P)=\deg g$ by the classification theorem.

5. **Compute the degree of an orthogonal self-map of a sphere by its determinant.** Quaternionic conjugation is the linear map $\operatorname{diag}(1,-1,-1,-1)$ of $\mathbb R^4$; its restriction to $S^3$ has degree equal to its determinant, $-1$.

6. **Realise every value of an additive invariant by powers of a generator.** Use the power maps $q\mapsto q^k$ (degree $k$) together with additivity of the clutching degree to produce a bundle of every Chern number.

---

# Hints

> [!note]- Hint 1
> A point of $\mathbb{HP}^1$ is a right $\mathbb H$-line $[h_0:h_1]$. On the chart $h_0\neq0$ scale on the right by $h_0^{-1}$ to write $[h_0:h_1]=[1:u]$ with $u=h_1h_0^{-1}$; on $h_1\neq0$ write $[v:1]$ with $v=h_0h_1^{-1}$. The two coordinates are related by $v=u^{-1}$. Now compare with the two stereographic charts of $S^4$ from the two poles — a single quaternion parametrises each.

> [!note]- Hint 2
> To see the bundle, you need local sections of $S^7\to\mathbb{HP}^1$. Over $h_0\neq0$ the obvious representative of $[1:u]$ is $(1,u)\in\mathbb H^2$; normalise it to land on $S^7$. Do the same with $(v,1)$ over $h_1\neq0$. On the overlap the two lie on the same fibre, so they differ by right multiplication by a unit quaternion — that unit quaternion is the transition function.

> [!note]- Hint 3
> Solving $s_1=s_0\cdot g_{01}$ gives $g_{01}=\bar u/|u|$. On the equator $|u|=1$, so $g_{01}=\bar u$: the clutching map is quaternionic conjugation $q\mapsto\bar q$, a self-map of $S^3$. What is its Brouwer degree? Conjugation fixes the real axis and negates the three imaginary directions; it is an orthogonal transformation of $\mathbb R^4$, and an orthogonal map restricts to $S^n$ with degree equal to its determinant.

> [!note]- Hint 4
> The Hopf bundle now has $|k|=1$. For the rest, the classification theorem says $k(P_g)=\deg g$ and that clutching degrees add under pointwise products of clutching maps. The identity map $q\mapsto q$ has degree $1$; its $k$-th pointwise power is $q\mapsto q^k$, of degree $k$ ([[Ex - Degree of the Power Maps on the Circle and on SU(2)]]). What Chern number does $P_{q^k}$ have?

---

# Solution

The plan is to first turn $\mathbb{HP}^1$ into a bona fide four-sphere by writing down the quaternionic stereographic diffeomorphism, so that the four-manifold classification theorem applies; then to compute the quaternionic Hopf bundle's transition function between the two affine charts, restrict it to the equatorial $S^3$, and recognise it as quaternionic conjugation, of degree $-1$; and finally to realise every Chern number by the power maps $q\mapsto q^k$, whose degrees are exactly the integers. The coincidence that the structure group $SU(2)$ is itself the sphere $S^3$ being clutched is what makes the last step immediate.

**Notation for the computation.** Points of $\mathbb{HP}^1$ are right $\mathbb H$-lines $[h_0:h_1]=[h_0q:h_1q]$ for $q\in\mathbb H^\times$. The affine charts are
$$V_0=\{[h_0:h_1]:h_0\neq0\},\quad u:=h_1h_0^{-1}\in\mathbb H;\qquad
V_1=\{h_1\neq0\},\quad v:=h_0h_1^{-1}\in\mathbb H,$$
with $v=u^{-1}$ on $V_0\cap V_1$; the chart $V_0$ omits $[0:1]$ and $V_1$ omits $[1:0]$. Write $S^4=\{(x,t)\in\mathbb H\times\mathbb R:|x|^2+t^2=1\}$ with north pole $N=(0,1)$ and south pole $S=(0,-1)$, and stereographic projections
$$\sigma_N(x,t)=\frac{x}{1-t}\ \ (\text{from }N),\qquad \sigma_S(x,t)=\frac{x}{1+t}\ \ (\text{from }S),\qquad x\in\mathbb H .$$

**Step 1: $\Phi$ is well defined on $\mathbb{HP}^1$.**

The formula
$$\Phi([h_0:h_1])=\frac{\big(2h_1\bar h_0,\ |h_1|^2-|h_0|^2\big)}{|h_0|^2+|h_1|^2}$$
lands in $S^4$ and is independent of the representative of $[h_0:h_1]$.

> [!note]- Derivation
> *Lands in $S^4$.* Put $r=|h_0|^2+|h_1|^2>0$. The candidate image is $(x,t)=(2h_1\bar h_0,\,|h_1|^2-|h_0|^2)/r$. Then, using $|h_1\bar h_0|=|h_1|\,|h_0|$ (the quaternionic norm is multiplicative) and hence $|2h_1\bar h_0|^2=4|h_0|^2|h_1|^2$,
> $$|x|^2+t^2=\frac{4|h_0|^2|h_1|^2+(|h_1|^2-|h_0|^2)^2}{r^2}=\frac{(|h_0|^2+|h_1|^2)^2}{r^2}=\frac{r^2}{r^2}=1\qquad\text{(since }4ab+(b-a)^2=(a+b)^2\text{).}$$
> So $\Phi([h_0:h_1])\in S^4$.
>
> *Independent of the representative.* Replace $(h_0,h_1)$ by $(h_0q,h_1q)$ for $q\in\mathbb H^\times$. The imaginary-part numerator transforms as
> $$2(h_1q)\overline{(h_0q)}=2h_1q\,\bar q\,\bar h_0=2h_1|q|^2\bar h_0=|q|^2\,(2h_1\bar h_0)\qquad\text{(since }q\bar q=|q|^2\in\mathbb R\text{ is central),}$$
> the real-part numerator as $|h_1q|^2-|h_0q|^2=|q|^2(|h_1|^2-|h_0|^2)$, and the denominator as $|h_0q|^2+|h_1q|^2=|q|^2 r$. The common factor $|q|^2$ cancels between numerator and denominator, so $\Phi([h_0q:h_1q])=\Phi([h_0:h_1])$. Hence $\Phi$ is a well-defined map $\mathbb{HP}^1\to S^4$. $\;\checkmark$

**Step 2: $\Phi$ is a diffeomorphism.**

In the chart $V_0$, $\Phi$ is inverse stereographic projection from the north pole; in $V_1$, inverse stereographic projection from the south pole composed with conjugation. Hence $\Phi$ is a smooth bijection with smooth inverse.

> [!note]- Derivation
> *Chart $V_0$.* For $[1:u]$ (that is $h_0=1$, $h_1=u$) the formula gives $x=2u/(1+|u|^2)$, $t=(|u|^2-1)/(1+|u|^2)$. Then
> $$1-t=\frac{(1+|u|^2)-(|u|^2-1)}{1+|u|^2}=\frac{2}{1+|u|^2},\qquad
> \sigma_N(\Phi([1:u]))=\frac{x}{1-t}=\frac{2u/(1+|u|^2)}{2/(1+|u|^2)}=u .$$
> Thus $\Phi|_{V_0}=\sigma_N^{-1}$, the inverse stereographic projection from $N$; it is a diffeomorphism of $V_0=\{[1:u]:u\in\mathbb H\}$ onto $S^4\setminus\{N\}$, and $\Phi([0:1])=(0,1)=N$ is the missing pole (the limit $|u|\to\infty$).
>
> *Chart $V_1$.* For $[v:1]$ the formula gives $x=2\bar v/(1+|v|^2)$, $t=(1-|v|^2)/(1+|v|^2)$, so $1+t=2/(1+|v|^2)$ and
> $$\sigma_S(\Phi([v:1]))=\frac{x}{1+t}=\frac{2\bar v/(1+|v|^2)}{2/(1+|v|^2)}=\bar v .$$
> Thus $\Phi|_{V_1}=\sigma_S^{-1}\circ(v\mapsto\bar v)$, a composition of two diffeomorphisms, hence a diffeomorphism of $V_1$ onto $S^4\setminus\{S\}$.
>
> *Global.* The two charts cover $\mathbb{HP}^1$ and their images cover $S^4$; on the overlap the two descriptions agree because the projective transition $v=u^{-1}$ matches the stereographic transition $\sigma_S\sigma_N^{-1}(u)=u/|u|^2=\overline{u^{-1}}$ (indeed $\bar v=\overline{u^{-1}}$). A map that is a diffeomorphism in each of two charts covering the domain, agreeing on overlaps and bijective onto the codomain, is a diffeomorphism. Therefore $\Phi\colon\mathbb{HP}^1\to S^4$ is a diffeomorphism, and the classification theorem for principal $SU(2)$-bundles over a closed connected oriented four-manifold applies to the Hopf bundle over $S^4$. $\;\checkmark$

**Step 3: The transition function of the quaternionic Hopf bundle.**

Over the two charts, unit sections of $\pi\colon S^7\to\mathbb{HP}^1$ are
$$s_0([1:u])=\frac{(1,u)}{\sqrt{1+|u|^2}}\ \text{ over }V_0,\qquad s_1([v:1])=\frac{(v,1)}{\sqrt{1+|v|^2}}\ \text{ over }V_1,$$
and their transition, defined by $s_1=s_0\cdot g_{01}$, is
$$g_{01}=\frac{\bar u}{|u|}\in Sp(1)\quad\text{on }V_0\cap V_1 .$$

> [!note]- Derivation
> The vector $(1,u)\in\mathbb H^2$ represents the line $[1:u]$ and has norm $\sqrt{1+|u|^2}$; normalising gives a point of $S^7$ with $\pi(s_0([1:u]))=[1:u]$, so $s_0$ is a smooth section over $V_0$. Likewise $s_1$ over $V_1$. On the overlap, using $v=u^{-1}$ and $|v|=|u|^{-1}$,
> $$\sqrt{1+|v|^2}=\sqrt{1+|u|^{-2}}=|u|^{-1}\sqrt{|u|^2+1}=|u|^{-1}\sqrt{1+|u|^2}.$$
> Since $s_0$ and $s_1$ lie on the same $Sp(1)$-fibre (they cover the same point $[h_0:h_1]$), there is a unique $g_{01}\in Sp(1)$ with $s_1=s_0\cdot g_{01}=s_0\, g_{01}$ (the right action). Reading the *second* quaternionic component of $s_1=s_0 g_{01}$,
> $$\frac{1}{\sqrt{1+|v|^2}}=\frac{u}{\sqrt{1+|u|^2}}\,g_{01}\ \Longrightarrow\
> g_{01}=u^{-1}\,\frac{\sqrt{1+|u|^2}}{\sqrt{1+|v|^2}}=u^{-1}\,|u|=\frac{\bar u}{|u|^2}\,|u|=\frac{\bar u}{|u|},$$
> where $u^{-1}=\bar u/|u|^2$ (the quaternionic inverse). The *first* component confirms it: $s_1$ has first component $v/\sqrt{1+|v|^2}=u^{-1}|u|/\sqrt{1+|u|^2}=(\bar u/|u|)/\sqrt{1+|u|^2}$, while $s_0 g_{01}$ has first component $1\cdot g_{01}/\sqrt{1+|u|^2}=(\bar u/|u|)/\sqrt{1+|u|^2}$; the two agree. Finally $|g_{01}|=|\bar u|/|u|=1$, so indeed $g_{01}\in Sp(1)$. $\;\checkmark$

**Step 4: The clutching map is conjugation, of degree $-1$; the Hopf bundle is a generator.**

Take $D$ to be a coordinate disc around the north pole $N=[0:1]\in V_1$, with $X\setminus D^\circ$ a disc around $S=[1:0]\in V_0$; the equator is the $S^3=\{|u|=1\}$. The clutching map is
$$g=g_{01}\big|_{|u|=1}=\big(u\mapsto\bar u\big)\colon S^3\longrightarrow Sp(1)=SU(2),\qquad \deg g=-1,$$
so $k(\text{quaternionic Hopf bundle})=\deg g=\pm1$ and the bundle generates.

> [!note]- Derivation
> Under $\Phi$, the equatorial three-sphere $\{t=0\}=\{(x,0):|x|=1\}$ of $S^4$ pulls back to $\{|h_0|=|h_1|\}$, that is $|u|=1$ in the $V_0$-coordinate (from Step 2, $t=(|u|^2-1)/(1+|u|^2)=0\iff|u|=1$). The disc $D$ around $N=[0:1]$ lies in $V_1$, so the inner trivialisation is $s_1$; the outer disc lies in $V_0$, trivialised by $s_0$. The classification theorem normalises the clutching map so that the inner trivialisation is the outer one times $g$, i.e. $s_1=s_0\cdot g$; by Step 3 this is $g=g_{01}=\bar u/|u|$, which on the equator $|u|=1$ is $g(u)=\bar u$.
>
> The clutching map is thus quaternionic conjugation restricted to the unit sphere, $\kappa\colon S^3\to S^3$, $\kappa(q)=\bar q$. In the real coordinates $q=a+bi+cj+dk\leftrightarrow(a,b,c,d)\in\mathbb R^4$, conjugation is the linear map
> $$\kappa=\operatorname{diag}(1,-1,-1,-1)\in O(4),\qquad \det\kappa=-1 .$$
> An orthogonal linear map $A\in O(n+1)$ restricts to a diffeomorphism of $S^n$ whose Brouwer degree equals $\det A$ (it is homotopic within $O(n+1)$ to a composition of $\det A$-many reflections when $\det A=\pm1$, and a single reflection of $S^n$ has degree $-1$). Hence
> $$\deg g=\deg\kappa=\det\kappa=-1 .$$
> By part (B) of the classification theorem, $k(P_g)=\deg g$, so the quaternionic Hopf bundle has Chern number $k=-1$ under the orientation conventions fixed on [[Def - The Hopf Bundle|the Hopf-bundle page]] (with the opposite choice of distinguished disc the clutching map is the inverse transition $u\mapsto u/|u|$, i.e. $q\mapsto q$ on the equator, of degree $+1$; the absolute sign of $k$ depends on the orientation of $S^4=\mathbb{HP}^1$). Either way $|k|=1$, so the quaternionic Hopf bundle is a generator of the $SU(2)$-bundles over $S^4$. $\;\checkmark$

**Step 5: Every Chern number is realised.**

For each $k\in\mathbb Z$ the clutching bundle $P_{g_k}$ of the power map $g_k(q)=q^k$ has Chern number $k$.

> [!note]- Derivation
> By part (C) of the classification theorem, for every clutching map $g\colon S^3\to SU(2)$ there is a bundle $P_g\to S^4$ with $k(P_g)=\deg g$, and the clutching degree is additive under pointwise products: $k(P_{g_1g_2})=k(P_{g_1})+k(P_{g_2})$. Take $g_k(q)=q^k$, the $k$-th pointwise power of the identity clutching map $\mathrm{id}(q)=q$. By [[Ex - Degree of the Power Maps on the Circle and on SU(2)|the power-map exercise]], the self-map $q\mapsto q^k$ of $S^3=Sp(1)$ has Brouwer degree $k$; therefore
> $$k(P_{g_k})=\deg g_k=k .$$
> (Consistently with additivity, $g_k=g_1^{\,k}$ pointwise gives $k(P_{g_k})=k\cdot k(P_{g_1})=k\cdot\deg(\mathrm{id})=k\cdot1=k$, since the identity map of $S^3$ has degree $1$.) As $k$ ranges over $\mathbb Z$, so does $k(P_{g_k})$; hence every integer is the Chern number of some principal $SU(2)$-bundle over $S^4$. The quaternionic Hopf bundle of Step 4 is the generator $|k|=1$ inside this family. $\;\blacksquare$

> [!note]- Complete formal solution
> **Claim.** The quaternionic Hopf bundle $S^7\to\mathbb{HP}^1$ has base diffeomorphic to $S^4$ and is a clutching generator ($|k|=1$), and every integer occurs as the Chern number of a principal $SU(2)$-bundle over $S^4$.
>
> *Base.* Define $\Phi([h_0:h_1])=(2h_1\bar h_0,\,|h_1|^2-|h_0|^2)/(|h_0|^2+|h_1|^2)$. Multiplicativity of the quaternionic norm gives $|x|^2+t^2=1$, so $\Phi$ maps into $S^4$; the factor $|q|^2$ cancels under $(h_0,h_1)\mapsto(h_0q,h_1q)$, so $\Phi$ is well defined on $\mathbb{HP}^1$. In the chart $h_0\neq0$ ($h_0=1$, $u=h_1$) one computes $\sigma_N\circ\Phi([1:u])=u$, and in $h_1\neq0$, $\sigma_S\circ\Phi([v:1])=\bar v$; thus $\Phi$ is inverse stereographic projection in each chart, agreeing on the overlap ($v=u^{-1}$ matches $\sigma_S\sigma_N^{-1}(u)=\overline{u^{-1}}$), hence a diffeomorphism $\mathbb{HP}^1\cong S^4$.
>
> *Clutching map.* Unit sections $s_0=(1,u)/\sqrt{1+|u|^2}$ over $\{h_0\neq0\}$ and $s_1=(v,1)/\sqrt{1+|v|^2}$ over $\{h_1\neq0\}$ satisfy $s_1=s_0\cdot g_{01}$ with $g_{01}=\bar u/|u|\in Sp(1)$ (from $\sqrt{1+|v|^2}=|u|^{-1}\sqrt{1+|u|^2}$ and $u^{-1}=\bar u/|u|^2$). Taking $D$ a disc around $[0:1]$, the equator is $\{|u|=1\}$ and the clutching map is $g(u)=\bar u$: quaternionic conjugation, the orthogonal map $\operatorname{diag}(1,-1,-1,-1)$ of $\mathbb R^4$, of determinant $-1$, hence a degree $-1$ self-map of $S^3$. By the classification theorem $k(P_g)=\deg g=\pm1$ (the sign being the orientation convention), so the Hopf bundle is a generator.
>
> *Realisation.* For $k\in\mathbb Z$, the power map $g_k(q)=q^k$ has degree $k$; the clutching bundle $P_{g_k}\to S^4$ has $k(P_{g_k})=\deg g_k=k$. Every integer is realised. $\;\blacksquare$

> [!warning] Illegal but tempting: using $2\bar h_0h_1$ (the complex-Hopf form) as the identification
> By analogy with Bär's complex Hopf map one is tempted to set $\Phi([h_0:h_1])=(2\bar h_0h_1,\,\ldots)$. This fails: under the *right* action $(h_0,h_1)\mapsto(h_0q,h_1q)$ the expression $\bar h_0h_1$ transforms as $\overline{h_0q}\,h_1q=\bar q(\bar h_0h_1)q$, a conjugate, so it is **not** invariant on $\mathbb{HP}^1$ and $\Phi$ is not even well defined. The correct invariant is $h_1\bar h_0$, for which $\,(h_1q)\overline{(h_0q)}=h_1q\bar q\bar h_0=h_1\bar h_0$ (using $q\bar q=1$). The extra condition that would rescue the naive formula is switching to a *left* $Sp(1)$-action $(h_0,h_1)\mapsto(qh_0,qh_1)$, under which $\bar h_0h_1$ *is* invariant; but the series fixes right actions on principal bundles throughout, so one must use $h_1\bar h_0$.

> [!note]- A remark on the sign and the orientation of $S^4$
> The absolute sign of the Chern number of the quaternionic Hopf bundle — whether $k=+1$ or $k=-1$ — is not intrinsic: it is the joint choice of an orientation on $S^4=\mathbb{HP}^1$, an orientation on the target $SU(2)\cong S^3$, and the boundary orientation on the equatorial $S^3=\partial D$. This is the four-dimensional analogue of the sign subtlety of [[Ex - The Tautological Bundle over CP^1 has Degree Minus One]]. What is convention-independent is the magnitude $|k|=1$ (the Hopf bundle generates) and the realisation of *every* integer by the power maps, because $\{\pm k:k\in\mathbb Z\}=\mathbb Z$ regardless of the sign. The series' fixed conventions and the resulting sign are recorded once on the ledger of [[Def - The Hopf Bundle|the Hopf-bundle page]].

---

# Key Takeaways

**When the structure group is itself the sphere being clutched, realisation of every characteristic number is automatic.** The classification theorem reduces $SU(2)$-bundles over $S^4$ to a single integer, the clutching degree $k(P)=\deg g$ of a map $g\colon S^3\to SU(2)$. The decisive structural fact is that $SU(2)\cong Sp(1)$ *is* the three-sphere, so the clutching maps are self-maps of $S^3$, and the group's own power maps $q\mapsto q^k$ supply self-maps of every degree with no further construction. This is a recurring luxury of low-dimensional gauge theory: the same coincidence $SU(2)\cong S^3$ underlies the cleanness of instanton counting on four-manifolds and the identification $\pi_3(SU(2))\cong\mathbb Z$ that (beyond this series' needs) would upgrade "every $k$ is realised" to "$k$ is a complete invariant". The transferable diagnostic: whenever an invariant is a homotopy class of maps into a Lie group that happens to be a sphere, look to the group's power maps to hit every value, and to additivity of the invariant under the group product to organise them.

**Identifying $\mathbb{HP}^1$ with $S^4$ is the exact quaternionic replay of $\mathbb{CP}^1\cong S^2$, and the only new hazard is noncommutativity.** The construction is the same in every line: two affine charts with reciprocal coordinates, matched to inverse stereographic projections from two poles, glued by an inversion. The single place where quaternions bite is the choice of invariant for the identification map — $h_1\bar h_0$, not $\bar h_0 h_1$ — dictated by the *right* action convention, because only $h_1\bar h_0$ is fixed when both entries are multiplied on the right by a unit quaternion. Carrying the complex intuition over verbatim produces an ill-defined map; carrying it over *with attention to the side on which scalars act* produces the diffeomorphism. This is the general lesson of quaternionic linear algebra: every formula that was symmetric over $\mathbb C$ acquires a definite handedness over $\mathbb H$, and the handedness is fixed by which side the structure group acts on. The same care governs the associated-bundle constructions of §3.4 and the representation-theoretic identifications of $SU(2)$.

**The clutching map of a Hopf-type bundle is the transition function on the equator, and its degree is the bundle's characteristic number — computed, when the map is linear, by a determinant.** The quaternionic Hopf bundle's transition function came out as $\bar u/|u|$, restricting on the equatorial $S^3$ to quaternionic conjugation $q\mapsto\bar q$; because conjugation is the orthogonal map $\operatorname{diag}(1,-1,-1,-1)$, its degree is its determinant, $-1$, with no integration required. This "degree of a linear self-map of a sphere is its determinant" shortcut is worth internalising: it computes the degree of antipodal maps, reflections, and conjugations instantly, and it is exactly how one sees that the antipodal map of $S^n$ has degree $(-1)^{n+1}$ (see [[Ex - The Antipodal Map of S^n has Degree Minus One to the Power n plus 1]]). The broader principle, shared with the two-dimensional [[Ex - The Tautological Bundle over CP^1 has Degree Minus One|tautological-bundle computation]], is that a bundle over a sphere is completely captured by one map of the equator into the structure group, so every question about it — triviality, characteristic number, generation — is a question about the degree, or homotopy class, of that single map.
