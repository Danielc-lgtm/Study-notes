---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Flat Connections and Monodromy Representations of the Fundamental Group"
  - "Def - Associated Bundle"
  - "Thm - Sections of an Associated Bundle are Equivariant Functions"
  - "Def - Flat Connection"
  - "Def - Representation of a Lie Group"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $M$ be a connected smooth manifold with base point $m\in M$, write $\Gamma=\pi_1(M,m)$ for its fundamental group, and let $q\colon\tilde M\to M$ be the universal cover, regarded as a principal $\Gamma$-bundle with the right deck action $\tilde x\cdot[\gamma]$. Let $\rho\colon\Gamma\to GL(V)$ be a representation of $\Gamma$ on a finite-dimensional vector space $V$ (over $\mathbb R$ or $\mathbb C$), and let
$$E=\tilde M\times_\rho V$$
be the associated flat vector bundle, equipped with its canonical flat covariant derivative $\nabla=\nabla_\rho$ — the connection whose horizontal sections in the equivariant-function picture are the *constant* functions, characterised by $q^\ast(\nabla s)=d\hat s$ for the $\Gamma$-equivariant map $\hat s\colon\tilde M\to V$ representing a section $s\in\Gamma(E)$.

Prove the following two statements.

**Part (i).** The vector space of global $\nabla$-parallel sections of $E$ is naturally isomorphic to the subspace of $\rho(\Gamma)$-invariant vectors of $V$:
$$\big\{\,s\in\Gamma(E):\nabla s=0\,\big\}\ \xrightarrow{\ \cong\ }\ V^{\rho(\Gamma)}:=\big\{\,v\in V:\rho([\gamma])v=v\ \text{ for all }[\gamma]\in\Gamma\,\big\},\qquad s\mapsto\hat s(\tilde m),$$
where $\tilde m\in q^{-1}(m)$ is a fixed lift of the base point. In particular the number of independent global parallel sections equals $\dim V^{\rho(\Gamma)}$.

**Part (ii).** The flat bundle $(E,\nabla)$ is **trivial as a flat bundle** — that is, there is an isomorphism of vector bundles $\Psi\colon M\times V\to E$ carrying the product (trivial) flat connection $d$ on $M\times V$ to $\nabla$, equivalently $E$ admits a global $\nabla$-parallel frame — **if and only if $\rho$ is the trivial representation** $\rho([\gamma])=\operatorname{id}_V$ for every $[\gamma]\in\Gamma$.

**Recall:**

The objects in play are the universal cover as a principal $\pi_1$-bundle, the associated bundle $\tilde M\times_\rho V$ together with its equivariant-function description of sections, the canonical flat connection of a representation, and the flat-connection–monodromy dictionary.

