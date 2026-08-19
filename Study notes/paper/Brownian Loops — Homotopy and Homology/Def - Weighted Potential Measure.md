---
type: definition
subject: probability
prereqs:
  - "Def - Bernstein Function, Subordinator, and Subordination"
  - "Def - Signed and Infinite Measures for Loop Measures"
tags: [paper, brownian-loops, levy-processes]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Definition 2.9"
---

# Notation

$\phi:(0,\infty)\to[0,\infty)$ a Bernstein function with Lévy–Khintchine data $(a,b,\nu)$ and subordinator law $\psi^\phi_t$ on $[0,\infty)$; the paper's Assumption 2.3 ($b>0$ or $\nu(0,\infty)=\infty$) is in force so $\psi^\phi_t(\{0\})=0$, i.e. $\psi^\phi_t$ is supported on $(0,\infty)$. $h:(0,\infty)\to[0,\infty)$ a non-negative measurable test function; $s>0$ the subordination variable.

> [!recall]- Bernstein function $\phi$, subordinator $S_t$, and its law $\psi^\phi_t$
> **Formally:** $\phi:(0,\infty)\to[0,\infty)$ is a **Bernstein function** if $\phi\in C^\infty$ with $(-1)^{n-1}\phi^{(n)}\ge 0$ for all $n\ge 1$; equivalently, $\phi(\lambda)=a+b\lambda+\int_0^\infty(1-e^{-\lambda s})\,\nu(ds)$ with $a,b\ge 0$ and $\int_0^\infty(1\wedge s)\,\nu(ds)<\infty$. A **subordinator** is an increasing Lévy process $S_t$, possibly killed at constant rate, with $\mathbb{E}[e^{-\lambda S_t}]=e^{-t\phi(\lambda)}$; $\psi^\phi_t$ is the law of $S_t$ on $[0,\infty)$.
> **In words:** $\phi$ is exactly the class of Laplace exponents of increasing random clocks; $\psi^\phi_t$ is the distribution of where such a clock reads at real time $t$.
> **Concretely:** $\phi(\lambda)=\lambda$ gives the trivial clock $S_t=t$ deterministically ($\psi^\phi_t=\delta_t$). $\phi(\lambda)=\lambda+\kappa$ gives $\psi^\phi_t=e^{-\kappa t}\delta_t$ — deterministic but with survival probability $e^{-\kappa t}$. $\phi(\lambda)=\lambda^{\alpha/2}$ gives a random clock whose density $\eta^\alpha_t(s)=t^{-2/\alpha}g_{\alpha/2}(st^{-2/\alpha})$ is the $\alpha/2$-stable density (heavy-tailed, skewed to large $s$). See [[Def - Bernstein Function, Subordinator, and Subordination]].

> [!recall]- The multiplicative Haar measure $\frac{dt}{t}$
> **Formally:** the $\sigma$-finite measure on $(0,\infty)$ with $\int_{\lambda a}^{\lambda b}\frac{dt}{t}=\int_a^b\frac{dt}{t}$ for every $\lambda>0$; infinite total mass, finite on compacts of $(0,\infty)$.
> **In words:** the scale-invariant weight on positive reals.
> **Concretely:** $\int_1^{e^n}\frac{dt}{t}=n$; the substitution $u=\log t$ turns it into ordinary Lebesgue $du$. See [[Def - Signed and Infinite Measures for Loop Measures]].

> [!recall]- Absolutely continuous measure ($V_\phi(ds)=V_\phi(s)\,ds$)
> **Formally:** a Borel measure $V$ on $(0,\infty)$ is **absolutely continuous with respect to Lebesgue $ds$** if every $ds$-null set is $V$-null; equivalently (Radon–Nikodym), there exists a measurable density $V(s)\ge 0$ with $V(ds)=V(s)\,ds$.
> **In words:** $V$ can be written as "some density times $ds$" — a genuine function on the positive reals telling you how much mass sits near each $s$.
> **Concretely:** for the trivial clock $\phi(\lambda)=\lambda$, $\psi^\phi_t=\delta_t$ is *not* absolutely continuous with respect to $ds$ (all its mass sits at the single point $s=t$), but $V_\phi$ *is*: it works out to $V_\phi(ds)=\frac{ds}{s}$ (see [[Ex - Weighted Potential Measures of the Paper's Bernstein Functions|Example 2.10(a)]]). More generally the $V_\phi$'s in this paper all come out absolutely continuous.

---

# Statement

> **Definition (weighted potential measure; Belyaev–Huseynli Def. 2.9).** For a Bernstein function $\phi$ satisfying Assumption 2.3, the **weighted potential measure** $V_\phi$ is the $\sigma$-finite Borel measure on $(0,\infty)$ characterised by
> $$\int_{(0,\infty)} h(s)\,V_\phi(ds) \;=\; \int_0^\infty \frac{dt}{t}\int_{(0,\infty)} h(s)\,\psi^\phi_t(ds)$$
> for every non-negative measurable $h:(0,\infty)\to[0,\infty]$ making the right-hand side finite. When $V_\phi$ is absolutely continuous with respect to Lebesgue we write $V_\phi(ds)=V_\phi(s)\,ds$; this is the case for every Bernstein function used in the paper.

---

# In One Line

The single measure on the subordination variable $s$ that results from collapsing the loop measure's outer $\int_0^\infty\frac{dt}{t}$ against the subordinator law $\psi^\phi_t$. It is what turns every subordinate-loop-mass double integral (one in $t$, one in $s$) into a *single* heat-kernel integral in $s$ (via [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]]).

---

# Motivation and Unpacking

**Why introduce $V_\phi$ at all.** The [[Def - Subordinate Brownian Loop Measure|subordinate loop measure]]'s mass computations always carry a *double* integral: one in $t$ (the loop's duration, against $\frac{dt}{t}$) and one in $s$ (the subordination time, against the clock law $\psi^\phi_t$). The paper wants to *collapse* the $t$-integral once and for all, so every subsequent computation reduces to a single $s$-integral of the *original* heat kernel $p^E(s,\cdot,\cdot)$. The recipe is the outer integral applied *slot-wise* to $\psi^\phi_\bullet$, and *that recipe is a measure in $s$*. That measure is $V_\phi$: by definition, testing $V_\phi$ against a non-negative $h$ returns the double integral $\int_0^\infty\frac{dt}{t}\int_{(0,\infty)}h(s)\,\psi^\phi_t(ds)$. So $V_\phi$ *is* the compressed record of "apply $\frac{dt}{t}$ to the family $\{\psi^\phi_t\}_{t>0}$." It is the technical heart of §2.4, following [SSV12, Ch. 5].

**Why the definition is a Tonelli-safe swap.** The characterisation of $V_\phi$ is a specific way of packaging the exchange $\int\int h(s)\,\psi^\phi_t(ds)\,\frac{dt}{t}=\int h(s)\,V_\phi(ds)$. Reading right-to-left is the definition; reading left-to-right is precisely the [[Thm - Fubini-Tonelli Theorem|Tonelli]] identity, valid because everything is non-negative and $\sigma$-finite. See [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]] for the mass-computing consequence.

**Sanity check: the paper's three cases.** The worked evaluations in [[Ex - Weighted Potential Measures of the Paper's Bernstein Functions|Example 2.10]] are illuminating and all short:

