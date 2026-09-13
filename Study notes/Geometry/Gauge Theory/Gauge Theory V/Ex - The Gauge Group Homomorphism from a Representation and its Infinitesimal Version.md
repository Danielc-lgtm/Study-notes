---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Gauge Group is the Space of Sections of the Adjoint Group Bundle"
  - "Def - Gauge Transformation"
  - "Def - Associated Bundle"
  - "Def - Adjoint Bundles ad P and Ad P"
  - "Def - Gauge Group of a Vector Bundle"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\pi\colon P\to M$ be a smooth principal $G$-bundle ($G$ a Lie group, acting on the right, $p\cdot g$), let $\rho\colon G\to GL(V)$ be a (finite-dimensional, real or complex) representation, and let
$$E:=P\times_\rho V=(P\times V)/G,\qquad (p,v)\cdot g=(p\cdot g,\ \rho(g)^{-1}v),$$
be the associated vector bundle, whose points are equivalence classes $[p,v]$ with $[p\cdot g,v]=[p,\rho(g)v]$ and whose projection is $[p,v]\mapsto\pi(p)$. Write $\mathfrak{g}=T_eG$ for the Lie algebra of $G$ (bracket the commutator for matrix groups), $\rho_*:=d_e\rho\colon\mathfrak{g}\to\operatorname{End}(V)$ for the differential of $\rho$ at the identity, $\operatorname{Ad}P=P\times_\alpha G$ ($\alpha$ the conjugation action $\alpha_g(h)=ghg^{-1}$) for the adjoint group bundle, and $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak{g}$ for the adjoint (Lie algebra) bundle. The gauge group of the vector bundle $E$ is
$$\mathcal{G}(E)=\{\,s\in\Gamma(\operatorname{End}E):s(m)\in GL(E_m)\text{ for all }m\,\},$$
the smooth sections that are invertible in every fibre, a group under fibrewise composition.

Prove the following.

**(i) The induced gauge-group homomorphism.** The representation $\rho$ induces a natural group homomorphism
$$\gamma\colon\mathcal{G}(P)\longrightarrow\mathcal{G}(E),\qquad \gamma(f)\,[p,v]:=[f(p),v].$$
Show $\gamma(f)$ is a well-defined vector-bundle automorphism covering $\operatorname{id}_M$ (hence $\gamma(f)\in\mathcal{G}(E)$), and that $\gamma$ is a homomorphism of groups.

**(ii) The infinitesimal Lie-algebra homomorphism.** The differential $\rho_*\colon\mathfrak{g}\to\operatorname{End}(V)$ induces a map
$$\gamma_*\colon\Gamma(\operatorname{ad}P)\longrightarrow\Gamma(\operatorname{End}E),\qquad \gamma_*(\xi)\,[p,w]:=[p,\rho_*(X)\,w]\ \text{ where }\xi(\pi p)=[p,X].$$
Show $\gamma_*$ is well defined and is a homomorphism of Lie algebras, where $\Gamma(\operatorname{ad}P)$ carries the fibrewise bracket induced by $[\cdot,\cdot]_{\mathfrak g}$ and $\Gamma(\operatorname{End}E)$ carries the fibrewise commutator $[S,T]=S\circ T-T\circ S$.

**(iii) Non-injectivity.** Show that $\gamma$ need not be injective, by taking $G=SU(2)$ and $\rho=\operatorname{Ad}\colon SU(2)\to GL(\mathfrak{su}(2))$: exhibit a nontrivial gauge transformation of $P$ (for a bundle with structure group $SU(2)$) that $\gamma$ sends to the identity.

**Recall:**

The objects in play are the associated bundle $E=P\times_\rho V$, the gauge groups $\mathcal{G}(P)$ and $\mathcal{G}(E)$, the adjoint bundles $\operatorname{Ad}P$ and $\operatorname{ad}P$, and the theorem that ties a gauge transformation to its fibre coordinate.

