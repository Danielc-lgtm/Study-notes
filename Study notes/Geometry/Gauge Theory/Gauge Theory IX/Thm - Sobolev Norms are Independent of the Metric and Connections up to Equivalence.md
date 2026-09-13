---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Sobolev Space of Sections"
  - "Thm - The Space of Connections is an Affine Space"
  - "Def - Compact Space"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a smooth, Hausdorff, second-countable manifold of dimension $n$ that is **compact** ([[Def - Compact Space|compact]]: every open cover has a finite subcover), and $E \to M$ is a smooth real [[Def - Vector Bundle|vector bundle]] of rank $r$. We write $\Gamma(E)$ for the space of smooth [[Def - Section of a Vector Bundle|sections]] of $E$, and $\Omega^1(M; \operatorname{End} E) = \Gamma(T^*M \otimes \operatorname{End} E)$ for the smooth $\operatorname{End} E$-valued $1$-forms.

By a **choice of Sobolev data** on $E$ we mean a quadruple $(g, \nabla^M, \nabla^E, h)$ consisting of a [[Def - Riemannian Metric|Riemannian metric]] $g$ on $M$, a [[Def - Connection on a Vector Bundle|connection]] $\nabla^M$ on the cotangent bundle $T^*M$, a connection $\nabla^E$ on $E$, and a fibre metric (a smooth field of inner products) $h$ on $E$. From such a quadruple one forms, for each integer $i \ge 0$, the bundle
$$F_i := (T^*M)^{\otimes i} \otimes E, \qquad F_0 = E,$$
carrying the induced connection $\nabla_{(i)}$ obtained from $\nabla^M$ on each cotangent factor and $\nabla^E$ on $E$ by the tensor-product (Leibniz) rule (cf. [[Def - Induced Connection on Tensor Bundles]]), and the induced fibre metric $\langle\cdot,\cdot\rangle_i$ obtained from the metric $g^{-1}$ on $T^*M$ (the fibre metric on cotangent vectors dual to $g$) and $h$ on $E$; we write $\lvert w \rvert_i = \langle w, w \rangle_i^{1/2}$ for $w \in F_i$. The **iterated covariant derivative** is defined recursively by
$$\nabla^0 u := u, \qquad \nabla^{i} u := \nabla_{(i-1)}\big(\nabla^{i-1} u\big) \in \Gamma(F_i) \quad (i \ge 1),$$
so that $\nabla^{i} u$ is the section of $F_i$ recording all covariant derivatives of $u$ up to order $i$. We write $\mathrm{vol}_g$ for the **Riemannian volume density** of $g$ — the positive measure that in any chart with coordinates $x = (x^1, \dots, x^n)$ equals $\sqrt{\det(g_{ab})}\, dx^1 \cdots dx^n$; it requires no orientation, and $\int_M f \, \mathrm{vol}_g$ is the integral of a function $f$ against it. The **Sobolev norm of order $k$** associated with the data $(g, \nabla^M, \nabla^E, h)$ is
$$\lVert u \rVert_{W^{k,2}}^2 \;:=\; \sum_{i=0}^{k} \int_M \lvert \nabla^{i} u \rvert_i^2 \, \mathrm{vol}_g, \qquad u \in \Gamma(E),$$
the object of [[Def - Sobolev Space of Sections|Def - Sobolev Space of Sections]]:

