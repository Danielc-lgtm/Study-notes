---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Distribution on a Manifold"
  - "Def - Involutive Distribution"
  - "Def - Integral Manifold of a Distribution"
  - "Def - Integrable Distribution"
  - "Def - The Lie Bracket of Vector Fields"
  - "Def - Flow of a Vector Field"
tags: [geometry, differential-geometry, frobenius]
---

# Notation

$M$ is a smooth $n$-manifold; $D$ is a smooth distribution of rank $k$ on $M$ — see [[Def - Distribution on a Manifold]]. $\Gamma(D)$ is the space of smooth (local or global) sections of $D$. $D$ is **involutive** if $\Gamma(D)$ is closed under the Lie bracket — see [[Def - Involutive Distribution]]. A **flat chart** for $D$ is a coordinate chart $(U, \varphi)$ with $\varphi(U)$ a cube in $\mathbb{R}^n$ such that $D = \mathrm{span}(\partial_1, \dots, \partial_k)$ on $U$. The notation $[X, Y]$ denotes the [[Def - The Lie Bracket of Vector Fields|Lie bracket]].

---

# Statement

> **Theorem (Frobenius — vector field version).** Let $M$ be a smooth $n$-manifold and $D$ a smooth distribution of rank $k$ on $M$. The following three conditions are equivalent:
>
> (a) $D$ is **involutive**: $[X, Y] \in \Gamma(D)$ for every pair of smooth local sections $X, Y \in \Gamma(D)$.
>
> (b) $D$ is **integrable**: every point of $M$ is contained in some integral manifold of $D$.
>
> (c) $D$ is **completely integrable**: every point has a neighborhood with a flat chart for $D$.

> **Corollary (existence of integral manifolds through every point).** If $D$ is involutive, then for every $p \in M$ there is a $k$-dimensional embedded submanifold $N_p$ through $p$ with $T_qN_p = D_q$ for every $q \in N_p$ — explicitly, the slice $\{x^{k+1} = c^{k+1}, \dots, x^n = c^n\}$ in any flat chart, with $c^{i} = x^{i}(p)$.

> **Corollary (Global Frobenius, see [[Def - Foliation]]).** If $D$ is involutive, then the collection of all maximal connected integral manifolds of $D$ forms a foliation of $M$.

The forms-language version is [[Thm - Frobenius Theorem in Forms Language]], stating the equivalent condition that the annihilating ideal $\mathcal{I}(D)$ is a differential ideal.

---

# Motivation

The question Frobenius answers is sharp: when does a rank-$k$ distribution admit integral submanifolds — $k$-dimensional submanifolds tangent to the distribution at every point? For rank $k = 1$ the answer is "always" by ODE theory; every nonvanishing vector field has integral curves through every point. For rank $k \geq 2$ the answer is "sometimes," and the question is to identify the exact condition.

The necessary condition is easy and is the easy half of the theorem. If $D$ has an integral manifold $N$ through $p$, and $X, Y \in \Gamma(D)$ are both tangent to $N$ along $N$, then their bracket $[X, Y]$ is tangent to $N$ along $N$ (this is `Corollary 8.32` in Lee — brackets of vector fields tangent to a submanifold remain tangent). Since this must hold for every $p$ (integrability is pointwise), $[X, Y] \in \Gamma(D)$ everywhere.

The sufficient direction is the deep content. Frobenius proves that closure under brackets is *enough* — bracket-closure forces the existence of integral manifolds, with the strongest form of regularity (flat charts) holding everywhere. This converts a local infinitesimal condition (bracket-closure of vector fields, checkable at each point) into a global geometric structure (a flat-chart structure, equivalently a foliation).

The conceptual content: *the algebraic condition $[\Gamma(D), \Gamma(D)] \subseteq \Gamma(D)$ is both necessary and sufficient for the geometric construction.* This is a recurring pattern in differential geometry — the [[Thm - The Inverse Function Theorem|inverse function theorem]] makes an algebraic condition (invertible derivative) sufficient for a geometric one (local diffeomorphism); the [[Thm - The Regular Value Theorem|regular value theorem]] makes a pointwise condition (surjectivity of differential) sufficient for a global submanifold structure on level sets. Frobenius is the higher-dimensional version of the same conceptual move.

