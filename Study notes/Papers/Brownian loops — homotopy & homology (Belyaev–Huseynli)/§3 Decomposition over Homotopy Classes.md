---
type: paper-section
paper: "BH26"
subject: brownian-loops
section: "3, 3.1, 3.4"
prereqs:
  - "Def - Fuchsian Group and the Quotient Surface"
  - "Def - Deck Transformations and the Lift of a Rooted Loop"
  - "Def - Free Homotopy Class and Conjugacy Class Correspondence"
  - "Constr - The Periodised Kernel"
  - "Constr - Standard-Form Representative and the Fundamental Strip"
  - "Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces"
  - "Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces"
tags: [paper, probability, hyperbolic-geometry, loop-measures]
---

# Notation

**Standing setting for this section.** $\Gamma\subset\mathrm{PSL}(2,\mathbb{R})$ is a torsion-free [[Def - Fuchsian Group and the Quotient Surface|Fuchsian group]] acting freely and properly discontinuously on $\mathbb{H}^2$, and $X=\Gamma\backslash\mathbb{H}^2$ is the resulting [[Def - Geometrically Finite Surfaces, Cusps and Funnels|geometrically finite]] hyperbolic surface. $(\mathcal{E},\mathcal{F})$ is a $\Gamma$-invariant regular symmetric Dirichlet form on $L^2(\mathbb{H}^2,\rho)$ whose semigroup has a jointly measurable kernel satisfying $p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,w)=p^{\mathcal{E}}_{\mathbb{H}^2}(t,hz,hw)$ for every $h\in\Gamma$. Unless stated otherwise, **all free homotopy classes are non-trivial and non-peripheral**: their loops are neither null-homotopic nor freely homotopic into a cusp or onto a boundary component.

- $\pi : \mathbb{H}^2\to X$ — the covering projection; $\Gamma$ is its deck group
- $\rho_{\mathbb{H}^2}$, $\rho_X$ — hyperbolic area measure upstairs and its descent downstairs
- $p^{\mathcal{E}}_{\mathbb{H}^2}$, $p^{\mathcal{E}}_X$ — the kernel upstairs and its [[Constr - The Periodised Kernel|periodisation]] downstairs
- $\tilde z, \tilde w$ — arbitrary lifts of $z,w\in X$; the periodisation does not depend on which
- $h_\omega\in\Gamma$ — the deck transformation recorded by a rooted loop $\omega$, defined by $\tilde\omega(t)=h_\omega\tilde x$
- $\mathcal{P}_X$ — the set of primitive oriented closed geodesics on $X$; $\ell_\gamma$ the translation length of $\gamma\in\mathcal{P}_X$
- $\tau\in\Gamma$ — a [[Constr - Standard-Form Representative and the Fundamental Strip|standard-form representative]] $\tau : z\mapsto e^{\ell_\gamma}z$, a hyperbolic isometry with axis the imaginary half-line
- $F_\tau=\{z\in\mathbb{H}^2 : 1\leq\operatorname{Im}(z)<e^{\ell_\gamma}\}$ — the fundamental strip, a fundamental region for $\langle\tau\rangle$
- $F\subset\mathbb{H}^2$ — a fundamental region for the whole of $\Gamma$
- $[\tau^m]_{\mathrm{conj}}=\{h\tau^m h^{-1} : h\in\Gamma\}$ — the conjugacy class of the $m$-th power
- $C_\Gamma(\tau^m)=\langle\tau\rangle$ — the centraliser; $\Gamma/\langle\tau\rangle$ its left cosets
- $\mathcal{C}_X(\gamma^m)$ — the free homotopy class of oriented closed curves winding $m$ times around $\gamma$
- $L := m\ell_\gamma$ — used throughout §3.1 onwards; note $\ell_\gamma/L = 1/m$
- $I_\phi(L)$ — the [[Constr - The Weighted Heat-Kernel Integral Iϕ|weighted heat-kernel integral]] of Definition 3.6
- $P\subset X$ — a closed discrete (hence countable, hence [[Def - Polar Set|polar]]) set, §3.4 only

---

# What this section is for

