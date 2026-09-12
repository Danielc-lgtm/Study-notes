---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Winding Number of a Map from the Circle to U(1)"
  - "Thm - Clutching Construction for Bundles over a Closed Manifold"
  - "Def - The Hopf Bundle"
  - "Thm - Sections of a Principal Bundle and Triviality"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\pi\colon S^3\to S^2$ be the **Hopf bundle**, the principal $U(1)$-bundle with total space $S^3=\{(w_1,w_2)\in\mathbb{C}^2:|w_1|^2+|w_2|^2=1\}$, base the round sphere $S^2=\{(z,t)\in\mathbb{C}\times\mathbb{R}:|z|^2+t^2=1\}$, right action $(w_1,w_2)\cdot\lambda=(w_1\lambda,w_2\lambda)$ for $\lambda\in U(1)$, and projection the Hopf map. Its base is covered by the two open sets $U_1=S^2\setminus\{(0,-1)\}$ and $U_2=S^2\setminus\{(0,1)\}$, over each of which the bundle is trivial, and the transition function relating the two trivialising sections is
$$g_{12}\colon U_{12}=S^2\setminus\{(0,1),(0,-1)\}\longrightarrow U(1),\qquad g_{12}(z,t)=\frac{z}{|z|}.$$

Prove that the Hopf bundle is **not** isomorphic to the trivial bundle $S^2\times U(1)\to S^2$, by the following route.

1. Realise the Hopf bundle as the clutching bundle $P_g$ over $X=S^2$ built from the coordinate disc $D$ (a closed cap around the north pole $(0,1)$) and the clutching map $g\colon S=\partial D\to U(1)$ obtained by restricting $g_{12}$ to the equator $S=\{(z,0):|z|=1\}\cong S^1$.
2. Compute the winding number of that clutching map and find $w(g)=1$.
3. Invoke the triviality criterion of the clutching construction: $P_g$ is trivial precisely when $g$ factors as a product of the boundary values of a map from $D$ and a map from $X\setminus D^\circ$; show that both such boundary values have winding number zero, so triviality would force $w(g)=0$, contradicting step 2.

Because $w(g)=1\neq0$, the Hopf bundle carries no global trivialisation. State also the alternative proof that goes through the absence of a global section.

**Recall:**

The objects in play are the Hopf bundle and its transition function, the winding number of a circle-valued map, the clutching construction of a bundle over a closed manifold from a map on the boundary of a disc, and the section–triviality correspondence for principal bundles.

