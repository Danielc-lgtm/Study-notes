---
type: theorem
subject: spinors
prereqs:
  - "Def - Clifford Algebra"
  - "Thm - Clifford Algebra Universal Property"
  - "Def - Quaternions"
tags: [geometry, algebra, spinors, k-theory]
---

# Notation

$\mathrm{Cl}(p, q)$ denotes the Clifford algebra $\mathrm{Cl}(\mathbb{R}^{p+q}, Q)$ with $Q(\vec x) = x_1^2 + \cdots + x_p^2 - x_{p+1}^2 - \cdots - x_{p+q}^2$ (signature $(p, q)$). $\mathbb{R}, \mathbb{C}, \mathbb{H}$ are the real, complex, and quaternion fields/division algebras. $M_n(\mathbb{F})$ is the algebra of $n \times n$ matrices over $\mathbb{F}$. The dimension of $\mathrm{Cl}(p, q)$ as an $\mathbb{R}$-algebra is $2^{p+q}$.

---

# Statement

> **Theorem (Classification of Real Clifford Algebras).** For each pair $(p, q)$ of non-negative integers, the Clifford algebra $\mathrm{Cl}(p, q)$ is isomorphic (as a real algebra) to a matrix algebra over $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{H}$, or to a direct sum of two such. Specifically, $\mathrm{Cl}(p, q) \cong M_{2^k}(\mathbb{F})$ or $M_{2^k}(\mathbb{F}) \oplus M_{2^k}(\mathbb{F})$ for appropriate $k$ and $\mathbb{F}$, with the pattern given by $p - q \pmod 8$:

| $p - q \pmod 8$ | $\mathrm{Cl}(p, q)$ structure |
|---|---|
| $0$ | $M_{2^{(p+q)/2}}(\mathbb{R})$ |
| $1$ | $M_{2^{(p+q-1)/2}}(\mathbb{R}) \oplus M_{2^{(p+q-1)/2}}(\mathbb{R})$ |
| $2$ | $M_{2^{(p+q)/2}}(\mathbb{R})$ |
| $3$ | $M_{2^{(p+q-1)/2}}(\mathbb{C})$ |
| $4$ | $M_{2^{(p+q-2)/2}}(\mathbb{H})$ |
| $5$ | $M_{2^{(p+q-3)/2}}(\mathbb{H}) \oplus M_{2^{(p+q-3)/2}}(\mathbb{H})$ |
| $6$ | $M_{2^{(p+q-2)/2}}(\mathbb{H})$ |
| $7$ | $M_{2^{(p+q-1)/2}}(\mathbb{C})$ |

> **Corollary (Bott periodicity for Clifford algebras).** $\mathrm{Cl}(p+8, q) \cong \mathrm{Cl}(p, q) \otimes_{\mathbb{R}} M_{16}(\mathbb{R})$, and similarly $\mathrm{Cl}(p, q+8) \cong \mathrm{Cl}(p, q) \otimes_{\mathbb{R}} M_{16}(\mathbb{R})$. So the structure repeats with period $8$ (up to matrix tensoring).

> **Corollary (Low-dimensional table).** The Clifford algebras in low dimensions:

| $(p, q)$ | $\mathrm{Cl}(p, q)$ |
|---|---|
| $(0, 0)$ | $\mathbb{R}$ |
| $(1, 0)$ | $\mathbb{R} \oplus \mathbb{R}$ |
| $(0, 1)$ | $\mathbb{C}$ |
| $(2, 0)$ | $M_2(\mathbb{R})$ |
| $(1, 1)$ | $M_2(\mathbb{R})$ |
| $(0, 2)$ | $\mathbb{H}$ |
| $(3, 0)$ | $M_2(\mathbb{C})$ (Pauli algebra) |
| $(2, 1)$ | $M_2(\mathbb{R}) \oplus M_2(\mathbb{R})$ |
| $(1, 2)$ | $M_2(\mathbb{C})$ |
| $(0, 3)$ | $\mathbb{H} \oplus \mathbb{H}$ |
| $(4, 0)$ | $M_2(\mathbb{H})$ |
| $(3, 1)$ | $M_4(\mathbb{R})$ |
| $(1, 3)$ | $M_2(\mathbb{H})$ (Dirac algebra, our convention) |
| $(0, 4)$ | $M_2(\mathbb{H})$ |

