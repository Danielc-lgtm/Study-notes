---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Discrete Valuation and Valuation Ring"
  - "Def - Noetherian Ring"
  - "Def - Local Ring and Residue Field"
  - "Def - Integral Closure and Normal Domain"
  - "Def - Krull Dimension and Height"
  - "Def - Radical of an Ideal and the Nilradical"
tags: [algebra, commutative-algebra]
---

# Notation

Let $(A, \mathfrak{m})$ be a Noetherian [[Def - Local Ring and Residue Field|local]] integral [[Def - Integral Domain|domain]] of [[Def - Krull Dimension and Height|Krull dimension]] $1$, with fraction field $K = \operatorname{Frac}(A)$ and residue field $k = A/\mathfrak{m}$. Equivalently, $\operatorname{Spec} A = \{(0), \mathfrak{m}\}$ with $\mathfrak{m} \neq (0)$. A **uniformizer** is an element $\pi$ generating $\mathfrak{m}$. We write $\mathfrak{m}^n$ for the $n$-th power ideal, $\sqrt{\mathfrak{a}}$ for the [[Def - Radical of an Ideal and the Nilradical|radical]], and $\dim_k \mathfrak{m}/\mathfrak{m}^2$ for the dimension of the cotangent space as a $k$-vector space. The full registry is on [[Commutative Algebra XIII — Dedekind Domains and DVRs]].

---

# Statement

> **Theorem (characterization of DVRs).** Let $(A, \mathfrak{m})$ be a Noetherian local integral domain of dimension $1$. The following are equivalent:
>
> 1. $A$ is a [[Def - Discrete Valuation and Valuation Ring|discrete valuation ring]].
> 2. $A$ is [[Def - Integral Closure and Normal Domain|integrally closed]] in $K = \operatorname{Frac}(A)$.
> 3. $\mathfrak{m}$ is a principal ideal.
> 4. Every nonzero ideal of $A$ is a power of $\mathfrak{m}$.
> 5. There exists $\pi \in A$ such that every nonzero ideal of $A$ is $(\pi^n)$ for some $n \geq 0$.
> 6. $\dim_k \mathfrak{m}/\mathfrak{m}^2 = 1$, where $k = A/\mathfrak{m}$.

> **Remark.** Conditions (3), (5), and (6) all say "$\mathfrak{m}$ needs exactly one generator": (3) directly, (5) names the generator $\pi$ and tracks its powers, and (6) reads the number of generators off the cotangent space via Nakayama. The substantive content is that these are equivalent to the *a priori* much stronger (1) and to the *a priori* unrelated (2). The proof runs the cycle $(1)\Rightarrow(2)\Rightarrow(3)\Rightarrow(4)\Rightarrow(5)\Rightarrow(1)$, with (6) attached to (3) by Nakayama.

---

# Motivation

A discrete valuation ring is, on its face, a ring carrying *extra structure*: a chosen valuation $v$ measuring divisibility. The point of this theorem is that the extra structure is an illusion — the valuation is forced by the ring, and "DVR" is an intrinsic, structural property detectable in five different ways that mention no valuation at all. This is what makes DVRs usable: you almost never produce a valuation by hand; you recognize a DVR by checking that its maximal ideal is principal, or that it is integrally closed, or that its cotangent space is one-dimensional, and the theorem then hands you the valuation for free.

The theorem also explains *why integral-closedness is the load-bearing hypothesis in the definition of a Dedekind domain*. Three of the conditions — Noetherian, local, dimension $1$ — are assumed throughout and are easy to arrange. The whole question of whether such a ring is "as nice as possible" comes down to a single fourth condition, and the theorem says that condition can be phrased as integral-closedness (an algebraic-closure property), or as principality of $\mathfrak{m}$ (an ideal-generation property), or as smoothness $\dim_k\mathfrak{m}/\mathfrak{m}^2 = 1$ (a geometric, cotangent property), and these are all the same. So when [[Def - Dedekind Domain|Dedekind domain]] is defined as "Noetherian, integrally closed, dimension $1$", this theorem is what guarantees that the localization at each prime is a DVR — that the global normality condition is exactly the local smoothness condition.

Finally, the theorem is the reason the whole subject is *computable*. Once you know a one-dimensional local domain is a DVR, condition (5) tells you its entire ideal theory in one line — the ideals are $A \supsetneq (\pi) \supsetneq (\pi^2) \supsetneq \cdots$ and nothing else — and every ideal question becomes arithmetic of exponents. The theorem converts a recognition problem into a computational windfall.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "Noetherian local domain of dimension $1$ satisfying one of (1)–(6)". The art is recognizing when one of the equivalent conditions is secretly available.

