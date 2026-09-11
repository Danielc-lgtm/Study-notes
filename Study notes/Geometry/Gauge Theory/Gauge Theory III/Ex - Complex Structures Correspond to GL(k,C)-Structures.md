---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Complex Vector Bundle and Hermitian Structure"
  - "Def - Frame Bundle of a Vector Bundle"
  - "Def - Reduction and Extension of the Structure Group"
  - "Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $E\to M$ be a smooth real [[Def - Vector Bundle|vector bundle]] of rank $2k$ over a smooth manifold $M$ (Hausdorff, second countable, $C^\infty$), with [[Def - Frame Bundle of a Vector Bundle|frame bundle]] $\operatorname{Fr}(E)$, a principal $GL_{2k}(\mathbb R)$-bundle. Let $I_{\mathrm{st}}$ be the **standard complex structure** on $\mathbb R^{2k}$,
$$I_{\mathrm{st}}(x_1,y_1,\dots,x_k,y_k):=(-y_1,x_1,\dots,-y_k,x_k),$$
which satisfies $I_{\mathrm{st}}^2=-\operatorname{id}$, and let
$$GL_k(\mathbb C):=\{A\in GL_{2k}(\mathbb R)\mid A\circ I_{\mathrm{st}}=I_{\mathrm{st}}\circ A\}\subseteq GL_{2k}(\mathbb R)$$
be the subgroup of real automorphisms commuting with $I_{\mathrm{st}}$.

> **Problem (Haydys, Exercise 28).**
> **(i)** Show that a complex vector bundle can equivalently be defined as a locally trivial family of complex vector spaces — a fibre bundle with typical fibre $\mathbb C^k$ whose local trivialisations are fibrewise $\mathbb C$-linear — akin to the definition of a vector bundle.
> **(ii)** Show that there is a canonical one-to-one correspondence between complex structures on $E$ and $GL_k(\mathbb C)$-structures on $E$, with $GL_k(\mathbb C)$ as displayed above.

The strategy for (ii) mirrors the volume-form exercise: send a complex structure $I$ to its bundle of **complex-linear frames** — the frames intertwining $I_{\mathrm{st}}$ with $I$ — and send a $GL_k(\mathbb C)$-structure $P$ back to the complex structure obtained by transporting $I_{\mathrm{st}}$ through any frame of $P$. The commuting condition $A I_{\mathrm{st}}=I_{\mathrm{st}}A$ is exactly what makes "$e$ is complex-linear" a $GL_k(\mathbb C)$-invariant condition. Part (i) supplies the complex frames needed to make everything smooth, and is the equivalence proved on the definition page, which we recall and reprove in the form needed here.

**Recall.**

The objects in play are a complex structure on a real vector space and on a bundle, the frame bundle and the frame action, a $G$-structure, and the group $GL_k(\mathbb C)$ realised inside $GL_{2k}(\mathbb R)$.