![[Thm - Flat Connections and Monodromy Representations of the Fundamental Group#Statement]]

![[Thm - Sections of an Associated Bundle are Equivariant Functions#Statement]]

Applied with the principal bundle $P=\tilde M$, structure group $G=\Gamma$ (a discrete group acting on the right by deck transformations), and the representation $\rho\colon\Gamma\to GL(V)$, this theorem gives a $\mathbb R$-linear (indeed $C^\infty(M)$-module) bijection between sections $s\in\Gamma(E)$ and $\rho$-equivariant functions
$$\hat s\colon\tilde M\to V,\qquad \hat s(\tilde x\cdot[\gamma])=\rho([\gamma])^{-1}\,\hat s(\tilde x)\quad\text{for all }\tilde x\in\tilde M,\ [\gamma]\in\Gamma,$$
determined by $s(q(\tilde x))=[\tilde x,\hat s(\tilde x)]$. The inverse of $\rho([\gamma])$ appears because the associated bundle is glued by $(\tilde x,v)\cdot[\gamma]=(\tilde x\cdot[\gamma],\rho([\gamma])^{-1}v)$, the rule that turns the left action $\rho$ into a right action so that the quotient is available (see [[Def - Associated Bundle]]).

![[Def - Flat Connection#The Definition]]

The single fact about the canonical flat connection we use is its equivariant-function description, part (a) of the monodromy theorem: for $s\in\Gamma(E)$ with equivariant representative $\hat s$,
$$q^\ast(\nabla s)=d\hat s,\qquad\text{so}\qquad \nabla s=0\iff d\hat s=0.$$
Here $q\colon\tilde M\to M$ is the covering projection; because $q$ is a local diffeomorphism (indeed a smooth covering, by [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|the universal-cover theorem]]), the pullback $q^\ast$ is injective on forms, so $\nabla s$ vanishes exactly when $d\hat s$ does.

![[Def - Representation of a Lie Group#The Definition]]

We also use that the universal cover $\tilde M$ is **connected**: it is simply connected by construction, and a simply connected space is connected. Consequently a smooth $V$-valued function on $\tilde M$ with vanishing differential is constant.

---

# Convergent Strategy

**Problem class.** This is a *translate-a-geometric-condition-into-representation-theory* problem: both a global geometric object (a parallel section, a flat trivialisation) and its representation-theoretic shadow ($\rho$-invariant vectors, triviality of $\rho$) are being matched, and the matching is done entirely through the equivariant-function description of an associated bundle. Problems of this class are solved by refusing to compute in the bundle $E$ at all and instead lifting everything to the total space $\tilde M$ of the principal bundle, where sections become honest $V$-valued functions and the connection becomes the ordinary exterior derivative.

**Assumption pattern.** Two hypotheses do all the work, each used exactly once. *Flatness* of $\nabla$ is used through the identity $q^\ast(\nabla s)=d\hat s$: it is what lets "parallel" ($\nabla s=0$) become "constant differential" ($d\hat s=0$). *Connectedness* of $\tilde M$ (from simple connectedness) is what upgrades "locally constant" to "globally constant". The recognisable trigger is the phrase "global parallel section of a flat bundle": whenever it appears, the move is to pass to the universal cover, where parallel means constant.

**Theorem routing.** The route for Part (i) is: use [[Thm - Sections of an Associated Bundle are Equivariant Functions|the equivariant-function theorem]] to write $s$ as $\hat s\colon\tilde M\to V$ with $\hat s(\tilde x[\gamma])=\rho([\gamma])^{-1}\hat s(\tilde x)$; use part (a) of [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the monodromy correspondence]] to turn $\nabla s=0$ into $d\hat s=0$; use connectedness of $\tilde M$ to turn $d\hat s=0$ into $\hat s\equiv v_0$ constant; feed the constant into the equivariance law to get $\rho([\gamma])v_0=v_0$; read off the isomorphism $s\mapsto v_0=\hat s(\tilde m)$ onto $V^{\rho(\Gamma)}$. Part (ii) is then a corollary: a flat trivialisation is the same thing as a global parallel frame, a parallel frame is $\dim V$ independent parallel sections, and by Part (i) that many exist if and only if $V^{\rho(\Gamma)}=V$, which says precisely that $\rho$ is trivial.

**Key decision point.** The one genuinely non-obvious move is to *lift the entire problem to $\tilde M$ before doing anything else*. On $E$ itself, "parallel" is a first-order differential condition tangled up with the twisting of the bundle, and there is no obvious way to see the invariant vectors. On $\tilde M$ the bundle untwists — the pullback $q^\ast E$ is the *trivial* bundle $\tilde M\times V$ with the *trivial* connection, because pulling a flat connection back to a simply connected space kills its holonomy — and the section becomes a plain function whose parallelism is just constancy. Every subtlety of the problem is absorbed into the single equivariance law the constant must satisfy. The secondary decision, in Part (ii), is to recognise that "trivial as a flat bundle" is not a statement about $E$ as a bare bundle but about the existence of a parallel frame, which is exactly a basis' worth of the parallel sections that Part (i) has already counted.

---

# Legal Operations Used

This solution deploys the following operations from the chapter's flat-connections toolkit; where the topic page is not yet written, each is named descriptively and the coordinator will reconcile the numbering.

1. **Lift a section of an associated bundle to an equivariant function on the total space.** By [[Thm - Sections of an Associated Bundle are Equivariant Functions|the equivariant-function theorem]], every $s\in\Gamma(E)$ is $s(q(\tilde x))=[\tilde x,\hat s(\tilde x)]$ for a unique $\hat s\colon\tilde M\to V$ satisfying $\hat s(\tilde x[\gamma])=\rho([\gamma])^{-1}\hat s(\tilde x)$, and the correspondence $s\leftrightarrow\hat s$ is a linear bijection. This is the operation that converts every geometric question about $E$ into a question about functions on $\tilde M$.

2. **Replace parallelism by constancy of the differential using flatness.** By part (a) of [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the monodromy correspondence]], the canonical flat connection satisfies $q^\ast(\nabla s)=d\hat s$; since $q$ is a local diffeomorphism, $\nabla s=0\iff d\hat s=0$. This turns a differential-geometric condition into an ordinary calculus condition on $\tilde M$.

3. **Upgrade locally constant to globally constant on a connected space.** A smooth map $\hat s\colon\tilde M\to V$ with $d\hat s=0$ is constant on the connected manifold $\tilde M$; the universal cover is connected because it is simply connected.

4. **Read a functional-equation constraint off a constant.** Substituting the constant value $\hat s\equiv v_0$ into the equivariance law $\hat s(\tilde x[\gamma])=\rho([\gamma])^{-1}\hat s(\tilde x)$ collapses it to the single algebraic constraint $\rho([\gamma])v_0=v_0$, i.e. $v_0\in V^{\rho(\Gamma)}$.

5. **Recognise a flat trivialisation as a global parallel frame.** A bundle isomorphism $M\times V\to E$ intertwining the trivial connection $d$ with $\nabla$ is the same datum as a $\dim V$-tuple of $\nabla$-parallel sections that is a basis of one — hence, by parallel transport, of every — fibre. This converts the triviality question of Part (ii) into a counting question answered by Part (i).

---

# Hints

> [!note]- Hint 1
> Do not try to work inside $E$. A section of $E=\tilde M\times_\rho V$ is the same thing as a function $\hat s\colon\tilde M\to V$ on the universal cover, subject to one twisting law. Write down that law, and write down what "$\nabla s=0$" becomes for $\hat s$.

> [!note]- Hint 2
> The equivariance law is $\hat s(\tilde x\cdot[\gamma])=\rho([\gamma])^{-1}\hat s(\tilde x)$ (the inverse is forced by the gluing convention of the associated bundle). Flatness says $q^\ast(\nabla s)=d\hat s$, so $\nabla s=0$ means $d\hat s=0$. What does a function with vanishing differential look like on a *connected* space — and is $\tilde M$ connected?

> [!note]- Hint 3
> Since $\tilde M$ is connected (it is simply connected), $d\hat s=0$ forces $\hat s\equiv v_0$ for a single vector $v_0\in V$. Now put $\hat s\equiv v_0$ into the equivariance law: it becomes $v_0=\rho([\gamma])^{-1}v_0$ for every $[\gamma]$, i.e. $\rho([\gamma])v_0=v_0$. That is exactly the condition $v_0\in V^{\rho(\Gamma)}$. Check that $s\mapsto v_0=\hat s(\tilde m)$ is linear and invertible (its inverse extends an invariant vector to the constant function).

> [!note]- Hint 4
> For Part (ii): "trivial as a flat bundle" means $E$ has a global frame made of parallel sections. A frame is $\dim V$ pointwise-linearly-independent sections; parallel sections are independent at one point if and only if at every point (parallel transport is an isomorphism). By Part (i) the parallel sections are $V^{\rho(\Gamma)}$, so you have a full parallel frame exactly when $V^{\rho(\Gamma)}=V$ — that is, when every vector is fixed by every $\rho([\gamma])$, which says $\rho([\gamma])=\operatorname{id}_V$ for all $[\gamma]$.

---

# Solution

The whole solution consists of lifting to the universal cover, where the flat bundle untwists into a trivial one and a parallel section becomes a constant function. The equivariance law that a section must obey then squeezes the constant into the invariant subspace $V^{\rho(\Gamma)}$, giving Part (i); Part (ii) follows by asking when there are enough invariant vectors to form a whole frame, which happens precisely when the representation fixes everything.

**Step 1: Rewrite a section as an equivariant function on $\tilde M$.**

Every section $s\in\Gamma(E)$ is encoded by a unique $\rho$-equivariant function $\hat s\colon\tilde M\to V$, and the encoding is a linear bijection.

> [!note]- Derivation
> We assume throughout that $M$ is connected with base point $m$, that $q\colon\tilde M\to M$ is the universal cover carrying the right deck action of $\Gamma=\pi_1(M,m)$, and that $\rho\colon\Gamma\to GL(V)$ is a representation; we must eventually show that the parallel sections of $E=\tilde M\times_\rho V$ are the invariant vectors of $V$.
>
> By [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|the universal-cover theorem]], $q\colon\tilde M\to M$ is a principal $\Gamma$-bundle for the discrete group $\Gamma$, and $\tilde M$ is a connected smooth manifold (it is simply connected, hence connected). Apply [[Thm - Sections of an Associated Bundle are Equivariant Functions|the equivariant-function theorem]] with principal bundle $P=\tilde M$, structure group $G=\Gamma$, and representation $\rho$. It gives a linear bijection
> $$\Gamma(E)\ \xrightarrow{\ \cong\ }\ C^\infty(\tilde M;V)^\Gamma:=\big\{\hat s\colon\tilde M\to V\ \text{smooth}\ :\ \hat s(\tilde x\cdot[\gamma])=\rho([\gamma])^{-1}\hat s(\tilde x)\ \ \forall\tilde x\in\tilde M,\ [\gamma]\in\Gamma\big\},\qquad s\mapsto\hat s,$$
> determined by
> $$s(q(\tilde x))=[\tilde x,\hat s(\tilde x)]\qquad\text{(defining relation of the equivariant-function theorem).}\tag{1}$$
> The inverse $\rho([\gamma])^{-1}$ in the equivariance law is not a choice: the associated bundle is the quotient of $\tilde M\times V$ by the right action $(\tilde x,v)\cdot[\gamma]=(\tilde x\cdot[\gamma],\rho([\gamma])^{-1}v)$, and this is a right action *only* with the inverse (otherwise the composition law $\rho([\gamma_2])\rho([\gamma_1])$ comes out in the wrong order — see the non-example on [[Def - Associated Bundle]]). We record the law as
> $$\hat s(\tilde x\cdot[\gamma])=\rho([\gamma])^{-1}\hat s(\tilde x).\tag{2}$$

**Step 2: A section is parallel if and only if its lift is constant.**

Flatness turns $\nabla s=0$ into $d\hat s=0$, and connectedness of $\tilde M$ turns that into $\hat s\equiv v_0$ for a single vector $v_0\in V$.

> [!note]- Derivation
> By part (a) of [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the monodromy correspondence]], the canonical flat connection $\nabla$ on $E$ is characterised by
> $$q^\ast(\nabla s)=d\hat s\qquad\text{(equation (47) of Haydys with local connection form }a=0\text{).}\tag{3}$$
> The projection $q$ is a smooth covering map, hence a local diffeomorphism (by [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|the universal-cover theorem]]); a local diffeomorphism has injective pullback on differential forms, because in local coordinates $q^\ast$ is composition with an invertible Jacobian. Therefore, from $(3)$,
> $$\nabla s=0\iff q^\ast(\nabla s)=0\iff d\hat s=0\qquad\text{(injectivity of }q^\ast\text{ on 1-forms, then (3)).}\tag{4}$$
> Now suppose $s$ is parallel, so $d\hat s=0$ by $(4)$. The manifold $\tilde M$ is connected (Step 1). A smooth map $\hat s\colon\tilde M\to V$ into a finite-dimensional vector space with $d\hat s=0$ is locally constant — in any chart each component has all partial derivatives zero, hence is constant on the chart's connected domain — and a locally constant map on a connected space is constant. Thus there is a single vector $v_0\in V$ with
> $$\hat s(\tilde x)=v_0\qquad\text{for all }\tilde x\in\tilde M.\tag{5}$$
> Conversely, if $\hat s\equiv v_0$ is constant then $d\hat s=0$, so $\nabla s=0$ by $(4)$; constancy is thus equivalent to parallelism.

**Step 3: The constant value is a $\rho(\Gamma)$-invariant vector, and this gives the isomorphism of Part (i).**

Substituting the constant $(5)$ into the equivariance law $(2)$ forces $v_0\in V^{\rho(\Gamma)}$, and the assignment $s\mapsto v_0$ is a linear isomorphism onto $V^{\rho(\Gamma)}$.

> [!note]- Derivation
> Let $s$ be parallel with constant lift $\hat s\equiv v_0$ as in $(5)$. Evaluate the equivariance law $(2)$ at any $\tilde x$ and any $[\gamma]\in\Gamma$: since $\hat s$ is constant, both sides use the value $v_0$, giving
> $$v_0=\hat s(\tilde x\cdot[\gamma])=\rho([\gamma])^{-1}\hat s(\tilde x)=\rho([\gamma])^{-1}v_0\qquad\text{(by (2) and (5)).}$$
> Applying $\rho([\gamma])$ to both ends,
> $$\rho([\gamma])v_0=v_0\qquad\text{for every }[\gamma]\in\Gamma,$$
> which is exactly the statement $v_0\in V^{\rho(\Gamma)}$. (The inverse is harmless here: as $[\gamma]$ ranges over the group $\Gamma$, so does $[\gamma]^{-1}$, so the conditions $\rho([\gamma])^{-1}v_0=v_0$ for all $[\gamma]$ and $\rho([\gamma])v_0=v_0$ for all $[\gamma]$ are identical.)
>
> **The map is well defined and linear.** Define
> $$T\colon\{s\in\Gamma(E):\nabla s=0\}\to V^{\rho(\Gamma)},\qquad T(s):=\hat s(\tilde m)=v_0,$$
> the value of the (constant) lift at the fixed lift $\tilde m$ of the base point; by the previous paragraph $v_0\in V^{\rho(\Gamma)}$, so $T$ lands in the invariant subspace. It is linear because $s\mapsto\hat s$ is linear (Step 1) and evaluation at $\tilde m$ is linear.
>
> **The map is injective.** If $T(s)=0$ then the constant lift is $\hat s\equiv 0$, so $s(q(\tilde x))=[\tilde x,0]=0$ for all $\tilde x$ by $(1)$, i.e. $s=0$.
>
> **The map is surjective.** Let $v_0\in V^{\rho(\Gamma)}$. Define $\hat s\colon\tilde M\to V$ by the constant $\hat s\equiv v_0$. It is equivariant: for any $[\gamma]$,
> $$\hat s(\tilde x\cdot[\gamma])=v_0=\rho([\gamma])^{-1}v_0=\rho([\gamma])^{-1}\hat s(\tilde x)\qquad\text{(the middle equality is }v_0\in V^{\rho(\Gamma)}\text{),}$$
> so by Step 1 it is the lift of a genuine section $s\in\Gamma(E)$, and by Step 2 that section is parallel (its lift is constant). Finally $T(s)=\hat s(\tilde m)=v_0$. Hence $T$ is onto.
>
> Therefore $T$ is a linear isomorphism
> $$\{s\in\Gamma(E):\nabla s=0\}\ \xrightarrow{\ \cong\ }\ V^{\rho(\Gamma)},$$
> proving Part (i); in particular the two spaces have equal dimension, so there are exactly $\dim V^{\rho(\Gamma)}$ independent global parallel sections.

**Step 4: Parallel sections independent at one point are independent everywhere.**

Because parallel transport is a linear isomorphism, a family of parallel sections that is linearly independent in one fibre is a frame at every point; this is the fact that lets Part (i) count frames.

> [!note]- Derivation
> Let $\sigma_1,\dots,\sigma_r$ be $\nabla$-parallel sections of $E$ and suppose $\sigma_1(x_0),\dots,\sigma_r(x_0)$ are linearly independent in the fibre $E_{x_0}$ for some point $x_0$. Fix any $x\in M$; since $M$ is connected (hence path connected, being a manifold), choose a piecewise smooth path $c$ from $x_0$ to $x$. A parallel section restricts along $c$ to a parallel section of $c^\ast E$, so $\sigma_i(x)=PT_c\big(\sigma_i(x_0)\big)$, where $PT_c\colon E_{x_0}\to E_x$ is parallel transport along $c$ (by [[Def - Parallel Transport in a Principal Bundle|the definition of parallel transport]], the value of a parallel section at the endpoint is the parallel transport of its value at the start). By [[Thm - Properties of Parallel Transport|the properties of parallel transport]], $PT_c$ is a linear isomorphism $E_{x_0}\to E_x$. A linear isomorphism carries a linearly independent set to a linearly independent set, so $\sigma_1(x),\dots,\sigma_r(x)$ are independent in $E_x$. As $x$ was arbitrary, $\sigma_1,\dots,\sigma_r$ are pointwise linearly independent everywhere.
>
> In particular, if $r=\dim V=\operatorname{rank}E$, then $\sigma_1,\dots,\sigma_r$ form a global frame of $E$ consisting of parallel sections — a **global parallel frame**.

**Step 5: The flat bundle is trivial if and only if $\rho$ is trivial (Part (ii)).**

Trivial-as-flat is equivalent to the existence of a global parallel frame; there are enough parallel sections to build one exactly when $V^{\rho(\Gamma)}=V$, which says $\rho$ is trivial.

> [!note]- Derivation
> **Trivial-as-flat $\Rightarrow$ parallel frame.** Suppose $\Psi\colon M\times V\to E$ is a vector-bundle isomorphism carrying the product connection $d$ to $\nabla$, i.e. $\Psi$ intertwines $d$ and $\nabla$. Fix a basis $e_1,\dots,e_r$ of $V$ ($r=\dim V$) and let $\varepsilon_i$ be the constant section $x\mapsto(x,e_i)$ of $M\times V$; these are $d$-parallel and form a global frame. Set $\sigma_i:=\Psi\circ\varepsilon_i\in\Gamma(E)$. Since $\Psi$ carries $d$ to $\nabla$, $\nabla\sigma_i=\Psi(d\varepsilon_i)=0$, so each $\sigma_i$ is parallel; and $\Psi$ is a fibrewise isomorphism, so the $\sigma_i(x)=\Psi(x,e_i)$ form a basis of every $E_x$. Thus $(\sigma_i)$ is a global parallel frame.
>
> **Parallel frame $\Rightarrow$ trivial-as-flat.** Conversely, suppose $\sigma_1,\dots,\sigma_r$ is a global parallel frame ($r=\dim V=\operatorname{rank}E$). Fix a basis $e_1,\dots,e_r$ of $V$ and define
> $$\Psi\colon M\times V\to E,\qquad \Psi\Big(x,\textstyle\sum_i a_i e_i\Big):=\sum_i a_i\,\sigma_i(x).$$
> This is a smooth bundle map, fibrewise linear, and a fibrewise isomorphism because $(\sigma_i(x))$ is a basis of $E_x$ for every $x$; hence a vector-bundle isomorphism. It carries $d$ to $\nabla$: for a constant section $\varepsilon=\sum_i a_i e_i$ we have $\Psi(\varepsilon)=\sum_i a_i\sigma_i$ with constant $a_i$, so $\nabla\Psi(\varepsilon)=\sum_i a_i\nabla\sigma_i=0=\Psi(d\varepsilon)$; and both $d$ and $\nabla$ satisfy the Leibniz rule, so agreement on constant sections and $C^\infty(M)$-linearity of $\Psi$ force $\nabla\circ\Psi=\Psi\circ d$ on all sections. Hence $(E,\nabla)$ is trivial as a flat bundle.
>
> So *trivial-as-flat $\iff$ a global parallel frame exists*. By Step 4 a global parallel frame is $r=\dim V$ pointwise-independent parallel sections, which exist if and only if the space of parallel sections has dimension at least $\dim V$; by Part (i) that space has dimension exactly $\dim V^{\rho(\Gamma)}\le\dim V$. Therefore a parallel frame exists
> $$\iff\ \dim V^{\rho(\Gamma)}=\dim V\ \iff\ V^{\rho(\Gamma)}=V\ \iff\ \rho([\gamma])v=v\ \text{ for all }[\gamma]\in\Gamma,\ v\in V\ \iff\ \rho([\gamma])=\operatorname{id}_V\ \text{ for all }[\gamma],$$
> the last equivalence being the definition of the trivial representation. This proves Part (ii). $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** With $M,m,\Gamma=\pi_1(M,m),q\colon\tilde M\to M,\rho\colon\Gamma\to GL(V)$ and $E=\tilde M\times_\rho V$ with its canonical flat connection $\nabla$ as above:
> (i) $s\mapsto\hat s(\tilde m)$ is a linear isomorphism from $\{s\in\Gamma(E):\nabla s=0\}$ onto $V^{\rho(\Gamma)}$; (ii) $(E,\nabla)$ is trivial as a flat bundle iff $\rho$ is trivial.
>
> By [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|the universal-cover theorem]], $q\colon\tilde M\to M$ is a principal $\Gamma$-bundle with $\tilde M$ a connected (indeed simply connected) smooth manifold and $q$ a local diffeomorphism. By [[Thm - Sections of an Associated Bundle are Equivariant Functions|the equivariant-function theorem]], sections $s\in\Gamma(E)$ correspond linearly and bijectively to functions $\hat s\colon\tilde M\to V$ with $\hat s(\tilde x[\gamma])=\rho([\gamma])^{-1}\hat s(\tilde x)$, via $s(q(\tilde x))=[\tilde x,\hat s(\tilde x)]$.
>
> *(i)* By part (a) of [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the monodromy correspondence]], $q^\ast(\nabla s)=d\hat s$; since $q$ is a local diffeomorphism, $q^\ast$ is injective on forms, so $\nabla s=0\iff d\hat s=0$. On the connected manifold $\tilde M$, $d\hat s=0$ means $\hat s\equiv v_0$ is constant. Feeding $\hat s\equiv v_0$ into the equivariance law gives $v_0=\rho([\gamma])^{-1}v_0$, i.e. $\rho([\gamma])v_0=v_0$ for all $[\gamma]$, so $v_0\in V^{\rho(\Gamma)}$. The map $T(s)=\hat s(\tilde m)=v_0$ is linear; it is injective (if $v_0=0$ then $\hat s\equiv0$ so $s=0$) and surjective (a vector $v_0\in V^{\rho(\Gamma)}$ gives the constant equivariant function $\hat s\equiv v_0$, hence a parallel section $s$ with $T(s)=v_0$). Thus $T\colon\{s:\nabla s=0\}\xrightarrow{\cong}V^{\rho(\Gamma)}$.
>
> *(ii)* First, $(E,\nabla)$ is trivial as a flat bundle iff $E$ has a global parallel frame: an intertwining isomorphism $\Psi\colon(M\times V,d)\to(E,\nabla)$ turns the constant frame of $M\times V$ into a parallel frame of $E$, and conversely a parallel frame $(\sigma_i)$ defines $\Psi(x,\sum a_i e_i)=\sum a_i\sigma_i(x)$, a bundle isomorphism intertwining $d$ and $\nabla$ (it maps constant sections to parallel sections and is $C^\infty(M)$-linear, so it intertwines the two Leibniz-rule connections). By [[Thm - Properties of Parallel Transport|parallel transport is a fibrewise isomorphism]], parallel sections independent at one point are independent everywhere, so a parallel frame is exactly $\dim V$ independent parallel sections. By (i) the parallel sections form a space of dimension $\dim V^{\rho(\Gamma)}$, so a parallel frame exists iff $V^{\rho(\Gamma)}=V$, iff every $\rho([\gamma])$ fixes every vector, iff $\rho$ is trivial.
>
> Both parts are proved. $\blacksquare$

