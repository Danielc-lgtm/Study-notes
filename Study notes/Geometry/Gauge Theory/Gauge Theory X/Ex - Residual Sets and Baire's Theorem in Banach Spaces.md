---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Residual Set and Generic Property"
  - "Thm - Baire Category Theorem"
  - "Def - Nowhere Dense and Meager"
  - "Def - Cauchy Sequence and Complete Metric Space"
  - "Thm - Sard-Smale Theorem"
  - "Def - Fredholm Map and Its Index"
tags: [geometry, gauge-theory]
---

# Problem Statement

The Sard–Smale theorem says that the regular values of a single smooth Fredholm map form a *residual* set in the target, and that a residual set in a Banach manifold is dense. In gauge theory one almost never perturbs to arrange a single genericity condition; one arranges *countably many at once* — that the connection is irreducible, that the linearised equation is surjective, that a whole sequence of auxiliary maps have a common regular value — and then wants the perturbations that work for all of them simultaneously to still be plentiful. This exercise establishes the stability of "residual" under countable intersection that makes such simultaneous arguments legitimate, and pins down exactly how large a residual set is.

Let $X$ be a topological space. Recall that a subset $A\subseteq X$ is **residual** if it contains a countable intersection of open dense subsets of $X$, and that a property is said to hold **generically** if the set of points where it holds is residual. Prove the following three statements.

1. **(Countable stability.)** If $\{A_k\}_{k\in\mathbb{N}}$ is a countable family of residual subsets of $X$, then $\bigcap_{k\in\mathbb{N}}A_k$ is residual.

2. **(Size in a Banach space.)** Let $E$ be a real Banach space with $E\neq\{0\}$. Then every residual subset $A\subseteq E$ is **dense** and **uncountable**.

3. **(Simultaneous regular values.)** Let $Y$ be a second countable Banach manifold and let $\{F_i\}_{i\in\mathbb{N}}$ be a countable family of smooth Fredholm maps $F_i\colon X_i\to Y$ (with possibly distinct second countable Banach-manifold domains $X_i$, common target $Y$). Then the set
$$R:=\{\,y\in Y : y\text{ is a regular value of }F_i\text{ for every }i\in\mathbb{N}\,\}$$
is residual in $Y$, hence dense.

**Recall:**

The objects in play are the residual (comeagre) sets, the notions of nowhere dense and meagre set, the completeness of a Banach space, Baire's theorem, and the Sard–Smale theorem for Fredholm maps.

