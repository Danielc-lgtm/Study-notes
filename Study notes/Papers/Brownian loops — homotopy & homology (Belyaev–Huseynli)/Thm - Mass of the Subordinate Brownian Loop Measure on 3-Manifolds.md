---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds"
  - "Thm - The H3 Fundamental-Slab Heat-Kernel Identity"
  - "Thm - Collapsing the Time Integral into the Weighted Potential Measure"
  - "Constr - The Weighted Potential Measure Vϕ"
tags: [paper, probability, hyperbolic-geometry, loop-measures]
---

# Notation

- $\phi$ — one of the paper's Bernstein functions; $V_\phi$ its [[Constr - The Weighted Potential Measure Vϕ|weighted potential measure]] on $(0,\infty)$
- $\gamma\in\mathcal{P}_X$ — a primitive closed geodesic on $X=\Gamma\backslash\mathbb{H}^3$, with complex length $L_\gamma=\ell_\gamma+i\theta_\gamma$
- $m\geq1$ — the winding number; $L=mL_\gamma=m\ell_\gamma+im\theta_\gamma$
- $s$ — the subordination variable inside the integral
- $F_\tau$ — the [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab|fundamental slab]]; $\psi^\phi_t$ the subordinator law

---

# Type card

> [!abstract] Type card — Theorem 7.2 (mass of the subordinate loop measure, 3-manifolds)
> **Given.** Any of the [[Def - Bernstein Function and the Lévy–Khintchine Representation|Bernstein functions]] considered in the paper; a primitive closed geodesic $\gamma\in\mathcal{P}_X$ with [[Def - Kleinian Group and Loxodromic Complex Length|complex length]] $L_\gamma=\ell_\gamma+i\theta_\gamma$; a winding number $m\geq1$. Write $L=mL_\gamma$. For jump processes, the left side is read through [[Constr - Loop Mass in a Homotopy Class for Jump Processes|Remark 3.1]].
>
> **Produces.** A closed-form value for $\mu^\phi_X(\mathcal{C}_X(\gamma^m))$, a non-negative number, as a purely geometric prefactor — containing the holonomy through $|e^L-1|^2$ — times a **single** integral against the [[Constr - The Weighted Potential Measure Vϕ|weighted potential measure]] $V_\phi$.
>
> **Lets you.** Specialise to any subordination in three dimensions exactly as in §3: the choice of process still enters only through $V_\phi$, so each case is a one-line substitution.

---

# Statement

> **Theorem 7.2 (mass of subordinate Brownian loop measure on hyperbolic 3-manifolds).** Let $\phi$ be one of the Bernstein functions considered in this paper. For any $\gamma\in\mathcal{P}_X$ and $m\geq1$,
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{\big|e^{L}-1\big|^2}\int_{(0,\infty)}\frac{2se^{-s}}{(4\pi s)^{3/2}}\,e^{-(m\ell_\gamma)^2/4s}\,V_\phi(\mathrm{d}s),\tag{90}$$
> where $L=mL_\gamma=m\ell_\gamma+im\theta_\gamma$ and $V_\phi$ is the weighted potential measure of Definition 2.9.

---

# Why it is true

It is [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] with two ingredients swapped, and the swap is exactly the two dimension-dependent ones.

The structure is unchanged. [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds|Theorem 7.1]] gives the class mass as a double integral in $t$ and the spatial variable; expanding the subordinate kernel by (6) makes it a triple integral in $(t,w,s)$; and the three variables are almost independent — the geometry lives in $w$, the subordination in $s$, and $t$ appears nowhere except inside $\psi^\phi_t$. So discharge them in the right order: the spatial integral first, by the [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity|slab identity (88)]]; the time integral second, by [[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11]].

**What changed from §3.** Only the two things that are genuinely three-dimensional. The **geometric prefactor** is now $\frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{|e^L-1|^2}$ rather than $\frac{\ell_\gamma}{2\sinh(L/2)}$ — this is where the holonomy angle lives, entering through the modulus $|e^{m\ell_\gamma+im\theta_\gamma}-1|^2$. And the **analytic factor** is $\frac{2se^{-s}}{(4\pi s)^{3/2}}e^{-(m\ell_\gamma)^2/4s}$ rather than $\frac{e^{-s/4}e^{-L^2/4s}}{2\sqrt{\pi s}}$ — different normalisation, and $e^{-s}$ rather than $e^{-s/4}$ because the bottom of the $L^2$-spectrum of $\Delta_{\mathbb{H}^n}$ is $(n-1)^2/4$, equal to $1$ in dimension $3$.

**What did not change: the separation.** The holonomy sits only in the prefactor; the analytic factor depends only on $s$ and the *real* part $m\ell_\gamma$. **That is why the subordination machinery goes through untouched — $V_\phi$ never meets $\theta_\gamma$.**

**The mechanism in one line: the geometry and the subordination live in different variables of the same triple integral, exactly as in §3, and the only three-dimensional content is which two explicit factors appear.**