The proof's main idea is also conceptually clean: an involutive distribution can be "straightened" by replacing its given local frame with a *commuting* frame, after which the [[Thm - Canonical Form for a Nonvanishing Vector Field|canonical-form theorem for commuting vector fields]] produces the flat chart. The construction of the commuting frame uses a coordinate projection to pull back the standard partial derivatives — once you have $k$ commuting fields whose flows mutually commute, you can compose their flows to parameterize integral manifolds explicitly.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is: *$D$ is an involutive smooth distribution.* The skill is recognizing involutivity in disguise.

The first disguised source is **a distribution given by spanning vector fields, with commuting (or known) Lie brackets.** Property $B$: $D = \mathrm{span}(X_1, \dots, X_k)$ where the brackets $[X_i, X_j]$ can be computed and lie in $\mathrm{span}(X_1, \dots, X_k)$ — at the easy extreme, $[X_i, X_j] = 0$ for all pairs (a commuting frame). The bridge: if all pairwise brackets are sections of $D$, by the [[Def - Involutive Distribution|local-frame criterion]] $D$ is involutive. *Example application:* the kernel of a submersion has a commuting frame in slice coordinates, hence is involutive.

The second disguised source is **a distribution defined as the kernel of a Lie algebra action.** Property $B$: a Lie algebra $\mathfrak{g}$ acts on $M$ by fundamental vector fields, with the orbit distribution $D_p = \{X^*_p : X \in \mathfrak{g}\}$. The bridge: the action being a Lie algebra homomorphism gives $[X^*, Y^*] = -[X, Y]^*$, so brackets remain in the orbit distribution. *Example:* the orbit distribution of a Lie group action is involutive, and the leaves of the resulting foliation are the orbits.

The third disguised source is **an overdetermined first-order PDE system whose compatibility conditions hold.** Property $B$: a system $\partial u/\partial x^i = \alpha^i(x, u)$ with the mixed-partial conditions $\partial_j\alpha^i + \alpha^j\partial_u\alpha^i = \partial_i\alpha^j + \alpha^i\partial_u\alpha^j$ holding identically. The bridge: these compatibility conditions are exactly $[\partial_{x^i} + \alpha^i\partial_u, \partial_{x^j} + \alpha^j\partial_u] = 0$, i.e. the spanning frame of the associated distribution is commuting (in particular, involutive). *Example:* a PDE compatibility theorem is a Frobenius application. See [[Ex - Frobenius Theorem Applied to an Overdetermined PDE]].

**Targets (Output Amplification)**

The conclusion $C$: *$D$ is completely integrable — a flat chart exists through every point.*

Combine $C$ with **the canonical form theorem for commuting vector fields.** The proof of Frobenius actually constructs the flat chart via this canonical form, applied to a *commuting* re-framing of $D$. The further result $E$: integral manifolds are explicitly the slices of the flat chart, parametrized by composing flows of the commuting frame fields. The non-obviousness: the flow-based construction gives an *explicit* parameterization, not just existence.

Combine $C$ with **a transverse submanifold $S$.** If $S \subseteq M$ is a codimension-$k$ embedded submanifold with $T_pS$ complementary to $D_p$ at every $p \in S$, then by Corollary 19.13 in Lee, there is a flat chart for $D$ in which $S \cap U$ is the slice $\{x^1 = \cdots = x^k = 0\}$. The further result $E$: through every point of $S$, the integral manifold of $D$ meeting $S$ transversally is uniquely determined. This is the input to the **Cauchy problem** for involutive distributions: prescribe data on $S$, propagate by leaves.

Combine $C$ with **the global Frobenius theorem.** Putting together the local flat-chart structure across all of $M$ gives a partition of $M$ into maximal connected integral manifolds — a foliation. The further result $E$: the cardinality of leaves, their topology, and their fitting-together properties become a global invariant of $D$ — the *foliation structure*.

---

# Why Is It True

**The single sentence: involutivity prevents the flow box from being twisted; integral submanifolds glue together when local pieces close under brackets.**

