---
type: theorem
subject: commutative-algebra
prereqs:
  - "Thm - The Weak Nullstellensatz"
  - "Def - Affine Variety and the Vanishing Set"
  - "Def - The Coordinate Ring and the Ideal of a Set"
  - "Def - Radical of an Ideal and the Nilradical"
  - "Def - Polynomial Ring"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Chapter standing data: a field $k$, an algebraically closed $\Omega \supseteq k$, affine space $\Omega^n$, the operations $V$ ([[Def - Affine Variety and the Vanishing Set]]) and $I$ ([[Def - The Coordinate Ring and the Ideal of a Set]]). The [[Def - Radical of an Ideal and the Nilradical|radical]] of $\mathfrak a \trianglelefteq k[T_1, \dots, T_n]$ is $\sqrt{\mathfrak a} = \{f : f^m \in \mathfrak a \text{ for some } m \geq 1\}$. We write $V(f) := V(\{f\})$, $\mathfrak a^e$ for the extension of $\mathfrak a$ to $k[T_1, \dots, T_n, T_{n+1}]$, and $A_f = \{f^{-m}\}^{-1}A$ for the [[Commutative Algebra IV — Localization|localization]] inverting $f$. The full registry is on [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz]].

---

# Statement

> **Theorem (Strong Nullstellensatz).** Let $k$ be a field, $\Omega \supseteq k$ algebraically closed, and $\mathfrak a$ an ideal of $k[T_1, \dots, T_n]$. Then
> $$I(V(\mathfrak a)) = \sqrt{\mathfrak a}.$$
> In words: a polynomial $f$ vanishes on the entire zero set of $\mathfrak a$ **if and only if** some power of $f$ lies in $\mathfrak a$.

> **Membership form.** For $f \in k[T_1, \dots, T_n]$:
> $$f(x) = 0 \text{ for all } x \in V(\mathfrak a) \quad \Longleftrightarrow \quad f^m \in \mathfrak a \text{ for some } m \geq 1.$$

The inclusion $\sqrt{\mathfrak a} \subseteq I(V(\mathfrak a))$ is elementary (a power of $f$ vanishing forces $f$ to vanish, since $\Omega$ is a domain). The content is the reverse, $I(V(\mathfrak a)) \subseteq \sqrt{\mathfrak a}$ — that vanishing on the variety is *witnessed algebraically* by a power lying in the ideal. This upgrades the [[Thm - The Weak Nullstellensatz|weak Nullstellensatz]] (which only sees emptiness) to a complete description of which functions vanish on a variety.

---

# Motivation

The weak Nullstellensatz answered "is the variety empty?". The strong Nullstellensatz answers the far more useful question "**which functions vanish on the variety?**" — and the answer is exactly the radical $\sqrt{\mathfrak a}$. This is the theorem that makes the algebra–geometry dictionary an *equivalence*: it computes the geometry-side operation $I(V(-))$ purely algebraically as "take the radical". Geometry can be done entirely in the ring, because the only thing geometry adds to an ideal $\mathfrak a$ is its radical, and the radical is an algebraic operation.

Why is the answer the *radical* and not $\mathfrak a$ itself? Because vanishing cannot distinguish $f$ from $f^m$. If $f^m \in \mathfrak a$, then $f^m$ vanishes on $V(\mathfrak a)$, so $f^m(x) = f(x)^m = 0$, so $f(x) = 0$ (the field $\Omega$ has no zero divisors): $f$ vanishes too, even though $f$ itself may not be in $\mathfrak a$. The simplest instance: $\mathfrak a = (T^2)$ in $k[T]$ has $V(\mathfrak a) = \{0\}$, and $T$ vanishes at $0$, so $T \in I(V(\mathfrak a))$; but $T \notin (T^2)$, while $T^2 \in (T^2)$, so $T \in \sqrt{(T^2)} = (T)$. The radical exactly collects the "ghost" functions that vanish on the variety because a *power* of them is in the ideal. The strong Nullstellensatz says these ghosts are *all* of $I(V(\mathfrak a))$ — there are no other vanishing functions.

