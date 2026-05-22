---
type: exercise-index
subject: linear-algebra
section: "5C-5E"
tags: [algebra, linear-algebra]
---

## §5C–E Upper Triangular, Diagonalizable, Commuting Operators — Exercises

The §5C–E exercises drill the **canonical form theory** of operators on complex vector spaces — what shapes operators can take in suitable bases. The hierarchy is:
$$\text{scalar multiple of } I \subset \text{diagonalisable} \subset \text{upper-triangularisable},$$
with the last condition automatic over $\mathbb{C}$. The exercises focus on the testing and constructing of operators in these classes, the use of Gershgorin disks for eigenvalue localisation, and the central role of commutativity in simultaneous diagonalisation. The unifying frame is that the minimal polynomial's factorisation pattern detects all of these properties: linear factors → upper-triangularisable; distinct linear factors → diagonalisable; commutativity → eigenvalues respected by the partner operator.

- [[Ex - Operators with the same minimal polynomial need not be similar]] (⭐⭐⭐) — demonstrates that $m_T$ is *not* a complete similarity invariant; constructs two $4 \times 4$ nilpotent matrices with $m_T = z^2$ but different ranks ([[Def - Minimal Polynomial]], [[Def - Diagonalizable Operator]], [[Thm - Conditions for Diagonalizability]]).
- [[Ex - Commuting operators share an eigenvector on complex spaces]] (⭐⭐) — uses commutativity to make an $S$-eigenspace $T$-invariant, then applies the existence theorem to $T$ on the eigenspace; this is the **inductive step** of simultaneous upper-triangularisation ([[Thm - Existence of Eigenvalues on Complex Vector Spaces]], [[Def - Eigenvalue and Eigenvector]], [[Def - Invariant Subspace]]).
- **(Web exercise — diagonalisability detection)** (⭐⭐) — show that an operator $T$ on $\mathbb{C}^n$ with $T^k = T$ for some $k \geq 2$ is diagonalisable. Reason: $m_T \mid z^k - z = z(z^{k-1} - 1)$, which factors over $\mathbb{C}$ as $z$ times $(z - 1)(z - \zeta)(z - \zeta^2) \cdots (z - \zeta^{k-2})$ for $\zeta = e^{2\pi i/(k-1)}$ — distinct linear factors. So $m_T$ has distinct linear factors, and by [[Thm - Conditions for Diagonalizability]], $T$ is diagonalisable ([[Thm - Cayley-Hamilton (Minimal-Polynomial Form)]], [[Thm - Conditions for Diagonalizability]]).
- **(Web exercise — Gershgorin bound)** (⭐) — show that the matrix $A = \begin{pmatrix} 10 & 1 & 1 \\ 1 & 5 & 1 \\ 1 & 1 & 1 \end{pmatrix}$ has all eigenvalues real and within the union of disks $\{|z - 10| \leq 2\} \cup \{|z - 5| \leq 2\} \cup \{|z - 1| \leq 2\}$. Apply [[Thm - Gershgorin Disk Theorem]] directly; the disks are disjoint, so exactly one eigenvalue in each ([[Thm - Gershgorin Disk Theorem]]).
- **(Web exercise — Cayley-Hamilton verification)** (⭐⭐) — for the matrix $A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$, compute the characteristic polynomial $\chi_A(z) = (z - 2)(z - 3)$, verify Cayley-Hamilton: $\chi_A(A) = (A - 2I)(A - 3I)$ — compute and confirm it equals zero. Also compute the minimal polynomial (which equals $\chi_A$ here since both eigenvalues are distinct with one-dimensional eigenspaces; $T$ is diagonalisable, so $m_A$ has distinct linear factors). Connection: [[Thm - Cayley-Hamilton (Minimal-Polynomial Form)]] says $m_A \mid \chi_A$, and equality holds when each eigenvalue has only one Jordan block ([[Thm - Cayley-Hamilton (Minimal-Polynomial Form)]], [[Thm - Conditions for Diagonalizability]]).
