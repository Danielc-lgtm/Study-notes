---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Fuchsian Group and the Quotient Surface"
  - "Def - Deck Transformations and the Lift of a Rooted Loop"
  - "Def - Regular Symmetric Dirichlet Form"
tags: [paper, probability, hyperbolic-geometry, heat-kernels]
---

# Signature

| symbol | type |
|---|---|
| $\pi$ | $\mathbb{H}^2\to X=\Gamma\backslash\mathbb{H}^2$; covering map |
| $(\mathcal{E},\mathcal{F})$ | regular symmetric Dirichlet form on $L^2(\mathbb{H}^2,\rho)$, **$\Gamma$-invariant** |
| $p^{\mathcal{E}}_{\mathbb{H}^2}$ | $(0,\infty)\times\mathbb{H}^2\times\mathbb{H}^2\to[0,\infty)$; jointly measurable, symmetric; density w.r.t. $\rho$ |
| $p^{\mathcal{E}}_X$ | $(0,\infty)\times X\times X\to[0,\infty)$; the periodisation |
| $\tilde z,\tilde w$ | any lifts: $\pi(\tilde z)=z$, $\pi(\tilde w)=w$ |
| $\delta$ | critical exponent of $\Gamma$; orbit growth rate $\#\{h:d(z,hz)\leq R\}\asymp e^{\delta R}$ |
| $\mu^{\mathcal{E}}_X$ | the loop measure of the descended form |

---

# Construction

> **Construction (11) — the periodised kernel.** Assume
> **(A1) $\Gamma$-invariance.** $\ p^{\mathcal{E}}_{\mathbb{H}^2}(t,hz,hw)=p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,w)$ for all $h\in\Gamma$, $t>0$, $z,w\in\mathbb{H}^2$.
> **(A2) Decay beats orbit growth.** $p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,w)$ decays in $d(z,w)$ fast enough that $\sum_{h\in\Gamma}p^{\mathcal{E}}_{\mathbb{H}^2}(t,\tilde z,h\tilde w)<\infty$ for each $t>0$.
>
> Then define
> $$p^{\mathcal{E}}_X(t,z,w) \;:=\; \sum_{h\in\Gamma} p^{\mathcal{E}}_{\mathbb{H}^2}(t,\tilde z,h\tilde w).\tag{11}$$

**Well-definedness (independence of lifts).** Replacing $(\tilde z,\tilde w)$ by $(q\tilde z,q'\tilde w)$, by (A1)
$$p^{\mathcal{E}}_{\mathbb{H}^2}(t,q\tilde z,hq'\tilde w)=p^{\mathcal{E}}_{\mathbb{H}^2}(t,\tilde z,q^{-1}hq'\tilde w),$$
and $h\mapsto q^{-1}hq'$ is a bijection of $\Gamma$, so the sum is unchanged. $\;\square$

> **(A3) Standing assumption.** The $\Gamma$-invariant form **descends** to a regular symmetric Dirichlet form on $L^2(X,\rho_X)$ whose transition density is precisely (11); $\mu^{\mathcal{E}}_X$ denotes the associated loop measure. *Assumed, not proved — the paper says so explicitly.*

> **(F1) Subordination commutes with periodisation.** In every subordinate Brownian case,
> $$p^\phi_X(t,z,w)=\int_{[0,\infty)}p_X(s,z,w)\,\psi^\phi_t(\mathrm{d}s)=\sum_{h\in\Gamma}p^\phi_{\mathbb{H}^2}(t,\tilde z,h\tilde w),$$
> by [[Thm - Fubini-Tonelli Theorem|Tonelli]] — both are averages over non-negative data.
>
> **(F2) (A1) holds in the subordinate cases.** $\Delta_{\mathbb{H}^2}$ is $\mathrm{PSL}(2,\mathbb{R})$-invariant and $\phi$ acts by functional calculus, so $p^\phi_{\mathbb{H}^2}$ is $\mathrm{PSL}(2,\mathbb{R})$-invariant — [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms|(PH)(C5)]].
>
> **(F3) (A2) holds in the subordinate cases.** Orbit growth is $e^{\delta R}$ with $\delta\leq1$; the hyperbolic heat kernel decays like $e^{-d(z,w)^2/4t}$, Gaussian, which dominates every exponential.