- **Brownian ($\phi=\lambda$):** $\psi^\phi_t=\delta_t$, so $\int h(s)\,\psi^\phi_t(ds)=h(t)$, giving $\int h(s)\,V_\phi(ds)=\int_0^\infty h(t)\,\frac{dt}{t}$. Hence **$V_\phi(ds)=\frac{ds}{s}$** — the multiplicative Haar measure comes back. (Subordination did nothing.)
- **Killing ($\phi=\lambda+\kappa$):** $\psi^\phi_t=e^{-\kappa t}\delta_t$, so $\int h(s)\,\psi^\phi_t(ds)=e^{-\kappa t}h(t)$, giving $\int h(s)\,V_\phi(ds)=\int_0^\infty e^{-\kappa t}h(t)\,\frac{dt}{t}$. Hence **$V_\phi(ds)=e^{-\kappa s}\,\frac{ds}{s}$**.
- **$\alpha$-stable ($\phi=\lambda^{\alpha/2}$):** the computation is a substitution ($u=s t^{-2/\alpha}$) that turns $\int_0^\infty\frac{1}{t}\,t^{-2/\alpha}g_{\alpha/2}(s t^{-2/\alpha})\,dt$ into $\frac{\alpha}{2s}\int_0^\infty g_{\alpha/2}(u)\,du=\frac{\alpha}{2s}$ (since $g_{\alpha/2}$ is a probability density). Hence **$V_\phi(ds)=\frac{\alpha}{2}\frac{ds}{s}$** — the Haar measure again, up to the constant $\alpha/2$.
- **Shifted $\alpha$-stable ($\phi=(\lambda+\kappa)^{\alpha/2}$):** by the same substitution applied to $\psi^\phi_t(ds)=e^{-\kappa s}\eta^\alpha_t(s)\,ds$, **$V_\phi(ds)=\frac{\alpha}{2}e^{-\kappa s}\,\frac{ds}{s}$**.

**The scale-invariance pattern.** Three of the four $V_\phi$'s are $\frac{ds}{s}$ up to a constant (Brownian and $\alpha$-stable), and two carry an $e^{-\kappa s}$ tilt (killing and shifted $\alpha$-stable). The pattern reflects the paper's Remark in §3.1.3: the stable clocks are *self-similar* and $\frac{dt}{t}$ is itself scale-invariant, so their combination yields the scale-invariant $\frac{ds}{s}$; killing breaks scale-invariance and shows up as an $e^{-\kappa s}$ tilt.

**What "makes the right-hand side finite" means.** The technical clause in the definition is not decorative: for pathological non-negative $h$ (e.g. constants) the double integral may be $+\infty$, and $V_\phi$ is defined implicitly by the identity only on the class of $h$ where it converges. The Bernstein functions in the paper all give an absolutely continuous $V_\phi$ with the explicit densities above, so the identity holds for every non-negative measurable $h$ in the usual $L^1(V_\phi)$ sense.

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.4]] as the technical device that collapses the $t$-integral. Its four worked evaluations for the paper's Bernstein functions are [[Ex - Weighted Potential Measures of the Paper's Bernstein Functions|Example 2.10]]; the general collapsing identity is [[Lemma - Collapsing the Time Integral of the Subordinate Kernel|Lemma 2.11]]. Every free-homotopy-class mass in §3 (as in [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] and its computations in §3.1) uses $V_\phi$ to reduce a $t$-integral of the subordinate kernel to a single $s$-integral of the original one.
