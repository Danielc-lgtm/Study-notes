---
type: definition
subject: ring-theory
prereqs:
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Unit and Field"
  - "Def - Integral Domain"
  - "Def - Polynomial Ring"
tags: [algebra, ring-theory]
---

# Notation

Throughout, $R$ is an [[Def - Integral Domain|integral domain]] — a non-zero commutative [[Def - Ring|ring]] with $1$ and no zero divisors. We write $\mathbb{Z}_{\geq 0}$ for the non-negative integers $\{0, 1, 2, \dots\}$, $R \setminus \{0\}$ for the non-zero elements of $R$, and $\varphi$ for a Euclidean function. For a field $F$, $F[X]$ is the [[Def - Polynomial Ring|polynomial ring]] and $\deg f$ the degree of a polynomial $f$. The ring $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$ is the **Gaussian integers**, a subring of $\mathbb{C}$, and $N(a + bi) = a^2 + b^2 = |a+bi|^2$ is its norm. The chapter symbol registry is on [[Rings II — §2.3–2.4]].

---

# Axiom Motivation

The single most powerful tool in elementary number theory is **division with remainder**: given integers $a$ and $b \neq 0$, you can write $a = bq + r$ with the remainder $r$ strictly smaller than $b$. Everything cascades from this — the Euclidean algorithm for greatest common divisors, Bézout's identity, the proof that every ideal of $\mathbb{Z}$ is principal, unique factorisation. The same machinery runs again, almost verbatim, for polynomials over a field, where "smaller" means "lower degree". A Euclidean domain is the abstraction that isolates *exactly* the structure these two examples share, so that all the cascading consequences can be proved once and for all.

So the design question is: what must an integral domain carry in order to support a division-with-remainder algorithm? We need two ingredients.

First, a notion of **size**. In $\mathbb{Z}$ the size of $n$ is $|n|$; in $F[X]$ the size of $f$ is $\deg f$. In both cases size is a non-negative integer, so we postulate a function $\varphi : R \setminus \{0\} \to \mathbb{Z}_{\geq 0}$. Why a non-negative integer and not, say, a real number? Because the entire force of the algorithm is that you cannot descend forever: a strictly decreasing sequence of non-negative integers must terminate. That well-foundedness is what makes the Euclidean algorithm *halt* and what makes induction-on-size arguments work. Real-valued sizes would not give a terminating algorithm; the codomain $\mathbb{Z}_{\geq 0}$ is not a convenience, it is the point. We exclude $0$ from the domain because $0$ has no sensible size — $\deg 0$ is conventionally $-\infty$, and $|0| = 0$ would clash with the next axiom.

Second, the **division property** itself: for any $a$ and any $b \neq 0$ there exist a quotient $q$ and remainder $r$ with
$$a = bq + r, \qquad r = 0 \ \text{ or } \ \varphi(r) < \varphi(b).$$
The escape clause "$r = 0$ or $\varphi(r) < \varphi(b)$" is the crucial shape. We *want* to be able to drive the remainder down, and the way an algorithm makes progress is by replacing a pair by a strictly smaller one. So the remainder must either vanish — success — or be genuinely smaller in $\varphi$ than the divisor $b$. If we dropped the strict inequality and only asked $\varphi(r) \le \varphi(b)$, the algorithm could stall, cycling without ever shrinking. The strictness is what guarantees termination, hand in hand with the well-foundedness of $\mathbb{Z}_{\geq 0}$.

There is a third condition, often stated and sometimes presented as optional: $\varphi(ab) \ge \varphi(b)$ for all non-zero $a, b$, i.e. **multiplying by something cannot decrease size**. What is this for? It is a compatibility axiom between $\varphi$ and the multiplicative structure, and it pins down the units and the smallest elements. From it, the elements of *minimal* $\varphi$-value are precisely the units: a unit $u$ satisfies $\varphi(b) = \varphi(u^{-1} u b) \ge \varphi(ub) \ge \varphi(b)$, so $\varphi$ is constant along associates, and one shows the minimum value is attained exactly on $R^\times$. Without this axiom the Euclidean function could behave erratically and the clean statement "smallest size = unit" would fail. (Some authors drop this condition because the principal-ideal-domain consequence survives without it; we keep it, as the Cambridge course does, because it makes $\varphi$ genuinely a measure of size.)

To see that the definition is *exactly right* and not a nearby variant, look ahead to its payoff theorem: **every Euclidean domain is a [[Def - Principal Ideal Domain|principal ideal domain]]**. The proof takes a non-zero ideal $I$, picks $b \in I$ with $\varphi(b)$ *minimal*, and shows $I = (b)$ — for any $a \in I$, divide $a = bq + r$; then $r = a - bq \in I$, and if $r \neq 0$ then $\varphi(r) < \varphi(b)$ would contradict minimality, so $r = 0$ and $a \in (b)$. Every clause of the definition is consumed: the codomain $\mathbb{Z}_{\geq 0}$ so that "minimal $\varphi$" exists; the division property so that $a = bq + r$; the *strict* inequality so that the contradiction with minimality bites. Weaken any one and the theorem breaks. That is the precise sense in which a Euclidean domain is the right abstraction: it is the minimal structure on which the "pick the smallest element of the ideal" argument runs.

