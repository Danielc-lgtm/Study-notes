---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Thm - Pull-Back of Connections and Curvature"
  - "Def - The Hopf Bundle"
  - "Thm - The Standard Connection on the Hopf Bundle"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\pi_n\colon S^{2n+1}\to\mathbb{CP}^n$ be the **Hopf bundle** with its standard **Hopf connection**
$$a^{(n)}_z(u)=\langle v_n(z),u\rangle\,i,\qquad v_n(z)=iz,\quad u\in T_zS^{2n+1},$$
and let
$$\iota\colon\mathbb{CP}^1\hookrightarrow\mathbb{CP}^n,\qquad\iota([w_0:w_1])=[w_0:w_1:0:\cdots:0]$$
be the standard linear inclusion (the first rung of the ladder $\mathbb{CP}^1\subset\mathbb{CP}^2\subset\cdots\subset\mathbb{CP}^n$). Form the pull-back bundle $\iota^*S^{2n+1}\to\mathbb{CP}^1$ with the pull-back connection $\iota^*a^{(n)}=\hat\iota^{\,*}a^{(n)}$ furnished by [[Thm - Pull-Back of Connections and Curvature|the pull-back theorem]], where $\hat\iota\colon\iota^*S^{2n+1}\to S^{2n+1}$ is the canonical $U(1)$-equivariant map.

Prove that the pull-back of the Hopf bundle along $\iota$ is, connection and all, the Hopf bundle in one dimension lower:
$$\big(\iota^*S^{2n+1}\to\mathbb{CP}^1,\ \iota^*a^{(n)}\big)\ \cong\ \big(S^3\to\mathbb{CP}^1,\ a^{(1)}\big)$$
as principal $U(1)$-bundles with connection. Concretely, exhibit a $U(1)$-equivariant bundle isomorphism $\Psi\colon S^3\to\iota^*S^{2n+1}$ covering the identity of $\mathbb{CP}^1$ and show $\Psi^*(\iota^*a^{(n)})=a^{(1)}$; deduce $F_{a^{(1)}}=\iota^*F_{a^{(n)}}$.

**Recall:**

The objects in play are the Hopf bundle in dimensions $1$ and $n$, the pull-back of a principal bundle and its canonical equivariant map, and the pull-back of a connection with its curvature.

