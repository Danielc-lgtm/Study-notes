---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Direct and Inverse Limits"
  - "Def - Directed Set and Direct System"
  - "Def - Group"
  - "Def - The I-adic Completion"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Fix a prime $p$. Consider the [[Def - Directed Set and Direct System|direct system]] of cyclic groups
$$\mathbb{Z}/p\mathbb{Z}\xrightarrow{\ \iota_1\ }\mathbb{Z}/p^2\mathbb{Z}\xrightarrow{\ \iota_2\ }\mathbb{Z}/p^3\mathbb{Z}\xrightarrow{\ \iota_3\ }\cdots,$$
where $\iota_n:\mathbb{Z}/p^n\mathbb{Z}\hookrightarrow\mathbb{Z}/p^{n+1}\mathbb{Z}$ is multiplication by $p$ (sending $1+p^n\mathbb{Z}\mapsto p+p^{n+1}\mathbb{Z}$), the inclusion of the unique subgroup of order $p^n$.

1. **(Identify the colimit.)** Prove $\varinjlim_n\mathbb{Z}/p^n\mathbb{Z}\cong\mathbb{Z}[1/p]/\mathbb{Z}$, the **Prüfer $p$-group** $\mathbb{Z}(p^\infty)$, equivalently the group of all $p$-power roots of unity in $\mathbb{C}^\times$.
2. **(Properties.)** Show $\mathbb{Z}(p^\infty)$ is an infinite, countable, **divisible** abelian group in which *every* element has finite order (a $p$-power), and that its proper subgroups are exactly the finite cyclic groups $\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}\cong\mathbb{Z}/p^n\mathbb{Z}$, totally ordered by inclusion.
3. **(Contrast with $\mathbb{Z}_p$.)** Explain why the *inverse* limit $\varprojlim_n\mathbb{Z}/p^n\mathbb{Z}=\mathbb{Z}_p$ of the *same* objects (with the opposite arrows, the projections) is utterly different: torsion-free, uncountable, not divisible.

**Recall:**