---

# The Definition

An [[Def - Integral Domain|integral domain]] $R$ is a **Euclidean domain** if there exists a function
$$\varphi : R \setminus \{0\} \longrightarrow \mathbb{Z}_{\geq 0},$$
called a **Euclidean function**, satisfying:

1. **Multiplicativity bound.** For all non-zero $a, b \in R$,
$$\varphi(ab) \geq \varphi(b).$$

2. **Division with remainder.** For all $a, b \in R$ with $b \neq 0$, there exist $q, r \in R$ — a **quotient** and a **remainder** — such that
$$a = bq + r, \qquad \text{and either } r = 0 \text{ or } \varphi(r) < \varphi(b).$$

The quotient and remainder need **not** be unique (they are unique in $\mathbb{Z}$ and $F[X]$, but uniqueness is not part of the definition and fails in $\mathbb{Z}[i]$). A ring may admit several different Euclidean functions; being a Euclidean domain only requires that *at least one* exists.

---

# Relate to Other Fields / Compression

A Euclidean domain is the algebraic distillation of the **Euclidean algorithm** itself — the oldest algorithm in mathematics, the repeated-division procedure for greatest common divisors in Euclid's *Elements*. Every occurrence of the phrase "Euclidean algorithm" in a first course — for integers, for polynomials over a field — is an instance of this single structure, and the definition exists so the algorithm and its consequences need be justified only once.

The right way to compress the definition is as a **well-founded size function compatible with division**. Strip away the ring and you are left with the bare engine of every terminating recursion in mathematics: a function into a well-ordered set such that each step strictly decreases the value. Computer scientists call such a function a *termination measure* or *variant*; the Euclidean function is exactly that variant, and the codomain $\mathbb{Z}_{\geq 0}$ is chosen for the same reason a loop variant is chosen to be a natural number — so that strict descent forces halting. From this angle "Euclidean domain" is "integral domain plus a termination measure for division", and the principal-ideal-domain theorem is the statement that a termination measure for division automatically gives a termination measure for the descending-ideal argument.

Specialised to $\mathbb{Z}$ with $\varphi = |\cdot|$, the structure is ordinary arithmetic. Specialised to $F[X]$ with $\varphi = \deg$, it is polynomial long division. Specialised to $\mathbb{Z}[i]$ with $\varphi = N$, it is a geometric "round to the nearest lattice point" procedure in the complex plane. These are not analogies — they are the *same* definition with $\varphi$ instantiated three ways, which is the whole reason the abstraction earns its keep.

---

# Examples / Corollaries

**Is an instance — $\mathbb{Z}$ with $\varphi(n) = |n|$.** Division with remainder is the familiar fact that any integer $a$ can be written $a = bq + r$ with $0 \le r < |b|$, and the bound $|ab| = |a||b| \ge |b|$ holds since $|a| \ge 1$ for non-zero $a$. This is the prototype; every clause of the definition was reverse-engineered from it.

**Is an instance — $F[X]$ for a field $F$, with $\varphi(f) = \deg f$.** Polynomial long division over a field produces $f = gq + r$ with $\deg r < \deg g$ (or $r = 0$); the field hypothesis is exactly what lets you divide by the leading coefficient of $g$ at each step. The degree bound $\deg(fg) = \deg f + \deg g \ge \deg g$ holds because there are no zero divisors. Note $F$ must be a field: $\mathbb{Z}[X]$ is *not* a Euclidean domain, because you cannot in general divide by a polynomial with non-unit leading coefficient (you cannot divide $X$ by $2$ inside $\mathbb{Z}[X]$).

**Is an instance — the Gaussian integers $\mathbb{Z}[i]$ with $\varphi(z) = N(z) = |z|^2$.**

> [!note]- Verification that $\mathbb{Z}[i]$ is a Euclidean domain
> *Multiplicativity bound.* The norm is multiplicative, $N(zw) = N(z)N(w)$, and $N(w) \ge 1$ for $w \neq 0$, so $\varphi(zw) = N(z)N(w) \ge N(z) = \varphi(z)$.
>
> *Division with remainder.* Given $a, b \in \mathbb{Z}[i]$ with $b \neq 0$, form the genuine complex quotient $\tfrac{a}{b} \in \mathbb{C}$. The Gaussian integers form a unit square lattice in the plane, and every point of $\mathbb{C}$ lies within distance $\le \tfrac{1}{\sqrt 2} < 1$ of some lattice point. Pick a lattice point $q \in \mathbb{Z}[i]$ with $\bigl|\tfrac{a}{b} - q\bigr| < 1$, and write $\tfrac{a}{b} = q + c$ with $|c| < 1$. Then
> $$a = bq + bc, \qquad r := bc = a - bq \in \mathbb{Z}[i],$$
> and $\varphi(r) = N(bc) = N(b)N(c) = N(b)|c|^2 < N(b) = \varphi(b)$. So division with remainder holds. (Here $q$ and $r$ are genuinely non-unique: a complex number can be within distance $1$ of several lattice points.)
>
> The argument used nothing about $\mathbb{Z}[i]$ beyond "it is a subring of $\mathbb{C}$ such that every complex number is within distance $< 1$ of a point of the ring". The same proof makes $\mathbb{Z}[\omega]$ (the Eisenstein integers, $\omega = e^{2\pi i/3}$) a Euclidean domain — but it visibly *fails* for $\mathbb{Z}[\sqrt{-5}]$, whose lattice is too stretched: there are complex points more than distance $1$ from every lattice point.