![[Def - The Hopf Bundle#The Definition]]

![[Thm - Pull-Back of Connections and Curvature#Statement]]

The **pull-back principal bundle** of $\pi\colon P\to M$ along $f\colon N\to M$ is
$$f^*P=\{(p,x)\in P\times N\mid \pi(p)=f(x)\},$$
with projection $\varpi(p,x)=x$, right $G$-action $(p,x)\cdot g=(pg,x)$, and canonical $G$-equivariant map $\hat f\colon f^*P\to P$, $\hat f(p,x)=p$, which covers $f$ in the sense $\pi\circ\hat f=f\circ\varpi$. For a connection $A$ on $P$, the pull-back connection is $f^*A:=\hat f^{\,*}A$, with curvature $F_{f^*A}=f^*F_A$.

Two facts from chapter I and chapter III are used. First, the Hopf connection form of Step 0 of [[Ex - The Induced Connection on the Tautological Bundle from the Hopf Connection|the tautological-bundle-connection exercise]] can be written as a Hermitian pairing, $a^{(n)}_z(u)=h(u,z)$, where $h(\zeta,\eta)=\sum_j\zeta_j\overline{\eta_j}$ is the standard Hermitian metric on $\mathbb{C}^{n+1}$; this is the cleanest form for pulling the connection back. Second, the ladder of inclusions $S^3\subset S^5\subset\cdots\subset S^{2n+1}$ covering $\mathbb{CP}^1\subset\cdots\subset\mathbb{CP}^n$ (the content of the remark on nested Hopf bundles) is realised by the equivariant inclusions $j\colon S^3\hookrightarrow S^{2n+1}$, $(z_0,z_1)\mapsto(z_0,z_1,0,\ldots,0)$.

---

# Convergent Strategy

**Problem class.** This is a *recognise-a-pulled-back-structure* problem: an abstract construction (pull-back of a bundle with connection) is applied to a concrete map, and the task is to identify the anonymous result with a bundle we already understand. The universal tool for such problems is the *universal property of the pull-back*: to name $f^*P$ it suffices to produce a $G$-equivariant bundle map into $P$ covering $f$, and such a map factors uniquely through $f^*P$.

**Assumption pattern.** The structural coincidence that makes the identification work is that the inclusion $\iota$ of base spaces is covered, upstairs, by a $U(1)$-equivariant inclusion $j\colon S^3\hookrightarrow S^{2n+1}$ of total spaces — the sphere $S^3$ of the first two coordinates sits inside $S^{2n+1}$ compatibly with the $U(1)$-actions and the projections. The recognisable trigger is that $\iota$ is a *linear* embedding of projective spaces, so it lifts to a linear (hence equivariant) embedding of the spheres.

**Theorem routing.** The route is: (i) verify $j$ is $U(1)$-equivariant and satisfies $\pi_n\circ j=\iota\circ\pi_1$; (ii) invoke the universal property of the pull-back to convert $j$ into a bundle map $\Psi\colon S^3\to\iota^*S^{2n+1}$, $\Psi(p)=(j(p),\pi_1(p))$, over $\mathrm{id}_{\mathbb{CP}^1}$; (iii) prove $\Psi$ is an isomorphism, using that a $U(1)$-equivariant morphism of principal $U(1)$-bundles over the identity is automatically an isomorphism; (iv) compute $\Psi^*(\iota^*a^{(n)})=(\hat\iota\circ\Psi)^*a^{(n)}=j^*a^{(n)}$ and show $j^*a^{(n)}=a^{(1)}$ by a one-line evaluation using $a^{(n)}_z=h(\,\cdot\,,z)$; (v) read off the curvature from [[Thm - Pull-Back of Connections and Curvature|the pull-back theorem]], part (b).

**Key decision point.** The only decision that requires insight is to *lift the base-space inclusion to a total-space inclusion* and then let the universal property do the identification, rather than trying to describe $\iota^*S^{2n+1}$ by hand as a set of pairs. Once $j$ is in hand, the composite $\hat\iota\circ\Psi=j$ collapses the pull-back connection $\hat\iota^{\,*}a^{(n)}$ into the honest restriction $j^*a^{(n)}$, and restricting a Hermitian-pairing connection form to a coordinate subsphere is immediate.

---

# Legal Operations Used

This solution deploys the following legal operations of the chapter (named descriptively; the topic page's Legal Operations will fix their numbering):

1. **Lift a map of base spaces to an equivariant map of total spaces.** The linear inclusion $\iota\colon\mathbb{CP}^1\hookrightarrow\mathbb{CP}^n$ is covered by the linear, hence $U(1)$-equivariant, inclusion $j\colon S^3\hookrightarrow S^{2n+1}$; equivariance and $\pi_n\circ j=\iota\circ\pi_1$ are the hypotheses of the next operation.

2. **Convert a covering bundle map into a map into the pull-back (universal property).** A $G$-equivariant map $j\colon Q\to P$ with $\pi_P\circ j=f\circ\pi_Q$ factors as $j=\hat f\circ\Psi$ for the unique bundle map $\Psi\colon Q\to f^*P$, $\Psi(q)=(j(q),\pi_Q(q))$, over $\mathrm{id}$.

3. **Promote a principal-bundle morphism over the identity to an isomorphism.** A $G$-equivariant smooth map between principal $G$-bundles over the same base covering $\mathrm{id}$ is bijective on each fibre (free transitive action) and a diffeomorphism, hence an isomorphism.

4. **Pull a connection back along a composite by composing the pull-backs.** $\Psi^*(\hat\iota^{\,*}a^{(n)})=(\hat\iota\circ\Psi)^*a^{(n)}=j^*a^{(n)}$, reducing the pull-back connection to a restriction.

5. **Restrict a Hermitian-pairing connection form to a coordinate subsphere.** With $a^{(n)}_z(u)=h(u,z)$, the restriction $j^*a^{(n)}$ evaluates to $h_{\mathbb{C}^2}$ against the first two coordinates, which is exactly $a^{(1)}$.

6. **Read the pulled-back curvature off the pull-back theorem.** By [[Thm - Pull-Back of Connections and Curvature|the pull-back theorem]], part (b), $F_{\iota^*a^{(n)}}=\iota^*F_{a^{(n)}}$, and under $\Psi$ this is $F_{a^{(1)}}$.

---

# Hints

> [!note]- Hint 1
> Do not try to describe $\iota^*S^{2n+1}=\{(p,x)\mid\pi_n(p)=\iota(x)\}$ directly. Instead find a bundle you *recognise* that maps into $S^{2n+1}$ over $\iota$. Which sphere maps into $S^{2n+1}$ so that the image of $[w_0:w_1]$-fibres lands in $[w_0:w_1:0:\cdots:0]$-fibres?

> [!note]- Hint 2
> The inclusion $j\colon S^3\hookrightarrow S^{2n+1}$, $(z_0,z_1)\mapsto(z_0,z_1,0,\ldots,0)$, is $U(1)$-equivariant and covers $\iota$: $\pi_n(j(p))=\iota(\pi_1(p))$. By the universal property of the pull-back, $j$ is the same data as a map $\Psi\colon S^3\to\iota^*S^{2n+1}$ over $\mathrm{id}_{\mathbb{CP}^1}$ with $\hat\iota\circ\Psi=j$. Why is $\Psi$ an isomorphism?

> [!note]- Hint 3
> Any $U(1)$-equivariant bundle map covering the identity of the base is an isomorphism: on each fibre it is an equivariant map between $U(1)$-torsors, hence bijective, and a bijective smooth bundle morphism has smooth inverse. Now for the connection: $\Psi^*(\hat\iota^{\,*}a^{(n)})=(\hat\iota\circ\Psi)^*a^{(n)}=j^*a^{(n)}$. Compute $j^*a^{(n)}$ using $a^{(n)}_z(u)=h(u,z)$.

---

# Solution

The proof never touches the set-theoretic description of the pull-back. It produces the low-dimensional Hopf sphere $S^3$ as a bundle mapping into $S^{2n+1}$ over $\iota$, invokes the universal property to turn that map into an isomorphism onto $\iota^*S^{2n+1}$, and then computes the pulled-back connection as an honest restriction, which for the Hermitian-pairing form $a^{(n)}_z=h(\,\cdot\,,z)$ is immediate. The curvature statement is then a direct quotation of the pull-back theorem.

**Step 1: The coordinate inclusion $j\colon S^3\hookrightarrow S^{2n+1}$ is equivariant and covers $\iota$.**

The linear embedding of the first two coordinates lifts $\iota$ compatibly with the $U(1)$-actions.

> [!note]- Derivation
> Define $j\colon S^3\to S^{2n+1}$ by $j(z_0,z_1)=(z_0,z_1,0,\ldots,0)$. It is smooth and, being the restriction of a complex-linear map, preserves norms, so it lands in $S^{2n+1}$.
>
> **Equivariance.** For $\lambda\in U(1)$,
> $$j\big((z_0,z_1)\cdot\lambda\big)=j(z_0\lambda,z_1\lambda)=(z_0\lambda,z_1\lambda,0,\ldots,0)=(z_0,z_1,0,\ldots,0)\cdot\lambda=j(z_0,z_1)\cdot\lambda\qquad(\text{diagonal }U(1)\text{-action}).$$
> **Covers $\iota$.** For $p=(z_0,z_1)\in S^3$,
> $$\pi_n\big(j(p)\big)=[z_0:z_1:0:\cdots:0]=\iota([z_0:z_1])=\iota\big(\pi_1(p)\big)\qquad(\text{definition of }\iota\text{ and of }\pi_1,\pi_n).$$
> Thus $j$ is a $U(1)$-equivariant bundle map from $S^3\to\mathbb{CP}^1$ to $S^{2n+1}\to\mathbb{CP}^n$ covering $\iota$.

**Step 2: The universal property produces a bundle map $\Psi\colon S^3\to\iota^*S^{2n+1}$ over the identity.**

The covering map $j$ is precisely the data of a map into the pull-back.

> [!note]- Derivation
> Define
> $$\Psi\colon S^3\to\iota^*S^{2n+1},\qquad\Psi(p)=\big(j(p),\pi_1(p)\big).$$
> **Well defined.** The pair $(j(p),\pi_1(p))$ lies in $\iota^*S^{2n+1}=\{(q,x)\mid\pi_n(q)=\iota(x)\}$ because $\pi_n(j(p))=\iota(\pi_1(p))$ by Step 1.
> **Covers $\mathrm{id}$.** $\varpi(\Psi(p))=\pi_1(p)$, so $\Psi$ is a map of bundles over $\mathbb{CP}^1$ (it covers the identity).
> **Equivariance.** For $\lambda\in U(1)$, using $j(p\lambda)=j(p)\lambda$ (Step 1) and $\pi_1(p\lambda)=\pi_1(p)$,
> $$\Psi(p\lambda)=\big(j(p)\lambda,\pi_1(p)\big)=\big(j(p),\pi_1(p)\big)\cdot\lambda=\Psi(p)\lambda\qquad(\text{action }(q,x)\cdot\lambda=(q\lambda,x)\text{ on }\iota^*S^{2n+1}).$$
> **Factorisation.** $\hat\iota(\Psi(p))=\hat\iota(j(p),\pi_1(p))=j(p)$, i.e. $\hat\iota\circ\Psi=j$; this is the identity that will collapse the pull-back connection to a restriction in Step 4.

**Step 3: $\Psi$ is an isomorphism of principal $U(1)$-bundles.**

A $U(1)$-equivariant bundle morphism over the identity is automatically invertible.

> [!note]- Derivation
> $\Psi$ is a smooth $U(1)$-equivariant map between two principal $U(1)$-bundles over $\mathbb{CP}^1$ covering $\mathrm{id}_{\mathbb{CP}^1}$.
>
> **Bijective on each fibre.** Fix $x\in\mathbb{CP}^1$. Both fibres $\pi_1^{-1}(x)$ and $\varpi^{-1}(x)$ are $U(1)$-torsors (free transitive $U(1)$-sets), and $\Psi$ restricts to a $U(1)$-equivariant map between them. Any equivariant map of torsors is a bijection: choose a base point $p_0\in\pi_1^{-1}(x)$; every point of the fibre is $p_0\lambda$ for a unique $\lambda$, and $\Psi(p_0\lambda)=\Psi(p_0)\lambda$ runs bijectively over $\varpi^{-1}(x)=\Psi(p_0)\cdot U(1)$. Hence $\Psi$ is a bijection.
>
> **Smooth inverse.** A smooth bundle morphism covering the identity that is fibrewise bijective is a diffeomorphism: in local trivialisations $\pi_1^{-1}(U)\cong U\times U(1)$ and $\varpi^{-1}(U)\cong U\times U(1)$, $\Psi$ has the form $(x,\mu)\mapsto(x,\varphi(x)\mu)$ for a smooth $\varphi\colon U\to U(1)$ (equivariance forces this shape), whose inverse $(x,\nu)\mapsto(x,\varphi(x)^{-1}\nu)$ is smooth. Therefore $\Psi$ is an isomorphism of principal $U(1)$-bundles.

**Step 4: The pull-back connection restricts to the Hopf connection on $S^3$.**

Composing pull-backs turns $\iota^*a^{(n)}$ into $j^*a^{(n)}$, which evaluates to $a^{(1)}$.

> [!note]- Derivation
> By definition $\iota^*a^{(n)}=\hat\iota^{\,*}a^{(n)}$ ([[Thm - Pull-Back of Connections and Curvature|the pull-back theorem]]). Using $\hat\iota\circ\Psi=j$ (Step 2) and functoriality of pull-back of forms,
> $$\Psi^*\big(\iota^*a^{(n)}\big)=\Psi^*\big(\hat\iota^{\,*}a^{(n)}\big)=(\hat\iota\circ\Psi)^*a^{(n)}=j^*a^{(n)}.$$
> **Evaluate $j^*a^{(n)}$.** Fix $p=(z_0,z_1)\in S^3$ and $u\in T_pS^3\subset\mathbb{C}^2$. The differential of the linear map $j$ is $dj_p(u)=(u,0,\ldots,0)$. Writing $a^{(n)}_w(\,\cdot\,)=h_{\mathbb{C}^{n+1}}(\,\cdot\,,w)$ for $w\in S^{2n+1}$ (the Hermitian-pairing form recalled above),
> $$\big(j^*a^{(n)}\big)_p(u)=a^{(n)}_{j(p)}\big(dj_p(u)\big)=h_{\mathbb{C}^{n+1}}\big((u,0,\ldots,0),\,(z_0,z_1,0,\ldots,0)\big)=h_{\mathbb{C}^2}\big(u,(z_0,z_1)\big)=a^{(1)}_p(u),$$
> where the third equality holds because the zero padding contributes nothing to the Hermitian sum, and the last is the definition of the Hopf connection form on $S^3$. Hence
> $$\Psi^*\big(\iota^*a^{(n)}\big)=a^{(1)}.$$
> Combined with Step 3, $\Psi$ is an isomorphism of principal $U(1)$-bundles carrying $\iota^*a^{(n)}$ to $a^{(1)}$: the pull-back of the Hopf bundle-with-connection along $\iota$ is the lower Hopf bundle-with-connection.

**Step 5: The curvature restricts accordingly.**

The pull-back theorem's curvature clause gives the matching identity for $F$.

> [!note]- Derivation
> By [[Thm - Pull-Back of Connections and Curvature|the pull-back theorem]], part (b), the curvature of a pull-back connection is the pull-back of the curvature:
> $$F_{\iota^*a^{(n)}}=\iota^*F_{a^{(n)}}.$$
> Transporting through the isomorphism $\Psi$ of Step 3–4, which carries $\iota^*a^{(n)}$ to $a^{(1)}$, this reads
> $$F_{a^{(1)}}=\iota^*F_{a^{(n)}}\qquad(\text{under the identification }\mathbb{CP}^1\xrightarrow{\iota}\mathbb{CP}^n).$$
> This is the connection-level statement of the nested-Hopf-bundle ladder: restricting the higher Hopf curvature $2$-form to the linearly embedded $\mathbb{CP}^1$ returns the Hopf curvature of $S^3\to\mathbb{CP}^1$.

> [!note]- Complete formal solution
> **Claim.** For the linear inclusion $\iota\colon\mathbb{CP}^1\hookrightarrow\mathbb{CP}^n$, the pull-back $(\iota^*S^{2n+1},\iota^*a^{(n)})$ is isomorphic, as a principal $U(1)$-bundle with connection, to $(S^3,a^{(1)})$; consequently $F_{a^{(1)}}=\iota^*F_{a^{(n)}}$.
>
> Let $j\colon S^3\hookrightarrow S^{2n+1}$, $(z_0,z_1)\mapsto(z_0,z_1,0,\ldots,0)$. Then $j$ is $U(1)$-equivariant ($j(p\lambda)=j(p)\lambda$) and covers $\iota$ ($\pi_n\circ j=\iota\circ\pi_1$). Define $\Psi\colon S^3\to\iota^*S^{2n+1}$ by $\Psi(p)=(j(p),\pi_1(p))$; it is well defined (as $\pi_n(j(p))=\iota(\pi_1(p))$), covers $\mathrm{id}_{\mathbb{CP}^1}$, is $U(1)$-equivariant, and satisfies $\hat\iota\circ\Psi=j$.
>
> $\Psi$ is an isomorphism: it is fibrewise a $U(1)$-equivariant map of $U(1)$-torsors, hence bijective, and covering the identity it is a diffeomorphism (in local trivialisations it has the form $(x,\mu)\mapsto(x,\varphi(x)\mu)$ with $\varphi\colon U\to U(1)$ smooth, invertible with smooth inverse).
>
> For the connection, using $\hat\iota\circ\Psi=j$ and $a^{(n)}_w=h(\,\cdot\,,w)$,
> $$\Psi^*(\iota^*a^{(n)})=(\hat\iota\circ\Psi)^*a^{(n)}=j^*a^{(n)},\qquad (j^*a^{(n)})_p(u)=h_{\mathbb{C}^{n+1}}\big((u,0,\ldots,0),j(p)\big)=h_{\mathbb{C}^2}(u,p)=a^{(1)}_p(u),$$
> so $\Psi^*(\iota^*a^{(n)})=a^{(1)}$. Finally, by the pull-back theorem $F_{\iota^*a^{(n)}}=\iota^*F_{a^{(n)}}$, which under $\Psi$ is $F_{a^{(1)}}=\iota^*F_{a^{(n)}}$. $\blacksquare$

> [!warning] Illegal but tempting: assuming a fibrewise bijection is automatically smooth-invertible without the bundle structure
> One might try to conclude $\Psi$ is an isomorphism merely from being a smooth bijection. A smooth bijection need not have smooth inverse in general (for example $t\mapsto t^3$ on $\mathbb{R}$). The legitimacy here comes specifically from $\Psi$ being a *bundle morphism over the identity between principal bundles*: local equivariant trivialisations force the shape $(x,\mu)\mapsto(x,\varphi(x)\mu)$, whose inverse is manifestly smooth. Drop the equivariance or the "over the identity" hypothesis and the argument fails.

---

# Key Takeaways

**To identify a pulled-back bundle, lift the base map upstairs and let the universal property do the work.** The reusable principle is that $f^*P$ is characterised by a universal property: a $G$-equivariant map $Q\to P$ covering $f$ is exactly the same data as a map $Q\to f^*P$ over the identity. So whenever a pull-back must be *named* rather than merely constructed, the efficient move is never to unravel the defining set $\{(p,x)\mid\pi(p)=f(x)\}$ but to find a familiar bundle $Q$ mapping equivariantly into $P$ over $f$. Here the familiar bundle is the lower Hopf sphere $S^3$ and the lift is the coordinate inclusion $j$. The trigger to recognise: a pull-back along a *linear* or otherwise structure-preserving base map almost always lifts to a structure-preserving map of total spaces, and the universal property then delivers the isomorphism for free.

**A principal-bundle morphism over the identity is automatically an isomorphism, and this is why so many bundle identifications reduce to writing down one equivariant map.** The transferable diagnostic is that between principal $G$-bundles over the same base, any $G$-equivariant smooth map covering the identity is invertible: fibrewise it is an equivariant self-map of a $G$-torsor, hence a bijection, and equivariant local trivialisations make its inverse smooth. This is the same mechanism behind [[Thm - Sections of a Principal Bundle and Triviality|the triviality criterion]] (a section trivialises a principal bundle) and it means one never has to construct an inverse by hand. Whenever two principal bundles over the same base are suspected isomorphic, produce a single equivariant map over the identity and stop; the inverse exists by structure.

**Pulling back commutes with the whole apparatus — bundle, connection, and curvature — so nested inclusions of base spaces give nested restrictions of gauge data.** The structural point worth storing is that [[Thm - Pull-Back of Connections and Curvature|the pull-back theorem]] is natural in every argument: $f^*$ of a connection is a connection, and $F_{f^*A}=f^*F_A$. Applied to the ladder $\mathbb{CP}^1\subset\mathbb{CP}^2\subset\cdots$, this says the Hopf connections and their curvatures on the small spheres are literally the restrictions of those on the large spheres. That compatibility is what lets a single computation on $\mathbb{CP}^1$ — such as the curvature integral $\int_{\mathbb{CP}^1}F_{a}=2\pi i$ from [[Ex - Curvature of the Standard Hopf Connection]] — control the tautological bundle over every $\mathbb{CP}^n$ at once, and it is the mechanism behind the naturality of characteristic classes proved in chapter VI. Companion exercise: [[Ex - The Induced Connection on the Tautological Bundle from the Hopf Connection]], where the same Hopf connection is instead pushed *forward* onto the associated tautological line bundle.
