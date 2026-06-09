---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Krull Dimension and Height"
  - "Ex - Dimension equals transcendence degree for a finitely generated domain"
  - "Thm - Noether Normalization"
  - "Thm - Integral Extensions Preserve Dimension"
  - "Def - Noetherian Ring"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $k$ be a field and $A$ a finitely generated $k$-algebra that is an integral domain. Prove that for every prime ideal $\mathfrak{p} \in \operatorname{Spec} A$,
$$\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p} = \dim A.$$

This is ES4 Q3(b). It is the **dimension formula** identifying height with codimension: $\operatorname{ht}\mathfrak{p} = \dim A - \dim A/\mathfrak{p}$, the dimension of the ambient space minus the dimension of the subvariety $V(\mathfrak{p})$. The route runs through the equality $\dim = \operatorname{trdeg}$ for finitely generated domains (Proposition 13.5; see [[Ex - Dimension equals transcendence degree for a finitely generated domain]]) together with the *catenary* fact (ES4 Q3a) that every non-refinable (saturated maximal) chain of primes in such an $A$ has length exactly $\dim A$. The formula is *false* for general Noetherian rings (ES4 Q4 exhibits $R = \mathbb{Z}_{(2)}[T]$ with $\dim A/\mathfrak{m} + \operatorname{ht}\mathfrak{m}$ taking two different values on two maximal ideals).

**Recall:**

The objects in play are height, the Krull dimension of a quotient, transcendence degree, and the catenary property.

![[Def - Krull Dimension and Height#Height of a prime, and of an ideal]]

The **dimension of the quotient** $\dim A/\mathfrak{p}$ measures the chains of primes *above* $\mathfrak{p}$: primes of $A/\mathfrak{p}$ correspond to primes of $A$ containing $\mathfrak{p}$, so $\dim A/\mathfrak{p}$ is the length of the longest chain $\mathfrak{p} = \mathfrak{q}_0 \subsetneq \mathfrak{q}_1 \subsetneq \cdots$ starting at $\mathfrak{p}$. Geometrically it is $\dim V(\mathfrak{p})$, the dimension of the subvariety cut out by $\mathfrak{p}$.

The **height** $\operatorname{ht}\mathfrak{p}$ measures chains *below* $\mathfrak{p}$. So $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p}$ is the length of a chain passing *through* $\mathfrak{p}$ — and the formula says this maximal through-$\mathfrak{p}$ chain has the full length $\dim A$.

The key bridge — *for finitely generated domains over a field*, $\dim A = \operatorname{trdeg}_k A$ (see [[Ex - Dimension equals transcendence degree for a finitely generated domain]]) and trdeg is additive: $\operatorname{trdeg}_k \operatorname{Frac}(A) = \operatorname{trdeg}_k \operatorname{Frac}(A/\mathfrak{p}) + (\text{the "codimension" trdeg drop across } \mathfrak{p})$.

---

# Convergent Strategy

**Problem class.** This is a *prove-an-additivity-identity* problem — show that two complementary measurements (chains below $\mathfrak{p}$, chains above $\mathfrak{p}$) sum to the global measurement (all chains). The natural-looking inequality $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p} \leq \dim A$ is almost free (concatenate a chain below $\mathfrak{p}$ with a chain above it). The content is the reverse inequality $\geq$, equivalently that *some* chain through $\mathfrak{p}$ achieves the full length $\dim A$ — which is the **catenary** property, the statement that all saturated maximal chains have the same length. This holds for finitely generated domains and *fails* in general, so the hypotheses are essential.

**Assumption pattern.** "$A$ finitely generated $k$-algebra domain" is the precise class on which the formula is true, and it is used through two consequences: (i) $\dim = \operatorname{trdeg}$ (Proposition 13.5, see the companion exercise), which converts dimensions into transcendence degrees that *add* in towers; (ii) Noether normalization and going-down, which guarantee that saturated chains are unrefinable to the full length — the catenary property. The recognisable trigger that the formula could *fail* is dropping either "finitely generated over a field" or "domain": ES4 Q4's ring $\mathbb{Z}_{(2)}[T]$ is a Noetherian domain but not a $k$-algebra, and there $\operatorname{ht}\mathfrak{m} + \dim A/\mathfrak{m}$ depends on $\mathfrak{m}$.

