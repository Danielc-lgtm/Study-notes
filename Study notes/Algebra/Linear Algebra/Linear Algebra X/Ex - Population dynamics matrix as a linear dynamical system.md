---
type: exercise
subject: linear-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Linear Dynamical System"
tags: [algebra, linear-algebra, applied, dynamics]
---

# Problem Statement

A simplified population model has age groups $0, 1, 2, 3$ (so the state vector $x_t \in \mathbb R^4$ records the number of individuals in each age group at year $t$). The birth rate is $b = (0, 0, 0.4, 0.1)$ (only ages $2$ and $3$ reproduce, with the given rates per individual per year), and the death rate is $d = (0.05, 0.1, 0.2, 1.0)$ (so the survival rate from age $i$ to age $i+1$ is $1 - d_i$; everyone in age group $3$ dies after one year).

(a) Write down the $4 \times 4$ dynamics matrix $A$ for the system $x_{t+1} = A x_t$.

(b) Given the initial state $x_1 = (100, 100, 100, 100)$ — equal numbers in each age group — compute $x_2$ explicitly.

(c) Verify that the matrix $A$ is consistent: total births at year $t$ produce age-$0$ individuals at year $t + 1$, and survivors from age $i$ become age $i + 1$ at year $t + 1$.

**Recall:**

A linear dynamical system $x_{t+1} = A x_t$ updates the state vector by left-multiplication by a fixed matrix $A$ (the time-invariant case). See [[Def - Linear Dynamical System]].

For the Boyd population model with birth rates $b$ and death rates $d$:
- $(x_{t+1})_1 = \sum_i b_i (x_t)_i = b^T x_t$ (the number of newborns).
- $(x_{t+1})_{i+1} = (1 - d_i)(x_t)_i$ for $i = 1, 2, 3$ (the survivors).

Combined, the dynamics matrix is
$$A = \begin{pmatrix} b_1 & b_2 & b_3 & b_4 \\ 1-d_1 & 0 & 0 & 0 \\ 0 & 1-d_2 & 0 & 0 \\ 0 & 0 & 1-d_3 & 0 \end{pmatrix}.$$

---

# Convergent Strategy

**Problem class.** This is a *direct construction* of the dynamics matrix for a structured linear dynamical system. The exercise drills the translation from a verbal description of a recurrence ("newborns this year are this many; survivors from age $i$ become age $i+1$") to a matrix.

**Assumption pattern.** Birth and death rates given as numerical vectors. The recurrence has two parts (newborns and survivors), and each contributes a row of the matrix.

**Theorem routing.** Mechanical construction from the [[Def - Linear Dynamical System|definition]]. Then verify by computing one step of the evolution numerically.

**Key decision point.** The structural insight is that the dynamics matrix has a **specific sparse structure**: the first row is the birth-rate vector $b^T$, the subdiagonal entries are the survival rates $1 - d_i$, and all other entries are zero. This sparsity is what makes the matrix interpretable: the first row "produces newborns from all reproductive age groups", and the subdiagonal "shifts each age group up by one, with mortality losses". Recognising this structural pattern allows the model to be written without thought once the rates are specified.

---

# Legal Operations Used

1. **Operation 1 (encode the phenomenon as a vector or matrix).** The age distribution is a $4$-vector; the recurrence is a $4 \times 4$ matrix.

2. **Operation 8 (iterate the dynamics matrix).** Compute $x_2 = Ax_1$ to verify the model.

---

# Hints

> [!note]- Hint 1
> Write the first row of $A$ as $b^T$, the transpose of the birth-rate vector. Each $(A)_{1,i}$ is the contribution of age group $i$ to next year's newborns.

> [!note]- Hint 2
> The subdiagonal of $A$ is the survival rates: $(A)_{i+1, i} = 1 - d_i$. All other entries (off the first row and the subdiagonal) are zero.

> [!note]- Hint 3
> To verify, compute $A x_1$ row by row: $(A x_1)_1 = b^T x_1$ (newborns), $(A x_1)_{i+1} = (1 - d_i)(x_1)_i$ (survivors from age $i$).

---

# Solution

The proof has three steps. Step 1 writes down the dynamics matrix $A$ from the rates. Step 2 computes $x_2 = A x_1$ by matrix-vector multiplication. Step 3 verifies that the entries of $x_2$ have the expected demographic interpretation.

**Step 1: Construct the dynamics matrix $A$.**

> [!note]- Derivation
> Each row of $A$ encodes one component of the next state $x_{t+1}$:
>
> **Row 1 (newborns).** $(x_{t+1})_1 = $ total newborns $= b^T x_t = b_1 (x_t)_1 + b_2 (x_t)_2 + b_3 (x_t)_3 + b_4 (x_t)_4 = 0 \cdot (x_t)_1 + 0 \cdot (x_t)_2 + 0.4 \cdot (x_t)_3 + 0.1 \cdot (x_t)_4$.
> So row 1 of $A$ is $(0, 0, 0.4, 0.1)$.
>
> **Row 2 (age 1 survivors).** $(x_{t+1})_2 = (1 - d_1)(x_t)_1 = 0.95 (x_t)_1$.
> So row 2 of $A$ is $(0.95, 0, 0, 0)$.
>
> **Row 3 (age 2 survivors).** $(x_{t+1})_3 = (1 - d_2)(x_t)_2 = 0.9 (x_t)_2$.
> So row 3 of $A$ is $(0, 0.9, 0, 0)$.
>
> **Row 4 (age 3 survivors).** $(x_{t+1})_4 = (1 - d_3)(x_t)_3 = 0.8 (x_t)_3$.
> So row 4 of $A$ is $(0, 0, 0.8, 0)$.
>
> Combining:
> $$A = \begin{pmatrix} 0 & 0 & 0.4 & 0.1 \\ 0.95 & 0 & 0 & 0 \\ 0 & 0.9 & 0 & 0 \\ 0 & 0 & 0.8 & 0 \end{pmatrix}.$$