The first disguised source is **a localization of a Dedekind domain at a prime**. The property $B$ is "$A = R_\mathfrak{p}$ for a Dedekind domain $R$ and nonzero prime $\mathfrak{p}$". The bridge to condition (2): $R$ is integrally closed, integral-closedness is a local property, so $R_\mathfrak{p}$ is integrally closed; and it is a Noetherian local domain of dimension $\operatorname{ht}\mathfrak{p} = 1$. The non-obvious part is that a *global* normality hypothesis on $R$ delivers a *local* DVR at every prime. *Example problem:* show $A_\mathfrak{p}$ is a DVR for any prime of $\mathbb{Z}[\sqrt{-5}]$ — used in [[Thm - A Dedekind Domain has Unique Factorization of Ideals|unique factorization of ideals]].

The second disguised source is **a one-dimensional local domain whose maximal ideal you can generate with one element**. The property $B$ is "$\mathfrak{m} = (\pi)$ for some explicit $\pi$" — condition (3). The bridge is immediate, but the value is that producing a single generator is often easy in concrete rings (in $k[T]_{(T-a)}$, take $\pi = T - a$). The non-obviousness is that *one* generator is enough; you need not exhibit the valuation. *Example problem:* prove $k[[T]]$ is a DVR by noting $\mathfrak{m} = (T)$.

The third disguised source is **a smooth point on a curve**. The property $B$ is "the local ring at $p$ has $\dim_k\mathfrak{m}/\mathfrak{m}^2 = 1$" — condition (6), the algebraic meaning of nonsingularity. The bridge to (3) is Nakayama: a one-dimensional cotangent space lifts to a single generator of $\mathfrak{m}$. The non-obviousness is that a *geometric* smoothness check (tangent space has the right dimension) certifies a *purely algebraic* DVR structure. *Example problem:* verify the local ring of $y^2 = x^3 + x$ at the origin is a DVR by computing $\mathfrak{m}/\mathfrak{m}^2$.

The fourth disguised source is **a UFD that is local of dimension $1$**. The property $B$ is "$A$ is a UFD" — and a UFD is integrally closed, giving condition (2). The non-obviousness: factorization of elements implies integral-closedness implies DVR. *Example problem:* any localization of a PID at a nonzero prime.

**Targets (Output Amplification)**

The conclusion is "$A$ is a DVR" with all six equivalent faces available.

Combine "DVR" with **the explicit ideal list of condition (5)**. Knowing every nonzero ideal is $(\pi^n)$ turns *any* statement about ideals of $A$ into a statement about non-negative integers: containment is $\geq$, products add exponents, intersection is max, sum is min. The further result $E$: the ideal lattice of a DVR is $(\mathbb{Z}_{\geq 0}, \geq)$, so $A$ is automatically a PID and a UFD. This is nonobvious because it deduces global ring structure (PID) from a recognition condition.

Combine "DVR" with **a finite module $M$ over $A$**. Over a DVR every finitely generated module is $A^r \oplus \bigoplus A/(\pi^{n_i})$ — the structure theorem for modules over a PID specializes, since a DVR is a *local* PID. The further result $E$: the classification of finitely generated modules over a DVR is as clean as over a field plus a single nilpotent. Nonobvious because it imports the entire Smith-normal-form theory the instant you recognize a DVR.

Combine "DVR" with **integral closure of the fraction field's order function**. Condition (1) gives a valuation $v$, and then $v$ extends the *order of vanishing* to all of $K$, including poles ($v < 0$). The further result $E$: $A = \{f : v(f) \geq 0\}$ recovers the ring as "functions without poles at the point", the geometric viewpoint that powers divisor theory. Nonobvious because it turns a ring-recognition into a function-theory dictionary.

---

# Why Is It True

The intuition is that all six conditions are saying **"$\mathfrak{m}$ needs exactly one generator, and that generator is a coordinate measuring everything"** — and the only real work is showing that the seemingly-weaker conditions force a single generator to exist.

**The bolded mechanism:** **in a one-dimensional Noetherian local domain, the radical of any nonzero proper ideal is $\mathfrak{m}$ (there is nowhere else for it to be), so every ideal is squeezed between consecutive powers of $\mathfrak{m}$ — and the *one* thing that can go wrong is $\mathfrak{m}$ needing two generators, which is exactly the failure of integral-closedness.**

