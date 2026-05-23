---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - de Rham Cohomology"
  - "Def - Differential k-Form on a Manifold"
  - "Def - Exterior Derivative on a Manifold"
  - "Def - Partition of Unity on a Manifold"
tags: [geometry, differential-geometry, cohomology, mayer-vietoris]
---

# Notation

$M$ is a smooth manifold; $U, V \subseteq M$ are open subsets with $U \cup V = M$. The four inclusions are $i : U \cap V \hookrightarrow U$, $j : U \cap V \hookrightarrow V$, $k : U \hookrightarrow M$, $l : V \hookrightarrow M$. The pullback maps on forms are denoted by the same letters with a star: $i^*, j^*, k^*, l^*$. The de Rham cohomology $H^p_{dR}$ is as in [[Def - de Rham Cohomology]].

---

# Statement

> **Theorem (Mayer–Vietoris Sequence).** Let $M$ be a smooth manifold and $U, V$ open subsets with $U \cup V = M$. For each $p \geq 0$, there is a linear **connecting homomorphism** $\delta : H^p_{dR}(U \cap V) \to H^{p+1}_{dR}(M)$ such that the following long sequence is exact:
> $$\cdots \xrightarrow{\delta} H^p_{dR}(M) \xrightarrow{(k^*, l^*)} H^p_{dR}(U) \oplus H^p_{dR}(V) \xrightarrow{i^* - j^*} H^p_{dR}(U \cap V) \xrightarrow{\delta} H^{p+1}_{dR}(M) \xrightarrow{(k^*, l^*)} \cdots$$
>
> Here "exact" means the image of each map equals the kernel of the next. The sequence starts in degree $0$:
> $$0 \to H^0_{dR}(M) \to H^0_{dR}(U) \oplus H^0_{dR}(V) \to H^0_{dR}(U \cap V) \to H^1_{dR}(M) \to \cdots$$

> **Corollary (computational principle).** When two of three of $H^*(U)$, $H^*(V)$, $H^*(U \cap V)$ are known, the third — and therefore $H^*(M)$ — is determined by exactness.

> **Corollary (application to $S^n$).** Covering $S^n$ by two open hemispheres (each contractible, intersection $\simeq S^{n-1}$), the sequence gives, by induction on $n$,
> $$H^p_{dR}(S^n) = \begin{cases} \mathbb{R} & p = 0 \text{ or } p = n \\ 0 & 0 < p < n. \end{cases}$$

---

# Motivation

After the Poincaré lemma — which kills cohomology on contractible pieces — the next natural question is: how does cohomology *assemble* from contractible pieces? Given a manifold cut into two open sets $U$ and $V$, we want to compute $H^*(M)$ from $H^*(U)$, $H^*(V)$, and $H^*(U \cap V)$. The Mayer–Vietoris theorem is the precise answer.

The point of the sequence is that the cohomologies are not freely related — they are tied together by a *long exact sequence*, which lets you compute any one term from the others by exactness. When $U$ and $V$ are contractible (so $H^*(U) = H^*(V) = 0$ in positive degrees), the entire cohomology of $M$ is captured by the cohomology of the intersection $U \cap V$, shifted by one degree via the connecting map. This is the engine behind every concrete computation: for $S^n$, the two contractible hemispheres meet in $S^{n-1} \times (-\epsilon, \epsilon) \simeq S^{n-1}$, and the sequence gives $H^*(S^n)$ from $H^*(S^{n-1})$ via degree shift, allowing induction.

The conceptual content is that *cohomology is computable from local data*. The Poincaré lemma is the most local statement — a single contractible piece has trivial cohomology — and Mayer–Vietoris is the gluing rule that turns local triviality into a computation for the global object. Every "good cover" computation (by sets diffeomorphic to balls), and by extension every cohomology computation, can in principle be done by iterating Mayer–Vietoris.

The proof at the form level is a piece of homological-algebra magic. The short exact sequence

$$0 \to \Omega^p(M) \xrightarrow{(k^*, l^*)} \Omega^p(U) \oplus \Omega^p(V) \xrightarrow{i^* - j^*} \Omega^p(U \cap V) \to 0$$

