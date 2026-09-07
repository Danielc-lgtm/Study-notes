---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Parallel Transport in a Principal Bundle"
  - "Thm - The Exponential Map of a Matrix Group is the Matrix Exponential"
tags: [geometry, gauge-theory]
---

# Notation

Throughout this page $\mathbb{K}$ is either $\mathbb{R}$ or $\mathbb{C}$, and $\operatorname{Mat}(n \times n; \mathbb{K})$ is the associative algebra of $n \times n$ matrices with entries in $\mathbb{K}$, with identity matrix $1_n$. We fix an interval $I = [0, L] \subset \mathbb{R}$ with $L > 0$ and a **continuous** curve of matrices
$$A : I \to \operatorname{Mat}(n \times n; \mathbb{K}), \qquad t \mapsto A(t).$$
Because $\operatorname{Mat}(n \times n; \mathbb{K}) \cong \mathbb{K}^{n^2}$ is finite-dimensional, all its norms are equivalent; we use the **operator norm** $\lVert M \rVert = \sup_{\lVert x \rVert = 1} \lVert M x \rVert$, which is submultiplicative, $\lVert MN \rVert \le \lVert M \rVert\, \lVert N \rVert$, and we abbreviate the sup-norm of $A$ over $I$ by $\lVert A \rVert_{C^0} = \sup_{t \in I} \lVert A(t) \rVert < \infty$ (finite because $A$ is continuous on a compact interval). A matrix-valued function is called $C^0$, respectively $C^1$, when each of its $n^2$ entries is continuous, respectively continuously differentiable, in $t$; the matrix Riemann integral $\int_0^t A(\tau)\, d\tau$ is taken entrywise, and $\frac{d}{dt}$ acts entrywise. The dot $\dot v = \frac{dv}{dt}$ denotes the $t$-derivative.

The vector unknown is $v : I \to \mathbb{K}^n$, and the linear ordinary differential equation of interest is
$$\dot v(t) = -A(t)\, v(t), \qquad v(0) = v_0, \tag{2.10}$$
with $v_0 \in \mathbb{K}^n$ a fixed initial vector. We write $\exp M = e^M = \sum_{k \ge 0} M^k / k!$ for the ordinary matrix exponential (the series converges absolutely in $\operatorname{Mat}(n \times n; \mathbb{K})$ for every $M$; see [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential]]), and $\mathcal{P}\exp$ for the path-ordered exponential defined below. The symbol $\mathcal{P}$ is not a separate object: $\mathcal{P}\exp\big({-}\int_0^t A\big)$ is a single piece of notation for the solution operator of $(2.10)$.

> [!warning] Convention: sign and time-ordering
> Bär writes the parallel-transport equation with a **minus sign**, $\dot v = -A(t) v$, matching the horizontal-lift equation $\dot h_\alpha = -\omega(\dot s_\alpha)\, h_\alpha$ for a matrix structure group (see the Relate section); this is the series convention. The ordered product $(2.14)$ below places the **latest time on the far left**, so that reading the product from right to left follows time forward from $0$ to $t$. The opposite ordering (latest time on the right) defines the inverse operator; this is the source of the "reversed-order exponential" in the calibration checks.

This is a compound page: it defines one notion — the path-ordered exponential $\mathcal{P}\exp\big({-}\int_0^t A\big)$ — in two equivalent guises (a series of iterated integrals and a limit of ordered products), and it proves the one corollary that ties the notion back to the ordinary exponential (the commuting case), because the whole point of the path-ordered exponential is to say precisely what replaces $\exp\big({-}\int A\big)$ when the matrices $A(t)$ fail to commute.

---

# Axiom Motivation

The object we are about to define exists to solve one concrete problem, and the cleanest way to discover it is to watch the naive guess succeed in a special case and then fail in general. The problem is this: given the linear system $\dot v = -A(t) v$ with $v(0) = v_0$, we want a **closed formula for the solution operator** — the map $U(t)$ with $v(t) = U(t) v_0$ — expressed directly in terms of $A$, not merely as "the solution, which exists by Picard–Lindelöf." A closed formula is what lets us compute holonomy, expand it in the size of a loop, and read curvature off the second-order term; the abstract existence theorem gives us none of that.

**The scalar and commuting cases, where the naive guess works.** When $n = 1$, or more generally when $A$ takes values in a commuting family of matrices, the answer is the one calculus suggests. Set $B(t) = \int_0^t A(\tau)\, d\tau$. One is tempted to write $v(t) = e^{-B(t)} v_0$ and to justify it by the chain rule $\frac{d}{dt} e^{-B(t)} = -\dot B(t)\, e^{-B(t)} = -A(t)\, e^{-B(t)}$. In the scalar case this is simply correct. In the matrix case the chain-rule step is exactly where the danger hides, and isolating that danger is what forces the definition upon us.

