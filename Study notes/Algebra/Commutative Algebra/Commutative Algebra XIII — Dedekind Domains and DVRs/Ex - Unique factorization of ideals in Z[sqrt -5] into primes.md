---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Dedekind Domain"
  - "Thm - A Dedekind Domain has Unique Factorization of Ideals"
  - "Thm - The Ring of Integers of a Number Field is Dedekind"
  - "Def - Prime and Maximal Ideal"
tags: [algebra, commutative-algebra]
---

# Problem Statement

In the ring $A = \mathbb{Z}[\sqrt{-5}]$, the element $6$ factors two different ways into irreducibles:
$$6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5}).$$
So $A$ is **not** a unique factorization domain. Nevertheless $A = \mathcal{O}_{\mathbb{Q}(\sqrt{-5})}$ is a [[Def - Dedekind Domain|Dedekind domain]], so its *ideals* factor uniquely. Prove this concretely:

1. Show $\mathfrak{p} = (2, 1+\sqrt{-5})$, $\mathfrak{q} = (3, 1+\sqrt{-5})$, $\bar{\mathfrak{q}} = (3, 1-\sqrt{-5})$ are prime ideals, with $(2) = \mathfrak{p}^2$, $(3) = \mathfrak{q}\bar{\mathfrak{q}}$, $(1+\sqrt{-5}) = \mathfrak{p}\mathfrak{q}$, $(1-\sqrt{-5}) = \mathfrak{p}\bar{\mathfrak{q}}$.
2. Deduce that both factorizations of $6$ give the **same** ideal factorization $(6) = \mathfrak{p}^2\mathfrak{q}\bar{\mathfrak{q}}$, regrouped two ways.

Use the norm $N(a + b\sqrt{-5}) = a^2 + 5b^2$, which is multiplicative.

**Recall:**

By [[Thm - The Ring of Integers of a Number Field is Dedekind|the integers-are-Dedekind theorem]], $A = \mathbb{Z}[\sqrt{-5}]$ is a Dedekind domain. By [[Thm - A Dedekind Domain has Unique Factorization of Ideals|unique factorization of ideals]], every nonzero ideal is uniquely a product of prime ideals.

The **norm** $N(\alpha) = \alpha\bar\alpha = a^2 + 5b^2$ for $\alpha = a + b\sqrt{-5}$ is multiplicative ($N(\alpha\beta) = N(\alpha)N(\beta)$), takes values in $\mathbb{Z}_{\geq 0}$, and $N(\alpha) = 1 \iff \alpha \in A^\times = \{\pm 1\}$. For an ideal $\mathfrak{a}$, the **ideal norm** $N(\mathfrak{a}) = |A/\mathfrak{a}|$ is also multiplicative, and $N((\alpha)) = |N(\alpha)|$.

---

# Convergent Strategy

