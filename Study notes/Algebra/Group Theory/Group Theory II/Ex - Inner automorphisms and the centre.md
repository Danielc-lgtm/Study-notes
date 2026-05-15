---
type: exercise
subject: group-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Automorphism Group"
  - "Def - Centraliser and Centre"
  - "Def - Homomorphism"
  - "Def - Kernel and Image"
  - "Def - Normal Subgroup"
  - "Thm - First Isomorphism Theorem"
tags: [algebra, group-theory]
---

# Problem Statement

Let $G$ be a group. For each $g \in G$, let $\gamma_g : G \to G$ be **conjugation by $g$**, the map
$$\gamma_g(x) = g x g^{-1}.$$
Each $\gamma_g$ is an automorphism of $G$ — an *inner automorphism*. Define $\gamma : G \to \operatorname{Aut}(G)$ by $\gamma(g) = \gamma_g$.

Prove the following.

1. $\gamma$ is a [[Def - Homomorphism|homomorphism]] $G \to \operatorname{Aut}(G)$; that is, $\gamma_{gh} = \gamma_g \circ \gamma_h$ for all $g, h \in G$.
2. The kernel of $\gamma$ is the centre $Z(G)$.
3. The image of $\gamma$ is the set $\operatorname{Inn}(G)$ of all inner automorphisms.
4. Deduce $G / Z(G) \cong \operatorname{Inn}(G)$.
5. Show $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$ — the inner automorphisms form a normal subgroup of the full automorphism group.

**Recall:**

The objects in play are the automorphism group, the centre, homomorphisms and their kernels and images, and the first isomorphism theorem.

