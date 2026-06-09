---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - The Induced Map on Spectra"
  - "Thm - Lying Over"
  - "Thm - Incomparability"
  - "Def - Gaussian Integers"
  - "Def - Prime and Maximal Ideal"
  - "Thm - Maximal and Prime Ideals via Quotients"
tags: [algebra, commutative-algebra]
---

# Problem Statement

The inclusion $\mathbb{Z} \subseteq \mathbb{Z}[i]$ is an integral extension ($i$ satisfies $X^2 + 1 = 0$). For each rational prime $p$, **determine the fibre** of the contraction map $\iota^* : \operatorname{Spec}\mathbb{Z}[i] \to \operatorname{Spec}\mathbb{Z}$ over the maximal ideal $(p)$ — that is, find all primes $\mathfrak{q} \trianglelefteq \mathbb{Z}[i]$ with $\mathfrak{q} \cap \mathbb{Z} = (p)$ — and identify the three cases:

- **$p = 2$:** the fibre has one prime, $\mathfrak{q} = (1+i)$, with $(2) = (1+i)^2$ up to a unit ($p$ **ramifies**);
- **$p \equiv 1 \pmod 4$:** the fibre has two distinct primes, $(\pi)$ and $(\bar\pi)$ where $p = \pi\bar\pi = a^2 + b^2$ ($p$ **splits**);
- **$p \equiv 3 \pmod 4$:** the fibre has one prime, $(p)$ itself ($p$ stays **inert**).

Verify in each case that the fibre is non-empty (lying over) and that its primes are pairwise incomparable and maximal (incomparability).

**Recall:**

The objects in play are the Gaussian integers, the induced map on spectra and its fibre, lying over, incomparability, and the prime/maximal-ideal criterion via quotients.