![[Def - Direct and Inverse Limits#The Definition]]

The [[Def - Direct and Inverse Limits|direct limit]] $\varinjlim X_i=\big(\coprod X_i\big)/\sim$ glues the objects, with $x_i\sim x_j$ iff $f_{ik}(x_i)=f_{jk}(x_j)$ for some $k$. Here every map is injective, so the system is a chain of subgroups and $\varinjlim$ is their increasing union.

![[Def - Directed Set and Direct System#The Definition]]

A group is **divisible** if for every element $g$ and every $n\geq1$ there is $h$ with $nh=g$ (in additive notation) — every element is infinitely divisible.

---

# Convergent Strategy

**Problem class.** This is an *identify-the-direct-limit-as-an-increasing-union* problem, the canonical worked example of the direct-limit side of the chapter. As the [[Commutative Algebra X — Completions and Limits#Problem-Solving Strategy|topic strategy]] records, when the transition maps are *inclusions*, the colimit is the union, and the recognition step is to find a single ambient group in which all the stages sit compatibly.

**Assumption pattern.** The trigger is *injective transition maps up a tower* — multiplication-by-$p$ embeddings $\mathbb{Z}/p^n\hookrightarrow\mathbb{Z}/p^{n+1}$. This is the opposite arrow-direction to a completion, and it signals "take the union", not "take threads". The ambient group is found by re-coordinatising: identify $\mathbb{Z}/p^n$ with the order-$p^n$ subgroup $\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}$ of $\mathbb{Q}/\mathbb{Z}$, under which the multiplication-by-$p$ map becomes an honest inclusion.

**Theorem routing.** The route is: (1) build the compatible maps $g_n:\mathbb{Z}/p^n\to\mathbb{Z}[1/p]/\mathbb{Z}$, $1\mapsto\frac{1}{p^n}$, check $g_{n+1}\circ\iota_n=g_n$, and use the [[Def - Direct and Inverse Limits|universal property]] plus surjectivity/injectivity to get the isomorphism; (2) divisibility and the torsion/subgroup structure are read off the explicit model $\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}$; (3) the contrast with $\mathbb{Z}_p$ is the duality "same objects, opposite arrows, dual limit" from [[Def - Direct and Inverse Limits]].

**Key decision point.** The non-obvious move is the *re-coordinatisation* $\mathbb{Z}/p^n\cong\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}$ that converts the multiplication-by-$p$ maps into inclusions. With the naive identification $\mathbb{Z}/p^n=\{0,\dots,p^n-1\}$ the map "multiply by $p$" looks like it *shrinks* (it lands in the multiples of $p$), and the union is opaque; with the $\frac{1}{p^n}$ identification the same map becomes the obvious inclusion of nested subgroups, and the union is transparently $\mathbb{Z}[1/p]/\mathbb{Z}$. Choosing the right coordinates is the whole difficulty.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra X — Completions and Limits#Legal Operations|the topic page's Legal Operations]]:

1. **Invoke the universal property of the direct limit (operation 1).** Build the colimit map from a compatible family $g_n:\mathbb{Z}/p^n\to\mathbb{Z}[1/p]/\mathbb{Z}$.

2. **Push a finite computation into one stage (operation 2, direct-limit form).** Every element of $\varinjlim$ comes from a single $\mathbb{Z}/p^n$, so finite computations and equalities are decided at one stage.

3. **Recognise the dual construction (operation 2, contrast).** The inverse limit of the same objects with reversed arrows is $\mathbb{Z}_p$ — "direct limits enlarge, inverse limits refine".

---

# Hints

> [!note]- Hint 1
> Each map is injective, so the system is a chain $\mathbb{Z}/p\subseteq\mathbb{Z}/p^2\subseteq\cdots$ of nested groups (once you identify them correctly), and the direct limit is their *union*. The trick is to find a single group containing compatible copies of all of them.

> [!note]- Hint 2
> Map $\mathbb{Z}/p^n\to\mathbb{Q}/\mathbb{Z}$ by $1+p^n\mathbb{Z}\mapsto\frac{1}{p^n}+\mathbb{Z}$. Check this sends the generator of $\mathbb{Z}/p^n$ to an element of order $p^n$, and that the multiplication-by-$p$ map $\iota_n$ becomes compatible: $\frac{1}{p^{n+1}}\cdot p=\frac{1}{p^n}$. So the images are the nested subgroups $\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}$.

> [!note]- Hint 3
> The union $\bigcup_n\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}=\mathbb{Z}[1/p]/\mathbb{Z}$ is the Prüfer group. For divisibility: given $\frac{a}{p^n}+\mathbb{Z}$ and any $m$, you must solve $mx=\frac{a}{p^n}$; if $p\nmid m$ this is easy, and dividing by $p$ goes one level up to $\frac{a}{p^{n+1}}$ — always available because the levels are unbounded.

> [!note]- Hint 4
> For the contrast: $\mathbb{Z}_p=\varprojlim\mathbb{Z}/p^n$ uses the *projections* $\mathbb{Z}/p^{n+1}\to\mathbb{Z}/p^n$, not the inclusions. A thread is a coherent system of residues (a left-infinite digit string) — there are uncountably many, none of finite order except $0$. Same objects, opposite arrows, dual limit.

---

# Solution

The proof re-coordinatises the cyclic groups as nested subgroups of $\mathbb{Q}/\mathbb{Z}$ so that the multiplication-by-$p$ maps become inclusions; the colimit is then the union $\mathbb{Z}[1/p]/\mathbb{Z}$, whose divisibility and subgroup structure are immediate from the model. The contrast with $\mathbb{Z}_p$ is the arrow-reversal duality.

**Step 1: The colimit is $\mathbb{Z}[1/p]/\mathbb{Z}$.**

The maps $g_n:\mathbb{Z}/p^n\mathbb{Z}\to\mathbb{Z}[1/p]/\mathbb{Z}$, $1+p^n\mathbb{Z}\mapsto\frac{1}{p^n}+\mathbb{Z}$, are compatible and induce an isomorphism $\varinjlim\mathbb{Z}/p^n\mathbb{Z}\cong\mathbb{Z}[1/p]/\mathbb{Z}$.

> [!note]- Derivation
> Define $g_n:\mathbb{Z}/p^n\mathbb{Z}\to\mathbb{Q}/\mathbb{Z}$ by $a+p^n\mathbb{Z}\mapsto\frac{a}{p^n}+\mathbb{Z}$. This is a well-defined injective group homomorphism (if $a\equiv a'\bmod p^n$ then $\frac{a-a'}{p^n}\in\mathbb{Z}$), with image the subgroup $\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}\cong\mathbb{Z}/p^n\mathbb{Z}$ of elements of order dividing $p^n$.
>
> *Compatibility with $\iota_n=(\times p)$.* We have $\iota_n(1+p^n\mathbb{Z})=p+p^{n+1}\mathbb{Z}$, so
> $$g_{n+1}(\iota_n(1+p^n\mathbb{Z}))=g_{n+1}(p+p^{n+1}\mathbb{Z})=\tfrac{p}{p^{n+1}}+\mathbb{Z}=\tfrac{1}{p^n}+\mathbb{Z}=g_n(1+p^n\mathbb{Z}).$$
> So $g_{n+1}\circ\iota_n=g_n$: the family $(g_n)$ is compatible. By the [[Def - Direct and Inverse Limits|universal property]] of the direct limit there is a unique $g:\varinjlim\mathbb{Z}/p^n\to\mathbb{Q}/\mathbb{Z}$ with $g\circ\lambda_n=g_n$.
>
> *$g$ is injective:* an element of $\varinjlim$ is $[\,a+p^n\mathbb{Z}\,]$ for some $n$; if $g$ kills it then $\frac{a}{p^n}\in\mathbb{Z}$, so $a\equiv0\bmod p^n$ and the element is already $0$. *$g$ has image $\bigcup_n\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}=\mathbb{Z}[1/p]/\mathbb{Z}$:* every $\frac{a}{p^n}+\mathbb{Z}$ is $g_n(a+p^n\mathbb{Z})$, and $\mathbb{Z}[1/p]/\mathbb{Z}$ is exactly the elements of $\mathbb{Q}/\mathbb{Z}$ whose order is a power of $p$, i.e. the union of the $\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}$. Hence $g$ is an isomorphism onto $\mathbb{Z}[1/p]/\mathbb{Z}=\mathbb{Z}(p^\infty)$. (Via $\frac{a}{p^n}+\mathbb{Z}\leftrightarrow e^{2\pi i a/p^n}$ this is the group of $p$-power roots of unity.)

