---
type: definition
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Unit and Field"
  - "Def - Integral Domain"
  - "Def - Irreducible and Prime Elements"
  - "Def - Unique Factorization Domain"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $R$ is an [[Def - Integral Domain|integral domain]]. We write $a \mid b$ for "$a$ [[Def - Irreducible and Prime Elements|divides]] $b$" (that is, $b = ac$ for some $c \in R$), and call $a$ and $b$ **associates** if each divides the other, equivalently $a = bc$ for a [[Def - Unit and Field|unit]] $c$. Elements $a_1, \dots, a_n \in R$ are the inputs; $d$ denotes a greatest common divisor and $m$ a least common multiple. The notation $\gcd(a_1, \dots, a_n)$ and $\operatorname{lcm}(a_1, \dots, a_n)$ stands for *any* representative of the (associate-class of the) gcd or lcm, since these are defined only up to associates. The chapter symbol registry is on [[Rings II — §2.3–2.4]].

---

# Axiom Motivation

In $\mathbb{Z}$ the greatest common divisor of $a$ and $b$ is "the largest integer dividing both", and the least common multiple is "the smallest positive integer that both divide". The words *largest* and *smallest* refer to the ordering of $\mathbb{Z}$ by size. But a general [[Def - Integral Domain|integral domain]] has no notion of size — there is no "largest" element of a [[Def - Ring|ring]]. So if we want gcd and lcm in an arbitrary domain, the very first task is to *re-found the definition on something other than magnitude*. The motivating realisation is that, even in $\mathbb{Z}$, "largest common divisor" is the wrong primitive; the right primitive is **divisibility**, and the gcd is characterised not by being numerically biggest but by being the *divisibility-greatest* common divisor.

Look at what the gcd does in $\mathbb{Z}$. Yes, $\gcd(12, 18) = 6$ is the numerically largest common divisor. But it has a stronger, purely divisibility-theoretic property: *every* common divisor of $12$ and $18$ — namely $1, 2, 3, 6$ and their negatives — divides $6$. The common divisors are not just $\le 6$ in size; they all *divide* $6$. This is the property to abstract, because it never mentions size. So we define: $d$ is a **greatest common divisor** of $a_1, \dots, a_n$ if

1. $d$ is a *common divisor* — $d \mid a_i$ for every $i$; and
2. $d$ is *greatest among them in the divisibility order* — every common divisor $d'$ (any $d'$ with $d' \mid a_i$ for all $i$) satisfies $d' \mid d$.

Clause 1 says $d$ is in the running; clause 2 says $d$ is at the *top* of the divisibility partial order restricted to common divisors. The word "greatest" has been silently re-interpreted: not greatest in magnitude, but greatest in the relation $\mid$. In the language of order theory, a gcd is a **greatest lower bound** (an infimum) of $a_1, \dots, a_n$ in the poset of $R$ ordered by divisibility.

Why is clause 2 phrased as "$d' \mid d$" and not "$d' \le d$" or "$d'$ is one of finitely many specified things"? Because $\mid$ is the only structure available, and because this phrasing makes the gcd *automatically as canonical as it can be*. Run the definition and ask: how unique is $d$? If $d$ and $d'$ are *both* greatest common divisors, then clause 2 applied to each gives $d' \mid d$ and $d \mid d'$ — so $d$ and $d'$ are mutual divisors, i.e. **associates**. They differ only by a unit. The definition does *not* pin down a single element, and it *cannot* — there is no canonical choice between $6$ and $-6$ in $\mathbb{Z}$, both are gcds of $12$ and $18$. This is not a defect; it is the honest situation, and the universal-property phrasing of clause 2 is exactly what makes "unique up to associates" fall out for free. (In $\mathbb{Z}$ one then conventionally picks the positive representative; in $F[X]$ one picks the monic one. The convention is a human choice on top of a definition that only ever determines an associate-class.)

The **least common multiple** is the exact order-theoretic dual. Reverse every arrow: $m$ is a least common multiple of $a_1, \dots, a_n$ if

