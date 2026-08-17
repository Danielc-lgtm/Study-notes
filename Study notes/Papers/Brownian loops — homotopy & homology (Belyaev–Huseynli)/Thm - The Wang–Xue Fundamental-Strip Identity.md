---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - Standard-Form Representative and the Fundamental Strip"
tags: [paper, hyperbolic-geometry, heat-kernels]
---

# Notation

- $p_{\mathbb{H}^2}(s,z,w)$ — the Brownian heat kernel on $\mathbb{H}^2$ at speed $2$, that is the kernel of $e^{-s\Delta_{\mathbb{H}^2}}$ against the hyperbolic area measure $\rho_{\mathbb{H}^2}$
- $\tau : z\mapsto e^{\ell_\gamma}z$ — the [[Constr - Standard-Form Representative and the Fundamental Strip|standard-form representative]]; $\tau^m z = e^{L}z$ with $L=m\ell_\gamma$
- $F_\tau=\{z\in\mathbb{H}^2 : 1\leq\operatorname{Im}(z)<e^{\ell_\gamma}\}$ — the fundamental strip
- $s>0$ — the time variable; note it is the **subordination** variable in the applications, not the loop duration
- $L=m\ell_\gamma>0$ — the length of the geodesic representative of the class

---

# Type card

> [!abstract] Type card — Lemma 3.4 (Wang–Xue)
> **Given.** $s>0$, $m\geq1$, the Brownian heat kernel on $\mathbb{H}^2$, and $\tau$ in [[Constr - Standard-Form Representative and the Fundamental Strip|standard form]] so that $\tau^m z=e^{L}z$ with $L=m\ell_\gamma$.
>
> **Produces.** A closed form for the spatial integral over the fundamental strip — a positive real number, factorising as a purely geometric prefactor times a purely analytic factor in $(s,L)$.
>
> **Lets you.** Discharge the spatial integral of [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]] completely, leaving a one-dimensional integral in the time variable — which is exactly the shape [[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11]] consumes.

---

# Statement

> **Lemma 3.4 (Wang–Xue).** For any $s>0$ and $m\geq1$,
> $$\int_{F_\tau}p_{\mathbb{H}^2}\big(s,z,e^{L}z\big)\,\mathrm{d}\rho_{\mathbb{H}^2}(z) \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}},\qquad L=m\ell_\gamma.\tag{20}$$

The paper quotes this from Wang–Xue rather than proving it.

---

# Why it is true

The shape of the answer is more informative than the derivation, and it is worth reading off each factor.

**The factorisation.** The right-hand side splits as
$$\underbrace{\frac{\ell_\gamma}{2\sinh(L/2)}}_{\text{geometric}}\times\underbrace{\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}}_{\text{analytic}},$$
and the split is the architectural fact of the paper. The geometric factor depends on the geodesic and the winding number and knows nothing about the process. The analytic factor depends on $(s,L)$ and is what the [[Constr - The Weighted Potential Measure Vϕ|weighted potential measure]] will be integrated against. **Change the process and only the analytic factor's integral changes; the prefactor is inert.** That is why every special case in §3.1 is a one-line substitution.

**Reading the analytic factor.** It is a one-dimensional Gaussian heat kernel in the displacement, times $e^{-s/4}$. The $e^{-L^2/(4s)}$ is the familiar "a Brownian path must travel distance $L$ in time $s$" cost — the loops in the class $\mathcal{C}_X(\gamma^m)$ must wrap around the geodesic, and their lifts must cover hyperbolic distance at least $L$. The $2\sqrt{\pi s}$ in the denominator is the one-dimensional normalisation: after integrating out the two transverse directions of the strip, one dimension is left, the direction along the axis. And the $e^{-s/4}$ is the signature of hyperbolic geometry — it is the bottom of the $L^2$-spectrum of $\Delta_{\mathbb{H}^2}$, which is $\tfrac14$, appearing as an exponential decay in time. **The number $\tfrac14$ that shows up throughout the paper, in $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ and in the range $\kappa\geq-\tfrac14$, enters here.**

**Reading the geometric factor.** $\ell_\gamma/2\sinh(L/2)$: the $\ell_\gamma$ is the "height" of the strip in the $\log\operatorname{Im}$ coordinate, which is what the integral along the axis direction contributes. The $2\sinh(L/2)=e^{L/2}-e^{-L/2}$ is the transverse volume factor — how much room there is around the axis at displacement $L$ — and it is what will combine with the Gaussian to produce $1/(e^L-1)$ in the Brownian case, via $e^{-L/2}/2\sinh(L/2)=1/(e^L-1)$.