![[Def - Gaussian Integers#The Definition]]

The [[Def - Gaussian Integers|Gaussian integers]] $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$ form a [[Def - Euclidean Domain|Euclidean domain]] under the norm $N(a+bi) = a^2 + b^2$, hence a [[Def - Principal Ideal Domain|PID]] and a [[Def - Unique Factorization Domain|UFD]]. The norm is multiplicative, $N(zw) = N(z)N(w)$, and $z \in \mathbb{Z}[i]$ is a unit iff $N(z) = 1$ (units: $\pm 1, \pm i$).

![[Def - The Induced Map on Spectra#The fibre over a prime]]

The **fibre** of $\iota^* : \operatorname{Spec}\mathbb{Z}[i] \to \operatorname{Spec}\mathbb{Z}$ over $(p)$ is $\{\mathfrak{q} \in \operatorname{Spec}\mathbb{Z}[i] : \mathfrak{q} \cap \mathbb{Z} = (p)\}$, and it is in bijection with $\operatorname{Spec}$ of the **fibre ring** $\mathbb{Z}[i] \otimes_{\mathbb{Z}} \mathbb{F}_p = \mathbb{Z}[i]/p\mathbb{Z}[i]$.

[[Thm - Lying Over|Lying over]]: for an integral extension, every prime of the base has a prime above it, so each fibre is non-empty. [[Thm - Incomparability|Incomparability]]: distinct primes over the same prime are incomparable, and (over the maximal ideal $(p)$) they are maximal. The [[Thm - Maximal and Prime Ideals via Quotients|quotient criterion]] reads the primes of $\mathbb{Z}[i]/p\mathbb{Z}[i]$ off the factorisation of $X^2+1$ via $\mathbb{Z}[i]/p\mathbb{Z}[i] \cong \mathbb{F}_p[X]/(X^2+1)$.

---

# Convergent Strategy

**Problem class.** This is a *compute-a-fibre* problem — the model instance of the chapter's central object, the fibre of a finite map over a point. As the [[Commutative Algebra VIII — Going Up and Going Down#Problem-Solving Strategy|topic-page strategy]] records, to describe a fibre completely you replace it by the spectrum of the fibre ring $B \otimes_A \kappa(\mathfrak{p})$, which over a field is an explicit finite-dimensional algebra whose primes you list by factoring a polynomial.

**Assumption pattern.** The hypothesis "$\mathbb{Z} \subseteq \mathbb{Z}[i]$ integral" gives lying over (fibres non-empty) and incomparability (fibres are antichains of maximal ideals). The hypothesis "$\mathbb{Z}[i] = \mathbb{Z}[X]/(X^2+1)$" lets the fibre ring be computed as $\mathbb{F}_p[X]/(X^2+1)$ — a *monogenic* extension, where one polynomial controls everything. The recognisable trigger is that the base prime $(p)$ is *maximal* with residue field $\mathbb{F}_p = \kappa((p))$, so the fibre ring is an honest $\mathbb{F}_p$-algebra.

**Theorem routing.** The route is: identify the fibre ring $\mathbb{Z}[i]/p\mathbb{Z}[i] \cong \mathbb{F}_p[X]/(X^2+1)$ (base change to $\mathbb{F}_p$); factor $X^2+1$ over $\mathbb{F}_p$ using "$-1$ is a square mod $p$ iff $p \equiv 1 \bmod 4$" (the [[Thm - Maximal and Prime Ideals via Quotients|quotient criterion]] then turns each irreducible factor into a maximal ideal of the fibre ring); pull these back through $\mathbb{Z}[i] \to \mathbb{Z}[i]/p\mathbb{Z}[i]$ to get the primes of $\mathbb{Z}[i]$ over $(p)$. Lying over guarantees at least one factor exists; incomparability matches the count of *distinct* primes to the count of *distinct* irreducible factors.

**Key decision point.** The non-obvious move is to compute the fibre *ring* rather than hunt for primes directly. One could try to factor $p$ in $\mathbb{Z}[i]$ by trial — but the systematic route is $\mathbb{Z}[i]/p\mathbb{Z}[i] \cong \mathbb{F}_p[X]/(X^2+1)$ and the arithmetic of $-1$ as a quadratic residue. The second decision is recognising that the three cases of factorisation ($X^2+1$ irreducible, split with distinct roots, square) correspond exactly to inert, split, ramified — and that the *square* case at $p = 2$ ($X^2 + 1 = (X+1)^2$ in $\mathbb{F}_2$) is the unique ramified prime, where the fibre ring is non-reduced.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VIII — Going Up and Going Down#Legal Operations|the topic page's Legal Operations]]:

1. **Translate the fibre into the fibre ring (operation 1, fibre-ring form).** Replace "primes of $\mathbb{Z}[i]$ over $(p)$" by "primes of $\mathbb{Z}[i] \otimes_{\mathbb{Z}}\mathbb{F}_p = \mathbb{Z}[i]/p\mathbb{Z}[i]$".

2. **Compute the fibre ring as a quotient of a polynomial ring over a field.** $\mathbb{Z}[i]/p\mathbb{Z}[i] \cong \mathbb{F}_p[X]/(X^2+1)$, using $\mathbb{Z}[i] \cong \mathbb{Z}[X]/(X^2+1)$ and reducing coefficients mod $p$.

3. **Reduce maximality to the base via the domain criterion (operation 6).** Over the maximal ideal $(p)$, every prime in the fibre is maximal; correspondingly every prime of the fibre ring is maximal (it is a finite $\mathbb{F}_p$-algebra).

4. **Recognise a finite fibre via the fibre ring (operation 9).** $\mathbb{F}_p[X]/(X^2+1)$ is $2$-dimensional over $\mathbb{F}_p$, hence Artinian, with at most two maximal ideals — so the fibre has one or two points.

5. **Read primes off a polynomial factorisation.** The maximal ideals of $\mathbb{F}_p[X]/(X^2+1)$ correspond to the irreducible factors of $X^2+1$ over $\mathbb{F}_p$, via the quotient criterion.

---

# Hints

> [!note]- Hint 1
> The fibre over $(p)$ is, by definition, the set of primes of $\mathbb{Z}[i]$ contracting to $(p)$. Do not hunt for them by hand. The chapter's reflex: the fibre is $\operatorname{Spec}$ of the *fibre ring* $\mathbb{Z}[i] \otimes_{\mathbb{Z}} \kappa((p))$. What is $\kappa((p))$, and what does tensoring $\mathbb{Z}[i]$ with it give?

> [!note]- Hint 2
> $\kappa((p)) = \mathbb{Z}/(p) = \mathbb{F}_p$, so the fibre ring is $\mathbb{Z}[i]/p\mathbb{Z}[i]$. Now use $\mathbb{Z}[i] \cong \mathbb{Z}[X]/(X^2+1)$ (sending $X \mapsto i$). Reducing mod $p$, $\mathbb{Z}[i]/p\mathbb{Z}[i] \cong \mathbb{F}_p[X]/(X^2+1)$. The primes of this ring are governed by how $X^2+1$ factors over $\mathbb{F}_p$.

> [!note]- Hint 3
> $X^2+1$ factors over $\mathbb{F}_p$ according to whether $-1$ is a square mod $p$. By the supplement to quadratic reciprocity, $-1$ is a square mod $p$ iff $p \equiv 1 \pmod 4$ (and $p = 2$ is special: $X^2+1 = (X+1)^2$ in $\mathbb{F}_2$). So there are three cases: irreducible ($p \equiv 3$), two distinct linear factors ($p \equiv 1$), a repeated linear factor ($p = 2$).

> [!note]- Hint 4
> Translate each case back to $\mathbb{Z}[i]$. *Irreducible:* $\mathbb{F}_p[X]/(X^2+1)$ is a field $\mathbb{F}_{p^2}$, one maximal ideal $(0)$, so $p\mathbb{Z}[i]$ is itself prime — $(p)$ is inert. *Two factors $X^2+1 = (X-a)(X+a)$:* two maximal ideals, pulling back to two primes $(p, i - a)$ and $(p, i + a)$, which are $(\pi), (\bar\pi)$ with $\pi = a + i$... rather $p = \pi\bar\pi$ — $p$ splits. *Repeated factor at $p=2$:* $X^2 + 1 = (X+1)^2$, one maximal ideal but the ring is non-reduced, $(2) = (1+i)^2$ up to a unit — $p$ ramifies.

---

# Solution

The proof is one computation applied three ways: compute the fibre ring $\mathbb{Z}[i]/p\mathbb{Z}[i] \cong \mathbb{F}_p[X]/(X^2+1)$, factor $X^2+1$ over $\mathbb{F}_p$, and read off the primes. The arithmetic input is the single fact "$-1$ is a square mod $p \iff p \equiv 1 \pmod 4$", which splits the analysis into inert ($p\equiv 3$), split ($p \equiv 1$), and the lone ramified prime $p = 2$.

**Step 1: The fibre over $(p)$ is $\operatorname{Spec}$ of the fibre ring $\mathbb{F}_p[X]/(X^2+1)$.**

The primes of $\mathbb{Z}[i]$ lying over $(p)$ correspond bijectively to the primes of $\mathbb{Z}[i]/p\mathbb{Z}[i] \cong \mathbb{F}_p[X]/(X^2+1)$.

> [!note]- Derivation
> By the [[Def - The Induced Map on Spectra|fibre dictionary]], the fibre over $(p)$ is in bijection with $\operatorname{Spec}(\mathbb{Z}[i] \otimes_{\mathbb{Z}} \kappa((p)))$. Here $\kappa((p)) = \operatorname{Frac}(\mathbb{Z}/(p)) = \mathbb{F}_p$ (as $(p)$ is maximal, the residue field is just $\mathbb{Z}/(p)$). So the fibre ring is
> $$\mathbb{Z}[i] \otimes_{\mathbb{Z}} \mathbb{F}_p = \mathbb{Z}[i]/p\mathbb{Z}[i].$$
> Using the presentation $\mathbb{Z}[i] \cong \mathbb{Z}[X]/(X^2+1)$ (the isomorphism $X \mapsto i$, valid since $i$ satisfies $X^2+1$ and $\mathbb{Z}[i]$ is spanned by $1, i$), reduce coefficients modulo $p$:
> $$\mathbb{Z}[i]/p\mathbb{Z}[i] \cong \big(\mathbb{Z}[X]/(X^2+1)\big)\big/ p \cong \mathbb{F}_p[X]/(X^2+1).$$
> This is a $2$-dimensional $\mathbb{F}_p$-algebra (basis $1, X$), hence Artinian, with finitely many primes — all maximal (a finite-dimensional algebra over a field is Artinian, so $\dim = 0$). The primes correspond, via the [[Thm - Maximal and Prime Ideals via Quotients|quotient criterion]], to the irreducible factors of $X^2+1$ in $\mathbb{F}_p[X]$. By [[Thm - Lying Over|lying over]] the fibre is non-empty, so $X^2+1$ always has at least one factor — which it does, being a non-unit.

**Step 2: $p \equiv 3 \pmod 4$ — inert (one prime).**

$X^2+1$ is irreducible over $\mathbb{F}_p$, so the fibre ring is the field $\mathbb{F}_{p^2}$, with one prime $(0)$; pulling back, $p\mathbb{Z}[i]$ is itself prime, and the fibre is the single prime $(p)$.

> [!note]- Derivation
> $X^2 + 1$ has a root in $\mathbb{F}_p$ iff $-1$ is a square mod $p$. For $p \equiv 3 \pmod 4$, $-1$ is a *non*-square (the multiplicative group $\mathbb{F}_p^\times$ is cyclic of order $p - 1 \equiv 2 \pmod 4$, so $-1$, the unique element of order $2$, is a square iff $4 \mid p - 1$). Hence $X^2 + 1$ has no root, and being degree $2$ it is irreducible over $\mathbb{F}_p$. Therefore
> $$\mathbb{F}_p[X]/(X^2+1) \cong \mathbb{F}_{p^2},$$
> a field, with unique prime $(0)$. Its preimage in $\mathbb{Z}[i]$ under $\mathbb{Z}[i] \to \mathbb{Z}[i]/p\mathbb{Z}[i]$ is $p\mathbb{Z}[i]$ itself, so $p\mathbb{Z}[i]$ is a maximal ideal of $\mathbb{Z}[i]$ — the single prime in the fibre. The element $p$ remains *prime* in $\mathbb{Z}[i]$: it does not factor. (For instance $p = 3, 7, 11$.) This is the **inert** case.

**Step 3: $p \equiv 1 \pmod 4$ — split (two distinct primes).**

$X^2+1 = (X-a)(X+a)$ with $a^2 \equiv -1$, two distinct linear factors, giving two maximal ideals of the fibre ring; these pull back to two distinct conjugate primes $(\pi), (\bar\pi)$ with $p = \pi\bar\pi = a'^2 + b'^2$.

> [!note]- Derivation
> For $p \equiv 1 \pmod 4$, $-1$ is a square mod $p$: there is $a \in \mathbb{F}_p$ with $a^2 = -1$. Then $X^2 + 1 = (X - a)(X + a)$ over $\mathbb{F}_p$, and the two factors are distinct (their difference $2a \neq 0$ since $p$ is odd and $a \neq 0$). By the [[Thm - Maximal and Prime Ideals via Quotients|quotient criterion]] (or the Chinese Remainder Theorem),
> $$\mathbb{F}_p[X]/(X^2+1) \cong \mathbb{F}_p \times \mathbb{F}_p,$$
> with two maximal ideals, the kernels of the two projections. Pulling back through $\mathbb{Z}[i] \to \mathbb{Z}[i]/p\mathbb{Z}[i]$, these are the primes $\mathfrak{q}_1 = (p, i - a)$ and $\mathfrak{q}_2 = (p, i + a)$ of $\mathbb{Z}[i]$ (lifting $a$ to an integer). They are distinct (their sum contains $2i$ and $2a$, hence $1$, only if they were equal — but $\mathfrak{q}_1 + \mathfrak{q}_2 = \mathbb{Z}[i]$ shows they are *coprime*, in particular distinct). Since $\mathbb{Z}[i]$ is a [[Def - Principal Ideal Domain|PID]], each is principal: $\mathfrak{q}_1 = (\pi)$, $\mathfrak{q}_2 = (\bar\pi)$ with $N(\pi) = p$, so $p = \pi\bar\pi$ and writing $\pi = a' + b'i$ gives $p = a'^2 + b'^2$ — the classical "$p \equiv 1 \bmod 4 \Rightarrow p$ is a sum of two squares". For example $5 = (2+i)(2-i)$, $13 = (3+2i)(3-2i)$. This is the **split** case.

**Step 4: $p = 2$ — ramified (one prime, with multiplicity).**

$X^2 + 1 = (X+1)^2$ over $\mathbb{F}_2$, so the fibre ring is non-reduced with a single maximal ideal; the unique prime over $(2)$ is $(1+i)$, and $(2) = (1+i)^2$ up to a unit.

> [!note]- Derivation
> Over $\mathbb{F}_2$, $X^2 + 1 = X^2 - 1 = (X-1)(X+1) = (X+1)^2$ (since $-1 = 1$ in $\mathbb{F}_2$). So
> $$\mathbb{F}_2[X]/(X^2+1) \cong \mathbb{F}_2[X]/(X+1)^2,$$
> a local ring with maximal ideal $(X+1)$ and a nilpotent $X+1$ ($(X+1)^2 = 0$) — it is *non-reduced*. Hence the fibre over $(2)$ has a single prime, the pullback of $(X+1)$, namely $\mathfrak{q} = (2, i + 1) = (1 + i)$ (the last equality because $2 = -i(1+i)^2$, so $2 \in (1+i)$ and $(2, 1+i) = (1+i)$). Indeed $N(1+i) = 2$, so $(1+i)$ is prime in the PID $\mathbb{Z}[i]$, and
> $$(1+i)^2 = 1 + 2i + i^2 = 2i, \qquad \text{so } (2) = (2i) = (1+i)^2 \text{ as ideals (}i\text{ a unit)}.$$
> The prime $(1+i)$ appears to the *second power* — the multiplicity is $2 = \deg(X^2+1)$ — which is what "ramified" means. The non-reducedness of the fibre ring is the algebraic signature of ramification. This is the unique ramified prime for $\mathbb{Z}[i]$.

> [!note]- Complete formal solution
> The extension $\mathbb{Z} \subseteq \mathbb{Z}[i]$ is integral, so by [[Thm - Lying Over|lying over]] every $(p)$ has a non-empty fibre, and by [[Thm - Incomparability|incomparability]] the fibre is a set of pairwise-incomparable primes, all maximal (they lie over the maximal ideal $(p)$).
>
> **Fibre ring.** The fibre over $(p)$ is $\operatorname{Spec}$ of
> $$\mathbb{Z}[i] \otimes_{\mathbb{Z}} \mathbb{F}_p = \mathbb{Z}[i]/p\mathbb{Z}[i] \cong \mathbb{F}_p[X]/(X^2+1),$$
> using $\mathbb{Z}[i] \cong \mathbb{Z}[X]/(X^2+1)$. Its maximal ideals correspond to the irreducible factors of $X^2+1$ over $\mathbb{F}_p$.
>
> **Case $p \equiv 3 \pmod 4$ (inert).** $-1$ is a non-square mod $p$, so $X^2+1$ is irreducible, the fibre ring is $\mathbb{F}_{p^2}$, and $p\mathbb{Z}[i]$ is the unique (prime) ideal in the fibre. $p$ stays prime.
>
> **Case $p \equiv 1 \pmod 4$ (split).** $-1 = a^2$ for some $a$, $X^2 + 1 = (X-a)(X+a)$ with distinct factors, fibre ring $\cong \mathbb{F}_p \times \mathbb{F}_p$, two distinct primes $(\pi) = (p, i-a)$ and $(\bar\pi) = (p, i+a)$, $p = \pi\bar\pi$, so $p = a'^2 + b'^2$.
>
> **Case $p = 2$ (ramified).** $X^2 + 1 = (X+1)^2$ over $\mathbb{F}_2$, fibre ring $\mathbb{F}_2[X]/(X+1)^2$ non-reduced with one maximal ideal; the unique prime is $(1+i)$, and $(2) = (1+i)^2$ up to a unit.
>
> In all three cases the fibre is non-empty (lying over) with one or two incomparable maximal primes (incomparability), confirming the abstract theorems on the prototype. $\blacksquare$

---

# Key Takeaways

**To describe a fibre, compute the fibre ring and factor.** The reusable principle is the chapter's central move: the fibre of $\operatorname{Spec} B \to \operatorname{Spec} A$ over $\mathfrak{p}$ is $\operatorname{Spec}(B \otimes_A \kappa(\mathfrak{p}))$, and when $B = A[X]/(f)$ is *monogenic* the fibre ring is $\kappa(\mathfrak{p})[X]/(\bar f)$ — so the entire fibre is encoded in how the single polynomial $\bar f$ factors over the residue field. The trigger is any "find the primes over $\mathfrak{p}$" question for a monogenic extension: reduce $f$ modulo $\mathfrak{p}$ and factor. This transfers verbatim to *every* number ring $\mathbb{Z}[\alpha] = \mathbb{Z}[X]/(g)$ — the splitting of $p$ is read off the factorisation of $g$ mod $p$ (Dedekind's theorem) — and to coordinate rings of plane curves, where the fibre of a projection is read off a defining polynomial.

**The three factorisation types are inert / split / ramified, and ramification is non-reducedness of the fibre ring.** Degree-$2$ has exactly three ways to factor mod $p$ — irreducible, two distinct factors, a repeated factor — and these are precisely the three behaviours of a prime in a quadratic extension. The diagnostic to internalise: a *repeated* factor (the fibre ring acquires a nilpotent, becomes non-reduced) is the signature of *ramification*, the case where the abstract count "number of primes $\leq$ degree" is strict because primes appear with multiplicity. Whenever a fibre ring is non-reduced, suspect ramification; whenever it is a product of fields, the prime splits cleanly; whenever it is a single field, the prime is inert. This reduces a subtle arithmetic phenomenon to "is this polynomial separable mod $p$?".

**Lying over and incomparability are not decoration — they certify the count.** It is easy to compute the factorisation and forget that the abstract theorems are doing work. Lying over guarantees $X^2+1$ has *at least one* factor over every $\mathbb{F}_p$ (the fibre is never empty), which one might otherwise have to check case by case. Incomparability guarantees the primes in a fibre are *distinct and incomparable* — so the two factors in the split case give two genuinely different primes, not one prime counted twice. When you generalise to higher-degree extensions, where a fibre can have many primes, these two theorems are what license "count the distinct irreducible factors to count the distinct primes", and the multiplicity of a factor (ramification index) is the refinement they do *not* see — that requires the finer structure of the non-reduced fibre ring. The companion exercise [[Ex - Fibres of a finite map are finite]] isolates exactly the finiteness that incomparability plus module-finiteness provides.
