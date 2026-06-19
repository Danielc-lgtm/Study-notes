---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Product and Coproduct"
  - "Def - Free Group and Free Product"
  - "Def - Direct Sum of Modules"
tags: [category-theory, foundations]
---

# Problem Statement

Identify the [[Def - Product and Coproduct|coproduct]] in $\mathbf{Set}$, $\mathbf{Ab}$, and $\mathbf{Grp}$, and verify the universal property in each. Show that the coproduct is the disjoint union in $\mathbf{Set}$, the [[Def - Direct Sum of Modules|direct sum]] in $\mathbf{Ab}$, and the [[Def - Free Group and Free Product|free product]] in $\mathbf{Grp}$. Explain why the coproduct coincides with the product for two summands in $\mathbf{Ab}$ but not in $\mathbf{Grp}$, and exhibit the discrepancy concretely with $C_2$ and $C_2$.

**Recall:**

A **coproduct** of $A$ and $B$ is an object $A + B$ with injections $\iota_1 : A \to A+B$, $\iota_2 : B \to A+B$ such that for every $X$ and pair $f : A \to X$, $g : B \to X$ there is a *unique* $[f,g] : A + B \to X$ with $[f,g]\iota_1 = f$, $[f,g]\iota_2 = g$. Equivalently $\mathcal{C}(A+B, X) \cong \mathcal{C}(A, X) \times \mathcal{C}(B, X)$.

