---
type: exercise
subject: commutative-algebra
difficulty: "⭐"
prereqs:
  - "Def - Discrete Valuation and Valuation Ring"
  - "Def - Local Ring and Residue Field"
  - "Def - Multiplicative Set and Localization"
  - "Def - Prime and Maximal Ideal"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $p$ be a prime number and $\mathbb{Z}_{(p)} = \big\{\tfrac ab \in \mathbb{Q} : p \nmid b\big\}$ the [[Def - Multiplicative Set and Localization|localization]] of $\mathbb{Z}$ at the prime ideal $(p)$. Prove that $\mathbb{Z}_{(p)}$ is a [[Def - Discrete Valuation and Valuation Ring|discrete valuation ring]] by:

1. Showing that $v_p\big(p^n \tfrac ab\big) = n$ (for $p \nmid a, b$), extended by $v_p(0) = \infty$, is a well-defined [[Def - Discrete Valuation and Valuation Ring|discrete valuation]] on $\mathbb{Q}$.
2. Identifying its valuation ring as exactly $\mathbb{Z}_{(p)}$.
3. Concluding that $\mathbb{Z}_{(p)}$ is a DVR with uniformizer $\pi = p$, maximal ideal $(p)$, and residue field $\mathbb{F}_p$.

**Recall:**

