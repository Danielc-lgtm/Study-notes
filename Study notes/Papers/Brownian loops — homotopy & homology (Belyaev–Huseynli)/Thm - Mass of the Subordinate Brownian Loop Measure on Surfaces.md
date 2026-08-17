---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces"
  - "Thm - The Wang–Xue Fundamental-Strip Identity"
  - "Thm - Collapsing the Time Integral into the Weighted Potential Measure"
  - "Constr - The Weighted Potential Measure Vϕ"
tags: [paper, probability, hyperbolic-geometry, loop-measures]
---

# Notation

- $\phi$ — a [[Def - Bernstein Function and the Lévy–Khintchine Representation|Bernstein function]] satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]]; $V_\phi$ its [[Constr - The Weighted Potential Measure Vϕ|weighted potential measure]] on $(0,\infty)$
- $\mu^\phi_X$ — the [[Constr - The Subordinate Brownian Loop Measure|subordinate Brownian loop measure]] on $X=\Gamma\backslash\mathbb{H}^2$
- $\gamma\in\mathcal{P}_X$ — a primitive oriented closed geodesic of length $\ell_\gamma$; $m\geq1$ the winding number
- $L := m\ell_\gamma$ — the length of the geodesic representative; note $\ell_\gamma/L=1/m$
- $\mathcal{C}_X(\gamma^m)$ — the free homotopy class winding $m$ times around $\gamma$
- $F_\tau$ — the fundamental strip; $\psi^\phi_t$ the subordinator law; $p_{\mathbb{H}^2}$ the Brownian heat kernel on $\mathbb{H}^2$
- $s$ — the subordination variable, **not** the loop duration $t$; in §4 onwards the same letter denotes the spectral parameter, a genuine notational collision the paper does not resolve

---

# Type card

> [!abstract] Type card — Theorem 3.5 (mass of the subordinate Brownian loop measure)
> **Given.** A [[Def - Bernstein Function and the Lévy–Khintchine Representation|Bernstein function]] $\phi$ satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]]; a [[Def - Primitive Hyperbolic Element and Translation Length|primitive closed geodesic]] $\gamma\in\mathcal{P}_X$ of length $\ell_\gamma$; a winding number $m\geq1$. Write $L=m\ell_\gamma$. For jump processes, the left-hand side is read through [[Constr - Loop Mass in a Homotopy Class for Jump Processes|Remark 3.1]].
>
> **Produces.** A closed-form value for $\mu^\phi_X(\mathcal{C}_X(\gamma^m))$ — a non-negative number, possibly infinite — as a purely geometric prefactor times a **single** integral of an explicit heat-kernel factor against the [[Constr - The Weighted Potential Measure Vϕ|weighted potential measure]] $V_\phi$.
>
> **Lets you.** Replace the double $(t,s)$ integral by one integral against $V_\phi$, which is what makes every later special case — Brownian, killing, $\alpha$-stable, shifted $\alpha$-stable — a one-line substitution of a single measure on $(0,\infty)$.

---

# Statement

> **Theorem 3.5 (mass of subordinate Brownian loop measure on hyperbolic surfaces).** Let $\phi$ be a Bernstein function satisfying Assumption 2.3. Then for any $\gamma\in\mathcal{P}_X$ and $m\geq1$,
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(\mathrm{d}s),\tag{21}$$
> where $L=m\ell_\gamma$ and $V_\phi$ is the weighted potential measure of Definition 2.9.

Writing $I_\phi(L)$ for the integral — see [[Constr - The Weighted Heat-Kernel Integral Iϕ|Definition 3.6]] — the theorem reads
$$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac{\ell_\gamma}{2\sinh(L/2)}\,I_\phi(L) = \frac1m\cdot\frac{L}{2\sinh(L/2)}\,I_\phi(L),\tag{24}$$
the second form using $\ell_\gamma=L/m$. **The second form is the one [[Thm - Selberg Zeta Criterion|Lemma 4.2]] operates on**, because it isolates the $1/m$ that will become a logarithm.

---

# Why it is true

The theorem is the composition of two discharges, and the reason it looks like an answer rather than a rearrangement is that each discharge kills a different variable.

After [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]], the class mass is $\int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau}p^\phi_{\mathbb{H}^2}(t,z,\tau^m z)\,\mathrm{d}\rho_{\mathbb{H}^2}(z)$. Expanding the subordinate kernel by (6) turns this into a *triple* integral, in $t$, in the spatial variable $z$, and in the subordination variable $s$. That looks worse. But the three variables are almost independent of one another: the geometry lives entirely in $z$, the subordination lives entirely in $s$, and $t$ appears nowhere except inside $\psi^\phi_t$.

So discharge them in the right order. **The spatial integral first**, by [[Thm - The Wang–Xue Fundamental-Strip Identity|Lemma 3.4]] — this is where all the hyperbolic geometry goes, and it comes out as the prefactor $\ell_\gamma/2\sinh(L/2)$ times a function of $(s,L)$. **The time integral second**, by [[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11]] — this is where all the subordination goes, and it comes out as $V_\phi$. What is left is one integral in $s$, against $V_\phi$, of the analytic factor Lemma 3.4 produced.

**The mechanism in one line: the geometry and the subordination live in different variables of the same triple integral, so each can be integrated out completely without touching the other, and the answer is their product.**

