---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Linear Map"
  - "Def - Null Space and Range"
  - "Def - Rank of a Linear Map"
  - "Def - Basis"
  - "Def - Dimension"
tags: [algebra, linear-algebra]
---

# Notation

Throughout, $T : V \to W$ is a [[Def - Linear Map|linear map]] with $V$ finite-dimensional; $\dim V$, $\dim \operatorname{null} T$, $\dim \operatorname{range} T$ are the dimensions appearing in the theorem. The full notation registry for the chapter is on [[Linear Algebra III — §3A–D Linear Maps]].

---

# Statement

> **Theorem (Fundamental Theorem of [[Def - Linear Map|Linear Maps]]).** Let $V$ be a finite-dimensional vector space over $\mathbf{F}$, let $W$ be any vector space over $\mathbf{F}$, and let $T \in \mathcal{L}(V, W)$. Then $\operatorname{range} T$ is finite-dimensional, and
>
> $$\dim V \;=\; \dim \operatorname{null} T \;+\; \dim \operatorname{range} T.$$

The theorem is also known as the **rank–nullity theorem**, in the form

> **Corollary (rank–nullity).** $\dim V = \operatorname{nullity}(T) + \operatorname{rank}(T)$, where $\operatorname{nullity}(T) = \dim \operatorname{null} T$ and $\operatorname{rank}(T) = \dim \operatorname{range} T$.

Note that $W$ is not required to be finite-dimensional — only $V$. If $W$ is finite-dimensional, then $\operatorname{range} T \subseteq W$ implies $\dim \operatorname{range} T \leq \dim W$, but the theorem itself does not need this.

---

# Motivation

This is the central theorem of finite-dimensional linear algebra. Almost every structural fact in [[Linear Algebra III — §3A–D Linear Maps]] is one or two lines away from it: injectivity-equals-surjectivity in equal finite [[Def - Dimension|dimensions]], the dimensional classification of isomorphic vector spaces, the dimension of the space of linear maps, every rank inequality involving compositions, and the impossibility of various prescribed-kernel-and-range constructions. The theorem is to linear algebra what [[Thm - Lagrange's Theorem|Lagrange's theorem]] is to finite [[Def - Group|group]] theory — a free conservation law that converts one unknown dimension into another, and rules out impossible configurations before any specific computation.

The question the theorem answers is: given a linear map $T : V \to W$, how does the dimension of the domain split between "what gets collapsed" and "what gets mapped into the codomain"? Intuitively, $T$ kills a subspace (its null space) and stretches the rest onto the range. The theorem says these two pieces add up to $\dim V$ exactly — no overlap, no slack, no information lost. Every dimension of $V$ is accounted for, either by being mapped to $0$ (null-space contribution) or by being mapped to a non-zero output (range contribution). It is a **conservation law for dimension**.

The deeper conceptual reading is that this is the dimension-counting shadow of a sharper algebraic statement: there is an isomorphism $V / \operatorname{null} T \cong \operatorname{range} T$, the **first isomorphism theorem** for vector spaces (which is itself a special case of the [[Thm - First Isomorphism Theorem|first isomorphism theorem for groups]] applied in the abelian-[[Def - Group|group]] setting of vector spaces). Taking [[Def - Dimension|dimensions]] of both sides converts the isomorphism into the rank–nullity equation. So rank–nullity is not a primitive theorem about dimensions — it is the dimensional shadow of a structural identity that holds in much greater generality (for [[Def - Module|modules]] over any [[Def - Ring|ring]], where dimensions need not even be defined). The clean linear-algebra version exists because vector spaces are [[Def - Module|modules]] over a field, and over a field every module is free and has a well-defined dimension.

The theorem also explains why "operators on a finite-dimensional space" behave so much better than operators in infinite dimensions: in finite dimensions, every operator has a *finite* rank and a *finite* nullity, summing to $\dim V$, and so the "size" of what is destroyed and what is preserved is bounded by a single number. In infinite dimensions, rank and nullity can both be infinite and unrelated, and the rich phenomena of functional analysis (compact operators, the Fredholm alternative, the spectrum-as-resolvent-set-complement) emerge from the failure of this rigidity.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition of the theorem — "$V$ is finite-dimensional, $T$ is linear" — is mild. The interesting question is **which problem setups secretly hand you the conditions for rank–nullity**, even when the words "rank" and "nullity" do not appear.

