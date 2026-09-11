---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Frame Bundle of a Vector Bundle"
  - "Def - Reduction and Extension of the Structure Group"
  - "Def - Complex Vector Bundle and Hermitian Structure"
  - "Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group"
  - "Def - Determinant"
  - "Def - Alternating Multilinear Form"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $E\to M$ be a smooth real [[Def - Vector Bundle|vector bundle]] of rank $k$ over a smooth manifold $M$ (Hausdorff, second countable, $C^\infty$), with [[Def - Frame Bundle of a Vector Bundle|frame bundle]] $\operatorname{Fr}(E)$, a principal $GL_k(\mathbb R)$-bundle. A **fibrewise volume form** on $E$ is a nowhere-vanishing section $\mu\in\Gamma(\Lambda^k E^*)$; an **$SL_k(\mathbb R)$-structure** on $E$ is an [[Def - Reduction and Extension of the Structure Group|$SL_k(\mathbb R)$-subbundle]] $P\subseteq\operatorname{Fr}(E)$, where $SL_k(\mathbb R)=\{h\in GL_k(\mathbb R):\det h=1\}$ is the special linear group.

> **Problem (Haydys, Exercise 27).** Prove that there is a canonical one-to-one correspondence between fibrewise volume forms on $E$ and $SL_k(\mathbb R)$-structures on $E$.

The route is to send a volume form $\mu$ to its bundle of **unimodular frames** — the frames on which $\mu$ evaluates to $1$ — and to send an $SL_k(\mathbb R)$-structure $P$ back to the unique volume form that equals $1$ on the frames of $P$. The heart of the argument is the single transformation law $\mu(e\cdot h)=(\det h)\,\mu(e)$, which is what turns "value $1$" into an $SL_k(\mathbb R)$-invariant condition. This is one row of the reductions dictionary; we prove it here in full as a self-contained drill.

**Recall.**

The objects in play are the frame bundle, a $G$-structure (a reduction of the structure group to a subgroup), a fibrewise volume form, the determinant of a linear map through its action on alternating forms, and the transformation of an alternating top form under a change of basis.

A **frame** of $E_m$ is a linear isomorphism $p\colon\mathbb R^k\to E_m$; equivalently the ordered basis $(p_1,\dots,p_k)=(p(\epsilon_1),\dots,p(\epsilon_k))$, where $(\epsilon_1,\dots,\epsilon_k)$ is the standard basis of $\mathbb R^k$. The group $GL_k(\mathbb R)$ acts on the right, fibrewise, by $p\cdot h=p\circ h$, so that
$$(p\cdot h)_i=(p\circ h)(\epsilon_i)=p\Big(\sum_{j=1}^k h_{ji}\,\epsilon_j\Big)=\sum_{j=1}^k h_{ji}\,p_j\qquad(h=(h_{ji})\in GL_k(\mathbb R)).$$
This action is free and transitive on each fibre $\operatorname{Fr}(E_m)$: given frames $p,q$ of $E_m$, the unique $h$ with $p\cdot h=q$ is $h=p^{-1}\circ q$ (see [[Def - Frame Bundle of a Vector Bundle|the frame-bundle page]]).

