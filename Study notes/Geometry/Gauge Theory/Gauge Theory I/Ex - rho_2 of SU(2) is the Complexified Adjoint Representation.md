---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Complex Representations of U(1) and SU(2)"
  - "Def - Constructions on Representations"
  - "Def - Representation of a Lie Group"
  - "Thm - Ad is a Smooth Representation and its Differential is ad"
  - "Thm - The Exponential Map of a Compact Connected Lie Group is Surjective"
  - "Thm - Naturality of the Exponential Map"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $SU(2)$ act on $\mathbb{C}^{2}$ by the standard representation $\varrho_{1}=\varrho_{\mathrm{st}}$, and let $\varrho_{2}=\odot^{2}\varrho_{1}$ be the induced representation on the symmetric square $\odot^{2}\mathbb{C}^{2}$, a three-dimensional complex vector space. Let $\operatorname{Ad}\colon SU(2)\to GL(\mathfrak{su}(2))$ be the adjoint representation on the three-dimensional real Lie algebra $\mathfrak{su}(2)$, and let $(\operatorname{Ad})_{\mathbb{C}}$ denote its complexification, acting on $\mathfrak{su}(2)_{\mathbb{C}}=\mathfrak{su}(2)\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}^{3}$.

Bär (Example 1.3.15) asserts that the matrix
$$T=\begin{pmatrix}-i&1&0\\1&-i&0\\0&0&1\end{pmatrix},\qquad T^{-1}=\begin{pmatrix}\tfrac{i}{2}&\tfrac12&0\\[2pt]\tfrac12&\tfrac{i}{2}&0\\[2pt]0&0&1\end{pmatrix},$$
written in the basis $e_{1}\odot e_{1},\,e_{2}\odot e_{2},\,e_{2}\odot e_{1}$ of $\odot^{2}\mathbb{C}^{2}$ (domain: the basis $-i\sigma_{1},-i\sigma_{2},-i\sigma_{3}$ of $\mathfrak{su}(2)$), satisfies
$$T\cdot\operatorname{Ad}_{g}\cdot T^{-1}=\varrho_{2}(g)\qquad\text{for all }g\in SU(2),\tag{$\ast$}$$
and hence exhibits $\varrho_{2}\cong(\operatorname{Ad})_{\mathbb{C}}$. Bär verifies $(\ast)$ only for diagonal $g=\operatorname{diag}(e^{i\varphi},e^{-i\varphi})$ and writes "it can be checked" that it holds for all $g$.

**Your task.** Carry out the full check, two ways.

1. **The Lie-algebra route.** Reduce the all-of-$SU(2)$ claim $(\ast)$ to a claim on the Lie algebra $\mathfrak{su}(2)$, using that $SU(2)$ is connected and $\exp$ is surjective. Then test the reduced claim on a basis of $\mathfrak{su}(2)$. You will discover that **Bär's printed $T$ satisfies $(\ast)$ only on the diagonal subgroup and fails off it**; diagnose exactly why, and produce the corrected intertwiner $T'$ for which $(\ast)$ genuinely holds on all of $SU(2)$.

2. **The classification route.** Independently, prove $\varrho_{2}\cong(\operatorname{Ad})_{\mathbb{C}}$ without computing any intertwiner, by showing that $(\operatorname{Ad})_{\mathbb{C}}$ is a *three-dimensional irreducible* complex representation of $SU(2)$ and invoking the classification: the unique such representation is $\varrho_{2}$. This is the content of Bär's Remark 1.3.4 ("since $\operatorname{Ad}_{SU(2)}$ is real three-dimensional, $\varrho_{2}$ is the only candidate").

