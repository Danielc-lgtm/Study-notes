---
type: theorem
subject: advanced-probability
prereqs:
  - "Def - Conditional Expectation"
  - "Thm - Existence and Uniqueness of Conditional Expectation"
  - "Thm - Jensen's Inequality"
tags: [probability, advanced-probability]
---

# Notation

$X,Y\in L^1(\Omega,\mathcal{F},\mathbb{P})$; $\mathcal{H}\subseteq\mathcal{G}\subseteq\mathcal{F}$ sub-$\sigma$-algebras; $\mathbb{E}[\cdot\mid\mathcal{G}]$ as in [[Def - Conditional Expectation|the definition]].

---

# Motivation

[[Def - Conditional Expectation|Conditional expectation]] was defined by a characterisation, not a formula. To *use* it one needs its calculus — the rules by which it interacts with addition, ordering, products, nested conditioning, limits, and convex functions. This theorem is that calculus. Two rules are the genuinely conditional ones, with no unconditional analogue: the **tower property** ("a coarser average of a finer average is the coarser average") and **taking out what is known** ("a $\mathcal{G}$-measurable factor passes through the conditioning"). The rest are the ordinary properties of expectation, conditionalised.

---

# Sources and Targets

**Sources.** Hypothesis: $X,Y\in L^1$ (or $\ge0$ for the monotone statements). Every property is proved the same way — *verify the candidate satisfies the two [[Def - Conditional Expectation|characterising properties]]*, then invoke [[Thm - Existence and Uniqueness of Conditional Expectation|uniqueness]].

**Targets.** Linearity makes $\mathbb{E}[\cdot\mid\mathcal{G}]$ a linear operator; the **tower property** is the defining identity of [[Def - Martingale|martingales]] and the engine of the [[Thm - Strong Law of Large Numbers|SLLN]]; **conditional Jensen** makes $|M_n|^p$ a [[Def - Submartingale|submartingale]] when $M_n$ is a martingale, powering [[Thm - Doob's Maximal Inequality|Doob's inequalities]]; the **$L^p$-contraction** $\|\mathbb{E}[X\mid\mathcal{G}]\|_p\le\|X\|_p$ gives the uniform integrability of conditional expectations.

---

# Formal Statement

Let $X,Y\in L^1$, $\alpha,\beta\in\mathbb{R}$, $\mathcal{H}\subseteq\mathcal{G}$. All identities hold $\mathbb{P}$-a.s.

1. **(Linearity)** $\mathbb{E}[\alpha X+\beta Y\mid\mathcal{G}]=\alpha\,\mathbb{E}[X\mid\mathcal{G}]+\beta\,\mathbb{E}[Y\mid\mathcal{G}]$.
2. **(Tower / iterated conditioning)** $\mathbb{E}\big[\mathbb{E}[X\mid\mathcal{G}]\mid\mathcal{H}\big]=\mathbb{E}[X\mid\mathcal{H}]$; in particular $\mathbb{E}\big[\mathbb{E}[X\mid\mathcal{G}]\big]=\mathbb{E}[X]$.
3. **(Taking out what is known)** If $Z$ is $\mathcal{G}$-measurable and bounded (or $ZX\in L^1$), $\mathbb{E}[ZX\mid\mathcal{G}]=Z\,\mathbb{E}[X\mid\mathcal{G}]$; in particular if $X$ is $\mathcal{G}$-measurable, $\mathbb{E}[X\mid\mathcal{G}]=X$.
4. **(Positivity / monotonicity)** $X\ge0\Rightarrow\mathbb{E}[X\mid\mathcal{G}]\ge0$; $X\le Y\Rightarrow\mathbb{E}[X\mid\mathcal{G}]\le\mathbb{E}[Y\mid\mathcal{G}]$.
5. **(Independence)** If $X$ is independent of $\mathcal{G}$, $\mathbb{E}[X\mid\mathcal{G}]=\mathbb{E}[X]$.
6. **(Conditional MCT / Fatou / DCT)** the convergence theorems hold for $\mathbb{E}[\cdot\mid\mathcal{G}]$.
7. **(Conditional Jensen)** for convex $\varphi$, $\mathbb{E}[\varphi(X)\mid\mathcal{G}]\ge\varphi(\mathbb{E}[X\mid\mathcal{G}])$; hence the **$L^p$-contraction** $\|\mathbb{E}[X\mid\mathcal{G}]\|_p\le\|X\|_p$ for $p\ge1$.

---

# Why Is It True

Every identity is proved by the **uniqueness recipe**: to show "$\mathbb{E}[\cdots\mid\mathcal{G}]=W$", check that $W$ is $\mathcal{G}$-measurable and that $\mathbb{E}[W\mathbf{1}_A]=\mathbb{E}[(\cdots)\mathbf{1}_A]$ for all $A\in\mathcal{G}$; [[Thm - Existence and Uniqueness of Conditional Expectation|uniqueness]] then forces equality. The art is only in checking the averaging identity.