![[Def - The Hopf Bundle#The Definition]]

The [[Def - The Hopf Bundle|Hopf bundle]] is the principal $U(1)$-bundle $S^3\to S^2$ just described; on the standing cover $\{U_1,U_2\}$ its transition function is $g_{12}(z,t)=z/|z|$, a map into the unit circle $U(1)=\{\lambda\in\mathbb{C}:|\lambda|=1\}$. (Bär's Example 2.2.17 records the computed value as $g_{12}(z,t)=z/|z|$ but then appends "$=|z|/z$"; the two expressions are reciprocals on the unit circle, so the appended form is a misprint. The computation on the definition page yields $z/|z|$, which is what we use; the sign of the resulting winding number is in any case immaterial to the argument.)

![[Thm - Winding Number of a Map from the Circle to U(1)#Statement]]

For a smooth map $g\colon S^1\to U(1)$ the [[Thm - Winding Number of a Map from the Circle to U(1)|winding number]] is $w(g)=\tfrac{1}{2\pi}\int_{S^1}g^*d\theta=\tfrac{1}{2\pi i}\int_{S^1}g^{-1}\,dg$, where $\theta$ is the angular coordinate on $U(1)$. It is an integer; it is additive under the pointwise product, $w(g_1g_2)=w(g_1)+w(g_2)$; it is a smooth-homotopy invariant; $w(z\mapsto z^k)=k$; and $w(g)=0$ if and only if $g$ extends to a smooth map $D^2\to U(1)$ on the closed unit disc.

![[Thm - Clutching Construction for Bundles over a Closed Manifold#Statement]]

The [[Thm - Clutching Construction for Bundles over a Closed Manifold|clutching construction]] takes a closed connected $n$-manifold $X$, a closed coordinate disc $D\subset X$ with boundary $S=\partial D\cong S^{n-1}$, and a smooth map $g\colon S\to G$, and produces a principal $G$-bundle $P_g$ that is trivial over $D$ and over $X\setminus D^\circ$ with $g$ as its transition function across a collar of $S$. Its triviality clause reads: $P_g$ is trivial if and only if $g=(a|_S)(b|_S)$ for smooth maps $a\colon X\setminus D^\circ\to G$ and $b\colon D\to G$.

![[Thm - Sections of a Principal Bundle and Triviality#Statement]]

The [[Thm - Sections of a Principal Bundle and Triviality|section–triviality theorem]] says that a principal $G$-bundle $P\to M$ is trivial if and only if it admits a global smooth section.

---

# Convergent Strategy

**Problem class.** This is a *prove-a-bundle-is-nontrivial* problem, and it belongs to the family of arguments that convert a *global geometric fact* (no trivialisation exists) into a *topological invariant of gluing data* (a nonzero integer attached to the transition function). The invariant here is the winding number of the abelian-group-valued clutching map. The recognisable shape is: the bundle is patched from two contractible pieces, so all of its topology is concentrated in a single map from the overlap sphere into the structure group, and one computes a homotopy invariant of that map that vanishes exactly when the bundle is trivial.

**Assumption pattern.** Two structural facts about the base do all of the work and must be flagged before any computation. First, $S^2$ decomposes as two closed discs glued along their common boundary circle — the northern and southern caps — so *both* pieces of the clutching decomposition are discs, not merely one. Second, the structure group is *abelian*, $U(1)$, which is what turns the multiplicative triviality condition $g=(a|_S)(b|_S)$ into the additive statement $w(g)=w(a|_S)+w(b|_S)$; without abelianness the winding number is not additive and the argument would need a different invariant. The trigger for the whole method is precisely the pairing "base is a sphere $=$ two discs" with "structure group abelian".

**Theorem routing.** The route is: use [[Def - The Hopf Bundle|the Hopf bundle]]'s explicit transition function $g_{12}=z/|z|$ and [[Thm - Clutching Construction for Bundles over a Closed Manifold|the clutching construction]] to identify $S^3\to S^2$ with $P_g$, where $g$ is $g_{12}$ restricted to the equator $S$; compute $w(g)$ from [[Thm - Winding Number of a Map from the Circle to U(1)|the winding-number theorem]] (the restriction is the identity map $z\mapsto z$, whose winding number is $1$ by part (e)); then assume triviality, apply the clutching triviality clause to write $g=(a|_S)(b|_S)$, apply additivity (part (b) of the winding-number theorem) to get $w(g)=w(a|_S)+w(b|_S)$, and apply the disc-extension clause (part (d)) to each factor — $a$ extends over the southern cap $X\setminus D^\circ$ and $b$ over the northern cap $D$, both discs — to conclude $w(a|_S)=w(b|_S)=0$. The contradiction $1=0$ finishes it.

**Key decision point.** The one genuinely non-obvious move is recognising that the *complement* $X\setminus D^\circ$ of the clutching disc is itself a disc, so that the boundary value $a|_S$ is the restriction of a map from a disc and hence has winding number zero. On a general base $X$ the complement of a coordinate disc is a complicated manifold with boundary, and the factor $w(a|_S)$ need not vanish; the argument is clean here *only because $S^2$ is the union of two discs*. Everything else is bookkeeping around the abelianness of $U(1)$, which lets the two winding numbers add. Missing this point is the usual way the proof is left incomplete: one shows $w(b|_S)=0$ for the disc side and forgets to argue the complement side.

---

# Legal Operations Used

This solution deploys the following operations from the chapter's toolkit; where the topic page for Gauge Theory III fixes their numbering, these are the operations named there, applied here as described.

1. **Read off the transition function from the standing trivialising sections.** The Hopf bundle comes with the two sections $s_1,s_2$ and the computed transition function $g_{12}=z/|z|$; we take this as given from [[Def - The Hopf Bundle|the definition page]] rather than recomputing it.

2. **Present a bundle over a sphere as a clutching bundle.** Choose the coordinate disc $D$ (northern cap) and cut the base $S^2$ into $D$ and its complementary cap $X\setminus D^\circ$; identify the bundle with $P_g$ for $g=g_{12}|_S$ via [[Thm - Clutching Construction for Bundles over a Closed Manifold|the clutching construction]].

3. **Compute a winding number by evaluating the defining integral or by recognising a power map.** On the equator $|z|=1$, so $g_{12}(z,0)=z$; recognise this as the identity $z\mapsto z^1$ and read $w=1$ from part (e), or integrate $g^{-1}dg$ directly.

4. **Convert a multiplicative triviality condition into an additive one using abelianness.** Because $U(1)$ is abelian, apply additivity of the winding number (part (b)) to the factorisation $g=(a|_S)(b|_S)$ to get $w(g)=w(a|_S)+w(b|_S)$.

5. **Kill a boundary-value winding number by extension over a disc.** Each of $a$ and $b$ is defined on a disc whose boundary is $S$; by part (d) of the winding-number theorem, a map that extends over a disc has winding number zero, so $w(a|_S)=w(b|_S)=0$.

6. **Close by contradiction against a computed invariant.** The two computed values $w(g)=1$ and (under the triviality hypothesis) $w(g)=0$ are incompatible; discard the hypothesis.

7. **Translate triviality into the existence of a global section when running the alternative proof.** Use [[Thm - Sections of a Principal Bundle and Triviality|the section–triviality correspondence]] to reduce nontriviality to the absence of a global section, then invoke the proved sibling theorem [[Thm - The Hopf Bundle is Nontrivial]].

---

# Hints

> [!note]- Hint 1
> The Hopf bundle is glued from two pieces over $U_1$ and $U_2$, and its entire topology sits in the single transition function $g_{12}(z,t)=z/|z|$. Cut $S^2$ into two closed caps meeting along the equator $S=\{(z,0):|z|=1\}$. What is $g_{12}$ when you restrict it to the equator, where $|z|=1$?

> [!note]- Hint 2
> On the equator $|z|=1$, so $g_{12}(z,0)=z$ — the identity map $S^1\to U(1)$. Its winding number is a number you know from the power-map clause of the winding-number theorem. Compute it. This is the clutching map $g$ of the Hopf bundle.

> [!note]- Hint 3
> Suppose, for contradiction, that the bundle were trivial. The clutching construction has a triviality criterion: $P_g$ is trivial exactly when $g=(a|_S)(b|_S)$ for smooth $a$ on the *complementary* cap $X\setminus D^\circ$ and smooth $b$ on the cap $D$. Because $U(1)$ is abelian, winding numbers add over products. What does that say about $w(g)$ in terms of $w(a|_S)$ and $w(b|_S)$?

> [!note]- Hint 4
> Both caps are discs. A map $b\colon D\to U(1)$ restricts on $\partial D=S$ to something that visibly extends over the disc $D$, so its winding number is zero by part (d). The same is true for $a$ on the *other* cap $X\setminus D^\circ$ — the crucial observation that this complement is itself a disc. Hence $w(g)=0+0=0$, contradicting $w(g)=1$.

---

# Solution

The proof concentrates the topology of the Hopf bundle into a single circle-valued map — the clutching function on the equator — and detects its nontriviality with one integer, the winding number. The bundle is glued from trivial pieces over two caps of $S^2$, so it is a clutching bundle $P_g$ with $g$ the equatorial restriction of the known transition function $z/|z|$; that restriction is the identity map of the circle, with winding number $1$. If the bundle were trivial, the clutching triviality criterion would factor $g$ as a product of two boundary values, each of which extends over a disc and hence has winding number zero; abelianness of $U(1)$ makes those winding numbers add, forcing $w(g)=0$ and contradicting the computed value.

**Step 1: Cut $S^2$ into two caps and present the Hopf bundle as a clutching bundle.**

Let $D\subset S^2$ be the closed northern cap $D=\{(z,t)\in S^2:t\geq0\}$, with interior $D^\circ=\{t>0\}$ and boundary the equator $S=\partial D=\{(z,0):|z|=1\}\cong S^1$. Its complement is the closed southern cap $X\setminus D^\circ=\{(z,t)\in S^2:t\leq0\}$, also bounded by $S$. The Hopf bundle is trivial over each cap, and its transition function across the equator is $g\colon S\to U(1)$, $g(z,0)=g_{12}(z,0)$.

> [!note]- Derivation
> We must first check that the cutting sets are legitimate clutching data and that the Hopf bundle really is the associated $P_g$. The northern cap $D=\{(z,t)\in S^2:t\geq0\}$ is a closed coordinate disc: stereographic projection from the south pole $(0,-1)$ carries it diffeomorphically onto a closed round disc in $\mathbb{C}$, and its boundary is the equator $S=\{(z,0):|z|^2=1\}$, a smoothly embedded circle. The complement $X\setminus D^\circ=\{(z,t)\in S^2:t\leq0\}$ is the closed southern cap, carried by stereographic projection from the north pole $(0,1)$ onto a closed round disc, again with boundary $S$. Thus $S^2=D\cup(X\setminus D^\circ)$ with the two pieces meeting exactly along $S$, which is the picture the clutching construction requires with $n=2$ and $G=U(1)$.
>
> The northern cap $D$ lies inside $U_1=S^2\setminus\{(0,-1)\}$ (it omits the south pole), where the section $s_1$ trivialises the bundle; the southern cap $X\setminus D^\circ$ lies inside $U_2=S^2\setminus\{(0,1)\}$ (it omits the north pole), where the section $s_2$ trivialises it. So the [[Def - The Hopf Bundle|Hopf bundle]] is trivial over each of the two caps and, on a collar of the shared boundary $S$, the change from the $s_1$-trivialisation to the $s_2$-trivialisation is given by the transition function $g_{12}$ (this is the content of $s_2=s_1\cdot g_{12}$, recorded on the definition page and in [[Def - Transition Functions and the Cocycle Condition|the transition-function conventions]]). By [[Thm - Clutching Construction for Bundles over a Closed Manifold|the clutching construction]], part (b) — every principal bundle that is trivial over $D$ and over $X\setminus D^\circ$ is isomorphic to $P_g$ with $g$ the transition function restricted to a collar of $S$ — the Hopf bundle is isomorphic to $P_g$ for the clutching map
> $$g\colon S\longrightarrow U(1),\qquad g(z,0)=g_{12}(z,0).$$
> We have used the clutching theorem's hypotheses by name: $X=S^2$ is a closed connected $2$-manifold, $D$ is a closed coordinate disc, and the bundle is trivial over both pieces.

**Step 2: The clutching map is the identity of the circle, with winding number $1$.**

On the equator $|z|=1$, so $g(z,0)=z$; under the identification $S\cong S^1$, $z\in U(1)$, this is the identity map $z\mapsto z$, and $w(g)=1$.

> [!note]- Derivation
> On the equator $S=\{(z,0):|z|=1\}$ every point has $|z|=1$, so the transition function evaluates to
> $$g(z,0)=g_{12}(z,0)=\frac{z}{|z|}=\frac{z}{1}=z\qquad(\text{since }|z|=1\text{ on }S).$$
> The equator is parametrised by $\theta\mapsto(e^{i\theta},0)$, $\theta\in[0,2\pi)$, and under the identification of $S$ with the unit circle $S^1=\{e^{i\theta}\}$ and of the fibre group with $U(1)=\{e^{i\theta}\}$, the map $g$ becomes $e^{i\theta}\mapsto e^{i\theta}$, that is, the identity map $z\mapsto z^1$ of the circle. By part (e) of [[Thm - Winding Number of a Map from the Circle to U(1)|the winding-number theorem]], $w(z\mapsto z^k)=k$; taking $k=1$,
> $$w(g)=1.$$
> As an independent check we evaluate the defining integral directly. With $g(e^{i\theta})=e^{i\theta}$ we have $g^{-1}=e^{-i\theta}$ and $dg=ie^{i\theta}\,d\theta$, hence $g^{-1}\,dg=e^{-i\theta}\cdot ie^{i\theta}\,d\theta=i\,d\theta$, and
> $$w(g)=\frac{1}{2\pi i}\int_{S^1}g^{-1}\,dg=\frac{1}{2\pi i}\int_0^{2\pi}i\,d\theta=\frac{1}{2\pi i}\,(2\pi i)=1\qquad(\text{direct evaluation of the integral}).$$
> Both routes agree. The orientation of $S$ or the choice of $g_{12}$ over $g_{21}=g_{12}^{-1}$ could flip the sign — by part (b), $w(g^{-1})=-w(g)$ — but in every convention $|w(g)|=1$, so $w(g)\neq0$, which is all the argument needs.

**Step 3: If the bundle were trivial, additivity and disc-extension would force $w(g)=0$.**

Assume, for contradiction, that the Hopf bundle $P_g$ is trivial. The clutching triviality criterion factors $g=(a|_S)(b|_S)$ with $a\colon X\setminus D^\circ\to U(1)$ and $b\colon D\to U(1)$ smooth. Each factor extends over a disc, so $w(a|_S)=w(b|_S)=0$; abelianness of $U(1)$ makes the winding numbers add, giving $w(g)=0$.

> [!note]- Derivation
> Suppose $P_g$ is trivial. By the triviality clause of [[Thm - Clutching Construction for Bundles over a Closed Manifold|the clutching construction]] — $P_g$ is trivial if and only if $g=(a|_S)(b|_S)$ for smooth maps $a\colon X\setminus D^\circ\to G$ and $b\colon D\to G$ — there exist smooth maps
> $$a\colon X\setminus D^\circ\to U(1),\qquad b\colon D\to U(1),\qquad\text{with}\qquad g=(a|_S)\,(b|_S)$$
> where $a|_S$ and $b|_S$ denote the restrictions of $a$ and $b$ to the common boundary $S=\partial D=\partial(X\setminus D^\circ)$, and the product is the pointwise product in the abelian group $U(1)$.
>
> **The disc side.** The map $b$ is defined on the whole cap $D$, and $D$ is a disc with $\partial D=S$; thus $b|_S$ is the boundary restriction of a smooth map from a disc into $U(1)$. By part (d) of [[Thm - Winding Number of a Map from the Circle to U(1)|the winding-number theorem]] — a smooth map $S^1\to U(1)$ has winding number zero if and only if it extends to a smooth map on the closed disc — the extension $b$ of $b|_S$ witnesses
> $$w(b|_S)=0\qquad(\text{by the disc-extension clause, extension }b\colon D\to U(1)).$$
>
> **The complement side.** This is the step that uses the special geometry of $S^2$. The complement $X\setminus D^\circ$ is the southern cap, which is *itself a disc* with boundary $S$ (Step 1). Hence $a|_S$ is also the boundary restriction of a smooth map from a disc into $U(1)$, namely $a$, and by the same disc-extension clause
> $$w(a|_S)=0\qquad(\text{by the disc-extension clause, extension }a\colon X\setminus D^\circ\to U(1)).$$
>
> **Additivity.** Because $U(1)$ is abelian, the pointwise product of circle maps is handled by part (b) of the winding-number theorem, $w(g_1g_2)=w(g_1)+w(g_2)$. Applying it to $g=(a|_S)(b|_S)$,
> $$w(g)=w(a|_S)+w(b|_S)=0+0=0\qquad(\text{by additivity, part (b), and the two vanishings above}).$$
> This contradicts $w(g)=1$ from Step 2.

**Step 4: Conclude nontriviality.**

The two computations of $w(g)$ are incompatible, so the triviality hypothesis is false: the Hopf bundle is nontrivial.

> [!note]- Derivation
> Steps 2 and 3 assign the single number $w(g)$ two different values: $w(g)=1$ unconditionally, and $w(g)=0$ under the assumption that $P_g$ is trivial. Since $1\neq0$, the assumption is untenable. The named contradiction is between the computed winding number $w(g)=1$ (Step 2) and the value $w(g)=0$ that triviality would force (Step 3). Therefore the Hopf bundle admits no global trivialisation:
> $$S^3\;\not\cong\;S^2\times U(1)\quad\text{as principal }U(1)\text{-bundles.}$$

> [!note]- Complete formal solution
> **Claim.** The Hopf bundle $\pi\colon S^3\to S^2$ is not isomorphic to the trivial principal $U(1)$-bundle.
>
> Write $X=S^2=\{(z,t)\in\mathbb{C}\times\mathbb{R}:|z|^2+t^2=1\}$. Let $D=\{(z,t)\in X:t\geq0\}$ be the closed northern cap and $X\setminus D^\circ=\{(z,t)\in X:t\leq0\}$ the closed southern cap; the two caps are closed coordinate discs (stereographic projection from the opposite pole is a diffeomorphism onto a round disc), and they meet exactly along the equator $S=\{(z,0):|z|=1\}\cong S^1$.
>
> The Hopf bundle is trivial over $U_1=S^2\setminus\{(0,-1)\}\supset D$ (via the section $s_1$) and over $U_2=S^2\setminus\{(0,1)\}\supset X\setminus D^\circ$ (via $s_2$), and across a collar of $S$ its transition function is $g_{12}(z,t)=z/|z|$. By [[Thm - Clutching Construction for Bundles over a Closed Manifold|the clutching construction]] (part (b)), the Hopf bundle is isomorphic to $P_g$ for the clutching map $g=g_{12}|_S\colon S\to U(1)$.
>
> On $S$ we have $|z|=1$, so $g(z,0)=z/|z|=z$; identifying $S\cong S^1$ and the fibre group with $U(1)$, $g$ is the identity map $z\mapsto z$. By part (e) of [[Thm - Winding Number of a Map from the Circle to U(1)|the winding-number theorem]], $w(g)=1$ (equivalently, $g^{-1}dg=i\,d\theta$ gives $w(g)=\tfrac{1}{2\pi i}\int_0^{2\pi}i\,d\theta=1$).
>
> Suppose $P_g$ were trivial. By the triviality clause of the clutching construction, $g=(a|_S)(b|_S)$ for smooth $a\colon X\setminus D^\circ\to U(1)$ and $b\colon D\to U(1)$. Since $D$ is a disc, $b|_S$ extends over a disc, so $w(b|_S)=0$ by part (d) of the winding-number theorem; since the complement $X\setminus D^\circ$ is *also* a disc, $a|_S$ likewise extends over a disc, so $w(a|_S)=0$. As $U(1)$ is abelian, part (b) gives $w(g)=w(a|_S)+w(b|_S)=0$, contradicting $w(g)=1$.
>
> Hence $P_g$, and therefore the Hopf bundle, is not trivial. $\blacksquare$

> [!warning] Illegal but tempting shortcut: "$g=z/|z|$ is nowhere zero and smooth on the whole overlap, so it extends and the bundle is trivial."
> The transition function $g_{12}(z,t)=z/|z|$ is indeed smooth on all of the *overlap* $U_{12}=S^2\setminus\{(0,\pm1)\}$, and one is tempted to conclude that it "extends" and the bundle is therefore trivial. This confuses two different extension problems. Triviality does not ask whether $g_{12}$ extends over the overlap — it already lives there — it asks whether the *equatorial clutching map* $g=g_{12}|_S$ factors as a product of boundary values of maps defined on the two *caps*. On the punctured overlap $U_{12}$ the formula $z/|z|$ cannot be extended smoothly across either pole (it has no limit as $(z,t)\to(0,\pm1)$, since $z/|z|$ has no limit as $z\to0$), which is exactly why the bundle is patched rather than trivial. The extension that would make the argument legal is a smooth extension of $b|_S$ over a *disc*; that is available for each cap separately as a factor, and the winding-number obstruction shows the product of two such factors can never reproduce the identity map of the circle.

> [!note]- Independent sanity check via the power-map family
> The same machinery classifies all the bundles one can clutch over $S^2$ with abelian structure group $U(1)$: the bundle $P_{g_k}$ for $g_k(z)=z^k$ has $w(g_k)=k$ (part (e)), and the argument above shows $P_{g_k}$ is trivial if and only if $k=0$. The Hopf bundle sits at $k=1$, the first nontrivial member. This is consistent with the classification of principal $U(1)$-bundles over $S^2$ by a single integer, developed downstream in the chapter; the winding number computed here is that integer for the Hopf bundle. That the trivial bundle sits at $k=0$ and the Hopf bundle at $k=1$ is exactly what one expects, and it confirms that no sign convention could accidentally place the Hopf bundle at $k=0$.

**The alternative proof, through the absence of a section.** Bär's own route to nontriviality does not compute a winding number at all; it uses the section–triviality correspondence. By [[Thm - Sections of a Principal Bundle and Triviality|the section–triviality theorem]] a principal bundle is trivial if and only if it has a global section, so it suffices to show the Hopf bundle has no global section. Bär argues that a global section would give a diffeomorphism $S^3\cong S^2\times S^1$, whence $\{e\}=\pi_1(S^3)\cong\pi_1(S^2)\times\pi_1(S^1)=\{e\}\times\mathbb{Z}=\mathbb{Z}$, a contradiction. This reasoning relies on facts about the fundamental group ($\pi_1(S^3)$ and $\pi_1(S^2)$ are trivial, $\pi_1(S^1)=\mathbb{Z}$, and $\pi_1$ of a product splits) that are developed only later in the series; the sibling theorem [[Thm - The Hopf Bundle is Nontrivial]] proves the no-section statement independently — a global section would produce a diffeomorphism $S^3\cong S^2\times S^1$, but $H^1_{\mathrm{dR}}(S^2\times S^1)\neq0$ while $H^1_{\mathrm{dR}}(S^3)=0$ — so the honest way to run this alternative in the vault is to cite that proved page. The winding-number proof given above is self-contained within Gauge Theory III and does not need any homotopy or de Rham input beyond the winding-number theorem.

---

# Key Takeaways

**When a bundle is glued from two contractible pieces, all of its topology is one map into the structure group, and the right homotopy invariant of that map decides triviality.** This is the reusable principle behind the whole exercise: a bundle over $S^n$ (or over any space cut into two discs meeting along an $S^{n-1}$) is completely determined by its clutching map $g\colon S^{n-1}\to G$ up to the equivalence $g\mapsto(a|_S)g(b|_S)$, and the bundle is trivial exactly when $g$ lies in the trivial class. The trigger condition to look for is a base that decomposes into two contractible patches; the moment you see it, stop thinking about the total space and start computing an invariant of the overlap map. For $G=U(1)$ over $S^2$ that invariant is the integer winding number, and it is complete; for $G=SU(2)$ over $S^4$ the analogous invariant is the degree of $g\colon S^3\to SU(2)$, which is the second Chern number. The transferable diagnostic is: nonzero clutching invariant $\Rightarrow$ nontrivial bundle, and the invariant is computed from $g$ alone, never from the total space.

**A multiplicative triviality condition becomes a computable additive one exactly when the structure group is abelian, and that is why $U(1)$ is the easy case.** The clutching triviality criterion $g=(a|_S)(b|_S)$ is a statement about factoring a group-valued map; on its own it is intractable, because deciding whether such $a,b$ exist is a nonlinear problem. Abelianness collapses it: the winding number is a group homomorphism from $(\text{smooth maps }S^1\to U(1),\ \text{pointwise product})$ to $(\mathbb{Z},+)$, so $w(g)=w(a|_S)+w(b|_S)$, and the factorisation forces $w(g)$ into the image of boundary values, which is $\{0\}$. Recognise this pattern whenever a triviality or exactness condition is phrased as a product or composite of pieces and the ambient group is abelian: apply the homomorphism that linearises the product and read off a numerical obstruction. When the group is nonabelian the winding number is replaced by a degree that is still additive under products for the relevant maps (as for $SU(2)$), but the additivity then requires a genuine computation with the Maurer–Cartan form rather than a one-line homomorphism property, and one must be careful about which invariant survives conjugation.

**The complement of a disc in $S^2$ is again a disc, and this "two-disc" symmetry is the load-bearing geometric fact, not a cosmetic one.** The argument would collapse if only the clutching disc $D$ contributed a vanishing winding number: one needs *both* $w(a|_S)=0$ and $w(b|_S)=0$, and the second comes from $D$ while the first comes from the complementary cap $X\setminus D^\circ$. The reason both vanish is that $S^2$ is the union of two discs, so the complement of a coordinate disc is not some complicated surface-with-boundary but another disc, over which any $U(1)$-valued map extends and hence has zero boundary winding. On a base where this fails — for instance a coordinate disc in a torus $T^2$, whose complement is a once-punctured torus, not a disc — the complement's boundary value can carry a nonzero winding number, the invariant $w(g)$ no longer detects triviality by itself, and the classification of bundles is correspondingly richer. The diagnostic to carry away: before trusting a clutching-invariant argument, check that *the complement of the disc is contractible*, or at least that boundary values of maps defined on it are forced into the trivial class; on spheres this is automatic, elsewhere it is a hypothesis that must be verified. This exercise is the cleanest instance of the pattern, and it pairs naturally with [[Ex - A Map Extending over a Bounding Manifold has Degree Zero]], which isolates the disc-extension vanishing as a standalone fact, and with [[Thm - The Hopf Bundle is Nontrivial]], which reaches the same conclusion through cohomology rather than winding numbers.
