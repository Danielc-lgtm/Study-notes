---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Self-Adjoint Operator"
tags: [paper, probability, dirichlet-forms, functional-analysis]
---

# Notation

- $(E,m)$ — a locally compact separable metric space with a Radon measure $m$ of full support
- $\langle\cdot,\cdot\rangle$, $\|\cdot\|$ — the inner product and norm of $L^2(E,m)$
- $(\mathcal{E},\mathcal{F})$ — a regular symmetric Dirichlet form: $\mathcal{E}$ a non-negative definite symmetric bilinear form on a dense linear subspace $\mathcal{F}\subseteq L^2(E,m)$, closed and Markovian
- $A$ — the generator: a non-negative definite self-adjoint operator on $L^2(E,m)$ with $\mathcal{F}=\operatorname{Dom}(A^{1/2})$ and $\mathcal{E}(u,v)=\langle A^{1/2}u,A^{1/2}v\rangle$
- $e^{-tA}$ — the associated strongly continuous contraction semigroup
- $p^{\mathcal{E}}(t,x,y)$ — the transition density against $m$, assumed jointly measurable and symmetric
- $\mathcal{E}_{X'}$ — the **part form** on an open $X'\subseteq E$: the form of the process killed on leaving $X'$

---

# In plain language

A Dirichlet form is the analytic name for a symmetric Markov process. Instead of describing the process by its paths, you describe it by a quadratic form — think of $\mathcal{E}(u,u)=\int|\nabla u|^2$ for Brownian motion — and the point is that the dictionary between the two descriptions is exact: Fukushima's theorem says a regular symmetric Dirichlet form determines a Hunt process, unique up to quasi-everywhere equivalence, and conversely.

Why the paper cares: [[Constr - The Brownian Loop Measure|Definition 2.1]] built a loop measure from a heat kernel and its bridges, and nothing in that recipe was about Brownian motion. To say "any process for which this works" one needs a class, and "regular symmetric Dirichlet form" is that class, stated as a *checkable condition on a quadratic form* rather than a wish about paths. Then §2.3 manufactures new members of the class by subordination, and the whole paper runs over them uniformly.

Three words in the definition are load-bearing. **Symmetric** gives $p^{\mathcal{E}}(t,x,y)=p^{\mathcal{E}}(t,y,x)$, used silently whenever a bridge from $x$ to $y$ is exchanged for one from $y$ to $x$ — and it is what makes the generator self-adjoint rather than merely closed. **Markovian** is the condition that makes the form come from a *process* rather than from an arbitrary operator: it says the form does not increase under the normal contractions of a function, which is the analytic shadow of "the semigroup preserves $0\leq u\leq1$". **Regular** is a compatibility between $\mathcal{F}$ and the continuous compactly supported functions; it is the technical hypothesis Fukushima's theorem needs.

---

# The definition

> **Definition (regular symmetric Dirichlet form).** Let $(E,m)$ be a locally compact separable metric space with a Radon measure $m$ of full support. A **symmetric Dirichlet form** on $L^2(E,m)$ is a pair $(\mathcal{E},\mathcal{F})$ in which $\mathcal{E}$ is a non-negative definite symmetric bilinear form defined on a dense linear subspace $\mathcal{F}\subseteq L^2(E,m)$, which is **closed** ($\mathcal{F}$ is complete in the norm $(\mathcal{E}(u,u)+\|u\|^2)^{1/2}$) and **Markovian**. It is **regular** when $\mathcal{F}\cap C_c(E)$ is dense both in $\mathcal{F}$ for the form norm and in $C_c(E)$ for the uniform norm.

> **Theorem (Fukushima's correspondence).** A regular symmetric Dirichlet form $(\mathcal{E},\mathcal{F})$ on $L^2(E,m)$ determines a Hunt process on $E$, unique up to quasi-everywhere equivalence, and conversely every $m$-symmetric Hunt process arises this way.

The generator side of the dictionary: such a form determines a non-negative definite self-adjoint operator $A$ on $L^2(E,m)$ with $\mathcal{F}=\operatorname{Dom}(A^{1/2})$ and $\mathcal{E}(u,v)=\langle A^{1/2}u,A^{1/2}v\rangle$, so that
$$\mathcal{E}(u,v)=\langle Au,v\rangle,\qquad u\in\operatorname{Dom}(A),\ v\in\mathcal{F},$$
and hence a strongly continuous semigroup $e^{-tA}$. **The paper assumes throughout that the semigroup admits a jointly measurable symmetric transition density $p^{\mathcal{E}}(t,x,y)$ with respect to $m$**, so that $(e^{-tA}f)(x)=\int_E p^{\mathcal{E}}(t,x,y)f(y)\,m(\mathrm{d}y)$. That assumption is not automatic and is exactly what [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]] protects in the subordinate case.

---

# Types and signatures

- $\mathcal{E} : \mathcal{F}\times\mathcal{F}\to\mathbb{R}$ — symmetric, bilinear, non-negative definite
- $\mathcal{F}\subseteq L^2(E,m)$ — a dense linear subspace, complete in the form norm; equal to $\operatorname{Dom}(A^{1/2})$
- $A$ — an unbounded operator with $\operatorname{Dom}(A)\subseteq\mathcal{F}$; self-adjoint, non-negative, so $\operatorname{spec}(A)\subseteq[0,\infty)$ ([[Def - Self-Adjoint Operator]])
- $e^{-tA} : L^2(E,m)\to L^2(E,m)$ — a strongly continuous contraction semigroup, $t\geq0$
- $p^{\mathcal{E}} : (0,\infty)\times E\times E\to[0,\infty)$ — jointly measurable, symmetric in the space variables, a density against $m$

---

# Example

Brownian motion on a Riemannian surface: $E=X$, $m=\mathrm{vol}_g$, $\mathcal{E}(u,u)=\int_X|\nabla u|^2\,\mathrm{d}\mathrm{vol}_g$, $\mathcal{F}=H^1(X)$ (or $H^1_0(X)$ with Dirichlet conditions on $\partial X$), $A=\Delta_X$, and $p^{\mathcal{E}}=p_X$ the heat kernel. Adding a constant killing rate gives $\mathcal{E}^\kappa(f,f)=\int_X|\nabla f|^2\,\mathrm{d}\mathrm{vol}_g+\kappa\int_X f^2\,\mathrm{d}\mathrm{vol}_g$, generator $\Delta_X+\kappa$, and density $e^{-\kappa t}p_X(t,x,y)$ — Example 2.6 of the paper.

**Near-miss non-example.** A non-symmetric Dirichlet form — the theory exists (Ma–Röckner) and its forms still generate semigroups — fails the symmetry clause, so its generator is not self-adjoint and its transition density need not satisfy $p(t,x,y)=p(t,y,x)$. The paper notes that the non-symmetric theory "has fewer connections to Markov processes"; concretely, the loop measure construction would break, because the identification of $\int_X W^t_{x\to x}\,\mathrm{d}\mathrm{vol}_g(x)$ as a natural object relies on the diagonal being symmetric in a way a non-reversible process does not supply.

---

# Used in this paper at

- [[Constr - The Dirichlet-Form Loop Measure]] — Definition 2.2 is stated for exactly this class
- [[Def - Subordinator and Subordination of a Semigroup]] — the subordinate form $(\mathcal{E}^\phi,\mathcal{F}^\phi)$ is again of this class, with the explicit expression (5)
- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]] — hypothesised as a $\Gamma$-invariant regular symmetric Dirichlet form on $L^2(\mathbb{H}^2,\rho)$
- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds|Theorem 7.1]] — the same, on $\mathbb{H}^3$
- [[Constr - The Brownian Loop Measure]] — restriction holds because the **part form** $\mathcal{E}_{X'}$ on an open subset is the form of the process killed on leaving $X'$, so its bridge measures are the ambient ones restricted to paths staying inside

---

# Where this sits in my DAG

The functional-analytic content — closed non-negative quadratic forms, self-adjoint generators, $L^2$ semigroups, the square-root domain — is *Functional Analysis* (🟢) and needs nothing further. The probabilistic content — Markov processes, Hunt processes, transition densities — is *Advanced Probability* (🟢) and *SDEs* (🟢).

The one genuinely non-anchor ingredient is **Fukushima's correspondence theorem itself**, which is quoted and not proved anywhere in the paper or in this note-set. It is not on the gaps list of [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes]] because nothing downstream depends on its *proof*: the paper only ever uses the direction "a form gives a process with a density", and in every concrete case (Brownian, killing, stable) the process and its density are written down explicitly anyway. The reference is Fukushima–Oshima–Takeda.
