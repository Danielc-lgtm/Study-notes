---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Associated Bundle"
  - "Def - The Hopf Bundle"
  - "Def - Complex Vector Bundle and Hermitian Structure"
  - "Thm - Free Proper Actions Give Principal Bundles"
  - "Def - Complex Projective Space as a Quotient"
tags: [geometry, gauge-theory]
difficulty: "⭐⭐"
---

# Problem Statement

Let $n\ge1$. Recall the **Hopf bundle**: $U(1)=\{\lambda\in\mathbb{C}:|\lambda|=1\}$ acts on the unit sphere

$$S^{2n+1}=\Big\{z=(z_0,\dots,z_n)\in\mathbb{C}^{n+1}\ :\ |z_0|^2+\cdots+|z_n|^2=1\Big\}$$

on the right by scalar multiplication, $z\cdot\lambda=z\lambda=(z_0\lambda,\dots,z_n\lambda)$, and the quotient map

$$\pi\colon S^{2n+1}\to\mathbb{CP}^n,\qquad \pi(z)=[z]=\mathbb{C}z$$

is a principal $U(1)$-bundle. Here $[z]\in\mathbb{CP}^n$ is the complex line $\ell_z:=\mathbb{C}z\subseteq\mathbb{C}^{n+1}$ spanned by $z$; we use the same symbol for the point of projective space and for the line it names. Recall also the **tautological line bundle**

$$\mathcal{O}(-1):=\Big\{(\ell,w)\in\mathbb{CP}^n\times\mathbb{C}^{n+1}\ :\ w\in\ell\Big\},\qquad \operatorname{pr}\colon\mathcal{O}(-1)\to\mathbb{CP}^n,\ (\ell,w)\mapsto\ell,$$

whose fibre over $\ell$ is the line $\ell$ itself (which contains $0$), realised as a rank-one complex subbundle of the trivial bundle $\mathbb{CP}^n\times\mathbb{C}^{n+1}$.

Fix the complex one-dimensional representation

$$\varrho_1\colon U(1)\to GL(\mathbb{C})=\mathbb{C}^\times,\qquad \varrho_1(\lambda)w=\lambda w,$$

and form the associated complex line bundle $S^{2n+1}\times_{U(1)}\mathbb{C}=S^{2n+1}\times_{\varrho_1}\mathbb{C}$, with the series convention $(z,w)\cdot\lambda=(z\lambda,\varrho_1(\lambda^{-1})w)=(z\lambda,\lambda^{-1}w)$, and classes $[z,w]$.

**Prove** the following.

1. **The representation is forced.** Among the one-dimensional complex representations $\varrho_m(\lambda)w=\lambda^m w$ ($m\in\mathbb{Z}$), the map $[z,w]\mapsto([z],wz)$ is well defined precisely for $m=1$; that is, $\varrho_1$ is the unique such representation making the formula independent of the representative.

2. **It is an isomorphism.** With this $\varrho_1$, the map

$$\Phi\colon S^{2n+1}\times_{U(1)}\mathbb{C}\longrightarrow\mathcal{O}(-1),\qquad [z,w]\longmapsto\big([z],\,wz\big)$$

is a smooth isomorphism of complex line bundles over $\mathbb{CP}^n$.

**Recall:**

The objects in play are the Hopf bundle, the associated bundle of a principal bundle and a representation, and complex line bundles.