![[Def - Automorphism Group#The Definition]]

An [[Def - Homomorphism|homomorphism]] is a map $\varphi : G \to H$ between groups with $\varphi(xy) = \varphi(x)\varphi(y)$. Its [[Def - Kernel and Image|kernel]] is $\ker\varphi = \{g : \varphi(g) = e_H\}$ — for the codomain $\operatorname{Aut}(G)$ the identity element $e_H$ is the **identity map** $\operatorname{id}_G$ — and its [[Def - Kernel and Image|image]] is $\operatorname{im}\varphi = \{\varphi(g) : g \in G\}$.

![[Def - Centraliser and Centre#The Definition]]

So the [[Def - Centraliser and Centre|centre]] $Z(G) = \{h \in G : hg = gh \text{ for all } g \in G\}$ is the set of elements commuting with everything in $G$.

The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] states that for any homomorphism $\varphi : G \to H$, the kernel is a [[Def - Normal Subgroup|normal subgroup]] and $G/\ker\varphi \cong \operatorname{im}\varphi$.

---

# Convergent Strategy

**Problem class.** This is a *set up a homomorphism and apply the first isomorphism theorem* problem. It is the canonical way to *identify a quotient*: rather than analysing $G/Z(G)$ from the inside, one builds a homomorphism out of $G$ whose kernel is $Z(G)$, and lets [[Thm - First Isomorphism Theorem|the first isomorphism theorem]] hand back the quotient as an image. The [[Group Theory II — §1.3–1.4#Problem-Solving Strategy|topic page's strategy]] flags this as the principal use of the conjugation action: conjugation packages $G$ as a homomorphism into a symmetry group.

**Assumption pattern.** There is no special hypothesis on $G$ — the result holds for every group. The structure comes entirely from the *map* $\gamma$: it is built from conjugation, and conjugation is exactly the action of $G$ on itself studied throughout §1.4. The recognisable pattern is "a natural map out of $G$ is given (or can be built), and we are asked for its kernel, image, and the resulting quotient" — the signature of a first-isomorphism-theorem problem.

**Theorem routing.** The route is fixed and runs through [[Thm - First Isomorphism Theorem]]. First verify $\gamma$ is a homomorphism (parts 1). Then compute its kernel — the elements whose conjugation is trivial — and recognise it as the [[Def - Centraliser and Centre|centre]] (part 2). Identify the image as $\operatorname{Inn}(G)$ by definition (part 3). The first isomorphism theorem then converts kernel and image into the isomorphism $G/Z(G) \cong \operatorname{Inn}(G)$ (part 4). Normality of $\operatorname{Inn}(G)$ in $\operatorname{Aut}(G)$ (part 5) is a separate short computation — a *conjugation-of-a-conjugation* identity.

**Key decision point.** Two computations are the heart of the exercise. The first is the kernel: $g \in \ker\gamma$ means $\gamma_g = \operatorname{id}_G$, i.e. $gxg^{-1} = x$ for *every* $x$ — and the decision is to read this correctly as "$g$ commutes with every element", which is the definition of the centre, not of a centraliser. The second is the normality identity in part 5: to show $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$ one must conjugate an inner automorphism $\gamma_g$ by an *arbitrary* automorphism $\phi$ and discover that the result $\phi \circ \gamma_g \circ \phi^{-1}$ is again inner — specifically $\gamma_{\phi(g)}$. The non-obvious move is composing three maps and pushing $\phi$ through the conjugation formula; the identity $\phi \circ \gamma_g \circ \phi^{-1} = \gamma_{\phi(g)}$ is the surprise that makes the normality automatic.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Group Theory II — §1.3–1.4#Legal Operations|the topic page's Legal Operations]]:

1. **Act on the group itself by conjugation** (operation 5). The map $\gamma$ is precisely the permutation representation of the conjugation action of $G$ on itself; recognising conjugation-by-$g$ as a homomorphism's value is the foundation.

2. **Convert an action into a homomorphism and take its kernel** (operation 3). The conjugation action *is* the homomorphism $\gamma : G \to \operatorname{Aut}(G)$; its kernel is the normal subgroup we want, and identifying that kernel is the central computation.

3. **Write down / apply the first isomorphism theorem** (a Group Theory I operation, used as a conversion device). With kernel $Z(G)$ and image $\operatorname{Inn}(G)$ in hand, [[Thm - First Isomorphism Theorem|the first isomorphism theorem]] delivers $G/Z(G) \cong \operatorname{Inn}(G)$ in one step.

---

# Hints

> [!note]- Hint 1
> For part 1, write out $\gamma_{gh}(x)$ and $(\gamma_g \circ \gamma_h)(x)$ separately and compare. The associativity of the group and the cancellation $h^{-1}g^{-1} = (gh)^{-1}$ are all you need.

> [!note]- Hint 2
> The codomain of $\gamma$ is $\operatorname{Aut}(G)$, whose identity element is the *identity map* $\operatorname{id}_G$. So $g \in \ker\gamma$ means $\gamma_g = \operatorname{id}_G$, i.e. $gxg^{-1} = x$ for **every** $x \in G$. Rearrange $gxg^{-1} = x$ to a statement about $g$ and $x$ commuting. Which standard subgroup is "the elements commuting with everything"?

> [!note]- Hint 3
> Parts 1–3 give a homomorphism with $\ker\gamma = Z(G)$ and $\operatorname{im}\gamma = \operatorname{Inn}(G)$. Quote [[Thm - First Isomorphism Theorem|the first isomorphism theorem]] for part 4. For part 5, let $\phi \in \operatorname{Aut}(G)$ be arbitrary and compute $\phi \circ \gamma_g \circ \phi^{-1}$ applied to a point $x$: push $\phi^{-1}$ in, conjugate, push $\phi$ out, and use that $\phi$ is a homomorphism so $\phi(g x' g^{-1}) = \phi(g)\phi(x')\phi(g)^{-1}$. You should land on $\gamma_{\phi(g)}$.

---

# Solution

The spine of the solution is: $\gamma$ is a homomorphism, its kernel is $Z(G)$, its image is $\operatorname{Inn}(G)$, and [[Thm - First Isomorphism Theorem|the first isomorphism theorem]] then gives both the isomorphism $G/Z(G) \cong \operatorname{Inn}(G)$ and (with a short extra computation) the normality of $\operatorname{Inn}(G)$.

**Step 1: $\gamma$ is a homomorphism: $\gamma_{gh} = \gamma_g \circ \gamma_h$.**

Conjugation by a product equals the composite of the two conjugations, because the inner $h^{-1}$ and $g^{-1}$ assemble into $(gh)^{-1}$.

> [!note]- Derivation
> Fix $g, h \in G$. For any $x \in G$,
> $$(\gamma_g \circ \gamma_h)(x) = \gamma_g\big(\gamma_h(x)\big) = \gamma_g\big(h x h^{-1}\big) = g(h x h^{-1})g^{-1} = (gh)\,x\,(h^{-1}g^{-1}) = (gh)\,x\,(gh)^{-1} = \gamma_{gh}(x),$$
> using associativity and $h^{-1}g^{-1} = (gh)^{-1}$. Since this holds for every $x$, the maps agree: $\gamma_{gh} = \gamma_g \circ \gamma_h$.
>
> The product in $\operatorname{Aut}(G)$ is composition, so this is exactly the statement that $\gamma(gh) = \gamma(g)\gamma(h)$ — i.e. $\gamma$ is a [[Def - Homomorphism|homomorphism]] $G \to \operatorname{Aut}(G)$. (That each $\gamma_g$ genuinely lies in $\operatorname{Aut}(G)$: $\gamma_g(xy) = gxyg^{-1} = gxg^{-1} \cdot gyg^{-1} = \gamma_g(x)\gamma_g(y)$ so $\gamma_g$ is a homomorphism, and $\gamma_g \circ \gamma_{g^{-1}} = \gamma_{gg^{-1}} = \gamma_e = \operatorname{id}_G$ shows it is invertible, hence an automorphism.)

**Step 2: $\ker\gamma = Z(G)$.**

An element $g$ lies in the kernel if and only if conjugation by $g$ is the identity map, if and only if $g$ commutes with every element of $G$ — which is the definition of the centre.

> [!note]- Derivation
> The identity element of the group $\operatorname{Aut}(G)$ is the identity map $\operatorname{id}_G$. So by [[Def - Kernel and Image|definition of the kernel]],
> $$g \in \ker\gamma \iff \gamma(g) = \operatorname{id}_G \iff \gamma_g = \operatorname{id}_G \iff gxg^{-1} = x \ \text{ for all } x \in G.$$
> Right-multiplying $gxg^{-1} = x$ by $g$ gives the equivalent condition $gx = xg$ for all $x \in G$. So
> $$g \in \ker\gamma \iff gx = xg \ \text{ for all } x \in G,$$
> which is exactly the defining condition for $g$ to belong to the [[Def - Centraliser and Centre|centre]] $Z(G)$. Hence $\ker\gamma = Z(G)$.

**Step 3: $\operatorname{im}\gamma = \operatorname{Inn}(G)$.**

The image is the set of all maps $\gamma_g$, which is by definition the set $\operatorname{Inn}(G)$ of inner automorphisms.

> [!note]- Derivation
> By [[Def - Kernel and Image|definition of the image]],
> $$\operatorname{im}\gamma = \{\gamma(g) : g \in G\} = \{\gamma_g : g \in G\}.$$
> An *inner automorphism* of $G$ is precisely an automorphism of the form $x \mapsto gxg^{-1}$ for some $g \in G$ — that is, a map $\gamma_g$. So $\{\gamma_g : g \in G\}$ is exactly the set $\operatorname{Inn}(G)$ of inner automorphisms, and $\operatorname{im}\gamma = \operatorname{Inn}(G)$.
>
> As the image of a homomorphism, $\operatorname{Inn}(G)$ is automatically a [[Def - Subgroup|subgroup]] of $\operatorname{Aut}(G)$ — closure and inverses are inherited from $\gamma$ being a homomorphism (Step 1).

**Step 4: $G/Z(G) \cong \operatorname{Inn}(G)$.**

Feeding the kernel and image into the first isomorphism theorem gives the isomorphism directly.

> [!note]- Derivation
> $\gamma : G \to \operatorname{Aut}(G)$ is a homomorphism (Step 1) with $\ker\gamma = Z(G)$ (Step 2) and $\operatorname{im}\gamma = \operatorname{Inn}(G)$ (Step 3). The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] states that for any homomorphism $\varphi$, $G/\ker\varphi \cong \operatorname{im}\varphi$. Applying it to $\gamma$:
> $$G / Z(G) = G/\ker\gamma \ \cong\ \operatorname{im}\gamma = \operatorname{Inn}(G).$$
> (In particular this re-proves that $Z(G)$ is a [[Def - Normal Subgroup|normal subgroup]] of $G$ — it is a kernel — and tells us $\operatorname{Inn}(G)$ measures exactly the part of $G$ that conjugation "can see": $G$ acts on itself by conjugation through the quotient $G/Z(G)$.)

**Step 5: $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$.**

Conjugating an inner automorphism $\gamma_g$ by any automorphism $\phi$ produces another inner automorphism, namely $\gamma_{\phi(g)}$ — so $\operatorname{Inn}(G)$ is closed under conjugation in $\operatorname{Aut}(G)$, hence normal.

> [!note]- Derivation
> We show that for every $\phi \in \operatorname{Aut}(G)$ and every $\gamma_g \in \operatorname{Inn}(G)$, the conjugate $\phi \circ \gamma_g \circ \phi^{-1}$ is again inner. Apply it to an arbitrary $x \in G$:
> $$\big(\phi \circ \gamma_g \circ \phi^{-1}\big)(x) = \phi\Big(\gamma_g\big(\phi^{-1}(x)\big)\Big) = \phi\Big(g\,\phi^{-1}(x)\,g^{-1}\Big).$$
> Now $\phi$ is a homomorphism, so it distributes over the product $g \cdot \phi^{-1}(x) \cdot g^{-1}$:
> $$\phi\Big(g\,\phi^{-1}(x)\,g^{-1}\Big) = \phi(g)\;\phi\big(\phi^{-1}(x)\big)\;\phi(g^{-1}) = \phi(g)\;x\;\phi(g)^{-1},$$
> using $\phi(\phi^{-1}(x)) = x$ and $\phi(g^{-1}) = \phi(g)^{-1}$. The right-hand side is conjugation of $x$ by the element $\phi(g) \in G$, that is, $\gamma_{\phi(g)}(x)$. Since this holds for all $x$,
> $$\phi \circ \gamma_g \circ \phi^{-1} = \gamma_{\phi(g)} \in \operatorname{Inn}(G).$$
> So $\operatorname{Inn}(G)$ is closed under conjugation by every element of $\operatorname{Aut}(G)$: for all $\phi \in \operatorname{Aut}(G)$, $\phi\,\operatorname{Inn}(G)\,\phi^{-1} \subseteq \operatorname{Inn}(G)$. By the [[Def - Normal Subgroup|definition of normality]] (a subgroup closed under conjugation by every element is normal), $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$. $\blacksquare$

> [!note]- Complete formal solution
> Let $G$ be a group, $\gamma_g(x) = gxg^{-1}$, and $\gamma(g) = \gamma_g$.
>
> **1. $\gamma$ is a homomorphism.** Each $\gamma_g$ is an automorphism: $\gamma_g(xy) = gxyg^{-1} = (gxg^{-1})(gyg^{-1}) = \gamma_g(x)\gamma_g(y)$, and $\gamma_g\circ\gamma_{g^{-1}} = \operatorname{id}_G$ gives invertibility. For $g,h \in G$ and any $x$,
> $$(\gamma_g\circ\gamma_h)(x) = g(hxh^{-1})g^{-1} = (gh)x(gh)^{-1} = \gamma_{gh}(x),$$
> so $\gamma_{gh} = \gamma_g\circ\gamma_h$, i.e. $\gamma(gh) = \gamma(g)\gamma(h)$. Thus $\gamma : G \to \operatorname{Aut}(G)$ is a [[Def - Homomorphism|homomorphism]].
>
> **2. $\ker\gamma = Z(G)$.** The identity of $\operatorname{Aut}(G)$ is $\operatorname{id}_G$, so $g \in \ker\gamma \iff \gamma_g = \operatorname{id}_G \iff gxg^{-1} = x$ for all $x \iff gx = xg$ for all $x \iff g \in Z(G)$.
>
> **3. $\operatorname{im}\gamma = \operatorname{Inn}(G)$.** By definition $\operatorname{im}\gamma = \{\gamma_g : g \in G\}$, and an inner automorphism is exactly a map of the form $\gamma_g$; so $\operatorname{im}\gamma = \operatorname{Inn}(G)$, a subgroup of $\operatorname{Aut}(G)$ as the image of a homomorphism.
>
> **4. $G/Z(G) \cong \operatorname{Inn}(G)$.** By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] applied to $\gamma$, $G/\ker\gamma \cong \operatorname{im}\gamma$, i.e. $G/Z(G) \cong \operatorname{Inn}(G)$.
>
> **5. $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$.** Let $\phi \in \operatorname{Aut}(G)$ and $\gamma_g \in \operatorname{Inn}(G)$. For any $x$,
> $$(\phi\circ\gamma_g\circ\phi^{-1})(x) = \phi\big(g\,\phi^{-1}(x)\,g^{-1}\big) = \phi(g)\,x\,\phi(g)^{-1} = \gamma_{\phi(g)}(x),$$
> using that $\phi$ is a homomorphism. Hence $\phi\circ\gamma_g\circ\phi^{-1} = \gamma_{\phi(g)} \in \operatorname{Inn}(G)$, so $\operatorname{Inn}(G)$ is closed under conjugation in $\operatorname{Aut}(G)$ and is therefore [[Def - Normal Subgroup|normal]]: $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$. $\blacksquare$

---

# Key Takeaways

**To identify a quotient $G/N$, build a homomorphism out of $G$ with kernel $N$ — never analyse the quotient directly.** The reusable move on display is the standard use of [[Thm - First Isomorphism Theorem|the first isomorphism theorem]]: a quotient group $G/N$ is hard to understand from the inside (its elements are cosets, its multiplication is coset multiplication), but if you can produce *any* homomorphism $\varphi$ out of $G$ whose kernel is exactly $N$, then $G/N$ is instantly identified as the concrete group $\operatorname{im}\varphi$. The skill is *constructing the right homomorphism*. Here the construction is canonical — conjugation packages $G$ as the map $\gamma : G \to \operatorname{Aut}(G)$ — and it reveals that the abstract quotient $G/Z(G)$ is the tangible group $\operatorname{Inn}(G)$ of inner automorphisms. The trigger for this technique is any request to "describe" or "identify" a quotient: stop manipulating cosets and ask what natural map has the right kernel. The candidates are usually actions (giving maps into symmetric or automorphism groups), determinant or sign maps, or projections onto factors.

**The centre is the kernel of conjugation — that single sentence explains everything the centre does.** This exercise makes precise *why* the centre is normal and *why* it measures non-commutativity. $Z(G)$ is the kernel of the conjugation homomorphism $\gamma$, and three facts follow immediately and for free. First, $Z(G) \trianglelefteq G$, because kernels are always normal — no separate verification needed. Second, $G/Z(G) \cong \operatorname{Inn}(G)$, so the quotient by the centre is exactly the group of symmetries that conjugation can actually produce: the centre is "the part of $G$ that conjugation cannot see", the elements that act invisibly. Third, $G$ is abelian precisely when $\gamma$ is trivial, precisely when $Z(G) = G$ — so the size of $Z(G)$ literally quantifies the failure of commutativity. The general lesson: when a standard subgroup is defined by a commuting or fixing condition, look for the homomorphism whose kernel it is — centralisers and centres are kernels of (restricted) conjugation actions, and recognising them as kernels imports normality and a quotient description at no cost.

**A subgroup defined by a "natural" construction is often normal — conjugation permutes the construction.** Part 5 illustrates a pattern worth abstracting: $\operatorname{Inn}(G)$ is normal in $\operatorname{Aut}(G)$ because conjugating an inner automorphism by *any* automorphism yields an inner automorphism — the identity $\phi \circ \gamma_g \circ \phi^{-1} = \gamma_{\phi(g)}$ shows conjugation merely relabels the index $g$ to $\phi(g)$. The deep reason is that "being inner" is a property *intrinsic* to the structure of $G$, and an automorphism $\phi$, being a structure-preserving bijection, must map intrinsic features to intrinsic features. This is the hallmark of a stronger notion, the *characteristic subgroup* — a subgroup preserved by every automorphism, not merely every inner one — and $\operatorname{Inn}(G)$, the centre $Z(G)$, the commutator subgroup, and the set of elements of a given order are all characteristic for exactly this reason. The trigger: whenever a subgroup is singled out by a description that makes no arbitrary choices — "the elements commuting with everything", "the automorphisms of the form $\gamma_g$", "the subgroup generated by all commutators" — expect it to be invariant under automorphisms, hence normal, and prove it by checking that the defining construction is carried to itself.
