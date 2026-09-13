---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Hodge Star in Arbitrary Signature"
  - "Thm - Properties of the Hodge Star in Arbitrary Signature"
  - "Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $V$ be an oriented real vector space of dimension $n$ with a non-degenerate symmetric bilinear form $g = \langle\cdot,\cdot\rangle$ of index $p$, and let $\lambda > 0$ be a positive real number. Consider the **conformally rescaled** form $g' := \lambda^2 g$. Write $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle'$ for the induced inner products on the exterior powers, $\mathrm{vol}$ and $\mathrm{vol}'$ for the two volume forms, and $\star$ and $\star'$ for the two Hodge stars, all attached to $g$ and $g'$ respectively. Prove the **conformal weights**:
$$\langle\cdot,\cdot\rangle'_{\Lambda^k V^*} = \lambda^{-2k}\,\langle\cdot,\cdot\rangle_{\Lambda^k V^*}, \qquad \mathrm{vol}' = \lambda^n\,\mathrm{vol}, \qquad \star' = \lambda^{\,n-2k}\,\star \ \text{ on } \Lambda^k V^*.$$
Conclude that in dimension $n = 4$, on $2$-forms ($k = 2$), the Hodge star is conformally invariant: $\star' = \star$. The statements hold verbatim, pointwise, for a conformal change $g' = \lambda^2 g$ with $\lambda \in C^\infty(M)$, $\lambda > 0$, on an oriented semi-Riemannian manifold $M$.

This is the algebraic content of the first half of Bär's discussion of conformal invariance (Remark 3.2.11): it records exactly how each Hodge-theoretic object scales when the metric is multiplied by a positive conformal factor, and it isolates dimension four with $k = 2$ as the unique degree in which the star does not scale at all. That single invariance is what makes the electromagnetic action $\tfrac12\int_M F\wedge\star F$ conformally invariant in four dimensions and forces the electromagnetic energy–momentum tensor to be trace-free; those physical conclusions are drawn on [[Thm - Conformal Invariance of the Electromagnetic Action and Tracelessness of the Energy-Momentum Tensor]]. Here we prove only the linear algebra of the weights.

> [!warning] Source typo (Bär p. 93)
> Bär's text writes the conformal rescaling as "$g' = \lambda \cdot g$" in the sentence defining conformal invariance, but every computation on the same page uses $g' = \lambda^2 g$ (he takes the rescaled generalized orthonormal basis to be $e_i' = \lambda^{-1}e_i$, which is $g'$-orthonormal only for $g' = \lambda^2 g$). We use the corrected form $g' = \lambda^2 g$ throughout, so that the two conventions Bär mixes are reconciled and the exponents come out as stated. The factor $\lambda^2$ (rather than $\lambda$) is also the standard normalisation in conformal geometry, where one writes $g' = e^{2f}g$.

**Recall:**

The objects in play are the generalized orthonormal basis and its induced structures on the exterior powers, and the Hodge star through its defining relation.