is exact at every degree (we will prove this — the surjectivity is the non-trivial part and uses a partition of unity). The **zigzag lemma** (or **snake lemma**, in the version for short exact sequences of complexes) then produces the long exact sequence in cohomology. The connecting map $\delta$ has an explicit construction: given a closed $p$-form $\omega$ on $U \cap V$, write $\omega = \omega_U|_{U \cap V} - \omega_V|_{U \cap V}$ using a partition of unity (the surjectivity step), then $d\omega_U = d\omega_V$ on $U \cap V$ — so the pair $d\omega_U$ on $U$, $d\omega_V$ on $V$ patches to a *global* $(p+1)$-form $\eta$ on $M$, closed by $d^2 = 0$ — and $\delta[\omega] := [\eta]$.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is: *$M = U \cup V$ for open $U, V \subseteq M$, with knowledge of $H^*(U)$, $H^*(V)$, and $H^*(U \cap V)$.*

The first disguised source is **a manifold with a natural decomposition into "half-pieces."** Property $B$: $M$ has a structure that suggests a two-set cover — e.g. a sphere has two hemispheres, a torus has a product structure $S^1 \times S^1$ that suggests a product cover, a projective space has an affine chart plus complement. The bridge: each such structural feature gives a natural Mayer–Vietoris cover. *Example:* the cover of $S^n$ by $U = S^n \setminus \{N\}$, $V = S^n \setminus \{S\}$ — each contractible, intersection $\simeq S^{n-1}$.

The second disguised source is **a manifold built by gluing.** Property $B$: $M$ is constructed as a quotient $X \sqcup_\phi Y$ along a smooth $\phi : Z \to X, Y$ where $Z = X \cap Y$ is a thickened submanifold. The bridge: open thickenings $U \supset X$, $V \supset Y$ in $M$ realize $X, Y$ as deformation retracts, with $U \cap V$ a deformation retract onto $Z$. *Example:* the connect sum $M_1 \# M_2$ along a sphere, with the cover by enlarged $M_1$ and $M_2$ with intersection $\simeq S^{n-1} \times \mathbb{R}$.

The third disguised source is **the existence of a good cover by contractibles.** Property $B$: $M$ admits a cover by open sets each diffeomorphic to a ball, with all finite intersections also diffeomorphic to balls (a *good cover*). The bridge: iterating Mayer–Vietoris on consecutive enlargements computes $H^*(M)$ entirely from the combinatorics of the cover — the **Čech–de Rham spectral sequence**. *Example:* every smooth manifold admits a good cover (by geodesic balls in any Riemannian metric, or by domains of charts in a refined atlas).

**Targets (Output Amplification)**

The conclusion $C$: *a long exact sequence relating $H^*(M)$ to $H^*(U)$, $H^*(V)$, $H^*(U \cap V)$.*

Combine $C$ with **knowledge of all but one term.** When three out of four of the cohomology groups in any segment of the sequence are known, exactness determines the fourth. The further result $E$: cohomology of $M$ is computed by reducing to simpler manifolds. This is the standard pattern in every Mayer–Vietoris application.

Combine $C$ with **the Poincaré lemma making $U, V$ trivial.** If $U$ and $V$ are contractible, then $H^p(U) = H^p(V) = 0$ for $p \geq 1$, so the sequence reduces to
$$0 \to \mathbb{R} \to \mathbb{R}^2 \to H^0(U \cap V) \to H^1(M) \to 0 \to 0 \to H^1(U \cap V) \to H^2(M) \to 0 \to \cdots$$
giving $H^p(M) \cong H^{p-1}(U \cap V)$ for $p \geq 2$ and the slightly delicate degree-1 computation. The further result $E$: the cohomology of $M$ is entirely determined by that of $U \cap V$, shifted by one. This is the computational core of the sphere computation.

Combine $C$ with **iteration on a good cover.** Starting with the cover $\{U_1, U_2\}$, then enlarging to $\{U_1 \cup U_2, U_3\}$, then $\{U_1 \cup U_2 \cup U_3, U_4\}$, etc., we compute $H^*$ inductively. The further result $E$: cohomology of any manifold is computable from a finite good cover plus iterated Mayer–Vietoris — the structural foundation of Čech-de Rham theory.

---

# Why Is It True

