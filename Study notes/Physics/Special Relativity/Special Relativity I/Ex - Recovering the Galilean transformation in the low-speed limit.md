---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - Galilean Spacetime and Its Failure"
tags: [physics, special-relativity]
---

# Problem Statement

Working with $c$ explicit, start from the Lorentz boost along $x$,
$$
x' = \gamma(x - vt), \qquad t' = \gamma\!\left(t - \frac{v}{c^2}x\right), \qquad \gamma = \frac{1}{\sqrt{1 - v^2/c^2}}.
$$

1. Expand $\gamma$ to leading order in the small parameter $\beta = v/c$, and state at what order in $\beta$ the boost first deviates from the [[Def - Galilean Spacetime and Its Failure|Galilean transformation]].
2. Show that in the formal limit $c \to \infty$ (with $v$ fixed) the boost becomes exactly the Galilean transformation $x' = x - vt$, $t' = t$. Identify *which term* in the clock equation is the one that disappears, and explain physically what its disappearance means.
3. A train moves at $v = 30\ \mathrm{m/s}$. By what fractional amount does $\gamma$ differ from $1$, and by how much does the relativistic clock equation's correction term $\frac{v}{c^2}x$ shift the time of an event $x = 1\ \mathrm{km}$ down the track? Comment on why Galilean physics is an excellent approximation here.

**Recall:**