1. $m$ is a *common multiple* — $a_i \mid m$ for every $i$; and
2. $m$ is *least among them in the divisibility order* — every common multiple $m'$ ($a_i \mid m'$ for all $i$) satisfies $m \mid m'$.

So an lcm is a **least upper bound** (a supremum) in the divisibility poset, just as the gcd is a greatest lower bound. Same "unique up to associates" conclusion, for the same reason.

Now the crucial subtlety, and the reason this definition is more delicate than its $\mathbb{Z}$-flavoured intuition suggests: **a gcd need not exist.** The definition above says what it *means* to be a gcd, but it does not *produce* one. In the divisibility poset of a general integral domain, two elements may simply have no greatest lower bound — the common divisors may form a set with no top element. This genuinely happens. In $R = \mathbb{Z}[\sqrt{-5}]$, the elements $6$ and $2 + 2\sqrt{-5}$ have common divisors $2$ and $1 + \sqrt{-5}$, neither of which divides the other and which have no common upper bound among common divisors — so no gcd exists at all. The definition is a *specification*, not a *construction*; existence is a separate question, and the answer depends on the ring.

This is exactly where the [[Def - Unique Factorization Domain|unique factorization domain]] earns its place. In a UFD, unique factorisation lets you *build* a gcd: factor each $a_i$ into irreducibles, and for each irreducible $p$ take the *minimum* exponent to which $p$ appears across all the $a_i$; the product of these prime powers is a gcd. The lcm uses the *maximum* exponent. Existence is recovered precisely because the multiplicative monoid is free (that is what unique factorisation says), and in a free commutative monoid every finite set has a meet and a join — computed coordinatewise as min and max of exponent vectors. So: gcd and lcm are *defined* in any integral domain, but *guaranteed to exist* only in a UFD. Holding those two facts apart — the specification versus the existence theorem — is the entire content of this definition.

---

# The Definition

Let $R$ be an [[Def - Integral Domain|integral domain]] and let $a_1, a_2, \dots, a_n \in R$.

**Greatest common divisor.** An element $d \in R$ is a **greatest common divisor** of $a_1, \dots, a_n$ if

1. $d \mid a_i$ for every $i$ (it is a *common divisor*); and
2. whenever $d' \in R$ satisfies $d' \mid a_i$ for every $i$, then $d' \mid d$ (every common divisor divides $d$).

**Least common multiple.** An element $m \in R$ is a **least common multiple** of $a_1, \dots, a_n$ if

1. $a_i \mid m$ for every $i$ (it is a *common multiple*); and
2. whenever $m' \in R$ satisfies $a_i \mid m'$ for every $i$, then $m \mid m'$ ($m$ divides every common multiple).

Two facts are part of the definition's basic behaviour:

- **Uniqueness up to associates.** If $d$ and $\tilde d$ are both greatest common divisors of $a_1, \dots, a_n$, then $d \mid \tilde d$ and $\tilde d \mid d$, so $d$ and $\tilde d$ are [[Def - Irreducible and Prime Elements|associates]]. The same holds for least common multiples. A gcd or lcm is therefore never a single element but an associate-class; the notation $\gcd(\cdots)$, $\operatorname{lcm}(\cdots)$ denotes any representative.

- **Existence is not automatic.** The definition is a specification of what a gcd or lcm *is*, not a proof that one *exists*. In a general integral domain, $a_1, \dots, a_n$ may have **no** greatest common divisor and **no** least common multiple. Existence is guaranteed in a [[Def - Unique Factorization Domain|unique factorization domain]] (theorem below), and in particular in any [[Def - Principal Ideal Domain|principal ideal domain]] and any [[Def - Euclidean Domain|Euclidean domain]].

**Theorem (existence in a UFD).** If $R$ is a [[Def - Unique Factorization Domain|unique factorization domain]], then every finite list $a_1, \dots, a_n$ of non-zero elements has a greatest common divisor and a least common multiple, each unique up to associates.

