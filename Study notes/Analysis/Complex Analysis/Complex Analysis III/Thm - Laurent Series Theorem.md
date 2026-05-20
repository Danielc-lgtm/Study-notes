---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Laurent Series"
  - "Def - Holomorphic Function"
  - "Thm - Cauchy's Theorem for Simply Connected Domains"
tags: [analysis, complex-analysis]
---

# Notation

$a \in \mathbb{C}$, $0 \leq r_0 < R_0 \leq \infty$, $A(a; r_0, R_0) = \{z : r_0 < |z - a| < R_0\}$. $f$ is holomorphic on $A(a; r_0, R_0)$. The Laurent coefficients are $c_n \in \mathbb{C}$ for $n \in \mathbb{Z}$. Full registry on [[Complex Analysis III — Winding, Laurent, Residues]].

---

# Motivation

A holomorphic function on a disc has a Taylor series — a power series converging on the disc and equal to the function pointwise. The Laurent series theorem is the analog for an *annular* domain: a function holomorphic on an annulus has a two-sided power series converging there.

This is the foundational result of singularity analysis. Without it, the Laurent expansion is just a formal object; with it, every function holomorphic on a punctured disc *has* a unique Laurent expansion, and the classification of singularities into removable/pole/essential becomes a structural theorem. All subsequent §3.3–§3.4 results — Riemann's removable singularity theorem, Casorati–Weierstrass, the residue theorem — rest on the Laurent series theorem.

The theorem also has a constructive flavor: the formula $c_n = (2\pi i)^{-1}\oint f(z)(z - a)^{-n-1}\,dz$ explicitly expresses each Laurent coefficient as a contour integral. So Laurent coefficients are computable, not just formal.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$f$ holomorphic on an annulus". The sources broaden this.

The first disguised source is **$f$ holomorphic on a punctured disc.** Property $B$: $f$ holomorphic on $D(a, R) \setminus \{a\}$. Bridge: a punctured disc is an annulus $A(a; 0, R)$. The Laurent theorem gives a unique expansion converging on the punctured disc; the structure of the negative-power part classifies the singularity.

The second disguised source is **$f$ holomorphic outside a compact set.** Property $B$: $f$ holomorphic on $\{|z| > R\}$. Bridge: this is an annulus $A(0; R, \infty)$. The Laurent expansion at $\infty$ gives information about behaviour at infinity — the coefficient $c_n$ for $n \geq 0$ gives polynomial-like growth, $c_n$ for $n < 0$ gives decay. Used in classifying behaviour of entire functions.

The third disguised source is **a meromorphic function on $\mathbb{C}$ with prescribed poles.** Property $B$: $f$ meromorphic on $\mathbb{C}$ with finitely many poles $a_1, \ldots, a_k$. Bridge: on each annulus $A(a_i; 0, \text{distance to nearest other pole})$, $f$ has a Laurent expansion. The principal parts at each $a_i$ characterize $f$ up to an entire function correction (Mittag-Leffler decomposition).

**Targets (Output Amplification)**

The conclusion is "$f$ has a unique Laurent expansion on the annulus, with coefficients given by a contour integral".

Combine with **Cauchy's integral formula structure.** Property $D$: the coefficient formula resembles a generalization of Cauchy's formula. Amplified result $E$: many specific function-theoretic identities — for instance, the Bessel function generating function $e^{(z/2)(t - 1/t)} = \sum J_n(z) t^n$ has $J_n(z) = (2\pi i)^{-1}\oint e^{(z/2)(t - 1/t)} t^{-n-1}\,dt$ by Laurent on $|t| > 0$.

Combine with **multiplication of holomorphic functions.** Property $D$: $f \cdot g$ for holomorphic $f, g$ on the annulus. Amplified result $E$: the Laurent coefficients of $fg$ are the *convolution* of the Laurent coefficients of $f$ and $g$. This is the discrete-Fourier-transform-like structure of Laurent expansion: multiplication of functions = convolution of coefficients.

Combine with **a sequence of holomorphic functions converging locally uniformly.** Property $D$: $f_n \to f$ locally uniformly on the annulus. Amplified result $E$: the Laurent coefficients of $f_n$ converge to those of $f$. The Laurent expansion is a continuous functional of the function (with respect to locally uniform convergence).

---

# Why Is It True

