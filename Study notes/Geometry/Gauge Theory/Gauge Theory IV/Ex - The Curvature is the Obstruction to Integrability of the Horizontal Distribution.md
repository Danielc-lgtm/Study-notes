---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Curvature of a Principal Connection"
  - "Def - Horizontal Subspace and Horizontal Lift"
  - "Def - Connection on a Principal Bundle"
  - "Thm - The Frobenius Theorem"
  - "Def - Involutive Distribution"
  - "Def - Distribution on a Manifold"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\pi\colon P\to M$ be a principal $G$-bundle carrying a connection form $\omega\in\Omega^1(P;\mathfrak{g})$, and let
$$H_p:=\ker\omega_p\subset T_pP,\qquad H:=\bigsqcup_{p\in P}H_p$$
be the associated **horizontal distribution**. Recall that $H$ is a smooth distribution of constant rank $\dim M$ on the total space $P$, with $T_pP=H_p\oplus V_p$ where $V_p=\ker d\pi_p$ is the vertical space, and that a vector field $Z$ on $P$ is a section of $H$ (is *horizontal*) if and only if $\omega(Z)=0$. Let $\Omega\in\Omega^2(P;\mathfrak{g})$ be the curvature form, $\Omega(X,Y):=d\omega(\pi_H X,\pi_H Y)$, where $\pi_H\colon T_pP\to H_p$ is the horizontal projection along $V_p$.

**Prove the following three-way equivalence:**
$$\boxed{\ \Omega=0\quad\Longleftrightarrow\quad H\text{ is involutive}\quad\Longleftrightarrow\quad H\text{ is integrable.}\ }$$

The second equivalence is the Frobenius theorem, applied to the distribution $H$; the burden of the exercise is the first equivalence, and its engine is the identity
$$\Omega(\tilde X,\tilde Y)=-\,\omega([\tilde X,\tilde Y])\qquad\text{for horizontal vector fields }\tilde X,\tilde Y,$$
which you should establish first, from the definition of $\Omega$ and the invariant formula for the exterior derivative. In words: *the curvature measures the failure of the bracket of two horizontal fields to be horizontal.* A connection whose curvature vanishes therefore has an integrable horizontal distribution; its integral manifolds are the horizontal leaves through which parallel transport is locally path-independent — the geometry of flat connections, the subject of Gauge Theory V.

**Recall.** The curvature form and the horizontal splitting are defined intrinsically as follows.