The first disguised source is **"a linear map between two named finite-dimensional spaces is given or can be built"**. The moment such a map appears — even if the problem only mentions $V$, $W$, and asks something about subspaces — rank–nullity gives a free dimension equation. The non-obvious step is to *notice that you have a linear map* and to *give it a name*. Example problem: "Show that every $n$-by-$n$ matrix $A$ with at least one zero column has $\det A = 0$." There is a linear map here — the map $\mathbf{F}^n \to \mathbf{F}^n$, $x \mapsto Ax$ — and the zero column says the standard basis vector $e_k$ is in the null space, so $\dim \operatorname{null} T \geq 1$, so $\dim \operatorname{range} T \leq n - 1$, so $T$ is not surjective, so $A$ is not invertible. Rank–nullity converted a structural feature of $A$ (zero column) into a dimensional obstruction.

The second disguised source is **"a system of homogeneous linear equations is given"**. A system $A x = 0$ with $A \in \mathbf{F}^{m, n}$ is the null space of the linear map $T_A : \mathbf{F}^n \to \mathbf{F}^m$, $T_A(x) = Ax$. The dimension of the solution space is $\dim \operatorname{null} T_A = n - \dim \operatorname{range} T_A = n - \operatorname{rank} A$, by rank–nullity. The non-obvious step is to *recognize that the question about solutions is really a question about null spaces of a linear map*. Example problem: "How many independent solutions does the system $x_1 + 2x_2 + 3x_3 + 4x_4 = 0$, $x_1 - x_2 + x_3 - x_4 = 0$ have?" Build the matrix, compute its rank ($2$, by linear independence of the two rows), and rank–nullity gives $4 - 2 = 2$ independent solutions.

The third disguised source is **"a quotient or subspace is implicitly defined by a vanishing condition"**. The subspace $\{v \in V : Tv \in U\}$ for a subspace $U \subseteq W$ is, in general, larger than just the null space — it is the preimage of $U$. Its dimension is $\dim \operatorname{null} T + \dim(U \cap \operatorname{range} T)$, and the proof is a clever application of rank–nullity to the **restriction map** $T|_{\text{preimage}} \to U$. The non-obvious step is to *apply rank–nullity to a cleverly-chosen restriction or quotient map* rather than to the original $T$. Example problem (Exercise 21 of LADR §3B): "$V$ finite-dimensional, $T \in \mathcal{L}(V, W)$, $U \subseteq W$. Show $\dim\{v : Tv \in U\} = \dim \operatorname{null} T + \dim(U \cap \operatorname{range} T)$." The right move is to consider the linear map $T : \{v : Tv \in U\} \to U \cap \operatorname{range} T$ (the restriction of $T$ to the preimage of $U$, with codomain restricted to the image): rank–nullity on *this map* gives the answer.

The fourth disguised source is **"a meta-map between spaces of linear maps is involved"**. The space $\mathcal{L}(V, W)$ is itself a vector space, and rank–nullity applies to linear maps between such spaces — for instance, the **restriction map** $\Phi : \mathcal{L}(V, W) \to \mathcal{L}(U, W)$, $\Phi(T) = T|_U$, for a subspace $U \subseteq V$. The non-obvious step is to *apply rank–nullity at the meta-level*: the dimension of the kernel of $\Phi$ (maps in $\mathcal{L}(V, W)$ that vanish on $U$) plus the dimension of the image (which, by extension, equals $\mathcal{L}(U, W)$ when $V$ is finite-dimensional) equals $\dim \mathcal{L}(V, W) = mn$. This is the technique used in Exercise 10 of LADR §3D.

**Targets (Output Amplification)**

The bare conclusion is the dimension equation. Combined with other facts it does much more.

Combine with **the dimensions of $V$ and $W$**. Once both are known, the equation $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$ with $\dim \operatorname{range} T \leq \dim W$ produces $\dim \operatorname{null} T \geq \dim V - \dim W$. So if $\dim V > \dim W$, the null space must be at least $(\dim V - \dim W)$-dimensional — *every* linear map from a higher-dimensional space to a lower-dimensional one is non-injective. This is the "pigeonhole principle of linear algebra": a free non-injectivity statement, with no specific calculation. Dually, if $\dim V < \dim W$, no map can be surjective — *every* linear map from a lower-dimensional space misses something.

