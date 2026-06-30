---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Alternate Forms and the Exterior Product"
  - "Def - Tensors on Minkowski Space"
tags: [physics, special-relativity]
---

# Problem Statement

Work in four dimensions, mostly-minus signature, $c = 1$.

1. Show that a $p$-form has independent components only for strictly increasing index tuples $\alpha_1 < \cdots < \alpha_p$, and hence that $\dim\mathscr{A}_p(E) = \binom{4}{p}$.
2. Tabulate the dimensions for $p = 0, 1, 2, 3, 4$, obtaining $1, 4, 6, 4, 1$, and confirm $\sum_p\dim\mathscr{A}_p = 2^4 = 16$.
3. Prove that $\mathscr{A}_p(E) = \{0\}$ for $p > 4$, and explain why the top non-trivial degree is $p = 4 = \dim E$.
4. Observe the symmetry $\binom{4}{p} = \binom{4}{4-p}$ and explain why it is the precondition for [[Def - The Hodge Star|Hodge duality]].

**Recall:**

![[Def - Alternate Forms and the Exterior Product#The Definition]]

A [[Def - Alternate Forms and the Exterior Product|p-form]] is a fully antisymmetric type-$(0,p)$ tensor; its components $A_{\alpha_1\dots\alpha_p}$ are antisymmetric, vanishing when two indices coincide and equal up to sign when the indices are permuted. The [[Def - The Hodge Star|Hodge star]] $\star : \mathscr{A}_p \to \mathscr{A}_{4-p}$ requires $\dim\mathscr{A}_p = \dim\mathscr{A}_{4-p}$ to be an isomorphism.

---

# Convergent Strategy

**Problem class.** A *structural / counting* problem establishing the dimensions of the exterior algebra. The [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality#Problem-Solving Strategy|topic strategy]]: count independent antisymmetric components by choosing distinct indices up to order.

**Assumption pattern.** Full antisymmetry is the only input: it forces components with a repeated index to vanish and components related by a permutation to be equal up to sign, so an independent component is a *choice of $p$ distinct values out of $4$*, unordered.

**Theorem routing.** Part 1: count strictly-increasing tuples = $\binom{4}{p}$. Part 2: evaluate the binomial coefficients and sum. Part 3: no $p > 4$ distinct values exist in $\{0,1,2,3\}$. Part 4: the binomial symmetry is the dimension match Hodge duality needs.

**Key decision point.** The crux is recognising that an independent component of a $p$-form is a $p$-element *subset* of $\{0,1,2,3\}$, not an ordered tuple — antisymmetry collapses all orderings to one (up to sign) and kills repeats. This subset-counting is what yields the binomial coefficients and, with them, the symmetry that makes Hodge duality possible. Seeing "independent component = subset" is the lesson.

---

# Legal Operations Used

1. **Operation 5 from the topic page (expand a $p$-form in the wedge basis).** The counting is the count of basis monomials $e^{\alpha_1}\wedge\cdots\wedge e^{\alpha_p}$ with $\alpha_1 < \cdots < \alpha_p$.

---

# Hints

> [!note]- Hint 1
> Antisymmetry means $A_{\alpha_1\dots\alpha_p}$ vanishes if two indices are equal, and is determined (up to sign) by the *set* $\{\alpha_1, \dots, \alpha_p\}$. So an independent component is a choice of $p$ distinct values from $\{0,1,2,3\}$, unordered: $\binom{4}{p}$ of them.

> [!note]- Hint 2
> $\binom{4}{0} = 1$, $\binom{4}{1} = 4$, $\binom{4}{2} = 6$, $\binom{4}{3} = 4$, $\binom{4}{4} = 1$. The sum $\sum_p\binom{4}{p} = 2^4 = 16$ counts all subsets of a $4$-element set.

> [!note]- Hint 3
> A nonzero component needs $p$ *distinct* indices from $\{0,1,2,3\}$. For $p > 4$ this is impossible (only four values available), so every component vanishes and $\mathscr{A}_p(E) = \{0\}$.

---

# Solution

The dimensions of the exterior algebra are pure combinatorics: an independent component is a subset. The plan: show independent components are strictly-increasing tuples (Step 1), tabulate the binomials (Step 2), prove the truncation at $p = 4$ (Step 3), and read the binomial symmetry as the Hodge precondition (Step 4).

**Step 1: $\dim\mathscr{A}_p(E) = \binom{4}{p}$.**

> [!note]- Derivation
> A [[Def - Alternate Forms and the Exterior Product|p-form]] has components $A_{\alpha_1\dots\alpha_p}$ that are fully antisymmetric. Two consequences:
> - *Repeats vanish.* If any two indices are equal, swapping them leaves the component unchanged but antisymmetry flips its sign, so $A_{\dots\alpha\dots\alpha\dots} = -A_{\dots\alpha\dots\alpha\dots} = 0$.
> - *Orderings are equal up to sign.* For distinct indices, any permutation $\sigma$ gives $A_{\alpha_{\sigma(1)}\dots\alpha_{\sigma(p)}} = (-1)^{k(\sigma)}A_{\alpha_1\dots\alpha_p}$, so all orderings of the same set are determined by one.
>
> Hence an *independent* component corresponds to a choice of $p$ *distinct* indices from $\{0,1,2,3\}$, taken once (say in increasing order). The number of such choices is the number of $p$-element subsets of a $4$-element set:
> $$\dim\mathscr{A}_p(E) = \binom{4}{p}.$$
> Equivalently, the basis monomials $e^{\alpha_1}\wedge\cdots\wedge e^{\alpha_p}$ with $\alpha_1 < \cdots < \alpha_p$ are linearly independent and span $\mathscr{A}_p(E)$, and there are $\binom{4}{p}$ of them.

**Step 2: the dimensions are $1, 4, 6, 4, 1$, summing to $16$.**

> [!note]- Derivation
> Evaluate:
> $$\dim\mathscr{A}_0 = \binom{4}{0} = 1, \quad \dim\mathscr{A}_1 = \binom{4}{1} = 4, \quad \dim\mathscr{A}_2 = \binom{4}{2} = 6, \quad \dim\mathscr{A}_3 = \binom{4}{3} = 4, \quad \dim\mathscr{A}_4 = \binom{4}{4} = 1.$$
> The sequence $1, 4, 6, 4, 1$ is the fourth row of Pascal's triangle. The total dimension of the full exterior algebra is
> $$\sum_{p=0}^{4}\dim\mathscr{A}_p = \sum_{p=0}^{4}\binom{4}{p} = 2^4 = 16,$$
> which counts *all* subsets of $\{0,1,2,3\}$ — each subset (of any size) gives one basis monomial of the exterior algebra $\Lambda^\bullet E^*$. The checks: $\mathscr{A}_0 = \mathbb{R}$ (scalars, dimension $1$), $\mathscr{A}_1 = E^*$ (one-forms, dimension $4$), $\mathscr{A}_2$ has the six bivector components, and $\mathscr{A}_4$ is spanned by the single volume form $e^0\wedge e^1\wedge e^2\wedge e^3$.

**Step 3: $\mathscr{A}_p(E) = \{0\}$ for $p > 4$.**

> [!note]- Derivation
> A nonzero component of a $p$-form requires $p$ *distinct* index values (Step 1). The index set is $\{0, 1, 2, 3\}$, with only $4$ elements. For $p > 4$, the pigeonhole principle forces at least two of the $p$ indices to coincide in *every* component, so every component vanishes by antisymmetry:
> $$\mathscr{A}_p(E) = \{0\} \quad\text{for } p > 4.$$
> The top non-trivial degree is therefore $p = 4 = \dim E$: there is exactly one way to choose all four distinct indices, giving $\dim\mathscr{A}_4 = 1$. This is why the exterior algebra of a four-dimensional space is *finite*, truncating at degree $4$ — and why $\binom{4}{p} = 0$ for $p > 4$ as binomial coefficients.

**Step 4: $\binom{4}{p} = \binom{4}{4-p}$ is the precondition for Hodge duality.**

> [!note]- Derivation
> The binomial coefficients satisfy $\binom{4}{p} = \binom{4}{4-p}$ — the symmetry of Pascal's triangle, here $1, 4, 6, 4, 1$ read forwards equals read backwards. Combinatorially: choosing a $p$-element subset is the same as choosing its $(4-p)$-element complement. Hence
> $$\dim\mathscr{A}_p(E) = \dim\mathscr{A}_{4-p}(E).$$
> This equality is exactly what makes the [[Def - The Hodge Star|Hodge star]] $\star : \mathscr{A}_p \to \mathscr{A}_{4-p}$ a candidate *isomorphism*: a linear map between vector spaces can be bijective only if they have the same dimension. The metric and orientation then supply a *canonical* such isomorphism. The pairing $p \leftrightarrow 4 - p$ is: $0\leftrightarrow4$ (scalars $\leftrightarrow$ top forms), $1\leftrightarrow3$ (vectors $\leftrightarrow$ "pseudo-vectors"), $2\leftrightarrow2$ ($2$-forms to themselves — which is why $\star$ is an automorphism of $\mathscr{A}_2$, the self-dual story). Without this dimension match there could be no Hodge duality.

> [!note]- Complete formal solution
> **(1)** Antisymmetry makes a component vanish on repeated indices and equal (up to sign) for permuted indices, so an independent component is a $p$-subset of $\{0,1,2,3\}$: $\dim\mathscr{A}_p(E) = \binom{4}{p}$.
> **(2)** $\binom{4}{0,1,2,3,4} = 1, 4, 6, 4, 1$; $\sum = 2^4 = 16$.
> **(3)** $p > 4$ forces a repeated index (pigeonhole, only $4$ values), so all components vanish: $\mathscr{A}_p(E) = \{0\}$; the top degree is $p = 4 = \dim E$.
> **(4)** $\binom{4}{p} = \binom{4}{4-p}$ (complement of a subset) gives $\dim\mathscr{A}_p = \dim\mathscr{A}_{4-p}$, the dimension match that lets $\star$ be an isomorphism. $\blacksquare$

---

# Key Takeaways

**An independent component of a $p$-form is a subset, not a tuple — antisymmetry collapses orderings and kills repeats.** The dimension count $\binom{4}{p}$ comes from the single observation that full antisymmetry makes a component depend only on the *set* of its indices: repeated indices give zero, and reordering gives the same value up to sign. So counting independent components is counting $p$-element subsets of the index set. This subset-counting principle is the reusable core: it gives $\binom{n}{p}$ for $p$-forms in $n$ dimensions, the truncation at $p = n$, and the total dimension $2^n$ of the exterior algebra. Whenever you need the number of independent components of an antisymmetric object, count subsets; whenever you need the components of a symmetric object, count multisets (combinations with repetition). The contrast — subsets for antisymmetric, multisets for symmetric — is the combinatorial signature of the two symmetry types.

**The exterior algebra of an $n$-dimensional space is finite, topping out at degree $n$.** Unlike the tensor algebra (which has tensors of every rank), the exterior algebra stops at $p = n = \dim E$, because you cannot choose more than $n$ distinct indices. This finiteness is what makes forms computationally tractable and what makes the [[Def - The Levi-Civita Tensor|top form]] (degree $n$) one-dimensional — the home of the determinant and the volume form. The reusable consequence: in four dimensions, any wedge of five or more one-forms is automatically zero, so any expression with too many wedged factors vanishes before you compute it. This is constantly exploited to truncate calculations — for instance, in checking that the field strength's wedge $F\wedge F\wedge F$ vanishes (it is a $6$-form in four dimensions, hence zero), or that the only non-trivial Chern-form in four dimensions is $F\wedge F$.

**The symmetry $\binom{n}{p} = \binom{n}{n-p}$ is what makes Hodge duality possible, and the self-duality of $\mathscr{A}_2$ in four dimensions is the case $p = n/2$.** The dimension match $\dim\mathscr{A}_p = \dim\mathscr{A}_{n-p}$, a triviality of binomial coefficients, is the structural precondition for the [[Def - The Hodge Star|Hodge star]] to be an isomorphism — no dimension match, no duality. The special middle case $p = n - p$, which in four dimensions is $p = 2$, makes $\star$ an *automorphism* of $\mathscr{A}_2$ (a $2$-form maps to a $2$-form), and this is precisely the setting of the self-dual/anti-self-dual decomposition and the $\mathbf E \pm i\mathbf B$ structure of electromagnetism. The transferable observation: the most interesting Hodge phenomena happen in the middle degree $p = n/2$ (when $n$ is even), where $\star$ acts on a space to itself and can have eigenforms; in four-dimensional spacetime this middle degree is the degree of the electromagnetic field, which is no coincidence — the field is a $2$-form precisely because $2$ is the self-dual middle degree of four-dimensional spacetime.