Walk the cycle. **(1) $\Rightarrow$ (2):** a valuation ring is integrally closed because if $x \in K$ satisfies a monic equation over $A$ with coefficients of value $\geq 0$, then $v(x) < 0$ leads to a numerical contradiction: the leading term $x^n$ has value $nv(x)$, strictly more negative than any lower term $a_i x^{n-i}$ (whose value is $\geq (n-i)v(x) > nv(x)$ since $v(a_i)\geq 0$), so the equation $x^n = -\sum a_i x^{n-i}$ cannot balance. Hence $v(x) \geq 0$ and $x \in A$. The valuation makes integral-closedness automatic because it gives a numerical handle on "size".

**(2) $\Rightarrow$ (3)** is the heart. We want a single generator of $\mathfrak{m}$, i.e. an $x \in K$ with $x^{-1}\mathfrak{m} = A$. The strategy is to find $x = b/a$ that *pushes $\mathfrak{m}$ just outside itself*: $x^{-1}\mathfrak{m} \subseteq A$ (so it is an ideal) but $x^{-1}\mathfrak{m} \not\subseteq \mathfrak{m}$ (so, being an ideal not in the unique maximal ideal, it is all of $A$). The first condition is arranged by taking $a \in \mathfrak{m}$ and $b \in \mathfrak{m}^{t-1}\setminus Aa$ where $\mathfrak{m}^t \subseteq Aa$ with $t$ minimal — then $bm \in \mathfrak{m}^t \subseteq Aa$ for all $m\in\mathfrak m$, so $(b/a)\mathfrak{m} \subseteq A$. The second condition, $x^{-1}\mathfrak{m} \not\subseteq \mathfrak{m}$, is where integral-closedness enters: if $x^{-1}\mathfrak{m} \subseteq \mathfrak{m}$, then $\mathfrak{m}$ would be a faithful module over $A[x^{-1}]$, finitely generated over $A$, forcing $x^{-1}$ integral over $A$ — but $x^{-1} = b/a$ is *not* in $A$ (that is how $b$ was chosen, $b \notin Aa$), and integral-closedness says not-in-$A$ means not-integral. So the escape happens, and $\mathfrak{m} = (x)$ is principal. The whole argument is "manufacture a uniformizer by pushing $\mathfrak{m}$ out of itself, using normality to guarantee the push succeeds".

**(3) $\Rightarrow$ (4) $\Rightarrow$ (5) $\Rightarrow$ (1)** is then bookkeeping. Once $\mathfrak{m} = (\pi)$, any nonzero ideal $\mathfrak{a}$ has $\sqrt{\mathfrak{a}} = \mathfrak{m}$ (nowhere else to be, by dimension $1$), so $\mathfrak{m}^t \subseteq \mathfrak{a}$ for some $t$; squeezing $\mathfrak{a}$ between $\mathfrak{m}^t$ and the largest $\mathfrak{m}^s \supseteq \mathfrak{a}$ and using $\mathfrak{m}^s = (\pi^s)$ shows $\mathfrak{a} = (\pi^s)$ exactly. So every ideal is $(\pi^n)$, the chain is strictly decreasing (Nakayama: $(\pi^{n+1}) = (\pi^n)$ would force $\mathfrak{m}^n = 0$), and defining $v(a)$ to be the $n$ with $(a) = (\pi^n)$ produces the valuation, exhibiting $A$ as a DVR.

**(3) $\iff$ (6)** is pure Nakayama: $\dim_k\mathfrak{m}/\mathfrak{m}^2$ is the minimal number of generators of $\mathfrak{m}$, so it is $1$ iff $\mathfrak{m}$ is principal. The cotangent space *counts the generators*, and one generator is the whole condition.

---

# What Makes This Hard

The single hard step is **(2) $\Rightarrow$ (3)**: manufacturing a uniformizer out of nothing but integral-closedness. Most people get stuck because there is no obvious element to try; the non-obvious move is to look for $x = b/a$ in the *fraction field* (not in $A$) chosen so that $x^{-1}\mathfrak{m}$ escapes $\mathfrak{m}$, and to recognize that "$x^{-1}\mathfrak{m} \subseteq \mathfrak{m}$ would make $x^{-1}$ integral" is the lever that integral-closedness pulls. The common error is to forget *why* $t$ must be chosen minimal (so that $b \in \mathfrak{m}^{t-1}\setminus Aa$ exists) and *why* $b \notin Aa$ is exactly $x^{-1} \notin A$. The rest of the cycle is routine, but this one implication is where the theorem earns its name.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Prove the cycle $(1)\Rightarrow(2)\Rightarrow(3)\Rightarrow(4)\Rightarrow(5)\Rightarrow(1)$, attaching $(3)\iff(6)$ via Nakayama. The only inventive step is $(2)\Rightarrow(3)$: build a uniformizer $x = b/a$ that pushes $\mathfrak{m}$ outside itself, using normality to force the escape. Everything after a principal $\mathfrak{m}$ is the observation that nonzero ideals are squeezed between powers of $\mathfrak{m}$.

