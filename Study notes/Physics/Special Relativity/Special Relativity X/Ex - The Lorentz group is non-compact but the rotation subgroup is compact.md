---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Topology of the Lorentz Group"
  - "Def - Rapidity"
  - "Def - The Lorentz Group"
tags: [physics, special-relativity, lie-groups, topology]
---

# Problem Statement

1. Show that the restricted Lorentz group $SO^+(1,3)$ is **non-compact** by exhibiting an unbounded sequence of group elements with no convergent subsequence.
2. Show that the rotation subgroup $SO(3) \subset SO^+(1,3)$ (the block matrices $\mathrm{diag}(1,R)$, $R \in SO(3)$) **is** compact.
3. Reconcile these with the product structure $SO^+(1,3) \cong \mathbb{R}^3 \times SO(3)$: identify which factor carries the non-compactness, and explain why the boosts cannot form a compact set.
4. Conclude that $SO^+(1,3)$ has no non-trivial finite-dimensional *unitary* representation, and explain in one sentence why this forces relativistic quantum theory to use fields.

**Recall:**

A topological space is **compact** if every sequence has a convergent subsequence (for subsets of a finite-dimensional matrix space, equivalently: closed and bounded, by Heine–Borel). The [[Def - The Lorentz Group|restricted Lorentz group]] $SO^+(1,3)$ is the proper orthochronous component, the matrices $\Lambda$ with $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$, $\det\Lambda = +1$, $\Lambda^0{}_0 \ge 1$.

