---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Residue"
  - "Def - Removable Singularity, Pole, Essential Singularity"
tags: [analysis, complex-analysis]
---

# Notation

$f$ holomorphic on $D(a, R) \setminus \{a\}$ with isolated singularity at $a$. $g, h$ are holomorphic, $k$ is a positive integer (pole order). Full registry on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Motivation

The residue theorem reduces contour integrals to sums of residues — but only if you can *compute* the residues. The residue at an isolated singularity is, by definition, the coefficient $c_{-1}$ of the Laurent expansion. In principle this requires constructing the entire Laurent expansion; in practice, several standard formulas collapse the residue computation to one or two derivative evaluations.

These formulas are the daily-use tools of complex analysis. Without them, residue computation would be slow (compute the Laurent expansion, read off $c_{-1}$); with them, residues become a routine bit of calculus. The three main formulas — simple pole limit, simple pole as quotient, higher-order pole derivative — handle the vast majority of cases that arise in practice.

The reason these formulas work is the Laurent-expansion-structure of singularities. At a pole of order $k$, $f(z) = (z - a)^{-k} g(z)$ for $g$ holomorphic with $g(a) \neq 0$. The Laurent coefficients $c_{-k}, c_{-k+1}, \ldots, c_{-1}, c_0, c_1, \ldots$ are exactly the Taylor coefficients of $g$ shifted: $c_{-k + m} = g^{(m)}(a)/m!$. In particular, the residue $c_{-1} = g^{(k - 1)}(a)/(k-1)!$. Multiplying by $(z - a)^k$ and taking $(k-1)$ derivatives extracts the residue from the polynomial $g$.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "you know the order of the pole (and want its residue)". Sources broaden recognition.

**A function written as $g(z)/(z - a)^k$ with $g$ holomorphic at $a$ and $g(a) \neq 0$.** This is the canonical pole-of-order-$k$ factored form. Apply the higher-order pole formula directly.

**A function written as $g(z)/h(z)$ with $g, h$ holomorphic, $h(a) = 0, h'(a) \neq 0, g(a) \neq 0$.** Simple pole. Formula: $\operatorname{Res}_a(g/h) = g(a)/h'(a)$.

**A function written as $g(z)/h(z)$ where $h$ has a higher-order zero at $a$.** Need to use the higher-order pole formula or factor out $(z - a)^k$.

**An essential singularity where you want $c_{-1}$ of the Laurent expansion.** No closed-form shortcut; expand the Laurent series and read off $c_{-1}$ directly.

**Targets (Output Amplification)**

Once you can compute residues:

- Apply the [[Thm - Residue Theorem|residue theorem]] to compute contour integrals.
- Apply the [[Thm - Argument Principle|argument principle]] to count zeros and poles.
- Apply [[Thm - Real Rational Integrals via Residues|real integral techniques]] by closing contours.
- Sum series via residue at integers of $\pi\cot(\pi z) g(z)$.

---

# Why Is It True

**Simple pole, limit form.** At a simple pole, $f(z) = c_{-1}/(z - a) + c_0 + c_1(z - a) + \ldots$, so $(z - a) f(z) = c_{-1} + c_0(z - a) + \ldots \to c_{-1}$ as $z \to a$. The limit picks out the residue.

**Higher-order pole, derivative form.** At a pole of order $k$, $f(z) = c_{-k}(z - a)^{-k} + \ldots + c_{-1}(z - a)^{-1} + c_0 + \ldots$. Multiply by $(z - a)^k$:
$$(z - a)^k f(z) = c_{-k} + c_{-k+1}(z - a) + \ldots + c_{-1}(z - a)^{k-1} + c_0 (z - a)^k + \ldots.$$
This is a Taylor series at $a$. Its $(k-1)$-th derivative evaluated at $a$ gives $(k-1)! \cdot c_{-1}$, so $c_{-1} = \frac{1}{(k-1)!}\lim_{z \to a}\frac{d^{k-1}}{dz^{k-1}}[(z - a)^k f(z)]$.