The consequence is the **Nullstellensatz correspondence**: $V$ and $I$ are inverse bijections between *radical* ideals and algebraic sets (a [[Thm - The Nullstellensatz Correspondence (radical ideals and varieties)|separate theorem]] built directly on this one). And the route to the proof is itself beautiful: the strong form is deduced from the *weak* form by a single trick (Rabinowitsch), adjoining one variable to convert "$f$ vanishes wherever $\mathfrak a$ does" into "a related system has no solution". The strong Nullstellensatz is the weak Nullstellensatz seen in one extra dimension.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\mathfrak a \trianglelefteq k[T_1, \dots, T_n]$, $\Omega$ algebraically closed". The recognition is "I want to know what vanishes on a variety, or to identify a radical".

The first disguised source is **"$f$ vanishes on $V(\mathfrak a)$ and I want to conclude something algebraic about $f$"**. The bridge: the strong Nullstellensatz turns the geometric hypothesis "$f|_{V(\mathfrak a)} = 0$" into the algebraic conclusion "$f^m \in \mathfrak a$". The non-obvious value is that a *pointwise* vanishing condition yields an *ideal-membership* statement with a concrete exponent. *Example problem:* if $f$ vanishes wherever $g_1, \dots, g_t$ all vanish, then $f^m = \sum h_i g_i$ for some $m$.

The second disguised source is **"compute $\sqrt{\mathfrak a}$" or "is $\mathfrak a$ radical?"**. The bridge: $\sqrt{\mathfrak a} = I(V(\mathfrak a))$, so the radical is the ideal of functions vanishing on the geometric zero set — often computable geometrically. The non-obvious payoff is that radical-membership becomes a vanishing question. *Example problem:* [[Ex - The radical as the intersection of maximal ideals containing it|show $\sqrt{\mathfrak a} = \bigcap_{\mathfrak a \subseteq \mathfrak m} \mathfrak m$]] (over a finitely generated algebra).

The third disguised source is **"two varieties are equal / contained"**, phrased as a set inclusion $V(\mathfrak a) \subseteq V(\mathfrak b)$. The bridge: applying $I$ and the strong Nullstellensatz, this is equivalent to $\sqrt{\mathfrak b} \subseteq \sqrt{\mathfrak a}$ — a purely algebraic inclusion of radicals. *Example problem:* $V(\mathfrak a) \subseteq V(\mathfrak b) \iff \mathfrak b \subseteq \sqrt{\mathfrak a}$.

**Targets (Output Amplification)**

The conclusion is "$I(V(\mathfrak a)) = \sqrt{\mathfrak a}$".

Combine with **"$I(X)$ is always radical and $V(I(X)) = X$ for $X$ algebraic"**. Then $V$ and $I$ are mutually inverse on the closed objects. The further result $E$ is the **[[Thm - The Nullstellensatz Correspondence (radical ideals and varieties)|order-reversing bijection]]** {radical ideals} $\leftrightarrow$ {algebraic sets}, the full dictionary.

Combine with **prime ideals**. Restrict the correspondence to *prime* radical ideals; primes are exactly the radical ideals whose varieties are irreducible. The further result $E$ is the bijection {prime ideals} $\leftrightarrow$ {[[Def - Irreducible Algebraic Set|irreducible varieties]]}, and {maximal ideals} $\leftrightarrow$ {points}, the stratified dictionary.

Combine with **the radical-as-intersection-of-primes identity** $\sqrt{\mathfrak a} = \bigcap_{\mathfrak a \subseteq \mathfrak p}\mathfrak p$ (from [[Commutative Algebra IV — Localization|localization]]). Over a finitely generated algebra, the strong Nullstellensatz refines this to $\sqrt{\mathfrak a} = \bigcap_{\mathfrak a \subseteq \mathfrak m}\mathfrak m$ — intersection of the *maximal* ideals — because such rings are Jacobson. The further result $E$ is the Jacobson-ring form of the Nullstellensatz.

---

# Why Is It True

The reverse inclusion is the **Rabinowitsch trick**: introduce one new variable to *force* a non-vanishing, reducing the strong form to the weak form. It is one of the slickest deductions in the subject.

**The bolded one-liner: to show $f$ vanishing on $V(\mathfrak a)$ has a power in $\mathfrak a$, adjoin a variable $T_{n+1}$ and the equation $T_{n+1}f = 1$; the enlarged system has no solution (wherever $\mathfrak a$ vanishes, $f$ vanishes, so $T_{n+1}f = 1$ is unsatisfiable), so by the weak Nullstellensatz $1$ lies in the enlarged ideal — and clearing the denominator $f$ produces $f^m \in \mathfrak a$.**