![[Def - Sobolev Space of Sections#The Definition]]

A second choice of data $(g', \nabla'^M, \nabla'^E, h')$ produces in the same way the bundles $F_i$ with a second induced connection $\nabla'_{(i)}$, a second fibre metric $\lvert\cdot\rvert'_i$, a second iterated derivative $\nabla'^{i}$, a second volume density $\mathrm{vol}_{g'}$, and a second norm $\lVert\cdot\rVert'_{W^{k,2}}$. Two norms $\lVert\cdot\rVert$ and $\lVert\cdot\rVert'$ on $\Gamma(E)$ are **equivalent** if there is a constant $C \ge 1$ with $C^{-1}\lVert u \rVert \le \lVert u \rVert' \le C \lVert u \rVert$ for every $u \in \Gamma(E)$; equivalent norms have the same Cauchy sequences and the same convergent sequences, hence the same completion.

> [!warning] Convention:
> Haydys writes the Sobolev integral simply as $\int_M$ and does not fix an orientation; on a Riemannian manifold this integral is taken against the volume density $\mathrm{vol}_g$ defined above, which exists whether or not $M$ is orientable. We use the density throughout, so no orientation is assumed anywhere on this page. Haydys states the equivalence of norms (the paragraph after his Theorem 136, p. 45, item A-I5.1.5, and Remark A-R5.1.3) **without proof**, as a remark that "different choices yield equivalent norms so that the resulting topology is independent of the choices made"; the complete proof below is supplied by these notes.

---

# Statement

> **Theorem (Sobolev norms are independent of the data up to equivalence).** Let $M$ be a compact $n$-manifold and $E \to M$ a smooth vector bundle. Let $(g, \nabla^M, \nabla^E, h)$ and $(g', \nabla'^M, \nabla'^E, h')$ be any two choices of Sobolev data on $E$, with associated Sobolev norms $\lVert\cdot\rVert_{W^{k,2}}$ and $\lVert\cdot\rVert'_{W^{k,2}}$ on $\Gamma(E)$. Then for every integer $k \ge 0$ the two norms are equivalent: there is a constant $C_k \ge 1$, depending on the two data sets and on $k$ but not on the section, with
> $$C_k^{-1}\,\lVert u \rVert_{W^{k,2}} \;\le\; \lVert u \rVert'_{W^{k,2}} \;\le\; C_k\,\lVert u \rVert_{W^{k,2}} \qquad \text{for all } u \in \Gamma(E).$$
> Consequently the completion $W^{k,2}(M; E)$ of $\Gamma(E)$ in the Sobolev norm is well defined, independently of the choice of data, as a topological vector space; being the completion of an inner-product norm, it is a Hilbertable space (it carries a Hilbert-space structure, canonical only up to the equivalent inner products the data provide).

> **Companion form (all exponents).** The same conclusion holds for the $W^{k,p}$ norms $\lVert u \rVert_{W^{k,p}}^p = \sum_{i=0}^k \int_M \lvert \nabla^{i} u \rvert_i^p \, \mathrm{vol}_g$ for every real $p \ge 1$: any two choices of data give equivalent $W^{k,p}$ norms, so $W^{k,p}(M; E)$ is well defined as a topological vector space, independently of the data.

The two forms are tied together by the proof: the argument for $p = 2$ uses only the triangle inequality, one Cauchy–Schwarz (or power-mean) estimate, and uniform bounds coming from compactness, and each of these has a version valid for every $p \ge 1$. The main statement is the case $p = 2$, which is the one the rest of the chapter uses; the companion form is recorded because the source states it for all $p > 1$.

---

# Motivation

The definition of the Sobolev norm on sections of a bundle is not canonical: to write down $\lVert u \rVert_{W^{k,2}}$ one must first choose a Riemannian metric $g$ (to measure the length of covariant derivatives and to integrate over $M$), connections $\nabla^M$ and $\nabla^E$ (to form the covariant derivatives in the first place), and a fibre metric $h$ on $E$ (to measure the value of $u$ itself). None of these choices is forced by the bundle $E$ alone. A reader meeting the definition is therefore owed an answer to an immediate and honest worry: **is the resulting analysis an artefact of the choices, or does it describe the bundle?** If two people set up Sobolev theory on the same $E$ with different metrics and connections, do they obtain the same spaces of sections, the same notion of convergence, the same completed function spaces — or do their theories merely resemble one another?

This is not a pedantic worry; it is the hinge on which the whole application of Sobolev theory to gauge theory turns. In gauge theory the object of study is a space of connections $\mathcal{A}(E)$ and a group of gauge transformations $\mathcal{G}(E)$ acting on it, and to do analysis one completes these in Sobolev norms. But a connection is exactly one of the ingredients that goes into defining a Sobolev norm, so there is a genuine circularity to dispel: the reference connection used to build the norm is itself a point of the space one is trying to topologise. If different reference connections gave inequivalent norms, the Sobolev completion $\mathcal{A}^{k,2}(E)$ would depend on an arbitrary base point and the configuration space of the theory would not be well defined. The theorem removes the circularity in one stroke: because any two connections give equivalent norms, the completion does not see the base point at all.

The reason the answer is clean, and the reason it is worth isolating as a theorem rather than folding into the definition, is a structural fact about connections that is easy to state and easy to underestimate. **The difference of two connections is not a differential operator but a tensor** — a zeroth-order, algebraic object, by [[Thm - The Space of Connections is an Affine Space|the affine structure of the space of connections]]. Changing $\nabla^E$ to $\nabla'^E$ therefore changes the first covariant derivative $\nabla u$ only by adding $a \cdot u$, where $a$ is a fixed smooth $1$-form with values in $\operatorname{End} E$; it does not touch the top-order part of the derivative at all. Iterating, the $i$-th derivative changes only by lower-order terms with smooth coefficients. On a compact manifold a smooth object is bounded, so those lower-order corrections, and the discrepancies between the two metrics and the two volume densities, are all controlled by constants — and constants are exactly what an equivalence of norms is made of. The theorem is thus the meeting point of two facts, one algebraic (a connection difference is a tensor) and one topological (a continuous function on a compact space is bounded).

We will assume the reader is comfortable with connections on vector bundles, the induced connections on tensor products, the affine structure of the space of connections, and the elementary theory of compactness; the argument requires nothing from measure theory beyond the existence of the Riemannian volume density and the monotonicity of the integral.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypotheses are mild — a compact base, a vector bundle, two choices of smooth data — so the useful question is: when does a problem secretly present a *compact* base, so that the theorem applies even though compactness is not announced?

The first disguised source is **a base that is a closed (compact boundaryless) submanifold, or more generally a closed subset of an already-compact space**. A projective variety, a level set of a proper submersion, a closed orbit of a compact group, a closed geodesic sphere — each is compact by the bridge "a closed subset of a compact space is compact", and any such subset that is a submanifold carries vector bundles to which the theorem applies verbatim. The non-obvious part is recognising that "closed and sitting inside something compact" is enough: one never has to exhibit a finite subcover by hand. *Example problem:* show that on the flag manifold $U(n)/T$ (a closed submanifold of a product of Grassmannians, hence compact) the Sobolev completion of sections of a homogeneous bundle does not depend on which invariant metric is used.

The second disguised source is **a base that is the total space of a fibre bundle with compact fibre over a compact base**, such as a sphere bundle, a projectivised bundle, a flag bundle, or a principal bundle for a compact structure group. The bridge is precisely the compactness lemma proved below (Lemma 1 in the rank-of-the-fibre setting): a fibre bundle with compact base and compact fibre has compact total space, because finitely many local trivialisations cover the base and each contributes a compact piece. The non-obviousness is that one gets compactness of a higher-dimensional space for free from compactness of two lower-dimensional ones. *Example problem:* set up Sobolev spaces of sections over the unit tangent bundle $S(TM)$ of a compact $M$ and conclude they are metric-independent.

The third disguised source is **a base presented as a cocompact quotient**, $M = \widetilde{M}/\Gamma$, where a discrete group $\Gamma$ acts freely and properly with compact quotient — the torus $\mathbb{R}^n/\mathbb{Z}^n$, a closed hyperbolic manifold $\mathbb{H}^n/\Gamma$, a nilmanifold. The bridge is that cocompactness *is* compactness of $M$; the covering space $\widetilde{M}$ may be non-compact, but the theorem is about $M$. The non-obviousness is that a $\Gamma$-invariant metric and connection upstairs descend to data downstairs, so equivalence of the downstairs norms follows even though one naturally computes upstairs. *Example problem:* show that Fourier-based and heat-kernel-based Sobolev norms on the flat torus agree up to equivalence, an instance of the theorem with $\widetilde{M} = \mathbb{R}^n$.

**Targets (Output Amplification).** The bare conclusion is an equivalence of norms. Combined with other results it produces the well-definedness on which the analysis of gauge theory rests.

Combine the conclusion with **the [[Def - Sobolev Space of Sections|Sobolev embedding theorem]]** ($W^{k,2}(M; E) \hookrightarrow C^0(M; E)$ for $2k > n$, and its higher-regularity refinements). The embedding is stated for *the* space $W^{k,2}(M; E)$; the present theorem is what licenses that definite article, because it shows the source space of the embedding is the same topological vector space no matter which data defined it. The payoff is that elliptic bootstrapping — "if $u \in W^{k,2}$ and $Pu$ is smooth then $u$ is smooth" — is a statement about the bundle, not about a gauge choice, and can be run in whatever gauge is convenient.

Combine the conclusion with **the affine structure of the space of connections** ([[Thm - The Space of Connections is an Affine Space]]). A Sobolev connection is defined as $\nabla_0 + a$ with $a \in W^{k,2}(\Omega^1(M; \operatorname{End} E))$ for a fixed smooth reference $\nabla_0$; the resulting configuration space $\mathcal{A}^{k,2}(E) = \nabla_0 + W^{k,2}(\Omega^1(M; \operatorname{End} E))$ is a priori attached to $\nabla_0$. The extra ingredient is that any two smooth reference connections differ by a smooth (hence $W^{k,2}$) $1$-form, and the present theorem says the $W^{k,2}$ topology on the affine part is independent of the metric-and-connection data. The payoff is that $\mathcal{A}^{k,2}(E)$ is a well-defined affine Hilbert manifold, the true configuration space of gauge theory, with no dependence on the base point.

Combine the conclusion with **the [[Def - Sobolev Space of Sections|Rellich compactness theorem]]** (the embedding $W^{k,2} \hookrightarrow W^{m,2}$ is compact for $k > m$). Compactness of an operator is a topological property of the pair of spaces; because both spaces are data-independent by the present theorem, the compactness of the embedding is too. The payoff is that the compactness arguments underlying moduli-space theory — extracting convergent subsequences of connections modulo gauge — do not depend on the metric or reference connection used to set up the Sobolev spaces, which is what makes the quotient $\mathcal{A}^{k,2}/\mathcal{G}^{k+1,2}$ a well-defined topological space.

---

# Why Is It True

Strip away the bookkeeping and one mechanism is doing all the work. Two connections on the same bundle never disagree about the *leading* term of a derivative; they can disagree only about lower-order corrections, and those corrections are tensorial — pointwise-linear, with smooth coefficients. On a compact base a smooth coefficient cannot run off to infinity, so every such correction is uniformly bounded. Likewise, two Riemannian metrics on a compact base are uniformly comparable, and their two volume densities differ by a smooth positive factor that is bounded above and below. An equivalence of norms is exactly an assertion that two ways of measuring differ by bounded factors, so once every discrepancy has been shown to be a bounded factor, the equivalence is assembled by the triangle inequality.

> **The mechanism in one sentence: the difference of two connections is a tensor, not a differential operator, so changing the data perturbs each iterated derivative only by lower-order terms with smooth coefficients, and on a compact manifold every smooth coefficient is bounded — bounded discrepancies are precisely what an equivalence of norms records.**

It is worth seeing why the leading terms agree, because that is the crux. On $E$ the two connections satisfy $\nabla'^E = \nabla^E + a$ with $a$ a smooth $\operatorname{End} E$-valued $1$-form. The Leibniz rule for a connection, $\nabla(f s) = df \otimes s + f\,\nabla s$, has its top-order piece $df \otimes s$ *independent of the connection* — it is the same $df$ for $\nabla^E$ and for $\nabla'^E$. All the connection-dependence sits in the zeroth-order piece. Iterating a connection therefore produces a top-order part (repeated ordinary differentiation, common to both towers) plus a cascade of lower-order corrections, each of which is a smooth tensor contracted against a lower derivative. When one measures $\nabla'^{i}u$ in the primed metric and integrates against the primed volume, one is measuring $\nabla^{i}u$ plus bounded-coefficient combinations of $\nabla^{0}u, \dots, \nabla^{i-1}u$, in a metric comparable to the unprimed one, against a comparable volume — and every one of those pieces is already part of the unprimed norm $\lVert u \rVert_{W^{k,2}}$. The primed norm is thus dominated by the unprimed one, and, the hypotheses being symmetric in the two data sets, vice versa.

---

# What Makes This Hard

The one genuinely non-obvious point is the *order count*: it is tempting to fear that the $i$-th derivative in one connection differs from the $i$-th derivative in the other by something of order $i$ — another $i$-th derivative with a different coefficient — which would make the discrepancy the same size as the term itself and forbid any clean domination. The content of the theorem is that this does not happen: the top-order parts coincide, and the difference $\nabla'^{i}u - \nabla^{i}u$ involves only derivatives of order **strictly less than $i$**. Getting the induction to record this faithfully — that each correction term $P_{ij}$ maps a $j$-th derivative with $j < i$ into the $i$-th slot, never an $i$-th into the $i$-th — is the step where a careless argument goes wrong. The second, quieter difficulty is bundling the many comparisons (one fibre-metric comparison on each $F_i$, one operator bound for each correction coefficient, one volume comparison) into finitely many uniform constants; this is legitimate only because $k$ is finite and each comparison is a maximum of a continuous function over a compact space, which the extreme value theorem guarantees is attained and finite.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Show the primed norm is dominated by a constant times the unprimed norm; the reverse follows by exchanging the two symmetric data sets, and the two inequalities together are the equivalence. To get the domination, control three sources of discrepancy by constants — the two fibre metrics on each derivative bundle, the two volume densities, and the difference between the two iterated derivatives — and combine them by the triangle inequality, summing over the finitely many derivative orders $i \le k$.

**Subgoal decomposition:**

1. **Uniform comparison of pointwise data over a compact base.**
   - *Hint:* A positive continuous function on a compact space attains a positive minimum and a finite maximum; apply this to the ratio of two fibre metrics on the unit sphere bundle, to the operator norm of a smooth bundle map, and to the smooth positive density ratio $\mathrm{vol}_{g'}/\mathrm{vol}_g$.
   - *Why needed:* Every discrepancy in the final estimate must become a constant; compactness is what turns "smooth" into "bounded".

2. **The connection difference is zeroth order, and iterating keeps corrections of lower order.**
   - *Hint:* Write $\nabla'^E = \nabla^E + a$ and $\nabla'^M = \nabla^M + b$ with $a, b$ smooth tensors (affine structure); use the tensor-product Leibniz rule to expand $\nabla'^{i}u$ and induct on $i$, checking that new terms carry derivatives of order $< i$.
   - *Why needed:* This is the order count that makes each derivative term dominated by lower-order terms already inside the unprimed norm.

3. **Assemble the one-sided estimate and symmetrise.**
   - *Hint:* Bound the $i$-th primed term using subgoals 1 and 2, sum over $i \le k$ to get $\lVert u \rVert' \le C_k \lVert u \rVert$, then exchange the roles of the data sets.
   - *Why needed:* It converts the pointwise/term-by-term bounds into the required norm inequality in both directions.

4. **Pass to completions.**
   - *Hint:* Equivalent norms have identical Cauchy and convergent sequences, so the identity of $\Gamma(E)$ extends to a linear homeomorphism of completions.
   - *Why needed:* The stated conclusion is about the completed space $W^{k,2}(M; E)$, not only about $\Gamma(E)$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The unit sphere bundle of a vector bundle over a compact base is compact
> **Statement:** Let $F \to M$ be a smooth vector bundle over a compact manifold $M$, and let $\langle\cdot,\cdot\rangle$ be a fibre metric on $F$ with norm $\lvert\cdot\rvert$. Then the unit sphere bundle $S(F) := \{\, w \in F : \lvert w \rvert = 1 \,\}$ is compact.
>
> **Hint:** Cover $M$ by finitely many trivialising opens; over each, $S(F)$ looks like a piece of $M$ times a Euclidean sphere, which is compact.
>
> **Why needed:** It is the space on which we take the maximum and minimum of a ratio of fibre metrics in Lemma 2; without its compactness the extreme value theorem does not apply.
>
> > [!note]- Full proof
> > **Reduce to a finite trivialising cover.** By local triviality of the vector bundle ([[Def - Local Trivialization|local trivialisation]]), every point of $M$ has an open neighbourhood over which $F$ is trivial. These neighbourhoods form an open cover of $M$; since $M$ is [[Def - Compact Space|compact]], finitely many of them, say $U_1, \dots, U_N$, already cover $M$ (by the definition of compactness). On each $U_\alpha$ fix a trivialisation $\Phi_\alpha : F|_{U_\alpha} \xrightarrow{\ \cong\ } U_\alpha \times \mathbb{R}^r$.
> >
> > **Shrink to a cover by compact sets.** A compact manifold is normal, so the finite open cover $(U_\alpha)$ admits a shrinking: there are opens $V_\alpha$ with closures $\overline{V_\alpha} \subset U_\alpha$ and $\bigcup_\alpha V_\alpha = M$ (this is the standard shrinking lemma for a finite open cover of a normal space, obtained by shrinking one set at a time while preserving the covering property). Each $\overline{V_\alpha}$ is a closed subset of the compact space $M$, hence compact.
> >
> > **Each piece of $S(F)$ is compact.** Fix $\alpha$. Under $\Phi_\alpha$, the fibre metric $\langle\cdot,\cdot\rangle$ becomes, at each $p \in U_\alpha$, an inner product on $\mathbb{R}^r$ depending smoothly on $p$; write $\lvert w \rvert^2 = v^\top G_\alpha(p)\, v$ for $w \in F_p$ with $\Phi_\alpha(w) = (p, v)$ and $G_\alpha(p)$ a smooth positive-definite symmetric matrix. Then
> > $$S(F)\big|_{\overline{V_\alpha}} \;=\; \Phi_\alpha^{-1}\big(\{\, (p, v) \in \overline{V_\alpha} \times \mathbb{R}^r : v^\top G_\alpha(p)\, v = 1 \,\}\big).$$
> > The set inside braces is a closed subset of $\overline{V_\alpha} \times \mathbb{R}^r$ (it is the zero set of the continuous function $(p, v) \mapsto v^\top G_\alpha(p) v - 1$) and it is bounded, because $v^\top G_\alpha(p) v = 1$ with $G_\alpha(p)$ having a positive smallest eigenvalue $\lambda_\alpha(p)$ that attains a positive minimum $\lambda_\alpha^{\min} > 0$ over the compact set $\overline{V_\alpha}$ (extreme value theorem, [[Ex - A Continuous Function on a Compact Manifold Attains its Maximum|a continuous function on a compact set attains its extrema]]), whence $\lvert v \rvert_{\mathrm{eucl}}^2 \le \lambda_\alpha^{\min\,-1}$; a closed and bounded subset of $\overline{V_\alpha} \times \mathbb{R}^r$ is compact by the [[Thm - Heine–Borel Theorem|Heine–Borel theorem]] applied in the Euclidean factor together with compactness of $\overline{V_\alpha}$. As the continuous image (under the homeomorphism $\Phi_\alpha^{-1}$) of a compact set, $S(F)|_{\overline{V_\alpha}}$ is compact.
> >
> > **Assemble.** Since $\bigcup_\alpha V_\alpha = M$ we have $S(F) = \bigcup_{\alpha=1}^N S(F)|_{\overline{V_\alpha}}$, a finite union of compact sets, and a finite union of compact sets is compact. Therefore $S(F)$ is compact. $\blacksquare$

> [!note]- Lemma 2: Uniform comparison of smooth pointwise data over a compact base
> **Statement:** Let $M$ be compact.
> **(a)** For any two fibre metrics $\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle'$ on a vector bundle $F \to M$ there are constants $0 < c \le C < \infty$ with $c\,\lvert w \rvert^2 \le \lvert w \rvert'^2 \le C\,\lvert w \rvert^2$ for every $w \in F$.
> **(b)** For any smooth bundle homomorphism $P : F \to F'$ between bundles carrying fixed fibre metrics there is a constant $K < \infty$ with $\lvert P(p)\, w \rvert' \le K\,\lvert w \rvert$ for every $p \in M$ and $w \in F_p$.
> **(c)** For any two Riemannian metrics $g, g'$ on $M$ the volume densities satisfy $\mathrm{vol}_{g'} = \rho\,\mathrm{vol}_g$ for a smooth positive function $\rho$, and there are constants $0 < c_0 \le C_0 < \infty$ with $c_0\,\mathrm{vol}_g \le \mathrm{vol}_{g'} \le C_0\,\mathrm{vol}_g$ as measures.
>
> **Hint:** In each case exhibit the discrepancy as a continuous positive function on a compact space and take its extrema.
>
> **Why needed:** Parts (a) and (c) turn "the metrics and volumes differ" into two constants; part (b) turns "the correction coefficients are smooth" into finitely many constants. These are the numbers the final estimate is built from.
>
> > [!note]- Full proof
> > **(a) Comparison of fibre metrics.** Consider the function
> > $$q : S(F) \to \mathbb{R}, \qquad q(w) := \lvert w \rvert'^2 = \langle w, w \rangle',$$
> > defined on the unit sphere bundle $S(F) = \{ \lvert w \rvert = 1 \}$, which is compact by **Lemma 1**. The function $q$ is continuous (it is the restriction of the smooth fibre-quadratic-form $w \mapsto \langle w, w\rangle'$) and strictly positive (a fibre metric is positive definite, so $\langle w, w\rangle' > 0$ for $w \ne 0$, and every $w \in S(F)$ is nonzero). By the extreme value theorem ([[Ex - A Continuous Function on a Compact Manifold Attains its Maximum|a continuous function on a compact set attains its maximum and minimum]]) $q$ attains a minimum $c := \min_{S(F)} q$ and a maximum $C := \max_{S(F)} q$, and $0 < c \le C < \infty$ because $q$ is positive. Now take any $w \in F$. If $w = 0$ the inequality $c\,\lvert w\rvert^2 \le \lvert w\rvert'^2 \le C\,\lvert w\rvert^2$ reads $0 \le 0 \le 0$ and holds. If $w \ne 0$, set $\hat w := w/\lvert w \rvert \in S(F)$; then $c \le q(\hat w) \le C$, and since both $\lvert\cdot\rvert^2$ and $\lvert\cdot\rvert'^2$ are homogeneous of degree $2$,
> > $$\lvert w \rvert'^2 = \lvert w \rvert^2\, q(\hat w) \qquad \text{(homogeneity: } \lvert w\rvert'^2 = \lvert\, \lvert w\rvert \hat w\,\rvert'^2 = \lvert w\rvert^2\,\lvert \hat w\rvert'^2 = \lvert w\rvert^2\, q(\hat w)\text{)},$$
> > so $c\,\lvert w\rvert^2 \le \lvert w \rvert'^2 \le C\,\lvert w\rvert^2$. This proves (a).
> >
> > **(b) Boundedness of a smooth bundle map.** Consider
> > $$\Psi : S(F) \to \mathbb{R}, \qquad \Psi(w) := \lvert P(p)\, w \rvert' \ \text{ for } w \in F_p,\ \lvert w\rvert = 1,$$
> > on the compact space $S(F)$ (Lemma 1). It is continuous, being the composite of the smooth bundle map $P$ (continuous) with the continuous fibre norm $\lvert\cdot\rvert'$ on $F'$. By the extreme value theorem it attains a finite maximum $K := \max_{S(F)} \Psi < \infty$. For any $p$ and any $w \in F_p$: if $w = 0$ then $P(p) w = 0$ and $\lvert P(p) w\rvert' = 0 \le K\,\lvert w\rvert$; if $w \ne 0$ then $\hat w = w/\lvert w\rvert \in S(F)$ and, since $P(p)$ is linear on the fibre,
> > $$\lvert P(p)\, w \rvert' = \lvert w\rvert\,\lvert P(p)\,\hat w\rvert' = \lvert w\rvert\,\Psi(\hat w) \le K\,\lvert w\rvert \qquad \text{(linearity of } P(p) \text{ and homogeneity of the norm; } \Psi(\hat w) \le K\text{)}.$$
> > This proves (b).
> >
> > **(c) Comparison of volume densities.** Work in an arbitrary coordinate chart $x = (x^1, \dots, x^n)$ on an open $U \subseteq M$. There $\mathrm{vol}_g = \sqrt{\det(g_{ab})}\, dx$ and $\mathrm{vol}_{g'} = \sqrt{\det(g'_{ab})}\, dx$, where $(g_{ab})$ and $(g'_{ab})$ are the smooth positive-definite matrices of $g$ and $g'$ in these coordinates and $dx = dx^1\cdots dx^n$. Hence on $U$
> > $$\mathrm{vol}_{g'} = \rho\,\mathrm{vol}_g, \qquad \rho := \sqrt{\frac{\det(g'_{ab})}{\det(g_{ab})}} \qquad \text{(dividing the two coordinate expressions; } \det(g_{ab}) > 0 \text{ since } g \text{ is positive definite)}.$$
> > The function $\rho$ is smooth and positive on $U$; and it is independent of the chart, because both $\mathrm{vol}_g$ and $\mathrm{vol}_{g'}$ are intrinsically defined densities, so their ratio is a well-defined global smooth positive function $\rho \in C^\infty(M)$ (on an overlap $U \cap U'$ the two coordinate formulas for $\rho$ agree, being the same ratio of the same two densities). Since $M$ is compact and $\rho$ is continuous and positive, the extreme value theorem gives $c_0 := \min_M \rho > 0$ and $C_0 := \max_M \rho < \infty$, whence $c_0\,\mathrm{vol}_g \le \mathrm{vol}_{g'} \le C_0\,\mathrm{vol}_g$ as measures (for a non-negative integrand $f$, $c_0 \int_M f\,\mathrm{vol}_g \le \int_M f\rho\,\mathrm{vol}_g = \int_M f\,\mathrm{vol}_{g'} \le C_0 \int_M f\,\mathrm{vol}_g$, by monotonicity of the integral applied to $c_0 f \le \rho f \le C_0 f$). This proves (c). $\blacksquare$