The proof has a beautiful Cauchy-integral-formula geometry. On the annulus, fix $w \in A(a; r_0, R_0)$. Choose radii $r_0 < \rho_1 < |w - a| < \rho_2 < R_0$. Consider the boundary of the sub-annulus $\{\rho_1 \leq |z - a| \leq \rho_2\}$ — this is the *difference* of two circles: $\gamma_2$ (outer, traversed counterclockwise) minus $\gamma_1$ (inner, traversed counterclockwise). The combined "cycle" $\gamma_2 - \gamma_1$ is homologous to zero in the larger annulus (because every external point has winding number zero), so Cauchy's integral formula applies:
$$f(w) = \frac{1}{2\pi i}\oint_{\gamma_2}\frac{f(z)}{z - w}\,dz - \frac{1}{2\pi i}\oint_{\gamma_1}\frac{f(z)}{z - w}\,dz.$$
The first integral is over the outer circle $|z - a| = \rho_2$, with $w$ inside. On this circle, $|z - a| > |w - a|$, so $1/(z - w) = 1/((z - a) - (w - a)) = \sum_{n \geq 0}(w - a)^n/(z - a)^{n+1}$ by geometric series. Substituting and integrating termwise (uniformly convergent on the compact circle) gives $\sum_{n \geq 0} c_n (w - a)^n$ with $c_n = (2\pi i)^{-1}\oint_{\gamma_2} f(z)/(z - a)^{n+1}\,dz$ — the regular part.

The second integral is over the inner circle, with $w$ outside. On this circle, $|z - a| < |w - a|$, so $1/(z - w) = -1/((w - a) - (z - a)) = -\sum_{n \geq 0}(z - a)^n/(w - a)^{n+1}$. Substituting (with appropriate sign) and integrating gives $\sum_{m \geq 1} c_{-m}(w - a)^{-m}$ with $c_{-m} = (2\pi i)^{-1}\oint_{\gamma_1} f(z)(z - a)^{m-1}\,dz$ — the principal part.

Adding, $f(w) = \sum_{n=-\infty}^\infty c_n (w - a)^n$. The coefficients $c_n$ are given by integrals over $\gamma_2$ for $n \geq 0$ and $\gamma_1$ for $n < 0$, but by Cauchy's theorem these can be unified to a single circle $|z - a| = \rho$ for any $\rho \in (r_0, R_0)$.

So Laurent's theorem is *Cauchy's theorem on the annulus, with two boundary circles*. The two circles play different roles — outer gives positive powers, inner gives negative powers — and their difference is what enables the two-sided expansion.

---

# What Makes This Hard

The non-obvious step is recognizing **the annulus's boundary as a "cycle" of two circles with opposite orientations**, and applying Cauchy's theorem to this cycle. The standard Cauchy theorem applies to a single closed curve; the annulus's boundary is naturally a difference of two circles, and learning to think of integrals as "outer minus inner" is the key conceptual move. A common error is to forget that the two expansions (geometric series of $1/(z - w)$ on the outer vs inner circle) go in *opposite directions* — the outer gives positive powers of $(w - a)$, the inner gives negative powers — and to confuse the signs in the resulting formulas.

---

# Rederivation Scaffold

**High-level strategy:**
For $w$ in the annulus, write $f(w)$ as a contour integral using Cauchy's formula on the boundary of a sub-annulus (outer minus inner circle). Expand $1/(z - w)$ as a geometric series on each circle — positive powers on the outer, negative powers on the inner — and integrate termwise.

**Subgoal decomposition:**

1. **Apply Cauchy's integral formula to the sub-annulus.** Choose $r_0 < \rho_1 < |w - a| < \rho_2 < R_0$; on the sub-annulus, $f$ is holomorphic; apply CIF to the boundary.
   - *Hint:* The boundary is $\gamma_2 - \gamma_1$ where $\gamma_i$ is the circle $|z - a| = \rho_i$ counterclockwise.
   - *Why needed:* Gives $f(w) = $ outer integral $-$ inner integral.

2. **Expand $1/(z - w)$ as a geometric series on the outer circle.** On $|z - a| = \rho_2 > |w - a|$, write $1/(z - w) = \sum_{n \geq 0}(w - a)^n/(z - a)^{n+1}$.
   - *Hint:* $z - w = (z - a) - (w - a)$, factor out $z - a$, geometric series in $(w-a)/(z-a)$.
   - *Why needed:* Generates the positive-power part of the Laurent expansion.