**Subgoal decomposition:**

1. **(1) $\Rightarrow$ (2).** Show a valuation ring is integrally closed.
   - *Hint:* For $x \in K$ integral, suppose $v(x) < 0$ and compare valuations of $x^n$ versus the lower terms in the monic equation; the leading term strictly dominates, a contradiction.
   - *Why needed:* It is the easy half that connects the valuation to normality.

2. **(2) $\Rightarrow$ (3).** Manufacture a principal generator of $\mathfrak{m}$.
   - *Hint:* Take $0 \neq a \in \mathfrak{m}$; since $\sqrt{Aa} = \mathfrak{m}$, $\mathfrak{m}^t \subseteq Aa$ for minimal $t$; pick $b \in \mathfrak{m}^{t-1}\setminus Aa$ and set $x = b/a$. Then $x^{-1}\mathfrak{m} \subseteq A$ (as $bm \in \mathfrak{m}^t \subseteq Aa$) and $x^{-1}\mathfrak{m} \not\subseteq \mathfrak{m}$ (else $x^{-1} = b/a$ integral, contradicting $b \notin Aa$ and normality). So $x^{-1}\mathfrak{m} = A$, i.e. $\mathfrak{m} = (x)$.
   - *Why needed:* This is the theorem; everything else is consequence.

3. **(3) $\Rightarrow$ (4).** Show every nonzero ideal is a power of $\mathfrak{m}$.
   - *Hint:* For $\mathfrak{a} \neq 0$, $\sqrt{\mathfrak{a}} = \mathfrak{m}$, so $\mathfrak{m}^\ell \subseteq \mathfrak{a}$; let $t$ be largest with $\mathfrak{a} \subseteq \mathfrak{m}^t = (\pi^t)$; pick $y \in \mathfrak{a}\setminus\mathfrak{m}^{t+1}$, write $y = a\pi^t$ with $a \notin \mathfrak{m}$ a unit, so $\pi^t \in \mathfrak{a}$ and $\mathfrak{a} = (\pi^t) = \mathfrak{m}^t$.
   - *Why needed:* It upgrades "principal $\mathfrak{m}$" to "all ideals are powers".

4. **(4) $\Rightarrow$ (5) $\Rightarrow$ (1).** Extract the uniformizer and the valuation.
   - *Hint:* From $\mathfrak{m} \neq \mathfrak{m}^2$ pick $\pi \in \mathfrak{m}\setminus\mathfrak{m}^2$; then $(\pi) = \mathfrak{m}^r$ with $r = 1$, so every ideal is $(\pi^n)$. The chain $(\pi^n)$ is strictly decreasing (else finitely many ideals, contradiction), so define $v(a) = n$ where $(a) = (\pi^n)$, extend to $K$ by $v(a/b) = v(a) - v(b)$; this is a discrete valuation with $A = A_v$.
   - *Why needed:* It closes the cycle, producing the valuation.

5. **(3) $\iff$ (6).** Relate principal $\mathfrak{m}$ to the cotangent space.
   - *Hint:* By Nakayama, $\dim_k\mathfrak{m}/\mathfrak{m}^2$ equals the minimal number of generators of $\mathfrak{m}$; it is $1$ iff $\mathfrak{m} = (\pi)$.
   - *Why needed:* It supplies the smoothness criterion (6).

---

# Lemma Decomposition

> [!note]- Lemma 1: A valuation ring is integrally closed
> **Statement:** If $A = A_v$ is the valuation ring of a discrete valuation $v$ on $K$, and $x \in K$ is integral over $A$, then $x \in A$.
>
> **Hint:** Use $v(x^n) = nv(x)$ and the ultrametric bound on the lower terms; if $v(x) < 0$ the leading term wins.
>
> **Why needed:** It is implication (1) $\Rightarrow$ (2), the easy connection between valuation and normality.
>
> > [!note]- Full proof
> > Let $x^n + a_1 x^{n-1} + \cdots + a_n = 0$ with $a_i \in A$, so $v(a_i) \geq 0$, and $n \geq 1$. Suppose for contradiction $v(x) < 0$. Then $x^n = -(a_1 x^{n-1} + \cdots + a_n)$, so
> > $$v(x^n) = nv(x) = v\big(a_1 x^{n-1} + \cdots + a_n\big) \geq \min_{1 \leq i \leq n}\big(v(a_i) + (n-i)v(x)\big).$$
> > Since $v(a_i) \geq 0$ and $v(x) < 0$, each term $v(a_i) + (n-i)v(x) \geq (n-i)v(x) > (n - i_0)v(x)$... more directly: the minimum is achieved at some $i_0$, giving $nv(x) \geq v(a_{i_0}) + (n - i_0)v(x) \geq (n-i_0)v(x)$. Subtracting, $i_0 v(x) \geq v(a_{i_0}) \geq 0$, so $i_0 v(x) \geq 0$; but $i_0 \geq 1$ and $v(x) < 0$ give $i_0 v(x) < 0$, a contradiction. Hence $v(x) \geq 0$, i.e. $x \in A$.

