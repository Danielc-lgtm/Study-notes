---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Integral Element and Integral Extension"
  - "Def - Integral Domain"
  - "Def - Unit and Field"
  - "Def - Prime and Maximal Ideal"
  - "Thm - Maximal and Prime Ideals via Quotients"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $A \subseteq B$ be an [[Def - Integral Element and Integral Extension|integral extension]] of rings. We write $R^\times$ for the group of units of a ring $R$. For a prime $\mathfrak q \trianglelefteq B$, its contraction is $\mathfrak q \cap A = \mathfrak q^c \trianglelefteq A$, a prime of $A$. A ring is a [[Def - Unit and Field|field]] if it is nonzero and every nonzero element is a unit; an ideal is [[Def - Prime and Maximal Ideal|maximal]] iff its quotient is a field ([[Thm - Maximal and Prime Ideals via Quotients|via quotients]]). The full registry is on [[Commutative Algebra VI — Integral Extensions]].

---

# Statement

> **Theorem (units and fields in an integral extension).** Let $A \subseteq B$ be an integral extension of rings.
>
> 1. **(Unit comparison.)** $A \cap B^\times = A^\times$: an element of $A$ that is invertible in $B$ is already invertible in $A$.
> 2. **(Field criterion.)** If $A$ and $B$ are integral domains, then $B$ is a field if and only if $A$ is a field.

> **Corollary (maximality transfer).** Let $A \subseteq B$ be integral and $\mathfrak q \trianglelefteq B$ a prime with contraction $\mathfrak p = \mathfrak q \cap A$. Then $\mathfrak q$ is maximal in $B$ if and only if $\mathfrak p$ is maximal in $A$.

---

# Motivation

This theorem is the bridge from the module-theoretic core of the chapter to the *prime-ideal* theory that dominates everything downstream — going-up, lying-over, the Nullstellensatz, dimension. Up to now integrality has been about finiteness of modules. Here it cashes out as a statement about *invertibility and maximal ideals*, and the cash value is large: it says an integral extension cannot turn a non-field into a field at the bottom or top without doing so at the other end, and dually that maximal ideals correspond to maximal ideals across the extension. Closed points map to closed points.

The intuition is that integrality keeps the two rings "the same size" in the sense that matters for fields. A field is a ring with no room — only $0$ and the whole ring as ideals. If $B$ is a field and $A \subseteq B$ is integral, then $A$ inherits enough of $B$'s invertibility to be a field too, because the integral equation of an element of $B$ lets you solve for its inverse *inside $A$*. Conversely if $A$ is a field, $B$ is forced to be a field because every nonzero $b \in B$ satisfies a minimal monic equation whose constant term, being nonzero, is invertible in $A$ — and that invertibility propagates an inverse for $b$. Both directions are short manipulations of an integral equation, and both are instances of the single mechanism "a monic equation lets you express inverses".

The reason this matters is the corollary. Maximality of an ideal is field-ness of a quotient ([[Thm - Maximal and Prime Ideals via Quotients|the quotient dictionary]]), and quotients of an integral extension are again integral. So "field iff field" upstairs/downstairs becomes "maximal iff maximal" upstairs/downstairs — the statement that a finite map sends closed points to closed points and that the fibre over a closed point is a finite set of closed points. This is the seed of **Cohen–Seidenberg** (going-up) and the engine of **Zariski's lemma**, the linchpin of the Nullstellensatz: a field that is a finitely generated algebra over a field $k$ is finite over $k$, proved by feeding Noether normalization into this field criterion. Without this theorem the entire prime-ideal theory of finite maps would have no foundation.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "integral extension of domains" plus a field/maximality question, reached as follows.

The first disguised source is **a finite extension of a field**. The property $B$ is "$B$ is a domain, finite-dimensional over a field $A = k$". Finite $\Rightarrow$ integral, so the criterion applies and $B$ is a field — recovering "a domain finite over a field is a field". Nonobvious because it gives the field-theoretic fact $k[\alpha] = k(\alpha)$ for algebraic $\alpha$ from a general principle. *Example problem:* show an integral domain integral over a field is a field (Atiyah–Macdonald 5.7).

The second disguised source is **a prime of $B$ over a maximal of $A$, or vice versa**. The property $B$ is "$\mathfrak p = \mathfrak q \cap A$ is maximal" (resp. $\mathfrak q$ maximal). Passing to the integral extension of domains $A/\mathfrak p \hookrightarrow B/\mathfrak q$ and applying the field criterion transfers maximality. Nonobvious because maximality *downstairs* controls maximality *upstairs* through a quotient. *Example problem:* in $\mathbb{Z} \subseteq \mathbb{Z}[i]$, primes over a maximal $(p)$ are maximal.

