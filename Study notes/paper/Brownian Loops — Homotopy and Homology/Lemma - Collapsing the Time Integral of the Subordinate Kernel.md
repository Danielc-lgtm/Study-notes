---
type: lemma
subject: probability
prereqs:
  - "Def - Weighted Potential Measure"
  - "Def - Subordinate Brownian Loop Measure"
  - "Def - Bernstein Function, Subordinator, and Subordination"
  - "Def - Signed and Infinite Measures for Loop Measures"
tags: [paper, brownian-loops]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Lemma 2.11"
---

# Notation

$(X,g)$ a Riemannian surface; $(\mathcal E,\mathcal F)$ a regular symmetric Dirichlet form on $L^2(X,\operatorname{vol}_g)$ with symmetric transition density $p^E:(0,\infty)\times X\times X\to(0,\infty)$. $\phi$ a Bernstein function satisfying the paper's Assumption 2.3 ($b>0$ or $\nu(0,\infty)=\infty$), with subordinator law $\psi^\phi_t$ on $[0,\infty)$; the assumption gives $\psi^\phi_t(\{0\})=0$. Subordinate transition density $p^\phi(t,x,y)=\int_{[0,\infty)}p^E(s,x,y)\,\psi^\phi_t(ds)=\int_{(0,\infty)}p^E(s,x,y)\,\psi^\phi_t(ds)$ (the second equality uses Assumption 2.3 to drop the atom at $0$). $V_\phi$ the weighted potential measure of Definition 2.9, defined by $\int_{(0,\infty)} h(s)\,V_\phi(ds)=\int_0^\infty\frac{dt}{t}\int_{(0,\infty)}h(s)\,\psi^\phi_t(ds)$. Points $x,y\in X$.

> [!recall]- Subordinate heat kernel $p^\phi$ (average of $p^E$ against the subordinator law)
> **Formally:** $p^\phi(t,x,y)=\int_{[0,\infty)}p^E(s,x,y)\,\psi^\phi_t(ds)$; Assumption 2.3 makes $\psi^\phi_t(\{0\})=0$ so equivalently the integration is over $(0,\infty)$.
> **In words:** the subordinate kernel at time $t$ is the *average* of the original kernel at subordination time $s$, weighted by the clock's law of "where the clock reads at real time $t$".
> **Concretely:** if $\phi(\lambda)=\lambda+\kappa$ then $\psi^\phi_t=e^{-\kappa t}\delta_t$, so $p^\phi(t,x,y)=e^{-\kappa t}p^E(t,x,y)$: the ambient kernel scaled by the survival probability. If $\phi(\lambda)=\lambda^{\alpha/2}$ then $\psi^\phi_t(ds)=\eta^\alpha_t(s)\,ds$ (the $\alpha/2$-stable density) and $p^\phi(t,x,y)=\int_0^\infty p^E(s,x,y)\,\eta^\alpha_t(s)\,ds$ — a genuine convolution of $p^E$ against a stable density. See [[Def - Bernstein Function, Subordinator, and Subordination]].

