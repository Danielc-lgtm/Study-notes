---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Path-Ordered Exponential"
  - "Def - Parallel Transport in a Principal Bundle"
  - "Thm - Existence and Uniqueness of Horizontal Lifts"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\mathbb{K}$ denotes either $\mathbb{R}$ or $\mathbb{C}$, and $\operatorname{Mat}(n \times n; \mathbb{K})$ is the associative algebra of $n \times n$ matrices over $\mathbb{K}$, acting on the column space $\mathbb{K}^n$. We fix once and for all a norm $\lvert \cdot \rvert$ on $\mathbb{K}^n$ (the Euclidean or Hermitian norm) and equip $\operatorname{Mat}(n \times n; \mathbb{K})$ with the associated **operator norm**
$$\lVert B \rVert := \sup\{\, \lvert Bx \rvert : x \in \mathbb{K}^n,\ \lvert x \rvert \le 1 \,\}, \qquad B \in \operatorname{Mat}(n \times n; \mathbb{K}),$$
which is submultiplicative, $\lVert BC \rVert \le \lVert B \rVert\, \lVert C \rVert$, and satisfies $\lVert 1_n \rVert = 1$, where $1_n$ is the identity matrix.

We write $I = [0, L] \subset \mathbb{R}$ for a fixed compact interval, $L > 0$. A map $A : I \to \operatorname{Mat}(n \times n; \mathbb{K})$ is **continuous** in the usual sense (each of its $n^2$ entries is continuous), and we abbreviate its uniform (supremum) norm by
$$\lVert A \rVert_{C^0(I)} := \sup_{t \in I} \lVert A(t) \rVert < \infty,$$
finite because a continuous $\operatorname{Mat}$-valued function on a compact interval is bounded. For a continuously differentiable $\mathbb{K}^n$- or $\operatorname{Mat}$-valued function $f$ on $I$ we write $\dot f = \frac{df}{dt}$ and use the norm $\lVert f \rVert_{C^1(I)} := \lVert f \rVert_{C^0(I)} + \lVert \dot f \rVert_{C^0(I)}$. The space of continuous $V$-valued functions on $I$ with the norm $\lVert \cdot \rVert_{C^0(I)}$ is denoted $C^0(I; V)$, and the space of continuously differentiable ones with $\lVert \cdot \rVert_{C^1(I)}$ is $C^1(I; V)$, for $V = \mathbb{K}^n$ or $V = \operatorname{Mat}(n \times n; \mathbb{K})$.

The **modulus of continuity** of a continuous $A : I \to \operatorname{Mat}(n \times n; \mathbb{K})$ is the function
$$\omega_A(\delta) := \sup\{\, \lVert A(\tau) - A(\sigma) \rVert : \tau, \sigma \in I,\ \lvert \tau - \sigma \rvert \le \delta \,\}, \qquad \delta \ge 0;$$
that $\omega_A(\delta) \to 0$ as $\delta \searrow 0$ is uniform continuity, established for us by the Heine–Cantor argument inside Lemma 5 (a continuous map on a compact interval is uniformly continuous).

The object of study is the linear initial value problem, written in the sign convention of the parallel-transport equation for a matrix structure group,
$$\dot v(t) = -A(t)\, v(t), \qquad v(0) = v_0 \in \mathbb{K}^n, \tag{PT}$$
which is Bär's equation (2.10). This is exactly the equation satisfied by the fibre coordinate of a horizontal lift in a matrix-group principal bundle: by the **[[Thm - Existence and Uniqueness of Horizontal Lifts|horizontal-lift reduction]]** — in a local trivialisation over the curve $c$, the horizontal lift is $\tilde c = s_\alpha(c) \cdot h$ with $h$ solving $\dot h = -A_\alpha(\dot c)\, h$, a linear first-order equation driven by the local connection form $A_\alpha$ pulled back along $c$ — the fibre coordinate $v(t)$ of the transported vector obeys (PT) with $A(t) = A_\alpha(\dot c(t))$. The solution operator of (PT) is the **path-ordered exponential** $\mathcal{P}\exp\big({-}\int_0^t A(\tau)\, d\tau\big)$ of the sibling definition page.

> [!warning] Convention:
> The sign in (PT) is $\dot v = -Av$, matching Bär §2.6, so that parallel transport of a vector against the flow of the connection appears with the minus sign and the holonomy of a small loop is $1_n - \int_S F + \cdots$ (see [[Thm - Curvature is the Infinitesimal Holonomy]]). A source writing $\dot v = +Av$ (parallel transport of the frame rather than the vector) obtains the same statements with $A$ replaced by $-A$; every displayed series and product below flips sign accordingly under that replacement.

---

# Statement

> **Theorem (path-ordered exponential solves the linear parallel-transport equation; Bär, Lemma 2.6.7).** Let $I = [0, L]$ and let $A : I \to \operatorname{Mat}(n \times n; \mathbb{K})$ be continuous. Then the initial value problem
> $$\dot v(t) = -A(t)\, v(t), \qquad v(0) = v_0 \in \mathbb{K}^n$$
> has a unique solution $v \in C^1(I; \mathbb{K}^n)$, and it is given by the **Dyson series**
> $$v(t) = \sum_{j=0}^{\infty} (-1)^j \int_0^t \! d\tau_j \int_0^{\tau_j} \! d\tau_{j-1} \cdots \int_0^{\tau_2} \! d\tau_1\ A(\tau_j)\, A(\tau_{j-1}) \cdots A(\tau_1)\, v_0, \tag{1}$$
> in which the $j$-th summand is integrated over the time-ordered simplex $0 \le \tau_1 \le \tau_2 \le \cdots \le \tau_j \le t$ and the matrices stand in path order (latest time on the left, so that the factors read left to right in decreasing time). The series converges absolutely and uniformly on $I$ in the Banach space $C^1(I; \mathbb{K}^n)$, so it may be differentiated term by term. Moreover the same solution is the limit of the ordered Euler products
> $$v(t) = \lim_{N \to \infty} \Big(1_n - \tfrac{t}{N} A\big(\tfrac{N-1}{N} t\big)\Big) \Big(1_n - \tfrac{t}{N} A\big(\tfrac{N-2}{N} t\big)\Big) \cdots \Big(1_n - \tfrac{t}{N} A(0)\Big)\, v_0 \tag{2}$$
> for each fixed $t \in I$, the factors ordered with the latest time on the left.

The right-hand side of $(1)$ is, by definition, the path-ordered exponential acting on $v_0$:

> **Restatement of the sibling definition.** ![[Def - Path-Ordered Exponential#The Definition]]

so the theorem is the assertion that $v(t) = \mathcal{P}\exp\big({-}\int_0^t A(\tau)\, d\tau\big)\, v_0$ is the unique solution of (PT), and that the ordered-product limit $(2)$ computes the same operator.

> [!warning] Corrected step (Bär's proof of the product formula).
> Bär's part (a) writes the one-step increment as $v(s+\epsilon) = (1_n - \epsilon A(s)) v(s) + O(\epsilon^2)$ and sums $N$ such errors to $N \cdot O(\epsilon^2) = O(1/N)$, but the $O(\epsilon^2)$ is not uniform in $s$ unless $A$ is Lipschitz or differentiable; for a merely continuous $A$ the per-step error is $o(\epsilon)$, not $O(\epsilon^2)$. Part III below replaces the heuristic with a telescoping estimate whose per-step error is $\tfrac{t}{N}\big(c\,\tfrac{t}{N} + \omega_A(\tfrac{t}{N})\big)$, controlled by the modulus of continuity $\omega_A$; summing gives total error $\le M^2 t\,\big(c\,\tfrac{t}{N} + \omega_A(\tfrac{t}{N})\big) \to 0$, which is the honest statement and needs only continuity.

---

# Motivation

Parallel transport in a matrix-group bundle is the solution operator of a linear ordinary differential equation, and this theorem is what makes that solution operator computable and estimable. Three things are at stake, and the notes need all three downstream.

First, the theorem is an **existence-and-uniqueness statement that holds on the entire interval at once**. For a general nonlinear equation $\dot v = f(t, v)$ the Picard–Lindelöf theorem gives a solution only on a short time interval, and continuation to all of $I$ requires a separate a priori bound. For the linear equation (PT) that separate bound is automatic — the growth is at most exponential, $\lvert v(t) \rvert \le e^{\lVert A \rVert_{C^0(I)}\, t} \lvert v_0 \rvert$ — so the solution never escapes to infinity in finite time and lives on all of $[0, L]$. This is precisely the global-existence input the **[[Thm - Existence and Uniqueness of Horizontal Lifts|existence and uniqueness of horizontal lifts]]** theorem needs for matrix groups: because the fibre equation is linear, the maximal horizontal lift is defined for as long as the base curve is, with no escape.

Second, the theorem supplies an **explicit convergent expansion**, the Dyson series, whose terms are ordered integrals of $A$. This is the working tool of every perturbative computation in gauge theory and quantum mechanics: the first two terms are exactly what one needs to read the curvature off a small loop (see [[Thm - Curvature is the Infinitesimal Holonomy]]), and the whole series is the time-dependent perturbation expansion of quantum mechanics when $-A(t)$ is $-\tfrac{i}{\hbar} H(t)$.

Third, the product formula $(2)$ realises parallel transport as a **limit of infinitesimal transports composed in order**. It is the statement that transporting a vector along a curve is the same as chopping the curve into $N$ tiny pieces, transporting by the linearised rule $1_n - \tfrac{t}{N} A$ across each, and letting $N \to \infty$. This is the picture behind the lattice-gauge-theory Wilson line and the physicist's definition of the Wilson loop, and it is the geometric reason the series is called *path-ordered*: the order of the factors records the order in which the pieces of the curve are traversed, and it cannot be permuted when the $A(t)$ fail to commute.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is mild — any continuous matrix-valued $A$ on a compact interval — so the question is which problems secretly present such an $A$.

The first disguised source is **a connection restricted to a curve**. Whenever one has a connection on a matrix-group principal bundle (or a vector bundle) and a piecewise smooth curve $c : I \to M$, choosing a local trivialisation turns the horizontality condition into (PT) with $A(t) = A_\alpha(\dot c(t))$, the local connection form evaluated on the velocity. The bridge $B \Rightarrow A$ is the horizontal-lift reduction: "there is a connection and a curve" becomes "there is a continuous $A : I \to \mathfrak{g} \subset \operatorname{Mat}$", and the theorem then computes the parallel transport as $\mathcal{P}\exp$. *Example problem:* on the trivial $U(1)$-bundle over $S^1$ with connection form $A = i a\, d\theta$, transport around the circle is $\mathcal{P}\exp(-\int_0^{2\pi} i a\, d\theta) = e^{-2\pi i a}$, the source of the abelian holonomy computation.

The second disguised source is **a time-dependent linear evolution in quantum mechanics or control theory**. The Schrödinger equation $i\hbar\, \dot\psi = H(t)\psi$ is (PT) with $A(t) = \tfrac{i}{\hbar} H(t)$; a linear control system $\dot x = M(t) x$ is (PT) with $A = -M$. The bridge is simply matching the equation: any first-order linear system with continuous, possibly non-commuting, coefficients is an instance. The non-obvious content is that the solution operator is *not* $\exp(-\int_0^t A)$ unless the $A(t)$ commute — the ordering matters. *Example problem:* a two-level atom driven by a time-dependent field, $A(t) = a(t)\sigma_1 + b(t)\sigma_3$, whose evolution is the Dyson series and whose second-order term is genuinely $\mathcal{P}$-ordered (see [[Ex - The Dyson Series for a Two-Level System]]).

The third disguised source is **a family of matrices depending continuously on a parameter that one wishes to integrate multiplicatively**. Any time a problem asks for an ordered product of matrices that vary continuously — a discrete cocycle in the continuum limit, a transfer matrix built from a continuously varying local datum, a holonomy of a lattice connection as the lattice is refined — the object being sought is the limit $(2)$, hence the path-ordered exponential of the theorem. The bridge is that the ordered Euler product converges, by this theorem, to $\mathcal{P}\exp$. *Example problem:* the continuum limit of a product of nearest-neighbour link variables $\prod_k \exp(-\tfrac{t}{N} A(\tfrac{k}{N} t))$ on a one-dimensional lattice is the Wilson line $\mathcal{P}\exp(-\int_0^t A)$.

**Targets (Output Amplification).** The conclusion is an identity of two expressions for one solution; combined with other ingredients it yields more.

Combine the Dyson series $(1)$ with **Stokes's theorem and a small loop**. Truncating $(1)$ at second order and integrating the first term over a loop bounding a surface $S$ turns $\int_c A$ into $\int_S dA$, and the second-order term contributes the commutator part $\int_S A \wedge A$; the extra ingredient $D$ is [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] together with the uniform remainder bound $\lVert (1)\text{'s }j\text{-th term} \rVert \le \tfrac{L^j}{j!}\lVert A \rVert^j_{C^0}$ from Lemma 5, and the payoff $E$ is the expansion $\operatorname{hol}(c_L) = 1_n - \int_{S_L} F + O(L^3)$ proved in [[Thm - Curvature is the Infinitesimal Holonomy]] — curvature *is* the infinitesimal holonomy.

Combine the commuting case of $(1)$ with **an abelian structure group**. When all $A(t)$ commute the ordering is vacuous and $(1)$ collapses to the ordinary matrix exponential $\exp(-\int_0^t A)$ (proved on the sibling definition page); the extra ingredient is abelianness of $G$, and the payoff is that holonomy of an abelian connection around a loop equals $\exp(-\oint A) = \exp(-\int_S F)$, the content of [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|the abelian holonomy theorem]] and the geometric origin of Dirac charge quantisation.

Combine the product formula $(2)$ with **a discretisation of the base**. Refining a lattice and taking the ordered product of link variables realises $(2)$; the extra ingredient is a sequence of lattices with mesh $\to 0$, and the payoff is the lattice-to-continuum limit of the Wilson line and the Wilson loop, the observables of lattice gauge theory. The order-of-factors bookkeeping in $(2)$ is exactly the path ordering of the Wilson loop.

---

# Why Is It True

Set the two formulas side by side and ask what each is doing. The equation $\dot v = -A v$ says: to first order in a small time step $\epsilon$, the vector changes by $v(s + \epsilon) \approx v(s) - \epsilon A(s) v(s) = (1_n - \epsilon A(s)) v(s)$. So transporting across a whole interval is, morally, a product of the infinitesimal factors $1_n - \epsilon A$, one per step, arranged in the order the steps are taken. That product, in the limit of infinitely many infinitely small steps, is formula $(2)$. Everything hard is in making "morally" precise, and the honest per-step error is controlled by how much $A$ can change over one step — its modulus of continuity — which is why continuity of $A$ is exactly the right hypothesis.

Now expand that same product formally in powers of $\epsilon$ and collect terms. A term with $j$ factors of $A$ contributes a sum over choices of $j$ of the $N$ steps at which an $A$ is picked rather than the $1_n$; because the steps are ordered in time, each such choice is a time-ordered tuple $s_1 \le s_2 \le \cdots \le s_j$, and the factors stand in the order $A(s_j) \cdots A(s_1)$. Passing to the continuum turns the ordered sum into the ordered integral over the simplex $0 \le \tau_1 \le \cdots \le \tau_j \le t$, and the result is exactly the $j$-th term of the Dyson series $(1)$. So the two formulas are the same object seen two ways: $(2)$ is the ordered product, $(1)$ is its expansion in powers of $A$, term by term the ordered integrals.

That the series actually *is* a solution is a direct differentiation. Differentiating the $j$-th term with respect to the upper limit $t$, the fundamental theorem of calculus peels off the outermost integral and pins its variable to $t$, promoting an $A(\tau_j)$ to $A(t)$ on the far left; what remains is exactly $-A(t)$ times the $(j-1)$-th term. Summing over $j$, the whole series reproduces $-A(t)$ times itself: $\dot v = -A v$. The only analytic subtlety is the licence to differentiate term by term, which the norm bounds $\lVert j\text{-th term} \rVert \le \tfrac{t^j}{j!}\lVert A \rVert^j$ and $\lVert \tfrac{d}{dt}(j\text{-th term}) \rVert \le \tfrac{t^{j-1}}{(j-1)!}\lVert A \rVert^j$ supply, since both are summable and the series therefore converges in $C^1$.

> **Mechanism in one sentence.** Picard iteration for a *linear* equation converges on the whole interval because the growth is at most exponential, and its successive iterates are precisely the time-ordered integrals of $A$, so the iteration series is the Dyson series and its ordered-product discretisation is $(2)$.

Uniqueness needs one more idea: two solutions differ by a solution of $\dot u = -A u$ with $u(0) = 0$, and Grönwall's inequality forces such a $u$ to vanish, because its size is bounded by $\lVert A \rVert$ times the accumulated integral of its own size, and the only non-negative function dominated by a constant multiple of its own running integral, starting from zero, is zero.

---

# What Makes This Hard

The non-obvious step is the rigorous proof of the product formula $(2)$ for a merely continuous $A$: the naive Euler estimate assigns each step an error $O(\epsilon^2)$, but that constant is uniform in the step only when $A$ is Lipschitz, and for continuous $A$ one must instead bound the per-step error by the modulus of continuity $\omega_A(\epsilon)$, obtaining $o(\epsilon)$ per step and $o(1)$ in total through a telescoping comparison of the exact one-step solution operator with the linearised factor. The common error is to sum $N$ copies of a non-uniform $O(\epsilon^2)$ as if the constant were the same at every step; the fix is uniform continuity, which the compactness of $I$ guarantees. The second trap is the ordering: one is tempted to write $\mathcal{P}\exp(-\int A) = \exp(-\int A)$, which is false whenever two values $A(s), A(s')$ fail to commute, because the ordered product cannot be collapsed to a single exponential — the simplex $0 \le \tau_1 \le \cdots \le \tau_j \le t$ is a fraction $1/j!$ of the cube $[0,t]^j$, and only when the integrand is symmetric under permuting the $\tau_i$ (the commuting case) does the ordered integral become $\tfrac{1}{j!}(\int_0^t A)^j$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Show the Dyson series is a $C^1$ function by bounding its terms and their derivatives in operator norm and invoking completeness of $C^1(I)$; differentiate it term by term to check it solves the equation; use Grönwall to see the solution is unique; and prove the product formula by comparing, one step at a time, the exact solution operator over a subinterval with its linearised factor $1_n - \tfrac{t}{N} A$, telescoping the differences and controlling each by the modulus of continuity of $A$.

**Subgoal decomposition:**

1. **Ordered-simplex volume.** Show $\int_0^t d\tau_j \int_0^{\tau_j} d\tau_{j-1} \cdots \int_0^{\tau_2} d\tau_1 = \tfrac{t^j}{j!}$.
   - *Hint:* Induct on $j$; the inner $(j-1)$-fold integral is $\tfrac{\tau_j^{\,j-1}}{(j-1)!}$, then integrate $\tau_j$ from $0$ to $t$.
   - *Why needed:* It converts the operator-norm bound on the $j$-th term into the summable $\tfrac{t^j}{j!}\lVert A \rVert^j$, giving absolute convergence.

2. **Banach spaces and absolute convergence.** Show $C^0(I; V)$ and $C^1(I; V)$ are complete and that an absolutely convergent series in a Banach space converges.
   - *Hint:* Uniform Cauchy sequences of continuous functions converge uniformly to a continuous limit; for $C^1$, control the function and its derivative separately and glue with the fundamental theorem of calculus.
   - *Why needed:* It is the licence to say the term-by-term bounds imply a genuine $C^1$ sum. This is Bär's item I2.6.3.

3. **Termwise differentiation.** Show that a series of $C^1$ functions whose $C^1$-norms are summable has a $C^1$ sum whose derivative is the sum of the derivatives.
   - *Hint:* Uniform convergence of $\sum f_j$ and of $\sum \dot f_j$, plus the fundamental theorem of calculus, let the limit pass through the integral.
   - *Why needed:* It licenses differentiating $(1)$ term by term in Part I.

4. **Grönwall and uniqueness.** Prove Grönwall's inequality and deduce that (PT) has at most one solution.
   - *Hint:* If $\phi(t) \le K \int_0^t \phi$ with $\phi \ge 0$, then $\phi \equiv 0$; apply to $\phi = \lvert v - w \rvert$ for two solutions.
   - *Why needed:* Existence (the series) plus uniqueness gives *the* solution operator, needed to even define $U(t,s)$ in Part III.

5. **Solution operator, its integral equation, and the one-step estimate.** Define $U(t,s)$, prove $U(t,s) = 1_n - \int_s^t A U$, the bound $\lVert U(t,s) \rVert \le e^{\lVert A \rVert_{C^0} (t-s)}$, and $\lVert U(s+h, s) - (1_n - h A(s)) \rVert \le h\big(c\, h + \omega_A(h)\big)$.
   - *Hint:* Subtract the integral equations for $U$ and for the linear factor; split $A(\tau)U(\tau,s) - A(s) = A(\tau)[U(\tau,s) - 1_n] + [A(\tau) - A(s)]$ and bound each, the second by $\omega_A(h)$.
   - *Why needed:* This is the corrected replacement for Bär's non-uniform $O(\epsilon^2)$; it is where continuity of $A$ does its work.

6. **Telescoping.** For ordered products, $\prod B_k - \prod C_k = \sum_k (\prod_{m>k} B_m)(B_k - C_k)(\prod_{m<k} C_m)$; combine with subgoal 5 and the exponential bounds to send $\lVert U(t,0) - P_N \rVert \to 0$.
   - *Hint:* $\prod_{m>k} B_m = U(t, t_{k+1})$ by the cocycle law; each product of factors is bounded by $e^{\lVert A \rVert_{C^0} L}$.
   - *Why needed:* It assembles the per-step estimate into the global convergence $(2)$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Volume of the time-ordered simplex
> **Statement:** For every integer $j \ge 1$ and every $t \ge 0$,
> $$\int_0^t d\tau_j \int_0^{\tau_j} d\tau_{j-1} \cdots \int_0^{\tau_2} d\tau_1 = \frac{t^j}{j!}.$$
>
> **Hint:** Induct on $j$; the inner $(j-1)$-fold integral evaluated with upper limit $\tau_j$ equals $\tfrac{\tau_j^{\,j-1}}{(j-1)!}$.
>
> **Why needed:** It turns the crude estimate $\lVert A(\tau_j) \cdots A(\tau_1) \rVert \le \lVert A \rVert^j_{C^0(I)}$ over the simplex into the summable bound $\tfrac{t^j}{j!}\lVert A \rVert^j_{C^0(I)}$ on the $j$-th term, which drives every convergence statement.
>
> > [!note]- Full proof
> > We argue by induction on $j$.
> >
> > **Base case $j = 1$.** The single integral is $\int_0^t d\tau_1 = t = \tfrac{t^1}{1!}$, as claimed.
> >
> > **Induction step.** Assume the identity holds for $j - 1$: for every upper limit $s \ge 0$,
> > $$\int_0^s d\tau_{j-1} \int_0^{\tau_{j-1}} d\tau_{j-2} \cdots \int_0^{\tau_2} d\tau_1 = \frac{s^{\,j-1}}{(j-1)!} \qquad \text{(induction hypothesis)}.$$
> > The $j$-fold integral is the integral over $\tau_j \in [0,t]$ of the $(j-1)$-fold integral with upper limit $\tau_j$, so
> > $$\int_0^t d\tau_j \int_0^{\tau_j} d\tau_{j-1} \cdots \int_0^{\tau_2} d\tau_1 = \int_0^t \frac{\tau_j^{\,j-1}}{(j-1)!}\, d\tau_j \qquad \text{(induction hypothesis with } s = \tau_j\text{)}$$
> > $$= \frac{1}{(j-1)!} \cdot \frac{t^{\,j}}{j} = \frac{t^{\,j}}{j!} \qquad \text{(power rule } \textstyle\int_0^t \tau^{j-1} d\tau = t^j/j\text{, and } j \cdot (j-1)! = j!\text{)}.$$
> > This closes the induction, and the identity holds for all $j \ge 1$. $\blacksquare$

> [!note]- Lemma 2: $C^0(I; V)$ and $C^1(I; V)$ are Banach spaces, and absolute convergence implies convergence
> **Statement:** Let $V$ be a finite-dimensional normed $\mathbb{K}$-vector space (here $V = \mathbb{K}^n$ or $V = \operatorname{Mat}(n \times n; \mathbb{K})$). Then $C^0(I; V)$ with the norm $\lVert \cdot \rVert_{C^0(I)}$ and $C^1(I; V)$ with the norm $\lVert \cdot \rVert_{C^1(I)}$ are complete, hence Banach spaces; and in any Banach space $\big(W, \lVert \cdot \rVert\big)$, a series $\sum_j x_j$ with $\sum_j \lVert x_j \rVert < \infty$ converges to some limit in $W$.
>
> **Hint:** A Cauchy sequence in $C^0$ is uniformly Cauchy, so it converges pointwise to a limit that is a uniform limit of continuous functions, hence continuous; for $C^1$, apply this to the functions and to their derivatives, then reconstruct the limit function by the fundamental theorem of calculus. For absolute convergence, show the partial sums are Cauchy.
>
> **Why needed:** It is Bär's item I2.6.3 and the licence to conclude, from the summable term bounds of Lemma 5, that the Dyson series has a genuine limit in $C^1$.
>
> > [!note]- Full proof
> > Because $V$ is finite-dimensional, it is complete (all norms on a finite-dimensional space are equivalent and $\mathbb{K}^m$ is complete), a fact we use freely below.
> >
> > **Completeness of $C^0(I; V)$.** Let $(f_k)_{k \ge 1}$ be a Cauchy sequence in $C^0(I; V)$: for every $\varepsilon > 0$ there is $K$ with $\lVert f_k - f_\ell \rVert_{C^0(I)} < \varepsilon$ for $k, \ell \ge K$. For each fixed $t \in I$ this gives $\lvert f_k(t) - f_\ell(t) \rvert \le \lVert f_k - f_\ell \rVert_{C^0(I)} < \varepsilon$, so $(f_k(t))_k$ is Cauchy in $V$ and, $V$ being complete, converges to a value we call $f(t)$. Letting $\ell \to \infty$ in $\lvert f_k(t) - f_\ell(t) \rvert < \varepsilon$ (valid for all $t$ simultaneously and all $k \ge K$) gives $\lvert f_k(t) - f(t) \rvert \le \varepsilon$ for all $t \in I$ and all $k \ge K$; that is, $f_k \to f$ uniformly on $I$. A uniform limit of continuous functions is continuous: given $t_0 \in I$ and $\varepsilon > 0$, pick $k \ge K$ so that $\lVert f_k - f \rVert_{C^0(I)} < \varepsilon/3$, then $\delta$ so that $\lvert f_k(t) - f_k(t_0) \rvert < \varepsilon/3$ for $\lvert t - t_0 \rvert < \delta$ (continuity of $f_k$), whence $\lvert f(t) - f(t_0) \rvert \le \lvert f(t) - f_k(t) \rvert + \lvert f_k(t) - f_k(t_0) \rvert + \lvert f_k(t_0) - f(t_0) \rvert < \varepsilon$ (triangle inequality, three terms). So $f \in C^0(I; V)$ and $\lVert f_k - f \rVert_{C^0(I)} \to 0$, proving completeness.
> >
> > **Completeness of $C^1(I; V)$.** Let $(f_k)$ be Cauchy in $C^1(I; V)$, so both $(f_k)$ and $(\dot f_k)$ are Cauchy in $C^0(I; V)$ (since $\lVert f_k - f_\ell \rVert_{C^0} \le \lVert f_k - f_\ell \rVert_{C^1}$ and likewise for the derivatives). By the previous paragraph there are $f, g \in C^0(I; V)$ with $f_k \to f$ and $\dot f_k \to g$ uniformly. By the fundamental theorem of calculus, $f_k(t) = f_k(0) + \int_0^t \dot f_k(\tau)\, d\tau$ for every $k$. Uniform convergence of $\dot f_k \to g$ lets us pass to the limit under the integral — $\big\lvert \int_0^t (\dot f_k - g) \big\rvert \le t\, \lVert \dot f_k - g \rVert_{C^0(I)} \to 0$ — and $f_k(0) \to f(0)$, so $f(t) = f(0) + \int_0^t g(\tau)\, d\tau$. The right-hand side is differentiable with derivative $g(t)$ (fundamental theorem of calculus, $g$ continuous), so $f \in C^1(I; V)$ with $\dot f = g$, and $\lVert f_k - f \rVert_{C^1(I)} = \lVert f_k - f \rVert_{C^0} + \lVert \dot f_k - g \rVert_{C^0} \to 0$. Hence $C^1(I; V)$ is complete.
> >
> > **Absolute convergence implies convergence.** Let $W$ be a Banach space and $\sum_j \lVert x_j \rVert < \infty$. Write $S_N = \sum_{j=0}^N x_j$. For $N > M$,
> > $$\lVert S_N - S_M \rVert = \Big\lVert \sum_{j=M+1}^N x_j \Big\rVert \le \sum_{j=M+1}^N \lVert x_j \rVert \qquad \text{(triangle inequality)},$$
> > and the right-hand side is the tail of a convergent series of non-negative reals, hence $< \varepsilon$ once $M$ is large enough. So $(S_N)$ is Cauchy in $W$ and, $W$ being complete, converges. $\blacksquare$

> [!note]- Lemma 3: Termwise differentiation of a $C^1$-absolutely-convergent series
> **Statement:** Let $(f_j)_{j \ge 0}$ be a sequence in $C^1(I; V)$ with $\sum_{j} \lVert f_j \rVert_{C^1(I)} < \infty$. Then $f := \sum_{j} f_j$ converges in $C^1(I; V)$, the sum $f$ is continuously differentiable, and $\dot f = \sum_{j} \dot f_j$, both series converging uniformly on $I$.
>
> **Hint:** The hypothesis makes $\sum f_j$ and $\sum \dot f_j$ each absolutely, hence uniformly, convergent; identify the derivative of the sum with the sum of the derivatives through the fundamental theorem of calculus.
>
> **Why needed:** It is exactly the operation performed in Part I, Step 2: differentiate the Dyson series term by term.
>
> > [!note]- Full proof
> > Since $\lVert f_j \rVert_{C^0(I)} \le \lVert f_j \rVert_{C^1(I)}$ and $\lVert \dot f_j \rVert_{C^0(I)} \le \lVert f_j \rVert_{C^1(I)}$, the hypothesis $\sum_j \lVert f_j \rVert_{C^1(I)} < \infty$ gives $\sum_j \lVert f_j \rVert_{C^0(I)} < \infty$ and $\sum_j \lVert \dot f_j \rVert_{C^0(I)} < \infty$. By Lemma 2 (absolute convergence in the Banach space $C^0(I; V)$), the partial sums $g_N := \sum_{j=0}^N f_j$ converge uniformly to a continuous function $f$, and the partial sums $h_N := \sum_{j=0}^N \dot f_j$ converge uniformly to a continuous function $h$.
> >
> > **The sum $g_N$ converges in $C^1$ and $\dot f = h$.** Each partial sum is $C^1$ with $\dot g_N = h_N$ (finite sum), so by the fundamental theorem of calculus,
> > $$g_N(t) = g_N(0) + \int_0^t h_N(\tau)\, d\tau \qquad \text{(fundamental theorem of calculus applied to } g_N\text{)}.$$
> > Let $N \to \infty$. On the left $g_N(t) \to f(t)$ pointwise. On the right $g_N(0) \to f(0)$, and
> > $$\Big\lvert \int_0^t h_N - \int_0^t h \Big\rvert \le t\, \lVert h_N - h \rVert_{C^0(I)} \to 0 \qquad \text{(uniform convergence } h_N \to h\text{ on } I\text{)},$$
> > so $\int_0^t h_N \to \int_0^t h$. Therefore $f(t) = f(0) + \int_0^t h(\tau)\, d\tau$. The right-hand side is differentiable with derivative $h(t)$ (fundamental theorem of calculus, $h$ continuous), so $f \in C^1(I; V)$ and $\dot f = h = \sum_j \dot f_j$. Finally $\lVert g_N - f \rVert_{C^1(I)} = \lVert g_N - f \rVert_{C^0} + \lVert h_N - h \rVert_{C^0} \to 0$, so the series converges in $C^1(I; V)$. $\blacksquare$

> [!note]- Lemma 4: Grönwall's inequality and uniqueness of the solution
> **Statement:** Let $\phi : I \to [0, \infty)$ be continuous, and suppose there are constants $\alpha \ge 0$ and $K \ge 0$ with
> $$\phi(t) \le \alpha + K \int_0^t \phi(\tau)\, d\tau \qquad \text{for all } t \in I.$$
> Then $\phi(t) \le \alpha\, e^{K t}$ for all $t \in I$. In particular, if $\alpha = 0$ then $\phi \equiv 0$. Consequently the initial value problem (PT) has at most one $C^1$ solution.
>
> **Hint:** Set $\Psi(t) = \alpha + K \int_0^t \phi$; then $\dot\Psi = K\phi \le K\Psi$, so $\tfrac{d}{dt}(e^{-Kt}\Psi) \le 0$ and $e^{-Kt}\Psi(t) \le \Psi(0) = \alpha$. For uniqueness apply this to $\phi = \lvert v - w \rvert$ with $\alpha = 0$, $K = \lVert A \rVert_{C^0(I)}$.
>
> **Why needed:** The Dyson series constructs *a* solution; Grönwall shows there is no other, so "the" solution operator is well defined — the object $U(t,s)$ of Part III depends on this.
>
> > [!note]- Full proof
> > **Grönwall.** Define $\Psi(t) := \alpha + K \int_0^t \phi(\tau)\, d\tau$, a $C^1$ function with $\Psi(0) = \alpha$ and, by the fundamental theorem of calculus, $\dot\Psi(t) = K\phi(t)$. The hypothesis is $\phi(t) \le \Psi(t)$, so
> > $$\dot\Psi(t) = K\phi(t) \le K\Psi(t) \qquad \text{(hypothesis } \phi \le \Psi \text{, and } K \ge 0\text{)}.$$
> > Multiply by the positive integrating factor $e^{-Kt}$:
> > $$\frac{d}{dt}\big(e^{-Kt}\Psi(t)\big) = e^{-Kt}\big(\dot\Psi(t) - K\Psi(t)\big) \le 0 \qquad \text{(product rule, then the displayed inequality)}.$$
> > Hence $t \mapsto e^{-Kt}\Psi(t)$ is non-increasing, so $e^{-Kt}\Psi(t) \le e^{-K \cdot 0}\Psi(0) = \alpha$, that is $\Psi(t) \le \alpha\, e^{Kt}$. Combining with $\phi \le \Psi$ gives $\phi(t) \le \alpha\, e^{Kt}$. If $\alpha = 0$ this reads $0 \le \phi(t) \le 0$, so $\phi \equiv 0$.
> >
> > **Uniqueness.** Let $v, w \in C^1(I; \mathbb{K}^n)$ both solve (PT), and set $u := v - w$. Then $u$ is $C^1$ with $\dot u(t) = -A(t) u(t)$ and $u(0) = v_0 - v_0 = 0$. By the fundamental theorem of calculus, $u(t) = u(0) + \int_0^t \dot u(\tau)\, d\tau = -\int_0^t A(\tau) u(\tau)\, d\tau$, so
> > $$\lvert u(t) \rvert = \Big\lvert \int_0^t A(\tau) u(\tau)\, d\tau \Big\rvert \le \int_0^t \lVert A(\tau) \rVert\, \lvert u(\tau) \rvert\, d\tau \le \lVert A \rVert_{C^0(I)} \int_0^t \lvert u(\tau) \rvert\, d\tau \qquad \text{(triangle inequality for integrals; operator-norm bound } \lvert A(\tau)u(\tau) \rvert \le \lVert A(\tau) \rVert \lvert u(\tau) \rvert\text{)}.$$
> > This is the Grönwall hypothesis for $\phi = \lvert u \rvert$ with $\alpha = 0$ and $K = \lVert A \rVert_{C^0(I)}$, so $\lvert u \rvert \equiv 0$, i.e. $v = w$. $\blacksquare$

> [!note]- Lemma 5: The solution operator, its integral equation, and the one-step estimate
> **Statement:** For $0 \le s \le t \le L$ let $U(t, s) \in \operatorname{Mat}(n \times n; \mathbb{K})$ be the linear map sending $v(s)$ to $v(t)$, where $v$ solves $\dot v = -A v$ on $[s, L]$ with the given value at $s$ (well defined and unique by Parts I–II). Then:
> 1. $U(s, s) = 1_n$ and $U(t, r)\, U(r, s) = U(t, s)$ for $s \le r \le t$ (cocycle law);
> 2. $\partial_t U(t, s) = -A(t)\, U(t, s)$ and the integral equation $U(t, s) = 1_n - \int_s^t A(\tau)\, U(\tau, s)\, d\tau$ hold;
> 3. $\lVert U(t, s) \rVert \le e^{\lVert A \rVert_{C^0(I)} (t - s)}$;
> 4. writing $h = t - s$, the exact one-step operator differs from the linearised factor by
> $$\big\lVert U(s + h,\, s) - \big(1_n - h A(s)\big) \big\rVert \le h\,\big(c\, h + \omega_A(h)\big), \qquad c := \lVert A \rVert^2_{C^0(I)}\, e^{\lVert A \rVert_{C^0(I)} L},$$
> where $\omega_A$ is the modulus of continuity of $A$, which tends to $0$ as $h \searrow 0$ because $A$ is uniformly continuous on the compact interval $I$.
>
> **Hint:** Every claim comes from the integral equation $U(t,s) = 1_n - \int_s^t A U$; for (4), also subtract the integral form of the linear factor and split $A(\tau)U(\tau,s) - A(s) = A(\tau)[U(\tau,s) - 1_n] + [A(\tau) - A(s)]$.
>
> **Why needed:** Clause (4) is the corrected, uniform replacement for Bär's non-uniform $O(\epsilon^2)$; clauses (1)–(3) supply the cocycle structure and the bounds that Lemma 6 telescopes.
>
> > [!note]- Full proof
> > **Well-definedness and clause (1).** For each fixed $s$, Parts I–II (applied to the equation on $[s, L]$, which is (PT) with the initial time shifted and any initial value at $s$; the Dyson construction and the Grönwall uniqueness argument are insensitive to the choice of initial time) give a unique solution for each initial value $v(s)$, and the map $v(s) \mapsto v(t)$ is linear because the equation is linear and the zero initial value gives the zero solution (uniqueness). Call this linear map $U(t, s)$. Then $U(s, s) = 1_n$ since the solution at its own initial time is the initial value. For $s \le r \le t$, the solution starting at $s$ agrees on $[r, L]$ with the solution that starts at $r$ from the value $U(r, s) v(s)$ (both solve the same equation with the same value at $r$; uniqueness), so evaluating at $t$ gives $U(t, s) = U(t, r) U(r, s)$.
> >
> > **Clause (2).** Apply $U(t, s)$ to a fixed vector $x$: the curve $t \mapsto U(t, s) x$ is the solution with value $x$ at $s$, so $\partial_t\big(U(t,s) x\big) = -A(t)\, U(t, s) x$; as this holds for every $x$, $\partial_t U(t, s) = -A(t) U(t, s)$. Integrating from $s$ to $t$ and using $U(s, s) = 1_n$,
> > $$U(t, s) = 1_n - \int_s^t A(\tau)\, U(\tau, s)\, d\tau \qquad \text{(fundamental theorem of calculus)}.$$
> >
> > **Clause (3).** From the integral equation and submultiplicativity,
> > $$\lVert U(t, s) \rVert \le \lVert 1_n \rVert + \int_s^t \lVert A(\tau) \rVert\, \lVert U(\tau, s) \rVert\, d\tau \le 1 + \lVert A \rVert_{C^0(I)} \int_s^t \lVert U(\tau, s) \rVert\, d\tau \qquad \text{(triangle inequality; } \lVert A(\tau) \rVert \le \lVert A \rVert_{C^0(I)}\text{)}.$$
> > This is the Grönwall hypothesis (Lemma 4) for $\phi(t) = \lVert U(t, s) \rVert$ on $[s, L]$ with $\alpha = 1$, $K = \lVert A \rVert_{C^0(I)}$ (shifted to start at $s$), giving $\lVert U(t, s) \rVert \le e^{\lVert A \rVert_{C^0(I)} (t - s)}$.
> >
> > **Uniform continuity of $A$ (Heine–Cantor).** Suppose, for contradiction, that $\omega_A(h) \not\to 0$; then there is $\varepsilon_0 > 0$ and sequences $\tau_m, \sigma_m \in I$ with $\lvert \tau_m - \sigma_m \rvert \to 0$ but $\lVert A(\tau_m) - A(\sigma_m) \rVert \ge \varepsilon_0$. By compactness of $I$ (Bolzano–Weierstrass, the [[Thm - Heine–Borel Theorem|Heine–Borel]] property of $[0,L]$), pass to a subsequence with $\tau_m \to \tau_* \in I$; then $\sigma_m \to \tau_*$ too (since $\lvert \tau_m - \sigma_m \rvert \to 0$), and by continuity $\lVert A(\tau_m) - A(\sigma_m) \rVert \to \lVert A(\tau_*) - A(\tau_*) \rVert = 0$, contradicting $\lVert A(\tau_m) - A(\sigma_m) \rVert \ge \varepsilon_0$. Hence $\omega_A(h) \to 0$ as $h \searrow 0$.
> >
> > **Clause (4).** Fix $s$ and $h = t - s > 0$ with $s + h \le L$. The linear factor $1_n - h A(s)$ can be written in integral form as $1_n - h A(s) = 1_n - \int_s^{s+h} A(s)\, d\tau$. Subtracting from the integral equation of clause (2),
> > $$U(s + h, s) - \big(1_n - h A(s)\big) = -\int_s^{s+h} \big[A(\tau) U(\tau, s) - A(s)\big]\, d\tau.$$
> > Split the bracket as $A(\tau) U(\tau, s) - A(s) = A(\tau)\big[U(\tau, s) - 1_n\big] + \big[A(\tau) - A(s)\big]$. For the first piece, the integral equation and clause (3) give, for $s \le \tau \le s + h$,
> > $$\lVert U(\tau, s) - 1_n \rVert = \Big\lVert \int_s^\tau A(\rho) U(\rho, s)\, d\rho \Big\rVert \le \lVert A \rVert_{C^0(I)}\, e^{\lVert A \rVert_{C^0(I)} L}\, (\tau - s) \le \lVert A \rVert_{C^0(I)}\, e^{\lVert A \rVert_{C^0(I)} L}\, h \qquad \text{(integral equation; clause (3) with } \tau - s \le L\text{)},$$
> > so $\lVert A(\tau)[U(\tau, s) - 1_n] \rVert \le \lVert A \rVert^2_{C^0(I)}\, e^{\lVert A \rVert_{C^0(I)} L}\, h = c\, h$. For the second piece, $\lVert A(\tau) - A(s) \rVert \le \omega_A(h)$ because $\lvert \tau - s \rvert \le h$. Therefore the integrand is bounded in norm by $c\, h + \omega_A(h)$, and
> > $$\big\lVert U(s + h, s) - (1_n - h A(s)) \big\rVert \le \int_s^{s+h} \big(c\, h + \omega_A(h)\big)\, d\tau = h\,\big(c\, h + \omega_A(h)\big) \qquad \text{(the integrand is constant in } \tau\text{, interval length } h\text{)}.$$
> > This is clause (4). $\blacksquare$

> [!note]- Lemma 6: The telescoping identity for ordered products
> **Statement:** Let $B_0, \dots, B_{N-1}$ and $C_0, \dots, C_{N-1}$ be matrices in $\operatorname{Mat}(n \times n; \mathbb{K})$. With ordered products written latest-index-on-the-left, $\prod_{m=N-1}^{0} B_m := B_{N-1} B_{N-2} \cdots B_0$, one has
> $$\prod_{m=N-1}^{0} B_m - \prod_{m=N-1}^{0} C_m = \sum_{k=0}^{N-1} \Big(\prod_{m=N-1}^{k+1} B_m\Big)\big(B_k - C_k\big)\Big(\prod_{m=k-1}^{0} C_m\Big),$$
> where an empty product is $1_n$.
>
> **Hint:** The right-hand side telescopes: the $k$-th summand replaces $C_k$ by $B_k$ in a hybrid product, and consecutive hybrids cancel.
>
> **Why needed:** It expresses the global discrepancy between the exact ordered product $\prod U$ and the linearised product $\prod (1_n - hA)$ as a sum of per-step discrepancies $B_k - C_k$, each estimated by Lemma 5(4).
>
> > [!note]- Full proof
> > For $0 \le k \le N$ define the hybrid product $H_k := \big(\prod_{m=N-1}^{k} B_m\big)\big(\prod_{m=k-1}^{0} C_m\big)$, in which the factors with index $\ge k$ are $B$'s and those with index $< k$ are $C$'s. Then $H_N = \prod_{m=N-1}^{0} C_m$ (all factors are $C$'s, the first product empty) and $H_0 = \prod_{m=N-1}^{0} B_m$ (all factors are $B$'s, the second product empty). We compute a single telescoping difference. For $0 \le k \le N - 1$,
> > $$H_k - H_{k+1} = \Big(\prod_{m=N-1}^{k+1} B_m\Big) B_k \Big(\prod_{m=k-1}^{0} C_m\Big) - \Big(\prod_{m=N-1}^{k+1} B_m\Big) C_k \Big(\prod_{m=k-1}^{0} C_m\Big) = \Big(\prod_{m=N-1}^{k+1} B_m\Big)\big(B_k - C_k\big)\Big(\prod_{m=k-1}^{0} C_m\Big),$$
> > where the two hybrids $H_k$ and $H_{k+1}$ share the factors of index $> k$ (all $B$'s) and of index $< k$ (all $C$'s) and differ only in the index-$k$ factor ($B_k$ versus $C_k$). Summing over $k = 0, \dots, N-1$ the left side telescopes:
> > $$\sum_{k=0}^{N-1}(H_k - H_{k+1}) = H_0 - H_N = \prod_{m=N-1}^{0} B_m - \prod_{m=N-1}^{0} C_m,$$
> > and the right side is the claimed sum. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $A : I = [0, L] \to \operatorname{Mat}(n \times n; \mathbb{K})$ be continuous and $v_0 \in \mathbb{K}^n$. For $j \ge 0$ write the $j$-th term of the Dyson series as
> $$T_j(t) := (-1)^j \int_0^t \! d\tau_j \int_0^{\tau_j} \! d\tau_{j-1} \cdots \int_0^{\tau_2} \! d\tau_1\ A(\tau_j)\, A(\tau_{j-1}) \cdots A(\tau_1)\, v_0 \in \mathbb{K}^n, \qquad T_0(t) := v_0.$$
>
> **Step 0 — the terms are well-defined $C^1$ functions.** Each iterated integral is the integral of a continuous $\operatorname{Mat}$-valued integrand over the ordered simplex, hence a continuous function of the upper limit $t$; the outermost integral $\int_0^t(\cdots) d\tau_j$ of a continuous integrand is, by the fundamental theorem of calculus, a $C^1$ function of $t$. So $T_j \in C^1(I; \mathbb{K}^n)$ for every $j$, and $T_j(0) = 0$ for $j \ge 1$ because the outer integral over $[0,0]$ vanishes.
>
> **Step 1 — norm bounds and $C^1$ convergence.** Over the simplex $0 \le \tau_1 \le \cdots \le \tau_j \le t$ the integrand satisfies $\lVert A(\tau_j) \cdots A(\tau_1) v_0 \rVert \le \lVert A \rVert^j_{C^0(I)}\, \lvert v_0 \rvert$ by submultiplicativity of the operator norm. Hence, using the simplex volume of **Lemma 1**,
> $$\lVert T_j \rVert_{C^0(I)} \le \Big(\sup_{t \in I} \int_0^t d\tau_j \cdots \int_0^{\tau_2} d\tau_1\Big)\, \lVert A \rVert^j_{C^0(I)}\, \lvert v_0 \rvert = \frac{L^j}{j!}\, \lVert A \rVert^j_{C^0(I)}\, \lvert v_0 \rvert \qquad \text{(Lemma 1 with the simplex volume } t^j/j! \le L^j/j!\text{)}.$$
> For the derivative, Step 0 and the fundamental theorem of calculus give, differentiating the outer integral,
> $$\dot T_j(t) = (-1)^j\, A(t) \int_0^t \! d\tau_{j-1} \int_0^{\tau_{j-1}} \! d\tau_{j-2} \cdots \int_0^{\tau_2} \! d\tau_1\ A(\tau_{j-1}) \cdots A(\tau_1)\, v_0 = -A(t)\, T_{j-1}(t) \qquad (j \ge 1), \tag{$\ast$}$$
> the last equality because $(-1)^j A(t)\int_0^t(\cdots) = -A(t)\cdot (-1)^{j-1}\int_0^t(\cdots) = -A(t) T_{j-1}(t)$, and $\dot T_0 = 0$. Taking norms in the middle expression of $(\ast)$ and using Lemma 1 on the remaining $(j-1)$-fold simplex,
> $$\lVert \dot T_j \rVert_{C^0(I)} \le \lVert A \rVert_{C^0(I)} \cdot \frac{L^{j-1}}{(j-1)!}\, \lVert A \rVert^{j-1}_{C^0(I)}\, \lvert v_0 \rvert = \frac{L^{j-1}}{(j-1)!}\, \lVert A \rVert^{j}_{C^0(I)}\, \lvert v_0 \rvert \qquad (j \ge 1).$$
> Therefore
> $$\sum_{j=0}^{\infty} \lVert T_j \rVert_{C^1(I)} \le \lvert v_0 \rvert + \lvert v_0 \rvert \sum_{j=1}^{\infty}\Big(\frac{L^j}{j!} + \frac{L^{j-1}}{(j-1)!}\Big) \lVert A \rVert^{j}_{C^0(I)} \le \lvert v_0 \rvert\,\big(1 + L^{-1}\big) e^{L \lVert A \rVert_{C^0(I)}} \cdot (\text{finite}) < \infty,$$
> the two exponential-type series both converging (they are dominated by $\sum_j \tfrac{(L\lVert A \rVert)^j}{j!} = e^{L\lVert A \rVert_{C^0(I)}}$). By **Lemma 2**, $C^1(I; \mathbb{K}^n)$ is a Banach space and absolute convergence implies convergence, so
> $$v(t) := \sum_{j=0}^{\infty} T_j(t)$$
> converges in $C^1(I; \mathbb{K}^n)$; in particular the series converges absolutely and uniformly on $I$, as claimed.
>
> **Step 2 — the series solves (PT).** By **Lemma 3** the sum $v$ is $C^1$ and may be differentiated term by term:
> $$\dot v(t) = \sum_{j=0}^{\infty} \dot T_j(t) = \sum_{j=1}^{\infty} \dot T_j(t) = \sum_{j=1}^{\infty}\big(-A(t)\, T_{j-1}(t)\big) \qquad \text{(Lemma 3 termwise; } \dot T_0 = 0\text{; then } (\ast)\text{)}.$$
> Re-indexing $k = j - 1$ and pulling the continuous factor $-A(t)$ out of the (uniformly convergent) sum,
> $$\dot v(t) = -A(t) \sum_{k=0}^{\infty} T_k(t) = -A(t)\, v(t) \qquad \text{(re-index } k = j-1\text{; matrix multiplication is continuous, so it commutes with the convergent sum)}.$$
> The initial condition is $v(0) = T_0(0) + \sum_{j \ge 1} T_j(0) = v_0 + 0 = v_0$ (Step 0). So $v$ solves (PT), proving existence and formula $(1)$.
>
> **Step 3 — uniqueness.** By **Lemma 4** (Grönwall), the problem (PT) has at most one $C^1$ solution; combined with Step 2, $v$ is *the* solution. This is what licenses the solution operator $U(t, s)$ used below: $v(t) = U(t, 0) v_0$.
>
> **Step 4 — the product formula $(2)$.** Fix $t \in (0, L]$ (for $t = 0$ both sides of $(2)$ are $v_0$). Partition $[0, t]$ into $N$ equal steps $t_k := \tfrac{k}{N} t$, $k = 0, \dots, N$, of length $h := t/N$. By the cocycle law **Lemma 5(1)**,
> $$U(t, 0) = U(t_N, t_{N-1})\, U(t_{N-1}, t_{N-2}) \cdots U(t_1, t_0) = \prod_{k=N-1}^{0} B_k, \qquad B_k := U(t_{k+1}, t_k),$$
> while the ordered Euler product in $(2)$ is $P_N := \prod_{k=N-1}^{0} C_k$ with $C_k := 1_n - h A(t_k)$. Apply the telescoping identity **Lemma 6**:
> $$U(t, 0) - P_N = \sum_{k=0}^{N-1} \Big(\prod_{m=N-1}^{k+1} B_m\Big)\big(B_k - C_k\big)\Big(\prod_{m=k-1}^{0} C_m\Big).$$
> We bound the three factors of each summand.
>
> First, by the cocycle law, $\prod_{m=N-1}^{k+1} B_m = U(t_N, t_{k+1}) = U(t, t_{k+1})$, so by **Lemma 5(3)**,
> $$\Big\lVert \prod_{m=N-1}^{k+1} B_m \Big\rVert = \lVert U(t, t_{k+1}) \rVert \le e^{\lVert A \rVert_{C^0(I)} (t - t_{k+1})} \le e^{\lVert A \rVert_{C^0(I)} L} =: M.$$
> Second,
> $$\Big\lVert \prod_{m=k-1}^{0} C_m \Big\rVert \le \prod_{m=0}^{k-1}\lVert 1_n - h A(t_m) \rVert \le \prod_{m=0}^{k-1}\big(1 + h \lVert A \rVert_{C^0(I)}\big) \le \big(1 + h \lVert A \rVert_{C^0(I)}\big)^{N} \le e^{N h \lVert A \rVert_{C^0(I)}} = e^{t \lVert A \rVert_{C^0(I)}} \le M,$$
> using submultiplicativity, the triangle inequality $\lVert 1_n - h A(t_m) \rVert \le 1 + h\lVert A \rVert_{C^0(I)}$, the elementary inequality $1 + x \le e^x$, and $Nh = t \le L$. Third, by **Lemma 5(4)** each per-step discrepancy obeys
> $$\lVert B_k - C_k \rVert = \big\lVert U(t_{k+1}, t_k) - (1_n - h A(t_k)) \big\rVert \le h\,\big(c\, h + \omega_A(h)\big), \qquad c = \lVert A \rVert^2_{C^0(I)}\, e^{\lVert A \rVert_{C^0(I)} L}.$$
> Assembling, with $N$ summands,
> $$\lVert U(t, 0) - P_N \rVert \le \sum_{k=0}^{N-1} M \cdot h\,\big(c\, h + \omega_A(h)\big) \cdot M = N\, h\, M^2 \big(c\, h + \omega_A(h)\big) = M^2\, t\,\big(c\, h + \omega_A(h)\big) \qquad (N h = t).$$
> As $N \to \infty$ we have $h = t/N \to 0$, so $c\, h \to 0$ and $\omega_A(h) \to 0$ (uniform continuity of $A$, **Lemma 5**), whence $\lVert U(t, 0) - P_N \rVert \to 0$. Applying to the fixed vector $v_0$ and using $v(t) = U(t, 0) v_0$,
> $$\lim_{N \to \infty} P_N\, v_0 = U(t, 0)\, v_0 = v(t),$$
> which is exactly formula $(2)$.
>
> **Conclusion.** The Dyson series $(1)$ converges absolutely and uniformly in $C^1(I; \mathbb{K}^n)$ (Step 1), defines the unique $C^1$ solution of the linear parallel-transport equation $\dot v = -A v$, $v(0) = v_0$ (Steps 2–3), and this solution is equally the limit of the ordered Euler products $(2)$ (Step 4). Therefore $v(t) = \mathcal{P}\exp\big({-}\int_0^t A(\tau)\, d\tau\big)\, v_0$, and both the series and the ordered-product limit compute the path-ordered exponential. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Time-dependent perturbation theory in quantum mechanics.** For a Hamiltonian $H(t)$ the Schrödinger equation $\dot\psi = -\tfrac{i}{\hbar} H(t)\psi$ is (PT) with $A(t) = \tfrac{i}{\hbar} H(t)$, and the Dyson series $(1)$ *is* the time-ordered perturbation expansion, its $j$-th term the $j$-th order amplitude. The theorem applies because a continuous $H$ on a bounded time interval gives a continuous $A$. It is non-obvious that the naive $\exp(-\tfrac{i}{\hbar}\int H)$ is wrong: it fails exactly when $[H(t), H(t')] \ne 0$, since the ordered second-order term $\int_0^t d\tau_2 \int_0^{\tau_2} d\tau_1\, H(\tau_2) H(\tau_1)$ differs from the symmetric $\tfrac12\big(\int_0^t H\big)^2$ precisely by the commutator, the origin of the interaction-picture time-ordering symbol $\mathcal{T}$. Concretely, work the two-level driven system of [[Ex - The Dyson Series for a Two-Level System]].

**Continuum limit of a lattice Wilson line.** On a one-dimensional lattice with link variables $U_k = \exp(-\tfrac{t}{N} A(\tfrac{k}{N} t)) \in G$, the ordered product $\prod_{k} U_k$ is the discrete parallel transport; replacing $\exp(-hA)$ by its first-order truncation $1_n - hA$ changes each factor by $O(h^2)$, and the theorem's product formula $(2)$ shows the refined product converges to the Wilson line $\mathcal{P}\exp(-\int_0^t A)$. The application is non-obvious because one must check that summing $N$ factor-replacements of size $O(h^2)$ leaves the limit unchanged — precisely the telescoping estimate of Part III — so the two discretisations, $1_n - hA$ and $\exp(-hA)$, have the same continuum limit.

**Transfer matrices and the Sturm–Liouville equation.** A second-order linear equation $-y'' + q(t) y = 0$ with continuous potential $q$ becomes a first-order system $\tfrac{d}{dt}\binom{y}{y'} = M(t)\binom{y}{y'}$ with $M(t) = \left(\begin{smallmatrix} 0 & 1 \\ q(t) & 0 \end{smallmatrix}\right)$, i.e. (PT) with $A = -M$. The theorem gives the transfer matrix across $[0, t]$ as the path-ordered exponential, and the product formula realises it as a limit of products of infinitesimal transfer matrices. The application is non-obvious because the $M(t)$ at different times do not commute (unless $q$ is constant), so the transfer matrix is genuinely path-ordered and not $\exp(\int M)$.

---

# Bridges

- **[[Thm - Curvature is the Infinitesimal Holonomy]]** — the first serious consumer of this theorem. Truncating the Dyson series $(1)$ at second order for a small loop $c_L$ of length $O(L)$, the remainder bound $\lVert T_j \rVert \le \tfrac{L^j}{j!}\lVert A \rVert^j$ from Step 1 controls the tail as $O(L^3)$, the first-order term becomes $\int_{S_L} dA$ by Stokes, and the ordered second-order term contributes the commutator part $\int_{S_L} A \wedge A$; the outcome is $\operatorname{hol}(c_L) = 1_n - \int_{S_L} F + O(L^3)$ with $F = dA + A \wedge A$. The non-commutativity of the ordered product is exactly the $A \wedge A$ term.

- **[[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral]]** — the commuting specialisation. When $G$ is abelian all $A(t)$ commute, the ordered integral over the simplex becomes $\tfrac{1}{j!}(\int_0^t A)^j$ (the integrand is symmetric under permuting the $\tau_i$), and $(1)$ collapses to the ordinary exponential $\exp(-\int_0^t A)$; combined with Stokes this gives the loop holonomy $\exp(-\int_S F)$.

- **[[Def - Path-Ordered Exponential]]** — the definition this theorem certifies. The sibling page *defines* $\mathcal{P}\exp(-\int_0^t A)$ by the series $(1)$ and the ordered-product limit $(2)$ and states their equivalence; this page proves that equivalence and proves that the common value solves (PT), so that the name "solution operator of $\dot v = -Av$" is justified.

- **[[Thm - Existence and Uniqueness of Horizontal Lifts]]** — the geometric source. That theorem reduces horizontality in a matrix-group bundle to the linear equation (PT) with $A(t) = A_\alpha(\dot c(t))$; the present theorem then delivers the global existence, uniqueness, and explicit form of the horizontal lift's fibre coordinate as $\mathcal{P}\exp(-\int A_\alpha(\dot c))$, closing the loop between the geometry (horizontal lift) and the analysis (linear ODE).

- **Grönwall's inequality and global existence for linear systems** — the analytic backbone, isolated as [[Ex - Global Existence for Linear ODEs via Gronwall]]. The exponential a priori bound $\lVert U(t, s) \rVert \le e^{\lVert A \rVert (t-s)}$ (Lemma 5(3)) is what makes the linear equation live on all of $I$ with no escape in finite time, in contrast to nonlinear equations where global existence must be earned separately.

---

# Unlocked by This

> [!tip] Wilson loops and lattice gauge theory *(from Quantum Field Theory)*
> The ordered-product form $(2)$ is the definition of the lattice Wilson line, and the trace of the path-ordered exponential around a closed loop, $\operatorname{tr}\,\mathcal{P}\exp(-\oint A)$, is the **Wilson loop**, the fundamental gauge-invariant observable of lattice gauge theory. The theorem's product formula is exactly the statement that the lattice observable converges to its continuum counterpart as the lattice is refined.

> [!tip] The time-ordering symbol and the Magnus expansion *(from Mathematical Physics)*
> The failure of $\mathcal{P}\exp(-\int A)$ to equal $\exp(-\int A)$ when the $A(t)$ do not commute is what forces Dyson's time-ordering symbol $\mathcal{T}$ and motivates the **Magnus expansion**, which writes $\mathcal{P}\exp(-\int_0^t A) = \exp(\Omega(t))$ with $\Omega = -\int A + \tfrac12 \int\!\int [\,\cdot\,,\,\cdot\,] + \cdots$ a series of iterated commutators — the "true exponent" of parallel transport, whose leading correction is the curvature.
