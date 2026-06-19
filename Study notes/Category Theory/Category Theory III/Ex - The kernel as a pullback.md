---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Pullback and Pushout"
  - "Def - Equalizer and Coequalizer"
  - "Def - Normal Subgroup"
tags: [category-theory, foundations]
---

# Problem Statement

Let $\varphi : G \to H$ be a group homomorphism. Show that the kernel $\ker\varphi$ is a [[Def - Pullback and Pushout|pullback]]: it is the fibre product of $\varphi : G \to H$ and the inclusion of the trivial subgroup $\{e\} \hookrightarrow H$,
$$\ker\varphi \;=\; G \times_H \{e\}.$$
Equivalently, show $\ker\varphi$ is the [[Def - Equalizer and Coequalizer|equalizer]] of $\varphi$ and the trivial homomorphism $0 : G \to H$ (the map sending everything to $e$). Deduce that $\ker\varphi$ is a [[Def - Normal Subgroup|normal subgroup]], using only that the pullback of a normal subgroup along a homomorphism is normal.

**Recall:**

A **pullback** of $A \xrightarrow{f} C \xleftarrow{g} B$ is $A \times_C B = \{(a,b) : f(a) = g(b)\}$ in $\mathbf{Set}$, universal among objects mapping compatibly to $A$ and $B$ over $C$.