> [!note]- Lemma 2: Manufacturing a uniformizer from integral-closedness
> **Statement:** If $(A, \mathfrak{m})$ is a Noetherian local domain of dimension $1$ that is integrally closed, then $\mathfrak{m}$ is principal.
>
> **Hint:** Find $x = b/a \in K$ with $x^{-1}\mathfrak{m} \subseteq A$ but $x^{-1}\mathfrak{m} \not\subseteq \mathfrak{m}$; then $x^{-1}\mathfrak{m} = A$ forces $\mathfrak{m} = (x)$.
>
> **Why needed:** It is the one hard implication (2) $\Rightarrow$ (3); the entire theorem hinges on it.
>
> > [!note]- Full proof
> > It suffices to find $x \in \operatorname{Frac}(A)$ with $\mathfrak{m} = Ax$, because then $x = 1\cdot x \in \mathfrak{m} \subseteq A$, so $x \in A$ automatically. Equivalently, writing $z = x^{-1}$, we seek $z \in K$ with $z\mathfrak{m} = A$. We arrange two conditions on $z$: **(I)** $z\mathfrak{m} \subseteq A$, which makes $z\mathfrak{m}$ an ideal of $A$; and **(II)** $z\mathfrak{m} \not\subseteq \mathfrak{m}$, which then forces $z\mathfrak{m} = A$ since $\mathfrak{m}$ is the unique maximal ideal and an ideal not contained in it must contain a unit.
> >
> > **Choosing $z$.** Pick any $0 \neq a \in \mathfrak{m}$. Since $\operatorname{Spec} A = \{(0), \mathfrak{m}\}$, the only prime containing $Aa$ is $\mathfrak{m}$, so $\sqrt{Aa} = \mathfrak{m}$. As $A$ is Noetherian, every ideal contains a power of its radical, so $\mathfrak{m}^t \subseteq Aa$ for some $t \geq 1$. Take $t$ minimal, so $\mathfrak{m}^{t-1} \not\subseteq Aa$, and choose $b \in \mathfrak{m}^{t-1}\setminus Aa$. Set $z = b/a \in K$.
> >
> > **Condition (I).** For each $m \in \mathfrak{m}$, $bm \in \mathfrak{m}^{t-1}\mathfrak{m} = \mathfrak{m}^t \subseteq Aa$, so $bm = ac$ for some $c \in A$, whence $zm = (b/a)m = c \in A$. Hence $z\mathfrak{m} \subseteq A$. ✓
> >
> > **Condition (II).** Suppose for contradiction $z\mathfrak{m} \subseteq \mathfrak{m}$, i.e. $(b/a)\mathfrak{m} \subseteq \mathfrak{m}$. Then $\mathfrak{m}$ is a module over the subring $A[z] \subseteq K$ stabilized by $z$, finitely generated and faithful over $A$ (it is a nonzero ideal of the domain $A$, so no nonzero element of $A$ — a fortiori of $A[z] \subseteq K$ — annihilates it). By the determinant trick / [[Thm - Characterizations of Integrality (Module-Finite Criterion)|module-finite criterion for integrality]], $z = b/a$ is integral over $A$. Since $A$ is integrally closed, $z \in A$, i.e. $b \in Aa$ — contradicting $b \notin Aa$. Hence $z\mathfrak{m} \not\subseteq \mathfrak{m}$. ✓
> >
> > By (I), $z\mathfrak{m}$ is an ideal of $A$; by (II) it is not contained in $\mathfrak{m}$, so it contains a unit, so $z\mathfrak{m} = A$. Therefore $\mathfrak{m} = A z^{-1} = (a/b)$ is principal, with uniformizer $\pi = a/b \in A$.

