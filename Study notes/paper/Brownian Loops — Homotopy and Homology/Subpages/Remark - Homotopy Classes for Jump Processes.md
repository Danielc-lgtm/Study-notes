---
type: remark
subject: probability-geometry
prereqs:
  - "Def - Bernstein Function, Subordinator, and Subordination"
  - "Def - Fuchsian Group and the Hyperbolic Quotient Surface"
  - "Def - Subordinate Brownian Loop Measure"
tags: [paper, brownian-loops, hyperbolic-geometry, jump-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Remark 3.1"
---

# Notation

- $\mathbb{H}^2$ — the upper-half-plane model of the hyperbolic plane; every symbol below lives on it or on its quotient.
- $\Gamma \subset \mathrm{PSL}(2,\mathbb{R})$ — a discrete, torsion-free group of hyperbolic isometries; $X = \Gamma\backslash\mathbb{H}^2$ is the resulting hyperbolic surface, $\pi : \mathbb{H}^2 \to X$ the projection.
- $\tau \in \Gamma$ — a primitive hyperbolic element; its conjugacy class in $\Gamma$ is written $[\tau^m]_{\mathrm{conj}} := \{q\tau^m q^{-1} : q \in \Gamma\}$; the free homotopy class of closed curves on $X$ corresponding to it is $C_X(\gamma^m)$, where $\gamma$ is the closed geodesic $\tau$ represents.
- $Y = (B, S)$ — a **subordinate process**: a Bernstein-function $\phi$ subordinator $S = (S_t)_{t\ge 0}$ time-changes an $\mathbb{H}^2$-Brownian motion $B = (B_s)_{s\ge 0}$; the observed path is $Y_t = B_{S_t}$, a càdlàg (right-continuous with left limits) path in $\mathbb{H}^2$ that jumps whenever $S$ jumps.
- $p^\phi_{\mathbb{H}^2}(t,z,w)$ — the transition density of $Y$ from $z$ to $w$ in time $t$, expressed by the subordination integral $\int_0^\infty p_{\mathbb{H}^2}(s,z,w)\,\psi^\phi_t(ds)$ over the subordinator's law $\psi^\phi_t$.
- $\mu^E_X$ — the loop measure on $X$ built from the Dirichlet form $E$ (equivalently, from the transition kernel $p^E$); for $\phi$-subordinate processes this is written $\mu^\phi_X$.
- $\rho_X$, $\rho_{\mathbb{H}^2}$ — the hyperbolic area measures on $X$ and $\mathbb{H}^2$.

> [!recall]- Free homotopy class $C_X(\gamma^m)$
> **Formally:** $C_X(\gamma^m)$ is the set of oriented closed curves $\omega:[0,t]\to X$ ($\omega(t)=\omega(0)$) equivalent to $\gamma^m$ under *free homotopy*: there is a continuous map $H:[0,t]\times[0,1]\to X$ with $H(\cdot,0)=\omega$, $H(\cdot,1)=\gamma^m$, and $H(0,s)=H(t,s)$ for every $s$ (the basepoint may move during the homotopy, but each intermediate curve is closed). Equivalently, $C_X(\gamma^m)$ corresponds to a single conjugacy class $[\tau^m]_{\mathrm{conj}} \subset \Gamma$ under the universal-cover monodromy.
> **In words:** "loops that go around the same holes in the same pattern, when we do not care where you started". Two loops belong to the same class if you can continuously slide one into the other without cutting it, letting the starting point drift as needed.
> **Concretely:** on the flat torus $T^2 = \mathbb{R}^2/\mathbb{Z}^2$ (a square with opposite edges glued), the class $C_{T^2}(\gamma^{(1,0)})$ contains every loop that goes once around horizontally (the taut horizontal circle, a slightly wavy version of it, a big detour that eventually crosses the vertical edge once, etc.), but not a loop that goes once around vertically — that lives in a different class.

> [!recall]- Càdlàg path
> **Formally:** a function $\omega : [0,t] \to X$ is **càdlàg** (French *continu à droite, limite à gauche*) if at every point $r \in [0,t)$ it is right-continuous ($\lim_{s\downarrow r}\omega(s) = \omega(r)$) and at every point $r \in (0,t]$ it has a left limit ($\lim_{s\uparrow r}\omega(s)$ exists, possibly $\ne \omega(r)$). Between consecutive left- and right-limits at $r$, the path may jump.
> **In words:** the path is allowed to teleport (jump), but at each jump time the "new value" is the one after the jump — the path is continuous *from the right*. Everywhere except at jump times it behaves like a continuous function.
> **Concretely:** for a Poisson process on the line, the sample path is a step function increasing by $1$ at each arrival time; at an arrival time $r$ the path equals its new (post-jump) value, and its left limit is the old (pre-jump) value. A one-dimensional $\alpha$-stable process has infinitely many small jumps in every interval — a "salt-shaker" of jumps of every size — but it is still càdlàg: at every time you can name the current value, and taking limits from the right or left gives the current or the immediately preceding value.

> [!recall]- Subordinate process $Y = B \circ S$
> **Formally:** given a Bernstein function $\phi$, an $\mathbb{H}^2$-Brownian motion $B = (B_s)_{s\ge 0}$, and an independent $\phi$-subordinator $S = (S_t)_{t\ge 0}$ (a non-decreasing càdlàg $[0,\infty)$-valued Lévy process with Laplace exponent $\phi$), the *subordinate process* is $Y_t := B_{S_t}$: at wall-clock time $t$, use the amount of "internal Brownian time" the subordinator has clocked up. Its transition density satisfies $p^\phi_{\mathbb{H}^2}(t,z,w) = \int_0^\infty p_{\mathbb{H}^2}(s,z,w)\,\psi^\phi_t(ds)$, where $\psi^\phi_t$ is the law of $S_t$.
> **In words:** run Brownian motion, but on a stopwatch that occasionally jumps forward. Between jumps of $S$, the observed process $Y$ traces the continuous Brownian arc unchanged; at each jump of $S$ of size $\Delta > 0$, $Y$ teleports from $B_{s^-}$ to $B_{s^- + \Delta}$, deleting the intervening arc.
> **Concretely:** if $\phi(\lambda) = \sqrt{\lambda}$ (the $\alpha=1$ Cauchy subordinator), $S_t$ has the same law as a stable process and jumps at arbitrarily small times; the resulting $Y$ jumps at densely many times in $[0,t]$, showing only *samples* $B_{S_{t_1}}, B_{S_{t_2}}, \ldots$ of an underlying continuous Brownian curve. If $\phi(\lambda) = \lambda$ (no jumps, $S_t = t$), then $Y = B$ is the ordinary Brownian motion and no arcs are deleted. Full detail: [[Def - Bernstein Function, Subordinator, and Subordination]] and [[Def - Subordinate Brownian Loop Measure]].

---

# Statement

> **Remark (Belyaev–Huseynli 3.1).** For a general subordinate process $Y = B\circ S$ with jumps (Bernstein $\phi \ne \lambda$), a sample path is càdlàg with deleted arcs of $B$, so $Y$ is not a continuous loop and *does not lift uniquely* to $\mathbb{H}^2$. Consequently, one cannot literally read a free homotopy class off a sample path of $Y$. The paper therefore **defines** the mass of the class $C_X(\gamma^m)$ under the subordinate loop measure $\mu^\phi_X$ by declaring the class-mass to be the analogue of the continuous-process formula:
> $$\mu^\phi_X\big(C_X(\gamma^m)\big) := \int_0^\infty \frac{dt}{t}\int_X \sum_{h\in[\tau^m]_{\mathrm{conj}}} p^\phi_{\mathbb{H}^2}(t,\tilde z, h\tilde z)\, d\rho_X(z).$$
> The right-hand side is meaningful (the sum over one conjugacy class is a $\Gamma$-invariant function of $z\in X$; the $t$-integral converges once the Brownian short-loop divergence is cut off by the geodesic length lower bound). The intuition is: the *underlying Brownian arc* $B$ has a genuine free homotopy class, and the class of the càdlàg path $Y$ is defined to be that of $B$.

---

# In One Line

For jump processes the class of a càdlàg path is not intrinsically recoverable from the path itself, so the paper *defines* the loop-measure mass of a homotopy class by pulling the periodisation formula through to the jump kernel, agreeing with the Brownian case in form.

---

# Unpacking

**A continuous loop lifts uniquely; a càdlàg loop does not.** The universal-cover lifting theorem gives every *continuous* loop $\omega:[0,t]\to X$ starting at $\omega(0) \in X$ a *unique* continuous lift $\tilde\omega:[0,t]\to\mathbb{H}^2$ starting at a chosen $\tilde z \in \pi^{-1}(\omega(0))$; the endpoint $\tilde\omega(t)$ then lies in the same fibre and equals $h_\omega \tilde z$ for a unique **monodromy element** $h_\omega \in \Gamma$. The conjugacy class $[h_\omega]_{\mathrm{conj}}$ is the loop's free homotopy class.

For a càdlàg path $\omega$, the lifting theorem breaks down at each jump: between the values $\omega(r^-)$ and $\omega(r)$ the path is silent, so any two lifts $\tilde\omega(r^-)$ and $\tilde\omega(r)$ compatible with $\pi\tilde\omega = \omega$ agree with the path but not with one another — there is no continuous curve upstairs connecting them, and no canonical way to pick which of the (infinitely many) preimages $h\tilde\omega(r^-)$ ($h\in\Gamma$) the process "goes to". The topological "type" of $\omega$ is therefore undefined from $\omega$ alone.

**The paper's fix: refer the class to the underlying Brownian arc.** The subordinate process has a hidden structure: $Y = (B, S)$ is the pair of a continuous Brownian motion $B$ on $\mathbb{H}^2$ (which *does* have a monodromy) and a subordinator $S$ that records only which Brownian times survived. If the pair $(B, S)$ is available, we may declare the class of $Y$ to be the class of the underlying $B$-arc that generates it, which is well-defined. Only the observed càdlàg path $Y_t = B_{S_t}$ is then insufficient to reconstruct the class — but *conceptually* the class exists on the fuller data.

**The formula.** Belyaev–Huseynli's definition is to write down the same right-hand side that Theorem 3.2 gives for a continuous process:
$$\mu^\phi_X\big(C_X(\gamma^m)\big) := \int_0^\infty\frac{dt}{t}\int_X\sum_{h\in[\tau^m]_{\mathrm{conj}}}p^\phi_{\mathbb{H}^2}(t,\tilde z, h\tilde z)\,d\rho_X(z),$$
using the *subordinate* kernel $p^\phi_{\mathbb{H}^2}$ instead of the Brownian $p_{\mathbb{H}^2}$. The sum over a conjugacy class is $\Gamma$-invariant, so the outer integral over $X$ is well-defined; the geodesic length lower bound $L = m\ell_\gamma > 0$ suppresses the small-$t$ divergence exactly as in the Brownian case. So the formula makes sense and everything downstream — Theorem 3.5, the closed-form masses of §3.1, the loop soup of §3.3 — reads the same in the jump case as in the Brownian case.

**Why this is a definition rather than a theorem.** In the Brownian case one would *derive* the formula by decomposing every continuous loop by its monodromy (which the loop determines). Here, the loop does not determine the monodromy, so one cannot derive; one has to *stipulate*. The stipulation is chosen so that the formula agrees with the Brownian result formally, and so that all further identities — the strip evaluation, the Poissonian structure — go through unchanged. The reader should keep the distinction in mind: for jump processes the class-mass identity is definitional, not derivable from a path property.

⚠️ *(Intuition, flagged.)* The "class of a càdlàg $Y$ is the class of its underlying $B$" reading only makes sense if the pair $(B, S)$ is retained as part of the data; from $Y$ alone the class is not intrinsic. The paper notes this and proceeds formally with the periodised integral as the definition.

---

# Where the paper uses this

Justifies the extension of [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] and [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] to jump processes (Bernstein $\phi$ with $\phi \ne \lambda$). Read in context: [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3]]. The $\alpha$-stable case §3.1.3 and the shifted $\alpha$-stable case §3.1.4 depend on this definitional reading of the class-mass.