---

# Type card

> [!abstract] Type card — the periodised kernel
> **Given.** **(H1)** $\Gamma$ torsion-free Fuchsian. **(H2)** $(\mathcal{E},\mathcal{F})$ regular symmetric on $L^2(\mathbb{H}^2,\rho)$ with density $p^{\mathcal{E}}_{\mathbb{H}^2}$ satisfying (A1). **(H3)** (A2). **(H4)** (A3).
>
> **Produces.** $p^{\mathcal{E}}_X:(0,\infty)\times X\times X\to[0,\infty)$, independent of lifts; assumed to be the transition density of a regular symmetric Dirichlet form on $L^2(X,\rho_X)$, hence of a process on $X$ with loop measure $\mu^{\mathcal{E}}_X$.
>
> **Lets you.** Index the downstairs kernel by deck transformations, so that a **topological** restriction acts on an **analytic** object: restricting the sum to a conjugacy class **is** restricting the loop measure to a free homotopy class.

---

# Depends on

- [[Def - Deck Transformations and the Lift of a Rooted Loop]] — the fibre is a $\Gamma$-torsor; (11)'s index set
- [[Def - Fuchsian Group and the Quotient Surface]] — $\pi$, $\rho_X$
- [[Def - Regular Symmetric Dirichlet Form]] — (H2)
- [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms]] — (C5), giving (F2)
- [[Def - Critical Exponent]] — the orbit growth rate in (F3)
- [[Thm - Fubini-Tonelli Theorem]] — (F1)

---

# Properties

**(P1) $\Gamma$-invariance, used twice.** Once here, for independence of lifts. And once, decisively, in Step 2 of [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]]:
$$p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,r\tau^mr^{-1}z)=p^{\mathcal{E}}_{\mathbb{H}^2}(t,r^{-1}z,\tau^mr^{-1}z),$$
which is what moves a coset representative onto the integration region. **Without (A1) there is no unfolding and no theorem.**

**(P2) Restriction to a conjugacy class.** For a **continuous** process, restricting (11) with $\tilde z=\tilde w$ to $h\in[\tau^m]_{\mathrm{conj}}$ selects exactly the loops in $\mathcal{C}_X(\gamma^m)$, by the lifting dictionary. **For a jump process this is false as a statement about paths** — the restriction is promoted to a definition: [[Constr - Loop Mass in a Homotopy Class for Jump Processes]].

**(P3) Twisting.** Replacing (11) by $\sum_{h}\chi(h)\,p^{\mathcal{E}}_{\mathbb{H}^2}(t,\tilde z,h\tilde w)$ for a unitary character $\chi$ of $\pi_1(X)$ is the twisted periodisation of Remark 3.3. §4.1.2 and §6.2 are the two instances.

---

# Consumed by

- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]] — as (H1); Steps 1,2 both operate on (11)
- [[Constr - Loop Mass in a Homotopy Class for Jump Processes]] — the jump definition (13) is (11) restricted to $[\tau^m]_{\mathrm{conj}}$
- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds]] — the $\mathbb{H}^3$ periodisation, same hypotheses
- [[§3.2 Euclidean Quantum Mechanics and the Path Integral]] — Remark 3.3 and (P3)

---

# Commentary

> [!note]- Commentary (skippable)
> The heat kernel downstairs is the sum of the heat kernel upstairs over all the ways to get there: a path on $X$ from $z$ to $w$ lifts to a path from $\tilde z$ to *some* point of the fibre over $w$, and the fibre is $\{h\tilde w:h\in\Gamma\}$.
>
> That the sum is indexed by $\Gamma$ is the whole point. By the correspondence, subsets of $\Gamma$ closed under conjugation correspond to free homotopy classes, so the periodised kernel arrives **already decomposed by topological type**. §3 is that observation carried out.
>
> Note the honest status of (A3): the paper assumes rather than proves that the periodisation is the density of a form on the quotient, and flags the assumption explicitly. In every concrete case it is verifiable directly.