![[Def - Free Group and Free Product#The Definition]]

The [[Def - Direct Sum of Modules|direct sum]] $A \oplus B$ of abelian groups is the set of pairs $(a,b)$ with componentwise addition; for two summands it equals the direct product.

---

# Convergent Strategy

**Problem class:** This is an "identify the universal object" problem, dual to the product case, but with a twist that makes it ⭐⭐: the coproduct is genuinely *different* in each category, and the difference is driven by whether maps out of the pieces can be combined freely. The routine is to verify the universal property of a candidate, but choosing the right candidate requires understanding how maps *out of* the object behave.

**Assumption pattern:** The discriminating feature is whether the target's structure forces the two images to interact. In $\mathbf{Set}$ there is no structure, so the pieces stay disjoint. In $\mathbf{Ab}$ the target is commutative, so the two images commute and can be added — that is why the direct sum works. In $\mathbf{Grp}$ the target need not be commutative, so nothing forces the images to commute, and the universal object must keep them maximally free — the free product.

**Theorem routing:** The verification routes through the gluing map $[f,g]$. In $\mathbf{Set}$, $[f,g]$ applies $f$ or $g$ depending on the piece. In $\mathbf{Ab}$, $[f,g](a,b) = f(a) + g(b)$, well-defined as a homomorphism *because the target is abelian*. In $\mathbf{Grp}$, $[f,g]$ sends a reduced word $x_1 x_2 \cdots$ to $f$ or $g$ of each letter and multiplies in $X$; the [[Def - Free Group and Free Product|free product]]'s universal property is exactly this. The general principle is $\mathcal{C}(A+B, X) \cong \mathcal{C}(A,X) \times \mathcal{C}(B,X)$.

**Key decision point:** The crux is recognising *why commutativity of the target is the deciding factor*. In $\mathbf{Ab}$, $f(a) + g(b)$ is forced to be the value, and it works because $+$ is commutative; in $\mathbf{Grp}$, attempting "$f(a) \cdot g(b)$" fails because there is no canonical order and no commutativity, so the universal object cannot collapse the two pieces — it must be the free product, not the direct product. The natural-but-wrong guess "coproduct = product" is correct in $\mathbf{Ab}$ and false in $\mathbf{Grp}$, and seeing exactly where it breaks is the lesson.

---

# Legal Operations Used

1. **Verify a universal property of a candidate (from the topic page).** In each category, take a target $X$ with maps from both pieces and produce the unique gluing map $[f,g]$ out of the candidate coproduct.

2. **Read maps out of a coproduct as pairs of maps (representability of the coproduct).** Use $\mathcal{C}(A+B, X) \cong \mathcal{C}(A,X) \times \mathcal{C}(B,X)$ to organise each verification as "a map out of the candidate is a pair of maps out of the pieces".

3. **Dualize a known product computation (operation: pass to the opposite category).** The coproduct is the product in $\mathcal{C}^{op}$; comparing with [[Ex - Products in Set Grp and Top]] highlights where the dualization is symmetric ($\mathbf{Set}$) and where the categories are not self-dual ($\mathbf{Grp}$).

---

# Hints

> [!note]- Hint 1
> The coproduct is about maps *out*. Ask: given $f : A \to X$ and $g : B \to X$, what is the most economical object $A + B$ through which both factor, adding no relations beyond what is forced?

> [!note]- Hint 2
> In $\mathbf{Ab}$, the only sensible value for the gluing map on $(a,b)$ is $f(a) + g(b)$. Check it is a homomorphism — and notice exactly which step uses that $X$ is abelian.

> [!note]- Hint 3
> In $\mathbf{Grp}$, the analogue "$f(a)g(b)$" has no canonical meaning because order matters. The fix is to keep $A$ and $B$ unmixed: form reduced alternating words. That is the free product.

> [!note]- Hint 4
> For the $C_2, C_2$ comparison: the direct product $C_2 \times C_2$ has order $4$; the free product $C_2 * C_2$ is infinite (it is the infinite dihedral group). Compute both and see they cannot be isomorphic.

---

# Solution

The plan is to verify the universal property of three candidate coproducts. In $\mathbf{Set}$ it is the disjoint union; in $\mathbf{Ab}$ the direct sum, with the gluing map $f(a)+g(b)$ working precisely because the target is commutative; in $\mathbf{Grp}$ the free product of reduced words, where the absence of forced commutativity prevents collapse to the direct product. The $C_2,C_2$ example makes the gap concrete: order $4$ versus infinite.

**Step 1: The coproduct in $\mathbf{Set}$ is the disjoint union.**

> [!note]- Derivation
> Let $A + B = (\{1\}\times A) \cup (\{2\}\times B)$ with $\iota_1(a) = (1,a)$, $\iota_2(b) = (2,b)$. Given $f : A \to X$, $g : B \to X$, define $[f,g](1,a) = f(a)$, $[f,g](2,b) = g(b)$. Then $[f,g]\iota_1 = f$, $[f,g]\iota_2 = g$, and any $u$ with these properties must agree with $[f,g]$ on each tagged element, so $[f,g]$ is unique. Hence $A+B$ is the coproduct.

**Step 2: The coproduct in $\mathbf{Ab}$ is the direct sum, and equals the product.**

> [!note]- Derivation
> Let $A \oplus B$ be the [[Def - Direct Sum of Modules|direct sum]]: pairs $(a,b)$ with $(a,b)+(a',b') = (a+a', b+b')$, injections $\iota_1(a) = (a,0)$, $\iota_2(b) = (0,b)$. Given homomorphisms $f : A \to X$, $g : B \to X$ into an abelian group $X$, define $[f,g](a,b) = f(a) + g(b)$. This is a homomorphism:
> $$[f,g]\big((a,b)+(a',b')\big) = f(a+a') + g(b+b') = f(a)+f(a') + g(b)+g(b') = [f,g](a,b) + [f,g](a',b'),$$
> where reordering $f(a') + g(b) = g(b) + f(a')$ **uses that $X$ is abelian**. We have $[f,g]\iota_1(a) = f(a) + g(0) = f(a)$ and similarly $[f,g]\iota_2 = g$. Uniqueness: any homomorphism $u$ with $u\iota_1 = f$, $u\iota_2 = g$ satisfies $u(a,b) = u\big(\iota_1(a) + \iota_2(b)\big) = f(a) + g(b)$. So $A \oplus B$ is the coproduct. Since for two summands $A \oplus B = A \times B$ as a group, the coproduct and product coincide — a **biproduct**.

**Step 3: The coproduct in $\mathbf{Grp}$ is the free product.**

> [!note]- Derivation
> Let $G * H$ be the [[Def - Free Group and Free Product|free product]]: its elements are reduced words alternating between non-identity elements of $G$ and of $H$, multiplied by concatenation-and-reduction; injections $\iota_G, \iota_H$ are the inclusions as one-letter words. Given homomorphisms $f : G \to X$, $g : H \to X$, define $[f,g]$ on a reduced word $x_1 x_2 \cdots x_n$ by replacing each letter $x_i$ with $f(x_i)$ or $g(x_i)$ (according to its factor) and multiplying the results in $X$. This is well-defined on reduced words and is a homomorphism (concatenation maps to product); $[f,g]\iota_G = f$, $[f,g]\iota_H = g$. Uniqueness: a homomorphism out of $G * H$ is determined by its values on the generators $G$ and $H$, i.e. by $f$ and $g$. So $G * H$ is the coproduct. Crucially, no commutation between $G$- and $H$-letters is imposed, because the generic target $X$ is non-abelian and would not respect it.

**Step 4: $C_2 \sqcup C_2$ differs in $\mathbf{Ab}$ and $\mathbf{Grp}$.**

> [!note]- Derivation
> In $\mathbf{Ab}$: $C_2 \oplus C_2$ is the Klein four-group, order $4$, every non-identity element of order $2$. In $\mathbf{Grp}$: $C_2 * C_2 = \langle a, b \mid a^2 = b^2 = 1\rangle$ contains $ab$ of infinite order (reduced words $abab\cdots$ never reduce), so $C_2 * C_2$ is infinite — it is the infinite dihedral group $D_\infty$. An order-$4$ group cannot be isomorphic to an infinite group, so the coproduct genuinely depends on the category. The difference is exactly the imposed commutativity: $\mathbf{Ab}$ forces $ab = ba$, collapsing $D_\infty$ onto its abelianization $C_2 \times C_2$.

> [!note]- Complete formal solution
> **$\mathbf{Set}$:** the disjoint union $A + B = \{1\}\times A \cup \{2\}\times B$ with tag injections; the gluing map $[f,g]$ applies $f$ on the $A$-tag and $g$ on the $B$-tag, uniquely determined.
> **$\mathbf{Ab}$:** the [[Def - Direct Sum of Modules|direct sum]] $A \oplus B$ with $\iota_1(a) = (a,0)$, $\iota_2(b) = (0,b)$; the gluing map $[f,g](a,b) = f(a)+g(b)$ is a homomorphism precisely because the target is abelian (the step $f(a')+g(b) = g(b)+f(a')$), and is forced by $u(a,b) = u(\iota_1 a + \iota_2 b)$. For two summands $A \oplus B = A \times B$, so coproduct $=$ product (a biproduct).
> **$\mathbf{Grp}$:** the [[Def - Free Group and Free Product|free product]] $G * H$ of reduced alternating words; $[f,g]$ substitutes $f$/$g$ for each letter and multiplies in $X$, determined by its values on generators, with no $G$–$H$ commutation imposed.
> **Discrepancy:** $C_2 \oplus C_2$ has order $4$; $C_2 * C_2 = \langle a,b \mid a^2=b^2=1\rangle = D_\infty$ is infinite (since $ab$ has infinite order). They are not isomorphic, so the coproduct depends on the category; passing to $\mathbf{Ab}$ imposes commutativity and abelianizes $D_\infty$ to $C_2\times C_2$. By [[Thm - Limits are Unique up to Unique Isomorphism|uniqueness of colimits]] each coproduct is well-defined up to unique isomorphism. $\blacksquare$

---

# Key Takeaways

**The coproduct is governed by what the target's structure forces on maps out, and commutativity is the pivot.** The transferable insight is that the coproduct is the *freest* object through which two maps-out factor, and how free depends entirely on what relations the codomain imposes. In $\mathbf{Ab}$, commutativity of every target lets you define the gluing map by addition $f(a)+g(b)$, collapsing the free combination down to the direct sum; in $\mathbf{Grp}$, no commutativity is available, so the universal object must keep the pieces unmixed as a free product. The trigger to recognise elsewhere: whenever you compute a coproduct, ask "what does an arbitrary map out of each piece look like, and what relations between their images are forced by the target?" — the answer is the coproduct.

**Product and coproduct coincide exactly when the category has biproducts, which is an additivity phenomenon.** The fact that $A \oplus B = A \times B$ in $\mathbf{Ab}$ (and $\mathbf{Vect}_k$, $\mathbf{Mod}_R$) is not a coincidence but the defining feature of **additive** and **abelian categories**: finite products and coproducts agree and are called biproducts. The diagnostic is the existence of a zero object and the ability to *add* parallel morphisms — that addition is what makes $f(a)+g(b)$ meaningful and forces product $=$ coproduct for finitely many summands. Recognising "this category has biproducts" tells you instantly that finite limits and colimits of discrete diagrams agree, which is structurally why homological algebra lives in abelian categories.

**The $C_2 * C_2 = D_\infty$ example is the canonical witness that forgetful functors destroy colimits.** This concrete computation — order $4$ in $\mathbf{Ab}$ versus infinite in $\mathbf{Grp}$ — is the example to keep in working memory, because it simultaneously shows that the coproduct is category-dependent and that the [[Def - Preservation, Reflection, and Creation of Limits|forgetful functor]] $U : \mathbf{Grp} \to \mathbf{Set}$ cannot preserve coproducts: the underlying set of $G * H$ is enormous, not the disjoint union $U(G) \sqcup U(H)$. The reusable principle is that *left*-adjoint-like structure (free constructions, colimits) is fragile under forgetting, whereas *right*-adjoint structure (limits) is preserved — the asymmetry developed in [[Ex - The forgetful functor from groups preserves limits not colimits]]. Whenever a free or universal-combination construction appears, expect its underlying set to be much larger than naive set-level gluing.