Here is the mechanism. Suppose $f \in I(V(\mathfrak a))$, i.e. $f$ vanishes on $V(\mathfrak a) \subseteq \Omega^n$. Form the ideal $\mathfrak b := \mathfrak a^e + (T_{n+1}f - 1)$ in the larger ring $k[T_1, \dots, T_n, T_{n+1}]$ (where $\mathfrak a^e$ is $\mathfrak a$ extended). Claim: $V(\mathfrak b) = \varnothing$ in $\Omega^{n+1}$. Indeed, a point $(x_1, \dots, x_{n+1}) \in V(\mathfrak b)$ would have $(x_1, \dots, x_n) \in V(\mathfrak a)$ (it satisfies all of $\mathfrak a$), so $f(x_1, \dots, x_n) = 0$ by hypothesis; but then $T_{n+1}f - 1$ evaluates to $x_{n+1}\cdot 0 - 1 = -1 \neq 0$, contradicting membership in $V(\mathfrak b)$. So $V(\mathfrak b) = \varnothing$, and the [[Thm - The Weak Nullstellensatz|weak Nullstellensatz]] gives $1 \in \mathfrak b$:
$$1 = \sum_i p_i(T_1, \dots, T_{n+1}) g_i(T_1, \dots, T_n) + q(T_1, \dots, T_{n+1})\big(T_{n+1}f - 1\big),$$
with $g_i \in \mathfrak a$. Now the trick's payoff: *substitute $T_{n+1} = 1/f$*. This is the localization $k[T_1, \dots, T_n]_f$: in the ring $A_f$ where $f$ is inverted, the relation $T_{n+1}f - 1$ becomes $0$, so the last term vanishes and we get $1 = \sum_i p_i(T, 1/f) g_i$ in $A_f$. Clearing the denominators — multiply by a high enough power $f^m$ — yields, *back in $k[T_1, \dots, T_n]$*,
$$f^m = \sum_i \tilde p_i g_i \in \mathfrak a.$$
So $f^m \in \mathfrak a$, i.e. $f \in \sqrt{\mathfrak a}$.

The conceptual content: **"$f$ vanishes wherever $\mathfrak a$ vanishes" is exactly "$\mathfrak a$ together with $1/f$ is inconsistent".** The extra variable $T_{n+1}$ is a stand-in for $1/f$; demanding $T_{n+1}f = 1$ forbids $f = 0$, so the geometric statement "$\mathfrak a \Rightarrow f = 0$" becomes "$\mathfrak a$ and $f \neq 0$ have no common solution", which the weak Nullstellensatz certifies as $1 \in \mathfrak b$. Clearing the artificial denominator returns the certificate to the original ring as a power of $f$. The exponent $m$ is the price of the denominators — it is *why* the answer is the radical, not the ideal.

(The localization-theoretic restatement: $A_f = A[T_{n+1}]/(T_{n+1}f - 1)$, so $f$ nilpotent in $A = k[T]/\mathfrak a$ $\iff$ $A_f = 0$ $\iff$ $V(\mathfrak b) = \varnothing$ — the same trick, phrased via [[Commutative Algebra IV — Localization|inverting $f$]].)

---

# What Makes This Hard

The genuine difficulty is *inventing the extra variable*: nothing in the statement suggests adjoining $T_{n+1}$ with the relation $T_{n+1}f = 1$, and seeing that this converts "vanishing" into "no solution" is the trick that makes the proof work. The non-obvious step is recognising that the hypothesis "$f$ vanishes on $V(\mathfrak a)$" is exactly what makes the enlarged variety $V(\mathfrak a^e + (T_{n+1}f - 1))$ *empty* — the new equation $T_{n+1}f = 1$ has no solution precisely where $f = 0$. The most common error is to get the direction of the inclusion wrong (the easy inclusion is $\sqrt{\mathfrak a} \subseteq I(V(\mathfrak a))$; the trick is for the reverse), or to forget that clearing denominators introduces the power $f^m$ — which is the whole reason the radical appears.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
The easy inclusion is direct. For the hard inclusion, given $f$ vanishing on $V(\mathfrak a)$, adjoin a variable $T_{n+1}$ and the polynomial $T_{n+1}f - 1$; the resulting variety is empty, so by the weak Nullstellensatz $1$ is in the enlarged ideal; substitute $T_{n+1} = 1/f$ (localize at $f$) and clear denominators to land $f^m \in \mathfrak a$.

