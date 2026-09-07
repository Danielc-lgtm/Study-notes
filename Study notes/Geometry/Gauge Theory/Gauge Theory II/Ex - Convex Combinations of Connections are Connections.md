---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Connection on a Vector Bundle"
tags: [geometry, gauge-theory, connections]
---

# Problem Statement

Let $E \to M$ be a smooth real [[Def - Vector Bundle|vector bundle]] over a manifold $M$.

**Part 1 (convex combinations).** Let $\nabla$ and $\hat\nabla$ be two [[Def - Connection on a Vector Bundle|connections]] on $E$, and let $t \in [0, 1]$. Prove that the affine combination
$$
\nabla' := t\nabla + (1 - t)\hat\nabla, \qquad \nabla' s := t\,\nabla s + (1 - t)\,\hat\nabla s,
$$
is again a connection on $E$. More generally, show that for real constants $\lambda_1, \dots, \lambda_N$ the combination $\sum_{\alpha=1}^N \lambda_\alpha \nabla_\alpha$ of connections $\nabla_1, \dots, \nabla_N$ is a connection **if and only if** $\sum_\alpha \lambda_\alpha = 1$.

**Part 2 (gluing with a partition of unity).** Let $\{U_\alpha\}_{\alpha \in I}$ be an open cover of $M$, let $\nabla_\alpha$ be a connection on $E|_{U_\alpha}$ for each $\alpha$, and let $\{\rho_\alpha\}_{\alpha \in I}$ be a smooth [[Thm - Existence of Smooth Partitions of Unity|partition of unity]] subordinate to the cover, so that $\operatorname{supp}\rho_\alpha \subseteq U_\alpha$, the family $\{\operatorname{supp}\rho_\alpha\}$ is locally finite, $0 \le \rho_\alpha \le 1$, and $\sum_\alpha \rho_\alpha \equiv 1$. Prove that
$$
\nabla s := \sum_{\alpha \in I} \rho_\alpha\,\nabla_\alpha\big(s|_{U_\alpha}\big),
$$
each summand extended by zero outside $\operatorname{supp}\rho_\alpha$, is a globally well-defined connection on $E$. This is the gluing step in the proof that connections exist ([[Thm - The Space of Connections is an Affine Space|the affine-space theorem]], part (a)).

**Recall:**

