---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Principal G-Bundle"
  - "Def - Fundamental Vector Field of a Group Action"
  - "Def - Equivariant and Basic Forms on a Principal Bundle"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\pi\colon P\to M$ be a **principal $G$-bundle**, with $G$ a Lie group of Lie algebra $\mathfrak{g}=T_eG$ acting on $P$ from the right, $R_g(p)=p\cdot g$. Fix a point $p\in P$. Two subspaces of the tangent space $T_pP$ are in play. The **vertical subspace** is
$$V_p:=\ker d\pi_p=\{v\in T_pP:d\pi_p(v)=0\}\subseteq T_pP,$$
the directions in which $\pi$ does not move. For each $\xi\in\mathfrak{g}$ the **fundamental vector field** $K_\xi$ has value
$$K_\xi(p):=\frac{d}{dt}\Big|_{t=0}\big(p\cdot\exp(t\xi)\big)\in T_pP,$$
the velocity at $p$ of the flow of the one-parameter subgroup $t\mapsto\exp(t\xi)$.

Prove the following.

1. **Set equality.** $V_p=\{K_\xi(p):\xi\in\mathfrak{g}\}$: a tangent vector at $p$ is vertical if and only if it is the value at $p$ of some fundamental vector field.
2. **Canonical isomorphism.** The map $K_p\colon\mathfrak{g}\to T_pP$, $\xi\mapsto K_\xi(p)$, is a linear isomorphism onto $V_p$; consequently $V_p\cong\mathfrak{g}$ canonically, with no choice of frame or trivialisation involved.

The two ingredients the argument must combine are named in the title of the technique: a **dimension count** (to see that the space $\{K_\xi(p)\}$ is as large as $V_p$) and **freeness** of the action (to see that distinct $\xi$ give distinct vertical vectors).

**Recall:**

The objects in play are a principal $G$-bundle, the fundamental vector field of a Lie-algebra element, the vertical subspace of a principal bundle, and the flow of a vector field.

