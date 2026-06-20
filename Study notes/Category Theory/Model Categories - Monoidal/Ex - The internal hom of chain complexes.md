---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Closed Monoidal Category"
  - "Def - Chain Map and Chain Homotopy"
  - "Def - Tensor Product of Modules"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $R$ be a commutative ring and $\mathbf{Ch}(R)$ the category of (unbounded) chain complexes of $R$-modules. The tensor product is $(M \otimes_R N)_n = \bigoplus_{p+q = n} M_p \otimes_R N_q$ with differential $d(x \otimes y) = dx \otimes y + (-1)^{|x|} x \otimes dy$. Show that $\mathbf{Ch}(R)$ is [[Def - Closed Monoidal Category|closed monoidal]] by constructing the internal hom $[M, N]$ with
$$[M, N]_n = \prod_{p} \mathrm{Hom}_R(M_p, N_{p+n}), \qquad (df)(x) = d(f(x)) - (-1)^{|f|} f(dx),$$
and verifying the tensor-hom adjunction $\mathbf{Ch}(R)(L \otimes_R M, N) \cong \mathbf{Ch}(R)(L, [M, N])$. Identify the degree-zero cycles $Z_0[M, N]$ and degree-zero homology $H_0[M, N]$ in terms of chain maps and chain homotopy.

**Recall:**

A [[Def - Closed Monoidal Category|closed monoidal category]] is $(\mathcal{C}, \otimes, I)$ with each $- \otimes B$ having a right adjoint $[B, -]$: $\mathcal{C}(A \otimes B, C) \cong \mathcal{C}(A, [B, C])$.