This is the heart of the paper. Everything before it builds a measure on loops; everything after it is analysis of the answer this section computes. The question is: **given a free homotopy class, what is its mass?**

The reason this is answerable at all is that a hyperbolic surface hands you a dictionary between topology and group theory, and the loop measure is built from a kernel that respects it. The dictionary is the covering-space picture. $\mathbb{H}^2$ is the universal cover of $X$ with deck group $\Gamma$; a loop $\omega$ rooted at $x$ lifts uniquely once you pick $\tilde x$ in the fibre, and the lift ends at $h_\omega\tilde x$ for a unique $h_\omega\in\Gamma$. That element is the topological content of the loop: it is the identity exactly when the loop is contractible. Forgetting the basepoint — which the loop measure has already done — replaces $h_\omega$ by its conjugacy class, because moving the start from $\tilde x$ to $q\tilde x$ translates the whole lifted arc and changes the recorded element to $qh_\omega q^{-1}$. Hence: **free homotopy classes of oriented closed curves on $X$ correspond bijectively to conjugacy classes in $\Gamma$**, and every non-trivial non-peripheral class contains a unique closed geodesic representative $m\gamma$ of length $m\ell_\gamma$.

On the analytic side the same group acts. The kernel downstairs is the [[Constr - The Periodised Kernel|periodisation]] $p^{\mathcal{E}}_X(t,z,w)=\sum_{h\in\Gamma}p^{\mathcal{E}}_{\mathbb{H}^2}(t,\tilde z,h\tilde w)$ — a sum indexed by $\Gamma$. So the heat kernel on $X$ arrives already decomposed by deck transformation, and restricting the sum to a conjugacy class *is* restricting the loop measure to a free homotopy class. That coincidence is the whole mechanism.

What remains is a computation, and it has exactly two steps, both of which are worth internalising because they recur verbatim in §7. **Step one: unfold.** The integral over a fundamental region $F$ for $\Gamma$, with the integrand summed over the conjugacy class, is turned into an integral over a fundamental region for the *cyclic* group $\langle\tau\rangle$ with the integrand a single term $p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,\tau^m z)$. This works because the conjugacy class is enumerated without repetition by the left cosets $\Gamma/\langle\tau\rangle$ ([[Def - Centraliser and Coset Enumeration of a Conjugacy Class|the centraliser of τᵐ is exactly ⟨τ⟩]]), and translating $F$ by each coset representative reassembles a fundamental region for $\langle\tau\rangle$. **Step two: choose a convenient fundamental region.** Since the integrand is $\langle\tau\rangle$-invariant, any fundamental region gives the same answer, so replace the awkward union $\bigsqcup_r r^{-1}F$ by the horizontal band $F_\tau$. That band is where an explicit computation becomes possible.

The rest of §3 is that computation carried out. Lemma 3.4, borrowed from Wang–Xue, evaluates the spatial integral against the hyperbolic Brownian kernel; Lemma 2.11 eats the time integral; and what comes out is Theorem 3.5, the formula the whole paper is organised around.