Combine with **equal dimensions $\dim V = \dim W < \infty$**. Then $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$ and $\dim \operatorname{range} T \leq \dim W = \dim V$, with equality iff $\operatorname{range} T = W$, iff $\dim \operatorname{null} T = 0$, iff $T$ is injective. So in equal finite dimensions, $T$ injective ⟺ $T$ surjective ⟺ $T$ invertible — the content of [[Thm - Injectivity Equals Surjectivity in Finite Dimensions]]. The further result $E$: half-statements about linear maps in equal dimensions automatically upgrade to full statements about invertibility, with no extra work.

Combine with **information about a composition** $ST$. The image of $ST$ is contained in the image of $S$, so $\dim \operatorname{range}(ST) \leq \dim \operatorname{range} S$; the null space of $T$ is contained in the null space of $ST$, so $\dim \operatorname{null}(ST) \geq \dim \operatorname{null} T$. Combined with rank–nullity applied to $ST$, one obtains the rank inequality $\operatorname{rank}(ST) \leq \min\{\operatorname{rank} S, \operatorname{rank} T\}$ (see [[Ex - Rank of a product is bounded by individual ranks]]). The further result $E$: bounds on the rank of a composition in terms of the ranks of the factors, which is the engine behind almost every claim about products of matrices having low rank.

Combine with **a homomorphism into a quotient or product space**. The dimensions of products and quotients are known: $\dim(V_1 \times \cdots \times V_m) = \sum \dim V_k$, and $\dim(V / U) = \dim V - \dim U$. Applying rank–nullity to a map *into* such a space turns the dimension equation into a constraint between the dimensions of the factors. The further result $E$: dimensional obstructions to the existence of maps with prescribed targets — for instance, "there is no surjective map $V \to V_1 \times V_2$ unless $\dim V \geq \dim V_1 + \dim V_2$".

---

# Why Is It True

Forget the formal proof and picture what is happening. A linear map $T : V \to W$ takes vectors of $V$ and produces vectors of $W$. Some vectors of $V$ are killed — they go to $0$ — and the set of those is the null space, a subspace of dimension $k$. The other vectors of $V$ produce non-zero outputs.

Now choose a basis of the null space: $u_1, \ldots, u_k$. Then extend this basis to a basis of all of $V$ by adding $v_1, \ldots, v_{n-k}$ where $n = \dim V$. The full list $u_1, \ldots, u_k, v_1, \ldots, v_{n-k}$ is a basis of $V$. Now apply $T$ to each basis vector. The first $k$ go to $0$ (by definition of the null space). The remaining $n - k$ go to $T v_1, \ldots, T v_{n-k}$ — non-zero vectors in $W$.

Two claims about these $n - k$ vectors:

1. **They span the range.** Any $w \in \operatorname{range} T$ is $Tv$ for some $v \in V$, and $v = \sum a_i u_i + \sum b_j v_j$ in the basis above. Linearity gives $Tv = \sum a_i (T u_i) + \sum b_j (T v_j) = \sum b_j T v_j$ — the $u$-contributions vanish. So $T v_1, \ldots, T v_{n-k}$ span the range.

2. **They are linearly independent.** Suppose $\sum c_j T v_j = 0$. Then $T(\sum c_j v_j) = 0$, so $\sum c_j v_j \in \operatorname{null} T$. But the $v_j$ are by construction *outside* the span of the null-space basis $u_1, \ldots, u_k$ — they extend it — so the linear combination $\sum c_j v_j$ being in the null space forces all $c_j = 0$.

So $T v_1, \ldots, T v_{n-k}$ form a basis of $\operatorname{range} T$, of length $n - k$. Hence $\dim \operatorname{range} T = n - k = \dim V - \dim \operatorname{null} T$, which rearranges to the theorem.

> **The whole intuition in one sentence: the null space accounts for the killed dimensions, and the rest of a basis of $V$ maps to a basis of the range — no information is lost or duplicated.**

