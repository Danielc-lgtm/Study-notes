---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Dense Subset"
  - "Def - Nowhere Dense and Meager"
  - "Thm - Baire Category Theorem"
  - "Def - Banach Manifold and Smooth Maps between Banach Spaces"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $X$ is a topological space; in the applications of this chapter $X$ is a [[Def - Banach Manifold and Smooth Maps between Banach Spaces|Banach manifold]] — a Hausdorff, second countable space with an atlas of charts $\varphi\colon V\to O$ onto open subsets $O$ of a fixed separable Banach space $(B,\lVert\cdot\rVert)$, with smooth transition maps. A subset $U\subseteq X$ is **open** if it belongs to the topology; $\overline{A}$ is the closure of $A$ and $\operatorname{int}(A)$ its interior. A subset $A\subseteq X$ is **dense** if $\overline{A}=X$, equivalently if $A$ meets every nonempty open set (see [[Def - Dense Subset]]). A subset $A$ is **nowhere dense** if $\operatorname{int}(\overline{A})=\varnothing$; a subset $S$ is **meager** (of the first category) if it is a countable union $S=\bigcup_{n\ge1}A_n$ of nowhere dense sets; a subset is of the **second category** if it is not meager (see [[Def - Nowhere Dense and Meager]]). We write $\mathbb{Q}$ for the rationals, $\mathbb{R}\setminus\mathbb{Q}$ for the irrationals, and $B(x,r)=\{y:\lVert y-x\rVert<r\}$, $\overline{B}(x,r)=\{y:\lVert y-x\rVert\le r\}$ for the open and closed balls in a normed space. A **Baire space** is a topological space in which every countable intersection of dense open sets is dense. The symbol registry for the chapter is on [[Gauge Theory X — Fredholm Maps, Transversality, and Degree]].

> [!warning] Convention: "second category" versus "residual"
> Haydys (*Introduction to Gauge Theory*, p. 53) writes that "a subset $A$ of a topological space is said to be of *second category* if $A$ can be represented as a countable intersection of open dense subsets." This is **not** the standard meaning of second category. In the classical Baire terminology used on [[Def - Nowhere Dense and Meager]] — and everywhere in this series — *second category* means merely *not meager*, whereas a set that contains a countable intersection of dense open subsets is called **residual** (synonymously **comeager**). A residual set is always of the second category, but not conversely. To read Haydys's statements in the series' language, replace his "of second category" by "residual". The one-line recipe: **Haydys's "second category" $=$ residual $=$ comeager $=$ the complement of a meager set.**

---

# Axiom Motivation

The goal of this chapter is to make sense of the phrase *"almost every value is a regular value"* in infinite dimensions. In finite dimensions [[Thm - Sard's Theorem for Smooth Maps|Sard's theorem]] delivers the sharp statement that the critical values of a smooth map form a set of Lebesgue measure zero, so that the regular values are a set of full measure. But a Banach space of infinite dimension carries **no translation-invariant measure at all** — every nonempty open ball would have to have the same positive measure as any other by translation, and countably many disjoint balls fit inside a bounded set, forcing that measure to be $0$ or $\infty$. There is therefore no "measure zero" to appeal to. We need a purely *topological* notion of a "large" set that (i) is preserved under countable intersection, so that we may impose countably many genericity conditions at once; (ii) forces the set to be nonempty, indeed dense, so that a "generic" object actually exists and can be found arbitrarily near any given one; and (iii) makes sense on any topological space, in particular on a Banach manifold. Residual sets are exactly this notion, and the Baire category theorem is what supplies property (ii).

Consider the desiderata one at a time, and let each clause of the definition be *forced* by the failure of the alternatives. We define a set $R\subseteq X$ to be **residual** if it contains a countable intersection $\bigcap_{n\ge1}U_n$ of subsets $U_n$ that are **open and dense**. Why each of the four words?

**Why "dense".** If the $U_n$ were only required to be open, the intersection could be empty, or nonempty but tiny, and there would be nothing "large" about it. Concretely, in $X=\mathbb{R}$ the sets $U_n=(0,1/n)$ are open, yet $\bigcap_{n\ge1}U_n=\varnothing$. A notion of largeness built on such families would call the empty set large, which is absurd. Requiring each $U_n$ to be dense is what prevents the intersection from being crowded out of any region: density says $U_n$ has representatives everywhere, and the Baire theorem below turns "everywhere, countably often" into "somewhere in every open set."

