---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Fuchsian Group and the Quotient Surface"
  - "Def - Covering Space"
tags: [paper, topology, hyperbolic-geometry]
---

# Signature

| symbol | type |
|---|---|
| $\pi$ | $\mathbb{H}^2\to X=\Gamma\backslash\mathbb{H}^2$; covering map, local isometry |
| $h$ | $\in\Gamma$; a deck transformation: isometry of $\mathbb{H}^2$ with $\pi\circ h=\pi$ |
| $x$ | $\in X$ a basepoint; $\tilde x\in\pi^{-1}(x)$ a chosen lift |
| $\pi^{-1}(x)$ | the fibre; a $\Gamma$-torsor — $\Gamma$ acts **simply transitively** on it |
| $\omega$ | $[0,t]\to X$ **continuous**, $\omega(0)=\omega(t)=x$ |
| $\tilde\omega$ | $[0,t]\to\mathbb{H}^2$; the unique lift with $\tilde\omega(0)=\tilde x$ |
| $h_\omega$ | $\in\Gamma$; defined by $\tilde\omega(t)=h_\omega\,\tilde x$ |
| $\pi_1(X,x)$ | fundamental group of $X$ at $x$ |

---

# Definition

> **Definition (deck transformation).** $h$ is a **deck transformation** of $\pi$ if $h$ is an isometry of $\mathbb{H}^2$ with $\pi\circ h=\pi$. For $X=\Gamma\backslash\mathbb{H}^2$ with $\Gamma$ torsion-free Fuchsian, the deck group is exactly $\Gamma$, and it acts **simply transitively** on each fibre:
> $$\forall x\in X\ \forall\tilde x,\tilde x'\in\pi^{-1}(x)\ \exists!\,h\in\Gamma:\ \tilde x'=h\tilde x .$$

> **Definition (the recorded element $h_\omega$).** Fix $x\in X$ and $\tilde x\in\pi^{-1}(x)$. For $\omega:[0,t]\to X$ **continuous** with $\omega(0)=\omega(t)=x$:
> **(D1) Unique lifting.** There is a unique continuous $\tilde\omega:[0,t]\to\mathbb{H}^2$ with $\pi\circ\tilde\omega=\omega$ and $\tilde\omega(0)=\tilde x$.
> **(D2) Endpoint in the fibre.** $\tilde\omega(t)\in\pi^{-1}(x)$, so by simple transitivity there is a unique $h_\omega\in\Gamma$ with
> $$\tilde\omega(t)=h_\omega\,\tilde x .$$
> **(D3) Triviality criterion.** $h_\omega=1\iff\tilde\omega$ closes up $\iff\omega$ is null-homotopic.

> **(F1) Isomorphism.** $\omega\mapsto h_\omega$ is constant on homotopy classes rel basepoint and induces an isomorphism $\pi_1(X,x)\xrightarrow{\ \sim\ }\Gamma$, **depending on the choice of $\tilde x$**.
>
> **(F2) Conjugation under change of lift.** Replacing $\tilde x$ by $q\tilde x$ ($q\in\Gamma$) carries $\tilde\omega$ to $q\tilde\omega$, whose endpoint is $qh_\omega\tilde x=(qh_\omega q^{-1})(q\tilde x)$. So
> $$\tilde x\rightsquigarrow q\tilde x\quad\Longrightarrow\quad h_\omega\rightsquigarrow qh_\omega q^{-1}.$$
> **$h_\omega$ is not an invariant of $\omega$; its conjugacy class is.**
>
> **(F3) Continuity is a hypothesis of (D1).** Unique path lifting fails for càdlàg $\omega$. Consequence: [[Def - The Space of Unrooted Unparametrised Loops|(F4) there]] and [[Constr - Loop Mass in a Homotopy Class for Jump Processes]].

---

# Type card