![[Def - Chain Map and Chain Homotopy#The Definition]]

The unit of $(\mathbf{Ch}(R), \otimes_R)$ is $R$ regarded as a complex concentrated in degree $0$.

---

# Convergent Strategy

**Problem class:** This is a *construct-and-verify-an-adjunction* problem: build a candidate internal hom complex, check it is a complex ($d^2 = 0$), and verify the natural bijection of the tensor-hom adjunction. It is the chain-complex instance of "closedness is the tensor-hom adjunction" from the topic page.

**Assumption pattern:** The crucial structural input is the **Koszul sign rule** in the tensor differential and the matching sign in the internal-hom differential — these signs are forced by the demand that $\mathrm{ev}$ be a chain map and that the adjunction be natural. The second input is that everything is computed degreewise from the module-level [[Def - Tensor Product of Modules|tensor-hom adjunction]], lifted to complexes by bookkeeping the degrees.

**Theorem routing:** The degreewise adjunction $\mathrm{Hom}_R(L_a \otimes_R M_b, N_c) \cong \mathrm{Hom}_R(L_a, \mathrm{Hom}_R(M_b, N_c))$ (the module tensor-hom adjunction) assembles, after summing over degrees and matching the differentials, into the complex-level adjunction $\mathbf{Ch}(R)(L \otimes_R M, N) \cong \mathbf{Ch}(R)(L, [M, N])$. The final identification of $Z_0$ and $H_0$ routes through the [[Def - Chain Map and Chain Homotopy|definitions of chain map and chain homotopy]].

**Key decision point:** The non-obvious choice is the sign convention in $(df)(x) = d(f(x)) - (-1)^{|f|} f(dx)$. With this sign, a degree-zero element $f$ is a *cycle* ($df = 0$) exactly when $f$ commutes with the differential, i.e. is a chain map; and two chain maps are *homologous* in $[M,N]$ exactly when they are chain homotopic. Getting the sign wrong breaks the identification and even breaks $d^2 = 0$. Recognizing that the internal hom *encodes chain maps and chain homotopies in its low-degree homology* is the payoff.

---

# Legal Operations Used

1. **Operation (closedness as adjunction), topic page.** We treat the internal hom as the right adjoint of $- \otimes_R M$ and verify the defining bijection, rather than positing $[M, N]$ abstractly.

2. **Operation (reduce to the module level).** The complex-level structure is built degreewise from the module tensor-hom adjunction; we lift a known adjunction up the grading rather than reproving it.

---

# Hints

> [!note]- Hint 1
> Build $[M, N]$ degreewise: an element of degree $n$ should be a family of $R$-linear maps raising degree by $n$. Write down which products of $\mathrm{Hom}_R(M_p, N_{p+n})$ this is.

> [!note]- Hint 2
> The differential on $[M, N]$ must be chosen so that the degree-zero cycles are exactly the chain maps. Try $(df) = d \circ f \pm f \circ d$ and fix the sign by demanding $d^2 = 0$ and that $df = 0$ means $f$ commutes with $d$.

> [!note]- Hint 3
> For the adjunction, transpose degreewise: a chain map $L \otimes_R M \to N$ restricted to $L_a \otimes_R M_b$ lands in $N_{a+b}$; transpose the module map $L_a \otimes_R M_b \to N_{a+b}$ to $L_a \to \mathrm{Hom}_R(M_b, N_{a+b})$ and reassemble into a map $L \to [M, N]$. Check the differential-compatibility matches.

> [!note]- Hint 4
> Once the differential is fixed, compute: $f \in [M,N]_0$ with $df = 0$ unwinds to $d_N f = f d_M$ (chain map); and $f - g = dh$ for $h \in [M,N]_1$ unwinds to the chain-homotopy equation $f - g = d_N h + h d_M$.

---

# Solution

The route is: (1) define $[M, N]$ degreewise and check $d^2 = 0$ using the Koszul sign; (2) verify the tensor-hom adjunction by transposing degreewise; (3) read off that $Z_0[M,N]$ is the chain maps and $H_0[M,N]$ the chain-homotopy classes. The sign in the differential is the linchpin.

**Step 1: $[M, N]$ is a chain complex.**

> [!note]- Derivation
> Define $[M, N]_n = \prod_p \mathrm{Hom}_R(M_p, N_{p+n})$, the $R$-module of degree-$n$ graded maps $M \to N$ (raising degree by $n$, not necessarily commuting with $d$). For $f$ homogeneous of degree $|f| = n$, set
> $$(df)(x) = d_N(f(x)) - (-1)^{n} f(d_M x).$$
> This $df$ has degree $n - 1$. Compute $d^2 f$: writing $d$ for the appropriate differentials,
> $$(d^2 f)(x) = d_N\big((df)(x)\big) - (-1)^{n-1}(df)(d_M x).$$
> Expanding both terms using $(df)(x) = d_N f(x) - (-1)^n f(d_M x)$ and $d_N^2 = d_M^2 = 0$, the four resulting terms cancel in pairs precisely because of the sign $-(-1)^n$ versus $-(-1)^{n-1} = (-1)^n$. Hence $d^2 = 0$ and $[M, N]$ is a chain complex.

**Step 2: The tensor-hom adjunction holds.**

> [!note]- Derivation
> Both sides are the $R$-modules of chain maps. A chain map $\Phi : L \otimes_R M \to N$ is a degree-zero graded map commuting with $d$; restricted to the summand $L_a \otimes_R M_b$ it is an $R$-linear map $\Phi_{a,b} : L_a \otimes_R M_b \to N_{a+b}$. By the module-level [[Def - Tensor Product of Modules|tensor-hom adjunction]], $\Phi_{a,b}$ transposes to $\widehat\Phi_{a,b} : L_a \to \mathrm{Hom}_R(M_b, N_{a+b})$. Assembling over $b$ gives $\widehat\Phi_a : L_a \to \prod_b \mathrm{Hom}_R(M_b, N_{a+b}) = [M, N]_a$, i.e. a degree-zero graded map $\widehat\Phi : L \to [M, N]$. A direct check shows $\Phi$ commutes with the tensor differential (with its Koszul sign) if and only if $\widehat\Phi$ commutes with the internal-hom differential (with its sign) — the signs are matched precisely so that this equivalence holds. Hence $\Phi \leftrightarrow \widehat\Phi$ is a bijection $\mathbf{Ch}(R)(L \otimes_R M, N) \cong \mathbf{Ch}(R)(L, [M, N])$, natural in $L$ and $N$. The evaluation $\mathrm{ev} : [M, N] \otimes_R M \to N$, $(f, x) \mapsto f(x)$, is the counit.

**Step 3: Low-degree (co)homology of $[M, N]$ encodes chain maps and homotopies.**

> [!note]- Derivation
> An element $f \in [M, N]_0$ is a degree-zero graded map $f : M \to N$. It is a *cycle* iff $df = 0$, i.e. $d_N f(x) - f(d_M x) = 0$ for all $x$, i.e. $d_N f = f d_M$: $f$ is a [[Def - Chain Map and Chain Homotopy|chain map]]. So $Z_0[M, N] = \{\text{chain maps } M \to N\}$.
> Two chain maps $f, g$ are *homologous* in $[M, N]_0$ iff $f - g = dh$ for some $h \in [M, N]_1$. With $|h| = 1$, $(dh)(x) = d_N h(x) + h(d_M x)$, so $f - g = d_N h + h d_M$ — exactly the [[Def - Chain Map and Chain Homotopy|chain homotopy]] equation. Hence
> $$H_0[M, N] = \frac{\text{chain maps } M \to N}{\text{chain homotopy}} = \mathbf{Ch}(R)(M, N)/\!\simeq,$$
> the chain-homotopy classes of chain maps. (More generally $H_n[M, N]$ is the degree-$n$ chain-homotopy classes; in the derived setting these compute $\mathrm{Ext}$.)

> [!note]- Complete formal solution
> Define $[M, N]_n = \prod_p \mathrm{Hom}_R(M_p, N_{p+n})$ with $(df)(x) = d_N(f(x)) - (-1)^{|f|} f(d_M x)$. A sign-tracking computation gives $d^2 = 0$ (the cross terms cancel because the two differential applications carry opposite signs), so $[M, N] \in \mathbf{Ch}(R)$. Restricting a chain map $L \otimes_R M \to N$ to $L_a \otimes_R M_b \to N_{a+b}$ and applying the module [[Def - Tensor Product of Modules|tensor-hom adjunction]] degreewise yields a natural bijection $\mathbf{Ch}(R)(L \otimes_R M, N) \cong \mathbf{Ch}(R)(L, [M, N])$, with the differential-compatibility on each side equivalent by the matched Koszul signs; the counit is evaluation. Thus $- \otimes_R M \dashv [M, -]$ and $\mathbf{Ch}(R)$ is [[Def - Closed Monoidal Category|closed symmetric monoidal]] with unit $R$. Finally, $Z_0[M, N] = \{\text{chain maps}\}$ (since $df = 0 \iff d_N f = f d_M$) and $H_0[M, N] = \{\text{chain maps}\}/\text{chain homotopy}$ (since $f - g = dh$ for $h$ of degree $1$ is the chain-homotopy equation $f - g = d_N h + h d_M$). $\qquad\blacksquare$

---

# Key Takeaways

**The internal hom of complexes is a complex whose low homology *is* the morphism theory of complexes — this is the prototype of "homotopy lives in the internal hom".** The construction reveals that the chain-complex $[M, N]$ is not an exotic gadget but a precise organizer: its zero-cycles are chain maps, its zero-homology is chain-homotopy classes, and its higher homology (after deriving) is Ext. The transferable lesson is that in any closed monoidal *model* category, the homotopy theory of maps $M \to N$ is recorded in the homotopy of the internal hom $[M, N]$, and "deriving the internal hom" (replacing $M$ cofibrantly, $N$ fibrantly) is exactly how mapping spaces and Ext groups get computed. When you see an internal hom in a homotopical setting, ask what its homotopy groups are — they are the derived mapping invariants.

**The Koszul sign rule is not decoration; it is forced by requiring the structure maps to be chain maps, and it is the same sign that recurs across all of homological algebra.** The cancellation in $d^2 = 0$ and the matching of the adjunction differentials both hinge on the sign $(-1)^{|f|}$. The trigger-reaction pattern is: whenever you tensor or hom graded objects with differentials, insert the sign $(-1)^{|\text{thing passed}|}$ when a differential hops over a homogeneous element, and verify $d^2 = 0$ as a check that the signs are right. This is the same sign discipline behind the tensor differential, the Eilenberg–Zilber map, the cup product, and the Koszul complex — get it right once here and it transfers everywhere graded objects meet differentials.

**The exercise is a worked instance of "build the closed structure degreewise from a known module-level adjunction", a strategy that scales to graded, filtered, and equivariant settings.** Rather than guessing the internal hom, we lifted the [[Def - Tensor Product of Modules|module tensor-hom adjunction]] up the grading, handling only the new bookkeeping (degrees and signs). The reusable diagnostic: to construct a closed monoidal structure on a category of "decorated modules" (graded, with differential, with a group action, with a filtration), find the adjunction on the underlying modules and ask what extra structure the decoration imposes on the hom-object — usually just a degree shift and a sign, occasionally an equalizer to enforce equivariance. This is exactly the pattern by which one equips spectra, dg-categories, and equivariant module categories with their internal homs. See also [[Ex - Mod_R is closed monoidal but not cartesian closed]] and [[Ex - The derived tensor on chain complexes computes Tor]].