3. **Expand $1/(z - w)$ as a geometric series on the inner circle.** On $|z - a| = \rho_1 < |w - a|$, write $1/(z - w) = -\sum_{m \geq 1}(z - a)^{m-1}/(w - a)^m$.
   - *Hint:* Same trick, but now factor out $w - a$.
   - *Why needed:* Generates the negative-power part.

4. **Integrate termwise.** Uniform convergence on the compact circles licenses termwise integration; each integral $\oint (z - a)^k\,dz$ for various $k$ gives the Laurent coefficient.

5. **Coefficient formula independent of the radius.** Show $c_n = (2\pi i)^{-1}\oint_{|z-a|=\rho} f(z)/(z-a)^{n+1}\,dz$ for any $\rho \in (r_0, R_0)$.
   - *Hint:* By Cauchy's theorem, the integrand is holomorphic on the annulus, so the integral is independent of $\rho$.

6. **Uniqueness.** Given another convergent Laurent series for $f$ on the annulus, term-by-term integration recovers the same coefficients.

---

# Lemma Decomposition

> [!note]- Lemma 1: Cauchy's integral formula on the annulus
> **Statement:** For $f$ holomorphic on $A(a; r_0, R_0)$ and $w$ in a sub-annulus $\{\rho_1 \leq |z - a| \leq \rho_2\}$, $f(w) = (2\pi i)^{-1}[\oint_{|z-a|=\rho_2} - \oint_{|z-a|=\rho_1}] f(z)/(z - w)\,dz$.
>
> **Hint:** The "cycle" $\gamma_2 - \gamma_1$ bounds the sub-annulus; apply CIF.
>
> > [!note]- Full proof
> > Choose an enlargement of the sub-annulus to a simply connected region: cut the sub-annulus by a radial segment, giving a simply connected region whose boundary traverses $\gamma_2$, the segment outward, $\gamma_1$ reversed, and the segment inward. The contributions of the segment in the two directions cancel, leaving $\gamma_2 - \gamma_1$. By Cauchy's integral formula on the (now simply connected) cut region, $f(w) = (2\pi i)^{-1}\oint_{\gamma_2 - \gamma_1} f(z)/(z - w)\,dz$.

> [!note]- Lemma 2: Geometric expansion of $1/(z - w)$ on each circle
> **Statement:** On $|z - a| = \rho_2$ with $|w - a| < \rho_2$: $1/(z - w) = \sum_{n \geq 0}(w - a)^n/(z - a)^{n+1}$, uniformly. On $|z - a| = \rho_1$ with $|w - a| > \rho_1$: $1/(z - w) = -\sum_{m \geq 1}(z - a)^{m-1}/(w - a)^m$, uniformly.
>
> **Hint:** Standard geometric series, factoring out the larger of $|z - a|$ and $|w - a|$.

---

# Formal Proof

