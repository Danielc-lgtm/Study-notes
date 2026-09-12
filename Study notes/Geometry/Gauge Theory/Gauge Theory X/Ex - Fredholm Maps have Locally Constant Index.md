---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Fredholm Map and Its Index"
  - "Def - Fredholm Operator and Index"
  - "Thm - Stability of the Fredholm Property under Small and Compact Perturbations"
  - "Def - Banach Manifold and Smooth Maps between Banach Spaces"
  - "Def - Connected Components"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $X$ and $Y$ be Banach manifolds and let $F\in C^\infty(X;Y)$ be a smooth **Fredholm map**, so that the differential $d_xF\colon T_xX\to T_{F(x)}Y$ is a Fredholm linear operator for every $x\in X$. Prove, using only the two facts that the set $\operatorname{Fred}(E,G)$ of Fredholm operators between two fixed Banach spaces $E,G$ is **open** in the space of all bounded operators and that the index is **locally constant** on $\operatorname{Fred}(E,G)$, that the function
$$g\colon X\to\mathbb{Z},\qquad g(x):=\operatorname{index}d_xF,$$
is constant on each connected component of $X$. Deduce that $\operatorname{index}F$ is well defined when $X$ is connected.

Then exhibit a smooth Fredholm map between Banach manifolds whose domain has two connected components carrying **different** indices, showing that connectedness of the domain is genuinely required for the single number $\operatorname{index}F$ to make sense.

**Recall:**

The objects in play are a Fredholm operator between Banach spaces and its index, a Fredholm map between Banach manifolds, the stability of the Fredholm property under small perturbations, and connected components.

