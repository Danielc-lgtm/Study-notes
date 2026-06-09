---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Module"
  - "Def - Free Module"
  - "Def - Prime and Maximal Ideal"
  - "Def - Multiplicative Set and Localization"
  - "Def - Local Property (Localizable and Local-to-Global)"
  - "Thm - Prime Ideals of a Localization"
tags: [algebra, commutative-algebra]
---

# Problem Statement

An $R$-module $M$ is **locally free** if $M_{\mathfrak{p}}$ is a [[Def - Free Module|free]] $R_{\mathfrak{p}}$-module for every [[Def - Prime and Maximal Ideal|prime]] $\mathfrak{p}$. Prove that **freeness is not a local property**: exhibit a ring $R$ and a module $M$ that is locally free but not free.

Concretely (Becker Example 4.30), take $R = \mathbb{C}\times\mathbb{C}$. Show:
1. $\operatorname{Spec} R = \{\mathfrak{p}_1, \mathfrak{p}_2\}$ with $\mathfrak{p}_1 = \mathbb{C}\times\{0\}$, $\mathfrak{p}_2 = \{0\}\times\mathbb{C}$, and $R_{\mathfrak{p}_1}\cong R_{\mathfrak{p}_2}\cong\mathbb{C}$ — so $R$ is *locally a field*, whence every $R$-module is locally free.
2. The ideal $M = \mathbb{C}\times\{0\}$ is an $R$-module that is **not free**.

Then explain (Example Sheet 3, Q3 and Remark 4.31) the more striking integral-domain version: the ideal $M = (2, 1+\sqrt{-5})\trianglelefteq\mathbb{Z}[\sqrt{-5}]$ is locally free (it is projective, hence locally free) but not free (it is a non-principal ideal). This is the algebraic seed of nontrivial **vector bundles**.

**Recall:**