> [!note]- Lemma 3: The difference of iterated covariant derivatives is a lower-order tensorial correction
> **Statement:** With the two Sobolev data sets fixed, for every $i \ge 0$ there exist smooth bundle homomorphisms $P_{ij} : F_j \to F_i$ for $0 \le j \le i-1$ (that is, $P_{ij} \in \Gamma(\operatorname{Hom}(F_j, F_i))$) such that
> $$\nabla'^{i} u \;=\; \nabla^{i} u \;+\; \sum_{j=0}^{i-1} P_{ij}\big(\nabla^{j} u\big) \qquad \text{for all } u \in \Gamma(E),$$
> where $\nabla^{i}, \nabla'^{i}$ are the iterated covariant derivatives of the two data sets. In particular the top-order parts coincide and every correction term carries a derivative of order strictly less than $i$.
>
> **Hint:** By the affine structure of connections, $\nabla'^E = \nabla^E + a$ and $\nabla'^M = \nabla^M + b$ with $a, b$ smooth $1$-forms valued in the respective endomorphism bundles; the induced connections on $F_i$ then differ by a smooth $\operatorname{End} F_i$-valued $1$-form, and one inducts on $i$ with the Leibniz rule.
>
> **Why needed:** This is the order count. It says that measuring $\nabla'^{i}u$ is the same as measuring $\nabla^{i}u$ up to bounded-coefficient combinations of lower derivatives already present in the unprimed norm.
>
> > [!note]- Full proof
> > **Step A — the connection differences are tensors.** By [[Thm - The Space of Connections is an Affine Space|the affine structure of the space of connections]], restated here:
> > > for any two connections $\nabla, \hat\nabla$ on a vector bundle $V \to M$, the difference $\nabla - \hat\nabla : \Gamma(V) \to \Omega^1(M; V)$ is $C^\infty(M)$-linear, hence is given by a unique $\alpha \in \Omega^1(M; \operatorname{End} V)$ via $(\nabla - \hat\nabla)s = \alpha \cdot s$.
> >
> > Applying this with $V = E$ gives a smooth $a \in \Omega^1(M; \operatorname{End} E)$ with $\nabla'^E s = \nabla^E s + a \cdot s$; applying it with $V = T^*M$ gives a smooth $b \in \Omega^1(M; \operatorname{End} T^*M)$ with $\nabla'^M \xi = \nabla^M \xi + b \cdot \xi$. Both $a$ and $b$ are smooth, being global smooth tensor fields.
> >
> > **Step B — the induced connections on $F_i$ differ by a smooth $\operatorname{End} F_i$-valued $1$-form.** The connection $\nabla_{(i)}$ on $F_i = (T^*M)^{\otimes i} \otimes E$ is the tensor-product connection built from $i$ copies of $\nabla^M$ and one copy of $\nabla^E$ (cf. [[Def - Induced Connection on Tensor Bundles]], whose defining Leibniz rule over tensor products we use). We claim that if two connections on vector bundles $V$ and $W$ differ by $\alpha \in \Omega^1(M; \operatorname{End} V)$ and $\beta \in \Omega^1(M; \operatorname{End} W)$ respectively, then the induced connections on $V \otimes W$ differ by $\alpha \otimes \mathrm{Id}_W + \mathrm{Id}_V \otimes \beta \in \Omega^1(M; \operatorname{End}(V \otimes W))$. Indeed, on a decomposable section $v \otimes w$ ($v \in \Gamma(V)$, $w \in \Gamma(W)$),
> > $$\nabla'_{V \otimes W}(v \otimes w) = \nabla'_V v \otimes w + v \otimes \nabla'_W w \qquad \text{(tensor-product Leibniz rule for } \nabla'\text{)}$$
> > $$= (\nabla_V v + \alpha\cdot v)\otimes w + v \otimes (\nabla_W w + \beta \cdot w) \qquad \text{(the two connection differences)}$$
> > $$= \nabla_{V\otimes W}(v\otimes w) + (\alpha\cdot v)\otimes w + v \otimes (\beta\cdot w) \qquad \text{(tensor-product Leibniz rule for } \nabla\text{, regrouping)},$$
> > and the last two terms are exactly $(\alpha \otimes \mathrm{Id}_W + \mathrm{Id}_V \otimes \beta)(v \otimes w)$. As both sides are $C^\infty(M)$-linear in the section and decomposable sections span $\Gamma(V \otimes W)$ over $C^\infty(M)$, the identity holds on all sections; the difference is therefore the stated smooth $1$-form. Applying this repeatedly across the $i+1$ tensor factors of $F_i$, we obtain a smooth $c_i \in \Omega^1(M; \operatorname{End} F_i)$ with
> > $$\nabla'_{(i)} \sigma = \nabla_{(i)} \sigma + c_i \cdot \sigma \qquad \text{for all } \sigma \in \Gamma(F_i),$$
> > where $c_i = \sum_{\ell=1}^{i}\big(\mathrm{Id}^{\otimes(\ell-1)} \otimes b \otimes \mathrm{Id}^{\otimes(i-\ell)} \otimes \mathrm{Id}_E\big) + \big(\mathrm{Id}_{(T^*M)^{\otimes i}} \otimes a\big)$ is smooth.
> >
> > **Step C — induction on $i$.** For $i = 0$ the claim reads $\nabla'^0 u = \nabla^0 u$, i.e. $u = u$, with the empty sum on the right; this is true. Assume the claim for $i-1$ (with $i \ge 1$): there are smooth $P_{i-1,j} \in \Gamma(\operatorname{Hom}(F_j, F_{i-1}))$, $0 \le j \le i-2$, with
> > $$\nabla'^{\,i-1} u = \nabla^{i-1} u + \sum_{j=0}^{i-2} P_{i-1,j}\big(\nabla^{j} u\big).$$
> > Apply $\nabla'_{(i-1)} = \nabla_{(i-1)} + c_{i-1}\cdot$ (Step B) to both sides and use the definition $\nabla'^{i} u = \nabla'_{(i-1)}(\nabla'^{\,i-1}u)$:
> > $$\nabla'^{i} u = \nabla_{(i-1)}\Big(\nabla^{i-1}u + \sum_{j=0}^{i-2} P_{i-1,j}(\nabla^{j}u)\Big) + c_{i-1}\cdot\Big(\nabla^{i-1}u + \sum_{j=0}^{i-2}P_{i-1,j}(\nabla^{j}u)\Big).$$
> > Evaluate the first group term by term. First, $\nabla_{(i-1)}(\nabla^{i-1}u) = \nabla^{i} u$ by the definition of the iterated derivative. Second, for each $j \le i-2$, the Leibniz rule for the induced connection on the homomorphism bundle $\operatorname{Hom}(F_j, F_{i-1})$ (paired with $F_j$) gives
> > $$\nabla_{(i-1)}\big(P_{i-1,j}(\nabla^{j}u)\big) = \big(\nabla^{\operatorname{Hom}} P_{i-1,j}\big)\!\cdot\!\big(\nabla^{j}u\big) + P_{i-1,j}\big(\nabla_{(j)}\nabla^{j}u\big) \qquad \text{(Leibniz rule for } \nabla \text{ acting on a homomorphism applied to a section)},$$
> > where $\nabla^{\operatorname{Hom}} P_{i-1,j} \in \Omega^1(M; \operatorname{Hom}(F_j, F_{i-1}))$ is smooth and, contracted with the $1$-form slot into $F_i$, defines a smooth homomorphism $F_j \to F_i$; and $\nabla_{(j)}\nabla^{j}u = \nabla^{j+1}u$ with $P_{i-1,j}$ regarded, after including $F_{i-1} \hookrightarrow F_i$ via the outer derivative slot, as a smooth homomorphism $F_{j+1} \to F_i$. Thus $\nabla_{(i-1)}(P_{i-1,j}(\nabla^{j}u))$ is a sum of a smooth homomorphism applied to $\nabla^{j}u$ (order $j \le i-2$) and a smooth homomorphism applied to $\nabla^{j+1}u$ (order $j+1 \le i-1$). Third, $c_{i-1}\cdot\nabla^{i-1}u$ is a smooth homomorphism ($c_{i-1}$ contracted into $F_i$) applied to $\nabla^{i-1}u$ (order $i-1$), and $c_{i-1}\cdot P_{i-1,j}(\nabla^{j}u)$ is a smooth homomorphism applied to $\nabla^{j}u$ (order $j \le i-2$).
> >
> > **Collect by order.** Every term produced above, apart from the single $\nabla^{i}u$, is a smooth bundle homomorphism into $F_i$ applied to some $\nabla^{m}u$ with $m \le i-1$. Grouping the coefficients of each $\nabla^{m}u$, $0 \le m \le i-1$, into a single smooth homomorphism $P_{im} \in \Gamma(\operatorname{Hom}(F_m, F_i))$ (a finite sum of smooth homomorphisms is a smooth homomorphism), we obtain
> > $$\nabla'^{i} u = \nabla^{i}u + \sum_{m=0}^{i-1} P_{im}\big(\nabla^{m}u\big),$$
> > which is the claim for $i$. By induction it holds for all $i \ge 0$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $(g, \nabla^M, \nabla^E, h)$ and $(g', \nabla'^M, \nabla'^E, h')$ be two choices of Sobolev data on $E \to M$, $M$ compact, and fix an integer $k \ge 0$. We must produce a constant $C_k \ge 1$ with $C_k^{-1}\lVert u\rVert_{W^{k,2}} \le \lVert u\rVert'_{W^{k,2}} \le C_k\lVert u\rVert_{W^{k,2}}$ for all $u \in \Gamma(E)$, and then pass to completions. Throughout, $\lvert\cdot\rvert_i$ and $\lvert\cdot\rvert'_i$ denote the unprimed and primed fibre norms on $F_i = (T^*M)^{\otimes i}\otimes E$, and $\nabla^{i}, \nabla'^{i}$ the two iterated covariant derivatives.
>
> **Step 0 — the two norms are well-defined norms, and the estimate need only be proved in one direction.** The map $u \mapsto \lVert u \rVert_{W^{k,2}}$ is a norm on $\Gamma(E)$: it is finite (each $\nabla^{i}u$ is a smooth section of $F_i$, so $\lvert\nabla^{i}u\rvert_i^2$ is a continuous function on the compact $M$, hence bounded and integrable against the finite measure $\mathrm{vol}_g$), it is homogeneous and satisfies the triangle inequality (it is the norm of the vector $(\nabla^{0}u, \dots, \nabla^{k}u)$ in the Hilbert space $\bigoplus_{i=0}^k L^2(F_i)$), and it is positive definite: if $\lVert u\rVert_{W^{k,2}} = 0$ then in particular $\int_M \lvert u\rvert_0^2\,\mathrm{vol}_g = 0$, and since $\lvert u\rvert_0^2$ is a non-negative continuous function whose integral against the strictly positive density $\mathrm{vol}_g$ vanishes, $\lvert u\rvert_0^2 \equiv 0$, so $u \equiv 0$. The same holds for the primed norm. The hypotheses on the two data sets are symmetric — nothing distinguishes primed from unprimed — so once we prove $\lVert u\rVert'_{W^{k,2}} \le C_k \lVert u\rVert_{W^{k,2}}$ with $C_k$ independent of $u$, exchanging the two data sets yields $\lVert u\rVert_{W^{k,2}} \le C_k'\lVert u\rVert'_{W^{k,2}}$, and $\max(C_k, C_k')$ is a constant witnessing the equivalence. We therefore prove the one-sided estimate.
>
> **Step 1 — the uniform constants.** Apply **Lemma 2** to the finitely many bundles and maps that appear for $i \le k$:
> - by Lemma 2(a) on each $F_i$ ($0 \le i \le k$), there is $A_i \ge 1$ with $\lvert w\rvert'^2_i \le A_i\,\lvert w\rvert_i^2$ for all $w \in F_i$;
> - by Lemma 2(c), there is $C_0 < \infty$ with $\mathrm{vol}_{g'} \le C_0\,\mathrm{vol}_g$ as measures;
> - by **Lemma 3**, $\nabla'^{i}u = \nabla^{i}u + \sum_{j=0}^{i-1} P_{ij}(\nabla^{j}u)$ with smooth $P_{ij} : F_j \to F_i$, and by Lemma 2(b) each such $P_{ij}$ has a bound $K_{ij} < \infty$ with $\lvert P_{ij}(p)w\rvert_i \le K_{ij}\lvert w\rvert_j$ for all $p, w$. Set $K_{ii} := 1$ and $K_{ij} := 0$ for $j > i$.
>
> All of $A_i, C_0, K_{ij}$ are finite and depend only on the two data sets and on $k$, not on $u$.
>
> **Step 2 — pointwise bound on each iterated derivative.** Fix $u \in \Gamma(E)$ and $0 \le i \le k$. Measuring the Lemma 3 expansion in the unprimed fibre norm and using the triangle inequality for $\lvert\cdot\rvert_i$ and the operator bounds of Step 1,
> $$\lvert \nabla'^{i}u \rvert_i \;\le\; \lvert\nabla^{i}u\rvert_i + \sum_{j=0}^{i-1}\lvert P_{ij}(\nabla^{j}u)\rvert_i \;\le\; \sum_{j=0}^{i} K_{ij}\,\lvert\nabla^{j}u\rvert_j \qquad \text{(triangle inequality; } \lvert P_{ij}(\nabla^{j}u)\rvert_i \le K_{ij}\lvert\nabla^{j}u\rvert_j \text{ by Lemma 2(b); } K_{ii} = 1\text{)}.$$
> Squaring and applying the Cauchy–Schwarz inequality ([[Thm - Cauchy-Schwarz Inequality|Cauchy–Schwarz]]) to the $(i+1)$-term sum, in the form $\big(\sum_{j=0}^{i} a_j\big)^2 \le (i+1)\sum_{j=0}^{i} a_j^2$ with $a_j = K_{ij}\lvert\nabla^{j}u\rvert_j$,
> $$\lvert\nabla'^{i}u\rvert_i^2 \;\le\; (i+1)\sum_{j=0}^{i} K_{ij}^2\,\lvert\nabla^{j}u\rvert_j^2 \qquad \text{(Cauchy–Schwarz on the finite sum).}$$
> Converting the left side to the primed fibre norm by Step 1 (Lemma 2(a) on $F_i$),
> $$\lvert\nabla'^{i}u\rvert'^2_i \;\le\; A_i\,\lvert\nabla'^{i}u\rvert_i^2 \;\le\; A_i\,(i+1)\sum_{j=0}^{i} K_{ij}^2\,\lvert\nabla^{j}u\rvert_j^2 \qquad \text{(Lemma 2(a), then the previous line).}$$
>
> **Step 3 — integrate and sum over $i$.** Integrate the last display against $\mathrm{vol}_{g'}$ and use $\mathrm{vol}_{g'} \le C_0\,\mathrm{vol}_g$ (Step 1, Lemma 2(c)) on the non-negative integrand:
> $$\int_M \lvert\nabla'^{i}u\rvert'^2_i\,\mathrm{vol}_{g'} \;\le\; A_i(i+1)\sum_{j=0}^{i} K_{ij}^2 \int_M \lvert\nabla^{j}u\rvert_j^2\,\mathrm{vol}_{g'} \;\le\; C_0\,A_i(i+1)\sum_{j=0}^{i} K_{ij}^2 \int_M \lvert\nabla^{j}u\rvert_j^2\,\mathrm{vol}_{g} \qquad \text{(monotonicity of the integral; Lemma 2(c)).}$$
> Write $\lVert\nabla^{j}u\rVert_{L^2}^2 := \int_M \lvert\nabla^{j}u\rvert_j^2\,\mathrm{vol}_g$, so the right-hand side is $C_0 A_i(i+1)\sum_{j=0}^i K_{ij}^2\,\lVert\nabla^{j}u\rVert_{L^2}^2$. Put $B_i := C_0\,A_i\,(i+1)\,\max_{0 \le j \le i} K_{ij}^2$; then, since $\sum_{j=0}^{i}\lVert\nabla^{j}u\rVert_{L^2}^2 \le \sum_{j=0}^{k}\lVert\nabla^{j}u\rVert_{L^2}^2 = \lVert u\rVert_{W^{k,2}}^2$ for every $i \le k$,
> $$\int_M \lvert\nabla'^{i}u\rvert'^2_i\,\mathrm{vol}_{g'} \;\le\; B_i \sum_{j=0}^{i}\lVert\nabla^{j}u\rVert_{L^2}^2 \;\le\; B_i\,\lVert u\rVert_{W^{k,2}}^2 \qquad \text{(definition of } B_i \text{; the tail sum is at most the full norm).}$$
> Summing over $i = 0, 1, \dots, k$ and recalling $\lVert u\rVert'^2_{W^{k,2}} = \sum_{i=0}^k \int_M \lvert\nabla'^{i}u\rvert'^2_i\,\mathrm{vol}_{g'}$,
> $$\lVert u\rVert'^2_{W^{k,2}} \;\le\; \Big(\sum_{i=0}^{k} B_i\Big)\,\lVert u\rVert_{W^{k,2}}^2 \qquad \text{(summing the previous display over the finitely many } i \le k\text{).}$$
> Set $C_k := \big(\sum_{i=0}^k B_i\big)^{1/2}$, a finite constant independent of $u$ (each $B_i$ is a product of the finite constants of Step 1). Taking square roots gives $\lVert u\rVert'_{W^{k,2}} \le C_k\,\lVert u\rVert_{W^{k,2}}$.
>
> **Step 4 — the reverse inequality and equivalence.** By the symmetry noted in Step 0, applying Steps 1–3 with the two data sets exchanged yields a finite constant $C_k' \ge 0$ with $\lVert u\rVert_{W^{k,2}} \le C_k'\,\lVert u\rVert'_{W^{k,2}}$ for all $u$. Let $\widetilde C_k := \max(C_k, C_k', 1) \ge 1$; then
> $$\widetilde C_k^{-1}\,\lVert u\rVert_{W^{k,2}} \le \lVert u\rVert'_{W^{k,2}} \le \widetilde C_k\,\lVert u\rVert_{W^{k,2}} \qquad \text{for all } u \in \Gamma(E),$$
> the first inequality from $\lVert u\rVert_{W^{k,2}} \le C_k'\lVert u\rVert'_{W^{k,2}} \le \widetilde C_k \lVert u\rVert'_{W^{k,2}}$ and the second from Step 3. This is the asserted equivalence of norms.
>
> **Step 5 — the completion is well-defined as a topological vector space, and is Hilbertable.** The two norms $\lVert\cdot\rVert_{W^{k,2}}$ and $\lVert\cdot\rVert'_{W^{k,2}}$ are equivalent on $\Gamma(E)$ by Step 4. Equivalent norms have identical Cauchy sequences: if $(u_m)$ is Cauchy for $\lVert\cdot\rVert_{W^{k,2}}$ then $\lVert u_m - u_{m'}\rVert'_{W^{k,2}} \le \widetilde C_k \lVert u_m - u_{m'}\rVert_{W^{k,2}} \to 0$, so it is Cauchy for $\lVert\cdot\rVert'_{W^{k,2}}$, and symmetrically. Let $W$ and $W'$ denote the two completions of $\Gamma(E)$ (the standard completion of a normed space: equivalence classes of Cauchy sequences, with $\Gamma(E)$ densely included as the classes of constant sequences). Since the identity map $\mathrm{id}: (\Gamma(E), \lVert\cdot\rVert_{W^{k,2}}) \to (\Gamma(E), \lVert\cdot\rVert'_{W^{k,2}})$ satisfies $\widetilde C_k^{-1}\lVert u\rVert \le \lVert \mathrm{id}(u)\rVert' \le \widetilde C_k\lVert u\rVert$, it is uniformly continuous with uniformly continuous inverse; a uniformly continuous map between normed spaces extends uniquely to a continuous map between their completions, so $\mathrm{id}$ extends to a linear bijection $J : W \to W'$ satisfying the same two-sided bound $\widetilde C_k^{-1}\lVert x\rVert_W \le \lVert Jx\rVert_{W'} \le \widetilde C_k\lVert x\rVert_W$ for all $x \in W$ (the bounds pass to the limit along a defining Cauchy sequence). Thus $J$ is a linear homeomorphism fixing $\Gamma(E)$; the completion is therefore the same topological vector space, canonically, whichever data set defines it. We call it $W^{k,2}(M; E)$. Finally, each norm $\lVert\cdot\rVert_{W^{k,2}}$ arises from the inner product $\langle u, v\rangle_{W^{k,2}} = \sum_{i=0}^{k}\int_M \langle\nabla^{i}u, \nabla^{i}v\rangle_i\,\mathrm{vol}_g$, so its completion $W$ is a Hilbert space; different data give different but equivalent inner products, hence the same underlying topological vector space carries a Hilbert-space structure that is canonical only up to the choice of data — that is, $W^{k,2}(M; E)$ is Hilbertable.
>
> **Conclusion.** For every $k \ge 0$ any two choices of Sobolev data give equivalent norms on $\Gamma(E)$, and consequently one and the same completed topological vector space $W^{k,2}(M; E)$, which is Hilbertable. $\blacksquare$