---

# Motivation

The classification answers: **for each quadratic vector space $(\mathbb{R}^n, Q)$ of given signature, what is the resulting Clifford algebra concretely?** The abstract definition $\mathrm{Cl}(p, q) = T(\mathbb{R}^{p+q})/I$ is unwieldy; the classification turns it into a *matrix algebra*, with explicit basis and product, that can be computed with.

The structure is remarkable: only three "ground fields" ($\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$) appear, and the pattern is **periodic with period 8** — a fact discovered by Cartan and Bott in the mid-20th century, and one of the deepest periodicity phenomena in mathematics. The period-$8$ structure underlies:

- **Bott periodicity in K-theory:** $KO^{-n}(\mathrm{pt}) \cong KO^{-n-8}(\mathrm{pt})$ for real K-theory.
- **Classification of topological insulators:** the "tenfold way" in condensed-matter physics, where 10 symmetry classes of free fermions are classified by Clifford algebra data and give the period-8 pattern.
- **Existence of special spinors:** Majorana spinors exist iff a certain reality condition is compatible with the Clifford structure, and this happens periodically in dimension.
- **Spacetime dimension constraints in string theory:** consistent string theories live in specific dimensions ($10$ for the superstring, $26$ for the bosonic string), and the dimension constraint comes from the Clifford-algebra structure of the worldsheet spinors.

The classification also distinguishes **real vs complex** Clifford algebras: $\mathrm{Cl}(p, q) \otimes \mathbb{C}$ — the complexification — depends only on $p + q$, and is always $M_{2^k}(\mathbb{C})$ (for $p + q$ even) or $M_{2^k}(\mathbb{C}) \oplus M_{2^k}(\mathbb{C})$ (for $p + q$ odd). The signature dependence is purely a *real* phenomenon, invisible after complexification — which is why most physics calculations using complexified spinors don't see the signature, but constructions involving Majorana spinors (real spinors) very much do.

---

# Sources and Targets

**Sources (Input Broadening)**

*Source 1: A specific signature $(p, q)$.* Given a pair $(p, q)$, looking up the table gives the explicit isomorphism class of $\mathrm{Cl}(p, q)$. Bridge: this is the standard input for any spinor calculation in dimension $p + q$ with given signature.

*Source 2: A known low-dimensional Clifford algebra.* If we already know $\mathrm{Cl}(p, q)$, the **Bott periodicity** corollary lets us compute $\mathrm{Cl}(p+8, q)$ by tensoring with $M_{16}(\mathbb{R})$. So the entire infinite table can be derived from the $8$ values for $p - q \pmod 8$ in low dimensions.

*Source 3: A spinor representation problem.* Given the spinor module of $\mathrm{Spin}(p, q)$ (the unique irreducible $\mathrm{Cl}(p, q)$-module up to isomorphism), the classification tells you what real, complex, or quaternionic structure the module carries — which determines whether **Majorana** or **Symplectic-Majorana** spinors exist in that dimension.

**Targets (Output Amplification)**

*Target 1: Construct the irreducible $\mathrm{Cl}(p, q)$-modules (spinor modules).* By the classification, $\mathrm{Cl}(p, q)$ is a matrix algebra (or direct sum), so its irreducible representations are explicitly known. For $M_n(\mathbb{F})$, the unique (up to iso) irreducible representation is $\mathbb{F}^n$. So the spinor module has real, complex, or quaternionic dimension $2^k$ depending on signature.