The consequence is the architecture of the second half of the paper. The prefactor is inert under changes of $\phi$; the integral is inert under changes of the surface. **Change the surface and only $\ell_\gamma$ moves; change the process and only $V_\phi$ moves.** This is why §3.1's four special cases are four substitutions of a one-line table, and why §4's zeta criterion can be stated with no geometry in it.

---

# Strategy

**Strategy.** Evaluate the spatial integral by the Wang–Xue identity (Lemma 3.4), then collapse the $\mathrm{d}t/t$ integral into $V_\phi$ by Lemma 2.11.

> [!note]- Proof (skippable)
> Applying [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]] with $p^{\mathcal{E}}_{\mathbb{H}^2}=p^\phi_{\mathbb{H}^2}$ and expanding via the subordination formula (6),
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = \int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau}\int_{[0,\infty)}p_{\mathbb{H}^2}(s,z,\tau^m z)\,\psi^\phi_t(\mathrm{d}s)\,\mathrm{d}\rho_{\mathbb{H}^2}(z).\tag{19}$$
>
> **Step 1 — the spatial integral.** By Lemma 3.4, for each fixed $s>0$,
> $$\int_{F_\tau}p_{\mathbb{H}^2}(s,z,\tau^m z)\,\mathrm{d}\rho_{\mathbb{H}^2}(z) = \frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}.$$
> Exchanging the $z$- and $s$-integrals in (19) by Tonelli — everything is non-negative — and substituting,
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty\frac{\mathrm{d}t}{t}\int_{[0,\infty)}\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,\psi^\phi_t(\mathrm{d}s).\tag{22}$$
> The geometric prefactor is independent of $s$ and $t$ and comes straight out of both integrals.
>
> **Step 2 — the time integral.** Apply [[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11]] with
> $$h(s) = \frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}},$$
> which is non-negative and measurable. The lemma — in its defining form (7) rather than in the kernel form (8), the two being the same statement — collapses the double integral into a single integral against $V_\phi$, giving (21). $\;\square$

---

# What this assumes, and where to climb

**Theorem 3.2**, hence its entire hypothesis stack: a $\Gamma$-invariant Dirichlet form whose kernel [[Constr - The Periodised Kernel|periodises]], the [[Def - Centraliser and Coset Enumeration of a Conjugacy Class|coset enumeration]], and the [[Constr - Standard-Form Representative and the Fundamental Strip|standard form and strip]]. Climb through [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]].

**Lemma 3.4**, which requires the *Brownian* heat kernel on $\mathbb{H}^2$ in standard form. This is the step that narrows the theorem from the Dirichlet-form generality of §3 down to subordinate Brownian motion: (6) writes $p^\phi_{\mathbb{H}^2}$ as an average of $p_{\mathbb{H}^2}(s,\cdot,\cdot)$, and it is the inner Brownian kernel that Lemma 3.4 evaluates. A Dirichlet form not obtained by subordinating Brownian motion would leave the spatial integral undischargeable, and Theorem 3.2 would be as far as one could go.

**Lemma 2.11 and hence Assumption 2.3.** Without a subordinate transition density there is no (19) to start from.

**No finiteness is assumed and none is concluded.** (21) is an identity in $[0,\infty]$. Whether the number is finite — and whether the sum over all classes is — is settled separately in [[Thm - Finiteness of the Total Mass|Corollary 4.7]].

**For jump processes**, the left-hand side is a definition. Recall from [[Constr - Loop Mass in a Homotopy Class for Jump Processes]] that in the $\alpha$-stable cases the identity relates a *defined* quantity to a computed one.

---

# What consumes this

- [[Constr - The Weighted Heat-Kernel Integral Iϕ|Definition 3.6]] — names the integral so that the theorem reads (24)
- [[§3 Decomposition over Homotopy Classes]] §3.1.1–3.1.4 — the four special cases, each a substitution of one line of the $V_\phi$ table
- [[Thm - Selberg Zeta Criterion|Lemma 4.2]] — operates on the form (24), and its hypothesis is a condition on $\frac{L}{2\sinh(L/2)}I_\phi(L)$
- [[Thm - Loop Masses Determine the Marked Length Spectrum|Proposition 3.11]] — inverts the Brownian and killing specialisations
- [[Constr - The Probability Measure on Free Homotopy Classes]] — the numerator of $\mathbb{P}_s$
- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds|Theorem 7.2]] — the three-dimensional analogue, proved by the identical two-step strategy

---

# Reading it against the rest of the paper

The Brownian specialisation $\mu_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac{1}{e^L-1}$ recovers Wang–Xue [WX25, Lemma 3.2], and the killing specialisation $\frac1m\frac{e^{(1-s)L}}{e^L-1}$ recovers Lemonde–Wang [LW26, Lemma 3.1]. So this theorem's novelty is not any single case but the *uniformity*: it proves both at once, plus the two stable cases, and it isolates exactly where a new process would enter.

Read alongside [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds|Corollary 7.3]], the theorem also shows what is dimension-specific. The prefactor $\ell_\gamma/2\sinh(L/2)$ and the analytic factor $e^{-s/4}e^{-L^2/4s}/2\sqrt{\pi s}$ both change in three dimensions; the *structure* — geometric prefactor times $V_\phi$-integral — does not. That structural persistence is what makes §7 short.
