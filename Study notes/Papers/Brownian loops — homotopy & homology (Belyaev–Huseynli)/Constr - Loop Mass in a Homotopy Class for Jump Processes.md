---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Periodised Kernel"
  - "Def - Free Homotopy Class and Conjugacy Class Correspondence"
  - "Def - Subordinator"
tags: [paper, probability, topology, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $\phi$ | Bernstein with $\nu\neq0$; running example $\phi(\lambda)=\lambda^{\alpha/2}$, $\alpha\in(0,2)$ |
| $B$ | the base Brownian motion on $\mathbb{H}^2$ / $X$; continuous paths |
| $S$ | the subordinator, $\perp B$; $Y_u=B_{S_u}$ the subordinate process, càdlàg |
| $(B,S)$ | the **marked pair**; the marked loop space, on which monodromy is measurable |
| $[\tau^m]_{\mathrm{conj}}$ | the conjugacy class; $p^{\mathcal{E}}_{\mathbb{H}^2}$ the upstairs kernel; $\rho_X$ the area on $X$ |
| $B\vert_{[S_{u^-},S_u]}$ | the Brownian segment deleted at a jump time $u$ |

---

# Construction

> **The obstruction.** For $\nu\neq0$ the sample loops of $Y$ are càdlàg. By [[Def - Deck Transformations and the Lift of a Rooted Loop|(F3)]], unique path lifting requires continuity, so a càdlàg loop:
> - admits **no** canonical lift;
> - records **no** deck transformation $h_\omega$;
> - lies in **no** free homotopy class.
>
> Hence $\mathcal{C}_X(\gamma^m)$ is **not** a measurable subset of $\mathcal{C}_X$, and $\mu^{\mathcal{E}}_X(\mathcal{C}_X(\gamma^m))$ has no meaning as a measured quantity.

> **Definition (Remark 3.1) — the convention.** For jump processes one **defines**
> $$\mu^{\mathcal{E}}_X\big(\mathcal{C}_X(\gamma^m)\big) \;:=\; \int_0^\infty\frac{\mathrm{d}t}{t}\int_X\ \sum_{h\in[\tau^m]_{\mathrm{conj}}} p^{\mathcal{E}}_{\mathbb{H}^2}\big(t,\tilde z,h\tilde z\big)\,\mathrm{d}\rho_X(z),\tag{13}$$
> the [[Constr - The Periodised Kernel|periodisation]] restricted to the conjugacy class.

**Consistency.** For a **continuous** process (13) is a *theorem*, not a definition: the lifting dictionary gives $W^{t,\mathcal{E}}_{z\to z,X}=\sum_{h\in\Gamma}\pi_*W^{t,\mathcal{E}}_{\tilde z\to h\tilde z,\mathbb{H}^2}$, so restricting to $\mathcal{C}_X(\gamma^m)$ **is** restricting the sum to $[\tau^m]_{\mathrm{conj}}$. The content of (13) is that the same right-hand side is adopted as the meaning of the left when the left has none.

> **(J1) Justification on the marked space.** Work on the space carrying the **pair** $(B,S)$, not the time-changed path $Y$. Condition on $S_t=s$. Then:
> - the term indexed by $h$ corresponds upstairs to a Brownian bridge from some $\tilde w$ to $h\tilde w$;
> - the projection of the **full** Brownian arc $B\vert_{[0,s]}$ is a genuine continuous loop with monodromy $h$, and $[h]_{\mathrm{conj}}$ is independent of the lift;
> - the subordinator only decides which portions of that arc are observed; at a jump time $u$ the segment $B\vert_{[S_{u^-},S_u]}$ is deleted, but **its endpoints, hence the accumulated deck transformation, are unchanged**.
>
> So restricting to $[\tau^m]_{\mathrm{conj}}$ selects exactly the marked loops whose underlying Brownian arc lies in $\mathcal{C}_X(\gamma^m)$.
>
> **(J2) What genuinely fails.** The class is **not** a function of $Y$: the deleted segments can be filled by continuous paths of differing monodromy, so two marked loops with the same $Y$ can carry different classes.
>
> **(J3) Open question (the paper's).** Is there a canonical continuous interpolation of the jumps geometrising a càdlàg loop intrinsically — and must any such scheme break the closed-form mass formulas (90)? The paper conjectures yes to the second.

---

# Type card

> [!abstract] Type card — Remark 3.1
> **Given.** **(H1)** $\phi$ Bernstein with $\nu\neq0$, so $Y$ is a jump process. **(H2)** the periodisation (11). **(H3)** $\gamma\in\mathcal{P}_X$ with representative $\tau$, $m\geq1$.
>
> **Produces.** A **definition** (13) of the number $\mu^{\mathcal{E}}_X(\mathcal{C}_X(\gamma^m))\in[0,\infty]$, agreeing with the measured quantity whenever the process is continuous.
>
> **Lets you.** State [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] and [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds|Theorem 7.2]] uniformly across diffusions and jump processes — at the explicit price that in the jump case the left-hand side is a definition.

---

# Depends on

- [[Constr - The Periodised Kernel]] — (13) is (11) restricted
- [[Def - Deck Transformations and the Lift of a Rooted Loop]] — (F3) there is the obstruction
- [[Def - The Space of Unrooted Unparametrised Loops]] — (F4) there is the same statement on the loop space
- [[Def - Free Homotopy Class and Conjugacy Class Correspondence]] — the class being restricted to
- [[Def - Subordinator]] — the marked pair $(B,S)$
- [[Constr - The Dirichlet-Form Loop Measure]] — the measure whose classes are being read

---

# Properties

**(P1) Which cases are affected.** For $\phi(\lambda)=\lambda$ and $\phi(\lambda)=\lambda+\kappa$ the process is a diffusion (killing does not change paths), so (13) is a theorem. **Only the two stable cases are conventions.** Consequence worth carrying: the identity $\mu^\alpha_X=\tfrac\alpha2\mu_X$ of §3.1.3 relates a *defined* quantity to a *measured* one.

**(P2) Inherited by the loop soup.** In the jump case, [[Thm - Poissonian Structure of Homotopy Classes|Proposition 3.8]] takes $\mathcal{L}_c$ to be the Poisson point process of **marked** loops, with the same intensity $c\,\mu^\phi_X(\mathcal{C}_X(\gamma^m))$.

---

# Consumed by

- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]] — Step 1 branches on continuity: continuous branch uses the bridge decomposition, jump branch uses (13)
- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] — the stable instances are read through (13)
- [[Thm - Poissonian Structure of Homotopy Classes]] — the marked loop soup
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)]] — part (iii) uses $\mu^\alpha_X=\tfrac\alpha2\mu_X$
- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]] — same convention in $\mathbb{H}^3$

---

# Commentary

> [!note]- Commentary (skippable)
> This is one of the honest parts of the paper and deserves reading rather than skimming. The failure is not a regularity technicality: **the invariant the paper computes does not exist as a function on càdlàg loops**, and the reason is a hypothesis of covering-space theory, not of anything probabilistic.
>
> (J1) is what makes the convention meaningful rather than merely formal. The marked space carrying $(B,S)$ *does* support the monodromy class, and the subordinator's role there is purely one of observation — it deletes segments without moving their endpoints, so the accumulated deck transformation survives.
>
> (J3) is a concrete open problem, and its shape is worth noting: the paper suspects that intrinsic geometrisation and closed-form tractability are in tension. If true, that is a statement about why the mass formulas are as clean as they are.
