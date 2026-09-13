---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Sphere Bundles and Mapping Tori"
  - "Thm - Orbit-Stabilizer for Lie Group Actions"
  - "Def - Smooth Action of a Lie Group"
tags: [geometry, gauge-theory, fibre-bundles, homogeneous-spaces, SO3]
---

# Problem Statement

The unit tangent bundle of the round two-sphere is a compact three-manifold; the exercise is to name it. Write
$$S(TS^{2})=\{(x,v)\in\mathbb{R}^{3}\times\mathbb{R}^{3}:\ \lvert x\rvert=1,\ \lvert v\rvert=1,\ \langle x,v\rangle=0\}$$
for the unit tangent bundle of $S^{2}\subset\mathbb{R}^{3}$ with its round metric, where we have used $T_{x}S^{2}=x^{\perp}=\{v\in\mathbb{R}^{3}:\langle x,v\rangle=0\}$, and let $\pi\colon S(TS^{2})\to S^{2}$, $\pi(x,v)=x$, be the bundle projection (the foot-point map). Let
$$SO(3)=\{g\in\mathrm{GL}(3,\mathbb{R}):\ g^{\top}g=I,\ \det g=1\}$$
act on $S(TS^{2})$ on the left by $g\cdot(x,v)=(gx,gv)$.

**Show:**

**(a)** the action is a well-defined smooth left action of $SO(3)$ on $S(TS^{2})$, it is **transitive**, and the stabiliser of the basepoint $p_{0}=(e_{3},e_{1})$ is **trivial**, $SO(3)_{p_{0}}=\{I\}$, where $e_{1},e_{2},e_{3}$ is the standard basis of $\mathbb{R}^{3}$;

**(b)** consequently, by the orbit–stabiliser theorem, the orbit map $\theta\colon SO(3)\to S(TS^{2})$, $\theta(g)=(ge_{3},ge_{1})$, is an $SO(3)$-equivariant **diffeomorphism**, so $S(TS^{2})\cong SO(3)$;

**(c)** under this diffeomorphism the bundle projection $\pi$ becomes the map $g\mapsto ge_{3}$, that is, the quotient map $SO(3)\to SO(3)/SO(2)=S^{2}$.

> [!warning] Convention: left actions for group actions on manifolds
> Throughout this series a Lie group acts on a principal bundle on the *right*, but a Lie group acting on an ordinary manifold acts on the *left*; here $SO(3)$ acts on the manifold $S(TS^{2})$ on the left, $g_{1}\cdot(g_{2}\cdot(x,v))=(g_{1}g_{2})\cdot(x,v)$. The orbit–stabiliser theorem below is stated for a transitive smooth left action, matching this setup.

**Recall:**

The unit tangent bundle is the unit sphere bundle of $TS^{2}$; the general construction and its manifold structure are the following.