*Target 2: Determine when Majorana spinors exist.* A Majorana spinor is a self-conjugate Dirac spinor, requiring the spinor module to admit a real structure. This happens iff the ground field of the matrix algebra in $\mathrm{Cl}(p, q)$ is $\mathbb{R}$ (or $\mathbb{H}$ with extra structure). The classification tells you exactly when: Majorana spinors exist in signatures with $p - q \equiv 0, 1, 2, 6, 7 \pmod 8$.

*Target 3: Determine when Weyl spinors exist.* In even dimension $p + q = 2k$, the volume element $\omega = e_1 e_2 \cdots e_{2k}$ has $\omega^2 = (-1)^{k(2k-1)/2}(-1)^q$, depending on $(p, q)$. Weyl spinors exist iff $\omega^2 = +1$, allowing the chirality projectors $P_\pm = \tfrac{1}{2}(1 \pm \omega)$. This happens for $p - q \equiv 0 \pmod 4$.

*Target 4: Compute the dimension of the spinor module in any signature.* The total $\mathbb{R}$-dimension of $\mathrm{Cl}(p, q)$ is $2^{p+q}$; the spinor module has $\mathbb{R}$-dimension $\dim_{\mathbb{R}}(\mathbb{F}^n) = (1, 2, \text{ or } 4) \times 2^k$ depending on $\mathbb{F}$.

---

# Why Is It True

The classification is built from a small set of **periodicity isomorphisms** that let you compute $\mathrm{Cl}(p+1, q)$ in terms of $\mathrm{Cl}(p, q)$ and similar inductive relations.

**The key inductive relations (Atiyah–Bott–Shapiro):**

1. $\mathrm{Cl}(p+1, q+1) \cong \mathrm{Cl}(p, q) \otimes M_2(\mathbb{R})$.
2. $\mathrm{Cl}(p+4, q) \cong \mathrm{Cl}(q, p) \otimes M_2(\mathbb{H})$ (signature flip combined with $M_2(\mathbb{H})$-tensoring).
3. $\mathrm{Cl}(p+8, q) \cong \mathrm{Cl}(p, q) \otimes M_{16}(\mathbb{R})$ (the period-$8$ relation).

**Mechanism in one line: the Clifford algebra has a period-$8$ periodicity because the underlying matrix algebra structure cycles through $\mathbb{R}, \mathbb{R} \oplus \mathbb{R}, \mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{H} \oplus \mathbb{H}, \mathbb{H}, \mathbb{C}, \mathbb{R}, \ldots$, completing one cycle every 8 steps.**

The base cases $\mathrm{Cl}(0, 0) = \mathbb{R}$, $\mathrm{Cl}(1, 0) = \mathbb{R} \oplus \mathbb{R}$, $\mathrm{Cl}(0, 1) = \mathbb{C}$, $\mathrm{Cl}(2, 0) = M_2(\mathbb{R})$, $\mathrm{Cl}(1, 1) = M_2(\mathbb{R})$, $\mathrm{Cl}(0, 2) = \mathbb{H}$ are checked directly by computing the Clifford relations explicitly. From these and the inductive relations, the full table is derived by induction on $p + q$.

The deep mathematical content is in the **periodicity itself**: why does the structure repeat every $8$ steps? The proof of the period-$8$ identity uses the explicit isomorphism $\mathrm{Cl}(8, 0) = M_{16}(\mathbb{R})$ (which is computed directly), combined with the multiplicativity $\mathrm{Cl}(p_1 + p_2, q_1 + q_2) = \mathrm{Cl}(p_1, q_1) \otimes \mathrm{Cl}(p_2, q_2)$ for appropriately graded tensor products.

---

# What Makes This Hard