**Step 2: $\mathbb{Z}(p^\infty)$ is countable, divisible, all-torsion, with totally-ordered finite cyclic proper subgroups.**

> [!note]- Derivation
> *Countable and infinite:* it is a countable union $\bigcup_n\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}$ of finite sets, strictly increasing, so countably infinite.
>
> *Every element has $p$-power order:* $\frac{a}{p^n}+\mathbb{Z}$ is killed by $p^n$, so its order divides $p^n$ — a $p$-power. The whole group is $p$-torsion.
>
> *Divisible:* given $x=\frac{a}{p^n}+\mathbb{Z}$ and $m\geq1$, write $m=p^s m'$ with $p\nmid m'$. Since $p\nmid m'$, $m'$ is invertible mod $p^{n+s}$, say $m'm''\equiv1$; then $y=\frac{a\,m''}{p^{n+s}}+\mathbb{Z}$ satisfies $my=\frac{p^s m' a m''}{p^{n+s}}+\mathbb{Z}=\frac{a m' m''}{p^n}+\mathbb{Z}=\frac{a}{p^n}+\mathbb{Z}=x$. So every element is divisible by every $m$ — the group is divisible. (Geometrically: dividing by $p$ just moves one level up the unbounded tower.)
>
> *Proper subgroups:* let $H\subsetneq\mathbb{Z}(p^\infty)$ be a proper subgroup. If $H$ contained an element of order $p^n$ for arbitrarily large $n$, it would contain every $\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}$ (each is cyclic, generated by any order-$p^n$ element) and hence all of $\mathbb{Z}(p^\infty)$. So the orders of elements of $H$ are bounded, say by $p^N$; then $H\subseteq\frac{1}{p^N}\mathbb{Z}/\mathbb{Z}$, and being a subgroup of a cyclic group it is $\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}\cong\mathbb{Z}/p^n\mathbb{Z}$ for some $n\leq N$. These are totally ordered by inclusion: $\frac{1}{p^a}\mathbb{Z}/\mathbb{Z}\subseteq\frac{1}{p^b}\mathbb{Z}/\mathbb{Z}\iff a\leq b$.

