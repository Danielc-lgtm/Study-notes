---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, probability, dirichlet-forms]
---

# Signature

| symbol | type |
|---|---|
| $(E,m)$ | locally compact separable metric space; $m$ Radon of full support |
| $(\mathcal{E},\mathcal{F})$ | a [[Def - Regular Symmetric Dirichlet Form\|regular symmetric Dirichlet form]] on $L^2(E,m)$ |
| $M$ | a Hunt process on $E$: strong Markov, right-continuous paths, quasi-left-continuous |
| q.e. | quasi-everywhere: outside a set of zero capacity for $(\mathcal{E},\mathcal{F})$ |

---

# Statement

> **(FK) Fukushima's correspondence.** *Precondition:*
> **(P1)** $(E,m)$ locally compact separable metric, $m$ Radon of full support;
> **(P2)** $(\mathcal{E},\mathcal{F})$ satisfies (D1) closed, (D2) Markovian, (D3) regular, and is symmetric.
>
> *Conclusion:* there exists an $m$-symmetric **Hunt process** $M$ on $E$ whose $L^2$ semigroup is $e^{-tA}$, with $A$ the generator of $(\mathcal{E},\mathcal{F})$; and $M$ is **unique up to quasi-everywhere equivalence**. Conversely, every $m$-symmetric Hunt process arises this way from a regular symmetric Dirichlet form.

> [!warning] What (FK) does *not* give
> It does **not** give a transition density. Existence of $p^{\mathcal{E}}$ satisfying [[Def - Transition Density and Heat Kernel|(D1)–(D3)]] is a separate hypothesis, assumed throughout the paper and protected under subordination by [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|(A2.3)]].

---

# Type card

> [!abstract] Type card — (FK)
> **Given.** (P1),(P2).
>
> **Produces.** A Hunt process on $E$, unique up to q.e. equivalence, with prescribed $L^2$ semigroup. An existence-and-uniqueness statement, not a formula.
>
> **Lets you.** Read "regular symmetric Dirichlet form" as a synonym for "$m$-symmetric Hunt process", so that the loop-measure construction can be hypothesised on the analytic side and applied on the probabilistic side without further comment.

---

# Status

- **Proved here:** no.
- **Source:** Fukushima, *Dirichlet spaces and strong Markov processes*, Trans. AMS 162 (1971); Fukushima–Oshima–Takeda, *Dirichlet forms and symmetric Markov processes*, 2011.
- **DAG node that would close this:** *Stochastic Analysis* (⭐🔵) together with *Functional Analysis* (🟢); the specific material is standard Dirichlet-form theory and is not currently a node.
- **What is safe to assume:** existence and q.e.-uniqueness of the process. **Nothing downstream uses the proof, and nothing uses the converse direction.** In every concrete case of the paper — Brownian, killing, $\alpha$-stable, shifted $\alpha$-stable — the process and its density are written down explicitly anyway, so (FK) functions as a licence to speak of "the process" in the general statements of §2.2 and §3.

---

# Used at

- [[Def - Regular Symmetric Dirichlet Form]] — to attach a process to the form
- [[Constr - The Dirichlet-Form Loop Measure]] — Definition 2.2 speaks of the paths of "the" process
- [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms]] — the subordinate form is again regular symmetric, hence again has a Hunt process

---

# Commentary

> [!note]- Commentary (skippable)
> The value of (FK) in this paper is entirely one of *phrasing*. §2.2 wants to say "the loop-measure construction runs for any symmetric Markov process with a transition density", and the class of such processes is not something one can quantify over without a handle on it. (FK) supplies the handle: the class is in bijection with a class of quadratic forms, and quadratic forms can be manipulated — in particular, subordinated.
>
> So the dependency is real but shallow. A reader who took (FK) on faith, or who simply restricted attention to the four explicit processes of §2.3, would lose nothing in §3–§7.