The classification has many indices and isomorphism patterns to keep straight, and the proof requires checking dimension counts at each step to verify that the candidate matrix algebra has the right size to be $\mathrm{Cl}(p, q)$. The trickiest step is the **period-$8$ identity** $\mathrm{Cl}(p+8, q) \cong \mathrm{Cl}(p, q) \otimes M_{16}(\mathbb{R})$, which requires explicitly constructing the $16$ generators of $M_{16}(\mathbb{R})$ in terms of the Clifford generators. Most introductory treatments just *state* the periodicity without a full proof, since the verification involves a substantial calculation. The connection to K-theory and Bott periodicity is the conceptual deepening that explains *why* the period is exactly $8$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Establish the base cases $\mathrm{Cl}(p, q)$ for $0 \leq p + q \leq 3$ by direct computation. Prove the inductive relations $\mathrm{Cl}(p+1, q+1) = \mathrm{Cl}(p, q) \otimes M_2(\mathbb{R})$, $\mathrm{Cl}(p+4, 0) = \mathrm{Cl}(0, p) \otimes M_2(\mathbb{H})$, and similar. Combine to derive the full table by induction.

**Subgoal decomposition:**

1. **Subgoal 1: Base cases.** Compute $\mathrm{Cl}(0, 0), \mathrm{Cl}(1, 0), \mathrm{Cl}(0, 1), \mathrm{Cl}(2, 0), \mathrm{Cl}(1, 1), \mathrm{Cl}(0, 2)$ directly.
   - *Hint:* Use dimension counts and explicit generators.
   - *Why needed:* These are the seeds for the induction.

2. **Subgoal 2: Multiplicativity of Clifford algebras.** $\mathrm{Cl}((V_1, Q_1) \oplus (V_2, Q_2)) \cong \mathrm{Cl}(V_1, Q_1) \hat\otimes \mathrm{Cl}(V_2, Q_2)$ (graded tensor product).
   - *Hint:* By the universal property, define the isomorphism by mapping generators to generators in the tensor product.
   - *Why needed:* The multiplicativity is what enables the inductive build-up.

3. **Subgoal 3: The "increment $(p, q) \to (p+1, q+1)$" identity.**  $\mathrm{Cl}(p+1, q+1) \cong \mathrm{Cl}(p, q) \otimes M_2(\mathbb{R})$.
   - *Hint:* Add one "+" and one "−" basis vector; their product squares to $-1$ and anticommutes with both. Use this to construct the $M_2(\mathbb{R})$ part.
   - *Why needed:* This is the simplest inductive step, used repeatedly.

4. **Subgoal 4: The "increment $(p, q) \to (p+4, q)$" identity.** $\mathrm{Cl}(p+4, q) \cong \mathrm{Cl}(q, p) \otimes M_2(\mathbb{H})$.
   - *Hint:* Adding $4$ "+" vectors gives a Clifford algebra whose volume element squares to $-1$ (in our convention). Combine with quaternionic structure to get $M_2(\mathbb{H})$.
   - *Why needed:* This relates signatures and gives the rotation back to $\mathbb{H}$.

5. **Subgoal 5: Period-$8$ identity.** Combine the $4$-step relations to derive $\mathrm{Cl}(p+8, q) \cong \mathrm{Cl}(p, q) \otimes M_{16}(\mathbb{R})$.
   - *Hint:* $\mathrm{Cl}(p+8, q) = \mathrm{Cl}((p+4) + 4, q) = \mathrm{Cl}(q, p+4) \otimes M_2(\mathbb{H}) = \mathrm{Cl}(p + 4, q) \otimes \cdots$ — combine.
   - *Why needed:* This is the period-$8$ statement.

6. **Subgoal 6: Tabulate the period-$8$ pattern.** Apply the inductive relations starting from base cases to fill in $\mathrm{Cl}(p, q)$ for $p - q \equiv k \pmod 8$ for each $k = 0, 1, \ldots, 7$.
   - *Hint:* Direct calculation.
   - *Why needed:* This gives the final table.

---

# Lemma Decomposition

