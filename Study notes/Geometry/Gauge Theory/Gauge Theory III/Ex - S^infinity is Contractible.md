---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Classifying Bundle and Classifying Map"
  - "Def - Homotopy"
  - "Def - Homotopy Equivalence and Contractible Space"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory, topology]
---

# Problem Statement

Let
$$S^\infty := \varinjlim_{n} S^{2n-1}, \qquad S^{2n-1} = \Big\{ (z_0, \dots, z_{n-1}) \in \mathbb{C}^n : \sum_{k=0}^{n-1} |z_k|^2 = 1 \Big\},$$
be the infinite-dimensional sphere, formed as the direct limit (colimit) of the chain of $U(1)$-equivariant inclusions
$$S^{2n-1} \hookrightarrow S^{2n+1}, \qquad (z_0, \dots, z_{n-1}) \longmapsto (z_0, \dots, z_{n-1}, 0),$$
and carrying the **direct-limit (weak) topology**: a subset $C \subseteq S^\infty$ is closed if and only if $C \cap S^{2n-1}$ is closed in $S^{2n-1}$ for every $n$. Concretely, a point of $S^\infty$ is a square-summable complex sequence $z = (z_0, z_1, \dots)$ with only finitely many nonzero entries and $\sum_k |z_k|^2 = 1$.

**Prove that $S^\infty$ is contractible**: the identity map $\mathrm{id}_{S^\infty}$ is homotopic to a constant map.

You are asked to produce the two homotopies explicitly and to verify that each is continuous *in the direct-limit topology*, which is the only delicate point:

1. a first homotopy $F$ from the identity to the **shift map** $T(z_0, z_1, z_2, \dots) = (0, z_0, z_1, z_2, \dots)$;
2. a second homotopy $G$ from the shift map $T$ to the **constant map** at the base point $e_0 = (1, 0, 0, \dots)$;

each given by a normalised straight-line formula, and the verification that both restrict to continuous maps on every finite stage $[0,1] \times S^{2n-1}$ and therefore, because $[0,1]$ is compact, define continuous maps on $[0,1] \times S^\infty$.

**Recall:**

The objects in play are the classifying bundle for $U(1)$ (of which $S^\infty$ is the total space), the notion of homotopy, contractibility, and the direct-limit topology.

