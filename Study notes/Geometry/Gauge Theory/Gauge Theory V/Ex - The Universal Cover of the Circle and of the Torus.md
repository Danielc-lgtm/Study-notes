---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group"
  - "Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map"
  - "Def - Discrete Group and Properly Discontinuous Action"
  - "Def - Universal Cover"
  - "Def - Simply Connected Space"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let the circle be $S^1=\{(\cos2\pi t,\sin2\pi t):t\in\mathbb R\}\subset\mathbb R^2$ and the two-torus be $T^2=S^1\times S^1$, and consider the two maps
$$q\colon\mathbb R\to S^1,\qquad q(t)=(\cos2\pi t,\sin2\pi t),\qquad\text{and}\qquad Q\colon\mathbb R^2\to T^2,\qquad Q(x,y)=\big(q(x),q(y)\big).$$

Prove the following.

**Part (i) — the circle.** The map $q\colon\mathbb R\to S^1$ is a smooth covering map; $\mathbb R$ is simply connected, so $q$ is the universal cover of $S^1$; the deck transformation group is
$$\operatorname{Deck}(\mathbb R/S^1)=\{\tau_n\colon t\mapsto t+n\ :\ n\in\mathbb Z\}\ \cong\ \mathbb Z,$$
acting on $\mathbb R$ by translation; and this exhibits $q$ as exactly the principal $\mathbb Z$-bundle produced by [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the quotient theorem of chapter I]] from the translation action of $\mathbb Z$ on $\mathbb R$, so that $S^1\cong\mathbb R/\mathbb Z$.

**Part (ii) — the torus.** The map $Q\colon\mathbb R^2\to T^2$ is a smooth covering map; $\mathbb R^2$ is simply connected, so $Q$ is the universal cover of $T^2$; the deck transformation group is
$$\operatorname{Deck}(\mathbb R^2/T^2)=\{\tau_{(m,n)}\colon(x,y)\mapsto(x+m,y+n)\ :\ (m,n)\in\mathbb Z^2\}\ \cong\ \mathbb Z^2,$$
acting on $\mathbb R^2$ by translation; and this exhibits $Q$ as exactly the principal $\mathbb Z^2$-bundle produced by [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the quotient theorem of chapter I]] from the translation action of $\mathbb Z^2$ on $\mathbb R^2$, so that $T^2\cong\mathbb R^2/\mathbb Z^2$.

In particular, in the notation of [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|the universal-cover theorem]], $\pi_1(S^1)\cong\mathbb Z$ and $\pi_1(T^2)\cong\mathbb Z^2$, recovering [[Thm - Pi_1 of S^1 is Z|the computation of π₁(S¹)]] and [[Ex - Pi_1 of the Torus is Z Squared|of π₁(T²)]] from the deck-group side.

**Recall:**

The objects in play are the universal cover characterised by simple connectedness, the deck transformation group, a properly discontinuous action of a discrete group, and the chapter-I quotient theorem that turns such an action into a smooth covering and principal bundle.