The third disguised source is **a unit in the big ring with a small-ring witness**. The property $B$ is "$a \in A$ has an inverse $b \in B$". Part 1 produces the inverse inside $A$ by multiplying $b$'s integral equation by a high power of $a$. Nonobvious because invertibility "leaks downward" through the integral structure. *Example problem:* in $\mathbb{Z}[\sqrt2] \supseteq \mathbb{Z}$, an integer invertible in $\mathbb{Z}[\sqrt2]$ is $\pm 1$.

**Targets (Output Amplification)**

The conclusion is "field iff field / maximal iff maximal / units agree".

Combine "maximal iff maximal" with **lying-over and surjectivity of $\operatorname{Spec}$**. Once closed points correspond, and (going-up) every prime of $A$ is hit, $\operatorname{Spec} B \to \operatorname{Spec} A$ is surjective and sends maximals to maximals. The further result $E$ is that a finite map is *surjective on points and closed*; the maximality transfer is the closed-points half. Nonobvious because it upgrades a single quotient computation to a statement about the whole spectrum map. (Developed in [[Commutative Algebra VIII — Going Up and Going Down]].)

Combine "field iff field" with **Noether normalization**. A finite-type algebra that is a field is, by Noether normalization, finite over a polynomial subring $k[y_1, \dots, y_d]$, which must itself be a field — forcing $d = 0$, so the algebra is finite over $k$. The further result $E$ is **Zariski's lemma**, hence the **Nullstellensatz**. Nonobvious because it converts "finitely generated field over $k$" into "finite over $k$" via the criterion. (Developed in [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz]].)

Combine "units agree" with **dimension preservation**. Because maximals correspond and chains of primes lift (going-up/incomparability), integral extensions preserve Krull dimension. The further result $E$ is $\dim B = \dim A$ for integral $A \subseteq B$ — finite maps do not change dimension. Nonobvious because it turns a pointwise (maximality) statement into a global (dimension) one. (Developed in [[Commutative Algebra VIII — Going Up and Going Down]].)

---

# Why Is It True

**Every claim is "an integral equation lets you solve for an inverse, with the solution landing in the smaller ring".** Run the mechanism three ways.

*Part 1, units agree.* Let $a \in A$ have inverse $b \in B$, so $ab = 1$. Since $b$ is integral, $b^n + a_1 b^{n-1} + \cdots + a_n = 0$ with $a_i \in A$. Multiply by $a^{n-1}$ and use $a^k b^k = (ab)^k = 1$, i.e. $a^{n-1} b^{n-j} = a^{j-1} \cdot (a^{n-j}b^{n-j}) = a^{j-1}$:
$$b + a_1 + a_2 a + a_3 a^2 + \cdots + a_n a^{n-1} = 0,$$
so $b = -(a_1 + a_2 a + \cdots + a_n a^{n-1}) \in A$. The inverse of $a$ was secretly in $A$ all along; integrality is what let you write it as a polynomial in $a$.

*Part 2, "$B$ field $\Rightarrow$ $A$ field".* Take $0 \neq a \in A \subseteq B$. Since $B$ is a field, $a$ has an inverse in $B$, i.e. $a \in A \cap B^\times$; by part 1, $a \in A^\times$. So every nonzero element of $A$ is a unit: $A$ is a field.

*Part 2, "$A$ field $\Rightarrow$ $B$ field".* Take $0 \neq b \in B$. Pick its integral equation of *minimal* degree, $b^n + a_1 b^{n-1} + \cdots + a_n = 0$. Then $a_n \neq 0$: otherwise $b(b^{n-1} + a_1 b^{n-2} + \cdots + a_{n-1}) = 0$, and since $B$ is a domain and $b \neq 0$, the bracket vanishes — a lower-degree integral equation, contradicting minimality. Now solve:
$$b\,(b^{n-1} + a_1 b^{n-2} + \cdots + a_{n-1}) = -a_n,$$
and $a_n \in A$ is nonzero, hence invertible because $A$ is a field. So $b \cdot \big({-a_n^{-1}}(b^{n-1} + \cdots + a_{n-1})\big) = 1$: $b$ is invertible in $B$. Every nonzero element of $B$ is a unit: $B$ is a field.

**The one-line mechanism: a minimal integral equation has a nonzero constant term $a_n$ (else you could cancel a factor of the element in the domain), and the equation rearranges to "element times something $= -a_n$" — so invertibility of $a_n$ (guaranteed when the base is a field) hands you the inverse.** The domain hypothesis is exactly what makes "minimal degree forces $a_n \neq 0$" work, by allowing cancellation of $b$.