![[Def - Classifying Bundle and Classifying Map#The Definition]]

A **classifying bundle** for a compact Lie group $G$ is a free $G$-space $E$ that is **contractible**; the quotient $B = E/G$ is then the classifying space and $E \to B$ carries every principal $G$-bundle back by pullback of a classifying map. For $G = U(1)$ the model is $S^\infty \to \mathbb{CP}^\infty$ with the scalar action $z \cdot \lambda = (z_0 \lambda, z_1 \lambda, \dots)$; the action is manifestly free, so the *one* nontrivial hypothesis to check is **contractibility of $S^\infty$**, which is exactly this exercise.

![[Def - Homotopy#The Definition]]

A **homotopy** between continuous maps $f_0, f_1\colon X \to Y$ is a continuous map $H\colon [0,1] \times X \to Y$ with $H(0, \cdot) = f_0$ and $H(1, \cdot) = f_1$; we write $H_t := H(t, \cdot)$ and $f_0 \simeq f_1$.

![[Def - Homotopy Equivalence and Contractible Space#The Definition]]

A space $X$ is **contractible** if it is homotopy equivalent to a one-point space; equivalently, the identity map $\mathrm{id}_X$ is homotopic to a constant map $x \mapsto x_0$ for some $x_0 \in X$. It is the latter formulation we verify: we build a homotopy from $\mathrm{id}_{S^\infty}$ to the constant map at $e_0$.

---

# Convergent Strategy

**Problem class.** This is a *contractibility* problem, and the obstruction it must dodge is dimension: no finite sphere $S^{2n-1}$ is contractible, so any honest contraction of $S^\infty$ has to use the room that the *infinite* direction provides. The recognisable move is the **Eilenberg swindle / infinite-shift trick**: in an infinite-dimensional sphere there is always "one more coordinate" into which a straight-line homotopy can push, and the segment from a point to its shift never passes through the origin because a vector and its shift have essentially disjoint support. The problem therefore splits into an algebraic part (write two homotopies whose straight-line numerators never vanish, so that normalising keeps us on the sphere) and a topological part (justify continuity for the colimit topology).

**Assumption pattern.** The hypothesis that does the work is the *direct-limit* structure: $S^\infty$ is the union of the $S^{2n-1}$ with the weak topology, and each inclusion raises the dimension by two. The trick uses this twice — the shift $T$ needs a spare coordinate to move into, and continuity is checked stage by stage. The recognisable trigger for "verify continuity on a colimit" is that the target formula, restricted to each finite stage, visibly lands in the *next* finite stage and is continuous there; continuity on the whole colimit then follows from a general point-set fact about products with a compact space.

**Theorem routing.** The route is: (i) define $F$ and $G$ by normalised linear interpolation and check the numerators are nowhere zero on $[0,1] \times S^\infty$ (an algebraic support argument), so the normalised maps are well defined and, on each finite stage, smooth; (ii) prove the point-set lemma that for compact $[0,1]$ and a colimit $S^\infty = \varinjlim S^{2n-1}$ of closed inclusions, $[0,1] \times S^\infty$ carries the colimit topology of the $[0,1] \times S^{2n-1}$, so a map continuous on each stage is continuous; (iii) concatenate $F$ and $G$ by the pasting lemma to get $\mathrm{id}_{S^\infty} \simeq \mathrm{const}_{e_0}$, using [[Def - Homotopy Equivalence and Contractible Space|the identity-nullhomotopic characterisation]] of contractibility.

**Key decision point.** Two choices decide the proof. First, *the shift as an intermediate stop*: one does not try to contract the identity to a constant in one linear homotopy — the straight segment from $z$ to $e_0$ can pass through the origin (take $z = -e_0$). Interposing the shift $T$ fixes this, because $z$ and $T z$ have disjoint support after the first coordinate, and $T z$ and $e_0$ are separated by the first coordinate. Second, *the decision to prove the compact-times-colimit lemma rather than wave at "continuity is obvious"*: this is the genuine content, since continuity on a colimit is not automatic from continuity on the pieces unless one knows that products with the compact interval preserve the colimit — which is what the tube-lemma argument establishes.

---

# Legal Operations Used

These are the operations of [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles#Legal Operations|the chapter's Legal Operations]] as they apply here (referred to descriptively, since the topic page's numbering is fixed when it is assembled).

1. **Interpolate linearly and normalise to stay on the sphere.** Replace a would-be map into the sphere by $(1-t)\,\square + t\,\square'$ divided by its norm; the operation is legal exactly on the region where the numerator does not vanish.

2. **Certify a straight segment avoids the origin by a support argument.** Show that the two endpoints of each segment have supports that cannot cancel, so no convex combination is zero; this licenses the normalisation.

3. **Use a spare coordinate provided by the infinite direction.** Push each point one coordinate along via the shift $T$, exploiting that $S^\infty$ always has an unused coordinate; this is what a finite sphere lacks.

4. **Check continuity stage by stage on a colimit.** Verify that each homotopy restricts, on $[0,1] \times S^{2n-1}$, to a continuous map into $S^{2n+1}$, compatibly with the inclusions.

5. **Promote stagewise continuity to the colimit using compactness of $[0,1]$.** Invoke the lemma that $[0,1] \times \varinjlim S^{2n-1} = \varinjlim([0,1] \times S^{2n-1})$, proved on the page via the tube lemma, to conclude the homotopies are continuous on $[0,1] \times S^\infty$.

6. **Concatenate homotopies by the pasting lemma.** Glue $F$ (on $[0, \tfrac12]$) and $G$ (on $[\tfrac12, 1]$) along $t = \tfrac12$, where both equal $T$, to obtain a single homotopy $\mathrm{id} \simeq \mathrm{const}$.

---

# Hints

> [!note]- Hint 1
> A finite sphere is not contractible, so the contraction must use the infinite direction. The base move: send each point $z$ to its **shift** $T z = (0, z_0, z_1, \dots)$, which lives in one higher coordinate. Why is the straight-line homotopy $t \mapsto (1-t) z + t\, T z$, once normalised, never forced through the origin?

> [!note]- Hint 2
> Look at the coordinates of $(1-t) z + t\, T z$: the $0$-th is $(1-t) z_0$, the $k$-th is $(1-t) z_k + t z_{k-1}$, and the last is $t z_{n-1}$. If this vanishes for some $t \in (0,1)$, deduce $z_0 = 0$, then $z_1 = 0$, and so on. What does that say about $z$?

> [!note]- Hint 3
> After reaching the shift $T$, contract $T z$ to the fixed base point $e_0 = (1,0,0,\dots)$ by $t \mapsto (1-t)\, T z + t\, e_0$. The $0$-th coordinate of this is exactly $t$ (because $T z$ has $0$-th coordinate zero). So for $t > 0$ the vector is nonzero, and at $t = 0$ it is $T z \neq 0$. Normalise. Now concatenate the two homotopies.

> [!note]- Hint 4
> For continuity: each homotopy, restricted to $[0,1] \times S^{2n-1}$, lands in $S^{2n+1}$ and is a normalised rational (hence smooth) map, continuous on that finite stage. To conclude continuity on $[0,1] \times S^\infty$ you need that $[0,1] \times S^\infty$ has the colimit topology of the $[0,1] \times S^{2n-1}$. This is *not* automatic for colimits, but holds because $[0,1]$ is compact — prove it with the tube lemma and the fact that each $[0,1] \times S^{2n-1}$ is a compact metric (hence normal) space.

---

# Solution

The idea is the infinite-shift trick. No finite sphere is contractible, so we exploit the one advantage $S^\infty$ has over each stage: an always-available extra coordinate. We slide the identity to the shift map $T$ along straight segments — which never cross the origin because a vector and its shift cannot cancel — then slide $T$ to the constant base point $e_0$ along straight segments, which never cross the origin because their first coordinate is forced to be positive. Normalising keeps everything on the sphere. The only real work is continuity in the direct-limit topology, which we secure by proving that products with the compact interval $[0,1]$ preserve the colimit.

Throughout, for $z = (z_0, z_1, \dots) \in S^\infty$ write $T z = (0, z_0, z_1, \dots)$ for the shift and $e_0 = (1, 0, 0, \dots)$ for the base point; $\|\cdot\|$ is the norm $\|z\|^2 = \sum_k |z_k|^2$, so $\|z\| = 1$ on $S^\infty$.

**Step 1: The two straight-line numerators never vanish.**

Set $N_F(t, z) = (1-t) z + t\, T z$ and $N_G(t, z) = (1-t)\, T z + t\, e_0$. Then $N_F(t, z) \neq 0$ and $N_G(t, z) \neq 0$ for every $t \in [0,1]$ and every $z \in S^\infty$.

> [!note]- Derivation
> **The homotopy toward the shift, $N_F$.** Fix $z \in S^{2n-1} \subset \mathbb{C}^n$ (so $z = (z_0, \dots, z_{n-1})$, remaining coordinates zero) and $t \in [0,1]$. In coordinates,
> $$N_F(t,z) = (1-t)(z_0, \dots, z_{n-1}, 0) + t (0, z_0, \dots, z_{n-1}) \in \mathbb{C}^{n+1},$$
> whose entries are
> $$\big(N_F\big)_0 = (1-t) z_0,\qquad \big(N_F\big)_k = (1-t) z_k + t z_{k-1}\ (1 \le k \le n-1),\qquad \big(N_F\big)_{n} = t\, z_{n-1}.$$
> - If $t = 0$, then $N_F(0, z) = z$, and $\|z\| = 1 \neq 0$.
> - If $t = 1$, then $N_F(1, z) = T z$, and $\|T z\| = \|z\| = 1 \neq 0$.
> - If $t \in (0,1)$, suppose for contradiction $N_F(t, z) = 0$. From $(N_F)_0 = (1-t) z_0 = 0$ and $1 - t \neq 0$ we get $z_0 = 0$. Inductively, if $z_0 = \dots = z_{k-1} = 0$ then $(N_F)_k = (1-t) z_k + t z_{k-1} = (1-t) z_k = 0$ forces $z_k = 0$. Running $k = 1, \dots, n-1$ gives $z = 0$, contradicting $\|z\| = 1$.
>
> Hence $N_F(t, z) \neq 0$ for all $t \in [0,1]$, $z \in S^\infty$. **The support argument in words:** $z$ occupies coordinates $0, \dots, n-1$ and $T z$ occupies $1, \dots, n$; the only way a convex combination could cancel is a domino collapse from the top coordinate down, which the presence of a nonzero entry forbids.
>
> **The homotopy toward the base point, $N_G$.** With $z$ as above,
> $$N_G(t,z) = (1-t)(0, z_0, \dots, z_{n-1}) + t(1, 0, \dots, 0) \in \mathbb{C}^{n+1},$$
> whose $0$-th entry is
> $$\big(N_G\big)_0 = (1-t)\cdot 0 + t \cdot 1 = t.$$
> - If $t \in (0, 1]$, then $(N_G)_0 = t \neq 0$, so $N_G(t, z) \neq 0$.
> - If $t = 0$, then $N_G(0, z) = T z$ and $\|T z\| = 1 \neq 0$.
>
> Hence $N_G(t, z) \neq 0$ for all $t \in [0,1]$, $z \in S^\infty$. **In words:** $T z$ has zero first coordinate while $e_0$ is supported entirely in the first coordinate, so the first coordinate of the segment is exactly $t$ and cannot vanish except at $t = 0$, where the vector is the unit vector $T z$.

**Step 2: Define the two homotopies and record their endpoints.**

The normalised maps
$$F(t, z) = \frac{N_F(t,z)}{\|N_F(t,z)\|}, \qquad G(t, z) = \frac{N_G(t,z)}{\|N_G(t,z)\|}$$
are well defined maps $[0,1] \times S^\infty \to S^\infty$ with $F(0, \cdot) = \mathrm{id}$, $F(1, \cdot) = T$, $G(0, \cdot) = T$, and $G(1, \cdot) = \mathrm{const}_{e_0}$.

> [!note]- Derivation
> By Step 1 the denominators $\|N_F\|, \|N_G\|$ are strictly positive on $[0,1] \times S^\infty$, so $F$ and $G$ are defined, and each value has norm $1$ by construction, hence lies in $S^\infty$ (the normalised vector has the same finite support as its numerator, so it is a genuine point of $S^\infty$). The endpoint values:
> $$F(0, z) = \frac{z}{\|z\|} = z = \mathrm{id}(z), \qquad F(1, z) = \frac{T z}{\|T z\|} = T z,$$
> $$G(0, z) = \frac{T z}{\|T z\|} = T z, \qquad G(1, z) = \frac{e_0}{\|e_0\|} = e_0 = \mathrm{const}_{e_0}(z).$$
> In particular $F(1, \cdot) = T = G(0, \cdot)$, so the two homotopies agree at the junction.

**Step 3: Each homotopy is continuous on every finite stage, compatibly with inclusions.**

For each $n$, the restrictions $F, G\colon [0,1] \times S^{2n-1} \to S^{2n+1}$ are continuous, and they commute with the inclusions $S^{2n-1} \hookrightarrow S^{2n+1}$.

> [!note]- Derivation
> Fix $n$ and restrict to $z \in S^{2n-1} \subset \mathbb{C}^n$. As computed in Step 1, $N_F(t,z)$ and $N_G(t,z)$ take values in $\mathbb{C}^{n+1}$, so $F$ and $G$ take values in $S^{2n+1} \subset \mathbb{C}^{n+1}$. On $[0,1] \times S^{2n-1}$, the numerator maps $(t, z) \mapsto N_F(t,z)$ and $(t,z) \mapsto N_G(t,z)$ are polynomial in $t$ and in the real and imaginary parts of the entries of $z$, hence continuous (indeed smooth); the norm $\|\cdot\|$ is continuous; and the norm is bounded below by a positive constant on the compact set $[0,1] \times S^{2n-1}$ (a positive continuous function on a compact space attains a positive minimum, by Step 1). Therefore the quotients $F$ and $G$ are continuous on $[0,1] \times S^{2n-1}$.
>
> **Compatibility with the inclusions.** If $z \in S^{2n-1}$ is regarded, via the inclusion, as a point of $S^{2n+1}$ (append a zero), then $T z$ is the same finite sequence whether computed in $\mathbb{C}^{n+1}$ or in $\mathbb{C}^{n+2}$, and the formulas for $N_F, N_G$ depend only on $z, T z, e_0$; hence the restriction of $F$ (respectively $G$) computed at stage $n+1$ agrees on $[0,1] \times S^{2n-1}$ with the composite of the stage-$n$ map followed by the inclusion $S^{2n+1} \hookrightarrow S^{2n+3}$. The stagewise maps therefore form a compatible family, and each defines a single set-theoretic map $[0,1] \times S^\infty \to S^\infty$ — namely $F$ and $G$ as in Step 2.

**Step 4: Products with $[0,1]$ preserve the colimit, so $F$ and $G$ are continuous on $[0,1] \times S^\infty$.**

Because $[0,1]$ is compact and $S^\infty = \varinjlim S^{2n-1}$ is the colimit of closed inclusions of compact metric spaces, the space $[0,1] \times S^\infty$ carries the colimit topology of the $[0,1] \times S^{2n-1}$; a map out of it that is continuous on each stage is continuous.

> [!note]- Derivation
> **Lemma (compact $\times$ colimit).** Let $K$ be a compact metric space and $X = \bigcup_{n\ge 1} X_n$ with $X_1 \subseteq X_2 \subseteq \cdots$, each $X_n$ a compact metric space, each $X_n$ closed in $X$, and $X$ carrying the weak topology ($C \subseteq X$ is closed if and only if $C \cap X_n$ is closed in $X_n$ for all $n$). Then a subset $A \subseteq K \times X$ is closed if and only if $A \cap (K \times X_n)$ is closed in $K \times X_n$ for every $n$; equivalently $K \times X = \varinjlim (K \times X_n)$.
>
> *Proof of the lemma.* The "only if" direction is immediate, since $K \times X_n$ is a subspace of $K \times X$. For "if", suppose $A_n := A \cap (K \times X_n)$ is closed in $K \times X_n$ for all $n$; note $K \times X_n$ is closed in $K \times X$ (as $X_n$ is closed in $X$), so each $A_n$ is closed in $K \times X$. We show the complement of $A$ is open. Let $(k_0, x_0) \in (K \times X) \setminus A$; choose $m$ with $x_0 \in X_m$.
>
> Each $K \times X_n$ is a product of compact metric spaces, hence a compact metric space, in particular **normal**. We construct open sets $O_n \subseteq K \times X_n$ (open in the subspace $K \times X_n$), for $n \ge m$, with
> $$(k_0, x_0) \in O_m, \qquad \overline{O_n}^{\,K\times X_n} \cap A = \varnothing, \qquad \overline{O_n}^{\,K\times X_n} \subseteq O_{n+1}.$$
> *Base ($n = m$).* The point $(k_0, x_0)$ and the closed set $A_m$ are disjoint in the normal space $K \times X_m$, so there is an open $O_m \ni (k_0, x_0)$ with $\overline{O_m} \cap A_m = \varnothing$; since $\overline{O_m} \subseteq K \times X_m$, meeting $A$ is the same as meeting $A_m$, so $\overline{O_m} \cap A = \varnothing$.
> *Step ($n \to n+1$).* The closure $\overline{O_n}^{\,K \times X_n}$ is a closed subset of the compact space $K \times X_n$, hence compact, hence closed in $K \times X_{n+1}$; it is disjoint from the closed set $A_{n+1}$ (as $\overline{O_n} \cap A = \varnothing$). By normality of $K \times X_{n+1}$ there is an open $O_{n+1} \supseteq \overline{O_n}^{\,K\times X_n}$ with $\overline{O_{n+1}}^{\,K\times X_{n+1}} \cap A_{n+1} = \varnothing$, hence $\overline{O_{n+1}} \cap A = \varnothing$. This also gives $O_n \subseteq \overline{O_n} \subseteq O_{n+1}$.
>
> Put $O^\ast = \bigcup_{n \ge m} O_n$. Then $(k_0, x_0) \in O^\ast$ and $O^\ast \cap A = \varnothing$ (each $O_n$ misses $A$). To see $O^\ast$ is open in $K \times X$, we check that $O^\ast \cap (K \times X_j)$ is open in $K \times X_j$ for every $j$. Because the $O_n$ increase, for $n < j$ we have $O_n \subseteq O_j \subseteq K \times X_j$, so those terms are absorbed into the $n = j$ term; thus
> $$O^\ast \cap (K \times X_j) = \bigcup_{n \ge j} \big( O_n \cap (K \times X_j)\big),$$
> a union of sets each open in $K \times X_j$ (as $O_n$ is open in $K \times X_n \supseteq K \times X_j$, its trace on the subspace $K \times X_j$ is open). Hence $O^\ast \cap (K \times X_j)$ is open in $K \times X_j$ for all $j$, so $O^\ast$ is open in the weak topology of $K \times X$. As $(k_0, x_0)$ was an arbitrary point of the complement of $A$, that complement is open and $A$ is closed. This proves $K \times X = \varinjlim(K \times X_n)$. $\square$
>
> **Application.** Take $K = [0,1]$ (compact metric) and $X_n = S^{2n-1}$ (compact metric, each closed in $S^\infty$ because $S^{2n-1}$ is the intersection of $S^\infty$ with the closed condition "coordinates from index $n$ onward vanish", so its trace on every stage is closed). The lemma gives $[0,1] \times S^\infty = \varinjlim([0,1] \times S^{2n-1})$. A map $H\colon [0,1] \times S^\infty \to S^\infty$ is continuous if and only if $H^{-1}(C)$ is closed for every closed $C \subseteq S^\infty$; by the lemma this holds if and only if $H^{-1}(C) \cap ([0,1] \times S^{2n-1})$ is closed for every $n$, i.e. if and only if each restriction $H|_{[0,1] \times S^{2n-1}}$ is continuous. By Step 3 the restrictions of $F$ and of $G$ are continuous on every stage; therefore $F$ and $G$ are continuous on $[0,1] \times S^\infty$.

**Step 5: Concatenate to a homotopy from the identity to a constant.**

Splicing $F$ and $G$ at $t = \tfrac12$ produces a continuous homotopy $H\colon [0,1] \times S^\infty \to S^\infty$ with $H_0 = \mathrm{id}$ and $H_1 = \mathrm{const}_{e_0}$; hence $S^\infty$ is contractible.

> [!note]- Derivation
> Define
> $$H(t, z) = \begin{cases} F(2t, z), & 0 \le t \le \tfrac12, \\[2pt] G(2t - 1, z), & \tfrac12 \le t \le 1. \end{cases}$$
> On the overlap $t = \tfrac12$ the two clauses agree: $F(1, z) = T z = G(0, z)$ (Step 2). The domains $[0, \tfrac12] \times S^\infty$ and $[\tfrac12, 1] \times S^\infty$ are closed in $[0,1] \times S^\infty$ and cover it, and $H$ is continuous on each (a reparametrisation $t \mapsto 2t$ or $t \mapsto 2t - 1$ composed with the continuous maps $F, G$ of Step 4). By the **pasting lemma** — a map that is continuous on each of finitely many closed sets covering the space, and agrees on overlaps, is continuous — $H$ is continuous on $[0,1] \times S^\infty$.
>
> Its endpoints are $H(0, z) = F(0, z) = z$ and $H(1, z) = G(1, z) = e_0$. Thus $H$ is a homotopy $\mathrm{id}_{S^\infty} \simeq \mathrm{const}_{e_0}$, which is exactly the [[Def - Homotopy Equivalence and Contractible Space|identity-nullhomotopic characterisation]] of contractibility. Therefore $S^\infty$ is contractible.

> [!note]- Complete formal solution
> **Claim.** The infinite sphere $S^\infty = \varinjlim S^{2n-1}$, with the direct-limit topology, is contractible.
>
> For $z = (z_0, z_1, \dots) \in S^\infty$ let $T z = (0, z_0, z_1, \dots)$ and $e_0 = (1,0,0,\dots)$. Define, for $(t,z) \in [0,1] \times S^\infty$,
> $$N_F = (1-t)z + t\,Tz, \quad N_G = (1-t)\,Tz + t\,e_0, \quad F = \frac{N_F}{\|N_F\|}, \quad G = \frac{N_G}{\|N_G\|}.$$
> *Nonvanishing.* Writing $z \in S^{2n-1} \subset \mathbb{C}^n$, the coordinates of $N_F$ are $(1-t)z_0$, then $(1-t)z_k + t z_{k-1}$, then $t z_{n-1}$. At $t=0$, $N_F = z$; at $t = 1$, $N_F = Tz$, both of norm $1$; for $t \in (0,1)$, $N_F = 0$ forces $z_0 = 0$, then successively $z_k = 0$, contradicting $\|z\| = 1$. The $0$-th coordinate of $N_G$ is $t$, so $N_G \neq 0$ for $t > 0$, and $N_G = Tz \neq 0$ at $t = 0$. Hence $F, G$ are defined, take values in $S^\infty$, and satisfy $F_0 = \mathrm{id}$, $F_1 = T = G_0$, $G_1 = \mathrm{const}_{e_0}$.
>
> *Continuity.* On each $[0,1] \times S^{2n-1}$, $N_F$ and $N_G$ land in $\mathbb{C}^{n+1}$, are polynomial hence continuous, and have norm bounded below by a positive constant (a positive continuous function on a compact set), so $F, G$ are continuous into $S^{2n+1}$; the stagewise maps are compatible with the inclusions. Since $[0,1]$ is compact and $S^\infty$ is the colimit of the closed inclusions of the compact metric spaces $S^{2n-1}$, the compact-times-colimit lemma gives $[0,1] \times S^\infty = \varinjlim([0,1] \times S^{2n-1})$; thus a map continuous on each stage is continuous, and $F, G$ are continuous on $[0,1] \times S^\infty$.
>
> *Concatenation.* Set $H(t,z) = F(2t, z)$ for $t \le \tfrac12$ and $H(t,z) = G(2t-1, z)$ for $t \ge \tfrac12$; the clauses agree at $t = \tfrac12$ (both equal $Tz$), so by the pasting lemma $H$ is continuous, with $H_0 = \mathrm{id}$ and $H_1 = \mathrm{const}_{e_0}$. Therefore $\mathrm{id}_{S^\infty} \simeq \mathrm{const}_{e_0}$, and $S^\infty$ is contractible. $\blacksquare$

> [!warning] Illegal but tempting route: contract directly along $t \mapsto \big((1-t)z + t e_0\big)/\|\cdots\|$.
> It is tempting to skip the shift and slide each point straight to $e_0$. But the straight segment from $z$ to $e_0$ *can* pass through the origin: take $z = -e_0 = (-1, 0, 0, \dots)$; then $(1-t)z + t e_0 = (2t - 1) e_0$, which is $0$ at $t = \tfrac12$, and the normalisation is undefined there (in fact the map jumps from $-e_0$ to $+e_0$). The single-segment contraction therefore fails precisely at the antipode of the target, and no reparametrisation repairs it, because a nonconstant map $S^{2n-1} \to S^{2n-1}$ cannot be a deformation retraction onto a point of a *finite* sphere at all. The shift $T$ is exactly the device that moves the picture into an unused coordinate so that no segment is antipodal: this is why contractibility is an infinite-dimensional phenomenon, false at every finite stage and true only in the colimit.

---

# Key Takeaways

**Infinite dimension is contracted by pushing into a spare coordinate: the shift, not the straight line to the target, is the right first move.** Every finite sphere $S^{2n-1}$ is genuinely non-contractible, so any contraction of $S^\infty$ must use something no finite stage has — an always-available extra coordinate. The infinite-shift $T z = (0, z_0, z_1, \dots)$ supplies it: sliding $z$ to $T z$ is free of the origin because $z$ and $T z$ have offset supports, and once at $T z$ the first coordinate is empty and can be filled by the target $e_0$. This "make room, then fill it" pattern — sometimes called the Eilenberg swindle when it appears for direct sums, K-theory, or free resolutions — is the reusable engine: whenever an object has a countable direct-sum or direct-limit structure, look for a shift that trades a finite obstruction for the infinite tail. The trigger is a contractibility, acyclicity, or "everything is stably trivial" claim about a countable colimit; the reaction is to write down the shift and a normalised straight-line homotopy to it.

**On a direct-limit space, continuity is checked stage by stage — but promoting stagewise continuity to the whole colimit is a theorem, and it needs compactness of the interval.** The direct-limit (weak) topology is defined so that a map *out of* $S^\infty$ is continuous exactly when its restriction to each $S^{2n-1}$ is. The subtlety that trips people is that a *homotopy* is a map out of $[0,1] \times S^\infty$, and the product of a colimit with another space is *not* in general the colimit of the products. What rescues the argument is that $[0,1]$ is compact: for a compact (metric) factor $K$ and a colimit of closed inclusions of compact metric spaces, $K \times \varinjlim X_n = \varinjlim (K \times X_n)$, proved by a tube-lemma induction that separates a point from the closed set stage by stage using normality of each $K \times X_n$. The transferable diagnostic: any time a homotopy, path, or family parametrised by a compact space is built on a CW complex or a direct limit, one may verify continuity skeleton by skeleton or stage by stage, and the compactness of the parameter space is the hypothesis that legitimises it. Forgetting this is the classic gap in "obvious" continuity claims about maps on CW complexes and infinite-dimensional spheres.

**Contractibility of the total space is the whole non-trivial content of a classifying bundle, and it is what makes $S^\infty \to \mathbb{CP}^\infty$ classify $U(1)$-bundles.** A classifying bundle for $G$ is a *free, contractible* $G$-space; freeness of the scalar $U(1)$-action on $S^\infty$ is visible, so contractibility is the substantive hypothesis, and this exercise supplies it. Its payoff downstream is exact: because $S^\infty$ is contractible, principal $U(1)$-bundles over a space $M$ are in bijection with homotopy classes of maps $M \to \mathbb{CP}^\infty$, and the pulled-back generator of the cohomology of $\mathbb{CP}^\infty$ becomes the first Chern class. The same construction with the quaternions gives the contractible $S^\infty$ with a free $Sp(1) = SU(2)$-action and classifying space $\mathbb{HP}^\infty$, used to define $c_2$ and to see that $SU(2)$-bundles over manifolds of dimension at most three are trivial (their classifying maps compress into the point that is the $3$-skeleton of $\mathbb{HP}^\infty$). The recognition pattern for the series: when a classification "by homotopy classes of maps into a model space" is invoked, the model's total space being contractible is the fact underwriting it, and it is almost always proved by exactly this shift-then-fill homotopy. See the companion drill [[Ex - Every SU(2)-Bundle over the 3-Torus is Trivial]], which reaches the same triviality conclusion for $SU(2)$ over a three-manifold by the transversality route rather than the classifying-space route.