**Problem class.** This is the *canonical worked example* of the chapter: a hands-on factorization of ideals in a non-UFD Dedekind domain, exhibiting how ideal factorization repairs the failure of element factorization. As the [[Commutative Algebra XIII — Dedekind Domains and DVRs#Insights|topic insights]] stress, the resolution of the $6 = 2\cdot3 = (1+\sqrt{-5})(1-\sqrt{-5})$ ambiguity *is* the regrouping of one prime-ideal factorization.

**Assumption pattern.** The driving tool is the **norm**, which is multiplicative on both elements and ideals. The recognizable pattern: to identify the prime ideals above a rational prime $p$, look at $A/pA = \mathbb{F}_p[x]/(x^2 + 5)$ and factor $x^2 + 5$ mod $p$ — the factorization of the polynomial gives the factorization of $(p)$. The norm certifies that the candidate ideals have the right size ($N(\mathfrak{p}) = p^f$) and that they are non-principal (no element has the matching norm).

**Theorem routing.** The route is: (i) compute $A/2A$ and $A/3A$ to see how $x^2 + 5$ factors mod $2$ and mod $3$, reading off $(2) = \mathfrak{p}^2$ (ramified, $x^2 + 5 \equiv (x+1)^2$) and $(3) = \mathfrak{q}\bar{\mathfrak{q}}$ (split, $x^2 + 5 \equiv (x+1)(x-1)$); (ii) verify the prime ideals via $A/\mathfrak{p} \cong \mathbb{F}_2$, $A/\mathfrak{q} \cong \mathbb{F}_3$ (quotients are fields, so the ideals are maximal); (iii) factor $(1\pm\sqrt{-5})$ by computing norms and matching; (iv) assemble $(6) = \mathfrak{p}^2\mathfrak{q}\bar{\mathfrak{q}}$ and check both element-factorizations regroup to it. [[Thm - A Dedekind Domain has Unique Factorization of Ideals|Unique factorization]] guarantees the answer is consistent.

**Key decision point.** The non-obvious move is to **factor the polynomial $x^2 + 5$ modulo $p$ to find the primes** (Dedekind's criterion): the prime ideals above $p$ correspond to the irreducible factors of $\min_\alpha(x) \bmod p$, with multiplicities giving ramification. The other key move is using the **norm to prove non-principality**: $\mathfrak{p}$ would be principal $(\alpha)$ only if $N(\alpha) = N(\mathfrak{p}) = 2$, but $a^2 + 5b^2 = 2$ has no integer solution — so $\mathfrak{p}$ is a genuine non-principal prime, which is *why* unique factorization of elements failed.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra XIII — Dedekind Domains and DVRs#Legal Operations|the topic page's Legal Operations]]:

1. **Certify Dedekind by the three axioms (operation 8) — done upstream.** $A = \mathcal{O}_{\mathbb{Q}(\sqrt{-5})}$ is Dedekind by [[Thm - The Ring of Integers of a Number Field is Dedekind]], so factorization applies.

2. **Trade primary decomposition for a product via coprimality (operation 4).** $(2) = \mathfrak{p}^2$ and $(3) = \mathfrak{q}\bar{\mathfrak{q}}$ are the local factorizations; coprimality of distinct primes gives $(6) = \mathfrak{p}^2\mathfrak{q}\bar{\mathfrak{q}}$.

3. **Use a norm to obstruct principality (insights trigger).** $\mathfrak{p}$ has ideal norm $2$, but no element has norm $2$, so $\mathfrak{p}$ is non-principal.

---

# Hints

> [!note]- Hint 1
> Since $A$ is Dedekind, the ideals factor uniquely. To find the primes above a rational prime $p$, look at $A/pA \cong \mathbb{F}_p[x]/(x^2 + 5)$ (using $A = \mathbb{Z}[x]/(x^2+5)$). How does $x^2 + 5$ factor mod $2$ and mod $3$?

> [!note]- Hint 2
> Mod $2$: $x^2 + 5 \equiv x^2 + 1 \equiv (x+1)^2$, a *repeated* factor — so $2$ ramifies, $(2) = \mathfrak{p}^2$ with $\mathfrak{p} = (2, \sqrt{-5}+1)$. Mod $3$: $x^2 + 5 \equiv x^2 + 2 \equiv x^2 - 1 \equiv (x-1)(x+1)$, two *distinct* factors — so $3$ splits, $(3) = \mathfrak{q}\bar{\mathfrak{q}}$.

> [!note]- Hint 3
> Verify $\mathfrak{p}$ is prime by computing $A/\mathfrak{p}$. Modulo $\mathfrak{p}$, $2 = 0$ and $\sqrt{-5} = -1$, so $A/\mathfrak{p} \cong \mathbb{F}_2$, a field — so $\mathfrak{p}$ is maximal, hence prime. Similarly $A/\mathfrak{q} \cong \mathbb{F}_3$.

> [!note]- Hint 4
> To factor $(1 + \sqrt{-5})$: its norm is $N(1+\sqrt{-5}) = 1 + 5 = 6 = 2\cdot 3$, so $(1+\sqrt{-5})$ has ideal norm $6 = N(\mathfrak{p})N(\mathfrak{q})$ and must be $\mathfrak{p}\mathfrak{q}$ (it contains both $\mathfrak{p}$ and $\mathfrak{q}$ since $1 + \sqrt{-5} \in \mathfrak{p} \cap \mathfrak{q}$). Then $(6) = (2)(3) = \mathfrak{p}^2\mathfrak{q}\bar{\mathfrak{q}}$, and also $(6) = (1+\sqrt{-5})(1-\sqrt{-5}) = (\mathfrak{p}\mathfrak{q})(\mathfrak{p}\bar{\mathfrak{q}}) = \mathfrak{p}^2\mathfrak{q}\bar{\mathfrak{q}}$ — the same.

---

# Solution

The proof factors $(2)$ and $(3)$ by reducing $x^2 + 5$ modulo each prime, verifies the resulting ideals are prime via their quotient fields, factors $(1\pm\sqrt{-5})$ by norms, and assembles $(6)$ both ways to the same prime-ideal product. The norm proves the primes are non-principal, which is exactly why element factorization failed.

**Step 1: factor $(2)$ and $(3)$ via reduction of $x^2 + 5$.**

$(2) = \mathfrak{p}^2$ with $\mathfrak{p} = (2, 1+\sqrt{-5})$ (ramified), and $(3) = \mathfrak{q}\bar{\mathfrak{q}}$ with $\mathfrak{q} = (3, 1+\sqrt{-5})$, $\bar{\mathfrak{q}} = (3, 1-\sqrt{-5})$ (split).

> [!note]- Derivation
> Write $A = \mathbb{Z}[\sqrt{-5}] = \mathbb{Z}[x]/(x^2 + 5)$, identifying $\sqrt{-5}$ with $x$. Then for a rational prime $p$,
> $$A/pA \cong \mathbb{F}_p[x]/(x^2 + 5),$$
> and the prime ideals of $A$ containing $p$ correspond to the irreducible factors of $x^2 + 5 \bmod p$, with the ramification exponent equal to the multiplicity.
>
> **At $p = 2$:** $x^2 + 5 \equiv x^2 + 1 = (x + 1)^2 \pmod 2$. The repeated factor $(x+1)$ gives the single prime $\mathfrak{p} = (2,\, x + 1) = (2,\, 1 + \sqrt{-5})$ with exponent $2$:
> $$(2) = \mathfrak{p}^2.$$
> **At $p = 3$:** $x^2 + 5 \equiv x^2 + 2 \equiv x^2 - 1 = (x-1)(x+1) \pmod 3$. Two distinct factors give two distinct primes $\mathfrak{q} = (3,\, x + 1) = (3, 1+\sqrt{-5})$ and $\bar{\mathfrak{q}} = (3,\, x - 1) = (3, 1 - \sqrt{-5})$ (using $-1 \equiv x - 1$ adjusted; explicitly $x - 1$ and $x + 1$):
> $$(3) = \mathfrak{q}\bar{\mathfrak{q}}.$$

**Step 2: verify $\mathfrak{p}, \mathfrak{q}, \bar{\mathfrak{q}}$ are prime.**

Each quotient $A/\mathfrak{p}$, $A/\mathfrak{q}$, $A/\bar{\mathfrak{q}}$ is a field, so each ideal is maximal, hence prime.

> [!note]- Derivation
> **$\mathfrak{p}$:** In $A/\mathfrak{p}$, the relations $2 = 0$ and $1 + \sqrt{-5} = 0$ hold, so $\sqrt{-5} \equiv -1$ and every element reduces to $a + b\sqrt{-5} \equiv a - b \pmod 2 \in \{0, 1\}$. Thus $A/\mathfrak{p} \cong \mathbb{F}_2$, a field, so $\mathfrak{p}$ is maximal (hence prime). Its ideal norm is $N(\mathfrak{p}) = |A/\mathfrak{p}| = 2$.
>
> **$\mathfrak{q}$:** In $A/\mathfrak{q}$, $3 = 0$ and $\sqrt{-5} \equiv -1$, so elements reduce to $a - b \pmod 3 \in \mathbb{F}_3$. Thus $A/\mathfrak{q} \cong \mathbb{F}_3$, a field, $\mathfrak{q}$ maximal, $N(\mathfrak{q}) = 3$. Similarly $A/\bar{\mathfrak{q}} \cong \mathbb{F}_3$ with $\sqrt{-5} \equiv +1$, so $\bar{\mathfrak{q}}$ is maximal with $N(\bar{\mathfrak{q}}) = 3$.
>
> **Consistency of norms:** $N((2)) = |N(2)| = 4 = N(\mathfrak{p})^2$ ✓ (matching $(2) = \mathfrak{p}^2$); $N((3)) = 9 = N(\mathfrak{q})N(\bar{\mathfrak{q}}) = 3\cdot 3$ ✓.
>
> **Non-principality of $\mathfrak{p}$:** if $\mathfrak{p} = (\alpha)$ then $N(\alpha) = N(\mathfrak{p}) = 2$, i.e. $a^2 + 5b^2 = 2$, which has *no* integer solution ($b = 0$ gives $a^2 = 2$, $|b| \geq 1$ gives $\geq 5$). So $\mathfrak{p}$ is a non-principal prime — the structural reason element factorization fails.

**Step 3: factor $(1 \pm \sqrt{-5})$.**

$(1 + \sqrt{-5}) = \mathfrak{p}\mathfrak{q}$ and $(1 - \sqrt{-5}) = \mathfrak{p}\bar{\mathfrak{q}}$.

> [!note]- Derivation
> Compute $N(1 + \sqrt{-5}) = 1^2 + 5\cdot 1^2 = 6$, so the ideal $(1+\sqrt{-5})$ has ideal norm $6 = 2\cdot 3 = N(\mathfrak{p})N(\mathfrak{q})$. Now $1 + \sqrt{-5} \in \mathfrak{p}$ (it is a generator) and $1 + \sqrt{-5} \in \mathfrak{q}$ (also a generator), so $\mathfrak{p} \mid (1+\sqrt{-5})$ and $\mathfrak{q} \mid (1+\sqrt{-5})$ ("to contain is to divide"). Since $\mathfrak{p}, \mathfrak{q}$ are distinct primes and the total norm is exactly $N(\mathfrak{p})N(\mathfrak{q})$, the factorization is
> $$(1 + \sqrt{-5}) = \mathfrak{p}\mathfrak{q}.$$
> Applying complex conjugation (the nontrivial automorphism $\sqrt{-5}\mapsto-\sqrt{-5}$, which swaps $\mathfrak{q} \leftrightarrow \bar{\mathfrak{q}}$ and fixes $\mathfrak{p}$):
> $$(1 - \sqrt{-5}) = \mathfrak{p}\bar{\mathfrak{q}}.$$

**Step 4: both factorizations of $6$ regroup to $(6) = \mathfrak{p}^2\mathfrak{q}\bar{\mathfrak{q}}$.**

The two element-factorizations of $6$ produce the *same* ideal factorization, grouped differently.

> [!note]- Derivation
> From the first element-factorization:
> $$(6) = (2)(3) = \mathfrak{p}^2 \cdot \mathfrak{q}\bar{\mathfrak{q}} = \mathfrak{p}^2\mathfrak{q}\bar{\mathfrak{q}}.$$
> From the second:
> $$(6) = (1+\sqrt{-5})(1-\sqrt{-5}) = (\mathfrak{p}\mathfrak{q})(\mathfrak{p}\bar{\mathfrak{q}}) = \mathfrak{p}^2\mathfrak{q}\bar{\mathfrak{q}}.$$
> Both equal $\mathfrak{p}^2\mathfrak{q}\bar{\mathfrak{q}}$. So at the level of ideals there is *one* factorization of $(6)$; the apparent ambiguity in factoring the *element* $6$ is just two ways of grouping the four prime-ideal factors $\mathfrak{p}, \mathfrak{p}, \mathfrak{q}, \bar{\mathfrak{q}}$ into pairs that happen to be principal. The factorization $2 = \mathfrak{p}\cdot\mathfrak{p}$, $3 = \mathfrak{q}\cdot\bar{\mathfrak{q}}$ pairs $\{\mathfrak{p},\mathfrak{p}\}$ and $\{\mathfrak{q},\bar{\mathfrak{q}}\}$; the factorization $1\pm\sqrt{-5} = \mathfrak{p}\mathfrak{q}, \mathfrak{p}\bar{\mathfrak{q}}$ pairs $\{\mathfrak{p},\mathfrak{q}\}$ and $\{\mathfrak{p},\bar{\mathfrak{q}}\}$. Unique factorization of ideals holds; unique factorization of elements fails because $\mathfrak{p}, \mathfrak{q}$ are non-principal.

> [!note]- Complete formal solution
> $A = \mathbb{Z}[\sqrt{-5}] = \mathbb{Z}[x]/(x^2+5)$ is Dedekind. Reducing $x^2 + 5$: mod $2$, $x^2+5 \equiv (x+1)^2$, so $(2) = \mathfrak{p}^2$ with $\mathfrak{p} = (2, 1+\sqrt{-5})$; mod $3$, $x^2 + 5 \equiv (x-1)(x+1)$, so $(3) = \mathfrak{q}\bar{\mathfrak{q}}$ with $\mathfrak{q} = (3, 1+\sqrt{-5})$, $\bar{\mathfrak{q}} = (3, 1-\sqrt{-5})$.
>
> Each is prime: $A/\mathfrak{p} \cong \mathbb{F}_2$, $A/\mathfrak{q} \cong A/\bar{\mathfrak{q}} \cong \mathbb{F}_3$ are fields. Norms: $N(\mathfrak{p}) = 2$, $N(\mathfrak{q}) = N(\bar{\mathfrak{q}}) = 3$. $\mathfrak{p}$ is non-principal since $a^2 + 5b^2 = 2$ is unsolvable.
>
> Since $N(1+\sqrt{-5}) = 6$ and $1 + \sqrt{-5} \in \mathfrak{p}\cap\mathfrak{q}$, we get $(1+\sqrt{-5}) = \mathfrak{p}\mathfrak{q}$; conjugating, $(1-\sqrt{-5}) = \mathfrak{p}\bar{\mathfrak{q}}$.
>
> Therefore $(6) = (2)(3) = \mathfrak{p}^2\mathfrak{q}\bar{\mathfrak{q}}$ and $(6) = (1+\sqrt{-5})(1-\sqrt{-5}) = \mathfrak{p}^2\mathfrak{q}\bar{\mathfrak{q}}$: the two element-factorizations are the same ideal factorization, regrouped. $\blacksquare$

---

# Key Takeaways

**To factor $(p)$ in a ring of integers, factor the defining polynomial modulo $p$ — Dedekind's criterion.** The whole computation runs on the isomorphism $A/pA \cong \mathbb{F}_p[x]/(\bar f)$ for $A = \mathbb{Z}[x]/(f)$: the prime ideals above $p$ are read off the irreducible factors of $f \bmod p$, and the multiplicity of each factor is the ramification index. Mod $2$ the polynomial $x^2 + 5$ has a *repeated* root, so $2$ ramifies ($(2) = \mathfrak{p}^2$); mod $3$ it has *two distinct* roots, so $3$ splits ($(3) = \mathfrak{q}\bar{\mathfrak{q}}$); a prime where $f$ stays irreducible would be *inert*. The trigger: whenever you must factor an ideal $(p)$ in $\mathbb{Z}[\alpha]$, reduce the minimal polynomial of $\alpha$ mod $p$ and factor it — this converts a hard ideal computation into a one-variable polynomial factorization over a finite field.

**The norm is the universal obstruction to principality, and non-principal primes are exactly why element factorization fails.** The ideal $\mathfrak{p}$ has ideal norm $2$, but no *element* has norm $2$ (the form $a^2 + 5b^2$ skips the value $2$), so $\mathfrak{p}$ cannot be principal. This single fact — a non-principal prime exists — is the root cause of $6$'s two factorizations: the prime ideals $\mathfrak{p}, \mathfrak{q}$ are honest and factor $6$ uniquely, but because they are non-principal you cannot see them as elements, and the only *elements* available ($2, 3, 1\pm\sqrt{-5}$) are products of two non-principal primes that happen to be principal, groupable two ways. The transferable diagnostic: to show an ideal is non-principal, compute its norm and check whether any element attains that norm; the gap between achievable ideal-norms and achievable element-norms is precisely the class group.

**Ideal factorization regroups the same primes; element factorization is the shadow that loses the grouping.** The deepest lesson is conceptual: there is *one* factorization $(6) = \mathfrak{p}^2\mathfrak{q}\bar{\mathfrak{q}}$, and the two element-factorizations are two ways of partitioning the multiset $\{\mathfrak{p}, \mathfrak{p}, \mathfrak{q}, \bar{\mathfrak{q}}\}$ into principal sub-products. This is *why* Kummer's "ideal numbers" work: passing to ideals refines the factorization to its atoms (the primes), and the non-uniqueness at the element level is just the failure of those atoms to be individually principal. When you see a non-UFD ring of integers, expect this pattern — the element-level ambiguity always resolves into a unique prime-ideal factorization once you refine, and the obstruction to descending back to elements is measured by the [[Ex - The class group measures failure of unique factorization|class group]], which for $\mathbb{Z}[\sqrt{-5}]$ is $\mathbb{Z}/2$ generated by $[\mathfrak{p}]$.