The corollary is the field criterion seen through quotients. $\mathfrak q$ maximal $\iff B/\mathfrak q$ a field; $\mathfrak p$ maximal $\iff A/\mathfrak p$ a field. The quotient extension $A/\mathfrak p \hookrightarrow B/\mathfrak q$ is integral (reduce monic equations mod $\mathfrak q$) and both quotients are domains (the contracted/quotiented primes are prime), so by part 2, $B/\mathfrak q$ is a field iff $A/\mathfrak p$ is — i.e. $\mathfrak q$ maximal iff $\mathfrak p$ maximal.

---

# What Makes This Hard

The crux is the direction "$A$ field $\Rightarrow$ $B$ field", and the non-obvious step is taking the integral equation of *minimal degree* and proving its constant term $a_n$ is nonzero — which needs the domain hypothesis to cancel a factor of $b$. People who take an arbitrary (non-minimal) equation get stuck because $a_n$ might be $0$, leaving nothing to invert. The most common error is to drop the "domains" hypothesis: without it, $a_n = 0$ can persist and the conclusion genuinely fails (e.g. $k \subseteq k \times k$ is integral, $k$ is a field, but $k \times k$ is not — it is not a domain, so the theorem does not apply, and indeed the conclusion is false). The unit-comparison part 1 hides a similar subtlety: the multiplication by $a^{n-1}$ must be paired correctly with $ab = 1$ to collapse all the mixed terms into $A$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Prove unit comparison by multiplying the inverse's integral equation by a high power of the element, collapsing it into the small ring. Get "$B$ field $\Rightarrow A$ field" immediately from unit comparison. Get "$A$ field $\Rightarrow B$ field" by taking a minimal integral equation, using the domain to force a nonzero constant term, and solving for the inverse. Deduce the maximality corollary by passing to quotient domains and applying the field criterion.

**Subgoal decomposition:**

1. **Unit comparison.** Show $a \in A$, $ab = 1$ in $B$ $\Rightarrow b \in A$.
   - *Hint:* Multiply $b$'s integral equation by $a^{n-1}$ and use $a^k b^k = 1$ to land every term in $A$.
   - *Why needed:* It gives "$B$ field $\Rightarrow A$ field" for free and is the units-agree statement.

2. **$A$ field $\Rightarrow B$ field.** Show every $0 \neq b \in B$ is invertible.
   - *Hint:* Take a *minimal* integral equation; the domain hypothesis forces the constant term $a_n \neq 0$; rearrange to $b \cdot (\cdots) = -a_n$ and invert $a_n$ in the field $A$.
   - *Why needed:* It is the hard direction; minimality $+$ domain is the whole trick.

3. **Maximality transfer.** Deduce $\mathfrak q$ maximal $\iff \mathfrak p = \mathfrak q \cap A$ maximal.
   - *Hint:* $A/\mathfrak p \hookrightarrow B/\mathfrak q$ is an integral extension of domains; apply the [[Thm - Maximal and Prime Ideals via Quotients|quotient dictionary]] and part 2.
   - *Why needed:* It is the corollary feeding going-up and the Nullstellensatz.

---

# Lemma Decomposition

> [!note]- Lemma 1: Unit comparison $A \cap B^\times = A^\times$
> **Statement:** If $A \subseteq B$ is integral and $a \in A$ has an inverse $b \in B$, then $b \in A$, so $a \in A^\times$.
>
> **Hint:** Multiply $b$'s integral equation by $a^{n-1}$; use $ab = 1$ to turn $a^{n-1}b^{n-k}$ into a power of $a$.
>
> **Why needed:** It is part 1 and immediately yields "$B$ field $\Rightarrow A$ field".
>
> > [!note]- Full proof
> > The inclusion $A^\times \subseteq A \cap B^\times$ is clear. Conversely let $a \in A \cap B^\times$ with $ab = 1$, $b \in B$. As $b$ is integral over $A$,
> > $$b^n + a_1 b^{n-1} + \cdots + a_{n-1} b + a_n = 0, \qquad a_i \in A.$$
> > Multiply by $a^{n-1}$. Using $ab = 1$, we have $a^{n-1} b^{n-k} = a^{n-1} b^{n} b^{-k}$... more directly, $a^{n-1} b^{n-k} = (ab)^{n-k} a^{k-1} = a^{k-1}$ for $0 \leq k \leq n$ (taking $b^0 = 1$). Term by term:
> > $$a^{n-1}b^n = a^{-1} = b,\quad a^{n-1}(a_1 b^{n-1}) = a_1,\quad a^{n-1}(a_2 b^{n-2}) = a_2 a,\ \dots,\ a^{n-1} a_n = a_n a^{n-1}.$$
> > So the equation becomes $b + a_1 + a_2 a + \cdots + a_n a^{n-1} = 0$, giving
> > $$b = -\big(a_1 + a_2 a + a_3 a^2 + \cdots + a_n a^{n-1}\big) \in A.$$
> > Hence $a$ has its inverse in $A$, i.e. $a \in A^\times$.