**The mechanism in one line: integrating the hyperbolic heat kernel over a band around a translation axis reduces to a one-dimensional Gaussian in the displacement, with the hyperbolic geometry contributing exactly two things — the spectral shift $e^{-s/4}$ and the transverse factor $1/2\sinh(L/2)$.**

---

# Strategy

**Strategy.** Parametrise the strip so that the displacement $d(z,e^Lz)$ becomes the natural variable; the change of variables makes the transverse factor of the hyperbolic volume element cancel against the $1/\sinh$ in the hyperbolic heat kernel, leaving an elementary Gaussian integral, with the strip's height $\ell_\gamma$ coming out as a multiplicative constant.

> [!note]- Proof (skippable)
> The paper cites this identity to Wang–Xue [WX25] and does not reproduce the derivation. **The three-dimensional analogue, [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity|equations (88)–(89)]], is derived in full in §7 precisely because no such citation is available there — and its derivation is the honest model for what this proof looks like.** Reading it is the efficient way to see why (20) holds: same strategy, same cancellation of the $1/\sinh$ factor against the Jacobian of the change of variables, same reduction to $\int s^{-3/2}e^{-as-b/s}\,\mathrm{d}s$, with the dimension-dependent powers adjusted.
>
> The structural points that transfer: (i) in standard form the displacement $u=d(z,\tau^m z)$ depends on $z$ only through its distance from the axis, so one transverse direction integrates out trivially; (ii) the height coordinate $\log\operatorname{Im}(z)$ runs over an interval of length exactly $\ell_\gamma$, producing the prefactor; (iii) the substitution from the transverse coordinate to $u$ produces a Jacobian containing $\sinh u$, cancelling the $1/\sinh u$ carried by the hyperbolic heat kernel; and (iv) after the cancellation the remaining integral is Gaussian in $u$ over $[L,\infty)$.

---

# What this assumes, and where to climb

**The standard form.** [[Constr - Standard-Form Representative and the Fundamental Strip]]. The identity is stated for $\tau^m z=e^Lz$ literally, so it presupposes the $\mathrm{PSL}(2,\mathbb{R})$-conjugation that puts the axis on the imaginary half-line. Without it there is no explicit $F_\tau$ and no explicit displacement function.

**Brownian motion specifically, at speed 2.** Unlike [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]], which holds for any $\Gamma$-invariant Dirichlet form, this lemma is about the *Brownian* kernel on $\mathbb{H}^2$ and its explicit form. This is why §3.1 has to specialise from the Dirichlet-form generality of §3 down to subordinate **Brownian** motion: the subordination formula (6) writes $p^\phi_{\mathbb{H}^2}$ as an average of $p_{\mathbb{H}^2}(s,\cdot,\cdot)$, and it is the *inner* Brownian kernel that this lemma evaluates. A Dirichlet form not obtained by subordinating Brownian motion would leave the spatial integral undischargeable.

**The speed-2 convention matters numerically.** At speed $1$ the factor would be $e^{-s/8}$ and the Gaussian $e^{-L^2/(2s)}$; the paper's $e^{-s/4}$ and $e^{-L^2/(4s)}$ are the speed-2 normalisation, consistent with generating the process by $-\Delta_X$ rather than $-\tfrac12\Delta_X$. Comparing against another source without checking this convention is the easiest way to get every constant in §3.1 wrong.

---

# What consumes this

- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] — the sole consumer, and the only place it is used. It discharges the inner spatial integral of (19), after which Lemma 2.11 does the rest
- [[Constr - The Weighted Heat-Kernel Integral Iϕ|Definition 3.6]] — $I_\phi(L)$ is precisely the integral of this lemma's analytic factor against $V_\phi$
- [[§3 Decomposition over Homotopy Classes]] — the worked special cases §3.1.1–3.1.4 all run on the analytic factor produced here

---

# Reading it against the rest of the paper

Wang–Xue's paper, *The Brownian loop measure on Riemann surfaces and applications to length spectra*, is the immediate predecessor of this one: it establishes the Brownian case on surfaces, from which the formula $\mu_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac{1}{e^L-1}$ and the [[Thm - Length-Spectrum Identity under Puncturing|length-spectrum identity]] both come. The present paper's contributions relative to it are the subordination framework — this lemma plus $V_\phi$ generates all four cases — and the extension to three dimensions.

The mirror-image situation in §7 is instructive about how much this lemma is doing. There, the corresponding identity has to be derived from scratch, and it takes about a page. Here, one citation. The asymmetry is the reason §7 reads as a short section despite covering the same ground as §3.