The picture starts from rank-$1$. A nonvanishing vector field $X$ on $M$ has integral curves $\gamma : J \to M$ — solutions to $\dot\gamma = X_\gamma$ — by ODE theory. The [[Thm - Canonical Form for a Nonvanishing Vector Field|canonical-form theorem]] then produces coordinates $(x^1, \dots, x^n)$ in which $X = \partial/\partial x^1$, so the integral curves are the coordinate lines, parametrized by $x^1$. The other coordinates $x^2, \dots, x^n$ label *which* integral curve.

For rank $k = 2$, we have two vector fields $X_1, X_2$ spanning $D$. The natural attempt is to look at "two-dimensional flow boxes" — parameterize a small disk by $(t_1, t_2) \mapsto \phi^{X_1}_{t_1}\phi^{X_2}_{t_2}(p)$, flowing first along $X_2$ for time $t_2$, then along $X_1$ for time $t_1$. If the two flows *commute* — equivalently, $[X_1, X_2] = 0$ — this gives a well-defined $2$-dimensional parameterization, and the image is an integral surface.

But if $[X_1, X_2] \neq 0$, the flows do *not* commute, and the order of operations matters: $\phi^{X_1}_{t_1}\phi^{X_2}_{t_2}(p) \neq \phi^{X_2}_{t_2}\phi^{X_1}_{t_1}(p)$. The difference at second order is $t_1 t_2 [X_1, X_2]$. If $[X_1, X_2]$ is *in* $D$, this discrepancy stays *tangent to the would-be integral surface*, and the surface can still be constructed (with a more careful parameterization). If $[X_1, X_2]$ is *out* of $D$, the discrepancy escapes — there is no $2$-dimensional integral surface, because the flow box has nowhere to close up.

This is the geometric content of involutivity: it is the condition that flow-box discrepancies *stay in* $D$, so local integral pieces can be glued.

The actual proof transforms this picture into an algebraic strategy. Given an involutive $D$ of rank $k$ with frame $X_1, \dots, X_k$, the proof constructs a new local frame $V_1, \dots, V_k$ that *commutes* — $[V_i, V_j] = 0$ for all pairs. With a commuting frame in hand, the canonical-form theorem for commuting vector fields produces the flat chart, and the integral manifolds are the slices.

The construction of the commuting frame is the heart of the proof. Choose local coordinates $(x^1, \dots, x^n)$ at $p$ such that $D_p$ is complementary to $\mathrm{span}(\partial_{k+1}, \dots, \partial_n)$ at $p$. Define the **coordinate projection** $\pi : U \to \mathbb{R}^k$, $\pi(x^1, \dots, x^n) = (x^1, \dots, x^k)$. Then $d\pi|_{D_q}$ is an isomorphism from $D_q$ to $\mathbb{R}^k$ at $p$ — and, by continuity, at every $q$ in a neighborhood of $p$. So we can *pull back* the standard frame $\partial_1, \dots, \partial_k$ of $\mathbb{R}^k$ via $(d\pi|_D)^{-1}$ to get a frame for $D$ near $p$:

$$V_i|_q := (d\pi|_{D_q})^{-1}\left(\frac{\partial}{\partial x^i}\big|_{\pi(q)}\right).$$

