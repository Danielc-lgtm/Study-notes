---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Homotopy Category of a Monoidal Model Category is Monoidal"
  - "Def - Monoidal Model Category"
  - "Def - Cofibrant and Fibrant Objects"
  - "Def - Tensor Product of Modules"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $R$ be a commutative ring and $\mathbf{Ch}(R)$ the chain complexes with the projective model structure (weak equivalences = quasi-isomorphisms; cofibrant objects include bounded-below complexes of projectives). View $R$-modules $M, N$ as complexes concentrated in degree $0$. Show that the [[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal|derived tensor product]] satisfies
$$H_n\big(M \otimes^{\mathbf{L}}_R N\big) \;=\; \mathrm{Tor}^R_n(M, N),$$
by cofibrantly replacing $M$ with a projective resolution $P_\bullet \xrightarrow{\sim} M$ and computing $H_n(P_\bullet \otimes_R N)$. Verify on the example $R = \mathbb{Z}$, $M = N = \mathbb{Z}/2$ that $\mathrm{Tor}^{\mathbb{Z}}_0(\mathbb{Z}/2, \mathbb{Z}/2) = \mathbb{Z}/2$ and $\mathrm{Tor}^{\mathbb{Z}}_1(\mathbb{Z}/2, \mathbb{Z}/2) = \mathbb{Z}/2$, and that the *naive* tensor $\mathbb{Z}/2 \otimes_{\mathbb{Z}} \mathbb{Z}/2$ sees only $\mathrm{Tor}_0$.

**Recall:**

The [[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal|derived tensor]] is $M \otimes^{\mathbf{L}}_R N = QM \otimes_R QN$, where $Q$ is [[Def - Cofibrant and Fibrant Objects|cofibrant replacement]]. In $\mathbf{Ch}(R)$, cofibrant replacement of a module is a **projective resolution**: $\cdots \to P_1 \to P_0 \to 0$ with each $P_i$ projective and $P_\bullet \xrightarrow{\sim} M$ a quasi-isomorphism. A module $N$ in degree $0$ is generally *not* cofibrant.

$\mathrm{Tor}^R_n(M, N)$ is, by definition, $H_n(P_\bullet \otimes_R N)$ for a projective resolution $P_\bullet$ of $M$ — independent of the resolution.

---

# Convergent Strategy

**Problem class:** This is a *compute-a-derived-functor* problem, the signature application of §3: identify an abstract derived tensor with a classical invariant by cofibrantly replacing and computing on the point set. It is the bridge between this chapter's machinery and the homological algebra the reader already knows.

**Assumption pattern:** The key recognition is that cofibrant replacement in $\mathbf{Ch}(R)$ *is* projective resolution, so the abstract $\otimes^{\mathbf{L}}_R$ becomes the very thing $\mathrm{Tor}$ is defined to be. The second input is that only *one* factor needs cofibrant replacement when computing homology, because tensoring with a complex of projectives is exact — this is the homotopical content of the pushout-product axiom for $\mathbf{Ch}(R)$.

**Theorem routing:** The route is: by [[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal|the derived-monoidal theorem]], $M \otimes^{\mathbf{L}}_R N = QM \otimes_R QN$ is well-defined; replace $M$ by $P_\bullet$ (projective resolution); use that $P_\bullet \otimes_R -$ preserves quasi-isomorphisms (so $QN$ may be taken to be $N$ itself); compute $H_n(P_\bullet \otimes_R N)$, which is $\mathrm{Tor}^R_n(M, N)$ by definition.

**Key decision point:** The non-obvious discipline is to replace *only* $M$, not both factors, and to justify it: $P_\bullet \otimes_R -$ is exact (sends quasi-isomorphisms to quasi-isomorphisms) because each $P_i$ is projective, so $P_\bullet \otimes_R QN \simeq P_\bullet \otimes_R N$. Recognizing that the well-definedness theorem permits this asymmetry — and that it recovers the classical, manifestly-one-sided definition of $\mathrm{Tor}$ — is the heart of the exercise.

---

# Legal Operations Used

1. **Operation 4 (cofibrantly replace before tensoring), topic page.** We compute $\otimes^{\mathbf{L}}_R$ by replacing $M$ with its cofibrant (projective) resolution before tensoring.

2. **Operation 5 (Ken Brown / homotopy-invariance on cofibrant objects), topic page.** We use that $P_\bullet \otimes_R -$ preserves weak equivalences (it is left Quillen with $P_\bullet$ cofibrant), licensing the replacement of $QN$ by $N$.

---

# Hints

> [!note]- Hint 1
> What is cofibrant replacement of a module $M$ (in degree $0$) in $\mathbf{Ch}(R)$? It is a quasi-isomorphism from a complex of projectives — a projective resolution.

