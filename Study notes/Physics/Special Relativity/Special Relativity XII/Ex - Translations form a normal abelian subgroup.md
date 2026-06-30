---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Poincaré Group"
  - "Def - The Lorentz Group"
tags: [physics, special-relativity]
---

# Problem Statement

In the [[Def - The Poincaré Group|Poincaré group]] $\mathrm{ISO}(1,3)$, the translations are the elements $(\boldsymbol{v}, \mathrm{Id})$. Working with $c = 1$:

1. Show the translations form a subgroup $T \cong (\mathbb{R}^4, +)$, and that it is **abelian**.
2. Prove $T$ is a **normal** subgroup by computing the conjugate $(\boldsymbol{w}, \Lambda)(\boldsymbol{v}, \mathrm{Id})(\boldsymbol{w}, \Lambda)^{-1}$ for a general Poincaré element $(\boldsymbol{w}, \Lambda)$, and show the result is the translation $(\Lambda\boldsymbol{v}, \mathrm{Id})$.
3. Conclude that the Poincaré group is **not simple**, and contrast this with the restricted Lorentz group $\mathrm{SO}^+(1,3)$, which is simple.
4. Show by contrast that the Lorentz subgroup $\{(\boldsymbol{0}, \Lambda)\}$ is *not* normal: exhibit a conjugate of a Lorentz element that is not a Lorentz element.

**Recall:**