---

# Strategy

**Strategy.** The §3.5 strategy verbatim: evaluate the spatial integral by the slab identity (88), then collapse the $\mathrm{d}t/t$ integral into $V_\phi$ by Lemma 2.11, applied with $h(s)=\frac{2se^{-s}}{(4\pi s)^{3/2}}e^{-(m\ell_\gamma)^2/4s}$.

> [!note]- Proof (skippable)
> Applying [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds|Theorem 7.1]] with $p^{\mathcal{E}}_{\mathbb{H}^3}=p^\phi_{\mathbb{H}^3}$ and expanding via the subordination formula (6),
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = \int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau}\int_{[0,\infty)}p_{\mathbb{H}^3}\big(s,w,\tau^mw\big)\,\psi^\phi_t(\mathrm{d}s)\,\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}(w).\tag{86}$$
>
> **Step 1 — the spatial integral.** The inner spatial integral is taken against the Brownian kernel $p_{\mathbb{H}^3}(s,\cdot,\cdot)$ at the subordination time $s$, and is evaluated by (88):
> $$\int_{F_\tau}p_{\mathbb{H}^3}\big(s,w,\tau^mw\big)\,\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}(w) = \frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{|e^L-1|^2}\cdot\frac{2se^{-s}}{(4\pi s)^{3/2}}\,e^{-(m\ell_\gamma)^2/4s}.$$
> Exchanging the $w$- and $s$-integrals by Tonelli — everything non-negative — and substituting,
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{|e^L-1|^2}\int_0^\infty\frac{\mathrm{d}t}{t}\int_{[0,\infty)}\frac{2se^{-s}}{(4\pi s)^{3/2}}e^{-(m\ell_\gamma)^2/4s}\,\psi^\phi_t(\mathrm{d}s),$$
> the geometric prefactor coming out of both integrals since it is independent of $s$ and $t$.
>
> **Step 2 — the time integral.** Apply [[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11]] with
> $$h(s) = \frac{2se^{-s}}{(4\pi s)^{3/2}}\,e^{-(m\ell_\gamma)^2/4s},$$
> non-negative and measurable, which collapses the double integral into a single integral against $V_\phi$, giving (90). $\;\square$

---

# What this assumes, and where to climb

**Theorem 7.1** — [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds]], hence the loxodromic standard form, the slab, the coset enumeration, and the periodisation with $\Gamma$-invariance.

**The slab identity** — [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity]], which requires the *Brownian* heat kernel on $\mathbb{H}^3$ in standard form. This is the step that narrows the theorem from the Dirichlet-form generality of Theorem 7.1 down to subordinate Brownian motion, exactly as Lemma 3.4 does in §3.

**Lemma 2.11 and hence Assumption 2.3** — [[Thm - Collapsing the Time Integral into the Weighted Potential Measure]] and [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)]]. Note that the *same* Lemma 2.11 serves both dimensions: it is a statement about kernels and subordinator laws with no geometry in it, and this is the second of its two uses in the paper.

**No finiteness is assumed or concluded.** (90) is an identity in $[0,\infty]$. **And unlike §3, no finiteness is ever established downstream** — there is no three-dimensional analogue of [[Thm - Finiteness of the Total Mass|Corollary 4.7]], because there is no three-dimensional zeta criterion. See below.

**For jump processes**, the left side is a definition, via [[Constr - Loop Mass in a Homotopy Class for Jump Processes]].

---

# What consumes this

- [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds|Corollary 7.3]] — the Brownian specialisation $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$
- [[§7 Brownian Loops on Hyperbolic 3-Manifolds]]

Nothing else. **§7 stops here**, and the reason is worth recording on this page since it is this theorem's answer that causes it.

---

# Reading it against the rest of the paper

Set (90) beside [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|(21)]] and the architecture is identical: geometric prefactor times $V_\phi$-integral, with the process entering only through $V_\phi$. **The persistence of that structure across a change of dimension is the strongest evidence that the paper's framework is about the right things** — a heat kernel, a discrete deck group, and a subordination, none of which is dimensional.

But the *values* do not persist, and that is what stops §7 short. Specialising to Brownian motion gives $\frac1m|e^{mL_\gamma}-1|^{-2}$ ([[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds|Corollary 7.3]]), and this is **not** of the form $\frac{C}{m}\frac{e^{(1-s)L}}{e^L-1}$ that [[Thm - Selberg Zeta Criterion|Lemma 4.2]] demands. So the Selberg criterion does not apply as stated: there is no zeta identity, no finiteness criterion, and no probability measure on the homotopy classes of a hyperbolic $3$-manifold.

The natural object is presumably a Selberg zeta function for $\Gamma\subset\mathrm{PSL}(2,\mathbb{C})$ built from complex lengths, and the natural question is which functional equation replaces (33). That is the paper's most concrete unfinished business, recorded on [[Map - Brownian Loops on Homotopy and Homology Classes]].
