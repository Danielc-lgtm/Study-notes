---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Subgroups and Components of the Lorentz Group"
  - "Def - The Lorentz Group"
  - "Def - Classification of Four-Vectors"
tags: [physics, special-relativity]
---

# Problem Statement

Prove directly from the defining data that the restricted Lorentz group
$$
SO^+(1,3) = \{\Lambda \in O(1,3) : \det\Lambda = +1 \ \text{and}\ \Lambda^0{}_0 \ge 1\}
$$
is a subgroup of $O(1,3)$. Specifically:

1. Show $\mathrm{Id} \in SO^+(1,3)$.
2. Show that if $\Lambda, \Lambda' \in SO^+(1,3)$ then $\Lambda\Lambda' \in SO^+(1,3)$ — the hard part is the time-component inequality $(\Lambda\Lambda')^0{}_0 \ge 1$.
3. Show that if $\Lambda \in SO^+(1,3)$ then $\Lambda^{-1} \in SO^+(1,3)$.

For part 2, establish the bound $(\Lambda\Lambda')^0{}_0 \ge \Lambda^0{}_0\,\Lambda'^0{}_0 - |\boldsymbol{\Lambda}|\,|\boldsymbol{\Lambda}'| \ge 1$ using the reversed Cauchy–Schwarz inequality, where $\boldsymbol{\Lambda} = (\Lambda^1{}_0, \Lambda^2{}_0, \Lambda^3{}_0)$ is the spatial part of the first column.

**Recall:**

![[Def - Subgroups and Components of the Lorentz Group#The Definition]]

A [[Def - The Lorentz Group|Lorentz transformation]] satisfies $\Lambda^{\mathsf T}\eta\Lambda = \eta$, equivalently $\eta_{\alpha\beta}\Lambda^\alpha{}_\mu\Lambda^\beta{}_\nu = \eta_{\mu\nu}$, with $\eta = \mathrm{diag}(1,-1,-1,-1)$. Setting $\mu = \nu = 0$ gives $(\Lambda^0{}_0)^2 - \sum_i(\Lambda^i{}_0)^2 = 1$, so $(\Lambda^0{}_0)^2 = 1 + |\boldsymbol{\Lambda}|^2 \ge 1$ where $|\boldsymbol{\Lambda}|^2 = \sum_i(\Lambda^i{}_0)^2$.

---

# Convergent Strategy

**Problem class.** A *subgroup-verification* problem from the [[Special Relativity IX — The Lorentz Group, Structure and Classification#Problem-Solving Strategy|topic strategy]]: to show a subset defined by closed conditions ($\det = +1$, $\Lambda^0{}_0 \ge 1$) is a subgroup, check closure under product and inverse and membership of the identity, with the technical work concentrated in whichever defining condition is hardest to propagate through a product. Here the determinant is trivially multiplicative; the time-component inequality is the real content.

**Assumption pattern.** The two defining conditions behave very differently under multiplication. The determinant is a homomorphism, $\det(\Lambda\Lambda') = \det\Lambda\det\Lambda'$, so $\det = +1$ propagates for free. The time-component $\Lambda^0{}_0$ is *not* multiplicative — $(\Lambda\Lambda')^0{}_0 \ne \Lambda^0{}_0\Lambda'^0{}_0$ in general — so its propagation needs an inequality, and the inequality comes from the structure $(\Lambda^0{}_0)^2 = 1 + |\boldsymbol{\Lambda}|^2$ that the defining equation forces on each column.

**Theorem routing.** The determinant half routes through multiplicativity directly. The time-component half routes through the [[Thm - The Reversed Triangle Inequality|reversed Cauchy–Schwarz inequality]] for the spatial vectors: writing $(\Lambda\Lambda')^0{}_0 = \Lambda^0{}_0\Lambda'^0{}_0 + \sum_i\Lambda^0{}_i\Lambda'^i{}_0$, the cross term is bounded by $|\boldsymbol{\Lambda}||\boldsymbol{\Lambda}'|$ (Cauchy–Schwarz), and $|\boldsymbol{\Lambda}|^2 = (\Lambda^0{}_0)^2 - 1$, giving $(\Lambda\Lambda')^0{}_0 \ge \Lambda^0{}_0\Lambda'^0{}_0 - \sqrt{((\Lambda^0{}_0)^2-1)((\Lambda'^0{}_0)^2-1)} \ge 1$.

**Key decision point.** The non-obvious choice is to bound the cross term $\sum_i\Lambda^0{}_i\Lambda'^i{}_0$ rather than compute it. One does not know its sign, but Cauchy–Schwarz bounds its magnitude by $|\boldsymbol{\Lambda}||\boldsymbol{\Lambda}'|$, and the final step is the elementary inequality $ab - \sqrt{(a^2-1)(b^2-1)} \ge 1$ for $a, b \ge 1$, which is exactly $\cosh(\xi - \xi') \ge 1$ when $a = \cosh\xi$, $b = \cosh\xi'$. The natural-but-wrong alternative is to try to compute $(\Lambda\Lambda')^0{}_0$ exactly, which is impossible without knowing all the matrix entries.

---

# Legal Operations Used

1. **Read the component of $\Lambda$ from its two signs** (operation 1 from the topic page): the membership conditions $\det = +1$ and $\Lambda^0{}_0 \ge 1$ are exactly the two sign data, and the proof is the verification that both propagate.

2. **Use the defining relation $(\Lambda^0{}_0)^2 = 1 + |\boldsymbol{\Lambda}|^2$**: derived from $\Lambda^{\mathsf T}\eta\Lambda = \eta$ at $\mu = \nu = 0$, this is the source of both the inequality $\Lambda^0{}_0 \ge 1$ and the bound on the cross term.

---

# Hints

> [!note]- Hint 1
> The identity and the determinant are easy: $\det\mathrm{Id} = 1$, $\mathrm{Id}^0{}_0 = 1$, and $\det$ is multiplicative. Concentrate all effort on showing $(\Lambda\Lambda')^0{}_0 \ge 1$.

> [!note]- Hint 2
> Write out the time–time entry of the product: $(\Lambda\Lambda')^0{}_0 = \sum_\alpha\Lambda^0{}_\alpha\Lambda'^\alpha{}_0 = \Lambda^0{}_0\Lambda'^0{}_0 + \sum_{i=1}^3\Lambda^0{}_i\Lambda'^i{}_0$. The first term is $\ge 1$; the problem is the sign and size of the second.

> [!note]- Hint 3
> Bound the cross term by Cauchy–Schwarz: $|\sum_i\Lambda^0{}_i\Lambda'^i{}_0| \le |\boldsymbol{\Lambda}^{\text{row}}||\boldsymbol{\Lambda}'|$, where $\boldsymbol{\Lambda}^{\text{row}} = (\Lambda^0{}_1, \Lambda^0{}_2, \Lambda^0{}_3)$ and $\boldsymbol{\Lambda}' = (\Lambda'^1{}_0, \Lambda'^2{}_0, \Lambda'^3{}_0)$. Both have squared length $(\Lambda^0{}_0)^2 - 1$ and $(\Lambda'^0{}_0)^2 - 1$ respectively (the first from $\Lambda^{\mathsf T}\eta\Lambda = \eta$, the second from the column relation).

> [!note]- Hint 4
> Reduce to the elementary inequality: for $a = \Lambda^0{}_0 \ge 1$ and $b = \Lambda'^0{}_0 \ge 1$, show $ab - \sqrt{(a^2-1)(b^2-1)} \ge 1$. Substitute $a = \cosh\xi$, $b = \cosh\xi'$: the left side becomes $\cosh\xi\cosh\xi' - \sinh\xi\sinh\xi' = \cosh(\xi-\xi') \ge 1$.

---

# Solution

The proof breaks into three parts. The identity and determinant conditions are immediate (Steps 1 and 3 below are short); the entire substance is Step 2, the time-component inequality, which we handle by bounding the off-diagonal contribution to the product's time–time entry via Cauchy–Schwarz and reducing to the hyperbolic identity $\cosh(\xi - \xi') \ge 1$.

**Step 1: The identity is restricted, and the determinant propagates.**

> [!note]- Derivation
> $\det\mathrm{Id} = 1 \ge $ (proper) and $\mathrm{Id}^0{}_0 = 1 \ge 1$ (orthochronous), so $\mathrm{Id} \in SO^+(1,3)$.
>
> For a product, $\det(\Lambda\Lambda') = \det\Lambda\,\det\Lambda' = (+1)(+1) = +1$ by multiplicativity of the determinant, so the product is proper. For an inverse, $\det\Lambda^{-1} = (\det\Lambda)^{-1} = 1$, so the inverse is proper. The determinant condition is thus closed under products and inverses for free.

**Step 2: The time-component inequality $(\Lambda\Lambda')^0{}_0 \ge 1$.**

> [!note]- Derivation
> Write the time–time entry of the product:
> $$(\Lambda\Lambda')^0{}_0 = \sum_{\alpha=0}^3 \Lambda^0{}_\alpha\,\Lambda'^\alpha{}_0 = \Lambda^0{}_0\,\Lambda'^0{}_0 + \sum_{i=1}^3 \Lambda^0{}_i\,\Lambda'^i{}_0.$$
> Set $a = \Lambda^0{}_0 \ge 1$, $b = \Lambda'^0{}_0 \ge 1$, $\mathbf{p} = (\Lambda^0{}_1, \Lambda^0{}_2, \Lambda^0{}_3)$ (a row of $\Lambda$), $\mathbf{q} = (\Lambda'^1{}_0, \Lambda'^2{}_0, \Lambda'^3{}_0)$ (the spatial part of $\Lambda'$'s first column). Then
> $$(\Lambda\Lambda')^0{}_0 = ab + \mathbf{p}\cdot\mathbf{q}.$$
>
> **Sizes of $\mathbf{p}$ and $\mathbf{q}$.** The relation $\Lambda\eta\Lambda^{\mathsf T} = \eta$ (equivalently the rows of $\Lambda$ are $\eta$-orthonormal) at the $(0,0)$ entry gives $(\Lambda^0{}_0)^2 - \sum_i(\Lambda^0{}_i)^2 = 1$, so $|\mathbf{p}|^2 = a^2 - 1$. The relation $\Lambda^{\mathsf T}\eta\Lambda = \eta$ at $\mu = \nu = 0$ gives $(\Lambda'^0{}_0)^2 - \sum_i(\Lambda'^i{}_0)^2 = 1$, so $|\mathbf{q}|^2 = b^2 - 1$.
>
> **Bound the cross term.** By the Cauchy–Schwarz inequality, $\mathbf{p}\cdot\mathbf{q} \ge -|\mathbf{p}||\mathbf{q}| = -\sqrt{(a^2-1)(b^2-1)}$. Therefore
> $$(\Lambda\Lambda')^0{}_0 = ab + \mathbf{p}\cdot\mathbf{q} \ge ab - \sqrt{(a^2-1)(b^2-1)}.$$
>
> **The elementary inequality.** Since $a, b \ge 1$, write $a = \cosh\xi$, $b = \cosh\xi'$ with $\xi, \xi' \ge 0$. Then $\sqrt{a^2-1} = \sinh\xi$, $\sqrt{b^2-1} = \sinh\xi'$, and
> $$ab - \sqrt{(a^2-1)(b^2-1)} = \cosh\xi\cosh\xi' - \sinh\xi\sinh\xi' = \cosh(\xi - \xi') \ge 1.$$
> Hence $(\Lambda\Lambda')^0{}_0 \ge 1$: the product is orthochronous. Combined with Step 1, $\Lambda\Lambda' \in SO^+(1,3)$.

**Step 3: The inverse is restricted.**

> [!note]- Derivation
> For $\Lambda \in O(1,3)$, the inverse is $\Lambda^{-1} = \eta\Lambda^{\mathsf T}\eta$ (from $\Lambda^{\mathsf T}\eta\Lambda = \eta$, multiply by $\eta$ and use $\eta^2 = I$). The $(0,0)$ entry of $\Lambda^{-1}$ is $(\Lambda^{-1})^0{}_0 = (\eta\Lambda^{\mathsf T}\eta)^0{}_0 = \eta^{00}(\Lambda^{\mathsf T})^0{}_0\eta_{00} = (+1)\Lambda^0{}_0(+1) = \Lambda^0{}_0 \ge 1$, so $\Lambda^{-1}$ is orthochronous. (Concretely, $(\Lambda^{-1})^0{}_0 = \Lambda^0{}_0$: the inverse has the same time–time entry.) With $\det\Lambda^{-1} = 1$ from Step 1, $\Lambda^{-1} \in SO^+(1,3)$.
>
> Therefore $SO^+(1,3)$ contains the identity and is closed under products and inverses: it is a subgroup. $\blacksquare$

> [!note]- Complete formal solution
> *Identity.* $\det\mathrm{Id} = 1$ and $\mathrm{Id}^0{}_0 = 1$, so $\mathrm{Id} \in SO^+(1,3)$.
>
> *Products.* For $\Lambda, \Lambda' \in SO^+(1,3)$: $\det(\Lambda\Lambda') = \det\Lambda\det\Lambda' = 1$, so the product is proper. For orthochronicity, $(\Lambda\Lambda')^0{}_0 = ab + \mathbf{p}\cdot\mathbf{q}$ with $a = \Lambda^0{}_0$, $b = \Lambda'^0{}_0$, $\mathbf{p} = (\Lambda^0{}_i)$, $\mathbf{q} = (\Lambda'^i{}_0)$; the row/column relations give $|\mathbf{p}|^2 = a^2 - 1$, $|\mathbf{q}|^2 = b^2 - 1$, and Cauchy–Schwarz gives $\mathbf{p}\cdot\mathbf{q} \ge -\sqrt{(a^2-1)(b^2-1)}$. Writing $a = \cosh\xi$, $b = \cosh\xi'$, $(\Lambda\Lambda')^0{}_0 \ge \cosh\xi\cosh\xi' - \sinh\xi\sinh\xi' = \cosh(\xi-\xi') \ge 1$. So $\Lambda\Lambda' \in SO^+(1,3)$.
>
> *Inverses.* $\Lambda^{-1} = \eta\Lambda^{\mathsf T}\eta$ has $\det\Lambda^{-1} = 1$ and $(\Lambda^{-1})^0{}_0 = \Lambda^0{}_0 \ge 1$, so $\Lambda^{-1} \in SO^+(1,3)$.
>
> Hence $SO^+(1,3)$ is a subgroup of $O(1,3)$. $\blacksquare$

---

# Key Takeaways

**The two defining conditions of a Lorentz subgroup propagate by completely different mechanisms, and recognising which is "hard" is the whole game.** The determinant is a group homomorphism, so any determinant condition ($\det = +1$, $\det = \pm 1$) propagates through products automatically — there is nothing to prove. The time-component condition is *not* multiplicative, because the time–time entry of a product picks up a cross term $\mathbf{p}\cdot\mathbf{q}$ from the spatial parts, and that cross term has unknown sign. The general lesson for subgroup-verification problems is to identify which defining condition fails to be a homomorphism and concentrate all the work there; the others come for free. Here the orthochronous condition is the non-homomorphic one, and the entire proof is the control of its cross term.

**Cauchy–Schwarz plus the hyperbolic substitution is the canonical way to propagate a $\Lambda^0{}_0 \ge 1$ condition.** The bound $(\Lambda\Lambda')^0{}_0 \ge ab - \sqrt{(a^2-1)(b^2-1)} = \cosh(\xi - \xi') \ge 1$ is a reusable template: whenever you must show that a product of orthochronous transformations is orthochronous, write the time–time entry as a diagonal term plus a cross term, bound the cross term by Cauchy–Schwarz using the column relations $|\boldsymbol{\Lambda}|^2 = (\Lambda^0{}_0)^2 - 1$, and reduce to $\cosh(\xi - \xi') \ge 1$ via the substitution $\Lambda^0{}_0 = \cosh\xi$. The trigger is "a product of orthochronous transformations"; the move is "diagonal term minus Cauchy–Schwarz bound, then hyperbolic identity." This same template shows the *antichronous* set is not closed (two antichronous transformations, $a, b \le -1$, give $ab \ge 1$, a positive product — orthochronous), which is why only the orthochronous piece is a group.

**The time–time entry is conjugation-invariant, which is why the inverse is automatic.** The computation $(\Lambda^{-1})^0{}_0 = \Lambda^0{}_0$ — the inverse has the *same* time–time entry — is worth remembering: it follows from $\Lambda^{-1} = \eta\Lambda^{\mathsf T}\eta$ and the fact that transposing fixes the $(0,0)$ entry while the two $\eta$'s contribute $(+1)^2$. This means the orthochronous condition is automatically closed under inverses (no inequality needed), and it foreshadows the deeper fact that $\Lambda^0{}_0$ is conjugation-friendly, which is what makes $SO^+(1,3)$ *normal* ([[Thm - The Restricted Lorentz Group is a Normal Subgroup]]). The pattern "the inverse preserves the orthochronous type" recurs throughout the component analysis, and it is the reason the orthochronous transformations form a subgroup while the antichronous ones do not.