> [!note]- Lemma 1: Multiplicativity (graded tensor product).
> **Statement:** For quadratic spaces $(V_1, Q_1)$ and $(V_2, Q_2)$, there is a natural algebra isomorphism $\mathrm{Cl}(V_1 \oplus V_2, Q_1 \oplus Q_2) \cong \mathrm{Cl}(V_1, Q_1) \hat\otimes \mathrm{Cl}(V_2, Q_2)$, where $\hat\otimes$ is the **graded tensor product** with sign convention $(a \otimes b)(c \otimes d) = (-1)^{|b||c|}(ac \otimes bd)$ for homogeneous $a, b, c, d$.
>
> **Hint:** Use the universal property: define the map by sending $(v_1, 0) \in V_1 \oplus V_2$ to $\iota_1(v_1) \otimes 1$ and $(0, v_2)$ to $1 \otimes \iota_2(v_2)$ in the graded tensor product. Verify the Clifford relation in the target — using the sign in the graded tensor product is essential to get $(1 \otimes v_2)(v_1 \otimes 1) = -v_1 \otimes v_2$, matching the requirement that $(v_1, 0)$ and $(0, v_2)$ anticommute in $\mathrm{Cl}(V_1 \oplus V_2)$.
>
> **Why needed:** This multiplicativity is what allows building higher-dimensional Clifford algebras from lower-dimensional ones.
>
> > [!note]- Full proof
> > Define $\varphi: V_1 \oplus V_2 \to \mathrm{Cl}(V_1) \hat\otimes \mathrm{Cl}(V_2)$ by $\varphi(v_1, v_2) = v_1 \otimes 1 + 1 \otimes v_2$ (where we identify $v_j \in V_j \subset \mathrm{Cl}(V_j)$ via $\iota_j$). Check the Clifford relation: $\varphi(v_1, v_2)^2 = (v_1 \otimes 1)^2 + (1 \otimes v_2)^2 + (v_1 \otimes 1)(1 \otimes v_2) + (1 \otimes v_2)(v_1 \otimes 1) = Q_1(v_1) \otimes 1 + 1 \otimes Q_2(v_2) - 0 = (Q_1(v_1) + Q_2(v_2)) \cdot 1$. (The middle two cross terms cancel by the graded-tensor sign rule.) Equals $(Q_1 \oplus Q_2)(v_1, v_2) \cdot 1$, as needed. By the universal property, $\varphi$ extends to $\tilde\varphi: \mathrm{Cl}(V_1 \oplus V_2, Q_1 \oplus Q_2) \to \mathrm{Cl}(V_1) \hat\otimes \mathrm{Cl}(V_2)$, and dimension count $\dim(\text{LHS}) = 2^{n_1 + n_2} = \dim(\text{RHS})$ makes it an isomorphism.

> [!note]- Lemma 2: $\mathrm{Cl}(1, 1) = M_2(\mathbb{R})$.
> **Statement:** The Clifford algebra of $\mathbb{R}^2$ with signature $(1, 1)$ is isomorphic to $M_2(\mathbb{R})$.
>
> **Hint:** Pick generators $e_1, e_2$ with $e_1^2 = +1, e_2^2 = -1, e_1 e_2 = -e_2 e_1$. Identify $e_1 = \sigma_1, e_2 = i\sigma_2$ in $M_2(\mathbb{C})$ — but $i\sigma_2 = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix}$ is real! So both generators are real matrices, the algebra lives in $M_2(\mathbb{R})$, and dimension count finishes.
>
> **Why needed:** Base case, and the input to the increment $(p, q) \to (p+1, q+1)$ identity.
>
> > [!note]- Full proof
> > In $M_2(\mathbb{R})$, take $e_1 = \begin{pmatrix} 1 & 0 \\ 0 & -1\end{pmatrix} = \sigma_3$ and $e_2 = \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix} = \sigma_1$. Compute: $e_1^2 = I$ ✓ ($Q(e_1) = +1$); $e_2^2 = I$ — wait, we wanted $e_2^2 = -1$. Redo: in signature $(1, 1)$, the *second* generator squares to $-1$. Take $e_1 = \sigma_3$ (so $e_1^2 = I$, ✓) and $e_2 = i\sigma_2 = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix}$ (so $e_2^2 = -I$ ✓, and $e_2 \in M_2(\mathbb{R})$). Verify $e_1 e_2 + e_2 e_1 = 0$: $e_1 e_2 = \begin{pmatrix} 0 & 1 \\ 1 & 0\end{pmatrix}$ and $e_2 e_1 = \begin{pmatrix} 0 & -1 \\ -1 & 0\end{pmatrix}$, sum is $0$ ✓. By the universal property, $\mathrm{Cl}(1, 1) \to M_2(\mathbb{R})$ is an algebra hom; dimension $4 = 4$, hence iso.