**Where the naive guess breaks: the ordering problem.** Differentiate the series $e^{-B(t)} = \sum_{j \ge 0} \frac{(-1)^j}{j!} B(t)^j$ term by term. The derivative of $B(t)^j$ by the product rule is
$$\frac{d}{dt} B(t)^j = \sum_{i=0}^{j-1} B(t)^i\, \dot B(t)\, B(t)^{j-1-i} = \sum_{i=0}^{j-1} B(t)^i\, A(t)\, B(t)^{j-1-i},$$
because $\dot B(t) = A(t)$ (the fundamental theorem of calculus, applicable entrywise since $A$ is continuous). If $A(t)$ commutes with $B(t)$ — which happens precisely when all the values $A(\tau)$, $0 \le \tau \le t$, commute with one another — every summand collapses to $A(t) B(t)^{j-1}$, the $j$ copies combine to $j\, A(t) B(t)^{j-1}$, and the computation closes to $-A(t) e^{-B(t)}$. But when the values of $A$ do **not** commute, $A(t)$ cannot be pulled through the powers of $B(t)$, the summands do not collapse, and $\frac{d}{dt} e^{-B(t)} \ne -A(t)\, e^{-B(t)}$. The naive exponential of the integral simply does not solve the equation. This is Bär's *ordering problem* (Remark 2.6.2 material, p. 69): "in the general case, this is not possible and we have an ordering problem." The failure is not a technicality to be smoothed over — it is the whole reason the path-ordered exponential has to be a genuinely new construction rather than a change of notation.

**What the replacement must capture, and what it must exclude.** Any acceptable definition of the solution operator must (i) reduce to $\exp\big({-}\int_0^t A\big)$ exactly when the values of $A$ commute, so that it extends the case we already understand and does not contradict it; (ii) solve $(2.10)$ for every continuous $A$, commuting or not; (iii) respect the arrow of time, since $\dot v = -A(t) v$ is a first-order evolution in which the value at a late time depends on the whole history in a definite temporal order; and (iv) be built from $A$ alone by convergent operations (integrals, products, limits), not merely be asserted to exist. The construction below meets all four. The iterated integrals in $(2.13)$ record the temporal order explicitly: in every product $A(\tau_j) A(\tau_{j-1}) \cdots A(\tau_1)$ the times satisfy $\tau_j \ge \tau_{j-1} \ge \cdots \ge \tau_1$, so later times stand to the left. The ordered-product form $(2.14)$ is the same statement discretised: it is the composition of infinitesimal steps $1_n - \frac{t}{N} A(t_k)$ taken in increasing time, latest on the left.

**Why "path-ordered" and why this is not over-engineering.** One might ask whether some cleverer commuting substitute could be found, avoiding the machinery. It cannot: the ordering is a real feature of the physics and geometry, not an artefact. If it could be dropped, holonomy around a small loop would depend only on the enclosed area weighted by a single number, whereas in a non-abelian gauge theory the holonomy carries the commutator $[A_j, A_k]$ of the connection components — the term that becomes the non-abelian part of the curvature (this is made precise in **Curvature is the Infinitesimal Holonomy**). Delete the ordering and that term vanishes, and with it Yang–Mills theory. So the definition is the minimal honest bookkeeping of "evolve, in order, from $0$ to $t$." A reader who has followed the collapse of the term-by-term derivative above could reconstruct it unaided: keep the iterated integrals but stop pretending the factors may be reordered.

---

# The Definition

Let $A : I = [0, L] \to \operatorname{Mat}(n \times n; \mathbb{K})$ be continuous and let $t \in I$. The **path-ordered exponential of $A$** is the solution operator of the linear ordinary differential equation $(2.10)$, defined by either of the two following equal expressions (Bär, Definition 2.6.8, p. 72):

**First form — the Dyson series of iterated integrals.**
$$\mathcal{P}\exp\!\left(-\int_0^t A(\tau)\, d\tau\right) \;:=\; \sum_{j=0}^{\infty} (-1)^j \int_0^t \! d\tau_j \int_0^{\tau_j} \! d\tau_{j-1} \cdots \int_0^{\tau_2} \! d\tau_1 \; A(\tau_j)\, A(\tau_{j-1}) \cdots A(\tau_1). \tag{2.13}$$
The $j = 0$ term is by convention $1_n$ (an empty product of matrices, and an empty tuple of integrations). In the $j$-th term the integration domain is the ordered simplex $\{(\tau_1, \dots, \tau_j) : 0 \le \tau_1 \le \tau_2 \le \cdots \le \tau_j \le t\}$, and the matrices are written with their time-arguments **decreasing from left to right**, $\tau_j \ge \tau_{j-1} \ge \cdots \ge \tau_1$.