**Theorem routing.** The clean route uses transcendence degree. Set $A/\mathfrak{p}$, itself a finitely generated $k$-algebra domain, so $\dim A/\mathfrak{p} = \operatorname{trdeg}_k A/\mathfrak{p}$. The height $\operatorname{ht}\mathfrak{p}$ measures the drop in dimension from $A$ to $A/\mathfrak{p}$, and via $\dim = \operatorname{trdeg}$ this is the drop in transcendence degree, which by tower-additivity is $\operatorname{trdeg}_k A - \operatorname{trdeg}_k A/\mathfrak{p}$. So $\operatorname{ht}\mathfrak{p} = \dim A - \dim A/\mathfrak{p}$. The careful version goes through ES4 Q3(a): every non-refinable chain through $\mathfrak{p}$ has length $\dim A$, proved by induction on $\dim A$ using Noether normalization, going-down, and incomparability — the catenary engine. Either way the identity follows.

**Key decision point.** The non-obvious recognition is that the formula is *not* a tautology but a theorem about **catenary** rings, and that the missing ingredient is the reverse inequality. Concatenating a longest chain below $\mathfrak{p}$ with a longest chain above gives a chain through $\mathfrak{p}$ of length $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p}$, hence $\leq \dim A$ — but a priori the *longest* chain in $A$ might avoid $\mathfrak{p}$ entirely, or pass through $\mathfrak{p}$ sub-optimally on one side. The genuine insight is that for finitely generated domains *no chain is wasted*: every saturated chain reaches the full length, because transcendence degree drops by exactly one at each step of a saturated chain. Recognising that this "each step drops trdeg by one" (equivalently, catenarity) is the real theorem — and that it fails without the hypotheses — is the conceptual crux.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra XII — Dimension Theory#Legal Operations|the topic page's Legal Operations]]:

1. **Translate $\dim A/\mathfrak{p}$ into chains above $\mathfrak{p}$.** Primes of $A/\mathfrak{p}$ are primes of $A$ containing $\mathfrak{p}$; $\dim A/\mathfrak{p}$ is the longest chain starting at $\mathfrak{p}$.

2. **Concatenate chains through $\mathfrak{p}$ for the easy inequality.** A longest chain below $\mathfrak{p}$ joined to a longest chain above gives $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p} \leq \dim A$.

3. **Convert dimension to transcendence degree (Proposition 13.5).** For finitely generated domains, $\dim A = \operatorname{trdeg}_k A$, applied to both $A$ and $A/\mathfrak{p}$.

4. **Use tower-additivity of transcendence degree.** $\operatorname{trdeg}_k A = \operatorname{trdeg}_k A/\mathfrak{p} + (\text{drop})$, and the drop equals $\operatorname{ht}\mathfrak{p}$.

5. **Invoke catenarity for the reverse inequality (ES4 Q3a).** Every non-refinable chain through $\mathfrak{p}$ has length $\dim A$, via Noether normalization and going-down.

---

# Hints

> [!note]- Hint 1
> Interpret the three terms as chain-lengths. $\operatorname{ht}\mathfrak{p}$ = longest chain *below* $\mathfrak{p}$; $\dim A/\mathfrak{p}$ = longest chain *above* $\mathfrak{p}$ (primes of $A/\mathfrak{p}$ are primes of $A$ containing $\mathfrak{p}$); $\dim A$ = longest chain anywhere. Which inequality between $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p}$ and $\dim A$ is immediate?

> [!note]- Hint 2
> $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p} \leq \dim A$ is free: concatenate a longest chain below $\mathfrak{p}$ (length $\operatorname{ht}\mathfrak{p}$, ending at $\mathfrak{p}$) with a longest chain above $\mathfrak{p}$ (length $\dim A/\mathfrak{p}$, starting at $\mathfrak{p}$) to get a chain of length $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p}$ in $A$. The hard part is $\geq$: you must show *some* chain through $\mathfrak{p}$ reaches the full $\dim A$.

> [!note]- Hint 3
> Use $\dim = \operatorname{trdeg}$ (Proposition 13.5) for finitely generated domains, applied to $A$ and to $A/\mathfrak{p}$. Transcendence degree is additive in towers. The drop $\operatorname{trdeg}_k A - \operatorname{trdeg}_k A/\mathfrak{p}$ should equal $\operatorname{ht}\mathfrak{p}$ — this is where the "domain, finitely generated over a field" hypothesis does its work.