![[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group#Statement]]

We use two features of this theorem. First, its uniqueness clause (part (a)): the universal cover is *the* simply connected covering, unique up to isomorphism over the base; so to identify a given simply connected covering with the universal cover it suffices to check that its total space is simply connected. Second, part (c): once identified, the universal cover is a principal $\pi_1$-bundle whose structure group is the deck group.

![[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map#Statement]]

Applied with $\Gamma=\mathbb Z$ (respectively $\mathbb Z^2$) acting by translation on $M=\mathbb R$ (respectively $\mathbb R^2$), this theorem says that once the action is checked to be smooth and properly discontinuous, the orbit space $\Gamma\backslash M$ is a smooth manifold and $\pi\colon M\to\Gamma\backslash M$ is a smooth covering map; a free properly discontinuous action of a discrete group makes $\pi$ a principal $\Gamma$-bundle with fibre a single $\Gamma$-orbit.

![[Def - Discrete Group and Properly Discontinuous Action#The Definition]]

A discrete group $\Gamma$ acting smoothly on $M$ is **properly discontinuous** when: (i) *local wandering* — every $p\in M$ has a neighbourhood $U$ with $g\cdot U\cap U\ne\varnothing\Rightarrow g=e$; and (ii) *orbit separation* — points $p,q$ in different orbits have neighbourhoods $U\ni p$, $W\ni q$ with $g\cdot U\cap W=\varnothing$ for all $g\in\Gamma$. Equivalently the action is free and proper. Both $\mathbb Z$ and $\mathbb Z^2$ are discrete groups (countable groups with the discrete topology), so this is the relevant notion.

![[Def - Simply Connected Space#The Definition]]

A space is **simply connected** if it is path connected and every loop is null-homotopic relative to its base point, i.e. $\pi_1=0$.

---

# Convergent Strategy

**Problem class.** This is a *verify-a-standard-model* exercise: two of the most-used covering spaces in all of geometry are asserted to have three properties each — covering map, simply connected total space, translation deck group — and the task is to check each property against its definition, then to see that the top-down construction (universal cover of a given base) and the bottom-up construction (quotient of $\mathbb R^n$ by a lattice) yield the *same* principal bundle. Exercises of this class are solved not by cleverness but by writing out each definition and confirming it on explicit coordinates.

**Assumption pattern.** Only two facts are doing real work. The first is that $\mathbb R^n$ is *simply connected*, which is what promotes "a covering" to "the universal cover" through the uniqueness clause of the universal-cover theorem — without it, $q$ and $Q$ would only be some coverings among many. The second is *proper discontinuity* of the lattice translation action, which is what the chapter-I quotient theorem needs as input; here it is visible directly because the lattice moves any small ball entirely off itself. The recognisable trigger is the phrase "$\mathbb R^n\to\mathbb R^n/\Lambda$ for a lattice $\Lambda$": whenever it appears, both facts are available for free from the geometry of the lattice.

**Theorem routing.** For each of $S^1$ and $T^2$ the route is the same three-step chain. First, exhibit the map as a smooth covering — either directly (evenly covered neighbourhoods) or by feeding the translation action into [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the quotient theorem]]. Second, show the total space is simply connected (contractibility of $\mathbb R^n$ via a straight-line null-homotopy), and invoke the uniqueness clause of [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|the universal-cover theorem]] to conclude it is *the* universal cover. Third, compute the deck group by solving $q\circ\varphi=q$: the constraint forces the difference $\varphi(t)-t$ to be an integer-valued continuous function on a connected space, hence a constant integer, so $\varphi$ is a translation. The torus is then the product of two circles, and the two constructions are identified by observing that the acting group in the quotient theorem is literally the deck group of the universal cover.

**Key decision point.** The one place a reader can go wrong is conflating "$q$ is a covering" with "$q$ is *the universal* covering". A covering map alone does not determine the deck group or the fundamental group; the extra input is simple connectedness of the total space, and it enters through the *uniqueness* half of the universal-cover theorem, not the existence half. The second small decision is realising that the deck-group computation is a connectedness argument in disguise: "$\varphi(t)-t\in\mathbb Z$ for all $t$" plus "$\mathbb R$ connected" plus "$\mathbb Z$ discrete" gives "$\varphi(t)-t$ constant", which is the whole content of "every deck transformation is a translation".

---

# Legal Operations Used

This solution deploys the following operations from the chapter's covering-space toolkit; where the topic page is not yet written, each is named descriptively and the coordinator will reconcile the numbering.

1. **Feed a properly discontinuous action into the quotient theorem.** Check that a discrete group acts smoothly and properly discontinuously, then invoke [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the chapter-I quotient theorem]] to obtain a smooth covering map and principal bundle $M\to\Gamma\backslash M$.

2. **Verify proper discontinuity on explicit neighbourhoods.** For a lattice translation action, produce for each point an open ball of radius less than half the shortest lattice vector; the lattice moves it entirely off itself, giving condition (i), and a distance estimate gives condition (ii).

3. **Promote "a covering" to "the universal cover" via simple connectedness.** Show the total space is simply connected (straight-line contraction of any loop in $\mathbb R^n$), then use the uniqueness clause of [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|the universal-cover theorem]] to identify the covering with the universal cover.

4. **Compute a deck group by the covering constraint plus connectedness.** Solve $q\circ\varphi=q$: the difference $\varphi-\operatorname{id}$ takes values in the discrete fibre-shift group, is continuous, and the domain is connected, so it is constant; hence every deck transformation is the corresponding translation.

5. **Take universal covers and fundamental groups of a product factorwise.** The product of the two universal covers is the universal cover of the product, and its deck group is the product of the deck groups, giving the torus from the circle.

---

# Hints

> [!note]- Hint 1
> Treat $S^1$ as $\mathbb R/\mathbb Z$: the group $\mathbb Z$ acts on $\mathbb R$ by $t\mapsto t+n$. Which chapter-I theorem turns "a discrete group acting properly discontinuously" into "a smooth covering map"? What do you have to check about the action before you may use it?

> [!note]- Hint 2
> Proper discontinuity is two conditions. For (i), around any $t_0$ take the open interval of radius $\tfrac12$; a nonzero integer translation moves it entirely off itself. For (ii), if $s,t$ differ by a non-integer, let $\delta$ be the distance from $s-t$ to $\mathbb Z$ and take balls of radius $\delta/3$. Write the two inequalities out.

> [!note]- Hint 3
> A covering is not automatically the *universal* cover. The extra fact is that $\mathbb R$ (and $\mathbb R^2$) is simply connected: any loop $c$ based at $x_0$ contracts along $H(s,\tau)=(1-\tau)c(s)+\tau x_0$. Once the total space is simply connected, the uniqueness clause of the universal-cover theorem says it *is* the universal cover, and the deck group *is* $\pi_1$ of the base.

> [!note]- Hint 4
> To find every deck transformation $\varphi$ of $q\colon\mathbb R\to S^1$, use $q(\varphi(t))=q(t)$, which says $\varphi(t)-t\in\mathbb Z$ for all $t$. The map $t\mapsto\varphi(t)-t$ is continuous into the discrete set $\mathbb Z$ on the connected space $\mathbb R$, so it is a constant integer $n$: thus $\varphi=\tau_n$. For the torus, do everything factorwise: $\mathbb R^2=\mathbb R\times\mathbb R$, $T^2=S^1\times S^1$, deck group $\mathbb Z\times\mathbb Z$.

---

# Solution

The plan is to run the same three-step verification for each space. We first check that the lattice translation action of $\mathbb Z$ (respectively $\mathbb Z^2$) on $\mathbb R$ (respectively $\mathbb R^2$) is smooth and properly discontinuous, so that the chapter-I quotient theorem hands us a smooth covering map and principal bundle; we then contract $\mathbb R^n$ to see the total space is simply connected, which by the uniqueness clause of the universal-cover theorem identifies the covering as *the* universal cover; and we finally compute the deck group directly from the covering constraint, finding it to be the translation lattice. The torus is obtained factorwise from the circle.

**Step 1: The translation action of $\mathbb Z$ on $\mathbb R$ is smooth, free, and properly discontinuous.**

Each $\tau_n(t)=t+n$ is a diffeomorphism, distinct translations are distinct, and small intervals are moved off themselves; conditions (i) and (ii) hold.

> [!note]- Derivation
> We must verify that $\mathbb Z$, acting on $\mathbb R$ by $n\cdot t=t+n$, is a smooth properly discontinuous action of a discrete group. The group $\mathbb Z$ is a discrete group (a countable group with the discrete topology, a $0$-dimensional Lie group). Each group element acts by $\tau_n(t)=t+n$, a smooth map with smooth inverse $\tau_{-n}$, and $(n,t)\mapsto t+n$ is smooth in $t$; so the action is smooth. It is **free**: if $\tau_n(t)=t$ then $t+n=t$, so $n=0$.
>
> **Condition (i), local wandering.** Fix $t_0\in\mathbb R$ and let $U=(t_0-\tfrac12,t_0+\tfrac12)$, the open interval of radius $\tfrac12$. Suppose $\tau_n(U)\cap U\ne\varnothing$ for some $n\in\mathbb Z$, so there are $u,u'\in U$ with $u+n=u'$. Then
> $$|n|=|u'-u|\le|u'-t_0|+|t_0-u|<\tfrac12+\tfrac12=1\qquad\text{(triangle inequality, both points in }U\text{),}$$
> and an integer of absolute value strictly less than $1$ is $n=0$. Hence $\tau_n(U)\cap U\ne\varnothing\Rightarrow n=0$, which is condition (i).
>
> **Condition (ii), orbit separation.** Let $s,t\in\mathbb R$ lie in different orbits, i.e. $s-t\notin\mathbb Z$. Set
> $$\delta:=\operatorname{dist}(s-t,\mathbb Z)=\min_{k\in\mathbb Z}|s-t-k|>0,$$
> which is positive because $s-t\notin\mathbb Z$. Take $U=(t-\tfrac\delta3,t+\tfrac\delta3)$ and $W=(s-\tfrac\delta3,s+\tfrac\delta3)$. For any $u\in U$, $w\in W$ and $n\in\mathbb Z$,
> $$|(u+n)-w|\ge|s-t-(-n)|-|u-t|-|w-s|>\delta-\tfrac\delta3-\tfrac\delta3=\tfrac\delta3>0\qquad\text{(reverse triangle inequality; }|s-t+n|\ge\delta\text{).}$$
> Thus $u+n\ne w$ for all choices, so $\tau_n(U)\cap W=\varnothing$ for every $n$, which is condition (ii).
>
> Therefore the action is smooth, free, and properly discontinuous (conditions (i) and (ii)).

**Step 2: $q\colon\mathbb R\to S^1$ is a smooth covering map and a principal $\mathbb Z$-bundle, and $S^1\cong\mathbb R/\mathbb Z$.**

The quotient theorem applies to the action of Step 1, and $q$ is the resulting quotient map after identifying $\mathbb R/\mathbb Z$ with $S^1$.

> [!note]- Derivation
> By Step 1 the discrete group $\mathbb Z$ acts smoothly and properly discontinuously on $\mathbb R$, so by [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the chapter-I quotient theorem]] the orbit space $\mathbb R/\mathbb Z$ carries a unique smooth structure making the quotient map $\pi\colon\mathbb R\to\mathbb R/\mathbb Z$ a smooth covering map; because the action is in addition free, each fibre $\pi^{-1}(\pi(t))=t+\mathbb Z$ is a single $\mathbb Z$-orbit, and $\pi$ is a principal $\mathbb Z$-bundle.
>
> The map $q\colon\mathbb R\to S^1$, $q(t)=(\cos2\pi t,\sin2\pi t)$, is smooth and satisfies $q(t)=q(t')\iff t-t'\in\mathbb Z$ (the sine and cosine of $2\pi t$ and $2\pi t'$ agree if and only if $2\pi(t-t')\in2\pi\mathbb Z$). Hence $q$ is constant on $\mathbb Z$-orbits and injective on the quotient, so by the universal property of the quotient it descends to a smooth bijection $\bar q\colon\mathbb R/\mathbb Z\to S^1$ with $\bar q\circ\pi=q$. This $\bar q$ is a diffeomorphism — it is a smooth bijection whose inverse is smooth because $q$ is a local diffeomorphism (its derivative $2\pi(-\sin2\pi t,\cos2\pi t)$ never vanishes) and $\pi$ is a local diffeomorphism, so $\bar q$ is a local diffeomorphism, and a bijective local diffeomorphism is a diffeomorphism. This is exactly the content of the chapter-I exercise [[Ex - The Circle as the Quotient of R by the Integers|identifying ℝ/ℤ with S¹]]. Composing, $q=\bar q\circ\pi$ is a smooth covering map and, via $\bar q$, the principal $\mathbb Z$-bundle $\pi$; so $S^1\cong\mathbb R/\mathbb Z$ as claimed.

**Step 3: $\mathbb R$ is simply connected, so $q$ is the universal cover of $S^1$.**

Any loop in $\mathbb R$ contracts to its base point along the straight-line homotopy; hence $\pi_1(\mathbb R)=0$, and the uniqueness clause identifies $q$ as the universal cover.

> [!note]- Derivation
> The space $\mathbb R$ is path connected (any two points are joined by the affine segment between them). Let $c\colon[0,1]\to\mathbb R$ be a loop based at $t_0$, so $c(0)=c(1)=t_0$. Define
> $$H\colon[0,1]\times[0,1]\to\mathbb R,\qquad H(s,\tau)=(1-\tau)\,c(s)+\tau\,t_0.$$
> This is continuous; at $\tau=0$, $H(s,0)=c(s)$; at $\tau=1$, $H(s,1)=t_0$ is the constant loop; and at the endpoints of the loop, $H(0,\tau)=(1-\tau)t_0+\tau t_0=t_0$ and likewise $H(1,\tau)=t_0$, so the homotopy fixes the base point throughout (by $c(0)=c(1)=t_0$). Thus $c$ is null-homotopic relative to $t_0$, and since $c$ was arbitrary, $\pi_1(\mathbb R,t_0)=0$. Being path connected with trivial fundamental group, $\mathbb R$ is [[Def - Simply Connected Space|simply connected]].
>
> By Step 2, $q\colon\mathbb R\to S^1$ is a covering map with simply connected total space $\mathbb R$. By part (a) of [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|the universal-cover theorem]], the universal cover is the simply connected covering and is unique up to isomorphism of coverings over $S^1$; a simply connected covering *is* the universal cover. Therefore $q$ is the universal cover of $S^1$.

**Step 4: The deck group of $q$ is $\mathbb Z$ acting by translation.**

Every homeomorphism $\varphi$ over $S^1$ satisfies $\varphi(t)-t\in\mathbb Z$, a continuous integer-valued function on the connected space $\mathbb R$, hence a constant integer.

> [!note]- Derivation
> A deck transformation of $q$ is a homeomorphism $\varphi\colon\mathbb R\to\mathbb R$ with $q\circ\varphi=q$ (an isomorphism of the covering with itself; by [[Def - Deck Transformation Group|the definition of the deck group]]). The equation $q(\varphi(t))=q(t)$ says $\varphi(t)-t\in\mathbb Z$ for every $t$ (from the fibre description in Step 2). Consider the map
> $$d\colon\mathbb R\to\mathbb Z,\qquad d(t)=\varphi(t)-t,$$
> which is continuous (difference of continuous maps) and takes values in the discrete set $\mathbb Z\subset\mathbb R$. Its domain $\mathbb R$ is connected, and a continuous map from a connected space to a discrete space is constant: if $d$ took two distinct values $n\ne n'$, then $d^{-1}(\{n\})$ and $d^{-1}(\mathbb Z\setminus\{n\})$ would be a separation of $\mathbb R$ into two nonempty disjoint open sets, contradicting connectedness. Hence $d(t)\equiv n$ for a single $n\in\mathbb Z$, that is,
> $$\varphi(t)=t+n=\tau_n(t)\qquad\text{for all }t.$$
> Conversely, every translation $\tau_n$ satisfies $q\circ\tau_n=q$ (since $q$ has period $1$) and is a diffeomorphism, hence a deck transformation. Therefore
> $$\operatorname{Deck}(\mathbb R/S^1)=\{\tau_n:n\in\mathbb Z\},$$
> and $n\mapsto\tau_n$ is a group isomorphism $\mathbb Z\xrightarrow{\cong}\operatorname{Deck}(\mathbb R/S^1)$ because $\tau_m\circ\tau_n=\tau_{m+n}$. This is the same group $\mathbb Z$ whose translation action produced $q$ in Step 2: the deck group of the universal cover *is* the acting group of the chapter-I quotient construction. By part (c) of [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|the universal-cover theorem]], $\pi_1(S^1)\cong\operatorname{Deck}(\mathbb R/S^1)\cong\mathbb Z$, in agreement with [[Thm - Pi_1 of S^1 is Z|the direct computation of π₁(S¹)]].

**Step 5: The torus, factorwise.**

Everything for $T^2=S^1\times S^1$ follows by taking the product of two copies of the circle picture.

> [!note]- Derivation
> The group $\mathbb Z^2$ acts on $\mathbb R^2$ by $(m,n)\cdot(x,y)=(x+m,y+n)$. This action is smooth and free (if $(x+m,y+n)=(x,y)$ then $(m,n)=(0,0)$), and it is properly discontinuous by the same two estimates as Step 1 carried out in the sup norm: for **(i)**, around $(x_0,y_0)$ take the open square $U=(x_0-\tfrac12,x_0+\tfrac12)\times(y_0-\tfrac12,y_0+\tfrac12)$; if $\tau_{(m,n)}(U)\cap U\ne\varnothing$ then $|m|<1$ and $|n|<1$ (each coordinate is the circle estimate), so $(m,n)=(0,0)$. For **(ii)**, if $(x,y)$ and $(x',y')$ lie in different orbits then some coordinate difference is a non-integer, say $x-x'\notin\mathbb Z$ with $\delta=\operatorname{dist}(x-x',\mathbb Z)>0$; the squares of side $\tfrac{2\delta}3$ about the two points satisfy $\tau_{(m,n)}(U)\cap W=\varnothing$ for all $(m,n)$, because already the first coordinate cannot match, by the Step-1 inequality. Hence the action is properly discontinuous.
>
> By [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the chapter-I quotient theorem]], $\mathbb R^2/\mathbb Z^2$ is a smooth manifold and the quotient map is a smooth covering and principal $\mathbb Z^2$-bundle. The map $Q(x,y)=(q(x),q(y))$ has $Q(x,y)=Q(x',y')\iff(x-x',y-y')\in\mathbb Z^2$, so as in Step 2 it descends to a diffeomorphism $\mathbb R^2/\mathbb Z^2\xrightarrow{\cong}S^1\times S^1=T^2$, and $Q$ is a smooth covering map and principal $\mathbb Z^2$-bundle with $T^2\cong\mathbb R^2/\mathbb Z^2$.
>
> The space $\mathbb R^2$ is simply connected by the identical straight-line homotopy $H(s,\tau)=(1-\tau)c(s)+\tau(x_0,y_0)$ (Step 3 verbatim in two coordinates), so by the uniqueness clause $Q$ is the universal cover of $T^2$. Finally, a deck transformation $\varphi$ of $Q$ satisfies $\varphi(x,y)-(x,y)\in\mathbb Z^2$ for all $(x,y)$; the map $(x,y)\mapsto\varphi(x,y)-(x,y)$ is continuous into the discrete set $\mathbb Z^2$ on the connected space $\mathbb R^2$, hence a constant $(m,n)\in\mathbb Z^2$, so $\varphi=\tau_{(m,n)}$ is a translation. Therefore $\operatorname{Deck}(\mathbb R^2/T^2)=\{\tau_{(m,n)}:(m,n)\in\mathbb Z^2\}\cong\mathbb Z^2$, again equal to the acting group of the quotient construction, and by part (c) of the universal-cover theorem $\pi_1(T^2)\cong\mathbb Z^2$, matching [[Ex - Pi_1 of the Torus is Z Squared|the direct computation]]. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** $q\colon\mathbb R\to S^1$ and $Q\colon\mathbb R^2\to T^2$ are the universal covers, with deck groups $\mathbb Z$ and $\mathbb Z^2$ acting by translation, and they are the principal bundles built by the chapter-I quotient theorem from the lattice translation actions.
>
> *The circle.* The discrete group $\mathbb Z$ acts on $\mathbb R$ by $\tau_n(t)=t+n$: smoothly, freely ($\tau_n(t)=t\Rightarrow n=0$), and properly discontinuously — for (i) the interval $(t_0-\tfrac12,t_0+\tfrac12)$ satisfies $\tau_n(U)\cap U\ne\varnothing\Rightarrow|n|<1\Rightarrow n=0$; for (ii) points $s,t$ with $s-t\notin\mathbb Z$ are separated by intervals of radius $\tfrac13\operatorname{dist}(s-t,\mathbb Z)$. By [[Thm - Quotient by a Properly Discontinuous Action is a Manifold and a Covering Map|the chapter-I quotient theorem]], $\pi\colon\mathbb R\to\mathbb R/\mathbb Z$ is a smooth covering and principal $\mathbb Z$-bundle; since $q(t)=q(t')\iff t-t'\in\mathbb Z$ and $q$ is a submersion, $q$ descends to a diffeomorphism $\mathbb R/\mathbb Z\cong S^1$ ([[Ex - The Circle as the Quotient of R by the Integers]]), so $q$ is that covering/bundle. The total space $\mathbb R$ is simply connected (any loop $c$ based at $t_0$ contracts along $H(s,\tau)=(1-\tau)c(s)+\tau t_0$, which fixes $t_0$), so by the uniqueness clause of [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|the universal-cover theorem]] $q$ is the universal cover. A deck transformation $\varphi$ obeys $q\varphi=q$, i.e. $\varphi(t)-t\in\mathbb Z$; the continuous map $t\mapsto\varphi(t)-t$ into discrete $\mathbb Z$ on connected $\mathbb R$ is a constant $n$, so $\varphi=\tau_n$; conversely each $\tau_n$ is a deck transformation. Hence $\operatorname{Deck}(\mathbb R/S^1)=\{\tau_n\}\cong\mathbb Z$, equal to the acting group, and $\pi_1(S^1)\cong\mathbb Z$.
>
> *The torus.* $\mathbb Z^2$ acts on $\mathbb R^2$ by $\tau_{(m,n)}(x,y)=(x+m,y+n)$; the same estimates in each coordinate (using open squares of side $1$ for (i) and side $\tfrac{2}{3}\operatorname{dist}(\cdot,\mathbb Z)$ for (ii)) show the action is smooth, free, and properly discontinuous, so $\mathbb R^2/\mathbb Z^2$ is a smooth covering and principal $\mathbb Z^2$-bundle; $Q$ descends to a diffeomorphism $\mathbb R^2/\mathbb Z^2\cong T^2$. $\mathbb R^2$ is simply connected by the same straight-line contraction, so $Q$ is the universal cover; a deck transformation is a constant $\mathbb Z^2$-translation by the connectedness argument, so $\operatorname{Deck}(\mathbb R^2/T^2)\cong\mathbb Z^2$ and $\pi_1(T^2)\cong\mathbb Z^2$. In both cases the deck group of the universal cover coincides with the discrete group whose properly discontinuous action the chapter-I theorem quotiented, so the top-down universal cover and the bottom-up lattice quotient are the same principal bundle. $\blacksquare$