> [!note]- Complete formal proof
> Fix $w \in A(a; r_0, R_0)$ and choose $r_0 < \rho_1 < |w - a| < \rho_2 < R_0$.
>
> By Lemma 1, $f(w) = (2\pi i)^{-1}\left[\oint_{|z-a|=\rho_2} - \oint_{|z-a|=\rho_1}\right] f(z)/(z - w)\,dz$.
>
> **Outer integral.** On $|z - a| = \rho_2$:
> $$\frac{1}{z - w} = \frac{1}{(z - a)(1 - (w - a)/(z - a))} = \sum_{n \geq 0}\frac{(w - a)^n}{(z - a)^{n+1}}, \quad \text{uniformly}.$$
> So $\oint_{|z-a|=\rho_2} f(z)/(z - w)\,dz = \sum_{n \geq 0}(w - a)^n \oint f(z)/(z - a)^{n+1}\,dz$. Defining $c_n = (2\pi i)^{-1}\oint_{|z-a|=\rho_2} f(z)/(z-a)^{n+1}\,dz$ for $n \geq 0$, the outer contribution is $2\pi i \sum_{n \geq 0} c_n (w - a)^n$.
>
> **Inner integral.** On $|z - a| = \rho_1$:
> $$\frac{1}{z - w} = \frac{-1}{(w - a)(1 - (z - a)/(w - a))} = -\sum_{m \geq 1}\frac{(z - a)^{m-1}}{(w - a)^m}, \quad \text{uniformly}.$$
> So $-\oint_{|z-a|=\rho_1} f(z)/(z - w)\,dz = \sum_{m \geq 1}(w - a)^{-m}\oint f(z)(z - a)^{m-1}\,dz$. Defining $c_{-m} = (2\pi i)^{-1}\oint_{|z-a|=\rho_1} f(z)(z - a)^{m-1}\,dz = (2\pi i)^{-1}\oint_{|z-a|=\rho_1} f(z)/(z - a)^{-m + 1}\,dz$ — i.e., the same formula $c_n = (2\pi i)^{-1}\oint f(z)/(z-a)^{n+1}\,dz$ with $n = -m$ — the inner contribution is $2\pi i \sum_{m \geq 1} c_{-m}(w - a)^{-m}$.
>
> **Adding:** $f(w) = \sum_{n=-\infty}^\infty c_n (w - a)^n$, with $c_n = (2\pi i)^{-1}\oint_{|z-a|=\rho} f(z)/(z-a)^{n+1}\,dz$ for any $\rho \in (r_0, R_0)$ (using Cauchy's theorem to deform the contour).
>
> **Uniform convergence on sub-annuli.** The geometric series $\sum (w - a)^n/(z - a)^{n+1}$ on the outer circle is dominated by $(|w - a|/\rho_2)^n/\rho_2$, geometric ratio $< 1$; similarly for the inner. So the Laurent series converges absolutely, uniformly on any closed sub-annulus.
>
> **Uniqueness.** If $f(z) = \sum d_n (z - a)^n$ is another Laurent expansion on the annulus, then $\oint f(z)(z - a)^{-m-1}\,dz = \sum_n d_n \oint (z - a)^{n - m - 1}\,dz = 2\pi i \cdot d_m$ (only the $n = m$ term contributes), so $d_m = c_m$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Bessel function generating function.** Show that $e^{(z/2)(t - 1/t)} = \sum_{n=-\infty}^\infty J_n(z) t^n$ where $J_n(z) = (2\pi i)^{-1}\oint_{|t|=1} e^{(z/2)(t - 1/t)} t^{-n-1}\,dt$ is the Bessel function. The expansion is the Laurent series in $t$ around $t = 0$ of an entire-in-$t$-for-each-$z$ function on the punctured plane. The contour-integral formula for the Laurent coefficients gives an integral representation of Bessel functions.

**Behaviour at infinity for entire functions.** An entire function $f$ has a Laurent expansion on the annulus $A(0; R, \infty)$ for any $R$. If $f$ is a polynomial of degree $n$, the expansion at infinity has only nonnegative powers up to $z^n$, and zero negative-power contribution. If $f$ has polynomial growth at infinity, finitely many positive powers. Liouville's theorem (bounded entire is constant) is the statement "Laurent at infinity has only the $c_0$ term".

**Mittag-Leffler theorem.** Given a sequence of points $a_k \to \infty$ in $\mathbb{C}$ and prescribed principal parts $P_k(z) = \sum_{n=1}^{N_k} c_{-n}^{(k)}/(z - a_k)^n$, there exists a meromorphic function on $\mathbb{C}$ with poles at exactly the $a_k$ and prescribed principal parts. The construction uses Laurent expansions and convergence of $\sum P_k(z)$ after subtracting suitable polynomial corrections.

---

# Bridges

- **[[Def - Laurent Series]]** — the object the theorem makes rigorous.

- **[[Thm - Cauchy's Theorem for Simply Connected Domains]]** — the cut-the-annulus argument uses Cauchy on a simply connected sub-region.

- **[[Def - Removable Singularity, Pole, Essential Singularity]]** — the trichotomy of singularities is read off the Laurent expansion.

- **[[Thm - Residue Theorem]]** — the residue theorem follows from Laurent (principal parts) plus Cauchy (regular parts integrate to zero).

---

# Unlocked by This

> [!tip] All of Singularity Analysis *(from §3.3)*
> Every result classifying or computing with isolated singularities — [[Thm - Riemann's Removable Singularity Theorem|Riemann's removable singularity theorem]], [[Thm - Pole Characterization|pole characterization]], [[Thm - Casorati–Weierstrass|Casorati–Weierstrass]] — uses the Laurent expansion as its central tool.

> [!tip] Spectral Theory and Holomorphic Functional Calculus *(from Functional Analysis)*
> The Laurent expansion of $(zI - A)^{-1}$ (the resolvent of a bounded operator $A$) around a point of the spectrum gives the **spectral projection** to the eigenspace at that point. The principal part is the projection onto the generalized eigenspace; the residue gives the spectral measure. The whole holomorphic functional calculus is built on Laurent.