**Linearity, positivity** — both characterising properties pass through sums and through "$\ge0$" trivially (positivity by the uniqueness Lemma's sign argument).

**Tower property** — the heart. To show $\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]\mid\mathcal{H}]=\mathbb{E}[X\mid\mathcal{H}]$: the right side is $\mathcal{H}$-measurable; for $A\in\mathcal{H}$, since $\mathcal{H}\subseteq\mathcal{G}$, $A\in\mathcal{G}$ too, so $\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]\mathbf{1}_A]=\mathbb{E}[X\mathbf{1}_A]=\mathbb{E}[\mathbb{E}[X\mid\mathcal{H}]\mathbf{1}_A]$ — the middle equality is the defining identity of $\mathbb{E}[X\mid\mathcal{G}]$ *used on an $\mathcal{H}$-set, legal because $\mathcal{H}$-sets are $\mathcal{G}$-sets*. The slogan: **averaging over more information ($\mathcal{G}$) and then over less ($\mathcal{H}$) is the same as averaging over less directly — the finer average is invisible to the coarser one.**

**Taking out what is known** — verify $Z\,\mathbb{E}[X\mid\mathcal{G}]$ satisfies the characterisation of $\mathbb{E}[ZX\mid\mathcal{G}]$. It is $\mathcal{G}$-measurable (product of $\mathcal{G}$-measurables); for the averaging identity, the standard machine — true for $Z=\mathbf{1}_B$ ($B\in\mathcal{G}$): $\mathbb{E}[Z\,\mathbb{E}[X\mid\mathcal{G}]\mathbf{1}_A]=\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]\mathbf{1}_{A\cap B}]=\mathbb{E}[X\mathbf{1}_{A\cap B}]=\mathbb{E}[ZX\mathbf{1}_A]$ — then extend to simple, then bounded $Z$. The intuition: a $\mathcal{G}$-measurable $Z$ is "already known" once $\mathcal{G}$ is given, hence behaves as a constant under $\mathbb{E}[\cdot\mid\mathcal{G}]$.

**Independence** — if $X\perp\mathcal{G}$, the constant $\mathbb{E}[X]$ is $\mathcal{G}$-measurable and $\mathbb{E}[\mathbb{E}[X]\mathbf{1}_A]=\mathbb{E}[X]\mathbb{P}(A)=\mathbb{E}[X\mathbf{1}_A]$ (independence), so by uniqueness $\mathbb{E}[X\mid\mathcal{G}]=\mathbb{E}[X]$.

**Conditional Jensen** — the [[Thm - Jensen's Inequality|supporting-line]] proof, conditionalised: $\varphi(x)\ge\varphi(m)+c(x-m)$ at $m=\mathbb{E}[X\mid\mathcal{G}]$ (now a random tangent point); substitute $X$, apply $\mathbb{E}[\cdot\mid\mathcal{G}]$ using linearity, positivity, and taking-out-what-is-known (the slope $c$ and tangent point $m$ are $\mathcal{G}$-measurable). The $L^p$-contraction is conditional Jensen with $\varphi(x)=|x|^p$ followed by an unconditional expectation.

---

# What Makes This Hard

No single step is deep; the difficulty is *bookkeeping* and seeing that **one method — verify the two characterising properties, invoke uniqueness — proves everything**. The genuinely conditional facts, with no unconditional shadow, are the tower property and taking-out-what-is-known; the subtle point in each is that an $\mathcal{H}$-set *is* a $\mathcal{G}$-set ($\mathcal{H}\subseteq\mathcal{G}$), resp. that a $\mathcal{G}$-measurable factor acts as a constant. Conditional Jensen's subtlety: the supporting-line tangent point $\mathbb{E}[X\mid\mathcal{G}]$ is now *random*, so the slope $c$ must be chosen $\mathcal{G}$-measurably.

---

# Rederivation Scaffold

**High-level strategy.** For each property, write down the candidate $W$, check $W$ is $\mathcal{G}$-measurable and $\mathbb{E}[W\mathbf{1}_A]=\mathbb{E}[(\text{target})\mathbf{1}_A]$ for $A\in\mathcal{G}$; conclude by [[Thm - Existence and Uniqueness of Conditional Expectation|uniqueness]].

**Subgoal decomposition.**

1. **Linearity, positivity.** Both characterising properties are linear / sign-preserving.
2. **Tower.** $A\in\mathcal{H}\Rightarrow A\in\mathcal{G}$; apply the $\mathcal{G}$-defining identity on $A$.
3. **Taking out what is known.** Standard machine in $Z$: indicators, simple, bounded.
4. **Independence.** The constant $\mathbb{E}[X]$ passes the characterisation, using $\mathbb{E}[X\mathbf{1}_A]=\mathbb{E}[X]\mathbb{P}(A)$.
5. **Conditional Jensen.** Supporting line at the random point $\mathbb{E}[X\mid\mathcal{G}]$, $\mathcal{G}$-measurable slope; apply $\mathbb{E}[\cdot\mid\mathcal{G}]$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Tower property
> **Statement:** $\mathcal{H}\subseteq\mathcal{G}\Rightarrow\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]\mid\mathcal{H}]=\mathbb{E}[X\mid\mathcal{H}]$.
>
> > [!note]- Full proof
> > $\mathbb{E}[X\mid\mathcal{H}]$ is $\mathcal{H}$-measurable. For $A\in\mathcal{H}$: since $\mathcal{H}\subseteq\mathcal{G}$, $A\in\mathcal{G}$, so $\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]\mathbf{1}_A]=\mathbb{E}[X\mathbf{1}_A]$ (defining identity of $\mathbb{E}[X\mid\mathcal{G}]$) $=\mathbb{E}[\mathbb{E}[X\mid\mathcal{H}]\mathbf{1}_A]$ (defining identity of $\mathbb{E}[X\mid\mathcal{H}]$). So $\mathbb{E}[X\mid\mathcal{H}]$ satisfies the characterisation of $\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]\mid\mathcal{H}]$; uniqueness finishes. $\square$