**Subgoal decomposition:**

1. **Easy inclusion.** $\sqrt{\mathfrak a} \subseteq I(V(\mathfrak a))$.
   - *Hint:* $f^m \in \mathfrak a \Rightarrow f^m$ vanishes on $V(\mathfrak a) \Rightarrow f(x)^m = 0 \Rightarrow f(x) = 0$ ($\Omega$ a domain).
   - *Why needed:* One half of the equality, and it explains *why* the radical is the natural answer.

2. **Set up Rabinowitsch.** Given $f \in I(V(\mathfrak a))$, form $\mathfrak b = \mathfrak a^e + (T_{n+1}f - 1) \trianglelefteq k[T_1, \dots, T_{n+1}]$ and show $V(\mathfrak b) = \varnothing$.
   - *Hint:* A point of $V(\mathfrak b)$ would have its first $n$ coordinates in $V(\mathfrak a)$, forcing $f = 0$ there, making $T_{n+1}f - 1 = -1 \neq 0$.
   - *Why needed:* Reduces to a *weak*-Nullstellensatz situation (emptiness).

3. **Apply the weak form.** $V(\mathfrak b) = \varnothing \Rightarrow 1 \in \mathfrak b$, giving $1 = \sum p_i g_i + q(T_{n+1}f - 1)$ with $g_i \in \mathfrak a$.
   - *Hint:* [[Thm - The Weak Nullstellensatz|Weak Nullstellensatz]] in $n+1$ variables.
   - *Why needed:* Produces the algebraic certificate.

4. **Substitute $T_{n+1} = 1/f$ and clear denominators.** In $A_f$ the relation kills the last term; multiplying by $f^m$ returns $f^m = \sum \tilde p_i g_i \in \mathfrak a$.
   - *Hint:* This is the [[Commutative Algebra IV — Localization|localization]] $k[T]_f$; the denominator power becomes the radical exponent.
   - *Why needed:* Lands the conclusion $f \in \sqrt{\mathfrak a}$, and explains the appearance of the power.

---

# Lemma Decomposition

> [!note]- Lemma 1: The easy inclusion
> **Statement:** $\sqrt{\mathfrak a} \subseteq I(V(\mathfrak a))$ for any ideal $\mathfrak a$ and any $\Omega$ that is an integral domain.
>
> **Hint:** A power vanishing forces the function to vanish, because $\Omega$ has no zero divisors.
>
> **Why needed:** Half the theorem, and the reason the *radical* (not $\mathfrak a$) is the answer.
>
> > [!note]- Full proof
> > Let $f \in \sqrt{\mathfrak a}$, so $f^m \in \mathfrak a$ for some $m \geq 1$. For any $x \in V(\mathfrak a)$, $f^m(x) = 0$ since $f^m \in \mathfrak a$. But $f^m(x) = f(x)^m$, and $\Omega$ is an integral domain, so $f(x) = 0$. Hence $f$ vanishes on $V(\mathfrak a)$, i.e. $f \in I(V(\mathfrak a))$.

> [!note]- Lemma 2: The Rabinowitsch variety is empty
> **Statement:** If $f$ vanishes on $V(\mathfrak a) \subseteq \Omega^n$, then $V(\mathfrak b) = \varnothing$ in $\Omega^{n+1}$, where $\mathfrak b = \mathfrak a^e + (T_{n+1}f - 1)$.
>
> **Hint:** Project a hypothetical solution to its first $n$ coordinates; those lie in $V(\mathfrak a)$, where $f = 0$, contradicting $T_{n+1}f = 1$.
>
> **Why needed:** It is the reduction of the strong form to the weak form — the heart of the trick.
>
> > [!note]- Full proof
> > Suppose $x = (x_1, \dots, x_{n+1}) \in V(\mathfrak b)$. Since $\mathfrak a^e \subseteq \mathfrak b$, every $g \in \mathfrak a$ vanishes at $x$, so $g(x_1, \dots, x_n) = 0$ (these $g$ do not involve $T_{n+1}$); hence $x_0 := (x_1, \dots, x_n) \in V(\mathfrak a)$. By hypothesis $f(x_0) = 0$. But $T_{n+1}f - 1 \in \mathfrak b$ also vanishes at $x$: $x_{n+1}f(x_0) - 1 = x_{n+1}\cdot 0 - 1 = -1$, which is nonzero — a contradiction. So no such $x$ exists and $V(\mathfrak b) = \varnothing$.