**Second form — the limit of ordered products.**
$$\mathcal{P}\exp\!\left(-\int_0^t A(\tau)\, d\tau\right) \;=\; \lim_{N \to \infty} \left(1_n - \tfrac{t}{N} A\!\left(\tfrac{N-1}{N} t\right)\right) \cdots \left(1_n - \tfrac{t}{N} A\!\left(\tfrac{1}{N} t\right)\right) \left(1_n - \tfrac{t}{N} A(0)\right). \tag{2.14}$$
Here the interval $[0, t]$ is partitioned into $N$ equal steps $t_k = \frac{k}{N} t$ for $k = 0, 1, \dots, N-1$, each factor $1_n - \frac{t}{N} A(t_k)$ is the elementary Euler step over one subinterval, and the factors are composed with the **latest time $t_{N-1}$ on the far left and the earliest time $0$ on the far right**, so that acting on $v_0$ evolves it forward through time.

That the two forms $(2.13)$ and $(2.14)$ are equal — and that their common value, applied to $v_0$, is the unique solution $v(t)$ of $(2.10)$ — is the content of the theorem [[Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation]], which states: *for continuous $A : [0, L] \to \operatorname{Mat}(n \times n; \mathbb{K})$ the unique solution of $\dot v = -A(t) v$, $v(0) = v_0$, is $v(t) = \Big[\sum_{j \ge 0} (-1)^j \int_0^t d\tau_j \cdots \int_0^{\tau_2} d\tau_1\, A(\tau_j) \cdots A(\tau_1)\Big] v_0$, the series converging absolutely and uniformly in $C^1([0, L])$, and equal to $\lim_{N \to \infty} \prod_{k = N-1}^{0} \big(1_n - \frac{t}{N} A(\frac{k}{N} t)\big) v_0$.* We restate the two facts we borrow from that page and use below: the series $(2.13)$ **converges absolutely in $\operatorname{Mat}(n \times n; \mathbb{K})$** with the term bound $\big\lVert j\text{-th term} \big\rVert \le \frac{L^j}{j!} \lVert A \rVert_{C^0}^j$, and its termwise $t$-derivative converges uniformly, so the operator $t \mapsto \mathcal{P}\exp\big({-}\int_0^t A\big)$ is $C^1$ and $\frac{d}{dt} \mathcal{P}\exp\big({-}\int_0^t A\big) = -A(t)\, \mathcal{P}\exp\big({-}\int_0^t A\big)$.

Applied to the initial vector, the definition says exactly
$$v(t) = \mathcal{P}\exp\!\left(-\int_0^t A(\tau)\, d\tau\right) v_0. \tag{$\ast$}$$

---

# Categorical / Structural Definition

The path-ordered exponential has a clean structural characterisation that does not mention the series at all, and it is the one worth carrying: **$\mathcal{P}\exp$ is the unique multiplicative time-evolution generated by $-A$.** Precisely, for $0 \le s \le t \le L$ define the two-time operator $U(t, s) \in \operatorname{Mat}(n \times n; \mathbb{K})$ by letting $U(t, s) w$ be the value at time $t$ of the solution of $\dot v = -A(\tau) v$ that equals $w$ at time $s$; then $U(t, 0) = \mathcal{P}\exp\big({-}\int_0^t A\big)$. The family $\{U(t, s)\}$ is the unique family satisfying

1. **the initial condition** $U(s, s) = 1_n$ for every $s$;
2. **the composition (cocycle) law** $U(t_2, t_1)\, U(t_1, t_0) = U(t_2, t_0)$ for all $t_0 \le t_1 \le t_2$;
3. **the generator law** $\left.\frac{\partial}{\partial t}\right|_{t = s} U(t, s) = -A(s)$ for every $s$.

