---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Alternate Forms and the Exterior Product"
  - "Def - Tensor Operations"
tags: [physics, special-relativity]
---

# Problem Statement

Work in an orthonormal frame, mostly-minus signature, $c = 1$. Index $0$ is time, $i, j, k \in \{1,2,3\}$ are space.

1. Show that a $2$-form expands as $A = \tfrac12 A_{\alpha\beta}\,e^\alpha\wedge e^\beta = \sum_{\alpha<\beta} A_{\alpha\beta}\,e^\alpha\wedge e^\beta$, reconciling the $\tfrac12$-with-all-indices form with the strictly-ordered-sum form.
2. List the six basis $2$-forms and the six independent components, identifying which are "electric-type" ($0i$) and which are "magnetic-type" ($ij$).
3. Write the electromagnetic field strength $F$ (with electric field $E_i$ and magnetic field $B_i$ relative to this frame) in the wedge basis, and read off its six components $F_{\alpha\beta}$.
4. Verify that the expansion reproduces the standard matrix $F_{\mu\nu}$, and confirm that the three $F_{0i}$ entries carry $\mathbf E$ while the three $F_{ij}$ entries carry $\mathbf B$.

**Recall:**

![[Def - Alternate Forms and the Exterior Product#The Definition]]

A [[Def - Alternate Forms and the Exterior Product|2-form]] expands in the wedge basis as $A = \sum_{\alpha<\beta} A_{\alpha\beta}\,e^\alpha\wedge e^\beta$, with $A_{\alpha\beta} = A(e_\alpha, e_\beta)$ the antisymmetric components. The field strength $F$ is the $2$-form whose components relative to an observer are the electric and magnetic fields.

---

# Convergent Strategy

**Problem class.** A *compute-a-tensor-operation* and *read-off-components* problem, exercising the [[Def - Alternate Forms and the Exterior Product|wedge-basis expansion]]. The [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality#Problem-Solving Strategy|topic strategy]]: expand in the strictly-increasing basis to get independent components.

**Assumption pattern.** Antisymmetry of $A_{\alpha\beta}$ (so $A_{\alpha\alpha} = 0$ and $A_{\beta\alpha} = -A_{\alpha\beta}$) reconciles the two forms of the expansion. The physical identification of $F_{0i}$ with $\mathbf E$ and $F_{ij}$ with $\mathbf B$ is the standard convention.

**Theorem routing.** Part 1: split the double sum into $\alpha < \beta$, $\alpha > \beta$, $\alpha = \beta$ and use antisymmetry. Part 2: enumerate the six $\binom{4}{2}$ basis elements. Part 3: assemble $F$ from $E_i$ and $B_i$. Part 4: match to the matrix.

**Key decision point.** The crux is the factor-of-two reconciliation: the form $\tfrac12 A_{\alpha\beta}e^\alpha\wedge e^\beta$ sums over *all* index pairs (double-counting each unordered pair and adding zero on the diagonal), while $\sum_{\alpha<\beta}A_{\alpha\beta}e^\alpha\wedge e^\beta$ sums over *ordered* pairs once. Antisymmetry of both $A_{\alpha\beta}$ and $e^\alpha\wedge e^\beta$ makes the two equal. Tracking this factor of two — which recurs in every $2$-form computation — is the lesson.

---

# Legal Operations Used

1. **Operation 5 from the topic page (expand a $p$-form in the wedge basis).** The central operation: writing $A$ and $F$ in the basis $e^\alpha\wedge e^\beta$.

2. **Operation 4 from the topic page (wedge two forms).** Used implicitly in handling the antisymmetric basis monomials $e^\alpha\wedge e^\beta = -e^\beta\wedge e^\alpha$.

---

# Hints

> [!note]- Hint 1
> In $\tfrac12 A_{\alpha\beta}e^\alpha\wedge e^\beta$, the diagonal terms ($\alpha = \beta$) vanish ($e^\alpha\wedge e^\alpha = 0$), and the pair $(\alpha,\beta)$ with $\alpha < \beta$ plus $(\beta,\alpha)$ with $\beta > \alpha$ each contribute $A_{\alpha\beta}e^\alpha\wedge e^\beta$ (using $A_{\beta\alpha}e^\beta\wedge e^\alpha = (-A_{\alpha\beta})(-e^\alpha\wedge e^\beta) = A_{\alpha\beta}e^\alpha\wedge e^\beta$), so the $\tfrac12$ and the doubling cancel.

> [!note]- Hint 2
> The six basis $2$-forms are $e^0\wedge e^1, e^0\wedge e^2, e^0\wedge e^3$ (time-space, "electric") and $e^1\wedge e^2, e^1\wedge e^3, e^2\wedge e^3$ (space-space, "magnetic").

> [!note]- Hint 3
> Convention: $F_{0i} = E_i$ (electric) and $F_{ij} = \epsilon_{ijk}B^k$ — i.e. $F_{12} = B_3$, $F_{13} = -B_2$, $F_{23} = B_1$ (magnetic). Then $F = \sum_{\alpha<\beta}F_{\alpha\beta}e^\alpha\wedge e^\beta = E_i\,e^0\wedge e^i + \tfrac12\epsilon_{ijk}B^k\,e^i\wedge e^j$.

---

# Solution

The field strength is the canonical $2$-form, and expanding it in the wedge basis is how its six components become $(\mathbf E, \mathbf B)$. The plan: reconcile the two expansion conventions via antisymmetry (Step 1), enumerate the six basis monomials (Step 2), assemble $F$ from the fields (Step 3), and match to the standard matrix (Step 4).

**Step 1: $A = \tfrac12 A_{\alpha\beta}e^\alpha\wedge e^\beta = \sum_{\alpha<\beta}A_{\alpha\beta}e^\alpha\wedge e^\beta$.**

> [!note]- Derivation
> Split the double sum $\tfrac12\sum_{\alpha,\beta}A_{\alpha\beta}e^\alpha\wedge e^\beta$ into three pieces by the relation between $\alpha$ and $\beta$:
> - *Diagonal $\alpha = \beta$:* $e^\alpha\wedge e^\alpha = 0$, so these contribute nothing.
> - *$\alpha < \beta$:* contributes $\tfrac12\sum_{\alpha<\beta}A_{\alpha\beta}e^\alpha\wedge e^\beta$.
> - *$\alpha > \beta$:* relabel $\alpha\leftrightarrow\beta$ to get $\tfrac12\sum_{\alpha<\beta}A_{\beta\alpha}e^\beta\wedge e^\alpha$. Now $A_{\beta\alpha} = -A_{\alpha\beta}$ (antisymmetric components) and $e^\beta\wedge e^\alpha = -e^\alpha\wedge e^\beta$ (antisymmetric basis), so $A_{\beta\alpha}e^\beta\wedge e^\alpha = (-A_{\alpha\beta})(-e^\alpha\wedge e^\beta) = A_{\alpha\beta}e^\alpha\wedge e^\beta$. This piece is also $\tfrac12\sum_{\alpha<\beta}A_{\alpha\beta}e^\alpha\wedge e^\beta$.
>
> Adding the two non-vanishing pieces: $\tfrac12 + \tfrac12 = 1$ times $\sum_{\alpha<\beta}A_{\alpha\beta}e^\alpha\wedge e^\beta$. Hence
> $$A = \tfrac12 A_{\alpha\beta}e^\alpha\wedge e^\beta = \sum_{\alpha<\beta}A_{\alpha\beta}e^\alpha\wedge e^\beta.$$
> The $\tfrac12$ is exactly the symmetry factor for double-counting each unordered pair; the ordered-sum form makes the $\binom{4}{2} = 6$ independent components manifest.

**Step 2: the six basis $2$-forms and components.**

> [!note]- Derivation
> The strictly-increasing index pairs give six basis $2$-forms, naturally split into time-space and space-space:
> $$\underbrace{e^0\wedge e^1,\ e^0\wedge e^2,\ e^0\wedge e^3}_{\text{electric-type } (0i)}, \qquad \underbrace{e^1\wedge e^2,\ e^1\wedge e^3,\ e^2\wedge e^3}_{\text{magnetic-type } (ij)}.$$
> Correspondingly, a general $2$-form has six independent components: $A_{01}, A_{02}, A_{03}$ (one time, one space index) and $A_{12}, A_{13}, A_{23}$ (two space indices). The "electric-type" components ($0i$) flip sign when both indices are raised (one time, one space → $-1$); the "magnetic-type" components ($ij$) keep their sign (two space → $+1$). This is the algebraic origin of the different behaviour of $\mathbf E$ and $\mathbf B$ under index-raising and under boosts.

**Step 3: the field strength in the wedge basis.**

> [!note]- Derivation
> With the convention $F_{0i} = E_i$ and $F_{ij} = \epsilon_{ijk}B^k$ (so $F_{12} = B_3$, $F_{23} = B_1$, $F_{31} = B_2$), the wedge-basis expansion is
> $$F = \sum_{\alpha<\beta}F_{\alpha\beta}\,e^\alpha\wedge e^\beta = \underbrace{F_{0i}\,e^0\wedge e^i}_{\text{electric}} + \underbrace{\sum_{i<j}F_{ij}\,e^i\wedge e^j}_{\text{magnetic}} = E_i\,e^0\wedge e^i + \tfrac12\epsilon_{ijk}B^k\,e^i\wedge e^j.$$
> Explicitly,
> $$F = E_1\,e^0\wedge e^1 + E_2\,e^0\wedge e^2 + E_3\,e^0\wedge e^3 + B_3\,e^1\wedge e^2 + B_1\,e^2\wedge e^3 + B_2\,e^3\wedge e^1.$$
> The three electric components sit on the time-space monomials, the three magnetic components on the space-space monomials — the six numbers $(\mathbf E, \mathbf B)$ are the six components of the single $2$-form $F$.

**Step 4: matching the standard matrix.**

> [!note]- Derivation
> Reading the components $F_{\alpha\beta}$ (with $F_{\beta\alpha} = -F_{\alpha\beta}$ filling the lower triangle) into a matrix:
> $$F_{\mu\nu} = \begin{pmatrix} 0 & E_1 & E_2 & E_3 \\ -E_1 & 0 & B_3 & -B_2 \\ -E_2 & -B_3 & 0 & B_1 \\ -E_3 & B_2 & -B_1 & 0 \end{pmatrix}.$$
> The first row and column (entries $F_{0i}$) carry the electric field $\mathbf E$; the spatial $3\times3$ block (entries $F_{ij}$) carries the magnetic field $\mathbf B$ through $F_{ij} = \epsilon_{ijk}B^k$. This is the standard lowered-index field-strength matrix (matching the one in [[Ex - Raising and lowering indices on a four-tensor]]). The expansion confirms that the six independent components of any $2$-form split, relative to a frame, into a "time-space" triple and a "space-space" triple — and for $F$ these are $\mathbf E$ and $\mathbf B$.

> [!note]- Complete formal solution
> **(1)** Splitting $\tfrac12\sum_{\alpha,\beta}A_{\alpha\beta}e^\alpha\wedge e^\beta$: diagonal vanishes; the $\alpha>\beta$ piece equals the $\alpha<\beta$ piece by double antisymmetry; so $\tfrac12 A_{\alpha\beta}e^\alpha\wedge e^\beta = \sum_{\alpha<\beta}A_{\alpha\beta}e^\alpha\wedge e^\beta$.
> **(2)** Six basis $2$-forms: $e^0\wedge e^i$ (electric-type, $i=1,2,3$) and $e^i\wedge e^j$ (magnetic-type, $i<j$); components $A_{0i}$ and $A_{ij}$.
> **(3)** $F = E_i\,e^0\wedge e^i + \tfrac12\epsilon_{ijk}B^k\,e^i\wedge e^j$, with $F_{0i} = E_i$, $F_{ij} = \epsilon_{ijk}B^k$.
> **(4)** The components fill the standard antisymmetric matrix with $\mathbf E$ in the time-space entries and $\mathbf B$ in the space-space block. $\blacksquare$

---

# Key Takeaways

**The factor of two in $\tfrac12 A_{\alpha\beta}e^\alpha\wedge e^\beta$ is the symmetry factor for double-counting unordered pairs.** The two forms of the $2$-form expansion — the $\tfrac12$-with-all-indices form and the strictly-ordered-sum form — are equal because summing over all index pairs double-counts each unordered pair (and adds zero on the diagonal), and the $\tfrac12$ exactly compensates. This factor recurs in *every* $p$-form expansion as $\tfrac1{p!}$ (compensating the $p!$ orderings of each index set), and getting it right is essential: a Hodge star, a field invariant, or an action integral computed with the wrong factor is off by $p!$. The reusable rule: when an index is summed over *all* values, divide by the symmetry factor ($p!$ for a $p$-form, $2$ for a $2$-form); when summed over *ordered* values only ($\alpha_1 < \cdots < \alpha_p$), do not. Decide once which convention you are using and stick to it — mixing the two within a computation is the single most common source of factor-of-$2$ (or factor-of-$p!$) errors in form calculations.

**The six components of a $2$-form split, relative to a frame, into a "time-space" triple and a "space-space" triple.** Expanding any $2$-form in the wedge basis exhibits its six components as three of "electric type" ($A_{0i}$, one time index) and three of "magnetic type" ($A_{ij}$, two space indices). For the field strength these are literally $\mathbf E$ and $\mathbf B$, but the split is generic: it applies to the angular-momentum $2$-form (giving "boost" and "rotation" parts), the four-rotation of an observer's frame (giving acceleration and spatial rotation), and any antisymmetric tensor. The reusable insight is that choosing a time direction (an observer) is what *defines* this split, and the two triples transform differently under boosts because they carry different numbers of time indices. This is the component-level shadow of the [[Thm - Orthogonal Decomposition of 2-Forms|observer decomposition]] of a $2$-form, and recognising it lets you read off the electric and magnetic parts of any antisymmetric tensor by inspection of its index structure.

**The field strength is one $2$-form, and "electric versus magnetic" is which basis monomials a component sits on.** The deepest lesson of the expansion is that $\mathbf E$ and $\mathbf B$ are not two objects but the two halves of the component list of a single $2$-form $F$ — the electric field is the coefficient of the time-space monomials $e^0\wedge e^i$, the magnetic field the coefficient of the space-space monomials $e^i\wedge e^j$. A change of observer (a boost) rotates the basis monomials, mixing the electric and magnetic coefficients — which is exactly why a moving observer sees a different $(\mathbf E, \mathbf B)$ split of the same $F$. This is the algebraic root of "electromagnetism is one field," and the wedge-basis expansion makes it concrete: there is one antisymmetric tensor, its six components are partitioned by the time/space character of their indices, and the partition is observer-dependent. Carrying this picture into the [[Special Relativity XXI — The Electromagnetic Field|electromagnetism chapters]] makes the field transformations and the invariants transparent rather than mysterious.