> [!note]- Lemma 2: Taking out what is known
> **Statement:** $Z$ bounded $\mathcal{G}$-measurable $\Rightarrow\mathbb{E}[ZX\mid\mathcal{G}]=Z\,\mathbb{E}[X\mid\mathcal{G}]$.
>
> > [!note]- Full proof
> > $Z\,\mathbb{E}[X\mid\mathcal{G}]$ is $\mathcal{G}$-measurable. For $Z=\mathbf{1}_B$, $B\in\mathcal{G}$, and any $A\in\mathcal{G}$: $\mathbb{E}[Z\,\mathbb{E}[X\mid\mathcal{G}]\mathbf{1}_A]=\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]\mathbf{1}_{A\cap B}]=\mathbb{E}[X\mathbf{1}_{A\cap B}]=\mathbb{E}[ZX\mathbf{1}_A]$. Extend to simple $Z$ by linearity, to bounded $Z$ by approximation. Uniqueness gives the identity. $\square$

> [!note]- Lemma 3: Conditional Jensen
> **Statement:** $\varphi$ convex $\Rightarrow\mathbb{E}[\varphi(X)\mid\mathcal{G}]\ge\varphi(\mathbb{E}[X\mid\mathcal{G}])$.
>
> > [!note]- Full proof
> > Write $\varphi=\sup_n\ell_n$ over countably many affine $\ell_n(x)=a_nx+b_n$ (a convex function is the sup of its rational supporting lines). For each $n$, $\varphi(X)\ge\ell_n(X)$, so by positivity and linearity $\mathbb{E}[\varphi(X)\mid\mathcal{G}]\ge\mathbb{E}[\ell_n(X)\mid\mathcal{G}]=a_n\mathbb{E}[X\mid\mathcal{G}]+b_n=\ell_n(\mathbb{E}[X\mid\mathcal{G}])$. Take the sup over $n$: $\mathbb{E}[\varphi(X)\mid\mathcal{G}]\ge\sup_n\ell_n(\mathbb{E}[X\mid\mathcal{G}])=\varphi(\mathbb{E}[X\mid\mathcal{G}])$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Linearity and positivity are immediate from the characterising properties. Lemmas 1–3 give the tower property, taking-out-what-is-known, and conditional Jensen. Independence: $\mathbb{E}[X]$ is $\mathcal{G}$-measurable and $\mathbb{E}[\mathbb{E}[X]\mathbf{1}_A]=\mathbb{E}[X]\mathbb{P}(A)=\mathbb{E}[X\mathbf{1}_A]$ for $A\in\mathcal{G}$ (independence). The conditional convergence theorems follow from positivity by the same arguments as their unconditional versions. The $L^p$-contraction is conditional Jensen with $\varphi=|\cdot|^p$, then $\mathbb{E}[\cdot]$ and the tower property. $\blacksquare$

---

# Cross-Field Exercise Suggestions

The **tower property** is the definition of a [[Def - Martingale|martingale]] ($\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=X_n$) and proves the [[Thm - Strong Law of Large Numbers|SLLN]] via backward martingales. **Conditional Jensen** makes $(|M_n|^p)$ a [[Def - Submartingale|submartingale]] for a martingale $M$ — the input to [[Thm - Doob's Maximal Inequality|Doob's $L^p$ inequality]]. **Taking out what is known** is the rule behind the optional-stopping and predictable-projection calculus.

---

# Bridges

- **[[Thm - Existence and Uniqueness of Conditional Expectation]]** — supplies the characterisation and the uniqueness lemma every proof here invokes.
- **[[Thm - Jensen's Inequality]]** — conditional Jensen is its conditionalisation, same supporting-line idea.
- **[[Def - Martingale]]** *(AP IV)* — the tower property *is* the martingale property.