Existence is the theorem cited above; uniqueness is the uniqueness of solutions of a linear ordinary differential equation, restated in the calibration section. Property (2) is the structural heart: it says $\mathcal{P}\exp$ is a **functor from the path category of the interval to $GL(n; \mathbb{K})$** — objects are times, a morphism $s \to t$ (with $s \le t$) is sent to $U(t, s)$, identities go to $1_n$, and composition of morphisms goes to composition of matrices. This is the finite-dimensional, single-chart shadow of parallel transport as a functor on the path groupoid of a manifold, which is the reason the same formula computes holonomy: concatenating curves multiplies path-ordered exponentials in exactly the order (2) prescribes, matching property (4) of [[Def - Parallel Transport in a Principal Bundle|parallel transport]], $\Gamma(c_2 \ast c_1) = \Gamma(c_2) \circ \Gamma(c_1)$. When all $A(\tau)$ commute the cocycle law degenerates to the additive law of exponents $e^{-B(t_2) + B(t_1)} e^{-B(t_1) + B(t_0)} = e^{-B(t_2) + B(t_0)}$, recovering the ordinary one-parameter subgroup; the non-commuting case is precisely where a genuine two-time kernel $U(t, s)$, rather than a function of $t - s$ or of $B(t) - B(s)$, is unavoidable.

---

# Relate to Other Fields / Compression

**True name.** Operationally, $\mathcal{P}\exp\big({-}\int_0^t A\big)$ is nothing more mysterious than *the fundamental matrix of the linear system $\dot v = -A(t) v$* — the matrix $U(t)$ whose columns are the solutions with the standard basis vectors as initial data, normalised by $U(0) = 1_n$. Every field that meets this system has its own name for the same object, and recognising them as one compresses a great deal:

- **Quantum mechanics and quantum field theory.** With $A(t) = \frac{i}{\hbar} H(t)$ for a time-dependent Hamiltonian $H$, $(2.10)$ becomes the Schrödinger equation $\dot\psi = -\frac{i}{\hbar} H(t) \psi$, and $(2.13)$ is Dyson's time-ordered expansion of the evolution operator $U(t) = \mathcal{T} \exp\big({-}\frac{i}{\hbar} \int_0^t H\big)$. The physicist's time-ordering symbol $\mathcal{T}$ and the geometer's path-ordering symbol $\mathcal{P}$ denote the same reordering rule: in each product, later times to the left. This is why the construction is called the *Dyson series*.
- **Gauge theory and Wilson loops.** With $A(t) = A_\alpha(\dot c(t))$ the local connection form contracted against the velocity of a curve $c$ (see below), $\mathcal{P}\exp\big({-}\oint_c A_\alpha\big)$ around a loop $c$ is the *Wilson loop* variable — the holonomy of the connection, the basic gauge-invariant observable of lattice and continuum gauge theory once one takes its trace.
- **Control theory and the theory of linear systems.** $U(t)$ is the *state-transition matrix* $\Phi(t, 0)$ of the time-varying linear system, and $(2.14)$ is the convergence of the forward Euler method to it. The *Peano–Baker series* of the control literature is $(2.13)$ verbatim (with $+A$ in place of $-A$).
- **Numerical analysis.** $(2.14)$ is exactly the statement that the composition of one-step explicit Euler updates converges to the exact flow as the step size $\frac{t}{N} \to 0$; the non-commuting corrections that $(2.13)$ resums are the source of the Baker–Campbell–Hausdorff and Magnus expansions used to build higher-order geometric integrators that stay in the group $G$.

**Compression.** All of these are one theorem — a first-order linear evolution has a unique fundamental solution, and it is computed by resumming the ordered products of the generator. The path-ordered exponential is the name that resummation carries in geometry, and its only genuinely non-scalar feature is the ordering, which encodes the failure of the generator to commute with itself at different times.

**The link to parallel transport.** The reason this analysis chapter opens with a purely matrix-algebraic construction is that, for a **matrix structure group** $G \subset GL(n; \mathbb{K})$, the horizontal-lift equation defining [[Def - Parallel Transport in a Principal Bundle|parallel transport]] *is* the system $(2.10)$. Along a curve $c$ in the base with a local section $s_\alpha$ of the principal bundle, the horizontal lift $\tilde c = s_\alpha \cdot h_\alpha$ has $h_\alpha : I \to G$ solving $\dot h_\alpha = -\omega(\dot s_\alpha)\, h_\alpha$; writing $A(t) := \omega\big(\dot s_\alpha(t)\big) = \big(s_\alpha^\ast \omega\big)\big(\dot c(t)\big) = A_\alpha\big(\dot c(t)\big)$ for the pullback of the connection $1$-form against the velocity, this is $\dot h_\alpha = -A(t)\, h_\alpha$, and hence $h_\alpha(t) = \mathcal{P}\exp\big({-}\int_0^t A_\alpha(\dot c)\, d\tau\big)\, h_\alpha(0)$. The same equation drives a parallel section $v(t)$ of an associated vector bundle in a trivialisation, with $A(t)$ the connection matrix contracted with $\dot c$. So $\mathcal{P}\exp$ computes parallel transport in one chart, and its value around a loop is the holonomy — the thread this chapter follows into [[Def - Holonomy Group of a Connection|holonomy groups]] and the small-loop expansion.