§3.4 is a coda, and its content is largely negative. The two structural properties of §2.1 — restriction and conformal invariance — combine, for pure Brownian motion, into a genuine identity between the length spectra of two *different* hyperbolic surfaces. For any nonlinear subordination the identity degenerates to a triviality, and the reason is worth stating precisely: a conformal change rescales the Laplacian, $\Delta_{X,g'}=e^{-2\sigma}\Delta_{X,g}$, and $\phi$ does not commute with that rescaling unless $\phi(\lambda)=c\lambda$. Subordination and conformal geometry are simply incompatible except in the linear case.

---

# The lifting picture

Before any result, the dictionary itself. Three pages carry it, and they should be read in this order.

[[Def - Deck Transformations and the Lift of a Rooted Loop]] — the covering projection $\pi$, the unique lift of a rooted loop, and the element $h_\omega\in\Gamma$ it records. This is where the identification $\pi_1(X,x)\cong\Gamma$ (after a choice of $\tilde x$) is set up.

[[Def - Free Homotopy Class and Conjugacy Class Correspondence]] — why forgetting the basepoint replaces $h_\omega$ by its conjugacy class, and what "non-trivial" and "non-peripheral" exclude. The unique closed geodesic representative in each class lives here.

[[Def - Centraliser and Coset Enumeration of a Conjugacy Class]] — the identity
$$[\tau^m]_{\mathrm{conj}} = \bigsqcup_{r\in\Gamma/\langle\tau\rangle}\{r\tau^m r^{-1}\},$$
one distinct conjugate per coset, resting on $C_\Gamma(\tau^m)=\langle\tau\rangle$. This is the combinatorial fact that makes the unfolding step of Theorem 3.2 legal, and it is the *only* place torsion-freeness of $\Gamma$ is genuinely used.

Alongside them, two constructions that appear later as hypotheses: [[Constr - The Periodised Kernel]] and [[Constr - Standard-Form Representative and the Fundamental Strip]].

## Remark 3.1 — what happens when the process jumps

> [!abstract] Type card — Remark 3.1 (jump-process convention)
> **Given.** A pure-jump subordinate process — say $\phi(\lambda)=\lambda^{\alpha/2}$, $\alpha\in(0,2)$ — whose sample loops are càdlàg maps into $X$ and therefore have **no** free homotopy class and **no** canonical lift.
>
> **Produces.** A *definition* (13): $\mu^{\mathcal{E}}_X(\mathcal{C}_X(\gamma^m)) := \int_0^\infty\frac{\mathrm{d}t}{t}\int_X\sum_{h\in[\tau^m]_{\mathrm{conj}}}p^{\mathcal{E}}_{\mathbb{H}^2}(t,\tilde z,h\tilde z)\,\mathrm{d}\rho_X(z)$, the part of the loop measure obtained by restricting the periodisation to the conjugacy class.
>
> **Lets you.** State Theorems 3.5 and 7.2 uniformly across diffusions and jump processes — at the explicit price that in the jump case the left-hand side is a definition, not a measured quantity.

This is one of the honest parts of the paper and deserves to be read rather than skimmed. There *is* a path-space interpretation, but it lives on a bigger space. Write the subordinate process as $Y_u = B_{S_u}$ on a space carrying the pair $(B,S)$ rather than the time-changed path alone. Conditional on $S_t=s$, the term indexed by $h$ corresponds upstairs to a Brownian bridge from some $\tilde w$ to $h\tilde w$, and the projection of the full Brownian arc $B|_{[0,s]}$ is a genuine continuous loop with monodromy $h$; the conjugacy class $[h]_{\mathrm{conj}}$ does not depend on the lift. The subordinator's only job is to decide which portions of that arc are observed, and at a jump time $u$ the segment $B|_{[S_{u^-},S_u]}$ is deleted — but its endpoints, and hence the accumulated deck transformation, are unchanged. So restricting the periodisation to $[\tau^m]_{\mathrm{conj}}$ selects exactly the marked loops whose underlying Brownian arc lies in $\mathcal{C}_X(\gamma^m)$.

What genuinely fails is recovery from the càdlàg path alone: the deleted segments can be filled by continuous paths whose projections have different monodromies, so the class is not a function of $Y$. The paper's open question — whether some canonical continuous interpolation of the jumps could geometrise a càdlàg loop, and whether any such scheme must break the closed-form mass formulas — is recorded on [[Constr - Loop Mass in a Homotopy Class for Jump Processes]] and on the map page.

---

# Results

## Theorem 3.2 — the general decomposition

> [!abstract] Type card — Theorem 3.2 (general homotopy class decomposition)
> **Given.** A $\Gamma$-invariant regular symmetric Dirichlet form whose kernel [[Constr - The Periodised Kernel|periodises]]; a primitive closed geodesic $\gamma\in\mathcal{P}_X$ with [[Constr - Standard-Form Representative and the Fundamental Strip|standard-form representative]] $\tau : z\mapsto e^{\ell_\gamma}z$; a winding number $m\geq 1$. For jump processes, the left side is read via [[Constr - Loop Mass in a Homotopy Class for Jump Processes|Remark 3.1]].
>
> **Produces.** The identity, an equality of numbers in $[0,\infty]$:
> $$\mu^{\mathcal{E}}_X\big(\mathcal{C}_X(\gamma^m)\big) = \int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau} p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,\tau^m z)\,\mathrm{d}\rho_{\mathbb{H}^2}(z).$$
>
> **Lets you.** Compute a homotopy-class mass entirely upstairs on $\mathbb{H}^2$, against a *single* group element $\tau^m$, over an *explicit* region. Both the sum over $\Gamma$ and the quotient geometry of $X$ have been eliminated; what is left is a two-variable integral that an explicit heat kernel can discharge.