![[Def - Connection on a Vector Bundle#The Definition]]

The two axioms are $\mathbb{R}$-linearity, $\nabla(a s + b u) = a\,\nabla s + b\,\nabla u$ for constants $a, b \in \mathbb{R}$, and the Leibniz rule $\nabla(fs) = df \otimes s + f\,\nabla s$ for $f \in C^\infty(M)$ and $s \in \Gamma(E)$. Both connections land in the same target $\Omega^1(M; E) = \Gamma(T^*M \otimes E)$, [[Def - Bundle-Valued Differential Forms|the space of $E$-valued $1$-forms]], so an affine combination of their outputs is again an element of that vector space.

A smooth [[Thm - Existence of Smooth Partitions of Unity|partition of unity]] subordinate to $\{U_\alpha\}$ is a family $\{\rho_\alpha\}$ of smooth functions $\rho_\alpha \colon M \to [0,1]$ with $\operatorname{supp}\rho_\alpha \subseteq U_\alpha$, with $\{\operatorname{supp}\rho_\alpha\}$ locally finite (every point has a neighbourhood meeting only finitely many of the supports), and with $\sum_\alpha \rho_\alpha = 1$ pointwise; such partitions exist for any open cover of a manifold.

---

# Convergent Strategy

**Problem class.** This is a *verify-this-is-a-connection* problem, the most basic task on a definition page: an operator is proposed and one checks the two axioms. What lifts it slightly above pure routine is the *if and only if* in Part 1 — the necessity of $\sum_\alpha \lambda_\alpha = 1$ is the conceptual heart, because it isolates why connections form an *affine* rather than a *linear* space. Part 2 is the same computation upgraded to smooth-function coefficients, together with a Step-0 check that the infinite sum and the extension-by-zero make sense.

**Assumption pattern.** In Part 1 the coefficients are *constants*; in Part 2 they are the *functions* $\rho_\alpha$ summing to $1$. The single fact that both halves turn on is that the Leibniz rule is an *inhomogeneous linear* condition: its right-hand side $df \otimes s + f\nabla s$ has a term, $df \otimes s$, that does not involve $\nabla$ at all. When one forms a combination $\sum_\alpha \lambda_\alpha \nabla_\alpha$, this inhomogeneous term is reproduced with total weight $\sum_\alpha \lambda_\alpha$, so the combination satisfies the Leibniz rule exactly when that weight is $1$.

**Theorem routing.** No named theorem is needed for the algebra; the route is a direct check of [[Def - Connection on a Vector Bundle|the connection axioms]]. Part 2 additionally invokes the *existence* and defining properties of a subordinate [[Thm - Existence of Smooth Partitions of Unity|partition of unity]] to justify that the sum is locally finite and that each $\rho_\alpha \nabla_\alpha(s|_{U_\alpha})$ extends smoothly by zero to all of $M$.

**Key decision point.** The one idea to hold onto is that the constant $1$ in "$\sum \lambda_\alpha = 1$" is not decorative: it is the exact bookkeeping weight of the $df \otimes s$ term. Everything else — $\mathbb{R}$-linearity, the homogeneous $f\nabla s$ term — passes through any real combination unchanged; only the inhomogeneous term imposes a constraint, and it imposes precisely one scalar equation, $\sum_\alpha \lambda_\alpha = 1$. Recognising that a single normalisation controls the whole matter is what makes both parts one-line computations.

---

# Legal Operations Used

The topic page for this chapter is written after its subpages, so the operations below are named descriptively; the orchestrator reconciles them with the numbered Legal Operations of the chapter's topic page.

1. **Form an affine combination of connections** (the operation "combine solutions of the Leibniz rule with weights summing to one"). This is the operation the exercise both uses and justifies: because the Leibniz rule is inhomogeneous-linear, its solution set is closed under affine combinations, and this is the algebraic engine behind the affine-space structure of $\mathcal{A}(E)$.

2. **Glue local objects with a partition of unity** (the operation "sew locally defined structures into a global one using $\{\rho_\alpha\}$ with $\sum \rho_\alpha = 1$"). Part 2 is a direct instance, structurally identical to the standard existence proof for Riemannian metrics, where local inner products are averaged into a global one by the same device; here local connections are averaged into a global connection.

3. **Extend by zero across the support boundary** (the operation "multiply by a bump/partition function to make a locally defined section globally smooth"). Each $\rho_\alpha \nabla_\alpha(s|_{U_\alpha})$, a priori defined only on $U_\alpha$, is turned into a global smooth $E$-valued $1$-form because $\rho_\alpha$ vanishes on a neighbourhood of $M \setminus U_\alpha$.

---

# Hints

> [!note]- Hint 1
> Both connections output into the same vector space $\Omega^1(M; E)$, so a linear combination of $\nabla s$ and $\hat\nabla s$ makes sense and is again an $E$-valued $1$-form. Just write out what $\nabla'(fs)$ is by applying the Leibniz rule to each of $\nabla$ and $\hat\nabla$ separately, and collect the $df \otimes s$ terms.

> [!note]- Hint 2
> When you collect the inhomogeneous terms in $\nabla'(fs) = t(df \otimes s + f\nabla s) + (1-t)(df \otimes s + f\hat\nabla s)$, the coefficient of $df \otimes s$ is $t + (1 - t)$. For $\nabla'$ to satisfy the Leibniz rule this coefficient must equal exactly $1$. That is where $t + (1 - t) = 1$, and in general $\sum_\alpha \lambda_\alpha = 1$, is forced.

> [!note]- Hint 3
> For the *necessity* half of the general statement, suppose $\nabla_{\text{comb}} = \sum_\alpha \lambda_\alpha \nabla_\alpha$ satisfies the Leibniz rule and compute $\nabla_{\text{comb}}(fs)$ two ways. Matching the $df \otimes s$ terms forces $\big(\sum_\alpha \lambda_\alpha\big)\,df \otimes s = df \otimes s$ for all $f, s$; choosing $f, s$ with $df \otimes s \neq 0$ somewhere gives $\sum_\alpha \lambda_\alpha = 1$.

> [!note]- Hint 4
> For Part 2, first handle well-definedness: local finiteness makes the sum finite near each point, and $\operatorname{supp}\rho_\alpha \subseteq U_\alpha$ lets you extend each term by zero. Then repeat the Part 1 computation with $\lambda_\alpha = \rho_\alpha(m)$ *functions*, using $\sum_\alpha \rho_\alpha = 1$ at the end. Note $\rho_\alpha$ is a scalar function, so $\rho_\alpha \nabla_\alpha$ is still $\mathbb{R}$-linear.

---

# Solution

The plan is to verify the two connection axioms for the affine combination directly (Steps 1 and 2), then extract the necessity of the normalisation from the Leibniz computation (Step 3), and finally repeat the argument with partition-of-unity coefficients after a well-definedness check (Steps 4 and 5). The whole exercise turns on one observation, made in Step 2: the inhomogeneous $df \otimes s$ term of the Leibniz rule is reproduced with total weight equal to the sum of the coefficients, so that sum must be $1$.

**Step 1: The convex combination is $\mathbb{R}$-linear.**

A real combination of $\mathbb{R}$-linear maps is $\mathbb{R}$-linear, so $\nabla' = t\nabla + (1-t)\hat\nabla$ is $\mathbb{R}$-linear regardless of the value of $t$.

> [!note]- Derivation
> Let $s, u \in \Gamma(E)$ and $a, b \in \mathbb{R}$. Using that $\nabla$ and $\hat\nabla$ are each $\mathbb{R}$-linear,
> $$
> \nabla'(as + bu) = t\,\nabla(as + bu) + (1-t)\,\hat\nabla(as + bu) \qquad \text{(definition of } \nabla'\text{)}
> $$
> $$
> = t\big(a\,\nabla s + b\,\nabla u\big) + (1-t)\big(a\,\hat\nabla s + b\,\hat\nabla u\big) \qquad \text{(} \mathbb{R}\text{-linearity of } \nabla \text{ and of } \hat\nabla\text{)}
> $$
> $$
> = a\big(t\,\nabla s + (1-t)\,\hat\nabla s\big) + b\big(t\,\nabla u + (1-t)\,\hat\nabla u\big) = a\,\nabla' s + b\,\nabla' u \qquad \text{(regrouping by } a, b\text{; definition of } \nabla'\text{).}
> $$
> Hence $\nabla'$ is $\mathbb{R}$-linear. This step used nothing about the value of $t$; it holds for any real coefficients.

**Step 2: The convex combination satisfies the Leibniz rule.**

Applying the Leibniz rule to each of $\nabla$ and $\hat\nabla$ and collecting terms, the inhomogeneous $df \otimes s$ term comes out with coefficient $t + (1 - t) = 1$, so $\nabla'$ obeys the Leibniz rule.

> [!note]- Derivation
> Let $f \in C^\infty(M)$ and $s \in \Gamma(E)$. Apply the definition of $\nabla'$, then the Leibniz rule for $\nabla$ and for $\hat\nabla$:
> $$
> \nabla'(fs) = t\,\nabla(fs) + (1-t)\,\hat\nabla(fs) \qquad \text{(definition of } \nabla'\text{)}
> $$
> $$
> = t\big(df \otimes s + f\,\nabla s\big) + (1-t)\big(df \otimes s + f\,\hat\nabla s\big) \qquad \text{(Leibniz rule for } \nabla\text{, and for } \hat\nabla\text{).}
> $$
> Separate the inhomogeneous terms (those with $df \otimes s$) from the homogeneous terms:
> $$
> = \big(t + (1 - t)\big)\,df \otimes s + f\big(t\,\nabla s + (1-t)\,\hat\nabla s\big) \qquad \text{(grouping the two } df \otimes s \text{ terms; factoring } f \text{ out of the rest).}
> $$
> Now $t + (1 - t) = 1$, and $t\,\nabla s + (1-t)\,\hat\nabla s = \nabla' s$ by definition, so
> $$
> \nabla'(fs) = df \otimes s + f\,\nabla' s.
> $$
> This is exactly the Leibniz rule for $\nabla'$. Together with Step 1, both axioms of [[Def - Connection on a Vector Bundle|a connection]] hold, so $\nabla' = t\nabla + (1-t)\hat\nabla$ is a connection. The coefficient of $df \otimes s$ came out right *because* the weights $t$ and $1 - t$ sum to $1$.

**Step 3: Sufficiency and necessity of $\sum_\alpha \lambda_\alpha = 1$ for a general combination.**

The same computation with $N$ connections shows that $\sum_\alpha \lambda_\alpha \nabla_\alpha$ satisfies the Leibniz rule if and only if $\sum_\alpha \lambda_\alpha = 1$; $\mathbb{R}$-linearity holds unconditionally.

> [!note]- Derivation
> Let $\nabla_1, \dots, \nabla_N$ be connections on $E$ and $\lambda_1, \dots, \lambda_N \in \mathbb{R}$, and set $L := \sum_\alpha \lambda_\alpha$ and $\nabla_{\text{comb}} := \sum_\alpha \lambda_\alpha \nabla_\alpha$.
>
> **$\mathbb{R}$-linearity** holds for any $\lambda_\alpha$, by the same argument as Step 1: a real combination of $\mathbb{R}$-linear maps is $\mathbb{R}$-linear.
>
> **Leibniz computation.** For $f \in C^\infty(M)$, $s \in \Gamma(E)$,
> $$
> \nabla_{\text{comb}}(fs) = \sum_{\alpha=1}^N \lambda_\alpha\,\nabla_\alpha(fs) = \sum_{\alpha=1}^N \lambda_\alpha\big(df \otimes s + f\,\nabla_\alpha s\big) \qquad \text{(Leibniz rule for each } \nabla_\alpha\text{)}
> $$
> $$
> = \Big(\sum_{\alpha=1}^N \lambda_\alpha\Big)\,df \otimes s + f\sum_{\alpha=1}^N \lambda_\alpha\,\nabla_\alpha s = L\,\big(df \otimes s\big) + f\,\nabla_{\text{comb}} s \qquad \text{(separating inhomogeneous from homogeneous terms; } L = \textstyle\sum_\alpha \lambda_\alpha\text{).}
> $$
>
> **Sufficiency.** If $L = 1$, this reads $\nabla_{\text{comb}}(fs) = df \otimes s + f\,\nabla_{\text{comb}}s$, the Leibniz rule, so $\nabla_{\text{comb}}$ is a connection.
>
> **Necessity.** Conversely, suppose $\nabla_{\text{comb}}$ is a connection, so it satisfies $\nabla_{\text{comb}}(fs) = df \otimes s + f\,\nabla_{\text{comb}}s$. Comparing with the computed value $L\,(df \otimes s) + f\,\nabla_{\text{comb}}s$ and cancelling the common homogeneous term $f\,\nabla_{\text{comb}}s$, we get
> $$
> (L - 1)\,df \otimes s = 0 \qquad \text{for all } f \in C^\infty(M),\ s \in \Gamma(E).
> $$
> Choose any point $m \in M$, a function $f$ with $d f_m \neq 0$ (for instance a local coordinate function multiplied by a bump function, which has nonzero differential at $m$), and a section $s$ with $s(m) \neq 0$; then $(df \otimes s)(m) = df_m \otimes s(m) \neq 0$ in $T^*_mM \otimes E_m$. The identity $(L-1)\,df \otimes s = 0$ therefore forces the scalar $L - 1 = 0$, that is, $L = \sum_\alpha \lambda_\alpha = 1$. This is the contradiction that would arise from $L \neq 1$: a nonzero multiple of a nonzero element would have to vanish. Hence $\sum_\alpha \lambda_\alpha = 1$ is necessary as well as sufficient.

**Step 4: The partition-of-unity sum is well-defined and globally smooth.**

Local finiteness makes the sum finite in a neighbourhood of each point, and $\operatorname{supp}\rho_\alpha \subseteq U_\alpha$ lets each term be extended by zero to a global smooth $E$-valued $1$-form; hence $\nabla s \in \Omega^1(M; E)$.

> [!note]- Derivation
> Fix $s \in \Gamma(E)$ and $\alpha \in I$. The section $s|_{U_\alpha}$ lies in $\Gamma(U_\alpha; E)$, so $\nabla_\alpha(s|_{U_\alpha}) \in \Omega^1(U_\alpha; E)$, and the product $\rho_\alpha\,\nabla_\alpha(s|_{U_\alpha})$ is an $E$-valued $1$-form on $U_\alpha$.
>
> **Extension by zero.** The support $\operatorname{supp}\rho_\alpha$ is, by hypothesis, a closed subset of $M$ contained in $U_\alpha$. On the open set $U_\alpha \setminus \operatorname{supp}\rho_\alpha$ the function $\rho_\alpha$ vanishes identically, so $\rho_\alpha\,\nabla_\alpha(s|_{U_\alpha})$ vanishes there. Define its extension $\eta_\alpha$ to $M$ by
> $$
> \eta_\alpha(m) := \begin{cases} \rho_\alpha(m)\,\nabla_\alpha(s|_{U_\alpha})(m), & m \in U_\alpha, \\[2pt] 0, & m \in M \setminus \operatorname{supp}\rho_\alpha. \end{cases}
> $$
> These two prescriptions agree on the overlap $U_\alpha \setminus \operatorname{supp}\rho_\alpha$ (both give $0$), and the two open sets $U_\alpha$ and $M \setminus \operatorname{supp}\rho_\alpha$ cover $M$ (any point not in the closed set $\operatorname{supp}\rho_\alpha \subseteq U_\alpha$ is in the second set; any point in $\operatorname{supp}\rho_\alpha$ is in $U_\alpha$). A form defined smoothly on each set of an open cover and agreeing on overlaps is a smooth form, so $\eta_\alpha \in \Omega^1(M; E)$.
>
> **The sum is locally finite.** The family $\{\operatorname{supp}\rho_\alpha\}$ is locally finite, so each $m \in M$ has a neighbourhood $V$ meeting only finitely many supports; on $V$ all but finitely many $\eta_\alpha$ vanish, so $\sum_\alpha \eta_\alpha$ is a *finite* sum near every point and defines a smooth form $\nabla s := \sum_\alpha \eta_\alpha \in \Omega^1(M; E)$. Thus $\nabla \colon \Gamma(E) \to \Omega^1(M; E)$ is a well-defined map of the correct type. In what follows we suppress the extension-by-zero and write $\rho_\alpha\,\nabla_\alpha(s|_{U_\alpha})$ for $\eta_\alpha$, understanding all sums to be locally finite.

**Step 5: The partition-of-unity sum is a connection.**

With scalar-function coefficients $\rho_\alpha$, the map $\nabla$ is $\mathbb{R}$-linear, and the Leibniz computation reproduces the $df \otimes s$ term with total weight $\sum_\alpha \rho_\alpha = 1$, so $\nabla$ is a connection.

> [!note]- Derivation
> **$\mathbb{R}$-linearity.** For $a, b \in \mathbb{R}$ and $s, u \in \Gamma(E)$, restriction is linear and each $\nabla_\alpha$ is $\mathbb{R}$-linear, so $\nabla_\alpha\big((as + bu)|_{U_\alpha}\big) = a\,\nabla_\alpha(s|_{U_\alpha}) + b\,\nabla_\alpha(u|_{U_\alpha})$; multiplying by the scalar function $\rho_\alpha$ and summing preserves the combination, so $\nabla(as + bu) = a\,\nabla s + b\,\nabla u$.
>
> **Leibniz rule.** Let $f \in C^\infty(M)$ and $s \in \Gamma(E)$. Near any point only finitely many terms are nonzero, so we may compute termwise:
> $$
> \nabla(fs) = \sum_\alpha \rho_\alpha\,\nabla_\alpha\big((fs)|_{U_\alpha}\big) = \sum_\alpha \rho_\alpha\,\nabla_\alpha\big(f|_{U_\alpha}\cdot s|_{U_\alpha}\big) \qquad \text{(restriction commutes with multiplication)}
> $$
> $$
> = \sum_\alpha \rho_\alpha\Big(df|_{U_\alpha} \otimes s|_{U_\alpha} + f|_{U_\alpha}\,\nabla_\alpha(s|_{U_\alpha})\Big) \qquad \text{(Leibniz rule for each } \nabla_\alpha \text{ on } E|_{U_\alpha}\text{)}
> $$
> $$
> = \Big(\sum_\alpha \rho_\alpha\Big)\,df \otimes s + f\sum_\alpha \rho_\alpha\,\nabla_\alpha(s|_{U_\alpha}) \qquad \text{(pulling the globally defined } df \otimes s \text{ and } f \text{ out; each } \rho_\alpha \text{ is a scalar function).}
> $$
> Here $\rho_\alpha\,\big(df|_{U_\alpha} \otimes s|_{U_\alpha}\big)$ extends by zero to $\rho_\alpha\,(df \otimes s)$ on $M$ because $df \otimes s$ is globally defined and $\rho_\alpha$ is supported in $U_\alpha$. Finally use the defining property $\sum_\alpha \rho_\alpha = 1$ of the partition of unity:
> $$
> \nabla(fs) = 1 \cdot df \otimes s + f\,\nabla s = df \otimes s + f\,\nabla s.
> $$
> This is the Leibniz rule for $\nabla$. With $\mathbb{R}$-linearity, both axioms hold, so $\nabla = \sum_\alpha \rho_\alpha \nabla_\alpha$ is a connection on $E$. This is precisely the gluing step that, given local connections $\nabla_\alpha$ on trivialising sets, produces a global connection and thereby proves $\mathcal{A}(E) \neq \varnothing$ in [[Thm - The Space of Connections is an Affine Space|the affine-space theorem]]. $\blacksquare$

> [!note]- Complete formal solution
> **Part 1.** Let $\nabla, \hat\nabla$ be connections on $E$ and $t \in [0,1]$; set $\nabla' = t\nabla + (1-t)\hat\nabla$.
>
> *$\mathbb{R}$-linear:* for $a, b \in \mathbb{R}$, $\nabla'(as + bu) = t(a\nabla s + b\nabla u) + (1-t)(a\hat\nabla s + b\hat\nabla u) = a\nabla' s + b\nabla' u$, using the $\mathbb{R}$-linearity of $\nabla$ and $\hat\nabla$.
>
> *Leibniz:* for $f \in C^\infty(M)$,
> $$
> \nabla'(fs) = t(df \otimes s + f\nabla s) + (1-t)(df \otimes s + f\hat\nabla s) = (t + 1 - t)\,df \otimes s + f\,\nabla' s = df \otimes s + f\,\nabla' s.
> $$
> So $\nabla'$ is a connection.
>
> *General combination.* For $\nabla_{\text{comb}} = \sum_\alpha \lambda_\alpha \nabla_\alpha$ with $L = \sum_\alpha \lambda_\alpha$, the same computation gives $\nabla_{\text{comb}}(fs) = L\,df \otimes s + f\,\nabla_{\text{comb}}s$, and $\mathbb{R}$-linearity holds always. Thus $\nabla_{\text{comb}}$ is a connection iff $L\,df \otimes s = df \otimes s$ for all $f, s$; choosing $m$, $f$ with $df_m \neq 0$, and $s$ with $s(m) \neq 0$ makes $df \otimes s$ nonzero at $m$, forcing $L = 1$. Hence $\sum_\alpha \lambda_\alpha \nabla_\alpha$ is a connection if and only if $\sum_\alpha \lambda_\alpha = 1$.
>
> **Part 2.** Let $\{\rho_\alpha\}$ be a partition of unity subordinate to $\{U_\alpha\}$, with $\nabla_\alpha$ a connection on $E|_{U_\alpha}$; set $\nabla s = \sum_\alpha \rho_\alpha \nabla_\alpha(s|_{U_\alpha})$.
>
> *Well-defined:* each $\rho_\alpha \nabla_\alpha(s|_{U_\alpha})$ extends smoothly by zero to $M$, since $\rho_\alpha$ vanishes on the open set $U_\alpha \setminus \operatorname{supp}\rho_\alpha$ and $\{U_\alpha,\ M \setminus \operatorname{supp}\rho_\alpha\}$ covers $M$; the sum is locally finite by local finiteness of $\{\operatorname{supp}\rho_\alpha\}$, so $\nabla s \in \Omega^1(M; E)$.
>
> *$\mathbb{R}$-linear:* immediate from the $\mathbb{R}$-linearity of each $\nabla_\alpha$ and of restriction, multiplied by the scalar functions $\rho_\alpha$.
>
> *Leibniz:* computing termwise (a finite sum near each point),
> $$
> \nabla(fs) = \sum_\alpha \rho_\alpha\big(df \otimes s + f\nabla_\alpha(s|_{U_\alpha})\big) = \Big(\sum_\alpha \rho_\alpha\Big) df \otimes s + f\,\nabla s = df \otimes s + f\,\nabla s,
> $$
> using $\sum_\alpha \rho_\alpha = 1$. Hence $\nabla$ is a connection on $E$, which is the existence step of the affine-space theorem. $\blacksquare$

> [!warning] Illegal but tempting: adding two connections
> It is tempting to think that if $\nabla$ and $\hat\nabla$ are connections then so is their sum $\nabla + \hat\nabla$, or a scalar multiple $2\nabla$. Neither is a connection: for the sum, $\big(\nabla + \hat\nabla\big)(fs) = 2\,df \otimes s + f(\nabla + \hat\nabla)s$, whose inhomogeneous term has weight $2 \neq 1$; for $2\nabla$, the weight is $2$ as well. The space of connections is *affine*, not linear — it has no distinguished zero and is not closed under addition or scalar multiplication, only under affine combinations $\sum_\alpha \lambda_\alpha \nabla_\alpha$ with $\sum_\alpha \lambda_\alpha = 1$. The extra condition that makes a linear combination legal is exactly that its coefficients sum to $1$; what *is* closed under all linear combinations is the *difference* space $\Omega^1(M; \operatorname{End} E)$ of $E$-valued endomorphism $1$-forms, the model vector space over which $\mathcal{A}(E)$ is an affine space.

---

# Key Takeaways

**The space of connections is affine because the Leibniz rule is inhomogeneous-linear.** A connection is a solution of the equation $\nabla(fs) - f\nabla s = df \otimes s$, and the right-hand side does not depend on $\nabla$. This is the defining shape of an *inhomogeneous linear* condition, and the solution set of such a condition is an affine space: it is a translate of the solution set of the associated *homogeneous* equation $A(fs) = fA(s)$, whose solutions are the $C^\infty$-linear maps, i.e. the tensors $\Omega^1(M; \operatorname{End} E)$. Concretely, an affine combination $\sum_\alpha \lambda_\alpha \nabla_\alpha$ solves the inhomogeneous equation precisely when the weights reproduce the inhomogeneous term once, which is the single scalar constraint $\sum_\alpha \lambda_\alpha = 1$. The reusable diagnostic is to look at any "derivative-like" operator's failure of $C^\infty$-linearity: if the failure is a *fixed* expression independent of the operator (here $df \otimes s$), the operators form an affine space and one manipulates them by weighted averages summing to one, never by unrestricted linear combination. This same pattern governs affine connections on principal bundles, splittings of an exact sequence, and lifts of a fixed map — all affine spaces for the same reason.

**Partition-of-unity gluing is weighted averaging, and it works because the weights sum to one.** The construction $\nabla = \sum_\alpha \rho_\alpha \nabla_\alpha$ is the universal device for manufacturing a global geometric object from local ones on a manifold, and it succeeds exactly when the object in question is preserved by convex (or more generally affine, weight-one) combinations. Connections qualify, as do Riemannian metrics (where $\sum_\alpha \rho_\alpha g_\alpha$ is again positive-definite because a convex combination of inner products is an inner product), volume forms up to normalisation, and any structure defined by an affine-linear condition. The trigger for reaching for this tool is "local existence is easy, global existence is wanted", and the routine has three moving parts: local objects on a cover, a subordinate partition of unity from [[Thm - Existence of Smooth Partitions of Unity|its existence theorem]], and a check that the structure survives weighted averaging with weights summing to one. The extension-by-zero and local-finiteness bookkeeping of Step 4 is the same in every instance and can be quoted rather than re-derived once understood. The place it *fails* is instructive: it fails for structures preserved only under a nonlinear operation, such as flatness of a connection or the property of being torsion-free-and-metric simultaneously, which is why the Levi-Civita connection is *not* built by gluing arbitrary local metric connections.

**Necessity proofs against a tensor identity are won by evaluating at a point.** The necessity half of Part 1 — that $\sum_\alpha \lambda_\alpha = 1$ is forced — is a small instance of a widely reusable move: to show a scalar $c$ appearing in an identity $c \cdot \omega = \omega$ (with $\omega$ a form or tensor field that is not identically zero) must equal $1$, exhibit a single point and a single choice of the free data making $\omega$ nonzero there, and read off $c = 1$ from the fibre, where everything is honest linear algebra. Here the free data are a function $f$ with nonvanishing differential and a section $s$ nonvanishing at the chosen point, which together make $df \otimes s$ a nonzero element of $T^*_mM \otimes E_m$; a nonzero multiple of a nonzero vector cannot vanish, so the multiplier is pinned. This "test against a well-chosen point and datum" tactic recurs throughout the subject — in showing curvature is nonzero by finding a section it moves, in showing a form is nonvanishing by pairing it with a cycle, and in every uniqueness argument that reduces a global tensor equation to pointwise linear algebra.