**The single sentence: the form-level short exact sequence is exact (the kernel of "restrict to each piece" equals the global forms, and surjectivity onto $\Omega^*(U \cap V)$ comes from a partition of unity splitting), and the zigzag lemma turns short exact sequences of complexes into long exact sequences of cohomologies.**

The argument has two halves: a form-level claim and a homological-algebra mechanism.

*Form level: the short exact sequence*
$$0 \to \Omega^p(M) \xrightarrow{(k^*, l^*)} \Omega^p(U) \oplus \Omega^p(V) \xrightarrow{i^* - j^*} \Omega^p(U \cap V) \to 0$$
is exact at every degree.

Injectivity at $\Omega^p(M)$: a form $\omega$ on $M$ with $\omega|_U = 0$ and $\omega|_V = 0$ must be zero everywhere (since $U \cup V = M$). So $(k^*, l^*)$ is injective.

Exactness in the middle: $(\omega_U, \omega_V) \in \Omega^p(U) \oplus \Omega^p(V)$ comes from a global form iff $\omega_U|_{U \cap V} = \omega_V|_{U \cap V}$ iff $i^*\omega_U - j^*\omega_V = 0$. So the image of $(k^*, l^*)$ equals the kernel of $i^* - j^*$.

Surjectivity onto $\Omega^p(U \cap V)$: given $\eta \in \Omega^p(U \cap V)$, we need $\omega_U \in \Omega^p(U)$ and $\omega_V \in \Omega^p(V)$ with $\omega_U|_{U \cap V} - \omega_V|_{U \cap V} = \eta$. Use a smooth partition of unity $\{\rho_U, \rho_V\}$ subordinate to $\{U, V\}$ (so $\mathrm{supp}\,\rho_U \subseteq U$, $\mathrm{supp}\,\rho_V \subseteq V$, and $\rho_U + \rho_V = 1$ on $M$). Define $\omega_U \in \Omega^p(U)$ by $\omega_U = \rho_V \eta$ on $U \cap V$ and $\omega_U = 0$ on $U \setminus \mathrm{supp}\,\rho_V$; this extends smoothly because $\rho_V \eta$ vanishes near $\partial(U \cap V) \cap U$. Similarly $\omega_V = -\rho_U \eta$ on $U \cap V$, $0$ on $V \setminus \mathrm{supp}\,\rho_U$. Then on $U \cap V$, $\omega_U - \omega_V = \rho_V \eta - (-\rho_U \eta) = (\rho_U + \rho_V)\eta = \eta$. So the surjectivity holds.

*Homological algebra: the zigzag lemma.* Given any short exact sequence of cochain complexes
$$0 \to A^* \to B^* \to C^* \to 0,$$
there is a natural long exact sequence on cohomology:
$$\cdots \to H^p(A) \to H^p(B) \to H^p(C) \xrightarrow{\delta} H^{p+1}(A) \to \cdots$$
The connecting map $\delta : H^p(C) \to H^{p+1}(A)$ is constructed by "tracing the zigzag": lift a class in $C$ to an element in $B$, apply $d$ in $B$, observe it lies in $A$ (since $d$ commutes with the maps), record this $A$-class. The result is well-defined, linear, and makes the sequence exact at every spot. The lemma's proof is a diagram chase using the snake-lemma technique.

Applied to our short exact sequence (parameterized by $p$, with $A = \Omega(M)$, $B = \Omega(U) \oplus \Omega(V)$, $C = \Omega(U \cap V)$), the zigzag lemma produces the Mayer–Vietoris sequence as stated.

The explicit construction of $\delta$ has a beautiful concrete meaning: given a closed form $\eta$ on $U \cap V$, lift via the partition of unity to $\omega_U$ on $U$ and $\omega_V$ on $V$ with $\omega_U - \omega_V = \eta$ on $U \cap V$. Then $d\omega_U$ on $U$ and $d\omega_V$ on $V$ agree on $U \cap V$ (since $d\eta = 0$ implies $d\omega_U = d\omega_V$ there), so they patch to a global form $\zeta$ on $M$ — and $[\zeta] = \delta[\eta]$. The connecting map *moves the discrepancy between local primitives up one degree*.

---

# What Makes This Hard