**Strategy.** Unfold the conjugacy-class sum over the left cosets of the cyclic centraliser $\langle\tau\rangle$, using $\Gamma$-invariance of the kernel to move each coset representative onto the integration region; then replace the reassembled fundamental region for $\langle\tau\rangle$ by the strip $F_\tau$, which is legal because the integrand $z\mapsto p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,\tau^m z)$ is $\langle\tau\rangle$-invariant.

Full proof: [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]]. **This is one of the three proofs in the paper worth reading in full**, because it is the only genuinely structural argument here and because §7 reuses it verbatim with $\mathbb{H}^3$ in place of $\mathbb{H}^2$.

## Lemma 3.4 — the Wang–Xue strip identity

> [!abstract] Type card — Lemma 3.4 (Wang–Xue)
> **Given.** $s>0$, $m\geq 1$, the hyperbolic Brownian heat kernel $p_{\mathbb{H}^2}$, and $\tau$ in standard form so that $\tau^m z = e^{L}z$ with $L=m\ell_\gamma$.
>
> **Produces.** The closed form, a positive real number:
> $$\int_{F_\tau} p_{\mathbb{H}^2}(s,z,e^{L}z)\,\mathrm{d}\rho_{\mathbb{H}^2}(z) = \frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}.$$
>
> **Lets you.** Discharge the spatial integral of Theorem 3.2 completely, leaving a one-dimensional integral in the time variable — which is exactly the shape Lemma 2.11 consumes.

The factorisation is the thing to notice: a purely **geometric** prefactor $\ell_\gamma/2\sinh(L/2)$, depending only on the geodesic, multiplied by a purely **analytic** factor depending only on $(s,L)$. That split is what makes the paper's architecture possible, because the analytic factor is the only thing $V_\phi$ ever touches.

Statement and discussion: [[Thm - The Wang–Xue Fundamental-Strip Identity]]. The paper cites this to Wang–Xue rather than proving it.

## Theorem 3.5 — the central formula

> [!abstract] Type card — Theorem 3.5 (mass of the subordinate Brownian loop measure)
> **Given.** A [[Def - Bernstein Function and the Lévy–Khintchine Representation|Bernstein function]] $\phi$ satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]]; a [[Def - Primitive Hyperbolic Element and Translation Length|primitive closed geodesic]] $\gamma\in\mathcal{P}_X$ of length $\ell_\gamma$; a winding number $m\geq 1$. Write $L=m\ell_\gamma$.
>
> **Produces.** A closed-form value for $\mu^\phi_X(\mathcal{C}_X(\gamma^m))$, a non-negative number, as a single integral of an explicit heat-kernel factor against the [[Constr - The Weighted Potential Measure Vϕ|weighted potential measure]]:
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(\mathrm{d}s).$$
>
> **Lets you.** Replace the double $(t,s)$ integral by one integral against $V_\phi$, which is what makes every later special case — Brownian, killing, $\alpha$-stable, shifted $\alpha$-stable — a one-line substitution.

**Strategy.** Evaluate the spatial integral by the Wang–Xue identity (Lemma 3.4), then collapse the $\mathrm{d}t/t$ integral into $V_\phi$ by Lemma 2.11.

Full proof: [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]].

## Definition 3.6 — isolating the analytic factor

