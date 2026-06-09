---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Ring"
  - "Def - Ideal"
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Finitely Generated Module"
  - "Def - Noetherian Ring"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Throughout, $R$ is a ring, $\mathfrak{a} \trianglelefteq R$ an [[Def - Ideal|ideal]], and $M$ an [[Def - Module|R-module]]. A filtration of $M$ is a descending chain of [[Def - Submodule|submodules]] $M = M_0 \supseteq M_1 \supseteq M_2 \supseteq \cdots$, written $(M_n)_{n \geq 0}$. We write $\mathfrak{a}^n$ for the $n$-th power of the ideal (with $\mathfrak{a}^0 = R$), and $\mathfrak{a}^n M = \{\sum_i a_i m_i : a_i \in \mathfrak{a}^n, m_i \in M\}$ for the submodule it cuts out. The canonical example is the **$\mathfrak{a}$-adic filtration** $(\mathfrak{a}^n M)_{n \geq 0}$. The full registry is on [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma]].

This is a compound page: it defines three nested notions — a **filtration**, an **$\mathfrak{a}$-filtration**, and a **stable $\mathfrak{a}$-filtration** — because each refines the previous, and the entire force of the Artin–Rees lemma lives in the gap between the second and the third.

---

# Axiom Motivation

A filtration is a way of measuring "how deep an element sits" — how divisible it is, how close to zero it is, how high its order of vanishing. The integers near a prime $p$ furnish the picture: the chain $\mathbb{Z} \supseteq p\mathbb{Z} \supseteq p^2\mathbb{Z} \supseteq \cdots$ sorts each integer by how many times $p$ divides it, and saying "$x$ is small" means "$x \in p^n\mathbb{Z}$ for large $n$". The definitions on this page abstract that idea in three escalating steps, and the reason to escalate is that the crudest version is too weak to do analysis with, while the strongest version is exactly strong enough to control submodules — which is the Artin–Rees lemma.

**Step one: why a filtration is just a descending chain $M_0 \supseteq M_1 \supseteq \cdots$ with $M_0 = M$.** At its barest, "measuring depth" requires only that the levels are nested — deeper means a smaller set — and that level $0$ is everything. We do *not* yet ask the levels to interact with any ideal; a filtration in this raw sense is purely a way of saying which elements are "at least as deep as level $n$". The descending condition is what lets "depth" be a coherent grading-by-cumulative-membership: the function $\nu(x) = \sup\{n : x \in M_n\}$ (the order of $x$) is well-behaved only because the $M_n$ are nested. Drop the descending requirement and $\nu$ is meaningless. This bare notion is enough to define a topology — declaring the $M_n$ a neighbourhood basis of $0$ — but not enough to relate the topology to the ring, which is what we ultimately want.

**Step two: why an $\mathfrak{a}$-filtration adds $\mathfrak{a} M_n \subseteq M_{n+1}$.** The raw filtration ignores the ring; we now demand that multiplying by the chosen ideal $\mathfrak{a}$ pushes you *down* at least one level. The desideratum is that $\mathfrak{a}$ should act as a "shift operator" on depth: an element of $\mathfrak{a}$ is itself deep (it should sit in $M_1$ when applied to $M_0$), so multiplying a depth-$n$ element by something in $\mathfrak{a}$ should land in depth $\geq n+1$. This single axiom is what makes the associated graded object $\bigoplus M_n/M_{n+1}$ a *module over* the associated graded ring $\bigoplus \mathfrak{a}^n/\mathfrak{a}^{n+1}$: the action of a degree-one element $\bar{a} \in \mathfrak{a}/\mathfrak{a}^2$ on $\bar{x} \in M_n/M_{n+1}$ is $\overline{ax} \in M_{n+1}/M_{n+2}$, and this is well-defined precisely because $\mathfrak{a} M_n \subseteq M_{n+1}$. Without this compatibility the filtration and the ideal have nothing to say to each other. Note the inequality is one-sided: $\mathfrak{a} M_n \subseteq M_{n+1}$ allows multiplication by $\mathfrak{a}$ to over-shoot and land *much* deeper. The canonical $\mathfrak{a}$-adic filtration $(\mathfrak{a}^n M)$ obviously satisfies it, with equality $\mathfrak{a} \cdot \mathfrak{a}^n M = \mathfrak{a}^{n+1} M$.