---

# Examples / Corollaries

Every clause below is verified on the page.

**Instance — constant $A$.** Let $A(t) \equiv A_0$ be constant. A constant family trivially commutes with itself, so the ordering problem is absent, and both defining forms collapse to the ordinary exponential. From $(2.13)$: since $A(\tau_j) \cdots A(\tau_1) = A_0^j$ is independent of the times, the $j$-th term is $(-1)^j A_0^j \int_0^t d\tau_j \int_0^{\tau_j} d\tau_{j-1} \cdots \int_0^{\tau_2} d\tau_1$, and the iterated integral over the ordered simplex equals $\frac{t^j}{j!}$ (this is step (b) of [[Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation]], the induction $\int_0^t d\tau_j \cdots \int_0^{\tau_2} d\tau_1 = t^j / j!$). Hence
$$\mathcal{P}\exp\!\left(-\int_0^t A_0\, d\tau\right) = \sum_{j = 0}^\infty (-1)^j \frac{t^j}{j!} A_0^j = \sum_{j=0}^\infty \frac{(-t A_0)^j}{j!} = e^{-t A_0} \qquad \text{(definition of the matrix exponential)}.$$
From $(2.14)$ the same value appears as $\lim_{N \to \infty} \big(1_n - \frac{t}{N} A_0\big)^N = e^{-t A_0}$, the standard limit characterisation of the exponential (each factor is identical, so the ordered product is an ordinary $N$-th power). The two forms agree, as they must, and both give $e^{-t A_0}$.

**Instance — commuting (in particular diagonal) $A(t)$: the corollary $\mathcal{P}\exp = \exp$ of the integral.** This is Bär's Corollary to Lemma 2.6.7 (the commuting case, pp. 68–69), promoted here to a proved statement.

