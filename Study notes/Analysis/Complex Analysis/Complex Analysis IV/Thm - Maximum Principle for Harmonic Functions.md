---
type: theorem
subject: complex-analysis
prereqs:
  - "Def - Harmonic Function"
  - "Thm - Mean Value Property of Harmonic Functions"
tags: [analysis, complex-analysis, pde]
---

# Notation

$u : D \to \mathbb{R}$ is harmonic on a domain (open, connected) $D \subseteq \mathbb{R}^2 \cong \mathbb{C}$. Full registry on [[Complex Analysis IV — Mapping Theory and Applications]].

---

# Motivation

The maximum principle says: a non-constant harmonic function on a domain does not attain a local maximum (or minimum) in the interior. All maxima and minima are on the boundary.

This is a powerful constraint. It immediately gives **uniqueness for the Dirichlet problem**: two harmonic functions with the same boundary values must agree in the interior. (Their difference is harmonic with zero boundary values; by the maximum/minimum principle, the difference is zero everywhere.)

The principle also has versions for *subharmonic* and *superharmonic* functions, and generalizes to higher dimensions, to elliptic operators beyond the Laplacian, and even to certain parabolic equations.

It is a *qualitative* constraint that captures the geometric meaning of "$\Delta u = 0$": harmonic functions are perfectly balanced averages, with no internal sources or sinks, hence no internal "peaks" or "valleys".

---

# Sources and Targets

**Sources (Input Broadening)**

**Harmonic function on a bounded domain.** Most common: $u$ harmonic on a domain $D$, continuous on $\overline{D}$.

**Real part of holomorphic.** Bridge: real parts of holomorphic functions are harmonic; apply max principle to them.

**Subharmonic function ($\Delta u \geq 0$).** Property $B$: weaker. Bridge: a maximum principle holds (no interior max); but a minimum principle fails (can have interior min). Used in Perron method.

**Targets (Output Amplification)**

Combine with **uniqueness for Dirichlet problem.** Property $D$: two harmonic functions with same boundary data. Amplified result $E$: they are equal (apply max principle to their difference).

Combine with **Hopf maximum principle.** Property $D$: $u$ achieves max at a smooth boundary point. Amplified result $E$: $\partial u/\partial n > 0$ at that point (outer normal derivative is strictly positive). The "boundary point lemma" used in PDE.

Combine with **stochastic interpretation.** Property $D$: $u$ harmonic, $B_t$ Brownian motion stopped at first exit from $D$. Amplified result $E$: $u(z) = \mathbb{E}_z[u(B_\tau)]$ — the expected value at the exit point. Max principle says $u \leq \max_{\partial D}$.

---

# Why Is It True

The proof uses the mean value property. Suppose $u$ attains an interior max at $a \in D$: $u(a) \geq u(z)$ for all $z \in D$, with equality at $a$. By the [[Thm - Mean Value Property of Harmonic Functions|mean value property]] on a small circle around $a$:
$$u(a) = \frac{1}{2\pi}\int_0^{2\pi} u(a + re^{i\theta})\,d\theta.$$
Since $u(a + re^{i\theta}) \leq u(a)$ for all $\theta$, the average equals $u(a)$ only if $u(a + re^{i\theta}) = u(a)$ for all $\theta$ (otherwise the integrand is strictly less than $u(a)$ somewhere, making the integral less than $u(a)$).

So $u \equiv u(a)$ on the entire circle. By varying $r$ (in a small range), $u \equiv u(a)$ on a small *disc* around $a$.

By connectedness of $D$: the set $\{z \in D : u(z) = u(a)\}$ is nonempty (contains $a$), closed (by continuity of $u$), and open (by the local argument above). So it is all of $D$, meaning $u$ is constant.

So a non-constant harmonic function cannot have an interior maximum. By the same argument with $-u$ in place of $u$: no interior minimum.

---

# What Makes This Hard

The non-obvious step is **using the mean value property to derive a contradiction from a local maximum**. Students often try to use the Laplacian condition $\Delta u = 0$ directly (e.g., second-derivative-test arguments), but these only work at non-degenerate critical points. The mean value approach is the cleanest, working in full generality.

A common mistake is to forget that max principle applies to *non-constant* harmonic functions; constants are harmonic and trivially attain their (constant) maximum everywhere.

---

# Rederivation Scaffold

**High-level strategy:**
Suppose $u$ attains an interior max at $a$. By mean value, $u(a) = $ average on a small circle. Average = max implies pointwise equality, so $u \equiv u(a)$ locally. By connectedness, $u$ constant.