> [!recall]- Weighted potential measure $V_\phi$
> **Formally:** the $\sigma$-finite measure on $(0,\infty)$ characterised by $\int h(s)\,V_\phi(ds)=\int_0^\infty\frac{dt}{t}\int h(s)\,\psi^\phi_t(ds)$ for every non-negative measurable $h$ making the right side finite. In every case of the paper, $V_\phi(ds)=V_\phi(s)\,ds$ (absolutely continuous), with explicit densities: $\frac{1}{s}$ (Brownian), $\frac{e^{-\kappa s}}{s}$ (killing), $\frac{\alpha}{2s}$ ($\alpha$-stable), $\frac{\alpha e^{-\kappa s}}{2s}$ (shifted $\alpha$-stable).
> **In words:** the compressed record of "apply the multiplicative Haar measure $\frac{dt}{t}$ to the subordinator's law." A measure that lives on the subordination variable $s$, encoding all the $t$-averaging.
> **Concretely:** for Brownian ($\phi=\lambda$), $\psi^\phi_t=\delta_t$, so $\int h(s)\,V_\phi(ds)=\int h(t)\,\frac{dt}{t}$ — reading off $V_\phi=\frac{ds}{s}$. The identity says: instead of doing the $t$-integral first, absorb it into a single measure $V_\phi$ in $s$. See [[Def - Weighted Potential Measure]] and [[Ex - Weighted Potential Measures of the Paper's Bernstein Functions]] for all four cases.

> [!recall]- $\sigma$-finite measure
> **Formally:** a measure $\mu$ on $(\Omega,\mathcal F)$ is **$\sigma$-finite** if $\Omega=\bigcup_n\Omega_n$ with $\mu(\Omega_n)<\infty$.
> **In words:** the space breaks into countably many finite-mass pieces, so integration behaves nicely (Fubini/Tonelli work).
> **Concretely:** $\frac{dt}{t}$ on $(0,\infty)$: infinite total, but $\int_{1/n}^n\frac{dt}{t}=2\log n<\infty$. The subordinator law $\psi^\phi_t$ (fixed $t$) is a *probability* measure (or sub-probability with $|\psi^\phi_t|=e^{-at}$ if there is killing), hence finite; the family $\{\psi^\phi_t\}_{t>0}$ threaded through $\frac{dt}{t}$ becomes $\sigma$-finite jointly. See [[Def - σ-Finite Measure]].

---

# Statement

> **Lemma (Belyaev–Huseynli 2.11).** Under the standing hypotheses, for all $x,y\in X$,
> $$\int_0^\infty \frac{dt}{t}\,p^\phi(t,x,y) \;=\; \int_{(0,\infty)} p^E(s,x,y)\,V_\phi(ds).$$

---

# In One Line

Integrating the subordinate kernel against the scale-invariant duration weight $\frac{dt}{t}$ equals integrating the *original* kernel against the weighted potential measure $V_\phi$ — the identity that collapses every subsequent loop-mass double integral (over duration $t$ and subordination time $s$) into a single $s$-integral of the original heat kernel.

---

# Why It's True

**Mechanism (one line).** $p^\phi$ is a $\psi^\phi_t$-average of $p^E(s,\cdot,\cdot)$; $V_\phi$ is by definition "$\int_0^\infty\frac{dt}{t}$ applied to $\psi^\phi_t$"; so integrating $p^\phi$ against $\frac{dt}{t}$ *must* reproduce $p^E$ integrated against $V_\phi$. The only genuine step is swapping the order of the $t$- and $s$-integrals, and $\sigma$-finiteness + non-negativity buys that.

**Why one should expect it before the proof.** Read the definitions in slow motion: $p^\phi(t,x,y)=\int p^E(s,x,y)\,\psi^\phi_t(ds)$ says "the subordinate kernel at $t$ is a linear functional of the map $s\mapsto p^E(s,x,y)$, with kernel $\psi^\phi_t$." Applying $\int_0^\infty\frac{dt}{t}(\cdot)$ to a linear functional in a family $\{\psi^\phi_t\}_t$ just glues the family into one big linear functional — namely $\int h(s)\,V_\phi(ds)$ — by the very definition of $V_\phi$. So the identity is bookkeeping about the definition of $V_\phi$, plus a legality check for the order swap.

---

# Proof

> [!cite]- External input — Fubini–Tonelli theorem (Tonelli half)
> **Statement (typed):** if $(\Omega_1,\mu_1)$ and $(\Omega_2,\mu_2)$ are $\sigma$-finite measure spaces and $F:\Omega_1\times\Omega_2\to[0,\infty]$ is jointly measurable and non-negative, then $\int_{\Omega_1}\!\int_{\Omega_2}F(x,y)\,d\mu_2(y)\,d\mu_1(x)=\int_{\Omega_2}\!\int_{\Omega_1}F(x,y)\,d\mu_1(x)\,d\mu_2(y)$ (both equal the double integral over $\Omega_1\times\Omega_2$; no integrability hypothesis is needed for non-negative $F$).
> **Why it's true:** for non-negative integrands both iterated integrals compute the total "volume under the graph" of $F$, which is order-independent. Monotone convergence lets you build the joint measurable structure from step functions where the swap is a finite sum.
> **Source:** [[Thm - Fubini-Tonelli Theorem|vault note]]; Folland, *Real Analysis*, Theorem 2.37. Applicable here because $p^E\ge 0$ and all the measures in play ($\frac{dt}{t}$ on $(0,\infty)$, the family $\{\psi^\phi_t\}_{t>0}$, and $V_\phi$) are $\sigma$-finite.

> [!note]- Gap-free proof of Lemma 2.11
> **Step 1 — expand the subordinate kernel.** By the subordination formula for the transition density,
> $$p^\phi(t,x,y) \;=\; \int_{(0,\infty)} p^E(s,x,y)\,\psi^\phi_t(ds).$$
> (Integration is over $(0,\infty)$ rather than $[0,\infty)$: Assumption 2.3 gives $\psi^\phi_t(\{0\})=0$, so the atom at $s=0$ contributes nothing.) Substituting,
> $$\int_0^\infty\frac{dt}{t}\,p^\phi(t,x,y) \;=\; \int_0^\infty\frac{dt}{t}\int_{(0,\infty)} p^E(s,x,y)\,\psi^\phi_t(ds).$$
>
> **Step 2 — set up Tonelli.** The integrand $F(t,s):=p^E(s,x,y)$ (with $x,y$ fixed) is a function on $(0,\infty)\times(0,\infty)$ that is non-negative, jointly measurable (Borel measurable in $(t,s)$, since it does not depend on $t$ and is Borel in $s$ by the assumed joint measurability of $p^E$), and the two measures $\frac{dt}{t}$ on $(0,\infty)$ and the kernel $\psi^\phi_\bullet$ (regarded as a $\sigma$-finite measure on $(0,\infty)\times(0,\infty)$ via $A\times B\mapsto\int_A\psi^\phi_t(B)\,\frac{dt}{t}$) are both $\sigma$-finite. All Tonelli hypotheses are met.
>
> **Step 3 — swap the order (Tonelli).** By the Tonelli half of Fubini–Tonelli (cited above),
> $$\int_0^\infty\frac{dt}{t}\int_{(0,\infty)} p^E(s,x,y)\,\psi^\phi_t(ds) \;=\; \int_{(0,\infty)} p^E(s,x,y)\,\Big(\int_0^\infty\frac{dt}{t}\,\psi^\phi_t(ds)\Big),$$
> where the bracketed object is *not* a number but the recipe that, tested against a non-negative $h$, returns $\int_0^\infty\frac{dt}{t}\int h\,d\psi^\phi_t$. This is exactly the definitional characterisation of $V_\phi$ ([[Def - Weighted Potential Measure|Definition 2.9]]).
>
> **Step 4 — recognise $V_\phi$.** Apply [[Def - Weighted Potential Measure|Definition 2.9]] with the test function $h(s):=p^E(s,x,y)$ (non-negative and measurable; the RHS is finite for the Bernstein functions in play — the paper's Example 2.10 gives $V_\phi(ds)$ explicitly, and $p^E$'s integrability against these $V_\phi$ is exactly the condition that the loop mass be well-defined). By definition,
> $$\int_0^\infty\frac{dt}{t}\int_{(0,\infty)} p^E(s,x,y)\,\psi^\phi_t(ds) \;=\; \int_{(0,\infty)} p^E(s,x,y)\,V_\phi(ds).$$
>
> **Chaining.** Steps 1–4 give
> $$\int_0^\infty\frac{dt}{t}\,p^\phi(t,x,y) \;=\; \int_{(0,\infty)} p^E(s,x,y)\,V_\phi(ds),$$
> as claimed. $\qquad\blacksquare$
>
> *(This is the paper's own two-line proof — "By (4) and Tonelli … taking $h(s)=p^E(s,x,y)$ in (7)" — written out with the Tonelli hypotheses checked explicitly and the $s=0$ atom accounted for by Assumption 2.3.)*

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.4]] as the payoff of the weighted-potential-measure device. Every free-homotopy-class mass in §3 (as in [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] and its per-process evaluations in §3.1) is of the form $\int_0^\infty\frac{dt}{t}(\text{subordinate kernel between }z\text{ and }\tau^m z)$; the Lemma rewrites each as a single $\int p^E(s,\cdot,\cdot)\,V_\phi(ds)$, and then the geometry of the geodesic lets the $s$-integral be evaluated in closed form. Also central to the zeta identities of §4.