Since the geometric prefactor never interacts with $\phi$, name what does:
$$I_\phi(L) := \int_0^\infty\frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt{\pi s}}\,V_\phi(\mathrm{d}s),\qquad L>0,$$
so that Theorem 3.5 reads $\mu^\phi_X(\mathcal{C}_X(\gamma^m)) = \frac{\ell_\gamma}{2\sinh(L/2)}I_\phi(L)$ with $L=m\ell_\gamma$. See [[Constr - The Weighted Heat-Kernel Integral Iϕ]]. The point of the naming is §4: [[Thm - Selberg Zeta Criterion|Lemma 4.2]] states a criterion for a zeta identity purely as a functional equation for $I_\phi$, with no geometry in it at all.

---

# Worked special cases

Four substitutions into Theorem 3.5. All four use one integral identity,
$$\int_0^\infty s^{-3/2}e^{-as-b/s}\,\mathrm{d}s = \sqrt{\tfrac{\pi}{b}}\,e^{-2\sqrt{ab}},$$
with $a$ shifted by the killing rate and $b = L^2/4$ throughout. It is worth having this identity in muscle memory; it is the only analysis in §3.1.

**Brownian ($\phi(\lambda)=\lambda$, so $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$).**
$$\mu_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac1m\cdot\frac{1}{e^{L}-1}.$$

> [!note]- Calculation (skippable)
> With $V_\phi(\mathrm{d}s)=\mathrm{d}s/s$, $I_{\mathrm{BM}}(L)=\int_0^\infty \frac{e^{-s/4}e^{-L^2/(4s)}}{2\sqrt\pi s^{3/2}}\,\mathrm{d}s$. Apply the identity with $a=1/4$, $b=L^2/4$: the integral equals $\sqrt{\pi/b}\,e^{-2\sqrt{ab}} = \frac{2\sqrt\pi}{L}e^{-L/2}$, so $I_{\mathrm{BM}}(L)=\frac{1}{2\sqrt\pi}\cdot\frac{2\sqrt\pi}{L}e^{-L/2}=\frac{e^{-L/2}}{L}$. Hence
> $$\mu_X(\mathcal{C}_X(\gamma^m)) = \frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-L/2}}{L} = \frac{\ell_\gamma}{L}\cdot\frac{e^{-L/2}}{2\sinh(L/2)} = \frac1m\cdot\frac{1}{e^L-1},$$
> using $\ell_\gamma/L=1/m$ and $e^{-L/2}/(2\sinh(L/2)) = 1/(e^L-1)$. This recovers Wang–Xue [WX25, Lemma 3.2].

**Brownian with killing ($\phi(\lambda)=\lambda+\kappa$, $V_\phi(\mathrm{d}s)=e^{-\kappa s}\,\mathrm{d}s/s$).**
$$I_\kappa(L) = \frac{e^{-L\sqrt{1/4+\kappa}}}{L},\qquad \mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac1m\cdot\frac{e^{(\frac12-\sqrt{\frac14+\kappa})L}}{e^L-1}.$$
The same identity with $a=\tfrac14+\kappa$. Setting $\kappa=0$ recovers the Brownian formula; this is Lemonde–Wang [LW26, Lemma 3.1]. **This formula is the one every later section actually uses** — §4, §5 and §6 all run on it rather than on Theorem 3.5 in general.

> [!note] Remark 3.7 — the range $\kappa \geq -\tfrac14$
> For $\kappa>0$, $\mu^\kappa_X$ is the loop measure of Brownian motion with a constant killing rate, whose generator is a Schrödinger operator with constant potential $+\kappa$ rather than the Laplacian. For $\kappa\in[-\tfrac14,0)$ the function $\phi(\lambda)=\lambda+\kappa$ is **no longer Bernstein** — its killing rate is negative — but the formula continues to make sense analytically, and the integral converges throughout. The boundary $\kappa=-\tfrac14$ is exactly where $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ stops being real; at $\kappa=-\tfrac14$ it gives $s=\tfrac12$, the bottom of the $L^2$-spectrum of $\Delta_{\mathbb{H}^2}$. So the extended range is not a technical convenience — it is the whole real-$s$ range, cut off precisely by the spectrum.