![[Def - The Hopf Bundle#The Definition]]

The right $U(1)$-action on $S^{2n+1}$ is free — $z\lambda=z$ with $z\ne0$ forces $\lambda=1$ — and $U(1)$ is compact, so by [[Thm - Free Proper Actions Give Principal Bundles|the free-proper-action theorem]] the action is proper and $\pi\colon S^{2n+1}\to S^{2n+1}/U(1)=\mathbb{CP}^n$ is a principal $U(1)$-bundle. Two points $z,z'\in S^{2n+1}$ have $[z]=[z']$ if and only if $z'=z\lambda$ for some $\lambda\in U(1)$.

![[Def - Associated Bundle#The Definition]]

For a principal $G$-bundle $\pi\colon P\to M$ and a representation $\rho\colon G\to GL(V)$, the [[Def - Associated Bundle|associated bundle]] $P\times_\rho V$ is the quotient of $P\times V$ by $(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$, with classes $[p,v]$. Its fibre over $m=\pi(p)$ is a vector space under $[p,v]+[p,v']=[p,v+v']$ and $c[p,v]=[p,cv]$ (common representative $p$). A local section $s\in\Gamma(U;P)$ gives the local trivialisation $(m,v)\mapsto[s(m),v]$, so $P\times_\rho V$ is a smooth vector bundle of rank $\dim V$; when $V=\mathbb{C}$ and $\rho$ is complex-linear it is a complex line bundle.

![[Def - Complex Vector Bundle and Hermitian Structure#The Definition]]

A **complex line bundle** over $M$ is a fibre bundle with fibre $\mathbb{C}$ whose local trivialisations are fibrewise $\mathbb{C}$-linear and whose transition functions take values in $GL_1(\mathbb{C})=\mathbb{C}^\times$; equivalently a complex vector bundle of rank one. An **isomorphism of complex line bundles** over $M$ is a smooth fibre-preserving map covering $\mathrm{id}_M$ that is a $\mathbb{C}$-linear isomorphism on each fibre.

---

# Convergent Strategy

**Problem class.** This is an *identify-and-verify* problem with a preliminary *reverse-engineering* step. First one must decide *which* representation of $U(1)$ makes the natural-looking formula $[z,w]\mapsto([z],wz)$ consistent — this is where the difficulty of the exercise sits, and it is why the problem is more than routine. Then, with the representation pinned down, one checks the four clauses of a line-bundle isomorphism, exactly as in the endomorphism-bundle exercise [[Ex - End(E) as an Associated Bundle of the Frame Bundle]].

**Assumption pattern.** The governing constraint is the associated-bundle quotient relation. Under the series convention, replacing the representative $(z,w)$ by $(z\lambda,\varrho_m(\lambda^{-1})w)=(z\lambda,\lambda^{-m}w)$ must not change the value of the map. Applying the formula to both representatives produces $wz$ from the first and $\lambda^{-m}w\cdot z\lambda=\lambda^{1-m}wz$ from the second; equality for all $\lambda\in U(1)$ forces $\lambda^{1-m}\equiv1$, i.e. $m=1$. So the exponent of the representation is *read off* from the requirement that the fibre coordinate $w$ and the scaling of the sphere point $z$ cancel. This is the same variance bookkeeping as in every associated bundle: the $\rho(g^{-1})$ in the action is what has to be absorbed by the geometric map.

**Theorem routing.** The route is: (1) compute the two representatives' images and solve $\lambda^{1-m}=1$ for $m$, giving $\varrho_1$; (2) with $\varrho_1$, verify well-definedness as a one-line cancellation; (3) observe $\Phi$ covers $\mathrm{id}_{\mathbb{CP}^n}$ and lands in $\mathcal{O}(-1)$ because $wz\in\mathbb{C}z=[z]$; (4) fix a representative $z$ over a point $\ell=[z]$ to see the fibre map is $w\mapsto wz$, the linear isomorphism $\mathbb{C}\xrightarrow{\sim}\ell$; (5) trivialise both bundles over the standard chart $U_i=\{[z]:z_i\ne0\}$ using an explicit smooth local section of the Hopf bundle, where $\Phi$ becomes $(m,w)\mapsto(m,c_i(m)w)$ with $c_i$ smooth and nowhere zero, settling smoothness of $\Phi$ and $\Phi^{-1}$.

**Key decision point.** Two non-obvious moves. First, *treating the exponent $m$ as an unknown to be solved for* rather than guessing: the phrase "$S^{2n+1}\times_{U(1)}\mathbb{C}$" hides the representation, and the exercise is exactly to recover it — the discipline is to write the quotient relation and demand consistency. Second, *choosing the norm-one representative $s_i([z])=\frac{\overline{z_i}}{|z_i|}\frac{z}{|z|}$ as the local section*: this particular section is smooth, lands in $S^{2n+1}$, and has a nowhere-vanishing $i$-th coordinate, which is what makes the trivialisation of $\mathcal{O}(-1)$ (project onto the $i$-th coordinate of $w$) compose with $\Phi$ into a nonvanishing scalar multiplication.

---

# Legal Operations Used

This solution deploys the following operations, in the numbering of the topic page's Legal Operations:

1. **Reverse-engineer a representation from a well-definedness demand** (operation 5 from the topic page). The exponent of $\varrho_m$ is not given; it is determined by requiring the geometric formula to be constant on quotient classes, which yields a single equation $\lambda^{1-m}=1$.

2. **Verify a map on classes against the quotient relation** (operation 5 from the topic page). Once $\varrho_1$ is fixed, well-definedness is the cancellation $(z\lambda,\lambda^{-1}w)\mapsto\lambda^{-1}w\cdot z\lambda=wz$.

3. **Read the tautological fibre as the line spanned by a sphere point** (operation 3 from the topic page). Over $\ell=[z]$ the fibre of $\mathcal{O}(-1)$ is the line $\mathbb{C}z$, and $w\mapsto wz$ is the isomorphism $\mathbb{C}\xrightarrow{\sim}\mathbb{C}z$.

4. **Trivialise an associated bundle from a local section of the principal bundle** (operation 6 from the topic page). The explicit sections $s_i$ of the Hopf bundle over the charts $U_i$ trivialise $S^{2n+1}\times_{\varrho_1}\mathbb{C}$.

5. **Compute a bundle map in matched trivialisations to read off smoothness** (operation 7 from the topic page). In the chart $U_i$, both bundles are trivialised and $\Phi$ becomes multiplication by the smooth nowhere-zero function $c_i([z])=|z_i|/|z|$.

---

# Hints

> [!note]- Hint 1
> Do not assume the representation. Write it as $\varrho_m(\lambda)w=\lambda^m w$ with $m$ unknown. The associated-bundle relation replaces $(z,w)$ by $(z\lambda,\varrho_m(\lambda^{-1})w)=(z\lambda,\lambda^{-m}w)$. Apply the proposed formula $[z,w]\mapsto([z],wz)$ to this second representative and demand the same output.

> [!note]- Hint 2
> The second representative gives $([z\lambda],\lambda^{-m}w\cdot z\lambda)=([z],\lambda^{1-m}wz)$, using $[z\lambda]=[z]$. For this to equal $([z],wz)$ for *all* $\lambda\in U(1)$, you need $\lambda^{1-m}=1$ identically. Which integer $m$ does that force?

> [!note]- Hint 3
> With $m=1$: check that $\Phi$ is fibre-preserving ($\Phi[z,w]$ projects to $[z]$) and that $wz$ really lies in the fibre of $\mathcal{O}(-1)$ over $[z]$, namely the line $\mathbb{C}z$. Then fix one $z$ over $\ell=[z]$ and note that $w\mapsto wz$ is a $\mathbb{C}$-linear bijection $\mathbb{C}\to\mathbb{C}z=\ell$ (because $z\ne0$).

> [!note]- Hint 4
> For smoothness work over $U_i=\{[z]:z_i\ne0\}$. A smooth section of the Hopf bundle there is $s_i([z])=\frac{\overline{z_i}}{|z_i|}\cdot\frac{z}{|z|}$ (check: norm one, projects to $[z]$, independent of the homogeneous representative). Trivialise $\mathcal{O}(-1)$ over $U_i$ by $(\ell,u)\mapsto u_i$ (the $i$-th coordinate of $u\in\ell$). Compose with $\Phi$ and watch a nowhere-zero smooth factor appear.

---

# Solution

The exercise has a reverse-engineering half and a verification half. The representation is not handed to us inside the symbol $S^{2n+1}\times_{U(1)}\mathbb{C}$; it is recovered by demanding that the natural formula $[z,w]\mapsto([z],wz)$ respect the associated-bundle quotient, which forces the standard representation $\varrho_1$. With $\varrho_1$ fixed, the map covers the identity and lands in the tautological line because $wz$ spans the same line as $z$; it is fibrewise the isomorphism $\mathbb{C}\xrightarrow{\sim}\mathbb{C}z$; and it is smooth with smooth inverse because, in the standard chart trivialised by an explicit section of the Hopf bundle, it is multiplication by the smooth nowhere-zero function $|z_i|/|z|$.

**Step 0: The two fibres over a point $\ell=[z]\in\mathbb{CP}^n$.**

We record the two fibres to be matched, so that "fibre-preserving" and "$\mathbb{C}$-linear on fibres" are precise.

> [!note]- Derivation
> On the left, a point of $S^{2n+1}\times_{\varrho_1}\mathbb{C}$ over $\ell=[z]$ is a class $[z,w]$ with $z\in S^{2n+1}$, $\pi(z)=\ell$, and $w\in\mathbb{C}$, subject to
> $$[z,w]=[z\lambda,\lambda^{-1}w]\qquad(\lambda\in U(1)),$$
> the associated-bundle relation for $\varrho_1$. The fibre over $\ell$ is a complex vector space with $[z,w]+[z,w']=[z,w+w']$ and $c[z,w]=[z,cw]$ (common representative $z$), so it is one-dimensional over $\mathbb{C}$.
>
> On the right, the fibre of $\mathcal{O}(-1)$ over $\ell$ is the line $\ell=\mathbb{C}z\subseteq\mathbb{C}^{n+1}$, a one-dimensional complex subspace.
>
> For $w\in\mathbb{C}$ and $z\in S^{2n+1}$ with $\pi(z)=\ell$, the vector $wz\in\mathbb{C}^{n+1}$ lies in $\mathbb{C}z=\ell$, so $([z],wz)\in\mathcal{O}(-1)$: the formula lands in the correct fibre once we know (Step 1) it does not depend on the representative.

**Step 1: The representation is forced to be $\varrho_1$, and then $\Phi$ is well defined.**

Testing the formula against the quotient relation for the general representation $\varrho_m$ yields the single equation $\lambda^{1-m}=1$, forcing $m=1$; with $m=1$ the value $wz$ is representative-independent.

> [!note]- Derivation
> Consider the candidate representation $\varrho_m(\lambda)w=\lambda^m w$, $m\in\mathbb{Z}$, with associated-bundle action $(z,w)\cdot\lambda=(z\lambda,\varrho_m(\lambda^{-1})w)=(z\lambda,\lambda^{-m}w)$. Apply the formula $[z,w]\mapsto([z],wz)$ to the two representatives $(z,w)$ and $(z\lambda,\lambda^{-m}w)$ of the same class:
> $$(z,w)\ \longmapsto\ ([z],\,wz),$$
> $$(z\lambda,\lambda^{-m}w)\ \longmapsto\ \big([z\lambda],\,(\lambda^{-m}w)(z\lambda)\big)=\big([z],\,\lambda^{-m}\lambda\,wz\big)=\big([z],\,\lambda^{1-m}wz\big),$$
> where $[z\lambda]=[z]$ because $z$ and $z\lambda$ span the same complex line (definition of $\mathbb{CP}^n$), and scalars in $\mathbb{C}$ commute. For the formula to descend to the quotient, these two outputs must agree for every $\lambda\in U(1)$ and every $z,w$; taking $z\ne0$ and $w\ne0$ and cancelling the nonzero vector $wz$ leaves
> $$\lambda^{1-m}=1\qquad\text{for all }\lambda\in U(1).$$
> Since $U(1)$ contains elements of infinite order (e.g. $\lambda=e^{i}$, whose powers are dense), $\lambda^{1-m}=1$ for all $\lambda$ forces the exponent to vanish: $1-m=0$, i.e. $m=1$. Thus **the unique representation for which the formula is consistent is the standard representation $\varrho_1(\lambda)w=\lambda w$**, which is why the bundle is $S^{2n+1}\times_{\varrho_1}\mathbb{C}$.
>
> With $m=1$ the computation above reads $[z\lambda,\lambda^{-1}w]\mapsto([z],\lambda^{1-1}wz)=([z],wz)$, identical to the image of $[z,w]$. Hence $\Phi([z,w]):=([z],wz)$ is independent of the representative and is a genuine map on classes.

**Step 2: $\Phi$ is fibre-preserving and, on each fibre, a $\mathbb{C}$-linear isomorphism.**

$\Phi$ covers $\mathrm{id}_{\mathbb{CP}^n}$, and over $\ell=[z]$ it is the isomorphism $w\mapsto wz$ from $\mathbb{C}$ onto the line $\mathbb{C}z=\ell$.

> [!note]- Derivation
> *Fibre-preserving.* The projection of $S^{2n+1}\times_{\varrho_1}\mathbb{C}$ sends $[z,w]$ to $\pi(z)=[z]$, and $\operatorname{pr}(\Phi[z,w])=\operatorname{pr}([z],wz)=[z]$. So $\Phi$ commutes with the two projections and covers the identity of $\mathbb{CP}^n$.
>
> *Linear on fibres.* Fix $\ell\in\mathbb{CP}^n$ and a representative $z\in S^{2n+1}$ with $\pi(z)=\ell$. Every class in the left fibre over $\ell$ is $[z,w]$ for a unique $w\in\mathbb{C}$: existence because any representative $(z',w')$ over $\ell$ has $z'=z\lambda$ for some $\lambda\in U(1)$, so $[z',w']=[z\lambda,w']=[z,\lambda w']$; uniqueness because $[z,w]=[z,w'']$ means $(z,w'')=(z\lambda,\lambda^{-1}w)$ for some $\lambda$, and $z\lambda=z$ forces $\lambda=1$ (freeness of the $U(1)$-action), hence $w''=w$. Under the resulting $\mathbb{C}$-linear identification $w\leftrightarrow[z,w]$ of the fibre with $\mathbb{C}$, the map $\Phi$ becomes
> $$w\ \longmapsto\ wz\in\mathbb{C}z=\ell.$$
> This map $\mathbb{C}\to\ell$ is $\mathbb{C}$-linear — $(w+w')z=wz+w'z$ and $(cw)z=c(wz)$ — and bijective: $z\ne0$ spans the one-dimensional space $\ell$, so every $u\in\ell$ is $u=wz$ for exactly one $w\in\mathbb{C}$ (its coordinate with respect to the basis $\{z\}$ of $\ell$). Hence $\Phi$ is a $\mathbb{C}$-linear isomorphism on each fibre. Its inverse on the fibre is $u\mapsto[z,w]$ where $u=wz$.

**Step 3: $\Phi$ and $\Phi^{-1}$ are smooth.**

Over each standard chart $U_i$, an explicit section of the Hopf bundle trivialises the associated bundle, projection onto the $i$-th coordinate trivialises $\mathcal{O}(-1)$, and $\Phi$ becomes multiplication by a smooth nowhere-vanishing function.

> [!note]- Derivation
> Fix $i\in\{0,\dots,n\}$ and let $U_i=\{[z]\in\mathbb{CP}^n:z_i\ne0\}$, an open set covering $\mathbb{CP}^n$ as $i$ varies.
>
> *A smooth section of the Hopf bundle over $U_i$.* Define
> $$s_i\colon U_i\to S^{2n+1},\qquad s_i([z])=\frac{\overline{z_i}}{|z_i|}\cdot\frac{z}{|z|},\qquad |z|:=\Big(\textstyle\sum_j|z_j|^2\Big)^{1/2}.$$
> This is well defined on $U_i$ (independent of the homogeneous representative): replacing $z$ by $z\mu$, $\mu\in\mathbb{C}^\times$, gives $\frac{\overline{z_i\mu}}{|z_i\mu|}\frac{z\mu}{|z\mu|}=\frac{\overline{\mu}\mu}{|\mu|^2}\,\frac{\overline{z_i}}{|z_i|}\frac{z}{|z|}=\frac{|\mu|^2}{|\mu|^2}s_i([z])=s_i([z])$. It has norm one, $|s_i([z])|=\frac{|z_i|}{|z_i|}\cdot\frac{|z|}{|z|}=1$, so it lands in $S^{2n+1}$; and $\pi(s_i([z]))=[z]$ since $s_i([z])$ is a nonzero scalar multiple of $z$. All operations ($z\mapsto\overline{z_i}$, division by the nonvanishing $|z_i|$ and $|z|$) are smooth on $U_i$, so $s_i$ is smooth. Thus $s_i$ is a smooth local section of the Hopf bundle over $U_i$.
>
> *Chart on the left.* By the [[Def - Associated Bundle|associated-bundle]] construction, $s_i$ gives the trivialisation
> $$\alpha_i\colon U_i\times\mathbb{C}\to\big(S^{2n+1}\times_{\varrho_1}\mathbb{C}\big)\big|_{U_i},\qquad ([z],w)\mapsto[s_i([z]),w],$$
> a diffeomorphism onto the restricted bundle.
>
> *Chart on the right.* Trivialise $\mathcal{O}(-1)$ over $U_i$ by extracting the $i$-th coordinate:
> $$\beta_i\colon\mathcal{O}(-1)|_{U_i}\to U_i\times\mathbb{C},\qquad (\ell,u)\mapsto([\,\ell\,],u_i),$$
> where $u_i$ is the $i$-th component of $u\in\mathbb{C}^{n+1}$. This is a $\mathbb{C}$-linear isomorphism on each fibre: over $\ell=[z]$ with $z_i\ne0$, a vector $u\in\ell=\mathbb{C}z$ is $u=cz$, so $u_i=cz_i$ determines $c=u_i/z_i$ and hence $u$; the inverse $\beta_i^{-1}([z],t)=([z],\frac{t}{z_i}z)$ is smooth in $([z],t)$ on $U_i\times\mathbb{C}$. Both $\beta_i$ and $\beta_i^{-1}$ are smooth (coordinate projection and multiplication by the smooth nonvanishing $z_i^{-1}$), so $\beta_i$ is a smooth trivialisation.
>
> *Compute $\Phi$ in the matched charts.* For $([z],w)\in U_i\times\mathbb{C}$,
> $$\beta_i\circ\Phi\circ\alpha_i\,([z],w)=\beta_i\big(\Phi[s_i([z]),w]\big)=\beta_i\big([z],\,w\,s_i([z])\big)\qquad\text{(definitions of }\alpha_i,\ \Phi\text{)}$$
> $$=\Big([z],\ w\,\big(s_i([z])\big)_i\Big)\qquad\text{(definition of }\beta_i\text{: take the }i\text{-th coordinate).}$$
> The $i$-th coordinate of the section is
> $$\big(s_i([z])\big)_i=\frac{\overline{z_i}}{|z_i|}\cdot\frac{z_i}{|z|}=\frac{|z_i|^2}{|z_i|\,|z|}=\frac{|z_i|}{|z|}=:c_i([z]),$$
> a real, strictly positive, smooth function on $U_i$ (well defined there: invariant under $z\mapsto z\mu$). Therefore
> $$\beta_i\circ\Phi\circ\alpha_i\,([z],w)=\big([z],\,c_i([z])\,w\big),$$
> which is smooth in $([z],w)$ and, since $c_i>0$ is nowhere zero, is a diffeomorphism of $U_i\times\mathbb{C}$ with inverse $([z],t)\mapsto([z],t/c_i([z]))$. Consequently $\Phi=\beta_i^{-1}\circ(\text{mult. by }c_i)\circ\alpha_i^{-1}$ is a smooth vector-bundle isomorphism over $U_i$, and so is $\Phi^{-1}$. As the $U_i$ cover $\mathbb{CP}^n$, both $\Phi$ and $\Phi^{-1}$ are smooth.
>
> Combining Steps 1–3: $\Phi$ is well defined, covers $\mathrm{id}_{\mathbb{CP}^n}$, is $\mathbb{C}$-linear and bijective on each fibre, and is smooth with smooth inverse. Hence $\Phi$ is an isomorphism of complex line bundles, and
> $$S^{2n+1}\times_{U(1)}\mathbb{C}\ \cong\ \mathcal{O}(-1).$$

> [!note]- Complete formal solution
> **Claim.** With $\varrho_1(\lambda)w=\lambda w$, the map $\Phi([z,w])=([z],wz)$ is a smooth isomorphism of complex line bundles $S^{2n+1}\times_{\varrho_1}\mathbb{C}\xrightarrow{\ \sim\ }\mathcal{O}(-1)$ over $\mathbb{CP}^n$, and $\varrho_1$ is the only $\varrho_m$ for which the formula descends to the quotient.
>
> *Representation.* For $\varrho_m$, the class relation identifies $(z,w)$ with $(z\lambda,\lambda^{-m}w)$; the formula sends these to $([z],wz)$ and $([z],\lambda^{1-m}wz)$ respectively (using $[z\lambda]=[z]$). Agreement for all $\lambda\in U(1)$ forces $\lambda^{1-m}=1$ identically, hence $m=1$. With $m=1$, $[z\lambda,\lambda^{-1}w]\mapsto([z],wz)=\Phi([z,w])$, so $\Phi$ is well defined.
>
> *Fibrewise isomorphism.* $\operatorname{pr}\circ\Phi=\pi$-projection, so $\Phi$ covers $\mathrm{id}$. Over $\ell=[z]$, every class is $[z,w]$ for a unique $w$ (transitivity and freeness of the $U(1)$-action), and $w\mapsto wz$ is a $\mathbb{C}$-linear bijection $\mathbb{C}\to\mathbb{C}z=\ell$ since $z\ne0$ spans $\ell$.
>
> *Smoothness.* Over $U_i=\{z_i\ne0\}$ take the smooth Hopf section $s_i([z])=\frac{\overline{z_i}}{|z_i|}\frac{z}{|z|}$ (norm one, projects to $[z]$, representative-independent). Trivialise the left bundle by $\alpha_i([z],w)=[s_i([z]),w]$ and $\mathcal{O}(-1)$ by $\beta_i(\ell,u)=(\ell,u_i)$. Then $\beta_i\Phi\alpha_i([z],w)=([z],c_i([z])w)$ with $c_i([z])=|z_i|/|z|>0$ smooth, so $\Phi$ and $\Phi^{-1}$ are smooth over each $U_i$, hence globally.
>
> Therefore $\Phi$ is an isomorphism of complex line bundles and $S^{2n+1}\times_{U(1)}\mathbb{C}\cong\mathcal{O}(-1)$. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> One is tempted to skip Step 1 and simply *assert* that $S^{2n+1}\times_{U(1)}\mathbb{C}$ uses "the standard representation" and that $[z,w]\mapsto wz$ "obviously works". But the map $[z,w]\mapsto([z],wz)$ is well defined *only* for the exponent $m=1$; for the conjugate representation $\varrho_{-1}(\lambda)w=\overline{\lambda}w=\lambda^{-1}w$ the same formula sends $(z\lambda,\lambda w)\mapsto([z],\lambda^2 wz)\ne([z],wz)$, so it does not descend, and $S^{2n+1}\times_{\varrho_{-1}}\mathbb{C}\cong\mathcal{O}(1)=\mathcal{O}(-1)^*$ instead. Getting the isomorphism right therefore *requires* the exponent computation; omitting it is not a harmless economy but the difference between $\mathcal{O}(-1)$ and its dual.

---

# Key Takeaways

**When an associated bundle is written $P\times_G V$ with the representation suppressed, recover the representation by demanding that the intended geometric map respect the quotient.** The whole difficulty of this exercise is that "$S^{2n+1}\times_{U(1)}\mathbb{C}$" does not display which $\varrho_m$ is meant, and the answer is fixed by the target: the tautological map $[z,w]\mapsto([z],wz)$ descends to the quotient only when the scaling $\lambda^{-m}$ of the fibre coordinate cancels the scaling $\lambda$ of the sphere point, i.e. when $m=1$. The transferable diagnostic: given a candidate isomorphism from an associated bundle, substitute the quotient relation $(p,v)\mapsto(pg,\rho(g^{-1})v)$ and collect the powers of $g$; the requirement that they cancel is a single equation that pins down the representation. This is the reverse of the [[Ex - End(E) as an Associated Bundle of the Frame Bundle|endomorphism-bundle exercise]], where the representation was given and only the cancellation was checked; here the cancellation *is* the definition of the representation.

**The tautological line bundle is the geometric incarnation of the Hopf bundle's defining representation, and its dual flips the exponent.** The identification $\mathcal{O}(-1)\cong S^{2n+1}\times_{\varrho_1}\mathbb{C}$ says that the "line remembered over each point of $\mathbb{CP}^n$" is exactly the complex line associated to the standard character of $U(1)$. This is the base case of a whole ladder: $\mathcal{O}(k):=\mathcal{O}(-1)^{\otimes(-k)}$ is associated to $\varrho_{-k}$, so $\mathcal{O}(1)=\mathcal{O}(-1)^*\cong S^{2n+1}\times_{\varrho_{-1}}\mathbb{C}$ and, more generally, tensoring line bundles corresponds to adding characters of $U(1)$. The trigger to recall this: any $U(1)$-bundle whose base is projective space carries a canonical family of line bundles indexed by $\mathbb{Z}=\{\text{characters of }U(1)\}$, and the tautological one sits at $-1$ by the sign convention $\int_{\mathbb{CP}^1}c_1(\mathcal{O}(-1))=-1$ used throughout the series. Getting the exponent right is what later makes the first Chern number come out with the correct sign.

**Smoothness of a map of associated bundles is settled by trivialising with an explicit local section of the principal bundle, which also exposes the transition functions.** The efficient route to smoothness — used in Step 3 — is never to fight the quotient directly but to pick a concrete smooth local section (here the Hopf section $s_i([z])=\frac{\overline{z_i}}{|z_i|}\frac{z}{|z|}$), trivialise both bundles over the same chart, and watch the map become multiplication by a smooth nowhere-zero scalar. The same computation hands over the transition functions of $\mathcal{O}(-1)$: comparing the sections $s_i$ and $s_j$ over $U_i\cap U_j$ gives $s_j=s_i\cdot g_{ij}$ with $g_{ij}([z])=\frac{\overline{z_j}|z_i|}{\overline{z_i}|z_j|}$ valued in $U(1)$, so $\mathcal{O}(-1)$ has cocycle $\{g_{ij}\}$, the object whose first Chern class is computed in [[Ex - The Tautological Bundle over CP^1 has Degree Minus One]]. The reusable principle: an explicit section does triple duty — it proves smoothness, it reveals the transition functions, and it makes the characteristic-class computation concrete.