By construction, $V_i$ is $\pi$-related to $\partial_i$ on $\mathbb{R}^k$. Now: $\pi$-related fields have $\pi$-related brackets, so $[V_i, V_j]$ is $\pi$-related to $[\partial_i, \partial_j] = 0$, i.e. $d\pi([V_i, V_j]) = 0$. But $d\pi$ is *injective* on $D$ (it's an isomorphism), so if $[V_i, V_j]$ is in $D$ and projects to zero, then $[V_i, V_j] = 0$.

This is exactly where involutivity enters: we need $[V_i, V_j] \in D$ to apply the injectivity argument. Involutivity gives us this for free, and the conclusion is $[V_i, V_j] = 0$ — a commuting frame.

Once we have a commuting frame, the canonical-form theorem produces the flat chart, and the proof concludes.

---

# What Makes This Hard

The conceptual obstacle is recognizing that **the bracket condition is exactly what stops "flow-box leakage" out of $D$** — the geometric picture of involutivity as "flows stay in the distribution" is the right intuition, but it takes work to translate into the algebraic proof. The non-obvious step is the **coordinate-projection construction of the commuting frame**: pulling back $\partial_1, \dots, \partial_k$ from $\mathbb{R}^k$ via $(d\pi|_D)^{-1}$ produces fields in $D$ that, by $\pi$-relatedness and involutivity, must commute. People often miss the involutivity-injectivity-zero chain at the end, which is the place where the hypothesis enters. The most common error is to try to prove the theorem by direct integration of the spanning fields without first re-engineering to a commuting frame.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Reduce involutivity to a commuting frame via a coordinate-projection construction; apply the canonical-form theorem for commuting vector fields to produce the flat chart; the integral manifolds are the slices.

**Subgoal decomposition:**

1. **Easy direction: integrable $\Longrightarrow$ involutive.** If $D$ has an integral manifold through every point, sections of $D$ are tangent to the integral manifold, so their brackets are tangent (by Corollary 8.32 in Lee — brackets of vector fields tangent to a submanifold remain tangent). Hence brackets are in $D$.
   - *Hint:* Restrict to a single integral manifold $N$; sections of $D$ restricted to $N$ are vector fields on $N$, and the bracket on $M$ restricted to $N$ equals the bracket on $N$.
   - *Why needed:* This is the necessary direction.

2. **Set up the coordinate projection.** Choose local coordinates $(x^1, \dots, x^n)$ at $p$ such that $D_p$ is complementary to $\mathrm{span}(\partial_{k+1}|_p, \dots, \partial_n|_p)$. The projection $\pi : U \to \mathbb{R}^k$, $\pi(x) = (x^1, \dots, x^k)$, has $d\pi|_{D_p}$ a linear isomorphism.
   - *Hint:* "Complementary" means $D_p \oplus \mathrm{span}(\partial_{k+1}, \dots, \partial_n) = T_pM$; this is achievable by reordering coordinates if necessary.
   - *Why needed:* The projection is the device that re-frames $D$ via a commuting frame.

3. **Construct the commuting frame.** Define $V_i = (d\pi|_D)^{-1}(\partial_i)$ for $i = 1, \dots, k$. By continuity $d\pi|_{D_q}$ is an isomorphism on a neighborhood of $p$, so $V_i$ is a smooth frame for $D$ on that neighborhood.
   - *Hint:* The pullback by $(d\pi|_D)^{-1}$ is the unique vector in $D_q$ that projects to $\partial_i|_{\pi(q)}$ under $d\pi$.
   - *Why needed:* This is the candidate commuting frame.

4. **Prove the frame commutes — the involutivity step.** Use that $V_i$ is $\pi$-related to $\partial_i$ on $\mathbb{R}^k$. Brackets of $\pi$-related fields are $\pi$-related, so $[V_i, V_j]$ is $\pi$-related to $[\partial_i, \partial_j] = 0$ — i.e. $d\pi([V_i, V_j]) = 0$. By involutivity, $[V_i, V_j] \in D$. Since $d\pi$ is injective on $D$, $[V_i, V_j] = 0$.
   - *Hint:* The injectivity of $d\pi|_D$ is what converts "projects to zero" into "is zero" for vectors in $D$.
   - *Why needed:* This is the crucial step where involutivity is used; without it the bracket could escape $D$ and not be zero.

5. **Apply the canonical-form theorem for commuting vector fields.** By [[Thm - Commuting Flows Theorem|the commuting-flows theorem]] (Theorem 9.46 in Lee), the existence of a commuting frame $V_1, \dots, V_k$ for $D$ near $p$ produces coordinates $(y^1, \dots, y^n)$ in which $V_i = \partial/\partial y^i$.
   - *Hint:* Compose the flows $\phi^{V_1}_{t_1} \circ \cdots \circ \phi^{V_k}_{t_k}$ starting from a transversal slice; commutativity makes the order irrelevant.
   - *Why needed:* This gives the flat chart for $D$.

6. **Conclude.** In the new coordinates, $D = \mathrm{span}(\partial_1, \dots, \partial_k)$, so the chart is flat for $D$ — slices $\{y^{k+1} = c^{k+1}, \dots, y^n = c^n\}$ are integral manifolds. The chart exists through every point; hence $D$ is completely integrable.
   - *Hint:* By construction $V_i = \partial_{y^i}$ are the spanning fields for $D$.
   - *Why needed:* This is the conclusion: completely integrable.

---

# Lemma Decomposition

> [!note]- Lemma 1: Easy direction — integral manifolds force involutivity
> **Statement:** Let $D$ be a smooth distribution on $M$. If $D$ has an integral manifold through every point, then $D$ is involutive.
>
> **Hint:** Sections of $D$ restricted to an integral manifold are vector fields on the integral manifold; brackets restrict consistently.
>
> **Why needed:** This is the necessary direction of Frobenius — already gives "integrable $\Longrightarrow$ involutive."
>
> > [!note]- Full proof
> > Let $X, Y \in \Gamma(D)$ be smooth local sections on an open set $U$. Let $p \in U$, and let $N$ be an integral manifold of $D$ containing $p$. Then for every $q \in N \cap U$, $X_q, Y_q \in D_q = T_qN$. So $X$ and $Y$ restrict to vector fields tangent to $N$ at every point of $N \cap U$. By Lee's Corollary 8.32 (brackets of vector fields tangent to a submanifold are tangent to the submanifold), $[X, Y]_q \in T_qN = D_q$ for $q \in N \cap U$. In particular $[X, Y]_p \in D_p$. Since $p$ was arbitrary, $[X, Y]_p \in D_p$ on all of $U$, so $[X, Y] \in \Gamma(D)$. Hence $D$ is involutive.

> [!note]- Lemma 2: $\pi$-related fields have $\pi$-related brackets
> **Statement:** Let $\pi : M \to N$ be a smooth map and let $X_1, X_2$ on $M$ be $\pi$-related to $Y_1, Y_2$ on $N$ (i.e. $d\pi_p(X_i|_p) = Y_i|_{\pi(p)}$ for every $p$). Then $[X_1, X_2]$ is $\pi$-related to $[Y_1, Y_2]$.
>
> **Hint:** This is the standard naturality of the Lie bracket under smooth maps — see [[Thm - Lie Bracket Properties]] or Proposition 8.30 in Lee.
>
> **Why needed:** This is the lemma that lets us conclude $[V_i, V_j]$ projects to $[\partial_i, \partial_j] = 0$ under $d\pi$.
>
> > [!note]- Full proof
> > See [[Thm - Lie Bracket Properties]] (Proposition 8.30 in Lee). The proof: for any smooth $f$ on $N$, $X_i(\pi^* f) = (\pi^*Y_i f)$ by $\pi$-relatedness applied to the directional derivative. Then $[X_1, X_2](\pi^*f) = X_1 X_2 (\pi^*f) - X_2 X_1(\pi^*f) = X_1(\pi^*(Y_2 f)) - X_2(\pi^*(Y_1 f)) = \pi^*(Y_1 Y_2 f) - \pi^*(Y_2 Y_1 f) = \pi^*([Y_1, Y_2]f)$. Hence $d\pi([X_1, X_2]) = [Y_1, Y_2] \circ \pi$, the $\pi$-relatedness.

> [!note]- Lemma 3: The coordinate projection produces a commuting frame
> **Statement:** Let $D$ be a smooth involutive distribution of rank $k$ on $\mathbb{R}^n$ near $0$, and assume $D_0$ is complementary to $\mathrm{span}(\partial_{k+1}|_0, \dots, \partial_n|_0)$. Let $\pi : \mathbb{R}^n \to \mathbb{R}^k$ be the projection $(x^1, \dots, x^n) \mapsto (x^1, \dots, x^k)$. Then there is a smooth local frame $V_1, \dots, V_k$ for $D$ near $0$ such that each $V_i$ is $\pi$-related to $\partial_i$ on $\mathbb{R}^k$, and $[V_i, V_j] = 0$.
>
> **Hint:** Define $V_i|_q$ to be the unique vector in $D_q$ such that $d\pi_q(V_i|_q) = \partial_i|_{\pi(q)}$; this is well-defined because $d\pi|_{D_q}$ is an isomorphism near $0$. Use Lemma 2 and involutivity.
>
> **Why needed:** This is the core construction of the proof — a commuting frame from an arbitrary involutive frame.
>
> > [!note]- Full proof
> > By assumption $d\pi_0|_{D_0}$ is a linear isomorphism $D_0 \to T_0\mathbb{R}^k$ (both are $k$-dimensional, and $D_0$ is complementary to $\ker d\pi_0$). By continuity of the smooth distribution $D$ and the smooth map $\pi$, $d\pi_q|_{D_q}$ is an isomorphism on a neighborhood of $0$.
> >
> > On this neighborhood, define $V_i|_q = (d\pi_q|_{D_q})^{-1}(\partial_i|_{\pi(q)})$. The $V_i$ are smooth vector fields (the inverse of a smoothly varying isomorphism is smooth), and they span $D$ by construction.
> >
> > By construction, $d\pi_q(V_i|_q) = \partial_i|_{\pi(q)}$, so $V_i$ is $\pi$-related to $\partial_i$. By Lemma 2, $[V_i, V_j]$ is $\pi$-related to $[\partial_i, \partial_j] = 0$. So $d\pi_q([V_i, V_j]|_q) = 0$ at every $q$.
> >
> > By involutivity of $D$, $[V_i, V_j]_q \in D_q$. So $[V_i, V_j]_q$ is in $D_q$ and is in $\ker(d\pi_q)$. But $d\pi_q$ is injective on $D_q$ (it is an isomorphism). So $[V_i, V_j]_q = 0$ at every $q$. Hence $[V_i, V_j] = 0$.

> [!note]- Lemma 4: Commuting vector fields admit a flat chart
> **Statement:** Let $V_1, \dots, V_k$ be smooth vector fields on $M$ in a neighborhood of $p$, linearly independent at $p$, and commuting ($[V_i, V_j] = 0$). Then there exist smooth coordinates $(y^1, \dots, y^n)$ near $p$ in which $V_i = \partial/\partial y^i$ for $i = 1, \dots, k$.
>
> **Hint:** This is the [[Thm - Commuting Flows Theorem|commuting-flows theorem]] of `Differential Geometry V` (Theorem 9.46 in Lee). The construction is to flow along the $V_i$'s starting from a transversal slice; commutativity makes the result independent of flow order.
>
> **Why needed:** This is the canonical form for commuting vector fields, which converts the commuting-frame construction into a flat chart for $D$.
>
> > [!note]- Full proof
> > Choose smooth coordinates $(x^1, \dots, x^n)$ at $p$ such that $V_i|_p$ for $i = 1, \dots, k$ together with $\partial_{k+1}|_p, \dots, \partial_n|_p$ form a basis of $T_pM$. Let $S = \{x \in U : x^1 = \cdots = x^k = 0\}$ be the corresponding $(n-k)$-dimensional transversal slice.
> >
> > Define $\Phi : U' \subseteq \mathbb{R}^k \times S \to M$ by $\Phi(t_1, \dots, t_k, q) = \phi^{V_1}_{t_1}\phi^{V_2}_{t_2}\cdots\phi^{V_k}_{t_k}(q)$, where $\phi^{V_i}_{t}$ is the flow of $V_i$. Because $[V_i, V_j] = 0$, the flows commute by the commuting-flows theorem, so the order of composition does not matter, and $\Phi$ is smooth and well-defined on a neighborhood of $0$ in $\mathbb{R}^k \times S$.
> >
> > $d\Phi$ at $(0, \dots, 0, p)$ sends $\partial_{t_i}$ to $V_i|_p$ and $T_pS$ to itself, so $d\Phi$ is invertible at the basepoint. By [[Thm - The Inverse Function Theorem|inverse function theorem]], $\Phi$ is a local diffeomorphism. Use $(t_1, \dots, t_k, \text{coordinates on } S)$ as the new coordinate system $(y^1, \dots, y^n)$. In these coordinates, flowing along $V_i$ corresponds to incrementing $t_i$ alone, so $V_i = \partial/\partial y^i$.

---

# Formal Proof

> [!note]- Complete formal proof
> We prove (a) $\Longleftrightarrow$ (c). The easy direction (c) $\Longrightarrow$ (a) follows because in a flat chart, $D$ is spanned by $\partial_1, \dots, \partial_k$, which commute trivially. The direction (a) $\Longrightarrow$ (b) is given by Lemma 1 in reverse: if every point has a flat chart, the slice through that point is an explicit integral manifold. And (b) $\Longrightarrow$ (a) is Lemma 1.
>
> So we prove the deep direction: (a) involutivity $\Longrightarrow$ (c) complete integrability.
>
> Let $p \in M$ and pass to local coordinates in which $M$ is replaced by an open neighborhood of $0$ in $\mathbb{R}^n$. By reordering coordinates, we may assume $D_0$ is complementary to $\mathrm{span}(\partial_{k+1}|_0, \dots, \partial_n|_0)$.
>
> **Step 1 — Coordinate projection.** Let $\pi : \mathbb{R}^n \to \mathbb{R}^k$ be the projection onto the first $k$ coordinates.
>
> **Step 2 — Commuting frame construction.** By Lemma 3, there is a smooth local frame $V_1, \dots, V_k$ for $D$ near $0$ such that each $V_i$ is $\pi$-related to $\partial_i$ on $\mathbb{R}^k$, and $[V_i, V_j] = 0$ for all $i, j$.
>
> **Step 3 — Flat chart from commuting frame.** By Lemma 4, the commuting frame $V_1, \dots, V_k$ admits smooth local coordinates $(y^1, \dots, y^n)$ in which $V_i = \partial/\partial y^i$ for $i = 1, \dots, k$. Hence in these coordinates, $D = \mathrm{span}(V_1, \dots, V_k) = \mathrm{span}(\partial/\partial y^1, \dots, \partial/\partial y^k)$.
>
> The coordinates $(y^1, \dots, y^n)$ form a flat chart for $D$ at $p$. Since $p$ was arbitrary, $D$ has a flat chart through every point — that is, $D$ is completely integrable. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Existence of solutions to overdetermined PDEs.** A system $\partial u/\partial x^i = \alpha^i(x, u)$ for $i = 1, \dots, n$ has a solution iff the associated distribution on $\mathbb{R}^{n+1}$ spanned by $X_i = \partial_{x^i} + \alpha^i\partial_u$ is involutive — equivalently, iff $[X_i, X_j] = 0$ for all $i, j$. The Frobenius theorem then constructs the integral manifold (the graph of the solution). This is the foundational existence theorem for first-order overdetermined PDE.

**Lie subalgebras and Lie subgroups.** Lee's Theorem 19.26: every Lie subalgebra $\mathfrak{h}$ of $\mathrm{Lie}(G)$ corresponds to a unique connected Lie subgroup of $G$. The proof uses Frobenius: the left-invariant distribution $D_g = \{X_g : X \in \mathfrak{h}\}$ on $G$ is involutive (because $\mathfrak{h}$ is a Lie subalgebra), so by Frobenius it has a foliation; the leaf through the identity is the desired Lie subgroup.

**Holonomic vs nonholonomic constraints.** In classical mechanics, a velocity constraint distribution $D \subseteq TQ$ on configuration space $Q$ is **holonomic** (comes from a submanifold constraint) iff $D$ is involutive — by Frobenius. The skate on ice, the rolling ball, and parallel-parking constraints are non-involutive distributions whose lack of integrability is *exactly* the geometric meaning of "non-holonomic." See [[Ex - A Non-Integrable Distribution on R^3 from the Standard Contact Form]].

**Integrability of complex structures (Newlander–Nirenberg).** An almost complex structure on a smooth manifold is a fiber-wise endomorphism $J : TM \to TM$ with $J^2 = -\mathrm{id}$; it is **integrable** (comes from a true complex manifold structure) iff a certain tensor — the **Nijenhuis tensor** — vanishes. The Newlander–Nirenberg theorem is the integrability theorem, and it can be viewed as a Frobenius theorem for the complexified distribution $T^{0,1}M \subseteq T^\mathbb{C}M$ — involutivity of $T^{0,1}M$ under the complex bracket equals vanishing Nijenhuis tensor equals integrability.

---

# Bridges

- **[[Thm - Existence and Uniqueness of Integral Curves|Existence and Uniqueness of Integral Curves]]** *(from `Differential Geometry V`)* — the rank-$1$ case of Frobenius. Every nonvanishing vector field has integral curves through every point; the bracket condition is vacuous at rank $1$, so the theorem is just ODE theory. Frobenius generalizes from $1$D to arbitrary rank, with the bracket condition replacing the vacuous one.

- **[[Thm - Commuting Flows Theorem|Commuting Flows Theorem]]** *(from `Differential Geometry V`)* — the canonical-form theorem for commuting vector fields, which is the key technical lemma in the Frobenius proof. The commuting-flows theorem produces a flat chart for any commuting frame, and Frobenius reduces involutivity to commutativity via the coordinate-projection construction.

- **[[Thm - Canonical Form for a Nonvanishing Vector Field|Canonical Form for a Nonvanishing Vector Field]]** *(from `Differential Geometry V`)* — the special case "single vector field." It produces coordinates in which $X = \partial_1$. Frobenius is the higher-rank generalization, with the new condition being involutivity (vacuous at rank $1$).

- **[[Thm - Frobenius Theorem in Forms Language|Frobenius Theorem in Forms Language]]** — the dual statement using annihilating $1$-forms instead of spanning vector fields. Involutivity of $D$ corresponds to differential-ideal closure of the annihilating ideal $\mathcal{I}(D)$. The forms version is often the most computable in practice — for codimension-$1$ distributions defined by a single $1$-form $\omega$, the criterion is just $\omega \wedge d\omega = 0$.

- **The de Rham theorem and integrability via cohomology** — although Frobenius itself does not directly use cohomology, there is a deep analogy: closedness ($d\omega = 0$) is the "infinitesimal" obstruction-free condition, and exactness is the "global" integration condition. Frobenius's involutivity is the analogous infinitesimal condition for distributions, and integrability is the global integration condition. Both theorems convert local algebra into global geometry.

- **Bracket-generating distributions and the Chow–Rashevskii theorem** — the *opposite* of Frobenius: a distribution is **bracket-generating** if iterating brackets eventually spans all of $TM$. The Chow–Rashevskii theorem says a bracket-generating distribution on a connected manifold is *globally controllable* — any two points can be connected by a path tangent to $D$. The non-involutive standard contact distribution on $\mathbb{R}^3$ is bracket-generating, which is why a parallel-parking maneuver can reach any configuration despite the local constraint.

---

# Unlocked by This

> [!tip] **Global Frobenius theorem and foliations** *(from this same topic)*
> The local flat-chart structure patches into a global foliation: an involutive distribution on $M$ gives a partition of $M$ into maximal connected integral submanifolds — the leaves. The global theorem (Lee Theorem 19.21) is a topological construction on top of the local Frobenius, giving foliations as the global structure dual to involutive distributions.

> [!tip] **Lie subgroup associated to a Lie subalgebra** *(from `Differential Geometry XI`)*
> Frobenius's central application in Lie theory: every Lie subalgebra $\mathfrak{h}$ of $\mathrm{Lie}(G)$ integrates to a unique connected Lie subgroup of $G$. The proof builds the left-invariant distribution $D_g = \{X_g : X \in \mathfrak{h}\}$, applies Frobenius to foliate $G$, and takes the leaf through the identity.

> [!tip] **Cartan's structure equations and connections** *(from Gauge Theory and Riemannian Geometry)*
> A **connection** on a principal bundle is a horizontal distribution complementary to the vertical bundle. Its **curvature** is the obstruction to involutivity — concretely, the vertical component of the bracket of horizontal fields. When curvature vanishes (flat connection), Frobenius gives a foliation by horizontal leaves, and the connection is locally trivial. Curvature is the "non-involutivity" of the horizontal distribution.

> [!tip] **Newlander–Nirenberg theorem** *(from Complex Geometry)*
> An almost complex structure $J$ on a manifold is integrable iff the Nijenhuis tensor vanishes, iff the complexified distribution $T^{0,1}M$ is involutive (under the complex bracket). This is a deep theorem (significantly harder than smooth Frobenius — uses elliptic PDE on $\bar\partial$), but the *form* of the theorem — algebraic condition equals geometric integrability — is the same Frobenius pattern.

> [!tip] **Cartan–Kähler theorem and exterior differential systems** *(from PDE and Symbol Calculus)*
> The most general integrability theorem for overdetermined PDE systems: the **Cartan–Kähler theorem** for **exterior differential systems** — ideals in the form algebra. The integrability condition is a more refined "Cartan's test" generalizing Frobenius's involutivity, and the theorem applies to non-linear PDE of arbitrary order. Every classical existence theorem for first-order systems (Frobenius), second-order (Darboux for Pfaffian systems), and Cauchy problems can be uniformly viewed via the Cartan–Kähler machinery.