**Is NOT an instance — $\mathbb{Z}[X]$.** The polynomial ring over the integers is an integral domain but admits no Euclidean function. Concretely, there is no way to "divide $X$ by $2$ with a smaller remainder": any expression $X = 2q + r$ in $\mathbb{Z}[X]$ has $r = X - 2q$, and no choice of $q \in \mathbb{Z}[X]$ makes $r$ vanish or shrink in a way consistent with a Euclidean function. The deeper reason is that $\mathbb{Z}[X]$ is not even a [[Def - Principal Ideal Domain|principal ideal domain]] — the ideal $(2, X)$ is not principal — and every Euclidean domain *is* a PID, so $\mathbb{Z}[X]$ cannot be Euclidean.

**Is NOT an instance — $\mathbb{Z}[\sqrt{-5}]$.** This integral domain is not a Euclidean domain; indeed it is not even a [[Def - Unique Factorization Domain|unique factorization domain]] (the element $6$ has two distinct irreducible factorisations $2 \cdot 3 = (1+\sqrt{-5})(1-\sqrt{-5})$). Since every Euclidean domain is a PID and every PID is a UFD, failure of unique factorisation rules out a Euclidean function. Geometrically, the lattice $\mathbb{Z}[\sqrt{-5}]$ in $\mathbb{C}$ is too sparse for the "nearest lattice point" argument that worked for $\mathbb{Z}[i]$.

**Corollary — the units of $R$ are the elements of minimal $\varphi$-value.** Using the bound $\varphi(ab) \ge \varphi(b)$: if $u$ is a unit then for any $b \neq 0$, $\varphi(b) = \varphi(u^{-1}(ub)) \ge \varphi(ub) \ge \varphi(b)$, forcing equality, so $\varphi$ is constant on each associate class and the units realise the minimum. This is a calibration check on axiom 1: if you can derive it, you understand why the multiplicativity bound is in the definition.

**Corollary — every Euclidean domain is a principal ideal domain.** Given a non-zero ideal $I$, pick $b \in I \setminus \{0\}$ with $\varphi(b)$ minimal; for any $a \in I$ write $a = bq + r$, note $r = a - bq \in I$, and conclude $r = 0$ (else $\varphi(r) < \varphi(b)$ contradicts minimality), so $a \in (b)$ and $I = (b)$. See [[Thm - Euclidean Domains are Principal Ideal Domains]] for the full statement. This is *the* reason the definition matters.

**Calibration check.** Verify that any field $F$ is trivially a Euclidean domain (take $\varphi \equiv 0$, or any constant; division is exact since $b \neq 0$ is invertible, $a = b(b^{-1}a) + 0$). Verify that the quotient and remainder for $a = 7, b = 5$ in $\mathbb{Z}$ are $q = 1, r = 2$, but for $a = -7$ they are $q = -2, r = 3$ — the remainder is kept non-negative, not nearest. Verify that in $\mathbb{Z}[i]$, dividing $3 + 2i$ by $1 + i$ admits more than one valid $(q, r)$. If you can also explain why the codomain *must* be $\mathbb{Z}_{\geq 0}$ rather than $\mathbb{R}_{\geq 0}$ — termination of descent — the definition has landed.

---

# Unlocked by This

> [!tip] Euclidean Domains are Principal Ideal Domains *(from this topic)*
> The Euclidean function directly forces every ideal to be principal: take the ideal element of minimal $\varphi$-value and divide everything else by it. See [[Thm - Euclidean Domains are Principal Ideal Domains]]. This is the first link in the chain Euclidean $\subseteq$ PID $\subseteq$ UFD.

> [!tip] Principal Ideal Domain *(from this topic)*
> A Euclidean domain is the most accessible source of [[Def - Principal Ideal Domain|principal ideal domains]] — and via the chain to [[Def - Unique Factorization Domain|unique factorization domains]], the cleanest sufficient condition for unique factorisation. To *prove* a given ring is a PID, by far the easiest route is to exhibit a Euclidean function on it.

> [!tip] Computing greatest common divisors *(from this topic)*
> The Euclidean function makes the [[Def - Greatest Common Divisor and Least Common Multiple|greatest common divisor]] genuinely *computable*: iterate division with remainder, and the strictly decreasing $\varphi$-values guarantee the algorithm halts, terminating at a gcd.