![[Def - Residual Set and Generic Property#The Definition]]

Throughout we use the definition in the primary form just recalled: $A\subseteq X$ is [[Def - Residual Set and Generic Property|residual]] if and only if there exist open dense sets $U_1,U_2,\dots\subseteq X$ with $\bigcap_{n\in\mathbb{N}}U_n\subseteq A$. A property is **generic** if it holds on a residual set. The complement of a residual set is called **meagre** (see below); "residual" and "comeagre" are synonyms.

![[Def - Nowhere Dense and Meager#The Definition]]

A subset $S\subseteq X$ is [[Def - Nowhere Dense and Meager|nowhere dense]] if its closure $\overline{S}$ has empty interior, and **meagre** (of the first category) if it is a countable union of nowhere dense sets. If $U\subseteq X$ is open and dense then its complement $U^{c}=X\setminus U$ is closed with $\operatorname{int}(U^{c})=X\setminus\overline{U}=X\setminus X=\varnothing$, so $U^{c}$ is nowhere dense; consequently a set that contains a countable intersection $\bigcap_{n}U_n$ of open dense sets has complement contained in $\bigcup_{n}U_n^{c}$, a meagre set. Thus **$A$ is residual if and only if $A^{c}$ is meagre.**

![[Def - Cauchy Sequence and Complete Metric Space#The Definition]]

A real Banach space $E$ is by definition a complete normed vector space; with the metric $d(x,y)=\lVert x-y\rVert$ it is a [[Def - Cauchy Sequence and Complete Metric Space|complete metric space]], so Baire's theorem applies to it.

![[Thm - Baire Category Theorem#Statement]]

We use both formulations of [[Thm - Baire Category Theorem|Baire's theorem]] on a complete metric space $X$: (1) the union of countably many nowhere dense subsets has empty interior — equivalently, no nonempty open subset of $X$ is meagre; and (2) the intersection of countably many dense open subsets is dense.

![[Thm - Sard-Smale Theorem#Statement]]

The [[Thm - Sard-Smale Theorem|Sard–Smale theorem]] states that for a smooth [[Def - Fredholm Map and Its Index|Fredholm map]] $F\colon X\to Y$ between second countable Banach manifolds, the set of regular values of $F$ is residual in $Y$, and in particular dense. Here $y\in Y$ is a **regular value** of $F$ if $d_xF\colon T_xX\to T_yY$ is surjective for every $x\in F^{-1}(y)$ (vacuously so when $F^{-1}(y)=\varnothing$).

---

# Convergent Strategy

**Problem class.** All three parts are *category-calculus* problems: they manipulate the ideal-like class of "small" (meagre) sets and its dual class of "large" (residual) sets. The decisive structural fact is that the meagre sets form a $\sigma$-ideal — closed under subsets and countable unions — in any topological space, and that this ideal is *proper* (does not contain the whole space) exactly when the space is a Baire space. Parts 1 and 3 are pure $\sigma$-ideal bookkeeping; part 2 is where the Baire property of the space is actually consumed.

**Assumption pattern.** The hypothesis "countable" is load-bearing and appears in the same way each time: a countable family of countable families is again countable, because $\mathbb{N}\times\mathbb{N}$ is countable. The hypothesis "complete" (equivalently, "Banach") is used *only once*, through Baire's theorem, and only in part 2 and the final density claim of part 3; the intersection statement of part 1 needs no completeness at all. Recognising which conclusions are topological identities and which require Baire is the whole discipline of the subject.

**Theorem routing.** Part 1 unwinds the definition of residual to a double countable intersection of open dense sets and re-enumerates it using a bijection $\mathbb{N}\times\mathbb{N}\to\mathbb{N}$. Part 2 routes density through Baire's second formulation (a countable intersection of dense open sets is dense, and $A$ contains one) and routes uncountability through Baire's first formulation: if $A$ were countable it would be meagre, and since $A^{c}$ is already meagre (residual $\Rightarrow$ complement meagre), the whole space $E$ would be meagre in itself, contradicting that $E$ is a nonempty complete metric space. Part 3 applies [[Thm - Sard-Smale Theorem|Sard–Smale]] to each $F_i$ to get residual sets $R_i$ of regular values, writes $R=\bigcap_i R_i$, and closes with part 1 for residuality and Baire for density.

**Key decision point.** The one genuine idea is in the uncountability half of part 2: to *use both meagreness of $A^{c}$ and (hypothetical) meagreness of $A$ against each other*. The naïve attempt — "a dense set is uncountable" — is false in general ($\mathbb{Q}$ is dense in $\mathbb{R}$), so density alone cannot give uncountability; what forces it is that $E$ has no isolated points, so a countable set is meagre, and a Baire space cannot be the union of two meagre sets. The second decision point, hidden in part 3, is that the maps $F_i$ may have *different domains*: the residual sets $R_i$ all live in the *common target* $Y$, which is where the intersection and Baire's theorem are applied.

---

# Legal Operations Used

This solution deploys the following operations, referenced descriptively (the numbering on [[Gauge Theory X — Fredholm Maps, Transversality, and Degree#Legal Operations|the topic page's Legal Operations]] will be reconciled by the orchestrator).

1. **Unwind "residual" to a witnessing sequence of dense open sets.** Whenever a set is residual, produce open dense $U_1,U_2,\dots$ with $\bigcap_n U_n\subseteq A$; whenever one must be proved residual, exhibit such a sequence.

2. **Re-index a countable-by-countable family through $\mathbb{N}\times\mathbb{N}$.** A countable union or intersection of countable collections is countable, via a fixed bijection $\mathbb{N}\times\mathbb{N}\to\mathbb{N}$.

3. **Pass between residual and meagre by complementation.** $A$ residual $\iff$ $A^{c}$ meagre; a subset of a meagre set is meagre; a countable union of meagre sets is meagre.

4. **Invoke Baire's theorem in a complete metric space** in its density form (dense-open intersections are dense) and in its non-meagreness form (a nonempty open set, in particular the whole space, is not meagre).

5. **Use that a nonzero normed space has no isolated points** to certify that singletons — hence countable sets — are nowhere dense, hence meagre.

6. **Apply Sard–Smale to each member of a countable family** to obtain a residual set of regular values in the common target, then intersect.

---

# Hints

> [!note]- Hint 1
> For part 1, write out what "$A_k$ is residual" means literally: there are open dense sets $U^{(k)}_1,U^{(k)}_2,\dots$ whose intersection lies inside $A_k$. What set is $\bigcap_k\bigcap_n U^{(k)}_n$, and how many sets are being intersected?

> [!note]- Hint 2
> For the density half of part 2, you do not need to work hard: $A$ contains a countable intersection of dense open sets, and Baire's theorem tells you directly what such an intersection is. A superset of a dense set is dense.

> [!note]- Hint 3
> For the uncountability half of part 2, argue by contradiction: suppose $A=\{a_1,a_2,\dots\}$ is countable. Show each singleton $\{a_j\}$ is nowhere dense — this is where you need $E\neq\{0\}$, so that no point is isolated. Then $A$ is meagre. But $A^{c}$ is *also* meagre because $A$ is residual. Add the two facts and confront Baire.

> [!note]- Hint 4
> For part 3, the sets you intersect all live in the same target $Y$, even though the maps $F_i$ start from different spaces. Sard–Smale makes each set of regular values residual in $Y$; part 1 makes the intersection residual; Baire (a Banach manifold is a Baire space) makes it dense.

---

# Solution

The three parts are logically independent modulo the definitions, so we prove them in turn. Part 1 is a re-indexing of a double intersection; part 2 consumes Baire's theorem twice, once for density and once — through the absence of isolated points — for uncountability; part 3 assembles Sard–Smale, part 1, and Baire. Throughout, "residual" is used in the primary form recalled above: $A$ is residual if some countable intersection of open dense sets is contained in $A$.

**Step 1: A countable intersection of residual sets is residual (part 1).**

We produce, from the witnessing sequences of the individual $A_k$, a single sequence of open dense sets whose intersection lies inside $\bigcap_k A_k$.

> [!note]- Derivation
> Let $\{A_k\}_{k\in\mathbb{N}}$ be residual subsets of the topological space $X$. **Unwind each hypothesis** (operation 1): for each $k\in\mathbb{N}$ there is a sequence of open dense sets $\big(U^{(k)}_n\big)_{n\in\mathbb{N}}$ with
> $$\bigcap_{n\in\mathbb{N}}U^{(k)}_n\;\subseteq\;A_k\qquad\text{(definition of residual, applied to }A_k\text{).}$$
> **Intersect over $k$.** Taking the intersection over all $k$ of both sides and using that intersection is monotone,
> $$\bigcap_{k\in\mathbb{N}}\;\bigcap_{n\in\mathbb{N}}U^{(k)}_n\;\subseteq\;\bigcap_{k\in\mathbb{N}}A_k\qquad\text{(if }S_k\subseteq A_k\text{ for all }k\text{ then }\textstyle\bigcap_k S_k\subseteq\bigcap_k A_k\text{).}$$
> The left-hand side is the intersection of the family $\{U^{(k)}_n : (k,n)\in\mathbb{N}\times\mathbb{N}\}$, indexed by the countable set $\mathbb{N}\times\mathbb{N}$.
> **Re-index through a countable set** (operation 2). Fix a bijection $\beta\colon\mathbb{N}\to\mathbb{N}\times\mathbb{N}$ (for instance the inverse of the Cantor pairing $(k,n)\mapsto\binom{k+n+1}{2}+n$), and set $V_m:=U^{(\beta(m))}$ for $m\in\mathbb{N}$, where we write $U^{(k,n)}:=U^{(k)}_n$. Each $V_m$ is open and dense (it is one of the $U^{(k)}_n$), and, because $\beta$ is a bijection,
> $$\bigcap_{m\in\mathbb{N}}V_m=\bigcap_{(k,n)\in\mathbb{N}\times\mathbb{N}}U^{(k)}_n=\bigcap_{k\in\mathbb{N}}\bigcap_{n\in\mathbb{N}}U^{(k)}_n\qquad\text{(reordering an intersection over a re-indexed set).}$$
> Combining the last displayed inclusion with this identity, $\bigcap_{m}V_m\subseteq\bigcap_k A_k$ with each $V_m$ open dense. Hence $\bigcap_k A_k$ contains a countable intersection of open dense sets, so it is residual by definition.

**Step 2: A residual subset of a nonzero Banach space is dense (part 2, density).**

Density follows directly from Baire's theorem, with no reference to completeness beyond the theorem itself.

> [!note]- Derivation
> Let $E\neq\{0\}$ be a real Banach space and $A\subseteq E$ residual. **Unwind residuality** (operation 1): there are open dense $U_1,U_2,\dots\subseteq E$ with $\bigcap_n U_n\subseteq A$. With the metric $d(x,y)=\lVert x-y\rVert$, $E$ is a [[Def - Cauchy Sequence and Complete Metric Space|complete metric space]] (a Banach space is complete by definition). **Apply Baire's density form** (operation 4): by [[Thm - Baire Category Theorem|Baire's theorem]], formulation (2), the intersection $\bigcap_n U_n$ of countably many dense open subsets of the complete metric space $E$ is dense in $E$. Since $\bigcap_n U_n\subseteq A$ and a superset of a dense set is dense (if $\overline{S}=E$ and $S\subseteq A$ then $E=\overline{S}\subseteq\overline{A}$, so $\overline{A}=E$), the set $A$ is dense.

**Step 3: A residual subset of a nonzero Banach space is uncountable (part 2, uncountability).**

We argue by contradiction, using that $E$ has no isolated points to make a countable set meagre, and then that a complete metric space is not meagre in itself.

> [!note]- Derivation
> Suppose, **for contradiction**, that a residual set $A\subseteq E$ is countable, say $A=\{a_1,a_2,\dots\}$ (a finite $A$ is handled by the same argument with a finite list).
>
> **Singletons are nowhere dense** (operation 5). Fix $j$. In a metric space every singleton $\{a_j\}$ is closed, so $\overline{\{a_j\}}=\{a_j\}$; we show it has empty interior. Because $E\neq\{0\}$, pick a vector $v\in E$ with $v\neq0$. For any radius $\varepsilon>0$ the point
> $$a_j+\frac{\varepsilon}{2\lVert v\rVert}\,v\qquad\text{lies in the open ball }B(a_j,\varepsilon)\text{ and differs from }a_j$$
> (its distance to $a_j$ is $\tfrac{\varepsilon}{2}<\varepsilon$, and it is $\neq a_j$ since $v\neq0$). Thus no ball around $a_j$ is contained in $\{a_j\}$, so $\operatorname{int}\{a_j\}=\varnothing$. Hence $\{a_j\}$ is [[Def - Nowhere Dense and Meager|nowhere dense]].
>
> **$A$ is meagre.** As $A=\bigcup_{j}\{a_j\}$ is a countable union of nowhere dense sets, $A$ is meagre by definition (operation 3).
>
> **$A^{c}$ is meagre.** Because $A$ is residual, its complement is meagre: writing $\bigcap_n U_n\subseteq A$ with $U_n$ open dense, we have $A^{c}\subseteq\bigcup_n U_n^{c}$, and each $U_n^{c}$ is closed with empty interior, hence nowhere dense (operation 3, recalled above).
>
> **Confront Baire** (operation 4). Then $E=A\cup A^{c}$ is a union of two meagre sets, so $E$ is itself meagre: it is a countable union of nowhere dense sets. But $E$ is a nonempty open subset of the complete metric space $E$, and by [[Thm - Baire Category Theorem|Baire's theorem]], formulation (1), no nonempty open subset of a complete metric space is meagre. This contradicts $E$ being meagre. The contradiction is between "$E$ is meagre" (just derived) and Baire's non-meagreness of the open set $E$.
>
> Therefore the assumption fails: $A$ is uncountable.

**Step 4: The common regular values of a countable family are residual and dense (part 3).**

We apply Sard–Smale to each map, intersect with Step 1, and finish with Step 2's density argument in the target.

> [!note]- Derivation
> Let $Y$ be a second countable Banach manifold and $\{F_i\}_{i\in\mathbb{N}}$ smooth [[Def - Fredholm Map and Its Index|Fredholm maps]] $F_i\colon X_i\to Y$ into the common target $Y$. For each $i$ set
> $$R_i:=\{\,y\in Y : y\text{ is a regular value of }F_i\,\}.$$
> **Apply Sard–Smale to each $F_i$** (operation 6). By the [[Thm - Sard-Smale Theorem|Sard–Smale theorem]] — for a smooth Fredholm map between second countable Banach manifolds the set of regular values is residual in the target — each $R_i$ is a residual subset of $Y$. The hypothesis is met for every $i$ because $X_i$ and $Y$ are second countable Banach manifolds and $F_i$ is smooth Fredholm.
>
> **Intersect** (operation 1 and Step 1). The set of simultaneous regular values is exactly
> $$R=\bigcap_{i\in\mathbb{N}}R_i,$$
> a countable intersection of residual subsets of $Y$. By Step 1 (part 1), $R$ is residual in $Y$.
>
> **Density** (operation 4). A Banach manifold is a Baire space: it is second countable and locally homeomorphic to open subsets of a Banach space, so [[Thm - Baire Category Theorem|Baire's theorem]] applies chart by chart, and a residual subset of a Baire space is dense (the density form of Baire in each chart, patched by second countability, is proved on [[Def - Residual Set and Generic Property|the residual-set page]]). Hence $R$ is dense in $Y$: a generic $y\in Y$ is simultaneously a regular value of every $F_i$.

> [!note]- Complete formal solution
> **Claim.** (1) A countable intersection of residual sets is residual. (2) A residual subset of a Banach space $E\neq\{0\}$ is dense and uncountable. (3) For countably many smooth Fredholm maps $F_i\colon X_i\to Y$ into a second countable Banach manifold $Y$, the set of common regular values is residual, hence dense.
>
> *Proof of (1).* Let $A_k$ ($k\in\mathbb{N}$) be residual, with open dense $U^{(k)}_n$ satisfying $\bigcap_n U^{(k)}_n\subseteq A_k$. Then $\bigcap_{(k,n)}U^{(k)}_n\subseteq\bigcap_k A_k$. Re-indexing the countable family $\{U^{(k)}_n\}_{(k,n)\in\mathbb{N}\times\mathbb{N}}$ by a bijection $\mathbb{N}\to\mathbb{N}\times\mathbb{N}$ exhibits $\bigcap_k A_k$ as containing a countable intersection of open dense sets, so it is residual.
>
> *Proof of (2), density.* With $\bigcap_n U_n\subseteq A$ ($U_n$ open dense), Baire's theorem in the complete metric space $E$ gives that $\bigcap_n U_n$ is dense; as $A\supseteq\bigcap_n U_n$, $A$ is dense.
>
> *Proof of (2), uncountability.* Suppose $A$ is countable, $A=\{a_1,a_2,\dots\}$. Since $E\neq\{0\}$, no point is isolated, so each $\{a_j\}$ is closed with empty interior, hence nowhere dense; thus $A=\bigcup_j\{a_j\}$ is meagre. Since $A$ is residual, $A^{c}$ is meagre. Then $E=A\cup A^{c}$ is meagre, contradicting Baire's theorem (a nonempty complete metric space is not meagre in itself). Hence $A$ is uncountable.
>
> *Proof of (3).* By Sard–Smale each set $R_i$ of regular values of $F_i$ is residual in $Y$. The common regular values are $R=\bigcap_i R_i$, residual by (1). A second countable Banach manifold is a Baire space, so the residual set $R$ is dense by (the manifold form of) Baire's theorem. $\blacksquare$

> [!warning] Illegal but tempting: "dense $\Rightarrow$ uncountable" without the Baire step
> It is tempting to shorten part 2 by saying "$A$ is dense in the uncountable space $E$, hence uncountable." This is false: $\mathbb{Q}$ is dense in $\mathbb{R}$ yet countable. Density is a topological largeness that is entirely compatible with countability. What genuinely forces uncountability is the *category* argument — a countable set is meagre (because points are non-isolated), and a Baire space is not the union of two meagre sets. The extra condition that rescues the tempting route is *completeness together with no isolated points*; drop either and the conclusion can fail (a countable metric space with no isolated points, such as $\mathbb{Q}$, has residual countable subsets — for example $\mathbb{Q}$ itself is residual in $\mathbb{Q}$).

---

# Key Takeaways

**Residual is stable under countable intersection, and this is the entire licence for "arrange countably many generic conditions at once".** The class of residual sets is closed under countable intersection because the class of meagre sets is a $\sigma$-ideal — closed downward under inclusion and under countable unions — and residual is the dual notion (complement meagre). The proof is nothing more than flattening a double countable intersection of dense open sets into a single one, using that $\mathbb{N}\times\mathbb{N}$ is countable. The trigger to reach for this in practice is the phrase "for a generic choice, all of the following hold", with the "following" being a countable list: whenever a construction needs a parameter that is simultaneously regular for a sequence of maps, transverse to a sequence of submanifolds, or avoids a sequence of bad loci, the intersection of the individual residual sets is again residual, hence — in a Baire space — nonempty and dense. This is precisely what lets one perturb a metric or a connection in gauge theory so that infinitely many moduli problems become transverse together, as on [[Thm - Sard-Smale Theorem|the Sard–Smale page]] and in the Seiberg–Witten transversality arguments.

**"Large" splits into two independent measurements — topological density and cardinality — and only the second needs the space's completeness through a no-isolated-points argument.** Part 2 makes the sharp distinction visible: density of a residual set is immediate from Baire's density formulation and says nothing about how many points the set has, whereas uncountability is a separate fact that fails for a countable ambient space and must be extracted from the non-meagreness of a Baire space. The reusable diagnostic is: to prove a set uncountable via category, do not argue from density; instead show that its complement is meagre (residuality), assume the set countable, note that in a perfect space (no isolated points) countable sets are meagre, and derive that the whole space is meagre — impossible in a complete metric space. The same template proves that the irrationals are uncountable, that a nonempty perfect complete metric space is uncountable, and that the set of nowhere-differentiable continuous functions on $[0,1]$ (a residual set in $C[0,1]$) is uncountable.

**The Baire property is the one place completeness is spent; everything else is set algebra.** Tracking which step uses which hypothesis is the meta-lesson. Part 1 is a pure identity valid in any topological space and uses no completeness. The density and the uncountability of part 2, and the density conclusion of part 3, all route through Baire's theorem, and Baire's theorem is exactly the statement that a complete metric space (or a locally compact Hausdorff space, or — patched by second countability — a Banach manifold) is a Baire space. When a proof in infinite dimensions claims a generic conclusion, the audit question is always "where did completeness enter?", and the answer is invariably "at the single invocation of Baire that turns residual into dense". This is why the target of a Fredholm map is required to be a *Banach* manifold and why second countability is imposed: without a Baire space the residual set of Sard–Smale could be empty, and the whole degree and transversality theory would say nothing. The companion drill [[Ex - Regular Values of a Fredholm Map of Negative Index]] uses the residual set produced here in the opposite direction — to show that when the index is negative, this large set of regular values consists entirely of points the map never hits.