> [!note]- Hint 4
> The rigorous reverse inequality is ES4 Q3(a): in a finitely generated domain over a field, *every* non-refinable (saturated maximal) chain of primes has length exactly $\dim A$ — the **catenary** property. Proof by induction on $\dim A$ via Noether normalization, the going-down theorem, and incomparability. Granting catenarity, a saturated chain refining "(chain below $\mathfrak{p}$) + $\mathfrak{p}$ + (chain above $\mathfrak{p}$)" has length $\dim A$ and length $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p}$, forcing equality. Warning: the formula *fails* without the hypotheses — see ES4 Q4.

---

# Solution

The formula says that height and quotient-dimension are complementary: chains below $\mathfrak{p}$ plus chains above $\mathfrak{p}$ recover all of $\dim A$, with no length lost. One inequality is free by concatenation; the other is the catenary property, which holds for finitely generated domains because transcendence degree — equal to dimension here — drops by exactly one at each step of a saturated chain.

**Step 1: The easy inequality $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p} \leq \dim A$.**

Concatenating a longest chain below $\mathfrak{p}$ with a longest chain above $\mathfrak{p}$ produces a chain of length $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p}$ in $A$.

> [!note]- Derivation
> Let $\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_h = \mathfrak{p}$ be a chain below $\mathfrak{p}$ of length $h = \operatorname{ht}\mathfrak{p}$ (such a chain realizing the height exists because $A$ is Noetherian, so heights are finite). Primes of $A/\mathfrak{p}$ correspond to primes of $A$ containing $\mathfrak{p}$, so let $\mathfrak{p} = \mathfrak{q}_0 \subsetneq \cdots \subsetneq \mathfrak{q}_c$ be a chain above $\mathfrak{p}$ of length $c = \dim A/\mathfrak{p}$. Splicing at $\mathfrak{p}$,
> $$\mathfrak{p}_0 \subsetneq \cdots \subsetneq \mathfrak{p}_h = \mathfrak{p} = \mathfrak{q}_0 \subsetneq \cdots \subsetneq \mathfrak{q}_c$$
> is a strictly increasing chain of primes of $A$ of length $h + c = \operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p}$. By the definition of [[Def - Krull Dimension and Height|Krull dimension]] as the supremum of chain lengths,
> $$\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p} \leq \dim A.$$

**Step 2: Reduce the reverse inequality to transcendence degree.**

Both $A$ and $A/\mathfrak{p}$ are finitely generated domains, so their dimensions are transcendence degrees, and the height is the transcendence-degree drop.

> [!note]- Derivation
> $A/\mathfrak{p}$ is a finitely generated $k$-algebra (quotient of one) and an integral domain (as $\mathfrak{p}$ is prime), so by Proposition 13.5 (see [[Ex - Dimension equals transcendence degree for a finitely generated domain]]),
> $$\dim A = \operatorname{trdeg}_k A, \qquad \dim A/\mathfrak{p} = \operatorname{trdeg}_k A/\mathfrak{p}.$$
> The reverse inequality $\operatorname{ht}\mathfrak{p} \geq \dim A - \dim A/\mathfrak{p} = \operatorname{trdeg}_k A - \operatorname{trdeg}_k A/\mathfrak{p}$ is now a statement about how much transcendence degree drops when we pass to the quotient by $\mathfrak{p}$. Intuitively, $\operatorname{Frac}(A/\mathfrak{p})$ is obtained from $\operatorname{Frac}(A)$ by imposing the $\operatorname{ht}\mathfrak{p}$ "independent conditions" that define $V(\mathfrak{p})$, each cutting transcendence degree by one — so $\operatorname{trdeg}_k A - \operatorname{trdeg}_k A/\mathfrak{p} = \operatorname{ht}\mathfrak{p}$. Making "each condition cuts trdeg by one" rigorous is the catenary property, Step 3.

**Step 3: Catenarity (ES4 Q3a) gives the reverse inequality.**

Every non-refinable chain through $\mathfrak{p}$ has length exactly $\dim A$, so the through-$\mathfrak{p}$ chain of Step 1 can be taken to have full length.