> [!note]- Lemma 3: Principal $\mathfrak{m}$ implies every ideal is a power of $\mathfrak{m}$
> **Statement:** If $(A,\mathfrak{m})$ is Noetherian local of dimension $1$ with $\mathfrak{m} = (\pi)$, then every nonzero ideal $\mathfrak{a}$ equals $\mathfrak{m}^t = (\pi^t)$ for a unique $t \geq 0$.
>
> **Hint:** $\sqrt{\mathfrak{a}} = \mathfrak{m}$ gives $\mathfrak{m}^\ell \subseteq \mathfrak{a}$; take $t$ largest with $\mathfrak{a} \subseteq \mathfrak{m}^t$ and find an element of $\mathfrak{a}$ of exact "order" $t$.
>
> **Why needed:** It is implication (3) $\Rightarrow$ (4), upgrading principality to full ideal control.
>
> > [!note]- Full proof
> > Let $\mathfrak{a}$ be a nonzero proper ideal. Since the only primes are $(0)$ and $\mathfrak{m}$ and $\mathfrak{a} \neq 0$, $\sqrt{\mathfrak{a}} = \mathfrak{m}$; as $A$ is Noetherian, $\mathfrak{m}^\ell \subseteq \mathfrak{a}$ for some $\ell \geq 1$. So $\mathfrak{a}$ is bounded on both sides: $\mathfrak{m}^\ell \subseteq \mathfrak{a} \subseteq \mathfrak{m}^1$. Let $t \geq 1$ be the largest integer with $\mathfrak{a} \subseteq \mathfrak{m}^t$; this exists and satisfies $t \leq \ell$, because $\mathfrak{m}^\ell \subseteq \mathfrak{a}$ together with strict decrease of the powers (Lemma 4) prevents $\mathfrak{a} \subseteq \mathfrak{m}^{\ell+1}$. Pick $y \in \mathfrak{a}$ with $y \notin \mathfrak{m}^{t+1}$ (such $y$ exists by maximality of $t$). Now $\mathfrak{m}^t = (\pi^t)$, so $y = a\pi^t$ for some $a \in A$; since $y \notin \mathfrak{m}^{t+1} = (\pi^{t+1})$, we cannot have $a \in \mathfrak{m}$ (else $y \in (\pi^{t+1})$), so $a \notin \mathfrak{m}$ is a unit. Then $\pi^t = a^{-1}y \in \mathfrak{a}$, so $(\pi^t) \subseteq \mathfrak{a} \subseteq (\pi^t)$, giving $\mathfrak{a} = (\pi^t) = \mathfrak{m}^t$. Uniqueness of $t$ follows since the powers $\mathfrak{m}^t$ are strictly decreasing (Lemma 4).

> [!note]- Lemma 4: The powers of $\mathfrak{m}$ strictly decrease, and the valuation exists
> **Statement:** If every nonzero ideal of $A$ is $(\pi^n)$ for a fixed $\pi$ (condition 5), then the chain $A \supsetneq (\pi) \supsetneq (\pi^2) \supsetneq \cdots$ is strictly decreasing, and $v(a) := n$ (where $(a) = (\pi^n)$), extended to $K$ by $v(a/b) = v(a) - v(b)$, is a discrete valuation with $A_v = A$. Hence $A$ is a DVR.
>
> **Hint:** If $(\pi^{n+1}) = (\pi^n)$ then $A$ has finitely many ideals, contradicting dimension $1$; check $v$ is a well-defined surjective homomorphism satisfying the ultrametric inequality.
>
> **Why needed:** It is implication (5) $\Rightarrow$ (1), closing the cycle by producing the valuation.
>
> > [!note]- Full proof
> > **Strict decrease.** Suppose $(\pi^{n+1}) = (\pi^n)$ for some $n$. Then $\pi^n = c\pi^{n+1}$ for some $c$, so $\pi^n(1 - c\pi) = 0$; as $A$ is a domain and $\pi \neq 0$, $1 - c\pi = 0$, making $\pi$ a unit, so $\mathfrak{m} = (\pi) = A$ — contradicting $\mathfrak{m}$ proper. (Equivalently $(\pi^{n+i}) = (\pi^n)$ for all $i$ gives finitely many ideals, impossible for a one-dimensional domain by the Noetherian chain $\mathfrak{m}^n$ argument.) So all inclusions are strict.
> >
> > **The valuation.** For $0 \neq a \in A$, $(a)$ is a nonzero ideal, hence $(a) = (\pi^n)$ for a unique $n = v(a) \geq 0$ by strict decrease. For $a/b \in K^\times$ set $v(a/b) = v(a) - v(b)$; this is well-defined (if $a/b = a'/b'$ then $ab' = a'b$, and $v$ is additive on $A$, so $v(a) + v(b') = v(a') + v(b)$). It is surjective onto $\mathbb{Z}$ (negative values from $1/\pi^n$), a homomorphism since $(\pi^{m})(\pi^n) = (\pi^{m+n})$ gives $v(xy) = v(x) + v(y)$, and it satisfies the ultrametric inequality: if $v(x) = m \leq n = v(y)$, write $x = u\pi^m$, $y = w\pi^n$ with $u, w$ units, then $x + y = \pi^m(u + w\pi^{n-m})$ and $u + w\pi^{n-m} \in A$, so $v(x+y) \geq m = \min$. Finally $A_v = \{x : v(x) \geq 0\} = A$ by construction. So $A$ is the valuation ring of $v$, a DVR.

