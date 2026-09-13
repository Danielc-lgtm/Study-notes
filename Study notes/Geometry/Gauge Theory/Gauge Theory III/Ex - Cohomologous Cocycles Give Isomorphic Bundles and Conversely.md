---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Principal Bundles are Classified by Cocycles"
  - "Def - Transition Functions and the Cocycle Condition"
  - "Def - Principal G-Bundle"
  - "Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles"
  - "Thm - Existence of Smooth Bump Functions"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Fix a Lie group $G$ and cover the circle $S^1=\mathbb{R}/2\pi\mathbb{Z}$ by the two arcs
$$U_1=S^1\setminus\{[\pi]\}=\{[\phi]:-\pi<\phi<\pi\},\qquad U_2=S^1\setminus\{[0]\}=\{[\phi]:0<\phi<2\pi\}.$$
Their overlap has exactly two connected components,
$$U_{12}:=U_1\cap U_2=V_+\sqcup V_-,\qquad V_+=\{[\phi]:0<\phi<\pi\},\quad V_-=\{[\phi]:\pi<\phi<2\pi\}.$$
A principal $G$-bundle described on this cover is encoded by a single smooth **transition function** (a **cocycle**) $g_{12}\colon U_{12}\to G$; the remaining data $g_{21}=g_{12}^{-1}$ and $g_{11}=g_{22}=e$ are forced, and the triple-overlap cocycle condition is vacuous because there is no third set. Two such cocycles $g_{12},\tilde g_{12}\colon U_{12}\to G$ are **cohomologous** when there exist smooth maps $h_1\colon U_1\to G$ and $h_2\colon U_2\to G$ with
$$g_{12}(x)=h_1(x)\,\tilde g_{12}(x)\,h_2(x)^{-1}\qquad\text{for all }x\in U_{12}.$$

Prove, working entirely on this two-arc cover:

1. **($\Leftarrow$)** If $g_{12}$ and $\tilde g_{12}$ are cohomologous, then the reconstructed bundles $P$ and $\tilde P$ are isomorphic as principal $G$-bundles, by an explicit isomorphism.
2. **($\Rightarrow$)** If the reconstructed bundles $P$ and $\tilde P$ are isomorphic as principal $G$-bundles over the identity of $S^1$, then $g_{12}$ and $\tilde g_{12}$ are cohomologous.
3. **(Corollary)** Deduce that **every principal $U(1)$-bundle over $S^1$ is trivial**, by exhibiting an explicit coboundary $h_1,h_2$ that trivialises an arbitrary $U(1)$-valued transition function; the construction takes a smooth logarithm on each component of $U_{12}$.

This is the special case of part (c) of the general classification theorem drilled on the simplest base on which a bundle can be non-trivial, together with the observation — decisive for the corollary — that connectedness of the structure group collapses the whole classification.

**Recall:**

The framework is the reconstruction of a principal bundle from a cocycle and the coboundary relation between two systems of local sections.