> [!note]- Derivation
> **ES4 Q3(a):** in a finitely generated $k$-algebra domain $A$, every *non-refinable* chain of primes $\mathfrak{p}_r \supsetneq \cdots \supsetneq \mathfrak{p}_0$ (where $\mathfrak{p}_r$ is maximal, $\mathfrak{p}_0$ is minimal $= (0)$, and no prime fits strictly between consecutive terms) has length $r = \dim A$. This is the **catenary** property; it is proved by induction on $\dim A$ using [[Thm - Noether Normalization|Noether normalization]], the **going-down theorem**, **incomparability**, and $\dim = \operatorname{trdeg}$ — the geometric content being that a saturated chain drops transcendence degree by exactly one at each step, so a saturated chain of length $r$ from $(0)$ to a maximal ideal has $r = \operatorname{trdeg}_k A = \dim A$.
>
> Apply it. Take the spliced chain from Step 1 and refine it to a non-refinable chain $\mathfrak{P}_0 \subsetneq \cdots \subsetneq \mathfrak{P}_N$ passing through $\mathfrak{p}$, with $\mathfrak{p} = \mathfrak{P}_h$ at position $h$. Refining cannot shorten, so the sub-chain below $\mathfrak{p}$ has length $\geq \operatorname{ht}\mathfrak{p}$, and is saturated, so it realizes a saturated chain below $\mathfrak{p}$; likewise above. By catenarity the whole chain has length $N = \dim A$, and it splits at $\mathfrak{p} = \mathfrak{P}_h$ into a saturated chain below (length $h$) and above (length $N - h$). Saturated chains below $\mathfrak{p}$ all have length $\operatorname{ht}\mathfrak{p}$ (catenarity applied to the domain $A_\mathfrak{p}$, equivalently to chains in $A$ below $\mathfrak{p}$), so $h = \operatorname{ht}\mathfrak{p}$; saturated chains above $\mathfrak{p}$ all have length $\dim A/\mathfrak{p}$, so $N - h = \dim A/\mathfrak{p}$. Therefore
> $$\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p} = h + (N - h) = N = \dim A.$$

**Step 4: Conclude the formula.**

Steps 1 and 3 give the two inequalities, hence equality.

> [!note]- Derivation
> Step 1 gives $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p} \leq \dim A$; Step 3 gives $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p} = \dim A$ outright (so in particular $\geq$). Hence
> $$\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p} = \dim A, \qquad \text{i.e.} \qquad \operatorname{ht}\mathfrak{p} = \dim A - \dim A/\mathfrak{p}. \qquad \blacksquare$$
> Height is codimension: the dimension of the ambient $\operatorname{Spec} A$ minus the dimension of the subvariety $V(\mathfrak{p})$.

> [!note]- Complete formal solution
> **Claim.** For $A$ a finitely generated $k$-algebra domain and $\mathfrak{p} \in \operatorname{Spec} A$: $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p} = \dim A$.
>
> *($\leq$)* Splice a length-$\operatorname{ht}\mathfrak{p}$ chain below $\mathfrak{p}$ to a length-$\dim A/\mathfrak{p}$ chain above $\mathfrak{p}$ (these correspond to chains in $A/\mathfrak{p}$); this is a chain in $A$ of length $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p}$, so $\leq \dim A$.
>
> *($=$)* By ES4 Q3(a), every non-refinable chain of primes in the finitely generated domain $A$ has length $\dim A$ (catenarity, via Noether normalization, going-down, incomparability, and $\dim = \operatorname{trdeg}$). Refine the spliced chain to a saturated chain through $\mathfrak{p}$; it has length $\dim A$ and splits at $\mathfrak{p}$ into a saturated chain below (length $\operatorname{ht}\mathfrak{p}$) and above (length $\dim A/\mathfrak{p}$). Hence $\operatorname{ht}\mathfrak{p} + \dim A/\mathfrak{p} = \dim A$. $\blacksquare$
>
> *Remark (failure in general, ES4 Q4).* For $R = \mathbb{Z}_{(2)}[T]$ (a Noetherian domain, not a $k$-algebra), the maximal ideals $\mathfrak{m}_1 = (2T - 1)$ and $\mathfrak{m}_2 = (T, 2)$ satisfy $\operatorname{ht}\mathfrak{m}_1 + \dim R/\mathfrak{m}_1 = 1$ but $\operatorname{ht}\mathfrak{m}_2 + \dim R/\mathfrak{m}_2 = 2$ — the through-prime chain lengths differ, so $R$ is *not* catenary in the strong sense the formula requires, and the dimension formula fails.

