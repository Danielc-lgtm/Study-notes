---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Subspace"
  - "Def - Dual Space"
  - "Def - Dual Basis"
  - "Def - Annihilator"
  - "Thm - Dimension of Dual Space"
  - "Thm - Fundamental Theorem of Linear Maps"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be a finite-dimensional vector space over $\mathbb{F}$ and $U \leq V$ a [[Def - Subspace|subspace]]. Prove the **annihilator dimension formula**:
$$\dim U + \dim U^0 = \dim V.$$

Equivalently, $\dim U^0 = \dim V - \dim U$.

Two proofs are worth knowing: the **basis-extension proof** (extend a basis of $U$ to a basis of $V$, dualise, and identify which dual-basis functionals annihilate $U$) and the **dual-inclusion proof** (apply rank-nullity to the dual of the inclusion $i : U \hookrightarrow V$). Carry out both.

**Recall:**

![[Def - Annihilator#The Definition]]

![[Thm - Dimension of Dual Space#Statement]]

The [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]] states $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$ for any linear map $T \in \mathcal{L}(V, W)$ between finite-dimensional spaces.

For a basis $v_1, \dots, v_n$ of $V$, the [[Def - Dual Basis|dual basis]] $\varphi_1, \dots, \varphi_n$ of $V'$ is determined by $\varphi_j(v_k) = \delta_{jk}$.

---

# Convergent Strategy

**Problem class.** This is a *dimension computation* (problem class 2 from the [[Linear Algebra IV — §3E–F Products, Quotients, Duality#Problem-Solving Strategy|topic page]]), and the answer is one of the cleanest identities in dual-space theory: $\dim U^0$ is the *complement* of $\dim U$ inside $\dim V$. The formula is the structural reason why the annihilator is the right notion of "the dual of $U$".

**Assumption pattern.** Finite-dimensional $V$ and a subspace $U$. The two proofs have different inputs: the basis-extension proof uses an explicit basis of $V$ adapted to $U$ (a basis of $U$ extended to one of $V$); the dual-inclusion proof uses the natural inclusion $i : U \hookrightarrow V$ and its dual $i' : V' \to U'$.

**Theorem routing.** The basis-extension proof goes: choose basis $u_1, \dots, u_m$ of $U$, extend to basis $u_1, \dots, u_m, w_1, \dots, w_k$ of $V$ ($m + k = n$), take the dual basis $\varphi_1, \dots, \varphi_m, \psi_1, \dots, \psi_k$ of $V'$, and observe that the functionals annihilating $U$ are exactly those with zero coefficients on the $\varphi_j$ (which would "pick up" elements of $U$), leaving just the $\psi_l$. So $U^0 = \operatorname{span}(\psi_1, \dots, \psi_k)$, of dimension $k = n - m = \dim V - \dim U$.

The dual-inclusion proof goes: $i : U \hookrightarrow V$ has dual $i' : V' \to U'$, and one checks $\operatorname{null} i' = U^0$. The fundamental theorem of linear maps gives $\dim V' = \dim \operatorname{null} i' + \dim \operatorname{range} i' = \dim U^0 + \dim \operatorname{range} i'$. The range $\operatorname{range} i' = U'$ (every functional on $U$ extends to one on $V$), so $\dim \operatorname{range} i' = \dim U' = \dim U$. Substituting and using $\dim V' = \dim V$ gives the formula.

**Key decision point.** The non-obvious move is *recognising that the dual of the inclusion is the right map to apply rank-nullity to*. The map $i' : V' \to U'$ goes from "functionals on $V$" to "functionals on $U$", and its null space is exactly $U^0$ — the functionals that restrict to zero on $U$. This is the structural source of the formula: the formula is rank-nullity applied to the dual of the inclusion.

---

# Legal Operations Used

From [[Linear Algebra IV — §3E–F Products, Quotients, Duality#Legal Operations|the topic page]]:

1. **Use the dual basis to read off coordinates** (operation 5). The basis-extension proof reads coefficients of $V'$-elements in a specific dual basis.

2. **Dualize a map to reverse direction** (operation 6). The dual-inclusion proof applies dualisation to the inclusion $U \hookrightarrow V$ to get a map $V' \to U'$.

3. **Take [[Def - Annihilator|annihilators]] to reverse inclusions** (operation 7). The whole exercise is about understanding the annihilator construction at the level of [[Def - Dimension|dimensions]].

---

# Hints

> [!note]- Hint 1
> For the basis-extension proof: choose a basis $u_1, \dots, u_m$ of $U$ and extend to a basis $u_1, \dots, u_m, w_1, \dots, w_k$ of $V$. Let $\varphi_1, \dots, \varphi_m, \psi_1, \dots, \psi_k$ be the dual basis. Which of these dual-basis functionals are in $U^0$?

> [!note]- Hint 2
> A functional $\varphi = \sum a_j \varphi_j + \sum b_l \psi_l$ vanishes on $U$ iff $\varphi(u_i) = 0$ for every $i$. Compute $\varphi(u_i)$ using biorthogonality.

> [!note]- Hint 3
> For the dual-inclusion proof: consider the inclusion $i : U \to V$, $i(u) = u$. The dual map $i' : V' \to U'$ takes a functional $\varphi$ on $V$ to its restriction $\varphi|_U$.

> [!note]- Hint 4
> Show that $\operatorname{null} i' = U^0$ (a functional restricts to zero on $U$ iff it annihilates $U$), and $\operatorname{range} i' = U'$ (every functional on $U$ extends to a functional on $V$). Then apply rank-nullity to $i'$.

> [!note]- Hint 5
> For the extension-of-functionals subfact: given $\varphi \in U'$, define $\tilde \varphi \in V'$ by $\tilde \varphi(u + w) = \varphi(u)$ for $u \in U, w \in W$, where $W$ is any complement of $U$. Or use the linear-map extension lemma directly with the basis $u_1, \dots, u_m, w_1, \dots, w_k$.

---

# Solution

The proof has two versions; carry out both.

**Version A (Basis-Extension Proof).**

Choose a basis adapted to $U$, dualise, and identify the annihilator as the span of the "new" dual-basis functionals.

**Step A1: Construct an adapted basis.**

Choose a basis $u_1, \dots, u_m$ of $U$ where $m = \dim U$. By the [[Thm - Every Linearly Independent List Extends to a Basis|basis-extension lemma]], extend to a basis $u_1, \dots, u_m, w_1, \dots, w_k$ of $V$, where $m + k = \dim V = n$.

**Step A2: Take the dual basis.**

Let $\varphi_1, \dots, \varphi_m, \psi_1, \dots, \psi_k$ be the dual basis of $V'$, defined by
$$\varphi_i(u_j) = \delta_{ij}, \quad \varphi_i(w_l) = 0, \quad \psi_l(u_j) = 0, \quad \psi_l(w_{l'}) = \delta_{l l'},$$
for $i, j \in \{1, \dots, m\}$, $l, l' \in \{1, \dots, k\}$.

**Step A3: Compute $U^0$.**

A general element $\varphi \in V'$ has unique expansion $\varphi = \sum_{i=1}^m a_i \varphi_i + \sum_{l=1}^k b_l \psi_l$ for some $a_i, b_l \in \mathbb{F}$. Then $\varphi \in U^0$ iff $\varphi(u_j) = 0$ for every $j = 1, \dots, m$.

> [!note]- Derivation
> Compute $\varphi(u_j)$ using biorthogonality:
> $$\varphi(u_j) = \sum_{i=1}^m a_i \varphi_i(u_j) + \sum_{l=1}^k b_l \psi_l(u_j) = \sum_{i=1}^m a_i \delta_{ij} + 0 = a_j.$$
> The first sum collapses by biorthogonality ($\varphi_i(u_j) = \delta_{ij}$), and the second sum is zero ($\psi_l(u_j) = 0$). So $\varphi(u_j) = a_j$.
>
> Hence $\varphi \in U^0$ iff $a_j = 0$ for every $j$, iff $\varphi = \sum_{l=1}^k b_l \psi_l \in \operatorname{span}(\psi_1, \dots, \psi_k)$.

**Step A4: Conclude.**

$U^0 = \operatorname{span}(\psi_1, \dots, \psi_k)$, and the $\psi_l$ are linearly independent (being part of a basis of $V'$), so they form a basis of $U^0$. Hence
$$\dim U^0 = k = n - m = \dim V - \dim U. \qquad \blacksquare$$

---

**Version B (Dual-Inclusion Proof).**

Apply rank-nullity to the dual of the inclusion $i : U \hookrightarrow V$.

**Step B1: Set up the inclusion and its dual.**

Let $i : U \to V$ be the inclusion, $i(u) = u$. It is a linear map. The [[Def - Dual Map|dual map]] $i' : V' \to U'$ is defined by $i'(\varphi) = \varphi \circ i$. For $u \in U$:
$$(i'(\varphi))(u) = (\varphi \circ i)(u) = \varphi(i(u)) = \varphi(u).$$
So $i'(\varphi)$ is just the *restriction* of $\varphi$ from $V$ to $U$. Denote this restriction $\varphi|_U$.

**Step B2: Compute the null space of $i'$.**

$\operatorname{null} i' = \{\varphi \in V' : \varphi|_U = 0\} = \{\varphi \in V' : \varphi(u) = 0 \text{ for all } u \in U\} = U^0$.

> [!note]- Derivation
> By definition, $\varphi \in \operatorname{null} i'$ iff $i'(\varphi) = 0$ in $U'$. Since $i'(\varphi)$ is the restriction $\varphi|_U$, this means $\varphi|_U = 0$ as a functional on $U$, i.e. $\varphi(u) = 0$ for every $u \in U$. By the definition of $U^0$, this is exactly $\varphi \in U^0$. So $\operatorname{null} i' = U^0$.

**Step B3: Compute the range of $i'$.**

$\operatorname{range} i' = U'$.

> [!note]- Derivation
> *Inclusion $\operatorname{range} i' \subseteq U'$:* tautological — every $i'(\varphi)$ is a functional on $U$, hence in $U'$.
>
> *Reverse inclusion $U' \subseteq \operatorname{range} i'$:* every $\varphi \in U'$ has an extension $\tilde \varphi \in V'$ with $\tilde \varphi|_U = \varphi$, by the linear-map extension lemma. Concretely: extend a basis $u_1, \dots, u_m$ of $U$ to a basis $u_1, \dots, u_m, w_1, \dots, w_k$ of $V$, define $\tilde \varphi(u_i) = \varphi(u_i)$ and $\tilde \varphi(w_l) = 0$ (or any value — the choice does not affect $\tilde \varphi|_U$), and extend linearly. Then $i'(\tilde \varphi) = \tilde \varphi|_U = \varphi$. So $\varphi \in \operatorname{range} i'$.
>
> Hence $\operatorname{range} i' = U'$.

**Step B4: Apply rank-nullity and conclude.**

By the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem]] applied to $i' : V' \to U'$:
$$\dim V' = \dim \operatorname{null} i' + \dim \operatorname{range} i' = \dim U^0 + \dim U'.$$
Using $\dim V' = \dim V$ and $\dim U' = \dim U$ (the [[Thm - Dimension of Dual Space|dual dimension theorem]] applied to $V$ and $U$):
$$\dim V = \dim U^0 + \dim U,$$
i.e. $\dim U^0 = \dim V - \dim U$. $\blacksquare$

> [!note]- Complete formal solution
> *Version A (basis-extension).* Choose basis $u_1, \dots, u_m$ of $U$, extend to basis $u_1, \dots, u_m, w_1, \dots, w_k$ of $V$ (with $m + k = n$). Take the dual basis $\varphi_1, \dots, \varphi_m, \psi_1, \dots, \psi_k$ of $V'$. For $\varphi = \sum a_i \varphi_i + \sum b_l \psi_l$:
> $$\varphi(u_j) = a_j \quad \text{(by biorthogonality)},$$
> so $\varphi \in U^0$ iff $a_j = 0$ for all $j$ iff $\varphi \in \operatorname{span}(\psi_1, \dots, \psi_k)$. Hence $U^0 = \operatorname{span}(\psi_1, \dots, \psi_k)$, of dimension $k = n - m = \dim V - \dim U$.
>
> *Version B (dual-inclusion).* The dual of $i : U \hookrightarrow V$ is $i' : V' \to U'$, $i'(\varphi) = \varphi|_U$. Direct check: $\operatorname{null} i' = U^0$, $\operatorname{range} i' = U'$. By rank-nullity on $i'$ and $\dim V' = \dim V$, $\dim U' = \dim U$:
> $$\dim V = \dim U^0 + \dim U. \qquad \blacksquare$$

> [!note]- Sanity check by example
> Take $V = \mathbb{R}^5$ with standard basis $e_1, \dots, e_5$ and dual basis $\varphi_1, \dots, \varphi_5$ (coordinate projections). Let $U = \operatorname{span}(e_1, e_2)$, of dimension $2$. The formula predicts $\dim U^0 = 5 - 2 = 3$. Direct computation: $\varphi = \sum a_j \varphi_j$ is in $U^0$ iff $\varphi(e_1) = a_1 = 0$ and $\varphi(e_2) = a_2 = 0$, so $U^0 = \operatorname{span}(\varphi_3, \varphi_4, \varphi_5)$, dimension $3$. The formula holds.

---

# Key Takeaways

**The dimension formula $\dim U + \dim U^0 = \dim V$ is the structural source of "annihilator-complement duality"**. The two [[Def - Dimension|dimensions]] complement each other — small $U$ has big annihilator, and vice versa. The boundary cases are the most informative: $\{0\}^0 = V'$ (everything annihilates zero) and $V^0 = \{0\}$ (only zero annihilates everything). The formula is what makes the order-reversing bijection $U \mapsto U^0$ a genuine *bijection* on subspace lattices (in finite dimensions), not just an order-reversing map. The same form of formula appears for orthogonal complements in inner product spaces ($\dim U + \dim U^\perp = \dim V$, [[Linear Algebra VI — §6 Inner Product Spaces|Chapter 6]]) and for the variety-[[Def - Ideal|ideal]] correspondence in algebraic geometry (codimension complements dimension). When you see a Galois connection with a non-degenerate pairing, expect a dimension-complement formula.

**Two proofs, two perspectives — both worth knowing**. The basis-extension proof is *constructive*: it produces an explicit basis of $U^0$ via the dual basis. This is what you want when the problem asks for a specific functional or a specific generator of the annihilator. The dual-inclusion proof is *structural*: it identifies $U^0$ as the null space of the dual of the inclusion, and the formula falls out of rank-nullity. This is what you want when the problem asks "why does the formula hold" or generalises to settings where bases are awkward (such as inner product spaces or infinite-dimensional spaces with topology). Both proofs are short, and seeing both gives the cleanest mental model of why the annihilator is "the right" dual to a subspace.

**The recognition trigger is "I have a subspace and I need a complementary dimension"**. Whenever a problem asks for a dimension formula involving a subspace and "the rest of the space", check whether the answer involves an annihilator. The annihilator formula converts subspace-dimension questions on $V$ into subspace-dimension questions on $V'$, swapping inclusion direction and turning sums into intersections. This is also the foundation for the *codimension* viewpoint: $\dim U^0$ is "the codimension of $U$ in $V$" (the dimension of the complement), and a *hyperplane* is a codimension-1 subspace, which corresponds to a 1-dimensional annihilator — that is, a hyperplane is the null space of a single non-zero functional.

**The identities $(U + W)^0 = U^0 \cap W^0$ and $(U \cap W)^0 = U^0 + W^0$ are immediate consequences.** Once you have the basic annihilator-dimension formula, these are easy: both sides have the same dimension (by the present formula and the [[Thm - Dimension of a Sum of Subspaces|sum-of-subspaces dimension formula]]) and a direct inclusion in one direction. The first identity says "annihilator of a sum is intersection of [[Def - Annihilator|annihilators]]" — a functional vanishes on both $U$ and $W$ iff it vanishes on their union, iff it vanishes on their sum (since vanishing on a spanning set extends). The second identity is the dual, applied to [[Def - Subspace|subspaces]] of $V'$. These two identities, combined with the dimension formula, are the practical *toolkit* for computing dimensions of annihilators.

**Cross-link to companion exercises.** This dimension formula is invoked in the proof of [[Thm - Null Space and Range of Dual Map]] (specifically in Lemma 3, where $\dim \operatorname{range} T' = \dim \operatorname{range} T$ is derived) and in [[Ex - Double dual is naturally isomorphic to the original]] (where the dimension equality $\dim V'' = \dim V$ is the input that lets the canonical injection $\Lambda$ become an isomorphism). The constructive Version A of the proof closely mirrors the technique used in many algebraic-geometry codimension computations.