> [!note]- Lemma 3: Increment $(p, q) \to (p+1, q+1)$.
> **Statement:** $\mathrm{Cl}(p+1, q+1) \cong \mathrm{Cl}(p, q) \otimes M_2(\mathbb{R})$.
>
> **Hint:** $\mathrm{Cl}(p+1, q+1) = \mathrm{Cl}(p, q) \hat\otimes \mathrm{Cl}(1, 1) = \mathrm{Cl}(p, q) \hat\otimes M_2(\mathbb{R})$. Since $M_2(\mathbb{R})$ is ungraded (or rather, the grading collapses), the graded tensor product equals the ordinary tensor product.
>
> **Why needed:** This is the increment step used in all the inductive arguments.

> [!note]- Lemma 4: Increment $(p, q) \to (p+4, q)$.
> **Statement:** $\mathrm{Cl}(p+4, q) \cong \mathrm{Cl}(q, p) \otimes M_2(\mathbb{H})$.
>
> **Hint:** Use $\mathrm{Cl}(4, 0) = M_2(\mathbb{H})$ (direct calculation from the four anticommuting square-roots of $+1$). Multiplicativity and signature manipulation gives the result.
>
> **Why needed:** Used together with the previous to get the period-$8$ identity.

> [!note]- Lemma 5: Period-$8$ identity.
> **Statement:** $\mathrm{Cl}(p+8, q) \cong \mathrm{Cl}(p, q) \otimes M_{16}(\mathbb{R})$.
>
> **Hint:** Apply Lemma 4 twice: $\mathrm{Cl}(p+8, q) = \mathrm{Cl}((p+4)+4, q) = \mathrm{Cl}(q, p+4) \otimes M_2(\mathbb{H}) = (\mathrm{Cl}(p, q) \otimes M_2(\mathbb{H})) \otimes M_2(\mathbb{H}) = \mathrm{Cl}(p, q) \otimes (M_2(\mathbb{H}) \otimes M_2(\mathbb{H}))$. Use $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{H} = M_4(\mathbb{R})$ (a deep identity) to conclude $M_2(\mathbb{H}) \otimes M_2(\mathbb{H}) = M_4(M_4(\mathbb{R})) = M_{16}(\mathbb{R})$.
>
> **Why needed:** The fundamental period-$8$ statement of the classification.

---

# Formal Proof