> [!note]- Hint 2
> By definition, $M \otimes^{\mathbf{L}}_R N = QM \otimes_R QN$. Take $QM = P_\bullet$. Do you need to replace $N$ too? Tensoring with a complex of projectives is exact, so no — $P_\bullet \otimes_R N \simeq P_\bullet \otimes_R QN$.

> [!note]- Hint 3
> Now $H_n(M \otimes^{\mathbf{L}}_R N) = H_n(P_\bullet \otimes_R N)$. But that is *precisely* the definition of $\mathrm{Tor}^R_n(M, N)$.

> [!note]- Hint 4
> For $\mathbb{Z}/2$: a free resolution is $0 \to \mathbb{Z} \xrightarrow{2} \mathbb{Z} \to 0$. Tensor with $\mathbb{Z}/2$: $\mathbb{Z}/2 \xrightarrow{0} \mathbb{Z}/2$. Read off $H_0 = \mathbb{Z}/2$, $H_1 = \mathbb{Z}/2$.

---

# Solution

The route is: (1) recognize cofibrant replacement $=$ projective resolution; (2) compute $\otimes^{\mathbf{L}}_R$ by replacing $M$ only, justified by exactness of $P_\bullet \otimes_R -$; (3) identify $H_n$ with $\mathrm{Tor}^R_n$ by definition; (4) run the $\mathbb{Z}/2$ example and contrast with the naive tensor.

**Step 1: Cofibrant replacement of $M$ is a projective resolution.**

> [!note]- Derivation
> In the projective model structure on $\mathbf{Ch}(R)$, a [[Def - Cofibrant and Fibrant Objects|cofibrant replacement]] of the module $M$ (a complex in degree $0$) is a quasi-isomorphism $QM \xrightarrow{\sim} M$ with $QM$ cofibrant. A bounded-below complex of projectives is cofibrant, and a projective resolution $P_\bullet = (\cdots \to P_1 \to P_0 \to 0)$ with $P_\bullet \xrightarrow{\sim} M$ is exactly such a replacement. So $QM = P_\bullet$.

**Step 2: Only $M$ needs replacing; $\otimes^{\mathbf{L}}_R N = P_\bullet \otimes_R N$.**

> [!note]- Derivation
> By definition $M \otimes^{\mathbf{L}}_R N = QM \otimes_R QN = P_\bullet \otimes_R QN$. The functor $P_\bullet \otimes_R -$ is exact (each $P_i$ is projective, hence flat, so $P_i \otimes_R -$ is exact, and the total complex of an exact-in-each-row double complex preserves quasi-isomorphisms). Therefore the quasi-isomorphism $QN \xrightarrow{\sim} N$ induces a quasi-isomorphism $P_\bullet \otimes_R QN \xrightarrow{\sim} P_\bullet \otimes_R N$, so in $\mathrm{Ho}(\mathbf{Ch}(R))$,
> $$M \otimes^{\mathbf{L}}_R N \;\simeq\; P_\bullet \otimes_R N.$$
> This one-sidedness is licensed by [[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal|the well-definedness theorem]]: the derived tensor does not depend on which factor (or how many) you replace, as long as enough is cofibrant for the tensor to be homotopical.

**Step 3: The homology is $\mathrm{Tor}$.**

> [!note]- Derivation
> Taking homology, $H_n(M \otimes^{\mathbf{L}}_R N) = H_n(P_\bullet \otimes_R N)$. By the classical definition, $\mathrm{Tor}^R_n(M, N) = H_n(P_\bullet \otimes_R N)$ for any projective resolution $P_\bullet$ of $M$ (independent of the resolution, by the comparison theorem for resolutions — which is the homological shadow of well-definedness of $\otimes^{\mathbf{L}}$). Hence
> $$H_n(M \otimes^{\mathbf{L}}_R N) = \mathrm{Tor}^R_n(M, N).$$

**Step 4: The example $\mathbb{Z}/2 \otimes^{\mathbf{L}}_{\mathbb{Z}} \mathbb{Z}/2$.**

> [!note]- Derivation
> A free resolution of $\mathbb{Z}/2$ over $\mathbb{Z}$ is $P_\bullet = (0 \to \mathbb{Z} \xrightarrow{\,2\,} \mathbb{Z} \to 0)$, in degrees $1$ and $0$. Tensor with $\mathbb{Z}/2$:
> $$P_\bullet \otimes_{\mathbb{Z}} \mathbb{Z}/2 = \big(0 \to \mathbb{Z}/2 \xrightarrow{\,2 = 0\,} \mathbb{Z}/2 \to 0\big),$$
> since multiplication by $2$ is the zero map on $\mathbb{Z}/2$. The homology is $H_0 = \mathbb{Z}/2$ (cokernel of $0$) and $H_1 = \mathbb{Z}/2$ (kernel of $0$). So $\mathrm{Tor}^{\mathbb{Z}}_0(\mathbb{Z}/2, \mathbb{Z}/2) = \mathbb{Z}/2$ and $\mathrm{Tor}^{\mathbb{Z}}_1(\mathbb{Z}/2, \mathbb{Z}/2) = \mathbb{Z}/2$. The **naive** tensor $\mathbb{Z}/2 \otimes_{\mathbb{Z}} \mathbb{Z}/2 \cong \mathbb{Z}/2$ is concentrated in degree $0$ and equals only $\mathrm{Tor}_0$; it misses the $\mathrm{Tor}_1$ entirely. This is exactly the failure of the naive tensor to be homotopy-invariant that motivated the chapter, and the derived tensor's degree-$1$ homology is the obstruction.