**$\alpha$-stable ($\phi(\lambda)=\lambda^{\alpha/2}$, $V_\phi(\mathrm{d}s)=\tfrac\alpha2\,\mathrm{d}s/s$).** Since $V_\phi$ is a constant multiple of the Brownian one, $I_\alpha(L)=\tfrac\alpha2 I_{\mathrm{BM}}(L)$ and
$$\mu^\alpha_X\big(\mathcal{C}_X(\gamma^m)\big) = \tfrac{\alpha}{2}\,\mu_X\big(\mathcal{C}_X(\gamma^m)\big).$$
**This collapse is the section's one negative result and it is structural, not accidental.** Self-similar subordinators are exactly the stable ones; the weight $\mathrm{d}t/t$ is itself scale-invariant; combining the two scalings in Definition 2.9 forces $V_\phi$ to be a constant multiple of $\mathrm{d}s/s$. So a scale-invariant subordination can never tell you anything about the geometry of $X$ that Brownian motion did not already tell you. To get a decomposition that differs *in form*, scale invariance must be broken.

**Shifted $\alpha$-stable ($\phi(\lambda)=(\lambda+\kappa)^{\alpha/2}$, $V_\phi(\mathrm{d}s)=\tfrac\alpha2 e^{-\kappa s}\,\mathrm{d}s/s$).** The paper's own repair. Combining the previous two computations,
$$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac{\alpha}{2}\cdot\frac1m\cdot\frac{e^{(\frac12-\sqrt{\frac14+\kappa})L}}{e^L-1}.$$
Note what this does and does not achieve: the shift breaks the scaling, but the resulting formula is the *killing* formula times $\alpha/2$. So the shifted stable case is a new process with an old mass profile, and the question of whether any subordination produces a genuinely different functional dependence on $L$ remains open.

---

# §3.4 Length-spectrum identities

The two structural properties of the Brownian loop measure, cashed in.

**What survives for a killing rate.** A Borel set $P\subset X$ is [[Def - Polar Set|polar]] if the process almost surely never hits it at a positive time; on a Riemann surface this holds for Brownian motion exactly when $P$ has zero logarithmic capacity in every chart, so every singleton is polar, polar sets form a $\sigma$-ideal, and every countable set is polar. A killing rate does not change the paths, so for $\phi(\lambda)=\lambda+\kappa$ the polar sets are Brownian ones. Taking $P$ closed and discrete, restriction gives
$$\mu^\kappa_{X,g}\big(\mathcal{C}_X(\gamma^m)\big) = \mu^\kappa_{X\setminus P, g}\big(\mathcal{C}_X(\gamma^m)\big),$$
with $g$ on the right meaning the *ambient* metric restricted to $X\setminus P$. This is genuine but weak: puncturing does not change the mass so long as the metric is unchanged.