The conceptual obstacle is recognizing that **a short exact sequence of complexes mechanically generates a long exact sequence of cohomologies, via the zigzag lemma** — this is a piece of homological algebra that does not depend on geometry but is unfamiliar at first. The non-obvious step in the proof is the **surjectivity of $i^* - j^* : \Omega^*(U) \oplus \Omega^*(V) \to \Omega^*(U \cap V)$**: every form on the intersection must split as a difference of forms on the pieces, and the partition of unity is what makes this work (a form on $U \cap V$ can be smoothly extended by zero into the rest of $U$ via multiplication by a partition function). The most common error is to forget the partition-of-unity step and assume restriction-only maps are surjective — they aren't, in general.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Verify the short exact sequence of complexes at the form level (using a partition of unity for surjectivity); apply the standard zigzag lemma of homological algebra to extract the long exact sequence in cohomology.

**Subgoal decomposition:**

1. **Form-level short exact sequence — injectivity.** Show $(k^*, l^*) : \Omega^p(M) \to \Omega^p(U) \oplus \Omega^p(V)$ is injective.
   - *Hint:* If $\omega|_U = 0$ and $\omega|_V = 0$ then $\omega = 0$ on $U \cup V = M$.
   - *Why needed:* It is the exactness at $\Omega^p(M)$.

2. **Form-level — exactness in the middle.** Show $\mathrm{image}(k^*, l^*) = \ker(i^* - j^*)$.
   - *Hint:* A pair $(\omega_U, \omega_V)$ comes from a global form iff its restrictions to $U \cap V$ agree.
   - *Why needed:* It is the exactness at $\Omega^p(U) \oplus \Omega^p(V)$.

3. **Form-level — surjectivity via partition of unity.** Show every $\eta \in \Omega^p(U \cap V)$ is of the form $i^*\omega_U - j^*\omega_V$ for some $\omega_U \in \Omega^p(U)$, $\omega_V \in \Omega^p(V)$.
   - *Hint:* Use a partition $\{\rho_U, \rho_V\}$ subordinate to $\{U, V\}$ and set $\omega_U = \rho_V \eta$, $\omega_V = -\rho_U \eta$ (extended by zero).
   - *Why needed:* It is the exactness at $\Omega^p(U \cap V)$, the non-trivial part of the short exact sequence.

4. **Apply the zigzag lemma.** From the short exact sequence of complexes
   $$0 \to \Omega^*(M) \to \Omega^*(U) \oplus \Omega^*(V) \to \Omega^*(U \cap V) \to 0,$$
   the standard homological algebra construction gives a long exact sequence in cohomology with explicit connecting map $\delta$.
   - *Hint:* The connecting map: lift $\eta \in Z^p(U \cap V)$ to $\omega_U, \omega_V$ via partition of unity; then $d\omega_U = d\omega_V$ on $U \cap V$, so they patch to a global form, which is $\delta[\eta]$.
   - *Why needed:* It is the final assembly into the long exact sequence.

---

# Lemma Decomposition

> [!note]- Lemma 1: Partition of unity surjectivity
> **Statement:** Let $\{U, V\}$ be an open cover of $M$ with smooth partition of unity $\{\rho_U, \rho_V\}$ ($\mathrm{supp}\,\rho_U \subseteq U$, $\mathrm{supp}\,\rho_V \subseteq V$, $\rho_U + \rho_V = 1$). For every $\eta \in \Omega^p(U \cap V)$, there exist $\omega_U \in \Omega^p(U)$ and $\omega_V \in \Omega^p(V)$ such that $\omega_U|_{U \cap V} - \omega_V|_{U \cap V} = \eta$.
>
> **Hint:** Define $\omega_U$ on $U$ to be $\rho_V \eta$ on $U \cap V$ and zero elsewhere; check smooth extendability using the support condition.
>
> **Why needed:** This is the only non-trivial part of the form-level short exact sequence; it is what makes the *cohomological* Mayer–Vietoris work.
>
> > [!note]- Full proof
> > Define $\omega_U \in \Omega^p(U)$ by setting $\omega_U = \rho_V \eta$ on $U \cap V$. Outside $U \cap V$ but in $U$, $\rho_V$ is zero (since $\mathrm{supp}\,\rho_V \subseteq V$, and we are in $U \setminus V$), so $\omega_U$ extends smoothly by zero to all of $U$. The extension is smooth because $\rho_V \eta$ has support contained in $\mathrm{supp}\,\rho_V \subseteq V$, so near the boundary of $U \cap V$ in $U$ the form $\rho_V \eta$ smoothly tends to zero.
> >
> > Similarly $\omega_V \in \Omega^p(V)$ defined by $-\rho_U \eta$ on $U \cap V$, extended by zero.
> >
> > On $U \cap V$: $\omega_U - \omega_V = \rho_V \eta - (-\rho_U \eta) = (\rho_V + \rho_U)\eta = 1 \cdot \eta = \eta$.