> [!note]- Construction and proof
> Let $p_1, \dots, p_k$ be a list of irreducibles, no two associate, containing every irreducible factor of every $a_i$. By unique factorisation (clause (i) of the UFD definition), write each
> $$a_i = u_i \prod_{j=1}^{k} p_j^{\,n_{ij}}, \qquad u_i \text{ a unit}, \quad n_{ij} \in \mathbb{Z}_{\geq 0}.$$
> The exponents $n_{ij}$ are well-defined because factorisation is *unique* (clause (ii)).
>
> *Greatest common divisor.* For each $j$ set $m_j = \min_i n_{ij}$, the smallest exponent of $p_j$ over all the $a_i$, and put
> $$d = \prod_{j=1}^{k} p_j^{\,m_j}.$$
> Since $m_j \le n_{ij}$ for every $i$, the factorisation of $a_i$ contains that of $d$, so $d \mid a_i$ for all $i$: clause 1 holds. For clause 2, let $d'$ be any common divisor, $d' = v \prod_j p_j^{\,t_j}$. From $d' \mid a_i$, comparing exponents in the unique factorisation gives $t_j \le n_{ij}$ for every $i$, hence $t_j \le \min_i n_{ij} = m_j$ for every $j$, hence $d' \mid d$. So $d$ is a greatest common divisor.
>
> *Least common multiple.* Dually, set $M_j = \max_i n_{ij}$ and put $m = \prod_j p_j^{\,M_j}$. Then $a_i \mid m$ since $n_{ij} \le M_j$; and any common multiple $m'$ has $p_j$-exponent $\ge n_{ij}$ for all $i$, hence $\ge M_j$, hence $m \mid m'$.
>
> *Uniqueness.* Immediate from the definition: any two greatest common divisors divide each other, hence are associates; likewise for least common multiples. $\blacksquare$
>
> The proof uses unique factorisation *twice* — once for existence of the exponents (clause (i)) and once for their well-definedness (clause (ii)) — which is the precise reason the theorem needs a UFD and not merely an integral domain.

---

# Relate to Other Fields / Compression

The greatest common divisor and least common multiple are the **meet and join of the divisibility lattice**, and this is the compression that organises everything. Order the elements of an integral domain $R$ (modulo associates) by divisibility: $[a] \le [b]$ means $a \mid b$. This is a partial order. In this poset, a greatest common divisor of $a_1, \dots, a_n$ is exactly their **infimum** (greatest lower bound), and a least common multiple is exactly their **supremum** (least upper bound). The definition's clause structure — "is a lower/upper bound" plus "is the greatest/least such" — is the verbatim definition of infimum and supremum. So gcd and lcm are not number-theoretic curiosities; they are the lattice operations $\wedge$ and $\vee$ of the divisibility order, and "the gcd exists for all pairs" is precisely the statement that the divisibility poset is a **lattice**. A UFD is exactly an integral domain whose divisibility poset is a lattice — in fact the lattice of finite multisets of irreducibles, ordered componentwise, where $\wedge$ is componentwise min and $\vee$ is componentwise max.

This recovers a familiar special case. Take $R = \mathbb{Z}$ and a single prime $p$; restrict attention to powers of $p$. The poset of $\{1, p, p^2, p^3, \dots\}$ under divisibility is just $(\mathbb{Z}_{\geq 0}, \le)$ via $p^n \mapsto n$, gcd is $\min$, lcm is $\max$. The full divisibility lattice of $\mathbb{Z}$ is the product of one such chain per prime — which is why the UFD construction computes gcd and lcm coordinatewise as min and max of exponent vectors. The number-theoretic identity $\gcd(a,b)\cdot\operatorname{lcm}(a,b) = ab$ (up to associates) is then the lattice identity $\min(x,y) + \max(x,y) = x + y$ applied in each coordinate.

There is a sharper, ideal-theoretic compression available in a [[Def - Principal Ideal Domain|principal ideal domain]]. There, divisibility *is* reverse ideal inclusion, so the infimum/supremum in the divisibility order corresponds to the supremum/infimum of *ideals*. Concretely: $\gcd(a, b)$ generates the ideal $(a) + (b) = (a, b)$ — the *smallest ideal containing both* — and $\operatorname{lcm}(a, b)$ generates the ideal $(a) \cap (b)$ — the *largest ideal contained in both*. This is the Bézout phenomenon: in a PID, $\gcd(a,b) = ra + sb$ for some $r, s$, precisely because $\gcd(a,b)$ generates $(a,b) = \{ra + sb\}$. The gcd-as-ideal-sum and lcm-as-ideal-intersection dictionary is the cleanest way to *compute* with these objects, and it explains why gcds in a PID automatically satisfy a Bézout identity while gcds in a bare UFD (like $\mathbb{Z}[X]$) need not.