> [!warning] A tempting shortcut that skips the load-bearing hypothesis
> It is tempting to argue "$q$ is a covering map, therefore its deck group is $\pi_1(S^1)$, therefore $\mathbb Z$." This inverts the logic. A covering map has $\operatorname{Deck}\cong\pi_1$ of the base *only when the covering is the universal (or a normal/regular) cover*; for a general covering the deck group is a proper quotient of a subgroup of $\pi_1$ and can even be trivial (as for a connected double cover of a space with $\pi_1=\mathbb Z/3$). The step that licenses "$\operatorname{Deck}\cong\pi_1$" here is precisely the simple connectedness of $\mathbb R^n$, checked in Step 3 — omit it and the conclusion does not follow. The correct order is: covering $\to$ simply connected total space $\to$ universal cover $\to$ deck group is $\pi_1$.

---

# Key Takeaways

**A lattice quotient $\mathbb R^n\to\mathbb R^n/\Lambda$ is the cleanest example of the whole covering-space machine, and it is worth holding as the mental picture behind every later flat-bundle statement.** Two facts about $\mathbb R^n$ make it work and neither is accidental: it is contractible, hence simply connected, so its quotients are automatically covered by *the* universal cover; and a lattice $\Lambda\cong\mathbb Z^n$ acts by translations that move any bounded set entirely off itself once the shift exceeds the set's diameter, which is proper discontinuity in its most visible form. Every torus $T^n=\mathbb R^n/\mathbb Z^n$, every flat manifold, and every crystallographic quotient is an instance of the same three-line verification carried out here. The transferable diagnostic: to recognise a universal cover, do not look for a "biggest" covering — look for a *simply connected* total space, because that single property, via the uniqueness clause of the universal-cover theorem, pins down the universal cover and forces the deck group to be $\pi_1$.

