---
type: remark
subject: probability-geometry
prereqs:
  - "Lemma - Selberg Zeta Criterion"
  - "Def - The Loop-Length Integral"
  - "Ex - The Subordinate Form of Brownian Motion with Killing"
tags: [paper, brownian-loops, zeta-functions]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "unnumbered; §4.1.1 — killing-case shape-check for the Selberg zeta criterion"
---

# Notation

- $X = \Gamma\backslash\mathbb H^2$ — a geometrically finite hyperbolic surface (quotient of the upper half-plane by a discrete isometry group $\Gamma$).
- $\gamma \in \mathcal P_X$ — a primitive oriented closed geodesic on $X$, of length $\ell_\gamma > 0$.
- $m \ge 1$ — the winding number of a loop around $\gamma$; **total translation length** $L := m\ell_\gamma > 0$.
- $\kappa \in [-\frac14, \infty)$ — a real **killing rate**; the driving Bernstein function is $\phi(\lambda) = \lambda + \kappa$.
- $I_\kappa(L)$ — the loop-length integral of the killed process; closed form $I_\kappa(L) = e^{-L\sqrt{1/4 + \kappa}}/L$.
- $s = s(\kappa) := \frac12 + \sqrt{\frac14 + \kappa}$ — the **spectral parameter** attached to $\kappa$; real for $\kappa \ge -\frac14$, with $s(-\frac14) = \frac12$, $s(0) = 1$, $s(\kappa) \to \infty$ as $\kappa \to \infty$.
- $C > 0$ — the constant appearing in the [[Lemma - Selberg Zeta Criterion|Selberg zeta criterion (Lemma 4.2)]]; here it will come out to $C = 1$.
- $2\sinh(L/2) = e^{L/2} - e^{-L/2}$ — the standard hyperbolic-sine identity, used throughout.

> [!recall]- Loop-length integral $I_\phi(L)$
> **Formally:** for a Bernstein function $\phi$ with weighted potential measure $V_\phi$ on $(0, \infty)$, and $L > 0$, $I_\phi(L) := \int_0^\infty \frac{e^{-s/4} e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(ds)$ (the internal-clock variable $s$ inside the integrand is *not* the zeta variable below). [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] states that the class-mass factors as $\mu^\phi_X(C_X(\gamma^m)) = \frac{\ell_\gamma}{2\sinh(L/2)}\,I_\phi(L)$ with $L = m\ell_\gamma$.
> **In words:** package every piece of the class-mass that depends on the driving process $\phi$ into one 1-D integral in a dummy variable; call it $I_\phi(L)$. The class-mass then splits cleanly into a **geometric prefactor** $\ell_\gamma/[2\sinh(L/2)]$ and a **process integral** $I_\phi(L)$; the Selberg zeta criterion asks whether the combination $\frac{L}{2\sinh(L/2)}\,I_\phi(L)$ has the canonical shape $C \cdot e^{(1-s)L}/(e^L - 1)$.
> **Concretely:** for plain Brownian motion ($\phi(\lambda) = \lambda$, $V_\phi(ds) = ds/s$), $I_\phi(L) = e^{-L/2}/L$; at $L = 1$, $I_\phi(1) = e^{-1/2} \approx 0.607$. For killed Brownian motion ($\phi(\lambda) = \lambda + \kappa$, $V_\phi(ds) = e^{-\kappa s}\,ds/s$), $I_\kappa(L) = e^{-L\sqrt{1/4 + \kappa}}/L$; at $\kappa = 0$ this recovers the Brownian case. Full detail: [[Def - The Loop-Length Integral]].

> [!recall]- Killed Bernstein function $\phi(\lambda) = \lambda + \kappa$ and its weighted potential
> **Formally:** the Bernstein function $\phi(\lambda) = \lambda + \kappa$, $\kappa \in [-\frac14, \infty)$, has weighted potential measure $V_\phi(ds) = e^{-\kappa s}\,ds/s$ on $(0, \infty)$; the corresponding subordinate process is Brownian motion **killed** at rate $\kappa$ (survival factor $e^{-\kappa t}$). Extended to $\kappa \in [-\frac14, 0)$ (which reaches down to the spectral bottom of $\Delta_{\mathbb H^2}$) by analytic continuation of the closed-form class mass.
> **In words:** exponential tilting of the ordinary Brownian loop measure by the survival weight $e^{-\kappa t}$: long loops are suppressed more strongly the larger $\kappa$. Corresponds to loops of the Schrödinger operator $\Delta_{\mathbb H^2} + \kappa$ (constant potential $\kappa$). The special value $\kappa = 0$ recovers plain Brownian motion.
> **Concretely:** at $\kappa = 0$ the weighted potential is $V_\phi(ds) = ds/s$ (the Brownian case) and $I_\kappa(L) = e^{-L/2}/L$. At $\kappa = 2$: $I_\kappa(L) = e^{-L\sqrt{9/4}}/L = e^{-3L/2}/L$, exponentially smaller. At the boundary $\kappa = -\frac14$: $I_\kappa(L) = e^{0}/L = 1/L$, and the corresponding $s = \frac12$. Full detail: [[Ex - The Subordinate Form of Brownian Motion with Killing]] and [[Remark - The Range of the Killing Parameter]].

> [!recall]- Selberg zeta criterion — the canonical shape
> **Formally:** the [[Lemma - Selberg Zeta Criterion|Selberg zeta criterion (Lemma 4.2)]] says: if there exist $C > 0$ and $s > \delta$, independent of $L$, such that
> $$\frac{L}{2\sinh(L/2)}\,I_\phi(L) \;=\; C \cdot \frac{e^{(1-s)L}}{e^L - 1} \qquad (L > 0),$$
> then $\sum_{\gamma, m}\mu^\phi_X(C_X(\gamma^m)) = -C\log Z_X(s)$.
> **In words:** the criterion is a **shape-matching test**; whenever the process-integral $I_\phi$ combines with the geometric prefactor $L/[2\sinh(L/2)]$ to give the canonical shape on the right, the total loop mass collapses to a value of the Selberg zeta. Verifying the shape is a one-line algebraic check per process.
> **Concretely:** the criterion is the recurring engine of §4.1: applied to the killing case (this remark; $C = 1$, $s = \frac12 + \sqrt{1/4 + \kappa}$), it gives [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]]; the pattern is repeated in the shifted $\alpha$-stable case ($C = \alpha/2$, same $s$). Full detail: [[Lemma - Selberg Zeta Criterion]].

