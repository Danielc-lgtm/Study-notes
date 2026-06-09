---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Discrete Valuation and Valuation Ring"
  - "Def - Principal Ideal Domain"
  - "Def - Local Ring and Residue Field"
  - "Thm - Characterization of Discrete Valuation Rings"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $(A, \mathfrak{m})$ be a Noetherian local domain of dimension $1$. Prove the chain of implications

$$\mathfrak{m} \text{ principal} \ \Longrightarrow\ \text{every nonzero ideal is a power of } \mathfrak{m} \ \Longrightarrow\ \exists\,\pi:\text{every nonzero ideal is } (\pi^n) \ \Longrightarrow\ A \text{ is a DVR},$$

and conclude that **a discrete valuation ring is exactly a local principal ideal domain that is not a field** — equivalently, a local PID with a unique nonzero prime. (This is parts (3)$\Rightarrow$(4)$\Rightarrow$(5)$\Rightarrow$(1) of the [[Thm - Characterization of Discrete Valuation Rings|DVR characterization]]; it is ES4 Q17(a)(i).)

**Recall:**

![[Def - Discrete Valuation and Valuation Ring#The Definition]]

A [[Def - Local Ring and Residue Field|local ring]] $(A, \mathfrak{m})$ has a unique maximal ideal $\mathfrak{m}$. "Dimension $1$" means $\operatorname{Spec} A = \{(0), \mathfrak{m}\}$ with $\mathfrak{m} \neq (0)$: the only primes are $(0)$ and the maximal ideal, with nothing between.

A [[Def - Principal Ideal Domain|principal ideal domain]] is an integral domain in which every ideal is principal. A **uniformizer** is a generator $\pi$ of $\mathfrak{m}$.

The supporting fact used repeatedly: in a Noetherian ring, every ideal contains a power of its radical; here, for any nonzero proper ideal $\mathfrak{a}$, $\sqrt{\mathfrak{a}} = \mathfrak{m}$ (the only prime over a nonzero proper ideal in a one-dimensional local domain), so $\mathfrak{m}^t \subseteq \mathfrak{a}$ for some $t$.

---

# Convergent Strategy

**Problem class.** This is a *forge-the-equivalence* problem: three implications that together upgrade "the maximal ideal needs one generator" to the full DVR structure. As the [[Commutative Algebra XIII — Dedekind Domains and DVRs#Problem-Solving Strategy|topic strategy]] notes, once $\mathfrak{m}$ is principal the entire ideal theory is forced, and the work is to show every ideal is squeezed onto a power of $\mathfrak{m}$.

**Assumption pattern.** Two structural facts drive everything: (i) dimension $1$ means $\sqrt{\mathfrak{a}} = \mathfrak{m}$ for any nonzero proper $\mathfrak{a}$, so $\mathfrak{m}^t \subseteq \mathfrak{a}$ (Noetherian); and (ii) $\mathfrak{m} = (\pi)$ principal means $\mathfrak{m}^n = (\pi^n)$, so the powers of $\mathfrak{m}$ are exactly the principal ideals $(\pi^n)$. The recognizable trigger for "every ideal is a power of $\mathfrak{m}$" is that an ideal is sandwiched $\mathfrak{m}^t \subseteq \mathfrak{a} \subseteq \mathfrak{m}^s$ between consecutive powers, and you must pin which power it equals.

**Theorem routing.** The route is: (3)$\Rightarrow$(4) — use $\sqrt{\mathfrak{a}} = \mathfrak{m}$ and a "find an element of exact order" argument to show $\mathfrak{a} = \mathfrak{m}^t$; (4)$\Rightarrow$(5) — extract $\pi$ from $\mathfrak{m}\setminus\mathfrak{m}^2$ (which is nonempty by Nakayama) so $(\pi) = \mathfrak{m}$ and every power is principal; (5)$\Rightarrow$(1) — define $v(a) = n$ for $(a) = (\pi^n)$, check it is a valuation, recover $A = A_v$. The final identification "DVR = local PID, not a field" is then a packaging of (5): all ideals principal and one nonzero prime.

**Key decision point.** The crux of (3)$\Rightarrow$(4) is the **"element of exact order $t$"** move: given $\mathfrak{a} \subseteq \mathfrak{m}^t$ with $t$ maximal, pick $y \in \mathfrak{a}\setminus\mathfrak{m}^{t+1}$, write $y = a\pi^t$, and argue $a \notin \mathfrak{m}$ (else $y \in \mathfrak{m}^{t+1}$), so $a$ is a unit and $\pi^t \in \mathfrak{a}$. This is non-obvious because it is tempting to try to generate $\mathfrak{a}$ by many elements; the insight is that *one* element of exact order $t$ already forces $\mathfrak{a} = (\pi^t)$. The other decision point is recognizing **Nakayama** as the source of $\mathfrak{m} \neq \mathfrak{m}^2$, which is what guarantees a uniformizer exists.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra XIII — Dedekind Domains and DVRs#Legal Operations|the topic page's Legal Operations]]:

1. **Use the radical to find the power (operation 9).** Since $\sqrt{\mathfrak{a}} = \mathfrak{m}$ in a one-dimensional local domain, $\mathfrak{m}^t \subseteq \mathfrak{a}$, sandwiching $\mathfrak{a}$ between powers of $\mathfrak{m}$.

2. **Detect a uniformizer via $\mathfrak{m} \neq \mathfrak{m}^2$ (operation 7).** Nakayama gives $\mathfrak{m} \supsetneq \mathfrak{m}^2$, so $\pi \in \mathfrak{m}\setminus\mathfrak{m}^2$ generates $\mathfrak{m}$.

3. **Read off valuation arithmetic (operation 1).** Define $v(a) = n$ for $(a) = (\pi^n)$ and verify multiplicativity and the ultrametric inequality from the ideal structure.

---

# Hints

> [!note]- Hint 1
> Every implication is about *ideals*, and the governing fact is that in a one-dimensional local domain, the radical of any nonzero proper ideal is forced to be $\mathfrak{m}$ — there is no other prime it could be. Combined with Noetherian, this gives $\mathfrak{m}^t \subseteq \mathfrak{a}$, so every ideal contains a power of $\mathfrak{m}$.

> [!note]- Hint 2
> For (3)$\Rightarrow$(4): with $\mathfrak{m} = (\pi)$, find the *largest* $t$ with $\mathfrak{a} \subseteq \mathfrak{m}^t = (\pi^t)$. Then there is $y \in \mathfrak{a}$ not in $\mathfrak{m}^{t+1}$. Write $y = a\pi^t$. Why must $a$ be a unit?

> [!note]- Hint 3
> If $a \in \mathfrak{m}$, then $y = a\pi^t \in \mathfrak{m}\cdot\mathfrak{m}^t = \mathfrak{m}^{t+1}$, contradicting the choice of $y$. So $a \notin \mathfrak{m}$, hence (local ring) $a$ is a unit, so $\pi^t = a^{-1}y \in \mathfrak{a}$. Now $(\pi^t) \subseteq \mathfrak{a} \subseteq (\pi^t)$.

> [!note]- Hint 4
> For (4)$\Rightarrow$(5): Nakayama gives $\mathfrak{m} \neq \mathfrak{m}^2$, so pick $\pi \in \mathfrak{m}\setminus\mathfrak{m}^2$; the ideal $(\pi)$ is some power $\mathfrak{m}^r$ by (4), and $\pi \notin \mathfrak{m}^2$ forces $r = 1$. For (5)$\Rightarrow$(1): define $v(a) = n$ where $(a) = (\pi^n)$, extend to $\operatorname{Frac}(A)$, and check the valuation axioms; then $A = \{v \geq 0\}$.

---

# Solution

The proof walks the three implications. Step 1 (3)$\Rightarrow$(4) squeezes any ideal between consecutive powers of $\mathfrak{m}$ and uses an element of exact order to pin it to a single power. Step 2 (4)$\Rightarrow$(5) extracts a uniformizer from $\mathfrak{m}\setminus\mathfrak{m}^2$ via Nakayama. Step 3 (5)$\Rightarrow$(1) builds the valuation from the exponents. The final packaging identifies a DVR as a local PID that is not a field.

**Step 1: (3) $\Rightarrow$ (4) — every nonzero ideal is a power of $\mathfrak{m}$.**

If $\mathfrak{m} = (\pi)$, then every nonzero ideal $\mathfrak{a}$ equals $\mathfrak{m}^t = (\pi^t)$ for a unique $t \geq 0$.

> [!note]- Derivation
> Take $\mathfrak{a}$ a nonzero proper ideal (the cases $\mathfrak{a} = A$, giving $t = 0$, and $\mathfrak{a} = 0$ are trivial). Since $\operatorname{Spec} A = \{(0), \mathfrak{m}\}$ and $\mathfrak{a} \neq 0$, the only prime containing $\mathfrak{a}$ is $\mathfrak{m}$, so $\sqrt{\mathfrak{a}} = \mathfrak{m}$. As $A$ is Noetherian, $\mathfrak{a}$ contains a power of its radical: $\mathfrak{m}^\ell \subseteq \mathfrak{a}$ for some $\ell$. Thus $\mathfrak{a}$ is bounded $\mathfrak{m}^\ell \subseteq \mathfrak{a} \subseteq \mathfrak{m}$.
>
> Let $t$ be the largest integer with $\mathfrak{a} \subseteq \mathfrak{m}^t$ (it exists, $1 \leq t \leq \ell$, since the powers $\mathfrak{m}^n = (\pi^n)$ strictly decrease — if $(\pi^{n+1}) = (\pi^n)$ then $\pi^n(1 - c\pi) = 0$, forcing $\pi$ a unit, absurd). By maximality, $\mathfrak{a} \not\subseteq \mathfrak{m}^{t+1}$, so choose $y \in \mathfrak{a}\setminus\mathfrak{m}^{t+1}$.
>
> Since $\mathfrak{m}^t = (\pi^t)$, write $y = a\pi^t$ for some $a \in A$. If $a \in \mathfrak{m}$, then $y = a\pi^t \in \mathfrak{m}\cdot(\pi^t) = \mathfrak{m}^{t+1}$, contradicting $y \notin \mathfrak{m}^{t+1}$. So $a \notin \mathfrak{m}$, and as $A$ is local, $a$ is a unit. Then $\pi^t = a^{-1}y \in \mathfrak{a}$, so $(\pi^t) \subseteq \mathfrak{a}$. Combined with $\mathfrak{a} \subseteq \mathfrak{m}^t = (\pi^t)$, this gives $\mathfrak{a} = (\pi^t) = \mathfrak{m}^t$. Uniqueness of $t$ is the strict decrease of the powers.

**Step 2: (4) $\Rightarrow$ (5) — a single $\pi$ works for all ideals.**

There exists $\pi \in A$ (namely any element of $\mathfrak{m}\setminus\mathfrak{m}^2$) such that every nonzero ideal is $(\pi^n)$.

> [!note]- Derivation
> By [[Commutative Algebra V — Nakayama's Lemma|Nakayama's lemma]], $\mathfrak{m} \neq \mathfrak{m}^2$: if $\mathfrak{m} = \mathfrak{m}^2$ then $\mathfrak{m} = 0$ (Nakayama applied to the finitely generated module $\mathfrak{m}$), contradicting dimension $1$. So $\mathfrak{m}\setminus\mathfrak{m}^2 \neq \varnothing$; pick $\pi$ in it.
>
> By (4), the ideal $(\pi)$ is a power $\mathfrak{m}^r$ for some $r \geq 1$. Since $\pi \in \mathfrak{m} = \mathfrak{m}^1$, we have $r \geq 1$; since $\pi \notin \mathfrak{m}^2$, we have $r \leq 1$. Hence $r = 1$ and $(\pi) = \mathfrak{m}$. Then $\mathfrak{m}^n = (\pi)^n = (\pi^n)$, and by (4) every nonzero ideal is some $\mathfrak{m}^n = (\pi^n)$. This is (5).

**Step 3: (5) $\Rightarrow$ (1) — build the valuation.**

Defining $v(a) = n$ where $(a) = (\pi^n)$, extended to $K = \operatorname{Frac}(A)$ by $v(a/b) = v(a) - v(b)$, gives a discrete valuation with $A = A_v$. Hence $A$ is a DVR.

> [!note]- Derivation
> **Strict decrease.** As in Step 1, $(\pi^{n+1}) = (\pi^n)$ would make $\pi$ a unit; so the chain $A \supsetneq (\pi) \supsetneq (\pi^2) \supsetneq \cdots$ is strictly decreasing, and for each $0 \neq a \in A$ the ideal $(a)$ equals $(\pi^n)$ for a unique $n = v(a) \geq 0$.
>
> **Well-defined on $K$.** For $a/b \in K^\times$ set $v(a/b) = v(a) - v(b)$. If $a/b = a'/b'$ then $ab' = a'b$, and additivity of $v$ on $A$ (from $(\pi^m)(\pi^n) = (\pi^{m+n})$) gives $v(a) + v(b') = v(a') + v(b)$, so $v(a) - v(b) = v(a') - v(b')$.
>
> **Valuation axioms.** $v$ is surjective onto $\mathbb{Z}$ ($v(1/\pi^n) = -n$). It is a homomorphism: $v(xy) = v(x) + v(y)$ since multiplying principal ideals adds exponents. Ultrametric inequality: if $v(x) = m \leq n = v(y)$, write $x = u\pi^m$, $y = w\pi^n$ with $u, w$ units, so $x + y = \pi^m(u + w\pi^{n-m})$ with $u + w\pi^{n-m} \in A$, giving $v(x+y) \geq m = \min$.
>
> **Valuation ring.** $A_v = \{x \in K : v(x) \geq 0\}$; for $x = a/b$, $v(x) \geq 0 \iff v(a) \geq v(b) \iff b \mid a$ in the divisibility sense $\iff x \in A$. So $A_v = A$. Therefore $A$ is the valuation ring of a discrete valuation on its fraction field — a DVR.

**Step 4: packaging — a DVR is a local PID that is not a field.**

A DVR is an integral domain in which every ideal is principal (so a PID), which is local (one maximal ideal), and which is not a field (it has the nonzero maximal ideal $\mathfrak{m}$).

> [!note]- Derivation
> By (5), every nonzero ideal of $A$ is $(\pi^n)$ — principal — and the zero ideal is $(0)$, principal; so $A$ is a [[Def - Principal Ideal Domain|PID]]. It is local with unique maximal ideal $\mathfrak{m} = (\pi)$, and it is not a field since $\mathfrak{m} \neq 0$ (a field has no nonzero maximal ideal). Conversely a local PID that is not a field is a Noetherian (PIDs are Noetherian) local domain whose maximal ideal is principal (every ideal is), of dimension $1$ (a nonzero prime in a PID is maximal, and there is exactly one), so it is a DVR by condition (3). Hence **DVR $=$ local PID $\neq$ field**.

> [!note]- Complete formal solution
> Let $(A, \mathfrak{m})$ be a Noetherian local domain of dimension $1$ with $\mathfrak{m} = (\pi)$.
>
> **(3)$\Rightarrow$(4).** For a nonzero proper ideal $\mathfrak{a}$, $\sqrt{\mathfrak{a}} = \mathfrak{m}$ (only prime over it), so $\mathfrak{m}^\ell \subseteq \mathfrak{a}$ for some $\ell$ (Noetherian). Let $t$ be maximal with $\mathfrak{a} \subseteq \mathfrak{m}^t = (\pi^t)$ (the powers strictly decrease). Pick $y \in \mathfrak{a}\setminus\mathfrak{m}^{t+1}$, write $y = a\pi^t$; $a \notin \mathfrak{m}$ (else $y \in \mathfrak{m}^{t+1}$), so $a$ is a unit, $\pi^t = a^{-1}y \in \mathfrak{a}$, and $\mathfrak{a} = (\pi^t) = \mathfrak{m}^t$.
>
> **(4)$\Rightarrow$(5).** Nakayama gives $\mathfrak{m} \neq \mathfrak{m}^2$; pick $\pi \in \mathfrak{m}\setminus\mathfrak{m}^2$. Then $(\pi) = \mathfrak{m}^r$ with $r = 1$ (since $\pi \in \mathfrak{m}$, $\pi \notin \mathfrak{m}^2$), so $(\pi) = \mathfrak{m}$ and every nonzero ideal is $\mathfrak{m}^n = (\pi^n)$.
>
> **(5)$\Rightarrow$(1).** Define $v(a) = n$ for $(a) = (\pi^n)$, extend by $v(a/b) = v(a) - v(b)$. This is a well-defined surjective homomorphism $K^\times \to \mathbb{Z}$ satisfying $v(x+y) \geq \min\{v(x), v(y)\}$ (factor out $\pi^{\min}$), and $A_v = A$. So $A$ is a DVR.
>
> **Packaging.** Every ideal of $A$ is principal, $A$ is local with $\mathfrak{m} = (\pi) \neq 0$, so $A$ is a local PID that is not a field; and conversely such a ring is a DVR by condition (3). $\blacksquare$

---

# Key Takeaways

**"Every ideal is a power of $\mathfrak{m}$" is proved by squeezing the ideal between consecutive powers and finding one element of exact order.** The central technique of Step 1 is universal in one-dimensional local rings: any nonzero ideal $\mathfrak{a}$ is automatically sandwiched $\mathfrak{m}^\ell \subseteq \mathfrak{a} \subseteq \mathfrak{m}^t$ because its radical is $\mathfrak{m}$, and to pin down *which* power it equals, you produce a single element $y \in \mathfrak{a}\setminus\mathfrak{m}^{t+1}$ — an element "of exact order $t$" — and show it generates $\mathfrak{m}^t$ inside $\mathfrak{a}$. The trigger to recognize: whenever you must identify an ideal in a ring with a single descending chain of ideals, do not try to compute many generators; find one element of the right order and let unit-times-power finish it. This is the same logic by which one computes the exponent in a prime factorization by valuation.

**Nakayama is the hidden source of the uniformizer: $\mathfrak{m} \neq \mathfrak{m}^2$ is what guarantees a single generator exists.** It is easy to take for granted that $\mathfrak{m}$ has an element not in $\mathfrak{m}^2$, but that is precisely [[Commutative Algebra V — Nakayama's Lemma|Nakayama's lemma]]: if $\mathfrak{m} = \mathfrak{m}^2$ then $\mathfrak{m} = 0$. This strict drop is what makes $\mathfrak{m}\setminus\mathfrak{m}^2$ nonempty and lets you pick a uniformizer; the same fact, read through the cotangent space, is the statement $\dim_k\mathfrak{m}/\mathfrak{m}^2 = 1$. Whenever you need to "extract a single generator of a maximal ideal", the reflex is "Nakayama gives me $\mathfrak{m} \neq \mathfrak{m}^2$, so any $\pi \in \mathfrak{m}\setminus\mathfrak{m}^2$ works" — and in a one-dimensional local ring this $\pi$ is automatically a generator.

**The operational identity "DVR = local PID that is not a field" is the fastest recognition criterion.** While the [[Thm - Characterization of Discrete Valuation Rings|characterization theorem]] lists five equivalent conditions, the most memorable packaging is this one: a DVR is a principal ideal domain that happens to be local and not a field. This is the form to carry into problems, because PIDs are familiar and "local" plus "not a field" are quick to check. It explains why $\mathbb{Z}_{(p)}$ and $k[[T]]$ are DVRs (local PIDs) while $\mathbb{Z}$ and $k[T]$ are not (PIDs with many maximal ideals) — the failure is exactly non-locality. It also explains why the structure theorem for modules over a PID specializes to DVRs, giving the clean classification of finitely generated modules over a DVR as $A^r \oplus \bigoplus A/(\pi^{n_i})$. When a problem asks you to recognize or exploit a DVR, "local PID, not a field" is the diagnostic to apply first.