A cleaner reformulation that subsumes this: there is an isomorphism $V / \operatorname{null} T \cong \operatorname{range} T$ given by $v + \operatorname{null} T \mapsto Tv$. The left-hand side has dimension $\dim V - \dim \operatorname{null} T$ (dimensions of quotients subtract), and so the dimension equation is automatic. This is the **first isomorphism theorem for vector spaces**, and the rank–nullity theorem is its dimensional shadow.

The reason this works in *finite dimensions* and fails in *infinite dimensions* is that in finite dimensions every subspace has a complement, the basis extension lemma works, and dimensions are well-defined natural numbers that add and subtract. In infinite dimensions, every step of this argument still goes through *for the isomorphism statement* — $V / \operatorname{null} T \cong \operatorname{range} T$ remains true — but the dimensions are cardinals, the equation $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$ becomes a cardinal arithmetic statement (where infinite cardinals satisfy $\kappa + \lambda = \max(\kappa, \lambda)$ for non-zero cardinals, making the equation trivial when one side is infinite), and the rigidity disappears. The finite-dimensional rigidity is genuinely a feature of finite dimensions.

---

# What Makes This Hard

The conceptual content is easy; the proof is essentially "extend a basis of the null space to a basis of $V$ and observe that the extension maps to a basis of the range". The trap is in the **linear independence of $Tv_1, \ldots, Tv_{n-k}$**: it requires using that the $v_j$ are *not* in the null space, which is implicit in their being basis-extensions of $u_1, \ldots, u_k$ but is sometimes mishandled. Beginners writing the proof either (a) forget to check linear independence and "prove" the theorem with a circular argument, or (b) get the linear independence right but bungle the spanning step by failing to use $Tu_i = 0$.

The other common error is to think rank–nullity applies when $V$ is infinite-dimensional. It does not, in any meaningful sense; in infinite dimensions, you need the isomorphism form $V / \operatorname{null} T \cong \operatorname{range} T$ (which holds always), not the dimension equation.

A third subtle point: the theorem requires $V$ finite-dimensional, but $W$ need not be. So a linear map from a finite-dimensional $V$ into an infinite-dimensional $W$ still has rank–nullity: $\operatorname{range} T \subseteq W$ is automatically finite-dimensional (because it is the linear image of a finite-dimensional space), and the equation $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$ holds. The asymmetry is real and worth noticing.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy.** Choose a basis of the null space, extend to a basis of $V$, and prove that the images of the basis-extension vectors are a basis of the range. The whole proof is one careful basis manipulation.

**Subgoal decomposition:**

1. **Set up the bases.** Let $u_1, \ldots, u_k$ be a basis of $\operatorname{null} T$, where $k = \dim \operatorname{null} T$. Extend to a basis $u_1, \ldots, u_k, v_1, \ldots, v_m$ of $V$, where $k + m = \dim V$.
   - *Hint:* Use the basis extension lemma — every linearly independent list in a finite-dimensional space extends to a basis.
   - *Why needed:* A basis of $V$ adapted to the null space is the only ingredient required; everything follows by inspection.

2. **Show $Tv_1, \ldots, Tv_m$ span $\operatorname{range} T$.** Every element of $\operatorname{range} T$ is $Tv$ for some $v \in V$; expanding $v$ in the basis and applying linearity, the $u$-contributions vanish (they are in $\operatorname{null} T$).
   - *Hint:* Linearity plus $Tu_i = 0$.
   - *Why needed:* Half of "being a basis": spanning.

3. **Show $Tv_1, \ldots, Tv_m$ are linearly independent.** A linear relation $\sum c_j Tv_j = 0$ means $\sum c_j v_j \in \operatorname{null} T$, but the $v_j$ are basis-extensions, so $\sum c_j v_j$ being in the null space forces all $c_j = 0$.
   - *Hint:* Use linear independence of the *full* basis $u_1, \ldots, u_k, v_1, \ldots, v_m$ — express $\sum c_j v_j$ as $\sum a_i u_i$ if it is in the null space, then read off $c_j = 0$.
   - *Why needed:* Other half of "being a basis".