**Why "open".** Density alone, without openness, is not preserved even under a single intersection: $\mathbb{Q}$ and $\mathbb{R}\setminus\mathbb{Q}$ are both dense in $\mathbb{R}$, yet their intersection is empty. It is precisely the *openness* of the $U_n$ that makes the Baire category theorem applicable, and openness together with density is the pair of hypotheses that theorem is built to consume. Drop openness and there is no theorem guaranteeing the intersection is nonempty; a countable family of dense sets can have empty intersection in any space with a countable dense subset. So the two words "open" and "dense" are not decoration: they are exactly the hypotheses of Baire's theorem, imported into the definition so that residual sets automatically inherit its conclusion.

**Why "countable".** An *uncountable* intersection of dense open sets can collapse to nothing: in $\mathbb{R}$, each $\mathbb{R}\setminus\{a\}$ is open and dense, but $\bigcap_{a\in\mathbb{R}}(\mathbb{R}\setminus\{a\})=\varnothing$. The Baire category theorem tolerates countably many conditions and no more; countability is the exact ceiling under which "dense $\cap$ dense $\cap\cdots$" stays dense in a complete space. This is the same ceiling that appears in measure theory (a countable union of null sets is null, an uncountable one need not be), and it is what lets us impose one genericity condition per element of a countable list — one per critical stratum, one per member of a countable family of maps — and still land in a set that is large.

**Why "contains" rather than "equals".** We ask only that $R$ *contain* a countable intersection of dense open sets, not that it *be* one. This makes the class of residual sets closed upward: if $R$ is residual and $R\subseteq R'$ then $R'$ is residual. Upward closure is exactly what a genericity notion must have, because genericity is used through implications: if a property $P$ holds on a residual set and $P\Rightarrow Q$ pointwise, then $Q$ holds on a residual set too. It also makes residuality closed under countable intersection (a countable intersection of countable intersections of dense open sets is again one), so that finitely or countably many "generic" conditions may be conjoined without leaving the class.

Finally, there is a clause that is not visible in the definition of residual itself but is essential to its usefulness: **the ambient space must be a Baire space.** On a general topological space a residual set can be empty. In the rationals $\mathbb{Q}$ with the subspace topology, every set $\mathbb{Q}\setminus\{q\}$ is open and dense, yet $\bigcap_{q\in\mathbb{Q}}(\mathbb{Q}\setminus\{q\})=\varnothing$ is a *residual* subset of $\mathbb{Q}$ that is not dense — indeed it is empty. Residuality is only worth having where residual $\Rightarrow$ dense, and that implication is precisely the statement that the ambient space is a Baire space. The [[Thm - Baire Category Theorem|Baire category theorem]] guarantees it for complete metric spaces and for locally compact Hausdorff spaces; the corollary below extends the guarantee to every Banach manifold, which is the setting of Sard–Smale. Without this clause the definition captures a plausible-looking largeness that carries no existence content; with it, "$P$ holds generically" implies "the set where $P$ holds is dense", hence nonempty, hence $P$-objects exist and approximate every point.

A reader who has internalised these four failures — open crushed to empty, dense not closed under intersection, uncountable collapsing, and the non-Baire ambient — could reconstruct the definition and its accompanying hypothesis on the ambient space without being told them.

---

# The Definition

Let $X$ be a topological space.

**Residual set.** A subset $R\subseteq X$ is **residual** (synonymously **comeager**) if there is a countable family $\{U_n\}_{n\ge1}$ of dense open subsets of $X$ with
$$\bigcap_{n\ge1}U_n\ \subseteq\ R.$$
Equivalently, $R$ is residual if and only if its complement $X\setminus R$ is [[Def - Nowhere Dense and Meager|meager]]; the equivalence is proved as Corollary 2 below.

**Generic property.** A property $P$ that each point $x\in X$ either has or lacks is said to hold **generically**, or **for a generic $x\in X$**, if the set
$$\{x\in X : P(x)\ \text{holds}\}$$
is residual in $X$. When we say that a generic value of a map is a regular value, or that a generic connection is irreducible, this is the meaning: the exceptional set — where the property fails — is meager, and the good set contains a countable intersection of dense open sets.

**The Baire property, in the setting we need.** On an arbitrary $X$ a residual set need not be dense. The content that makes the notion useful is the following, which is why every space we call the definition on will be a Baire space:

> **Corollary 1 (a Banach manifold is a Baire space).** Let $X$ be a [[Def - Banach Manifold and Smooth Maps between Banach Spaces|Banach manifold]]. Then every countable intersection of dense open subsets of $X$ is dense; consequently every residual subset of $X$ is dense. The same conclusion holds when $X$ is a complete metric space or a locally compact Hausdorff space, by the [[Thm - Baire Category Theorem|Baire category theorem]] directly.

The proof of Corollary 1 is in the Examples / Corollaries section; it reduces the statement to the [[Thm - Baire Category Theorem|Baire category theorem]] applied inside a single chart, on a closed ball of the model Banach space.

---

# Relate to Other Fields / Compression

Residuality is the **topological twin of full measure**. Both single out a $\sigma$-ideal of "small" sets — the meager sets on one side, the null sets on the other — and call a set "large" when its complement is small; both ideals are closed under countable union and under passing to subsets, and in each theory the large sets are closed under countable intersection. The two notions are genuinely independent: on $\mathbb{R}$ there is a residual set of Lebesgue measure zero and a full-measure set that is meager, so "topologically large" and "measure-theoretically large" can point in opposite directions. Gauge theory works with the topological notion for the structural reason given in the Axiom Motivation — an infinite-dimensional Banach space admits no useful measure, but it is a complete metric space, so Baire category is available where Lebesgue measure is not.

**True name.** Stripped of the wrappings, residual means *comeager*: the complement is a countable union of nowhere dense sets. The operational characterisation — the form in which the notion is actually used — is a recipe rather than a description: **to prove a property is generic, write the good set as a countable intersection $\bigcap_n U_n$ where each $U_n$ is open (the property is stable under small perturbations, so its set is open) and dense (the property can be achieved by an arbitrarily small perturbation, so its set is dense), and invoke Baire.** Openness is a *stability* statement, density is an *achievability* statement, and Baire converts "stable and achievable, countably often" into "holds on a dense set." This is exactly the shape of the [[Thm - Sard-Smale Theorem|Sard–Smale theorem]]'s conclusion and of the parametric transversality argument.

The same pattern recurs across analysis under the name **generic** or **Baire-generic**. In dynamical systems the Kupka–Smale theorem says a generic diffeomorphism has only hyperbolic periodic orbits with transverse stable and unstable manifolds; in spectral theory the generic self-adjoint operator in a family has simple spectrum; in the calculus of variations the generic metric makes the eigenvalues of the Laplacian simple. In each case the proof is the recipe above, and the payoff — "such objects exist and are dense" — is Corollary 1 in the relevant complete space. The detection of meager sets by an infinite game, the **Banach–Mazur game**, gives a second, game-theoretic route to the same $\sigma$-ideal.

---

# Examples / Corollaries

**Is an instance — the irrationals in $\mathbb{R}$.** The set $\mathbb{R}\setminus\mathbb{Q}$ of irrational numbers is residual in $\mathbb{R}$. Enumerate the rationals as $\mathbb{Q}=\{q_1,q_2,\dots\}$ (possible since $\mathbb{Q}$ is countable) and set $U_n=\mathbb{R}\setminus\{q_n\}$. Each $U_n$ is **open** (the complement of a point in a Hausdorff space is open) and **dense** (removing one point from $\mathbb{R}$ leaves a set whose closure is all of $\mathbb{R}$, since every neighbourhood of $q_n$ contains other reals). Their intersection is
$$\bigcap_{n\ge1}U_n=\mathbb{R}\setminus\{q_1,q_2,\dots\}=\mathbb{R}\setminus\mathbb{Q},$$
a countable intersection of dense open sets, so $\mathbb{R}\setminus\mathbb{Q}$ is residual by definition (indeed it equals such an intersection, so the containment in the definition holds with equality). Since $\mathbb{R}$ is a complete metric space, Corollary 1 confirms that this residual set is dense, as of course it is.

**Is an instance — the complement of a countable union of proper submanifolds.** Let $M$ be a smooth manifold and let $\{N_k\}_{k\ge1}$ be a countable family of [[Def - Embedded Submanifold|embedded submanifolds]], each closed as a subset of $M$ and of dimension strictly less than $\dim M$. Then $M\setminus\bigcup_{k}N_k$ is residual in $M$. We verify the two clauses for each $N_k$. **Empty interior:** in a submanifold chart, $N_k$ is carried to a slice $\mathbb{R}^{d_k}\times\{0\}\subseteq\mathbb{R}^{n}$ with $d_k=\dim N_k<n=\dim M$; a slice of positive codimension contains no open ball of $\mathbb{R}^n$, so $\operatorname{int}(N_k)=\varnothing$ (were $x$ interior to $N_k$, a whole $\mathbb{R}^n$-ball around $x$ would lie in the slice, impossible). **Closed with empty interior is nowhere dense:** since $N_k$ is closed, $\overline{N_k}=N_k$, so $\operatorname{int}(\overline{N_k})=\operatorname{int}(N_k)=\varnothing$, which is the definition of nowhere dense. Hence $\bigcup_k N_k$ is a countable union of nowhere dense sets, that is [[Def - Nowhere Dense and Meager|meager]], and its complement is residual by Corollary 2. This is the prototype of a generic condition in geometry: a property that fails only on a countable union of lower-dimensional strata holds generically, and Corollary 1 (with $M$ a manifold, hence locally a complete metric space) makes the good set dense.

