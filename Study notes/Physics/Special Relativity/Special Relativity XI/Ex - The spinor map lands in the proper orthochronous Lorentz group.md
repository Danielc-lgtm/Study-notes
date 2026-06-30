---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Spinor Map and SL(2,C)"
  - "Def - Pauli Matrices and the Hermitian-Matrix Correspondence"
tags: [physics, special-relativity]
---

# Problem Statement

Let $A = \begin{pmatrix}\alpha & \beta \\ \gamma & \delta\end{pmatrix} \in SL(2,\mathbb{C})$ ($\alpha\delta - \beta\gamma = 1$) act on spacetime by the [[Def - The Spinor Map and SL(2,C)|spinor map]], $\underline X \mapsto A\underline X A^\dagger$.

1. Show that $\Phi_A(\underline X) = A\underline X A^\dagger$ maps Hermitian matrices to Hermitian matrices and preserves the determinant, so $\Lambda_A$ is a Lorentz transformation.
2. Show $\mathscr{S}$ is a homomorphism: $\Lambda_A\Lambda_B = \Lambda_{AB}$.
3. Compute the time–time component $(\Lambda_A)^0{}_0 = \tfrac12\mathrm{tr}(\sigma_0 A\sigma_0 A^\dagger)$ and show it equals $\tfrac12(|\alpha|^2 + |\beta|^2 + |\gamma|^2 + |\delta|^2) > 0$, so $\Lambda_A$ is **orthochronous**.
4. Show $\det\Lambda_A = 1$, so $\Lambda_A$ is **proper**. Conclude $\mathscr{S}(A) \in SO^+(1,3)$.

**Recall:**

![[Def - The Spinor Map and SL(2,C)#The Definition]]

A Lorentz transformation $\Lambda$ is **orthochronous** if $\Lambda^0{}_0 > 0$ (it preserves the time-orientation, mapping future to future) and **proper** if $\det\Lambda = +1$ (it preserves orientation). The **restricted** Lorentz group $SO^+(1,3)$ is the proper orthochronous part — the identity component. The component is read off from $A\sigma_\nu A^\dagger = (\Lambda_A)^\mu{}_\nu\sigma_\mu$, so $(\Lambda_A)^\mu{}_\nu = \tfrac12\mathrm{tr}(\sigma_\mu A\sigma_\nu A^\dagger)$.

---

# Convergent Strategy

**Problem class.** A *structural-verification* problem: prove that the spinor map's image lands where it should, in the restricted Lorentz group, rather than in some larger group that includes time-reversal or parity. The [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map#Sources and Targets|topic's target list]] names "establish a homomorphism or covering property" as a recurring goal, and this exercise does the foundational case.

**Assumption pattern.** The single assumption $\det A = 1$ does all the work: it forces the determinant of $\Phi_A(\underline X)$ to equal that of $\underline X$ (preserving the interval), and it constrains the trace combination so that $(\Lambda_A)^0{}_0$ is a sum of squared moduli, manifestly positive. The signpost is that everything reduces to the algebra of $\dagger$ and $\det$.

**Theorem routing.** No external theorem is invoked; this exercise *proves* the claims asserted on [[Def - The Spinor Map and SL(2,C)|the spinor-map definition page]] and used as Step 0 in [[Thm - SL(2,C) is the Double Cover of the Restricted Lorentz Group]]. The two algebraic facts it routes through are $(AB)^\dagger = B^\dagger A^\dagger$ (for Hermiticity and the homomorphism) and $\det(AB) = \det A\det B$ (for interval-preservation and properness).

**Key decision point.** The crux is part 3: rather than computing all sixteen components of $\Lambda_A$, observe that orthochronicity needs only the *single* component $(\Lambda_A)^0{}_0$, and that this component is $\tfrac12\mathrm{tr}(A A^\dagger)$ (since $\sigma_0 = I$), which is a sum of squared moduli of the entries of $A$ — automatically positive. Recognising that one number settles orthochronicity avoids a sixteen-entry computation; recognising that $\mathrm{tr}(AA^\dagger) = \sum|A_{ij}|^2$ (the Frobenius norm) makes positivity instant.

---

# Legal Operations Used