4. **Conclude.** $Tv_1, \ldots, Tv_m$ is a basis of $\operatorname{range} T$ of length $m$, so $\dim \operatorname{range} T = m = \dim V - \dim \operatorname{null} T$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Null space and range are [[Def - Subspace|subspaces]]
> **Statement:** $\operatorname{null} T$ is a subspace of $V$ and $\operatorname{range} T$ is a subspace of $W$, for any linear map $T : V \to W$.
>
> **Hint:** Check the three subspace axioms (contains zero, closed under sum, closed under scalar multiplication) using linearity of $T$.
>
> **Why needed:** To even speak of $\dim \operatorname{null} T$ and $\dim \operatorname{range} T$, these subsets must be [[Def - Subspace|subspaces]]. The dimension is undefined for general subsets.
>
> > [!note]- Full proof
> > For $\operatorname{null} T$: $T(0_V) = 0_W$, so $0_V \in \operatorname{null} T$. If $u, v \in \operatorname{null} T$, then $T(u + v) = Tu + Tv = 0 + 0 = 0$, so $u + v \in \operatorname{null} T$. If $\lambda \in \mathbf{F}$ and $v \in \operatorname{null} T$, then $T(\lambda v) = \lambda Tv = \lambda \cdot 0 = 0$, so $\lambda v \in \operatorname{null} T$.
> >
> > For $\operatorname{range} T$: $0_W = T(0_V) \in \operatorname{range} T$. If $w_1 = Tv_1$ and $w_2 = Tv_2$ are in the range, then $w_1 + w_2 = T(v_1 + v_2) \in \operatorname{range} T$. If $\lambda \in \mathbf{F}$ and $w = Tv \in \operatorname{range} T$, then $\lambda w = \lambda Tv = T(\lambda v) \in \operatorname{range} T$.

> [!note]- Lemma 2: Basis extension
> **Statement:** In a finite-dimensional vector space $V$, any linearly independent list of vectors $u_1, \ldots, u_k$ extends to a basis $u_1, \ldots, u_k, v_1, \ldots, v_m$ of $V$, where $k + m = \dim V$.
>
> **Hint:** Standard fact from [[Linear Algebra II — §2 Finite-Dimensional Vector Spaces]]: in a finite-dimensional space, every linearly independent list can be extended to a basis. The construction adds, one at a time, a vector not in the span of the previous list.
>
> **Why needed:** This is the construction that produces a basis of $V$ adapted to the null space. Without it, the proof cannot get started.
>
> > [!note]- Full proof
> > If $u_1, \ldots, u_k$ already spans $V$, then $m = 0$ and the list is already a basis (linearly independent and spanning). Otherwise, pick any $v_1 \in V \setminus \operatorname{span}(u_1, \ldots, u_k)$; the list $u_1, \ldots, u_k, v_1$ is linearly independent (a vector outside the span of a linearly independent list cannot be expressed as a linear combination of the list, so any linear relation forces the coefficient of the new vector to be $0$, then the rest of the coefficients to be $0$ by linear independence of $u_1, \ldots, u_k$). Repeat until the list spans $V$. Since $V$ is finite-dimensional, this terminates after at most $\dim V - k$ steps.

> [!note]- Lemma 3: Images of basis-extension vectors span the range
> **Statement:** Let $u_1, \ldots, u_k$ be a basis of $\operatorname{null} T$ extended to a basis $u_1, \ldots, u_k, v_1, \ldots, v_m$ of $V$. Then $Tv_1, \ldots, Tv_m$ spans $\operatorname{range} T$.
>
> **Hint:** Expand an arbitrary $v \in V$ in the basis, apply $T$, and use $Tu_i = 0$ to kill the null-space contributions.
>
> **Why needed:** This is one half of showing $Tv_1, \ldots, Tv_m$ is a basis of $\operatorname{range} T$.
>
> > [!note]- Full proof
> > Let $w \in \operatorname{range} T$, so $w = Tv$ for some $v \in V$. Expand $v$ in the basis: $v = \sum_{i=1}^k a_i u_i + \sum_{j=1}^m b_j v_j$ for some scalars $a_i, b_j$. Then
> > $$w = Tv = \sum_{i=1}^k a_i Tu_i + \sum_{j=1}^m b_j Tv_j = 0 + \sum_{j=1}^m b_j Tv_j = \sum_{j=1}^m b_j Tv_j,$$
> > so $w \in \operatorname{span}(Tv_1, \ldots, Tv_m)$. As $w$ was arbitrary, $\operatorname{range} T \subseteq \operatorname{span}(Tv_1, \ldots, Tv_m)$. The reverse inclusion is automatic: each $Tv_j \in \operatorname{range} T$, so any span is in $\operatorname{range} T$.

