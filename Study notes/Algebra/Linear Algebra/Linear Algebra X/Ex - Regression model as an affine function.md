---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Affine and Linear Functions on Rn"
tags: [algebra, linear-algebra, applied, statistics]
---

# Problem Statement

A **regression model** is a function $\hat y : \mathbb R^n \to \mathbb R$ defined by
$$\hat y(x) = x^T \beta + v,$$
where $x$ is the **feature vector** (the input), $\beta \in \mathbb R^n$ is the **weight vector** (the slope), and $v \in \mathbb R$ is the **offset** or **intercept**.

Show that:
1. $\hat y(x)$ is an **affine function** of $x$, but is *not* a linear function when $v \neq 0$.
2. Identify the linear part and the offset explicitly.
3. Show how to re-express $\hat y$ as a single inner product $\tilde x^T \tilde \beta$ by augmenting the feature vector with a constant feature $1$, and identify $\tilde x, \tilde \beta$.

**Recall:**

A function $f : \mathbb R^n \to \mathbb R$ is **linear** if it satisfies
$$f(\alpha x + \beta y) = \alpha f(x) + \beta f(y) \quad \text{for all } x, y \in \mathbb R^n,\ \alpha, \beta \in \mathbb R.$$
By the [[Def - Affine and Linear Functions on Rn|representation theorem for linear functions]], every linear $f : \mathbb R^n \to \mathbb R$ has the form $f(x) = a^T x$ for a unique $a \in \mathbb R^n$.

A function $f : \mathbb R^n \to \mathbb R$ is **affine** if the same identity holds whenever $\alpha + \beta = 1$. Equivalently, $f$ is affine iff $f(x) = a^T x + b$ for a unique pair $(a, b)$. The constant $b = f(0)$ is the **offset**, and $a$ is the **linear part** (the gradient).

The simplest counterexample to "all affine functions are linear" is $f(x) = 1$ for $x \in \mathbb R$: this is affine with $a = 0$, $b = 1$, but $f(2x) = 1 \neq 2 = 2 f(x)$, so superposition fails.

---

# Convergent Strategy

**Problem class.** This is a *direct verification of the linear-vs-affine distinction*: given an explicit formula $\hat y(x) = x^T \beta + v$, check superposition by direct substitution. The Boyd-style applied-linear-algebra reader should be able to do this verification fluently — it is the foundational exercise that anchors the affine/linear taxonomy.

**Assumption pattern.** The formula $\hat y(x) = x^T \beta + v$ has two pieces — the inner product $x^T \beta$ (which is linear by [[Def - Affine and Linear Functions on Rn|the representation theorem]]) and the constant $v$. The presence of the constant term is the source of the affine-but-not-linear behaviour: removing it would give a linear function, but applied modelling needs the intercept.

**Theorem routing.** Two routes: (a) check superposition directly to confirm affine; check $\hat y(0) = v$ to confirm not linear (when $v \neq 0$); (b) apply the [[Def - Affine and Linear Functions on Rn|representation theorem for affine functions]], which says $\hat y(x) = a^T x + b$ uniquely with $a = $ gradient and $b = $ offset; identify $a = \beta$, $b = v$. Both routes give the same answer.

**Key decision point.** The standard trick for converting affine to linear is to **prepend a constant feature of $1$ to the input**, giving $\tilde x = (1, x) \in \mathbb R^{n+1}$ and $\tilde \beta = (v, \beta) \in \mathbb R^{n+1}$. The new function $\tilde y(\tilde x) = \tilde x^T \tilde \beta$ is genuinely linear in $\tilde x$. This is what statistical software does internally — the "constant feature" trick lets the same algorithm handle linear and affine models uniformly. Recognising this trick is the structural insight of the exercise.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra X — Applied I — Vectors, Distance, Equations, Dynamics#Legal Operations|the topic page's Legal Operations]]:

1. **Operation 2 (reduce a question to an inner product).** The original regression formula $x^T \beta + v$ has an inner product plus a scalar. After the homogenisation trick, the entire formula becomes a single inner product $\tilde x^T \tilde \beta$, exhibiting the affine function as "linear in the enlarged input".

2. **Operation 9 (diagnose by counting / type-classify).** The very first step of the exercise is to classify what kind of function $\hat y$ is: not linear (since $\hat y(0) = v \neq 0$ in general), but affine (since superposition holds with $\alpha + \beta = 1$). This classification dictates the route — apply the affine representation theorem and read off the data.

---

# Hints

> [!note]- Hint 1
> Apply the definition of affine: check $\hat y(\alpha x + \beta y) = \alpha \hat y(x) + \beta \hat y(y)$ when $\alpha + \beta = 1$, by direct substitution. Then check $\hat y(0)$ and see whether it is zero.

