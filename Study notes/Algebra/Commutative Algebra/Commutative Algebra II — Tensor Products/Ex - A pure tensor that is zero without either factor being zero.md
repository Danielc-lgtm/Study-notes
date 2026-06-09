---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Tensor Product of Modules"
  - "Def - Bilinear and Multilinear Maps"
  - "Thm - Universal Property of the Tensor Product of Modules"
  - "Def - Submodule"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Work over $R = \mathbb{Z}$.

**(a)** Show that in $\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/2$ the pure tensor $2\otimes\bar1$ equals $0$, even though $2\neq 0$ in $\mathbb{Z}$ and $\bar1\neq 0$ in $\mathbb{Z}/2$.

**(b)** Show that in the *different* tensor product $(2\mathbb{Z})\otimes_{\mathbb{Z}}\mathbb{Z}/2$, the symbol $2\otimes\bar1$ is **nonzero**, by constructing a single $\mathbb{Z}$-bilinear map that does not kill it.

**(c)** Conclude that "$m\otimes n = 0$" is not a property of the symbols $m, n$ alone — it depends on the ambient modules $M, N$ — and that vanishing of a tensor is *not* inherited from a submodule: $(2\mathbb{Z})\otimes\mathbb{Z}/2$ is **not** a submodule of $\mathbb{Z}\otimes\mathbb{Z}/2$ in any natural way. State which direction *does* always work.

**Recall:**