> [!note]- Lemma 4: Images of basis-extension vectors are linearly independent
> **Statement:** With notation as in Lemma 3, $Tv_1, \ldots, Tv_m$ are linearly independent in $W$.
>
> **Hint:** A linear relation $\sum c_j Tv_j = 0$ becomes $T(\sum c_j v_j) = 0$, so $\sum c_j v_j \in \operatorname{null} T$. Express this in the $u$-basis of the null space; linear independence of the *full* basis $u_1, \ldots, u_k, v_1, \ldots, v_m$ forces all coefficients to be zero.
>
> **Why needed:** Other half of showing $Tv_1, \ldots, Tv_m$ is a basis of $\operatorname{range} T$.
>
> > [!note]- Full proof
> > Suppose $c_1 Tv_1 + \cdots + c_m Tv_m = 0$ for some scalars $c_j$. By linearity, $T(c_1 v_1 + \cdots + c_m v_m) = 0$, so $c_1 v_1 + \cdots + c_m v_m \in \operatorname{null} T$. Since $u_1, \ldots, u_k$ is a basis of $\operatorname{null} T$, we can write
> > $$c_1 v_1 + \cdots + c_m v_m = a_1 u_1 + \cdots + a_k u_k$$
> > for some scalars $a_i$. Rearranging,
> > $$-a_1 u_1 - \cdots - a_k u_k + c_1 v_1 + \cdots + c_m v_m = 0.$$
> > This is a linear relation among the basis $u_1, \ldots, u_k, v_1, \ldots, v_m$ of $V$. Since the basis is linearly independent, all coefficients are zero: $a_1 = \cdots = a_k = c_1 = \cdots = c_m = 0$. In particular, $c_1 = \cdots = c_m = 0$, as required.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $V$ be finite-dimensional with $\dim V = n$, and let $T : V \to W$ be linear.
>
> **Step 0 — the dimensions exist.** $\operatorname{null} T$ is a subspace of $V$ (Lemma 1), hence finite-dimensional with $\dim \operatorname{null} T \leq \dim V = n$. Let $k = \dim \operatorname{null} T$. We must show $\operatorname{range} T$ is finite-dimensional with $\dim \operatorname{range} T = n - k$.
>
> **Step 1 — choose adapted bases.** Let $u_1, \ldots, u_k$ be a basis of $\operatorname{null} T$. By the basis extension lemma (Lemma 2), this list extends to a basis $u_1, \ldots, u_k, v_1, \ldots, v_m$ of $V$, with $k + m = n$, so $m = n - k$.
>
> **Step 2 — the images $Tv_1, \ldots, Tv_m$ span $\operatorname{range} T$.** By Lemma 3, every $w \in \operatorname{range} T$ is in $\operatorname{span}(Tv_1, \ldots, Tv_m)$.
>
> **Step 3 — the images $Tv_1, \ldots, Tv_m$ are linearly independent.** By Lemma 4.
>
> **Step 4 — conclude.** $Tv_1, \ldots, Tv_m$ is a basis of $\operatorname{range} T$, of length $m$. Hence $\operatorname{range} T$ is finite-dimensional, and $\dim \operatorname{range} T = m = n - k = \dim V - \dim \operatorname{null} T$. Rearranging,
> $$\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T. \qquad \blacksquare$$

---

# Cross-Field Exercise Suggestions

**Pigeonhole in linear algebra.** Show that any linear map $\mathbf{F}^{n+1} \to \mathbf{F}^n$ has a non-trivial null space. Rank–nullity gives $\dim \operatorname{null} T = (n+1) - \dim \operatorname{range} T \geq (n+1) - n = 1$. So *every* linear map from a higher-dimensional space to a lower-dimensional space is non-injective. This is the linear-algebra pigeonhole principle, and it underlies the (non-)existence of many constructions: there is no injective linear map $\mathbb{R}^3 \to \mathbb{R}^2$, no continuous injective linear map between Banach spaces of different finite dimensions, and so on. The application is non-obvious because the "pigeonhole" framing suggests combinatorics, but the actual proof is one line of rank–nullity.