> [!note]- Lemma 2: $B$ field $\Rightarrow$ $A$ field
> **Statement:** If $A \subseteq B$ is integral, both domains, and $B$ is a field, then $A$ is a field.
>
> **Hint:** A nonzero $a \in A$ is invertible in the field $B$; apply Lemma 1.
>
> **Why needed:** It is the easy half of the field criterion.
>
> > [!note]- Full proof
> > Let $0 \neq a \in A$. Since $A \subseteq B$ and $B$ is a field, $a$ has an inverse in $B$, so $a \in A \cap B^\times$. By Lemma 1, $a \in A^\times$. As $a$ was an arbitrary nonzero element and $A$ is nonzero, $A$ is a field.

> [!note]- Lemma 3: $A$ field $\Rightarrow$ $B$ field
> **Statement:** If $A \subseteq B$ is integral, both domains, and $A$ is a field, then $B$ is a field.
>
> **Hint:** Take a minimal-degree integral equation; the domain forces the constant term nonzero; solve for the inverse using that $A$ is a field.
>
> **Why needed:** It is the hard half; minimality plus the domain hypothesis is the entire mechanism.
>
> > [!note]- Full proof
> > Let $0 \neq b \in B$. Among all integral equations for $b$, choose one of minimal degree $n$:
> > $$b^n + a_1 b^{n-1} + \cdots + a_{n-1} b + a_n = 0, \qquad a_i \in A.$$
> > *Claim $a_n \neq 0$.* If $a_n = 0$, then $b(b^{n-1} + a_1 b^{n-2} + \cdots + a_{n-1}) = 0$; since $B$ is a domain and $b \neq 0$, the bracket is $0$, giving a monic integral equation for $b$ of degree $n - 1$ — contradicting minimality. So $a_n \neq 0$.
> >
> > Rearrange the equation as
> > $$b\,\big(b^{n-1} + a_1 b^{n-2} + \cdots + a_{n-1}\big) = -a_n.$$
> > Since $a_n \in A$ is nonzero and $A$ is a field, $a_n^{-1} \in A \subseteq B$. Therefore
> > $$b \cdot \Big({-a_n^{-1}}\big(b^{n-1} + a_1 b^{n-2} + \cdots + a_{n-1}\big)\Big) = 1,$$
> > so $b$ is invertible in $B$. As $b$ was an arbitrary nonzero element, $B$ is a field.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $A \subseteq B$ be an integral extension.
>
> ---
> **Part 1 (unit comparison).** This is Lemma 1: $A \cap B^\times = A^\times$, the inverse of $a \in A \cap B^\times$ being $-(a_1 + a_2 a + \cdots + a_n a^{n-1}) \in A$.
>
> ---
> **Part 2 (field criterion), $A, B$ domains.** ($\Leftarrow$) If $A$ is a field, $B$ is a field by Lemma 3. ($\Rightarrow$) If $B$ is a field, $A$ is a field by Lemma 2. $\blacksquare$
>
> ---
> **Corollary (maximality transfer).** Let $\mathfrak q \trianglelefteq B$ be prime, $\mathfrak p = \mathfrak q \cap A$.
>
> The composite $A \hookrightarrow B \twoheadrightarrow B/\mathfrak q$ has kernel $\mathfrak q \cap A = \mathfrak p$, inducing an injection $A/\mathfrak p \hookrightarrow B/\mathfrak q$. Both quotients are integral domains ($\mathfrak p, \mathfrak q$ are prime). The extension $A/\mathfrak p \hookrightarrow B/\mathfrak q$ is integral: any $b \in B$ satisfies a monic equation over $A$, and reducing mod $\mathfrak q$ gives a monic equation for $b + \mathfrak q$ over $A/\mathfrak p$.
>
> By the [[Thm - Maximal and Prime Ideals via Quotients|quotient dictionary]], $\mathfrak q$ is maximal $\iff B/\mathfrak q$ is a field, and $\mathfrak p$ is maximal $\iff A/\mathfrak p$ is a field. By Part 2 applied to $A/\mathfrak p \hookrightarrow B/\mathfrak q$, $B/\mathfrak q$ is a field $\iff A/\mathfrak p$ is a field. Chaining, $\mathfrak q$ is maximal $\iff \mathfrak p$ is maximal. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**A domain integral over a field is a field.** The case $A = k$ a field, $B$ a domain integral over $k$: by part 2, $B$ is a field. This recovers $k[\alpha] = k(\alpha)$ for $\alpha$ algebraic over $k$ — adjoining an algebraic element to a field already gives a field, no inversion needed. The application is nonobvious because the familiar field-theory fact is a special case of a ring-theoretic principle, and the proof (minimal polynomial, nonzero constant term) is the field-theory proof in disguise.