![[Def - Free Module#The Definition]]

A [[Def - Free Module|free module]] has a basis: a linearly independent generating set. The ideals of a finite product $\prod R_i$ are exactly the products $\prod I_i$ of ideals, prime iff exactly one factor is prime and the rest are the whole ring. [[Def - Local Property (Localizable and Local-to-Global)|Locally free]] means free at every prime.

![[Thm - Prime Ideals of a Localization#Statement]]

---

# Convergent Strategy

**Problem class.** This is a *counterexample-construction* problem of the highest difficulty: demonstrate that a plausible local-to-global statement *fails*, by building a witness. Per the [[Commutative Algebra IV — Localization#Legal Operations|topic's illegal-but-tempting list]], "freeness is local" is the canonical false belief, and the value is in the negative result — it draws the boundary of the local–global principle.

**Assumption pattern.** The strategy is to choose a ring whose localizations are *as simple as possible* (fields), so that "locally free" is automatic and free of content, then find a single module that fails to be free for a *global* reason. The recognisable trigger: a *disconnected* spectrum (a product of rings) has localizations that collapse to single factors, so it is "locally a field" while globally carrying idempotents — and idempotents annihilate ideals, destroying linear independence.

**Theorem routing.** Part 1: compute $\operatorname{Spec}(\mathbb{C}\times\mathbb{C})$ from the product structure, then localize via the [[Thm - Prime Ideals of a Localization|prime correspondence]] / direct computation to get $R_{\mathfrak{p}_i}\cong\mathbb{C}$; since a field's modules are all free (vector spaces have bases), $M_{\mathfrak{p}}$ is free for every $\mathfrak{p}$ and every $M$. Part 2: show $M = \mathbb{C}\times\{0\}$ has *no* linearly independent generating set — the idempotent $(0,1)$ annihilates all of $M$, so the empty set is the only independent subset, and it does not generate. The domain version routes through projective $\Rightarrow$ locally free (projective modules over local rings are free) and non-principal $\Rightarrow$ non-free for an ideal.

**Key decision point.** Two crucial choices. First, *use a disconnected ring* so that local freeness is vacuous (every localization is a field) — this isolates the global obstruction cleanly. Second, *pick the module to be a factor ideal* $\mathbb{C}\times\{0\}$, because the complementary idempotent $(0,1)$ annihilates it, which is exactly what forbids a basis: any nonzero element $(x,0)$ satisfies the nontrivial relation $(0,1)\cdot(x,0) = 0$, so no subset is linearly independent. The non-obvious insight is that *non-freeness here is a torsion phenomenon caused by a zero-divisor*, even though over a field there is no torsion — torsion appears only globally.

---

# Legal Operations Used

This solution deploys the following [[Commutative Algebra IV — Localization#Legal Operations|legal operations from the topic page]]:

1. **Operation 6 (read primes off disjointness).** Computing $\operatorname{Spec}(\mathbb{C}\times\mathbb{C}) = \{\mathfrak{p}_1, \mathfrak{p}_2\}$ and the localizations.

2. **Operation 2 (invoke the universal property).** Identifying $R_{\mathfrak{p}_1}\cong\mathbb{C}$ via the projection $(x,y)\mapsto y$ inverting $S$.

3. **Operation 1 (clear denominators).** Showing $(x,0)/(a,b) = 0$ in $R_{\mathfrak{p}_1}$ because $(0,1)\in S$ kills $(x,0)$.

---

# Hints

> [!note]- Hint 1
> To make "locally free" trivially true, choose a ring all of whose localizations are *fields* — then every module is a vector space locally, hence locally free. A product of two fields is the simplest such ring. What are the primes of $\mathbb{C}\times\mathbb{C}$, and what do its localizations look like?

> [!note]- Hint 2
> The primes of $R_1\times R_2$ are $\mathfrak{p}\times R_2$ and $R_1\times\mathfrak{q}$ for primes $\mathfrak{p}, \mathfrak{q}$. For $\mathbb{C}\times\mathbb{C}$ these are $\mathfrak{p}_1 = \mathbb{C}\times\{0\}$ and $\mathfrak{p}_2 = \{0\}\times\mathbb{C}$. Localizing at $\mathfrak{p}_1$ inverts $S = \mathbb{C}\times(\mathbb{C}\setminus\{0\})$; the projection $(x,y)\mapsto y$ inverts $S$. What is $R_{\mathfrak{p}_1}$?

> [!note]- Hint 3
> Now find a module that is not free. Try the ideal $M = \mathbb{C}\times\{0\}$. The complementary idempotent $(0,1)\in R$ satisfies $(0,1)\cdot(x,0) = (0,0)$ for *every* $(x,0)\in M$. What does this say about linear independence of any subset of $M$? Can $M$ have a basis?

> [!note]- Hint 4
> Every nonzero $(x,0)\in M$ obeys the nontrivial relation $(0,1)(x,0) = 0$ with $(0,1)\neq 0$ in $R$ — so $\{(x,0)\}$ is *linearly dependent*. Hence the only linearly independent subset of $M$ is $\varnothing$, which spans only $\{0\}\neq M$. So $M$ has no basis: not free. Yet $M_{\mathfrak{p}_i}$ is free (a vector space over $\mathbb{C}$). Locally free, not free.

---

# Solution

Choose $R = \mathbb{C}\times\mathbb{C}$ so that every localization is the field $\mathbb{C}$, making *every* module locally free for free. Then the ideal $M = \mathbb{C}\times\{0\}$ fails to be free: the idempotent $(0,1)$ annihilates it, so no subset is linearly independent except $\varnothing$, which does not generate. The domain version replaces "field localizations" by "projective $\Rightarrow$ locally free" and "annihilated by an idempotent" by "non-principal ideal".

**Step 1: $\operatorname{Spec}(\mathbb{C}\times\mathbb{C})$ has exactly two points.**

The primes are $\mathfrak{p}_1 = \mathbb{C}\times\{0\}$ and $\mathfrak{p}_2 = \{0\}\times\mathbb{C}$.

> [!note]- Derivation
> The ideals of a product $R_1\times R_2$ are exactly $I_1\times I_2$ with $I_j\trianglelefteq R_j$ (project and recombine). Such an ideal is prime iff the quotient $(R_1/I_1)\times(R_2/I_2)$ is a domain, which forces one factor to be a domain and the other to be the zero ring — i.e. one $I_{j}$ is prime and the other is the whole ring. For $R = \mathbb{C}\times\mathbb{C}$, the only prime of $\mathbb{C}$ is $(0)$, so the primes of $R$ are $(0)\times\mathbb{C} = \{0\}\times\mathbb{C} =: \mathfrak{p}_2$ and $\mathbb{C}\times(0) = \mathbb{C}\times\{0\} =: \mathfrak{p}_1$. Both are maximal (the quotients are $\mathbb{C}$). So $\operatorname{Spec} R = \{\mathfrak{p}_1, \mathfrak{p}_2\}$, two closed points, a disconnected space.

**Step 2: $R_{\mathfrak{p}_1}\cong\mathbb{C}$ — $R$ is locally a field.**

Localizing at $\mathfrak{p}_1$ collapses $R$ to $\mathbb{C}$ via the second projection.

> [!note]- Derivation
> $R_{\mathfrak{p}_1} = S^{-1}R$ with $S = R\setminus\mathfrak{p}_1 = \mathbb{C}\times(\mathbb{C}\setminus\{0\})$. The projection $\phi_0 : R\to\mathbb{C}$, $(x,y)\mapsto y$, sends every $(a,b)\in S$ (with $b\neq 0$) to a unit $b\in\mathbb{C}^\times$, so by the [[Thm - Universal Property of Localization|universal property]] it factors as $\phi : R_{\mathfrak{p}_1}\to\mathbb{C}$, $\phi(\tfrac{(x,y)}{(a,b)}) = \tfrac yb$. This $\phi$ is surjective. Its kernel is the set of $\tfrac{(x,0)}{(a,b)}$ (numerator with second coordinate $0$); but each such fraction is $0$ in $R_{\mathfrak{p}_1}$, because $(0,1)\in S$ annihilates $(x,0)$: $(0,1)\cdot(x,0) = (0,0)$, so $\tfrac{(x,0)}{(a,b)} = \tfrac01$. Hence $\phi$ is injective too, so $R_{\mathfrak{p}_1}\cong\mathbb{C}$. Symmetrically $R_{\mathfrak{p}_2}\cong\mathbb{C}$ (project to the first coordinate). So both localizations are fields.

**Step 3: Every $R$-module is locally free.**

Over a field, every module is free, so $M_{\mathfrak{p}}$ is free for every $M$ and every $\mathfrak{p}$.

> [!note]- Derivation
> For any $R$-module $M$ and either prime $\mathfrak{p}_i$, the localization $M_{\mathfrak{p}_i}$ is a module over $R_{\mathfrak{p}_i}\cong\mathbb{C}$, i.e. a $\mathbb{C}$-vector space. Every vector space has a basis, hence is [[Def - Free Module|free]]. So $M_{\mathfrak{p}_1}$ and $M_{\mathfrak{p}_2}$ are free, i.e. $M$ is **locally free** — automatically, for *every* $R$-module $M$. The "locally free" condition carries no information over this ring.

**Step 4: The ideal $M = \mathbb{C}\times\{0\}$ is not free.**

The idempotent $(0,1)$ annihilates $M$, so no nonempty subset is linearly independent.

> [!note]- Derivation
> $M = \mathbb{C}\times\{0\}$ is an ideal of $R$, hence an $R$-module. Consider linear independence over $R$. For *any* element $(x,0)\in M$,
> $$(0,1)\cdot(x,0) = (0\cdot x,\ 1\cdot 0) = (0,0),$$
> and $(0,1)\neq(0,0)$ in $R$. So $\{(x,0)\}$ satisfies the nontrivial relation $r\cdot(x,0) = 0$ with $r = (0,1)\neq 0$ — it is *linearly dependent*. Therefore no nonempty subset of $M$ is linearly independent; the only [[Def - Free Module|linearly independent]] subset is $\varnothing$. But $\varnothing$ generates only $\{0\}$, and $M\neq\{0\}$ (it contains $(1,0)$). So $M$ has no basis: $M$ is **not free**.
>
> Combining Steps 3 and 4: $M$ is locally free but not free. Hence freeness is **not a local property**. $\blacksquare$

**Step 5: The integral-domain version (ES3 Q3 / Remark 4.31).**

Over a domain, $M = (2, 1+\sqrt{-5})\trianglelefteq\mathbb{Z}[\sqrt{-5}]$ is locally free (projective) but not free (non-principal).

> [!note]- Derivation
> The product example is "cheap" because $R$ has zero-divisors; the deep example uses a *domain*, where there is no torsion. Let $R = \mathbb{Z}[\sqrt{-5}]$ (a domain, the ring of integers of $\mathbb{Q}(\sqrt{-5})$) and $M = (2, 1+\sqrt{-5})$. Two facts:
>
> *Locally free:* $M$ is **projective** (it is a direct summand of $R\oplus R$ — concretely, the failure of unique factorisation $2\cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$ makes $M$ an invertible ideal, and invertible ideals are projective). A projective module over a *local* ring is free (a finitely generated projective over a local ring is free, by Nakayama). So $M_{\mathfrak{p}}$ is free over the local ring $R_{\mathfrak{p}}$ for every $\mathfrak{p}$: $M$ is locally free.
>
> *Not free:* an ideal of a domain $R$ is free iff it is principal and generated by a non-zero-divisor (then $a\mapsto ax : R\xrightarrow{\sim}(x)$ is an isomorphism, rank $1$; the zero ideal is free of rank $0$; no other ideal is free, since two elements $x, y$ of an ideal always satisfy the relation $y\cdot x - x\cdot y = 0$, so an ideal needs a *single* generator to be free). But $M = (2, 1+\sqrt{-5})$ is **not principal** (this is the standard witness that $\mathbb{Z}[\sqrt{-5}]$ is not a UFD: if $M = (\alpha)$ then $\alpha\mid 2$ and $\alpha\mid 1+\sqrt{-5}$, and a norm computation, $N(2) = 4$, $N(1+\sqrt{-5}) = 6$, $\gcd = 2 = N(\alpha)$ has no solution with $\alpha\in\mathbb{Z}[\sqrt{-5}]$). So $M$ is not free.
>
> Thus $M$ is locally free but not free, over an *integral domain* — a genuine non-trivial line bundle on $\operatorname{Spec}\mathbb{Z}[\sqrt{-5}]$, with non-trivial class in the ideal class group / Picard group.

> [!note]- Complete formal solution
> **Product example.** $R = \mathbb{C}\times\mathbb{C}$. Its primes are $\mathfrak{p}_1 = \mathbb{C}\times\{0\}$, $\mathfrak{p}_2 = \{0\}\times\mathbb{C}$ (ideals of a product are products of ideals, prime iff one factor is prime and the other is the whole ring). $R_{\mathfrak{p}_1}\cong\mathbb{C}$: the projection $(x,y)\mapsto y$ inverts $S = R\setminus\mathfrak{p}_1$ and induces an isomorphism, since $(x,0)$ is killed by $(0,1)\in S$. Symmetrically $R_{\mathfrak{p}_2}\cong\mathbb{C}$. Hence every $R$-module localizes to a vector space, so is locally free.
>
> The ideal $M = \mathbb{C}\times\{0\}$ is not free: for every $(x,0)\in M$, $(0,1)(x,0) = 0$ with $(0,1)\neq 0$, so no nonempty subset is linearly independent; the only independent subset $\varnothing$ does not generate $M\neq 0$. So $M$ is locally free but not free — freeness is not local.
>
> **Domain example.** $R = \mathbb{Z}[\sqrt{-5}]$, $M = (2, 1+\sqrt{-5})$. $M$ is projective (invertible ideal), and projective over a local ring is free, so $M$ is locally free. But $M$ is not principal (norm argument), and a non-principal ideal of a domain is not free. So $M$ is locally free but not free. $\blacksquare$

---

# Key Takeaways

**To break a local-to-global statement, make "local" vacuous and isolate a global obstruction.** The whole construction is strategic: choose $R$ so simple locally (every $R_{\mathfrak{p}}$ a field) that "locally free" holds for *every* module with no content, then find one module that fails to be free for a reason invisible after localizing. This is the universal template for disproving a local-to-global claim — *engineer trivial local data, exhibit a nontrivial global witness*. The same disconnected-spectrum trick disproves "domain is local" ([[Ex - Being reduced is a local property|see there]]): a product of fields is locally a field but globally has zero-divisors. Recognise the pattern: when a property is suspected non-local, reach for $R_1\times R_2$ (disconnected $\operatorname{Spec}$) or a Dedekind domain with nontrivial class group (the projective-non-free ideals), the two canonical sources of local-global failure.

**Non-freeness is a torsion/idempotent phenomenon that local rings cannot see.** Over the product $\mathbb{C}\times\mathbb{C}$, the obstruction to a basis for $M = \mathbb{C}\times\{0\}$ is the relation $(0,1)\cdot(x,0) = 0$: the complementary idempotent annihilates the module, so every element is "torsion", and torsion forbids linear independence. But localizing kills exactly this — at $\mathfrak{p}_1$, the idempotent $(0,1)$ becomes a unit (it is in $S$), so the relation disappears and $M_{\mathfrak{p}_1}$ is a free $\mathbb{C}$-module. The transferable diagnostic: *freeness fails when there are global relations (torsion, twisting) that every localization trivialises*. Over a domain there is no torsion, so the obstruction is subtler — it is the *twisting* of a non-principal ideal, a genuine topological non-triviality rather than torsion. Knowing which kind of obstruction you face (torsion over non-domains, twisting over domains) tells you which example to build.

**This is the algebraic birth certificate of vector bundles and the Serre–Swan correspondence.** A locally free module that is not free is *exactly* a non-trivial vector bundle: locally trivial (free at every point) yet globally twisted (not free). The **Serre–Swan** theorem makes this precise — finitely generated projective modules over $R$ correspond to vector bundles on $\operatorname{Spec} R$ (or on a compact space, to $C(X)$-modules), with free $=$ trivial bundle. The ideal $(2, 1+\sqrt{-5})$ is a non-trivial *line bundle* on $\operatorname{Spec}\mathbb{Z}[\sqrt{-5}]$, and its class in the **ideal class group** (the Picard group) measures the failure of unique factorisation, which is the same number measuring the failure of freeness. So the failure of "freeness is local" is not a defect of the theory but its most fertile feature: it is where the entire subject of vector bundles, characteristic classes, and the class group is born, and it is the reason the [[Thm - The Local-Global Principle|local–global principle]] *must* exclude freeness from its list. The boundary of the principle is where geometry gets interesting.