> [!note]- Hint 2
> For the linearity check, take $x = y = 0$ in the superposition identity. If $\hat y$ were linear, $\hat y(0) = 0$; the regression formula gives $\hat y(0) = v$. So if $v \neq 0$, the function is not linear.

> [!note]- Hint 3
> For the augmentation trick: write out $\tilde x^T \tilde \beta$ explicitly for $\tilde x = (1, x_1, x_2, \dots, x_n)$ and $\tilde \beta = (v, \beta_1, \beta_2, \dots, \beta_n)$, and check that it equals $v + \beta^T x = \hat y(x)$.

---

# Solution

The proof has three steps. Step 1 verifies that $\hat y$ is affine by direct superposition with $\alpha + \beta = 1$. Step 2 refutes linearity by computing $\hat y(0) = v \neq 0$. Step 3 applies the homogenisation trick, augmenting the input with a constant feature of $1$, to express $\hat y$ as a single inner product.

**Step 1: $\hat y$ is affine.**

Compute superposition with $\alpha + \beta = 1$.

> [!note]- Derivation
> For any $x, y \in \mathbb R^n$ and scalars $\alpha, \beta$ with $\alpha + \beta = 1$:
> $$\hat y(\alpha x + \beta y) = (\alpha x + \beta y)^T \beta_{\text{wt}} + v = \alpha x^T \beta_{\text{wt}} + \beta y^T \beta_{\text{wt}} + v,$$
> where I've written $\beta_{\text{wt}}$ for the weight vector to avoid confusion with the scalar $\beta$. The right side is
> $$\alpha (x^T \beta_{\text{wt}} + v) + \beta (y^T \beta_{\text{wt}} + v) = \alpha \hat y(x) + \beta \hat y(y),$$
> using $\alpha v + \beta v = (\alpha + \beta) v = v$ since $\alpha + \beta = 1$. So $\hat y(\alpha x + \beta y) = \alpha \hat y(x) + \beta \hat y(y)$, confirming affineness.

**Step 2: $\hat y$ is not linear (when $v \neq 0$).**

If $\hat y$ were linear, then $\hat y(0) = 0$ (every linear function maps the zero vector to zero, by the representation theorem $\hat y(0) = 0^T \beta_{\text{wt}} = 0$). But the regression formula gives $\hat y(0) = 0^T \beta_{\text{wt}} + v = v$. So $\hat y$ is linear iff $v = 0$.

> [!note]- Derivation
> Suppose $\hat y$ is linear. Then by the [[Def - Affine and Linear Functions on Rn|representation theorem for linear functions]], $\hat y(x) = a^T x$ for some $a \in \mathbb R^n$. In particular, $\hat y(0) = a^T 0 = 0$.
>
> But $\hat y(0) = 0^T \beta_{\text{wt}} + v = v$. So $v = 0$, which contradicts our assumption $v \neq 0$. Hence $\hat y$ is not linear.
>
> Alternatively (without contradiction), apply superposition with $\alpha = \beta = 1$ (so $\alpha + \beta = 2 \neq 1$): $\hat y(2x) = 2 x^T \beta_{\text{wt}} + v$, while $2 \hat y(x) = 2 x^T \beta_{\text{wt}} + 2 v$. These differ by $v$, so general superposition fails when $v \neq 0$.

**Step 3: Express $\hat y$ as a single inner product via augmentation.**

Prepend a constant feature $1$ to the input.

> [!note]- Derivation
> Define $\tilde x \in \mathbb R^{n+1}$ by $\tilde x = (1, x_1, x_2, \dots, x_n) = (1, x)$ — the original $n$-vector with a leading $1$. Define $\tilde \beta_{\text{wt}} \in \mathbb R^{n+1}$ by $\tilde \beta_{\text{wt}} = (v, \beta_1, \beta_2, \dots, \beta_n) = (v, \beta_{\text{wt}})$ — the weight vector with the offset $v$ prepended.
>
> Compute the inner product:
> $$\tilde x^T \tilde \beta_{\text{wt}} = 1 \cdot v + x_1 \beta_1 + x_2 \beta_2 + \cdots + x_n \beta_n = v + x^T \beta_{\text{wt}} = \hat y(x).$$
>
> So $\hat y(x) = \tilde x^T \tilde \beta_{\text{wt}}$, an inner product of two $(n+1)$-vectors. As a function of $\tilde x$, this is *linear* (no offset term): $\tilde y(\tilde x) := \tilde x^T \tilde \beta_{\text{wt}}$ satisfies superposition for any $\alpha, \beta$ without the constraint $\alpha + \beta = 1$.
>
> Of course, the augmented input $\tilde x$ is *constrained* to have first entry $1$, so not every $\tilde x \in \mathbb R^{n+1}$ corresponds to a valid input. The trick is purely notational: it lets the same algorithm that handles linear functions also handle affine functions, by working in one dimension higher.