---

# Key Takeaways

**Height is codimension, and the dimension formula is what makes that literally true.** The identity $\operatorname{ht}\mathfrak{p} = \dim A - \dim A/\mathfrak{p}$ is the precise statement that the **height of a prime equals the codimension of the subvariety it cuts out**: ambient dimension minus subvariety dimension. Without this formula, "height" and "codimension" are merely analogous; with it, they are equal numbers. This is the result that lets a geometer pass freely between the algebraic invariant (longest chain of primes below $\mathfrak{p}$) and the geometric one (how many independent equations to cut $V(\mathfrak{p})$ out of $\operatorname{Spec} A$). It underwrites all of intersection theory: when subvarieties meet, their *codimensions add* in the generic case, and that statement is the dimension formula applied iteratively. The lesson for spaced practice: whenever you see "height," translate it to "codimension," and remember that the translation is licensed by *this theorem* and only for the well-behaved (finitely-generated-over-a-field) rings.

**The easy inequality is concatenation; the content is catenarity — every saturated chain reaches full length.** The structural lesson is to *separate the two inequalities and locate the content*. The $\leq$ direction is a pure concatenation: stack a longest chain below $\mathfrak{p}$ onto a longest chain above, and you cannot exceed the global longest chain. This is free and would hold in any ring. The $\geq$ direction — equivalently, that some through-$\mathfrak{p}$ chain achieves the *full* $\dim A$ — is the **catenary** property, and it is a genuine theorem that *fails* in general Noetherian rings. The geometric reason it holds for finitely generated domains is that transcendence degree drops by exactly one at each step of a saturated chain (each step imposes one independent condition), so saturated chains cannot be short. Internalizing "the $\leq$ is bookkeeping, the $\geq$ is catenarity, and catenarity is 'no chain is wasted'" is the right mental model, and it generalizes: every additivity-of-dimension identity has a free inequality and a hard catenary-type reverse.

**The hypotheses are load-bearing: the formula is a theorem about finitely generated $k$-algebra domains, not about Noetherian rings.** It is essential to remember *where the formula fails*, because the failure is instructive. ES4 Q4's ring $\mathbb{Z}_{(2)}[T]$ is a perfectly nice Noetherian domain, yet $\operatorname{ht}\mathfrak{m} + \dim R/\mathfrak{m}$ takes the value $1$ at one maximal ideal and $2$ at another — so there is no single "$\dim R$" that the through-prime lengths all reach. The obstruction is the mixing of two "directions" of different lengths: the arithmetic direction (from $\mathbb{Z}_{(2)}$) and the geometric direction (the variable $T$), which do not have a uniform transcendence-degree bookkeeping over a common base field. This is the same family of pathologies as Nagata's infinite-dimensional ring (see [[Ex - A Noetherian ring of infinite dimension]]): both arise from leaving the category of finite-type $k$-algebras. The takeaway is a discipline of hypothesis-tracking — "$\dim = \operatorname{trdeg}$" and "catenary" are privileges of finitely-generated-over-a-field, and reaching for the dimension formula in a general Noetherian ring is a classic trap.

**This is the catenary backbone of well-defined codimension throughout algebraic geometry.** The formula is the algebraic expression of the fact that, on a **bold plain text — variety**, codimension is well-defined: every maximal chain of irreducible subvarieties between two given ones has the same length, so "the codimension of $Y$ in $X$" is an honest number independent of how you compute it. This **catenary** property — built here from $\dim = \operatorname{trdeg}$ and the going-down theorem — is what lets the whole apparatus of **bold plain text — Weil divisors, codimension-one cycles, and the dimension formula for fibres of a morphism** function. For a dominant morphism $f : X \to Y$ of varieties, the fibre dimension is $\dim X - \dim Y$ generically, and that is the dimension formula applied along the map; the catenary property guarantees the codimensions behave additively as you stratify. So this modest-looking identity is the foundation on which "codimension" becomes a usable, additive invariant — the geometric payoff that makes height worth defining via chains in the first place.