The genuinely novel content, with no clean analogue elsewhere, is the **non-existence** phenomenon. One's lattice-theoretic intuition, trained on $\mathbb{Z}$, suggests two elements always have a meet. The lesson of this definition is that divisibility posets of general integral domains are *not* lattices — they can have pairs with no greatest lower bound — and the failure is the same failure that breaks unique factorisation. Gcd-existence, UFD-ness, and lattice-ness of the divisibility order are three faces of one condition.

---

# Examples / Corollaries

**Is an instance — gcd and lcm in $\mathbb{Z}$.** For $a = 12, b = 18$: the common divisors are $\pm 1, \pm 2, \pm 3, \pm 6$, and each divides $6$, so $6$ is a greatest common divisor — as is $-6$, its associate. Convention selects the positive representative, $\gcd(12, 18) = 6$. The common multiples are the multiples of $36$, the least (up to sign) being $36 = \operatorname{lcm}(12, 18)$. Note $\gcd \cdot \operatorname{lcm} = 6 \cdot 36 = 216 = 12 \cdot 18$, the lattice identity in action.

**Is an instance — gcd of polynomials in $F[X]$.** In $\mathbb{Q}[X]$, a greatest common divisor of $X^2 - 1$ and $X^2 - 2X + 1 = (X-1)^2$ is $X - 1$ — but so is $2X - 2$ and $7X - 7$, all associates (units of $\mathbb{Q}[X]$ are non-zero constants). The conventional representative is the *monic* one, $X - 1$. Since $F[X]$ is a [[Def - Euclidean Domain|Euclidean domain]], this gcd is computable by the Euclidean algorithm and satisfies a Bézout identity.

**Is an instance — existence in any UFD.** In $\mathbb{Z}[X]$, a unique factorization domain, the gcd of $2X$ and $6$ is $2$ (the irreducible $2$ appears, with exponent $\min(1,1) = 1$; the irreducible $X$ has exponent $\min(1, 0) = 0$). This gcd exists by the existence theorem above. Observe, however, that $\mathbb{Z}[X]$ is *not* a PID, so this gcd need not be a Bézout combination: indeed $2 \neq f \cdot 2X + g \cdot 6$ for any $f, g \in \mathbb{Z}[X]$, since the right side always has even constant term equal to $6g(0)$ — there is no Bézout identity for $\gcd(2X, 6)$. Existence of the gcd and the Bézout property are *different* statements; a UFD guarantees the first, only a PID the second.

**Is NOT an instance — no gcd exists in $\mathbb{Z}[\sqrt{-5}]$.** This is the essential non-example: it exhibits a pair of elements in an integral domain with *no greatest common divisor at all*.