**Step 3: Contrast with $\mathbb{Z}_p$.**

$\varprojlim\mathbb{Z}/p^n\mathbb{Z}=\mathbb{Z}_p$ is built from the *same* objects with the *projections*, and is torsion-free, uncountable, not divisible — the opposite of $\mathbb{Z}(p^\infty)$.

> [!note]- Derivation
> The Prüfer group used the *inclusions* $\iota_n=(\times p)$ pointing up the tower and took the *direct* limit (union). The $p$-adic integers use the *projections* $h_n:\mathbb{Z}/p^{n+1}\to\mathbb{Z}/p^n$ pointing down and take the *inverse* limit (threads). By the duality of [[Def - Direct and Inverse Limits]], these are opposite constructions on the same objects, and the results could not be more different:
>
> | | $\mathbb{Z}(p^\infty)=\varinjlim\mathbb{Z}/p^n$ | $\mathbb{Z}_p=\varprojlim\mathbb{Z}/p^n$ |
> |---|---|---|
> | arrows | inclusions (up) | projections (down) |
> | limit | union (enlarge) | threads (refine) |
> | cardinality | countable | uncountable ($p^{\aleph_0}$ threads) |
> | torsion | all elements $p$-power torsion | torsion-free (only $0$ has finite order) |
> | divisible? | yes | no ($p\notin\mathbb{Z}_p^\times$) |
> | structure | divisible torsion group | compact local domain |
>
> The slogan: **direct limits enlarge, inverse limits refine.** The Prüfer group is the increasing union of the finite cyclic groups; $\mathbb{Z}_p$ is the completion that adds limiting threads. Same building blocks $\mathbb{Z}/p^n$, opposite arrows, dual limits.

> [!note]- Complete formal solution
> **(1)** Define $g_n:\mathbb{Z}/p^n\to\mathbb{Q}/\mathbb{Z}$, $a\mapsto\frac{a}{p^n}+\mathbb{Z}$, an injection with image $\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}$. Since $g_{n+1}(\iota_n(1))=\frac{p}{p^{n+1}}+\mathbb{Z}=\frac{1}{p^n}+\mathbb{Z}=g_n(1)$, the family is compatible, inducing $g:\varinjlim\mathbb{Z}/p^n\to\mathbb{Q}/\mathbb{Z}$. It is injective (an element killed by $g$ is already $0$ at its stage) with image $\bigcup_n\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}=\mathbb{Z}[1/p]/\mathbb{Z}$, so $\varinjlim\mathbb{Z}/p^n\cong\mathbb{Z}[1/p]/\mathbb{Z}=\mathbb{Z}(p^\infty)$.
>
> **(2)** It is a countable strictly-increasing union, hence countably infinite; every $\frac{a}{p^n}$ is killed by $p^n$, so all-torsion; divisible since $\frac{a}{p^n}$ can be divided by any $m=p^s m'$ by moving $s$ levels up and inverting $m'$ mod a high power of $p$. A proper subgroup has bounded element orders (else it is everything), so sits in some $\frac{1}{p^N}\mathbb{Z}/\mathbb{Z}$ and equals $\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}\cong\mathbb{Z}/p^n$; these are totally ordered by inclusion.
>
> **(3)** $\mathbb{Z}_p=\varprojlim\mathbb{Z}/p^n$ uses the projections (opposite arrows) and is the *inverse* limit: torsion-free, uncountable, non-divisible — the dual object built from the same $\mathbb{Z}/p^n$. $\blacksquare$