![[Def - Discrete Valuation and Valuation Ring#The Definition]]

A [[Def - Multiplicative Set and Localization|localization]] $\mathbb{Z}_{(p)} = S^{-1}\mathbb{Z}$ with $S = \mathbb{Z}\setminus(p) = \{n \in \mathbb{Z} : p\nmid n\}$ consists of all fractions $\tfrac ab$ in lowest terms with $p \nmid b$; it is a [[Def - Local Ring and Residue Field|local ring]] with unique maximal ideal $(p)\mathbb{Z}_{(p)} = \{\tfrac ab : p \mid a,\ p\nmid b\}$.

Every nonzero rational has a unique expression $x = p^n \tfrac ab$ with $n \in \mathbb{Z}$ and $p \nmid a$, $p \nmid b$, by collecting all factors of $p$ from numerator and denominator. The integer $n$ is the **$p$-adic valuation** $v_p(x)$, positive when $p$ divides the numerator, negative when $p$ divides the denominator.

---

# Convergent Strategy

**Problem class.** This is a *recognize-a-DVR* problem in its most basic form: a concretely given local ring is to be exhibited as the valuation ring of an explicit valuation. As the [[Commutative Algebra XIII — Dedekind Domains and DVRs#Problem-Solving Strategy|topic strategy]] records, the cleanest route to "this is a DVR" is condition (1) of the [[Thm - Characterization of Discrete Valuation Rings|characterization]] — produce the valuation directly — when the valuation is staring at you, as it is here ($v_p$ = power of $p$).

**Assumption pattern.** The single structural fact is unique factorization in $\mathbb{Z}$: every integer, hence every rational, has a unique power of $p$ in it. This is what makes $v_p$ well-defined and additive. The assumption "$p$ is prime" enters exactly to guarantee that $p \mid ab \Rightarrow p \mid a$ or $p \mid b$, which is what gives $v_p(xy) = v_p(x) + v_p(y)$ and forbids cancellation from creating new $p$'s.

**Theorem routing.** The route is direct: verify the three axioms of a [[Def - Discrete Valuation and Valuation Ring|discrete valuation]] ($v_p$ surjective onto $\mathbb{Z}$, multiplicative, ultrametric) using unique factorization; then compute the valuation ring $\{v_p \geq 0\} = \mathbb{Z}_{(p)}$ by reading off "no $p$ in the denominator $\iff v_p \geq 0$"; then the definition of a DVR is satisfied by construction. No characterization theorem is even needed — this is the *model* the characterization abstracts.

**Key decision point.** The only subtlety is the **ultrametric inequality** $v_p(x + y) \geq \min\{v_p(x), v_p(y)\}$, which is not multiplicative bookkeeping but an additive fact. The non-obvious move is to factor out the smaller power of $p$ from the sum: if $v_p(x) = m \leq n = v_p(y)$, write $x = p^m u$, $y = p^m(p^{n-m}w)$ with $u, w$ having no $p$, so $x + y = p^m(u + p^{n-m}w)$ and the bracket is an integer (no negative $p$-power), giving $v_p(x+y) \geq m$. Recognizing that "factor out the minimum" is the mechanism is the whole insight.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra XIII — Dedekind Domains and DVRs#Legal Operations|the topic page's Legal Operations]]:

1. **Read off valuation arithmetic (operation 1).** Once $v_p$ is established, multiplicativity $v_p(xy) = v_p(x) + v_p(y)$ and the units/uniformizer description ($u$ a unit $\iff v_p(u) = 0$, $\pi = p$) follow by collecting powers of $p$.

2. **Detect a uniformizer / read the ideals (operation 1 applied to ideals).** The ideals $\{v_p \geq n\} = (p^n)$ are read directly off the valuation, exhibiting $\mathbb{Z}_{(p)}$ as having the single descending chain of ideals characteristic of a DVR.

---

# Hints

> [!note]- Hint 1
> You are asked to show a local ring is a DVR, and a DVR is *defined* as the valuation ring of some discrete valuation. The valuation is already named: $v_p(x)$ is the power of $p$ in $x$. So the task is purely to check $v_p$ satisfies the three axioms, then compute $\{v_p \geq 0\}$.

> [!note]- Hint 2
> Well-definedness and multiplicativity are unique factorization in $\mathbb{Z}$: write $x = p^m a/b$, $y = p^n c/d$ with no $p$ in $a, b, c, d$; then $xy = p^{m+n}\cdot ac/bd$ and $p \nmid ac, bd$ because $p$ is prime. So $v_p(xy) = m + n$.

> [!note]- Hint 3
> For the ultrametric inequality, suppose $v_p(x) = m \leq n = v_p(y)$ and factor out $p^m$ from the sum: $x + y = p^m(\text{something with no negative power of } p)$. Conclude $v_p(x+y) \geq m = \min$. Watch that equality can fail — e.g. $p + (-p) = 0$ has $v_p = \infty$.

> [!note]- Hint 4
> The valuation ring is $\{x : v_p(x) \geq 0\}$ = "no $p$ in the denominator" = $\{\tfrac ab : p \nmid b\} = \mathbb{Z}_{(p)}$. The units are $v_p = 0$ (no $p$ at all), the maximal ideal is $v_p \geq 1$ = $(p)$, and the residue field is $\mathbb{Z}_{(p)}/(p) \cong \mathbb{Z}/p = \mathbb{F}_p$.

---

# Solution

The proof is three short verifications. Step 1 checks $v_p$ is a discrete valuation using unique factorization in $\mathbb{Z}$, with the only real content in the ultrametric inequality. Step 2 computes the valuation ring and finds it is exactly $\mathbb{Z}_{(p)}$. Step 3 reads off the DVR data — uniformizer $p$, maximal ideal $(p)$, residue field $\mathbb{F}_p$ — and concludes.

**Step 1: $v_p$ is a discrete valuation on $\mathbb{Q}$.**

The map $v_p : \mathbb{Q}^\times \to \mathbb{Z}$, $v_p(p^n \tfrac ab) = n$ (with $p\nmid a, b$), is a well-defined surjective homomorphism satisfying the ultrametric inequality.

> [!note]- Derivation
> **Well-defined.** By unique factorization in $\mathbb{Z}$, each nonzero rational $x$ has a unique form $x = p^n \tfrac ab$ with $p \nmid a$ and $p \nmid b$: collect every factor of $p$ from numerator and denominator into $p^n$. So $n = v_p(x)$ is unambiguous.
>
> **Surjective.** $v_p(p^n) = n$ for every $n \in \mathbb{Z}$ (negative $n$ via $1/p^{|n|}$), so $v_p$ hits all of $\mathbb{Z}$.
>
> **Homomorphism.** Let $x = p^m\tfrac ab$, $y = p^n\tfrac cd$ with $p \nmid a,b,c,d$. Then $xy = p^{m+n}\tfrac{ac}{bd}$, and since $p$ is prime, $p \nmid ac$ and $p \nmid bd$. Hence $v_p(xy) = m + n = v_p(x) + v_p(y)$.
>
> **Ultrametric inequality.** Suppose $x, y, x+y$ are all nonzero, and without loss $m = v_p(x) \leq n = v_p(y)$. Write $x = p^m u$, $y = p^n w = p^m(p^{n-m}w)$ where $u = \tfrac ab$, $w = \tfrac cd$ have $v_p = 0$. Then
> $$x + y = p^m\big(u + p^{n-m}w\big).$$
> The bracket $u + p^{n-m}w = \tfrac{ad + p^{n-m}cb}{bd}$ has denominator $bd$ with $p \nmid bd$, so it lies in $\mathbb{Z}_{(p)}$, i.e. $v_p(u + p^{n-m}w) \geq 0$. Therefore $v_p(x+y) = m + v_p(u + p^{n-m}w) \geq m = \min\{v_p(x), v_p(y)\}$. With $v_p(0) = \infty$ the inequality holds in all cases.

**Step 2: the valuation ring is $\mathbb{Z}_{(p)}$.**

$A_{v_p} = \{x \in \mathbb{Q} : v_p(x) \geq 0\} \cup \{0\} = \mathbb{Z}_{(p)}$.

> [!note]- Derivation
> An element $x = p^n\tfrac ab$ (with $p\nmid a,b$) has $v_p(x) \geq 0$ iff $n \geq 0$ iff there is no negative power of $p$, iff $p \nmid b$ when $x$ is written in lowest terms. So
> $$\{x : v_p(x) \geq 0\} = \Big\{\tfrac ab : p \nmid b\Big\} = \mathbb{Z}_{(p)}.$$
> Conversely every element of $\mathbb{Z}_{(p)}$ has $p\nmid b$, hence $v_p \geq 0$. So the valuation ring of $v_p$ is exactly $\mathbb{Z}_{(p)}$, and $\operatorname{Frac}(\mathbb{Z}_{(p)}) = \mathbb{Q}$.

**Step 3: $\mathbb{Z}_{(p)}$ is a DVR with the stated data.**

Since $\mathbb{Z}_{(p)} = A_{v_p}$ is the valuation ring of a discrete valuation on its own fraction field $\mathbb{Q}$, it is a DVR by definition. Its uniformizer is $\pi = p$, maximal ideal $(p)$, residue field $\mathbb{F}_p$.

> [!note]- Derivation
> By definition, an integral domain that is the valuation ring of a discrete valuation on its fraction field *is* a DVR — and Steps 1–2 established exactly that. The DVR data:
> - **Units:** $\mathbb{Z}_{(p)}^\times = \{v_p = 0\} = \{\tfrac ab : p\nmid a, p\nmid b\}$.
> - **Uniformizer:** $v_p(p) = 1$, so $\pi = p$ is a uniformizer, and every nonzero $x = p^{v_p(x)}u$ with $u$ a unit.
> - **Maximal ideal:** $\mathfrak{m} = \{v_p \geq 1\} = p\mathbb{Z}_{(p)} = (p)$, principal.
> - **Ideals:** the nonzero ideals are $(p^n) = \{v_p \geq n\}$ for $n \geq 0$, the single descending chain $\mathbb{Z}_{(p)} \supsetneq (p) \supsetneq (p^2) \supsetneq \cdots$.
> - **Residue field:** $\mathbb{Z}_{(p)}/(p) \cong \mathbb{Z}/p\mathbb{Z} = \mathbb{F}_p$ (the localization map $\mathbb{Z}\to\mathbb{Z}_{(p)}/(p)$ is surjective with kernel $(p)$).

> [!note]- Complete formal solution
> **Claim.** $\mathbb{Z}_{(p)}$ is a DVR with valuation $v_p$, uniformizer $p$, maximal ideal $(p)$, residue field $\mathbb{F}_p$.
>
> Define $v_p : \mathbb{Q}^\times \to \mathbb{Z}$ by $v_p(p^n\tfrac ab) = n$ for $p\nmid a, b$, and $v_p(0) = \infty$. By unique factorization in $\mathbb{Z}$ this is well-defined; it is surjective ($v_p(p^n) = n$); it is a homomorphism ($v_p(xy) = v_p(x) + v_p(y)$, using that $p$ prime gives $p\nmid ac, bd$); and it satisfies the ultrametric inequality (factoring out $p^{\min}$ from a sum leaves a $p$-integral bracket). So $v_p$ is a discrete valuation on $\mathbb{Q}$.
>
> Its valuation ring is $\{x : v_p(x) \geq 0\} = \{\tfrac ab : p\nmid b\} = \mathbb{Z}_{(p)}$. Hence $\mathbb{Z}_{(p)}$ is the valuation ring of a discrete valuation on its fraction field $\mathbb{Q}$, so it is a DVR. The units are $\{v_p = 0\}$, the uniformizer is $p$ (as $v_p(p) = 1$), the maximal ideal is $\{v_p \geq 1\} = (p)$ (principal), the nonzero ideals are $(p^n)$, and the residue field is $\mathbb{Z}_{(p)}/(p) \cong \mathbb{F}_p$. $\blacksquare$

---

# Key Takeaways

**The $p$-adic valuation is the prototype every DVR is modeled on, and recognizing it is the fastest route to "this is a DVR".** The entire abstract theory of discrete valuations is the distillation of one concrete object: "count the power of $p$". When a problem hands you a local ring whose elements have a visible notion of "order" — power of $p$, order of vanishing, degree of a pole, lowest-term exponent — the reflex should be to *define the valuation by that order* and check the three axioms, rather than reaching for the [[Thm - Characterization of Discrete Valuation Rings|characterization theorem]]. The axioms are cheap to verify because they are exactly the properties unique factorization already gives you: multiplicativity is "powers add", and the ultrametric inequality is "factor out the minimum". This is the most direct of the five equivalent DVR conditions, and it is available precisely when the valuation is concrete.

**The ultrametric inequality is the one non-multiplicative axiom, and "factor out the minimum power" is its universal proof.** Multiplicativity of a valuation is routine — it just tracks how a single prime distributes over products. The subtle axiom is the one about *sums*, and it is subtle because addition can do unexpected things (cancellation can raise the valuation, as $p + (-p) = 0$ shows). The mechanism that always works is to factor the smaller power of $p$ out of the sum: $x + y = p^{\min}(\cdots)$ where the bracket is integral, forcing $v_p(x+y) \geq \min$. This same move proves the ultrametric inequality for order-of-vanishing on curves, for the degree valuation on Laurent series, and for every concrete valuation; it is worth internalizing as "the valuation of a sum is at least the min, proved by pulling out the min". The inequality is strict exactly when the two minimal terms cancel.

**A DVR is what you get by localizing a Dedekind domain at one prime, and $\mathbb{Z}_{(p)}$ is that operation applied to $\mathbb{Z}$.** This exercise is the smallest instance of the chapter's central reduction: $\mathbb{Z}$ is a Dedekind domain with infinitely many primes, and localizing at one of them isolates the arithmetic at that single prime, producing a DVR. The valuation $v_p$ that emerges is exactly the local exponent that, reassembled over all primes, gives the factorization of any ideal — so this computation is the local building block of [[Thm - A Dedekind Domain has Unique Factorization of Ideals|unique factorization of ideals]]. When you later compute the factorization of $(6)$ in $\mathbb{Z}[\sqrt{-5}]$ (see [[Ex - Unique factorization of ideals in Z[sqrt -5] into primes]]), you will be doing this same $v_p$ computation at each prime of that Dedekind domain. The general statement that localizing a Dedekind domain gives a DVR is [[Thm - Localization of a Dedekind Domain is a DVR]]; this exercise is its archetype.