> [!abstract] Type card — the lifting dictionary
> **Given.** **(H1)** $\Gamma$ torsion-free Fuchsian, $\pi:\mathbb{H}^2\to X$. **(H2)** $x\in X$, $\tilde x\in\pi^{-1}(x)$. **(H3)** $\omega:[0,t]\to X$ **continuous** with $\omega(0)=\omega(t)=x$.
>
> **Produces.** A unique lift $\tilde\omega$ and a unique element $h_\omega\in\Gamma$, with $h_\omega=1\iff\omega$ contractible; an isomorphism $\pi_1(X,x)\cong\Gamma$; and the conjugation law (F2).
>
> **Lets you.** Convert topology into group theory. Since [[Constr - The Periodised Kernel|the heat kernel downstairs is a Γ-indexed sum]], the analytic object arrives already decomposed by topological type: restricting the sum to a conjugacy class **is** restricting the loop measure to a free homotopy class.

---

# Depends on

- [[Def - Fuchsian Group and the Quotient Surface]] — (H1)
- [[Def - Free and Properly Discontinuous Action]] — the covering consequence there gives $\pi$ and the deck group
- [[Def - Covering Space]], [[Def - Regular (Galois) Covering]], [[Thm - Galois Correspondence for Covering Spaces]] — (D1),(F1); $\pi$ is universal since $\mathbb{H}^2$ is simply connected, and regular since $\Gamma$ is transitive on fibres
- [[Def - Path-Product and the Fundamental Group]] — the target of (F1)

---

# Checks

**Instance.** $X$ the hyperbolic cylinder $\langle\tau\rangle\backslash\mathbb{H}^2$, $\tau:z\mapsto e^{\ell}z$; $x=\pi(i)$, $\tilde x=i$. The loop once around the core lifts to the segment of the imaginary axis from $i$ to $e^{\ell}i$ — it does **not** close up — so $h_\omega=\tau$. Winding $m$ times gives $\tau^m$; the reverse gives $\tau^{-1}$; a small disc-bounding loop lifts to a closed loop, $h_\omega=1$, confirming (D3).

**Non-instance (the lift-dependence is real).** Same $\omega$, but lift started at $q\tilde x$: the recorded element becomes $qh_\omega q^{-1}$, a **conjugate**, by (F2). So the assignment $\omega\mapsto h_\omega$ is not well defined without a choice of $\tilde x$. Since the loop measure has already forgotten the basepoint, the conjugacy class is exactly the right amount of information — [[Def - Free Homotopy Class and Conjugacy Class Correspondence]].

**Non-instance (fails F3).** $\omega\in D([0,t];X)\setminus C([0,t];X)$. (D1) has no content: there is no unique continuous lift, hence no $h_\omega$, hence no homotopy class. This is not a regularity technicality — the invariant the paper computes simply does not exist as a function on càdlàg loops.

---

# Used at

- [[Def - Free Homotopy Class and Conjugacy Class Correspondence]] — (F2) **is** the correspondence
- [[Constr - The Periodised Kernel]] — the $\Gamma$-indexed sum indexed by recorded deck transformations
- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]] — Step 1: $W^{t,\mathcal{E}}_{z\to z,X}=\sum_{h\in\Gamma}\pi_*W^{t,\mathcal{E}}_{\tilde z\to h\tilde z,\mathbb{H}^2}$, i.e. this dictionary applied to bridge measures
- [[Constr - Loop Mass in a Homotopy Class for Jump Processes]] — where (F3) forces a convention
- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds]] — the same on $\mathbb{H}^3$

---

# Commentary

> [!note]- Commentary (skippable)
> $\mathbb{H}^2$ covers $X$, and $\Gamma$ is the group of symmetries of that covering. A loop upstairs need not close: it ends somewhere in the fibre, and since $\Gamma$ acts simply transitively there, it records a unique group element. That element is the topological content of the loop, trivial exactly when the loop is contractible.
>
> Why this belongs in a probability paper: the heat kernel downstairs is $\sum_{h\in\Gamma}p_{\mathbb{H}^2}(t,\tilde z,h\tilde w)$ — a sum indexed by $\Gamma$. So the analytic object arrives already sorted by topological type, and restricting the sum to a conjugacy class is the same operation as restricting the loop measure to a free homotopy class. That coincidence is the mechanism of the whole paper.
>
> (F3) is the clause with downstream teeth, and its position is worth noting: it is a hypothesis of *unique path lifting*, i.e. of covering-space theory, not of anything probabilistic. The failure for jump processes is inherited from topology.
