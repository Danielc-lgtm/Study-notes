---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - The I-adic Completion"
  - "Def - Noetherian Ring"
  - "Def - Local Ring and Residue Field"
  - "Def - Finitely Generated Module"
tags: [algebra, commutative-algebra]
---

# Problem Statement

*(Becker Example Sheet 4, Q15.)* Let $M$ be an $R$-module and $\mathfrak{a}\trianglelefteq R$ an ideal, with [[Def - The I-adic Completion|completion map]] $\varphi:M\to\widehat{M}=\varprojlim_n M/\mathfrak{a}^n M$.

1. **(Kernel.)** Show that $\ker\varphi=\bigcap_{n\geq0}\mathfrak{a}^n M$.
2. **(Injectivity.)** Assume $R$ is [[Def - Noetherian Ring|Noetherian]] and [[Def - Local Ring and Residue Field|local]], $M$ is [[Def - Finitely Generated Module|finitely generated]] over $R$, and $\mathfrak{a}$ is a proper ideal. Prove that $\varphi$ is injective. *(The same holds if $R$ is a Noetherian integral domain, not necessarily local.)*

The crux of part 2 is the [[Thm - The Krull Intersection Theorem|Krull intersection theorem]]: under these hypotheses $\bigcap_n\mathfrak{a}^n M=0$, which by part 1 is exactly $\ker\varphi=0$. The lever for Krull is the [[Thm - The Artin-Rees Lemma|Artin–Rees lemma]], which produces an element of $1+\mathfrak{a}$ annihilating the intersection.

**Recall:**