> [!warning] Illegal but tempting: reading the colimit off the naive identification $\mathbb{Z}/p^n=\{0,\dots,p^n-1\}$
> With the naive coordinates, $\iota_n=(\times p)$ sends $\mathbb{Z}/p^n$ *into the multiples of $p$* inside $\mathbb{Z}/p^{n+1}$, and it looks as though the system is "shrinking", making the union mysterious. The fix is the re-coordinatisation $\mathbb{Z}/p^n\cong\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}$, under which $\iota_n$ becomes the genuine inclusion of nested subgroups and the union is visibly $\mathbb{Z}[1/p]/\mathbb{Z}$. Forgetting to re-coordinatise — and trying to "glue residues" directly — is the standard source of confusion; the multiplication-by-$p$ maps are inclusions of *subgroups*, not of representatives.

---

# Key Takeaways

**When the transition maps of a direct system are injective, the colimit is the increasing union — but you must find the right ambient object to see it.** A direct limit of inclusions is conceptually a union, yet the system is given abstractly, with the stages not literally nested. The work is to produce a single object receiving compatible embeddings of all the stages; here, $\mathbb{Q}/\mathbb{Z}$ receives $\mathbb{Z}/p^n$ as $\frac{1}{p^n}\mathbb{Z}/\mathbb{Z}$, turning the multiplication-by-$p$ maps into honest inclusions. The trigger to recognise: injective transition maps up a tower mean "union", and the move is to re-coordinatise the stages as nested subobjects of a natural ambient. This is the same technique that realises $\overline{\mathbb{F}_p}=\varinjlim\mathbb{F}_{p^{n!}}$ as a union inside an algebraic closure, and germs $\varinjlim_{U\ni x}\mathcal{O}(U)$ as functions defined on shrinking neighbourhoods.

**Direct and inverse limits of the same objects are duals and can be wildly different — always read the arrows, never the objects.** The Prüfer group and the $p$-adic integers are built from the identical sequence $\mathbb{Z}/p^n\mathbb{Z}$; only the arrow direction differs (inclusions vs projections), and the results are opposite in every structural respect — countable divisible torsion vs uncountable torsion-free compact. This is the sharpest possible warning against the common error of inferring the limit from the objects. The transferable diagnostic: before computing any limit, identify the transition maps. Up-maps with $\varinjlim$ enlarge by union; down-maps with $\varprojlim$ refine by threading. The contrast here is the canonical illustration, and it is worth holding as the reference example for the [[Commutative Algebra X — Completions and Limits#Legal Operations|"don't confuse \varinjlim with \varprojlim"]] warning.

**Divisibility of the Prüfer group comes from the tower being unbounded — there is always one more level to divide into.** The reason every element of $\mathbb{Z}(p^\infty)$ is infinitely divisible is structural: dividing $\frac{a}{p^n}$ by $p$ lands in $\frac{a}{p^{n+1}}$, which is available because the levels never stop. This is the abstract content of "a direct limit absorbs all the stages", and it makes $\mathbb{Z}(p^\infty)$ the standard example of an injective $\mathbb{Z}$-module (divisible = injective over a PID) and the building block of the classification of injective abelian groups. The trigger: divisibility, or injectivity of a module, often comes from an unbounded direct system in which the "dividing" operation moves you one stage up. Compare the companion exercise [[Ex - The p-adic integers as an inverse limit]], where the *inverse* limit produces the opposite — a torsion-free ring in which $p$ is a non-unit, hence *not* divisible.