> [!warning] Convention (Bär's Pauli labelling)
> Throughout this page we work with **Bär's** labelling of the Pauli matrices, which is the physics-standard one with $\sigma_{1}$ and $\sigma_{2}$ interchanged:
> $$\sigma_{1}=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad\sigma_{2}=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad\sigma_{3}=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$
> We set $b_{a}:=-i\sigma_{a}$ for $a=1,2,3$; these are anti-Hermitian and traceless, so they form a real basis of $\mathfrak{su}(2)=\{X\in\mathfrak{gl}(2;\mathbb{C}):X^{*}=-X,\ \operatorname{tr}X=0\}$. We adopt this labelling *only* so that Bär's printed matrices $\operatorname{Ad}_{g}$ (Example 1.3.2) and $T$ appear verbatim and can be checked as printed. The sibling page [[Ex - su(2) in the Basis of Anti-Hermitian Pauli Matrices]] uses the physics-standard labelling (in which the structure constants read $[-i\sigma_{a},-i\sigma_{b}]=2\varepsilon_{abc}(-i\sigma_{c})$); passing to Bär's labelling swaps $\sigma_{1}\leftrightarrow\sigma_{2}$ and therefore flips the sign of every structure constant, giving $[b_{a},b_{b}]=-2\varepsilon_{abc}\,b_{c}$ here. All brackets and matrices below are recomputed from scratch in Bär's labelling, so the page is internally self-contained and does not depend on either sibling page's sign.

**Recall.**

The objects in play are the standard and symmetric-power representations of $SU(2)$, the adjoint representation and its differential, the complexification of a real representation, equivalence of representations, and the classification of complex representations of $SU(2)$.

![[Def - Constructions on Representations#The Definition]]

We use three constructions from [[Def - Constructions on Representations|the constructions page]]. The **symmetric square** $\odot^{2}\varrho_{1}$ acts by $(\odot^{2}\varrho_{1})(g)(u\odot v)=(gu)\odot(gv)$; its differential is $(\odot^{2}\varrho_{1})_{*}(X)(u\odot v)=(Xu)\odot v+u\odot(Xv)$, obtained by differentiating $t\mapsto(e^{tX}u)\odot(e^{tX}v)$ at $t=0$ with the product rule. The **complexification** of the real representation $\operatorname{Ad}$ is $(\operatorname{Ad})_{\mathbb{C}}=\operatorname{Ad}\otimes\operatorname{id}_{\mathbb{C}}$ on $\mathfrak{su}(2)_{\mathbb{C}}$; in the real basis $b_{1},b_{2},b_{3}$, regarded now as a complex basis of $\mathbb{C}^{3}$, the matrix of $(\operatorname{Ad})_{\mathbb{C},g}$ is the *same* real matrix as $\operatorname{Ad}_{g}$, and its differential is $(\operatorname{ad})_{\mathbb{C}}$ with the same matrices as $\operatorname{ad}$.

![[Def - Representation of a Lie Group#The Definition]]

Two representations $\varrho\colon G\to\operatorname{Aut}(V)$ and $\tilde\varrho\colon G\to\operatorname{Aut}(\tilde V)$ are **equivalent** if there is a linear isomorphism $T\colon V\to\tilde V$ with $T\varrho(g)=\tilde\varrho(g)T$ for all $g$; equation $(\ast)$ is exactly this condition, with $T$ mapping the $\operatorname{Ad}$-space to the $\varrho_{2}$-space.

![[Thm - Ad is a Smooth Representation and its Differential is ad#Statement]]

We use that $\operatorname{Ad}_{g}X=gXg^{-1}$ for the matrix group $SU(2)$, that $\operatorname{ad}_{X}Y=[X,Y]$, and that $d_{e}\operatorname{Ad}=\operatorname{ad}$, whence $\operatorname{Ad}_{\exp X}=\exp(\operatorname{ad}_{X})$ (naturality of $\exp$). The diagonal computation of $\operatorname{Ad}_{g}$ for $g=\operatorname{diag}(e^{i\varphi},e^{-i\varphi})$ is drilled in [[Ex - The Adjoint Representation of SU(2) in the Pauli Basis]].

![[Thm - Complex Representations of U(1) and SU(2)#Statement]]

We invoke part (B): each $\varrho_{k}=\odot^{k}\varrho_{1}$ is an irreducible complex representation of $SU(2)$ of dimension $k+1$, the $\varrho_{k}$ are pairwise inequivalent, and *every* complex representation of $SU(2)$ is equivalent to a direct sum of $\varrho_{k}$'s. In particular the only irreducible complex representation of $SU(2)$ of dimension three is $\varrho_{2}$. We also invoke the theorem's **Lemma 5** (the Lie-algebra passage: for a connected Lie group, a subspace is $\varrho(G)$-invariant if and only if it is $\varrho_{*}(\mathfrak{g})$-invariant), of which the intertwiner-level statement used in Route 1 is the exact analogue, re-proved below.

We also use that $SU(2)$ is **compact and connected** (it is diffeomorphic to $S^{3}$, [[Ex - SU(2) is Diffeomorphic to S^3]]), so by [[Thm - The Exponential Map of a Compact Connected Lie Group is Surjective|the compact-connected surjectivity theorem]] the exponential $\exp\colon\mathfrak{su}(2)\to SU(2)$ is onto, and by [[Thm - Naturality of the Exponential Map|naturality of the exponential]] every representation satisfies $\varrho(\exp X)=\exp(\varrho_{*}X)$.

---

# Convergent Strategy

**Problem class.** This is a *verify-an-equivalence* problem with a twist: the source hands us a candidate intertwiner and asserts it works, and the honest task is to *check*, not to trust. The productive attitude is that "$T\operatorname{Ad}_{g}T^{-1}=\varrho_{2}(g)$ for all $g$" is a claim with a definite truth value for the *specific* $T$ printed, and the way to settle it cheaply is to move from the group (infinitely many $g$) to the Lie algebra (a three-dimensional check on a basis).

**Assumption pattern.** The structural fact that makes the reduction legal is that $SU(2)$ is *connected with surjective exponential*. This converts a statement about all of a curved three-manifold's worth of group elements into a statement about the flat tangent space $\mathfrak{su}(2)$ at the identity, because every $g$ is $\exp X$ and conjugation commutes with the matrix exponential. The recognisable trigger is "prove a linear relation for all $g$ in a connected matrix group": differentiate, check on a basis of the Lie algebra, integrate back.

**Theorem routing.** Route 1: reduce $(\ast)$ to $T\operatorname{ad}_{X}=\varrho_{2*}(X)T$ for $X$ in a basis $b_{1},b_{2},b_{3}$ of $\mathfrak{su}(2)$ (reduction lemma, proved in Step 0 from $\exp$-surjectivity); compute the three $3\times3$ matrices $\operatorname{ad}_{b_{a}}$ (from the brackets) and the three matrices $\varrho_{2*}(b_{a})$ (from the symmetric-square differential); substitute Bär's $T$; observe it works for $b_{3}$ but fails for $b_{1},b_{2}$; find the correct $T'$ by fixing the one relative scale Bär got wrong. Route 2: show $(\operatorname{Ad})_{\mathbb{C}}$ is irreducible (a nonzero invariant subspace is a complex ideal of the *simple* Lie algebra $\mathfrak{sl}(2;\mathbb{C})$), of dimension three, and quote the classification theorem's part (B) to identify it as $\varrho_{2}$; Schur's lemma then guarantees the intertwiner is unique up to a scalar, matching Route 1.

**Key decision point.** The single decisive move is *distrust the printed $T$ and test it directionally.* Because $\operatorname{Ad}_{g}$ for diagonal $g$ only exercises the $b_{3}$-direction (the maximal torus), Bär's diagonal check is blind to the two off-torus directions $b_{1},b_{2}$ — and it is exactly there that his $T$ fails. The diagnostic insight is that an intertwiner between two irreducibles is unique *up to a single overall scalar* (Schur), so the freedom in choosing $T$ is one complex number, not three; Bär's $T$ secretly used a *different* scalar on each of the two weight lines $b_{1}\pm ib_{2}$, which is invisible on the torus (where those lines are eigenlines and independent rescalings still diagonalise) but breaks the intertwining as soon as a group element mixes the two lines.

---

# Legal Operations Used

1. **Differentiate a group identity to a Lie-algebra identity, then integrate back** (operation "pass to the Lie algebra on a connected group", using [[Thm - The Exponential Map of a Compact Connected Lie Group is Surjective|surjectivity of the exponential]] and [[Thm - Naturality of the Exponential Map|naturality]]). *Trigger:* a linear relation asserted for all $g$ in a connected matrix group. *Pattern:* it holds for all $g$ if and only if its differential holds for all $X$ in the Lie algebra, i.e. on a basis.

2. **Compute $\operatorname{ad}$ from structure constants** (from [[Thm - Ad is a Smooth Representation and its Differential is ad|the adjoint page]], $\operatorname{ad}_{X}Y=[X,Y]$). *Trigger:* need the matrix of $\operatorname{ad}_{b_{a}}$. *Pattern:* its columns are the brackets $[b_{a},b_{1}],[b_{a},b_{2}],[b_{a},b_{3}]$ expressed in the basis.

3. **Differentiate a symmetric-power representation** (from [[Def - Constructions on Representations|the constructions page]]). *Trigger:* need $\varrho_{2*}(X)=(\odot^{2}\varrho_{1})_{*}(X)$. *Pattern:* apply the Leibniz rule $X\cdot(u\odot v)=(Xu)\odot v+u\odot(Xv)$.

4. **Schur's lemma for complex irreducibles** (a nonzero intertwiner of irreducibles is an isomorphism, and self-intertwiners are scalars; proved inline in Step 5). *Trigger:* comparing two irreducible representations, or counting intertwiners. *Pattern:* invariant kernel and image force isomorphism; a scalar eigenvalue argument forces uniqueness up to scale.

5. **Irreducibility via simplicity of the Lie algebra** (operation "an $\operatorname{Ad}$-invariant subspace is an ideal"). *Trigger:* deciding whether the adjoint representation is irreducible. *Pattern:* a complex invariant subspace is a complex ideal; if the complexified Lie algebra is simple, only $0$ and the whole space qualify.

---

# Hints

> [!note]- Hint 1
> To test $(\ast)$ for all $g$ without an infinite computation, differentiate it at $g=\exp(tX)$, $t=0$. Because $SU(2)$ is connected and $\exp$ is onto, the differentiated (Lie-algebra) version is *equivalent* to the original, not merely necessary. So it suffices to check a relation on the three basis vectors $b_{1},b_{2},b_{3}$.

> [!note]- Hint 2
> Compute the three matrices $\operatorname{ad}_{b_{a}}$ from the brackets $[b_{a},b_{b}]=-2\varepsilon_{abc}b_{c}$ (Bär's labelling), and the three matrices $\varrho_{2*}(b_{a})$ from $\varrho_{2*}(X)(u\odot v)=(Xu)\odot v+u\odot(Xv)$. Keep the ordered basis $f_{1}=e_{1}\odot e_{1},\ f_{2}=e_{2}\odot e_{2},\ f_{3}=e_{2}\odot e_{1}$ fixed.

> [!note]- Hint 3
> Test Bär's $T$ in the form $T\operatorname{ad}_{b_{a}}=\varrho_{2*}(b_{a})T$. The $b_{3}$ (diagonal / torus) case works. Now try $b_{1}$: the two sides disagree. Bär's diagonal verification never saw $b_{1}$ or $b_{2}$.

> [!note]- Hint 4
> The failure is a *relative scale*. Diagonalise $\operatorname{ad}_{b_{3}}$: its eigenvectors are $b_{3}$ (eigenvalue $0$) and $b_{1}\pm ib_{2}$ (eigenvalues $\pm 2i$). An intertwiner must send each of these eigenlines into the matching eigenline of $\varrho_{2*}(b_{3})=\operatorname{diag}(-2i,2i,0)$, but the *ratio* of the scales on the two lines $b_{1}\pm ib_{2}$ is fixed by Schur to a single value. Bär's $T$ uses the wrong ratio. Impose the $b_{1}$-relation to pin the ratio and read off the corrected $T'$.

> [!note]- Hint 5
> For Route 2: a complex subspace $W\subseteq\mathfrak{su}(2)_{\mathbb{C}}$ invariant under $(\operatorname{Ad})_{\mathbb{C}}$ is invariant under $(\operatorname{ad})_{\mathbb{C}}$ (differentiate), i.e. $[X,W]\subseteq W$ for all $X$ — a complex ideal of $\mathfrak{sl}(2;\mathbb{C})=\mathfrak{su}(2)_{\mathbb{C}}$. Show $\mathfrak{sl}(2;\mathbb{C})$ has no nonzero proper ideals, conclude irreducibility, and quote the classification.

---

# Solution

The plan is: prove the reduction lemma that turns $(\ast)$ into a Lie-algebra check (Step 0); assemble the two families of $3\times3$ matrices $\operatorname{ad}_{b_{a}}$ and $\varrho_{2*}(b_{a})$ (Steps 1–2); test Bär's $T$ and expose its off-torus failure (Step 3); repair it to the correct intertwiner $T'$ and verify $T'$ on all three generators (Step 4); then give the independent classification argument with the Schur input it needs (Step 5).

**Step 0: Reduction lemma. — $(\ast)$ holds for all $g\in SU(2)$ if and only if $T\operatorname{ad}_{b_{a}}=\varrho_{2*}(b_{a})T$ for $a=1,2,3$.**

> [!note]- Derivation
> Let $T\colon\mathbb{C}^{3}\to\odot^{2}\mathbb{C}^{2}$ be any fixed linear isomorphism (we identify $\mathfrak{su}(2)_{\mathbb{C}}\cong\mathbb{C}^{3}$ via $b_{1},b_{2},b_{3}$). We claim
> $$T(\operatorname{Ad})_{\mathbb{C},g}=\varrho_{2}(g)\,T\ \ \forall g\in SU(2)\quad\Longleftrightarrow\quad T(\operatorname{ad})_{\mathbb{C},X}=\varrho_{2*}(X)\,T\ \ \forall X\in\mathfrak{su}(2).$$
>
> **($\Rightarrow$).** Assume the group relation. Put $g=\exp(tX)$ for $X\in\mathfrak{su}(2)$ and differentiate at $t=0$. By naturality of the exponential, $\varrho_{2}(\exp(tX))=\exp(t\varrho_{2*}(X))$ and $(\operatorname{Ad})_{\mathbb{C},\exp(tX)}=\exp(t(\operatorname{ad})_{\mathbb{C},X})$ (using $d_{e}\operatorname{Ad}=\operatorname{ad}$ from [[Thm - Ad is a Smooth Representation and its Differential is ad|the adjoint page]]); differentiating $T\exp(t(\operatorname{ad})_{\mathbb{C},X})=\exp(t\varrho_{2*}(X))T$ at $t=0$ gives $T(\operatorname{ad})_{\mathbb{C},X}=\varrho_{2*}(X)T$.
>
> **($\Leftarrow$).** Assume the Lie-algebra relation for all $X\in\mathfrak{su}(2)$. Because $SU(2)$ is compact and connected, $\exp\colon\mathfrak{su}(2)\to SU(2)$ is surjective ([[Thm - The Exponential Map of a Compact Connected Lie Group is Surjective|surjectivity theorem]]): every $g\in SU(2)$ is $g=\exp X$ for some $X$. For matrices, conjugation commutes with the exponential series, $T\exp(M)T^{-1}=\exp(TMT^{-1})$ (apply $T(\,\cdot\,)T^{-1}$ term by term to $\sum_{k}M^{k}/k!$, using $T M^{k}T^{-1}=(TMT^{-1})^{k}$). Hence
> $$T\,(\operatorname{Ad})_{\mathbb{C},g}\,T^{-1}=T\exp\!\bigl((\operatorname{ad})_{\mathbb{C},X}\bigr)T^{-1}=\exp\!\bigl(T(\operatorname{ad})_{\mathbb{C},X}T^{-1}\bigr)=\exp\!\bigl(\varrho_{2*}(X)\bigr)=\varrho_{2}(\exp X)=\varrho_{2}(g),$$
> the middle equality by the Lie-algebra relation $T(\operatorname{ad})_{\mathbb{C},X}T^{-1}=\varrho_{2*}(X)$ and the last two by naturality. This is $(\ast)$.
>
> This is precisely the intertwiner form of **Lemma 5** of [[Thm - Complex Representations of U(1) and SU(2)|the classification theorem]]: on a connected group the group- and algebra-level relations coincide. Finally, since $(\operatorname{ad})_{\mathbb{C},X}$, $\varrho_{2*}(X)$, and $T$ are all complex-linear in $X$, the Lie-algebra relation holds for all $X\in\mathfrak{su}(2)$ (equivalently all $X\in\mathfrak{su}(2)_{\mathbb{C}}$) if and only if it holds for the three basis vectors $b_{1},b_{2},b_{3}$. This proves the lemma.

**Step 1: The matrices $\operatorname{ad}_{b_{a}}$. — assembles the adjoint action on $\mathfrak{su}(2)$ in Bär's basis.**

> [!note]- Derivation
> With Bär's labelling the basis matrices are
> $$b_{1}=-i\sigma_{1}=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad b_{2}=-i\sigma_{2}=\begin{pmatrix}0&-i\\-i&0\end{pmatrix},\quad b_{3}=-i\sigma_{3}=\begin{pmatrix}-i&0\\0&i\end{pmatrix}.$$
> Their commutators, computed directly (for instance $b_{1}b_{2}=\left(\begin{smallmatrix}i&0\\0&-i\end{smallmatrix}\right)$ and $b_{2}b_{1}=\left(\begin{smallmatrix}-i&0\\0&i\end{smallmatrix}\right)$, so $[b_{1},b_{2}]=\left(\begin{smallmatrix}2i&0\\0&-2i\end{smallmatrix}\right)=-2b_{3}$), are
> $$[b_{1},b_{2}]=-2b_{3},\qquad[b_{2},b_{3}]=-2b_{1},\qquad[b_{3},b_{1}]=-2b_{2}\qquad\text{(each verified from the explicit }2\times2\text{ products),}$$
> that is $[b_{a},b_{b}]=-2\varepsilon_{abc}b_{c}$, consistent with the Convention callout. Since $\operatorname{ad}_{b_{a}}(b_{c})=[b_{a},b_{c}]$, the columns of $\operatorname{ad}_{b_{a}}$ in the ordered basis $(b_{1},b_{2},b_{3})$ are the images $[b_{a},b_{1}],[b_{a},b_{2}],[b_{a},b_{3}]$:
> $$\operatorname{ad}_{b_{1}}=\begin{pmatrix}0&0&0\\0&0&2\\0&-2&0\end{pmatrix},\qquad\operatorname{ad}_{b_{2}}=\begin{pmatrix}0&0&-2\\0&0&0\\2&0&0\end{pmatrix},\qquad\operatorname{ad}_{b_{3}}=\begin{pmatrix}0&2&0\\-2&0&0\\0&0&0\end{pmatrix}.$$
> As a consistency check, $\operatorname{Ad}_{\exp(-\varphi b_{3})}=\exp(-\varphi\operatorname{ad}_{b_{3}})$ is the rotation by $+2\varphi$ in the $(b_{1},b_{2})$-plane, and $\exp(-\varphi b_{3})=\operatorname{diag}(e^{i\varphi},e^{-i\varphi})$, reproducing Bär's Example 1.3.2 matrix $\operatorname{Ad}_{\operatorname{diag}(e^{i\varphi},e^{-i\varphi})}=\left(\begin{smallmatrix}\cos2\varphi&-\sin2\varphi&0\\\sin2\varphi&\cos2\varphi&0\\0&0&1\end{smallmatrix}\right)$ of [[Ex - The Adjoint Representation of SU(2) in the Pauli Basis]].

**Step 2: The matrices $\varrho_{2*}(b_{a})$. — assembles the symmetric-square differential on $\odot^{2}\mathbb{C}^{2}$.**

> [!note]- Derivation
> Fix the ordered basis $f_{1}=e_{1}\odot e_{1}$, $f_{2}=e_{2}\odot e_{2}$, $f_{3}=e_{2}\odot e_{1}$ of $\odot^{2}\mathbb{C}^{2}$ (note $e_{1}\odot e_{2}=e_{2}\odot e_{1}=f_{3}$ by symmetry). By operation 3, $\varrho_{2*}(X)(u\odot v)=(Xu)\odot v+u\odot(Xv)$. Reading the action of each $b_{a}$ on $e_{1},e_{2}$ off the $2\times2$ matrices — $b_{1}e_{1}=e_{2},\ b_{1}e_{2}=-e_{1}$; $b_{2}e_{1}=-ie_{2},\ b_{2}e_{2}=-ie_{1}$; $b_{3}e_{1}=-ie_{1},\ b_{3}e_{2}=ie_{2}$ — we compute, for $b_{1}$,
> $$\varrho_{2*}(b_{1})f_{1}=(b_{1}e_{1})\odot e_{1}+e_{1}\odot(b_{1}e_{1})=e_{2}\odot e_{1}+e_{1}\odot e_{2}=2f_{3},$$
> $$\varrho_{2*}(b_{1})f_{2}=-e_{1}\odot e_{2}-e_{2}\odot e_{1}=-2f_{3},\qquad\varrho_{2*}(b_{1})f_{3}=(b_{1}e_{2})\odot e_{1}+e_{2}\odot(b_{1}e_{1})=-e_{1}\odot e_{1}+e_{2}\odot e_{2}=-f_{1}+f_{2}.$$
> For $b_{2}$, using $b_{2}e_{1}=-ie_{2}$ and $b_{2}e_{2}=-ie_{1}$,
> $$\varrho_{2*}(b_{2})f_{1}=(b_{2}e_{1})\odot e_{1}+e_{1}\odot(b_{2}e_{1})=(-ie_{2})\odot e_{1}+e_{1}\odot(-ie_{2})=-2i f_{3},$$
> $$\varrho_{2*}(b_{2})f_{2}=(b_{2}e_{2})\odot e_{2}+e_{2}\odot(b_{2}e_{2})=(-ie_{1})\odot e_{2}+e_{2}\odot(-ie_{1})=-2i f_{3},$$
> $$\varrho_{2*}(b_{2})f_{3}=(b_{2}e_{2})\odot e_{1}+e_{2}\odot(b_{2}e_{1})=(-ie_{1})\odot e_{1}+e_{2}\odot(-ie_{2})=-i f_{1}-i f_{2}.$$
> For $b_{3}$, using $b_{3}e_{1}=-ie_{1}$ and $b_{3}e_{2}=ie_{2}$,
> $$\varrho_{2*}(b_{3})f_{1}=(b_{3}e_{1})\odot e_{1}+e_{1}\odot(b_{3}e_{1})=(-ie_{1})\odot e_{1}+e_{1}\odot(-ie_{1})=-2i f_{1},$$
> $$\varrho_{2*}(b_{3})f_{2}=(b_{3}e_{2})\odot e_{2}+e_{2}\odot(b_{3}e_{2})=(ie_{2})\odot e_{2}+e_{2}\odot(ie_{2})=2i f_{2},$$
> $$\varrho_{2*}(b_{3})f_{3}=(b_{3}e_{2})\odot e_{1}+e_{2}\odot(b_{3}e_{1})=(ie_{2})\odot e_{1}+e_{2}\odot(-ie_{1})=i f_{3}-i f_{3}=0.$$
> Collecting columns,
> $$\varrho_{2*}(b_{1})=\begin{pmatrix}0&0&-1\\0&0&1\\2&-2&0\end{pmatrix},\qquad\varrho_{2*}(b_{2})=\begin{pmatrix}0&0&-i\\0&0&-i\\-2i&-2i&0\end{pmatrix},\qquad\varrho_{2*}(b_{3})=\begin{pmatrix}-2i&0&0\\0&2i&0\\0&0&0\end{pmatrix}.$$
> The diagonal $\varrho_{2*}(b_{3})=\operatorname{diag}(-2i,2i,0)$ matches the differential of Bär's diagonal $\varrho_{2}(\operatorname{diag}(e^{i\varphi},e^{-i\varphi}))=\operatorname{diag}(e^{2i\varphi},e^{-2i\varphi},1)$ at $\varphi=0$ (recall $\operatorname{diag}(e^{i\varphi},e^{-i\varphi})=\exp(-\varphi b_{3})$, so the derivative is $-(-2i,2i,0)\cdot(-1)$, i.e. $\operatorname{diag}(-2i,2i,0)$).

**Step 3: Bär's $T$ fails off the torus. — tests $(\ast)$ on the three generators and exposes the discrepancy.**

> [!note]- Derivation
> By Step 0, $(\ast)$ is equivalent to $T\operatorname{ad}_{b_{a}}=\varrho_{2*}(b_{a})T$ for $a=1,2,3$, with Bär's $T=\left(\begin{smallmatrix}-i&1&0\\1&-i&0\\0&0&1\end{smallmatrix}\right)$.
>
> **The torus direction $b_{3}$ works.** Computing both sides,
> $$T\operatorname{ad}_{b_{3}}=\begin{pmatrix}-i&1&0\\1&-i&0\\0&0&1\end{pmatrix}\begin{pmatrix}0&2&0\\-2&0&0\\0&0&0\end{pmatrix}=\begin{pmatrix}-2&-2i&0\\2i&2&0\\0&0&0\end{pmatrix},$$
> $$\varrho_{2*}(b_{3})T=\begin{pmatrix}-2i&0&0\\0&2i&0\\0&0&0\end{pmatrix}\begin{pmatrix}-i&1&0\\1&-i&0\\0&0&1\end{pmatrix}=\begin{pmatrix}-2&-2i&0\\2i&2&0\\0&0&0\end{pmatrix}.$$
> They agree, reproducing Bär's diagonal verification (differentiated).
>
> **The off-torus direction $b_{1}$ fails.** Now
> $$T\operatorname{ad}_{b_{1}}=\begin{pmatrix}-i&1&0\\1&-i&0\\0&0&1\end{pmatrix}\begin{pmatrix}0&0&0\\0&0&2\\0&-2&0\end{pmatrix}=\begin{pmatrix}0&0&2\\0&0&-2i\\0&-2&0\end{pmatrix},$$
> $$\varrho_{2*}(b_{1})T=\begin{pmatrix}0&0&-1\\0&0&1\\2&-2&0\end{pmatrix}\begin{pmatrix}-i&1&0\\1&-i&0\\0&0&1\end{pmatrix}=\begin{pmatrix}0&0&-1\\0&0&1\\-2i-2&2+2i&0\end{pmatrix}.$$
> These are **not equal**: for instance the $(1,3)$ entries are $2$ versus $-1$. Hence Bär's printed $T$ does **not** satisfy $(\ast)$; the relation "$T\operatorname{Ad}_{g}T^{-1}=\varrho_{2}(g)$ for all $g\in SU(2)$" is false for that particular $T$.
>
> **A concrete group counterexample.** To see the failure at the group level (not merely infinitesimally), take $g=\exp(\tfrac{\pi}{2}b_{1})=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)\in SU(2)$. From $ge_{1}=e_{2},\,ge_{2}=-e_{1}$ we get $\varrho_{2}(g)f_{1}=f_{2},\ \varrho_{2}(g)f_{2}=f_{1},\ \varrho_{2}(g)f_{3}=(-e_{1})\odot e_{2}=-f_{3}$, so $\varrho_{2}(g)=\left(\begin{smallmatrix}0&1&0\\1&0&0\\0&0&-1\end{smallmatrix}\right)$; and $\operatorname{Ad}_{g}b_{a}=gb_{a}g^{-1}$ gives $\operatorname{Ad}_{g}=\operatorname{diag}(1,-1,-1)$ (direct $2\times2$ conjugation, using $g^{-1}=-b_{1}$). Then
> $$T\operatorname{Ad}_{g}T^{-1}=\begin{pmatrix}0&-i&0\\i&0&0\\0&0&-1\end{pmatrix}\ \neq\ \begin{pmatrix}0&1&0\\1&0&0\\0&0&-1\end{pmatrix}=\varrho_{2}(g),$$
> the off-diagonal entries differing by a factor $\pm i$. This confirms the infinitesimal failure. ⚠️ **Bär's Example 1.3.15 is in error here:** the printed $T$ intertwines only over the maximal torus $\{\operatorname{diag}(e^{i\varphi},e^{-i\varphi})\}$, and his "it can be checked ... for all $g$" does not hold for that $T$. (The *conclusion* $\varrho_{2}\cong(\operatorname{Ad})_{\mathbb{C}}$ is nonetheless correct; only the exhibited intertwiner is wrong. Route 2 proves the equivalence independently, and Step 4 supplies a correct intertwiner.)

**Step 4: The corrected intertwiner $T'$. — pins the one wrong scale and verifies $(\ast)$ on all generators.**

> [!note]- Derivation
> **Diagnosis.** The operator $\operatorname{ad}_{b_{3}}$ is diagonalisable with eigenvalue $0$ on $b_{3}$ and eigenvalues $\pm2i$ on $b_{1}\pm ib_{2}$: indeed $\operatorname{ad}_{b_{3}}(b_{1}+ib_{2})=[b_{3},b_{1}]+i[b_{3},b_{2}]=-2b_{2}+i(2b_{1})=2i(b_{1}+ib_{2})$, so $b_{1}+ib_{2}$ has eigenvalue $+2i$, and likewise $b_{1}-ib_{2}$ has eigenvalue $-2i$. On the target side, $\varrho_{2*}(b_{3})=\operatorname{diag}(-2i,2i,0)$ has eigenvalue $+2i$ on $f_{2}$, $-2i$ on $f_{1}$, $0$ on $f_{3}$. An intertwiner $T'$ must carry each $\operatorname{ad}_{b_{3}}$-eigenline to the equal-eigenvalue $\varrho_{2*}(b_{3})$-eigenline:
> $$T'(b_{1}+ib_{2})=\beta f_{2},\qquad T'(b_{1}-ib_{2})=\alpha f_{1},\qquad T'(b_{3})=\gamma f_{3},$$
> for scalars $\alpha,\beta,\gamma$. Any such $T'$ automatically satisfies the $b_{3}$-relation (this is why the torus check cannot detect an error): the scalars $\alpha,\beta,\gamma$ are three *independent* degrees of freedom on the torus. Bär's $T$ corresponds to $\alpha_{\mathrm{B}}=-2i$, $\beta_{\mathrm{B}}=2$, $\gamma_{\mathrm{B}}=1$ (read off by applying $T$ to $b_{1}\pm ib_{2}$ and $b_{3}$), whose ratio $\alpha_{\mathrm{B}}/\beta_{\mathrm{B}}=-i$ is what the $b_{1}$-relation forbids.
>
> **Fixing the scale.** Writing $T'b_{1}=\tfrac12(\alpha f_{1}+\beta f_{2})$, $T'b_{2}=\tfrac1{2i}(\beta f_{2}-\alpha f_{1})$, $T'b_{3}=\gamma f_{3}$ and imposing $T'\operatorname{ad}_{b_{1}}=\varrho_{2*}(b_{1})T'$ entrywise yields the equations $i\alpha=-\gamma$ (from entry $(1,3)$), $-i\beta=\gamma$ (from $(2,3)$), and $\alpha-\beta=0$ (from $(3,1)$); these are consistent and give
> $$\alpha=\beta,\qquad\gamma=-i\alpha.$$
> So Schur's one scalar of freedom is $\alpha$; taking $\alpha=\beta=1$ and $\gamma=-i$,
> $$T'=\begin{pmatrix}\tfrac12&\tfrac{i}{2}&0\\[2pt]\tfrac12&-\tfrac{i}{2}&0\\[2pt]0&0&-i\end{pmatrix},\qquad T'^{-1}=\begin{pmatrix}1&1&0\\-i&i&0\\0&0&i\end{pmatrix}$$
> (the inverse verified by $T'T'^{-1}=\mathbb{1}$). Bär's $T$ differs from $T'$ not by an overall scalar but by *unequal* scalars on the two weight lines, which is exactly why it is not an intertwiner.
>
> **Verification of $T'$ on all three generators.** We check $T'\operatorname{ad}_{b_{a}}=\varrho_{2*}(b_{a})T'$ for $a=1,2,3$.
> For $a=3$: carrying out both products (the columns of $T'\operatorname{ad}_{b_{3}}$ are $-2\,t_{2}=(-i,i,0)$, $2\,t_{1}=(1,1,0)$, $0$, where $t_{1},t_{2},t_{3}$ denote the columns of $T'$),
> $$T'\operatorname{ad}_{b_{3}}=\begin{pmatrix}-i&1&0\\i&1&0\\0&0&0\end{pmatrix}=\varrho_{2*}(b_{3})T'\qquad(\varrho_{2*}(b_{3})=\operatorname{diag}(-2i,2i,0)\text{ scales the rows of }T').$$
> For $a=1$:
> $$T'\operatorname{ad}_{b_{1}}=\begin{pmatrix}\tfrac12&\tfrac{i}{2}&0\\\tfrac12&-\tfrac{i}{2}&0\\0&0&-i\end{pmatrix}\begin{pmatrix}0&0&0\\0&0&2\\0&-2&0\end{pmatrix}=\begin{pmatrix}0&0&i\\0&0&-i\\0&2i&0\end{pmatrix}=\begin{pmatrix}0&0&-1\\0&0&1\\2&-2&0\end{pmatrix}\begin{pmatrix}\tfrac12&\tfrac{i}{2}&0\\\tfrac12&-\tfrac{i}{2}&0\\0&0&-i\end{pmatrix}=\varrho_{2*}(b_{1})T'.$$
> For $a=2$:
> $$T'\operatorname{ad}_{b_{2}}=\begin{pmatrix}0&0&-1\\0&0&-1\\-2i&0&0\end{pmatrix}=\varrho_{2*}(b_{2})T',$$
> both sides computed directly. All three relations hold, so by Step 0 the corrected $T'$ satisfies $(\ast)$ for *all* $g\in SU(2)$: $T'\operatorname{Ad}_{g}T'^{-1}=\varrho_{2}(g)$. As a final cross-check at the earlier group counterexample $g=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$ with $\operatorname{Ad}_{g}=\operatorname{diag}(1,-1,-1)$,
> $$T'\operatorname{Ad}_{g}T'^{-1}=\begin{pmatrix}0&1&0\\1&0&0\\0&0&-1\end{pmatrix}=\varrho_{2}(g),$$
> now in agreement. Therefore $T'$ is a genuine intertwiner and $\varrho_{2}\cong(\operatorname{Ad})_{\mathbb{C}}$.

**Step 5: The classification route. — proves the equivalence with no intertwiner, via irreducibility and Schur.**

> [!note]- Derivation
> **$(\operatorname{Ad})_{\mathbb{C}}$ is irreducible.** Let $W\subseteq\mathfrak{su}(2)_{\mathbb{C}}$ be a complex subspace invariant under $(\operatorname{Ad})_{\mathbb{C},g}$ for all $g\in SU(2)$. Differentiating $g=\exp(tX)$ at $t=0$ (as in Step 0) shows $W$ is invariant under $(\operatorname{ad})_{\mathbb{C},X}$ for all $X\in\mathfrak{su}(2)$, hence, by complex linearity, for all $X\in\mathfrak{su}(2)_{\mathbb{C}}=\mathfrak{sl}(2;\mathbb{C})$; that is, $[X,W]\subseteq W$ for all $X$, so $W$ is a complex *ideal* of $\mathfrak{sl}(2;\mathbb{C})$.
>
> Now $\mathfrak{sl}(2;\mathbb{C})$ is *simple* (its only ideals are $0$ and itself). Indeed, in the standard basis $H=\left(\begin{smallmatrix}1&0\\0&-1\end{smallmatrix}\right)$, $E=\left(\begin{smallmatrix}0&1\\0&0\end{smallmatrix}\right)$, $F=\left(\begin{smallmatrix}0&0\\1&0\end{smallmatrix}\right)$ with $[H,E]=2E$, $[H,F]=-2F$, $[E,F]=H$, the operator $\operatorname{ad}_{H}$ has three distinct eigenvalues $2,0,-2$ on the eigenlines $\mathbb{C}E,\mathbb{C}H,\mathbb{C}F$; any nonzero ideal $W$, being $\operatorname{ad}_{H}$-invariant, is a sum of some of these eigenlines and so contains at least one of $E,H,F$. If $H\in W$ then $[F,H]=2F\in W$ and $[E,H]=-2E\in W$, so $W=\mathfrak{sl}(2;\mathbb{C})$; if $E\in W$ then $[F,E]=-H\in W$ and we reduce to the previous case; if $F\in W$ then $[E,F]=H\in W$ likewise. Hence $W=0$ or $W=\mathfrak{sl}(2;\mathbb{C})$, and $(\operatorname{Ad})_{\mathbb{C}}$ is irreducible. Its dimension is $\dim_{\mathbb{C}}\mathfrak{su}(2)_{\mathbb{C}}=\dim_{\mathbb{R}}\mathfrak{su}(2)=3$.
>
> **Identification via the classification.** By part (B) of [[Thm - Complex Representations of U(1) and SU(2)|the classification theorem]], the irreducible complex representations of $SU(2)$ are exactly the $\varrho_{k}=\odot^{k}\varrho_{1}$, with $\dim\varrho_{k}=k+1$, and they are pairwise inequivalent. The unique one of dimension three is $\varrho_{2}$ ($k=2$). Since $(\operatorname{Ad})_{\mathbb{C}}$ is an irreducible complex representation of dimension three, it is equivalent to $\varrho_{2}$:
> $$(\operatorname{Ad})_{\mathbb{C}}\cong\varrho_{2}.$$
> This is Bär's Remark 1.3.4 made precise: because $\operatorname{Ad}_{SU(2)}$ is *real* three-dimensional, its complexification is a three-dimensional complex representation, and $\varrho_{2}$ (dimension $2+1=3$) is the only member of the family it can match — the neighbouring $\varrho_{1}$ (dimension $2$) and $\varrho_{3}$ (dimension $4$) are ruled out on dimension alone.
>
> **Schur's lemma reconciles the two routes.** A nonzero intertwiner $S$ between two irreducible representations is an isomorphism, because $\ker S$ and $\operatorname{im}S$ are invariant subspaces of an irreducible representation, hence $0$ or everything, and $S\neq0$ forces $\ker S=0$, $\operatorname{im}S=$ all. Moreover, over $\mathbb{C}$, a self-intertwiner $S$ of an irreducible representation is a scalar: it has an eigenvalue $\mu$ (algebraically closed field), $S-\mu\,\mathbb{1}$ is again a self-intertwiner with nonzero kernel, so $S-\mu\,\mathbb{1}=0$. Consequently the space of intertwiners $(\operatorname{Ad})_{\mathbb{C}}\to\varrho_{2}$ is *at most one-dimensional*: if $S_{1},S_{2}$ are two, then $S_{2}^{-1}S_{1}$ is a self-intertwiner of $(\operatorname{Ad})_{\mathbb{C}}$, hence a scalar, so $S_{1}=\lambda S_{2}$. This is exactly the single scalar of freedom found in Step 4 (the parameter $\alpha$), and it explains structurally why Bär's $T$ — which used *two* independent scalars — could not lie in this one-dimensional space unless those scalars were equal.

> [!note]- Complete formal solution
> Work in Bär's Pauli labelling, $b_{a}=-i\sigma_{a}$, with $[b_{a},b_{b}]=-2\varepsilon_{abc}b_{c}$ (Step 1). Fix bases $b_{1},b_{2},b_{3}$ of $\mathfrak{su}(2)_{\mathbb{C}}$ and $f_{1}=e_{1}\odot e_{1},f_{2}=e_{2}\odot e_{2},f_{3}=e_{2}\odot e_{1}$ of $\odot^{2}\mathbb{C}^{2}$.
>
> *Reduction.* For a fixed linear isomorphism $T$, $(\ast)$ holds for all $g\in SU(2)$ iff $T(\operatorname{ad})_{\mathbb{C},X}=\varrho_{2*}(X)T$ for all $X\in\mathfrak{su}(2)$, iff it holds for $X=b_{1},b_{2},b_{3}$. Forward: differentiate $(\ast)$ at $\exp(tX)$, $t=0$, using naturality of $\exp$. Backward: $\exp$ is onto $SU(2)$ (compact connected), and $T\exp(M)T^{-1}=\exp(TMT^{-1})$, so the algebra relation integrates to $(\ast)$.
>
> *The matrices.* From the brackets, $\operatorname{ad}_{b_{1}}=\left(\begin{smallmatrix}0&0&0\\0&0&2\\0&-2&0\end{smallmatrix}\right)$, $\operatorname{ad}_{b_{2}}=\left(\begin{smallmatrix}0&0&-2\\0&0&0\\2&0&0\end{smallmatrix}\right)$, $\operatorname{ad}_{b_{3}}=\left(\begin{smallmatrix}0&2&0\\-2&0&0\\0&0&0\end{smallmatrix}\right)$. From $\varrho_{2*}(X)(u\odot v)=(Xu)\odot v+u\odot(Xv)$, $\varrho_{2*}(b_{1})=\left(\begin{smallmatrix}0&0&-1\\0&0&1\\2&-2&0\end{smallmatrix}\right)$, $\varrho_{2*}(b_{2})=\left(\begin{smallmatrix}0&0&-i\\0&0&-i\\-2i&-2i&0\end{smallmatrix}\right)$, $\varrho_{2*}(b_{3})=\operatorname{diag}(-2i,2i,0)$.
>
> *Bär's $T$ fails.* With $T=\left(\begin{smallmatrix}-i&1&0\\1&-i&0\\0&0&1\end{smallmatrix}\right)$ the relation holds for $b_{3}$ but $T\operatorname{ad}_{b_{1}}\neq\varrho_{2*}(b_{1})T$ (their $(1,3)$ entries are $2$ and $-1$); equivalently $T\operatorname{Ad}_{g}T^{-1}\neq\varrho_{2}(g)$ at $g=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$. So Bär's intertwiner is valid only on the maximal torus.
>
> *Corrected intertwiner.* An intertwiner must map $b_{1}\pm ib_{2}$ (the $\pm2i$-eigenlines of $\operatorname{ad}_{b_{3}}$) into $f_{2},f_{1}$ respectively and $b_{3}$ into $f_{3}$; imposing the $b_{1}$-relation forces the relative scale to $\alpha=\beta,\ \gamma=-i\alpha$, giving $T'=\left(\begin{smallmatrix}1/2&i/2&0\\1/2&-i/2&0\\0&0&-i\end{smallmatrix}\right)$. Direct computation confirms $T'\operatorname{ad}_{b_{a}}=\varrho_{2*}(b_{a})T'$ for $a=1,2,3$, so $T'\operatorname{Ad}_{g}T'^{-1}=\varrho_{2}(g)$ for all $g$, and $\varrho_{2}\cong(\operatorname{Ad})_{\mathbb{C}}$.
>
> *Classification route.* A complex $(\operatorname{Ad})_{\mathbb{C}}$-invariant subspace is a complex ideal of $\mathfrak{sl}(2;\mathbb{C})$; $\mathfrak{sl}(2;\mathbb{C})$ is simple (the $H,E,F$ argument), so $(\operatorname{Ad})_{\mathbb{C}}$ is irreducible of dimension $3$. By the classification (part B) the unique three-dimensional irreducible complex representation of $SU(2)$ is $\varrho_{2}$; hence $(\operatorname{Ad})_{\mathbb{C}}\cong\varrho_{2}$. By Schur the intertwiner is unique up to one scalar, matching the free parameter $\alpha$ in $T'$. $\blacksquare$

> [!warning] Illegal but tempting route
> It is tempting to accept $(\ast)$ on the strength of Bär's diagonal check alone, reasoning "every element of $SU(2)$ is conjugate to a diagonal one, and both sides transform by conjugation, so the torus case suffices." The flaw is that the *intertwiner $T$ is fixed once and for all*; conjugating $g$ to a diagonal $hgh^{-1}$ replaces $\operatorname{Ad}_{g}$ by $\operatorname{Ad}_{h}\operatorname{Ad}_{g}\operatorname{Ad}_{h}^{-1}$ and $\varrho_{2}(g)$ by $\varrho_{2}(h)\varrho_{2}(g)\varrho_{2}(h)^{-1}$, so $T\operatorname{Ad}_{g}T^{-1}=\varrho_{2}(g)$ off the torus requires $T\operatorname{Ad}_{h}=\varrho_{2}(h)T$ for the conjugating $h$ *as well* — which is the very relation in doubt. The torus check verifies $(\ast)$ only where $h$ can be taken in the torus (the centraliser of $g$), i.e. on the torus itself. The correct principle is the Lie-algebra reduction of Step 0: check on a *basis* of $\mathfrak{su}(2)$, which includes the off-torus directions $b_{1},b_{2}$, not merely on one Cartan direction.

---

# Key Takeaways

The transferable principle is the **Lie-algebra reduction for connected groups**: a linear identity asserted for all $g$ in a connected matrix group with surjective exponential — here $SU(2)$ — holds for all $g$ if and only if its differential holds on a *basis* of the Lie algebra, because $\exp$ is onto and conjugation commutes with the matrix exponential. This is the standard machine for verifying intertwiners, invariance of a bilinear form, or a conservation law "for all group elements": never check infinitely many $g$; differentiate to $\mathfrak{g}$, check three (here) numbers' worth of relations, integrate back. The trigger is the phrase "for all $g$" attached to a smooth, linear-in-$g$ statement on a connected group; the reaction is to pass to the Lie algebra. The same reduction reappears throughout the gauge-theory notes — in checking that a connection form is $\operatorname{Ad}$-equivariant, that a Chern–Weil polynomial is invariant, or that a gauge transformation preserves a structure — always as "it is enough to check on the Lie algebra".

The second, sharper lesson is a *diagnostic about where a verification can hide an error*: the **maximal torus is blind to off-diagonal structure**. Bär's intertwiner passes the diagonal test yet fails globally because diagonal elements exercise only the Cartan direction $b_{3}$, on which the two weight lines $b_{1}\pm ib_{2}$ are independent eigenlines that tolerate independent rescalings. Schur's lemma says the true intertwiner between irreducibles has exactly *one* scalar of freedom, so any construction that secretly introduces a second scalar (a different normalisation on each weight line) will look right on the torus and break the instant a group element mixes the lines. Whenever a claimed equivalence has been checked only "on the torus", "on the diagonal", or "on a maximal abelian subalgebra", treat it as unverified in the off-diagonal directions; the raising and lowering operators are where the real constraints live. This is the representation-theoretic form of a general modelling caution: a symmetry check restricted to the fixed locus of a large stabiliser cannot detect errors that live transverse to that locus.

Finally, the pair of routes illustrates the complementary value of **explicit intertwiners versus classification**. Route 2 proves $\varrho_{2}\cong(\operatorname{Ad})_{\mathbb{C}}$ with almost no computation — irreducibility of the adjoint from simplicity of $\mathfrak{sl}(2;\mathbb{C})$, a dimension count, and the classification theorem — and it is the argument to reach for when one only needs *that* two representations agree. Route 1 produces the actual isomorphism $T'$, which one needs whenever the identification must be used concretely: to write the associated $SU(2)$ bundle $P\times_{\varrho_{2}}\odot^{2}\mathbb{C}^{2}$ as the complexified adjoint bundle $\mathfrak{g}_{P}\otimes\mathbb{C}$ (chapter III), to translate spinor computations into $\mathfrak{so}(3)$ language, or to match the physicists' "spin-$1$" representation with the vector representation of $SO(3)$. Carrying both — the cheap existence proof and the explicit, *correctly normalised* intertwiner — is the reusable habit; and the correction of Bär's $T'$ is a reminder that "an explicit formula from a reference" is data to be checked, not a theorem to be trusted. Companion exercises are [[Ex - The Adjoint Representation of SU(2) in the Pauli Basis]] (the torus computation whose blind spot this exercise exposes) and [[Ex - Decomposing the Tensor Square of the Standard Representation of SU(2)]] (the neighbouring Clebsch–Gordan decomposition $\varrho_{1}\otimes\varrho_{1}\cong\varrho_{2}\oplus\varrho_{0}$, another weight computation).