![[Def - The Lorentz Transformation#The Definition]]

The [[Def - Galilean Spacetime and Its Failure|Galilean transformation]] is $x' = x - vt$, $y' = y$, $z' = z$, $t' = t$, with velocities adding as $u = u' + v$; its defining clause is the absolute clock $t' = t$. The dimensionless velocity is $\beta = v/c$, and $\gamma = (1 - \beta^2)^{-1/2}$ is the [[Def - The Lorentz Transformation|Lorentz factor]], always $\ge 1$ with $\gamma = 1$ exactly at $v = 0$.

---

# Convergent Strategy

**Problem class.** This is a *limiting-case / Newtonian-correspondence* problem: take a relativistic formula and show it reduces to the familiar non-relativistic one in the appropriate regime. The [[Special Relativity I — Postulates and Lorentz Transformations#Problem-Solving Strategy|topic strategy]] flags such problems as routine — the technique is a Taylor expansion in $\beta = v/c$ — and the value is conceptual: it pins down exactly which term carries the relativistic content.

**Assumption pattern.** The only assumption is that $\beta = v/c \ll 1$, the low-speed regime. This unlocks the binomial expansion of $\gamma$ and the smallness of the $\frac{v}{c^2}x$ term. The key recognition is that the *spatial* equation $x' = \gamma(x - vt)$ is already Galilean apart from the prefactor $\gamma$, while the *clock* equation $t' = \gamma(t - \frac{v}{c^2}x)$ contains a genuinely new term, $-\frac{v}{c^2}x$, with no Galilean counterpart — this term is the relativity of simultaneity, and it is what vanishes.

**Theorem routing.** No theorem is invoked beyond the definition of the boost; the route is direct substitution and expansion. The corollary of [[Thm - Uniqueness of the Lorentz Transformation from the Postulates|the uniqueness theorem]] tells you in advance that the limit *must* be Galilean (the Galilean transformation is the $\gamma = 1$ member of the family), so the computation is a confirmation, not a discovery.

**Key decision point.** The non-obvious move is to track the *clock* equation rather than the spatial one. A reader who only checks $x' = \gamma(x - vt) \to x - vt$ misses the whole point: the spatial part was never the problem. The interesting content is in $t'$, where the position-dependent term $-\frac{v}{c^2}x$ — the source of relative simultaneity — is precisely what the $c \to \infty$ limit kills, restoring the absolute clock $t' = t$.

---

# Legal Operations Used

1. **Operation 1 from the topic page (apply the Lorentz transformation to map events).** We use the boost equations as the starting expressions and manipulate them directly, treating the spatial and temporal parts separately.

2. **Operation 4 from the topic page (recover the Galilean limit / read the $c$-restored form).** The core move is the controlled approximation $\gamma \approx 1 + \tfrac12\beta^2$ and the $c \to \infty$ limit, which is the standing technique for checking Newtonian correspondence.

---

# Hints

> [!note]- Hint 1
> Use the binomial approximation $(1 - \beta^2)^{-1/2} \approx 1 + \tfrac12\beta^2 + \cdots$ for small $\beta$. Note that the *first* correction is of order $\beta^2$, not $\beta$ — there is no linear-in-$\beta$ term.

> [!note]- Hint 2
> In the clock equation $t' = \gamma(t - \frac{v}{c^2}x)$, set $\gamma \to 1$ and look at the term $\frac{v}{c^2}x$. As $c \to \infty$ this term has a $c^2$ in the denominator and goes to zero, while $v$ stays fixed. What is left?

> [!note]- Hint 3
> For part 3 compute $\beta = 30/(3\times 10^8) = 10^{-7}$, so $\gamma - 1 \approx \tfrac12\beta^2 = 5\times 10^{-15}$. The clock correction is $\frac{v}{c^2}x = \frac{30 \cdot 10^3}{(3\times10^8)^2}\ \mathrm{s}$. Both are minuscule.

---

# Solution

The boost is Galilean apart from two things: the prefactor $\gamma$, which differs from $1$ only at order $\beta^2$, and the clock term $\frac{v}{c^2}x$, which carries the relativity of simultaneity and vanishes as $c \to \infty$. The plan is to expand $\gamma$ (Step 1), take the limit and identify the vanishing term (Step 2), and put numbers to it for a train (Step 3).

**Step 1: $\gamma = 1 + \tfrac12\beta^2 + O(\beta^4)$; the boost first deviates from Galilean at order $\beta^2$.**

> [!note]- Derivation
> With $\beta = v/c$, the binomial series gives
> $$\gamma = (1 - \beta^2)^{-1/2} = 1 + \tfrac12\beta^2 + \tfrac38\beta^4 + O(\beta^6).$$
> There is no term linear in $\beta$ — $\gamma$ is an *even* function of $v$ (a fact forced by isotropy in [[Thm - Uniqueness of the Lorentz Transformation from the Postulates|Lemma 3]]). So to first order in $\beta$, $\gamma \approx 1$, and the spatial equation reads $x' \approx x - vt$ — the Galilean form. The leading correction to the *spatial* transformation is $(\gamma - 1)(x - vt) \approx \tfrac12\beta^2(x - vt)$, of order $\beta^2$. Likewise the clock equation's prefactor correction is order $\beta^2$. Hence the boost agrees with the Galilean transformation through first order in $\beta$ and first deviates at order $\beta^2 = v^2/c^2$.

**Step 2: As $c \to \infty$ the boost becomes $x' = x - vt$, $t' = t$; the vanishing term is $\frac{v}{c^2}x$.**

> [!note]- Derivation
> Take $c \to \infty$ with $v$ held fixed, so $\beta = v/c \to 0$ and $\gamma \to 1$.
>
> *Spatial equation.* $x' = \gamma(x - vt) \to 1\cdot(x - vt) = x - vt$.
>
> *Clock equation.* $t' = \gamma\left(t - \frac{v}{c^2}x\right)$. The prefactor $\gamma \to 1$. Inside the bracket, $t$ is fixed while $\frac{v}{c^2}x \to 0$ because the denominator $c^2 \to \infty$ with numerator $vx$ fixed. Hence
> $$t' \to 1\cdot(t - 0) = t.$$
> The term that disappears is $\frac{v}{c^2}x$ — the *position-dependent* part of the clock equation. Physically, this term is the relativity of simultaneity: it says two events at different positions $x$ but the same $t$ in $S$ have *different* $t'$ in $S'$. Its disappearance is the restoration of the absolute clock $t' = t$ — simultaneity becomes shared by all frames, which is exactly the [[Def - Galilean Spacetime and Its Failure|Galilean]] assumption. So the Galilean transformation is special relativity with the relativity of simultaneity switched off, and "switching it off" is literally sending $c \to \infty$ (making light infinitely fast, so that no finite speed can reveal the slicing).

**Step 3: For a train at $30\ \mathrm{m/s}$, $\gamma - 1 \approx 5\times10^{-15}$ and the clock shift over $1\ \mathrm{km}$ is $\sim 3\times10^{-12}\ \mathrm{s}$.**

> [!note]- Derivation
> With $v = 30\ \mathrm{m/s}$ and $c = 3\times10^8\ \mathrm{m/s}$,
> $$\beta = \frac{30}{3\times10^8} = 10^{-7}, \qquad \gamma - 1 \approx \tfrac12\beta^2 = \tfrac12(10^{-7})^2 = 5\times10^{-15}.$$
> So $\gamma$ differs from $1$ by five parts in a thousand trillion — utterly negligible. The clock-equation correction term for an event $1\ \mathrm{km}$ down the track ($x = 10^3\ \mathrm{m}$) is
> $$\frac{v}{c^2}x = \frac{30 \cdot 10^3}{(3\times10^8)^2} = \frac{3\times10^4}{9\times10^{16}} \approx 3.3\times10^{-13}\ \mathrm{s}.$$
> This is a third of a picosecond — far below the resolution of any train timetable. Both relativistic corrections are negligible because they are controlled by $\beta^2 \sim 10^{-14}$ (for $\gamma$) and $\beta \cdot x/c \sim 10^{-13}\ \mathrm{s}$ (for the simultaneity term). This is *why* Newtonian mechanics works so well in daily life: relativistic effects scale as $v^2/c^2$, and for everything short of particle accelerators and GPS satellites, $v/c$ is tiny.

> [!note]- Complete formal solution
> Expanding the Lorentz factor, $\gamma = (1 - \beta^2)^{-1/2} = 1 + \tfrac12\beta^2 + O(\beta^4)$ with $\beta = v/c$; the absence of a linear term reflects $\gamma_v = \gamma_{-v}$. Thus the boost agrees with the Galilean transformation through $O(\beta)$ and first deviates at $O(\beta^2)$. Taking $c \to \infty$ with $v$ fixed sends $\gamma \to 1$ and $\frac{v}{c^2}x \to 0$, so $x' = \gamma(x - vt) \to x - vt$ and $t' = \gamma(t - \frac{v}{c^2}x) \to t$ — the Galilean transformation. The term that vanishes is the position-dependent $\frac{v}{c^2}x$ in the clock equation, whose presence is the relativity of simultaneity; its removal restores absolute time. Numerically, for $v = 30\ \mathrm{m/s}$: $\beta = 10^{-7}$, $\gamma - 1 \approx 5\times10^{-15}$, and the clock correction over $x = 1\ \mathrm{km}$ is $\frac{v}{c^2}x \approx 3.3\times10^{-13}\ \mathrm{s}$. Both are negligible, which is why Galilean physics is an excellent approximation at everyday speeds. $\blacksquare$

---

# Key Takeaways

**Relativistic corrections to kinematics scale as $v^2/c^2$, and that quadratic smallness is the whole reason Newton survived two centuries.** The single most useful number to carry is $\beta^2 = v^2/c^2$: the Lorentz factor deviates from $1$ by $\tfrac12\beta^2$, time dilation and length contraction are $\beta^2$ effects, and almost every "relativistic correction" you will ever estimate is a $\beta^2$ correction. Because $\gamma$ is *even* in $v$, there is no linear-in-$\beta$ effect to leading order — the corrections are second order, hence doubly small. The trigger to reach for this expansion is any problem asking "how big is the relativistic effect?" or "does this reduce to the Newtonian answer?": expand in $\beta$, and the leading correction is $\beta^2$ unless a special cancellation intervenes. For a car ($\beta \sim 10^{-7}$) the effect is $10^{-14}$; for a satellite ($\beta \sim 10^{-5}$) it is $10^{-10}$, which over a day of GPS timing is a kilometre of position error — small per second, but not negligible when accumulated.

**The Galilean transformation is special relativity with the relativity of simultaneity switched off, and the switch is the term $\frac{v}{c^2}x$.** The deepest content of this exercise is *which* part of the boost is the relativistic part. The spatial equation $x' = \gamma(x - vt)$ was Galilean all along apart from a prefactor; the genuinely new physics lives entirely in the clock equation, in the position-dependent term $-\frac{v}{c^2}x$. That one term says clocks at different places, synchronised in $S$, are *not* synchronised in $S'$ — the relativity of simultaneity. Sending $c \to \infty$ deletes exactly this term and nothing essential else, recovering $t' = t$. So when you want to know "where is the relativity in this formula?", look for the term with a bare power of $1/c^2$ multiplying a position — that is the simultaneity term, and it is the seed of every relativistic surprise.

**Taking $c \to \infty$ is the universal Newtonian-limit check, and a correct relativistic formula must always pass it.** The formal limit $c \to \infty$ (equivalently $\beta \to 0$) is the standard sanity test for *any* relativistic result: energy $\gamma mc^2 \to mc^2 + \tfrac12 mv^2$, momentum $\gamma m v \to mv$, the velocity-addition law $(u'+v)/(1 + u'v/c^2) \to u' + v$, and here the boost $\to$ the Galilean transformation. The pattern is that the relativistic theory *contains* the Newtonian one as its low-speed limit — this is İnönü–Wigner group contraction in disguise, the [[Def - The Poincaré Group|Poincaré group]] contracting to the Galilean group. The transferable habit: whenever you derive or are handed a relativistic formula, immediately take $c \to \infty$ and confirm it lands on the familiar Newtonian expression; if it does not, you have made an error. This single check catches sign mistakes, missing factors of $\gamma$, and misplaced powers of $c$ faster than any other.