**Step 2: Compute $x_2 = A x_1$.**

> [!note]- Derivation
> $x_1 = (100, 100, 100, 100)^T$. Compute $A x_1$ row by row:
>
> $(A x_1)_1 = 0 \cdot 100 + 0 \cdot 100 + 0.4 \cdot 100 + 0.1 \cdot 100 = 40 + 10 = 50$.
>
> $(A x_1)_2 = 0.95 \cdot 100 + 0 + 0 + 0 = 95$.
>
> $(A x_1)_3 = 0 + 0.9 \cdot 100 + 0 + 0 = 90$.
>
> $(A x_1)_4 = 0 + 0 + 0.8 \cdot 100 + 0 = 80$.
>
> So $x_2 = (50, 95, 90, 80)^T$.

**Step 3: Verify the demographic interpretation.**

> [!note]- Derivation
> *Newborns.* The newborns are $50$, which is the sum of births from age $2$ ($0.4 \cdot 100 = 40$) and age $3$ ($0.1 \cdot 100 = 10$). ✓
>
> *Age 1 survivors.* The age 1 group in year 2 comes from the age 0 group in year 1 with a $5\%$ mortality, giving $0.95 \cdot 100 = 95$. ✓
>
> *Age 2 survivors.* From age 1 with $10\%$ mortality: $0.9 \cdot 100 = 90$. ✓
>
> *Age 3 survivors.* From age 2 with $20\%$ mortality: $0.8 \cdot 100 = 80$. ✓
>
> The total population in year 2 is $50 + 95 + 90 + 80 = 315$, compared to $400$ in year 1. The population is shrinking because the birth rate ($50$ newborns) is less than the deaths from the model ($100 \cdot 1.0 = 100$ deaths from age $3$, plus mortality losses $5 + 10 + 20 = 35$ from younger ages, total $135$ deaths; net change is $50 - 135 = -85$, consistent with the population going from $400$ to $315$).

> [!note]- Complete formal solution
> Given birth rates $b = (0, 0, 0.4, 0.1)$ and death rates $d = (0.05, 0.1, 0.2, 1.0)$, the population dynamics matrix is
> $$A = \begin{pmatrix} 0 & 0 & 0.4 & 0.1 \\ 0.95 & 0 & 0 & 0 \\ 0 & 0.9 & 0 & 0 \\ 0 & 0 & 0.8 & 0 \end{pmatrix},$$
> with the first row being $b^T$ and the subdiagonal entries being $1 - d_i$ for $i = 1, 2, 3$.
>
> For the initial state $x_1 = (100, 100, 100, 100)^T$,
> $$x_2 = A x_1 = (50, 95, 90, 80)^T.$$
>
> The demographic interpretation:
> - **Newborns** $(x_2)_1 = 50$: total births from reproductive age groups.
> - **Age 1** $(x_2)_2 = 95$: survivors from age 0 with $5\%$ mortality.
> - **Age 2** $(x_2)_3 = 90$: survivors from age 1 with $10\%$ mortality.
> - **Age 3** $(x_2)_4 = 80$: survivors from age 2 with $20\%$ mortality.
>
> Total population shrinks from $400$ to $315$ because deaths exceed births. $\quad\blacksquare$

---

# Key Takeaways

**Population dynamics is the prototypical structured linear dynamical system.** The dynamics matrix $A$ has two sources: the *first row* encoding the birth rates (newborns are a linear combination of reproductive age groups), and the *subdiagonal* encoding the survival rates (each age group transitions to the next with a mortality loss). This sparse structure — known as a **Leslie matrix** in demography — is what makes population projection a textbook example: the matrix is easy to write down from biological inputs, easy to iterate, and amenable to spectral analysis. The dominant eigenvalue of $A$ is the long-term growth rate of the population (positive: population grows; equal to $1$: stable; less than $1$: declines), and the corresponding eigenvector is the long-term stable age distribution.

**The matrix-vector form is more than notational compression — it enables efficient computation and structural reasoning.** Once the model is in matrix form, you can compute any future year's age distribution by repeated multiplication: $x_t = A^{t-1} x_1$. For very long horizons ($t$ large), you can diagonalise $A$ (if possible) and reduce $A^{t-1}$ to scalar powers, giving an exact closed-form solution. For short horizons, you simply iterate. For intermediate scales (like a million-year demographic simulation), specialised algorithms exploit the sparsity of $A$. None of this is possible if the dynamics are expressed verbally; the matrix form is what makes the model *computable*.

**The trigger-reaction pattern is: "see a recurrence with linear transitions $\to$ write it as $x_{t+1} = A x_t$".** This recurs across applied modelling: economic input-output systems (Leontief matrices), epidemic models with compartment transitions, supply-chain dynamics, electrical circuit simulation, mechanical systems after Euler discretisation. In each case, the recurrence has the form "next state = linear function of current state, possibly with input", and the goal of the modelling step is to identify the dynamics matrix $A$, the input matrix $B$, and any time-dependence or offsets. Once these are in hand, the linear-algebra toolkit — eigenvalues for stability, matrix powers for short-horizon prediction, controllability and observability for control-theoretic analysis — takes over. This is the master pattern of [[Linear Algebra X — Applied I — Vectors, Distance, Equations, Dynamics|Boyd Ch 9]] and the foundation for all of dynamical-systems analysis.