![[Thm - Principal Bundles are Classified by Cocycles#Statement]]

For a cover $\{U_\alpha\}$ of a manifold $M$ and a system of smooth transition functions $g_{\alpha\beta}\colon U_{\alpha\beta}\to G$ satisfying the cocycle conditions, the **reconstructed bundle** is
$$P=\Big(\bigsqcup_\alpha U_\alpha\times G\Big)\Big/\sim,\qquad (x,g)_\alpha\sim(x,g')_\beta\ :\Longleftrightarrow\ x=x'\ \text{and}\ g=g_{\alpha\beta}(x)\,g',$$
with right action $[x,g]_\alpha\cdot k=[x,gk]_\alpha$, projection $\pi[x,g]_\alpha=x$, and canonical local sections $s_\alpha(x)=[x,e]_\alpha$ whose transition functions are the $g_{\alpha\beta}$. By part (a) it is a principal $G$-bundle; by part (b) every principal $G$-bundle with these transition functions is isomorphic to it; and by part (c) two cocycles on one cover reconstruct isomorphic bundles if and only if they are cohomologous.

![[Def - Transition Functions and the Cocycle Condition#The Definition]]

The **coboundary relation** between two systems of local sections of one bundle is the tool used in the ($\Rightarrow$) direction, restated here at its point of use:

> **Lemma (change of local sections gives a coboundary).** Let $Q\to M$ be a principal $G$-bundle and let $\{\sigma_\alpha\}$ and $\{\sigma'_\alpha\}$ be two systems of smooth local sections over the same cover $\{U_\alpha\}$, with transition functions $c_{\alpha\beta}$ (defined by $\sigma_\beta=\sigma_\alpha c_{\alpha\beta}$) and $c'_{\alpha\beta}$ respectively. There are unique smooth maps $h_\alpha\colon U_\alpha\to G$ with $\sigma'_\alpha=\sigma_\alpha h_\alpha$, and then $c'_{\alpha\beta}=h_\alpha^{-1}c_{\alpha\beta}h_\beta$; equivalently $c_{\alpha\beta}=h_\alpha c'_{\alpha\beta}h_\beta^{-1}$ after renaming $h_\alpha\mapsto h_\alpha^{-1}$.

This lemma is proved in full on **[[Def - Transition Functions and the Cocycle Condition]]** (it is the content of Bär's Theorem 2.2.11); the existence and uniqueness of $h_\alpha$ come from the freeness and fibrewise transitivity of the $G$-action, and its smoothness from a local trivialisation.

![[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles#Statement]]

The single clause used in the corollary is: **a principal $G$-bundle over a contractible manifold — in particular over an open interval — is trivial.** This is part (c) of the theorem above, proved there by sliding a trivialisation along the interval.

---

# Convergent Strategy

**Problem class.** This is a *both-directions equivalence* of the classifying kind: the objects are cocycles (local gluing recipes) on one side and bundle isomorphism classes on the other, and the claim is that the coboundary relation on cocycles is exactly the isomorphism relation on bundles. The special two-arc cover of $S^1$ strips the general theorem of everything inessential — a single transition function, no triple overlaps, a base that is a curve — so that the two directions and the connectedness corollary all become visible computations rather than bookkeeping.

**Assumption pattern.** Two hypotheses drive the two directions. Cohomology ($g_{12}=h_1\tilde g_{12}h_2^{-1}$) is an *explicit gluing datum* and is used constructively: it is fed straight into a candidate map between total spaces, whose well-definedness is the single identity $h_1^{-1}g_{12}=\tilde g_{12}h_2^{-1}$. Bundle isomorphism is an *abstract equality of gluing classes* and is used through the canonical sections: an isomorphism transports the canonical sections of $P$ onto a second system of sections of $\tilde P$, and two systems of sections of one bundle are always cohomologous. The corollary then adds the structural hypothesis "$U(1)$ is connected", which is used in the disguised form "a smooth $U(1)$-valued function on an interval has a smooth real logarithm".

**Theorem routing.** For ($\Leftarrow$): take the coboundary $h_1,h_2$; define $\Phi[x,g]_\alpha=[x,h_\alpha(x)^{-1}g]_\alpha$; verify well-definedness across the gluing, equivariance, smoothness, and that it is fibre-preserving over the identity, hence a principal-bundle isomorphism. For ($\Rightarrow$): apply the given isomorphism $\Phi\colon P\to\tilde P$ to the canonical sections $s_\alpha$ of $P$, note the images $\Phi\circ s_\alpha$ are sections of $\tilde P$ with transition functions $g_{\alpha\beta}$ (equivariance), and compare them with the canonical sections $\tilde s_\alpha$ of $\tilde P$ (transition functions $\tilde g_{\alpha\beta}$) through the coboundary lemma. For the corollary: use **[[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|triviality over an interval]]** to trivialise any $U(1)$-bundle over each arc, so it is reconstructed from some $g_{12}\colon U_{12}\to U(1)$; take a smooth logarithm on each component; extend the real phase across one arc; read off $h_1,h_2$ witnessing that $g_{12}$ is cohomologous to the constant cocycle $e$, whose bundle is the product.

**Key decision point.** The one genuinely non-obvious move is *which coboundary to write down in the corollary*. Because $U(1)$ is connected and each component of the overlap is an interval, the transition function has a smooth **real logarithm** there; the phase can then be extended smoothly across the middle of one arc (using a bump function), and the entire twist can be absorbed into a single $h_1$ with $h_2\equiv 1$. The contrast to keep in mind — and the reason this exercise is paired with the Möbius reconstruction — is that if the structure group were disconnected (say $\{\pm1\}$) the logarithm would not exist, the phase could not be extended, and some cocycles would not be coboundaries; connectedness is exactly what makes the extension unobstructed.

---

# Legal Operations Used

The topic page for §3.3 is not yet assembled; the operations are named descriptively and will be reconciled with its Legal Operations list.

1. **Reconstruct a bundle from a cocycle.** Turn a system of transition functions on a cover into the total space $\bigsqcup_\alpha U_\alpha\times G/\sim$; here the cover is two arcs and the datum is a single map $g_{12}$.

2. **Build a bundle map from a coboundary.** Given $h_1,h_2$ with $g_{12}=h_1\tilde g_{12}h_2^{-1}$, define $\Phi[x,g]_\alpha=[x,h_\alpha^{-1}g]_\alpha$ and verify the coboundary identity is exactly the condition for $\Phi$ to respect the two gluings.

3. **Verify a map is a principal-bundle isomorphism.** Check fibre-preservation over the identity, right-$G$-equivariance, smoothness in the reconstruction charts, and invertibility, so that a fibrewise bijection upgrades to a bundle isomorphism.

4. **Transport canonical sections through an isomorphism.** Apply an abstract bundle isomorphism to the canonical sections $s_\alpha=[x,e]_\alpha$ and use equivariance to compute the transition functions of the image sections.

5. **Compare two systems of sections of one bundle via the coboundary lemma.** Two systems of local sections of the same principal bundle are related by smooth $G$-valued maps, and their transition functions differ by the corresponding coboundary.

6. **Trivialise over a contractible piece.** Invoke that a principal bundle over an interval is trivial to obtain a local section, hence a description on the two-arc cover.

7. **Take a smooth logarithm on a contractible overlap component and extend it.** On each interval component of the overlap write a $U(1)$-valued map as $e^{i\theta}$ with smooth real $\theta$, then extend $\theta$ across an arc with a bump function to manufacture the trivialising coboundary.

---

# Hints

> [!note]- Hint 1
> On the two-arc cover there are no triple overlaps, so a "cocycle" is nothing but a single smooth map $g_{12}\colon U_{12}\to G$, and "cohomologous" is the single equation $g_{12}=h_1\tilde g_{12}h_2^{-1}$ on $U_{12}$. For the first direction, you are handed $h_1,h_2$; the reconstructed total spaces are quotients of $U_1\times G$ and $U_2\times G$. What is the most economical map $U_\alpha\times G\to U_\alpha\times G$ built from $h_\alpha$?

> [!note]- Hint 2
> Try $\Phi[x,g]_\alpha=[x,h_\alpha(x)^{-1}g]_\alpha$. The only thing that can go wrong is that a point of $P$ has two names, $[x,a]_1=[x,b]_2$ with $a=g_{12}(x)b$, and $\Phi$ must send them to the same point of $\tilde P$. Write out what $[x,h_1^{-1}a]_1=[x,h_2^{-1}b]_2$ means in $\tilde P$ and watch the coboundary identity appear.

> [!note]- Hint 3
> For the converse, remember that each reconstructed bundle carries *canonical* sections $s_\alpha(x)=[x,e]_\alpha$ whose transition functions are the original $g_{\alpha\beta}$. Push the sections of $P$ forward by the isomorphism $\Phi$. Because $\Phi$ commutes with the right $G$-action, the pushed-forward sections still have transition functions $g_{\alpha\beta}$ — but now they live in $\tilde P$, alongside the canonical sections $\tilde s_\alpha$ of $\tilde P$ with transition functions $\tilde g_{\alpha\beta}$. Two systems of sections of one bundle differ by a coboundary.

> [!note]- Hint 4
> For the corollary, first get onto the two-arc cover: each arc is contractible, so the bundle is trivial there and gives a section; hence any $U(1)$-bundle over $S^1$ is reconstructed from some $g_{12}\colon U_{12}\to U(1)$. Now trivialise $g_{12}$. On the interval $V_+$ write $g_{12}=e^{i\theta_+}$ with $\theta_+$ smooth and real; do the same on $V_-$. You want $h_1,h_2$ with $g_{12}=h_1h_2^{-1}$ (take $\tilde g_{12}\equiv 1$; $U(1)$ is abelian). Can you take $h_2\equiv 1$ and let $h_1$ be $e^{i\Theta}$ for a smooth $\Theta\colon U_1\to\mathbb{R}$ that equals $\theta_\pm$ near the two ends of the arc $U_1$?

---

# Solution

The two directions are the two ways the coboundary datum can be read: constructively (a coboundary *is* a bundle map) and abstractly (a bundle map *produces* a coboundary by comparing canonical sections). The corollary then uses that on a connected structure group the coboundary can always be produced, because a $U(1)$-valued function on an interval has a smooth logarithm and a real phase extends across an arc without obstruction.

**Step 1: The two-arc data and the shape of the two reconstructed bundles.**

On the cover $\{U_1,U_2\}$ a cocycle is a single smooth map $g_{12}\colon U_{12}\to G$, and the reconstructed bundle glues $U_1\times G$ to $U_2\times G$ over $U_{12}$.

> [!note]- Derivation
> The cocycle conditions on a two-set cover reduce to $g_{11}=g_{22}=e$ and $g_{21}=g_{12}^{-1}$ (from **[[Def - Transition Functions and the Cocycle Condition|the cocycle identities]]** $g_{\alpha\alpha}=e$ and $g_{\alpha\beta}=g_{\beta\alpha}^{-1}$), while the triple identity $g_{\alpha\beta}g_{\beta\gamma}g_{\gamma\alpha}=e$ is vacuous because $U_1\cap U_2\cap U_\gamma$ requires a third index. Hence the entire cocycle is the one smooth map $g_{12}\colon U_{12}\to G$, and every smooth $g_{12}$ is admissible.
>
> The reconstructed bundle is
> $$P=\big((U_1\times G)\sqcup(U_2\times G)\big)/\sim,\qquad (x,a)_1\sim(x,b)_2\iff x\in U_{12}\text{ and }a=g_{12}(x)\,b,$$
> with right action $[x,g]_\alpha\cdot k=[x,gk]_\alpha$ and $\pi[x,g]_\alpha=x$; its canonical sections are $s_\alpha(x)=[x,e]_\alpha$, and by construction $s_1(x)=[x,e]_1=[x,g_{12}(x)^{-1}]_2$ on $U_{12}$, so $s_2=s_1g_{12}$, recovering $g_{12}$ as the transition function (this is part (a) of **[[Thm - Principal Bundles are Classified by Cocycles|the classification theorem]]**, restated in the Recall). We write $\tilde P$ for the bundle reconstructed identically from $\tilde g_{12}$, with gluing $\approx$ and canonical sections $\tilde s_\alpha$.

**Step 2 (Direction $\Leftarrow$): a coboundary defines an explicit isomorphism.**

Assume $g_{12}=h_1\tilde g_{12}h_2^{-1}$ on $U_{12}$ for smooth $h_1\colon U_1\to G$, $h_2\colon U_2\to G$. Then
$$\Phi\colon P\to\tilde P,\qquad \Phi\big([x,g]_\alpha\big)=[x,\,h_\alpha(x)^{-1}g]_\alpha$$
is a well-defined isomorphism of principal $G$-bundles over $\mathrm{id}_{S^1}$.

> [!note]- Derivation
> **Well-definedness across the gluing.** The map is given on the two pieces $U_\alpha\times G$ by $(x,g)\mapsto(x,h_\alpha(x)^{-1}g)$, which descends to the quotient provided it respects $\sim$. The only identifications are over $U_{12}$, between index $1$ and index $2$. Suppose $[x,a]_1=[x,b]_2$ in $P$; by Step 1 this means
> $$a=g_{12}(x)\,b.$$
> We must check $\Phi[x,a]_1=\Phi[x,b]_2$ in $\tilde P$, that is $[x,h_1(x)^{-1}a]_1=[x,h_2(x)^{-1}b]_2$, which by the definition of $\approx$ means
> $$h_1(x)^{-1}a=\tilde g_{12}(x)\,\big(h_2(x)^{-1}b\big).$$
> Compute the left-hand side using $a=g_{12}(x)b$ and the coboundary hypothesis $g_{12}=h_1\tilde g_{12}h_2^{-1}$:
> $$h_1^{-1}a=h_1^{-1}g_{12}\,b=h_1^{-1}\big(h_1\tilde g_{12}h_2^{-1}\big)b=\tilde g_{12}\,h_2^{-1}b\qquad\text{(substitute }a\text{; substitute }g_{12}\text{; cancel }h_1^{-1}h_1=e\text{).}$$
> This is exactly the right-hand side, so $\Phi$ is well-defined. (Arguments over $U_1$-only or $U_2$-only points involve no identification and are automatic.)
>
> **Equivariance.** For $k\in G$,
> $$\Phi\big([x,g]_\alpha\cdot k\big)=\Phi\big([x,gk]_\alpha\big)=[x,h_\alpha^{-1}gk]_\alpha=[x,h_\alpha^{-1}g]_\alpha\cdot k=\Phi\big([x,g]_\alpha\big)\cdot k\qquad\text{(definition of the action; definition of }\Phi\text{; definition of the action).}$$
>
> **Fibre-preservation and smoothness.** $\pi_{\tilde P}\big(\Phi[x,g]_\alpha\big)=x=\pi_P[x,g]_\alpha$, so $\Phi$ covers $\mathrm{id}_{S^1}$. In the reconstruction charts $U_\alpha\times G\to P$ (diffeomorphisms onto open sets, by part (a) of the classification theorem) $\Phi$ reads $(x,g)\mapsto(x,h_\alpha(x)^{-1}g)$, which is smooth because $h_\alpha$ is smooth and group multiplication and inversion are smooth.
>
> **Inverse.** The coboundary relation is symmetric: $\tilde g_{12}=h_1^{-1}g_{12}h_2$ exhibits $\tilde g_{12}$ as a coboundary of $g_{12}$ with maps $h_1^{-1},h_2^{-1}$. The same construction gives $\Psi\colon\tilde P\to P$, $\Psi[x,\tilde g]_\alpha=[x,h_\alpha(x)\tilde g]_\alpha$, and $\Psi\circ\Phi[x,g]_\alpha=[x,h_\alpha h_\alpha^{-1}g]_\alpha=[x,g]_\alpha$, likewise $\Phi\circ\Psi=\mathrm{id}$. Hence $\Phi$ is a diffeomorphism.
>
> A fibre-preserving, right-$G$-equivariant diffeomorphism over the identity is precisely an isomorphism of principal $G$-bundles. Therefore $P\cong\tilde P$.

**Step 3 (Direction $\Rightarrow$): an isomorphism produces a coboundary.**

Conversely, assume $\Phi\colon P\to\tilde P$ is an isomorphism of principal $G$-bundles over $\mathrm{id}_{S^1}$. Then $g_{12}$ and $\tilde g_{12}$ are cohomologous.

> [!note]- Derivation
> **Push the canonical sections forward.** Let $s_\alpha(x)=[x,e]_\alpha$ be the canonical sections of $P$ over $U_\alpha$ and set
> $$\hat s_\alpha:=\Phi\circ s_\alpha\colon U_\alpha\to\tilde P.$$
> Each $\hat s_\alpha$ is a smooth section of $\tilde P$ over $U_\alpha$ because $\Phi$ is a smooth bundle map over the identity: $\pi_{\tilde P}\circ\hat s_\alpha=\pi_{\tilde P}\circ\Phi\circ s_\alpha=\pi_P\circ s_\alpha=\mathrm{id}_{U_\alpha}$.
>
> **Their transition functions are $g_{\alpha\beta}$.** By Step 1 the canonical sections of $P$ satisfy $s_\beta=s_\alpha g_{\alpha\beta}$ on $U_{\alpha\beta}$. Applying $\Phi$ and using its right-$G$-equivariance (invoked by name),
> $$\hat s_\beta=\Phi\circ s_\beta=\Phi\big(s_\alpha\,g_{\alpha\beta}\big)=\big(\Phi\circ s_\alpha\big)g_{\alpha\beta}=\hat s_\alpha\,g_{\alpha\beta}\qquad\text{(definition of }\hat s\text{; }s_\beta=s_\alpha g_{\alpha\beta}\text{; equivariance of }\Phi\text{; definition of }\hat s\text{).}$$
> So $\{\hat s_\alpha\}$ is a system of local sections of $\tilde P$ with transition functions $g_{\alpha\beta}$.
>
> **Compare with the canonical sections of $\tilde P$.** The bundle $\tilde P$ also carries its canonical sections $\tilde s_\alpha$, with transition functions $\tilde g_{\alpha\beta}$. Now $\{\hat s_\alpha\}$ and $\{\tilde s_\alpha\}$ are two systems of local sections of the *same* principal bundle $\tilde P$ over the same cover. By the **coboundary lemma** (change of local sections gives a coboundary; restated in the Recall, proved on **[[Def - Transition Functions and the Cocycle Condition]]**) there are unique smooth $h_\alpha\colon U_\alpha\to G$ with $\tilde s_\alpha=\hat s_\alpha\,h_\alpha$, and then the two transition systems are related by
> $$g_{\alpha\beta}=h_\alpha\,\tilde g_{\alpha\beta}\,h_\beta^{-1}\qquad\text{on }U_{\alpha\beta}.$$
> (Here $\{\hat s_\alpha\}$ plays the role of the first system, with transition functions $g_{\alpha\beta}$, and $\{\tilde s_\alpha\}=\{\hat s_\alpha h_\alpha\}$ the second, with $\tilde g_{\alpha\beta}$; the lemma's identity $c'_{\alpha\beta}=h_\alpha^{-1}c_{\alpha\beta}h_\beta$ reads $\tilde g_{\alpha\beta}=h_\alpha^{-1}g_{\alpha\beta}h_\beta$, which rearranges to the displayed equation.)
>
> For the two-arc cover this is the single equation $g_{12}=h_1\tilde g_{12}h_2^{-1}$ on $U_{12}$: the cocycles are cohomologous.

**Step 4 (Corollary): every principal $U(1)$-bundle over $S^1$ is trivial.**

Take $G=U(1)$. Any principal $U(1)$-bundle over $S^1$ is reconstructed from some $g_{12}\colon U_{12}\to U(1)$, and every such $g_{12}$ is cohomologous to the constant cocycle $e$, whose bundle is the product $S^1\times U(1)$. Hence the bundle is trivial.

> [!note]- Derivation
> **Reduce to the two-arc cover.** Let $P\to S^1$ be a principal $U(1)$-bundle. Each arc $U_\alpha$ is diffeomorphic to the open interval $(-\pi,\pi)$ (respectively $(0,2\pi)$), hence contractible, so by **[[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|triviality over a contractible base]]** — restated in the Recall — the restriction $P|_{U_\alpha}$ is trivial and admits a smooth section $s_\alpha\colon U_\alpha\to P$. These two sections have a transition function $g_{12}\colon U_{12}\to U(1)$ with $s_2=s_1g_{12}$, and by part (b) of **[[Thm - Principal Bundles are Classified by Cocycles|the classification theorem]]** $P$ is isomorphic to the bundle reconstructed from $g_{12}$. It therefore suffices to trivialise $g_{12}$.
>
> **A smooth logarithm on each overlap component.** Fix one component of $U_{12}$, an interval $I$ parametrised by $\phi$, and view $g:=g_{12}|_I\colon I\to U(1)\subset\mathbb{C}$ as a smooth map with $|g|\equiv 1$. Differentiating $\bar g g=1$ gives $\overline{g}\,g'+\overline{g'}\,g=0$, so $\overline g\,g'=-\overline{\overline g\,g'}$ is purely imaginary; write $\overline g\,g'=i\rho$ with $\rho:=\operatorname{Im}(\overline g\,g')\colon I\to\mathbb{R}$ smooth. Choose $\phi_0\in I$ and $\theta_0\in\mathbb{R}$ with $e^{i\theta_0}=g(\phi_0)$, and set
> $$\theta(\phi):=\theta_0+\int_{\phi_0}^{\phi}\rho(\tau)\,d\tau\qquad(\phi\in I).$$
> Then $\theta$ is smooth and $g=e^{i\theta}$ on $I$: indeed
> $$\frac{d}{d\phi}\big(g\,e^{-i\theta}\big)=g'e^{-i\theta}-i\theta'\,g\,e^{-i\theta}=e^{-i\theta}\big(g'-i\rho\,g\big)\qquad\text{(product rule; }\theta'=\rho\text{),}$$
> and $i\rho\,g=(\overline g\,g')\,g=g'(\overline g\,g)=g'|g|^2=g'$, so the bracket vanishes; hence $g\,e^{-i\theta}$ is constant, equal to its value $g(\phi_0)e^{-i\theta_0}=1$ at $\phi_0$, giving $g=e^{i\theta}$. Applying this on the two components produces smooth real phases
> $$\theta_+\colon V_+\to\mathbb{R},\qquad\theta_-\colon V_-\to\mathbb{R},\qquad g_{12}=e^{i\theta_\pm}\ \text{on}\ V_\pm.$$
>
> **Extend the phase across one arc.** The two components $V_+,V_-$ are the two ends of the arc $U_1=\{[\phi]:-\pi<\phi<\pi\}$: on $U_1$ they are $\{0<\phi<\pi\}$ and $\{-\pi<\phi<0\}$ (the latter is $V_-$ written in the coordinate of $U_1$). Choose disjoint closed sub-intervals $K_+\subset\{0<\phi<\pi\}$ and $K_-\subset\{-\pi<\phi<0\}$ containing the ends, and a smooth bump function $\chi\colon U_1\to[0,1]$ with $\chi\equiv 1$ on a neighbourhood of $K_+\cup K_-$ inside $V_+\cup V_-$ and $\chi$ supported away from a neighbourhood of $\phi=0$ (such $\chi$ exists by **[[Thm - Existence of Smooth Bump Functions|the existence of smooth bump functions]]**). Because $V_+$ and $V_-$ are disjoint sub-arcs at opposite ends of the interval $U_1$, the function equal to $\theta_+$ on the outer end and to $\theta_-$ on the inner end extends to a single smooth $\Theta\colon U_1\to\mathbb{R}$ with $\Theta=\theta_\pm$ on the two components of $U_{12}$: explicitly, pick any smooth $\Theta_0\colon U_1\to\mathbb{R}$ that restricts to $\theta_+$ near the $V_+$-end and to $\theta_-$ near the $V_-$-end (interpolate arbitrarily in the middle, where no constraint is imposed — this is where connectedness of $U(1)$, i.e. the freedom of the real logarithm, is used), and set $\Theta:=\Theta_0$. There is no matching condition to violate because the constraints sit on the two *disjoint* ends of a single interval.
>
> **Read off the coboundary.** Define
> $$h_1:=e^{i\Theta}\colon U_1\to U(1),\qquad h_2:\equiv 1\colon U_2\to U(1).$$
> Both are smooth. On $U_{12}$ we have $h_1h_2^{-1}=e^{i\Theta}=e^{i\theta_\pm}=g_{12}$ on $V_\pm$, that is
> $$g_{12}=h_1\cdot 1\cdot h_2^{-1}=h_1\,\tilde g_{12}\,h_2^{-1}\qquad\text{with }\tilde g_{12}\equiv 1.$$
> Thus $g_{12}$ is cohomologous to the constant cocycle $e$. By Step 2 the bundle reconstructed from $g_{12}$ is isomorphic to the bundle reconstructed from $\tilde g_{12}\equiv e$, which is the product $S^1\times U(1)$ (the canonical sections $\tilde s_\alpha$ glue with $\tilde g_{12}\equiv e$, so they patch to a global section, and by **[[Thm - Sections of a Principal Bundle and Triviality|a principal bundle with a global section is trivial]]** the bundle is the product). Therefore $P$ is trivial.

> [!note]- Complete formal solution
> **Claim.** On the two-arc cover $\{U_1,U_2\}$ of $S^1$ two cocycles $g_{12},\tilde g_{12}\colon U_{12}\to G$ reconstruct isomorphic principal $G$-bundles if and only if they are cohomologous; consequently every principal $U(1)$-bundle over $S^1$ is trivial.
>
> On this cover a cocycle is a single smooth map $g_{12}\colon U_{12}\to G$ (the identities $g_{\alpha\alpha}=e$, $g_{21}=g_{12}^{-1}$ are forced, the triple identity vacuous), and the reconstructed bundle is $P=(U_1\times G)\sqcup(U_2\times G)/\!\sim$ with $(x,a)_1\sim(x,b)_2\iff x\in U_{12},\ a=g_{12}(x)b$, right action $[x,g]_\alpha k=[x,gk]_\alpha$, canonical sections $s_\alpha=[x,e]_\alpha$, $s_2=s_1g_{12}$.
>
> ($\Leftarrow$) Given $g_{12}=h_1\tilde g_{12}h_2^{-1}$ with $h_\alpha\colon U_\alpha\to G$ smooth, define $\Phi[x,g]_\alpha=[x,h_\alpha(x)^{-1}g]_\alpha$. If $[x,a]_1=[x,b]_2$, i.e. $a=g_{12}b$, then $h_1^{-1}a=h_1^{-1}g_{12}b=h_1^{-1}(h_1\tilde g_{12}h_2^{-1})b=\tilde g_{12}(h_2^{-1}b)$, so $[x,h_1^{-1}a]_1=[x,h_2^{-1}b]_2$ in $\tilde P$: $\Phi$ is well-defined. It is equivariant ($\Phi([x,g]_\alpha k)=[x,h_\alpha^{-1}gk]_\alpha=\Phi([x,g]_\alpha)k$), covers $\mathrm{id}_{S^1}$, is smooth in the reconstruction charts, and has smooth inverse $[x,\tilde g]_\alpha\mapsto[x,h_\alpha\tilde g]_\alpha$; hence it is a principal-bundle isomorphism, $P\cong\tilde P$.
>
> ($\Rightarrow$) Given an isomorphism $\Phi\colon P\to\tilde P$ over $\mathrm{id}_{S^1}$, the sections $\hat s_\alpha=\Phi\circ s_\alpha$ of $\tilde P$ satisfy $\hat s_\beta=\Phi(s_\alpha g_{\alpha\beta})=\hat s_\alpha g_{\alpha\beta}$ by equivariance, so they have transition functions $g_{\alpha\beta}$. The canonical sections $\tilde s_\alpha$ of $\tilde P$ have transition functions $\tilde g_{\alpha\beta}$. Two systems of sections of one bundle satisfy $\tilde s_\alpha=\hat s_\alpha h_\alpha$ for unique smooth $h_\alpha$, and by the coboundary lemma (proved on [[Def - Transition Functions and the Cocycle Condition]]) $\tilde g_{\alpha\beta}=h_\alpha^{-1}g_{\alpha\beta}h_\beta$, i.e. $g_{12}=h_1\tilde g_{12}h_2^{-1}$: cohomologous.
>
> (Corollary) For $G=U(1)$: each arc is contractible, so $P|_{U_\alpha}$ is trivial ([[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|triviality over an interval]]) with a section $s_\alpha$; $P$ is reconstructed from the resulting $g_{12}\colon U_{12}\to U(1)$. On each interval component of $U_{12}$, $g_{12}=e^{i\theta_\pm}$ for a smooth real $\theta_\pm$ (set $\theta=\theta_0+\int\operatorname{Im}(\bar g g')$; then $(ge^{-i\theta})'=0$). Extend the two boundary phases to a smooth $\Theta\colon U_1\to\mathbb{R}$ (unobstructed: the constraints sit on disjoint ends of an interval; bump function), and put $h_1=e^{i\Theta}$, $h_2\equiv 1$. Then $g_{12}=h_1h_2^{-1}$, so $g_{12}$ is cohomologous to $e$; by ($\Leftarrow$) the bundle is isomorphic to the one from the trivial cocycle, namely $S^1\times U(1)$. Hence every principal $U(1)$-bundle over $S^1$ is trivial. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> One is tempted to conclude "$P$ and $\tilde P$ are isomorphic $\Rightarrow$ cohomologous" by *choosing new sections of $P$* rather than pushing sections *into $\tilde P$*. That confuses the two bundles: the coboundary lemma compares two section systems of **one** bundle, so the isomorphism must first be used to move the sections of $P$ into $\tilde P$ (the step $\hat s_\alpha=\Phi\circ s_\alpha$). Skipping it compares sections living in different total spaces, where "$\tilde s_\alpha=\hat s_\alpha h_\alpha$" is not even a meaningful equation. The step that makes it legal is equivariance of $\Phi$, which guarantees the transported sections keep the transition functions $g_{\alpha\beta}$.

---

# Key Takeaways

**A coboundary is not merely a certificate that two bundles are isomorphic; it *is* the isomorphism, written out.** The content of the ($\Leftarrow$) direction is that the very maps $h_\alpha$ appearing in $g_{\alpha\beta}=h_\alpha\tilde g_{\alpha\beta}h_\beta^{-1}$ assemble, one arc at a time, into the bundle map $[x,g]_\alpha\mapsto[x,h_\alpha^{-1}g]_\alpha$, and the coboundary identity is precisely the compatibility that lets the piecewise definition survive the gluing. Whenever a problem hands you a coboundary relation between cocycles, the reflex should be to *build the isomorphism from it* rather than to search for one abstractly. The reverse direction is the same fact read backwards: an abstract isomorphism, applied to the canonical sections, manufactures the maps $h_\alpha$ by comparing two section systems of one bundle. The trigger for that reading is the phrase "canonical sections", which every reconstructed bundle carries and whose transition functions are, by construction, the cocycle itself; transporting them by an isomorphism and using equivariance is the standard way to convert "isomorphic" into "cohomologous".

**Connectedness of the structure group is what collapses the classification over $S^1$.** The corollary is not really about $U(1)$ as a circle; it is about $U(1)$ being *connected*, hence about every $U(1)$-valued function on an interval having a smooth real logarithm. That logarithm is the only reason the trivialising phase $\Theta$ can be extended across the middle of an arc: the two constraints it must satisfy live on the two disjoint ends of an interval, so there is nothing to obstruct the interpolation. The transferable diagnostic is that principal $G$-bundles over $S^1$ are classified by $\pi_0(G)$ — the components of the structure group — through the values of the transition function on the two components of the overlap; when $G$ is connected there is one class (trivial), and the logarithm exhibits it explicitly. The companion exercise **[[Ex - Reconstructing the Möbius Bundle from a Z over 2 Cocycle]]** is the same computation with $G=\{\pm1\}$ disconnected, where the extension is obstructed and a genuinely non-trivial bundle survives; reading the two side by side isolates exactly which hypothesis does the work.

**On the two-arc cover the entire theory of cocycles becomes one map and one equation, and this is the right laboratory for the general statement.** Because there are no triple overlaps, the cocycle condition is trivial and a bundle is a single smooth $g_{12}\colon U_{12}\to G$; because the overlap has two components, the interesting information is the pair of "germs" of $g_{12}$ at the two components, and cohomology is the freedom to adjust them by boundary values $h_1,h_2$. Every phenomenon of the general classification theorem — reconstruction, the meaning of an isomorphism, the coboundary relation — is present here in miniature and can be checked by hand, which is why this drill is worth reconstructing from scratch after a lapse: if you can rebuild the explicit $\Phi$ and the logarithmic coboundary, you have internalised the general theorem. The single sentence to remember is that *a principal bundle is a gluing recipe, the recipe is the cocycle, and changing the local sections changes the recipe by a coboundary* — over $S^1$ with two arcs, "recipe" is one map and "coboundary" is the room the two arcs give you to absorb it.