1. **Act by congruence $\underline X \mapsto A\underline X A^\dagger$** (operation 2 from the topic page): the entire exercise studies this action, computing its effect on Hermiticity, determinant, and the time component.

2. **Use $(AB)^\dagger = B^\dagger A^\dagger$ and $\det(AB) = \det A\det B$** (operation 9 from the topic page): part 1 uses the first to show Hermiticity is preserved and the second to show the determinant is preserved; part 2 uses the first for the homomorphism property.

3. **Recast a four-vector as a Hermitian matrix** (operation 1 from the topic page): the component extraction $(\Lambda_A)^\mu{}_\nu = \tfrac12\mathrm{tr}(\sigma_\mu A\sigma_\nu A^\dagger)$ uses the Pauli-basis decomposition.

---

# Hints

> [!note]- Hint 1
> For Hermiticity, take the adjoint of $A\underline X A^\dagger$ and use $(MN)^\dagger = N^\dagger M^\dagger$ together with $\underline X^\dagger = \underline X$. For the determinant, use $\det(MNP) = \det M\det N\det P$ and $\det A^\dagger = \overline{\det A}$.

> [!note]- Hint 2
> For the homomorphism, compute $\Phi_A(\Phi_B(\underline X)) = A(B\underline X B^\dagger)A^\dagger$ and regroup using $(AB)^\dagger = B^\dagger A^\dagger$ to get $(AB)\underline X(AB)^\dagger = \Phi_{AB}(\underline X)$.

> [!note]- Hint 3
> Since $\sigma_0 = I$, $(\Lambda_A)^0{}_0 = \tfrac12\mathrm{tr}(I\cdot A\cdot I\cdot A^\dagger) = \tfrac12\mathrm{tr}(AA^\dagger)$. The diagonal entries of $AA^\dagger$ are $|\alpha|^2 + |\beta|^2$ and $|\gamma|^2 + |\delta|^2$, so the trace is $|\alpha|^2 + |\beta|^2 + |\gamma|^2 + |\delta|^2$.

> [!note]- Hint 4
> For properness, $\det\Lambda_A = +1$ because the map $A \mapsto \Lambda_A$ is continuous, $\Lambda_I = \mathrm{Id}$ has determinant $+1$, and $SL(2,\mathbb{C})$ is connected, so $\det\Lambda_A$ cannot jump to $-1$. (Alternatively, compute via the Kronecker-product expression $\Lambda_A = T^{-1}(A\otimes\overline A)T$, giving $\det\Lambda_A = (\det A)^2(\overline{\det A})^2 = 1$.)

---

# Solution

The exercise verifies four facts, each a short consequence of the algebra of adjoints and determinants. Parts 1 and 2 use $(AB)^\dagger = B^\dagger A^\dagger$ and multiplicativity of the determinant; part 3 reduces orthochronicity to the positivity of a Frobenius norm; part 4 fixes properness by connectedness. Together they place the image in $SO^+(1,3)$.

**Step 1: $\Phi_A$ preserves Hermiticity and the determinant.**

> [!note]- Derivation
> *Hermiticity.* For Hermitian $\underline X$ ($\underline X^\dagger = \underline X$),
> $$(A\underline X A^\dagger)^\dagger = (A^\dagger)^\dagger\,\underline X^\dagger\,A^\dagger = A\,\underline X\,A^\dagger,$$
> using $(MNP)^\dagger = P^\dagger N^\dagger M^\dagger$ and $(A^\dagger)^\dagger = A$. So $\Phi_A(\underline X)$ is Hermitian and corresponds to a real four-vector.
>
> *Determinant.* Using multiplicativity and $\det A^\dagger = \overline{\det A}$,
> $$\det(A\underline X A^\dagger) = \det A\,\det\underline X\,\det A^\dagger = \det A\,\overline{\det A}\,\det\underline X = |\det A|^2\det\underline X = \det\underline X,$$
> since $|\det A| = 1$ ($\det A = 1$). As $\det\underline X = X\cdot X$, the interval is preserved, so $\Lambda_A$ is a Lorentz transformation.

**Step 2: $\mathscr{S}$ is a homomorphism, $\Lambda_A\Lambda_B = \Lambda_{AB}$.**