**Solving systems of equations.** A homogeneous system $Ax = 0$ for $A \in \mathbf{F}^{m, n}$ has solution space $\operatorname{null} T_A$ of dimension $n - \operatorname{rank} A$. So the number of independent solutions is $n - r$, where $r$ is the rank. This is the workhorse fact for solving linear systems by hand: count the rank, subtract from $n$, get the number of free parameters. The application is non-obvious only in that students often compute the solution space directly rather than realising rank–nullity gives the dimension for free.

**Existence of operators with prescribed kernel and range.** Given subspaces $X \subseteq V$ and $Y \subseteq W$ with $V$ finite-dimensional, when does there exist $T \in \mathcal{L}(V, W)$ with $\operatorname{null} T = X$ and $\operatorname{range} T = Y$? Rank–nullity gives a necessary condition: $\dim V = \dim X + \dim Y$. The condition is also sufficient — and the construction uses the linear-map lemma and rank–nullity together. This is Exercise 31 of LADR §3B and an excellent application: rank–nullity converts an existence question into a dimension-counting question.

**Fredholm operators and the index in functional analysis.** A bounded operator $T : X \to Y$ between Banach spaces is **Fredholm** if $\dim \operatorname{null} T < \infty$ and $\operatorname{codim} \operatorname{range} T < \infty$. The **Fredholm index** is $\operatorname{ind}(T) := \dim \operatorname{null} T - \operatorname{codim} \operatorname{range} T$, a refinement of rank–nullity (in the finite-dimensional case, this index is $\dim V - \dim W$, a constant of the dimensions independent of $T$). The Atiyah–Singer index theorem expresses the analytical Fredholm index of an elliptic operator on a manifold in terms of topological invariants — one of the great theorems of 20th-century mathematics, and a direct descendant of rank–nullity.

**The implicit function theorem (rank theorem in calculus).** Smooth maps $f : \mathbb{R}^n \to \mathbb{R}^m$ at a point where the Jacobian has rank $r$ are locally equivalent to the standard projection $(x_1, \ldots, x_n) \mapsto (x_1, \ldots, x_r, 0, \ldots, 0)$, by a change of coordinates. This is the **rank theorem** of multivariable calculus, the global form of which is the implicit function theorem. The proof uses rank–nullity at every point and assembles the local rank-$r$ pieces into a global statement. The application is non-obvious because "rank" in calculus is "rank of the Jacobian", but it really is the same rank from linear algebra. See [[Linear Algebra IV — §3E–F Products, Quotients, Duality]] for related applications in dual spaces and [[Multivariate Analysis I — Differentiation in Several Variables]] for the calculus version.

---

# Bridges

- **[[Thm - First Isomorphism Theorem]] (group theory)** — the algebraic source of rank–nullity. For groups, the first isomorphism theorem says $G / \ker \varphi \cong \operatorname{im} \varphi$ for any homomorphism $\varphi$. In the special case of vector-space homomorphisms (linear maps), this becomes $V / \operatorname{null} T \cong \operatorname{range} T$. Taking dimensions: $\dim V - \dim \operatorname{null} T = \dim \operatorname{range} T$, which rearranges to rank–nullity. The bridge runs both ways: rank–nullity is the dimensional shadow of the first isomorphism theorem; conversely, knowing the rank–nullity equation for *every* linear map is equivalent to knowing all the quotient isomorphisms. The first isomorphism theorem also holds for [[Def - Module|modules]] (with "submodule" replacing "subspace") and for [[Def - Ring|rings]] (with "ideal"), so rank–nullity has analogues — though without dimensions — in those settings.

- **[[Thm - Injectivity Equals Surjectivity in Finite Dimensions]]** — the immediate corollary. With $\dim V = \dim W < \infty$, rank–nullity gives $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$, and $\dim \operatorname{range} T \leq \dim W = \dim V$; equality (i.e., surjectivity) holds iff $\dim \operatorname{null} T = 0$, iff $T$ is injective. So injective ⟺ surjective ⟺ invertible, and the proof is two lines of rank–nullity.

