---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Def - Conditional Density"
  - "Def - Conditional Expectation"
  - "Thm - Fubini-Tonelli Theorem"
tags: [probability, advanced-probability]
---

# Problem Statement

Let $(U,V)$ have joint density $f_{U,V}$ on $\mathbb{R}^2$, and $h:\mathbb{R}\to\mathbb{R}$ Borel with $h(V)\in L^1$.

**(a)** Show that $\mathbb{E}[h(V)\mid U]=g(U)$, where $g(u)=\int_\mathbb{R}h(v)\,f_{V\mid U}(v\mid u)\,\mathrm{d}v$ is the integral against the [[Def - Conditional Density|conditional density]].

**(b)** Verify the two [[Def - Conditional Expectation|characterising properties]] for $g(U)$.

**(c)** Conclude the computational rule: *for variables with a joint density, conditional expectation is integration against the conditional density.*

**Recall:**

![[Def - Conditional Density#The Definition]]

---

# Convergent Strategy

**Problem class:** confirming the concrete density formula computes the abstract conditional expectation.

**Assumption pattern:** propose the candidate $g(U)$; it is manifestly $\sigma(U)$-measurable; the averaging identity over $\{U\in B\}$ is a [[Thm - Fubini-Tonelli Theorem|Fubini]] computation against the joint density.

---

# Legal Operations Used

1. **Propose $g(U)$, verify the two characterising properties.**
2. **Fubini–Tonelli** against the joint density.

---

# Hints

> [!note]- Hint 1
> $g(U)$ is a function of $U$, hence $\sigma(U)$-measurable.

> [!note]- Hint 2
> A generic $A\in\sigma(U)$ is $\{U\in B\}$. Compute $\mathbb{E}[h(V)\mathbf{1}_{U\in B}]=\iint h(v)\mathbf{1}_B(u)f_{U,V}(u,v)\,\mathrm{d}u\,\mathrm{d}v$.

> [!note]- Hint 3
> Substitute $f_{U,V}=f_{V\mid U}\,f_U$ and apply Fubini.

---

# Solution

The proof breaks into two steps. Step 1 (combined a and b) proposes the candidate $g(U) = \int h(v)\,f_{V\mid U}(v\mid u)\,dv$, observes it is $\sigma(U)$-measurable, and verifies the averaging identity over generic $\sigma(U)$-sets $\{U \in B\}$ by writing $f_{U, V} = f_{V\mid U} f_U$ and applying Fubini to extract $\mathbb{E}[g(U)\mathbf{1}_A]$; Step 2 reads off the concrete computational rule. The non-obvious move is in Step 1 — using the identity $f_{U, V} = f_{V \mid U} f_U$ to split the double integral is what allows Fubini to factor the $v$-integral out, recovering $g$ as a function of $u$.

**Step 1 — (a),(b).** Set $g(u)=\int_\mathbb{R}h(v)f_{V\mid U}(v\mid u)\,\mathrm{d}v$ and consider the candidate $g(U)$.

> [!note]- Derivation
> *$\sigma(U)$-measurability.* $g(U)$ is a Borel function of $U$, hence $\sigma(U)$-measurable.
> *Averaging identity.* Every $A\in\sigma(U)$ has the form $\{U\in B\}$, $B$ Borel. By the [[Ex - Expectation via the law|change-of-variables formula]] and the joint density,
> $$\mathbb{E}[h(V)\mathbf{1}_{U\in B}]=\iint_{\mathbb{R}^2}h(v)\mathbf{1}_B(u)\,f_{U,V}(u,v)\,\mathrm{d}u\,\mathrm{d}v.$$
> Substitute $f_{U,V}(u,v)=f_{V\mid U}(v\mid u)\,f_U(u)$ (definition of the [[Def - Conditional Density|conditional density]]) and apply [[Thm - Fubini-Tonelli Theorem|Fubini]] — integrating $v$ first:
> $$=\int_\mathbb{R}\mathbf{1}_B(u)\Big(\int_\mathbb{R}h(v)f_{V\mid U}(v\mid u)\,\mathrm{d}v\Big)f_U(u)\,\mathrm{d}u=\int_\mathbb{R}\mathbf{1}_B(u)\,g(u)\,f_U(u)\,\mathrm{d}u=\mathbb{E}[g(U)\mathbf{1}_{U\in B}].$$
> So $\mathbb{E}[h(V)\mathbf{1}_A]=\mathbb{E}[g(U)\mathbf{1}_A]$ for all $A\in\sigma(U)$ — the averaging identity. With $\sigma(U)$-measurability, $g(U)$ satisfies the characterisation; by [[Thm - Existence and Uniqueness of Conditional Expectation|uniqueness]], $\mathbb{E}[h(V)\mid U]=g(U)$.

**Step 2 — (c).** Thus, for jointly-continuous variables, the abstract conditional expectation is a concrete integral:
$$\mathbb{E}[h(V)\mid U=u]=\int_\mathbb{R}h(v)\,f_{V\mid U}(v\mid u)\,\mathrm{d}v.$$
One forms the conditional density (joint over marginal), integrates $h$ against it in $v$, and the result, evaluated at $U$, is the conditional expectation. The conditioning event $\{U=u\}$ has probability zero, yet the formula is perfectly well-defined — that is the payoff of *defining* conditional expectation by a characterisation rather than a quotient.

> [!note]- Complete formal solution
> $g(U)$ is $\sigma(U)$-measurable. For $A=\{U\in B\}\in\sigma(U)$: $\mathbb{E}[h(V)\mathbf{1}_A]=\iint h(v)\mathbf{1}_B(u)f_{U,V}\,\mathrm{d}u\,\mathrm{d}v$; writing $f_{U,V}=f_{V\mid U}f_U$ and applying Fubini gives $\int\mathbf{1}_B(u)g(u)f_U(u)\,\mathrm{d}u=\mathbb{E}[g(U)\mathbf{1}_A]$. Uniqueness $\Rightarrow\mathbb{E}[h(V)\mid U]=g(U)$. $\blacksquare$

---

# Key Takeaways

**For variables with a joint density, conditional expectation is integration against the [[Def - Conditional Density|conditional density]] — the abstract object becomes a concrete one-variable integral.** $\mathbb{E}[h(V)\mid U=u]=\int h(v)f_{V\mid U}(v\mid u)\,\mathrm{d}v$, with $f_{V\mid U}=f_{U,V}/f_U$ the ratio of joint to marginal. The proof is the universal *propose-and-verify*: $g(U)$ is manifestly a function of $U$, and the averaging identity is a [[Thm - Fubini-Tonelli Theorem|Fubini]] computation that *uses the definition $f_{U,V}=f_{V\mid U}f_U$ to split the double integral*.

**This is the formula that makes Bayesian computation concrete — and it works despite conditioning on a probability-zero event.** $\{U=u\}$ is null whenever $U$ is continuous, so the elementary quotient $\mathbb{E}[\cdot\mathbf{1}_{U=u}]/\mathbb{P}(U=u)$ is "$0/0$" — yet $\int h\,f_{V\mid U}(\cdot\mid u)\,\mathrm{d}v$ is a genuine, finite quantity. The reconciliation is precisely that conditional expectation is *defined by the two characterising properties*, not by a ratio; the conditional density supplies a candidate, and Fubini verifies it. The same machinery, with $V$ a parameter and $U$ the data, is the posterior expectation of [[Def - Conditional Density|Bayesian inference]].