![[Def - Fredholm Operator and Index#The Definition]]

A bounded linear operator $B\colon E\to G$ between Banach spaces is a [[Def - Fredholm Operator and Index|Fredholm operator]] if its kernel $\ker B$ is finite-dimensional, its image $\operatorname{Im}B$ is closed, and its cokernel $\operatorname{coker}B:=G/\operatorname{Im}B$ is finite-dimensional; its **index** is the integer $\operatorname{index}B:=\dim\ker B-\dim\operatorname{coker}B$. We write $\operatorname{Fred}(E,G)\subset\operatorname{Hom}(E,G)$ for the set of such operators inside the Banach space $\operatorname{Hom}(E,G)$ of all bounded linear maps $E\to G$, equipped with the operator-norm topology $\lVert B\rVert=\sup_{\lVert v\rVert\le1}\lVert Bv\rVert$.

![[Def - Fredholm Map and Its Index#The Definition]]

A smooth map $F\in C^\infty(X;Y)$ between [[Def - Banach Manifold and Smooth Maps between Banach Spaces|Banach manifolds]] is a [[Def - Fredholm Map and Its Index|Fredholm map]] if $d_xF$ is a Fredholm operator for every $x\in X$; the local constancy proved below is exactly what lets one define $\operatorname{index}F:=\operatorname{index}d_xF$ for connected $X$. Recall that $F$ being smooth means that in every pair of charts its local representative is a smooth map between open subsets of the model Banach spaces, and that "$C^1$" for a map $\hat{F}\colon\tilde U\subseteq E\to G$ means precisely that the assignment $u\mapsto d_u\hat{F}\in\operatorname{Hom}(E,G)$ is continuous for the operator-norm topology.

The single external input is the stability theorem, whose first part is the only piece we use.

> [!note] Invoked result — stability of the Fredholm property (part (i))
> **[[Thm - Stability of the Fredholm Property under Small and Compact Perturbations|Stability theorem]], part (i).** Let $E,G$ be Banach spaces. Then $\operatorname{Fred}(E,G)$ is open in $\operatorname{Hom}(E,G)$, and the map $\operatorname{index}\colon\operatorname{Fred}(E,G)\to\mathbb{Z}$ is locally constant: for each $B_0\in\operatorname{Fred}(E,G)$ there is $\varepsilon>0$ such that every bounded operator $B$ with $\lVert B-B_0\rVert<\varepsilon$ is again Fredholm and satisfies $\operatorname{index}B=\operatorname{index}B_0$.

We take this result as proved on its own page (in the Hilbert-space setting the whole series uses, which covers every application here); the present exercise is the passage from this operator-level statement to the map-level statement about $x\mapsto\operatorname{index}d_xF$.

---

# Convergent Strategy

**Problem class.** This is a *transport-a-local-fact-to-a-global-conclusion* problem, of the simplest and most frequently recurring kind: an invariant attached pointwise to a map (here the integer index of the differential) is shown to be constant on connected pieces because it is (a) integer-valued and (b) locally constant. The entire content is the implication "locally constant plus integer-valued $\Rightarrow$ constant on connected components", fed by the reason the index is locally constant. Recognising a problem as a member of this class means recognising that no computation is needed — only the two topological inputs and one chart argument to make "locally constant" legitimate on a manifold.

**Assumption pattern.** The hypothesis "$F$ is a Fredholm map" is used in exactly one way: it guarantees that the continuous family of differentials $x\mapsto d_xF$ lands inside $\operatorname{Fred}$, where the openness and local constancy of the index are available. The recognisable trigger is that we have a *pointwise integer invariant* ($\operatorname{index}d_xF$) that we want to be *locally constant*; the mediating fact is always that the invariant is locally constant on the space of objects it is computed from (here $\operatorname{Fred}(E,G)$), and that the objects vary continuously with the point.

**Theorem routing.** The route is: pass to charts so that $d_xF$ becomes a genuine bounded operator between fixed model spaces varying continuously with the point (this is what "$F$ is $C^1$" delivers); observe that composing with the chart isomorphisms leaves the index unchanged, so the chart-level index equals the manifold-level index; feed the continuous family of differentials into the [[Thm - Stability of the Fredholm Property under Small and Compact Perturbations|stability theorem]], whose part (i) makes $\operatorname{index}$ locally constant on $\operatorname{Fred}$; conclude that $g$ is locally constant; finish with the topological lemma that a locally constant map is constant on each [[Def - Connected Components|connected component]].

**Key decision point.** The one move that is easy to skip and must not be is the chart reduction. On a manifold $d_xF$ maps between the *varying* spaces $T_xX$ and $T_{F(x)}Y$, and "$\lVert d_xF-d_{x_0}F\rVert$" is meaningless until both operators act between the same fixed spaces. The decision is to trivialise both tangent bundles locally by charts, note that the chart differentials are Banach-space isomorphisms, and check that pre- and post-composing a Fredholm operator with isomorphisms changes neither the Fredholm property nor the index — only then is "$x\mapsto\operatorname{index}d_xF$ is locally constant" a statement one can prove from operator-norm continuity.

---

# Legal Operations Used

This solution deploys the following legal operations (numbering to be reconciled with the topic page's Legal Operations once it is written):

1. **Localise a manifold statement by passing to charts.** Local constancy is a local property, so it suffices to prove it in a single chart around each point; charts turn the differential into a bounded operator between fixed model Banach spaces.

2. **Trivialise the differential by the chart isomorphisms and use invariance of the index under composition with isomorphisms.** Writing $d_u\hat{F}=d_{F(x)}\psi\circ d_xF\circ(d_x\varphi)^{-1}$ with $d_x\varphi$, $d_{F(x)}\psi$ isomorphisms, read off that $\operatorname{index}d_u\hat{F}=\operatorname{index}d_xF$, so the chart computation returns the same integer as the manifold one.

3. **Feed a continuous family of operators into the stability theorem.** The assignment $u\mapsto d_u\hat{F}$ is continuous into $\operatorname{Hom}(E,G)$ because $\hat{F}$ is $C^1$; its image lies in $\operatorname{Fred}(E,G)$ because $F$ is Fredholm; the stability theorem then supplies openness and local constancy of the index there.

4. **Compose a continuous map with a locally constant one to get a locally constant map.** The composite $u\mapsto d_u\hat{F}\mapsto\operatorname{index}d_u\hat{F}$ is locally constant; unwound with $\varepsilon$ and $\delta$, this is the explicit statement that $g$ is constant on a small ball around every point.

5. **Promote local constancy to constancy on components.** For each integer $c$ the level set $g^{-1}(c)$ is open, and its complement is a union of the other open level sets, so $g^{-1}(c)$ is clopen; intersecting with a connected component, which is connected, forces it to be all or nothing.

---

# Hints

> [!note]- Hint 1
> You are asked to show an integer-valued function on a space is constant on connected pieces. There is a general topological principle for this that needs no computation at all: an integer-valued function that is *locally constant* is automatically constant on each connected component. So the whole task reduces to proving that $x\mapsto\operatorname{index}d_xF$ is locally constant. What does the stability theorem give you about the index of a nearby operator?

> [!note]- Hint 2
> Local constancy of $g$ is a *local* claim, so you may work inside a single chart around a chosen point $x_0$, and a chart around $F(x_0)$. But be careful: $d_xF$ maps between the tangent spaces $T_xX$ and $T_{F(x)}Y$, which change as $x$ moves. To compare $d_xF$ with $d_{x_0}F$ in operator norm you must first make them act between *fixed* Banach spaces. How do the chart maps let you do that, and why does the index survive the change?

> [!note]- Hint 3
> In charts the local representative $\hat{F}\colon\tilde U\subseteq E\to G$ satisfies $d_u\hat{F}=d_{F(x)}\psi\circ d_xF\circ(d_x\varphi)^{-1}$ by the chain rule, where $d_x\varphi\colon T_xX\to E$ and $d_{F(x)}\psi\colon T_{F(x)}Y\to G$ are isomorphisms. Pre- and post-composing a Fredholm operator with isomorphisms sends kernel and cokernel bijectively to kernel and cokernel, so the index is unchanged: $\operatorname{index}d_u\hat{F}=\operatorname{index}d_xF$. Thus it is enough to show $u\mapsto\operatorname{index}d_u\hat{F}$ is locally constant on $\tilde U\subseteq E$.

> [!note]- Hint 4
> Because $\hat{F}$ is $C^1$, the map $u\mapsto d_u\hat{F}\in\operatorname{Hom}(E,G)$ is continuous; because $F$ is Fredholm, its values lie in $\operatorname{Fred}(E,G)$. Now chain two facts: the stability theorem gives $\varepsilon>0$ with $\operatorname{index}B=\operatorname{index}d_{u_0}\hat{F}$ for $\lVert B-d_{u_0}\hat{F}\rVert<\varepsilon$; continuity gives $\delta>0$ with $\lVert d_u\hat{F}-d_{u_0}\hat{F}\rVert<\varepsilon$ for $\lVert u-u_0\rVert<\delta$. Combine them. For the counterexample, forget analysis entirely: take a *disjoint union* of two finite-dimensional spaces of different dimension and map both to the line.

---

# Solution

The proof has no computation in it: the index is locally constant on the operator space by the imported stability theorem, the differentials of a $C^1$ map vary continuously, and a continuous map into a space where the index is locally constant is composed with that locally constant index to give a locally constant integer-valued function on the manifold; an integer-valued locally constant function is constant on connected components. The only real care is the chart reduction that makes "the differentials vary continuously" a meaningful statement between fixed Banach spaces.

**Step 0: Fix the chart data and reduce to a statement between fixed model spaces.**

Local constancy is local, so we fix $x_0\in X$ and produce a neighbourhood on which $g$ is constant.

> [!note]- Derivation
> Choose a chart $(U,\varphi)$ of $X$ about $x_0$, where $\varphi\colon U\to\tilde U$ is a diffeomorphism onto an open subset $\tilde U$ of the model Banach space $E$, and a chart $(V,\psi)$ of $Y$ about $F(x_0)$, where $\psi\colon V\to\tilde V$ is a diffeomorphism onto an open subset of the model Banach space $G$. Since $F$ is continuous we may shrink $U$ so that $F(U)\subseteq V$. The **local representative**
> $$\hat{F}:=\psi\circ F\circ\varphi^{-1}\colon\tilde U\longrightarrow G$$
> is smooth (composition of smooth maps between open subsets of Banach spaces; this is the meaning of "$F$ smooth" together with the smoothness of the transition and chart maps).
>
> For $u\in\tilde U$ write $x=\varphi^{-1}(u)\in U$. By the chain rule for maps between Banach manifolds,
> $$d_u\hat{F}=d_{F(x)}\psi\circ d_xF\circ d_u(\varphi^{-1})=d_{F(x)}\psi\circ d_xF\circ(d_x\varphi)^{-1}\qquad\text{(chain rule; }d_u(\varphi^{-1})=(d_x\varphi)^{-1}\text{ since }\varphi\text{ is a diffeomorphism).}$$
> Here $d_x\varphi\colon T_xX\to E$ and $d_{F(x)}\psi\colon T_{F(x)}Y\to G$ are **bounded linear isomorphisms**, because a chart of a Banach manifold is a diffeomorphism onto an open set and its differential at each point is invertible with bounded inverse.

**Step 1: The index in the chart equals the index on the manifold.**

Composing a Fredholm operator with isomorphisms on either side changes neither the Fredholm property nor the index, so $\operatorname{index}d_u\hat{F}=\operatorname{index}d_xF=g(x)$.

> [!note]- Derivation
> Let $B\colon T_xX\to T_{F(x)}Y$ be Fredholm and let $P:=d_x\varphi$, $Q:=d_{F(x)}\psi$ be the chart isomorphisms, so that $d_u\hat{F}=Q\,B\,P^{-1}$. We check clause by clause that $QBP^{-1}$ is Fredholm with the same index.
>
> - **Kernel.** Since $P^{-1}\colon E\to T_xX$ is a bijection and $Q\colon T_{F(x)}Y\to G$ is injective, $QBP^{-1}v=0$ iff $BP^{-1}v=0$ iff $P^{-1}v\in\ker B$; thus $P$ restricts to a linear isomorphism $\ker(QBP^{-1})\xrightarrow{\ \sim\ }\ker B$, so $\dim\ker(QBP^{-1})=\dim\ker B<\infty$.
> - **Image and cokernel.** As $Q$ is an isomorphism and $P^{-1}$ is surjective, $\operatorname{Im}(QBP^{-1})=Q(\operatorname{Im}B)$; because $Q$ is a homeomorphism it carries the closed subspace $\operatorname{Im}B$ to the closed subspace $Q(\operatorname{Im}B)$, and it induces an isomorphism of quotients $G/Q(\operatorname{Im}B)\cong T_{F(x)}Y/\operatorname{Im}B=\operatorname{coker}B$ (the map $[w]\mapsto[Qw]$ is a well-defined linear bijection). Hence $\operatorname{Im}(QBP^{-1})$ is closed and $\dim\operatorname{coker}(QBP^{-1})=\dim\operatorname{coker}B<\infty$.
>
> Therefore $QBP^{-1}$ is Fredholm and
> $$\operatorname{index}(QBP^{-1})=\dim\ker(QBP^{-1})-\dim\operatorname{coker}(QBP^{-1})=\dim\ker B-\dim\operatorname{coker}B=\operatorname{index}B\qquad\text{(the two isomorphisms above).}$$
> Applying this with $B=d_xF$ gives $\operatorname{index}d_u\hat{F}=\operatorname{index}d_xF=g(\varphi^{-1}(u))$. In particular $d_u\hat{F}\in\operatorname{Fred}(E,G)$ for every $u\in\tilde U$, since $F$ is a Fredholm map and each $d_xF$ is Fredholm.

**Step 2: The chart index is locally constant, by continuity plus the stability theorem.**

The map $u\mapsto d_u\hat{F}$ is continuous into $\operatorname{Fred}(E,G)$, and the index is locally constant there; the composite is therefore locally constant.

> [!note]- Derivation
> Because $\hat{F}$ is $C^1$ (indeed smooth), the assignment
> $$D\colon\tilde U\to\operatorname{Hom}(E,G),\qquad D(u):=d_u\hat{F},$$
> is continuous for the operator-norm topology — this is precisely the definition of $\hat{F}$ being of class $C^1$. By Step 1, $D(\tilde U)\subseteq\operatorname{Fred}(E,G)$.
>
> Fix $u_0\in\tilde U$. By the **[[Thm - Stability of the Fredholm Property under Small and Compact Perturbations|stability theorem]] (part (i))** — for each $B_0\in\operatorname{Fred}(E,G)$ there is $\varepsilon>0$ with $\operatorname{index}B=\operatorname{index}B_0$ whenever $\lVert B-B_0\rVert<\varepsilon$ — applied to $B_0:=D(u_0)$, there is $\varepsilon>0$ such that
> $$\lVert B-D(u_0)\rVert<\varepsilon\ \Longrightarrow\ B\in\operatorname{Fred}(E,G)\text{ and }\operatorname{index}B=\operatorname{index}D(u_0).\tag{$\ast$}$$
> By continuity of $D$ at $u_0$, there is $\delta>0$ with $B(u_0,\delta):=\{u\in E:\lVert u-u_0\rVert<\delta\}\subseteq\tilde U$ and
> $$\lVert u-u_0\rVert<\delta\ \Longrightarrow\ \lVert D(u)-D(u_0)\rVert<\varepsilon\qquad\text{(continuity of }D\text{, with the }\varepsilon\text{ from }(\ast)\text{).}$$
> Combining the last display with $(\ast)$ applied to $B=D(u)$,
> $$\lVert u-u_0\rVert<\delta\ \Longrightarrow\ \operatorname{index}D(u)=\operatorname{index}D(u_0).$$
> That is, $u\mapsto\operatorname{index}d_u\hat{F}$ is constant on $B(u_0,\delta)$.

**Step 3: Transport back to $X$ and conclude local constancy of $g$.**

> [!note]- Derivation
> By Step 1, for every $u\in\tilde U$ we have $\operatorname{index}d_u\hat{F}=g(\varphi^{-1}(u))$, i.e. $g|_U=\big(u\mapsto\operatorname{index}d_u\hat{F}\big)\circ\varphi$. The set $W:=\varphi^{-1}\big(B(u_0,\delta)\big)$ is an open neighbourhood of $x_0=\varphi^{-1}(u_0)$ in $X$ (as $\varphi$ is a homeomorphism), and on it, by Step 2,
> $$g(x)=\operatorname{index}d_{\varphi(x)}\hat{F}=\operatorname{index}d_{u_0}\hat{F}=g(x_0)\qquad\text{for all }x\in W.$$
> Since $x_0\in X$ was arbitrary, $g$ is **locally constant** on $X$.

**Step 4: A locally constant integer-valued function is constant on each connected component.**

> [!note]- Derivation
> Let $c\in\mathbb{Z}$. The level set $g^{-1}(c)$ is **open**: for $x\in g^{-1}(c)$ the neighbourhood $W$ produced in Step 3 has $g\equiv g(x)=c$ on it, so $W\subseteq g^{-1}(c)$. The complement of $g^{-1}(c)$ in $X$ is $\bigcup_{c'\ne c}g^{-1}(c')$, a union of open sets (each level set is open by the same argument), hence open; therefore $g^{-1}(c)$ is also **closed**, i.e. clopen.
>
> Let $C\subseteq X$ be a [[Def - Connected Components|connected component]] and fix $x_1\in C$; set $c:=g(x_1)$. Then $C\cap g^{-1}(c)$ is a clopen subset of the connected space $C$ (intersection of the clopen $g^{-1}(c)$ with $C$), and it is non-empty (it contains $x_1$). A connected space has no proper non-empty clopen subset, so $C\cap g^{-1}(c)=C$, that is $g\equiv c$ on $C$.
>
> Therefore $g$ is **constant on every connected component of $X$**. In particular, if $X$ is connected then $g$ takes a single value, and this common value is by definition $\operatorname{index}F$. $\blacksquare$

**Step 5: Two components of different index.**

> [!note]- Derivation
> Take the disjoint union of two finite-dimensional manifolds of different dimension, which is a Banach manifold with exactly two connected components:
> $$X:=\mathbb{R}\ \sqcup\ \mathbb{R}^2,\qquad Y:=\mathbb{R},\qquad F|_{\mathbb{R}}(t):=t,\quad F|_{\mathbb{R}^2}(a,b):=a.$$
> Both restrictions are smooth, so $F$ is smooth. On the first component the differential is $d_tF=\operatorname{id}_{\mathbb{R}}\colon\mathbb{R}\to\mathbb{R}$, with $\ker=0$ and $\operatorname{coker}=0$, hence Fredholm of index $0=1-1$. On the second component the differential is the projection $d_{(a,b)}F=\operatorname{pr}_1\colon\mathbb{R}^2\to\mathbb{R}$, $(u,v)\mapsto u$, with $\ker=\{0\}\times\mathbb{R}$ (dimension $1$) and $\operatorname{coker}=0$, hence Fredholm of index $1=2-1$. Thus $F$ is a smooth Fredholm map, its index is $0$ on the component $\mathbb{R}$ and $1$ on the component $\mathbb{R}^2$, and there is no single integer $\operatorname{index}F$. This is consistent with Step 4: the index is constant on each component, but *different* components may carry different values, which is exactly why the definition of $\operatorname{index}F$ requires $X$ connected.
>
> The same phenomenon occurs in genuinely infinite dimensions. With $E=G=\ell^2$, let $S\colon\ell^2\to\ell^2$ be the right shift $S(x_1,x_2,\dots)=(0,x_1,x_2,\dots)$ and $S^{*}$ its adjoint the left shift $S^{*}(x_1,x_2,\dots)=(x_2,x_3,\dots)$. On $X:=\ell^2\sqcup\ell^2$ with $Y:=\ell^2$ set $F$ equal to $S$ on the first copy and $S^{*}$ on the second. Each is linear, so its differential at every point is itself; $S$ is injective with $\operatorname{coker}$ of dimension $1$ (the image is $\{y:y_1=0\}$), giving index $-1$, while $S^{*}$ is surjective with $\ker=\operatorname{span}(e_1)$ of dimension $1$, giving index $+1$. Again $F$ is a smooth Fredholm map with two components of unequal index, $-1\ne+1$.

> [!note]- Complete formal solution
> **Claim.** If $F\in C^\infty(X;Y)$ is a Fredholm map between Banach manifolds, then $g(x):=\operatorname{index}d_xF$ is constant on each connected component of $X$; when $X$ is connected, $\operatorname{index}F:=g$ is well defined.
>
> Fix $x_0\in X$. Take charts $\varphi\colon U\to\tilde U\subseteq E$ about $x_0$ and $\psi\colon V\to\tilde V\subseteq G$ about $F(x_0)$ with $F(U)\subseteq V$, and set $\hat{F}:=\psi\circ F\circ\varphi^{-1}$. By the chain rule, for $x=\varphi^{-1}(u)$,
> $$d_u\hat{F}=d_{F(x)}\psi\circ d_xF\circ(d_x\varphi)^{-1}=Q\,d_xF\,P^{-1},$$
> with $P=d_x\varphi$, $Q=d_{F(x)}\psi$ bounded isomorphisms. Composition with isomorphisms sends $\ker$ and $\operatorname{coker}$ isomorphically ($P$ restricts to $\ker(Q\,d_xF\,P^{-1})\cong\ker d_xF$; $Q$ induces $\operatorname{coker}(Q\,d_xF\,P^{-1})\cong\operatorname{coker}d_xF$) and preserves closedness of the image, so $d_u\hat{F}$ is Fredholm with $\operatorname{index}d_u\hat{F}=\operatorname{index}d_xF=g(\varphi^{-1}(u))$.
>
> Because $\hat{F}$ is $C^1$, the map $D\colon u\mapsto d_u\hat{F}$ is continuous into $\operatorname{Hom}(E,G)$, with $D(\tilde U)\subseteq\operatorname{Fred}(E,G)$. By the [[Thm - Stability of the Fredholm Property under Small and Compact Perturbations|stability theorem]] (part (i)) there is $\varepsilon>0$ with $\operatorname{index}B=\operatorname{index}D(u_0)$ whenever $\lVert B-D(u_0)\rVert<\varepsilon$, and by continuity of $D$ there is $\delta>0$ with $\lVert D(u)-D(u_0)\rVert<\varepsilon$ for $\lVert u-u_0\rVert<\delta$; hence $\operatorname{index}D(u)=\operatorname{index}D(u_0)$ on $B(u_0,\delta)$. Transporting through $\varphi$, $g$ equals $g(x_0)$ on the open set $W=\varphi^{-1}(B(u_0,\delta))\ni x_0$. As $x_0$ was arbitrary, $g$ is locally constant.
>
> For each $c\in\mathbb{Z}$ the set $g^{-1}(c)$ is open (local constancy) and its complement, a union of open level sets, is open, so $g^{-1}(c)$ is clopen. On a connected component $C$, taking $c=g(x_1)$ for some $x_1\in C$ makes $C\cap g^{-1}(c)$ a non-empty clopen subset of the connected space $C$, hence all of $C$; so $g\equiv c$ on $C$. When $X$ is connected this is a single value $\operatorname{index}F$.
>
> Finally $F\colon\mathbb{R}\sqcup\mathbb{R}^2\to\mathbb{R}$, $t\mapsto t$ on the first component and $(a,b)\mapsto a$ on the second, is a smooth Fredholm map with index $0$ on $\mathbb{R}$ and index $1$ on $\mathbb{R}^2$, so different components can carry different indices. $\blacksquare$

---

# Key Takeaways

**An integer-valued invariant that is locally constant is constant on connected components, and this is a purely topological fact requiring no estimate.** The strategic recognition here is that the index, being a difference of two integers, cannot vary continuously without being locally constant; and any locally constant function into a discrete space (equivalently, any continuous function into $\mathbb{Z}$) has clopen level sets, so it is constant on each connected piece of its domain. The trigger for reaching for this pattern is the appearance of a *pointwise-defined integer* — a dimension, an index, a degree, a Betti number, a winding number, the number of points in a fibre — that one wishes to globalise. The diagnostic to run is always the same two-part test: is the invariant locally constant (usually because it is locally constant on the space of objects it is read off from, and those objects vary continuously), and is the domain connected (or, if not, one settles for constancy on each component). The same argument shows the mod-$2$ and integer degrees of a proper Fredholm map are locally constant on regular values, and it is the reason the dimension of a manifold is a well-defined invariant of each of its components.

**On a manifold, comparing differentials at different points is meaningless until charts trivialise the varying tangent spaces, and one must check the invariant survives the trivialisation.** The subtle content of this otherwise routine drill is Step 1: $d_xF$ maps $T_xX\to T_{F(x)}Y$, and these spaces move with $x$, so the operator norm $\lVert d_xF-d_{x_0}F\rVert$ is literally undefined until both operators are conjugated by chart isomorphisms into fixed model spaces. The reusable principle is that whenever a proof wants to speak of a *family* of linear maps between fibres of vector bundles varying continuously — differentials, connections, curvatures, symbols of operators — it must first fix local trivialisations, and then verify that the quantity of interest (here the index) is invariant under the change of trivialisation, which acts by pre- and post-composition with isomorphisms. For the index the check is immediate because composition with an isomorphism carries kernel to kernel and cokernel to cokernel; for other quantities the invariance may be exactly the substance of the definition. The transferable diagnostic: if a statement about a "continuously varying operator" on a manifold has no visible chart in sight, the chart reduction is the missing first step, and the invariance check is its silent partner.

**The definition of $\operatorname{index}F$ quietly assumes connectedness, and the two-component example shows the assumption is not a convenience but a necessity.** It is tempting to read "$\operatorname{index}F$" as a single number attached to any Fredholm map, but the exercise makes precise that the number is attached to a *component*, and different components can disagree — trivially so, since even $\mathbb{R}\sqcup\mathbb{R}^2\to\mathbb{R}$ realises indices $0$ and $1$ at once, and $\ell^2\sqcup\ell^2\to\ell^2$ realises $-1$ and $+1$ through shift operators. The lesson for spaced practice is to treat "let $F$ be a Fredholm map of index $d$" as carrying a hidden hypothesis that the domain is connected (or that a component has been fixed), and to be alert that in gauge theory the relevant domains — configuration spaces of connections, Sobolev completions of section spaces — are indeed connected or are worked with one component at a time, which is what licenses the single symbol $\operatorname{index}F$ used throughout the moduli-space dimension counts. When a Fredholm map arises whose domain is a disjoint union (for instance a space of connections split by topological type of the bundle), the index must be recomputed on each piece.