> [!note]- Derivation
> Compose the congruences:
> $$\Phi_A(\Phi_B(\underline X)) = A(B\underline X B^\dagger)A^\dagger = (AB)\,\underline X\,(B^\dagger A^\dagger) = (AB)\,\underline X\,(AB)^\dagger = \Phi_{AB}(\underline X),$$
> using $B^\dagger A^\dagger = (AB)^\dagger$. Transporting through $\mathscr{H}$, $\Lambda_A\Lambda_B = \mathscr{H}^{-1}\Phi_A\mathscr{H}\,\mathscr{H}^{-1}\Phi_B\mathscr{H} = \mathscr{H}^{-1}(\Phi_A\Phi_B)\mathscr{H} = \mathscr{H}^{-1}\Phi_{AB}\mathscr{H} = \Lambda_{AB}$. Hence $\mathscr{S}(AB) = \mathscr{S}(A)\mathscr{S}(B)$.

**Step 3: $(\Lambda_A)^0{}_0 = \tfrac12(|\alpha|^2 + |\beta|^2 + |\gamma|^2 + |\delta|^2) > 0$ (orthochronous).**

> [!note]- Derivation
> Since $\sigma_0 = I$, the formula $(\Lambda_A)^\mu{}_\nu = \tfrac12\mathrm{tr}(\sigma_\mu A\sigma_\nu A^\dagger)$ gives
> $$(\Lambda_A)^0{}_0 = \tfrac12\mathrm{tr}(\sigma_0 A\sigma_0 A^\dagger) = \tfrac12\mathrm{tr}(AA^\dagger).$$
> Compute $AA^\dagger$ with $A = \begin{pmatrix}\alpha&\beta\\\gamma&\delta\end{pmatrix}$, $A^\dagger = \begin{pmatrix}\bar\alpha&\bar\gamma\\\bar\beta&\bar\delta\end{pmatrix}$:
> $$AA^\dagger = \begin{pmatrix}|\alpha|^2 + |\beta|^2 & \alpha\bar\gamma + \beta\bar\delta \\ \gamma\bar\alpha + \delta\bar\beta & |\gamma|^2 + |\delta|^2\end{pmatrix},$$
> whose trace is $|\alpha|^2 + |\beta|^2 + |\gamma|^2 + |\delta|^2 = \|A\|_F^2$, the squared Frobenius norm. Therefore
> $$(\Lambda_A)^0{}_0 = \tfrac12\big(|\alpha|^2 + |\beta|^2 + |\gamma|^2 + |\delta|^2\big) > 0,$$
> strictly positive because $A \neq 0$ (indeed $\det A = 1$). So $\Lambda_A$ preserves the time-orientation: it is orthochronous.

**Step 4: $\det\Lambda_A = 1$ (proper), hence $\mathscr{S}(A) \in SO^+(1,3)$.**

> [!note]- Derivation
> *By connectedness.* The map $A \mapsto \det\Lambda_A$ is continuous on the connected group $SL(2,\mathbb{C})$ (the entries of $\Lambda_A$ are polynomials in those of $A$ and $\overline A$). It takes values in $\{\pm 1\}$ (since $\Lambda_A$ is a Lorentz transformation, $\det\Lambda_A = \pm 1$), and a continuous $\{\pm 1\}$-valued function on a connected space is constant. At $A = I$, $\Lambda_I = \mathrm{Id}$ with $\det = +1$, so $\det\Lambda_A = +1$ everywhere.
>
> *By the Kronecker product (alternative).* Writing $h = (\underline X_{11}, \underline X_{12}, \underline X_{21}, \underline X_{22})$ as a column, the relation $\Phi_A(\underline X) = A\underline X A^\dagger$ becomes, with $A^\dagger = \overline A^{\mathsf T}$, the linear map $h \mapsto (A\otimes\overline A)h$ on $\mathbb{C}^4$, and $\Lambda_A = T^{-1}(A\otimes\overline A)T$ for the fixed change-of-basis $T$ relating $h$ to $(x^0,x^1,x^2,x^3)$. Using $\det(M\otimes N) = (\det M)^2(\det N)^2$ for $2\times 2$ matrices, $\det\Lambda_A = \det(A\otimes\overline A) = (\det A)^2(\overline{\det A})^2 = 1$.
>
> Combining Steps 1–4: $\Lambda_A$ is a Lorentz transformation, orthochronous ($(\Lambda_A)^0{}_0 > 0$) and proper ($\det\Lambda_A = +1$), hence $\mathscr{S}(A) \in SO^+(1,3)$.

