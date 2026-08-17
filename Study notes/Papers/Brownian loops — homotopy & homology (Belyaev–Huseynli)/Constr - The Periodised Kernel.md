---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Fuchsian Group and the Quotient Surface"
  - "Def - Deck Transformations and the Lift of a Rooted Loop"
  - "Def - Dirichlet Form and the Hunt Process Correspondence"
tags: [paper, probability, hyperbolic-geometry, heat-kernels]
---

# Notation

- $\pi:\mathbb{H}^2\to X=\Gamma\backslash\mathbb{H}^2$ — the covering projection; $\Gamma$ torsion-free Fuchsian
- $(\mathcal{E},\mathcal{F})$ — a $\Gamma$-invariant regular symmetric [[Def - Dirichlet Form and the Hunt Process Correspondence|Dirichlet form]] on $L^2(\mathbb{H}^2,\rho)$
- $p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,w)$ — its jointly measurable integral kernel with respect to $\rho$, satisfying the invariance $p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,w)=p^{\mathcal{E}}_{\mathbb{H}^2}(t,hz,hw)$ for all $h\in\Gamma$
- $\tilde z,\tilde w\in\mathbb{H}^2$ — any lifts of $z,w\in X$, that is $\pi(\tilde z)=z$, $\pi(\tilde w)=w$
- $p^{\mathcal{E}}_X(t,z,w)$ — the periodised kernel on $X$; $\rho_X$ the induced area measure
- $p^\phi_{\mathbb{H}^2}$, $p^\phi_X$ — the subordinate versions
- $\mu^{\mathcal{E}}_X$ — the loop measure associated with the descended form

---

# In plain language

The heat kernel downstairs is the sum of the heat kernel upstairs over all the ways to get there.

Concretely: a path on $X$ from $z$ to $w$ lifts to a path upstairs from $\tilde z$ to *some* point of the fibre over $w$, and the fibre is $\{h\tilde w : h\in\Gamma\}$. Summing the upstairs kernel over the fibre reassembles the downstairs kernel. That is the periodisation, and it is the analytic half of the covering-space dictionary — the probabilistic half being that the bridge measure downstairs decomposes as a sum of upstairs bridge measures pushed down.

**Why this is the construction the paper needs, rather than a technical convenience.** The sum is indexed by $\Gamma$. By [[Def - Free Homotopy Class and Conjugacy Class Correspondence|the correspondence]], subsets of $\Gamma$ closed under conjugation correspond to free homotopy classes of loops. So the periodised kernel arrives **already decomposed by topological type**, and restricting the sum to a conjugacy class is the same operation as restricting the loop measure to a free homotopy class. The whole of §3 is that observation carried out.

Two hypotheses make it work, and both must be stated because both are used. **$\Gamma$-invariance of the kernel**, $p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,w)=p^{\mathcal{E}}_{\mathbb{H}^2}(t,hz,hw)$, is what makes the sum independent of which lifts $\tilde z,\tilde w$ were chosen — and it is used again, crucially, in the unfolding step of Theorem 3.2 to move a coset representative onto the integration region. **Decay fast enough to beat the orbit growth of $\Gamma$** is what makes the sum converge. For subordinate Brownian motion on $\mathbb{H}^2$ both hold: $\Delta_{\mathbb{H}^2}$ is $\mathrm{PSL}(2,\mathbb{R})$-invariant and $\phi$ acts by functional calculus, so $p^\phi_{\mathbb{H}^2}$ is $\mathrm{PSL}(2,\mathbb{R})$-invariant; and the Gaussian-type decay in $d(z,w)$ dominates the exponential orbit growth at rate $\delta\leq1$.

---

# The construction

> **Construction (equation (11) — the periodised kernel).** Assume $(\mathcal{E},\mathcal{F})$ is $\Gamma$-invariant and its semigroup admits a jointly measurable heat kernel $p^{\mathcal{E}}_{\mathbb{H}^2}$ with $p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,w)$ decaying in $d(z,w)$ fast enough to beat the orbit growth of $\Gamma$. Then for each $t>0$ the series
> $$p^{\mathcal{E}}_X(t,z,w) := \sum_{h\in\Gamma} p^{\mathcal{E}}_{\mathbb{H}^2}(t,\tilde z, h\tilde w)\tag{11}$$
> converges, where $\tilde z,\tilde w\in\mathbb{H}^2$ are any points with $\pi(\tilde z)=z$ and $\pi(\tilde w)=w$; the value does not depend on the choice of lifts.

> **Standing assumption.** It is assumed throughout §3 that the $\Gamma$-invariant form descends to a regular symmetric Dirichlet form on $L^2(X,\rho_X)$ whose transition density is precisely the periodisation (11), and $\mu^{\mathcal{E}}_X$ denotes the associated loop measure.

**This holds in all the subordinate Brownian cases**, where the two ways of computing agree:
$$p^\phi_X(t,z,w) = \int_{[0,\infty)}p_X(s,z,w)\,\psi^\phi_t(\mathrm{d}s) = \sum_{h\in\Gamma}p^\phi_{\mathbb{H}^2}(t,\tilde z, h\tilde w).$$
That the two agree is the statement that subordination and periodisation commute — both are averaging operations, one over the subordinator law and one over the group, and Tonelli exchanges them.