**What is lost.** For Brownian motion, conformal invariance lets you swap the restricted metric for the unique complete hyperbolic metric $g'$ of $X\setminus P$ — a genuinely different metric, with a cusp at each puncture — and the identity becomes a comparison of *geodesic length spectra of two different surfaces*. For any subordinate process this fails, and the obstruction is exact: in two dimensions a conformal change $g'=e^{2\sigma}g$ rescales the Laplacian as $\Delta_{X,g'}=e^{-2\sigma}\Delta_{X,g}$, and $\phi(e^{-2\sigma}\Delta_{X,g})\neq e^{-2\sigma}\phi(\Delta_{X,g})$ unless $\phi(\lambda)=c\lambda$. Conformal covariance is a *linear* phenomenon and nonlinear subordination destroys it.

> [!abstract] Type card — Theorem 3.9 (Wang–Xue, length-spectrum identity)
> **Given.** A complete hyperbolic surface $X$ without boundary — possibly of infinite type, possibly with cusps or funnels — a non-empty closed [[Def - Polar Set|polar]] set $P\subset X$, and $X'=X\setminus P$ equipped with its own complete hyperbolic metric.
>
> **Produces.** For every $\gamma\in\mathcal{P}_X$ and $m\geq1$, the identity between length spectra
> $$\frac1m\cdot\frac{1}{e^{m\ell_\gamma}-1} = \sum_{\substack{\gamma'\in\mathcal{P}_{X'},\,m'\geq1\\ \gamma'^{m'}\simeq_X\gamma^m}}\frac{1}{m'}\cdot\frac{1}{e^{m'\ell_{\gamma'}}-1},$$
> where $\simeq_X$ is free homotopy as curves in $X$ and the two lengths are measured in the respective hyperbolic metrics.
>
> **Lets you.** Trade conformal invariance of $\mu_X$ for an exact relation between the length spectra of a surface and its puncturing — and, read the other way, see precisely which structural property each side of the identity is paying for.

Discussion and the exact failure mode for subordinate processes: [[Thm - Length-Spectrum Identity under Puncturing]].

**Recovering the marked length spectrum.** The [[Def - Marked Length Spectrum|marked length spectrum]] assigns to each non-trivial free homotopy class the infimum of the lengths of loops in it, which on a hyperbolic surface is attained by the unique closed geodesic, so $\mathrm{MLS}(\mathcal{C}_X(\gamma^m))=m\ell_\gamma$. The marking — the record of *which class* realises which length — matters, because Vignéras produced non-isometric hyperbolic surfaces whose geodesic lengths agree as a set.

> [!abstract] Type card — Proposition 3.11 and Corollary 3.12
> **Given.** The masses $\mu^\kappa_X(\mathcal{C}_X(\gamma^m))$ for $\kappa\geq-\tfrac14$, over all free homotopy classes; for Corollary 3.12, two hyperbolic metrics $g_1,g_2$ on a closed surface $X$ with equal masses in every class.
>
> **Produces.** For $\kappa=0$, the explicit inversion $\ell_\gamma = \log\!\big(1+1/\mu_X(\mathcal{C}_X(\gamma))\big)$; for general $\kappa$, strict monotonicity of the mass in $\ell_\gamma$, hence injectivity. For Corollary 3.12: an isometry between $g_1$ and $g_2$ isotopic to the identity, so the two metrics define the same point of Teichmüller space.
>
> **Lets you.** Read the loop masses as a complete invariant of the marked hyperbolic structure — the masses lose no geometric information at all.

**Strategy (3.11).** Invert the Brownian formula directly; in the killing case compute the logarithmic derivative of the mass in $\ell_\gamma$ and observe it is bounded above by $\tfrac12 - 1 < 0$. **Strategy (3.12).** Proposition 3.11 gives equality of marked length spectra with the identity marking; then quote Otal and Croke, who proved that a negatively curved metric on a closed surface is determined up to isometry by its marked length spectrum (the two-dimensional case of the Burns–Katok conjecture).

Pages: [[Thm - Loop Masses Determine the Marked Length Spectrum]], [[Thm - Loop Masses Determine the Hyperbolic Surface]].

---

# What to carry forward

**The mass formula in the killing case.** $\mu^\kappa_X(\mathcal{C}_X(\gamma^m)) = \frac1m\frac{e^{(1-s)L}}{e^L-1}$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ and $L=m\ell_\gamma$. Every result in §4, §5 and §6 is an operation on this expression. If you remember one formula from the paper, this is it.

**The general form $\frac{C}{m}\frac{e^{(1-s)L}}{e^L-1}$.** [[Thm - Selberg Zeta Criterion|Lemma 4.2]] is precisely the statement that any $\phi$ whose mass has this shape yields a Selberg zeta identity, with $C$ the constant of proportionality. Brownian and killing give $C=1$; the two stable cases give $C=\alpha/2$.

**The unfolding move.** Conjugacy-class sum $\to$ cosets of the cyclic centraliser $\to$ change of fundamental region. It is used once in §3 and once in §7 and it is the only structural argument in the paper.

**That homotopy classes are not measurable for jump processes**, so that all the $\alpha$-stable statements are statements about a defined quantity on a marked space.

**That $\alpha$-stable subordination adds nothing geometric**, for a reason (scale invariance) rather than by accident.

Next, in any order: [[§4 Zeta Identities and Finiteness of the Total Mass]] (the analytic payoff), [[§3.3 The Loop Soup and its Poissonian Structure]] (needed before §6.2), [[§3.2 Euclidean Quantum Mechanics and the Path Integral]] (skippable digression), [[§7 Brownian Loops on Hyperbolic 3-Manifolds]] (the same argument one dimension up).
