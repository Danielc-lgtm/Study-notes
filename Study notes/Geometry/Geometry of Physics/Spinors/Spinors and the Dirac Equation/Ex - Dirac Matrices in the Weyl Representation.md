---
type: exercise
subject: spinors
difficulty: "⭐"
prereqs:
  - "Def - Dirac Gamma Matrices"
  - "Def - The Pauli Matrices"
tags: [geometry, spinors, quantum-mechanics, relativity]
---

# Problem Statement

Write down the Dirac gamma matrices $\gamma^0, \gamma^1, \gamma^2, \gamma^3$ in the **Weyl (chiral) representation** as $4 \times 4$ block matrices in terms of the Pauli matrices $\sigma_1, \sigma_2, \sigma_3$ and $I_2$. Verify the Clifford relation $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I_4$ explicitly for the following pairs:

1. $\{\gamma^0, \gamma^0\}$ (verify $= -2I_4$, since $\eta^{00} = -1$).
2. $\{\gamma^0, \gamma^1\}$ (verify $= 0$, since $\eta^{01} = 0$).
3. $\{\gamma^1, \gamma^1\}$ (verify $= +2I_4$, since $\eta^{11} = +1$).
4. $\{\gamma^1, \gamma^2\}$ (verify $= 0$).

Then compute the chirality matrix $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3$ in block form, verify $(\gamma^5)^2 = I_4$, and verify $\{\gamma^5, \gamma^\mu\} = 0$ for one of the $\gamma^\mu$.

**Recall:**

The Dirac matrices satisfy:

![[Def - Dirac Gamma Matrices#The Definition]]

The Pauli matrices:

![[Def - The Pauli Matrices#The Definition]]

The Frankel signature convention is $\eta = \mathrm{diag}(-1, +1, +1, +1)$, so $\eta^{00} = -1$ and $\eta^{kk} = +1$ for $k = 1, 2, 3$.

---

# Convergent Strategy

**Problem class:** *Direct computation of matrix products in block form.* This is the basic verification that the Weyl-representation formula for the gamma matrices satisfies the Clifford relation — a routine algebra exercise but a foundational one.

**Assumption pattern:** Given the block-matrix structure $\gamma^0 = \begin{pmatrix} 0 & -I_2 \\ I_2 & 0\end{pmatrix}$, $\gamma^k = \begin{pmatrix} 0 & \sigma_k \\ \sigma_k & 0\end{pmatrix}$, we need to multiply $4 \times 4$ block matrices and read off the Clifford relations from the resulting $2 \times 2$ blocks. The Pauli matrices satisfy $\sigma_j\sigma_k = \delta_{jk}I_2 + i\epsilon_{jkl}\sigma_l$, so all $\sigma$-products reduce to combinations of $I_2$ and other $\sigma$'s.

**Theorem routing:** Just direct block matrix multiplication, using the Pauli identity for products of Pauli matrices. The structure: $\gamma^\mu\gamma^\nu$ has off-diagonal blocks that vanish (since each $\gamma$ is purely off-diagonal in the block decomposition), and diagonal blocks that involve $\pm\sigma_j\sigma_k$ or $\pm I$.

**Key decision point:** The trickiest part is the *signs* and order of multiplication: when multiplying off-diagonal block matrices $\begin{pmatrix} 0 & A \\ B & 0\end{pmatrix}\begin{pmatrix} 0 & C \\ D & 0\end{pmatrix} = \begin{pmatrix} AD & 0 \\ 0 & BC\end{pmatrix}$, the signs and orders of $A, B, C, D$ must be tracked carefully. In particular, $\gamma^0$ has *negative* upper-right block $-I_2$, while $\gamma^k$ has *positive* upper-right block $\sigma_k$ — the sign difference is what produces the negative diagonal $\{\gamma^0, \gamma^0\} = -2I_4$ matching $\eta^{00} = -1$.

---

# Legal Operations Used

1. **Operation 12 from the topic page (convert between gamma-matrix conventions):** The Weyl representation we use is one of several unitarily-equivalent representations. The specific block-diagonal form $\gamma^5 = \mathrm{diag}(-I_2, I_2)$ in the Weyl representation makes it the natural choice for chirality-related calculations.

2. **Operation 5 from the topic page (square the Dirac operator using the Clifford relation):** While not directly in this exercise, the Clifford relation we are verifying *is* the operator identity that makes $\not\partial^2 = \Box$ — see [[Thm - Dirac Equation Squares to Klein-Gordon]].

---

# Hints

> [!note]- Hint 1
> For block-matrix products of the form $\begin{pmatrix} 0 & A \\ B & 0\end{pmatrix}^2$, use $\begin{pmatrix} 0 & A \\ B & 0\end{pmatrix}\begin{pmatrix} 0 & A \\ B & 0\end{pmatrix} = \begin{pmatrix} AB & 0 \\ 0 & BA\end{pmatrix}$. The off-diagonal blocks vanish; the diagonal blocks are $AB$ (upper-left) and $BA$ (lower-right).

> [!note]- Hint 2
> For mixed products $\gamma^0 \gamma^k$: $\begin{pmatrix} 0 & -I_2 \\ I_2 & 0\end{pmatrix}\begin{pmatrix} 0 & \sigma_k \\ \sigma_k & 0\end{pmatrix} = \begin{pmatrix} -\sigma_k & 0 \\ 0 & \sigma_k\end{pmatrix}$. And $\gamma^k\gamma^0 = \begin{pmatrix} \sigma_k & 0 \\ 0 & -\sigma_k\end{pmatrix}$. Sum: $\gamma^0\gamma^k + \gamma^k\gamma^0 = 0$, confirming the off-diagonal anticommutation.

> [!note]- Hint 3
> For $\gamma^5$: compute $\gamma^0\gamma^1\gamma^2\gamma^3$ block by block. $\gamma^0\gamma^1 = \begin{pmatrix} -\sigma_1 & 0 \\ 0 & \sigma_1\end{pmatrix}$ (from Hint 2 with $k = 1$). $\gamma^2\gamma^3 = \begin{pmatrix} 0 & \sigma_2 \\ \sigma_2 & 0\end{pmatrix}\begin{pmatrix} 0 & \sigma_3 \\ \sigma_3 & 0\end{pmatrix} = \begin{pmatrix} \sigma_2\sigma_3 & 0 \\ 0 & \sigma_2\sigma_3\end{pmatrix} = \begin{pmatrix} i\sigma_1 & 0 \\ 0 & i\sigma_1\end{pmatrix}$ (using $\sigma_2\sigma_3 = i\sigma_1$). Multiply: $\gamma^0\gamma^1 \cdot \gamma^2\gamma^3 = \begin{pmatrix} -i\sigma_1^2 & 0 \\ 0 & i\sigma_1^2\end{pmatrix} = \begin{pmatrix} -iI_2 & 0 \\ 0 & iI_2\end{pmatrix}$. So $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3 = i \cdot \begin{pmatrix} -iI_2 & 0 \\ 0 & iI_2\end{pmatrix} = \begin{pmatrix} I_2 & 0 \\ 0 & -I_2\end{pmatrix}$ — wait, this is the *opposite* sign from the convention $\gamma^5 = \mathrm{diag}(-I_2, I_2)$ used in the rest of the topic. The sign discrepancy is conventional and arises from differing definitions of $\gamma^5$; some authors use $\gamma^5 = -i\gamma^0\gamma^1\gamma^2\gamma^3$ to get $\mathrm{diag}(-I_2, I_2)$, others $\gamma^5 = +i\gamma^0\gamma^1\gamma^2\gamma^3$ giving $\mathrm{diag}(I_2, -I_2)$. Both are valid; we use the latter convention in the calculation below.

---

# Solution

The plan: compute each $\gamma^\mu\gamma^\nu$ via block-matrix multiplication, then verify the Clifford relation $\{\gamma^\mu, \gamma^\nu\} = 2\eta^{\mu\nu}I_4$ for the requested pairs. Then compute $\gamma^5$ as a block-diagonal matrix and verify its key properties.

**Step 1: $\{\gamma^0, \gamma^0\} = -2I_4$ (matches $\eta^{00} = -1$).**

> [!note]- Derivation
> $\gamma^0\gamma^0 = \begin{pmatrix} 0 & -I_2 \\ I_2 & 0\end{pmatrix}\begin{pmatrix} 0 & -I_2 \\ I_2 & 0\end{pmatrix} = \begin{pmatrix} -I_2 & 0 \\ 0 & -I_2\end{pmatrix} = -I_4$.
>
> So $\{\gamma^0, \gamma^0\} = 2\gamma^0\gamma^0 = -2I_4 = 2\eta^{00}I_4$. ✓

**Step 2: $\{\gamma^0, \gamma^1\} = 0$ (matches $\eta^{01} = 0$).**

> [!note]- Derivation
> $\gamma^0\gamma^1 = \begin{pmatrix} 0 & -I_2 \\ I_2 & 0\end{pmatrix}\begin{pmatrix} 0 & \sigma_1 \\ \sigma_1 & 0\end{pmatrix} = \begin{pmatrix} -\sigma_1 & 0 \\ 0 & \sigma_1\end{pmatrix}$.
>
> $\gamma^1\gamma^0 = \begin{pmatrix} 0 & \sigma_1 \\ \sigma_1 & 0\end{pmatrix}\begin{pmatrix} 0 & -I_2 \\ I_2 & 0\end{pmatrix} = \begin{pmatrix} \sigma_1 & 0 \\ 0 & -\sigma_1\end{pmatrix}$.
>
> Sum: $\gamma^0\gamma^1 + \gamma^1\gamma^0 = \begin{pmatrix} -\sigma_1 + \sigma_1 & 0 \\ 0 & \sigma_1 - \sigma_1\end{pmatrix} = 0$. ✓

**Step 3: $\{\gamma^1, \gamma^1\} = +2I_4$ (matches $\eta^{11} = +1$).**

> [!note]- Derivation
> $\gamma^1\gamma^1 = \begin{pmatrix} 0 & \sigma_1 \\ \sigma_1 & 0\end{pmatrix}\begin{pmatrix} 0 & \sigma_1 \\ \sigma_1 & 0\end{pmatrix} = \begin{pmatrix} \sigma_1^2 & 0 \\ 0 & \sigma_1^2\end{pmatrix} = \begin{pmatrix} I_2 & 0 \\ 0 & I_2\end{pmatrix} = I_4$.
>
> So $\{\gamma^1, \gamma^1\} = 2I_4 = 2\eta^{11}I_4$. ✓

**Step 4: $\{\gamma^1, \gamma^2\} = 0$ (matches $\eta^{12} = 0$).**

> [!note]- Derivation
> $\gamma^1\gamma^2 = \begin{pmatrix} 0 & \sigma_1 \\ \sigma_1 & 0\end{pmatrix}\begin{pmatrix} 0 & \sigma_2 \\ \sigma_2 & 0\end{pmatrix} = \begin{pmatrix} \sigma_1\sigma_2 & 0 \\ 0 & \sigma_1\sigma_2\end{pmatrix}$.
>
> $\gamma^2\gamma^1 = \begin{pmatrix} \sigma_2\sigma_1 & 0 \\ 0 & \sigma_2\sigma_1\end{pmatrix}$.
>
> Using $\sigma_1\sigma_2 = -\sigma_2\sigma_1$ (anticommutativity of distinct Pauli matrices):
> Sum: $\gamma^1\gamma^2 + \gamma^2\gamma^1 = \begin{pmatrix} \sigma_1\sigma_2 + \sigma_2\sigma_1 & 0 \\ 0 & \sigma_1\sigma_2 + \sigma_2\sigma_1\end{pmatrix} = 0$. ✓

**Step 5: Compute $\gamma^5$ and verify its properties.**

$\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3 = \mathrm{diag}(I_2, -I_2)$ (in the convention used in this exercise; see Hint 3 for the sign discussion). Squares to $I_4$ and anticommutes with each $\gamma^\mu$.

> [!note]- Derivation
> From Hint 3: $\gamma^0\gamma^1\gamma^2\gamma^3 = \begin{pmatrix} -iI_2 & 0 \\ 0 & iI_2\end{pmatrix}$, so $\gamma^5 = i \cdot \mathrm{diag}(-iI_2, iI_2) = \mathrm{diag}(I_2, -I_2) = \begin{pmatrix} I_2 & 0 \\ 0 & -I_2\end{pmatrix}$.
>
> *Square:* $(\gamma^5)^2 = \begin{pmatrix} I_2 & 0 \\ 0 & -I_2\end{pmatrix}^2 = \begin{pmatrix} I_2 & 0 \\ 0 & I_2\end{pmatrix} = I_4$. ✓
>
> *Anticommutation with $\gamma^0$:* $\gamma^5\gamma^0 = \begin{pmatrix} I_2 & 0 \\ 0 & -I_2\end{pmatrix}\begin{pmatrix} 0 & -I_2 \\ I_2 & 0\end{pmatrix} = \begin{pmatrix} 0 & -I_2 \\ -I_2 & 0\end{pmatrix}$.
>
> $\gamma^0\gamma^5 = \begin{pmatrix} 0 & -I_2 \\ I_2 & 0\end{pmatrix}\begin{pmatrix} I_2 & 0 \\ 0 & -I_2\end{pmatrix} = \begin{pmatrix} 0 & I_2 \\ I_2 & 0\end{pmatrix}$.
>
> Sum: $\gamma^5\gamma^0 + \gamma^0\gamma^5 = \begin{pmatrix} 0 & 0 \\ 0 & 0\end{pmatrix} = 0$. ✓

> [!note]- Complete formal solution
> The Weyl-representation gamma matrices are
> $$\gamma^0 = \begin{pmatrix} 0 & -I_2 \\ I_2 & 0\end{pmatrix}, \quad \gamma^k = \begin{pmatrix} 0 & \sigma_k \\ \sigma_k & 0\end{pmatrix} \quad (k = 1, 2, 3).$$
>
> *Clifford relation verifications.*
>
> 1. $\gamma^0\gamma^0 = \begin{pmatrix} -I_2 & 0 \\ 0 & -I_2\end{pmatrix} = -I_4$, so $\{\gamma^0, \gamma^0\} = -2I_4 = 2\eta^{00}I_4$ (with $\eta^{00} = -1$). ✓
>
> 2. $\gamma^0\gamma^1 = \mathrm{diag}(-\sigma_1, \sigma_1)$, $\gamma^1\gamma^0 = \mathrm{diag}(\sigma_1, -\sigma_1)$; sum is $0 = 2\eta^{01}I_4$. ✓
>
> 3. $\gamma^1\gamma^1 = \mathrm{diag}(\sigma_1^2, \sigma_1^2) = I_4$, so $\{\gamma^1, \gamma^1\} = 2I_4 = 2\eta^{11}I_4$. ✓
>
> 4. $\gamma^1\gamma^2 + \gamma^2\gamma^1 = \mathrm{diag}(\sigma_1\sigma_2 + \sigma_2\sigma_1, \sigma_1\sigma_2 + \sigma_2\sigma_1) = 0$ (using $\{\sigma_1, \sigma_2\} = 0$). ✓
>
> *Chirality matrix.* $\gamma^5 = i\gamma^0\gamma^1\gamma^2\gamma^3 = i \cdot \mathrm{diag}(-iI_2, iI_2) = \mathrm{diag}(I_2, -I_2)$. (Sign depends on convention; with $\gamma^5 = -i\gamma^0\gamma^1\gamma^2\gamma^3$ one gets $\mathrm{diag}(-I_2, I_2)$, the convention used in the rest of this topic.) $(\gamma^5)^2 = I_4$, $\{\gamma^5, \gamma^\mu\} = 0$ for each $\gamma^\mu$.

---

# Key Takeaways

**The Weyl (chiral) representation is the natural one for chirality and Lorentz-covariance calculations.** In this representation, $\gamma^5$ is block-diagonal, so the chiral projectors $P_L = \tfrac{1}{2}(I - \gamma^5)$ and $P_R = \tfrac{1}{2}(I + \gamma^5)$ pick out the upper and lower $\mathbb{C}^2$ blocks of $\psi$ — i.e., the left- and right-handed Weyl spinors $\psi_L$ and $\psi_R$. The Dirac equation in this basis takes the **off-diagonal coupled form** that displays mass as a chirality-mixing term: $\sigma^\mu\partial_\mu \psi_L = m\psi_R$, $\bar\sigma^\mu\partial_\mu\psi_R = m\psi_L$. For chirality-sensitive calculations (V-A structure of weak interactions, chiral anomaly, etc.), the Weyl basis is the natural workspace.

**The block-matrix structure $\gamma = \begin{pmatrix} 0 & \cdot \\ \cdot & 0\end{pmatrix}$ encodes the spinor-cospinor decomposition.** The Dirac spinor module $\mathbb{C}^4$ splits as $\mathbb{C}^2_L \oplus \mathbb{C}^2_R$ (left-handed Weyl + right-handed Weyl). The off-diagonal-block structure of each $\gamma^\mu$ means that Clifford multiplication *swaps* the two chiral components — sending $S^+$ to $S^-$ and vice versa. This is why $\not\partial$ maps positive chirality to negative chirality (and conversely), giving the chirality-grading structure of the Dirac operator on even-dimensional spin manifolds. The same pattern appears in higher dimensions: in $D = 2k$ the Weyl-rep gamma matrices have an off-diagonal $\binom{2k}{k} \times \binom{2k}{k}$ block structure.

**The Clifford relation can be verified directly in the Weyl rep by elementary $2 \times 2$ Pauli computations.** The block structure reduces $4 \times 4$ Clifford calculations to $2 \times 2$ Pauli ones, which use the master identity $\sigma_j\sigma_k = \delta_{jk}I + i\epsilon_{jkl}\sigma_l$. This is the reason the Weyl rep is computationally convenient: every $4 \times 4$ calculation factors through $2 \times 2$ Pauli arithmetic. In contrast, the Dirac (standard) and Majorana representations have other virtues but require more work for explicit Clifford verifications.