> [!note]- Lemma 2: The zigzag lemma
> **Statement:** Given a short exact sequence of cochain complexes
> $$0 \to A^* \xrightarrow{\alpha} B^* \xrightarrow{\beta} C^* \to 0,$$
> there exists a natural connecting homomorphism $\delta : H^p(C^*) \to H^{p+1}(A^*)$ such that the sequence
> $$\cdots \to H^p(A) \xrightarrow{\alpha_*} H^p(B) \xrightarrow{\beta_*} H^p(C) \xrightarrow{\delta} H^{p+1}(A) \xrightarrow{\alpha_*} \cdots$$
> is exact.
>
> **Hint:** Construct $\delta$ by chasing the diagram: given $[c] \in H^p(C)$, lift to $b \in B^p$ with $\beta(b) = c$; then $\beta(db) = d(\beta b) = dc = 0$, so $db = \alpha(a)$ for some $a \in A^{p+1}$. Set $\delta[c] := [a]$.
>
> **Why needed:** This is the homological-algebra mechanism that turns a short exact sequence of complexes into a long exact sequence of cohomologies. It is general (not de-Rham-specific) and is the basis of every long-exact-sequence construction in cohomology theory.
>
> > [!note]- Full proof
> > *Construction of $\delta$.* For $[c] \in H^p(C)$, choose any $b \in B^p$ with $\beta(b) = c$ (possible by surjectivity of $\beta$). Then $\beta(db) = d\beta(b) = dc = 0$ (since $c$ is closed). By exactness at $B$, $db = \alpha(a)$ for some unique $a \in A^{p+1}$ (uniqueness because $\alpha$ is injective). Check $a$ is closed: $\alpha(da) = d\alpha(a) = d(db) = 0$, and $\alpha$ injective gives $da = 0$. Set $\delta[c] := [a]$.
> >
> > *Well-definedness.* If $b'$ is another lift, $\beta(b - b') = 0$, so $b - b' = \alpha(a'')$ for some $a''$. Then $db - db' = d\alpha(a'') = \alpha(da'')$, so the new $a$ is $a - da''$, differing from $a$ by an exact form — same class. If $[c]$ is changed to $[c + dc']$, lift $dc'$ to $\alpha(\text{something exact in } A)$, again same class.
> >
> > *Exactness.* The three exactness verifications (at $H^p(A)$, $H^p(B)$, $H^p(C)$) are similar diagram chases. For instance, exactness at $H^p(C)$: $\delta \beta_* = 0$ by direct computation; if $\delta[c] = 0$, the class $[a]$ in $H^{p+1}(A)$ is zero, so $a = da'$ for some $a' \in A^p$; then $b - \alpha(a')$ lifts $c$ and is closed, giving $[c] = \beta_*[b - \alpha a']$ in the image of $\beta_*$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $M = U \cup V$ with $U, V$ open. We prove the Mayer–Vietoris sequence in three steps.
>
> **Step 1 — Form-level short exact sequence.** For each $p$, the sequence
> $$0 \to \Omega^p(M) \xrightarrow{(k^*, l^*)} \Omega^p(U) \oplus \Omega^p(V) \xrightarrow{i^* - j^*} \Omega^p(U \cap V) \to 0$$
> is exact.
>
> *Injectivity of $(k^*, l^*)$.* If $\omega \in \Omega^p(M)$ with $k^*\omega = 0$ and $l^*\omega = 0$, then $\omega = 0$ on $U$ and on $V$. Since $M = U \cup V$, $\omega = 0$ on $M$.
>
> *Exactness in the middle.* If $\omega \in \Omega^p(M)$, then $i^*k^*\omega - j^*l^*\omega = (k \circ i)^*\omega - (l \circ j)^*\omega = \omega|_{U \cap V} - \omega|_{U \cap V} = 0$. Conversely, if $(\omega_U, \omega_V)$ satisfies $i^*\omega_U = j^*\omega_V$ (i.e. $\omega_U$ and $\omega_V$ agree on $U \cap V$), they patch to a smooth form $\omega \in \Omega^p(M)$.
>
> *Surjectivity.* By Lemma 1, every $\eta \in \Omega^p(U \cap V)$ is of the form $\omega_U|_{U \cap V} - \omega_V|_{U \cap V}$ for $\omega_U, \omega_V$ on $U, V$ respectively.
>
> **Step 2 — The short exact sequence is a sequence of cochain complexes.** The maps $(k^*, l^*)$ and $i^* - j^*$ commute with the exterior derivative $d$, so the sequence above is a short exact sequence of cochain complexes (not just vector spaces at each degree). Indeed, $d k^* = k^* d$ and similarly for $l^*, i^*, j^*$, by the basic property that pullback commutes with $d$ ([[Thm - Pullback Commutes with d for Forms on Manifolds]]).
>
> **Step 3 — Apply the zigzag lemma.** By Lemma 2 (the zigzag lemma applied to this short exact sequence of cochain complexes), there is a connecting homomorphism $\delta : H^p_{dR}(U \cap V) \to H^{p+1}_{dR}(M)$ making the long sequence
> $$\cdots \to H^p_{dR}(M) \to H^p_{dR}(U) \oplus H^p_{dR}(V) \to H^p_{dR}(U \cap V) \xrightarrow{\delta} H^{p+1}_{dR}(M) \to \cdots$$
> exact. $\blacksquare$
>
> **Explicit form of $\delta$.** Given $[\eta] \in H^p_{dR}(U \cap V)$ with $d\eta = 0$: lift $\eta = \omega_U|_{U \cap V} - \omega_V|_{U \cap V}$ via Lemma 1; then $d\omega_U$ on $U$ and $d\omega_V$ on $V$ agree on $U \cap V$ (since $d\omega_U - d\omega_V = d\eta = 0$), so they patch to a global closed form $\zeta \in \Omega^{p+1}(M)$. Then $\delta[\eta] = [\zeta]$.

---

# Cross-Field Exercise Suggestions

**Cohomology of the $n$-sphere.** Use the cover of $S^n$ by two open hemispheres (each contractible — [[Def - Homotopy|homotopy]] equivalent to a point, $H^* = \mathbb{R}$ in degree $0$). Their intersection is an open neighborhood of the equator, [[Def - Homotopy|homotopy]] equivalent to $S^{n-1}$. The Mayer–Vietoris sequence (combined with the inductive hypothesis $H^*(S^{n-1})$) gives $H^p(S^n) = \mathbb{R}$ for $p = 0, n$ and zero otherwise.

**Cohomology of the $n$-torus.** For $T^n = S^1 \times S^1 \times \cdots \times S^1$, the **Künneth formula** $H^*(T^n) = H^*(S^1)^{\otimes n}$ (where $\otimes$ is the graded tensor product over $\mathbb{R}$) gives $H^k(T^n) = \mathbb{R}^{\binom{n}{k}}$. The Künneth formula can be proved by induction using Mayer–Vietoris, with the cover $T^n = U \times S^1$, $V \times S^1$ where $\{U, V\}$ covers $T^{n-1}$.

**Cohomology of $\mathbb{R}^n \setminus \{0\}$.** Cover by $U = \mathbb{R}^n \setminus \{x_n \leq 0\}$ and $V = \mathbb{R}^n \setminus \{x_n \geq 0\}$ — each is half-Euclidean, hence contractible. Their intersection is $\mathbb{R}^n \setminus \{x_n = 0\}$, which is the union of two disjoint half-spaces, each contractible. Mayer–Vietoris gives $H^{n-1}(\mathbb{R}^n \setminus \{0\}) = \mathbb{R}$ and zero otherwise (in positive degree). Alternatively, $\mathbb{R}^n \setminus \{0\} \simeq S^{n-1}$ by homotopy invariance.

**Cohomology of a wedge of spheres.** $S^n \vee S^m$ (the wedge at a basepoint) is computed by the cover $U = S^n \cup (\text{small open neighborhood of basepoint in } S^m)$ — $U \simeq S^n$, similarly $V \simeq S^m$, and $U \cap V$ is contractible (around the basepoint). Mayer–Vietoris gives $H^k(S^n \vee S^m) = H^k(S^n) \oplus H^k(S^m)$ for $k > 0$ and $\mathbb{R}$ in degree $0$.

---

# Bridges

- **[[Thm - The Poincaré Lemma on a Star-Shaped Region|Poincaré lemma]]** — the *local input* to Mayer–Vietoris. On a "good cover" (cover by contractible open sets), the Poincaré lemma kills cohomology of each piece in positive degrees, so all cohomological information is carried by the gluing data, accessed via Mayer–Vietoris's connecting map.

- **The Čech–de Rham theorem and spectral sequences** — Mayer–Vietoris is the two-set case; for an arbitrary cover, the **Čech–de Rham bicomplex** and its spectral sequence generalize. Every smooth manifold has a good cover, and the spectral sequence converges to its de Rham cohomology with E_1 page computable from the combinatorics. Mayer–Vietoris is the simplest instance of this powerful general machinery.

- **Singular cohomology Mayer–Vietoris** — there is an analogous long exact sequence for singular cohomology with real coefficients, with the same form (and the same proof, by the same zigzag lemma applied to the corresponding short exact sequence of singular cochain complexes). By the [[Thm - The de Rham Theorem (Statement)|de Rham theorem]], the two long exact sequences agree.

- **Excision and the long exact sequence of a pair** — Mayer–Vietoris is closely related to (but not the same as) the long exact sequence of the pair $(M, U)$ for $U$ an open subset. Both arise from zigzag lemmas, but applied to different short exact sequences. Mayer–Vietoris uses two open sets covering $M$; the pair sequence uses one open subset and a relative cohomology. The two are equivalent by formal manipulation and excision.

- **Group theory: the connecting map as a quotient/inclusion analogue** — the connecting map $\delta$ assigns to each class on the overlap a class on the global manifold of one higher degree. Algebraically, this is the same kind of construction as the *snake lemma* in module theory: a way to relate kernels and cokernels across a short exact sequence. It is a piece of [[Thm - First Isomorphism Theorem|first-isomorphism-theorem]]-style algebra packaged into a homological-algebra mechanism.

---

# Unlocked by This

> [!tip] **Cohomology of every "simple" manifold** *(from this same topic)*
> Iterating Mayer–Vietoris on a good cover computes $H^*$ for spheres, tori, projective spaces, Grassmannians, and many more. Every introductory cohomology computation is via this route.

> [!tip] **Čech-to-derived-functor spectral sequence** *(from Sheaf Cohomology)*
> Mayer–Vietoris is the first page of the **Čech-to-derived-functor spectral sequence** for any sheaf with reasonable open cover. This generalizes from de Rham cohomology to *any* sheaf cohomology — Dolbeault, Čech cohomology of constant sheaves, sheaf cohomology in algebraic geometry — providing a uniform computational machine.

> [!tip] **Künneth formula** *(from Algebraic Topology and Algebraic Geometry)*
> The cohomology of a product satisfies $H^*(M \times N) = H^*(M) \otimes H^*(N)$ (with real coefficients, or more generally with field coefficients). The proof uses iterated Mayer–Vietoris on a product cover, and the formula is the foundation for computing cohomology of fiber bundles via the Leray–Hirsch theorem.

> [!tip] **Poincaré duality** *(from Algebraic Topology of Manifolds)*
> For a compact oriented $n$-manifold $M$, **Poincaré duality** is the isomorphism $H^k(M; \mathbb{R}) \cong H^{n-k}(M; \mathbb{R})$, mediated by the cap product with the fundamental class. The proof uses Mayer–Vietoris plus a careful analysis of compactly supported cohomology, and it is what makes cohomology a "two-sided" object — top-degree dual to bottom-degree.

> [!tip] **Mayer–Vietoris for compactly supported cohomology and Poincaré–Lefschetz duality** *(from Algebraic Topology)*
> A dual Mayer–Vietoris sequence for compactly supported cohomology, with arrows reversed, computes $H^k_c(M)$. The two Mayer–Vietoris sequences fit together in **Poincaré–Lefschetz duality** for manifolds with boundary, the master computational tool of geometric topology.