> [!note]- Complete formal proof (outline)
> The full proof is long; we give an outline emphasizing the structural steps.
>
> **Base cases.** Compute $\mathrm{Cl}(0, 0) = \mathbb{R}$, $\mathrm{Cl}(1, 0) = \mathbb{R}[e]/(e^2 - 1) = \mathbb{R} \oplus \mathbb{R}$ (with idempotents $\tfrac{1}{2}(1 \pm e)$), $\mathrm{Cl}(0, 1) = \mathbb{R}[e]/(e^2 + 1) = \mathbb{C}$. For $\mathrm{Cl}(2, 0) = M_2(\mathbb{R})$: use $e_1 = \sigma_1, e_2 = \sigma_3$ as real matrices satisfying $e_j^2 = I, \{e_1, e_2\} = 0$; algebra dimension $4 = \dim M_2(\mathbb{R})$. For $\mathrm{Cl}(1, 1) = M_2(\mathbb{R})$: see Lemma 2. For $\mathrm{Cl}(0, 2) = \mathbb{H}$: $e_1, e_2$ with $e_j^2 = -1$ and $e_1 e_2 = -e_2 e_1$; setting $i = e_1, j = e_2, k = e_1 e_2$ recovers Hamilton's relations.
>
> **Multiplicativity (Lemma 1).** The Clifford algebra of a direct sum is the graded tensor product of the Clifford algebras of the summands.
>
> **Inductive step (Lemma 3).** $\mathrm{Cl}(p+1, q+1) \cong \mathrm{Cl}(p, q) \otimes M_2(\mathbb{R})$. This handles "diagonal" moves in the $(p, q)$ grid.
>
> **Higher-dimensional inputs.** $\mathrm{Cl}(3, 0) = \mathrm{Cl}(1, 0) \hat\otimes \mathrm{Cl}(2, 0) = (\mathbb{R} \oplus \mathbb{R}) \hat\otimes M_2(\mathbb{R})$. Using the graded structure, this is $M_2(\mathbb{C})$ (the Pauli algebra). Similarly compute the full $8$-period of base cases.
>
> **Period-$8$ identity (Lemma 5).** $\mathrm{Cl}(p+8, q) \cong \mathrm{Cl}(p, q) \otimes M_{16}(\mathbb{R})$. This is the key periodicity.
>
> **Filling in the table.** Combine the base cases and the inductive relations to derive $\mathrm{Cl}(p, q)$ for all $(p, q)$, with the pattern matching the table.
>
> **Verification of dimension.** At each step, check $\dim_\mathbb{R}\mathrm{Cl}(p, q) = 2^{p+q}$ matches the dimension of the candidate matrix algebra; equality forces the embedding to be an isomorphism.

---

# Cross-Field Exercise Suggestions

1. **Identify the Pauli algebra explicitly as $\mathrm{Cl}(3, 0) = M_2(\mathbb{C})$.** Verify the entries in the low-dimension table by writing down explicit isomorphisms; use the universal property as in [[Ex - Pauli Matrices Generate Cl(R^3)]].

2. **Compute the dimension of the spinor module in various dimensions.** Using the table, compute that the Dirac spinor in $10$ dimensions (relevant for superstring theory) is a $32$-component complex object; in $11$ dimensions (M-theory) it is a $32$-component real Majorana spinor; etc.

3. **Verify $\mathbb{H} \otimes_{\mathbb{R}} \mathbb{H} = M_4(\mathbb{R})$.** This is a deep but elementary fact: the algebra $\mathbb{H} \otimes \mathbb{H}$ contains the orthogonal idempotents $\tfrac{1}{4}(1 \otimes 1 \pm i \otimes i \pm j \otimes j \pm k \otimes k)$ (with constraints making 4 of them); using these one decomposes $\mathbb{H} \otimes \mathbb{H}$ as $M_4(\mathbb{R})$.

4. **Determine when Majorana-Weyl spinors exist.** Combine the Majorana condition (signature $\equiv 0, 1, 2, 6, 7 \pmod 8$) with the Weyl condition (even dimension, $p - q \equiv 0 \pmod 4$). The result: Majorana–Weyl spinors exist only in dimensions $2 \pmod 8$ — so $D = 2, 10, 18, \ldots$. This is why the **superstring lives in $D = 10$**.

---

# Bridges

- **Bott periodicity in real K-theory.** The period-$8$ structure of Clifford algebras is mirrored exactly in real K-theory: $KO^{-n}(\mathrm{pt}) = KO^{-n-8}(\mathrm{pt})$. The Atiyah–Bott–Shapiro construction realizes this connection precisely: there is a natural map from $\mathbb{Z}/2$-graded $\mathrm{Cl}(n)$-modules modulo extension to $KO^{-n}(\mathrm{pt})$, and this map is an isomorphism. So the classification of Clifford algebras *is* the algebraic shadow of Bott periodicity.