> [!note]- Lemma 3: Clearing the denominator
> **Statement:** If $1 = \sum_i p_i(T_1, \dots, T_{n+1}) g_i + q\cdot(T_{n+1}f - 1)$ with $g_i \in \mathfrak a$, then $f^m \in \mathfrak a$ for some $m \geq 1$.
>
> **Hint:** Work in the localization $A_f = k[T_1, \dots, T_n]_f$, where $T_{n+1} \mapsto 1/f$ kills the last term; then multiply through by a power of $f$ to return to the polynomial ring.
>
> **Why needed:** It converts the weak-Nullstellensatz certificate into a radical-membership statement, producing the exponent.
>
> > [!note]- Full proof
> > Map $k[T_1, \dots, T_{n+1}] \to k(T_1, \dots, T_n)$ by $T_i \mapsto T_i$ ($i \leq n$) and $T_{n+1} \mapsto 1/f$ (valid since $f \neq 0$ in the fraction field). Under this map $T_{n+1}f - 1 \mapsto (1/f)f - 1 = 0$, so the identity becomes $1 = \sum_i p_i(T_1, \dots, T_n, 1/f)\, g_i$ in $k(T_1, \dots, T_n)$. Each $p_i(T, 1/f)$ is a polynomial in $1/f$, so has the form $P_i/f^{m_i}$ with $P_i \in k[T_1, \dots, T_n]$. Let $m = \max_i m_i$. Multiplying the identity by $f^m$ gives $f^m = \sum_i \tilde P_i\, g_i$ with $\tilde P_i = P_i f^{m - m_i} \in k[T_1, \dots, T_n]$. The right side lies in $\mathfrak a$ (each $g_i$ does), so $f^m \in \mathfrak a$, i.e. $f \in \sqrt{\mathfrak a}$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathfrak a \trianglelefteq k[T_1, \dots, T_n]$, $\Omega \supseteq k$ algebraically closed.
>
> **($\supseteq$) The easy inclusion.** By **Lemma 1**, $\sqrt{\mathfrak a} \subseteq I(V(\mathfrak a))$.
>
> **($\subseteq$) The Rabinowitsch trick.** Let $f \in I(V(\mathfrak a))$; we show $f \in \sqrt{\mathfrak a}$. (If $f = 0$ this is trivial, so assume $f \neq 0$.) In $k[T_1, \dots, T_n, T_{n+1}]$ form
> $$\mathfrak b := \mathfrak a^e + (T_{n+1}f - 1).$$
> By **Lemma 2**, $V(\mathfrak b) = \varnothing$ in $\Omega^{n+1}$. By the [[Thm - The Weak Nullstellensatz|weak Nullstellensatz]], $1 \in \mathfrak b$, so there are $p_i, q \in k[T_1, \dots, T_{n+1}]$ and generators $g_i \in \mathfrak a$ with
> $$1 = \sum_i p_i\, g_i + q\,(T_{n+1}f - 1).$$
> By **Lemma 3**, substituting $T_{n+1} = 1/f$ and clearing denominators yields $f^m \in \mathfrak a$ for some $m \geq 1$. Hence $f \in \sqrt{\mathfrak a}$.
>
> Combining, $I(V(\mathfrak a)) = \sqrt{\mathfrak a}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Certifying a polynomial vanishes on a variety.** Given that $f$ vanishes wherever $g_1, g_2$ vanish over $\mathbb{C}$, the strong Nullstellensatz guarantees an *explicit* identity $f^m = h_1 g_1 + h_2 g_2$; finding $m$ and the $h_i$ is a Gröbner-basis radical-membership computation. The application is nonobvious because a purely geometric hypothesis (vanishing on a set) is converted into a finite algebraic certificate with a computable exponent.