> [!note]- Lemma 5: The cotangent space counts the generators (Nakayama)
> **Statement:** $\dim_k \mathfrak{m}/\mathfrak{m}^2$ equals the minimal number of generators of $\mathfrak{m}$; in particular $\dim_k\mathfrak{m}/\mathfrak{m}^2 = 1 \iff \mathfrak{m}$ is principal.
>
> **Hint:** Elements of $\mathfrak{m}$ generate $\mathfrak{m}$ iff their images span $\mathfrak{m}/\mathfrak{m}^2$ over $k$, by [[Commutative Algebra V — Nakayama's Lemma|Nakayama]].
>
> **Why needed:** It is the equivalence (3) $\iff$ (6), supplying the smoothness criterion.
>
> > [!note]- Full proof
> > $\mathfrak{m}/\mathfrak{m}^2$ is a module over $A/\mathfrak{m} = k$, i.e. a $k$-vector space. By [[Commutative Algebra V — Nakayama's Lemma|Nakayama's lemma]] (in the "lifting generators" form): elements $x_1, \dots, x_r \in \mathfrak{m}$ generate $\mathfrak{m}$ as an ideal if and only if their images $\bar{x}_1, \dots, \bar{x}_r$ span $\mathfrak{m}/\mathfrak{m}^2$ as a $k$-vector space. Hence the minimal number of ideal-generators of $\mathfrak{m}$ equals $\dim_k\mathfrak{m}/\mathfrak{m}^2$. So this dimension is $1$ exactly when $\mathfrak{m}$ can be generated by a single element, i.e. $\mathfrak{m}$ is principal.

---

# Formal Proof

> [!note]- Complete formal proof
> We prove $(1)\Rightarrow(2)\Rightarrow(3)\Rightarrow(4)\Rightarrow(5)\Rightarrow(1)$ and $(3)\iff(6)$.
>
> ---
> **(1) $\Rightarrow$ (2)** is Lemma 1: the valuation ring is integrally closed.
>
> **(2) $\Rightarrow$ (3)** is Lemma 2: integral-closedness manufactures a principal generator of $\mathfrak{m}$ via $x = a/b$ with $b \in \mathfrak{m}^{t-1}\setminus Aa$, $t$ minimal with $\mathfrak{m}^t \subseteq Aa$.
>
> **(3) $\Rightarrow$ (4)** is Lemma 3: with $\mathfrak{m} = (\pi)$, every nonzero ideal is $\mathfrak{m}^t = (\pi^t)$.
>
> **(4) $\Rightarrow$ (5):** By (4), $\mathfrak{m} \neq \mathfrak{m}^2$ (else by Nakayama $\mathfrak{m} = 0$). Choose $\pi \in \mathfrak{m}\setminus\mathfrak{m}^2$; by (4) the ideal $(\pi)$ is a power $\mathfrak{m}^r$, and $\pi \notin \mathfrak{m}^2$ forces $r = 1$, so $(\pi) = \mathfrak{m}$. Then every nonzero ideal $\mathfrak{m}^t = (\pi^t)$, establishing (5).
>
> **(5) $\Rightarrow$ (1)** is Lemma 4: the powers $(\pi^n)$ strictly decrease, and $v(a) = n$ for $(a) = (\pi^n)$, extended to $K$, is a discrete valuation with valuation ring $A$.
>
> **(3) $\iff$ (6)** is Lemma 5: by Nakayama, $\dim_k\mathfrak{m}/\mathfrak{m}^2$ is the minimal number of generators of $\mathfrak{m}$, which is $1$ iff $\mathfrak{m}$ is principal.
>
> This closes the cycle, so all six conditions are equivalent. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Power series rings are DVRs (analysis / formal geometry).** The ring $k[[T]]$ of formal power series is a Noetherian local domain with maximal ideal $\mathfrak{m} = (T)$, hence a DVR by condition (3), with valuation $v(f)$ the order of the lowest nonzero term. The nonobvious recognition is that an *infinite-dimensional* $k$-vector space carries a one-dimensional cotangent space; the application connects formal-neighbourhood geometry to valuation theory, and $k[[T]]$ is the completion of every smooth curve's local ring.

**The local ring of a node is NOT a DVR (singularity theory).** For the nodal cubic $k[x,y]/(xy)$ localized at the origin, $\dim_k\mathfrak{m}/\mathfrak{m}^2 = 2$, so condition (6) fails and the ring is not a DVR. This battle-tests the theorem by exhibiting a one-dimensional local ring (it has two minimal primes though — better: use $k[x,y]/(y^2-x^3)$, the cusp, a domain) where the cotangent space detects the singularity. The application links the algebraic characterization to resolution of singularities: normalization replaces the bad local ring by a DVR.

**$p$-adic integers in number theory.** The ring $\mathbb{Z}_p$ of $p$-adic integers is a complete DVR with uniformizer $p$ and residue field $\mathbb{F}_p$. Recognizing it via condition (3) — $\mathfrak{m} = (p)$ is principal — is immediate, and the theorem then certifies it carries a unique valuation $v_p$. The application is the foundation of local number theory: Hensel's lemma, local class field theory, and the local–global principle all run on the DVR structure of $\mathbb{Z}_p$.

---

# Bridges

- **[[Def - Dedekind Domain|Dedekind domains]]** — this theorem is *why* the two definitions of a Dedekind domain agree. "Integrally closed" (a global condition) localizes to "$A_\mathfrak{p}$ integrally closed", which by this theorem is "$A_\mathfrak{p}$ is a DVR" — and that is the second definition. Without the (2) $\iff$ (1) equivalence proved here, the global normality condition and the local DVR condition would be unrelated. The theorem is the hinge connecting them.

- **[[Commutative Algebra V — Nakayama's Lemma|Nakayama's lemma]] and the cotangent space** — condition (6), $\dim_k\mathfrak{m}/\mathfrak{m}^2 = 1$, is exactly Nakayama applied to $\mathfrak{m}$: the minimal number of generators of $\mathfrak{m}$ is the dimension of its cotangent space. This is the algebraic definition of a **regular local ring**, and a DVR is precisely a regular local ring of dimension one. The theorem thus places DVRs at the bottom of the regularity hierarchy.

- **[[Thm - Characterizations of Integrality (Module-Finite Criterion)|The module-finite criterion for integrality]]** — the determinant-trick fact that "$x$ stabilizes a faithful finitely generated module $\Rightarrow x$ integral" is the precise tool used in (2) $\Rightarrow$ (3) to derive a contradiction: if $x^{-1}\mathfrak{m} \subseteq \mathfrak{m}$ then $x^{-1}$ stabilizes the f.g. faithful module $\mathfrak{m}$, hence is integral, hence (by normality) lies in $A$, the contradiction that forces the escape.

- **[[Def - Discrete Valuation and Valuation Ring|The valuation]]** — condition (5) is the bridge to the explicit valuation: $v(a) = n$ for $(a) = (\pi^n)$ recovers the valuation from the ideal structure, proving it was intrinsic all along. This is what licenses "the valuation of a DVR" as a well-defined object rather than a chosen extra.

---

# Unlocked by This

> [!tip] Regular local rings and smoothness *(from Algebraic Geometry)*
> Condition (6) generalizes: a Noetherian local ring $(A, \mathfrak{m})$ is **regular** if $\dim_k\mathfrak{m}/\mathfrak{m}^2 = \dim A$, the cotangent space matching the Krull dimension. A DVR is the one-dimensional case. Regular local rings are the local rings of **smooth points** on varieties of any dimension, and the theory of regular sequences, depth, and Cohen–Macaulay rings all builds on this condition. The Auslander–Buchsbaum theorem (regular $\iff$ finite global dimension) is the homological deepening.

> [!tip] Valuative criteria and the limits of families *(from Algebraic Geometry)*
> Because a DVR is the algebraic model of "a small disk and its puncture", maps out of a DVR test whether limits exist. The **valuative criterion of properness** says a morphism is proper iff every map from the punctured spectrum (the fraction field) extends uniquely over the DVR. This makes DVRs the standard probe for separatedness, properness, and specialization in scheme theory — a direct consequence of recognizing DVRs by the clean ideal structure this theorem provides.