- **[[Def - Pin and Spin Groups|Spin and pin groups]] across dimensions.** The classification dictates the structure of $\mathrm{Spin}(n)$: in dimension $n$, $\mathrm{Spin}(n) \subset \mathrm{Cl}^0(n, 0)^\times$, and the structure of $\mathrm{Cl}^0(n, 0)$ as a matrix algebra (read from the table) determines $\mathrm{Spin}(n)$ up to isomorphism. The accidental low-dimensional isomorphisms ($\mathrm{Spin}(3) = SU(2)$, $\mathrm{Spin}(4) = SU(2) \times SU(2)$, $\mathrm{Spin}(5) = Sp(2)$, $\mathrm{Spin}(6) = SU(4)$) all follow from the classification's low-dimensional entries.

- **String theory dimension constraints.** The requirement that the superstring admit Majorana–Weyl worldsheet fermions forces the spacetime dimension to satisfy specific constraints derivable from the classification: $D = 10$ for the superstring, $D = 11$ for M-theory (with Majorana but not Weyl spinors), $D = 26$ for the bosonic string. These "magic dimensions" are direct consequences of the period-$8$ Clifford-algebra structure.

- **Hurwitz's theorem (composition algebras).** Hurwitz classified the *normed* real division algebras as $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$ (the four Cayley–Dickson algebras). Three of these ($\mathbb{R}, \mathbb{C}, \mathbb{H}$) appear in the Clifford classification; the octonions $\mathbb{O}$ are conspicuously absent because they are non-associative, while Clifford algebras are by definition associative. The connection between Hurwitz's theorem and the Clifford classification is deep and runs through the **exceptional Lie groups** ($G_2$, $F_4$, $E_6, E_7, E_8$) — but is not yet fully explained.

---

# Unlocked by This

> [!tip] Atiyah-Bott-Shapiro Construction and Real K-Theory
> The **Atiyah–Bott–Shapiro (ABS) construction** (1964) provides a natural isomorphism between the group of $\mathbb{Z}/2$-graded $\mathrm{Cl}(n)$-modules modulo extension to $\mathrm{Cl}(n+1)$-modules and the real K-theory $KO^{-n}(\mathrm{pt})$. This is the deep statement that **the classification of real Clifford algebras** *is* **Bott periodicity in K-theory**: both repeat with period $8$, and the explicit module-theoretic generators on the Clifford side match the homotopy-theoretic generators on the K-theory side. The construction is one of the most important bridges between algebra and topology in 20th-century mathematics.

> [!tip] Periodicity of Symmetry Classes in Condensed Matter Physics
> The **tenfold way** (Altland–Zirnbauer classification) of free-fermion symmetry classes in condensed-matter physics maps directly onto the period-$8$ Clifford structure: the $10$ classes are labeled by the combination of time-reversal, particle-hole, and chiral symmetries, and the classification of topological insulators and superconductors in each dimension follows the period-$8$ pattern. This is one of the most striking applications of the Clifford classification outside pure mathematics — it underlies the entire theory of **topological insulators**, **Weyl semimetals**, and the experimental discoveries of the 2010s in topological condensed matter.

> [!tip] Special Dimensions in Supergravity and String Theory
> The maximal supergravity dimension is $D = 11$, where Majorana spinors exist (signature $(1, 10)$ has $p - q = 9 \equiv 1 \pmod 8$); the dimension cannot be raised further because no Majorana spinors exist in $D = 12$ with Lorentzian signature. The superstring lives in $D = 10$, where Majorana–Weyl spinors exist. These "magic dimensions" are direct outputs of the classification — features of the spinor algebra that no other structure of physics can override.