**Quotient form, simple pole.** If $f = g/h$ with $h(a) = 0, h'(a) \neq 0, g(a) \neq 0$, then $h(z) = h'(a)(z - a) + O((z - a)^2)$ near $a$. So $f(z) = g(z)/(h'(a)(z - a) + O((z-a)^2)) = g(z)/(h'(a)(z - a)) \cdot (1 + O(z - a)) = g(a)/(h'(a)(z - a)) + O(1)$ — a simple pole with residue $g(a)/h'(a)$. Cleaner: $(z - a) f(z) = (z - a) g(z)/h(z)$, and by L'Hôpital this limits to $g(a)/h'(a)$.

These three formulas are interrelated: the quotient form is the simple-pole limit applied to $f = g/h$; the higher-order derivative form generalizes the limit to higher orders.

---

# What Makes This Hard

The non-obvious step is **knowing which formula to use**: which case you're in, and how to massage $f$ into the right form. Confusion between order of pole (determines $k$) and order of zero of denominator (which can be different if numerator also vanishes) is common. The derivative formula for higher-order poles can be computationally heavy when $k$ is large or $f$ is complicated; sometimes it's easier to expand numerator/denominator in Taylor series and divide.

---

# Rederivation Scaffold

**High-level strategy:**
Identify the order of the pole. For simple poles, use the limit or quotient form. For higher-order poles, use the $(k-1)$-th derivative form. For essential singularities, expand the Laurent series directly.

**Subgoal decomposition:**

1. **Determine pole order $k$.** Factor out the pole: write $f(z) = (z - a)^{-k} g(z)$ with $g$ holomorphic and $g(a) \neq 0$.
   - *Hint:* Look at the zero order of $1/f$ at $a$, or factor explicitly.

2. **Apply the right formula.**
   - Simple pole: $\operatorname{Res}_a f = \lim_{z \to a}(z - a) f(z)$.
   - Simple pole as $g/h$ with simple zero of $h$: $\operatorname{Res}_a(g/h) = g(a)/h'(a)$.
   - Pole of order $k$: $\operatorname{Res}_a f = \frac{1}{(k-1)!}\lim_{z \to a}\frac{d^{k-1}}{dz^{k-1}}[(z - a)^k f(z)]$.
   - Essential: Laurent-expand and read $c_{-1}$.

3. **Compute the limit or derivative.** This is the calculus step.

---

# Formal Proof

> [!note]- Complete formal proof
>
> **(i) Simple pole formula.** Suppose $f$ has a simple pole at $a$, so $f(z) = \sum_{n \geq -1} c_n (z - a)^n$ with $c_{-1} \neq 0$. Then
> $$(z - a) f(z) = c_{-1} + c_0(z - a) + c_1(z - a)^2 + \ldots,$$
> which is a power series in $(z - a)$ (holomorphic at $a$, since the Laurent series of $f$ has lowest term $-1$). Evaluating at $z = a$: $\lim_{z \to a}(z - a) f(z) = c_{-1} = \operatorname{Res}_a f$.
>
> **(ii) Pole of order $k$ formula.** Suppose $f$ has a pole of order $k$ at $a$, so $f(z) = \sum_{n \geq -k} c_n(z - a)^n$. Then
> $$(z - a)^k f(z) = c_{-k} + c_{-k+1}(z - a) + \ldots + c_{-1}(z - a)^{k-1} + c_0(z - a)^k + \ldots,$$
> a power series at $a$. Differentiating $(k-1)$ times:
> $$\frac{d^{k-1}}{dz^{k-1}}[(z - a)^k f(z)] = (k-1)! c_{-1} + k! c_0 (z - a) + \ldots$$
> Evaluating at $z = a$: $\lim_{z \to a}\frac{d^{k-1}}{dz^{k-1}}[(z - a)^k f(z)] = (k-1)! c_{-1}$. Dividing: $\operatorname{Res}_a f = c_{-1} = \frac{1}{(k-1)!}\lim_{z \to a}\frac{d^{k-1}}{dz^{k-1}}[(z - a)^k f(z)]$.
>
> **(iii) Quotient formula for simple poles.** Suppose $f = g/h$ with $g, h$ holomorphic at $a$, $g(a) \neq 0$, $h(a) = 0$, and $h'(a) \neq 0$. Then $h$ has a simple zero at $a$, so $f$ has a simple pole. By (i),
> $$\operatorname{Res}_a f = \lim_{z \to a}(z - a) g(z)/h(z) = g(a) \cdot \lim_{z \to a}(z - a)/h(z).$$
> The Taylor expansion of $h$ at $a$ is $h(z) = h'(a)(z - a) + h''(a)(z - a)^2/2 + \ldots$, so $h(z)/(z - a) \to h'(a)$ as $z \to a$. Thus $\operatorname{Res}_a f = g(a)/h'(a)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Residues of trigonometric integrands.** Compute $\operatorname{Res}_0 \cot z = \operatorname{Res}_0 (\cos z / \sin z) = \cos 0 / (\sin)'(0) = 1$. Compute $\operatorname{Res}_0 (1/\sin z) = 1/(\cos 0) = 1$. These are basic building blocks for trigonometric contour integrals.

**Residues of exponential integrands.** $\operatorname{Res}_a (e^z/(z - a)^k) = e^a/(k-1)!$ by the derivative formula. Compute $\operatorname{Res}_0(e^z/z^3) = e^0/2! = 1/2$.

**Residues at higher-order poles, complicated cases.** $\operatorname{Res}_i 1/(z^2 + 1)^2 = ?$. The pole at $i$ is of order $2$: $1/(z^2 + 1)^2 = 1/((z - i)(z + i))^2$. $(z - i)^2 \cdot 1/((z - i)(z + i))^2 = 1/(z + i)^2$. Derivative at $z = i$: $d/dz[1/(z+i)^2] = -2/(z+i)^3$. At $z = i$: $-2/(2i)^3 = -2/(-8i) = 1/(4i) = -i/4$. So $\operatorname{Res}_i 1/(z^2+1)^2 = -i/4$.

**Residue at an essential singularity.** $\operatorname{Res}_0 e^{1/z} = $ coefficient of $1/z$ in $\sum z^{-n}/n! = 1$ (from the $n = 1$ term). $\operatorname{Res}_0 \sin(1/z) = $ coefficient of $1/z$ in $1/z - 1/(6z^3) + \ldots = 1$.

---

# Bridges

- **[[Def - Residue]]** — the object computed.

- **[[Thm - Residue Theorem]]** — application: residues are summed weighted by winding numbers.

- **[[Def - Removable Singularity, Pole, Essential Singularity]]** — the singularity type determines which formula to use.

- **[[Thm - Real Rational Integrals via Residues]]** — uses residue computation to evaluate real integrals.

---

# Unlocked by This

> [!tip] Practical Contour Integration *(from §3.4)*
> The residue formulas are what make contour integration a *computational* technique, not just a theoretical framework. Every contour integral exercise in §3.4 reduces to: identify poles, compute residues, apply residue theorem.