> [!warning] A shortcut through the correspondence theorem, and why it needs one extra word
> Part (ii) can also be read directly off part (d) of the monodromy correspondence: flat bundles up to isomorphism are in bijection with conjugacy classes of representations, the product flat bundle $M\times V$ has monodromy the trivial representation, and $E=\tilde M\times_\rho V$ has monodromy $\rho$; so $E$ is flat-trivial iff $[\rho]=[\text{trivial}]$. This is correct, but the tempting last step "$[\rho]=[\text{trivial}]\Rightarrow\rho=\text{trivial}$" needs the observation that the only representation conjugate to the trivial one is the trivial one itself ($a\,\operatorname{id}_V\,a^{-1}=\operatorname{id}_V$). Omitting that word would leave open the (empty, but unaddressed) possibility of a non-trivial representation in the trivial conjugacy class. The parallel-frame argument above avoids the conjugacy bookkeeping entirely, which is why it is the primary route here.

---

# Key Takeaways

**A flat bundle untwists on its own universal cover, and this is the master move for every question about parallel objects.** The pullback of a flat connection to a simply connected space has trivial holonomy, so it becomes the product connection there; concretely, $q^\ast E\cong\tilde M\times V$ with $q^\ast\nabla=d$. Once this is internalised, a whole family of questions collapses to linear algebra: parallel sections of $E$ become constant functions $\tilde M\to V$, parallel frames become constant frames, and the only surviving data is *how the deck group permutes those constants*, which is the equivariance law. The trigger for the move is any global, holonomy-sensitive object on a flat bundle — a parallel section, a parallel frame, a flat trivialisation, a covariantly constant tensor. The diagnostic to carry away: whenever you meet "$\nabla(\text{something})=0$ globally on a flat bundle", lift to the universal cover, where $\nabla$ is $d$ and "$=0$ globally" is "constant", and then let the equivariance under $\pi_1$ do the rest.

