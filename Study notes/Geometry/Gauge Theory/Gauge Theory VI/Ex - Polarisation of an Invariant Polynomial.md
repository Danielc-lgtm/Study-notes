---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Ad-Invariant Polynomial"
  - "Def - Multilinear Form"
  - "Def - Determinant"
  - "Def - Trace"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $G$ be a Lie group with Lie algebra $\mathfrak{g}$ over the field $\mathbb{K}\in\{\mathbb{R},\mathbb{C}\}$, and fix an integer $d\ge1$. Recall the two ways of presenting an invariant of degree $d$: as a homogeneous polynomial $p\colon\mathfrak{g}\to\mathbb{K}$, or as a symmetric $d$-linear form $\lambda\colon\mathfrak{g}^{d}\to\mathbb{K}$; the two are tied by the **diagonal restriction** $p(\xi)=\lambda(\xi,\dots,\xi)$. Prove the following.

1. **The polarisation formula.** Every homogeneous polynomial $p$ of degree $d$ on $\mathfrak{g}$ is the diagonal of a **unique** symmetric $d$-linear form $\lambda$, and that form is given explicitly by
$$\lambda(\xi_1,\dots,\xi_d)=\frac{1}{d!}\sum_{S\subseteq\{1,\dots,d\}}(-1)^{d-|S|}\,p\!\Big(\sum_{i\in S}\xi_i\Big).\tag{$\ast$}$$
Consequently diagonal restriction is a linear bijection between symmetric $d$-linear forms and homogeneous degree-$d$ polynomials.

2. **Invariance transfers both ways.** For $p$ and its polar form $\lambda$ related by $(\ast)$, the polynomial $p$ is $\operatorname{Ad}$-invariant if and only if the form $\lambda$ is $\operatorname{Ad}$-invariant. Hence the two definitions of an $\operatorname{Ad}$-invariant homogeneous polynomial — Haydys's polynomial and Bär's symmetric multilinear form — carry the same information.

3. **A worked polar form.** Compute the polar form of the determinant $p=\det$ on $\mathfrak{gl}_2(\mathbb{K})$ (which is homogeneous of degree $d=2$), obtaining the symmetric bilinear form
$$\lambda(\xi_1,\xi_2)=\tfrac12\big(\operatorname{tr}\xi_1\operatorname{tr}\xi_2-\operatorname{tr}(\xi_1\xi_2)\big),$$
and verify that its diagonal is $\det$.

**Recall:**

The objects in play are the $\operatorname{Ad}$-invariant homogeneous polynomial and its equivalent symmetric multilinear form, the notion of a multilinear form, and (for Part 3) the determinant and trace.