![[Def - The I-adic Completion#The Definition]]

The completion map is $\varphi:M\to\widehat{M}$, $m\mapsto(m+\mathfrak{a}^n M)_n$.

![[Def - Noetherian Ring#The Definition]]

A ring is [[Def - Noetherian Ring|Noetherian]] if every ideal is finitely generated, equivalently every ascending chain of ideals stabilises. Over a Noetherian ring, submodules of finitely generated modules are finitely generated.

![[Def - Local Ring and Residue Field#The Definition]]

In a [[Def - Local Ring and Residue Field|local ring]] $(R,\mathfrak{m})$, the maximal ideal $\mathfrak{m}$ is the Jacobson radical, so $1+a$ is a unit for every $a\in\mathfrak{m}$; if $\mathfrak{a}$ is proper then $\mathfrak{a}\subseteq\mathfrak{m}$, so $1+a$ is a unit for every $a\in\mathfrak{a}$.

---

# Convergent Strategy

**Problem class.** This is the chapter's signature *prove-the-completion-map-is-injective* problem. As the [[Commutative Algebra X — Completions and Limits#Problem-Solving Strategy|topic strategy]] records, injectivity is a two-step descent: first write the kernel as $\bigcap_n\mathfrak{a}^n M$ (automatic), then show this vanishes via Krull intersection, whose hypotheses you verify.

**Assumption pattern.** The trigger is *"is $\varphi$ injective?"*, which immediately becomes *"is $\bigcap_n\mathfrak{a}^n M=0$?"*. The hypotheses Noetherian + local + f.g. + proper $\mathfrak{a}$ are *exactly* Krull's hypotheses, repackaged: Noetherian unlocks Artin–Rees, local makes $\mathfrak{a}$ sit in the Jacobson radical (so $1+\mathfrak{a}\subseteq R^\times$), and f.g. makes the intersection a finitely generated module on which the determinant trick / Nakayama can act.

**Theorem routing.** The route is: (1) read off $\ker\varphi=\bigcap_n\mathfrak{a}^n M$ from the inverse-limit definition ([[Thm - The Inverse Limit and Completeness|kernel formula]]); (2) set $I=\bigcap_n\mathfrak{a}^n M$ and apply [[Thm - The Artin-Rees Lemma|Artin–Rees]] to the submodule $I\subseteq M$ to get $\mathfrak{a}I=I$; (3) conclude $I=0$ by the standard "$(1+a)I=0$ for some $a\in\mathfrak{a}$, and $1+a$ is a unit (local) or non-zero in a domain". This is the proof of the [[Thm - The Krull Intersection Theorem|Krull intersection theorem]].

**Key decision point.** The non-obvious step is producing $\mathfrak{a}I=I$ from Artin–Rees. One has trivially $\mathfrak{a}I\subseteq I$; the reverse $I\subseteq\mathfrak{a}I$ is where Artin–Rees does its work: applying it to $I\subseteq M$ gives $I=I\cap\mathfrak{a}^n M=\mathfrak{a}^{n-c}(I\cap\mathfrak{a}^c M)\subseteq\mathfrak{a}I$ for large $n$, because $I\subseteq\mathfrak{a}^n M$ for all $n$. Recognising that the intersection $I$ "absorbs a factor of $\mathfrak{a}$" is the whole engine; the rest is Nakayama.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra X — Completions and Limits#Legal Operations|the topic page's Legal Operations]]:

1. **Compute the kernel of completion (operation 5).** $\ker\varphi=\bigcap_n\mathfrak{a}^n M$, read off the inverse-limit definition.

2. **Apply Krull intersection (operation 6).** Over a Noetherian local ring with $\mathfrak{a}$ proper and $M$ f.g., $\bigcap_n\mathfrak{a}^n M=0$.

3. **Transport finiteness through the safety package (operation 7).** $R$ Noetherian makes the intersection $I$ finitely generated (a submodule of f.g. $M$), so the determinant trick applies.

---

# Hints

> [!note]- Hint 1
> An element of $\widehat{M}$ is a thread; $\varphi(m)$ is the thread of truncations of $m$. When is it the zero thread? Each coordinate $m+\mathfrak{a}^n M$ must be $0$, i.e. $m\in\mathfrak{a}^n M$ — for *every* $n$.

> [!note]- Hint 2
> So $\ker\varphi=\bigcap_n\mathfrak{a}^n M=:I$. Injectivity is exactly $I=0$. To kill $I$, show it absorbs a factor of $\mathfrak{a}$: $\mathfrak{a}I=I$.

> [!note]- Hint 3
> Apply [[Thm - The Artin-Rees Lemma|Artin–Rees]] to the submodule $I\subseteq M$: there is $c$ with $I\cap\mathfrak{a}^n M=\mathfrak{a}^{n-c}(I\cap\mathfrak{a}^c M)$ for $n\geq c$. But $I\subseteq\mathfrak{a}^n M$ for all $n$, so $I\cap\mathfrak{a}^n M=I$. Read off $I=\mathfrak{a}^{n-c}(\cdots)\subseteq\mathfrak{a}I$, hence $\mathfrak{a}I=I$.

> [!note]- Hint 4
> From $\mathfrak{a}I=I$ with $I$ finitely generated, the determinant trick (Cayley–Hamilton for modules) gives $a\in\mathfrak{a}$ with $(1+a)I=0$. In a local ring with $\mathfrak{a}\subseteq\mathfrak{m}$, $1+a$ is a unit, so $I=0$. (In a domain, $1+a\neq0$ and there are no zero-divisors, so $I=0$.)

---

# Solution

The proof is the two-step descent: the kernel is the infinite intersection (definitional), and the intersection vanishes by Artin–Rees plus the determinant trick — the Krull intersection theorem. The hypotheses are exactly what Krull needs.

**Step 1: $\ker\varphi=\bigcap_n\mathfrak{a}^n M$.**

> [!note]- Derivation
> By definition $\varphi(m)=(m+\mathfrak{a}^n M)_n\in\varprojlim M/\mathfrak{a}^n M$, and the zero element of the inverse limit is the thread all of whose coordinates vanish. So
> $$\varphi(m)=0\iff m+\mathfrak{a}^n M=0\ \text{in}\ M/\mathfrak{a}^n M\ \text{for all }n\iff m\in\mathfrak{a}^n M\ \text{for all }n\iff m\in\bigcap_{n\geq0}\mathfrak{a}^n M.$$
> Hence $\ker\varphi=\bigcap_{n\geq0}\mathfrak{a}^n M$. This part needs no hypotheses on $R$ or $M$. In particular $\varphi$ is injective iff $\bigcap_n\mathfrak{a}^n M=0$.

**Step 2: The intersection absorbs a factor of $\mathfrak{a}$ (Artin–Rees).**

Set $I=\bigcap_n\mathfrak{a}^n M$. Then $\mathfrak{a}I=I$.

> [!note]- Derivation
> The inclusion $\mathfrak{a}I\subseteq I$ is immediate ($I$ is a submodule and $\mathfrak{a}I\subseteq\mathfrak{a}\cdot\mathfrak{a}^n M=\mathfrak{a}^{n+1}M\subseteq\mathfrak{a}^n M$ for all $n$, so $\mathfrak{a}I\subseteq\bigcap\mathfrak{a}^n M=I$).
>
> For the reverse, apply the [[Thm - The Artin-Rees Lemma|Artin–Rees lemma]] to the submodule $I\subseteq M$ over the Noetherian ring $R$ with the $\mathfrak{a}$-adic filtration: there is an integer $c\geq0$ such that
> $$I\cap\mathfrak{a}^n M=\mathfrak{a}^{n-c}\big(I\cap\mathfrak{a}^c M\big)\qquad\text{for all }n\geq c.$$
> Now $I\subseteq\mathfrak{a}^n M$ for *every* $n$ (that is the definition of $I$), so $I\cap\mathfrak{a}^n M=I$ and $I\cap\mathfrak{a}^c M=I$. Substituting with $n=c+1$,
> $$I=\mathfrak{a}^{(c+1)-c}\big(I\cap\mathfrak{a}^c M\big)=\mathfrak{a}\cdot I.$$
> Hence $\mathfrak{a}I=I$.

**Step 3: $I=0$ (determinant trick / Nakayama).**

> [!note]- Derivation
> Since $R$ is Noetherian and $I\subseteq M$ with $M$ finitely generated, $I$ is finitely generated. From $\mathfrak{a}I=I$ — i.e. $I=\mathfrak{a}I$ — the **determinant trick** (Cayley–Hamilton for modules: if a f.g. module $I$ satisfies $I=\mathfrak{a}I$, there is $a\in\mathfrak{a}$ with $(1+a)I=0$) yields $a\in\mathfrak{a}$ with
> $$(1+a)\,I=0.$$
> *Local case.* Since $\mathfrak{a}$ is proper, $\mathfrak{a}\subseteq\mathfrak{m}$, and $\mathfrak{m}=\mathrm{Jac}(R)$ in a local ring, so $1+a$ is a unit. Multiplying $(1+a)I=0$ by $(1+a)^{-1}$ gives $I=0$.
>
> *Domain case.* If $R$ is a Noetherian domain and $\mathfrak{a}$ proper, then $a\in\mathfrak{a}\neq R$ so $1+a\neq0$; as $R$ is a domain and $(1+a)I=0$ with $1+a\neq0$, every element of $I$ is annihilated by a non-zero ring element, forcing $I=0$.
>
> In both cases $\bigcap_n\mathfrak{a}^n M=I=0$, so by Step 1 $\ker\varphi=0$ and $\varphi$ is injective.

> [!note]- Complete formal solution
> **(1)** $\varphi(m)=(m+\mathfrak{a}^n M)_n$ is the zero thread iff $m\in\mathfrak{a}^n M$ for all $n$, so $\ker\varphi=\bigcap_n\mathfrak{a}^n M$.
>
> **(2)** Let $I=\bigcap_n\mathfrak{a}^n M$. By [[Thm - The Artin-Rees Lemma|Artin–Rees]] applied to $I\subseteq M$, there is $c$ with $I\cap\mathfrak{a}^n M=\mathfrak{a}^{n-c}(I\cap\mathfrak{a}^c M)$ for $n\geq c$; since $I\subseteq\mathfrak{a}^n M$ always, $I\cap\mathfrak{a}^n M=I$, giving $I=\mathfrak{a}I$. As $R$ is Noetherian and $M$ f.g., $I$ is f.g.; the determinant trick gives $a\in\mathfrak{a}$ with $(1+a)I=0$. In the local case $1+a$ is a unit (as $\mathfrak{a}\subseteq\mathfrak{m}=\mathrm{Jac}(R)$), so $I=0$; in the domain case $1+a\neq0$ and $R$ has no zero-divisors, so $I=0$. Hence $\ker\varphi=I=0$ and $\varphi$ is injective. $\blacksquare$

> [!warning] Illegal but tempting: concluding injectivity without the hypotheses
> It is tempting to declare $\varphi$ injective for any ring, by analogy with $\mathbb{Z}\hookrightarrow\mathbb{Z}_p$. But Step 3 *needs* Noetherian (for Artin–Rees and finite generation) and *needs* $1+a$ invertible-or-non-zero (local or domain). Drop these and the intersection can be non-zero: in $R=k[x_1,x_2,\dots]/(x_i-x_{i+1}x_i)$ or in a non-Noetherian ring with $\mathfrak{a}^2=\mathfrak{a}$, one finds $0\neq m\in\bigcap\mathfrak{a}^n M$. The repair is precisely the four hypotheses of Krull. Concretely, without local/domain, $(1+a)I=0$ does *not* force $I=0$ because $1+a$ might be a non-unit zero-divisor.

---

# Key Takeaways

**Injectivity of completion is a two-step descent: kernel = infinite intersection, intersection = zero by Krull.** The structure of this proof is the template for every "is $\varphi$ injective?" question. Step one is free — the kernel formula $\ker\varphi=\bigcap_n\mathfrak{a}^n M$ is just the inverse-limit definition. Step two is the entire content — showing the intersection vanishes — and it is the [[Thm - The Krull Intersection Theorem|Krull intersection theorem]], whose hypotheses (Noetherian, f.g., $\mathfrak{a}$ in the radical or domain) you must verify. The trigger to internalise: "completion injective" reduces instantly to "$\bigcap\mathfrak{a}^n M=0$", and the latter is Krull. When the hypotheses hold the answer is yes; when any fails, hunt for an infinitely-$\mathfrak{a}$-divisible element instead of assuming injectivity.

**The intersection $\bigcap\mathfrak{a}^n M$ absorbs a factor of $\mathfrak{a}$ — that is what Artin–Rees buys you, and Nakayama finishes.** The genuinely clever step is $\mathfrak{a}I=I$, and it comes from feeding the submodule $I$ (which lies in *every* $\mathfrak{a}^n M$) into Artin–Rees: the induced filtration on $I$ is the constant filtration $I$, so the Artin–Rees identity collapses to $I=\mathfrak{a}I$. Then the determinant trick (the same Cayley–Hamilton mechanism behind Nakayama) produces $a\in\mathfrak{a}$ with $(1+a)I=0$, and locality/domain makes $1+a$ killable. The transferable diagnostic: whenever you have a module equal to $\mathfrak{a}$ times itself, $M=\mathfrak{a}M$, reach for the determinant trick — it forces $M=0$ exactly when $1+\mathfrak{a}$ avoids zero-divisors, which is Nakayama's hypothesis. This single move — "$M=\mathfrak{a}M\Rightarrow M=0$" — underlies Nakayama, Krull intersection, and the injectivity of completion.

**The four hypotheses of Krull are not redundant — each blocks a specific failure of infinite divisibility.** Noetherian is needed for Artin–Rees (the absorption step) and for finite generation of $I$ (the determinant trick); local-or-domain is needed to make $1+a$ killable. Removing any one allows a non-zero element divisible by every power of $\mathfrak{a}$, and completion then collapses part of $M$. The diagnostic for spaced practice: if a completion problem misbehaves, check whether one of these hypotheses was quietly lost — most often by passing to a non-finitely-generated module or a non-Noetherian ring. This connects to the topic page's [[Commutative Algebra X — Completions and Limits#Insights|insight]] that "Noetherian is non-negotiable" — every good property of completion (injectivity, Noetherianity, exactness) flows through Artin–Rees, which is only true over a Noetherian ring. The companion exercise [[Ex - The p-adic integers as an inverse limit]] does this vanishing by hand (finite $p$-adic valuation) in the simplest case.