**Independence of lifts.** Changing $\tilde z$ to $q\tilde z$ and $\tilde w$ to $q'\tilde w$ replaces the summand by $p^{\mathcal{E}}_{\mathbb{H}^2}(t,q\tilde z,hq'\tilde w) = p^{\mathcal{E}}_{\mathbb{H}^2}(t,\tilde z,q^{-1}hq'\tilde w)$ by $\Gamma$-invariance, and $h\mapsto q^{-1}hq'$ is a bijection of $\Gamma$, so the sum is unchanged.

---

# Type card

> [!abstract] Type card — the periodised kernel
> **Given.** A $\Gamma$-invariant regular symmetric Dirichlet form on $L^2(\mathbb{H}^2,\rho)$ whose semigroup has a jointly measurable kernel $p^{\mathcal{E}}_{\mathbb{H}^2}$ satisfying $p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,w)=p^{\mathcal{E}}_{\mathbb{H}^2}(t,hz,hw)$ for all $h\in\Gamma$, with decay beating the orbit growth of $\Gamma$.
>
> **Produces.** A kernel $p^{\mathcal{E}}_X : (0,\infty)\times X\times X\to(0,\infty)$, independent of the lifts chosen, assumed to be the transition density of a regular symmetric Dirichlet form on $L^2(X,\rho_X)$ — hence of a process on $X$ with an associated loop measure $\mu^{\mathcal{E}}_X$.
>
> **Lets you.** Index the terms of the downstairs heat kernel by deck transformations, which is what makes a *topological* decomposition of an *analytic* object possible at all. Restricting the sum to a conjugacy class is restricting the loop measure to a free homotopy class.

---

# Properties relied on later

**$\Gamma$-invariance, used twice.** Once here, to make (11) independent of lifts. And once, decisively, in Step 2 of [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]]: for a coset representative $r$, invariance gives
$$p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,r\tau^m r^{-1}z) = p^{\mathcal{E}}_{\mathbb{H}^2}(t,r^{-1}z,\tau^m r^{-1}z),$$
which is exactly what allows the substitution $w=r^{-1}z$ to move the whole integral onto the translated region $r^{-1}F$. **Without $\Gamma$-invariance there is no unfolding and no theorem.**

**Convergence.** The decay hypothesis is stated qualitatively in the paper ("fast enough to beat the orbit growth of $\Gamma$; this is the case in all our examples") rather than as a sharp condition. The quantitative content: the number of orbit points within distance $R$ grows like $e^{\delta R}$ with $\delta\leq1$ by [[Def - Critical Exponent and the Prime Geodesic Theorem|the critical exponent]], and the hyperbolic heat kernel decays like $e^{-d(z,w)^2/4t}$, which is Gaussian and dominates every exponential.

**Restriction to a conjugacy class.** For a continuous process, restricting the sum in (11) with $\tilde z=\tilde w$ to $h\in[\tau^m]_{\mathrm{conj}}$ picks out exactly the loops in $\mathcal{C}_X(\gamma^m)$, by the lifting picture. **For a jump process this is false as a statement about paths, and the restriction is promoted to a definition** — see [[Constr - Loop Mass in a Homotopy Class for Jump Processes]].

---

# Consumed by

- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]] — assumed as a hypothesis; Steps 1 and 2 both operate on (11)
- [[Constr - Loop Mass in a Homotopy Class for Jump Processes]] — the jump-case definition (13) is the periodisation restricted to $[\tau^m]_{\mathrm{conj}}$
- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds|Theorem 7.1]] — the $\mathbb{H}^3$ periodisation, assumed under the same decay hypothesis
- [[§3.2 Euclidean Quantum Mechanics and the Path Integral|Remark 3.3]] — twisting the loop measure by a unitary representation replaces (11) by $\sum_h\chi(h)\,p^{\mathcal{E}}_{\mathbb{H}^2}(t,\tilde z,h\tilde w)$, and that twisted periodisation is what §4's Ruelle identity and §6.2's $L$-function identity are secretly about

---

# Where this sits in my DAG

Three ingredients. The covering-space dictionary is [[Def - Deck Transformations and the Lift of a Rooted Loop]], a genuine non-anchor rung reducing to [[Def - Covering Space]] and [[Thm - Galois Correspondence for Covering Spaces]] in the vault. The quotient geometry is [[Def - Fuchsian Group and the Quotient Surface]]. The analytic content — heat kernels, integral kernels of semigroups, Tonelli for the exchange of the group sum with the subordinator average — is anchors: *Analysis of PDEs* (🟢), *Functional Analysis* (🟢), *Advanced Probability* (🟢).

That the periodisation is the transition density of a form on the quotient is **assumed rather than proved** in the paper, and the assumption is flagged explicitly there ("we assume throughout that the $\Gamma$-invariant form descends..."). In every concrete case of the paper it is verifiable directly.