**Invariant vectors count parallel sections; a full invariant space means a flat trivialisation.** The clean statement $\{\text{parallel sections}\}\cong V^{\rho(\Gamma)}$ is worth memorising as a dictionary entry: the geometry of the flat bundle sees the representation $\rho$ only through its fixed vectors. This immediately grades triviality. If $\rho$ is trivial, $V^{\rho(\Gamma)}=V$ and the bundle is flat-trivial — it is honestly the product with the product connection. If $\rho$ has *no* nonzero fixed vector (an irreducible non-trivial representation of a group with no trivial subrepresentation), the bundle has *no* nonzero parallel section at all, and is in a strong sense maximally twisted. The intermediate cases, $0<\dim V^{\rho(\Gamma)}<\dim V$, are bundles that split off a trivial flat sub-bundle of rank $\dim V^{\rho(\Gamma)}$ but no more. The transferable principle: on a flat bundle, "how many parallel sections are there?" is never a differential-geometry question — it is the representation-theoretic question "how big is the invariant subspace of the monodromy?".

**Triviality as a flat bundle is much stronger than triviality as a bundle, and the difference is exactly the monodromy.** A rank-$r$ flat bundle over a manifold may well be trivial as a bare vector bundle — the Möbius line bundle over $S^1$ is the only obstruction in rank one, and many higher-rank flat bundles are topologically trivial — while carrying a nontrivial flat connection with nontrivial holonomy. The present exercise measures the *flat* triviality, which remembers the connection, and finds it controlled by whether $\rho$ is the trivial homomorphism, not by any characteristic class. This is the first place in the series where "trivial" must be qualified by the category one is working in, and it is a rehearsal for the moduli-space viewpoint: the representation variety $\mathcal R(M;G)$ is precisely the set of flat bundles-with-connection up to isomorphism, and its single most distinguished point — the class of the trivial representation — is the product flat bundle. Every other point is a flat bundle that no gauge transformation can straighten into a product. The companion exercises [[Ex - A Flat Connection on the Möbius Line Bundle with Holonomy Minus One]] and [[Ex - Flat U(1)-Connections on the Torus]] exhibit the two extremes: a topologically nontrivial flat bundle whose monodromy is forced to be nontrivial, and a family of topologically trivial flat bundles parametrised by their nontrivial monodromy.