![[Def - Curvature of a Principal Connection#The Definition]]

![[Def - Horizontal Subspace and Horizontal Lift#The Definition]]

The underlying connection form is characterised by:

![[Def - Connection on a Principal Bundle#The Definition]]

A **distribution** and what it means for one to be **involutive** or **integrable** are recalled from differential geometry.

![[Def - Distribution on a Manifold#The Definition]]

![[Def - Involutive Distribution#The Definition]]

Concretely, a smooth distribution $D$ on a manifold is **involutive** if the space $\Gamma(D)$ of its smooth local sections is closed under the Lie bracket of vector fields — $[X,Y]\in\Gamma(D)$ whenever $X,Y\in\Gamma(D)$ — and **integrable** if every point lies on an integral manifold of $D$, that is, an immersed submanifold $N$ with $T_qN=D_q$ for all $q\in N$. The equivalence of these two conditions is the content of the Frobenius theorem.

![[Thm - The Frobenius Theorem#Statement]]

Finally, we shall use the **invariant formula for the exterior derivative of a one-form**, restated here at the point of use and proved on its own page. For a (real- or vector-valued) one-form $\eta$ and vector fields $X,Y$,
$$d\eta(X,Y)=X\bigl(\eta(Y)\bigr)-Y\bigl(\eta(X)\bigr)-\eta([X,Y]),$$
where $X(\eta(Y))$ is the derivative of the function $\eta(Y)$ along $X$; see [[Thm - Coordinate Expression for the Exterior Derivative]]. For the $\mathfrak{g}$-valued form $\omega$ the identity holds componentwise in any basis of $\mathfrak{g}$, hence as an equation of $\mathfrak{g}$-valued functions.

---

# Convergent Strategy

**Problem class.** This is a *prove-an-equivalence-chain* problem that unifies a differential-geometric object (curvature) with a topological-integrability condition (Frobenius). Its shape is standard: one of the two equivalences is a named theorem invoked wholesale (Frobenius: involutive $\Leftrightarrow$ integrable), and the real work is a single bridge identity that translates the analytic object into the language in which the named theorem speaks. Here the bridge is $\Omega(\tilde X,\tilde Y)=-\omega([\tilde X,\tilde Y])$: it converts "$\Omega=0$" into "brackets of horizontal fields are horizontal", which is verbatim the hypothesis of Frobenius.

**Assumption pattern.** Two structural facts about the horizontal distribution do all the load-bearing. First, *horizontality is detected by $\omega$*: a field $Z$ lies in $\Gamma(H)$ exactly when $\omega(Z)=0$, because $H_p=\ker\omega_p$ by definition. Second, *the curvature is a horizontal (tensorial) two-form*: $\Omega(X,Y)=d\omega(\pi_H X,\pi_H Y)$ depends only on the horizontal parts of its arguments, so $\Omega$ vanishes identically if and only if it vanishes on all pairs of horizontal fields. The recognisable trigger is the appearance of $\ker\omega$: whenever a distribution is presented as the kernel of a one-form, "the section is in the distribution" becomes "the one-form annihilates it", and the exterior derivative of that one-form measures involutivity.

**Theorem routing.** The route is: (i) establish the bridge identity $\Omega(\tilde X,\tilde Y)=-\omega([\tilde X,\tilde Y])$ from the definition of $\Omega$, horizontality ($\pi_H\tilde X=\tilde X$, $\omega(\tilde X)=0$), and the invariant formula for $d\omega$ ([[Thm - Coordinate Expression for the Exterior Derivative]]); (ii) show $\Omega=0$ iff $\Omega$ vanishes on all horizontal pairs, using that $\Omega$ is horizontal and that every horizontal tangent vector is the value of a horizontal vector field ([[Def - Horizontal Subspace and Horizontal Lift|horizontal lifts]]); (iii) chain the identity: $\Omega=0$ iff $\omega([\tilde X,\tilde Y])=0$ for all horizontal $\tilde X,\tilde Y$ iff $[\tilde X,\tilde Y]$ is horizontal for all such iff $H$ is involutive; (iv) invoke [[Thm - The Frobenius Theorem]] for involutive iff integrable.

**Key decision point.** The one non-obvious move is step (ii): passing from "$\Omega$ kills every horizontal pair" to "$\Omega=0$ as a form." This is *not* automatic for a general two-form, and it is exactly where the tensoriality of curvature — its dependence on arguments only through $\pi_H$ — is used. A reader who omits this step has proved only that $\Omega$ restricted to $H$ vanishes, which without horizontality would be weaker than $\Omega=0$. The second, subtler decision is to check involutivity on *all* horizontal fields rather than a chosen frame: the bridge identity holds for every pair of horizontal fields, so no frame is needed and the argument stays coordinate-free.

---

# Legal Operations Used

This solution deploys the following legal operations. Because the chapter topic page has not yet been assembled, the operations are named descriptively; the orchestrator will reconcile the numbering with the topic page's Legal Operations section.

1. **Read horizontality off the connection form.** Use $H_p=\ker\omega_p$ to translate "$Z\in\Gamma(H)$" into "$\omega(Z)=0$", and back.

2. **Reduce the horizontal projection to the identity on horizontal inputs.** For a horizontal field $\tilde X$, $\pi_H\tilde X=\tilde X$, so $\Omega(\tilde X,\tilde Y)=d\omega(\tilde X,\tilde Y)$.

3. **Expand $d\omega$ by the invariant formula.** Apply $d\omega(X,Y)=X(\omega(Y))-Y(\omega(X))-\omega([X,Y])$ (from [[Thm - Coordinate Expression for the Exterior Derivative]]) and simplify using $\omega(\tilde X)=\omega(\tilde Y)=0$.

4. **Use tensoriality (horizontality) of the curvature.** Since $\Omega(X,Y)=d\omega(\pi_H X,\pi_H Y)$, $\Omega$ depends on its arguments only through $\pi_H$; in particular $\Omega$ vanishes when either argument is vertical, and $\Omega(X,Y)=\Omega(\pi_H X,\pi_H Y)$ always.

5. **Realise a horizontal vector as the value of a horizontal field.** Given $w\in H_p$, take the [[Def - Horizontal Subspace and Horizontal Lift|horizontal lift]] $\tilde X$ of a local extension of $d\pi_p(w)$; then $\tilde X_p=w$.

6. **Apply the definition of involutivity.** $H$ involutive means $\Gamma(H)$ is closed under the Lie bracket, i.e. $[\tilde X,\tilde Y]\in\Gamma(H)$ for all horizontal $\tilde X,\tilde Y$.

7. **Invoke the Frobenius theorem.** For the constant-rank smooth distribution $H$, involutivity is equivalent to integrability by [[Thm - The Frobenius Theorem]].

---

# Hints

> [!note]- Hint 1
> The distribution is $H=\ker\omega$. So "a vector field $Z$ is horizontal" and "$\omega(Z)=0$" are the *same statement*. Involutivity of $H$ asks that the bracket of two horizontal fields be horizontal — rewrite that condition using $\omega$.

> [!note]- Hint 2
> Compute $\omega([\tilde X,\tilde Y])$ for horizontal $\tilde X,\tilde Y$ using the invariant formula $d\omega(X,Y)=X(\omega(Y))-Y(\omega(X))-\omega([X,Y])$. Two of the three terms vanish because $\tilde X,\tilde Y$ are horizontal. What is left relates $\omega([\tilde X,\tilde Y])$ to $d\omega(\tilde X,\tilde Y)$, and on horizontal inputs $d\omega(\tilde X,\tilde Y)=\Omega(\tilde X,\tilde Y)$.

> [!note]- Hint 3
> You now have $\Omega(\tilde X,\tilde Y)=-\omega([\tilde X,\tilde Y])$. Read it both ways: $H$ involutive means the right side is always $0$, i.e. $\Omega$ vanishes on all horizontal pairs. To upgrade "vanishes on horizontal pairs" to "$\Omega=0$", remember that $\Omega(X,Y)=d\omega(\pi_H X,\pi_H Y)$ only sees the horizontal parts of $X,Y$ — so if $\Omega$ kills every horizontal pair, it kills every pair.

> [!note]- Hint 4
> For the upgrade in Hint 3 you must know that every horizontal *vector* $w\in H_p$ is $\tilde X_p$ for some horizontal *field* $\tilde X$. Build $\tilde X$ as the horizontal lift of any vector field on $M$ extending $d\pi_p(w)$. Then only the Frobenius theorem remains: $H$ is a smooth distribution of constant rank, so involutive $\Leftrightarrow$ integrable.

---

# Solution

The proof runs in three movements. First we establish the bridge identity $\Omega(\tilde X,\tilde Y)=-\omega([\tilde X,\tilde Y])$, which is a direct computation from the definition of curvature and the invariant formula for $d\omega$. Second we use it, together with the horizontality of $\Omega$, to prove the analytic equivalence $\Omega=0\Leftrightarrow H$ involutive. Third we invoke the Frobenius theorem for the topological equivalence $H$ involutive $\Leftrightarrow H$ integrable, and assemble the chain.

**Step 1: The bridge identity $\Omega(\tilde X,\tilde Y)=-\omega([\tilde X,\tilde Y])$ for horizontal fields.**

For horizontal vector fields $\tilde X,\tilde Y$ on $P$, the curvature evaluated on them equals minus the connection form of their bracket.

> [!note]- Derivation
> Let $\tilde X,\tilde Y\in\Gamma(H)$, so by definition of $H=\ker\omega$ we have $\omega(\tilde X)=0$ and $\omega(\tilde Y)=0$ (operation 1), and the horizontal projection fixes them, $\pi_H\tilde X=\tilde X$, $\pi_H\tilde Y=\tilde Y$.
>
> By the definition of the curvature form (operation 2),
> $$\Omega(\tilde X,\tilde Y)=d\omega(\pi_H\tilde X,\pi_H\tilde Y)=d\omega(\tilde X,\tilde Y)\qquad(\text{definition of }\Omega;\ \pi_H\tilde X=\tilde X,\ \pi_H\tilde Y=\tilde Y).$$
> Now apply the invariant formula for the exterior derivative of the one-form $\omega$ (operation 3; [[Thm - Coordinate Expression for the Exterior Derivative]], read componentwise in a basis of $\mathfrak{g}$):
> $$d\omega(\tilde X,\tilde Y)=\tilde X\bigl(\omega(\tilde Y)\bigr)-\tilde Y\bigl(\omega(\tilde X)\bigr)-\omega([\tilde X,\tilde Y])\qquad(\text{invariant formula for }d\omega).$$
> The functions $\omega(\tilde Y)$ and $\omega(\tilde X)$ are identically zero because $\tilde X,\tilde Y$ are horizontal, so their derivatives $\tilde X(\omega(\tilde Y))=\tilde X(0)=0$ and $\tilde Y(\omega(\tilde X))=\tilde Y(0)=0$ vanish. Hence
> $$\Omega(\tilde X,\tilde Y)=d\omega(\tilde X,\tilde Y)=-\omega([\tilde X,\tilde Y])\qquad(\text{the two derivative terms vanish since }\omega(\tilde X)=\omega(\tilde Y)=0).$$
> This is the bridge identity. Note that $[\tilde X,\tilde Y]$ need not be horizontal — the whole point is that $\omega$ measures its vertical part, which is $-\Omega(\tilde X,\tilde Y)$.

**Step 2: $\Omega$ vanishes identically if and only if it vanishes on all horizontal pairs.**

Because the curvature depends on its arguments only through the horizontal projection, checking it on horizontal fields checks it everywhere.

> [!note]- Derivation
> ($\Rightarrow$) If $\Omega=0$ as a two-form on $P$, then in particular $\Omega(\tilde X,\tilde Y)=0$ for all horizontal $\tilde X,\tilde Y$.
>
> ($\Leftarrow$) Suppose $\Omega(\tilde X,\tilde Y)=0$ for every pair of horizontal vector fields. Fix $p\in P$ and arbitrary $u,v\in T_pP$. By the definition of $\Omega$ (operation 4),
> $$\Omega_p(u,v)=d\omega_p(\pi_H u,\pi_H v)=\Omega_p(\pi_H u,\pi_H v),$$
> so $\Omega_p$ depends on $u,v$ only through their horizontal parts $\pi_H u,\pi_H v\in H_p$; in particular $\Omega_p$ vanishes whenever $u$ or $v$ is vertical. It therefore suffices to show $\Omega_p(w_1,w_2)=0$ for $w_1,w_2\in H_p$.
>
> Given $w\in H_p$, set $x:=d\pi_p(w)\in T_{\pi(p)}M$, choose a local vector field $X$ on $M$ near $\pi(p)$ with $X_{\pi(p)}=x$, and let $\tilde X$ be its horizontal lift — the unique horizontal vector field on $\pi^{-1}(U)$ that is $\pi$-related to $X$ (operation 5, [[Def - Horizontal Subspace and Horizontal Lift]]). Then $\tilde X_p\in H_p$ and $d\pi_p(\tilde X_p)=X_{\pi(p)}=x=d\pi_p(w)$; since $d\pi_p|_{H_p}\colon H_p\to T_{\pi(p)}M$ is an isomorphism, $\tilde X_p=w$. So every $w\in H_p$ is the value at $p$ of a horizontal field.
>
> Applying this to $w_1,w_2$, choose horizontal fields $\tilde X_1,\tilde X_2$ with $(\tilde X_1)_p=w_1$, $(\tilde X_2)_p=w_2$. By hypothesis $\Omega(\tilde X_1,\tilde X_2)\equiv 0$, so $\Omega_p(w_1,w_2)=\Omega(\tilde X_1,\tilde X_2)_p=0$. As $w_1,w_2\in H_p$ were arbitrary and $\Omega_p$ vanishes off $H_p\times H_p$, we conclude $\Omega_p=0$. As $p$ was arbitrary, $\Omega=0$.

**Step 3: $\Omega=0$ if and only if $H$ is involutive.**

Combining the bridge identity with Step 2 turns the vanishing of curvature into closure of horizontal fields under the bracket.

> [!note]- Derivation
> By the definition of involutivity (operation 6), $H$ is involutive precisely when $[\tilde X,\tilde Y]\in\Gamma(H)$ for all $\tilde X,\tilde Y\in\Gamma(H)$. Since $\Gamma(H)=\{Z:\omega(Z)=0\}$ (operation 1), the membership $[\tilde X,\tilde Y]\in\Gamma(H)$ is equivalent to $\omega([\tilde X,\tilde Y])=0$. Therefore
> $$H\text{ involutive}\iff \omega([\tilde X,\tilde Y])=0\ \text{ for all horizontal }\tilde X,\tilde Y.$$
> By the bridge identity of Step 1, $\omega([\tilde X,\tilde Y])=-\Omega(\tilde X,\tilde Y)$, so the right-hand condition is exactly $\Omega(\tilde X,\tilde Y)=0$ for all horizontal $\tilde X,\tilde Y$. By Step 2, this holds if and only if $\Omega=0$. Chaining the two equivalences,
> $$H\text{ involutive}\iff \Omega(\tilde X,\tilde Y)=0\ \text{for all horizontal }\tilde X,\tilde Y\iff \Omega=0.$$

**Step 4: $H$ is involutive if and only if $H$ is integrable (Frobenius).**

The horizontal distribution is smooth and of constant rank, so the Frobenius theorem applies directly.

> [!note]- Derivation
> The horizontal distribution $H\subset TP$ is smooth and of constant rank $\dim M$: at every $p$, $H_p=\ker\omega_p$ and $T_pP=H_p\oplus V_p$ with $\dim V_p=\dim G$ constant, so $\dim H_p=\dim P-\dim G=\dim M$ is constant, and smoothness of $\omega$ makes $p\mapsto H_p$ a smooth distribution ([[Def - Horizontal Subspace and Horizontal Lift]]). The Frobenius theorem (operation 7, [[Thm - The Frobenius Theorem]]) states that for a smooth constant-rank distribution the conditions *involutive* and *integrable* (indeed *completely integrable*, i.e. flat charts through every point) are equivalent. Applying it to $H$:
> $$H\text{ involutive}\iff H\text{ integrable}.$$

> [!note]- Complete formal solution
> **Claim.** For a connection $\omega$ on a principal $G$-bundle $\pi\colon P\to M$ with horizontal distribution $H=\ker\omega$ and curvature $\Omega(X,Y)=d\omega(\pi_H X,\pi_H Y)$, the conditions $\Omega=0$, "$H$ involutive", and "$H$ integrable" are equivalent.
>
> *Bridge identity.* Let $\tilde X,\tilde Y$ be horizontal vector fields, so $\omega(\tilde X)=\omega(\tilde Y)=0$ and $\pi_H\tilde X=\tilde X$, $\pi_H\tilde Y=\tilde Y$. Then
> $$\Omega(\tilde X,\tilde Y)=d\omega(\tilde X,\tilde Y)=\tilde X(\omega(\tilde Y))-\tilde Y(\omega(\tilde X))-\omega([\tilde X,\tilde Y])=-\omega([\tilde X,\tilde Y]),$$
> using the definition of $\Omega$, the invariant formula $d\omega(X,Y)=X(\omega(Y))-Y(\omega(X))-\omega([X,Y])$ ([[Thm - Coordinate Expression for the Exterior Derivative]], componentwise in $\mathfrak{g}$), and $\omega(\tilde X)=\omega(\tilde Y)=0$.
>
> *$\Omega=0\Leftrightarrow H$ involutive.* Since $H=\ker\omega$, a field $Z$ is horizontal iff $\omega(Z)=0$; hence $H$ is involutive iff $\omega([\tilde X,\tilde Y])=0$ for all horizontal $\tilde X,\tilde Y$, iff (bridge identity) $\Omega(\tilde X,\tilde Y)=0$ for all horizontal $\tilde X,\tilde Y$. This last condition is equivalent to $\Omega=0$: the forward direction is trivial, and conversely, because $\Omega(X,Y)=d\omega(\pi_H X,\pi_H Y)$ depends on $X,Y$ only through $\pi_H$, we have $\Omega_p(u,v)=\Omega_p(\pi_H u,\pi_H v)$ for all $u,v\in T_pP$; every $w\in H_p$ equals $\tilde X_p$ for the horizontal lift $\tilde X$ of an extension of $d\pi_p(w)$ (as $d\pi_p|_{H_p}$ is an isomorphism), so $\Omega_p$ vanishes on $H_p\times H_p$ and hence on all of $T_pP\times T_pP$, giving $\Omega=0$.
>
> *$H$ involutive $\Leftrightarrow H$ integrable.* The distribution $H$ is smooth of constant rank $\dim M$; by the Frobenius theorem ([[Thm - The Frobenius Theorem]]), involutivity is equivalent to integrability.
>
> Chaining, $\Omega=0\iff H\text{ involutive}\iff H\text{ integrable}$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: "$\Omega$ vanishes on $H$, so $\Omega=0$ needs nothing more"
> After Step 1 one is tempted to declare victory the moment $\Omega(\tilde X,\tilde Y)=0$ on horizontal pairs, treating this as literally "$\Omega=0$". For a *general* two-form on $P$ this inference is false: a two-form can annihilate every pair drawn from a subspace and still be nonzero on mixed or vertical pairs. The inference is legitimate here only because $\Omega$ is a *horizontal* (tensorial) form — $\Omega(X,Y)=d\omega(\pi_H X,\pi_H Y)$ vanishes whenever an argument is vertical and equals $\Omega(\pi_H X,\pi_H Y)$ in general. The extra condition that rescues the shortcut is precisely tensoriality; Step 2 is where it is invoked, and skipping it leaves the first equivalence unproved.

> [!note]- Interpretation: this is why a flat connection foliates the total space
> A connection with $\Omega=0$ is called *flat*. The equivalence just proved says its horizontal distribution $H$ is integrable, so by the Frobenius theorem $P$ is foliated by horizontal integral manifolds — leaves $L$ with $T_qL=H_q$ at every $q\in L$. Along such a leaf every tangent vector is horizontal, so a curve staying in a leaf and projecting to a path $c$ in $M$ is a horizontal lift of $c$; consequently parallel transport of a flat connection depends only on the homotopy class of the base path, and around a contractible loop it is trivial. The nonvanishing of $\Omega$ is exactly the local obstruction to this picture: it is the vertical part $-\omega([\tilde X,\tilde Y])$ of the bracket of horizontal lifts, the amount by which two infinitesimal horizontal displacements fail to commute. This is developed into holonomy and the monodromy representation of $\pi_1(M)$ in Gauge Theory V.

---

# Key Takeaways

**When a distribution is presented as the kernel of a one-form, its involutivity is read off the exterior derivative of that form — and here that exterior derivative is the curvature.** The reusable principle is the chain "$H=\ker\omega$, so $Z$ horizontal $\Leftrightarrow\omega(Z)=0$, and $\omega([\tilde X,\tilde Y])=-d\omega(\tilde X,\tilde Y)$ on horizontal inputs by the invariant formula." Any time a geometric structure is a kernel of a form (a contact structure $\ker\alpha$, the horizontal bundle of a connection, the annihilator of a codimension-one foliation), the integrability question is settled by evaluating $d$ of that form on sections of the kernel; the two derivative terms in $d\eta(X,Y)=X(\eta(Y))-Y(\eta(X))-\eta([X,Y])$ die precisely because the inputs annihilate the form, leaving $\eta([X,Y])$ alone. Recognising this lets one convert an integrability problem into a computation of one exterior derivative, which is almost always easier. The trigger condition is the phrase "kernel of a one-form"; the reaction is "differentiate the form and restrict to the kernel."

**Curvature is a tensorial, horizontal two-form, and that tensoriality is what lets a check on horizontal fields become a global statement.** The subtle step of the proof — upgrading "$\Omega$ vanishes on horizontal pairs" to "$\Omega=0$" — succeeds only because $\Omega(X,Y)=d\omega(\pi_H X,\pi_H Y)$ factors through the horizontal projection, so $\Omega$ carries no information about vertical directions. The transferable diagnostic: before concluding that a form vanishes from its vanishing on a sub-bundle, verify that the form is *basic* or *horizontal* with respect to that sub-bundle; if it is, the sub-bundle carries all of its information and the upgrade is valid, and if it is not, the conclusion is simply false. In gauge theory this tensoriality is what allows curvature — defined upstairs on $P$ — to descend to a genuine two-form $F_\omega$ on the base $M$ with values in the adjoint bundle $\operatorname{ad}P$; the same horizontality that powers Step 2 is what makes the descent possible.

**Curvature is the local obstruction to flatness, and "flat" means "the horizontal distribution integrates."** The single most reusable statement of this exercise is that $\Omega$ is the vertical component of the bracket of horizontal lifts: $\Omega(\tilde X,\tilde Y)=-\omega([\tilde X,\tilde Y])$. This is the principal-bundle avatar of a pattern that recurs throughout geometry — curvature as the failure of infinitesimal displacements to commute, whether it is the Riemann tensor measuring the failure of second covariant derivatives to commute, the Frobenius obstruction measuring the failure of a distribution to close under brackets, or the field strength $F_{\mu\nu}$ of the companion exercise measuring the non-commutativity of covariant derivatives in coordinates. The lesson for spaced practice is that "flat connection" is not a metaphor: $\Omega=0$ is *literally* the Frobenius integrability of $H$, and the leaves are the horizontal foliation along which parallel transport becomes path-independent. Companion exercises are [[Ex - The Horizontal Distribution of the Hopf Connection is Not Integrable]], which exhibits a concrete non-flat connection whose horizontal fields have $[v_2,v_3]=-2v_1$ vertical (so $\Omega\ne0$), and [[Ex - Bianchi Identity for an SU(2) Potential in Coordinates]], which computes with the descended curvature $F$ that this exercise's tensoriality produces.