> [!note]- Corollary and full proof: for a commuting family, the path-ordered exponential is the ordinary exponential of the integral
> **Statement.** Suppose the values of $A$ commute pairwise: $A(\sigma)\, A(\tau) = A(\tau)\, A(\sigma)$ for all $\sigma, \tau \in [0, t]$ (equivalently, $A$ takes values in a commutative subalgebra of $\operatorname{Mat}(n \times n; \mathbb{K})$; the diagonal-matrix case is the model instance). Then
> $$\mathcal{P}\exp\!\left(-\int_0^t A(\tau)\, d\tau\right) = \exp\!\left(-\int_0^t A(\tau)\, d\tau\right).$$
>
> *Proof.* We must show that the right-hand side, applied to an arbitrary $v_0 \in \mathbb{K}^n$, solves the initial value problem $(2.10)$; since $\mathcal{P}\exp\big({-}\int_0^t A\big) v_0$ is *the* solution of $(2.10)$ (by [[Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation]], invoked here as the existence-and-uniqueness input), the two operators then agree on every $v_0$, hence are equal.
>
> **Step 0 — set up the integrated generator and record its two properties.** Define $B(t) = \int_0^t A(\tau)\, d\tau \in \operatorname{Mat}(n \times n; \mathbb{K})$, the entrywise Riemann integral, which exists because $A$ is continuous. First, $B(t)$ **commutes with $A(s)$ for every $s \in [0, t]$**: $B(t)$ is a norm-limit of Riemann sums $\sum_i A(\xi_i)\, \Delta\tau_i$, each summand commutes with $A(s)$ by hypothesis, matrix multiplication is continuous, so the limit commutes with $A(s)$; the same argument gives that $B(t)$ commutes with $B(s)$. Second, $\dot B(t) = A(t)$ by the fundamental theorem of calculus applied entrywise, valid because each entry of $A$ is continuous.
>
> **Step 1 — differentiate the exponential series term by term.** Write $\exp(-B(t)) = \sum_{j \ge 0} \frac{(-1)^j}{j!} B(t)^j$. The partial sums $S_N(t) = \sum_{j = 0}^N \frac{(-1)^j}{j!} B(t)^j$ are $C^1$ in $t$ (finite sums of products of the $C^1$ matrix $B$), and $S_N(t) \to \exp(-B(t))$ pointwise. Their $t$-derivatives are $S_N'(t) = \sum_{j = 1}^N \frac{(-1)^j}{j!} \frac{d}{dt} B(t)^j$, and we bound the tail: by the product rule (Step 1 computation below) each term satisfies $\big\lVert \frac{(-1)^j}{j!} \frac{d}{dt} B(t)^j \big\rVert \le \frac{1}{j!} \cdot j\, \lVert A \rVert_{C^0} \lVert B(t) \rVert^{j-1} \le \lVert A \rVert_{C^0} \frac{(L \lVert A \rVert_{C^0})^{j-1}}{(j-1)!}$, using $\lVert B(t) \rVert \le \int_0^t \lVert A(\tau) \rVert d\tau \le L \lVert A \rVert_{C^0}$. The right-hand side is a convergent series of constants (Weierstrass $M$-test, with $\sum_j \lVert A \rVert_{C^0} \frac{(L\lVert A\rVert_{C^0})^{j-1}}{(j-1)!} = \lVert A \rVert_{C^0}\, e^{L \lVert A \rVert_{C^0}} < \infty$), so $S_N'(t)$ converges **uniformly** on $[0, L]$. By the theorem that a series of $C^1$ functions converging pointwise, whose termwise derivatives converge uniformly, has a $C^1$ sum with derivative the sum of the derivatives (the theorem licensing termwise differentiation, whose hypothesis of uniform convergence of the derivative series we have just verified), $\exp(-B(t))$ is $C^1$ and
> $$\frac{d}{dt} \exp(-B(t)) = \sum_{j = 1}^\infty \frac{(-1)^j}{j!} \frac{d}{dt} B(t)^j.$$
>
> **Step 2 — evaluate the derivative of each power using commutativity.** By the product rule for a $t$-dependent matrix,
> $$\frac{d}{dt} B(t)^j = \sum_{i = 0}^{j-1} B(t)^i\, \dot B(t)\, B(t)^{j - 1 - i} = \sum_{i = 0}^{j-1} B(t)^i\, A(t)\, B(t)^{j-1-i} \qquad (\dot B(t) = A(t),\ \text{Step 0}).$$
> Because $A(t)$ commutes with $B(t)$ (Step 0), each summand equals $A(t)\, B(t)^{j-1}$, and the $j$ equal summands give
> $$\frac{d}{dt} B(t)^j = j\, A(t)\, B(t)^{j-1} \qquad (\text{the } j \text{ terms coincide by commutativity of } A(t) \text{ and } B(t)).$$
>
> **Step 3 — resum.** Substituting into the differentiated series,
> $$\frac{d}{dt} \exp(-B(t)) = \sum_{j = 1}^\infty \frac{(-1)^j}{j!}\, j\, A(t)\, B(t)^{j-1} = -A(t) \sum_{j = 1}^\infty \frac{(-1)^{j-1}}{(j-1)!}\, B(t)^{j-1} \qquad \left(\tfrac{j}{j!} = \tfrac{1}{(j-1)!},\ \text{factor out } -A(t)\right),$$
> and re-indexing $k = j - 1$ the remaining sum is $\sum_{k \ge 0} \frac{(-1)^k}{k!} B(t)^k = \exp(-B(t))$, so
> $$\frac{d}{dt} \exp(-B(t)) = -A(t)\, \exp(-B(t)).$$
> The factoring of $-A(t)$ to the **left** is legitimate precisely because $A(t)$ commutes with the powers of $B(t)$; this is the single place the hypothesis is used, and it is exactly the step that fails in the non-commuting case (see Axiom Motivation).
>
> **Step 4 — check the initial condition and conclude.** At $t = 0$, $B(0) = \int_0^0 A = 0$, so $\exp(-B(0)) = \exp(0) = 1_n$. Setting $w(t) = \exp(-B(t)) v_0$, Steps 1–3 give $\dot w(t) = -A(t)\, w(t)$ and $w(0) = v_0$, so $w$ solves $(2.10)$. By the uniqueness clause of [[Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation]], $w(t) = \mathcal{P}\exp\big({-}\int_0^t A\big) v_0$ for all $t$. As $v_0 \in \mathbb{K}^n$ was arbitrary, the two operators agree, that is $\mathcal{P}\exp\big({-}\int_0^t A\big) = \exp\big({-}\int_0^t A\big)$. Therefore, whenever the values of $A$ commute the path-ordered exponential is the ordinary exponential of the integral. $\blacksquare$

As the concrete diagonal instance, take $n = 2$ and $A(t) = \operatorname{diag}\big(a(t), b(t)\big)$ with $a, b : I \to \mathbb{K}$ continuous. All diagonal matrices commute, so the corollary applies and
$$\mathcal{P}\exp\!\left(-\int_0^t A\right) = \exp\!\left(-\int_0^t \operatorname{diag}(a, b)\right) = \operatorname{diag}\!\left(\exp\!\Big({-}\!\int_0^t a\Big),\ \exp\!\Big({-}\!\int_0^t b\Big)\right),$$
which one may also read off directly from $(2.10)$: the system decouples into two independent scalar equations $\dot v_1 = -a(t) v_1$ and $\dot v_2 = -b(t) v_2$, each solved by the scalar exponential of the negative integral. The two computations agree, confirming the corollary in a case where the answer is independently visible.