---

# Claim / Identity

> **Claim (killing case fits the Selberg zeta criterion).** For the killed Bernstein function $\phi(\lambda) = \lambda + \kappa$ with $\kappa \ge -\frac14$, the loop-length integral $I_\kappa(L) = e^{-L\sqrt{1/4 + \kappa}}/L$ satisfies
> $$\frac{L}{2\sinh(L/2)}\,I_\kappa(L) \;=\; \frac{e^{(1-s)L}}{e^L - 1}, \qquad s = \frac12 + \sqrt{\frac14 + \kappa}, \qquad L > 0.$$
> That is, the killed process meets the hypothesis of the [[Lemma - Selberg Zeta Criterion|Selberg zeta criterion]] with **constant $C = 1$** and the spectral parameter $s = s(\kappa) = \frac12 + \sqrt{\frac14 + \kappa}$.

---

# In One Line

The one-line closed form $I_\kappa(L) = e^{-L\sqrt{1/4 + \kappa}}/L$ has exactly the algebraic shape the Selberg zeta criterion asks for — a hyperbolic-sine expansion plus one substitution of variables identifies the exponent $\sqrt{\frac14 + \kappa}$ inside $I_\kappa$ with the exponent $s - \frac12$ inside the criterion's canonical form. This shape-check is what turns [[Lemma - Selberg Zeta Criterion|Lemma 4.2]] (a general criterion) into [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]] (a concrete zeta identity for the killed Brownian loop mass).

---

# Why It's True

**Mechanism (one sentence).** *Expand $2\sinh(L/2) = e^{L/2}(1 - e^{-L})$; the $L$ in the numerator and the $L$ in the denominator of $I_\kappa(L)$ cancel; multiply numerator and denominator by $e^L$; the resulting exponent $L(\frac12 - \sqrt{\frac14 + \kappa})$ is exactly $(1 - s)L$ with $s = \frac12 + \sqrt{\frac14 + \kappa}$.*

The point of the shape-check is that **all the process-specific content sits in one exponent**. The killed loop-length integral $I_\kappa(L)$ carries a single exponential factor $e^{-L\sqrt{1/4 + \kappa}}$ with a $1/L$ prefactor; the geometric prefactor $L/[2\sinh(L/2)]$ carries an $L$ that cancels the $1/L$ and a hyperbolic sine that, once expanded, produces the $(e^L - 1)^{-1}$ denominator of the criterion's canonical form. The remaining exponent is then a straight linear combination of $L/2$ and $L\sqrt{\frac14 + \kappa}$, which the substitution $s := \frac12 + \sqrt{\frac14 + \kappa}$ rewrites as $(1 - s)L$. No new machinery — just the identity $2\sinh(x) = e^x - e^{-x}$ and one change of variables.

Once the shape is verified, the [[Lemma - Selberg Zeta Criterion|Selberg zeta criterion]] applies with $C = 1$, and the killed total mass is $-\log Z_X(s)$ — this is the content of [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]].

---

# Derivation