**Zariski's lemma and the Nullstellensatz.** If a field $L$ is finitely generated as a $k$-algebra, Noether normalization makes $L$ finite (hence integral) over a polynomial subring $k[y_1, \dots, y_d]$; by part 2, that subring must be a field, forcing $d = 0$, so $L$ is finite over $k$. This is **Zariski's lemma**, the heart of the Nullstellensatz. The application is nonobvious because the field criterion is the precise gear converting "finitely generated field" into "finite extension".

**Splitting of primes in $\mathbb{Z}[i]$.** For $\mathbb{Z} \subseteq \mathbb{Z}[i]$ (integral, both domains), the maximality transfer says a Gaussian prime $\mathfrak q$ over $(p)$ is maximal, so $\mathbb{Z}[i]/\mathfrak q$ is a finite field — letting one read off how rational primes split ($p \equiv 1 \pmod 4$ splits, $p \equiv 3$ stays inert). The application is nonobvious because the abstract corollary controls the very concrete arithmetic of Gaussian primes.

**Hilbert's Nullstellensatz as "maximal ideals are points".** Over $\mathbb{C}$, the maximality transfer plus Zariski's lemma show every maximal ideal of $\mathbb{C}[x_1, \dots, x_n]$ has residue field $\mathbb{C}$, hence is $(x_1 - a_1, \dots, x_n - a_n)$ for a point $a$. The application is nonobvious because the field criterion is what forces the residue field to be exactly $\mathbb{C}$, identifying maximal ideals with points.

---

# Bridges

- **[[Thm - Maximal and Prime Ideals via Quotients|Maximal and prime ideals via quotients]]** — the tool that converts the field criterion into the maximality corollary. "Maximal $\iff$ field quotient" is applied to both $A/\mathfrak p$ and $B/\mathfrak q$, and the integral extension between these quotients lets part 2 transfer field-ness, hence maximality. The two theorems together say closed points correspond under finite maps.

- **[[Thm - Characterizations of Integrality (Module-Finite Criterion)|The module-finite criterion]]** — supplies the integral equations this theorem manipulates, and underlies "finite $\Rightarrow$ integral" so that finite extensions of fields fall under the field criterion. The minimal-degree integral equation used in Lemma 3 is the analogue of the minimal polynomial.

- **Going-up and lying-over** — the maximality transfer is the closed-points case of the general statement that $\operatorname{Spec} B \to \operatorname{Spec} A$ is surjective and well-behaved on chains. Developed fully in [[Commutative Algebra VIII — Going Up and Going Down]], where this corollary is one of the base cases.

- **Zariski's lemma / the Nullstellensatz** — the field criterion is the final step of Zariski's lemma: a finitely generated $k$-algebra that is a field is finite over $k$, because Noether normalization plus part 2 force the polynomial subring to be a field of transcendence degree $0$. See [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz]].

---

# Unlocked by This

> [!tip] Going-up, lying-over, and dimension *(from Commutative Algebra)*
> The maximality transfer is the closed-point case of the **Cohen–Seidenberg theorems**: $\operatorname{Spec} B \to \operatorname{Spec} A$ is surjective (lying-over), chains lift (going-up), incomparable primes stay incomparable, and consequently $\dim B = \dim A$ — integral extensions preserve dimension. Geometrically, a finite map is surjective, closed, with finite fibres, and dimension-preserving. Developed in [[Commutative Algebra VIII — Going Up and Going Down]].

> [!tip] The Nullstellensatz and the algebra–geometry dictionary *(from Algebraic Geometry)*
> Via Zariski's lemma, the field criterion forces the residue field at a maximal ideal of $k[x_1, \dots, x_n]$ (for $k$ algebraically closed) to be $k$ itself — so **maximal ideals are exactly points** $(x_1 - a_1, \dots, x_n - a_n)$. This is the foundation of the **Nullstellensatz** and the entire dictionary between radical ideals and varieties; see [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz]].