![[Def - Associated Bundle#The Definition]]

![[Def - Adjoint Bundles ad P and Ad P#The Definition]]

![[Def - Gauge Group of a Vector Bundle#The Definition]]

![[Thm - The Gauge Group is the Space of Sections of the Adjoint Group Bundle#Statement]]

We shall use one standard fact about representations, recalled and applied at its point of use: the differential of a Lie group homomorphism is a Lie algebra homomorphism.

![[Thm - Lie Group Homomorphism Induces Lie Algebra Homomorphism#Statement]]

---

# Convergent Strategy

**Problem class.** This is a *transport-a-structure-through-the-associated-bundle-construction* problem. A gauge transformation $f$ of $P$ is a symmetry of the total space; the functor $P\times_\rho(-)$ turns symmetries of $P$ into symmetries of $E$, and its linearised version turns infinitesimal symmetries (sections of $\operatorname{ad}P$) into endomorphism fields. The recurring move is to define a map on *representatives* $[p,v]$ and then discharge two debts: well-definedness (independence of the representative, using the equivalence relation $[pg,v]=[p,\rho(g)v]$) and the homomorphism property.

**Assumption pattern.** Two facts about $\rho$ do all the work. First, $\rho$ is a group homomorphism, $\rho(gh)=\rho(g)\rho(h)$ — this is what makes $\gamma$ well defined and a homomorphism. Second, its differential $\rho_*$ is a Lie algebra homomorphism and intertwines the adjoint actions, $\rho_*(\operatorname{Ad}_gX)=\operatorname{Ad}_{\rho(g)}\rho_*(X)=\rho(g)\rho_*(X)\rho(g)^{-1}$ — the first clause makes $\gamma_*$ a Lie-algebra map, the second makes it well defined on $\operatorname{ad}P$. Recognising *which* of these two is needed at each step is the whole strategy.

**Theorem routing.** For (i): define $\gamma(f)$ on classes; check well-definedness against $[pg,v]=[p,\rho(g)v]$ using $f(pg)=f(p)g$ ([[Def - Gauge Transformation|equivariance of the gauge transformation]]); check fibrewise linearity and invertibility to land in $\mathcal{G}(E)$; check $\gamma(f_1\circ f_2)=\gamma(f_1)\circ\gamma(f_2)$. For (ii): define $\gamma_*(\xi)$ on classes; check well-definedness using the intertwining relation $\rho_*(\operatorname{Ad}_{g^{-1}}X)=\rho(g)^{-1}\rho_*(X)\rho(g)$; then reduce the Lie-algebra-homomorphism property fibrewise to [[Thm - Lie Group Homomorphism Induces Lie Algebra Homomorphism|the fact that the differential of a representation is a Lie algebra homomorphism]]. For (iii): compute $\gamma$ in the $\operatorname{Ad}$-representation and use $\ker\operatorname{Ad}=Z(SU(2))=\{\pm\mathbf 1\}$.

**Key decision point.** The subtle step is the well-definedness of $\gamma_*$: the naive attempt writes $\gamma_*(\xi)$ using a *chosen* $p$ with $\xi(\pi p)=[p,X]$, and one must verify the resulting endomorphism of the fibre $E_{\pi p}$ does not depend on that choice. The computation forces exactly the intertwining relation $\rho_*(\operatorname{Ad}_{g^{-1}}X)=\rho(g)^{-1}\rho_*(X)\rho(g)$, which is the linearisation of $\rho(g^{-1}hg)=\rho(g)^{-1}\rho(h)\rho(g)$. Seeing that this relation is *demanded by, not incidental to,* the construction is the point of the exercise.

---

# Legal Operations Used

This solution deploys the following operations from [[Gauge Theory V — Parallel Transport, Holonomy, Gauge Transformations, and Flat Connections#Legal Operations|the topic page's Legal Operations]].

1. **Define a bundle map on representatives and discharge well-definedness against the equivalence relation.** For $E=P\times_\rho V$ with $[pg,v]=[p,\rho(g)v]$, a formula on $[p,v]$ is a genuine map only after checking it agrees on $[pg,\rho(g)^{-1}v]$; here the checks consume the equivariance of $f$ (for $\gamma$) and the intertwining of $\rho_*$ (for $\gamma_*$).

2. **Use $\rho(gh)=\rho(g)\rho(h)$ to turn a group action of $P$ into a linear action on $E$.** The homomorphism property of $\rho$ is what makes $\gamma(f)$ fibrewise linear and $\gamma$ a group homomorphism.

3. **Linearise a conjugation identity.** Differentiating $\rho(ghg^{-1})=\rho(g)\rho(h)\rho(g)^{-1}$ at $h=e$ produces $\rho_*(\operatorname{Ad}_gX)=\rho(g)\rho_*(X)\rho(g)^{-1}$, the exact relation making $\gamma_*$ descend to $\operatorname{ad}P$.

4. **Reduce a bundle-level algebraic identity to its fibre and quote the finite-dimensional theorem.** The Lie-algebra-homomorphism property of $\gamma_*$ is checked fibrewise and there reduces to [[Thm - Lie Group Homomorphism Induces Lie Algebra Homomorphism|the bracket-preservation of the differential]].

5. **Detect non-injectivity through a kernel computation in the fibre.** $\gamma(f)=\operatorname{id}$ forces $\rho(\hat f(p))=\operatorname{id}_V$ pointwise, i.e. $\hat f(p)\in\ker\rho$; a nontrivial $f$ with central-valued fibre coordinate in $\ker\rho$ then witnesses non-injectivity.

---

# Hints

> [!note]- Hint 1
> Define $\gamma(f)[p,v]:=[f(p),v]$. Before anything else, this must not depend on the representative: recompute it on $[p\cdot g,\ \rho(g)^{-1}v]$, which is the *same* point of $E$ as $[p,v]$. You will need to move $f$ past the right action — which relation of $f$ lets you do that?

> [!note]- Hint 2
> Equivariance $f(pg)=f(p)g$ gives $\gamma(f)[pg,\rho(g)^{-1}v]=[f(p)g,\rho(g)^{-1}v]=[f(p),v]$, matching $\gamma(f)[p,v]$. For fibrewise linearity, fix $p\in P_m$; every element of $E_m$ is uniquely $[p,v]$, and $\gamma(f)[p,v]=[f(p),v]$; work in the trivialisation given by a local section to see this is linear and invertible.

> [!note]- Hint 3
> For $\gamma_*$, define $\gamma_*(\xi)[p,w]=[p,\rho_*(X)w]$ where $\xi(\pi p)=[p,X]$. Well-definedness: the same section is $\xi(\pi p)=[pg,\operatorname{Ad}_{g^{-1}}X]$. So you must check $[pg,\rho_*(\operatorname{Ad}_{g^{-1}}X)w']$ gives the *same endomorphism* as $[p,\rho_*(X)\cdot]$. Differentiate $\rho(g^{-1}hg)=\rho(g)^{-1}\rho(h)\rho(g)$ at $h=e$ to get the relation you need.

> [!note]- Hint 4
> For non-injectivity with $\rho=\operatorname{Ad}$: $\gamma(f)[p,X]=[f(p),X]=[p\cdot\hat f(p),X]=[p,\operatorname{Ad}_{\hat f(p)}X]$. So $\gamma(f)=\operatorname{id}$ iff $\operatorname{Ad}_{\hat f(p)}=\operatorname{id}$ for all $p$, i.e. $\hat f(p)\in\ker\operatorname{Ad}=Z(SU(2))=\{\pm\mathbf 1\}$. The constant $\hat f\equiv-\mathbf 1$ is a nontrivial gauge transformation in the kernel of $\gamma$.

---

# Solution

The construction is the associated-bundle functor applied to a symmetry. A gauge transformation $f$ moves the points of $P$ that label the fibres of $E$; carrying $v$ along unchanged, $[p,v]\mapsto[f(p),v]$, gives a linear map on each fibre because $\rho$ is a homomorphism, and it is well defined because $f$ is equivariant. Linearising — replacing the finite group element $\hat f(p)$ by an infinitesimal $X$ and $\rho$ by $\rho_*$ — gives the Lie-algebra version, whose well-definedness needs exactly the linearised conjugation identity, and whose bracket-preservation is the fibrewise statement that $\rho_*$ preserves brackets.

## Part (i): the induced gauge-group homomorphism $\gamma$

**Step 1: $\gamma(f)$ is a well-defined map $E\to E$ covering $\operatorname{id}_M$.**

For $f\in\mathcal{G}(P)$, the formula $\gamma(f)[p,v]:=[f(p),v]$ defines a map $E\to E$ with $\pi_E\circ\gamma(f)=\pi_E$.

> [!note]- Derivation
> **Independence of the representative.** A point of $E$ has many labels: $[p,v]=[p\cdot g,\rho(g)^{-1}v]$ for every $g\in G$, by the defining equivalence of the [[Def - Associated Bundle|associated bundle]]. Applying the formula to the second label,
> $$\gamma(f)[p\cdot g,\ \rho(g)^{-1}v]=[f(p\cdot g),\ \rho(g)^{-1}v]=[f(p)\cdot g,\ \rho(g)^{-1}v]\qquad(\text{equivariance }f(p\cdot g)=f(p)\cdot g\text{ of }f\in\mathcal{G}(P)),$$
> and by the same equivalence relation $[f(p)\cdot g,\ \rho(g)^{-1}v]=[f(p),\ v]$. This equals $\gamma(f)[p,v]$, so the value is independent of the chosen representative: $\gamma(f)$ is a well-defined map $E\to E$. Equivariance of $f$ is used here and nowhere else in Step 1.
>
> **Covering the identity.** The class $[p,v]$ lies over $\pi(p)$, and $[f(p),v]$ lies over $\pi(f(p))=\pi(p)$ because $f$ is a gauge transformation, hence covers the identity, $\pi\circ f=\pi$ ([[Def - Gauge Transformation|Def - Gauge Transformation]]). Thus $\gamma(f)$ maps the fibre $E_m$ into itself for every $m$, i.e. $\pi_E\circ\gamma(f)=\pi_E$.

**Step 2: $\gamma(f)$ is a smooth vector-bundle automorphism, so $\gamma(f)\in\mathcal{G}(E)$.**

On each fibre $\gamma(f)$ is a linear isomorphism, and it is smooth; hence $\gamma(f)\in\mathcal{G}(E)$.

> [!note]- Derivation
> **Fibrewise linearity.** Fix $m\in M$ and $p\in P_m$. Every element of $E_m$ is uniquely $[p,v]$ with $v\in V$ (for fixed $p$, the map $v\mapsto[p,v]$ is a linear isomorphism $V\to E_m$, part of the [[Def - Associated Bundle|associated-bundle]] vector-space structure). Then
> $$\gamma(f)\big([p,v]+[p,v']\big)=\gamma(f)[p,v+v']=[f(p),v+v']=[f(p),v]+[f(p),v']=\gamma(f)[p,v]+\gamma(f)[p,v'],$$
> $$\gamma(f)\big(\lambda[p,v]\big)=\gamma(f)[p,\lambda v]=[f(p),\lambda v]=\lambda[f(p),v]=\lambda\,\gamma(f)[p,v]\qquad(\lambda\in\mathbb K),$$
> using that $w\mapsto[q,w]$ is linear for the fixed frame $q=f(p)$ as well. So $\gamma(f)|_{E_m}$ is linear.
>
> **Smoothness and the explicit local form.** Let $s\colon U\to P$ be a smooth local section and let $g_s:=\hat f\circ s\colon U\to G$, where $\hat f\colon P\to G$ is the fibre coordinate of $f$ from [[Thm - The Gauge Group is the Space of Sections of the Adjoint Group Bundle|the identification theorem]] ($f(p)=p\cdot\hat f(p)$). In the local trivialisation $E|_U\cong U\times V$, $[s(m),v]\leftrightarrow(m,v)$, we compute
> $$\gamma(f)[s(m),v]=[f(s(m)),v]=[s(m)\cdot g_s(m),\ v]=[s(m),\ \rho(g_s(m))\,v]\qquad(\text{equivalence }[qg,v]=[q,\rho(g)v]).$$
> Hence in this trivialisation $\gamma(f)$ is $(m,v)\mapsto(m,\rho(g_s(m))v)$, i.e. the endomorphism field $m\mapsto\rho(g_s(m))\in GL(V)$. This is smooth because $g_s$ is smooth (composition of smooth maps) and $\rho$ is smooth; and it takes values in $GL(V)$ because $\rho(g_s(m))$ is invertible (a group homomorphism sends $G$ into $GL(V)$). Therefore $\gamma(f)$ is a smooth section of $\operatorname{End}E$ that is fibrewise invertible: $\gamma(f)\in\mathcal{G}(E)$. In the language of the adjoint bundle, $\gamma(f)$ is $\rho$ applied fibrewise to the section $\Phi(f)=(m\mapsto[p,\hat f(p)])\in\Gamma(\operatorname{Ad}P)$.

**Step 3: $\gamma$ is a group homomorphism.**

For $f_1,f_2\in\mathcal{G}(P)$, $\gamma(f_1\circ f_2)=\gamma(f_1)\circ\gamma(f_2)$, and $\gamma(\operatorname{id}_P)=\operatorname{id}_E$.

> [!note]- Derivation
> Directly from the definition, for every class $[p,v]$,
> $$\gamma(f_1\circ f_2)[p,v]=[(f_1\circ f_2)(p),v]=[f_1(f_2(p)),v]=\gamma(f_1)[f_2(p),v]=\gamma(f_1)\big(\gamma(f_2)[p,v]\big)=\big(\gamma(f_1)\circ\gamma(f_2)\big)[p,v],$$
> where the group operation on $\mathcal{G}(P)$ is composition and the operation on $\mathcal{G}(E)$ is fibrewise composition of bundle automorphisms. Also $\gamma(\operatorname{id}_P)[p,v]=[\operatorname{id}_P(p),v]=[p,v]$, so $\gamma(\operatorname{id}_P)=\operatorname{id}_E$. Therefore $\gamma\colon\mathcal{G}(P)\to\mathcal{G}(E)$ is a homomorphism of groups. Its naturality is the statement that $\gamma$ is the effect of $f$ under the functor $P\times_\rho(-)$ from representations to vector bundles: a $G$-equivariant self-map of $P$ induces a self-map of every associated bundle, compatibly with morphisms of representations.

## Part (ii): the infinitesimal Lie-algebra homomorphism $\gamma_*$

**Step 4: the intertwining relation for $\rho_*$.**

For every $g\in G$ and $X\in\mathfrak{g}$,
$$\rho_*(\operatorname{Ad}_gX)=\rho(g)\,\rho_*(X)\,\rho(g)^{-1},\qquad\text{equivalently}\qquad \rho_*(\operatorname{Ad}_{g^{-1}}X)=\rho(g)^{-1}\rho_*(X)\rho(g).$$

> [!note]- Derivation
> Because $\rho$ is a group homomorphism, $\rho(g\,h\,g^{-1})=\rho(g)\,\rho(h)\,\rho(g)^{-1}$ for all $h\in G$. Apply both sides to $h=\exp(tX)$ and differentiate at $t=0$. On the left, $\tfrac{d}{dt}\big|_0\,g\exp(tX)g^{-1}=\operatorname{Ad}_gX$ by the definition of $\operatorname{Ad}$, so by the chain rule
> $$\frac{d}{dt}\Big|_0\rho\big(g\exp(tX)g^{-1}\big)=\rho_*\Big(\tfrac{d}{dt}\big|_0\,g\exp(tX)g^{-1}\Big)=\rho_*(\operatorname{Ad}_gX).$$
> On the right, $\rho(g)$ and $\rho(g)^{-1}$ are constant in $t$, so
> $$\frac{d}{dt}\Big|_0\rho(g)\,\rho(\exp(tX))\,\rho(g)^{-1}=\rho(g)\Big(\tfrac{d}{dt}\big|_0\rho(\exp tX)\Big)\rho(g)^{-1}=\rho(g)\,\rho_*(X)\,\rho(g)^{-1},$$
> using $\tfrac{d}{dt}\big|_0\rho(\exp tX)=\rho_*(X)$ (the differential of $\rho$ at $e$). Equating gives $\rho_*(\operatorname{Ad}_gX)=\rho(g)\rho_*(X)\rho(g)^{-1}$; replacing $g$ by $g^{-1}$ gives the second form.

**Step 5: $\gamma_*(\xi)$ is a well-defined smooth section of $\operatorname{End}E$.**

For $\xi\in\Gamma(\operatorname{ad}P)$, the formula $\gamma_*(\xi)[p,w]:=[p,\rho_*(X)w]$, where $\xi(\pi p)=[p,X]$, defines a smooth endomorphism field of $E$.

> [!note]- Derivation
> **The endomorphism does not depend on the frame $p$ representing $\xi$.** Fix $m\in M$. The section value $\xi(m)\in(\operatorname{ad}P)_m$ has many labels: $\xi(m)=[p,X]=[p\cdot g,\operatorname{Ad}_{g^{-1}}X]$ for every $g\in G$, by the defining equivalence of $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak g$. Using the frame $p$, $\gamma_*(\xi)$ is the endomorphism $T_p$ of $E_m$ with $T_p[p,w]=[p,\rho_*(X)w]$; using the frame $p\cdot g$, it is $T_{pg}$ with $T_{pg}[pg,w']=[pg,\rho_*(\operatorname{Ad}_{g^{-1}}X)w']$. We check $T_p=T_{pg}$ on an arbitrary element of $E_m$, written as $[p,w]=[pg,\rho(g)^{-1}w]$ (so $w'=\rho(g)^{-1}w$):
> $$T_{pg}[p,w]=T_{pg}[pg,\rho(g)^{-1}w]=[pg,\ \rho_*(\operatorname{Ad}_{g^{-1}}X)\,\rho(g)^{-1}w]=[pg,\ \rho(g)^{-1}\rho_*(X)\rho(g)\,\rho(g)^{-1}w]$$
> $$=[pg,\ \rho(g)^{-1}\rho_*(X)w]=[p,\ \rho_*(X)w]=T_p[p,w],$$
> where the third equality is the intertwining relation of Step 4 and the fifth is $[pg,\rho(g)^{-1}u]=[p,u]$ with $u=\rho_*(X)w$. Hence $T_p=T_{pg}$: the endomorphism is independent of the representing frame, and $\gamma_*(\xi)$ is well defined fibrewise.
>
> **Linearity and smoothness.** On $E_m$, with $p$ fixed, $[p,w]\mapsto[p,\rho_*(X)w]$ is $\mathbb R$-linear in $w$ because $\rho_*(X)\in\operatorname{End}(V)$ is linear and $w\mapsto[p,w]$ is a linear isomorphism $V\to E_m$. Smoothness in $m$ is seen in a local trivialisation from a section $s\colon U\to P$: writing $\xi(m)=[s(m),\zeta(m)]$ with $\zeta\colon U\to\mathfrak g$ smooth (the local principal-frame description of $\xi$), $\gamma_*(\xi)[s(m),w]=[s(m),\rho_*(\zeta(m))w]$, i.e. the endomorphism field $m\mapsto\rho_*(\zeta(m))\in\operatorname{End}(V)$, smooth because $\zeta$ is smooth and $\rho_*$ is linear (hence smooth). So $\gamma_*(\xi)\in\Gamma(\operatorname{End}E)$, and $\gamma_*$ is $\mathbb R$-linear in $\xi$ because $\rho_*$ is linear.

**Step 6: $\gamma_*$ is a Lie-algebra homomorphism.**

For $\xi,\eta\in\Gamma(\operatorname{ad}P)$, $\gamma_*([\xi,\eta])=[\gamma_*(\xi),\gamma_*(\eta)]$, the left bracket the fibrewise Lie bracket on $\operatorname{ad}P$ and the right one the commutator of endomorphisms.

> [!note]- Derivation
> The bracket on $\Gamma(\operatorname{ad}P)$ is defined fibrewise from the bracket of $\mathfrak g$: if $\xi(m)=[p,X]$ and $\eta(m)=[p,Y]$ with the *same* frame $p$ (always achievable, as $G$ acts transitively on the fibre of $P$), then $[\xi,\eta](m)=[p,[X,Y]_{\mathfrak g}]$. This is well defined by the same intertwining used in Step 5, applied to the linear map $\operatorname{Ad}_{g^{-1}}$ which is a Lie algebra automorphism, so $[\operatorname{Ad}_{g^{-1}}X,\operatorname{Ad}_{g^{-1}}Y]=\operatorname{Ad}_{g^{-1}}[X,Y]$.
>
> Now evaluate both sides at $m$ using this common frame $p$. On the left,
> $$\gamma_*([\xi,\eta])(m)\,[p,w]=[p,\ \rho_*([X,Y]_{\mathfrak g})\,w].$$
> By [[Thm - Lie Group Homomorphism Induces Lie Algebra Homomorphism|the theorem that the differential of a Lie group homomorphism is a Lie algebra homomorphism]] — restated: *for a Lie group homomorphism $\rho\colon G\to H$, the differential $\rho_*\colon\mathfrak g\to\mathfrak h$ satisfies $\rho_*[X,Y]=[\rho_*X,\rho_*Y]$* — applied to $\rho\colon G\to GL(V)$ (whose Lie algebra is $\operatorname{End}(V)$ with the commutator bracket),
> $$\rho_*([X,Y]_{\mathfrak g})=[\rho_*(X),\rho_*(Y)]=\rho_*(X)\rho_*(Y)-\rho_*(Y)\rho_*(X).$$
> On the right, using the fibrewise action twice (with the same frame $p$),
> $$\big[\gamma_*(\xi),\gamma_*(\eta)\big](m)\,[p,w]=\gamma_*(\xi)\big([p,\rho_*(Y)w]\big)-\gamma_*(\eta)\big([p,\rho_*(X)w]\big)=[p,\rho_*(X)\rho_*(Y)w]-[p,\rho_*(Y)\rho_*(X)w]$$
> $$=[p,\ (\rho_*(X)\rho_*(Y)-\rho_*(Y)\rho_*(X))\,w].$$
> The two displayed results agree by the boxed identity $\rho_*[X,Y]=[\rho_*X,\rho_*Y]$. Since $m$ and $w$ were arbitrary, $\gamma_*([\xi,\eta])=[\gamma_*(\xi),\gamma_*(\eta)]$. Combined with the $\mathbb R$-linearity from Step 5, $\gamma_*$ is a homomorphism of Lie algebras.

## Part (iii): $\gamma$ need not be injective

**Step 7: for $\rho=\operatorname{Ad}$ of $SU(2)$, $\gamma$ has nontrivial kernel.**

Let $G=SU(2)$ and $\rho=\operatorname{Ad}\colon SU(2)\to GL(\mathfrak{su}(2))$, so $E=\operatorname{ad}P$. The constant-fibre-coordinate gauge transformation with $\hat f\equiv-\mathbf 1$ is nontrivial yet lies in $\ker\gamma$.

> [!note]- Derivation
> **$\gamma$ in the adjoint representation.** For $f\in\mathcal{G}(P)$ with fibre coordinate $\hat f$ ($f(p)=p\cdot\hat f(p)$), Step 2 gives, on $E=P\times_{\operatorname{Ad}}\mathfrak{su}(2)=\operatorname{ad}P$,
> $$\gamma(f)[p,X]=[f(p),X]=[p\cdot\hat f(p),X]=[p,\ \operatorname{Ad}_{\hat f(p)}X]\qquad(\text{equivalence }[qg,X]=[q,\operatorname{Ad}_gX]).$$
> Hence $\gamma(f)=\operatorname{id}_E$ if and only if $\operatorname{Ad}_{\hat f(p)}X=X$ for all $p\in P$ and all $X\in\mathfrak{su}(2)$, i.e. $\hat f(p)\in\ker\operatorname{Ad}$ for every $p$.
>
> **The kernel of $\operatorname{Ad}$ is the centre, which is $\{\pm\mathbf 1\}$.** For any Lie group, $\operatorname{Ad}_a=\operatorname{id}_{\mathfrak g}$ means $a\exp(tX)a^{-1}=\exp(tX)$ for all $X$ near $0$ and all small $t$ (since $\operatorname{Ad}_a=\operatorname{id}$ forces $\tfrac{d}{dt}\big|_0 a\exp(tX)a^{-1}=X$, and integrating, $a\exp(tX)a^{-1}=\exp(t\operatorname{Ad}_aX)=\exp(tX)$); as $SU(2)$ is connected and generated by such $\exp(tX)$, $a$ commutes with all of $SU(2)$, so $a\in Z(SU(2))$. Conversely central elements have $\operatorname{Ad}_a=\operatorname{id}$. Thus $\ker\operatorname{Ad}=Z(SU(2))$, and $Z(SU(2))=\{\pm\mathbf 1\}$: a matrix $a\in SU(2)$ commuting with every element of $SU(2)$ commutes in particular with the Pauli-basis anti-Hermitian generators, forcing $a$ to be a scalar $\lambda\mathbf 1$, and $\det a=1$, $|\lambda|=1$ give $\lambda^2=1$, $\lambda=\pm1$. (This is the computation of [[Ex - Conjugation and the Centre|the centre]], and $\ker\operatorname{Ad}_{SU(2)}=\{\pm\mathbf 1\}$ is exactly [[Ex - The Adjoint Representation of SU(2) in the Pauli Basis|the non-faithfulness of Ad recorded there]].)
>
> **A nontrivial element of $\ker\gamma$.** Since $-\mathbf 1\in Z(SU(2))$, the constant map $\hat f\equiv-\mathbf 1$ is conjugation-invariant, $\hat f(pg)=g^{-1}(-\mathbf 1)g=-\mathbf 1=\hat f(p)$, so by [[Thm - The Gauge Group is the Space of Sections of the Adjoint Group Bundle|the identification theorem]] it is the fibre coordinate of a genuine gauge transformation $f(p)=p\cdot(-\mathbf 1)$. This $f$ is **not** the identity: $f(p)=p\cdot(-\mathbf 1)\ne p$ because the right action is free and $-\mathbf 1\ne e$. Yet $\hat f(p)=-\mathbf 1\in\ker\operatorname{Ad}$ for all $p$, so $\gamma(f)=\operatorname{id}_E$ by the first paragraph. Hence $f\in\ker\gamma\setminus\{\operatorname{id}_P\}$: $\gamma$ is not injective. The kernel is exactly the central gauge transformations $C^\infty(M;\{\pm\mathbf 1\})$, of which $-\mathbf 1$ is the simplest nontrivial member.

> [!note]- Complete formal solution
> **Claim.** With $E=P\times_\rho V$: (i) $\gamma(f)[p,v]=[f(p),v]$ defines a group homomorphism $\gamma\colon\mathcal{G}(P)\to\mathcal{G}(E)$; (ii) $\gamma_*(\xi)[p,w]=[p,\rho_*(X)w]$ (for $\xi(\pi p)=[p,X]$) defines a Lie-algebra homomorphism $\Gamma(\operatorname{ad}P)\to\Gamma(\operatorname{End}E)$; (iii) $\gamma$ need not be injective.
>
> **(i)** *Well defined:* $\gamma(f)[pg,\rho(g)^{-1}v]=[f(pg),\rho(g)^{-1}v]=[f(p)g,\rho(g)^{-1}v]=[f(p),v]=\gamma(f)[p,v]$, using $f(pg)=f(p)g$. It covers $\operatorname{id}_M$ since $\pi f=\pi$. *Fibrewise linear and invertible:* fixing $p\in P_m$, $[p,v]\mapsto[f(p),v]$ is linear in $v$; in a trivialisation from a section $s$ with $g_s=\hat f\circ s$, $\gamma(f)[s(m),v]=[s(m),\rho(g_s(m))v]$, so $\gamma(f)$ is the smooth field $m\mapsto\rho(g_s(m))\in GL(V)$, hence in $\mathcal{G}(E)$. *Homomorphism:* $\gamma(f_1\circ f_2)[p,v]=[f_1(f_2(p)),v]=(\gamma(f_1)\circ\gamma(f_2))[p,v]$, and $\gamma(\operatorname{id})=\operatorname{id}$.
>
> **(ii)** Differentiating $\rho(ghg^{-1})=\rho(g)\rho(h)\rho(g)^{-1}$ at $h=e$ gives $\rho_*(\operatorname{Ad}_gX)=\rho(g)\rho_*(X)\rho(g)^{-1}$. *Well defined:* with $\xi(m)=[p,X]=[pg,\operatorname{Ad}_{g^{-1}}X]$ and $[p,w]=[pg,\rho(g)^{-1}w]$, $T_{pg}[p,w]=[pg,\rho_*(\operatorname{Ad}_{g^{-1}}X)\rho(g)^{-1}w]=[pg,\rho(g)^{-1}\rho_*(X)w]=[p,\rho_*(X)w]=T_p[p,w]$; linear and smooth as in Step 5. *Lie algebra map:* with a common frame $p$, $\gamma_*([\xi,\eta])[p,w]=[p,\rho_*[X,Y]w]$ and $[\gamma_*\xi,\gamma_*\eta][p,w]=[p,(\rho_*X\rho_*Y-\rho_*Y\rho_*X)w]$; these agree by $\rho_*[X,Y]=[\rho_*X,\rho_*Y]$, the theorem that a Lie group homomorphism's differential is a Lie algebra homomorphism.
>
> **(iii)** For $\rho=\operatorname{Ad}$ of $SU(2)$, $\gamma(f)[p,X]=[p,\operatorname{Ad}_{\hat f(p)}X]$, so $\gamma(f)=\operatorname{id}$ iff $\hat f(p)\in\ker\operatorname{Ad}=Z(SU(2))=\{\pm\mathbf 1\}$. The gauge transformation $f(p)=p\cdot(-\mathbf 1)$ is nontrivial (the action is free, $-\mathbf 1\ne e$) but $\gamma(f)=\operatorname{id}$; hence $\gamma$ is not injective. $\blacksquare$

> [!warning] Illegal but tempting shortcut: defining $\gamma_*(\xi)$ "on the total space" without checking the frame-independence
> One is tempted to write $\gamma_*(\xi)$ by picking, once and for all, a section of $P$ and setting $\gamma_*(\xi)=\rho_*\circ\xi$ in that trivialisation. But $\xi$ is a section of $\operatorname{ad}P$, whose fibre value $[p,X]$ has representatives differing by $\operatorname{Ad}_{g^{-1}}$; a definition that fixes one representative is only consistent if the *intertwining relation* $\rho_*(\operatorname{Ad}_{g^{-1}}X)=\rho(g)^{-1}\rho_*(X)\rho(g)$ holds — exactly the relation of Step 4. Skipping the check hides the one place where $\rho$ being a homomorphism (not merely a linear map) is used; the construction becomes legal precisely because $\rho_*$ intertwines the two adjoint actions.

---

# Key Takeaways

**A representation transports gauge symmetry from the principal bundle to every associated bundle, and the transport is a homomorphism because the representation is.** The reusable principle is that $P\times_\rho(-)$ is a functor from $G$-representations to vector bundles, and functors carry symmetries to symmetries: an automorphism $f$ of $P$ induces an automorphism $\gamma(f)$ of $E=P\times_\rho V$ by acting on the frame and leaving the fibre vector fixed, $[p,v]\mapsto[f(p),v]$. The two debts one always pays — well-definedness against the equivalence relation and the homomorphism law — are discharged, respectively, by the equivariance of $f$ and the homomorphism property $\rho(gh)=\rho(g)\rho(h)$. The trigger to reach for this is any construction that must "act on sections of an associated bundle by a gauge transformation": rather than trivialise, define the action on classes $[p,v]$ and let the equivalence relation dictate what must be checked. This same pattern gives the action of $\mathcal{G}(P)$ on connections, on curvatures, and on the Chern–Weil forms, all of which are sections of bundles associated to $P$.

**Infinitesimalising a bundle construction replaces group elements by Lie algebra elements, representations by their differentials, and adjoint conjugation by adjoint bracket — and the differential of a homomorphism is again a homomorphism.** The map $\gamma_*$ is the exact linearisation of $\gamma$: where $\gamma$ used $\rho(\hat f(p))$ and the conjugation-equivariance $\hat f(pg)=g^{-1}\hat f(p)g$, its infinitesimal version uses $\rho_*(X)$ and the adjoint-equivariance $[pg,\operatorname{Ad}_{g^{-1}}X]$. The single technical fact powering both the well-definedness and the bracket-preservation is that $\rho_*$ intertwines the two levels: $\rho_*(\operatorname{Ad}_gX)=\operatorname{Ad}_{\rho(g)}\rho_*(X)$ (well-definedness) and $\rho_*[X,Y]=[\rho_*X,\rho_*Y]$ (Lie-algebra homomorphism). The transferable diagnostic: whenever a construction on $\operatorname{Ad}P$ has a counterpart on $\operatorname{ad}P$, the counterpart's consistency conditions are the *linearisations at the identity* of the group-level conditions, and they are automatically satisfied precisely because differentiation turns group homomorphisms into Lie algebra homomorphisms. This is why $\Gamma(\operatorname{ad}P)$ is the Lie algebra of the gauge group $\mathcal{G}(P)$, and why the infinitesimal gauge action on connections is the covariant derivative $d^{\nabla}$, a linear operator, rather than a nonlinear one.

**Non-injectivity of $\gamma$ is a kernel-of-$\rho$ phenomenon, and it is the bundle-level shadow of a non-faithful representation.** Because $\gamma(f)$ acts fibrewise by $\rho(\hat f(p))$, its kernel consists exactly of the gauge transformations whose fibre coordinate lands in $\ker\rho$ pointwise; when $\rho$ is not faithful, $\gamma$ cannot be injective. The archetype is $\operatorname{Ad}\colon SU(2)\to SO(3)$, whose kernel is the centre $\{\pm\mathbf 1\}$: the central gauge transformation $f(p)=p\cdot(-\mathbf 1)$ is invisible to the adjoint (and to any $SO(3)$-)bundle, even though it is a genuine, nontrivial symmetry of the $SU(2)$-bundle. This is not a pathology to be avoided but a structural feature that organises much of low-dimensional gauge theory: it is why $SU(2)$- and $SO(3)$-gauge theory differ, why the *centre* of the structure group governs the reducible connections and the stabilisers studied in [[Ex - Stabiliser of a Connection is the Centraliser of its Holonomy|the stabiliser exercise]], and why one must fix the structure group, not merely its adjoint form, before counting instantons. The diagnostic for spaced recall: to test whether an induced gauge map loses information, compute the kernel of the inducing representation — a faithful representation gives an injective $\gamma$, and only the failure of faithfulness produces a kernel, measured by $\ker\rho$.
