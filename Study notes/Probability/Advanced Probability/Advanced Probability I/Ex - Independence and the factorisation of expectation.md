---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Def - Independence"
  - "Thm - Fubini-Tonelli Theorem"
  - "Thm - Product Measure"
tags: [probability, advanced-probability]
---

# Problem Statement

Let $X,Y$ be [[Def - Independence|independent]] random variables.

**(a)** Show that for non-negative Borel $f,g$ (and for $f(X),g(Y)\in L^1$), $\mathbb{E}[f(X)g(Y)]=\mathbb{E}[f(X)]\,\mathbb{E}[g(Y)]$. In particular $\mathbb{E}[XY]=\mathbb{E}X\,\mathbb{E}Y$ when $X,Y\in L^1$ are independent.

**(b)** Deduce independent integrable variables are **uncorrelated**.

**(c)** Show the law of the sum $X+Y$ is the **convolution** $\mu_X*\mu_Y$.

**Recall:**

[[Def - Independence|Independence]] of $X,Y$ $\iff$ the joint law is the [[Thm - Product Measure|product]] $\mu_{(X,Y)}=\mu_X\otimes\mu_Y$. [[Thm - Fubini-Tonelli Theorem|Fubini–Tonelli]].

---

# Convergent Strategy

**Problem class:** computing with independent variables — and the master tool is that *independence = product law*, so [[Thm - Fubini-Tonelli Theorem|Fubini]] applies.

**Assumption pattern:** $X,Y$ independent means $\mu_{(X,Y)}=\mu_X\otimes\mu_Y$. Any expectation of a function of $(X,Y)$ is an integral against this product measure, which Fubini splits into iterated one-variable integrals.

**Theorem routing:** $\mathbb{E}[f(X)g(Y)]=\int f(x)g(y)\,d(\mu_X\otimes\mu_Y)\overset{\text{Fubini}}{=}(\int f\,d\mu_X)(\int g\,d\mu_Y)$.

---

# Legal Operations Used

1. **Independence $=$ product law** $\mu_{(X,Y)}=\mu_X\otimes\mu_Y$.
2. **Change of variables** to integrate against the joint law.
3. **Fubini–Tonelli** to split the product integral.

---

# Hints

> [!note]- Hint 1
> By independence, $\mu_{(X,Y)}=\mu_X\otimes\mu_Y$. By [[Ex - Expectation via the law|change of variables]], $\mathbb{E}[f(X)g(Y)]=\int f(x)g(y)\,d(\mu_X\otimes\mu_Y)$.

> [!note]- Hint 2
> The integrand $f(x)g(y)$ separates; [[Thm - Fubini-Tonelli Theorem|Tonelli]] (for $f,g\ge0$) or Fubini splits it into a product of integrals.

> [!note]- Hint 3
> (c): $\mathbb{P}(X+Y\le t)=\int\int\mathbf{1}_{x+y\le t}\,d\mu_X(x)\,d\mu_Y(y)$.

---

# Solution

**Step 1 — (a) Factorisation.** Independence gives $\mu_{(X,Y)}=\mu_X\otimes\mu_Y$. For $f,g\ge0$ Borel, the [[Ex - Expectation via the law|change-of-variables formula]] and [[Thm - Fubini-Tonelli Theorem|Tonelli]]:
$$\mathbb{E}[f(X)g(Y)]=\int_{\mathbb{R}^2}f(x)g(y)\,d(\mu_X\otimes\mu_Y)=\int_\mathbb{R}f(x)\,d\mu_X(x)\cdot\int_\mathbb{R}g(y)\,d\mu_Y(y)=\mathbb{E}[f(X)]\,\mathbb{E}[g(Y)],$$
the middle step because the integrand *factors* and Tonelli splits the double integral. For integrable (signed) $f(X),g(Y)$, apply this to $|f|,|g|$ to check joint integrability, then to $f^\pm,g^\pm$ and recombine (Fubini). Taking $f(x)=x$, $g(y)=y$: $\mathbb{E}[XY]=\mathbb{E}X\,\mathbb{E}Y$.

**Step 2 — (b) Uncorrelated.** $\mathrm{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E}X\,\mathbb{E}Y=0$ by (a). So independent integrable variables are uncorrelated — and hence $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y$. (The converse fails: uncorrelated $\not\Rightarrow$ independent.)

**Step 3 — (c) Convolution.** For any $t$,
$$\mathbb{P}(X+Y\le t)=\int_{\mathbb{R}^2}\mathbf{1}_{\{x+y\le t\}}\,d(\mu_X\otimes\mu_Y)=\int_\mathbb{R}\Big(\int_\mathbb{R}\mathbf{1}_{\{x\le t-y\}}\,d\mu_X(x)\Big)d\mu_Y(y)=\int_\mathbb{R}\mu_X((-\infty,t-y])\,d\mu_Y(y),$$
by [[Thm - Fubini-Tonelli Theorem|Fubini]]. This is precisely the convolution: $\mu_{X+Y}=\mu_X*\mu_Y$, where $(\mu_X*\mu_Y)(B)=\int\mu_X(B-y)\,d\mu_Y(y)$. If $X,Y$ have densities $p,q$, then $X+Y$ has density $p*q$.

> [!note]- Complete formal solution
> (a) Independence $\Rightarrow\mu_{(X,Y)}=\mu_X\otimes\mu_Y$; change of variables + Tonelli give $\mathbb{E}[f(X)g(Y)]=(\int f d\mu_X)(\int g d\mu_Y)$; $f=g=\mathrm{id}$ gives $\mathbb{E}[XY]=\mathbb{E}X\,\mathbb{E}Y$. (b) $\mathrm{Cov}(X,Y)=\mathbb{E}[XY]-\mathbb{E}X\mathbb{E}Y=0$. (c) Fubini on $\mathbf{1}_{x+y\le t}$ against the product law gives $\mathbb{P}(X+Y\le t)=\int\mu_X((-\infty,t-y])d\mu_Y(y)$, i.e. $\mu_{X+Y}=\mu_X*\mu_Y$. $\blacksquare$

---

# Key Takeaways

**Independence *is* the product-measure structure, so every computation with independent variables is a [[Thm - Fubini-Tonelli Theorem|Fubini]] computation against a product law.** "$X,Y$ independent" should immediately be read as "$\mu_{(X,Y)}=\mu_X\otimes\mu_Y$" — and then expectations of functions of $(X,Y)$ split into iterated integrals. Factorisation of expectation ($\mathbb{E}[f(X)g(Y)]=\mathbb{E}f(X)\,\mathbb{E}g(Y)$) and the convolution formula for the law of a sum are the two everyday consequences; both are Fubini applied to a separating, resp. shift-structured, integrand.

**Independence $\Rightarrow$ uncorrelated, and the law of a sum of independents is a convolution — these are the two facts that make sums of independent variables tractable.** Uncorrelatedness makes variance additive ($\mathrm{Var}(S_n)=n\mathrm{Var}(X_1)$ for i.i.d. sums), the engine of the [[Thm - Strong Law of Large Numbers|laws of large numbers]]. The convolution structure means the [[Def - Characteristic Function|characteristic function]] of a sum is the *product* of characteristic functions ($\widehat{\mu*\nu}=\hat\mu\hat\nu$) — turning the analysis of $S_n=\sum X_i$ into the analysis of $\varphi_X^n$, which is precisely the route of the [[Thm - Central Limit Theorem|central limit theorem]].