- **[[Thm - Two Vector Spaces Isomorphic iff Same Dimension]]** — also an easy corollary. Two finite-dimensional spaces of equal dimension admit an isomorphism (by the linear-map lemma on a chosen basis); conversely, an isomorphism preserves dimension (by injectivity giving $\dim V = \dim W$ via rank–nullity on the inverse). So dimension is the complete invariant.

- **Rank of a product** — $\operatorname{rank}(ST) \leq \min\{\operatorname{rank} S, \operatorname{rank} T\}$, see [[Ex - Rank of a product is bounded by individual ranks]]. The proof is "the image of $ST$ is in the image of $S$" (giving the $\operatorname{rank} S$ bound) and "the image of $ST$ is $S$ applied to the image of $T$, hence dimension at most $\dim \operatorname{range} T$" (giving the $\operatorname{rank} T$ bound). Both bounds are tight in different situations.

- **[[Thm - The Inverse Function Theorem]] and the rank theorem (multivariate analysis)** — the calculus version. A smooth map between manifolds at a point where the Jacobian has rank $r$ is locally equivalent, by a smooth change of coordinates on each side, to the standard rank-$r$ map. The rank in question is the rank of the Jacobian, which is the rank of the [[Def - The Total Derivative and Differentiability|total derivative]] — the same rank from linear algebra. The implicit function theorem and the regular-value preimage theorem are the global forms.

---

# Unlocked by This

> [!tip] First Isomorphism Theorem for Modules *(from Module Theory)*
> Every module homomorphism $T : M \to N$ over a ring $R$ has $M / \ker T \cong \operatorname{im} T$, and rank–nullity is the special case of this for vector spaces (taking dimensions of both sides). For modules that are not free (i.e., not vector spaces), dimensions need not be defined, but the quotient isomorphism still holds. See [[Def - Module Homomorphism]].

> [!tip] Smith Normal Form and Structure Theorem for Modules over a PID *(from Linear Algebra V and Module Theory)*
> Every $\mathbf{F}[x]$-module structure on a finite-dimensional vector space $V$ — equivalently, every linear operator $T : V \to V$ — gives $V$ the structure of a finitely-generated $\mathbf{F}[x]$-module. The **Smith normal form** of $T - xI$ (a matrix with polynomial entries) gives the **invariant factors** of $V$ as an $\mathbf{F}[x]$-module, and the structure theorem for f.g. modules over a PID decomposes $V$ as a direct sum of cyclic $\mathbf{F}[x]$-modules. Specialising to algebraically closed fields and $\mathbf{F}[x]/(x - \lambda)^{n}$-summands gives the **Jordan canonical form**. The whole structure is governed by rank–nullity at every stage.

> [!tip] The Index of a Fredholm Operator *(from Functional Analysis)*
> For bounded operators on infinite-dimensional Banach spaces, rank–nullity fails (both sides can be infinite). The right refinement is the **Fredholm index** of a Fredholm operator: $\operatorname{ind}(T) = \dim \operatorname{null} T - \operatorname{codim} \operatorname{range} T \in \mathbb{Z}$. This is a deformation-invariant of $T$ — it does not change under continuous deformation through Fredholm operators — and underlies the **K-theory** of Banach spaces, the **Atiyah–Singer index theorem**, and the analytical proof of the Bott periodicity theorem. The whole subject of "elliptic theory" on manifolds is the infinite-dimensional analogue of rank–nullity, with the index playing the role of "$\dim V - \dim W$".

> [!tip] Effective Dimension and Low-Rank Approximation *(from Statistics and Data Science)*
> A data matrix's **effective rank** — the number of "really independent" rows or columns — is the quantity governing dimensionality reduction. The best rank-$r$ approximation in Frobenius norm is given by truncating the singular value decomposition, and the error is determined by the discarded singular values. **Principal component analysis**, **matrix factorisation in recommender systems**, **compressed sensing**, and **deep learning model compression** are all applications of low-rank approximation, with rank–nullity providing the underlying dimensional bookkeeping. See [[Linear Algebra VII — §7 Operators on Inner Product Spaces]] for the SVD and [[Linear Algebra XI — Applied II — Least Squares]] for least-squares applications.