**Step three: why stability demands $\mathfrak{a} M_n = M_{n+1}$ for all large $n$.** This is the crucial refinement and the one that pays for the Artin–Rees lemma. An $\mathfrak{a}$-filtration only requires $\mathfrak{a} M_n \subseteq M_{n+1}$; the filtration could spiral down arbitrarily faster than $\mathfrak{a}$ dictates, with $M_{n+1}$ a tiny submodule of $\mathfrak{a} M_n$. **Stable** means the filtration is, from some point on, *exactly* driven by $\mathfrak{a}$: each level is gotten from the previous by multiplying by $\mathfrak{a}$, with no extra collapse, so $M_{n+1} = \mathfrak{a} M_n$ for $n \gg 0$. The reason this is the right strength is a finiteness one: a stable $\mathfrak{a}$-filtration is, after the stabilization point $n_0$, *generated* from the single level $M_{n_0}$ by powers of $\mathfrak{a}$ — $M_{n_0 + r} = \mathfrak{a}^r M_{n_0}$ — so the whole infinite tower is finitely determined. Over a [[Def - Noetherian Ring|Noetherian ring]] this finiteness is exactly what makes the associated module $M^* = \bigoplus M_n$ finitely generated over the Rees algebra (see [[Thm - The Artin-Rees Lemma]]), and that finite generation is the engine of every result in the chapter. Why "for all *large* $n$" rather than "for all $n$"? Because the first few levels are allowed to be arbitrary — only the eventual behaviour matters for the topology and for finiteness — and this slack is exactly what lets the intersection $N \cap M_n$ of a submodule with a stable filtration be itself stable (it agrees with $\mathfrak{a}^n N$ only eventually, not from the start). Demanding stability from $n=0$ would be the rigid condition "$M_n = \mathfrak{a}^n M$ exactly", which submodule-intersections do not satisfy; the "large $n$" slack is what makes the class of stable filtrations *closed under the operations we need*.

**Why all stable filtrations are interchangeable.** The deepest reason to isolate stability is that any two stable $\mathfrak{a}$-filtrations of the same module are *equivalent* — each is sandwiched inside a finite shift of the other — and therefore induce the same topology (the same notion of "small") and the same completion. So "stable $\mathfrak{a}$-filtration" is not really a structure on $M$ but a property: the property of being eventually $\mathfrak{a}$-driven, and the canonical representative is always the $\mathfrak{a}$-adic filtration $(\mathfrak{a}^n M)$. This is why one can prove things about *a* stable filtration and conclude things about *the* $\mathfrak{a}$-adic one — they are the same up to a harmless finite reindexing. The precise statement is [[Thm - Stable Filtrations Induce the Same Topology]].

---

# The Definition

Let $R$ be a ring, $M$ an [[Def - Module|R-module]], and $\mathfrak{a} \trianglelefteq R$ an [[Def - Ideal|ideal]].

## Filtration

A **filtration** of $M$ is a sequence $(M_n)_{n \geq 0}$ of [[Def - Submodule|submodules]] of $M$ with
$$M_0 = M \qquad \text{and} \qquad M_n \supseteq M_{n+1} \ \text{ for all } n \geq 0,$$
i.e. a descending chain $M = M_0 \supseteq M_1 \supseteq M_2 \supseteq \cdots$ starting at $M$.

## $\mathfrak{a}$-filtration

A filtration $(M_n)_{n \geq 0}$ is an **$\mathfrak{a}$-filtration** if
$$\mathfrak{a} M_n \subseteq M_{n+1} \quad \text{for all } n \geq 0.$$

## Stable $\mathfrak{a}$-filtration

An $\mathfrak{a}$-filtration $(M_n)_{n \geq 0}$ is **stable** (or **$\mathfrak{a}$-stable**) if
$$\mathfrak{a} M_n = M_{n+1} \quad \text{for all sufficiently large } n,$$
that is, there is $n_0 \geq 0$ with $\mathfrak{a} M_n = M_{n+1}$ for all $n \geq n_0$. Equivalently, $M_{n_0 + r} = \mathfrak{a}^r M_{n_0}$ for all $r \geq 0$: beyond level $n_0$ the filtration is generated from $M_{n_0}$ by powers of $\mathfrak{a}$.

## The canonical example

The **$\mathfrak{a}$-adic filtration** is $M_n = \mathfrak{a}^n M$ (with $\mathfrak{a}^0 = R$, so $M_0 = M$). It is an $\mathfrak{a}$-filtration, since $\mathfrak{a} \cdot \mathfrak{a}^n M = \mathfrak{a}^{n+1} M$, and it is stable, with equality holding for *all* $n \geq 0$ (so $n_0 = 0$).

