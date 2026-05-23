---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Bump Function and Smooth Cutoff"
  - "Def - Smooth Function on a Manifold"
  - "Def - Support of a Function"
tags: [geometry, differential-geometry]
---

# Problem Statement

Construct an explicit smooth function $\psi : \mathbb{R} \to [0, 1]$ such that

- $\psi(x) = 1$ for all $x \in [-1, 1]$,
- $\psi(x) = 0$ for all $x \in \mathbb{R} \setminus [-2, 2]$.

Start from the function $\psi_0 : \mathbb{R} \to \mathbb{R}$ defined by

$$\psi_0(t) = \begin{cases} e^{-1/t^2} & t > 0 \\ 0 & t \leq 0 \end{cases}.$$

Then construct, from $\psi$, a smooth bump function $H : \mathbb{R}^n \to [0, 1]$ with $H(x) = 1$ on $\overline{B(0, 1)}$ and $H(x) = 0$ on $\mathbb{R}^n \setminus B(0, 2)$.

**Recall:**

The relevant definitions are:

![[Def - Bump Function and Smooth Cutoff#The Definition]]

The function $\psi_0(t) = e^{-1/t^2}$ for $t > 0$, $\psi_0(t) = 0$ for $t \leq 0$ is smooth on $\mathbb{R}$ with $\psi_0^{(k)}(0) = 0$ for every $k \geq 0$. (This is essentially Lee Lemma 2.20, with $1/t$ replaced by $1/t^2$; the qualitative behaviour is the same — every derivative vanishes at $0$ — and the proof is parallel.)

---

# Convergent Strategy

**Problem class:** Explicit construction of a smooth function with prescribed values and support — the canonical "bump function" task. The routine: start from the $\psi_0$ germ (which vanishes on one side of $0$ and is positive on the other), build a smooth cutoff transitioning from $1$ to $0$ over an interval, then produce a "two-sided" bump by combining one-sided cutoffs.

**Assumption pattern:** The hypothesis is that $\psi_0$ is smooth on $\mathbb{R}$ with every derivative at $0$ equal to $0$. This is a one-sided smoothness with the unusual property of being non-analytic (the Taylor series at $0$ is identically $0$, but the function is positive on $(0, \infty)$). The non-analyticity is what makes the construction possible — analytic functions vanishing on an open set vanish everywhere.

**Theorem routing:** Build $h(t) = \psi_0(2 - t)/(\psi_0(2 - t) + \psi_0(t - 1))$, a smooth function equal to $1$ on $(-\infty, 1]$ and $0$ on $[2, \infty)$. From $h$, build $\psi(x) = h(|x|)$ for $x \in \mathbb{R}$ (treating $|x|$ as the natural one-sided argument): $\psi$ is even, equal to $1$ on $[-1, 1]$, and $0$ on $\mathbb{R} \setminus [-2, 2]$. For the radial bump in $\mathbb{R}^n$, use $H(x) = h(|x|)$ where $|x|$ is the Euclidean norm.

**Key decision point:** The non-obvious move is the *quotient* form $h = \psi_0(2 - t)/(\psi_0(2 - t) + \psi_0(t - 1))$ rather than the sum. The denominator is positive everywhere (one of the two $\psi_0$ values is always positive), so the quotient is well-defined and smooth. The numerator vanishes exactly when $\psi_0(2 - t) = 0$, i.e. when $2 - t \leq 0$, i.e. $t \geq 2$. The denominator equals the numerator exactly when $\psi_0(t - 1) = 0$, i.e. $t \leq 1$. So $h(t) = 1$ on $(-\infty, 1]$, $h(t) = 0$ on $[2, \infty)$, $h(t) \in (0, 1)$ on $(1, 2)$. The quotient is the standard "smooth-cutoff" recipe (Lee Lemma 2.21); the alternative "linear combination" approach (e.g., $\psi_0(2 - t)$ alone, suitably normalized) fails to reach exactly $1$ and $0$ on the prescribed intervals.

---

# Legal Operations Used

1. **Construct smooth real-valued functions via the $e^{-1/t}$ germ (operation 4 from the topic page).** The function $\psi_0$ is the basic atom; everything else is built from it.

2. **Pull back to charts to check smoothness (operation 1 from the topic page).** In $\mathbb{R}^n$, the "chart" is just the identity, so smoothness checks reduce to ordinary Euclidean smoothness — but the smoothness of $|x|$ at $0$ is delicate, requiring care.

3. **Use bump functions to localize / cut off (operation 7 from the topic page).** The construction produces the prototype bump that all later localizations use.

---

# Hints

> [!note]- Hint 1
> Start by understanding $\psi_0$. Compute $\psi_0(t)$ at $t = 1, 1/2, 1/4, \ldots$ to verify it shrinks to $0$ as $t \to 0^+$, and check that $\psi_0$ matches $0$ from the left. The smoothness at $t = 0$ is the non-trivial fact (every derivative is $0$ there).

> [!note]- Hint 2
> The smooth cutoff $h(t)$ that transitions from $1$ to $0$ over $[1, 2]$ has the form
> $$h(t) = \frac{\text{something nonzero on } t \leq 1, \text{ zero on } t \geq 2}{\text{something positive on all of } \mathbb{R}}.$$
> The numerator should be $\psi_0(2 - t)$ (zero on $t \geq 2$, positive on $t < 2$). The denominator should ensure the right value of $h$ at the endpoints; $h(t) = 1$ on $t \leq 1$ means denominator = numerator there, so denominator = $\psi_0(2-t) + (\text{something that vanishes on } t \leq 1)$. The natural choice is $\psi_0(t - 1)$.

> [!note]- Hint 3
> For the radial bump on $\mathbb{R}^n$, set $H(x) = h(|x|)$. The function $|x|$ is smooth on $\mathbb{R}^n \setminus \{0\}$ (as a composition of smooth functions), but not differentiable at $0$. However, $h$ is constant $1$ in a neighbourhood of $0$ (specifically on $|x| \leq 1$), so $H$ is also constant $1$ there — and a constant function is smooth.

> [!note]- Hint 4
> For the one-dimensional bump $\psi : \mathbb{R} \to [0, 1]$, use $\psi(x) = h(|x|)$ — same as the radial bump, in [[Def - Dimension|dimension]] $1$. Verify directly: $|x| \leq 1 \Rightarrow \psi(x) = h(|x|) = 1$ (since $|x| \leq 1 \Rightarrow$ $h(|x|) = 1$); $|x| \geq 2 \Rightarrow \psi(x) = h(|x|) = 0$. Smoothness at $x = 0$: $\psi$ is constant $1$ near $0$, hence smooth there.

---

# Solution

The construction proceeds in three steps. First, build the smooth one-sided germ $\psi_0(t) = e^{-1/t^2}$ for $t > 0$ and $0$ otherwise, and confirm it is smooth with all derivatives at $0$ equal to $0$. Second, combine two scaled copies of $\psi_0$ into a smooth cutoff $h(t) = \psi_0(2-t)/(\psi_0(2-t) + \psi_0(t-1))$ transitioning from $1$ on $t \leq 1$ to $0$ on $t \geq 2$. Third, build the one-dimensional bump $\psi(x) = h(|x|)$ and the $n$-dimensional radial bump $H(x) = h(|x|)$ (Euclidean norm). The non-obvious move is the *quotient* form of $h$ — the denominator's positivity is essential.

**Step 1: $\psi_0$ is smooth.**

Define $\psi_0(t) = e^{-1/t^2}$ for $t > 0$, $\psi_0(t) = 0$ for $t \leq 0$.

> [!note]- Derivation
> For $t > 0$, $\psi_0$ is a composition of smooth functions ($t \mapsto 1/t^2$ smooth on $(0, \infty)$, $u \mapsto e^{-u}$ smooth on $\mathbb{R}$), hence smooth. For $t < 0$, $\psi_0$ is the zero function, smooth.
>
> The only non-trivial point is smoothness at $t = 0$. We show by induction that $\psi_0^{(k)}(t) = p_k(1/t) e^{-1/t^2}$ for $t > 0$, where $p_k$ is a polynomial; and that $\lim_{t \to 0^+} \psi_0^{(k)}(t) = 0$ for every $k$.
>
> For $k = 0$: $\psi_0(t) = e^{-1/t^2}$, so $p_0(u) = 1$ and $\lim_{t \to 0^+} e^{-1/t^2} = 0$ (the exponential dominates).
>
> For $k + 1$: $\psi_0^{(k+1)}(t) = \frac{d}{dt}[p_k(1/t) e^{-1/t^2}] = -\frac{1}{t^2} p_k'(1/t) e^{-1/t^2} + p_k(1/t) \cdot \frac{2}{t^3} e^{-1/t^2} = q_k(1/t) e^{-1/t^2}$, where $q_k(u) = -u^2 p_k'(u) + 2u^3 p_k(u)$, a polynomial. So $p_{k+1} = q_k$.
>
> The limit: any polynomial times $e^{-1/t^2}$ tends to $0$ as $t \to 0^+$, because $e^{-1/t^2} = O(e^{-1/t^2})$ shrinks faster than any polynomial in $1/t$ grows.
>
> The one-sided derivatives at $0$: from the right, $\psi_0^{(k)}(0^+) = \lim_{t \to 0^+} \frac{\psi_0^{(k-1)}(t) - \psi_0^{(k-1)}(0)}{t} = \lim_{t \to 0^+} \frac{\psi_0^{(k-1)}(t)}{t}$ (using $\psi_0^{(k-1)}(0) = 0$ by induction) $= \lim_{t \to 0^+} \frac{p_{k-1}(1/t) e^{-1/t^2}}{t}$, which is again a polynomial-in-$1/t$ times $e^{-1/t^2}$, tending to $0$. From the left, $\psi_0$ is constant $0$, so all derivatives from the left are $0$. The two one-sided derivatives agree at $0$, so $\psi_0^{(k)}(0) = 0$.
>
> Hence $\psi_0$ is $C^\infty$ on $\mathbb{R}$ with $\psi_0^{(k)}(0) = 0$ for every $k$.

**Step 2: build the smooth cutoff $h(t)$.**

Define
$$h(t) = \frac{\psi_0(2 - t)}{\psi_0(2 - t) + \psi_0(t - 1)}.$$

This $h$ is smooth on $\mathbb{R}$, takes values in $[0, 1]$, equals $1$ on $(-\infty, 1]$, equals $0$ on $[2, \infty)$, and is strictly in $(0, 1)$ on $(1, 2)$.

> [!note]- Derivation
> *Denominator positivity:* For every $t \in \mathbb{R}$, at least one of $2 - t$ and $t - 1$ is positive (since their sum is $1$, at least one is $\geq 1/2 > 0$). So at least one of $\psi_0(2 - t), \psi_0(t - 1)$ is positive (since $\psi_0(s) > 0$ iff $s > 0$). The denominator is a sum of two non-negative quantities, at least one of which is positive, so the denominator is positive everywhere.
>
> *Smoothness:* $\psi_0(2 - t)$ and $\psi_0(t - 1)$ are smooth functions of $t$ (compositions of $\psi_0$ with affine maps). Their sum is smooth and positive, so the ratio is smooth.
>
> *Values in $[0, 1]$:* numerator and denominator both nonneg; numerator $\leq$ denominator (numerator is one of the terms summed in the denominator, with both terms non-negative). So $0 \leq h \leq 1$.
>
> *On $t \leq 1$:* $\psi_0(t - 1) = 0$ (since $t - 1 \leq 0$). So denominator = $\psi_0(2 - t)$ = numerator, hence $h(t) = 1$. (Also $\psi_0(2 - t) > 0$ since $2 - t \geq 1 > 0$.)
>
> *On $t \geq 2$:* $\psi_0(2 - t) = 0$ (since $2 - t \leq 0$). So numerator = $0$, hence $h(t) = 0$.
>
> *On $1 < t < 2$:* both $\psi_0(2 - t) > 0$ and $\psi_0(t - 1) > 0$, so $0 < h(t) < 1$.

**Step 3: build the one-dimensional bump $\psi(x)$ and the $n$-dimensional radial bump $H(x)$.**

Define $\psi : \mathbb{R} \to [0, 1]$ by $\psi(x) = h(|x|)$. Define $H : \mathbb{R}^n \to [0, 1]$ by $H(x) = h(|x|)$ where $|x|$ is the Euclidean norm.

Both functions satisfy: equal to $1$ on $\overline{B(0, 1)}$, equal to $0$ on $\mathbb{R}^n \setminus B(0, 2)$, in $[0, 1]$ everywhere, smooth on the entire domain.

> [!note]- Derivation
> *Values:* on $|x| \leq 1$, $\psi(x) = h(|x|) = 1$ (since $h \equiv 1$ on $(-\infty, 1]$, and $|x| \leq 1$ is in this interval). On $|x| \geq 2$, $\psi(x) = h(|x|) = 0$. For $1 < |x| < 2$, $\psi(x) = h(|x|) \in (0, 1)$.
>
> *Smoothness on $|x| \neq 0$:* For $x \neq 0$, $|x|$ is a smooth function of $x$ (the Euclidean norm is smooth on $\mathbb{R}^n \setminus \{0\}$: it is the square root of $\sum x_i^2$, a smooth function with positive value, and $\sqrt{}$ is smooth on $(0, \infty)$). So $h \circ |\cdot|$ is a composition of smooth functions, hence smooth, on $\mathbb{R}^n \setminus \{0\}$.
>
> *Smoothness at $0$:* The function $|x|$ is *not* smooth at $0$ in general (in [[Def - Dimension|dimension]] $\geq 2$, it has a "conical" singularity, not differentiable). However, $h \circ |\cdot|$ is *constant equal to $1$* on $|x| \leq 1$ — and constant functions are smooth. So even though $|x|$ is not smooth at $0$, the composition $h(|x|)$ avoids the singularity by being constant in a neighbourhood of $0$.
>
> More precisely: for any $x$ with $|x| < 1$, there is an open neighbourhood of $x$ in $\mathbb{R}^n$ where $|y| < 1$ (the open ball $B(x, 1 - |x|)$), and on this neighbourhood $\psi(y) = 1$ — a constant function, smooth. So $\psi$ is smooth at $x$. In particular at $x = 0$.
>
> The whole function: smooth on $\mathbb{R}^n \setminus \{0\}$ (composition argument) and smooth at $0$ (constant near $0$), hence smooth on $\mathbb{R}^n$.
>
> Note: this elegantly sidesteps the non-differentiability of $|x|$ at $0$. The cutoff $h$ is "flat" near $|x| = 0$ (constant $1$), so the composition is constant near $x = 0$ and smoothness is automatic.

> [!note]- Complete formal solution
> **Claim.** The function $\psi : \mathbb{R} \to [0, 1]$ defined by $\psi(x) = h(|x|)$ where
> $$h(t) = \frac{\psi_0(2 - t)}{\psi_0(2 - t) + \psi_0(t - 1)}, \quad \psi_0(t) = \begin{cases} e^{-1/t^2} & t > 0 \\ 0 & t \leq 0 \end{cases},$$
> is smooth, equals $1$ on $[-1, 1]$, equals $0$ on $\mathbb{R} \setminus [-2, 2]$, and takes values in $[0, 1]$.
>
> *Proof.* By Step 1, $\psi_0$ is $C^\infty$ on $\mathbb{R}$. By Step 2, $h$ is smooth, takes values in $[0, 1]$, equals $1$ on $(-\infty, 1]$, equals $0$ on $[2, \infty)$. By Step 3, $\psi(x) = h(|x|)$ is smooth on $\mathbb{R}$ (away from $0$ by composition; near $0$ because $\psi$ is constant $1$), equals $1$ on $[-1, 1]$ (since $|x| \leq 1$ there), equals $0$ on $\mathbb{R} \setminus [-2, 2]$ (since $|x| \geq 2$ there), and is in $[0, 1]$ everywhere. $\quad\blacksquare$
>
> The radial bump $H(x) = h(|x|)$ on $\mathbb{R}^n$ has the same properties: smooth, equal to $1$ on $\overline{B(0, 1)}$, equal to $0$ outside $B(0, 2)$, in $[0, 1]$. The argument is identical, with $|x|$ now the Euclidean norm.

> [!warning] Illegal but tempting alternative route
> One might try to define a smooth cutoff by a polynomial spline — e.g., $h(t) =$ cubic on $[1, 2]$ matching the endpoint values and slopes. But cubic splines, no matter how clever, can only be $C^k$ for finite $k$ at the gluing points (they fail to be $C^\infty$ unless they are *constants*, which won't transition $1$ to $0$). The polynomial approach fundamentally cannot produce a smooth cutoff that transitions between two different constants — only the $\psi_0$-trick can, because of the magical "all derivatives vanish at $0$" property of $e^{-1/t^2}$. The non-analyticity of $\psi_0$ is essential and irreplaceable by polynomials or rational functions.

---

# Key Takeaways

**The $e^{-1/t}$-trick (or $e^{-1/t^2}$-trick) is the entire technology of smooth bumps.** Every bump function on every smooth manifold is built from this one function. The $\psi_0$ germ has the precisely-balanced property: every derivative at $0$ is exactly $0$ (so it glues smoothly to the constant-$0$ function on the left), and the function is positive on $(0, \infty)$ (so it provides positive "fuel" for the cutoff). No analytic function has this property (an analytic function with all derivatives zero at a point is identically zero in a neighbourhood), so the smooth-vs-analytic gap is what licenses the construction. This is one of the highest-leverage facts in differential geometry: a single non-analytic smooth function produces, by scaling and translation, all the smooth bumps needed for partition-of-unity, extension lemma, and Riemannian-metric existence proofs. The recognition trigger is any problem requiring a smooth function with prescribed compact support; the reaction is to invoke this construction.

**The quotient form of the cutoff is the standard recipe.** The cutoff $h(t) = \psi_0(2 - t)/(\psi_0(2 - t) + \psi_0(t - 1))$ is the canonical way to transition smoothly from $1$ to $0$. The denominator is positive everywhere (at least one of two non-negative terms is positive), the numerator vanishes on the "off" side, the ratio equals $1$ on the "on" side because numerator equals denominator there. The pattern generalizes: to construct a smooth function equal to $a$ on $K_1$ and $b$ on $K_2$ (with $K_1, K_2$ closed disjoint), use $a + (b - a) \cdot (\text{cutoff from } K_1 \text{ to } K_2)$. The cutoff is the universal "smooth interpolant" between disjoint closed sets, and the quotient form is what makes it computable.

**The constant-near-zero trick avoids the non-smoothness of $|x|$ at the origin.** A naive radial bump $H(x) = h(|x|)$ might worry about $|x|$ being non-smooth at $0$, but the smooth cutoff $h$ is *constant* in a neighbourhood of $0$ (equal to $1$ on $t \leq 1$), so the composition $h(|x|)$ is also constant near $x = 0$ — and constant functions are smooth. The smoothness at the origin is "given away" by the constant region of $h$. This is a recurring strategy: when a composition would have a singularity, ensure the outer function is constant in a neighbourhood of the inner function's singular value. The reaction pattern is: "I need to compose smooth-with-non-smooth-at-zero, but the outer function is constant near zero" $\Rightarrow$ "the composition is constant there, hence smooth".

This exercise constructs the prototype bump for every later partition-of-unity argument. See [[Thm - Existence of Smooth Bump Functions]] for the existence theorem on a general smooth manifold (which uses chart-pullbacks of this bump) and [[Thm - Existence of Smooth Partitions of Unity]] for the full partition-of-unity machinery built from chart-bumps. Companion exercise: [[Ex - Smooth Partition of Unity Subordinate to a Cover]] applies these bumps to a chart cover of a manifold.
