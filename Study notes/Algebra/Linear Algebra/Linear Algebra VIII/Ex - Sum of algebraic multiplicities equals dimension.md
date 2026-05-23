---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Algebraic and Geometric Multiplicity"
  - "Def - Generalized Eigenspace"
  - "Thm - Generalized Eigenspace Decomposition"
tags: [algebra, linear-algebra]
---

# Problem Statement

Suppose $\mathbf{F} = \mathbb{C}$ and $T \in \mathcal{L}(V)$. Prove that the sum of the algebraic multiplicities of the eigenvalues of $T$ equals $\dim V$:

$$\sum_{\lambda \text{ eigenvalue of } T} \dim G(\lambda, T) = \dim V.$$

**Recall:**

The objects are an operator on a complex space and its generalized eigenspaces.

![[Def - Generalized Eigenspace#The Definition]]

![[Def - Algebraic and Geometric Multiplicity#The Definition]]

The headline theorem [[Thm - Generalized Eigenspace Decomposition]] says:

![[Thm - Generalized Eigenspace Decomposition#Statement]]

In particular, $V$ is the direct sum of the generalized eigenspaces.

The dimension formula for a direct sum says $\dim(U_1 \oplus \cdots \oplus U_m) = \sum_k \dim U_k$.

---

# Convergent Strategy

**Problem class.** This is a *dimension-counting consequence of a direct-sum decomposition* problem — given a structural decomposition theorem, extract the dimension identity. The class is drilled by countless results that combine a decomposition (in this case, the generalized eigenspace decomposition) with the additivity of dimension across direct sums to extract a numerical consequence.

**Assumption pattern.** $\mathbf{F} = \mathbb{C}$ is the crucial hypothesis — it is what makes the generalized eigenspace decomposition apply. Over $\mathbb{R}$ the result fails: an operator on $\mathbb{R}^2$ with no real eigenvalues has *no* generalized eigenspaces at all, so the left side is an empty sum (= $0$), while the right side is $2$. The complex hypothesis ensures every operator has at least one eigenvalue, and the generalized eigenspaces fill $V$.

**Theorem routing.** Single theorem chain: [[Thm - Generalized Eigenspace Decomposition]] $\to$ direct-sum dimension formula. The theorem gives $V = \bigoplus_k G(\lambda_k, T)$; the dimension formula gives $\dim V = \sum_k \dim G(\lambda_k, T)$. Done.

**Key decision point.** The non-obvious move (such as it is) is to *recognise that the statement of the decomposition theorem is overkill for the dimension identity*. The theorem says the sum is direct *and* equals $V$, with each piece a $T$-invariant subspace on which $T - \lambda_k I$ is nilpotent. We only need the *dimension* identity, which uses just the direct-sum property and the fact that the sum is $V$. The structural properties (invariance, nilpotence on each piece) are not used. This is a soft proof — applying a heavy theorem and immediately taking [[Def - Dimension|dimensions]] — but it is the right pattern. Many corollaries of the generalized eigenspace decomposition are obtained by this "structural theorem $\to$ take [[Def - Dimension|dimensions]]" route.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Linear Algebra VIII — §8 Operators on Complex Vector Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Decompose into generalized eigenspaces** (operation 1). The first move is to invoke the generalized eigenspace decomposition and rewrite $V$ as a direct sum.

2. **Read off dimensional invariants of $T$** (a variant of operation 7, here for the dimension itself rather than the trace or determinant). The dimension is additive across direct sums; this is the only nontrivial step.

---

# Hints

> [!note]- Hint 1
> The [[Thm - Generalized Eigenspace Decomposition|generalized eigenspace decomposition]] gives $V = G(\lambda_1, T) \oplus \cdots \oplus G(\lambda_m, T)$. Take dimensions.

> [!note]- Hint 2
> For a direct sum $V = U_1 \oplus \cdots \oplus U_m$ of [[Def - Subspace|subspaces]], $\dim V = \dim U_1 + \cdots + \dim U_m$. Apply this with $U_k = G(\lambda_k, T)$.

> [!note]- Hint 3
> The $\dim G(\lambda_k, T)$ is by definition the algebraic multiplicity $\operatorname{mult}_{\text{alg}}(\lambda_k)$. So $\dim V = \sum_k \operatorname{mult}_{\text{alg}}(\lambda_k)$.

---

# Solution

The strategy is to invoke the generalized eigenspace decomposition and immediately take dimensions. The whole proof is two steps.

**Step 1: Apply the generalized eigenspace decomposition.**

By [[Thm - Generalized Eigenspace Decomposition]] (since $\mathbf{F} = \mathbb{C}$),

$$V = G(\lambda_1, T) \oplus G(\lambda_2, T) \oplus \cdots \oplus G(\lambda_m, T),$$

where $\lambda_1, \dots, \lambda_m$ are the distinct eigenvalues of $T$.

> [!note]- Derivation
> The generalized eigenspace decomposition says: for $T \in \mathcal{L}(V)$ on a complex space, the generalized eigenspaces $G(\lambda_k, T)$ for the distinct eigenvalues $\lambda_k$ are $T$-invariant, $(T - \lambda_k I)|_{G(\lambda_k, T)}$ is nilpotent for each $k$, and $V = \bigoplus G(\lambda_k, T)$. We use only the third part of the conclusion.

**Step 2: Take dimensions.**

For a direct sum of [[Def - Subspace|subspaces]] $V = U_1 \oplus \cdots \oplus U_m$, the dimension formula gives $\dim V = \sum_k \dim U_k$. Applied to the generalized eigenspaces,

$$\dim V = \sum_{k=1}^m \dim G(\lambda_k, T) = \sum_{k=1}^m \operatorname{mult}_{\text{alg}}(\lambda_k).$$

> [!note]- Derivation
> The dimension formula for a direct sum is a standard result: if $V = U_1 \oplus \cdots \oplus U_m$, then $\dim V = \dim U_1 + \cdots + \dim U_m$. (Proof sketch: choose a basis for each $U_k$; their concatenation is a basis for $V$ because the sum is direct, and the total number of vectors is the sum of dimensions.)
>
> By definition (see [[Def - Algebraic and Geometric Multiplicity]]), the algebraic multiplicity of $\lambda_k$ is $\dim G(\lambda_k, T)$. So $\dim V = \sum_k \dim G(\lambda_k, T) = \sum_k \operatorname{mult}_{\text{alg}}(\lambda_k)$, as desired.

> [!note]- Complete formal solution
> Let $\mathbf{F} = \mathbb{C}$ and $T \in \mathcal{L}(V)$, with distinct eigenvalues $\lambda_1, \dots, \lambda_m$.
>
> By the generalized eigenspace decomposition ([[Thm - Generalized Eigenspace Decomposition]]),
> $$V = G(\lambda_1, T) \oplus G(\lambda_2, T) \oplus \cdots \oplus G(\lambda_m, T).$$
>
> Taking dimensions and using the additivity of dimension across direct sums,
> $$\dim V = \sum_{k=1}^m \dim G(\lambda_k, T).$$
>
> By definition of the algebraic multiplicity ([[Def - Algebraic and Geometric Multiplicity]]), $\dim G(\lambda_k, T) = \operatorname{mult}_{\text{alg}}(\lambda_k)$. Hence
> $$\dim V = \sum_{k=1}^m \operatorname{mult}_{\text{alg}}(\lambda_k),$$
> as required. $\blacksquare$

---

# Key Takeaways

**Structural decompositions yield dimensional identities by taking dimensions.** The pattern "take a structural theorem, take dimensions, get a dimension identity" recurs throughout linear algebra. The generalized eigenspace decomposition gives "the sum of algebraic multiplicities equals $\dim V$"; the eigenspace decomposition for diagonalisable operators gives "the sum of geometric multiplicities equals $\dim V$"; the rank-nullity theorem can be seen as taking dimensions of the decomposition $V \cong \operatorname{null} T \oplus W$ for a complement $W$; the singular value decomposition gives several dimension formulas similarly. Whenever a structural decomposition appears in a problem, ask immediately what dimension identity it yields — this is one of the most reliable corollary patterns in the subject.

**The complex hypothesis is what makes the result clean.** Over $\mathbb{C}$, the generalized eigenspace decomposition exhausts $V$, so the algebraic multiplicities sum to $\dim V$ exactly. Over $\mathbb{R}$, an operator may have no eigenvalues at all (e.g., rotation by $90°$ on $\mathbb{R}^2$), in which case the generalized eigenspaces of $T$ on $V_\mathbb{R}$ are all zero, and the sum of multiplicities is $0 < \dim V$. The cleanest workaround over $\mathbb{R}$ is to *complexify*: view $V_\mathbb{R}$ as a real subspace of $V_\mathbb{R} \otimes_\mathbb{R} \mathbb{C}$, run the complex theory on the complexification, and observe that complex-conjugate eigenvalues come in pairs. The transferable lesson is that the cleanness of "sum of multiplicities = dimension" is a *complex-field* phenomenon, and adapting the result to other fields requires careful tracking of the irreducible factors of the minimal polynomial.

**The algebraic multiplicity is the right notion for this identity, not the geometric.** The geometric multiplicities sum to $\leq \dim V$, with equality only when $T$ is diagonalisable. The algebraic multiplicities always sum to exactly $\dim V$. This distinction is the algebraic content of "non-diagonalisable operators still have full-dimensional generalized eigenspaces" — the failure of diagonalisability shows up as a discrepancy $\dim G(\lambda, T) - \dim E(\lambda, T) > 0$ at some eigenvalue, but $\dim G(\lambda, T)$ summed across eigenvalues still equals $\dim V$. The reusable insight is that when you want an exact dimension identity, the algebraic multiplicity is the structural invariant to use; the geometric multiplicity is for finer questions (number of Jordan blocks, diagonalisability checks).