**Implicitization of parametrised curves.** A rational curve $t \mapsto (x(t), y(t))$ has an implicit equation $F(x, y) = 0$; the ideal of relations is the radical of an elimination ideal, computed via the Nullstellensatz. The application battle-tests the source "what vanishes on this image?", turning a parametrisation into its defining equation — standard in computer-aided geometric design.

**Combinatorial Nullstellensatz and zero-sum problems.** Alon's *Combinatorial Nullstellensatz* is a quantitative cousin: a polynomial vanishing on a grid $S_1 \times \dots \times S_n$ must have each variable's degree controlled, used to prove existence results in combinatorics (e.g. the Cauchy–Davenport theorem). The application is nonobvious because it exports the "vanishing forces algebraic structure" principle from algebraically closed fields to finite grids, a workhorse of the polynomial method.

---

# Bridges

- **[[Thm - The Weak Nullstellensatz|The Weak Nullstellensatz]]** — the sole input. The strong form is the weak form plus the Rabinowitsch trick: adjoin $T_{n+1}$, force $f \neq 0$, get emptiness, apply the weak form, clear denominators. Logically the weak form carries all existence content; the strong form repackages it as "the radical is what vanishes".

- **[[Def - Radical of an Ideal and the Nilradical|The radical]]** — the answer. The theorem identifies the geometric operation $I(V(-))$ with the algebraic operation $\sqrt{(-)}$. The exponent $m$ in $f^m \in \mathfrak a$ — the "denominator power" of the trick — is precisely the radical's defining feature; geometry literally cannot see beyond the radical because $V(\mathfrak a) = V(\sqrt{\mathfrak a})$.

- **[[Commutative Algebra IV — Localization|Localization]]** — the mechanism of the trick. Adjoining $T_{n+1}$ with $T_{n+1}f - 1$ is exactly forming $A_f = A[T_{n+1}]/(T_{n+1}f - 1)$, the localization inverting $f$; "$V(\mathfrak b) = \varnothing$" is "$A_f = 0$" is "$f$ nilpotent in $A = k[T]/\mathfrak a$" is "$f \in \sqrt{\mathfrak a}$". The strong Nullstellensatz is the geometric reading of "$R_f = 0 \iff f$ nilpotent", the collapse criterion of the localization chapter.

- **[[Thm - The Nullstellensatz Correspondence (radical ideals and varieties)|The Nullstellensatz correspondence]]** — the payoff. $I(V(\mathfrak a)) = \sqrt{\mathfrak a}$ is exactly the identity that makes $V$ and $I$ inverse bijections between radical ideals and algebraic sets; the correspondence is this theorem plus "$V(I(X)) = X$".

---

# Unlocked by This

> [!tip] The geometry–algebra dictionary is exact: $I(V(\mathfrak a)) = \sqrt{\mathfrak a}$ *(from Algebraic Geometry)*
> The strong Nullstellensatz is the theorem that makes "spaces are their rings of functions" *precise* and *computable*: the only information geometry loses about an ideal is its non-radical part, and "take the radical" is the exact translation between the ideal and the functions vanishing on its variety. Every operation on varieties (intersection, union, containment) becomes an operation on radical ideals (sum-then-radical, intersection, radical-containment), developed fully in the [[Thm - The Nullstellensatz Correspondence (radical ideals and varieties)|correspondence]]. The non-radical ideals — those with nilpotents — are not garbage but the entry point to **scheme theory**, where one keeps $\mathfrak a$ itself and the nilpotents in $k[T]/\mathfrak a$ record *multiplicity* and *infinitesimal thickening* (e.g. $(T^2)$ is a "double point" at the origin, geometrically invisible but algebraically real).

> [!tip] Radical membership, primary decomposition, and effective bounds *(from Computational Algebra)*
> The membership form "$f$ vanishes on $V(\mathfrak a) \iff f^m \in \mathfrak a$" is the basis of **radical-ideal algorithms**: deciding whether $f$ vanishes on a variety reduces to testing $f \in \sqrt{\mathfrak a}$, computable by the Rabinowitsch construction (add $T_{n+1}f - 1$, test $1 \in \mathfrak b$ via a Gröbner basis). The minimal exponent $m$ is bounded effectively, and the radical $\sqrt{\mathfrak a}$ decomposes via [[Commutative Algebra IX — Primary Decomposition|primary decomposition]] into the prime ideals of the irreducible components — making "which functions vanish on which component" a finite computation.