> [!note]- Complete formal solution
> In $\mathbf{Ch}(R)$ with the projective model structure, [[Def - Cofibrant and Fibrant Objects|cofibrant replacement]] of a module $M$ is a projective resolution $P_\bullet \xrightarrow{\sim} M$. By [[Thm - The Homotopy Category of a Monoidal Model Category is Monoidal|the derived-monoidal theorem]], $M \otimes^{\mathbf{L}}_R N = QM \otimes_R QN$. Since $P_\bullet \otimes_R -$ is exact (each $P_i$ flat), it preserves the quasi-isomorphism $QN \xrightarrow{\sim} N$, so $M \otimes^{\mathbf{L}}_R N \simeq P_\bullet \otimes_R N$. Taking homology, $H_n(M \otimes^{\mathbf{L}}_R N) = H_n(P_\bullet \otimes_R N) = \mathrm{Tor}^R_n(M, N)$ by definition. For $R = \mathbb{Z}$, $M = N = \mathbb{Z}/2$, the resolution $0 \to \mathbb{Z}\xrightarrow{2}\mathbb{Z}\to 0$ tensored with $\mathbb{Z}/2$ gives $0 \to \mathbb{Z}/2 \xrightarrow{0} \mathbb{Z}/2 \to 0$, whence $\mathrm{Tor}_0 = \mathrm{Tor}_1 = \mathbb{Z}/2$; the naive tensor $\mathbb{Z}/2 \otimes_{\mathbb{Z}} \mathbb{Z}/2 = \mathbb{Z}/2$ recovers only $\mathrm{Tor}_0$. $\qquad\blacksquare$

---

# Key Takeaways

**The derived tensor *is* Tor, and this identification is the Rosetta stone between model-category language and homological algebra.** Everything abstract in this chapter — cofibrant replacement, the pushout-product axiom, the well-definedness of $\otimes^{\mathbf{L}}$ — translates, in $\mathbf{Ch}(R)$, into the familiar apparatus of projective resolutions and Tor. The transferable lesson is that "derived functor" in homological algebra and "total left derived functor of a left Quillen functor" in model categories are the *same notion*, with projective resolution being the special case of cofibrant replacement. Whenever you meet a derived functor, you may compute it by cofibrant (or fibrant) replacement; whenever you meet cofibrant replacement, expect it to specialize to a resolution you already know.

**Replace only as much as you must, and justify the asymmetry by exactness — this is the practical core of computing derived functors.** The exercise shows you need not replace both factors: because $P_\bullet \otimes_R -$ is exact, replacing $M$ suffices. The trigger-reaction pattern: to compute a derived tensor (or any derived bifunctor), cofibrantly replace one variable, then check whether the resulting functor is already exact in the other variable — if so, leave the second variable alone. This is why the classical definition of $\mathrm{Tor}$ resolves only one factor and still gets a balanced, symmetric answer; the balancing is the homotopical well-definedness, and the one-sided computation is the efficient route. The same discipline computes Ext (resolve the source projectively or the target injectively), hyper-Tor, and derived smash products.

**$\mathrm{Tor}_1$ is the visible obstruction to the naive tensor being homotopy-invariant — the example $\mathbb{Z}/2 \otimes^{\mathbf{L}} \mathbb{Z}/2$ is the whole chapter in miniature.** The naive tensor of $\mathbb{Z}/2$ with itself sees only $\mathrm{Tor}_0$; the derived tensor's extra degree-$1$ homology, $\mathrm{Tor}_1 = \mathbb{Z}/2$, is exactly the information lost by not resolving. This single computation explains *why* the chapter exists: $\otimes$ is not homotopy-invariant, the failure is measured by higher Tor, and $\otimes^{\mathbf{L}}$ is the repair. The reusable diagnostic: whenever a tensor (or any functor) gives "too small" an answer on a non-cofibrant object, suspect that the higher derived functors are hiding the missing information, and resolve to expose them. See also [[Ex - Monoids in chain complexes are differential graded algebras]] and [[Ex - The derived tensor is well-defined independent of replacement]].