---

# Relate to Other Fields / Compression

The cleanest compression: **a filtration is an order-of-vanishing function on a module, an $\mathfrak{a}$-filtration is one for which $\mathfrak{a}$ raises the order, and a stable $\mathfrak{a}$-filtration is one that is eventually *exactly* the $\mathfrak{a}$-adic order.** The single example to keep is $\mathbb{Z} \supseteq p\mathbb{Z} \supseteq p^2\mathbb{Z} \supseteq \cdots$, the order being $\nu_p$, the $p$-adic valuation.

**True name:** the operational content of "stable" is *"the filtration is finitely generated as a Rees-algebra module"* — beyond some level $n_0$ everything is $\mathfrak{a}^r M_{n_0}$, so the whole tower is determined by the finitely many modules $M_0, \dots, M_{n_0}$. When a problem hands you a stable filtration, the move is to invoke this finiteness: pass to the Rees algebra $\bigoplus \mathfrak{a}^n$ and recognise that $\bigoplus M_n$ is finitely generated over it. This is the bridge that turns a topological/filtration question into a Noetherian-finiteness question.

The construction is the algebraic version of an **adic topology** and ultimately of a **completion**. Declaring the submodules $M_n$ to be a neighbourhood basis of $0$ makes $M$ a topological group; the $\mathfrak{a}$-adic filtration gives the **$\mathfrak{a}$-adic topology**, in which "$x_k \to 0$" means "$x_k \in \mathfrak{a}^n M$ eventually, for every $n$". Completing $M$ in this topology produces the **$\mathfrak{a}$-adic completion** $\varprojlim M/\mathfrak{a}^n M$, the algebraic analogue of forming the $p$-adic integers from $\mathbb{Z}$ or of taking Taylor expansions at a point — the subject of the previous chapter. Stable filtrations matter precisely because they all give the *same* topology and hence the *same* completion as the $\mathfrak{a}$-adic one.

---

# Examples / Corollaries

**Is an instance ($\mathfrak{a}$-filtration and stable) — the $\mathfrak{a}$-adic filtration.** $M_n = \mathfrak{a}^n M$. This is the template; everything is measured against it. In $\mathbb{Z}$ with $\mathfrak{a} = (p)$ it is $\mathbb{Z} \supseteq p\mathbb{Z} \supseteq p^2\mathbb{Z} \supseteq \cdots$, sorting integers by $\nu_p$.

**Is an instance — a shifted $\mathfrak{a}$-adic filtration.** Fix $c \geq 0$ and set $M_n = \mathfrak{a}^{n+c} M$ for the first few levels, padding $M_0 = M$. Concretely $M_0 = M$, $M_1 = \mathfrak{a}^{c+1} M, M_2 = \mathfrak{a}^{c+2}M, \dots$ is a stable $\mathfrak{a}$-filtration that is *not* the $\mathfrak{a}$-adic one but is equivalent to it: it stabilizes immediately and differs only by a finite shift. This shows the "for large $n$" slack in the definition is genuinely used — stable filtrations form a whole equivalence class around the $\mathfrak{a}$-adic representative.

**Is an instance — a submodule intersection (the Artin–Rees output).** If $(M_n)$ is a stable $\mathfrak{a}$-filtration of $M$ and $N \subseteq M$ is a submodule, then $(N \cap M_n)_{n \geq 0}$ is an $\mathfrak{a}$-filtration of $N$: indeed $\mathfrak{a}(N \cap M_n) \subseteq N \cap \mathfrak{a} M_n \subseteq N \cap M_{n+1}$. That it is moreover *stable* is the entire content of [[Thm - The Artin-Rees Lemma|Artin–Rees]] — and it is the example that motivates isolating stability, because stability of this intersected filtration is precisely what fails to be obvious.