> [!note]- Complete formal solution
> $\Phi_A(\underline X) = A\underline X A^\dagger$ is Hermitian (take adjoints: $(A\underline X A^\dagger)^\dagger = A\underline X A^\dagger$) and has $\det(A\underline X A^\dagger) = |\det A|^2\det\underline X = \det\underline X$, so $\Lambda_A$ preserves the interval and is a Lorentz transformation. It is a homomorphism since $A(B\underline X B^\dagger)A^\dagger = (AB)\underline X(AB)^\dagger$. Its time–time component is $(\Lambda_A)^0{}_0 = \tfrac12\mathrm{tr}(AA^\dagger) = \tfrac12(|\alpha|^2+|\beta|^2+|\gamma|^2+|\delta|^2) > 0$, so it is orthochronous; and $\det\Lambda_A = +1$ by continuity from $\Lambda_I = \mathrm{Id}$ on the connected group $SL(2,\mathbb{C})$ (or via $\det(A\otimes\overline A) = (\det A)^2(\overline{\det A})^2 = 1$), so it is proper. Hence $\mathscr{S}(A) \in SO^+(1,3)$. $\blacksquare$

---

# Key Takeaways

**Orthochronicity is a positivity, and positivity comes from a sum of squares.** The single most efficient observation in this exercise is that $(\Lambda_A)^0{}_0 = \tfrac12\mathrm{tr}(AA^\dagger)$ is half the squared Frobenius norm of $A$, hence automatically positive. This is why the spinor map can *never* produce a time-reversing transformation: the time–time component is structurally a sum of $|A_{ij}|^2$, which cannot be negative. The reusable pattern is that "preserves time-orientation" translates, on the cover, into "a manifestly positive quadratic in the matrix entries," and whenever you need to show a constructed Lorentz transformation is orthochronous, computing the single component $\Lambda^0{}_0$ and recognising it as a sum of squares is the quickest route. The same logic shows the image misses parity and time-reversal entirely — they would need $\Lambda^0{}_0 < 0$ or $\det\Lambda = -1$, neither reachable.

**Properness by connectedness is a recurring "no jump" argument.** Rather than computing the sixteen-entry determinant of $\Lambda_A$, the cleanest proof that $\det\Lambda_A = +1$ is topological: the determinant is a continuous function into the discrete set $\{\pm 1\}$, so on a connected domain it is constant, and its value at the identity is $+1$. This "continuous function into a discrete set is locally constant, hence constant on a connected space" argument is one of the most reusable in the subject — it proves that the image of any connected group under a continuous homomorphism lands in a single component, and it is how one shows the spinor map cannot reach the disconnected pieces of $O(1,3)$. Whenever a quantity is discrete-valued and you can connect your object to a known base point, invoke connectedness rather than computing.

**The homomorphism property is exactly $(AB)^\dagger = B^\dagger A^\dagger$ in disguise.** That $\mathscr{S}(AB) = \mathscr{S}(A)\mathscr{S}(B)$ is not a deep fact; it is the order-reversal of the adjoint applied to the congruence, $A(B\underline X B^\dagger)A^\dagger = (AB)\underline X(AB)^\dagger$. The lesson is that the two factors in the congruence (one plain $A$, one daggered) are arranged precisely so that composition works: the left factors multiply in order $A\cdot B$, and the right factors multiply in the reversed order $B^\dagger\cdot A^\dagger = (AB)^\dagger$, so the sandwich of a sandwich is again a sandwich. This is why the congruence — and not, say, $\underline X \mapsto A\underline X A^{\mathsf T}$ or $A\underline X A^{-1}$ — is the right action: it is the unique bilinear-in-$A$ form that is both Hermitian-preserving and a homomorphism, and recognising it as "the homomorphism-respecting Hermitian action" is the structural insight that the bare formula hides.