**Subgoal decomposition:**

1. **Suppose $u(a) = \max u$ over $D$**, with $a \in D$.

2. **Apply mean value on a small circle.** $u(a) = $ average of $u$ on $|z - a| = r$.

3. **Average $=$ max implies pointwise equality.** $u(a + re^{i\theta}) = u(a)$ for all $\theta$.

4. **Locally constant.** $u \equiv u(a)$ on a small disc around $a$.

5. **By connectedness, globally constant.** The set $\{u = u(a)\}$ is open (Step 4), closed (continuity), nonempty ($a \in $); by connectedness of $D$, this set is all of $D$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $u : D \to \mathbb{R}$ be harmonic on a domain $D$, with an interior maximum at $a \in D$: $u(a) = \sup_D u$. We show $u$ is constant.
>
> Define $S = \{z \in D : u(z) = u(a)\}$.
> - **$S$ nonempty**: $a \in S$.
> - **$S$ closed in $D$**: $S = u^{-1}(\{u(a)\}) = $ preimage of a single point under the continuous $u$, hence closed.
> - **$S$ open in $D$**: take $a' \in S$, so $u(a') = u(a)$. Choose $r > 0$ with $\overline{D(a', r)} \subset D$. By the mean value property:
>   $$u(a') = \frac{1}{2\pi}\int_0^{2\pi} u(a' + re^{i\theta})\,d\theta.$$
>   Since $u(a' + re^{i\theta}) \leq u(a) = u(a')$ for all $\theta$, the integral equals $u(a')$ only if $u(a' + re^{i\theta}) = u(a')$ for all $\theta$. Hence $u \equiv u(a)$ on the entire circle $|z - a'| = r$. The same argument applies for all smaller radii, giving $u \equiv u(a)$ on the entire closed disc $\overline{D(a', r)}$. So $D(a', r) \subset S$, hence $a'$ is interior to $S$. So $S$ is open.
>
> By connectedness of $D$ and $S \subseteq D$ nonempty, closed, and open in $D$: $S = D$. So $u \equiv u(a)$ on $D$ — constant.
>
> Contrapositive: a non-constant harmonic function does not attain an interior maximum.
>
> **Minimum principle.** Apply the maximum principle to $-u$: a non-constant harmonic $u$ does not attain an interior minimum. $\blacksquare$
>
> **Boundary form.** If $u$ is harmonic on a *bounded* domain $D$, continuous on $\overline{D}$, and non-constant, then $u(z) < \sup_{\partial D} u$ and $u(z) > \inf_{\partial D} u$ for all $z \in D$. So all interior values are strictly between the boundary supremum and infimum.

---

# Cross-Field Exercise Suggestions

**Uniqueness of Dirichlet problem.** If $u_1, u_2$ are harmonic on $D$ with same boundary values on $\partial D$, then $u_1 - u_2$ is harmonic with zero boundary values. By max/min, $u_1 - u_2 \equiv 0$. Hence Dirichlet solutions are unique.

**Maximum modulus from maximum principle.** For a holomorphic $f$ on $D$, the function $u = \log|f|$ is harmonic on $\{f \neq 0\}$, so by the max principle (and a continuity argument at zeros), $|f|$ has no interior maximum. This is the maximum modulus principle, derived from the harmonic max principle.

**Stability of the heat equation.** For the heat equation $u_t = \Delta u$ on a bounded $D \times [0, T]$, a maximum principle holds: the max/min are attained on the parabolic boundary (initial time + spatial boundary). Used in proving stability and uniqueness for parabolic PDEs.

---

# Bridges

- **[[Thm - Mean Value Property of Harmonic Functions]]** — the engine.

- **Maximum modulus principle** (in CA II) — the holomorphic analog.

- **[[Thm - Poisson Integral Formula]]** — uses uniqueness from max principle.

---

# Unlocked by This

> [!tip] Uniqueness of Dirichlet Solutions *(from PDE)*
> Direct corollary: Dirichlet problems on bounded domains have at most one solution.

> [!tip] Hopf Boundary Point Lemma *(from PDE)*
> A strengthened version: max principle plus boundary regularity gives sign of normal derivative at boundary maxima. Crucial in elliptic PDE theory.

> [!tip] Phragmén–Lindelöf Principle *(from Complex Analysis)*
> An extension to unbounded domains: under growth conditions at infinity, the maximum modulus principle still holds. Used in the theory of entire functions of finite order.