**Is NOT an instance (of stability) — a filtration that outpaces $\mathfrak{a}$.** Take $R = k[x]$, $M = R$, $\mathfrak{a} = (x)$, and the filtration $M_n = (x^{2^n})$. Each level is a submodule and $\mathfrak{a} M_n = (x^{2^n + 1}) \subseteq (x^{2^{n+1}}) = M_{n+1}$ for $n \geq 0$, so this *is* an $\mathfrak{a}$-filtration. But $\mathfrak{a} M_n = (x^{2^n+1})$ is strictly smaller than $M_{n+1} = (x^{2^{n+1}})$ for every $n \geq 1$, so it is never the case that $\mathfrak{a} M_n = M_{n+1}$: the filtration plunges faster than $\mathfrak{a}$ drives it, and it is *not* stable. It induces a topology strictly finer than the $(x)$-adic one. This is the non-example that shows "$\mathfrak{a}$-filtration" is strictly weaker than "stable $\mathfrak{a}$-filtration".

**Is NOT an instance (of being an $\mathfrak{a}$-filtration) — a chain $\mathfrak{a}$ ignores.** In $R = k[x,y]$, $M = R$, $\mathfrak{a} = (x)$, the filtration $M_n = (y^n)$ is descending with $M_0 = R$, so it is a filtration. But $\mathfrak{a} M_n = (xy^n)$ is *not* contained in $M_{n+1} = (y^{n+1})$ (the element $xy^n$ has a factor of $x$, not $y^{n+1}$), so it is not an $\mathfrak{a}$-filtration: multiplying by $\mathfrak{a} = (x)$ does not increase $y$-depth. A filtration only becomes an $\mathfrak{a}$-filtration when $\mathfrak{a}$ genuinely shifts its levels.

**Corollary — every $\mathfrak{a}$-filtration dominates the $\mathfrak{a}$-adic one.** If $(M_n)$ is any $\mathfrak{a}$-filtration, then iterating $\mathfrak{a} M_n \subseteq M_{n+1}$ from $M_0 = M$ gives $\mathfrak{a}^n M \subseteq M_n$ for all $n$. So the $\mathfrak{a}$-adic filtration is the *finest* (deepest-plunging) $\mathfrak{a}$-filtration: any other sits above it. Stability is then exactly the condition that it does not sit *too far* above — the reverse containment $M_{n} \subseteq \mathfrak{a}^{n - n_0} M$ holds eventually.

**Calibration check.** Verify $\mathfrak{a}^n M \subseteq M_n$ for any $\mathfrak{a}$-filtration by induction. Confirm the $\mathfrak{a}$-adic filtration is stable with $n_0 = 0$, and that the shifted filtration $M_n = \mathfrak{a}^{n+c}M$ ($n \geq 1$) is stable but not $\mathfrak{a}$-adic. Show $(N \cap M_n)$ is always an $\mathfrak{a}$-filtration of $N$ using $\mathfrak{a}(N \cap M_n) \subseteq N \cap \mathfrak{a} M_n$. Finally, exhibit a non-stable $\mathfrak{a}$-filtration and explain why it gives a strictly finer topology than the $\mathfrak{a}$-adic one.

---

# Unlocked by This

> [!tip] The a-adic topology and completion *(from Commutative Algebra X)*
> A filtration $(M_n)$ turns $M$ into a topological module with the $M_n$ as a basis of neighbourhoods of $0$. For the $\mathfrak{a}$-adic filtration this is the **$\mathfrak{a}$-adic topology**, and completing in it gives the **$\mathfrak{a}$-adic completion** $\hat{M} = \varprojlim M/\mathfrak{a}^n M$ — the algebraic incarnation of Taylor expansion and of the $p$-adic numbers. Because all stable $\mathfrak{a}$-filtrations give the same topology, they give the same completion; this is the bridge to the completions chapter, where $\hat{R}$ is studied in its own right. The kernel of the completion map $M \to \hat{M}$ is exactly $\bigcap_n \mathfrak{a}^n M$, whose vanishing is the Krull intersection theorem.

> [!tip] Order of vanishing and discrete valuations *(from Commutative Algebra XIII)*
> When $R$ is a one-dimensional regular local ring (a discrete valuation ring) with maximal ideal $\mathfrak{m} = (\pi)$, the $\mathfrak{m}$-adic filtration $R \supseteq (\pi) \supseteq (\pi^2) \supseteq \cdots$ *is* the valuation: the order $\nu(x) = \sup\{n : x \in \mathfrak{m}^n\}$ is the discrete valuation, and $\mathfrak{m}^n/\mathfrak{m}^{n+1}$ is one-dimensional over the residue field for every $n$. The filtration machinery of this chapter is the general-dimension analogue of a valuation: a way to assign each element an "order of vanishing", which collapses to an honest valuation exactly in the DVR case.