> [!note]- Why $6$ and $2 + 2\sqrt{-5}$ have no gcd in $\mathbb{Z}[\sqrt{-5}]$
> Recall (from the [[Def - Unique Factorization Domain|UFD]] non-example) that in $R = \mathbb{Z}[\sqrt{-5}]$ the elements $2$ and $1 + \sqrt{-5}$ are both irreducible, are not associates (norms $4$ and $6$ differ), and neither divides the other.
>
> Consider $a = 6$ and $b = 2 + 2\sqrt{-5} = 2(1 + \sqrt{-5})$. Both $2$ and $1 + \sqrt{-5}$ are common divisors: $2 \mid 6$ and $2 \mid b$ obviously; and $1 + \sqrt{-5} \mid b$ obviously, while $1 + \sqrt{-5} \mid 6$ because $6 = (1+\sqrt{-5})(1 - \sqrt{-5})$.
>
> Suppose, for contradiction, that a greatest common divisor $d$ of $a$ and $b$ existed. By clause 2, every common divisor divides $d$, so $2 \mid d$ and $(1 + \sqrt{-5}) \mid d$. Taking norms, $N(2) = 4$ and $N(1 + \sqrt{-5}) = 6$ both divide $N(d)$, so $\operatorname{lcm}(4,6) = 12 \mid N(d)$, giving $N(d) \ge 12$. On the other hand $d \mid a = 6$, so $N(d) \mid N(6) = 36$. The divisors of $36$ that are multiples of $12$ are $12$ and $36$. One checks no element of $\mathbb{Z}[\sqrt{-5}]$ has norm $12$ (the equation $x^2 + 5y^2 = 12$ has no integer solution), and an element of norm $36$ dividing $6$ would be an associate of $6$, which does not have both $2$ and $1+\sqrt{-5}$ as divisors of itself in a way making it a *common* divisor of $a$ and $b$ — chasing this through, no candidate $d$ works. So no greatest common divisor of $6$ and $2 + 2\sqrt{-5}$ exists.
>
> The structural reason is exactly the failure of unique factorisation: the common divisors $2$ and $1 + \sqrt{-5}$ are incomparable atoms with no common "supremum among common divisors", so the divisibility poset of $\mathbb{Z}[\sqrt{-5}]$ is not a lattice.

**Corollary — uniqueness up to associates, always.** In *any* integral domain, if $d$ and $\tilde d$ are both greatest common divisors of the same list, then by clause 2 each divides the other, so they are associates. This needs no UFD hypothesis — it is immediate from the definition — and it is why one never speaks of "the" gcd as a specific element without first fixing a convention (positive in $\mathbb{Z}$, monic in $F[X]$).

**Corollary — coprimality.** Elements $a_1, \dots, a_n$ are called **coprime** if $1$ is a greatest common divisor — equivalently, their only common divisors are units. In a [[Def - Principal Ideal Domain|principal ideal domain]] this is the same as the existence of a Bézout identity $1 = r_1 a_1 + \cdots + r_n a_n$, since $\gcd = 1$ means the [[Def - Ideal|ideal]] $(a_1, \dots, a_n)$ is all of $R$. In a bare UFD coprimality still makes sense (no common irreducible factor) but need not give a Bézout identity.

**Calibration check.** Verify that $\gcd(a, 0) = a$ up to associates (every divisor of $a$ divides $0$, so the common divisors of $a$ and $0$ are exactly the divisors of $a$, with top element $a$), and that $\operatorname{lcm}(a, 0) = 0$. Verify that if $a \mid b$ then $\gcd(a, b) = a$ and $\operatorname{lcm}(a, b) = b$ up to associates. Confirm that in a UFD, $\gcd(a,b) \cdot \operatorname{lcm}(a,b)$ is an associate of $ab$, and locate where the proof uses $\min(x,y) + \max(x,y) = x + y$. If you can also explain, in one sentence, *why* a gcd can fail to exist — the common divisors form a poset with no top element — the definition has fully landed.

---

# Unlocked by This

> [!tip] Bézout's identity in a principal ideal domain *(from this topic)*
> In a [[Def - Principal Ideal Domain|principal ideal domain]] the greatest common divisor $d$ of $a$ and $b$ generates the ideal $(a, b)$, so $d = ra + sb$ for some $r, s \in R$. This Bézout identity is the engine of the proof that [[Thm - Principal Ideal Domains are Unique Factorization Domains|irreducible elements are prime in a PID]], and hence of unique factorisation itself.

> [!tip] The Chinese Remainder Theorem *(from later ring theory)*
> Coprimality — defined here as $\gcd = 1$ — is exactly the hypothesis of the Chinese Remainder Theorem: if $a$ and $b$ are coprime in a suitable ring then $R/(ab) \cong R/(a) \times R/(b)$. The theorem is the structural payoff of the gcd reaching $1$.

> [!tip] Computing gcds via the Euclidean algorithm *(from this topic)*
> In a [[Def - Euclidean Domain|Euclidean domain]] the greatest common divisor is not merely guaranteed to exist — it is *computed* by the Euclidean algorithm, iterating division with remainder until the remainder vanishes. The last non-zero remainder is a gcd, and back-substitution produces the Bézout coefficients.
