---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Hodge Star"
  - "Def - The Levi-Civita Tensor"
  - "Def - Metric Duality and Index Manipulation"
tags: [physics, special-relativity]
---

# Problem Statement

Work in a right-handed orthonormal frame, mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, $c = 1$, with $\varepsilon_{0123} = +1$.

1. Compute the Hodge duals of the six basis $2$-forms. In particular show $\star(e^0\wedge e^1) = -\,e^2\wedge e^3$ and $\star(e^2\wedge e^3) = +\,e^0\wedge e^1$.
2. Tabulate the action of $\star$ on all six basis $2$-forms, distinguishing the electric-type ($e^0\wedge e^i$) and magnetic-type ($e^i\wedge e^j$) monomials.
3. For the field strength $F$ with electric and magnetic parts $(\mathbf E, \mathbf B)$, show that $\star F$ has parts $(-\mathbf B, \mathbf E)$ — a quarter-turn in the field plane.
4. Confirm directly that applying $\star$ twice to a basis $2$-form returns minus the original, $\star\star(e^0\wedge e^1) = -e^0\wedge e^1$.

**Recall:**

![[Def - The Hodge Star#The Definition]]

The [[Def - The Hodge Star|Hodge star]] on a $2$-form has components $(\star A)_{\alpha\beta} = \tfrac12\varepsilon_{\mu\nu\alpha\beta}\,A^{\mu\nu}$, where $A^{\mu\nu} = \eta^{\mu\rho}\eta^{\nu\sigma}A_{\rho\sigma}$ is the [[Def - Metric Duality and Index Manipulation|raised]] form and $\varepsilon$ is the [[Def - The Levi-Civita Tensor|Levi-Civita tensor]]. The basis $2$-form $e^\alpha\wedge e^\beta$ has components $(e^\alpha\wedge e^\beta)_{\mu\nu} = \delta^\alpha_\mu\delta^\beta_\nu - \delta^\beta_\mu\delta^\alpha_\nu$.

---

# Convergent Strategy

**Problem class.** A *compute-a-tensor-operation* problem exercising the [[Def - The Hodge Star|Hodge star]] on concrete $2$-forms. The [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality#Problem-Solving Strategy|topic strategy]]: work in an orthonormal frame, raise indices (watch the signs), contract into $\varepsilon$.

**Assumption pattern.** Orthonormal frame, so $\varepsilon$ components equal the symbol. The only subtlety is the sign acquired in raising the indices of the $2$-form with the indefinite metric: an electric-type component ($0i$) gets one $-1$, a magnetic-type ($ij$) gets two $-1$'s.

**Theorem routing.** Part 1: plug the basis $2$-form into $(\star A)_{\alpha\beta} = \tfrac12\varepsilon_{\mu\nu\alpha\beta}A^{\mu\nu}$, carefully raising. Part 2: repeat for all six. Part 3: assemble $F$ and apply the table. Part 4: apply $\star$ twice using parts 1–2.

**Key decision point.** The crux is the sign bookkeeping in raising the $2$-form's indices: $\star(e^0\wedge e^1) = -e^2\wedge e^3$ has a minus sign (from $\eta^{00}\eta^{11} = -1$), while $\star(e^2\wedge e^3) = +e^0\wedge e^1$ has a plus (from $\eta^{22}\eta^{33} = +1$). This asymmetry between electric-type and magnetic-type monomials is what makes $\star F$ send $(\mathbf E, \mathbf B) \to (-\mathbf B, \mathbf E)$ rather than a symmetric swap, and ultimately what makes $\star^2 = -1$. Getting these signs right is the entire exercise.

---

# Legal Operations Used

1. **Operation 6 from the topic page (compute a Hodge dual by contracting into $\varepsilon$).** The central operation: $(\star A)_{\alpha\beta} = \tfrac12\varepsilon_{\mu\nu\alpha\beta}A^{\mu\nu}$ applied to each basis $2$-form.

2. **Operation 1 from the topic page (raise/lower with the metric).** Used to raise the $2$-form's indices before contracting into $\varepsilon$; the signs here are the crux.

---

# Hints

> [!note]- Hint 1
> For $A = e^0\wedge e^1$: $A_{01} = 1$, $A_{10} = -1$, rest zero. Raise: $A^{01} = \eta^{00}\eta^{11}A_{01} = (1)(-1)(1) = -1$, $A^{10} = +1$. Then $(\star A)_{23} = \tfrac12\varepsilon_{\mu\nu 23}A^{\mu\nu} = \tfrac12(\varepsilon_{0123}A^{01} + \varepsilon_{1023}A^{10}) = \tfrac12((1)(-1) + (-1)(1)) = -1$.

> [!note]- Hint 2
> For $A = e^2\wedge e^3$: $A^{23} = \eta^{22}\eta^{33}A_{23} = (-1)(-1)(1) = +1$. Then $(\star A)_{01} = \tfrac12\varepsilon_{\mu\nu 01}A^{\mu\nu} = \tfrac12(\varepsilon_{2301}A^{23} + \varepsilon_{3201}A^{32}) = \tfrac12((1)(1) + (-1)(-1)) = +1$ (since $\varepsilon_{2301} = +1$, an even permutation of $0123$).

> [!note]- Hint 3
> Using $F = E_i\,e^0\wedge e^i + \tfrac12\epsilon_{ijk}B^k\,e^i\wedge e^j$ and the table from part 2: $\star$ sends each electric-type monomial to minus a magnetic-type one and each magnetic-type to plus an electric-type one. Track where $\mathbf E$ and $\mathbf B$ end up.

---

# Solution

Computing the Hodge dual of the basis $2$-forms is a careful exercise in raising indices through the indefinite metric. The plan: compute the two representative duals with full sign-tracking (Step 1), tabulate all six (Step 2), apply the table to the field strength to get the $(\mathbf E, \mathbf B) \to (-\mathbf B, \mathbf E)$ rotation (Step 3), and confirm $\star\star = -1$ directly (Step 4).

**Step 1: $\star(e^0\wedge e^1) = -e^2\wedge e^3$ and $\star(e^2\wedge e^3) = +e^0\wedge e^1$.**

> [!note]- Derivation
> *Electric-type.* Let $A = e^0\wedge e^1$, so $A_{01} = 1$, $A_{10} = -1$, all other components zero. [[Def - Metric Duality and Index Manipulation|Raise]] both indices:
> $$A^{01} = \eta^{00}\eta^{11}A_{01} = (1)(-1)(1) = -1, \qquad A^{10} = \eta^{11}\eta^{00}A_{10} = (-1)(1)(-1) = +1.$$
> The only nonzero component of $\star A$ is the one complementary to $\{0,1\}$, namely $(\star A)_{23}$:
> $$(\star A)_{23} = \tfrac12\varepsilon_{\mu\nu 23}A^{\mu\nu} = \tfrac12\big(\varepsilon_{0123}A^{01} + \varepsilon_{1023}A^{10}\big) = \tfrac12\big((+1)(-1) + (-1)(+1)\big) = \tfrac12(-2) = -1.$$
> So $(\star A)_{23} = -1$, $(\star A)_{32} = +1$, giving $\star(e^0\wedge e^1) = -\,e^2\wedge e^3$.
>
> *Magnetic-type.* Let $A = e^2\wedge e^3$, so $A_{23} = 1$. Raise: $A^{23} = \eta^{22}\eta^{33}A_{23} = (-1)(-1)(1) = +1$, $A^{32} = -1$. The complementary component is $(\star A)_{01}$:
> $$(\star A)_{01} = \tfrac12\varepsilon_{\mu\nu 01}A^{\mu\nu} = \tfrac12\big(\varepsilon_{2301}A^{23} + \varepsilon_{3201}A^{32}\big) = \tfrac12\big((+1)(+1) + (-1)(-1)\big) = +1,$$
> using $\varepsilon_{2301} = +1$ (an even permutation of $(0,1,2,3)$: $2301$ is a cyclic shift, two transpositions). So $\star(e^2\wedge e^3) = +\,e^0\wedge e^1$. The asymmetry in sign — minus for electric-type, plus for magnetic-type — comes from raising one time index ($-1$ once) versus two space indices ($-1$ twice).

**Step 2: the full table of $\star$ on basis $2$-forms.**

> [!note]- Derivation
> Repeating the computation for all six basis $2$-forms (right-handed orthonormal frame, $\varepsilon_{0123} = +1$):
> $$
> \begin{array}{llll}
> \star(e^0\wedge e^1) = -\,e^2\wedge e^3, & \star(e^0\wedge e^2) = -\,e^3\wedge e^1, & \star(e^0\wedge e^3) = -\,e^1\wedge e^2, \\[2pt]
> \star(e^2\wedge e^3) = +\,e^0\wedge e^1, & \star(e^3\wedge e^1) = +\,e^0\wedge e^2, & \star(e^1\wedge e^2) = +\,e^0\wedge e^3.
> \end{array}
> $$
> The pattern: $\star$ maps each electric-type monomial $e^0\wedge e^i$ to **minus** the complementary magnetic-type monomial, and each magnetic-type monomial to **plus** the complementary electric-type monomial. (The complementary pair to $\{0,i\}$ is $\{j,k\}$ with $(i,j,k)$ a cyclic permutation of $(1,2,3)$.) Equivalently, $\star$ acts as a "rotation by a quarter turn" that carries electric monomials into magnetic and magnetic into electric, with a sign asymmetry between the two directions — the hallmark of $\star^2 = -1$.

**Step 3: $\star F$ has fields $(-\mathbf B, \mathbf E)$.**

> [!note]- Derivation
> Write the field strength as $F = E_i\,e^0\wedge e^i + \tfrac12\epsilon_{ijk}B^k\,e^i\wedge e^j$ (from [[Ex - Expanding a 2-form in the wedge basis]]): the electric field is the coefficient of the time-space monomials, the magnetic field the coefficient of the space-space monomials. Apply $\star$ termwise with the table of Step 2:
> - The electric part $E_i\,e^0\wedge e^i$ maps to $E_i\,(-e^j\wedge e^k)$, a *space-space* term — so the electric field of $F$ becomes (part of) the magnetic field of $\star F$.
> - The magnetic part $\tfrac12\epsilon_{ijk}B^k\,e^i\wedge e^j$ maps to $+B^k\,e^0\wedge e^k$, a *time-space* term — so the magnetic field of $F$ becomes (part of) the electric field of $\star F$.
>
> Reading the coefficients back with the standard convention $F_{0i} = E_i$, $F_{ij} = \epsilon_{ijk}B^k$, the dual field strength has electric field $\mathbf E_{\star F} = -\mathbf B$ and magnetic field $\mathbf B_{\star F} = \mathbf E$:
> $$F = (\mathbf E, \mathbf B) \quad\xrightarrow{\ \star\ }\quad \star F = (-\mathbf B,\ \mathbf E).$$
> The defining feature, independent of any sign convention, is that $\star$ acts as a **quarter-turn in the $(\mathbf E, \mathbf B)$ plane**: it carries the electric field into the magnetic slot and the magnetic field into the electric slot, with one sign flip. Applying it again gives $(\mathbf E, \mathbf B) \mapsto (-\mathbf B, \mathbf E) \mapsto (-\mathbf E, -\mathbf B) = -(\mathbf E, \mathbf B)$, i.e. $\star^2 = -1$ — the duality rotation is by $90°$, and four of them ($\star^4 = +1$) return to the start.

**Step 4: $\star\star(e^0\wedge e^1) = -e^0\wedge e^1$.**

> [!note]- Derivation
> Apply $\star$ twice using Steps 1–2:
> $$\star\star(e^0\wedge e^1) = \star\big(-e^2\wedge e^3\big) = -\,\star(e^2\wedge e^3) = -\,(+e^0\wedge e^1) = -\,e^0\wedge e^1.$$
> So $\star\star(e^0\wedge e^1) = -e^0\wedge e^1$, confirming $\star^2 = -1$ on $2$-forms by direct computation. The minus sign is the product of the electric-type sign ($-1$, first application) and the magnetic-type sign ($+1$, second application): one $-$ and one $+$ multiply to $-$. This is the concrete, component-level reason behind the general identity $\star\star = (-1)^{p+1}$ at $p = 2$.

> [!note]- Complete formal solution
> **(1)** $A = e^0\wedge e^1$: raising gives $A^{01} = -1$, so $(\star A)_{23} = \tfrac12(\varepsilon_{0123}A^{01} + \varepsilon_{1023}A^{10}) = -1$, hence $\star(e^0\wedge e^1) = -e^2\wedge e^3$. $A = e^2\wedge e^3$: $A^{23} = +1$, $(\star A)_{01} = +1$, hence $\star(e^2\wedge e^3) = +e^0\wedge e^1$.
> **(2)** $\star(e^0\wedge e^i) = -e^j\wedge e^k$ and $\star(e^i\wedge e^j) = +e^0\wedge e^k$ (complementary indices, cyclic): electric-type $\to$ minus magnetic-type, magnetic-type $\to$ plus electric-type.
> **(3)** Applying the table to $F = (\mathbf E, \mathbf B)$: $\star F = (-\mathbf B, \mathbf E)$, a quarter-turn in the field plane.
> **(4)** $\star\star(e^0\wedge e^1) = \star(-e^2\wedge e^3) = -(+e^0\wedge e^1) = -e^0\wedge e^1$, confirming $\star^2 = -1$. $\blacksquare$

---

# Key Takeaways

**The Hodge star swaps electric and magnetic monomials with a sign asymmetry, and that asymmetry is $\star^2 = -1$.** The table $\star(e^0\wedge e^i) = -e^j\wedge e^k$, $\star(e^i\wedge e^j) = +e^0\wedge e^k$ shows that $\star$ carries electric-type monomials to *minus* magnetic-type ones, and magnetic-type to *plus* electric-type. The opposite signs are forced by raising one time index versus two space indices through the indefinite metric. Composing the two (electric $\to$ magnetic $\to$ electric) multiplies a $-1$ by a $+1$, giving $-1$ — this is the component-level mechanism of $\star^2 = -1$. The reusable lesson is that the Hodge star in Lorentzian signature is *not* a symmetric swap of electric and magnetic; the indefinite metric breaks the symmetry, and that broken symmetry is exactly the $-1$ that forces complexification. Whenever you compute a Hodge dual, the electric-type and magnetic-type pieces pick up opposite signs, and forgetting this gives the wrong (Euclidean) answer $\star^2 = +1$.

**Hodge duality is a quarter-turn in the $(\mathbf E, \mathbf B)$ plane, generating a $U(1)$ duality rotation.** The action $\star : (\mathbf E, \mathbf B) \mapsto (-\mathbf B, \mathbf E)$ is a $90°$ rotation in the two-dimensional plane spanned by the electric and magnetic fields, and applying it four times returns to the start ($\star^4 = +1$). This is the discrete shadow of a *continuous* duality: the source-free Maxwell equations are invariant under $F \mapsto F\cos\theta + \star F\sin\theta$ for any angle $\theta$, a $U(1)$ symmetry rotating electric into magnetic. The reusable insight is that the Hodge star *generates* this duality rotation — it is the "$90°$ element" — and that the quarter-turn structure ($\star^2 = -1$, $\star^4 = 1$) is why the duality group is $U(1)$ rather than $\mathbb{Z}_2$. This electric-magnetic duality is a deep symmetry of source-free electromagnetism and a template for the dualities of more elaborate gauge theories; recognising the Hodge star as its generator is the entry point.

**Computing a Hodge dual is "find the complementary monomial, then fix the sign by counting raised time indices."** The practical algorithm the exercise teaches: to Hodge-dualise a basis $p$-form $e^{\alpha_1}\wedge\cdots\wedge e^{\alpha_p}$, the result is (up to sign) the complementary monomial $e^{\beta_1}\wedge\cdots\wedge e^{\beta_{4-p}}$ on the indices *not* appearing, and the sign is determined by the Levi-Civita component $\varepsilon_{\alpha_1\dots\alpha_p\beta_1\dots\beta_{4-p}}$ together with the signs from raising the original indices (one $-1$ per time index raised). This reduces any Hodge-star computation on a basis form to a permutation-sign lookup plus a count of raised time indices — no full contraction needed. The transferable diagnostic: the magnitude of a basis-form's Hodge dual is always $1$ (it is another basis form), and only the *sign* requires thought; get the sign from "complementary-index Levi-Civita symbol times $(-1)^{\#\text{time indices raised}}$." This is the fast route through every Hodge computation in the electromagnetism chapters.