![[Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms#The Definition]]

For a non-degenerate symmetric bilinear form $g$ on $V$, a **generalized orthonormal basis** $e_1,\dots,e_n$ satisfies $g(e_i,e_j) = \epsilon_i\delta_{ij}$ with $\epsilon_i \in \{+1,-1\}$; the **index** $p$ is the number of $i$ with $\epsilon_i = -1$. Writing $e_1^*,\dots,e_n^*$ for the dual basis of $V^*$ and $e_I^* := e_{i_1}^* \wedge \dots \wedge e_{i_k}^*$ for a multi-index $I = (i_1 < \dots < i_k)$, the **induced inner product** on $\Lambda^k V^*$ is determined by $\langle e_I^*, e_J^*\rangle = \delta_{IJ}\,\epsilon_{i_1}\cdots\epsilon_{i_k}$ (so the $e_I^*$ form a generalized orthonormal basis of $\Lambda^k V^*$), and the **volume form** of an oriented $V$ is $\mathrm{vol} = e_1^* \wedge \dots \wedge e_n^*$ for a positively oriented generalized orthonormal basis.

![[Def - Hodge Star in Arbitrary Signature#The Definition]]

The **Hodge star** $\star: \Lambda^k V^* \to \Lambda^{n-k} V^*$ of $(V, g)$ is the unique linear map with
$$\alpha \wedge \beta = \langle\star\alpha,\beta\rangle\,\mathrm{vol} \qquad \text{for all } \alpha \in \Lambda^k V^*,\ \beta \in \Lambda^{n-k} V^*.$$
Existence and uniqueness rest on the non-degeneracy of the induced inner product on $\Lambda^{n-k} V^*$ (see [[Thm - Existence and Uniqueness of the Hodge Star]] and part (ii) of [[Thm - The Induced Inner Product and Volume Form are Well-Defined]]): a linear functional on $\Lambda^{n-k}V^*$ is represented by a *unique* element, and that element is $\star\alpha$.

> [!warning] Convention: three Hodge stars
> This series uses Bär's convention $\alpha\wedge\beta = \langle\star_B\alpha,\beta\rangle\,\mathrm{vol}$ throughout; here $\star = \star_B$. It relates to the vault's Riemannian star $\star_V$ (defined by $\alpha\wedge\star_V\beta = \langle\alpha,\beta\rangle\,\mathrm{vol}$, [[Def - The Hodge Star Operator]]) by $\star_B = (-1)^p\star_V$, and to the convention $\star'_{\mathrm{alt}}\alpha\wedge\beta = \langle\alpha,\beta\rangle\,\mathrm{vol}$ by $\star'_{\mathrm{alt}} = (-1)^{k(n-k)}\star_V$. All three agree when $p = 0$. Conformal weights are unaffected by which convention one uses, because the conformal factor $\lambda$ is a metric datum and the intervening signs are metric-independent constants that cancel between $g$ and $g'$.

---

# Convergent Strategy

**Problem class.** This is a *scaling-weight* problem: a family of geometric objects is built functorially from a metric, the metric is rescaled by a positive factor, and one asks for the power of $\lambda$ by which each object is multiplied. The recognisable feature is that every object — inner product, volume form, star — is *defined* from an orthonormal basis and a wedge relation, so once one knows how a single orthonormal basis rescales, every weight follows by tracking powers of $\lambda$.

**Assumption pattern.** The whole computation hinges on one observation: if $e_i$ is $g$-orthonormal, then $e_i' = \lambda^{-1}e_i$ is $g'$-orthonormal *with the same signs* $\epsilon_i$, hence the same index $p$. Positivity of $\lambda$ is used twice — to take a square root implicitly (so that $\lambda^{-1}$ is real and the rescaled basis is genuine) and to ensure the orientation is preserved so that $\mathrm{vol}$ and $\mathrm{vol}'$ use compatible orderings. Non-degeneracy of the induced form on $\Lambda^{n-k}V^*$ is used once, to pass from an identity of pairings to an identity of the stars themselves.

**Theorem routing.** The route is: (1) rescale the basis, $e_i' = \lambda^{-1}e_i$, and dualise to $(e_i^*)' = \lambda e_i^*$; (2) read off the inner-product weight $\lambda^{-2k}$ on $\Lambda^k$ from the fact that $\omega$ evaluated on $k$ rescaled basis vectors picks up $\lambda^{-k}$ per argument, appearing squared; (3) read off $\mathrm{vol}' = \lambda^n\mathrm{vol}$ from the dual-basis rescaling in top degree; (4) combine (2) and (3) inside the [[Def - Hodge Star in Arbitrary Signature|defining relation]] of $\star'$ and use [[Thm - The Induced Inner Product and Volume Form are Well-Defined|non-degeneracy]] to solve for $\star'$; (5) set $n = 4$, $k = 2$ so the exponent $n - 2k$ vanishes.

**Key decision point.** The one genuine subtlety is *bookkeeping the exponent in the star weight*, and it is the point at which the source's stated exponent must be read carefully. The defining relation of $\star'$ pairs a form in $\Lambda^k$ with a form in $\Lambda^{n-k}$, so *two different inner-product weights* enter — $\lambda^{-2k}$ and $\lambda^{-2(n-k)}$ — together with the volume weight $\lambda^{n}$. Whether the net exponent comes out as $n - 2k$ or $2k - n$ depends entirely on *which degree the star is acting on*. We take $\star'$ acting on $\Lambda^k$ and obtain $\star' = \lambda^{n-2k}\star$; Bär displays the same identity with the exponent $2k - n$ because in his display the star acts on the complementary form in $\Lambda^{n-k}$. Recognising that these are the *same* statement re-indexed by $k \mapsto n-k$ is the decision that keeps the sign of the exponent straight.

---

# Legal Operations Used

This solution deploys the following operations, in the sense of the topic page's Legal Operations for the Hodge star (numbers to be reconciled once the [[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory|chapter topic page]] is assembled):

1. **Rescale a generalized orthonormal basis under a conformal change.** From a $g$-orthonormal basis $e_i$ produce the $g'$-orthonormal basis $e_i' = \lambda^{-1}e_i$, preserving all signs $\epsilon_i$ and the index $p$; dualise to $(e_i^*)' = \lambda e_i^*$.

2. **Track a scaling weight through a multilinear evaluation.** Evaluating a $k$-form on $k$ rescaled vectors multiplies the value by $\lambda^{-k}$; since the induced inner product is a sum of products of two such evaluations, its weight is $\lambda^{-2k}$.

3. **Compute the top-degree weight from the dual basis.** The volume form is a wedge of $n$ dual basis vectors, each carrying weight $\lambda$, giving $\mathrm{vol}' = \lambda^n\mathrm{vol}$.

4. **Solve for a linear map inside the defining relation using non-degeneracy.** Substitute the two weights into $\alpha\wedge\beta = \langle\star'\alpha,\beta\rangle'\,\mathrm{vol}'$, match against the unprimed defining relation, and cancel the common non-degenerate pairing to isolate $\star'$ in terms of $\star$.

5. **Specialise a general exponent to a critical dimension.** Set $n = 4$, $k = 2$ to make $n - 2k = 0$, collapsing $\star' = \lambda^{n-2k}\star$ to $\star' = \star$.

---

# Hints

> [!note]- Hint 1
> Everything is built from a generalized orthonormal basis. So first answer: if $e_1,\dots,e_n$ is orthonormal for $g$, what simple rescaling $e_i' = c\,e_i$ makes it orthonormal for $g' = \lambda^2 g$? Solve $g'(e_i',e_i') = \pm 1$ for the constant $c$. Do the signs $\epsilon_i$ change?

> [!note]- Hint 2
> You should find $e_i' = \lambda^{-1}e_i$, with the same signs $\epsilon_i$ (so the same index $p$). Now dualise: if $e_i' = \lambda^{-1}e_i$, what is the basis of $V^*$ dual to the $e_i'$? Check that $(\lambda e_i^*)(\lambda^{-1}e_j) = \delta_{ij}$. This gives $(e_i^*)' = \lambda e_i^*$.

> [!note]- Hint 3
> A $k$-form $\omega$ evaluated on $e_{i_1}',\dots,e_{i_k}'$ equals $\lambda^{-k}\,\omega(e_{i_1},\dots,e_{i_k})$ by multilinearity. The induced inner product $\langle\omega,\eta\rangle'$ is a sum of terms $\epsilon\cdots\,\omega(\dots)\eta(\dots)$ with the primed basis inserted, so each term acquires $\lambda^{-k}\cdot\lambda^{-k} = \lambda^{-2k}$. For the volume form, $\mathrm{vol}' = (e_1^*)'\wedge\dots\wedge(e_n^*)'$; count the powers of $\lambda$.

> [!note]- Hint 4
> For the star, use its defining relation for $\star'$: $\alpha\wedge\beta = \langle\star'\alpha,\beta\rangle'\,\mathrm{vol}'$ with $\alpha\in\Lambda^k$, $\beta\in\Lambda^{n-k}$. Here $\star'\alpha$ and $\beta$ both live in $\Lambda^{n-k}$, so the inner-product weight is $\lambda^{-2(n-k)}$, and $\mathrm{vol}' = \lambda^n\mathrm{vol}$. Combine the two exponents, compare with the unprimed relation $\alpha\wedge\beta = \langle\star\alpha,\beta\rangle\,\mathrm{vol}$, and cancel by non-degeneracy. Watch the sign of the final exponent.

---

# Solution

The whole computation follows one rescaled basis through every definition. A $g$-orthonormal basis, shrunk by $\lambda^{-1}$, is $g'$-orthonormal; its dual grows by $\lambda$; and the powers of $\lambda$ that the inner product and volume form pick up combine, inside the defining relation of the star, to the single exponent $n - 2k$, which vanishes exactly when $2k = n$.

**Step 1: The rescaled basis $e_i' = \lambda^{-1}e_i$ is $g'$-orthonormal, with dual $(e_i^*)' = \lambda e_i^*$.**

Shrinking a $g$-orthonormal basis by the factor $\lambda^{-1}$ produces a $g'$-orthonormal basis with unchanged signs, and its dual basis is scaled by $\lambda$.

> [!note]- Derivation
> Let $e_1,\dots,e_n$ be a positively oriented generalized orthonormal basis for $g$, so $g(e_i,e_j) = \epsilon_i\delta_{ij}$. Define $e_i' := \lambda^{-1}e_i$, which is a genuine basis because $\lambda > 0$. Then, using $g' = \lambda^2 g$ and bilinearity,
> $$g'(e_i',e_j') = \lambda^2\,g(\lambda^{-1}e_i,\lambda^{-1}e_j) = \lambda^2\lambda^{-2}\,g(e_i,e_j) = \epsilon_i\delta_{ij} \qquad (g' = \lambda^2 g;\ \text{bilinearity};\ g\text{-orthonormality of }e_i).$$
> Hence $e_1',\dots,e_n'$ is a generalized orthonormal basis for $g'$ **with the same signs** $\epsilon_i$, so $g'$ has the same index $p$ as $g$; and since $\lambda > 0$, the change $e_i \mapsto \lambda^{-1}e_i$ has positive determinant $\lambda^{-n}$ and so preserves the orientation, making $e_i'$ positively oriented.
>
> For the dual basis, let $(e_i^*)'$ denote the basis of $V^*$ dual to $e_1',\dots,e_n'$, characterised by $(e_i^*)'(e_j') = \delta_{ij}$. The form $\lambda e_i^*$ satisfies
> $$(\lambda e_i^*)(e_j') = (\lambda e_i^*)(\lambda^{-1}e_j) = \lambda\lambda^{-1}\,e_i^*(e_j) = e_i^*(e_j) = \delta_{ij} \qquad (\text{definition of }e_j';\ \text{linearity};\ e_i^*(e_j) = \delta_{ij}),$$
> so by uniqueness of the dual basis $(e_i^*)' = \lambda\,e_i^*$.

**Step 2: The induced inner product on $\Lambda^k V^*$ scales by $\lambda^{-2k}$.**

Because a $k$-form evaluated on $k$ shrunk vectors picks up $\lambda^{-k}$, and the inner product multiplies two such evaluations, $\langle\cdot,\cdot\rangle'_{\Lambda^k} = \lambda^{-2k}\langle\cdot,\cdot\rangle$.

> [!note]- Derivation
> Fix $\omega,\eta \in \Lambda^k V^*$. By definition of the induced inner product for $g'$, computed in the $g'$-orthonormal basis $e_i'$ (legitimate by [[Thm - The Induced Inner Product and Volume Form are Well-Defined|basis-independence]], part (i)),
> $$\langle\omega,\eta\rangle' = \sum_{i_1 < \dots < i_k} \epsilon_{i_1}\cdots\epsilon_{i_k}\,\omega(e_{i_1}',\dots,e_{i_k}')\,\eta(e_{i_1}',\dots,e_{i_k}') \qquad (\text{induced product in the }g'\text{-orthonormal basis; signs }\epsilon_i\text{ unchanged, Step 1}).$$
> Each evaluation scales by $\lambda^{-k}$, since $\omega$ is $k$-linear and each of its $k$ arguments $e_{i_j}' = \lambda^{-1}e_{i_j}$ contributes a factor $\lambda^{-1}$:
> $$\omega(e_{i_1}',\dots,e_{i_k}') = \omega(\lambda^{-1}e_{i_1},\dots,\lambda^{-1}e_{i_k}) = \lambda^{-k}\,\omega(e_{i_1},\dots,e_{i_k}) \qquad (k\text{-linearity of }\omega),$$
> and likewise $\eta(e_{i_1}',\dots,e_{i_k}') = \lambda^{-k}\,\eta(e_{i_1},\dots,e_{i_k})$. Substituting, the constant $\lambda^{-k}\cdot\lambda^{-k} = \lambda^{-2k}$ factors out of every summand:
> $$\langle\omega,\eta\rangle' = \lambda^{-2k}\sum_{i_1 < \dots < i_k}\epsilon_{i_1}\cdots\epsilon_{i_k}\,\omega(e_{i_1},\dots,e_{i_k})\,\eta(e_{i_1},\dots,e_{i_k}) = \lambda^{-2k}\,\langle\omega,\eta\rangle \qquad (\text{factor out }\lambda^{-2k};\ \text{recognise the }g\text{-induced product}).$$
> Since $\omega,\eta$ were arbitrary, $\langle\cdot,\cdot\rangle'_{\Lambda^k V^*} = \lambda^{-2k}\langle\cdot,\cdot\rangle_{\Lambda^k V^*}$.

**Step 3: The volume form scales by $\lambda^{n}$.**

The top-degree wedge of the rescaled dual basis multiplies each of the $n$ factors by $\lambda$, giving $\mathrm{vol}' = \lambda^n\mathrm{vol}$.

> [!note]- Derivation
> The volume form of $(V, g')$ for the positively oriented $g'$-orthonormal basis $e_i'$ (positively oriented by Step 1) is
> $$\mathrm{vol}' = (e_1^*)' \wedge \dots \wedge (e_n^*)' = (\lambda e_1^*) \wedge \dots \wedge (\lambda e_n^*) \qquad (\text{definition of }\mathrm{vol}';\ (e_i^*)' = \lambda e_i^*\text{, Step 1}).$$
> Each of the $n$ factors carries a scalar $\lambda$, and scalars pull out of the wedge product, so
> $$\mathrm{vol}' = \lambda^n\, e_1^* \wedge \dots \wedge e_n^* = \lambda^n\,\mathrm{vol} \qquad (n\text{ scalar factors }\lambda\text{ extracted from the wedge}).$$
> (As a consistency check, $\langle\mathrm{vol}',\mathrm{vol}'\rangle' = \lambda^{-2n}\langle\mathrm{vol}',\mathrm{vol}'\rangle = \lambda^{-2n}\lambda^{2n}\langle\mathrm{vol},\mathrm{vol}\rangle = (-1)^p$ by Steps 2 and 3, matching the required value $\langle\mathrm{vol}',\mathrm{vol}'\rangle' = (-1)^p$ for the index-$p$ form $g'$.)

**Step 4: The Hodge star on $\Lambda^k V^*$ scales by $\lambda^{n-2k}$.**

Feeding the two weights into the defining relation of $\star'$ and cancelling the non-degenerate pairing yields $\star' = \lambda^{n-2k}\star$ on $\Lambda^k V^*$.

> [!note]- Derivation
> Fix $\alpha \in \Lambda^k V^*$. The Hodge star $\star'$ of $g'$ is characterised by its defining relation: for all $\beta \in \Lambda^{n-k} V^*$,
> $$\alpha \wedge \beta = \langle\star'\alpha,\beta\rangle'\,\mathrm{vol}' \qquad (\text{defining relation of }\star').$$
> Now $\star'\alpha \in \Lambda^{n-k} V^*$ and $\beta \in \Lambda^{n-k} V^*$, so the primed inner product on the right is the one on $\Lambda^{n-k}V^*$, which by Step 2 (with $k$ replaced by $n-k$) equals $\lambda^{-2(n-k)}$ times the unprimed inner product; and $\mathrm{vol}' = \lambda^n\mathrm{vol}$ by Step 3. Therefore
> $$\alpha \wedge \beta = \lambda^{-2(n-k)}\,\langle\star'\alpha,\beta\rangle\cdot\lambda^{n}\,\mathrm{vol} = \lambda^{\,2k-n}\,\langle\star'\alpha,\beta\rangle\,\mathrm{vol} \qquad (\langle\cdot,\cdot\rangle' = \lambda^{-2(n-k)}\langle\cdot,\cdot\rangle\text{ on }\Lambda^{n-k}\text{, Step 2};\ \mathrm{vol}' = \lambda^n\mathrm{vol}\text{, Step 3};\ -2(n-k)+n = 2k-n).$$
> On the other hand, the unprimed defining relation gives $\alpha\wedge\beta = \langle\star\alpha,\beta\rangle\,\mathrm{vol}$. Equating the two expressions for $\alpha\wedge\beta$ and cancelling $\mathrm{vol}$ (a non-zero element of the one-dimensional $\Lambda^n V^*$),
> $$\langle\star\alpha,\beta\rangle = \lambda^{\,2k-n}\,\langle\star'\alpha,\beta\rangle \qquad \text{for all }\beta \in \Lambda^{n-k} V^*.$$
> The induced inner product on $\Lambda^{n-k}V^*$ is **non-degenerate** (part (ii) of [[Thm - The Induced Inner Product and Volume Form are Well-Defined]]), so a form annihilated by pairing against every $\beta$ is zero; applied to $\star\alpha - \lambda^{2k-n}\star'\alpha$, this gives $\star\alpha = \lambda^{2k-n}\star'\alpha$, that is
> $$\star'\alpha = \lambda^{-(2k-n)}\,\star\alpha = \lambda^{\,n-2k}\,\star\alpha.$$
> Since $\alpha \in \Lambda^k V^*$ was arbitrary, $\star' = \lambda^{n-2k}\star$ on $\Lambda^k V^*$.

> [!note]- Reconciling the exponent with Bär's displayed formula
> Bär's page 93 concludes "$\star' = \lambda^{2k-n}\star$", which at first sight has the opposite exponent. The two statements are identical once one is careful about *which degree the star acts on*. In Bär's display the identity $\langle\omega,\star\eta\rangle\,\mathrm{vol} = \omega\wedge\eta = \lambda^{n-2k}\langle\omega,\star'\eta\rangle\,\mathrm{vol}$ is written with $\omega \in \Lambda^k$ and $\eta \in \Lambda^{n-k}$, so the star there acts on $\eta$, a form of degree $n-k$; his exponent $2k-n$ is indexed by the degree $k$ of the *paired* form $\omega$. If one renames the acting degree to $m := n-k$, his formula reads $\star' = \lambda^{2(n-m)-n}\star = \lambda^{n-2m}\star$, which is exactly the formula proved above with $m$ the degree the star acts on. In short: **on $\Lambda^k V^*$ the weight is $\lambda^{n-2k}$**, and Bär's $\lambda^{2k-n}$ is the same statement for the complementary degree. The two agree at $2k = n$, which is the only case used in the physics, so no conclusion downstream is affected; the spec's transcription "$\star' = \lambda^{2k-n}$ on $\Lambda^k$" inherits Bär's index labelling and is corrected here. ⚠️ [flagged: exponent sign relative to the spec/source, resolved by the $k \leftrightarrow n-k$ re-indexing above.]

**Step 5: In dimension four, on 2-forms, the star is conformally invariant.**

Setting $n = 4$ and $k = 2$ makes the exponent vanish, so $\star' = \star$.

> [!note]- Derivation
> Take $n = 4$ and $k = 2$. Then the exponent in Step 4 is $n - 2k = 4 - 4 = 0$, so
> $$\star' = \lambda^{\,0}\,\star = \star \qquad \text{on }\Lambda^2 V^*\text{ with }\dim V = 4.$$
> The Hodge star on middle-degree forms in the middle dimension is unchanged by any conformal rescaling of the metric. This is the algebraic reason that the four-dimensional electromagnetic Lagrangian $\tfrac12 F\wedge\star F$ — built from the $2$-form $F$ and its star in dimension four — is conformally invariant, the conclusion drawn on [[Thm - Conformal Invariance of the Electromagnetic Action and Tracelessness of the Energy-Momentum Tensor]].

> [!note]- Complete formal solution
> **Claim.** Let $(V, g)$ be an oriented $n$-dimensional real vector space with a non-degenerate symmetric bilinear form of index $p$, let $\lambda > 0$, and set $g' = \lambda^2 g$. Then $\langle\cdot,\cdot\rangle'_{\Lambda^k V^*} = \lambda^{-2k}\langle\cdot,\cdot\rangle$, $\mathrm{vol}' = \lambda^n\mathrm{vol}$, and $\star' = \lambda^{n-2k}\star$ on $\Lambda^k V^*$; in particular $\star' = \star$ when $n = 4$, $k = 2$.
>
> *Proof.* Let $e_1,\dots,e_n$ be a positively oriented $g$-orthonormal basis, $g(e_i,e_j) = \epsilon_i\delta_{ij}$. Set $e_i' = \lambda^{-1}e_i$. Then $g'(e_i',e_j') = \lambda^2 g(\lambda^{-1}e_i,\lambda^{-1}e_j) = \epsilon_i\delta_{ij}$, so $e_i'$ is $g'$-orthonormal with the same signs (hence $g'$ has index $p$) and, as $\lambda > 0$, is positively oriented; its dual basis is $(e_i^*)' = \lambda e_i^*$, since $(\lambda e_i^*)(\lambda^{-1}e_j) = \delta_{ij}$.
>
> For $\omega,\eta \in \Lambda^k V^*$, computing the $g'$-induced inner product in the basis $e_i'$ and using $k$-linearity, $\omega(e_{i_1}',\dots,e_{i_k}') = \lambda^{-k}\omega(e_{i_1},\dots,e_{i_k})$ and $\eta(e_{i_1}',\dots,e_{i_k}') = \lambda^{-k}\eta(e_{i_1},\dots,e_{i_k})$, so each summand of the defining sum acquires the factor $\lambda^{-k}\cdot\lambda^{-k} = \lambda^{-2k}$ and $\langle\omega,\eta\rangle' = \lambda^{-2k}\langle\omega,\eta\rangle$. In top degree, $\mathrm{vol}' = (\lambda e_1^*)\wedge\dots\wedge(\lambda e_n^*) = \lambda^n\,e_1^*\wedge\dots\wedge e_n^* = \lambda^n\mathrm{vol}$.
>
> For $\alpha \in \Lambda^k V^*$ and any $\beta \in \Lambda^{n-k}V^*$, the defining relation of $\star'$ combined with these weights gives, since $\star'\alpha,\beta \in \Lambda^{n-k}V^*$,
> $$\alpha\wedge\beta = \langle\star'\alpha,\beta\rangle'\mathrm{vol}' = \lambda^{-2(n-k)}\langle\star'\alpha,\beta\rangle\,\lambda^n\mathrm{vol} = \lambda^{2k-n}\langle\star'\alpha,\beta\rangle\,\mathrm{vol},$$
> while the defining relation of $\star$ gives $\alpha\wedge\beta = \langle\star\alpha,\beta\rangle\mathrm{vol}$. Cancelling $\mathrm{vol}$ and using that $\langle\cdot,\cdot\rangle$ is non-degenerate on $\Lambda^{n-k}V^*$ yields $\star\alpha = \lambda^{2k-n}\star'\alpha$, i.e. $\star' = \lambda^{n-2k}\star$ on $\Lambda^k V^*$. Setting $n = 4$, $k = 2$ gives $\star' = \lambda^0\star = \star$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: reading the weight off the double-star formula
> One might try to fix the exponent by demanding consistency with $\star\star = (-1)^{k(n-k)+p}\,\mathrm{id}$: since that sign is a pure number, "the star must be conformally invariant in every degree". This is false. The double-star relation is invariant under conformal rescaling — $\star'\star' = \lambda^{(n-2(n-k))}\lambda^{(n-2k)}\star\star = \lambda^{(2k-n)+(n-2k)}\star\star = \star\star$, because the star acts successively on $\Lambda^k$ and then on $\Lambda^{n-k}$, and the two weights $\lambda^{n-2k}$ and $\lambda^{n-2(n-k)} = \lambda^{2k-n}$ are reciprocals — but $\star$ itself scales by $\lambda^{n-2k}$, which is $1$ only when $2k = n$. The invariance of $\star\star$ is compatible with the non-invariance of $\star$ precisely because the composite runs through complementary degrees whose weights cancel. The extra condition that makes "$\star$ is conformally invariant" legitimate is exactly $2k = n$: middle degree in even dimension.

> [!note]- Independent check in low dimensions
> Two cheap verifications of $\star' = \lambda^{n-2k}\star$. (i) Euclidean line, $n = 1$, $k = 0$: here $\star f = f\,\mathrm{vol}$ for a scalar $f \in \Lambda^0$, and $\star'f = f\,\mathrm{vol}' = f\lambda\,\mathrm{vol} = \lambda\,\star f$, so the weight is $\lambda^1 = \lambda^{n-2k}$ with $n-2k = 1-0 = 1$. (ii) Euclidean $\mathbb{R}^3$, $n = 3$, $k = 1$: $\star\,dx = dy\wedge dz$, and testing $\star'\,dx = c\,dy\wedge dz$ against $\beta = dy\wedge dz$ in the defining relation gives $dx\wedge dy\wedge dz = \langle c\,dy\wedge dz, dy\wedge dz\rangle'\mathrm{vol}'$, i.e. $\mathrm{vol} = c\lambda^{-4}\cdot\lambda^3\mathrm{vol} = c\lambda^{-1}\mathrm{vol}$, so $c = \lambda$; thus $\star'\,dx = \lambda\,dy\wedge dz = \lambda\,\star\,dx$, matching $\lambda^{n-2k} = \lambda^{3-2} = \lambda$. Both confirm the exponent $n-2k$, and both would fail for the naive $\lambda^{2k-n}$ (which predicts $\lambda^{-1}$ in each case).

---

# Key Takeaways

**A geometric object built functorially from a metric has a well-defined conformal weight, and the fastest way to find it is to rescale a single orthonormal basis and count powers.** The entire family — induced inner products, volume form, Hodge star — inherits its scaling from the one fact $e_i \mapsto \lambda^{-1}e_i$, $e_i^* \mapsto \lambda e_i^*$. The trigger for this technique is any question of the form "how does [metric-built object] change under $g \mapsto \lambda^2 g$"; the transferable move is to write the object in an orthonormal basis, replace the basis by its rescaled version, and read the weight off as a power of $\lambda$. The weights compose additively in the exponent: an inner product on $\Lambda^k$ carries $\lambda^{-2k}$, the volume form carries $\lambda^n$, and any object defined by an equation involving them inherits the algebraic sum of their exponents. This is the same accounting that gives Sobolev exponents their conformal weights and that underlies the whole apparatus of conformal geometry, where one systematically classifies tensors by how they transform under $g \mapsto e^{2f}g$.

**The middle degree in even dimension is the unique conformally invariant slot for the Hodge star, and this single algebraic fact carries a great deal of physics.** The exponent $n - 2k$ vanishes exactly when $2k = n$; in dimension four this is $k = 2$, the degree of the electromagnetic and Yang–Mills field strengths. Consequently the star acting on curvature $2$-forms in four dimensions does not see a conformal rescaling of the metric, so the action $\tfrac12\int F\wedge\star F$ is conformally invariant, the self-duality condition $\star F = F$ is conformally invariant, and the notions of self-dual and anti-self-dual $2$-forms — and hence instantons — depend on the metric only through its conformal class. The diagnostic to carry away: whenever a variational or duality condition is written with a Hodge star on middle-degree forms in even dimension, suspect conformal invariance, and confirm it by checking that the relevant exponent $n - 2k$ is zero. When it is not zero, the same computation tells you precisely the power of $\lambda$ that breaks the invariance.

**Exponent signs in scaling laws are only meaningful once the degree the operator acts on is pinned down, and comparing two sources demands re-indexing before comparing.** The apparent conflict between the weight $\lambda^{n-2k}$ derived here and Bär's displayed $\lambda^{2k-n}$ dissolves once one notices that his exponent is indexed by the degree of the *paired* form, not the degree the star acts on; the substitution $k \mapsto n-k$ turns one into the other. This is a recurring hazard: two references can write "the same" scaling law with opposite-looking exponents purely because of a silent choice of which slot indexes the formula. The habit worth internalising is to state such laws with the acting degree explicit ("$\star'$ on $\Lambda^k$ is $\lambda^{n-2k}\star$"), to sanity-check the sign against a trivial case ($k = 0$, where $\star$ is multiplication by the volume form and must scale like $\mathrm{vol}$, i.e. by $\lambda^n = \lambda^{n-2\cdot 0}$), and only then to compare with a source. The companion sign drills are [[Ex - Double Star Sign in Arbitrary Signature]] and [[Ex - The Hodge Star is an Isometry up to the Sign of the Index]], and the physical payoff is developed on [[Thm - Conformal Invariance of the Electromagnetic Action and Tracelessness of the Energy-Momentum Tensor]].