![[Def - Reduction and Extension of the Structure Group#$G$-structures on a vector bundle]]

Thus, for a closed subgroup $G\le GL_k(\mathbb R)$, a **$G$-structure** on $E$ is a subset $P\subseteq\operatorname{Fr}(E)$ that is an embedded submanifold, is invariant under the restricted right $G$-action ($p\in P,\ g\in G\Rightarrow p\cdot g\in P$), and is itself a principal $G$-bundle over $M$ under $\pi|_P$ with that action. The subgroup $SL_k(\mathbb R)=\{h\in GL_k(\mathbb R):\det h=1\}$ is closed in $GL_k(\mathbb R)$, being the preimage $\det^{-1}(\{1\})$ of a point under the continuous homomorphism $\det\colon GL_k(\mathbb R)\to\mathbb R^\times$.

A **fibrewise volume form** on $E$ is a nowhere-vanishing section $\mu\in\Gamma(\Lambda^k E^*)$; concretely, a smooth choice of a nonzero alternating $k$-linear form $\mu_m\colon E_m\times\cdots\times E_m\to\mathbb R$ for each $m$, smooth in the sense that $m\mapsto\mu_m(s_1(m),\dots,s_k(m))$ is a smooth function for all smooth sections $s_1,\dots,s_k\in\Gamma(E)$. Here $\Lambda^k E^*$ is the top exterior power of the dual bundle, a real line bundle, and a fibrewise volume form is exactly a nowhere-vanishing section of it, that is, a trivialisation of $\Lambda^k E^*$. This is the definition recorded on [[Def - Complex Vector Bundle and Hermitian Structure|the complex-and-Hermitian-structures page]].

The correspondence we prove is one row of the reductions theorem, whose statement we recall and whose $SL_k(\mathbb R)$ row we are proving in detail:

> **Theorem (structures as reductions, the $SL_k(\mathbb R)$ row — [[Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group|reductions theorem]]).** For a real vector bundle $E$ of rank $k$, fibrewise volume forms on $E$ correspond bijectively to $SL_k(\mathbb R)$-structures $P\subseteq\operatorname{Fr}(E)$.

Finally, the determinant enters through its defining action on alternating top forms. By [[Def - Determinant|the definition of the determinant]], for an operator $T$ on a $k$-dimensional real vector space $V$ and any nonzero alternating $k$-linear form $\alpha$ on $V$,
$$\alpha(Tv_1,\dots,Tv_k)=(\det T)\,\alpha(v_1,\dots,v_k)\qquad(v_1,\dots,v_k\in V),$$
which is the basis-evaluation characterisation of $\det$ (an [[Def - Alternating Multilinear Form|alternating $k$-form]] is determined up to scale, and $T$ multiplies it by $\det T$).

---

# Convergent Strategy

**Problem class.** This is a *set-up-a-bijection-between-two-kinds-of-geometric-data* problem: extra fibrewise structure on one side (a volume form) and a reduction of the structure group on the other (an $SL_k(\mathbb R)$-subbundle of frames). Every such correspondence in the subject — metrics $\leftrightarrow O(k)$, orientations $\leftrightarrow GL_k^+(\mathbb R)$, complex structures $\leftrightarrow GL_k(\mathbb C)$, Hermitian metrics $\leftrightarrow U(k)$ — is proved by the *same three-move template*: (1) from the structure, cut out the subset of frames *compatible* with it; (2) show the compatible frames form one orbit of the stabiliser subgroup, so they are a subbundle with that structure group; (3) invert by reconstructing the structure from any compatible frame and checking independence of the choice. Recognising the template is most of the work; the row-specific content is only which subgroup stabilises which structure.

**Assumption pattern.** The recognisable trigger is that the extra structure — the volume form $\mu$ — is an *alternating top form*, and the group that preserves the value of an alternating top form under change of basis is exactly $\{h:\det h=1\}=SL_k(\mathbb R)$. The moment one writes the transformation law $\mu(e\cdot h)=(\det h)\mu(e)$, the special linear group appears on its own: "value unchanged" is "$\det h=1$". So the assumption "$\mu$ is a nowhere-vanishing top form" is used in exactly one way — to convert the geometric condition "$e$ is unimodular for $\mu$" into the algebraic condition "$\det$ of the change of frame is $1$".

**Theorem routing.** The route is: define $P_\mu=\{e\in\operatorname{Fr}(E):\mu(e_1,\dots,e_k)=1\}$; use the *transformation law* (from [[Def - Determinant|the determinant]]) to see that $SL_k(\mathbb R)$ preserves $P_\mu$ and acts freely and transitively on each fibre; use nowhere-vanishing of $\mu$ to see each fibre of $P_\mu$ is non-empty; assemble the local trivialisations of $P_\mu$ from those of $\operatorname{Fr}(E)$ using a smooth unimodular frame to confirm $P_\mu$ is an [[Def - Reduction and Extension of the Structure Group|$SL_k(\mathbb R)$-structure]]. For the inverse, given $P$, define $\mu_P$ on each fibre by declaring $\mu_P(p_1,\dots,p_k)=1$ for $p\in P_m$; use the transformation law again to prove independence of the choice of $p\in P_m$; use local sections of $P$ for smoothness; and check that the two constructions are mutually inverse.

**Key decision point.** The one non-obvious move is *to look at the frames on which $\mu$ equals exactly $1$* — not merely the frames on which $\mu$ is positive, and not the frames on which $\mu$ is nonzero (which is all of them). "Value $\neq0$" is preserved by all of $GL_k(\mathbb R)$ and cuts out nothing; "value $>0$" is preserved by $GL_k^+(\mathbb R)$ and gives the *orientation* row; only "value $=1$" pins the structure group down to $SL_k(\mathbb R)$. The normalisation to the specific number $1$ is what encodes the volume form and distinguishes this row from the orientation row. The second decision, in the inverse direction, is to *define an alternating form by prescribing its value on a single basis* — legitimate precisely because an alternating top form on a $k$-dimensional space is determined by its value on one basis.

---

# Legal Operations Used

This solution deploys the following operations, in the sense of the [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles|topic page's Legal Operations]]; where the topic page is not yet assembled, the operation is named descriptively and will be reconciled by number.

1. **Cut out the compatible sub-frame-bundle.** From the extra structure (here a volume form $\mu$), form the subset of $\operatorname{Fr}(E)$ consisting of frames *compatible* with it — the unimodular frames $\mu(e_1,\dots,e_k)=1$. This is the operation that turns "structure on $E$" into "subset of $\operatorname{Fr}(E)$".

2. **Transform an alternating top form under a change of frame by the determinant.** Apply the identity $\mu(e\cdot h)=(\det h)\,\mu(e)$, which follows from the multilinearity and alternation of $\mu$ and the definition of $\det$; it is the single algebraic fact that drives both directions.

3. **Read a subgroup off an invariance condition.** The frames preserving the value of $\mu$ are exactly those changes of frame with $\det h=1$; hence the stabiliser is $SL_k(\mathbb R)$ and the compatible frames form one $SL_k(\mathbb R)$-orbit per fibre.

4. **Build local trivialisations of a sub-bundle from a compatible local frame.** A smooth unimodular local frame $e_S$ over $U$ gives the chart $(m,h)\mapsto e_S(m)\cdot h$, $U\times SL_k(\mathbb R)\to\pi^{-1}(U)\cap P_\mu$, exhibiting $P_\mu$ as a smooth embedded principal $SL_k(\mathbb R)$-subbundle.

5. **Define an alternating form by its value on one basis, then prove independence of the basis.** In the inverse direction, prescribe $\mu_P(p_1,\dots,p_k)=1$ for $p\in P_m$; the transformation law makes this independent of the choice of $p\in P_m$ because any two such $p$ differ by an element of $SL_k(\mathbb R)$, which fixes the value.

6. **Verify a bijection by composing both ways.** Show $\mu\mapsto P_\mu\mapsto\mu_{P_\mu}=\mu$ and $P\mapsto\mu_P\mapsto P_{\mu_P}=P$, using that a top form is determined by its value on a basis and that $SL_k(\mathbb R)$ acts transitively on the unimodular frames of each fibre.

---

# Hints

> [!note]- Hint 1
> The two sides of the correspondence live in different places: a volume form is a section of a line bundle $\Lambda^k E^*$, while an $SL_k(\mathbb R)$-structure is a subbundle of the frame bundle $\operatorname{Fr}(E)$. To connect them, ask: given $\mu$, which frames does $\mu$ single out? Evaluate $\mu$ on a frame $(e_1,\dots,e_k)$ — you get a nonzero real number. The natural distinguished frames are the ones where this number takes a fixed normalised value. Which value should you normalise to, so that the frames preserving it form a *group*?

> [!note]- Hint 2
> Compute how $\mu(e_1,\dots,e_k)$ changes when you replace the frame $e$ by $e\cdot h$ for $h\in GL_k(\mathbb R)$. Because $\mu$ is alternating and $k$-linear, and $(e\cdot h)_i=\sum_j h_{ji}e_j$, the answer is $\mu(e\cdot h)=(\det h)\,\mu(e)$ — this is just the defining property of the determinant. So the frames with $\mu(e)=1$ are preserved exactly by the $h$ with $\det h=1$: the group $SL_k(\mathbb R)$.

> [!note]- Hint 3
> Set $P_\mu:=\{e\in\operatorname{Fr}(E):\mu(e_1,\dots,e_k)=1\}$. To show it is an $SL_k(\mathbb R)$-structure you must check: (a) $SL_k(\mathbb R)$ preserves $P_\mu$ (Hint 2); (b) each fibre $(P_\mu)_m$ is non-empty — given any frame $e_0$ with $\mu(e_0)=c\neq0$, rescale one vector, e.g. $e_0\cdot\operatorname{diag}(1/c,1,\dots,1)$, to get value $1$; (c) $SL_k(\mathbb R)$ acts freely and transitively on $(P_\mu)_m$ — two unimodular frames differ by an $h$ with $\det h=1$; (d) smoothness/embeddedness — build a smooth unimodular local frame from any local frame and use it as a chart.

> [!note]- Hint 4
> For the inverse, given an $SL_k(\mathbb R)$-structure $P$, define $\mu_P$ on $E_m$ to be the unique alternating $k$-form with $\mu_P(p_1,\dots,p_k)=1$ for one (hence every) $p\in P_m$. "Hence every" is the crux: if $p'\in P_m$ is another, then $p'=p\cdot h$ with $h\in SL_k(\mathbb R)$, so $\mu_P(p')=(\det h)\mu_P(p)=1\cdot1=1$ — the value is forced to be $1$ on all of $P_m$ automatically. Then check $\mu_P$ is nowhere vanishing (it is dual to a basis), smooth (use a local section of $P$), and that $\mu\mapsto P_\mu$ and $P\mapsto\mu_P$ undo each other.

---

# Solution

The whole correspondence turns on one computation — the determinant transformation law $\mu(e\cdot h)=(\det h)\,\mu(e)$ — used twice. Forwards, it says that "$\mu$ evaluates to $1$" is a condition preserved by exactly $SL_k(\mathbb R)$, so the unimodular frames form an $SL_k(\mathbb R)$-subbundle. Backwards, it says that the value of a candidate volume form on the frames of an $SL_k(\mathbb R)$-structure is forced to be constant, so the structure determines a volume form. We first isolate the transformation law, then run the two directions and check they are inverse.

**Step 0: The determinant transformation law for a top form.**

For any frame $e$ of $E_m$, any $h\in GL_k(\mathbb R)$, and any alternating $k$-linear form $\mu_m$ on $E_m$, $\mu_m\big((e\cdot h)_1,\dots,(e\cdot h)_k\big)=(\det h)\,\mu_m(e_1,\dots,e_k)$.

> [!note]- Derivation
> **Goal.** Prove $\mu_m(e\cdot h)=(\det h)\,\mu_m(e)$, writing $\mu_m(e)$ for $\mu_m(e_1,\dots,e_k)$.
>
> Recall $(e\cdot h)_i=\sum_{j=1}^k h_{ji}\,e_j$ (the frame-action formula from the Recall). Let $T\colon E_m\to E_m$ be the linear operator determined on the basis $(e_1,\dots,e_k)$ by $T e_i:=\sum_{j=1}^k h_{ji}e_j=(e\cdot h)_i$; its matrix in the basis $(e_i)$ has $(j,i)$-entry $h_{ji}$, that is, the matrix of $T$ is $h$ itself (its $i$-th column is $(h_{ji})_{j}$). Then
> $$\mu_m(e\cdot h)=\mu_m(Te_1,\dots,Te_k)=(\det T)\,\mu_m(e_1,\dots,e_k)\qquad(\text{by the basis-evaluation property of }\det\text{, }[[Def - Determinant|\text{definition of the determinant}]]),$$
> and $\det T=\det h$ because the matrix of $T$ in the basis $(e_i)$ is $h$ (the determinant of an operator equals the determinant of any of its matrices, [[Def - Determinant|definition of the matrix determinant]]). Hence
> $$\mu_m(e\cdot h)=(\det h)\,\mu_m(e_1,\dots,e_k).$$
> For completeness, the basis-evaluation property is itself immediate from multilinearity and alternation: expanding $\mu_m\big(\sum_{j_1}h_{j_11}e_{j_1},\dots,\sum_{j_k}h_{j_kk}e_{j_k}\big)$ by $k$-linearity gives $\sum_{j_1,\dots,j_k}h_{j_11}\cdots h_{j_kk}\,\mu_m(e_{j_1},\dots,e_{j_k})$; every term with a repeated index vanishes (alternation), leaving the terms where $(j_1,\dots,j_k)=(\sigma(1),\dots,\sigma(k))$ is a permutation $\sigma$, and $\mu_m(e_{\sigma(1)},\dots,e_{\sigma(k)})=\operatorname{sgn}(\sigma)\,\mu_m(e_1,\dots,e_k)$ (alternation), so the sum is $\big(\sum_\sigma\operatorname{sgn}(\sigma)\,h_{\sigma(1)1}\cdots h_{\sigma(k)k}\big)\mu_m(e)=(\det h)\,\mu_m(e)$ by the Leibniz formula for $\det h$. $\blacksquare$

**Step 1: From a volume form $\mu$, build the bundle of unimodular frames $P_\mu$.**

Set $P_\mu:=\{e\in\operatorname{Fr}(E):\mu(e_1,\dots,e_k)=1\}$. Then $P_\mu$ is invariant under the right $SL_k(\mathbb R)$-action, meets every fibre, and $SL_k(\mathbb R)$ acts freely and transitively on each fibre $(P_\mu)_m$.

> [!note]- Derivation
> Fix a fibrewise volume form $\mu\in\Gamma(\Lambda^k E^*)$; by definition each $\mu_m$ is a nonzero alternating $k$-form on $E_m$.
>
> **Invariance under $SL_k(\mathbb R)$.** Let $e\in P_\mu$ (so $\mu(e)=1$) and $h\in SL_k(\mathbb R)$ (so $\det h=1$). By Step 0,
> $$\mu\big((e\cdot h)\big)=(\det h)\,\mu(e)=1\cdot1=1\qquad(\text{Step 0, and }\det h=1\text{ since }h\in SL_k(\mathbb R)),$$
> so $e\cdot h\in P_\mu$. Thus $P_\mu$ is closed under the restricted right $SL_k(\mathbb R)$-action.
>
> **Each fibre is non-empty.** Fix $m\in M$. Choose any frame $e^{(0)}\in\operatorname{Fr}(E_m)$ (frames exist because $E_m$ is a $k$-dimensional vector space). Since $\mu_m\neq0$ and $(e^{(0)}_1,\dots,e^{(0)}_k)$ is a basis, $c:=\mu(e^{(0)})\neq0$ (a nonzero alternating top form is nonzero on any basis). Put $h_0:=\operatorname{diag}(1/c,1,\dots,1)\in GL_k(\mathbb R)$, an invertible matrix with $\det h_0=1/c\neq0$. Then by Step 0,
> $$\mu\big(e^{(0)}\cdot h_0\big)=(\det h_0)\,\mu(e^{(0)})=\tfrac1c\cdot c=1,$$
> so $e^{(0)}\cdot h_0\in(P_\mu)_m$; the fibre is non-empty.
>
> **Freeness.** The $SL_k(\mathbb R)$-action on $(P_\mu)_m$ is the restriction of the free $GL_k(\mathbb R)$-action on $\operatorname{Fr}(E_m)$ (Recall), so it is free: $e\cdot h=e\Rightarrow h=\operatorname{id}$.
>
> **Transitivity.** Let $e,e'\in(P_\mu)_m$, so $\mu(e)=\mu(e')=1$. Since $GL_k(\mathbb R)$ is transitive on $\operatorname{Fr}(E_m)$, there is a unique $h\in GL_k(\mathbb R)$ with $e'=e\cdot h$, namely $h=e^{-1}\circ e'$. Applying Step 0,
> $$1=\mu(e')=\mu(e\cdot h)=(\det h)\,\mu(e)=(\det h)\cdot1=\det h,$$
> so $\det h=1$, that is $h\in SL_k(\mathbb R)$. Hence any two unimodular frames of $E_m$ differ by an element of $SL_k(\mathbb R)$: the action is transitive on $(P_\mu)_m$. $\blacksquare$

**Step 2: $P_\mu$ is a smooth embedded $SL_k(\mathbb R)$-subbundle, i.e. an $SL_k(\mathbb R)$-structure.**

Over any trivialising open $U$ there is a smooth unimodular local frame $e_S\colon U\to P_\mu$, and $(m,h)\mapsto e_S(m)\cdot h$ is a diffeomorphism $U\times SL_k(\mathbb R)\to\pi^{-1}(U)\cap P_\mu$; these charts make $P_\mu$ an embedded submanifold and a principal $SL_k(\mathbb R)$-bundle.

> [!note]- Derivation
> **Goal.** Produce the subbundle charts and verify the clauses of an $SL_k(\mathbb R)$-structure.
>
> **A smooth unimodular local frame.** Let $U\subseteq M$ be open with a smooth local frame $e=(e_1,\dots,e_k)$ of $E$ (these cover $M$ by local triviality of $E$). The function
> $$c(m):=\mu_m\big(e_1(m),\dots,e_k(m)\big)$$
> is smooth (definition of smoothness of $\mu$, applied to the smooth sections $e_i$) and nowhere zero on $U$ (since $\mu_m\neq0$ and the $e_i(m)$ are a basis). Define a new local frame by rescaling the first vector,
> $$e_S:=e\cdot\operatorname{diag}\big(1/c,1,\dots,1\big),\qquad\text{i.e. } (e_S)_1=\tfrac1c\,e_1,\ (e_S)_i=e_i\ (i\geq2).$$
> Each $(e_S)_i$ is a smooth section (as $1/c$ is smooth), so $e_S$ is a smooth local frame; and by Step 0, $\mu(e_S)=\det\!\big(\operatorname{diag}(1/c,1,\dots,1)\big)\,\mu(e)=\tfrac1c\cdot c=1$, so $e_S(m)\in(P_\mu)_m$ for all $m\in U$. Thus $e_S\colon U\to P_\mu$ is a smooth section of $\operatorname{Fr}(E)$ landing in $P_\mu$.
>
> **The subbundle charts.** Define $\Psi^S_U\colon U\times SL_k(\mathbb R)\to\pi^{-1}(U)$ by $\Psi^S_U(m,h)=e_S(m)\cdot h$. Its image lies in $P_\mu$ by the invariance of Step 1 (as $e_S(m)\in P_\mu$ and $h\in SL_k(\mathbb R)$), and by transitivity of $SL_k(\mathbb R)$ on $(P_\mu)_m$ (Step 1) it is onto $\pi^{-1}(U)\cap P_\mu$; it is injective by freeness. Under the ambient frame-bundle chart $\Psi_U(m,g)=e_S(m)\cdot g$ of [[Def - Frame Bundle of a Vector Bundle|$\operatorname{Fr}(E)$]] (which is a diffeomorphism $U\times GL_k(\mathbb R)\to\pi^{-1}(U)$), the map $\Psi^S_U$ is the restriction to the submanifold $U\times SL_k(\mathbb R)\subseteq U\times GL_k(\mathbb R)$. Since $SL_k(\mathbb R)=\det^{-1}(1)$ is an embedded Lie subgroup of $GL_k(\mathbb R)$ (it is closed, being the preimage of a point under the smooth $\det$, and $1$ is a regular value of $\det\colon GL_k(\mathbb R)\to\mathbb R^\times$, so $\det^{-1}(1)$ is an embedded submanifold and a subgroup, hence a Lie subgroup), $U\times SL_k(\mathbb R)\hookrightarrow U\times GL_k(\mathbb R)$ is a smooth embedding; composing with the diffeomorphism $\Psi_U$ shows $\pi^{-1}(U)\cap P_\mu=\Psi_U\big(U\times SL_k(\mathbb R)\big)$ is an embedded submanifold and $\Psi^S_U$ is a diffeomorphism onto it.
>
> **The clauses of an $SL_k(\mathbb R)$-structure.** These charts cover $P_\mu$ (their base opens cover $M$), so $P_\mu$ is a smooth embedded submanifold of $\operatorname{Fr}(E)$. It is invariant under the restricted right $SL_k(\mathbb R)$-action (Step 1). The restricted action is smooth (restriction of the smooth $GL_k(\mathbb R)$-action), free (Step 1), and in the chart $\Psi^S_U$ reads $\big((m,h),h'\big)\mapsto(m,hh')$, so $\pi|_{P_\mu}\colon P_\mu\to M$ with these charts and this action is a principal $SL_k(\mathbb R)$-bundle: the charts are $SL_k(\mathbb R)$-equivariant trivialisations by the same computation as for [[Def - Frame Bundle of a Vector Bundle|the frame bundle]] ($\Psi^S_U(m,h)\cdot h'=e_S(m)\cdot(hh')=\Psi^S_U(m,hh')$). Hence $P_\mu$ is an [[Def - Reduction and Extension of the Structure Group|$SL_k(\mathbb R)$-structure]] on $E$. $\blacksquare$

**Step 3: From an $SL_k(\mathbb R)$-structure $P$, build a fibrewise volume form $\mu_P$.**

For each $m$, let $\mu_P^m$ be the unique alternating $k$-form on $E_m$ with $\mu_P^m(p_1,\dots,p_k)=1$ for one (equivalently every) $p\in P_m$. Then $\mu_P:=\{\mu_P^m\}$ is a nowhere-vanishing smooth section of $\Lambda^k E^*$.

> [!note]- Derivation
> **Existence and independence of the representative.** Fix $m$ and pick any $p\in P_m$ (non-empty because $P\to M$ is a bundle). Since $(p_1,\dots,p_k)$ is a basis of $E_m$, there is a unique alternating $k$-form $\mu_P^m$ on $E_m$ with $\mu_P^m(p_1,\dots,p_k)=1$: an alternating top form is determined by its value on a basis (the space of alternating $k$-forms on a $k$-dimensional space is one-dimensional, [[Def - Alternating Multilinear Form|alternating-uniqueness]]), and the one whose value on the given basis is $1$ is the dual top form $p^1\wedge\cdots\wedge p^k$. We must check this does not depend on the choice of $p\in P_m$. If $p'\in P_m$ is another, then, because $SL_k(\mathbb R)$ is transitive on the fibre $P_m$ (as $P$ is a principal $SL_k(\mathbb R)$-bundle), $p'=p\cdot h$ with $h\in SL_k(\mathbb R)$; hence by Step 0,
> $$\mu_P^m(p'_1,\dots,p'_k)=\mu_P^m(p\cdot h)=(\det h)\,\mu_P^m(p_1,\dots,p_k)=1\cdot1=1,$$
> so the form defined by "value $1$ on $p'$" is the same form (both are the unique alternating $k$-form taking value $1$ on the respective — and on either — basis; they agree on the basis $(p_1,\dots,p_k)$ since both give it value $1$). Thus $\mu_P^m$ is well defined, independent of the representative.
>
> **Nowhere vanishing.** $\mu_P^m\neq0$ because it takes the value $1\neq0$ on the basis $(p_1,\dots,p_k)$; so $\mu_P$ vanishes at no point of $M$.
>
> **Smoothness.** Over a trivialising open $U$ for $P$, choose a smooth local section $s\colon U\to P$ (these exist because $P$ is locally trivial, by [[Thm - Sections of a Principal Bundle and Triviality|the sections–triviality theorem]]: a principal bundle admits a smooth local section over any trivialising open). Then $s(m)=(s_1(m),\dots,s_k(m))$ is a smooth local frame of $E$ (its components $s_i$ are smooth sections of $E$), and by construction $\mu_P^m(s_1(m),\dots,s_k(m))=1$ for all $m\in U$. For arbitrary smooth sections $t_1,\dots,t_k\in\Gamma(E|_U)$, write $t_i=\sum_j a_{ji}s_j$ with smooth coefficients $a_{ji}\in C^\infty(U)$ (expansion in the smooth frame $s$); then by multilinearity and Step 0,
> $$\mu_P^m\big(t_1(m),\dots,t_k(m)\big)=\det\!\big(a_{ji}(m)\big)\,\mu_P^m\big(s_1(m),\dots,s_k(m)\big)=\det\!\big(a_{ji}(m)\big),$$
> a smooth function of $m$ (the determinant is a polynomial in the smooth entries $a_{ji}$). Since this holds for all smooth $t_i$, $\mu_P$ is a smooth section of $\Lambda^k E^*$ (smoothness of a section of $\Lambda^k E^*$ is exactly smoothness of $m\mapsto\mu_P^m(t_1(m),\dots,t_k(m))$ for all smooth $t_i$). Therefore $\mu_P$ is a fibrewise volume form. $\blacksquare$

**Step 4: The two constructions are mutually inverse.**

$\mu\mapsto P_\mu\mapsto\mu_{P_\mu}$ returns $\mu$, and $P\mapsto\mu_P\mapsto P_{\mu_P}$ returns $P$.

> [!note]- Derivation
> **First round trip: $\mu_{P_\mu}=\mu$.** Let $\mu$ be a fibrewise volume form and $P_\mu$ its unimodular-frame bundle (Step 1). By construction of $\mu_{P_\mu}$ (Step 3), at each $m$ the form $\mu_{P_\mu}^m$ is the unique alternating $k$-form taking value $1$ on the frames of $(P_\mu)_m$. But $\mu$ *itself* takes value $1$ on those frames — that is the definition of $P_\mu$. Two alternating top forms that agree on a single basis are equal (one-dimensionality of the space of alternating $k$-forms), and $(P_\mu)_m$ contains a basis (Step 1, non-emptiness); hence $\mu_{P_\mu}^m=\mu_m$ for every $m$, so $\mu_{P_\mu}=\mu$.
>
> **Second round trip: $P_{\mu_P}=P$.** Let $P$ be an $SL_k(\mathbb R)$-structure and $\mu_P$ its volume form (Step 3). By definition (Step 1 applied to $\mu_P$), $P_{\mu_P}=\{e\in\operatorname{Fr}(E):\mu_P(e_1,\dots,e_k)=1\}$. *($P\subseteq P_{\mu_P}$.)* For $p\in P_m$ we have $\mu_P(p_1,\dots,p_k)=1$ by the very definition of $\mu_P$, so $p\in P_{\mu_P}$. *($P_{\mu_P}\subseteq P$.)* Let $e\in(P_{\mu_P})_m$, so $\mu_P(e)=1$. Pick any $p\in P_m$; since $GL_k(\mathbb R)$ is transitive on $\operatorname{Fr}(E_m)$, write $e=p\cdot h$ with $h\in GL_k(\mathbb R)$. Then, by Step 0 and $\mu_P(p)=1$,
> $$1=\mu_P(e)=\mu_P(p\cdot h)=(\det h)\,\mu_P(p)=\det h,$$
> so $h\in SL_k(\mathbb R)$; and because $P$ is invariant under the $SL_k(\mathbb R)$-action with $p\in P_m$, $e=p\cdot h\in P_m$. Hence $P_{\mu_P}=P$ as subsets of $\operatorname{Fr}(E)$, and they carry the same $SL_k(\mathbb R)$-bundle structure (the same subspace with the same restricted action). The two assignments are therefore inverse bijections between fibrewise volume forms and $SL_k(\mathbb R)$-structures. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** For a real vector bundle $E\to M$ of rank $k$, the assignments $\mu\mapsto P_\mu:=\{e\in\operatorname{Fr}(E):\mu(e_1,\dots,e_k)=1\}$ and $P\mapsto\mu_P$ (the unique fibrewise form with $\mu_P(p_1,\dots,p_k)=1$ for $p\in P$) are mutually inverse bijections between fibrewise volume forms and $SL_k(\mathbb R)$-structures on $E$.
>
> **The transformation law.** For a frame $e$ of $E_m$, $h\in GL_k(\mathbb R)$, and an alternating $k$-form $\mu_m$, one has $(e\cdot h)_i=\sum_j h_{ji}e_j$, so $\mu_m(e\cdot h)=(\det h)\,\mu_m(e_1,\dots,e_k)$ by the defining basis-evaluation property of the determinant ([[Def - Determinant|definition of $\det$]]; equivalently by expanding via multilinearity and alternation into the Leibniz sum).
>
> **Forward map is well defined.** Let $\mu\in\Gamma(\Lambda^k E^*)$ be nowhere vanishing and $P_\mu$ as above. If $e\in P_\mu$ and $h\in SL_k(\mathbb R)$ then $\mu(e\cdot h)=(\det h)\mu(e)=1$, so $P_\mu$ is $SL_k(\mathbb R)$-invariant. Each fibre is non-empty: given any frame $e^{(0)}$ of $E_m$, $c:=\mu(e^{(0)})\neq0$, and $e^{(0)}\cdot\operatorname{diag}(1/c,1,\dots,1)$ has $\mu$-value $1$. The action is free (restriction of the free frame action) and transitive on $(P_\mu)_m$: two unimodular frames differ by $h=e^{-1}e'$ with $\det h=\mu(e')/\mu(e)=1$. A smooth unimodular local frame $e_S=e\cdot\operatorname{diag}(1/c,1,\dots,1)$ (with $c=\mu(e)$ smooth and nowhere zero) gives the chart $(m,h)\mapsto e_S(m)\cdot h$, exhibiting $P_\mu$ as an embedded principal $SL_k(\mathbb R)$-subbundle because $SL_k(\mathbb R)=\det^{-1}(1)$ is an embedded Lie subgroup ($1$ is a regular value of $\det$) and the chart is the restriction of the ambient frame-bundle chart. Thus $P_\mu$ is an $SL_k(\mathbb R)$-structure.
>
> **Backward map is well defined.** Given an $SL_k(\mathbb R)$-structure $P$, for each $m$ let $\mu_P^m$ be the unique alternating $k$-form with $\mu_P^m(p_1,\dots,p_k)=1$ for $p\in P_m$ (a top form is determined by its value on a basis). This is independent of $p\in P_m$: any other is $p\cdot h$ with $h\in SL_k(\mathbb R)$ (transitivity of $SL_k(\mathbb R)$ on $P_m$), and $\mu_P^m(p\cdot h)=(\det h)\mu_P^m(p)=1$. It is nowhere vanishing (value $1$ on a basis) and smooth: over a trivialising $U$ for $P$ take a smooth section $s\colon U\to P$ ([[Thm - Sections of a Principal Bundle and Triviality|sections–triviality]]); then $\mu_P(s)=1$, and for smooth $t_i=\sum_j a_{ji}s_j$, $\mu_P(t_1,\dots,t_k)=\det(a_{ji})$ is smooth. So $\mu_P\in\Gamma(\Lambda^k E^*)$ is a fibrewise volume form.
>
> **Mutual inverse.** $\mu_{P_\mu}=\mu$: both are the alternating top form taking value $1$ on the unimodular frames, and a top form is determined by its value on one basis. $P_{\mu_P}=P$: clearly $P\subseteq P_{\mu_P}$; conversely if $\mu_P(e)=1$ and $e=p\cdot h$ with $p\in P_m$, then $\det h=\mu_P(e)/\mu_P(p)=1$, so $e=p\cdot h\in P$ by invariance. Hence the correspondence is a bijection. $\blacksquare$

> [!warning] Illegal but tempting route: normalising to "$\mu>0$" instead of "$\mu=1$"
> One might try to define the distinguished frames as those with $\mu(e_1,\dots,e_k)>0$. This set *is* a subbundle, but its structure group is $GL_k^+(\mathbb R)=\{h:\det h>0\}$, not $SL_k(\mathbb R)$: by the transformation law $\mu(e\cdot h)=(\det h)\mu(e)$, the sign of the value is preserved exactly by $\det h>0$. So "$\mu>0$" only remembers the *orientation* induced by $\mu$ (the [[Ex - Orientations Correspond to GL-plus Reductions|$GL_k^+$ row]]), throwing away the actual volume normalisation; two volume forms $\mu$ and $2\mu$ give the same positive-frame bundle but different unimodular-frame bundles. The condition must be the exact equality "$\mu=1$" for the correspondence to be with $SL_k(\mathbb R)$ and to be injective in $\mu$.

---

# Key Takeaways

**Extra fibrewise structure is a reduction of the structure group, and the reduction is always "the frames compatible with the structure".** This exercise is one instance of the master dictionary of the subject: a geometric structure on the fibres of $E$ — a metric, an orientation, a complex structure, a volume form — is the same datum as a subbundle of $\operatorname{Fr}(E)$ whose structure group is the subgroup of $GL_k$ preserving that structure on the model fibre. The recognisable move, whenever a problem hands you a fibrewise structure and asks for a $G$-structure (or vice versa), is: form the set of frames *compatible* with the structure, prove that compatibility is preserved by exactly the subgroup $G$, and read off that the compatible frames are a single $G$-orbit in each fibre. The row here — volume form $\leftrightarrow SL_k(\mathbb R)$ — is the cleanest instance because "compatible" means the single scalar equation $\mu(e)=1$, and the stabiliser drops out of the determinant transformation law with no further work. When you meet metrics, orientations, or complex structures, expect the same three moves with $O(k)$, $GL_k^+(\mathbb R)$, or $GL_k(\mathbb C)$ in place of $SL_k(\mathbb R)$.

**The determinant is the universal bookkeeping for how a top form changes under a change of basis; whenever an alternating top object appears, the special linear group is one line away.** The entire content of both directions is the identity $\mu(e\cdot h)=(\det h)\,\mu(e)$, which is nothing but the defining property of the determinant restated for frames. The trigger to reach for it is the presence of a top-degree alternating object — a volume form, a determinant line, an orientation, a Jacobian — together with a change of frame or coordinate. Its diagnostic power is that it *converts a geometric normalisation into an algebraic constraint on $\det$*: "$\mu$ unchanged" becomes "$\det=1$" ($SL_k$), "$\mu$ sign unchanged" becomes "$\det>0$" ($GL_k^+$), "$\mu$ scaled by a positive unit" becomes "$\det>0$ up to scale". Learning to see which normalisation you are imposing tells you immediately which subgroup you are reducing to; conflating them (as in the illegal route above) is the standard error.

**A section of a line bundle is the same as a trivialisation, and a global unit-normalised frame of it is a global structure.** A fibrewise volume form is a nowhere-vanishing section of the real line bundle $\Lambda^k E^*$, i.e. a trivialisation of $\Lambda^k E^*$; this exercise shows such a trivialisation is equivalent to an $SL_k(\mathbb R)$-reduction of $\operatorname{Fr}(E)$. The transferable principle is that questions about *existence* of the structure become questions about triviality of an associated determinant line bundle: $E$ admits a fibrewise volume form if and only if $\Lambda^k E^*$ (equivalently $\Lambda^k E$, the determinant line bundle $\det E$) is trivial, which for real bundles is exactly orientability plus the always-available metric normalisation. This is the seed of characteristic-class thinking — the obstruction to reducing $GL_k(\mathbb R)$ to $SL_k(\mathbb R)$ lives in the determinant line bundle — and it recurs verbatim for the $GL_k^+$ (orientation, first Stiefel–Whitney class) and $U(k)$ (Hermitian, first Chern class) rows, treated in the companion exercises [[Ex - Orientations Correspond to GL-plus Reductions]] and [[Ex - Complex Structures Correspond to GL(k,C)-Structures]].