![[Def - Tensor Product of Modules#The Definition]]

The relations used are $r(m\otimes n) = (rm)\otimes n = m\otimes(rn)$. The key tool for non-vanishing is the [[Thm - Universal Property of the Tensor Product of Modules|vanishing criterion]]: $\sum_i m_i\otimes n_i = 0$ in $M\otimes N$ **iff** $\sum_i f(m_i, n_i) = 0$ for every $R$-module $L$ and every $R$-bilinear $f : M\times N\to L$. So a tensor is nonzero as soon as *one* bilinear map fails to kill it.

![[Def - Bilinear and Multilinear Maps#Bilinear map]]

Here $2\mathbb{Z} = \{2x : x\in\mathbb{Z}\}\leq\mathbb{Z}$ is the [[Def - Submodule|submodule]] of even integers; as a $\mathbb{Z}$-module it is free of rank $1$ on the generator $2$, so its elements are uniquely $2x$ with $x\in\mathbb{Z}$.

---

# Convergent Strategy

**Problem class.** This is a *decide-whether-a-tensor-vanishes* problem, and it is the canonical warning that vanishing is two-sided and ring-dependent. As the [[Commutative Algebra II — Tensor Products#Problem-Solving Strategy|topic strategy]] records, proving a tensor zero is an *inside* computation (slide scalars to collapse), while proving it nonzero is an *outside* construction (exhibit one surviving bilinear map) — and this exercise does both for the *same symbol* in two different tensor products.

**Assumption pattern.** The trigger in (a) is *a scalar that can be slid onto a factor where it dies*: in $\mathbb{Z}\otimes\mathbb{Z}/2$, the $2$ in $2\otimes\bar1$ can be moved across to give $\bar2 = 0$. The trigger in (b) is the *failure of that move*: in $2\mathbb{Z}$, you cannot factor $2 = 2\cdot 1$ legally because $1\notin 2\mathbb{Z}$, so the collapse argument is blocked, signalling that the tensor might survive — which you then confirm by building a bilinear map.

**Theorem routing.** Part (a): slide the scalar, $2\otimes\bar1 = 1\otimes\overline{2} = 1\otimes\bar0 = 0$. Part (b): build $b : 2\mathbb{Z}\times\mathbb{Z}/2\to\mathbb{Z}/2$, $b(2x, \bar y) = \overline{xy}$, check it is well-defined and bilinear, and evaluate $b(2, \bar1) = \bar1\neq 0$; by the [[Thm - Universal Property of the Tensor Product of Modules|vanishing criterion]], $2\otimes\bar1\neq 0$. Part (c): the two computations differ only in the ambient module, so vanishing is ambient-dependent; and the collapse in (a) used $2 = 2\cdot 1$ with $1\in\mathbb{Z}$, illegal in $2\mathbb{Z}$.

**Key decision point.** The crux is in (b): *the bilinear map must use the generator $2$ of $2\mathbb{Z}$ as a unit of measurement*. The well-definedness of $b(2x, \bar y) = \overline{xy}$ rests on $2\mathbb{Z}$ being free on $2$, so every element is uniquely $2x$ and $x$ is well-defined. The non-obvious recognition is that the collapse in (a) is *exactly the step that fails* in (b): in $\mathbb{Z}\otimes\mathbb{Z}/2$ one writes $2\otimes\bar1 = 2(1\otimes\bar1) = (1\otimes 2\bar1)$, using $1\in\mathbb{Z}$ to "halve" the $2$; inside $2\mathbb{Z}$ there is no $1$, so the $2$ cannot be pulled out, and the tensor survives. Seeing that the *same algebraic move* is licensed in one module and forbidden in the other is the whole lesson.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra II — Tensor Products#Legal Operations|the topic page's Legal Operations]]:

1. **Slide scalars across the $\otimes$ (operation 1).** In (a), $2\otimes\bar1 = 1\otimes\overline{2} = 0$ — slide the $2$ onto $\mathbb{Z}/2$ where it dies.

2. **Certify a tensor nonzero with one bilinear map (operation 3).** In (b), the map $b(2x,\bar y) = \overline{xy}$ survives $2\otimes\bar1$, so it is nonzero.

3. **Replace a bilinear map by a linear map out of the tensor product (operation 2).** The vanishing criterion is the universal property applied to certify non-vanishing.

4. **Awareness of illegal-operation 2 (reading $m\otimes n = 0$ without naming the tensor product).** Part (c) is exactly this warning made precise.

---

# Hints

> [!note]- Hint 1
> For (a), the $2$ in $2\otimes\bar1$ is a $\mathbb{Z}$-scalar times $1\otimes\bar1$. Slide it onto the *second* factor: $2\otimes\bar1 = 2(1\otimes\bar1) = 1\otimes(2\cdot\bar1) = 1\otimes\overline{2}$. What is $\overline2$ in $\mathbb{Z}/2$?

> [!note]- Hint 2
> For (b), the collapse in (a) used $2 = 2\cdot 1$ with $1\in\mathbb{Z}$. But in $2\mathbb{Z}$, $1\notin 2\mathbb{Z}$ — you cannot pull a $2$ out of the generator. So the collapse is blocked. To *prove* the tensor is nonzero, build a bilinear map that doesn't kill it.

> [!note]- Hint 3
> Try $b : 2\mathbb{Z}\times\mathbb{Z}/2\to\mathbb{Z}/2$, $b(2x, \bar y) = \overline{xy}$. Every element of $2\mathbb{Z}$ is uniquely $2x$ (it is free on $2$), so $x$ is well-defined. Check $b$ is bilinear, then compute $b(2, \bar1)$ (here $2 = 2\cdot 1$, so $x = 1$).

> [!note]- Hint 4
> $b(2,\bar1) = \overline{1\cdot 1} = \bar1\neq 0$. By the vanishing criterion, $2\otimes\bar1\neq 0$ in $2\mathbb{Z}\otimes\mathbb{Z}/2$. Compare with (a): same symbol, different tensor product, different answer — so vanishing depends on the ambient modules. Which direction (sub-to-big or big-to-sub) always preserves vanishing?

---

# Solution

The proof collapses the tensor in one module and certifies it nonzero in the other, then draws the moral. Step 1 (a) slides the scalar to get $0$. Step 2 (b) builds the surviving bilinear map. Step 3 (c) extracts the lesson and the one-directional inheritance. The non-obvious thread is that the collapse move of Step 1 is precisely what is illegal in Step 2's module.

**Step 1 (a): $2\otimes\bar1 = 0$ in $\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/2$.**

Slide the scalar $2$ onto $\mathbb{Z}/2$, where $\overline2 = 0$.

> [!note]- Derivation
> Using $r(m\otimes n) = (rm)\otimes n = m\otimes(rn)$ with $r = 2$, $m = 1\in\mathbb{Z}$, $n = \bar1\in\mathbb{Z}/2$:
> $$2\otimes\bar1 = 2(1\otimes\bar1) = 1\otimes(2\cdot\bar1) = 1\otimes\overline{2} = 1\otimes\bar0 = 0,$$
> since $\overline2 = 0$ in $\mathbb{Z}/2$ and $m\otimes 0 = 0$. So $2\otimes\bar1 = 0$ in $\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/2$, even though $2\neq 0$ and $\bar1\neq 0$. (This step crucially writes the first factor as $2 = 2\cdot 1$ with $1\in\mathbb{Z}$, then moves the $2$ across.)

**Step 2 (b): $2\otimes\bar1\neq 0$ in $(2\mathbb{Z})\otimes_{\mathbb{Z}}\mathbb{Z}/2$.**

The bilinear map $b(2x, \bar y) = \overline{xy}$ sends $2\otimes\bar1$ to $\bar1\neq 0$.

> [!note]- Derivation
> Every element of $2\mathbb{Z}$ is uniquely $2x$ with $x\in\mathbb{Z}$ (as $2\mathbb{Z}$ is [[Def - Free Module|free]] of rank $1$ on $2$). Define
> $$b : 2\mathbb{Z}\times\mathbb{Z}/2\to\mathbb{Z}/2, \qquad b(2x, \bar y) = \overline{xy}.$$
> *Well-defined.* $x$ is determined by $2x$ (uniqueness of the coefficient), and $\overline{xy}$ depends only on $\bar y$: if $\bar y = \bar y'$ then $y\equiv y'\pmod2$, so $xy\equiv xy'\pmod 2$. So $b$ is unambiguous.
>
> *Bilinear.* In the first slot, $b(2x + 2x', \bar y) = b(2(x+x'),\bar y) = \overline{(x+x')y} = \overline{xy}+\overline{x'y}$, and $b(r\cdot 2x, \bar y) = b(2(rx),\bar y) = \overline{rxy} = r\,\overline{xy}$ for $r\in\mathbb{Z}$; in the second slot, $b(2x, \bar y+\bar y') = \overline{x(y+y')} = \overline{xy}+\overline{xy'}$ and $b(2x, r\bar y) = \overline{x(ry)} = r\overline{xy}$. So $b$ is $\mathbb{Z}$-bilinear.
>
> *Survives.* $b(2, \bar1) = b(2\cdot 1, \bar1) = \overline{1\cdot 1} = \bar1\neq 0$. By the [[Thm - Universal Property of the Tensor Product of Modules|vanishing criterion]], since one bilinear map has $b(2,\bar1)\neq 0$, the tensor $2\otimes\bar1\neq 0$ in $(2\mathbb{Z})\otimes_{\mathbb{Z}}\mathbb{Z}/2$.
>
> *Why the collapse of Step 1 fails here.* In Step 1 we wrote $2\otimes\bar1 = 2(1\otimes\bar1)$, pulling a $2$ out of the first factor as $2 = 2\cdot 1$. Inside $2\mathbb{Z}$ the element "$1$" does not exist ($1\notin 2\mathbb{Z}$), so $2$ cannot be written as $2$ times an element of $2\mathbb{Z}$; the move that killed the tensor in $\mathbb{Z}$ is simply not available in $2\mathbb{Z}$. (Indeed $(2\mathbb{Z})\otimes_{\mathbb{Z}}\mathbb{Z}/2\cong\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/2\cong\mathbb{Z}/2$ via $2x\mapsto x$, and $2\otimes\bar1$ is the nonzero generator.)

**Step 3 (c): The moral and the one-directional inheritance.**

Vanishing depends on the ambient modules; only "submodule $\Rightarrow$ ambient" preserves it.

> [!note]- Derivation
> The *same symbol* $2\otimes\bar1$ is $0$ in $\mathbb{Z}\otimes\mathbb{Z}/2$ but nonzero in $(2\mathbb{Z})\otimes\mathbb{Z}/2$. So "$m\otimes n = 0$" is **not** a property of $m, n$ alone — it is a statement *about the ambient tensor product*, determined by $M$, $N$, and $R$. In particular it is **wrong** to view $(2\mathbb{Z})\otimes_{\mathbb{Z}}\mathbb{Z}/2$ as a submodule of $\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/2$: the natural map $(2\mathbb{Z})\otimes\mathbb{Z}/2\to\mathbb{Z}\otimes\mathbb{Z}/2$ induced by the inclusion $2\mathbb{Z}\hookrightarrow\mathbb{Z}$ sends $2\otimes\bar1\mapsto 0$ — it is **not injective** (it kills the nonzero generator). This is the [[Thm - Functoriality of the Tensor Product|failure of injectivity]] of $\iota\otimes\operatorname{id}$ in action.
>
> *The direction that always works.* If $M'\leq M$, $N'\leq N$ are submodules and $\sum_i m_i\otimes n_i = 0$ in $M'\otimes N'$, then $\sum_i m_i\otimes n_i = 0$ in $M\otimes N$ as well — applying the inclusion-induced map $M'\otimes N'\to M\otimes N$ sends $0\mapsto 0$. So vanishing in the *smaller* tensor product forces vanishing in the *larger* (going up). What fails is the converse: vanishing in $M\otimes N$ need not imply vanishing in $M'\otimes N'$, exactly as $2\otimes\bar1$ shows.

> [!note]- Complete formal solution
> **(a)** $2\otimes\bar1 = 2(1\otimes\bar1) = 1\otimes\overline{2} = 1\otimes\bar0 = 0$ in $\mathbb{Z}\otimes_{\mathbb{Z}}\mathbb{Z}/2$, using $\overline2 = 0$.
>
> **(b)** In $(2\mathbb{Z})\otimes_{\mathbb{Z}}\mathbb{Z}/2$, define $b(2x,\bar y) = \overline{xy}$ ($x$ well-defined as $2\mathbb{Z}$ is free on $2$; bilinear by direct check). Then $b(2,\bar1) = \bar1\neq 0$, so by the vanishing criterion $2\otimes\bar1\neq 0$. The collapse of (a) needed $2 = 2\cdot1$ with $1\in\mathbb{Z}$, which is illegal in $2\mathbb{Z}$ since $1\notin 2\mathbb{Z}$.
>
> **(c)** The same symbol is $0$ in one tensor product and nonzero in the other, so vanishing depends on the ambient $M, N, R$; the inclusion-induced map $(2\mathbb{Z})\otimes\mathbb{Z}/2\to\mathbb{Z}\otimes\mathbb{Z}/2$ kills $2\otimes\bar1$ and is not injective, so $(2\mathbb{Z})\otimes\mathbb{Z}/2$ is not a submodule of $\mathbb{Z}\otimes\mathbb{Z}/2$. The direction that always holds: vanishing in $M'\otimes N'$ (submodules) implies vanishing in $M\otimes N$. $\blacksquare$

---

# Key Takeaways

**Vanishing of a tensor is a statement about the ambient modules, never about the symbols alone.** The single most important warning in the subject: $2\otimes\bar1$ has no meaning until you name the tensor product it lives in, and the *same symbols* give $0$ in $\mathbb{Z}\otimes\mathbb{Z}/2$ and a nonzero generator in $(2\mathbb{Z})\otimes\mathbb{Z}/2$. The trigger for spaced recall: whenever you write $m\otimes n$, *track which $M$, $N$, $R$ you are in*, and never carry a vanishing conclusion across a change of ambient module. This is the practical form of illegal-operation 2 on the [[Commutative Algebra II — Tensor Products#Legal Operations|topic page]], and it is the source of a large fraction of beginner errors — the symbols look stable but their meaning is not.

**To prove a tensor is zero, slide scalars; to prove it is nonzero, build one surviving bilinear map — and the collapse move that works in one module may be forbidden in another.** This exercise is the cleanest illustration of the two-sided method. The collapse $2\otimes\bar1 = 2(1\otimes\bar1) = 1\otimes\overline2 = 0$ relies on writing $2 = 2\cdot 1$ with $1\in\mathbb{Z}$; inside $2\mathbb{Z}$ that factorisation is unavailable, so the collapse is blocked and the tensor survives — certified by the bilinear map $b(2x,\bar y) = \overline{xy}$. The transferable diagnostic: when a scalar-sliding collapse seems to kill a tensor, *check that every factorisation you used is legal in the actual module* (no borrowing of $1$'s or inverses that the module lacks); if a needed factorisation is illegal, suspect the tensor is nonzero and construct the incriminating bilinear map. The construction technique — measure the generator (here $2$) against itself, using freeness — is the standard way to build surviving maps, and it reappears in [[Ex - Z mod m tensor Z mod n is Z mod gcd|the gcd computation]].

**Vanishing goes up but not down: $M'\otimes N'\to M\otimes N$ can kill things, because $\otimes$ does not preserve injections.** The structural lesson is that the inclusion $2\mathbb{Z}\hookrightarrow\mathbb{Z}$, tensored with $\operatorname{id}_{\mathbb{Z}/2}$, is *not injective* — it sends the nonzero $2\otimes\bar1$ to $0$. This is exactly the [[Thm - Functoriality of the Tensor Product|failure of injectivity]] under $\otimes$, here for an honest submodule inclusion rather than a multiplication map. So a tensor of submodules is *not* a submodule of the tensor: vanishing in the smaller object forces vanishing in the larger (functoriality sends $0\mapsto 0$), but not conversely. The diagnostic for spaced practice: never treat $M'\otimes N'$ as sitting inside $M\otimes N$; the natural map may have a kernel, and detecting that kernel is precisely the obstruction that **flatness** removes — a module $M$ is flat iff tensoring with it preserves *all* injections, including submodule inclusions. This single example is the concrete seed of the flatness theory in [[Commutative Algebra III — Flatness and Exactness]].