![[Def - Ad-Invariant Polynomial#The Definition]]

The **[[Def - Ad-Invariant Polynomial|invariant-polynomial definition]]** presents the object in two guises. A homogeneous polynomial $p\colon\mathfrak{g}\to\mathbb{K}$ of degree $d$ is $\operatorname{Ad}$-invariant if $p(\operatorname{Ad}_g\xi)=p(\xi)$ for all $g\in G$; a symmetric $d$-linear form $\lambda\colon\mathfrak{g}^{d}\to\mathbb{K}$ is $\operatorname{Ad}$-invariant if $\lambda(\operatorname{Ad}_g\xi_1,\dots,\operatorname{Ad}_g\xi_d)=\lambda(\xi_1,\dots,\xi_d)$ for all $g\in G$. The present exercise proves in detail the equivalence that the definition page states as its polarisation proposition, so that either presentation may be used freely thereafter.

![[Def - Multilinear Form#The Definition]]

A **[[Def - Multilinear Form|d-linear form]]** $\lambda\colon\mathfrak{g}^{d}\to\mathbb{K}$ is $\mathbb{K}$-linear in each argument with the others held fixed; it is **symmetric** if $\lambda(\xi_{\sigma(1)},\dots,\xi_{\sigma(d)})=\lambda(\xi_1,\dots,\xi_d)$ for every permutation $\sigma$ of $\{1,\dots,d\}$. We write $S_d$ for the symmetric group on $d$ letters and $|S|$ for the cardinality of a finite set $S$.

![[Def - Determinant#The Definition]]

For Part 3 we use that the [[Def - Determinant|determinant]] on $\mathfrak{gl}_2$ is $\det\begin{pmatrix}a&b\\c&d\end{pmatrix}=ad-bc$, homogeneous of degree $2$, and that the [[Def - Trace|trace]] $\operatorname{tr}\xi=\sum_k\xi_{kk}$ is linear with $\operatorname{tr}(\xi_1\xi_2)=\operatorname{tr}(\xi_2\xi_1)$.

---

# Convergent Strategy

**Problem class.** This is a *representation-of-an-object* problem: we are asked to show that two apparently different data structures — a single polynomial function and a symmetric tensor — encode the same information, and to make the dictionary between them explicit and computable. The characteristic obstacle is not depth but bookkeeping: one must invert the many-to-one operation "restrict a multilinear form to its diagonal", and the inverse is an inclusion–exclusion sum whose cancellations must be controlled exactly.

**Assumption pattern.** The proof rests on two facts that recur throughout multilinear algebra. First, *a homogeneous degree-$d$ polynomial expands, upon substituting a sum $\sum_{i\in S}\xi_i$ into a symmetric $d$-linear form's diagonal, into a sum over all functions from the $d$ slots into $S$* — this is just distributing multilinearity. Second, *the signed sum $\sum_{S\supseteq T}(-1)^{d-|S|}$ over supersets of a fixed set $T$ collapses by the binomial theorem to a Kronecker delta $[\,|T|=d\,]$* — this is the engine that kills every function except the bijections. Recognising that the polarisation formula is exactly a Möbius/inclusion–exclusion inversion is the strategic key.

**Assumption pattern (continued).** Uniqueness and the explicit formula come together from a single lemma: *$(\ast)$ applied to the diagonal of any symmetric form $\nu$ returns $\nu$*. Existence needs a separate, easy construction — symmetrising a monomial — because the inversion lemma presupposes that a polar form exists before it can identify it.

**Theorem routing.** Part 1 routes as: (i) an inversion lemma showing $(\ast)$ recovers a symmetric form from its diagonal, via the binomial collapse; (ii) an existence construction realising every homogeneous polynomial as a diagonal, via symmetrised monomials; (iii) assembly into "existence, formula, uniqueness". Part 2 routes through the linearity of $\operatorname{Ad}_g$: invariance of $\lambda$ pushes to $p$ by evaluating on the diagonal, and invariance of $p$ pushes to $\lambda$ by feeding $\operatorname{Ad}_g$ through the linear-in-each-slot formula $(\ast)$. Part 3 routes through the degree-two instance $\lambda(\xi_1,\xi_2)=\tfrac12(p(\xi_1+\xi_2)-p(\xi_1)-p(\xi_2))$ and the entrywise $2\times2$ mixed-determinant identity.

**Key decision point.** The decisive move is to prove the *inversion lemma for an arbitrary symmetric form $\nu$*, not directly for the $p$ at hand. This single lemma does three jobs at once: it shows any polar form equals $(\ast)$ (uniqueness), it shows $(\ast)$ is genuinely symmetric and multilinear (because it equals the $\nu$ produced by existence), and it supplies the explicit formula. Attempting instead to verify symmetry, multilinearity, and the diagonal property of $(\ast)$ by direct expansion is possible but far messier; routing through "$(\ast)$ inverts diagonal restriction" is what keeps the argument clean.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory VI — Chern–Weil Theory, Characteristic Classes, and the Chern–Simons Functional#Legal Operations|the topic page's Legal Operations]]; where the topic page is not yet assembled the operations are named descriptively and the numbering will be reconciled.

1. **Expand a diagonal by distributing multilinearity over a sum.** Substituting $\eta_S=\sum_{i\in S}\xi_i$ into $\nu(\eta_S,\dots,\eta_S)$ and distributing produces a sum over all functions $f\colon\{1,\dots,d\}\to S$; this converts a diagonal value into a manageable sum of $\nu$-values.

2. **Invert an inclusion–exclusion sum by the binomial collapse.** The signed superset sum $\sum_{S\supseteq\operatorname{im}f}(-1)^{d-|S|}=(1-1)^{d-|\operatorname{im}f|}$ vanishes unless $f$ is a bijection, isolating the permutation terms.

3. **Reduce existence to a monomial by linearity.** Both diagonal restriction and $(\ast)$ are linear in $p$, so existence of a polar form need only be checked on monomials, where it is exhibited by symmetrising over $S_d$.

4. **Transfer a group invariance across a linear isomorphism.** Because $\operatorname{Ad}_g$ is linear, it commutes with $(\ast)$ and with evaluation on the diagonal, so invariance of one presentation forces invariance of the other.

5. **Compute a low-degree polar form from the two-term difference and reduce to trace data.** Use the $d=2$ formula $\lambda(\xi_1,\xi_2)=\tfrac12(p(\xi_1+\xi_2)-p(\xi_1)-p(\xi_2))$ and the $2\times2$ identity $\det(\xi_1+\xi_2)-\det\xi_1-\det\xi_2=\operatorname{tr}\xi_1\operatorname{tr}\xi_2-\operatorname{tr}(\xi_1\xi_2)$.

---

# Hints

> [!note]- Hint 1
> To prove $(\ast)$ recovers a symmetric form from its diagonal, start from an *arbitrary* symmetric $d$-linear form $\nu$, set $q(\xi)=\nu(\xi,\dots,\xi)$, and substitute $q$ into the right-hand side of $(\ast)$. Expand each $q(\sum_{i\in S}\xi_i)$ by multilinearity. Do not yet worry about the $p$ you actually care about.

> [!note]- Hint 2
> After expanding, you get a double sum over subsets $S$ and over functions $f\colon\{1,\dots,d\}\to\{1,\dots,d\}$ with $\operatorname{im}f\subseteq S$. Swap the order: fix $f$, and sum the sign $(-1)^{d-|S|}$ over all $S$ containing $\operatorname{im}f$. Recognise this inner sum as a binomial expansion of $(1-1)^{d-|\operatorname{im}f|}$.

> [!note]- Hint 3
> The binomial collapse kills every $f$ except those with $|\operatorname{im}f|=d$, i.e. the bijections — the permutations $\sigma\in S_d$. Symmetry of $\nu$ makes every permuted evaluation equal to $\nu(\xi_1,\dots,\xi_d)$, and there are $d!$ of them. This proves $(\ast)$ applied to $\nu$'s diagonal returns $\nu$: uniqueness and the formula in one stroke.

> [!note]- Hint 4
> For existence — that *some* symmetric form has diagonal $p$ — reduce to a monomial $p=x^{\alpha}$ by linearity, and symmetrise: average $\prod_k x_{m_k}(\eta_{\sigma(k)})$ over $\sigma\in S_d$, where the multiset $(m_1,\dots,m_d)$ lists the variables of $x^{\alpha}$ with multiplicity.

> [!note]- Hint 5
> For the invariance transfer, the forward direction is a one-liner (evaluate the invariance of $\lambda$ on the diagonal). For the converse, apply $(\ast)$ to $\lambda(\operatorname{Ad}_g\xi_1,\dots)$ and use that $\operatorname{Ad}_g$ is *linear*, so $\operatorname{Ad}_g\sum_{i\in S}\xi_i=\sum_{i\in S}\operatorname{Ad}_g\xi_i$; then invoke invariance of $p$ term by term.

> [!note]- Hint 6
> For $p=\det$ on $\mathfrak{gl}_2$, use the $d=2$ case of $(\ast)$: $\lambda(\xi_1,\xi_2)=\tfrac12(\det(\xi_1+\xi_2)-\det\xi_1-\det\xi_2)$. Expand $\det(\xi_1+\xi_2)$ from the entries and collect; you will meet $\operatorname{tr}\xi_1\operatorname{tr}\xi_2$ and $\operatorname{tr}(\xi_1\xi_2)$.

---

# Solution

The plan has three movements. First, an inversion lemma: the formula $(\ast)$, applied to the diagonal of any symmetric $d$-linear form $\nu$, returns $\nu$ — this delivers uniqueness and pins down the formula. Second, an existence construction realises every homogeneous degree-$d$ polynomial as a diagonal, after which assembly gives Part 1 and the linear bijection. Third, the invariance transfer and the concrete determinant computation. Throughout, $\eta_S:=\sum_{i\in S}\xi_i$ for a subset $S\subseteq\{1,\dots,d\}$, and the empty sum is $\eta_\varnothing=0$.

**Step 1: The formula $(\ast)$ inverts diagonal restriction.**

For any symmetric $d$-linear form $\nu$, substituting its diagonal $q(\xi)=\nu(\xi,\dots,\xi)$ into $(\ast)$ returns $\nu$ itself; the cancellation is a binomial collapse over supersets.

> [!note]- Derivation
> Let $\nu\colon\mathfrak{g}^{d}\to\mathbb{K}$ be symmetric $d$-linear and set $q(\xi)=\nu(\xi,\dots,\xi)$. We compute the right-hand side of $(\ast)$ with $p$ replaced by $q$.
>
> **Expand each diagonal value.** For a subset $S\subseteq\{1,\dots,d\}$, distribute multilinearity of $\nu$ across all $d$ slots of $\nu(\eta_S,\dots,\eta_S)$, where $\eta_S=\sum_{i\in S}\xi_i$:
> $$q(\eta_S)=\nu(\eta_S,\dots,\eta_S)=\sum_{f\colon\{1,\dots,d\}\to S}\nu\big(\xi_{f(1)},\dots,\xi_{f(d)}\big)\qquad\text{(one summand per choice of index }f(k)\in S\text{ in each slot }k\text{).}$$
> **Substitute and regroup by the function $f$.** Inserting this into $(\ast)$,
> $$\frac{1}{d!}\sum_{S\subseteq\{1,\dots,d\}}(-1)^{d-|S|}q(\eta_S)=\frac{1}{d!}\sum_{S}(-1)^{d-|S|}\sum_{f\colon\{1,\dots,d\}\to S}\nu\big(\xi_{f(1)},\dots,\xi_{f(d)}\big).$$
> A function $f\colon\{1,\dots,d\}\to\{1,\dots,d\}$ appears in the $S$-term precisely when $\operatorname{im}f\subseteq S$. Interchanging the two finite sums and grouping by $f$,
> $$=\frac{1}{d!}\sum_{f\colon\{1,\dots,d\}\to\{1,\dots,d\}}\Big(\sum_{S\,:\,\operatorname{im}f\subseteq S}(-1)^{d-|S|}\Big)\,\nu\big(\xi_{f(1)},\dots,\xi_{f(d)}\big).$$
> **Collapse the inner sign sum.** Fix $f$ and put $m:=|\operatorname{im}f|$, $N:=d-m$. The subsets $S$ with $\operatorname{im}f\subseteq S$ are obtained by adjoining to $\operatorname{im}f$ any subset of the $N$ remaining indices; if $j$ indices are adjoined then $|S|=m+j$, and there are $\binom{N}{j}$ such $S$. Hence
> $$\sum_{S\,:\,\operatorname{im}f\subseteq S}(-1)^{d-|S|}=\sum_{j=0}^{N}\binom{N}{j}(-1)^{d-(m+j)}=\sum_{j=0}^{N}\binom{N}{j}(-1)^{N-j}=(-1+1)^{N}=0^{N}\qquad\text{(binomial theorem with }a=-1,\,b=1\text{),}$$
> which equals $0$ when $N\ge1$ and equals $1$ when $N=0$. So only functions $f$ with $N=0$, i.e. $|\operatorname{im}f|=d$, survive; a function from a $d$-element set onto a $d$-element set is a **bijection**, that is a permutation $\sigma\in S_d$.
>
> **Use symmetry of $\nu$.** For each permutation $\sigma$, symmetry gives $\nu(\xi_{\sigma(1)},\dots,\xi_{\sigma(d)})=\nu(\xi_1,\dots,\xi_d)$, and there are exactly $d!$ permutations. Therefore
> $$\frac{1}{d!}\sum_{S}(-1)^{d-|S|}q(\eta_S)=\frac{1}{d!}\sum_{\sigma\in S_d}\nu(\xi_{\sigma(1)},\dots,\xi_{\sigma(d)})=\frac{1}{d!}\cdot d!\cdot\nu(\xi_1,\dots,\xi_d)=\nu(\xi_1,\dots,\xi_d).$$
> That is, $(\ast)$ applied to the diagonal of $\nu$ returns $\nu$. In particular, if a symmetric $d$-linear form has diagonal $p$, it is forced to equal the right-hand side of $(\ast)$ — this is **uniqueness**, and it identifies the formula.

**Step 2: Every homogeneous degree-$d$ polynomial is a diagonal.**

By linearity it suffices to realise a single monomial as the diagonal of a symmetric form, which is done by symmetrising.

> [!note]- Derivation
> Both the operation "restrict a symmetric form to its diagonal" and the operation $(\ast)$ are $\mathbb{K}$-linear in their polynomial/tensor argument. Every homogeneous polynomial of degree $d$ is a $\mathbb{K}$-linear combination of monomials $x^{\alpha}=x_1^{\alpha_1}\cdots x_n^{\alpha_n}$ with $|\alpha|=\alpha_1+\dots+\alpha_n=d$, where $x_i=e_i^{*}$ is the $i$-th coordinate functional relative to a fixed basis $\xi_1,\dots,\xi_n$ of $\mathfrak{g}$. It therefore suffices to construct, for each such monomial $p=x^{\alpha}$, a symmetric $d$-linear form with diagonal $p$; the general case follows by taking the same linear combination of the resulting forms.
>
> Let $(m_1,\dots,m_d)$ be the list of variable-indices of $x^{\alpha}$ with multiplicity (the index $i$ appears $\alpha_i$ times). Define
> $$\mu(\eta_1,\dots,\eta_d):=\frac{1}{d!}\sum_{\sigma\in S_d}\;\prod_{k=1}^{d}x_{m_k}\big(\eta_{\sigma(k)}\big).$$
> Each factor $x_{m_k}(\eta_{\sigma(k)})$ is linear in the argument $\eta_{\sigma(k)}$, so $\mu$ is $d$-linear; and averaging over all of $S_d$ makes $\mu$ symmetric, since precomposing the arguments with a permutation $\tau$ only reindexes the average over $\sigma$. Its diagonal is
> $$\mu(\xi,\dots,\xi)=\frac{1}{d!}\sum_{\sigma\in S_d}\prod_{k=1}^{d}x_{m_k}(\xi)=\frac{1}{d!}\cdot d!\cdot\prod_{k=1}^{d}x_{m_k}(\xi)=x^{\alpha}(\xi)=p(\xi),$$
> because each of the $d!$ summands equals the same product $\prod_k x_{m_k}(\xi)$ (the arguments no longer depend on $\sigma$ when all slots hold $\xi$), and $\prod_k x_{m_k}(\xi)=\prod_i x_i(\xi)^{\alpha_i}=x^{\alpha}(\xi)$. So $\mu$ is a symmetric $d$-linear form whose diagonal is the monomial $p$. Extending linearly, every homogeneous degree-$d$ polynomial is a diagonal.

**Step 3: Assemble Part 1 — existence, formula, uniqueness, bijection.**

> [!note]- Derivation
> Let $p$ be homogeneous of degree $d$. By Step 2 there is a symmetric $d$-linear form $\mu$ with diagonal $p$. By Step 1 applied to $\nu=\mu$, the formula $(\ast)$ evaluated on $p=\mu(\cdot,\dots,\cdot)$'s diagonal returns $\mu$; in particular the right-hand side of $(\ast)$ *is* the symmetric multilinear form $\mu$, so $(\ast)$ defines a symmetric $d$-linear form polarising $p$ — this is **existence together with the explicit formula**.
>
> For **uniqueness**, suppose $\nu_1,\nu_2$ are symmetric $d$-linear forms both with diagonal $p$. By Step 1, $(\ast)$ applied to $p$ returns $\nu_1$ (taking $\nu=\nu_1$) and also returns $\nu_2$ (taking $\nu=\nu_2$); since $(\ast)$ is one fixed expression, $\nu_1=\nu_2$. Hence the polar form is unique and equals $(\ast)$.
>
> Finally, write $R$ for diagonal restriction, from symmetric $d$-linear forms to homogeneous degree-$d$ polynomials, and $P$ for the map $(\ast)$. Both are linear. Step 2 shows $R$ is surjective; Step 1 says $R\circ P=\operatorname{id}$ on polynomials (given $p$, form $P(p)$, restrict, recover $p$) and $P\circ R=\operatorname{id}$ on forms (this is exactly "$(\ast)$ applied to $\nu$'s diagonal returns $\nu$"). So $R$ is a linear bijection with inverse $P$.

**Step 4: Invariance transfers both ways (Part 2).**

> [!note]- Derivation
> Let $p$ and $\lambda$ correspond under $(\ast)$, so $p(\xi)=\lambda(\xi,\dots,\xi)$.
>
> **($\lambda$ invariant $\Rightarrow$ $p$ invariant).** Assume $\lambda(\operatorname{Ad}_g\xi_1,\dots,\operatorname{Ad}_g\xi_d)=\lambda(\xi_1,\dots,\xi_d)$ for all $g,\xi_i$. Evaluating on the diagonal $\xi_1=\dots=\xi_d=\xi$,
> $$p(\operatorname{Ad}_g\xi)=\lambda(\operatorname{Ad}_g\xi,\dots,\operatorname{Ad}_g\xi)=\lambda(\xi,\dots,\xi)=p(\xi)\qquad\text{(invariance of }\lambda\text{ on the diagonal),}$$
> so $p$ is $\operatorname{Ad}$-invariant.
>
> **($p$ invariant $\Rightarrow$ $\lambda$ invariant).** Assume $p(\operatorname{Ad}_g\xi)=p(\xi)$ for all $g,\xi$. Fix $g\in G$. Because $\operatorname{Ad}_g$ is a $\mathbb{K}$-linear map of $\mathfrak{g}$, it commutes with finite sums: $\sum_{i\in S}\operatorname{Ad}_g\xi_i=\operatorname{Ad}_g\big(\sum_{i\in S}\xi_i\big)=\operatorname{Ad}_g\eta_S$. Apply the formula $(\ast)$ to the tuple $(\operatorname{Ad}_g\xi_1,\dots,\operatorname{Ad}_g\xi_d)$:
> $$\lambda(\operatorname{Ad}_g\xi_1,\dots,\operatorname{Ad}_g\xi_d)=\frac{1}{d!}\sum_{S}(-1)^{d-|S|}p\big(\operatorname{Ad}_g\eta_S\big)=\frac{1}{d!}\sum_{S}(-1)^{d-|S|}p(\eta_S)=\lambda(\xi_1,\dots,\xi_d),$$
> using in turn the formula $(\ast)$, then linearity of $\operatorname{Ad}_g$ to write $\sum_{i\in S}\operatorname{Ad}_g\xi_i=\operatorname{Ad}_g\eta_S$, then invariance of $p$ term by term ($p(\operatorname{Ad}_g\eta_S)=p(\eta_S)$), then $(\ast)$ again. So $\lambda$ is $\operatorname{Ad}$-invariant. The two invariance conditions are therefore equivalent, and Bär's and Haydys's definitions coincide.

**Step 5: The polar form of $\det$ on $\mathfrak{gl}_2$ (Part 3).**

> [!note]- Derivation
> The determinant on $\mathfrak{gl}_2(\mathbb{K})$ is homogeneous of degree $d=2$ ($\det(s\xi)=s^{2}\det\xi$), so its polar form is a symmetric bilinear form. Specialising $(\ast)$ to $d=2$: the subsets of $\{1,2\}$ are $\varnothing,\{1\},\{2\},\{1,2\}$, contributing signs $(-1)^{2},(-1)^{1},(-1)^{1},(-1)^{0}$; since $p(\eta_\varnothing)=p(0)=0$ by homogeneity, the formula reads
> $$\lambda(\xi_1,\xi_2)=\tfrac12\big(p(\xi_1+\xi_2)-p(\xi_1)-p(\xi_2)\big)=\tfrac12\big(\det(\xi_1+\xi_2)-\det\xi_1-\det\xi_2\big).$$
> We evaluate the difference from the entries. Write $\xi_1=\begin{pmatrix}a&b\\c&e\end{pmatrix}$ and $\xi_2=\begin{pmatrix}p'&q'\\r'&s'\end{pmatrix}$ (the primes avoid clashing with the polynomial $p$). Then
> $$\det(\xi_1+\xi_2)=(a+p')(e+s')-(b+q')(c+r')=(ae-bc)+(p's'-q'r')+\big(as'+p'e-br'-q'c\big),$$
> where the first two grouped terms are $\det\xi_1$ and $\det\xi_2$. Hence
> $$\det(\xi_1+\xi_2)-\det\xi_1-\det\xi_2=as'+p'e-br'-q'c.$$
> Now compute the two trace expressions from the entries:
> $$\operatorname{tr}\xi_1\,\operatorname{tr}\xi_2=(a+e)(p'+s')=ap'+as'+ep'+es',$$
> $$\operatorname{tr}(\xi_1\xi_2)=\operatorname{tr}\begin{pmatrix}ap'+br' & \ast\\ \ast & cq'+es'\end{pmatrix}=ap'+br'+cq'+es',$$
> so that
> $$\operatorname{tr}\xi_1\,\operatorname{tr}\xi_2-\operatorname{tr}(\xi_1\xi_2)=(ap'+as'+ep'+es')-(ap'+br'+cq'+es')=as'+ep'-br'-cq'.$$
> This is identical to $\det(\xi_1+\xi_2)-\det\xi_1-\det\xi_2$ computed above. Therefore
> $$\lambda(\xi_1,\xi_2)=\tfrac12\big(\operatorname{tr}\xi_1\,\operatorname{tr}\xi_2-\operatorname{tr}(\xi_1\xi_2)\big),$$
> a manifestly symmetric bilinear form (both terms are symmetric in $\xi_1\leftrightarrow\xi_2$, the second by cyclicity of the trace). **Check the diagonal.** Setting $\xi_1=\xi_2=\xi$,
> $$\lambda(\xi,\xi)=\tfrac12\big((\operatorname{tr}\xi)^{2}-\operatorname{tr}(\xi^{2})\big)=\det\xi,$$
> the last equality being the $2\times2$ identity $(\operatorname{tr}\xi)^{2}-\operatorname{tr}(\xi^{2})=2\det\xi$ (proved by the same entry computation, or read off from the two displays above with $\xi_1=\xi_2=\xi$). So the diagonal of $\lambda$ is indeed $\det$, confirming that $\lambda$ is the polar form of the determinant on $\mathfrak{gl}_2$.

> [!note]- Complete formal solution
> **Claim.** (1) Every homogeneous polynomial $p$ of degree $d$ on $\mathfrak{g}$ is the diagonal of a unique symmetric $d$-linear form $\lambda$, given by $(\ast)$; diagonal restriction is a linear bijection. (2) $p$ is $\operatorname{Ad}$-invariant iff $\lambda$ is. (3) On $\mathfrak{gl}_2$ the polar form of $\det$ is $\lambda(\xi_1,\xi_2)=\tfrac12(\operatorname{tr}\xi_1\operatorname{tr}\xi_2-\operatorname{tr}(\xi_1\xi_2))$.
>
> *Inversion lemma.* For any symmetric $d$-linear $\nu$ with diagonal $q$, and $\eta_S:=\sum_{i\in S}\xi_i$,
> $$\frac{1}{d!}\sum_{S\subseteq\{1,\dots,d\}}(-1)^{d-|S|}q(\eta_S)=\frac{1}{d!}\sum_{f\colon[d]\to[d]}\Big(\sum_{S\supseteq\operatorname{im}f}(-1)^{d-|S|}\Big)\nu(\xi_{f(1)},\dots,\xi_{f(d)}).$$
> The inner sum equals $(1-1)^{d-|\operatorname{im}f|}$, which is $0$ unless $f$ is a bijection and $1$ when it is; by symmetry each of the $d!$ permutation terms equals $\nu(\xi_1,\dots,\xi_d)$, so the whole expression is $\nu(\xi_1,\dots,\xi_d)$. Thus $(\ast)$ recovers $\nu$ from its diagonal.
>
> *Existence.* By linearity in $p$ it suffices to treat a monomial $p=x^{\alpha}$, $|\alpha|=d$; with $(m_1,\dots,m_d)$ its variable-indices with multiplicity, $\mu(\eta_1,\dots,\eta_d)=\tfrac{1}{d!}\sum_{\sigma\in S_d}\prod_k x_{m_k}(\eta_{\sigma(k)})$ is symmetric $d$-linear with diagonal $\prod_k x_{m_k}(\xi)=x^{\alpha}(\xi)=p(\xi)$.
>
> *Assembly.* Given $p$, existence yields $\mu$ with diagonal $p$; the inversion lemma with $\nu=\mu$ shows $(\ast)$ equals $\mu$, hence $(\ast)$ is a symmetric $d$-linear polar form of $p$. If $\nu_1,\nu_2$ both polarise $p$, the lemma gives $(\ast)=\nu_1$ and $(\ast)=\nu_2$, so $\nu_1=\nu_2$. Diagonal restriction $R$ and $P:=(\ast)$ satisfy $R\circ P=\operatorname{id}$ and $P\circ R=\operatorname{id}$, so $R$ is a linear bijection.
>
> *Invariance.* If $\lambda$ is invariant, then $p(\operatorname{Ad}_g\xi)=\lambda(\operatorname{Ad}_g\xi,\dots,\operatorname{Ad}_g\xi)=\lambda(\xi,\dots,\xi)=p(\xi)$. Conversely, if $p$ is invariant, then since $\operatorname{Ad}_g$ is linear, $\lambda(\operatorname{Ad}_g\xi_1,\dots,\operatorname{Ad}_g\xi_d)=\tfrac{1}{d!}\sum_S(-1)^{d-|S|}p(\operatorname{Ad}_g\eta_S)=\tfrac{1}{d!}\sum_S(-1)^{d-|S|}p(\eta_S)=\lambda(\xi_1,\dots,\xi_d)$.
>
> *Determinant.* For $d=2$, $(\ast)$ reads $\lambda(\xi_1,\xi_2)=\tfrac12(\det(\xi_1+\xi_2)-\det\xi_1-\det\xi_2)$. The entrywise computation gives $\det(\xi_1+\xi_2)-\det\xi_1-\det\xi_2=\operatorname{tr}\xi_1\operatorname{tr}\xi_2-\operatorname{tr}(\xi_1\xi_2)$, so $\lambda(\xi_1,\xi_2)=\tfrac12(\operatorname{tr}\xi_1\operatorname{tr}\xi_2-\operatorname{tr}(\xi_1\xi_2))$, with diagonal $\tfrac12((\operatorname{tr}\xi)^2-\operatorname{tr}(\xi^2))=\det\xi$. $\blacksquare$

> [!warning] Illegal but tempting: defining $\lambda$ by "just symmetrise the polynomial's coefficients" and calling it canonical without proving uniqueness
> A natural shortcut is to *define* the polar form by the symmetrised-monomial construction $\mu$ of Step 2 and declare the problem solved. This produces *a* symmetric form with the right diagonal, but it does not by itself show the form is **unique** — a priori a different symmetric form might share the same diagonal, in which case "the" polar form and the transfer of invariance would be ill-posed. The uniqueness is exactly what the inversion lemma of Step 1 supplies: because $(\ast)$ recovers *any* symmetric form from its diagonal, two symmetric forms with equal diagonals are equal. Only after uniqueness is established may one speak of *the* polar form and transport invariance across the correspondence without ambiguity. Skipping the lemma is legitimate only in characteristic zero *and* only once one has separately proved that diagonal restriction is injective on symmetric forms — which is the lemma again.

Independent sanity check: the polar form $\lambda(\xi_1,\xi_2)=\tfrac12(\operatorname{tr}\xi_1\operatorname{tr}\xi_2-\operatorname{tr}(\xi_1\xi_2))$ is $\operatorname{Ad}$-invariant, as Part 2 predicts (the determinant is invariant). Directly: $\operatorname{tr}(\operatorname{Ad}_g\xi)=\operatorname{tr}(g\xi g^{-1})=\operatorname{tr}\xi$ and $\operatorname{tr}(\operatorname{Ad}_g\xi_1\operatorname{Ad}_g\xi_2)=\operatorname{tr}(g\xi_1\xi_2 g^{-1})=\operatorname{tr}(\xi_1\xi_2)$, so both terms of $\lambda$ are conjugation-invariant, confirming invariance of $\lambda$ independently of the general theorem.

---

# Key Takeaways

**Polarisation is inclusion–exclusion: to invert "restrict to the diagonal", take a signed sum over the subsets of the argument slots.** The reusable engine of this exercise is the formula $(\ast)$ and, more importantly, the reason it works — the signed superset sum $\sum_{S\supseteq T}(-1)^{d-|S|}$ collapses by the binomial theorem to a Kronecker delta detecting $|T|=d$, which annihilates every non-injective substitution and leaves only the permutations. This is the same Möbius-inversion mechanism that recovers a measure from its cumulative distribution, a set function from its partial sums, or a symmetric bilinear form from its quadratic form; recognising a diagonal-restriction problem as an inclusion–exclusion inversion is what turns an apparently hard existence-and-uniqueness question into a bookkeeping computation. The trigger condition is precisely the shape "reconstruct a symmetric multi-argument object from its equal-argument values", and the diagnostic that the reconstruction will be a signed subset sum is that the forward map (diagonal restriction) loses exactly the information distinguishing the off-diagonal slots, information the alternating signs are engineered to reassemble.

**Separate existence from uniqueness, and route uniqueness through an inversion lemma stated for arbitrary inputs.** A structural lesson of the proof is that the cleanest path proves the inversion lemma for an *arbitrary* symmetric form $\nu$, not for the specific $p$ in hand. That single lemma simultaneously yields uniqueness (two forms with the same diagonal are both returned by $(\ast)$, hence equal), the explicit formula, and — once existence is supplied separately by symmetrising a monomial — the fact that $(\ast)$ actually is symmetric and multilinear. The general heuristic worth carrying: when asked to show a construction is well defined and canonical, look for a *retraction* — a formula that recovers the input from the output — because a retraction proves injectivity of the forward map in one stroke, and injectivity is usually the whole content of "canonical". Trying instead to verify symmetry, multilinearity, and the diagonal property of $(\ast)$ by direct expansion is the tempting but longer road, and it never delivers uniqueness on its own.

**Invariance is a property of the correspondence, not of either presentation alone, and it transfers because the group acts linearly.** The equivalence of Bär's invariant multilinear form and Haydys's invariant polynomial is not a coincidence of two definitions but a consequence of a single fact: $\operatorname{Ad}_g$ is a linear map, so it commutes both with evaluation on the diagonal and with the linear formula $(\ast)$. Whenever two encodings of an object are related by a linear isomorphism that is equivariant for a group action, an invariance visible in one encoding is automatically present in the other; the polynomial-versus-tensor dictionary here is the prototype. This is why, in the chapter to come, one may compute a Chern–Weil form either by evaluating an invariant polynomial on the curvature matrix or by feeding the curvature $d$ times into the polar multilinear form — the two give the same closed form because the presentations are equivariantly isomorphic. The transferable pattern: to move an invariance across a change of representation, check only that the change of representation is linear and commutes with the group action.

**Low-degree polar forms reduce to trace pairings, and $\det$ on $\mathfrak{gl}_2$ polarises to the fundamental symmetric bilinear form $\tfrac12(\operatorname{tr}\xi_1\operatorname{tr}\xi_2-\operatorname{tr}(\xi_1\xi_2))$.** The concrete computation is worth remembering as a primitive: the polar form of the degree-two invariant $\det$ is, up to the factor $\tfrac12$, the pairing $\operatorname{tr}\xi_1\operatorname{tr}\xi_2-\operatorname{tr}(\xi_1\xi_2)$, whose diagonal reproduces the $2\times2$ identity $(\operatorname{tr}\xi)^2-\operatorname{tr}(\xi^2)=2\det\xi$. On the traceless subalgebra $\mathfrak{su}(2)$ the first term drops and the polar form becomes $-\tfrac12\operatorname{tr}(\xi_1\xi_2)$, which is exactly the $\operatorname{Ad}$-invariant inner product used to build the Yang–Mills functional and the second Chern number; the companion drill [[Ex - The Coefficients of the Characteristic Polynomial are Ad-Invariant]] arrives at the same $c_2=\det$ from the characteristic-polynomial side and pins the sign. The general trigger: when a characteristic-class computation needs the *bilinear* pairing behind a quadratic invariant — an energy, a norm, a cup-product form — polarise the invariant, and in the classical matrix cases the answer will be a combination of $\operatorname{tr}\xi_1\operatorname{tr}\xi_2$ and $\operatorname{tr}(\xi_1\xi_2)$ whose coefficients are fixed by matching the diagonal.