**The deck group of a lattice quotient is computed by a connectedness argument, not by algebraic topology.** The computation "$\operatorname{Deck}(\mathbb R/S^1)=\mathbb Z$" needed no path lifting and no covering-space Galois theory: the covering constraint $q\circ\varphi=q$ forced $\varphi(t)-t$ into the discrete group $\mathbb Z$, and continuity on the connected line collapsed that to a single integer. The same three ingredients — a covering relation that constrains a difference to a discrete set, continuity of the difference, connectedness of the domain — recur whenever one identifies the automorphisms of a regular covering, and they are cheaper than lifting loops. When you next need the deck group of an explicit covering, first try to solve $p\circ\varphi=p$ pointwise and read off that $\varphi$ shifts by an element of a discrete group that is then forced to be constant; only if the total space is disconnected or the constraint is not discrete do you need heavier tools.

**The two constructions of the same bundle — top-down and bottom-up — meet exactly at the deck group, and this is the bridge that lets chapter V build flat bundles from representations.** Read one way, $q\colon\mathbb R\to S^1$ is the universal cover of a given space $S^1$, and part (c) of the universal-cover theorem promotes it to a principal $\pi_1(S^1)$-bundle. Read the other way, $q$ is what the chapter-I quotient theorem manufactures from the abstract translation action of $\mathbb Z$ on $\mathbb R$, a principal $\mathbb Z$-bundle. These coincide because the deck group *is* the acting group, $\pi_1(S^1)\cong\mathbb Z$. That coincidence is not a curiosity: it is precisely the input to [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the flat-connection–monodromy correspondence]], which builds a flat $G$-bundle over $M$ by extending the structure group of the principal $\pi_1(M)$-bundle $\tilde M\to M$ along a representation $\rho\colon\pi_1(M)\to G$. Having $\tilde M\to M$ concretely in hand as a lattice quotient — as here for $S^1$ and $T^2$ — is what turns that abstract correspondence into computable examples such as [[Ex - Flat U(1)-Connections on the Torus|the flat U(1)-connections on the torus]], where the representation variety $\operatorname{Hom}(\mathbb Z^n,U(1))=U(1)^n$ is read straight off the deck group $\mathbb Z^n$ computed here.