![[Def - Complex Vector Bundle and Hermitian Structure#The Definition]]

In particular, a **complex vector bundle** is a real vector bundle $E\to M$ together with a section $I\in\Gamma(\operatorname{End}E)$ satisfying $I^2=-\operatorname{id}_E$, called a **complex structure**; each fibre $E_m$ becomes a complex vector space of complex dimension $k=\tfrac12\operatorname{rk}E$ under $(a+bi)\cdot v=av+b\,I_m v$. A **frame** of $E_m$ is a real-linear isomorphism $e\colon\mathbb R^{2k}\to E_m$, with the right $GL_{2k}(\mathbb R)$-action $e\cdot h=e\circ h$; the action is free and transitive on each fibre $\operatorname{Fr}(E_m)$ (see [[Def - Frame Bundle of a Vector Bundle|the frame-bundle page]]).

![[Def - Reduction and Extension of the Structure Group#$G$-structures on a vector bundle]]

Thus, for a closed subgroup $G\le GL_{2k}(\mathbb R)$, a **$G$-structure** on $E$ is an embedded submanifold $P\subseteq\operatorname{Fr}(E)$, invariant under the restricted right $G$-action and forming a principal $G$-bundle over $M$ under $\pi|_P$.

The correspondence we prove is one row of the reductions theorem, whose relevant statement we recall (and whose $GL_k(\mathbb C)$ row we prove here in detail):

> **Theorem (structures as reductions, the complex row — [[Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group|reductions theorem]]).** For a real vector bundle $E$ of rank $2k$, complex structures on $E$ correspond bijectively to reductions of $\operatorname{Fr}(E)$ to $GL_k(\mathbb C)$, that is, to $GL_k(\mathbb C)$-structures $P\subseteq\operatorname{Fr}(E)$.

> [!warning] Convention: the rank index and a source typo
> We index by *complex* rank $k$, so $\operatorname{rk}_{\mathbb R}E=2k$ and the structure group is $GL_k(\mathbb C)$, matching Haydys's Exercise 28. (The reductions-theorem page uses the letter $m$ for the same complex rank; $GL_k(\mathbb C)$ here is $GL_m(\mathbb C)$ there.) Haydys's Exercise 28 prints "a real vector bundle *or* rank $2k$"; this is a typographical slip for "*of* rank $2k$", which we use.

---

# Convergent Strategy

**Problem class.** Part (ii) is again a *bijection-between-two-kinds-of-geometric-data* problem, of the same family as metrics $\leftrightarrow O(k)$ and volume forms $\leftrightarrow SL_k(\mathbb R)$, solved by the identical three-move template: cut out the frames compatible with the structure, show they are a single orbit of the stabiliser subgroup, and invert by reconstructing the structure from any compatible frame. Part (i) is a *two-definitions-agree* problem, proved by constructing each object's data from the other's and checking the constructions are mutually inverse. The novelty over the volume-form row is that "compatible frame" is now an *intertwining* condition ($e\circ I_{\mathrm{st}}=I\circ e$) rather than a scalar equation, and that the compatible frames need part (i) to exist smoothly.

**Assumption pattern.** The trigger is that a complex structure is precisely "a smooth way to multiply by $i$", and multiplying by $i$ on the model fibre $\mathbb R^{2k}=\mathbb C^k$ is the operator $I_{\mathrm{st}}$. A real-linear map $A$ of $\mathbb C^k$ is $\mathbb C$-linear if and only if it commutes with multiplication by $i$, i.e. $A I_{\mathrm{st}}=I_{\mathrm{st}}A$; this is the entire reason $GL_k(\mathbb C)=\{A:AI_{\mathrm{st}}=I_{\mathrm{st}}A\}$. So the assumption "$I$ is a complex structure" is used in exactly one way — to declare which frames count as complex-linear, namely those $e$ with $e\circ I_{\mathrm{st}}=I\circ e$, so that transporting $I_{\mathrm{st}}$ through them returns $I$.

**Theorem routing.** For (ii): define $P_I:=\{e\in\operatorname{Fr}(E):e\circ I_{\mathrm{st}}=I\circ e\}$; use the *commuting condition* to show $GL_k(\mathbb C)$ preserves $P_I$ and acts freely and transitively on each fibre; use *part (i)* (existence of smooth $\mathbb C$-linear frames) to show each fibre is non-empty and to build the subbundle charts; hence $P_I$ is a [[Def - Reduction and Extension of the Structure Group|$GL_k(\mathbb C)$-structure]]. Invert by $P\mapsto I_P$ with $I_P|_{E_m}:=p\circ I_{\mathrm{st}}\circ p^{-1}$ for $p\in P_m$; use the commuting condition to prove independence of $p$; use local sections of $P$ for smoothness; check both round trips. For (i): from $I$ produce $\mathbb C$-linear trivialisations by choosing a complex fibre basis and extending; from a $\mathbb C^k$-bundle produce $I$ by transporting multiplication by $i$; check mutually inverse.

**Key decision point.** The non-obvious moves are two. First, in (ii), *to encode "complex-linear frame" as the intertwining equation $e\circ I_{\mathrm{st}}=I\circ e$ rather than as any explicit list of vectors* — this is the coordinate-free form that makes the $GL_k(\mathbb C)$-invariance a one-line computation. Second, in the inverse direction, *to define $I_P$ by conjugating the fixed model operator $I_{\mathrm{st}}$ by a frame*, $I_P=pI_{\mathrm{st}}p^{-1}$ — a "transport of structure" that is well defined precisely because changing $p$ within $P_m$ conjugates $I_{\mathrm{st}}$ by an element that commutes with it, leaving it fixed. Recognising that "commutes with $I_{\mathrm{st}}$" is doing exactly the job "preserves the value of $\mu$" did in the volume-form row is the transferable insight.

---

# Legal Operations Used

This solution deploys the following operations, in the sense of the [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles|topic page's Legal Operations]]; where the topic page is not yet assembled, the operation is named descriptively and will be reconciled by number.

1. **Cut out the compatible sub-frame-bundle.** From the complex structure $I$, form the subset of $\operatorname{Fr}(E)$ of frames *compatible* with it — the complex-linear frames $e\circ I_{\mathrm{st}}=I\circ e$.

2. **Realise $\mathbb C$-linearity as commuting with $I_{\mathrm{st}}$.** Use that a real-linear map of $\mathbb C^k$ is $\mathbb C$-linear if and only if it commutes with multiplication by $i=I_{\mathrm{st}}$; this both defines $GL_k(\mathbb C)$ and identifies the complex-linear frames.

3. **Read a subgroup off an invariance condition.** The frames intertwining $I_{\mathrm{st}}$ with $I$ are permuted among themselves exactly by the $A$ with $AI_{\mathrm{st}}=I_{\mathrm{st}}A$; hence the stabiliser is $GL_k(\mathbb C)$ and the compatible frames form one $GL_k(\mathbb C)$-orbit per fibre.

4. **Transport a structure by conjugation with a frame.** In the inverse direction, define $I_P:=p\circ I_{\mathrm{st}}\circ p^{-1}$; well-definedness is exactly the statement that conjugating $I_{\mathrm{st}}$ by an element of $GL_k(\mathbb C)$ (which commutes with $I_{\mathrm{st}}$) does nothing.

5. **Build local trivialisations of a sub-bundle from a compatible local frame.** A smooth $\mathbb C$-linear local frame $e_{\mathbb C}$ over $U$ (from part (i)) gives the chart $(m,A)\mapsto e_{\mathbb C}(m)\cdot A$, $U\times GL_k(\mathbb C)\to\pi^{-1}(U)\cap P_I$.

6. **Prove an equivalence of two definitions by constructing mutually inverse data.** For part (i), construct $\mathbb C$-linear trivialisations from $I$ and construct $I$ from $\mathbb C$-linear trivialisations, and verify the constructions undo each other.

7. **Verify a bijection by composing both ways.** For part (ii), show $I\mapsto P_I\mapsto I_{P_I}=I$ and $P\mapsto I_P\mapsto P_{I_P}=P$.

---

# Hints

> [!note]- Hint 1
> For (ii), imitate the volume-form row: given the complex structure $I$, single out the frames "compatible" with it. A frame is a real isomorphism $e\colon\mathbb R^{2k}\to E_m$; it should be called complex-linear when it carries "multiply by $i$ on $\mathbb R^{2k}=\mathbb C^k$" to "multiply by $i$ on $E_m$", i.e. when it intertwines $I_{\mathrm{st}}$ with $I$. Write that condition as an equation of linear maps.

> [!note]- Hint 2
> The condition is $e\circ I_{\mathrm{st}}=I\circ e$, equivalently $I=e\circ I_{\mathrm{st}}\circ e^{-1}$. Now compute: if $e$ satisfies it and $A\in GL_{2k}(\mathbb R)$, when does $e\cdot A=e\circ A$ also satisfy it? You will find $(eA)I_{\mathrm{st}}=I(eA)$ holds iff $AI_{\mathrm{st}}=I_{\mathrm{st}}A$, i.e. iff $A\in GL_k(\mathbb C)$. That is the whole point of the definition of $GL_k(\mathbb C)$.

> [!note]- Hint 3
> Let $P_I:=\{e:e\circ I_{\mathrm{st}}=I\circ e\}$. Non-emptiness of each fibre is exactly the existence of a $\mathbb C$-linear frame at $m$: take a complex basis $u_1,\dots,u_k$ of $(E_m,I_m)$ and set $e(\epsilon_{2j-1})=u_j$, $e(\epsilon_{2j})=I_m u_j$; check $e I_{\mathrm{st}}=I e$ using $I_{\mathrm{st}}\epsilon_{2j-1}=\epsilon_{2j}$ and $I_{\mathrm{st}}\epsilon_{2j}=-\epsilon_{2j-1}$. Freeness and transitivity of $GL_k(\mathbb C)$ on $(P_I)_m$ come from Hint 2 plus the freeness/transitivity of the full frame action. Smoothness needs a *smooth* $\mathbb C$-linear local frame — that is part (i).

> [!note]- Hint 4
> For the inverse, given a $GL_k(\mathbb C)$-structure $P$, transport $I_{\mathrm{st}}$: set $I_P:=p\circ I_{\mathrm{st}}\circ p^{-1}$ on $E_m$ for $p\in P_m$. Independence of $p$: another is $p'=p\cdot A$ with $A\in GL_k(\mathbb C)$, so $p'I_{\mathrm{st}}p'^{-1}=pAI_{\mathrm{st}}A^{-1}p^{-1}=pI_{\mathrm{st}}p^{-1}$ because $AI_{\mathrm{st}}=I_{\mathrm{st}}A$. Then $I_P^2=pI_{\mathrm{st}}^2p^{-1}=-\operatorname{id}$. For (i), build $\mathbb C$-linear local frames exactly as in Hint 3 but with smooth sections, using continuity of the determinant to keep them a frame near $m$.

---

# Solution

We do part (i) first, since part (ii) uses it to make the complex-linear frames smooth. Throughout, the guiding identity is that a real-linear map of $\mathbb C^k$ is $\mathbb C$-linear precisely when it commutes with $I_{\mathrm{st}}$, so that "complex-linear frame" and "commutes with $I_{\mathrm{st}}$" are the two faces of the same condition.

## Part (i): a complex vector bundle is a locally trivial family of complex vector spaces

**Plan.** In one direction, a complex structure $I$ lets us pick, near each point, a smooth complex frame, and the associated real trivialisation followed by $\mathbb R^{2k}\cong\mathbb C^k$ is a fibrewise $\mathbb C$-linear trivialisation. In the other, a $\mathbb C^k$-bundle with $\mathbb C$-linear trivialisations carries a canonical $I$ obtained by transporting multiplication by $i$; the two constructions are mutually inverse.

**Step (i).1: A complex structure gives $\mathbb C$-linear trivialisations.**

> [!note]- Derivation
> **Goal.** Given a complex vector bundle $(E,I)$ of real rank $2k$, produce near each point a fibre bundle chart $\psi_U\colon E|_U\to U\times\mathbb C^k$ that is $\mathbb C$-linear on each fibre.
>
> Fix $m\in M$. Because $(E_m,I_m)$ is a complex vector space of complex dimension $k$, choose a complex basis $u_1,\dots,u_k\in E_m$. Then $(u_1,I_mu_1,\dots,u_k,I_mu_k)$ is a *real* basis of $E_m$: if $\sum_j(a_ju_j+b_jI_mu_j)=0$ with $a_j,b_j\in\mathbb R$, then $\sum_j(a_j+ib_j)u_j=0$ in the complex structure (since $b_jI_mu_j=(ib_j)\cdot u_j$), forcing $a_j+ib_j=0$, hence all $a_j=b_j=0$ (complex linear independence of the $u_j$).
>
> **Extend to smooth sections.** Pick a smooth *real* local trivialisation of $E$ near $m$ and let $v_1,\dots,v_k\in\Gamma(E|_W)$ be the smooth sections on a neighbourhood $W\ni m$ that are constant in that trivialisation with $v_j(m)=u_j$. The $2k$ sections $v_1,Iv_1,\dots,v_k,Iv_k$ are smooth ($I$ is smooth). Expressed in the real trivialisation they form a smooth matrix-valued map on $W$ whose value at $m$ is invertible (previous paragraph), so its determinant is nonzero at $m$; by continuity of the determinant there is a neighbourhood $U\subseteq W$ of $m$ on which the determinant stays nonzero. On $U$ the family $(v_1,Iv_1,\dots,v_k,Iv_k)$ is a real frame, so for each $x\in U$ the vectors $v_1(x),\dots,v_k(x)$ are a *complex* basis of $(E_x,I_x)$ (a complex basis is exactly a real basis of the form $(w_j,I_xw_j)$).
>
> **The $\mathbb C$-linear chart.** Define $\psi_U\colon E|_U\to U\times\mathbb C^k$ by writing $w\in E_x$ uniquely as $w=\sum_{j=1}^k(a_jv_j(x)+b_jI_xv_j(x))$ ($a_j,b_j\in\mathbb R$) and setting $\psi_U(w)=(x,(a_1+ib_1,\dots,a_k+ib_k))$. This is a diffeomorphism over $U$ (the real trivialisation for the frame $(v_j,Iv_j)$ composed with $\mathbb R^{2k}\cong\mathbb C^k$). It is fibrewise $\mathbb C$-linear: multiplication by $i$ sends $v_j\mapsto Iv_j$ and $Iv_j\mapsto I^2v_j=-v_j$, i.e. $(a_j,b_j)\mapsto(-b_j,a_j)$, which is multiplication of $a_j+ib_j$ by $i$. Transition functions between two such charts are fibrewise $\mathbb C$-linear and invertible, hence valued in $GL_k(\mathbb C)$. So $E$ is a locally trivial family of complex vector spaces. $\blacksquare$

**Step (i).2: A $\mathbb C^k$-bundle with $\mathbb C$-linear trivialisations gives a complex structure, and the two constructions are inverse.**

> [!note]- Derivation
> **Goal.** Given a fibre bundle $E\to M$ with fibre $\mathbb C^k$ and fibrewise $\mathbb C$-linear trivialisations $\psi_\alpha\colon E|_{U_\alpha}\to U_\alpha\times\mathbb C^k$ (transition functions in $GL_k(\mathbb C)$), produce $I\in\Gamma(\operatorname{End}E)$ with $I^2=-\operatorname{id}$.
>
> **Definition of $I$.** For $w\in E_x$ with $x\in U_\alpha$, set $I_xw:=\psi_\alpha^{-1}(x,\,i\cdot\operatorname{pr}_2\psi_\alpha(w))$, transporting multiplication by $i$ on $\mathbb C^k$. **Well-defined (independent of $\alpha$).** If $x\in U_\alpha\cap U_\beta$, then on $E_x$ one has $\operatorname{pr}_2\psi_\beta=g_{\beta\alpha}(x)\operatorname{pr}_2\psi_\alpha$ with $g_{\beta\alpha}(x)\in GL_k(\mathbb C)$; since $g_{\beta\alpha}(x)$ is $\mathbb C$-linear it commutes with multiplication by $i$, so the vector produced using $\beta$ equals that using $\alpha$ (the operation "$\times i$" is unchanged under conjugation by the $\mathbb C$-linear $g_{\beta\alpha}(x)$). **Smooth.** In each chart $I$ is the constant fibrewise map "multiply the $\mathbb C^k$-coordinate by $i$" conjugated by the smooth $\psi_\alpha$, hence smooth. **The equation.** $I^2$ transports multiplication by $i^2=-1$, so $I^2=-\operatorname{id}$. Thus $(E,I)$ is a complex vector bundle in the endomorphism sense.
>
> **Mutually inverse.** Starting from $(E,I)$, Step (i).1 builds $\mathbb C$-linear charts in which $I$ acts as $\times i$ (that was checked there); feeding these into Step (i).2 recovers exactly this $I$ (transporting $\times i$ through a chart in which $I=\times i$ returns $I$). Starting from a $\mathbb C^k$-bundle, Step (i).2 builds $I$, and Step (i).1's charts for this $I$ are again fibrewise $\mathbb C$-linear (the original charts serve). Hence the two definitions of "complex vector bundle" coincide. $\blacksquare$

The same equivalence is proved on [[Def - Complex Vector Bundle and Hermitian Structure|the definition page]]; we have reproduced it because part (ii) uses the smooth $\mathbb C$-linear local frames it produces.

## Part (ii): complex structures correspond to $GL_k(\mathbb C)$-structures

**Plan.** Send $I$ to its bundle of complex-linear frames $P_I$; the commuting relation $AI_{\mathrm{st}}=I_{\mathrm{st}}A$ makes $GL_k(\mathbb C)$ exactly the stabiliser, and part (i) makes $P_I$ smooth. Invert by transporting $I_{\mathrm{st}}$ through a frame of $P$. Then check the round trips.

**Step 0: $GL_k(\mathbb C)$ is the group of $\mathbb C$-linear automorphisms, and it is a closed subgroup.**

> [!note]- Derivation
> Identify $\mathbb R^{2k}$ with $\mathbb C^k$ by $(x_1,y_1,\dots,x_k,y_k)\leftrightarrow(x_1+iy_1,\dots,x_k+iy_k)$; under it, multiplication by $i$ is the real-linear map $I_{\mathrm{st}}$, since $i(x_j+iy_j)=-y_j+ix_j\leftrightarrow(-y_j,x_j)$, matching the displayed formula. A real-linear $A\in GL_{2k}(\mathbb R)$ is $\mathbb C$-linear as a map $\mathbb C^k\to\mathbb C^k$ if and only if $A(i\cdot z)=i\cdot A(z)$ for all $z$, i.e. $A\circ I_{\mathrm{st}}=I_{\mathrm{st}}\circ A$. Hence $GL_k(\mathbb C)=\{A\in GL_{2k}(\mathbb R):AI_{\mathrm{st}}=I_{\mathrm{st}}A\}$ is exactly the group of invertible $\mathbb C$-linear self-maps of $\mathbb C^k$, as the notation promises.
>
> It is a subgroup: it contains $\operatorname{id}$, and if $A,B$ commute with $I_{\mathrm{st}}$ then so do $AB$ (associativity) and $A^{-1}$ (from $AI_{\mathrm{st}}=I_{\mathrm{st}}A$, left- and right-multiply by $A^{-1}$ to get $I_{\mathrm{st}}A^{-1}=A^{-1}I_{\mathrm{st}}$). It is **closed** in $GL_{2k}(\mathbb R)$: the condition $AI_{\mathrm{st}}-I_{\mathrm{st}}A=0$ is a finite system of linear equations in the entries of $A$, so $GL_k(\mathbb C)=\{A:AI_{\mathrm{st}}-I_{\mathrm{st}}A=0\}\cap GL_{2k}(\mathbb R)$ is the intersection of a closed linear subspace with $GL_{2k}(\mathbb R)$; being a closed subgroup it is, by [[Thm - The Closed Subgroup Theorem|the closed subgroup theorem]] — a closed subgroup of a Lie group is an embedded Lie subgroup — an embedded Lie subgroup of $GL_{2k}(\mathbb R)$. $\blacksquare$

**Step 1: From a complex structure $I$, build the bundle of complex-linear frames $P_I$.**

Set $P_I:=\{e\in\operatorname{Fr}(E):e\circ I_{\mathrm{st}}=I\circ e\}$. Then $P_I$ is invariant under the right $GL_k(\mathbb C)$-action, meets every fibre, and $GL_k(\mathbb C)$ acts freely and transitively on each fibre $(P_I)_m$.

> [!note]- Derivation
> Recall a frame is $e\colon\mathbb R^{2k}\to E_m$ and the condition $e\circ I_{\mathrm{st}}=I\circ e$ says $e$ intertwines $I_{\mathrm{st}}$ with $I_m$, equivalently $I_m=e\circ I_{\mathrm{st}}\circ e^{-1}$.
>
> **Invariance under $GL_k(\mathbb C)$.** Let $e\in P_I$ and $A\in GL_k(\mathbb C)$, so $AI_{\mathrm{st}}=I_{\mathrm{st}}A$. Then
> $$(e\cdot A)\circ I_{\mathrm{st}}=e\circ A\circ I_{\mathrm{st}}=e\circ I_{\mathrm{st}}\circ A=(e\circ I_{\mathrm{st}})\circ A=(I\circ e)\circ A=I\circ(e\cdot A)\qquad(\text{using }AI_{\mathrm{st}}=I_{\mathrm{st}}A\text{ and }e\in P_I),$$
> so $e\cdot A\in P_I$. Thus $P_I$ is closed under the restricted $GL_k(\mathbb C)$-action.
>
> **Each fibre is non-empty.** Fix $m$. As $(E_m,I_m)$ has complex dimension $k$, take a complex basis $u_1,\dots,u_k$ and define $e\colon\mathbb R^{2k}\to E_m$ on the standard basis by $e(\epsilon_{2j-1}):=u_j$ and $e(\epsilon_{2j}):=I_mu_j$. This $e$ is a real isomorphism (its image is the real basis $(u_1,I_mu_1,\dots,u_k,I_mu_k)$, shown a basis in part (i)). It lies in $P_I$: using $I_{\mathrm{st}}\epsilon_{2j-1}=\epsilon_{2j}$ and $I_{\mathrm{st}}\epsilon_{2j}=-\epsilon_{2j-1}$,
> $$e(I_{\mathrm{st}}\epsilon_{2j-1})=e(\epsilon_{2j})=I_mu_j=I_m\,e(\epsilon_{2j-1}),\qquad e(I_{\mathrm{st}}\epsilon_{2j})=e(-\epsilon_{2j-1})=-u_j=I_m^2u_j=I_m\,e(\epsilon_{2j}),$$
> so $e\circ I_{\mathrm{st}}=I_m\circ e$ on the basis, hence everywhere. Thus $(P_I)_m\neq\varnothing$.
>
> **Freeness.** The $GL_k(\mathbb C)$-action on $(P_I)_m$ is the restriction of the free $GL_{2k}(\mathbb R)$-action on $\operatorname{Fr}(E_m)$, hence free.
>
> **Transitivity.** Let $e,e'\in(P_I)_m$. Since $GL_{2k}(\mathbb R)$ is transitive on $\operatorname{Fr}(E_m)$, write $e'=e\cdot A$ with $A=e^{-1}\circ e'\in GL_{2k}(\mathbb R)$. From $e'\in P_I$,
> $$e\circ A\circ I_{\mathrm{st}}=e'\circ I_{\mathrm{st}}=I\circ e'=I\circ e\circ A=e\circ I_{\mathrm{st}}\circ A\qquad(\text{using }e'=eA\text{ and }e\in P_I,\text{ so }Ie=eI_{\mathrm{st}}),$$
> and cancelling the isomorphism $e$ on the left gives $A\circ I_{\mathrm{st}}=I_{\mathrm{st}}\circ A$, i.e. $A\in GL_k(\mathbb C)$. Hence any two complex-linear frames of $E_m$ differ by an element of $GL_k(\mathbb C)$: the action is transitive on $(P_I)_m$. $\blacksquare$

**Step 2: $P_I$ is a smooth embedded $GL_k(\mathbb C)$-subbundle, i.e. a $GL_k(\mathbb C)$-structure.**

Over any small $U$ there is a smooth $\mathbb C$-linear local frame $e_{\mathbb C}\colon U\to P_I$, and $(m,A)\mapsto e_{\mathbb C}(m)\cdot A$ is a diffeomorphism $U\times GL_k(\mathbb C)\to\pi^{-1}(U)\cap P_I$; these charts make $P_I$ an embedded submanifold and a principal $GL_k(\mathbb C)$-bundle.

> [!note]- Derivation
> **A smooth $\mathbb C$-linear local frame.** By part (i) (Step (i).1), near each $m$ there is a smooth frame $e_{\mathbb C}=(v_1,Iv_1,\dots,v_k,Iv_k)$ of $E$ on some $U$ with $v_1,\dots,v_k$ a smooth complex frame; equivalently the real isomorphism $e_{\mathbb C}(x)\colon\mathbb R^{2k}\to E_x$, $\epsilon_{2j-1}\mapsto v_j(x)$, $\epsilon_{2j}\mapsto I_xv_j(x)$, is smooth in $x$. By the computation in Step 1 (non-emptiness), $e_{\mathbb C}(x)\in(P_I)_x$ for every $x\in U$. So $e_{\mathbb C}\colon U\to P_I$ is a smooth section of $\operatorname{Fr}(E)$ landing in $P_I$.
>
> **The subbundle charts.** Define $\Psi^{\mathbb C}_U\colon U\times GL_k(\mathbb C)\to\pi^{-1}(U)$ by $\Psi^{\mathbb C}_U(m,A)=e_{\mathbb C}(m)\cdot A$. Its image lies in $P_I$ (invariance, Step 1), and by transitivity of $GL_k(\mathbb C)$ on $(P_I)_m$ (Step 1) it is onto $\pi^{-1}(U)\cap P_I$; it is injective by freeness. Under the ambient frame-bundle chart $\Psi_U(m,g)=e_{\mathbb C}(m)\cdot g$ of [[Def - Frame Bundle of a Vector Bundle|$\operatorname{Fr}(E)$]] (a diffeomorphism $U\times GL_{2k}(\mathbb R)\to\pi^{-1}(U)$), the map $\Psi^{\mathbb C}_U$ is the restriction to the embedded submanifold $U\times GL_k(\mathbb C)\subseteq U\times GL_{2k}(\mathbb R)$, using that $GL_k(\mathbb C)$ is an embedded Lie subgroup (Step 0). Hence $\pi^{-1}(U)\cap P_I=\Psi_U(U\times GL_k(\mathbb C))$ is an embedded submanifold and $\Psi^{\mathbb C}_U$ is a diffeomorphism onto it.
>
> **The clauses of a $GL_k(\mathbb C)$-structure.** These charts cover $P_I$, so $P_I$ is a smooth embedded submanifold of $\operatorname{Fr}(E)$. It is invariant under the restricted $GL_k(\mathbb C)$-action (Step 1). The action is smooth (restriction), free (Step 1), and in the chart $\Psi^{\mathbb C}_U$ reads $\big((m,A),A'\big)\mapsto(m,AA')$, so $\pi|_{P_I}\colon P_I\to M$ with these $GL_k(\mathbb C)$-equivariant trivialisations ($\Psi^{\mathbb C}_U(m,A)\cdot A'=e_{\mathbb C}(m)\cdot(AA')=\Psi^{\mathbb C}_U(m,AA')$) is a principal $GL_k(\mathbb C)$-bundle. Therefore $P_I$ is a [[Def - Reduction and Extension of the Structure Group|$GL_k(\mathbb C)$-structure]] on $E$. $\blacksquare$

**Step 3: From a $GL_k(\mathbb C)$-structure $P$, build a complex structure $I_P$.**

For $m\in M$ and $p\in P_m$ set $I_P|_{E_m}:=p\circ I_{\mathrm{st}}\circ p^{-1}$. This is independent of $p\in P_m$, satisfies $I_P^2=-\operatorname{id}$, and is a smooth section of $\operatorname{End}E$.

> [!note]- Derivation
> **Independence of the representative.** Let $p,p'\in P_m$. Because $P$ is a principal $GL_k(\mathbb C)$-bundle, $GL_k(\mathbb C)$ is transitive on the fibre $P_m$, so $p'=p\cdot A$ with $A\in GL_k(\mathbb C)$, i.e. $p'=p\circ A$. Then
> $$p'\circ I_{\mathrm{st}}\circ p'^{-1}=p\circ A\circ I_{\mathrm{st}}\circ A^{-1}\circ p^{-1}=p\circ I_{\mathrm{st}}\circ A\circ A^{-1}\circ p^{-1}=p\circ I_{\mathrm{st}}\circ p^{-1}\qquad(\text{using }A I_{\mathrm{st}}=I_{\mathrm{st}}A,\text{ so }AI_{\mathrm{st}}A^{-1}=I_{\mathrm{st}}),$$
> so the value does not depend on the choice of $p\in P_m$; $I_P|_{E_m}$ is well defined.
>
> **The equation.** $I_P^2|_{E_m}=p\circ I_{\mathrm{st}}\circ p^{-1}\circ p\circ I_{\mathrm{st}}\circ p^{-1}=p\circ I_{\mathrm{st}}^2\circ p^{-1}=p\circ(-\operatorname{id})\circ p^{-1}=-\operatorname{id}_{E_m}$, using $I_{\mathrm{st}}^2=-\operatorname{id}$.
>
> **Smoothness.** Over a trivialising open $U$ for $P$, choose a smooth local section $s\colon U\to P$ (these exist by [[Thm - Sections of a Principal Bundle and Triviality|the sections–triviality theorem]]: a principal bundle has smooth local sections over any trivialising open). Then for each $m\in U$, $I_P|_{E_m}=s(m)\circ I_{\mathrm{st}}\circ s(m)^{-1}$, and since $s$ is smooth (so $m\mapsto s(m)$ and $m\mapsto s(m)^{-1}$ are smooth as bundle maps) and $I_{\mathrm{st}}$ is a fixed linear map, $I_P$ is a smooth section of $\operatorname{End}E$ on $U$; smoothness being local, $I_P\in\Gamma(\operatorname{End}E)$. Therefore $(E,I_P)$ is a complex vector bundle. $\blacksquare$

**Step 4: The two constructions are mutually inverse.**

$I\mapsto P_I\mapsto I_{P_I}$ returns $I$, and $P\mapsto I_P\mapsto P_{I_P}$ returns $P$.

> [!note]- Derivation
> **First round trip: $I_{P_I}=I$.** Let $I$ be a complex structure and $P_I$ its complex-linear-frame bundle. For $p\in(P_I)_m$ we have $p\circ I_{\mathrm{st}}=I\circ p$ by definition of $P_I$, hence $p\circ I_{\mathrm{st}}\circ p^{-1}=I|_{E_m}$. But $I_{P_I}|_{E_m}$ is by definition $p\circ I_{\mathrm{st}}\circ p^{-1}$ for any $p\in(P_I)_m$. Therefore $I_{P_I}|_{E_m}=I|_{E_m}$ for every $m$, so $I_{P_I}=I$.
>
> **Second round trip: $P_{I_P}=P$.** Let $P$ be a $GL_k(\mathbb C)$-structure and $I_P$ its complex structure. By definition $P_{I_P}=\{e\in\operatorname{Fr}(E):e\circ I_{\mathrm{st}}=I_P\circ e\}$. *($P\subseteq P_{I_P}$.)* For $p\in P_m$, $I_P|_{E_m}=p\circ I_{\mathrm{st}}\circ p^{-1}$ (definition of $I_P$), so $I_P\circ p=p\circ I_{\mathrm{st}}$, i.e. $p\in P_{I_P}$. *($P_{I_P}\subseteq P$.)* Let $e\in(P_{I_P})_m$, so $e\circ I_{\mathrm{st}}=I_P\circ e$. Pick any $p\in P_m$; by transitivity of $GL_{2k}(\mathbb R)$ on $\operatorname{Fr}(E_m)$, write $e=p\cdot A$ with $A\in GL_{2k}(\mathbb R)$. Using $I_P|_{E_m}=p\circ I_{\mathrm{st}}\circ p^{-1}$,
> $$p\circ A\circ I_{\mathrm{st}}=e\circ I_{\mathrm{st}}=I_P\circ e=p\circ I_{\mathrm{st}}\circ p^{-1}\circ p\circ A=p\circ I_{\mathrm{st}}\circ A,$$
> and cancelling $p$ gives $A\circ I_{\mathrm{st}}=I_{\mathrm{st}}\circ A$, so $A\in GL_k(\mathbb C)$; then $e=p\cdot A\in P_m$ by invariance of $P$. Hence $P_{I_P}=P$ as subsets, with the same restricted $GL_k(\mathbb C)$-bundle structure. The two assignments are inverse bijections between complex structures and $GL_k(\mathbb C)$-structures. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** (i) A complex vector bundle $(E,I)$ is the same datum as a fibre bundle with fibre $\mathbb C^k$ and fibrewise $\mathbb C$-linear trivialisations. (ii) For a real bundle $E$ of rank $2k$, the maps $I\mapsto P_I:=\{e\in\operatorname{Fr}(E):e\circ I_{\mathrm{st}}=I\circ e\}$ and $P\mapsto I_P$ ($I_P|_{E_m}:=p\circ I_{\mathrm{st}}\circ p^{-1}$ for $p\in P_m$) are mutually inverse bijections between complex structures on $E$ and $GL_k(\mathbb C)$-structures.
>
> **(i).** From $I$: near $m$ pick a complex basis $u_1,\dots,u_k$ of $(E_m,I_m)$; the real vectors $(u_j,I_mu_j)$ form a real basis, so smooth constant-in-a-real-trivialisation extensions $v_j$ with $v_j(m)=u_j$ give, by continuity of the determinant, a real frame $(v_j,Iv_j)$ on a neighbourhood $U$; the induced chart $E|_U\to U\times\mathbb R^{2k}\cong U\times\mathbb C^k$ is fibrewise $\mathbb C$-linear because $\times i$ sends $v_j\mapsto Iv_j\mapsto -v_j$. From a $\mathbb C^k$-bundle with $\mathbb C$-linear charts $\psi_\alpha$: set $I_xw=\psi_\alpha^{-1}(x,i\cdot\operatorname{pr}_2\psi_\alpha w)$; well defined because $GL_k(\mathbb C)$-transitions commute with $\times i$, smooth in each chart, and $I^2=-\operatorname{id}$. These are mutually inverse.
>
> **(ii).** $GL_k(\mathbb C)=\{A:AI_{\mathrm{st}}=I_{\mathrm{st}}A\}$ is exactly the $\mathbb C$-linear automorphisms of $\mathbb C^k$ and is a closed (hence embedded Lie) subgroup of $GL_{2k}(\mathbb R)$, being cut out by linear equations. *Forward.* $P_I$ is $GL_k(\mathbb C)$-invariant: $e I_{\mathrm{st}}=Ie$ and $AI_{\mathrm{st}}=I_{\mathrm{st}}A$ give $(eA)I_{\mathrm{st}}=I(eA)$. Each fibre is non-empty (the frame $\epsilon_{2j-1}\mapsto u_j,\ \epsilon_{2j}\mapsto I_mu_j$ lies in it, via $I_{\mathrm{st}}\epsilon_{2j-1}=\epsilon_{2j},\ I_{\mathrm{st}}\epsilon_{2j}=-\epsilon_{2j-1}$). The action is free (restriction of the frame action) and transitive on $(P_I)_m$ (if $e'=eA$ with both in $P_I$ then $AI_{\mathrm{st}}=I_{\mathrm{st}}A$). A smooth $\mathbb C$-linear local frame from (i) gives charts $U\times GL_k(\mathbb C)\to\pi^{-1}(U)\cap P_I$ exhibiting $P_I$ as an embedded principal $GL_k(\mathbb C)$-subbundle. *Backward.* $I_P|_{E_m}=pI_{\mathrm{st}}p^{-1}$ is independent of $p\in P_m$ (another is $pA$, $A\in GL_k(\mathbb C)$, and $AI_{\mathrm{st}}A^{-1}=I_{\mathrm{st}}$), satisfies $I_P^2=-\operatorname{id}$, and is smooth via a local section of $P$. *Inverse.* $I_{P_I}=I$ since $p\in P_I\Rightarrow pI_{\mathrm{st}}p^{-1}=I$; and $P_{I_P}=P$ since $P\subseteq P_{I_P}$ trivially, while $e\in P_{I_P}$ with $e=pA$ forces $AI_{\mathrm{st}}=I_{\mathrm{st}}A$, so $e\in P$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: "any $\mathbb R$-linear frame will do to define $I_P$"
> To invert, one might try to define $I_P$ by conjugating $I_{\mathrm{st}}$ through *any* frame $e\in\operatorname{Fr}(E_m)$, not only frames of $P$. This fails: for a general $e=p\cdot A$ with $A\in GL_{2k}(\mathbb R)\setminus GL_k(\mathbb C)$, the operator $eI_{\mathrm{st}}e^{-1}=pAI_{\mathrm{st}}A^{-1}p^{-1}$ depends on $A$ (since $AI_{\mathrm{st}}A^{-1}\neq I_{\mathrm{st}}$ when $A$ does not commute with $I_{\mathrm{st}}$), so the recipe is not well defined on all of $\operatorname{Fr}(E_m)$. It becomes well defined *exactly* when $e$ ranges over a $GL_k(\mathbb C)$-orbit — that is, over a $GL_k(\mathbb C)$-structure. The reduction to $GL_k(\mathbb C)$ is precisely the data that makes "transport $I_{\mathrm{st}}$ by a frame" unambiguous.

---

# Key Takeaways

**A complex structure is a smooth global "multiplication by $i$", and the frames that respect it are exactly the $\mathbb C$-linear frames — a $GL_k(\mathbb C)$-reduction.** This exercise is the complex row of the same dictionary that gave metrics $\leftrightarrow O(k)$ and volume forms $\leftrightarrow SL_k(\mathbb R)$: extra fibrewise structure equals a reduction of the structure group to the subgroup preserving that structure on the model fibre. The subgroup here, $GL_k(\mathbb C)=\{A:AI_{\mathrm{st}}=I_{\mathrm{st}}A\}$, is the stabiliser of the operator $I_{\mathrm{st}}$ under conjugation, and "complex-linear frame" is "$e$ conjugates $I_{\mathrm{st}}$ to $I$". The transferable move, whenever a structure is *an operator on the fibres* (a complex structure, a product structure, a polarisation), is to encode compatibility as an intertwining equation $e\circ(\text{model operator})=(\text{fibre operator})\circ e$ and read the structure group off as the conjugation-stabiliser of the model operator. Contrast the volume-form row, where the structure was a *form* and compatibility was a scalar equation with stabiliser $SL_k$: form-type structures give determinant-type conditions, operator-type structures give commutator-type conditions.

**"Commutes with $I_{\mathrm{st}}$" is the algebraic engine of the complex row, exactly as "$\det=1$" was for the volume-form row.** The whole correspondence runs on one relation used twice: forward, $AI_{\mathrm{st}}=I_{\mathrm{st}}A$ is what keeps the complex-linear condition stable under change of frame, so the stabiliser is $GL_k(\mathbb C)$; backward, the same relation is what makes conjugation $I_P=pI_{\mathrm{st}}p^{-1}$ independent of the frame $p\in P_m$, since conjugating $I_{\mathrm{st}}$ by something that commutes with it changes nothing. The diagnostic to carry away: when a construction "transports a fixed model object through a frame", it is well defined precisely on the orbit of the subgroup fixing that model object, and identifying that subgroup tells you which reduction you need. Trying to transport through an arbitrary frame (the illegal shortcut) is the standard error, and its cure is always "restrict to the compatible frames".

**Two definitions of the same object should be reconciled by building each one's data from the other and checking the constructions undo each other — and the smooth version of "pick a basis" is the load-bearing step.** Part (i) is a template for every "coordinate-free datum $\leftrightarrow$ atlas of compatible charts" equivalence in bundle theory: from the intrinsic $I$ produce compatible local trivialisations, from compatible trivialisations reconstruct $I$, and verify mutual inversion. The one subtle point, which recurs constantly, is upgrading a *pointwise* linear-algebra choice (a complex basis of the single fibre $E_m$) to a *smooth local* choice (a complex frame near $m$); this is done by extending the fibre basis to smooth sections and using continuity of the determinant to guarantee they remain a basis on a neighbourhood. That "extend and use $\det\neq0$ on a neighbourhood" argument is the same device that produces smooth orthonormal frames (Gram–Schmidt, the $O(k)$ row) and smooth unimodular frames (rescaling, the $SL_k$ row in [[Ex - Fibrewise Volume Forms Correspond to SL(k,R)-Structures|the companion exercise]]); once a fibre basis is chosen, a neighbourhood on which it persists always exists, and that is what makes reductions smooth. The Hermitian refinement — reducing further to $U(k)$ by keeping only the $\mathbb C$-linear frames that are also orthonormal — is treated in [[Ex - Every Complex Vector Bundle Admits a Hermitian Structure|the Hermitian-structure exercise]] and completes the ladder $GL_{2k}(\mathbb R)\supset GL_k(\mathbb C)\supset U(k)$.