**Is NOT an instance — the rationals are dense but not residual.** The set $\mathbb{Q}$ is dense in $\mathbb{R}$ (every interval contains a rational), yet $\mathbb{Q}$ is **not** residual. Suppose it were. The irrationals $\mathbb{R}\setminus\mathbb{Q}$ are residual by the first example, and the intersection of two residual sets is residual (Corollary 3 below), so $\mathbb{Q}\cap(\mathbb{R}\setminus\mathbb{Q})=\varnothing$ would be residual; but $\mathbb{R}$ is a complete metric space, so by Corollary 1 a residual subset is dense, whereas $\varnothing$ is not dense. This contradiction shows $\mathbb{Q}$ is not residual. The example is the sharp separation between the two notions in the definition's Notation: **dense is strictly weaker than residual**, and it is exactly the ambient Baire property that a residual set can exploit but a merely dense one cannot. Equivalently and more directly, $\mathbb{Q}=\bigcup_n\{q_n\}$ is meager, so if $\mathbb{Q}$ were also residual its complement would be both meager and residual, again forcing $\varnothing=\mathbb{Q}\cap(\mathbb{R}\setminus\mathbb{Q})$ to be dense.

**Corollary 1 (a Banach manifold is a Baire space) — proof.** We restate it and prove it in full.