> [!note]- Gap-free derivation
> **Step 1 — substitute the closed form of $I_\kappa$.** By [[Def - The Loop-Length Integral|Definition 3.6]] applied to $\phi(\lambda) = \lambda + \kappa$ (whose weighted potential measure is $V_\phi(ds) = e^{-\kappa s}\,ds/s$; see the Notation recall or [[Ex - The Subordinate Form of Brownian Motion with Killing]]),
> $$I_\kappa(L) \;=\; \int_0^\infty \frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,e^{-\kappa s}\,\frac{ds}{s} \;=\; \int_0^\infty \frac{e^{-(\frac14 + \kappa)s}\,e^{-L^2/(4s)}}{2\sqrt{\pi}\,s^{3/2}}\,ds.$$
> Apply the Gaussian-type identity $\int_0^\infty s^{-3/2} e^{-as - b/s}\,ds = \sqrt{\pi/b}\,e^{-2\sqrt{ab}}$ with $a = \frac14 + \kappa$, $b = L^2/4$ (so $\sqrt{\pi/b} = 2\sqrt\pi/L$ and $2\sqrt{ab} = L\sqrt{\frac14 + \kappa}$):
> $$I_\kappa(L) \;=\; \frac{1}{2\sqrt\pi}\cdot\frac{2\sqrt\pi}{L}\,e^{-L\sqrt{1/4 + \kappa}} \;=\; \frac{e^{-L\sqrt{1/4 + \kappa}}}{L}.$$
>
> **Step 2 — assemble $\frac{L}{2\sinh(L/2)}\,I_\kappa(L)$; the $L$'s cancel.** Multiplying the closed form of $I_\kappa$ by $L/[2\sinh(L/2)]$,
> $$\frac{L}{2\sinh(L/2)}\,I_\kappa(L) \;=\; \frac{L}{2\sinh(L/2)}\cdot\frac{e^{-L\sqrt{1/4 + \kappa}}}{L} \;=\; \frac{e^{-L\sqrt{1/4 + \kappa}}}{2\sinh(L/2)}.$$
>
> **Step 3 — expand $2\sinh(L/2)$ and factor $e^{L/2}$ out of the denominator.** Using $2\sinh(L/2) = e^{L/2} - e^{-L/2} = e^{L/2}(1 - e^{-L})$,
> $$\frac{e^{-L\sqrt{1/4 + \kappa}}}{2\sinh(L/2)} \;=\; \frac{e^{-L\sqrt{1/4 + \kappa}}}{e^{L/2}(1 - e^{-L})} \;=\; \frac{e^{-L(\sqrt{1/4 + \kappa} + 1/2)}}{1 - e^{-L}}.$$
>
> **Step 4 — multiply numerator and denominator by $e^L$ to bring the denominator into the Selberg-criterion form.** Since $(1 - e^{-L})\cdot e^L = e^L - 1$,
> $$\frac{e^{-L(\sqrt{1/4 + \kappa} + 1/2)}}{1 - e^{-L}} \;=\; \frac{e^{-L(\sqrt{1/4 + \kappa} + 1/2)}\cdot e^L}{e^L - 1} \;=\; \frac{e^{L(1 - \sqrt{1/4 + \kappa} - 1/2)}}{e^L - 1} \;=\; \frac{e^{L(1/2 - \sqrt{1/4 + \kappa})}}{e^L - 1}.$$
>
> **Step 5 — set $s := \frac12 + \sqrt{\frac14 + \kappa}$ and read off $C = 1$.** With this $s$, $1 - s = \frac12 - \sqrt{\frac14 + \kappa}$, so the exponent in the numerator is precisely $(1 - s)L$:
> $$\frac{L}{2\sinh(L/2)}\,I_\kappa(L) \;=\; \frac{e^{(1-s)L}}{e^L - 1} \;=\; 1 \cdot \frac{e^{(1-s)L}}{e^L - 1}.$$
> Comparing with the [[Lemma - Selberg Zeta Criterion|Selberg zeta criterion]]'s hypothesis $\frac{L}{2\sinh(L/2)}\,I_\phi(L) = C \cdot e^{(1-s)L}/(e^L - 1)$, the killing case satisfies it with **$C = 1$** and this specific $s = s(\kappa)$. $\blacksquare$

The constant $s$-value is real for all $\kappa \ge -\frac14$: at $\kappa = -\frac14$, $s = \frac12$ (the spectral bottom of $\Delta_{\mathbb H^2}$); at $\kappa = 0$, $s = 1$ (the natural home of the un-killed Brownian case); as $\kappa \to \infty$, $s \to \infty$. The correspondence $\kappa \leftrightarrow s$ is the change of variable $s(s - 1) = \kappa$, precisely the $\kappa_-(s)$ appearing in [[Thm - Twisted Ruelle Zeta Identity|Corollary 4.6]] — same reason, same algebra.

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §4 Zeta Functions and Total Mass|§4.1.1]] as the immediate input to [[Thm - Selberg Zeta Identity for the Total Loop Mass|Corollary 4.3]] (the killed Selberg zeta identity). The same shape-check pattern, with the same $s$ but a different $C = \alpha/2$, is invoked implicitly for the shifted $\alpha$-stable process (giving the identity $\sum_{\gamma, m}\mu^\phi_X(C_X(\gamma^m)) = -(\alpha/2)\log Z_X(s)$ under the analogous hypothesis $s > \delta$). Through Corollary 4.3, this shape-check feeds the physical re-reading [[Remark - Bosonic Partition Function Interpretation|Remark 4.4]] and the finite-area divergence [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5]] renormalises.