![[Def - The Poincaré Group#The Definition]]

A subgroup $N \le G$ is **normal**, written $N \trianglelefteq G$, if $gng^{-1} \in N$ for all $g \in G$ and $n \in N$ — conjugation by any group element keeps $N$ inside itself. A group is **simple** if its only normal subgroups are the trivial group and the whole group. The Poincaré group law is $(\boldsymbol{v}_1, \Lambda_1)(\boldsymbol{v}_2, \Lambda_2) = (\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2, \Lambda_1\Lambda_2)$, with inverse $(\boldsymbol{v}, \Lambda)^{-1} = (-\Lambda^{-1}\boldsymbol{v}, \Lambda^{-1})$; see [[Def - The Lorentz Group]] for $\Lambda$.

---

# Convergent Strategy

**Problem class.** A *prove-normality* problem: show a subgroup is closed under conjugation, hence normal, hence the group is not simple. The [[Special Relativity XII — Inertial Observers and the Poincaré Group#Problem-Solving Strategy|topic strategy]] for group-structure problems says normality is one conjugation computed via the semidirect law.

**Assumption pattern.** The tool is the group law and its inverse. Conjugation $gng^{-1}$ is three multiplications; the semidirect law evaluates each. The signpost is "is the subgroup normal?" — conjugate a generic element and check it stays inside.

**Theorem routing.** The route is the conjugation computation: $(\boldsymbol{w}, \Lambda)(\boldsymbol{v}, \mathrm{Id})(\boldsymbol{w}, \Lambda)^{-1}$, evaluated by two applications of the group law, gives $(\Lambda\boldsymbol{v}, \mathrm{Id})$ — a translation again. Closure under conjugation *is* normality; normality of a proper nontrivial subgroup *is* non-simplicity.

**Key decision point.** The crux is that conjugating a translation by a boost yields the *Lorentz-rotated* translation, which is still a translation — the semidirect structure is exactly designed so the translations are normal. The contrasting computation, conjugating a Lorentz element by a translation, yields a Lorentz-element-plus-translation, which is *not* a pure Lorentz element — so the Lorentz subgroup is not normal. Recognising that the semidirect law makes the *left* factor ($\mathbb{R}^4$) normal but not the *right* factor ($\mathrm{O}(1,3)$) is the structural payoff.

---

# Legal Operations Used

1. **Prove normality by conjugation** (operation 6 from the topic page). The translations are shown normal by computing $(\boldsymbol{w}, \Lambda)(\boldsymbol{v}, \mathrm{Id})(\boldsymbol{w}, \Lambda)^{-1} = (\Lambda\boldsymbol{v}, \mathrm{Id})$, a translation.

2. **Compose using the semidirect law** (operation 5 from the topic page). Each step of the conjugation is evaluated with $(\boldsymbol{v}_1, \Lambda_1)(\boldsymbol{v}_2, \Lambda_2) = (\boldsymbol{v}_1 + \Lambda_1\boldsymbol{v}_2, \Lambda_1\Lambda_2)$ and the inverse formula.

---

# Hints

> [!note]- Hint 1
> For the subgroup property, compose two translations: $(\boldsymbol{v}_1, \mathrm{Id})(\boldsymbol{v}_2, \mathrm{Id}) = (\boldsymbol{v}_1 + \mathrm{Id}\,\boldsymbol{v}_2, \mathrm{Id}\cdot\mathrm{Id}) = (\boldsymbol{v}_1 + \boldsymbol{v}_2, \mathrm{Id})$. The Lorentz parts are both $\mathrm{Id}$, so the twist is trivial and the translations add — abelian, and isomorphic to $(\mathbb{R}^4, +)$.

> [!note]- Hint 2
> Conjugate step by step. First $(\boldsymbol{w}, \Lambda)(\boldsymbol{v}, \mathrm{Id}) = (\boldsymbol{w} + \Lambda\boldsymbol{v}, \Lambda)$. Then multiply on the right by $(\boldsymbol{w}, \Lambda)^{-1} = (-\Lambda^{-1}\boldsymbol{w}, \Lambda^{-1})$.

> [!note]- Hint 3
> $(\boldsymbol{w} + \Lambda\boldsymbol{v}, \Lambda)(-\Lambda^{-1}\boldsymbol{w}, \Lambda^{-1}) = (\boldsymbol{w} + \Lambda\boldsymbol{v} + \Lambda(-\Lambda^{-1}\boldsymbol{w}),\, \Lambda\Lambda^{-1})$. The $\boldsymbol{w}$ terms cancel and the Lorentz part is $\mathrm{Id}$, leaving $(\Lambda\boldsymbol{v}, \mathrm{Id})$ — a translation.

> [!note]- Hint 4
> For the non-normality of the Lorentz subgroup, conjugate $(\boldsymbol{0}, \Lambda)$ by a translation $(\boldsymbol{a}, \mathrm{Id})$: compute $(\boldsymbol{a}, \mathrm{Id})(\boldsymbol{0}, \Lambda)(\boldsymbol{a}, \mathrm{Id})^{-1}$ and check whether the translation part is zero.

---

# Solution

The proof is one conjugation. Step 1 shows the translations are an abelian subgroup. Step 2 conjugates a translation by a general element and gets $(\Lambda\boldsymbol{v}, \mathrm{Id})$, still a translation — normality. Step 3 concludes non-simplicity. Step 4 shows the Lorentz subgroup is *not* normal, sharpening the asymmetry of the semidirect product.

**Step 1: The translations are an abelian subgroup.**

> [!note]- Derivation
> Compose two translations using the group law with $\Lambda_1 = \Lambda_2 = \mathrm{Id}$:
> $$(\boldsymbol{v}_1, \mathrm{Id})(\boldsymbol{v}_2, \mathrm{Id}) = (\boldsymbol{v}_1 + \mathrm{Id}\,\boldsymbol{v}_2,\; \mathrm{Id}\cdot\mathrm{Id}) = (\boldsymbol{v}_1 + \boldsymbol{v}_2,\; \mathrm{Id}).$$
> The result is a translation, so the set $T = \{(\boldsymbol{v}, \mathrm{Id}) : \boldsymbol{v}\in E\}$ is closed under multiplication; it contains the identity $(\boldsymbol{0}, \mathrm{Id})$, and the inverse $(\boldsymbol{v}, \mathrm{Id})^{-1} = (-\mathrm{Id}^{-1}\boldsymbol{v}, \mathrm{Id}^{-1}) = (-\boldsymbol{v}, \mathrm{Id})$ is again a translation. So $T$ is a subgroup. The map $\boldsymbol{v}\mapsto(\boldsymbol{v}, \mathrm{Id})$ is an isomorphism $T \cong (\mathbb{R}^4, +)$ (it sends $\boldsymbol{v}_1 + \boldsymbol{v}_2$ to the product). Since addition in $\mathbb{R}^4$ is commutative, $T$ is **abelian**: $(\boldsymbol{v}_1, \mathrm{Id})(\boldsymbol{v}_2, \mathrm{Id}) = (\boldsymbol{v}_1 + \boldsymbol{v}_2, \mathrm{Id}) = (\boldsymbol{v}_2 + \boldsymbol{v}_1, \mathrm{Id}) = (\boldsymbol{v}_2, \mathrm{Id})(\boldsymbol{v}_1, \mathrm{Id})$.

**Step 2: The translations are normal.**

> [!note]- Derivation
> Take a general Poincaré element $(\boldsymbol{w}, \Lambda)$ and a translation $(\boldsymbol{v}, \mathrm{Id})$, and compute the conjugate. First the left product:
> $$(\boldsymbol{w}, \Lambda)(\boldsymbol{v}, \mathrm{Id}) = (\boldsymbol{w} + \Lambda\boldsymbol{v},\; \Lambda\cdot\mathrm{Id}) = (\boldsymbol{w} + \Lambda\boldsymbol{v},\; \Lambda).$$
> Now multiply on the right by the inverse $(\boldsymbol{w}, \Lambda)^{-1} = (-\Lambda^{-1}\boldsymbol{w}, \Lambda^{-1})$:
> $$(\boldsymbol{w} + \Lambda\boldsymbol{v},\; \Lambda)(-\Lambda^{-1}\boldsymbol{w},\; \Lambda^{-1}) = \big(\boldsymbol{w} + \Lambda\boldsymbol{v} + \Lambda(-\Lambda^{-1}\boldsymbol{w}),\; \Lambda\Lambda^{-1}\big).$$
> The translation part simplifies: $\Lambda(-\Lambda^{-1}\boldsymbol{w}) = -\boldsymbol{w}$, so $\boldsymbol{w} + \Lambda\boldsymbol{v} - \boldsymbol{w} = \Lambda\boldsymbol{v}$, and the Lorentz part is $\Lambda\Lambda^{-1} = \mathrm{Id}$. Therefore
> $$(\boldsymbol{w}, \Lambda)(\boldsymbol{v}, \mathrm{Id})(\boldsymbol{w}, \Lambda)^{-1} = (\Lambda\boldsymbol{v},\; \mathrm{Id}).$$
> The conjugate of a translation is the translation by the Lorentz-rotated vector $\Lambda\boldsymbol{v}$ — *still a translation*, hence still in $T$. So $T$ is closed under conjugation by every element of the Poincaré group: $T \trianglelefteq \mathrm{ISO}(1,3)$. (This verifies Gourgoulhon's condition (A.3) for normality of the semidirect-product kernel.)

**Step 3: The Poincaré group is not simple.**

> [!note]- Derivation
> The translation subgroup $T$ is *proper* (it is not all of $\mathrm{ISO}(1,3)$ — it contains no nontrivial Lorentz transformation) and *nontrivial* (it is not just the identity — it is four-dimensional). A group with a proper nontrivial normal subgroup is by definition **not simple**. Hence the Poincaré group is not simple.
>
> Contrast: the restricted Lorentz group $\mathrm{SO}^+(1,3)$ *is* simple — it has no proper nontrivial normal subgroups (a fact established in [[Special Relativity IX — The Lorentz Group, Structure and Classification]] / its Lie-algebra simplicity). So enlarging the simple Lorentz group by translations *destroys* simplicity: the price of including spacetime translations is a normal abelian subgroup. Structurally, this is exactly the semidirect-product signature — the normal factor $\mathbb{R}^4$ is the obstruction to simplicity, and it is why the Poincaré group has a clean quotient $\mathrm{ISO}(1,3)/\mathbb{R}^4 \cong \mathrm{O}(1,3)$ (forgetting the translation, keeping the Lorentz part).

**Step 4: The Lorentz subgroup is not normal.**

> [!note]- Derivation
> Take a Lorentz element $(\boldsymbol{0}, \Lambda)$ with $\Lambda \neq \mathrm{Id}$ and conjugate it by a translation $(\boldsymbol{a}, \mathrm{Id})$, $\boldsymbol{a} \neq \boldsymbol{0}$. The inverse is $(\boldsymbol{a}, \mathrm{Id})^{-1} = (-\boldsymbol{a}, \mathrm{Id})$. First product:
> $$(\boldsymbol{a}, \mathrm{Id})(\boldsymbol{0}, \Lambda) = (\boldsymbol{a} + \mathrm{Id}\cdot\boldsymbol{0},\; \mathrm{Id}\cdot\Lambda) = (\boldsymbol{a},\; \Lambda).$$
> Then:
> $$(\boldsymbol{a},\; \Lambda)(-\boldsymbol{a}, \mathrm{Id}) = (\boldsymbol{a} + \Lambda(-\boldsymbol{a}),\; \Lambda\cdot\mathrm{Id}) = (\boldsymbol{a} - \Lambda\boldsymbol{a},\; \Lambda).$$
> The conjugate is $(\boldsymbol{a} - \Lambda\boldsymbol{a}, \Lambda)$. Its translation part $\boldsymbol{a} - \Lambda\boldsymbol{a} = (\mathrm{Id} - \Lambda)\boldsymbol{a}$ is *nonzero* whenever $\Lambda\boldsymbol{a} \neq \boldsymbol{a}$, i.e. whenever $\boldsymbol{a}$ is not fixed by $\Lambda$ (which holds for generic $\boldsymbol{a}$ if $\Lambda \neq \mathrm{Id}$). So the conjugate is *not* a pure Lorentz element $(\boldsymbol{0}, \cdot)$ — it carries a translation. Therefore the Lorentz subgroup $\{(\boldsymbol{0}, \Lambda)\}$ is **not normal** in the Poincaré group: conjugating a boost by a translation produces a boost-plus-translation. This is the asymmetry of the semidirect product — the translation factor is normal, the Lorentz factor is not.

> [!note]- Complete formal solution
> The translations $T = \{(\boldsymbol{v}, \mathrm{Id})\}$ form a subgroup: $(\boldsymbol{v}_1, \mathrm{Id})(\boldsymbol{v}_2, \mathrm{Id}) = (\boldsymbol{v}_1 + \boldsymbol{v}_2, \mathrm{Id})$, with identity $(\boldsymbol{0}, \mathrm{Id})$ and inverse $(-\boldsymbol{v}, \mathrm{Id})$; the map $\boldsymbol{v}\mapsto(\boldsymbol{v}, \mathrm{Id})$ is an isomorphism onto $(\mathbb{R}^4, +)$, so $T$ is abelian. For normality, $(\boldsymbol{w}, \Lambda)(\boldsymbol{v}, \mathrm{Id})(\boldsymbol{w}, \Lambda)^{-1} = (\boldsymbol{w} + \Lambda\boldsymbol{v}, \Lambda)(-\Lambda^{-1}\boldsymbol{w}, \Lambda^{-1}) = (\boldsymbol{w} + \Lambda\boldsymbol{v} - \boldsymbol{w}, \mathrm{Id}) = (\Lambda\boldsymbol{v}, \mathrm{Id}) \in T$, so $T \trianglelefteq \mathrm{ISO}(1,3)$. Since $T$ is proper and nontrivial, the Poincaré group is not simple (whereas $\mathrm{SO}^+(1,3)$ is simple). Finally the Lorentz subgroup is not normal: $(\boldsymbol{a}, \mathrm{Id})(\boldsymbol{0}, \Lambda)(-\boldsymbol{a}, \mathrm{Id}) = (\boldsymbol{a} - \Lambda\boldsymbol{a}, \Lambda)$, whose translation part $(\mathrm{Id} - \Lambda)\boldsymbol{a} \neq \boldsymbol{0}$ for generic $\boldsymbol{a}$ when $\Lambda \neq \mathrm{Id}$. $\blacksquare$

---

# Key Takeaways

**Normality is one conjugation, and in a semidirect product the kernel factor is always normal.** The proof of normality is the single computation $(\boldsymbol{w}, \Lambda)(\boldsymbol{v}, \mathrm{Id})(\boldsymbol{w}, \Lambda)^{-1} = (\Lambda\boldsymbol{v}, \mathrm{Id})$ — conjugating a translation gives the Lorentz-rotated translation, still a translation. This is no accident: in *any* semidirect product $N \rtimes H$, the normal factor $N$ is normal by construction (that is what "semidirect product" means), and conjugation by $H$ acts on $N$ through the defining action $\varphi$. The transferable diagnostic: to test normality of a subgroup, conjugate a generic element and check it lands back inside; for the translations this is immediate from the group law. The same one-line computation proves the Euclidean translations normal in $\mathrm{ISO}(3)$, the affine translations normal in the affine group, and the abelian ideal normal in any semidirect Lie algebra.

**Non-simplicity is the structural cost of including translations — and it has physical content.** The restricted Lorentz group is simple, but the Poincaré group is not, because adding the translations creates a proper normal subgroup. This is not a mere technicality: the normal subgroup of translations is generated by the four-momentum operators $P^\mu$, and its being abelian and normal is exactly what allows the eigenvalues of $P^\mu$ — the energy and momentum — to be simultaneously diagonalised and to label states (the momentum eigenbasis of quantum field theory). The quotient $\mathrm{ISO}(1,3)/\mathbb{R}^4 \cong \mathrm{O}(1,3)$ is the "internal" Lorentz structure that survives after the translations are quotiented out, and it is what acts on the rest-frame spin. Whenever a symmetry group is non-simple with an abelian normal subgroup, expect that subgroup's generators to be simultaneously-measurable conserved quantities labelling the states.

**The semidirect product is asymmetric: the left factor is normal, the right is not.** Step 4 is the essential counterweight to the normality result. Conjugating a *Lorentz* element by a translation produces $(\mathrm{Id} - \Lambda)\boldsymbol{a}$ in the translation slot — a genuine translation — so the Lorentz subgroup is *not* normal. The semidirect product $\mathbb{R}^4 \rtimes \mathrm{O}(1,3)$ is lopsided by design: only the kernel $\mathbb{R}^4$ is normal, while the complement $\mathrm{O}(1,3)$ is merely a subgroup (a section of the quotient map). The geometric content is that "where you put the origin" (the translation) can be canonically separated out and quotiented, but "which way your axes point relative to a translated frame" (the Lorentz part) cannot — boosting and then translating genuinely differs from translating in the boosted frame. Recognising which factor of a semidirect product is normal, and which is not, is the key to its representation theory: representations are built by inducing from the normal abelian factor's characters, which for the Poincaré group are exactly the momentum eigenvalues that seed Wigner's classification.