> [!note]- Extension to all exponents $p \ge 1$ (companion form)
> The proof above uses the exponent $2$ in exactly two places, and each has a version for every real $p \ge 1$, so the entire argument transports.
>
> **Fibre-metric and volume comparisons are exponent-free.** Lemma 2 makes no reference to $p$: it gives $\lvert w\rvert'_i \le A_i^{1/2}\lvert w\rvert_i$, $\lvert P_{ij}(p)w\rvert_i \le K_{ij}\lvert w\rvert_j$, and $\mathrm{vol}_{g'} \le C_0\,\mathrm{vol}_g$, all as pointwise or measure inequalities. Lemma 3 is purely algebraic and likewise exponent-free.
>
> **Cauchy–Schwarz is replaced by the power-mean (Jensen) inequality.** In Step 2, for $p \ge 1$ the convexity of $t \mapsto t^p$ gives, for the same non-negative $a_j = K_{ij}\lvert\nabla^{j}u\rvert_j$,
> $$\Big(\sum_{j=0}^{i} a_j\Big)^p \le (i+1)^{p-1}\sum_{j=0}^{i} a_j^{\,p} \qquad \text{(Jensen's inequality for the convex function } t \mapsto t^p \text{, applied to the average } \tfrac{1}{i+1}\sum a_j\text{)}.$$
> Hence $\lvert\nabla'^{i}u\rvert_i^{\,p} \le (i+1)^{p-1}\sum_{j\le i} K_{ij}^{\,p}\lvert\nabla^{j}u\rvert_j^{\,p}$, and converting the fibre norm by $\lvert\nabla'^{i}u\rvert'^{\,p}_i \le A_i^{p/2}\lvert\nabla'^{i}u\rvert_i^{\,p}$ and integrating against $\mathrm{vol}_{g'} \le C_0\,\mathrm{vol}_g$ gives, exactly as in Step 3,
> $$\int_M \lvert\nabla'^{i}u\rvert'^{\,p}_i\,\mathrm{vol}_{g'} \le C_0\,A_i^{p/2}(i+1)^{p-1}\Big(\max_{j\le i} K_{ij}^{\,p}\Big)\sum_{j=0}^{i}\lVert\nabla^{j}u\rVert_{L^p}^{\,p} \le B_i^{(p)}\,\lVert u\rVert_{W^{k,p}}^{\,p},$$
> where $\lVert\nabla^{j}u\rVert_{L^p}^{\,p} = \int_M \lvert\nabla^{j}u\rvert_j^{\,p}\,\mathrm{vol}_g$ and $B_i^{(p)} := C_0 A_i^{p/2}(i+1)^{p-1}\max_{j\le i}K_{ij}^{\,p}$. Summing over $i \le k$, $\lVert u\rVert'^{\,p}_{W^{k,p}} \le \big(\sum_{i\le k} B_i^{(p)}\big)\lVert u\rVert_{W^{k,p}}^{\,p}$, so $\lVert u\rVert'_{W^{k,p}} \le C_{k,p}\lVert u\rVert_{W^{k,p}}$ with $C_{k,p} = \big(\sum_{i\le k}B_i^{(p)}\big)^{1/p}$. Symmetry gives the reverse inequality, and Step 5 (which used only equivalence of norms, not the exponent) gives the well-defined completion $W^{k,p}(M; E)$. For $p = 2$ this reproduces the main theorem. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Elliptic operator theory on a closed manifold.** The elliptic estimate $\lVert u\rVert_{W^{k+m,2}} \le C(\lVert Pu\rVert_{W^{k,2}} + \lVert u\rVert_{L^2})$ for an order-$m$ elliptic operator $P$ is always stated with definite Sobolev norms. Applying the present theorem, one checks that the *validity* of the estimate is metric-independent even though the *constant* $C$ is not: changing the metric multiplies both sides by bounded factors, so an estimate valid for one metric is valid for all. This is non-obvious because the elliptic estimate is usually proved in one fixed metric (via a partition of unity and constant-coefficient model operators), and the theorem is exactly what frees the conclusion from that choice.

**Hodge theory and harmonic representatives.** The Hodge decomposition $\Omega^k(M) = \mathcal{H}^k \oplus \operatorname{im} d \oplus \operatorname{im} d^*$ is proved by completing $\Omega^k$ in a Sobolev norm and applying elliptic theory to the Laplacian $\Delta = dd^* + d^*d$. The Sobolev completion depends on a metric, and the Laplacian depends on a metric; the present theorem guarantees that the *topological vector space* being decomposed does not depend on which metric set it up, which is why the dimensions of the harmonic spaces (the Betti numbers) come out as topological invariants. The exercise is to isolate exactly where metric-independence of the *space* (as opposed to the *decomposition*) is used.

**Configuration spaces in gauge theory.** In defining the Seiberg–Witten or anti-self-dual moduli spaces one completes the space of connections and the gauge group in Sobolev norms built from a reference connection and a metric. Show that the smooth structure of the completed configuration space $\mathcal{A}^{k,2}(E)/\mathcal{G}^{k+1,2}(E)$ does not depend on the reference connection, using the theorem to identify the $W^{k,2}$ topologies coming from different references. This is non-obvious because the reference connection is a *point of the very space one is completing*, so the independence is what makes the construction non-circular.

---

# Bridges

- **[[Thm - The Space of Connections is an Affine Space|The affine structure of connections]].** The single algebraic input to the whole proof is that a difference of connections is a tensor. That fact is proved once, on its own page, as the statement that $\mathcal{A}(E)$ is an affine space modelled on $\Omega^1(M; \operatorname{End} E)$; here it is invoked twice (for $E$ and for $T^*M$) to write $\nabla'^E = \nabla^E + a$ and $\nabla'^M = \nabla^M + b$ with smooth tensor coefficients. Every "the difference is zeroth order" step in analysis on bundles routes through this bridge.

- **[[Def - Induced Connection on Tensor Bundles|Induced connections on tensor products]].** The tower $F_i = (T^*M)^{\otimes i}\otimes E$ carries a connection assembled from $\nabla^M$ and $\nabla^E$ by the tensor-product Leibniz rule, and the difference of two such induced connections is computed on decomposable sections and extended by $C^\infty(M)$-linearity. This construction — connection on a tensor product equals sum of the connections on the factors — is what lets the zeroth-order perturbation on the constituents $E$ and $T^*M$ propagate to a zeroth-order perturbation on every $F_i$.

- **Compactness as boundedness of smooth data.** The topological input is the single principle that a continuous function on a compact space attains its extrema. It is used three times over — for the ratio of two fibre metrics on a sphere bundle, for the operator norm of a smooth bundle map, and for the density ratio $\rho = \mathrm{vol}_{g'}/\mathrm{vol}_g$. The bridge to build in one's mind is: *smooth object + compact base $\Rightarrow$ uniform bound*, which is the mechanism that converts pointwise algebra into global estimates and recurs throughout the analysis on closed manifolds. It fails on non-compact $M$, which is exactly why the theorem is stated for compact base (and why on non-compact manifolds one must fix weights or work with compactly supported sections).

- **[[Def - Sobolev Space of Sections|The Sobolev space of sections]].** This theorem is what makes the notation $W^{k,2}(M; E)$ legitimate: the definition on the previous page fixes data to write down a norm, and this page shows the fixed data drops out of the completed space. Every later page of the chapter — embedding, Rellich compactness, elliptic estimates, the Fredholm property, the Hodge theorem — uses $W^{k,2}(M; E)$ as a definite object, silently relying on this result.

---

# Unlocked by This

> [!tip] Well-defined Sobolev configuration space *(from Gauge Theory)*
> Because the $W^{k,2}$ topology on $\Omega^1(M; \operatorname{End} E)$ is data-independent, the space of Sobolev connections $\mathcal{A}^{k,2}(E) = \nabla_0 + W^{k,2}(\Omega^1(M; \operatorname{End} E))$ is a well-defined affine Hilbert manifold not depending on the smooth reference $\nabla_0$; this is the configuration space on which **Yang–Mills and Seiberg–Witten theory** are built. See [[Thm - The Space of Connections is an Affine Space]].

> [!tip] Metric-independence of Sobolev-defined invariants *(from Global Analysis)*
> Any invariant defined by completing a space of sections in a Sobolev norm and reading off a topological quantity — the dimension of a harmonic space, the index of an elliptic operator, the rank of a cohomology group — is automatically independent of the metric used to set up the completion, because this theorem identifies the completed spaces. This is the structural reason **analytic definitions of topological invariants are well-posed**.