![[Def - Sphere Bundles and Mapping Tori#The unit sphere bundle]]

A **[[Def - Smooth Action of a Lie Group|smooth left action]]** of a Lie group $G$ on a manifold $M$ is a smooth map $G\times M\to M$, $(g,m)\mapsto g\cdot m$, with $e\cdot m=m$ and $g_{1}\cdot(g_{2}\cdot m)=(g_{1}g_{2})\cdot m$; it is **transitive** if for all $m,m'\in M$ there is $g$ with $g\cdot m=m'$, and the **stabiliser** of $m$ is the closed subgroup $G_{m}=\{g\in G:g\cdot m=m\}$. The decisive tool is the smooth orbit–stabiliser theorem.

![[Thm - Orbit-Stabilizer for Lie Group Actions#Statement]]

We will apply it with $G=SO(3)$, $M=S(TS^{2})$, and $p=p_{0}=(e_{3},e_{1})$. That $SO(3)$ is a compact three-dimensional Lie group — a closed subgroup of $\mathrm{GL}(3,\mathbb{R})$ — is established in [[Ex - The Orthogonal Group as a Regular Level Set|the orthogonal group as a regular level set]]; that $S(TS^{2})$ is a smooth manifold (a fibre bundle over $S^{2}$ with fibre $S^{1}$) is part of the unit-sphere-bundle construction recalled above.

---

# Convergent Strategy

**Problem class.** This is an *identification* problem: a manifold $M=S(TS^{2})$ arrives with no group structure, and we must recognise it as a known homogeneous space $G/H$. The universal method is to find a Lie group $G$ that acts on $M$ transitively, compute the stabiliser $H$ of one convenient point, and invoke the orbit–stabiliser theorem to conclude $M\cong G/H$. When the stabiliser turns out to be trivial, the conclusion sharpens to $M\cong G$ outright.

**Assumption pattern.** The manifold is a set of *orthonormal configurations* in $\mathbb{R}^{3}$: a point $(x,v)\in S(TS^{2})$ is an orthonormal pair, and $SO(3)$ is exactly the group of rigid rotations that permutes such configurations. This is the recurring signature "$M$ is the space of frames/flags/configurations of a fixed linear-algebraic type" that flags $M$ as a Stiefel-type homogeneous space of an orthogonal or unitary group. The orthonormal pair $(x,v)$ can be completed by $x\times v$ to a positively oriented orthonormal basis of $\mathbb{R}^{3}$, i.e. to an element of $SO(3)$ — the observation that turns transitivity and triviality of the stabiliser into one-line linear algebra.

**Theorem routing.** The engine is the smooth [[Thm - Orbit-Stabilizer for Lie Group Actions|orbit–stabiliser theorem]]: a transitive smooth action of $G$ on $M$ with stabiliser $G_{p}$ gives an equivariant diffeomorphism $G/G_{p}\cong M$. The route is: (i) verify the action is well defined (rotations preserve norms and orthogonality) and smooth (it is the restriction of a linear action); (ii) prove transitivity by the complete-to-a-frame construction; (iii) compute $SO(3)_{p_{0}}$ by using the $SO(3)$-equivariance of the cross product, $g(a\times b)=(ga)\times(gb)$, to show that fixing $e_{3}$ and $e_{1}$ forces fixing $e_{2}=e_{3}\times e_{1}$, hence $g=I$; (iv) read off $SO(3)/\{I\}=SO(3)\cong S(TS^{2})$; (v) trace the projection $\pi$ through $\theta$ to get $g\mapsto ge_{3}$, the quotient $SO(3)\to SO(3)/SO(2)=S^{2}$ of [[Ex - S^2 as a Homogeneous Space of SO(3)|the sphere as a homogeneous space]].

**Key decision point.** Two choices carry the argument. First, the **basepoint**: choosing $p_{0}=(e_{3},e_{1})$ rather than, say, $(e_{1},e_{2})$ is what makes the projection $\pi$ turn into the standard map $g\mapsto ge_{3}$ and dovetail with the realisation $S^{2}=SO(3)/SO(2)$; a different basepoint gives an isomorphic answer with a conjugate stabiliser but obscures part (c). Second, the **completion trick**: given an orthonormal pair, appending its cross product produces a rotation matrix, and this both proves transitivity and supplies an explicit smooth inverse $(x,v)\mapsto[v\mid x\times v\mid x]$ of the orbit map — a self-contained confirmation that $\theta$ is a diffeomorphism, independent of the orbit–stabiliser machinery.

---

# Legal Operations Used

1. **Restrict a linear action to an invariant submanifold (operation: an isometric linear action descends to sphere and frame bundles).** The standard action of $SO(3)$ on $\mathbb{R}^{3}$ preserves the norm and the inner product, hence preserves the set of orthonormal pairs $S(TS^{2})$; restricting it there gives a smooth action without any further checking of smoothness, because the restriction of a smooth map to an embedded submanifold on which it is invariant is smooth.

2. **Complete an orthonormal $k$-frame to a full frame (operation: the cross product as the missing basis vector).** In $\mathbb{R}^{3}$ an orthonormal pair $(x,v)$ is completed to the positively oriented orthonormal basis $(v,\,x\times v,\,x)$; the matrix with these columns lies in $SO(3)$. This is the operation that realises configurations as group elements.

3. **Use equivariance of a natural operation to pin down a stabiliser (operation: cross-product equivariance).** Because $g\in SO(3)$ satisfies $g(a\times b)=(ga)\times(gb)$, a rotation fixing two basis vectors automatically fixes their cross product, forcing it to be the identity. Equivariance turns "fixes $e_{1}$ and $e_{3}$" into "fixes a basis".

4. **Invoke the orbit–stabiliser theorem (operation: transitive action $\Rightarrow$ homogeneous-space identification).** With transitivity and the stabiliser in hand, the [[Thm - Orbit-Stabilizer for Lie Group Actions|orbit–stabiliser theorem]] delivers the equivariant diffeomorphism $SO(3)/SO(3)_{p_{0}}\cong S(TS^{2})$ directly.

---

# Hints

> [!note]- Hint 1
> A point of $S(TS^{2})$ is a pair of unit vectors $(x,v)$ in $\mathbb{R}^{3}$ that are orthogonal. What natural group moves such pairs around while keeping them orthonormal?

> [!note]- Hint 2
> Given two orthonormal pairs, you want a single rotation carrying the first to the second. You are one vector short of a basis. Manufacture the third vector.

> [!note]- Hint 3
> For an orthonormal pair $(x,v)$, the triple $(v,\,x\times v,\,x)$ is an orthonormal basis. Check that the matrix $[v\mid x\times v\mid x]$ has determinant $+1$, so it lies in $SO(3)$, and see what it does to $e_{1},e_{2},e_{3}$.

> [!note]- Hint 4
> For the stabiliser of $(e_{3},e_{1})$: if $g$ fixes $e_{3}$ and $e_{1}$, what does it do to $e_{3}\times e_{1}$? Recall (and prove) that $g(a\times b)=(ga)\times(gb)$ for $g\in SO(3)$.

> [!note]- Hint 5
> Once the stabiliser is trivial, orbit–stabiliser gives $SO(3)/\{I\}=SO(3)\cong S(TS^{2})$. For part (c), compute $\pi(\theta(g))=\pi(ge_{3},ge_{1})$ and compare with the action of $SO(3)$ on $S^{2}$.

---

# Solution

**Plan.** We check that the rotation action restricts to $S(TS^{2})$ and is smooth, then prove transitivity and compute the stabiliser of $p_{0}=(e_{3},e_{1})$ by the complete-to-a-frame construction and cross-product equivariance. The orbit–stabiliser theorem then upgrades transitivity plus trivial stabiliser to the equivariant diffeomorphism $\theta\colon SO(3)\xrightarrow{\sim}S(TS^{2})$. Finally we trace the bundle projection through $\theta$ to identify it with $g\mapsto ge_{3}$, and confirm everything by exhibiting the explicit smooth inverse $(x,v)\mapsto[v\mid x\times v\mid x]$.

**Step 1: The action is well defined and smooth.**

> [!note]- Derivation
> Let $g\in SO(3)$ and $(x,v)\in S(TS^{2})$. Since $g$ is orthogonal, $\langle gu,gw\rangle=\langle u,w\rangle$ for all $u,w\in\mathbb{R}^{3}$. Therefore
> $$\lvert gx\rvert^{2}=\langle gx,gx\rangle=\langle x,x\rangle=1,\qquad \lvert gv\rvert^{2}=\langle v,v\rangle=1,\qquad \langle gx,gv\rangle=\langle x,v\rangle=0,$$
> each equality holding because $g$ is orthogonal and using $\lvert x\rvert=\lvert v\rvert=1$, $\langle x,v\rangle=0$. Hence $(gx,gv)\in S(TS^{2})$: the map $g\cdot(x,v)=(gx,gv)$ genuinely lands in $S(TS^{2})$ (operation 1). It is a **left action**: $I\cdot(x,v)=(x,v)$, and
> $$g_{1}\cdot\big(g_{2}\cdot(x,v)\big)=g_{1}\cdot(g_{2}x,g_{2}v)=(g_{1}g_{2}x,\,g_{1}g_{2}v)=(g_{1}g_{2})\cdot(x,v)\qquad\text{(associativity of matrix multiplication).}$$
> **Smoothness.** The map $SO(3)\times(\mathbb{R}^{3}\times\mathbb{R}^{3})\to\mathbb{R}^{3}\times\mathbb{R}^{3}$, $(g,(x,v))\mapsto(gx,gv)$, is polynomial in the entries of $g,x,v$, hence smooth; $S(TS^{2})$ is an embedded submanifold of $\mathbb{R}^{3}\times\mathbb{R}^{3}$ (the unit sphere bundle of $TS^{2}$, by the [[Def - Sphere Bundles and Mapping Tori|sphere-bundle construction]]) that the action preserves, so the corestriction $SO(3)\times S(TS^{2})\to S(TS^{2})$ is smooth. Thus we have a smooth left action.

**Step 2: A helper — cross-product equivariance of $SO(3)$.**

> [!note]- Derivation
> **Claim.** For all $g\in SO(3)$ and $a,b\in\mathbb{R}^{3}$, $\ g(a\times b)=(ga)\times(gb)$.
>
> **Proof.** For every $c\in\mathbb{R}^{3}$, the scalar triple product satisfies $\langle a\times b,c\rangle=\det[a\mid b\mid c]$ (the standard identity between the cross product and the determinant). Compute, for arbitrary $c$,
> $$\langle (ga)\times(gb),\,c\rangle=\det[ga\mid gb\mid c]=\det\!\big(g\,[a\mid b\mid g^{-1}c]\big)=\det(g)\,\det[a\mid b\mid g^{-1}c],$$
> where the middle equality writes $c=g(g^{-1}c)$ and factors $g$ out of all three columns, and the last is multiplicativity of the determinant. Since $\det g=1$ (as $g\in SO(3)$),
> $$\langle (ga)\times(gb),\,c\rangle=\det[a\mid b\mid g^{-1}c]=\langle a\times b,\,g^{-1}c\rangle=\langle g(a\times b),\,c\rangle,$$
> the last step because $g$ is orthogonal, so $\langle u,g^{-1}c\rangle=\langle gu,c\rangle$. As $c$ is arbitrary and the inner product is nondegenerate, $(ga)\times(gb)=g(a\times b)$. $\square$
>
> This is exactly the statement that the defining representation of $SO(3)$ carries the cross product to itself, and it is the content of [[Ex - The Adjoint Representation of SO(3) is the Defining Representation|the adjoint representation of SO(3) being the defining representation]].

**Step 3: The action is transitive.**

> [!note]- Derivation
> For an orthonormal pair $(x,v)\in S(TS^{2})$ set
> $$M(x,v):=[\,v\mid x\times v\mid x\,]\in\mathbb{R}^{3\times3}\qquad\text{(columns }v,\ x\times v,\ x\text{).}$$
> Its columns are orthonormal: $\lvert v\rvert=\lvert x\rvert=1$ and $\langle x,v\rangle=0$ by hypothesis, and $x\times v$ is orthogonal to both $x$ and $v$ with $\lvert x\times v\rvert=\lvert x\rvert\,\lvert v\rvert\sin(\pi/2)=1$. Hence $M(x,v)^{\top}M(x,v)=I$, so $M(x,v)\in O(3)$. Its determinant is computed from the scalar triple product $\det[a\mid b\mid c]=\langle a\times b,\,c\rangle$:
> $$\det[\,v\mid x\times v\mid x\,]=\langle\, v\times (x\times v),\ x\,\rangle,\qquad v\times(x\times v)=x\,\langle v,v\rangle-v\,\langle v,x\rangle=x,$$
> using the vector triple product $a\times(b\times c)=b\langle a,c\rangle-c\langle a,b\rangle$ with $a=v,b=x,c=v$ together with $\langle v,v\rangle=1$ and $\langle v,x\rangle=0$. Therefore $\det M(x,v)=\langle x,x\rangle=1$, so $M(x,v)\in SO(3)$. By construction the columns are the images of $e_{1},e_{2},e_{3}$:
> $$M(x,v)e_{1}=v,\qquad M(x,v)e_{2}=x\times v,\qquad M(x,v)e_{3}=x.$$
> Now let $(x,v),(x',v')\in S(TS^{2})$ be arbitrary and put $g:=M(x',v')\,M(x,v)^{-1}=M(x',v')\,M(x,v)^{\top}\in SO(3)$ (a product of two elements of $SO(3)$). Then, since $M(x,v)^{\top}=M(x,v)^{-1}$ sends $v\mapsto e_{1}$ and $x\mapsto e_{3}$,
> $$g\,x=M(x',v')\big(M(x,v)^{-1}x\big)=M(x',v')\,e_{3}=x',\qquad g\,v=M(x',v')\,e_{1}=v'.$$
> Hence $g\cdot(x,v)=(x',v')$, and the action is **transitive**.

**Step 4: The stabiliser of $p_{0}=(e_{3},e_{1})$ is trivial.**

> [!note]- Derivation
> First note $p_{0}=(e_{3},e_{1})\in S(TS^{2})$: $\lvert e_{3}\rvert=\lvert e_{1}\rvert=1$ and $\langle e_{3},e_{1}\rangle=0$. Let $g\in SO(3)_{p_{0}}$, so $g\cdot(e_{3},e_{1})=(e_{3},e_{1})$, that is
> $$g\,e_{3}=e_{3}\qquad\text{and}\qquad g\,e_{1}=e_{1}.$$
> By Step 2 (cross-product equivariance) and the standard relation $e_{3}\times e_{1}=e_{2}$,
> $$g\,e_{2}=g(e_{3}\times e_{1})=(g\,e_{3})\times(g\,e_{1})=e_{3}\times e_{1}=e_{2}.$$
> Thus $g$ fixes $e_{1},e_{2},e_{3}$; a linear map fixing a basis is the identity, so $g=I$. Conversely $I$ fixes $p_{0}$. Therefore $SO(3)_{p_{0}}=\{I\}$, the **trivial** subgroup. (The stabiliser is automatically closed, being $\theta^{-1}(\{p_{0}\})$ for the continuous orbit map, so the orbit–stabiliser hypotheses are met; here it is not merely closed but trivial.)

**Step 5: Orbit–stabiliser gives $S(TS^{2})\cong SO(3)$.**

> [!note]- Derivation
> By Steps 1, 3 and 4, $SO(3)$ acts smoothly and transitively on the smooth manifold $S(TS^{2})$ with stabiliser $SO(3)_{p_{0}}=\{I\}$ at $p_{0}=(e_{3},e_{1})$. Restating the [[Thm - Orbit-Stabilizer for Lie Group Actions|orbit–stabiliser theorem]]: *for a smooth transitive action of a Lie group $G$ on a manifold $M$ and any $p\in M$, the orbit map $\theta^{(p)}\colon G\to M$, $g\mapsto g\cdot p$, descends to a $G$-equivariant diffeomorphism $\bar\theta^{(p)}\colon G/G_{p}\xrightarrow{\sim}M$.* Here the orbit map is
> $$\theta:=\theta^{(p_{0})}\colon SO(3)\to S(TS^{2}),\qquad \theta(g)=g\cdot(e_{3},e_{1})=(g\,e_{3},\,g\,e_{1}),$$
> and $G/G_{p_{0}}=SO(3)/\{I\}=SO(3)$ with the quotient map $\pi_{\{I\}}\colon SO(3)\to SO(3)/\{I\}$ the identity. Therefore $\bar\theta^{(p_{0})}=\theta$ itself is an $SO(3)$-equivariant diffeomorphism
> $$\theta\colon SO(3)\ \xrightarrow{\ \sim\ }\ S(TS^{2}).$$
> The dimensions agree as a check: $\dim SO(3)=3$ and $\dim S(TS^{2})=\dim S^{2}+\dim S^{1}=2+1=3$, consistent with the corollary $\dim M=\dim G-\dim G_{p}=3-0=3$.

**Step 6: The projection becomes $g\mapsto ge_{3}$.**

> [!note]- Derivation
> Compose the bundle projection with the diffeomorphism $\theta$:
> $$(\pi\circ\theta)(g)=\pi(g\,e_{3},\,g\,e_{1})=g\,e_{3}\qquad\text{(the projection reads off the first, foot-point, factor).}$$
> So under the identification $S(TS^{2})\cong SO(3)$ the projection $\pi$ is the map $q\colon SO(3)\to S^{2}$, $q(g)=g\,e_{3}$. This $q$ is the orbit map of the transitive action of $SO(3)$ on $S^{2}$ (rotations act transitively on the unit sphere), and the stabiliser of $e_{3}\in S^{2}$ is $\{g\in SO(3):g\,e_{3}=e_{3}\}=SO(2)$, the group of rotations about the $e_{3}$-axis. By the orbit–stabiliser theorem applied to this second action, $q$ descends to a diffeomorphism $SO(3)/SO(2)\cong S^{2}$, exactly the realisation proved in [[Ex - S^2 as a Homogeneous Space of SO(3)|S² as a homogeneous space of SO(3)]]. Hence the unit-tangent-bundle projection $\pi\colon S(TS^{2})\to S^{2}$ is, after the identification, the principal $SO(2)$-bundle $SO(3)\to SO(3)/SO(2)=S^{2}$.

> [!note]- Complete formal solution
> **Well-defined smooth action.** For $g\in SO(3)$, $g$ preserves the inner product, so $\lvert gx\rvert=\lvert x\rvert$, $\lvert gv\rvert=\lvert v\rvert$, $\langle gx,gv\rangle=\langle x,v\rangle$; hence $(gx,gv)\in S(TS^{2})$ whenever $(x,v)\in S(TS^{2})$. The axioms $I\cdot(x,v)=(x,v)$ and $g_{1}\cdot(g_{2}\cdot(x,v))=(g_{1}g_{2})\cdot(x,v)$ hold by associativity of matrix multiplication. The map is a polynomial in the entries of $(g,x,v)$, so its restriction to the embedded invariant submanifold $S(TS^{2})$ is a smooth left action.
>
> **Cross-product equivariance.** For $g\in SO(3)$ and $a,b,c\in\mathbb{R}^{3}$: $\langle(ga)\times(gb),c\rangle=\det[ga\mid gb\mid c]=\det(g)\det[a\mid b\mid g^{-1}c]=\det[a\mid b\mid g^{-1}c]=\langle a\times b,g^{-1}c\rangle=\langle g(a\times b),c\rangle$, using $\langle a\times b,c\rangle=\det[a\mid b\mid c]$, $\det g=1$, and orthogonality of $g$. As $c$ is arbitrary, $g(a\times b)=(ga)\times(gb)$.
>
> **Transitivity.** For $(x,v)\in S(TS^{2})$ set $M(x,v)=[v\mid x\times v\mid x]$. Its columns are orthonormal (from $\lvert x\rvert=\lvert v\rvert=1$, $\langle x,v\rangle=0$, $x\times v\perp x,v$, $\lvert x\times v\rvert=1$), and $\det M(x,v)=\langle v\times(x\times v),x\rangle=\langle x,x\rangle=1$ by the triple-product identity $v\times(x\times v)=x\langle v,v\rangle-v\langle v,x\rangle=x$; so $M(x,v)\in SO(3)$, with $M(x,v)e_{1}=v$, $M(x,v)e_{2}=x\times v$, $M(x,v)e_{3}=x$. Given $(x,v),(x',v')$, the element $g=M(x',v')M(x,v)^{\top}\in SO(3)$ satisfies $gx=M(x',v')e_{3}=x'$ and $gv=M(x',v')e_{1}=v'$, so $g\cdot(x,v)=(x',v')$. The action is transitive.
>
> **Stabiliser.** $p_{0}=(e_{3},e_{1})\in S(TS^{2})$. If $g\in SO(3)$ fixes $p_{0}$ then $ge_{3}=e_{3}$, $ge_{1}=e_{1}$, whence $ge_{2}=g(e_{3}\times e_{1})=(ge_{3})\times(ge_{1})=e_{3}\times e_{1}=e_{2}$ by cross-product equivariance and $e_{3}\times e_{1}=e_{2}$. A rotation fixing the standard basis is $I$, so $SO(3)_{p_{0}}=\{I\}$.
>
> **Identification.** By the [[Thm - Orbit-Stabilizer for Lie Group Actions|orbit–stabiliser theorem]], the orbit map $\theta(g)=(ge_{3},ge_{1})$ descends to an $SO(3)$-equivariant diffeomorphism $SO(3)/SO(3)_{p_{0}}\to S(TS^{2})$; since $SO(3)_{p_{0}}=\{I\}$, the quotient is $SO(3)$ and $\theta\colon SO(3)\xrightarrow{\sim}S(TS^{2})$ is itself a diffeomorphism. Dimensions match: $3=\dim SO(3)=\dim S(TS^{2})=\dim S^{2}+\dim S^{1}$.
>
> **Projection.** $(\pi\circ\theta)(g)=\pi(ge_{3},ge_{1})=ge_{3}$. The map $g\mapsto ge_{3}$ is the quotient $SO(3)\to SO(3)/SO(2)=S^{2}$, with $SO(2)=\{g:ge_{3}=e_{3}\}$ the stabiliser of $e_{3}\in S^{2}$; by [[Ex - S^2 as a Homogeneous Space of SO(3)|orbit–stabiliser for the sphere]] this is a diffeomorphism onto $S^{2}$. Hence under $\theta$ the unit-tangent-bundle projection is the bundle $SO(3)\to SO(3)/SO(2)=S^{2}$. $\qquad\blacksquare$

> [!note]- Independent sanity check — the explicit smooth inverse (the frame viewpoint)
> Orbit–stabiliser proves $\theta$ is a diffeomorphism abstractly; here is the inverse in closed form, which reconfirms it by hand and exhibits the geometric content. Define
> $$\Phi\colon S(TS^{2})\to SO(3),\qquad \Phi(x,v)=[\,v\mid x\times v\mid x\,]=M(x,v).$$
> By Step 3, $\Phi(x,v)\in SO(3)$, and $\Phi$ is smooth (its entries are polynomials in $x,v$). Then, for all $g\in SO(3)$ and $(x,v)\in S(TS^{2})$,
> $$\Phi(\theta(g))=\Phi(ge_{3},ge_{1})=[\,ge_{1}\mid (ge_{3})\times(ge_{1})\mid ge_{3}\,]=[\,ge_{1}\mid g e_{2}\mid ge_{3}\,]=g,$$
> using cross-product equivariance and $e_{3}\times e_{1}=e_{2}$ in the middle column, and reading the three columns as $g$ applied to $e_{1},e_{2},e_{3}$; and
> $$\theta(\Phi(x,v))=\big(\Phi(x,v)\,e_{3},\ \Phi(x,v)\,e_{1}\big)=(x,v),$$
> since the third and first columns of $\Phi(x,v)$ are $x$ and $v$. So $\Phi=\theta^{-1}$, a smooth two-sided inverse: $\theta$ is a diffeomorphism, as claimed. Geometrically, $\Phi$ says that an orthonormal pair *is* a rotation matrix once one appends the cross product as the middle column — the unit tangent bundle of $S^{2}$ is the manifold of oriented orthonormal frames of $\mathbb{R}^{3}$, that is, $SO(3)$ itself.

> [!warning] Illegal but tempting shortcut — concluding $S(TS^{2})\cong SO(3)$ from a dimension count
> The equality $\dim S(TS^{2})=3=\dim SO(3)$, or even the coincidence that both are compact connected orientable $3$-manifolds, does **not** by itself give a diffeomorphism: $S^{3}$ and $SO(3)=\mathbb{RP}^{3}$ are both compact connected orientable $3$-manifolds of the same dimension yet are *not* diffeomorphic (they have different fundamental groups, $1$ versus $\mathbb{Z}/2$). Dimension and elementary invariants only *permit* a diffeomorphism; they never produce one. The genuine content is the transitive action with trivial stabiliser, which constructs the diffeomorphism explicitly. The extra ingredient that would upgrade a dimension count to an identification is exactly a transitive group action (or an explicit map with smooth inverse, as in the sanity check).

---

# Key Takeaways

**The space of orthonormal configurations of a fixed type is a homogeneous space of the relevant orthogonal group, and a trivial stabiliser identifies it with the group itself.** The unit tangent bundle $S(TS^{2})$ is the manifold of orthonormal $2$-frames $(x,v)$ in $\mathbb{R}^{3}$, and the completion $(x,v)\mapsto(v,x\times v,x)$ shows this is the manifold of full oriented orthonormal frames, i.e. $SO(3)$. The reusable principle is that a Stiefel manifold $V_{k}(\mathbb{R}^{n})$ of orthonormal $k$-frames is $SO(n)/SO(n-k)$ (with a trivial stabiliser exactly when $k=n-1$ or $k=n$, so that no freedom is left in the unspecified directions); here $n=3$, $k=2$, and $n-k=1$ gives $SO(1)=\{I\}$, hence $S(TS^{2})=V_{2}(\mathbb{R}^{3})\cong SO(3)$. The trigger to reach for this is "a manifold presented as the set of tuples of vectors subject to inner-product constraints"; the reaction is "let the isometry group act, complete to a frame, and read off the stabiliser".

**Equivariance of a natural algebraic operation is the clean way to compute a stabiliser.** Rather than solve the equations $ge_{3}=e_{3}$, $ge_{1}=e_{1}$ by brute force in the entries of $g$, we used that the cross product is $SO(3)$-equivariant, so fixing two vectors of a basis forces fixing the third and hence the whole rotation. The transferable diagnostic: whenever a stabiliser condition fixes some but not all of a generating set for the space, look for a natural equivariant operation (cross product, wedge, bracket, contraction, complex structure) that manufactures the remaining generators from the fixed ones — it collapses the stabiliser computation to a line. The same move computes the stabiliser of a flag, of a complex line, or of a symplectic pair.

**The identification is not just of manifolds but of bundles, and it exposes a chain of classical fibrations.** Tracing the projection through the diffeomorphism turned $\pi\colon S(TS^{2})\to S^{2}$ into the quotient $SO(3)\to SO(3)/SO(2)=S^{2}$, so the unit tangent bundle of the sphere *is* the principal circle bundle $SO(2)\hookrightarrow SO(3)\to S^{2}$. This places three facts on one page: $S(TS^{2})\cong SO(3)\cong\mathbb{RP}^{3}$ (rotations of $\mathbb{R}^{3}$ form real projective three-space); the two-to-one cover $SU(2)=S^{3}\to SO(3)$ from [[Ex - SU(2) is Diffeomorphic to S^3|the identification of SU(2) with S³]] realises $S^{3}$ as the double cover of the unit tangent bundle of $S^{2}$; and the whole tower sits below the Hopf fibration $S^{1}\hookrightarrow S^{3}\to S^{2}$, whose base circle action is the double cover of the $SO(2)$ here. The lesson for gauge theory is that the "unit tangent bundle of $S^{2}$" and "the frame bundle of $S^{2}$ reduced to $SO(2)$" and "the principal $SO(2)$-bundle $SO(3)\to S^{2}$" are three names for one object, and recognising a bundle as a coset space $G\to G/H$ is what makes its connections, curvature, and characteristic classes computable by the homogeneous-space methods of the later chapters. A natural companion is [[Ex - The Klein Bottle as a Mapping Torus]], where the twist that here vanishes (the bundle $S(TS^{2})$ is nontrivial as a circle bundle, with Euler number $\pm2$) is instead detected by non-orientability.