> [!note]- Proof that a Banach manifold is a Baire space
> **Claim.** Let $X$ be a [[Def - Banach Manifold and Smooth Maps between Banach Spaces|Banach manifold]], modelled on a separable Banach space $(B,\lVert\cdot\rVert)$, and let $\{U_n\}_{n\ge1}$ be dense open subsets of $X$. Then $\bigcap_{n\ge1}U_n$ is dense in $X$. Consequently any residual $R\supseteq\bigcap_n U_n$ is dense.
>
> **What must be shown.** A subset is dense if and only if it meets every nonempty open set. So we fix a nonempty open set $W\subseteq X$ and must produce a point of $W\cap\bigcap_{n\ge1}U_n$.
>
> **Step 0 — reduce to a chart, then to a closed ball of the model space.** Pick a point $p\in W$ and a chart $\varphi\colon V\to O$ of $X$ with $p\in V$, where $O=\varphi(V)$ is open in $B$ (such a chart exists by the definition of a Banach manifold, [[Def - Banach Manifold and Smooth Maps between Banach Spaces]]). Replacing $V$ by $V\cap W$ and $O$ by $\varphi(V\cap W)$ — still a chart onto an open subset of $B$, since $\varphi$ is a homeomorphism and $V\cap W$ is open — we may assume $V\subseteq W$. It now suffices to find a point of $\bigcap_{n\ge1}(U_n\cap V)$, because $V\subseteq W$. Set $p'=\varphi(p)\in O$. As $O$ is open in the normed space $B$, choose $\rho>0$ with $\overline{B}(p',\rho)\subseteq O$ (a nonempty open subset of a normed space contains a closed ball about each of its points). Let $K=\overline{B}(p',\rho)$. Being a closed subset of the complete metric space $(B,\lVert\cdot\rVert)$, $K$ is itself a complete metric space in the induced metric (a closed subset of a complete metric space is complete: a Cauchy sequence in $K$ converges in $B$, and its limit lies in $K$ because $K$ is closed).
>
> **Step 1 — transport the $U_n$ into $K$ and check they are dense open there.** For each $n$ put
> $$G_n:=\varphi\big(U_n\cap V\big)\cap B(p',\rho)\ \subseteq\ K,$$
> the image in the chart of $U_n$, intersected with the open ball. First, $\varphi(U_n\cap V)$ is **open** in $O$ (hence in $B$): $U_n\cap V$ is open in $X$ and $\varphi$ is a homeomorphism onto $O$, and $O$ is open in $B$. Therefore $G_n=\varphi(U_n\cap V)\cap B(p',\rho)$ is open in $B$, and so $G_n$ is open in the subspace $K$. Second, $G_n$ is **dense in $K$**: the set $U_n\cap V$ is dense in $V$ because $U_n$ is dense in $X$ and $V$ is open (an open set intersected with a dense set is dense in that open set — if $Y\subseteq V$ is open and nonempty then $Y$ is open in $X$, so $U_n\cap Y\ne\varnothing$ by density of $U_n$, whence $U_n\cap V$ meets $Y$); applying the homeomorphism $\varphi$, the set $\varphi(U_n\cap V)$ is dense in $O$, hence dense in $B(p',\rho)$; and the open ball $B(p',\rho)$ is dense in the closed ball $K=\overline{B}(p',\rho)$ (in a normed space every point of the sphere $\lVert x-p'\rVert=\rho$ is a limit of the radial segment $p'+t(x-p')$, $t\uparrow1$, which lies in the open ball). Composing these two densities, $G_n=\varphi(U_n\cap V)\cap B(p',\rho)$ is dense in $K$.
>
> **Step 2 — apply the Baire category theorem on the complete metric space $K$.** By Step 1, $\{G_n\}_{n\ge1}$ is a countable family of dense open subsets of the complete metric space $K$. The [[Thm - Baire Category Theorem|Baire category theorem]] — in a complete metric space, the intersection of countably many dense open subsets is dense — applies to $K$ and gives that $\bigcap_{n\ge1}G_n$ is dense in $K$, in particular nonempty.
>
> **Step 3 — pull a point back and conclude.** Take any $z\in\bigcap_{n\ge1}G_n$. For every $n$, $z\in G_n\subseteq\varphi(U_n\cap V)$, so $\varphi^{-1}(z)\in U_n\cap V\subseteq U_n$; and $\varphi^{-1}(z)\in V\subseteq W$. Hence $\varphi^{-1}(z)\in W\cap\bigcap_{n\ge1}U_n$. Since $W$ was an arbitrary nonempty open set, $\bigcap_{n\ge1}U_n$ is dense. Finally, any residual $R$ contains some such intersection $\bigcap_n U_n$, and a superset of a dense set is dense, so $R$ is dense.
>
> **Remark on the hypotheses used.** The argument used only that $X$ is *locally* modelled on a complete metric space (the completeness of the closed ball $K\subseteq B$), applied inside one chart around the arbitrary point $p$; it did not use second countability. Second countability of the Banach manifold is not needed for the Baire property itself, but it is used downstream: the [[Thm - Sard-Smale Theorem|Sard–Smale theorem]] covers $X$ by countably many charts (the Lindelöf property that second countability provides) so that the residual set of regular values is a *countable* intersection. $\blacksquare$

**Corollary 2 (residual $\iff$ meager complement).** A subset $R\subseteq X$ is residual if and only if $X\setminus R$ is meager.

> [!note]- Proof of Corollary 2
> **What must be shown.** Two implications. Write $A^c=X\setminus A$ throughout.
>
> **($\Rightarrow$) Residual implies meager complement.** Assume $R$ is residual, so $\bigcap_{n\ge1}U_n\subseteq R$ with each $U_n$ dense open. Taking complements reverses the inclusion: $R^c\subseteq\big(\bigcap_n U_n\big)^c=\bigcup_{n\ge1}U_n^c$. Each $U_n^c$ is closed (complement of an open set) and has empty interior: if $U_n^c$ contained a nonempty open set $Y$, then $Y\cap U_n=\varnothing$, contradicting the density of $U_n$. A closed set with empty interior is [[Def - Nowhere Dense and Meager|nowhere dense]] (its closure is itself). Hence $\bigcup_n U_n^c$ is a countable union of nowhere dense sets, that is meager, and $R^c$, being a subset of a meager set, is meager (a subset of a nowhere dense set is nowhere dense, so a subset of a countable union of them is again such a union).
>
> **($\Leftarrow$) Meager complement implies residual.** Assume $R^c=\bigcup_{n\ge1}A_n$ with each $A_n$ nowhere dense, that is $\operatorname{int}(\overline{A_n})=\varnothing$. Put $U_n:=X\setminus\overline{A_n}$. Each $U_n$ is **open** (complement of a closed set) and **dense**: its closure is all of $X$ precisely because $\overline{A_n}$ has empty interior (a set is dense if and only if its complement has empty interior, and $\operatorname{int}(\overline{A_n})=\varnothing$). Now
> $$\bigcap_{n\ge1}U_n=\bigcap_{n\ge1}\big(X\setminus\overline{A_n}\big)=X\setminus\bigcup_{n\ge1}\overline{A_n}\subseteq X\setminus\bigcup_{n\ge1}A_n=X\setminus R^c=R,$$
> where the inclusion holds because $A_n\subseteq\overline{A_n}$. Thus $R$ contains the countable intersection $\bigcap_n U_n$ of dense open sets, so $R$ is residual. $\blacksquare$

**Corollary 3 (countable intersections of residual sets are residual).** If $\{R_m\}_{m\ge1}$ are residual in $X$, then $\bigcap_{m\ge1}R_m$ is residual.

> [!note]- Proof of Corollary 3
> **What must be shown.** That $\bigcap_m R_m$ contains a countable intersection of dense open sets.
>
> **Proof.** For each $m$ choose, by the definition of residual, a countable family $\{U_{m,n}\}_{n\ge1}$ of dense open sets with $\bigcap_{n\ge1}U_{m,n}\subseteq R_m$. The doubly-indexed family $\{U_{m,n}\}_{(m,n)\in\mathbb{N}\times\mathbb{N}}$ is countable (a countable union of countable families is countable, since $\mathbb{N}\times\mathbb{N}$ is countable), each member is dense and open, and
> $$\bigcap_{m\ge1}\bigcap_{n\ge1}U_{m,n}=\bigcap_{(m,n)}U_{m,n}\ \subseteq\ \bigcap_{m\ge1}\Big(\bigcap_{n\ge1}U_{m,n}\Big)\ \subseteq\ \bigcap_{m\ge1}R_m,$$
> using $\bigcap_n U_{m,n}\subseteq R_m$ for each $m$ in the last step. Hence $\bigcap_m R_m$ contains a countable intersection of dense open sets and is residual. In the language of generic properties: **countably many properties that each hold generically all hold simultaneously on a residual, hence (on a Banach manifold, by Corollary 1) dense, set.** $\blacksquare$

**Calibration check.** Three verifications the reader can carry out from what is on this page. First, a finite subset $\{x_1,\dots,x_k\}$ of $\mathbb{R}^n$ is **not** residual: it is closed with empty interior, hence nowhere dense, hence meager, so by Corollary 2 its complement is residual and it is not (were it residual it would be dense by Corollary 1, but a finite set is not dense in $\mathbb{R}^n$). Second, the whole space $X$ is residual (take the single dense open set $U_1=X$, so $\bigcap U_n=X\subseteq X$), and correspondingly $\varnothing$ is meager. Third — the one to be sure of — explain why the implication "residual $\Rightarrow$ dense" *needs* the ambient to be a Baire space: exhibit, in $X=\mathbb{Q}$, the residual set $\bigcap_{q}(\mathbb{Q}\setminus\{q\})=\varnothing$, which is not dense, and identify which step of the proof of Corollary 1 fails there (there is no complete metric space to apply Baire to, because a closed ball of $\mathbb{Q}$ is not complete).

---

# Unlocked by This

> [!tip] The Sard–Smale theorem *(from this chapter)*
> The whole point of the definition is the [[Thm - Sard-Smale Theorem|Sard–Smale theorem]]: for a smooth [[Def - Fredholm Map and Its Index|Fredholm map]] $F\colon X\to Y$ between Banach manifolds, the set of **regular values** of $F$ is residual in $Y$, hence dense. This is the infinite-dimensional replacement for [[Thm - Sard's Theorem for Smooth Maps|Sard's theorem]]: "regular value" is a generic property of the target point.

> [!tip] Parametric transversality and generic parameters *(from this chapter)*
> In [[Thm - Parametric Transversality|parametric transversality]] the set of parameters $w$ for which a chosen value is regular for the individual map $\mathcal{F}_w$ is residual in the parameter space; "a generic parameter makes the equation transverse" is this statement, and it is what makes moduli spaces smooth for generic data.

> [!tip] Generic metrics and irreducibility *(from Gauge Theory XI)*
> The Freed–Uhlenbeck theorem that a **generic** Riemannian metric (or generic perturbation) makes the moduli space of irreducible solutions a smooth manifold is a residuality statement in the space of metrics; the exceptional metrics form a meager set. The Seiberg–Witten and Donaldson theories are built on such genericity, and every such "for a generic choice" is the definition on this page.