![[Def - Normal Subgroup#The Definition]]

The **kernel** of $\varphi : G \to H$ is $\ker\varphi = \{g \in G : \varphi(g) = e_H\}$.

---

# Convergent Strategy

**Problem class:** This is a "recognise a familiar object as a universal construction" problem — taking the kernel, defined element-wise, and re-deriving it as a pullback so that its properties (normality, functoriality) follow categorically rather than by hand. The routine: match the element-wise definition to the pullback's compatible-pair description, then transport structural facts.

**Assumption pattern:** The key assumption is the presence of a *basepoint* $\{e\} \hookrightarrow H$ — the inclusion of the trivial subgroup. The kernel is "the preimage of the basepoint", and preimages are pullbacks along inclusions; recognising "$\ker = \varphi^{-1}(e)$" as a preimage is what routes to a pullback.

**Theorem routing:** Two equivalent routes. The pullback route: $G \times_H \{e\} = \{(g, *) : \varphi(g) = e\} \cong \{g : \varphi(g) = e\} = \ker\varphi$. The equalizer route: $\mathrm{eq}(\varphi, 0) = \{g : \varphi(g) = 0(g) = e\} = \ker\varphi$, using that the kernel is where $\varphi$ agrees with the zero map (see [[Def - Equalizer and Coequalizer]]). Normality then follows from "pullback of a normal subgroup is normal", since $\{e\} \trianglelefteq H$.

**Key decision point:** The non-obvious choice is *which* pullback to take. The kernel is the pullback of $\varphi$ against the basepoint inclusion $\{e\} \hookrightarrow H$ — not against $H \to 1$ (that gives $G$ itself) nor against $\varphi$ with itself (that gives the kernel *pair*, the relation $\{(g,g') : \varphi(g) = \varphi(g')\}$, a different object). Distinguishing the kernel from the kernel pair is the crux.

---

# Legal Operations Used

1. **Recognise a preimage as a pullback along an inclusion (from the topic page: pullbacks compute preimages).** $\varphi^{-1}(\{e\})$ is the pullback of $\varphi$ and $\{e\} \hookrightarrow H$.

2. **Translate the kernel into an equalizer (operation: kernel $=$ equalizer of $(\varphi, 0)$).** Use that $\varphi(g) = e \iff \varphi(g) = 0(g)$ to present $\ker\varphi$ as $\mathrm{eq}(\varphi, 0)$, then as a pullback of the diagonal.

3. **Transport normality through the pullback (operation: pullback of a normal subgroup is normal).** Since $\{e\} \trianglelefteq H$ and pullbacks preserve normality of subobjects, $\ker\varphi \trianglelefteq G$ without conjugation calculation.

---

# Hints

> [!note]- Hint 1
> The kernel is the preimage $\varphi^{-1}(\{e\})$. Preimages are pullbacks: $f^{-1}(B) = A \times_C B$ when $B \hookrightarrow C$. Set $f = \varphi$ and $B = \{e\}$.

> [!note]- Hint 2
> Compute the pullback set $G \times_H \{e\} = \{(g, *) : \varphi(g) = e\}$ and identify it with $\ker\varphi$ via $(g,*) \mapsto g$.

> [!note]- Hint 3
> Alternatively: $\varphi(g) = e$ says $\varphi$ agrees with the trivial map $0$ at $g$, so $\ker\varphi = \mathrm{eq}(\varphi, 0)$. Both presentations are the same subobject by [[Thm - Limits are Unique up to Unique Isomorphism|uniqueness]].

> [!note]- Hint 4
> For normality: the subgroup $\{e\} \trianglelefteq H$ is normal; pulling back a normal subgroup along a homomorphism yields a normal subgroup, so $\ker\varphi \trianglelefteq G$ for free.

---

# Solution

The plan: present the kernel as the pullback of $\varphi$ against the basepoint inclusion, verifying the compatible-pair description matches the element-wise kernel; note the equivalent equalizer presentation; then deduce normality by transporting it through the pullback from $\{e\} \trianglelefteq H$.

**Step 1: The pullback $G \times_H \{e\}$ is the kernel as a set/group.**

> [!note]- Derivation
> Form the pullback of $\varphi : G \to H$ and the inclusion $\iota : \{e\} \hookrightarrow H$. Its underlying set is
> $$G \times_H \{e\} = \{(g, x) \in G \times \{e\} : \varphi(g) = \iota(x) = e\} = \{(g, e) : \varphi(g) = e\}.$$
> The projection $(g, e) \mapsto g$ is a bijection onto $\{g : \varphi(g) = e\} = \ker\varphi$, and a group isomorphism (the pullback in $\mathbf{Grp}$ has componentwise operations, and the second component is constant). So $\ker\varphi \cong G \times_H \{e\}$, with $p_1$ the inclusion into $G$.

**Step 2: The same object is the equalizer of $\varphi$ and $0$.**

> [!note]- Derivation
> Let $0 : G \to H$ be the trivial homomorphism $g \mapsto e$. Then $\varphi(g) = e \iff \varphi(g) = 0(g)$, so the [[Def - Equalizer and Coequalizer|equalizer]] $\mathrm{eq}(\varphi, 0) = \{g : \varphi(g) = 0(g)\} = \ker\varphi$. This matches the pullback presentation, as it must: the equalizer of $(\varphi, 0)$ is the pullback of $\langle \varphi, 0\rangle : G \to H \times H$ against the diagonal, and the diagonal restricted to the basepoint recovers $\{e\} \hookrightarrow H$. By [[Thm - Limits are Unique up to Unique Isomorphism|uniqueness of limits]] all these descriptions give the same subobject.

**Step 3: Normality of $\ker\varphi$ is inherited from $\{e\} \trianglelefteq H$.**

> [!note]- Derivation
> The trivial subgroup $\{e\}$ is [[Def - Normal Subgroup|normal]] in $H$. The pullback of a normal subgroup $N \trianglelefteq H$ along a homomorphism $\varphi : G \to H$ is the normal subgroup $\varphi^{-1}(N) \trianglelefteq G$: for $g \in \varphi^{-1}(N)$ and $x \in G$, $\varphi(xgx^{-1}) = \varphi(x)\varphi(g)\varphi(x)^{-1} \in N$ since $N$ is normal, so $xgx^{-1} \in \varphi^{-1}(N)$. Applying this with $N = \{e\}$ gives $\ker\varphi = \varphi^{-1}(\{e\}) \trianglelefteq G$. No direct conjugation calculation on the kernel was needed — normality is transported through the pullback.

> [!note]- Complete formal solution
> Let $\varphi : G \to H$ and $\iota : \{e\} \hookrightarrow H$. The pullback $G \times_H \{e\}$ has underlying set $\{(g,e) : \varphi(g) = e\}$, which projects isomorphically (as a group) onto $\ker\varphi = \{g : \varphi(g) = e\}$ via $(g,e) \mapsto g$, with $p_1$ the inclusion $\ker\varphi \hookrightarrow G$. So $\ker\varphi = G \times_H \{e\}$ is a pullback. Equivalently, writing $0 : G \to H$ for the trivial homomorphism, $\ker\varphi = \mathrm{eq}(\varphi, 0)$ since $\varphi(g) = e \iff \varphi(g) = 0(g)$; this equalizer is the pullback of $\langle\varphi,0\rangle$ against the diagonal, the same subobject up to unique isomorphism by [[Thm - Limits are Unique up to Unique Isomorphism|uniqueness]]. Finally, $\{e\} \trianglelefteq H$ and the pullback of a normal subgroup along $\varphi$ is normal — $\varphi(xgx^{-1}) = \varphi(x)\varphi(g)\varphi(x)^{-1} \in N$ for $g \in \varphi^{-1}(N)$ — so $\ker\varphi = \varphi^{-1}(\{e\}) \trianglelefteq G$. $\blacksquare$

---

# Key Takeaways

**The kernel is "preimage of the basepoint", and preimages are pullbacks — this re-derivation makes normality structural.** The reusable insight is that defining the kernel as a pullback $G \times_H \{e\}$ converts a property usually proved by conjugation (normality) into a transported property: because the basepoint $\{e\}$ is normal in $H$ and pullbacks preserve normality of subobjects, $\ker\varphi$ is normal for free. This is the categorical upgrade of the element-wise fact, and it generalises — the preimage of *any* normal subgroup is normal, the preimage of an ideal is an ideal, the preimage of a closed set is closed — all because these are pullbacks along the relevant map and the property is pullback-stable. The trigger: whenever you see "preimage of a structured subobject", expect a pullback and expect the structure to transport.

**Distinguish the kernel from the kernel pair — same map, different pullback.** The crucial discrimination is that the kernel $\ker\varphi = G \times_H \{e\}$ (pullback against the *basepoint*) is different from the kernel *pair* $G \times_H G = \{(g,g') : \varphi(g) = \varphi(g')\}$ (pullback of $\varphi$ *with itself*). The kernel is a subobject of $G$; the kernel pair is an equivalence relation on $G$, and its [[Def - Equalizer and Coequalizer|coequalizer]] reconstructs the image — the categorical [[Thm - First Isomorphism Theorem|first isomorphism theorem]]. Keeping these straight is essential because both are "pullbacks involving $\varphi$" and beginners conflate them. The diagnostic: pulling back against a *point* gives a fibre (the kernel), pulling back against *itself* gives a relation (the kernel pair).

**Kernel as equalizer and kernel as pullback are the same subobject, illustrating that limits coincide across presentations.** That $\ker\varphi$ is simultaneously $\mathrm{eq}(\varphi, 0)$ and $G \times_H \{e\}$ is an instance of [[Thm - Limits are Unique up to Unique Isomorphism|uniqueness of limits]]: two different universal-property descriptions of the "same" object must agree up to unique isomorphism. The transferable principle is that you may compute a limit by whichever shape is most convenient — equalizer when the comparison is with a fixed map, pullback when there is a natural cospan — and the answer is canonically the same. This flexibility is constantly exploited: the fibre of a map, the preimage of a subspace, and the equalizer of "the map and a constant" are interchangeable presentations of one subobject. The companion [[Ex - An intersection is a pullback and a limit]] develops the parallel "intersection is a pullback" identification.