> [!note]- Complete formal solution
> Let $\beta_{\text{wt}} \in \mathbb R^n$, $v \in \mathbb R$, and define $\hat y : \mathbb R^n \to \mathbb R$ by $\hat y(x) = x^T \beta_{\text{wt}} + v$.
>
> *$\hat y$ is affine.* For any $x, y \in \mathbb R^n$ and scalars $\alpha, \beta$ with $\alpha + \beta = 1$:
> \begin{align}
> \hat y(\alpha x + \beta y) &= (\alpha x + \beta y)^T \beta_{\text{wt}} + v \\
> &= \alpha x^T \beta_{\text{wt}} + \beta y^T \beta_{\text{wt}} + (\alpha + \beta) v \\
> &= \alpha (x^T \beta_{\text{wt}} + v) + \beta (y^T \beta_{\text{wt}} + v) \\
> &= \alpha \hat y(x) + \beta \hat y(y).
> \end{align}
> So affine superposition holds.
>
> *$\hat y$ is not linear when $v \neq 0$.* $\hat y(0) = 0^T \beta_{\text{wt}} + v = v$. Any linear function $f : \mathbb R^n \to \mathbb R$ satisfies $f(0) = 0$ (since $f(0) = f(0 + 0) = f(0) + f(0)$, hence $f(0) = 0$). So if $v \neq 0$, $\hat y$ cannot be linear.
>
> *The linear part is $\beta_{\text{wt}}$ and the offset is $v$.* By the affine representation theorem $\hat y(x) = a^T x + b$ uniquely with $a$ the linear part and $b$ the offset. Comparing with $\hat y(x) = x^T \beta_{\text{wt}} + v$, we read off $a = \beta_{\text{wt}}$ and $b = v$.
>
> *Single-inner-product form via augmentation.* Define $\tilde x \in \mathbb R^{n+1}$ by $\tilde x_1 = 1$, $\tilde x_{i+1} = x_i$ for $i = 1, \dots, n$. Define $\tilde \beta \in \mathbb R^{n+1}$ by $\tilde \beta_1 = v$, $\tilde \beta_{i+1} = (\beta_{\text{wt}})_i$ for $i = 1, \dots, n$. Then
> $$\tilde x^T \tilde \beta = 1 \cdot v + \sum_{i=1}^n x_i (\beta_{\text{wt}})_i = v + x^T \beta_{\text{wt}} = \hat y(x).$$
> So $\hat y(x) = \tilde x^T \tilde \beta$, an inner product of the augmented vectors. The augmented function $\tilde y(\tilde x) = \tilde x^T \tilde \beta$ is linear in $\tilde x$ (without the affine restriction $\alpha + \beta = 1$ on the superposition), at the cost of constraining the first entry of $\tilde x$ to be $1$. $\quad\blacksquare$

---

# Key Takeaways

**Affine $\neq$ linear, and the difference is exactly a translation.** A function $f(x) = a^T x + b$ is affine but not linear unless $b = 0$. The class of affine functions is the class of "linear plus translation"; it is what applied modelling actually needs, because real-world variables almost never have a natural zero point. Regression has an intercept, prices have a level, dynamics have an offset, Taylor expansion has a constant term — all of these are affine, not linear. The trigger for recognising "this is affine, not linear" is to evaluate at the zero vector: $f(0) \neq 0$ rules out linearity. The remedy, when the algorithm in front of you wants a linear function, is the homogenisation trick: prepend a constant feature of $1$ to the input, absorb the offset into the new first weight, and the augmented function is genuinely linear in the augmented input.

**The constant-feature trick is a standard reflex.** Whenever you encounter an affine function and a "linear-only" framework (e.g., a software library that fits linear models, or a theorem that requires linearity), the immediate move is to homogenise: the original $n$-vector input $x$ becomes the $(n+1)$-vector $\tilde x = (1, x)$, the original parameters $(\beta, v)$ become the single $(n+1)$-vector $\tilde \beta = (v, \beta)$, and the original affine formula becomes a single inner product $\tilde x^T \tilde \beta$. This trick is so universal that statistical software does it silently — the user fits "a regression with intercept" and the library prepends a $1$ to every feature vector internally. Once internalised, the trick eliminates the cognitive overhead of distinguishing linear and affine for most purposes.

**The representation theorem makes the analysis mechanical.** Once a function is identified as affine, the [[Def - Affine and Linear Functions on Rn|representation theorem]] hands you the exact form $f(x) = a^T x + b$ with $a, b$ determined uniquely by $a_i = f(e_i) - f(0)$ and $b = f(0)$. Verifying that a given formula is affine, identifying its linear part and offset, and rewriting it in standardised form — all of these become routine calculations once you know the function is affine and apply the theorem. The exercise of "regression model is an affine function" is the simplest possible instance, but the same technique generalises to any applied setting where you need to extract the linear and constant parts of a known affine function. The general pattern: classify (linear / affine / neither) → apply the corresponding representation theorem → identify the data.