**Non-instance — the ordering genuinely matters.** We exhibit a piecewise-constant $A$ for which $\mathcal{P}\exp\big({-}\int_0^2 A\big) \ne \exp\big({-}\int_0^2 A\big)$, so that the commuting corollary cannot be dropped. Use the Pauli matrices
$$\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad \sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}, \qquad \sigma_1^2 = \sigma_3^2 = 1_2, \qquad \sigma_1 \sigma_3 = -\sigma_3 \sigma_1 \ (\text{so } [\sigma_1, \sigma_3] \ne 0),$$
and set $A(t) = \sigma_1$ for $t \in [0, 1]$ and $A(t) = \sigma_3$ for $t \in [1, 2]$. (This $A$ is continuous on each piece; the path-ordered exponential over $[0,2]$ is the ordered composition of the transports over $[1,2]$ and $[0,1]$, exactly the cocycle law of the Categorical section, property (2), which is why concatenating a piecewise-continuous generator is legitimate.) On each piece $A$ is constant, so by the constant-$A$ instance above the transport over that piece is an ordinary exponential, and with the latest piece on the left,
$$\mathcal{P}\exp\!\left(-\int_0^2 A\right) = \Big[\mathcal{P}\exp\!\big({-}\!\int_1^2 \sigma_3\big)\Big] \Big[\mathcal{P}\exp\!\big({-}\!\int_0^1 \sigma_1\big)\Big] = e^{-\sigma_3}\, e^{-\sigma_1}.$$
We compute both sides. Using $\sigma_k^2 = 1_2$, the exponential of a multiple of a Pauli matrix is $e^{c \sigma_k} = \cosh(c)\, 1_2 + \sinh(c)\, \sigma_k$, so
$$e^{-\sigma_1} = \cosh 1\, 1_2 - \sinh 1\, \sigma_1 = \begin{pmatrix} \cosh 1 & -\sinh 1 \\ -\sinh 1 & \cosh 1 \end{pmatrix}, \qquad e^{-\sigma_3} = \operatorname{diag}(e^{-1}, e^{1}),$$
and their product (latest on the left, $e^{-\sigma_3}$ multiplying $e^{-\sigma_1}$ on the left) is
$$e^{-\sigma_3} e^{-\sigma_1} = \begin{pmatrix} e^{-1} & 0 \\ 0 & e \end{pmatrix}\begin{pmatrix} \cosh 1 & -\sinh 1 \\ -\sinh 1 & \cosh 1 \end{pmatrix} = \begin{pmatrix} e^{-1}\cosh 1 & -e^{-1}\sinh 1 \\ -e\, \sinh 1 & e\, \cosh 1 \end{pmatrix}.$$
On the other hand $\int_0^2 A = \int_0^1 \sigma_1\, dt + \int_1^2 \sigma_3\, dt = \sigma_1 + \sigma_3$, so the naive exponential is $\exp\big({-}(\sigma_1 + \sigma_3)\big)$. Put $M = \sigma_1 + \sigma_3 = \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$; then $M^2 = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = 2\, 1_2$, so with $r = \sqrt{2}$ we have $e^{-M} = \cosh r\, 1_2 - \frac{\sinh r}{r} M$ (same computation as for a Pauli matrix but with $M^2 = 2\, 1_2$ giving the factor $1/r$). The cleanest way to see the two matrices differ is to compare traces, an invariant equal on equal matrices:
$$\operatorname{tr}\big(e^{-\sigma_3} e^{-\sigma_1}\big) = e^{-1}\cosh 1 + e\, \cosh 1 = \cosh 1\,(e^{-1} + e) = \cosh 1 \cdot 2\cosh 1 = 2\cosh^2 1 \approx 4.762,$$
$$\operatorname{tr}\big(e^{-(\sigma_1 + \sigma_3)}\big) = \operatorname{tr}\big(\cosh r\, 1_2\big) - \tfrac{\sinh r}{r}\operatorname{tr}(M) = 2\cosh\sqrt{2} - 0 \approx 2 \times 2.178 = 4.356,$$
using $\operatorname{tr}(M) = 1 + (-1) = 0$. Since $4.762 \ne 4.356$ the traces differ, hence $e^{-\sigma_3} e^{-\sigma_1} \ne e^{-(\sigma_1 + \sigma_3)}$, that is
$$\mathcal{P}\exp\!\left(-\int_0^2 A\right) \ne \exp\!\left(-\int_0^2 A\right).$$
The obstruction is exactly $[\sigma_1, \sigma_3] \ne 0$: the path-ordered exponential keeps the two evolutions in temporal order and does not let them be added inside a single exponential.