![[Thm - Topology of the Lorentz Group#Statement]]

A boost of [[Def - Rapidity|rapidity]] $\psi$ along $x$ has matrix entries $\Lambda^0{}_0 = \Lambda^1{}_1 = \cosh\psi$, $\Lambda^0{}_1 = \Lambda^1{}_0 = \sinh\psi$, unbounded as $\psi \to \infty$.

---

# Convergent Strategy

**Problem class.** A *structural / topological* problem about the global shape of the group. The [[Special Relativity X — The Lorentz Group as a Lie Group#Problem-Solving Strategy|topic strategy]] routes all such questions through the polar decomposition and the product manifold $\mathbb{R}^3 \times SO(3)$: the boost factor is the source of non-compactness, the rotation factor the only compactness.

**Assumption pattern.** The defining matrix entries of a boost grow without bound with the rapidity — $\cosh\psi \to \infty$ — which is the signpost for non-compactness. Conversely the entries of a rotation matrix are bounded by $1$ (they are cosines and sines), the signpost for compactness. The product structure tells us these two behaviours live in separate factors.

**Theorem routing.** Part 1: exhibit boosts $\Lambda_n$ of rapidity $n$; their $(0,0)$ entries $\cosh n \to \infty$, so the sequence is unbounded, so by Heine–Borel the group is not compact ([[Thm - Topology of the Lorentz Group]]). Part 2: $SO(3)$ is closed (defined by polynomial equations $R^{\mathsf T}R = I$, $\det R = 1$) and bounded (each entry $|R_{ij}| \le 1$), hence compact. Part 3: read off the product $\mathbb{R}^3 \times SO(3)$ — the $\mathbb{R}^3$ boost factor is unbounded, the $SO(3)$ rotation factor compact. Part 4: a standard representation-theory theorem (a non-compact simple Lie group has no non-trivial finite-dimensional unitary representation) plus the observation that boosts are represented by non-unitary matrices.

**Key decision point.** The crux of part 3 is seeing *why* the boosts cannot be made into a compact set: the rapidity is a genuinely unbounded parameter (you can always boost more), so the boosts are diffeomorphic to all of $\mathbb{R}^3$, which is closed in the group but not bounded. The temptation is to think a "bounded velocity" $|v| < 1$ makes the boosts bounded — but velocity compresses the infinite rapidity line into the open interval $(-1,1)$, which is *not closed*, so the boosts are still non-compact. Rapidity, not velocity, is the honest coordinate.

---

# Legal Operations Used

1. **Read topology off the product manifold (operation 8 from the topic page).** Parts 1–3 use $SO^+(1,3) \cong \mathbb{R}^3 \times SO(3)$: a product is compact iff both factors are, and the $\mathbb{R}^3$ factor (boosts) is not.

2. **Factor a transformation by the polar decomposition (operation 7 from the topic page).** Implicit in identifying the two factors: every restricted transformation is a boost times a rotation, and the boost part ranges over the non-compact $\mathbb{R}^3$.

---

# Hints

> [!note]- Hint 1
> A set in a finite-dimensional matrix space is compact if and only if it is closed and bounded. To show $SO^+(1,3)$ is *not* compact, it suffices to find group elements with arbitrarily large entries — then the set is unbounded.

> [!note]- Hint 2
> Take the boost of rapidity $n$ along $x$, for $n = 1, 2, 3, \dots$. Its $(0,0)$ entry is $\cosh n$, which $\to \infty$. No subsequence can converge (a convergent sequence is bounded).

> [!note]- Hint 3
> For $SO(3)$: the entries of an orthogonal matrix satisfy $\sum_j R_{ij}^2 = 1$ for each row, so $|R_{ij}| \le 1$ — bounded. And $SO(3)$ is the solution set of continuous equations $R^{\mathsf T}R = I$, $\det R = 1$ — closed. Closed and bounded means compact.

> [!note]- Hint 4
> For part 3, recall that the boosts are parametrised by the rapidity vector $\boldsymbol\psi = \psi\mathbf{n} \in \mathbb{R}^3$, with no upper bound on $\psi$. Trying to use velocity $v = \tanh\psi$ instead maps the boosts to the open ball $|\mathbf{v}| < 1$, which is bounded but *not closed* — so still non-compact.

> [!note]- Hint 5
> For part 4: a boost $\exp(\psi K)$ has unbounded entries, so it cannot be a unitary matrix (unitary matrices have entries bounded by $1$). A non-trivial finite-dimensional representation that sent boosts to unitary matrices would contradict this; hence such representations are non-unitary.

---

# Solution

The non-compactness comes entirely from the boosts, whose rapidity is unbounded; the rotations are bounded and compact. The product structure $\mathbb{R}^3 \times SO(3)$ makes this precise: the $\mathbb{R}^3$ boost factor is non-compact, the $SO(3)$ factor compact, and a product is compact only if both factors are.

**Step 1: $SO^+(1,3)$ is non-compact.**

> [!note]- Derivation
> For $n \in \mathbb{N}$ let $\Lambda_n$ be the boost of rapidity $n$ along the $x$-axis,
> $$\Lambda_n = \begin{pmatrix}\cosh n & \sinh n & 0 & 0\\ \sinh n & \cosh n & 0 & 0\\ 0 & 0 & 1 & 0\\ 0 & 0 & 0 & 1\end{pmatrix} \in SO^+(1,3).$$
> Each $\Lambda_n$ is a genuine restricted Lorentz transformation ($\det = \cosh^2 n - \sinh^2 n = 1$, $\Lambda_n^0{}_0 = \cosh n \ge 1$). The $(0,0)$ entry is $\cosh n \to \infty$ as $n \to \infty$, so the sequence $(\Lambda_n)$ is unbounded. An unbounded sequence has no convergent subsequence (any convergent sequence is bounded). By the Heine–Borel criterion, a subset of a finite-dimensional matrix space is compact iff closed and bounded; $SO^+(1,3)$ contains an unbounded sequence, hence is **not compact**. $\blacksquare$

**Step 2: $SO(3)$ is compact.**

> [!note]- Derivation
> View $SO(3)$ as the set of $\mathrm{diag}(1, R)$ with $R \in SO(3)$, a subset of $\mathbb{R}^9$ (the $3\times 3$ entries). It is **bounded**: each row of $R$ is a unit vector, $\sum_j R_{ij}^2 = 1$, so every entry satisfies $|R_{ij}| \le 1$, confining $SO(3)$ to the box $[-1,1]^9$. It is **closed**: it is the simultaneous solution set of the continuous equations $R^{\mathsf T}R = I$ (nine polynomial equations) and $\det R = 1$ (one more), and the solution set of continuous equations is closed (a preimage of the closed set $\{0\}$ under a continuous map). Closed and bounded in a finite-dimensional space means **compact**. $\blacksquare$

**Step 3: The product structure localises the non-compactness.**

> [!note]- Derivation
> By [[Thm - Topology of the Lorentz Group|the topology theorem]], the polar decomposition gives a homeomorphism $SO^+(1,3) \cong \mathbb{R}^3 \times SO(3)$, the $\mathbb{R}^3$ factor being the boosts (parametrised by the rapidity vector $\boldsymbol\psi = \psi\mathbf{n}$) and the $SO(3)$ factor the rotations. A product $X \times Y$ is compact if and only if both $X$ and $Y$ are compact. Here $SO(3)$ is compact (Step 2) but $\mathbb{R}^3$ is *not* (it is unbounded), so the product is not compact — consistent with Step 1.
>
> Why can the boosts not be made compact? The boost factor is genuinely $\mathbb{R}^3$: the rapidity $\psi$ ranges over $[0,\infty)$ with no upper bound, and every rapidity vector $\boldsymbol\psi \in \mathbb{R}^3$ gives a distinct boost. One might hope to use *velocity* $v = \tanh\psi$ as coordinate instead, compressing $\psi \in [0,\infty)$ into $v \in [0,1)$ and the boosts into the open unit ball $\{|\mathbf{v}| < 1\}$. But that ball is bounded yet *not closed* — its boundary $|\mathbf{v}| = 1$ (the speed of light) is missing, and a sequence of boosts with $v_n \to 1$ has no limit in the group (the limit would be a "boost to the speed of light", which does not exist). So whether one uses rapidity (unbounded) or velocity (bounded but open), the boosts are non-compact. The non-compactness is intrinsic: there is no ceiling on boosting.

**Step 4: No non-trivial finite-dimensional unitary representation.**

> [!note]- Derivation
> A unitary matrix $U$ satisfies $U^\dagger U = I$, which forces every entry to satisfy $|U_{ij}| \le 1$ (each column is a unit vector) — so the unitary group $U(N)$ is *bounded*, hence compact. Now suppose $\rho : SO^+(1,3) \to U(N)$ were a continuous non-trivial finite-dimensional unitary representation. Consider the boosts $\Lambda_n$ of rapidity $n$: in any *faithful* finite-dimensional representation their images $\rho(\Lambda_n)$ would have to grow unboundedly (a boost is represented by a non-compact one-parameter subgroup, $\rho(\exp(\psi K)) = \exp(\psi\,\mathrm{d}\rho(K))$, which is bounded only if $\mathrm{d}\rho(K) = 0$). But $\rho(\Lambda_n) \in U(N)$ is bounded by $1$ — a contradiction unless $\mathrm{d}\rho(K) = 0$ for all boost generators $K$. Since the boosts generate $SO^+(1,3)$ together with the rotations and the algebra is simple, $\mathrm{d}\rho$ killing all boosts forces $\mathrm{d}\rho = 0$, so $\rho$ is trivial. Hence the only finite-dimensional unitary representation is the trivial one.
>
> **One-sentence consequence:** since a relativistic quantum theory needs *unitary* representations (probabilities must be conserved) and those are infinite-dimensional for the non-compact Lorentz group, a relativistic quantum object cannot be described by a finite-component wavefunction transforming unitarily — it must be a **field**, carrying a finite-dimensional *non-unitary* representation at the level of components while its states fill an infinite-dimensional Hilbert space.

> [!note]- Complete formal solution
> The boosts $\Lambda_n$ of rapidity $n$ have $(0,0)$ entry $\cosh n \to \infty$, so $SO^+(1,3)$ contains an unbounded sequence and is non-compact (Heine–Borel). The rotation subgroup $\{\mathrm{diag}(1,R) : R \in SO(3)\}$ is closed (solution set of $R^{\mathsf T}R = I$, $\det R = 1$) and bounded ($|R_{ij}| \le 1$), hence compact. The polar decomposition gives $SO^+(1,3) \cong \mathbb{R}^3 \times SO(3)$; a product is compact iff both factors are, and the boost factor $\mathbb{R}^3$ is non-compact (rapidity unbounded; even in velocity coordinates the boosts fill the *open* ball $|\mathbf{v}|<1$, bounded but not closed). Finally, unitary matrices are bounded, so a boost — represented by an unbounded one-parameter subgroup unless trivially — cannot map into $U(N)$ nontrivially; hence the only finite-dimensional unitary representation of $SO^+(1,3)$ is trivial, forcing relativistic quantum theory onto infinite-dimensional (field) representations. $\blacksquare$

---

# Key Takeaways

**Non-compactness lives in the boosts because the rapidity is unbounded — and velocity does not save you.** The whole non-compactness of the Lorentz group is the single fact that you can always boost a little more: the rapidity ranges over $[0,\infty)$ with no ceiling, so the boost matrices have unbounded entries ($\cosh\psi \to \infty$). The instinct to bound the boosts by noting $|v| < 1$ fails on a subtle point — velocity compresses the infinite rapidity line into the *open* interval $(-1,1)$, bounded but not closed, and the missing endpoint (the speed of light) is exactly where the would-be limit lives. The diagnostic to carry: a one-parameter subgroup is non-compact iff its parameter ranges over an unbounded or non-closed set, and for the Lorentz boosts both the rapidity description (unbounded) and the velocity description (open) confirm non-compactness. This is the structural reason "boost" and "rotation" feel categorically different: rotations close up (compact circle), boosts run off to infinity (non-compact line).

**The product manifold localises every topological property to one factor.** The decomposition $SO^+(1,3) \cong \mathbb{R}^3 \times SO(3)$ is the master tool for the group's topology, and the principle it exploits is that topological properties of a product are determined factor-by-factor: a product is compact iff both factors are, connected iff both are, and its fundamental group is the product of the factors' fundamental groups. So non-compactness is traced to the $\mathbb{R}^3$ boost factor, while in the companion exercise the non-trivial fundamental group $\mathbb{Z}/2$ is traced to the $SO(3)$ rotation factor. The trigger for this technique is any global question about the Lorentz group; the move is always to split into boosts and rotations and ask the question of each factor separately. The boosts, being a contractible $\mathbb{R}^3$, contribute non-compactness but no fundamental group; the rotations, being a compact $\mathbb{R}\mathbb{P}^3$, contribute compactness-of-that-factor and all the interesting topology.

**Non-compactness has a sharp representation-theoretic consequence that shapes all of quantum field theory.** The chain "non-compact $\Rightarrow$ no non-trivial finite-dimensional unitary representation $\Rightarrow$ relativistic quantum states need infinite-dimensional representations $\Rightarrow$ fields" is one of the deepest structural facts in physics, and it follows from the elementary observation that unitary matrices are bounded while boosts are not. A compact group like $SO(3)$ has finite-dimensional unitary representations (the spin-$j$ multiplets), which is why a non-relativistic particle can be described by a finite-component spinor wavefunction. The Lorentz group's non-compactness removes this option: its finite-dimensional representations (the $(j_A,j_B)$ of the [[Thm - The Complexification of so(1,3) and the (A,B) Decomposition|complexification]]) are necessarily *non-unitary*, and the unitary representations that carry conserved-probability quantum states are infinite-dimensional — they are the one-particle Hilbert spaces of the Wigner classification. This is the precise sense in which special relativity *forces* the transition from quantum mechanics (wavefunctions) to quantum field theory (fields): the symmetry group is too big, in the non-compact direction, to act unitarily on a finite-dimensional space.