![[Def - Principal G-Bundle#The Definition]]

A [[Def - Principal G-Bundle|principal $G$-bundle]] is a fibre bundle $\pi\colon P\to M$ carrying a smooth **free** right $G$-action that preserves the fibres ($\pi(p\cdot g)=\pi(p)$) and is **transitive** on each of them, together with $G$-equivariant local trivialisations. Two consequences of this definition are used below and restated where they are needed: $\pi$ is a **surjective submersion** (so $d\pi_p$ is surjective for every $p$), and the typical fibre is $G$, so $\dim P=\dim M+\dim G$. "Free" means $p\cdot g=p$ for a single $p$ already forces $g=e$.

![[Def - Fundamental Vector Field of a Group Action#The Definition]]

For a right action, the [[Def - Fundamental Vector Field of a Group Action|fundamental vector field]] of $\xi\in\mathfrak{g}$ is the smooth vector field $K_\xi$ on $P$ with $K_\xi(q)=\frac{d}{dt}\big|_{0}\,q\cdot\exp(t\xi)$; in the series' standing notation this same field is written $\xi_P$, and we use $K_\xi$ here to match the source (Haydys, §2.2). Writing $\ell_p\colon G\to P$, $\ell_p(g)=p\cdot g$, for the orbit map through $p$, one has $K_\xi(p)=d_e\ell_p(\xi)$, so $\xi\mapsto K_\xi(p)$ is linear.

![[Def - Equivariant and Basic Forms on a Principal Bundle#The Definition]]

The **vertical subspace** at $p$ is $V_p=\ker d\pi_p$; a differential form on $P$ is called **basic** when it vanishes as soon as one of its arguments is vertical. The present exercise supplies the geometric fact that makes "basic" a usable notion: the vertical vectors are exactly the infinitesimal generators of the group action, so a basic form is precisely one that ignores the group directions.

The single external analytic input is the uniqueness half of the theory of flows.

> A smooth vector field $X$ on a manifold has, through each point $q$, a **unique** maximal integral curve $\gamma$ with $\gamma(0)=q$ and $\gamma'(t)=X(\gamma(t))$; in particular, if $X(q)=0$ then the constant curve $t\mapsto q$ is *the* integral curve through $q$. This is the content of the [[Thm - Fundamental Theorem on Flows|fundamental theorem on flows]] and the underlying existence-and-uniqueness theorem for integral curves.

---

# Convergent Strategy

**Problem class.** This is a *two-subspaces-are-equal* problem, of the kind that is almost always won not by a direct mutual-inclusion chase of individual vectors but by producing a single linear map, showing its image lands in one subspace, and then matching dimensions. One inclusion here is completely soft (every $K_\xi(p)$ is vertical); the whole content is the reverse inclusion, and dimension counting converts it into arithmetic once injectivity is in hand.

**Assumption pattern.** The principal-bundle hypotheses split cleanly by role. *Freeness* is the hypothesis that controls the **domain** side: it is used exactly once, to prove that $\xi\mapsto K_\xi(p)$ has trivial kernel, so that its image has dimension $\dim\mathfrak{g}$. The *fibre-bundle structure* (that $\pi$ is a submersion with fibre $G$) controls the **target** side: it fixes $\dim V_p=\dim P-\dim M=\dim G$. The recognisable trigger is that we are asked to identify a kernel ($V_p=\ker d\pi_p$) with an image ($\operatorname{im}K_p$), and the two hypotheses are precisely what pin the two dimensions to the common value $\dim G$.

**Theorem routing.** The route is: (i) show $\operatorname{im}K_p\subseteq V_p$ by differentiating $\pi(p\cdot\exp(t\xi))=\pi(p)$; (ii) show $K_p$ injective by identifying the flow of $K_\xi$ with the right action $R_{\exp(t\xi)}$ and invoking the uniqueness clause of the [[Thm - Fundamental Theorem on Flows|fundamental theorem on flows]] together with **freeness**; (iii) compute $\dim V_p=\dim G$ from the [[Def - Principal G-Bundle|submersion property and the fibre dimension]]; (iv) conclude by the elementary fact that a subspace of a finite-dimensional space whose dimension equals that of the ambient space is the whole space.

**Key decision point.** The one genuinely non-obvious move is *how* freeness enters. Freeness is a statement about the group acting without fixed points; it does not, on its face, say anything about tangent vectors. The bridge is the observation that $K_\xi$ is not an arbitrary field but the *generator of the action*, whose flow is $R_{\exp(t\xi)}$. A zero of a vector field is an equilibrium of its flow; so $K_\xi(p)=0$ says $p$ is fixed by every $\exp(t\xi)$, and *now* freeness applies and forces $\exp(t\xi)=e$ for all $t$, hence $\xi=0$. Recognising that "$K_\xi(p)=0$" must be upgraded from an infinitesimal statement to the finite statement "$p$ is fixed by the whole one-parameter subgroup" before freeness can be used is the crux of the exercise.

---

# Legal Operations Used

The solution deploys the following operations; where the §3.4 topic page numbers its Legal Operations, these correspond to the operations for passing between the group action, its infinitesimal generators, and the bundle projection.

1. **Differentiate an identity in the group parameter to get an infinitesimal identity.** From the finite fact $\pi(p\cdot g)=\pi(p)$, valid for all $g$, differentiate along $g=\exp(t\xi)$ at $t=0$ to obtain $d\pi_p(K_\xi(p))=0$. This is the manufacture of a vertical vector out of the fibre-preservation property.

2. **Recognise a fundamental vector field as the generator of the action, and read off its flow.** The integral curve of $K_\xi$ through $q$ is $t\mapsto q\cdot\exp(t\xi)$; the flow of $K_\xi$ is the right translation $R_{\exp(t\xi)}$. This turns a differential-geometric object (a vector field) into a group-theoretic one (a one-parameter subgroup acting).

3. **Upgrade a vanishing derivative to a fixed point via uniqueness of integral curves.** A zero of $K_\xi$ at $p$ makes the constant curve the integral curve through $p$; uniqueness forces $p\cdot\exp(t\xi)=p$ for all $t$. This is the operation that lets the finite hypothesis of freeness bite on infinitesimal data.

4. **Invoke freeness to pass from a fixed point of a one-parameter subgroup to the vanishing of its generator.** From $p\cdot\exp(t\xi)=p$ and freeness, $\exp(t\xi)=e$ for all $t$, hence $\xi=0$.

5. **Match dimensions to promote an inclusion of subspaces to an equality.** With $\operatorname{im}K_p\subseteq V_p$ and $\dim\operatorname{im}K_p=\dim G=\dim V_p$, conclude $\operatorname{im}K_p=V_p$.

---

# Hints

> [!note]- Hint 1
> Split the target statement $V_p=\{K_\xi(p)\}$ into two inclusions and rank them by difficulty. One direction — every $K_\xi(p)$ is vertical — is a one-line differentiation of the fibre-preservation identity $\pi(p\cdot g)=\pi(p)$. The other direction is the substance; do not attack it by taking an arbitrary vertical vector and building a $\xi$, but instead count dimensions.

> [!note]- Hint 2
> The map $K_p\colon\mathfrak{g}\to T_pP$, $\xi\mapsto K_\xi(p)$, is linear (it is $d_e\ell_p$ for the orbit map $\ell_p(g)=p\cdot g$) and has image inside $V_p$. If you can show it is injective, its image has dimension $\dim\mathfrak{g}=\dim G$. Separately, what is $\dim V_p$? Use that $\pi$ is a submersion and that $\dim P=\dim M+\dim G$.

> [!note]- Hint 3
> For injectivity you must use freeness, but freeness talks about group elements, not tangent vectors. Bridge the gap: the fundamental vector field $K_\xi$ has a flow. Compute it. Show that $t\mapsto q\cdot\exp(t\xi)$ is the integral curve of $K_\xi$ through $q$ (you will need $\exp\big((t+s)\xi\big)=\exp(t\xi)\exp(s\xi)$).

> [!note]- Hint 4
> Suppose $K_\xi(p)=0$. Then $p$ is a zero of the field $K_\xi$, so the *constant* curve at $p$ is an integral curve of $K_\xi$. By uniqueness of integral curves, the integral curve through $p$ you found in Hint 3 must be constant: $p\cdot\exp(t\xi)=p$ for all $t$. Now freeness applies. Finish, then assemble: injective linear map into $V_p$ with $\dim\operatorname{im}=\dim V_p$ is onto.

---

# Solution

The proof is the standard "a linear map whose image sits in a subspace, is injective, and matches the subspace's dimension is an isomorphism onto it" argument, with the two dimensions supplied by the two halves of the principal-bundle structure. Freeness makes $K_p=d_e\ell_p$ injective; the submersion property and the fibre dimension make $\dim V_p=\dim G$; and the soft inclusion $\operatorname{im}K_p\subseteq V_p$ is a one-line differentiation. The one subtlety, isolated in Step 2, is that freeness is a finite statement and must be reached through the flow of $K_\xi$ and the uniqueness of integral curves.

**Step 1: Every fundamental vector is vertical, and $K_p$ is linear.**

We show the linear map $K_p\colon\mathfrak{g}\to T_pP$, $\xi\mapsto K_\xi(p)$, has image contained in $V_p=\ker d\pi_p$.

> [!note]- Derivation
> Fix $\xi\in\mathfrak{g}$ and consider the smooth curve $c(t):=p\cdot\exp(t\xi)$ in $P$, with $c(0)=p$ and $c'(0)=K_\xi(p)$ by the definition of the fundamental vector field.
>
> **The projection of $c$ is constant.** Because the $G$-action preserves fibres (a defining clause of a [[Def - Principal G-Bundle|principal $G$-bundle]]: $\pi(q\cdot g)=\pi(q)$ for all $q\in P$, $g\in G$),
> $$\pi\big(c(t)\big)=\pi\big(p\cdot\exp(t\xi)\big)=\pi(p)\qquad\text{for all }t\qquad\text{(fibre-preservation of the action).}$$
> The right-hand side does not depend on $t$, so $t\mapsto\pi(c(t))$ is the constant curve at $\pi(p)$.
>
> **Differentiate.** Applying $\frac{d}{dt}\big|_{0}$ and the chain rule,
> $$d\pi_p\big(K_\xi(p)\big)=d\pi_p\big(c'(0)\big)=\frac{d}{dt}\Big|_{0}\pi\big(c(t)\big)=\frac{d}{dt}\Big|_{0}\pi(p)=0\qquad\text{(chain rule; constancy of }\pi\circ c\text{).}$$
> Hence $K_\xi(p)\in\ker d\pi_p=V_p$.
>
> **Linearity of $K_p$.** Let $\ell_p\colon G\to P$, $\ell_p(g)=p\cdot g$, be the orbit map through $p$; it is smooth because the action is smooth. Then, by the chain rule and $\frac{d}{dt}\big|_{0}\exp(t\xi)=\xi$ (the exponential map has differential the identity at the origin, $d_0\exp=\operatorname{id}_{\mathfrak g}$),
> $$K_\xi(p)=\frac{d}{dt}\Big|_{0}\ell_p\big(\exp(t\xi)\big)=d_e\ell_p\Big(\frac{d}{dt}\Big|_{0}\exp(t\xi)\Big)=d_e\ell_p(\xi)\qquad\text{(chain rule; }d_0\exp=\operatorname{id}\text{).}$$
> Thus $K_p=d_e\ell_p\colon\mathfrak{g}=T_eG\to T_pP$ is the differential of a smooth map at a point, hence linear. Combining with the previous paragraph, $K_p$ is a linear map with $\operatorname{im}K_p\subseteq V_p$.

**Step 2: $K_p$ is injective (this is where freeness is used).**

We show that $K_\xi(p)=0$ forces $\xi=0$, so $\ker K_p=\{0\}$.

> [!note]- Derivation
> The argument passes through the flow of the field $K_\xi$; we first identify that flow, then use it.
>
> **The flow of $K_\xi$ is right translation by $\exp(t\xi)$.** Fix an arbitrary $q\in P$ and set $\gamma_q(t):=q\cdot\exp(t\xi)$. Then $\gamma_q(0)=q$, and differentiating,
> $$\gamma_q'(t)=\frac{d}{ds}\Big|_{0}\,q\cdot\exp\big((t+s)\xi\big)=\frac{d}{ds}\Big|_{0}\,\big(q\cdot\exp(t\xi)\big)\cdot\exp(s\xi)=K_\xi\big(q\cdot\exp(t\xi)\big)=K_\xi\big(\gamma_q(t)\big),$$
> where the second equality is the one-parameter-subgroup identity $\exp\big((t+s)\xi\big)=\exp(t\xi)\exp(s\xi)$ together with associativity of the action, and the third is the definition of $K_\xi$ evaluated at the point $q\cdot\exp(t\xi)$. Therefore $\gamma_q$ is the integral curve of $K_\xi$ through $q$; equivalently, the flow of $K_\xi$ is $\Phi_t=R_{\exp(t\xi)}$.
>
> **A zero of $K_\xi$ is a fixed point of the flow.** Suppose now $K_\xi(p)=0$. Then $p$ is a zero of the vector field $K_\xi$, so the constant curve $\delta(t):=p$ satisfies $\delta(0)=p$ and $\delta'(t)=0=K_\xi(p)=K_\xi(\delta(t))$; that is, $\delta$ is an integral curve of $K_\xi$ through $p$. By the **uniqueness** clause of the [[Thm - Fundamental Theorem on Flows|fundamental theorem on flows]] — through each point there is exactly one maximal integral curve — the two integral curves of $K_\xi$ through $p$ coincide:
> $$p\cdot\exp(t\xi)=\gamma_p(t)=\delta(t)=p\qquad\text{for all }t\qquad\text{(uniqueness of integral curves).}$$
>
> **Apply freeness.** The identity $p\cdot\exp(t\xi)=p$ says that each element $\exp(t\xi)\in G$ fixes the point $p$. Because the $G$-action of a [[Def - Principal G-Bundle|principal bundle]] is **free** — the only group element fixing any given point is the identity — this forces
> $$\exp(t\xi)=e\qquad\text{for all }t\qquad\text{(freeness of the action).}$$
> Differentiating this constant identity at $t=0$ gives $\xi=\frac{d}{dt}\big|_{0}\exp(t\xi)=\frac{d}{dt}\big|_{0}e=0$. Hence $\ker K_p=\{0\}$: the map $K_p$ is injective.
>
> Consequently $\dim\operatorname{im}K_p=\dim\mathfrak{g}=\dim G$ (the rank of an injective linear map equals the dimension of its domain, and $\dim\mathfrak{g}=\dim T_eG=\dim G$).

**Step 3: The vertical subspace has dimension $\dim G$.**

We compute $\dim V_p=\dim P-\dim M=\dim G$ using only that $\pi$ is a submersion with fibre $G$.

> [!note]- Derivation
> **$\pi$ is a submersion.** In a [[Def - Principal G-Bundle|principal $G$-bundle]] the projection $\pi\colon P\to M$ is a surjective submersion: locally there is a $G$-equivariant trivialisation $\psi_U\colon\pi^{-1}(U)\to U\times G$ with $\operatorname{pr}_U\circ\psi_U=\pi$, and $\operatorname{pr}_U$ is a submersion, so $\pi$ is one too. Hence for every $p$ the linear map $d\pi_p\colon T_pP\to T_{\pi(p)}M$ is **surjective**, and its rank is $\operatorname{rank}d\pi_p=\dim M$.
>
> **Rank–nullity.** By the rank–nullity theorem applied to $d\pi_p$,
> $$\dim V_p=\dim\ker d\pi_p=\dim T_pP-\operatorname{rank}d\pi_p=\dim P-\dim M\qquad\text{(rank–nullity; }\dim T_pP=\dim P\text{).}$$
>
> **The fibre dimension.** The same local trivialisation $\psi_U\colon\pi^{-1}(U)\to U\times G$ is a diffeomorphism, so $\dim P=\dim(U\times G)=\dim M+\dim G$. Substituting,
> $$\dim V_p=\dim P-\dim M=(\dim M+\dim G)-\dim M=\dim G.$$

**Step 4: Assemble — set equality and canonical isomorphism.**

We combine Steps 1–3 to conclude $\operatorname{im}K_p=V_p$ and that $K_p$ is an isomorphism onto $V_p$.

> [!note]- Derivation
> By **Step 1**, $\operatorname{im}K_p\subseteq V_p$; by **Step 2**, $\dim\operatorname{im}K_p=\dim G$; by **Step 3**, $\dim V_p=\dim G$. A subspace $\operatorname{im}K_p$ of the finite-dimensional space $V_p$ whose dimension equals that of $V_p$ must be all of $V_p$: if $W\subseteq V$ with $\dim W=\dim V<\infty$ then $W=V$, since a basis of $W$ is a linearly independent set of $\dim V$ vectors in $V$, hence a basis of $V$. Therefore
> $$\{K_\xi(p):\xi\in\mathfrak{g}\}=\operatorname{im}K_p=V_p,$$
> which is the required set equality, part 1.
>
> For part 2, the linear map $K_p\colon\mathfrak{g}\to V_p$ is injective (Step 2) and surjective (just shown), hence a linear isomorphism. It is **canonical** in the strong sense that its definition $\xi\mapsto\frac{d}{dt}\big|_{0}p\cdot\exp(t\xi)$ uses only the group action and the point $p$: no local frame, trivialisation, or basis of $\mathfrak{g}$ was chosen. Therefore $V_p\cong\mathfrak{g}$ canonically, via $K_p^{-1}$.

> [!note]- Complete formal solution
> **Claim.** For a principal $G$-bundle $\pi\colon P\to M$ and $p\in P$, the map $K_p\colon\mathfrak{g}\to T_pP$, $K_p(\xi)=K_\xi(p)=\frac{d}{dt}\big|_{0}p\cdot\exp(t\xi)$, is a linear isomorphism onto $V_p=\ker d\pi_p$; in particular $V_p=\{K_\xi(p):\xi\in\mathfrak{g}\}$ and $V_p\cong\mathfrak{g}$ canonically.
>
> *Linearity and verticality.* Writing $\ell_p(g)=p\cdot g$ for the orbit map, $K_\xi(p)=d_e\ell_p(\xi)$ (chain rule, $d_0\exp=\operatorname{id}$), so $K_p=d_e\ell_p$ is linear. Since the action preserves fibres, $\pi(p\cdot\exp(t\xi))=\pi(p)$ is constant in $t$; differentiating gives $d\pi_p(K_\xi(p))=0$, so $\operatorname{im}K_p\subseteq V_p$.
>
> *Injectivity.* The curve $t\mapsto q\cdot\exp(t\xi)$ is the integral curve of $K_\xi$ through $q$, because its velocity is $K_\xi$ at each of its points (using $\exp((t+s)\xi)=\exp(t\xi)\exp(s\xi)$); thus the flow of $K_\xi$ is $R_{\exp(t\xi)}$. If $K_\xi(p)=0$, then $p$ is a zero of $K_\xi$, so the constant curve at $p$ is an integral curve through $p$; by uniqueness of integral curves ([[Thm - Fundamental Theorem on Flows|fundamental theorem on flows]]), $p\cdot\exp(t\xi)=p$ for all $t$. Freeness of the action forces $\exp(t\xi)=e$ for all $t$, whence $\xi=\frac{d}{dt}\big|_0\exp(t\xi)=0$. So $K_p$ is injective and $\dim\operatorname{im}K_p=\dim G$.
>
> *Dimension of $V_p$.* As $\pi$ is a submersion, $d\pi_p$ is surjective of rank $\dim M$; rank–nullity gives $\dim V_p=\dim P-\dim M$. A local trivialisation $\pi^{-1}(U)\cong U\times G$ gives $\dim P=\dim M+\dim G$, so $\dim V_p=\dim G$.
>
> *Conclusion.* $\operatorname{im}K_p\subseteq V_p$ with $\dim\operatorname{im}K_p=\dim G=\dim V_p$, so $\operatorname{im}K_p=V_p$. Being injective and surjective, $K_p\colon\mathfrak{g}\to V_p$ is a linear isomorphism, defined without any auxiliary choice; hence $V_p=\{K_\xi(p):\xi\in\mathfrak{g}\}$ and $V_p\cong\mathfrak{g}$ canonically. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> One is tempted to argue injectivity of $K_p$ *directly* from freeness: "$K_\xi(p)=K_\eta(p)$ gives $p\cdot\exp(t\xi)=p\cdot\exp(t\eta)$, so by freeness $\exp(t\xi)=\exp(t\eta)$, hence $\xi=\eta$." This is **not** valid: the equality of derivatives $K_\xi(p)=K_\eta(p)$ at $t=0$ does *not* imply the equality of the whole curves $p\cdot\exp(t\xi)=p\cdot\exp(t\eta)$ — two curves with the same initial velocity need not agree. The flow argument of Step 2 is exactly what is required to convert the infinitesimal equality $K_\xi(p)=0$ into the finite equality $p\cdot\exp(t\xi)=p$ *for all $t$*, at which point freeness may legitimately be applied. The extra ingredient that licenses the shortcut is the uniqueness of integral curves.

---

# Key Takeaways

**To identify a kernel with an image, produce one linear map, land it in the kernel, and count dimensions rather than chasing vectors.** The whole exercise is an instance of a recurring pattern: two subspaces of a tangent space are asserted equal, one described as a kernel ($V_p=\ker d\pi_p$) and the other as the image of a natural map ($\operatorname{im}K_p$). The efficient proof never constructs, for a given vertical vector, the Lie-algebra element mapping to it; instead it verifies the *soft* inclusion $\operatorname{im}K_p\subseteq V_p$ by differentiation, establishes injectivity of $K_p$, and then lets $\dim\operatorname{im}K_p=\dim V_p$ force equality. The trigger for reaching for this pattern is precisely a "kernel $=$ image" claim in finite dimensions where one inclusion is one line and injectivity is available; the diagnostic is that the reverse inclusion, attempted by hand, would require inverting the map, which the dimension count sidesteps. This same machine reappears wherever one shows a tangent space is spanned by generators of a group action — for isometry groups, for the vertical bundle of any fibre bundle with structure group, and for the tangent space to a homogeneous space $G/H$ at the identity coset, which is $\mathfrak{g}/\mathfrak{h}$ by the identical count.

**Freeness of an action is a finite statement about fixed points; to use it on infinitesimal data, first integrate the generator to its flow.** The load-bearing subtlety of the proof is that "$K_\xi(p)=0$" is an infinitesimal condition — a single tangent vector vanishes — while freeness speaks about group elements fixing points. These cannot be matched directly. The bridge is that a fundamental vector field is never an arbitrary field: it is the infinitesimal generator of the action, and its flow is the action of the one-parameter subgroup $t\mapsto\exp(t\xi)$. A zero of any vector field is an equilibrium of its flow, so a zero of $K_\xi$ at $p$ means $p$ is fixed by the *entire* subgroup $\exp(t\xi)$, and only now does freeness bite, giving $\exp(t\xi)=e$ and $\xi=0$. The general lesson for spaced practice: whenever a proof holds an infinitesimal hypothesis about a fundamental vector field and a finite hypothesis about the action (freeness, properness, the size of a stabiliser), the missing step that connects them is almost always "integrate the generator, use uniqueness of integral curves, then apply the finite hypothesis to the resulting curve."

**The isomorphism $V_p\cong\mathfrak{g}$ is canonical fibrewise but twists by $\operatorname{Ad}$ along the fibre, which is why the vertical bundle is $\operatorname{ad}P$, not $M\times\mathfrak{g}$.** The map $K_p$ needs no choices, so at each single point the identification $V_p\cong\mathfrak{g}$ is genuinely canonical. It is worth knowing exactly how it fails to be constant as $p$ moves within a fibre. Differentiating the equivariance $R_g(p\cdot\exp(t\xi))=(p\cdot g)\cdot\exp\big(t\operatorname{Ad}_{g^{-1}}\xi\big)$ — which itself follows from $g^{-1}\exp(t\xi)g=\exp(t\operatorname{Ad}_{g^{-1}}\xi)$ — gives $dR_g\big(K_\xi(p)\big)=K_{\operatorname{Ad}_{g^{-1}}\xi}(p\cdot g)$. So transporting a vertical vector from $p$ to $p\cdot g$ by the group action carries the label $\xi$ to $\operatorname{Ad}_{g^{-1}}\xi$: the fibrewise trivialisation by $\mathfrak{g}$ is only $G$-equivariant up to the adjoint action, not $G$-invariant. This is the exact reason that the collection of vertical spaces assembles into the associated bundle $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak{g}$ rather than the trivial bundle $M\times\mathfrak{g}$, and it is the mechanism behind every later statement in which curvature, gauge potentials, or infinitesimal gauge transformations are described as $\operatorname{ad}P$-valued objects on the base. The companion exercise **[[Ex - The Adjoint Bundle of an Abelian Principal Bundle is Trivial]]** is precisely the degenerate case in which the $\operatorname{Ad}$-twist vanishes, so that $\operatorname{ad}P$ collapses back to $M\times\mathfrak{g}$.