**Calibration check.** Three verifications a reader can carry out from the page.

*Value at $t = 0$ is the identity.* From $(2.13)$ every integral $\int_0^0 \cdots$ over a nondegenerate simplex vanishes for $j \ge 1$, leaving only the $j = 0$ term $1_n$; equivalently $B(0) = 0$ makes even the naive $\exp(-B(0)) = 1_n$, consistent with $v(0) = 1_n\, v_0 = v_0$. So $\mathcal{P}\exp\big({-}\int_0^0 A\big) = 1_n$.

*Invertibility.* The operator $U(t) := \mathcal{P}\exp\big({-}\int_0^t A\big)$ is invertible for every $t$. Let $W : I \to \operatorname{Mat}(n \times n; \mathbb{K})$ solve the "right" linear equation $\dot W(t) = W(t)\, A(t)$ with $W(0) = 1_n$ (this is again a linear system, so it has a unique global solution by the same existence theorem, applied to each row of $W$). Then
$$\frac{d}{dt}\big(W(t) U(t)\big) = \dot W U + W \dot U = W A\, U + W(-A\, U) = W A U - W A U = 0 \qquad (\dot U = -A U \text{ by } (\ast),\ \dot W = W A),$$
so $W(t) U(t)$ is constant, and at $t = 0$ it is $1_n \cdot 1_n = 1_n$; hence $W(t) U(t) = 1_n$ for all $t$. A square matrix over a field with a left inverse is invertible, so $U(t)$ is invertible with $U(t)^{-1} = W(t)$.

*The inverse is the reversed-order exponential.* The equation $\dot W = W A$ is $(2.10)$ read with the factors on the opposite side and the sign of $A$ reversed; iterating it exactly as in $(2.13)$ gives $W(t) = \sum_{j \ge 0} \int_0^t d\tau_j \cdots \int_0^{\tau_2} d\tau_1\, A(\tau_1) A(\tau_2) \cdots A(\tau_j)$, the same iterated integrals but with the matrices in the **increasing** time order (earliest on the left) and with $+$ signs — the reversed-order exponential $\overline{\mathcal{P}}\exp\big({+}\int_0^t A\big)$. Geometrically this is the transport along the reversed curve, matching property (3) of [[Def - Parallel Transport in a Principal Bundle|parallel transport]], $\Gamma(\bar c) = \Gamma(c)^{-1}$. Thus $\mathcal{P}\exp\big({-}\int_0^t A\big)^{-1} = \overline{\mathcal{P}}\exp\big({+}\int_0^t A\big)$, as claimed.

---

# Unlocked by This

> [!tip] Holonomy in a local trivialisation *(from Gauge Theory V)*
> With $A(t) = A_\alpha(\dot c(t))$ the pulled-back connection form along a loop $c$, the value $\mathcal{P}\exp\big({-}\oint_c A_\alpha\big)$ is the holonomy of the connection around $c$; the **[[Def - Holonomy Group of a Connection|holonomy group]]** is the set of all such matrices, and its structure (a subgroup, conjugation under base change) follows from the multiplicative cocycle law recorded in the Categorical section together with the properties of parallel transport.

> [!tip] The small-loop expansion and curvature *(from Gauge Theory V)*
> Expanding the Dyson series $(2.13)$ to second order for a shrinking family of loops shows that the holonomy of a small loop is $1_n$ minus the flux of the curvature through it, $\operatorname{hol}(c_L) = 1_n - \int_{S_L} F + O(L^3)$, with the non-abelian term $A \wedge A$ arising exactly from the ordering the path-ordered exponential enforces. This is proved in **Curvature is the Infinitesimal Holonomy**.

> [!tip] The abelian case and Stokes *(from Gauge Theory V)*
> When the structure group is abelian the commuting corollary above turns the loop holonomy into $\exp\big({-}\oint_c A_\alpha\big) = \exp\big({-}\int_S dA_\alpha\big)$ by Stokes' theorem, expressing holonomy directly as the exponential of the enclosed curvature flux; this is proved in **Holonomy of an Abelian Connection is the Exponential of the Curvature Integral** and underlies Dirac charge quantisation in Gauge Theory VII.
