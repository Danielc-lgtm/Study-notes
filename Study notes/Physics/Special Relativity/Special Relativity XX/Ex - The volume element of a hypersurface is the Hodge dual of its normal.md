---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Volume, Area, Length Elements and Flux Integrals"
  - "Def - The Hodge Star"
  - "Def - The Levi-Civita Tensor"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$ and signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$.

1. Let $\mathscr{V}$ be a hypersurface with future unit normal $\vec{n}$. The volume-element 3-form is defined as $\epsilon_{\mathscr{V}} = \epsilon(\vec{n}, \cdot, \cdot, \cdot)$. Compute its components $(\epsilon_{\mathscr{V}})_{\alpha\beta\gamma}$ and compare with the component formula for the Hodge dual $\star\underline{n}$ of the normal's 1-form, thereby proving $\epsilon_{\mathscr{V}} = \star\underline{n}$.
2. In adapted coordinates, derive the explicit volume element $\mathrm{d}V = \epsilon_{\mathscr{V}}(\mathrm{d}\vec{\ell}_1, \mathrm{d}\vec{\ell}_2, \mathrm{d}\vec{\ell}_3) = n^0\sqrt{|g|}\,\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3$.
3. Apply this to the sphere $t = 0$, $r = R$ in spherical coordinates (a spacelike 2-surface — but here treat the *spatial ball's boundary as a hypersurface of the $t=0$ slice* by using the 3D Euclidean restriction; more simply, apply part 2 to the hyperplane $t=0$ and confirm $\mathrm{d}V = r^2\sin\theta\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi$). Recover the volume of a ball of radius $R$.
4. Verify the corollary "$\mathrm{vol}(\mathscr{V}) = \Phi_{\mathscr{V}}(\vec{n})$": the volume of a hypersurface equals the flux of its own unit normal through it.

**Recall:**

The volume element of a hypersurface and its relation to the Hodge star are defined as follows.

![[Def - Volume, Area, Length Elements and Flux Integrals#The Definition]]

The Hodge dual of a 1-form $\underline{n}$ (components $n_\mu$) is the 3-form $\star\underline{n}$ with $(\star\underline{n})_{\alpha\beta\gamma} = n^\mu\epsilon_{\mu\alpha\beta\gamma}$, where $n^\mu = \eta^{\mu\nu}n_\nu$ and $\epsilon$ is the Levi-Civita tensor with $\epsilon_{0123} = \sqrt{|g|}$ in a right-handed coordinate basis.

---

# Convergent Strategy

**Problem class.** A *structural-identity* problem: prove that the geometrically-motivated volume element coincides with an algebraically-defined Hodge dual. It establishes the uniform "$\epsilon_{\mathscr{V}}$ = Hodge dual of the normals" recipe of [[Def - Volume, Area, Length Elements and Flux Integrals]].

**Assumption pattern.** A hypersurface with a unit normal, and the component definitions of $\epsilon(\vec{n},\cdot,\cdot,\cdot)$ and $\star\underline{n}$. The signpost is that both objects are 3-forms built from the single vector $\vec{n}$ and the Levi-Civita tensor, so they should agree — the exercise is to see the agreement is *exact*, by definition of the Hodge star.

**Theorem routing.** Part 1 is a direct component comparison. Part 2 evaluates the 3-form on the coordinate triad $\mathrm{d}\vec{\ell}_i = \mathrm{d}x^i\vec{e}_i$. Part 3 specialises to a familiar metric. Part 4 uses the flux definition $\Phi_{\mathscr{V}}(\vec{n}) = \int\star\underline{n}$ together with $\vec{n}\cdot\vec{n} = \pm1$.

**Key decision point.** The crux is recognising that "$\epsilon$ with one slot filled by $\vec{n}$" *is* the definition of the Hodge star of $\underline{n}$ — so the identity is not a computation to be ground out but a definitional match, once the index conventions are aligned. Getting the index placement right (the $\mu$ on $\vec{n}$ being raised) is the only subtlety.

---

# Legal Operations Used

1. **Operation 3 from the topic page (build the submanifold's volume form from its normals).** The exercise establishes the foundational instance of this operation — that the hypersurface volume form is $\star\underline{n}$.

2. **Operation 8 from the topic page (compute the normal as the metric dual of a coordinate gradient).** Implicitly, the normal $\vec{n} = \vec{e}_0$ to the $t=0$ slice is the (normalised) dual of $\mathrm{d}t$, which is what gives $n^0 = 1$ in part 3.

3. **Operation 4 from the topic page (express a flux as the integral of a Hodge dual).** Part 4 uses $\Phi_{\mathscr{V}}(\vec{n}) = \int\star\underline{n}$ to identify the volume with a flux.

---

# Hints

> [!note]- Hint 1
> Write out $(\epsilon_{\mathscr{V}})_{\alpha\beta\gamma} = \epsilon(\vec{n}, \vec{e}_\alpha, \vec{e}_\beta, \vec{e}_\gamma) = n^\mu\epsilon_{\mu\alpha\beta\gamma}$ (the first slot contracts $\vec{n} = n^\mu\vec{e}_\mu$ into $\epsilon$). This is *literally* the component formula for $\star\underline{n}$. So $\epsilon_{\mathscr{V}} = \star\underline{n}$.

> [!note]- Hint 2
> Evaluate on the coordinate triad: $\mathrm{d}V = (\epsilon_{\mathscr{V}})_{\alpha\beta\gamma}(\mathrm{d}x^1\delta^\alpha_1)(\mathrm{d}x^2\delta^\beta_2)(\mathrm{d}x^3\delta^\gamma_3) = (\epsilon_{\mathscr{V}})_{123}\,\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3$. Now $(\epsilon_{\mathscr{V}})_{123} = n^\mu\epsilon_{\mu123} = n^0\epsilon_{0123} = n^0\sqrt{|g|}$.

> [!note]- Hint 3
> For the hyperplane $t=0$ in spherical coordinates, $\vec{n} = \vec{e}_0$ (normalised, $n^0=1$) and $\sqrt{|g|} = r^2\sin\theta$. So $\mathrm{d}V = r^2\sin\theta\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi$, and integrating over $r\le R$ gives $\frac{4}{3}\pi R^3$.

> [!note]- Hint 4
> Take $\vec{v} = \vec{n}$ in the flux formula: $\Phi_{\mathscr{V}}(\vec{n}) = \pm\int\vec{n}\cdot\vec{n}\,\mathrm{d}V = \pm\int(\pm1)\,\mathrm{d}V = \int\mathrm{d}V = \mathrm{vol}(\mathscr{V})$.

---

# Solution

The identity $\epsilon_{\mathscr{V}} = \star\underline{n}$ is a definitional match: filling one slot of $\epsilon$ with $\vec{n}$ is exactly the component recipe for the Hodge star of $\underline{n}$. From there the explicit volume element, the sphere/ball check, and the flux corollary all follow by evaluation.

**Step 1: $\epsilon_{\mathscr{V}} = \star\underline{n}$.**

> [!note]- Derivation
> The volume-element 3-form is $\epsilon_{\mathscr{V}} = \epsilon(\vec{n}, \cdot, \cdot, \cdot)$. Its components are obtained by feeding coordinate basis vectors into the open slots:
> $$(\epsilon_{\mathscr{V}})_{\alpha\beta\gamma} = \epsilon(\vec{n}, \vec{e}_\alpha, \vec{e}_\beta, \vec{e}_\gamma) = n^\mu\,\epsilon(\vec{e}_\mu, \vec{e}_\alpha, \vec{e}_\beta, \vec{e}_\gamma) = n^\mu\,\epsilon_{\mu\alpha\beta\gamma},$$
> using $\vec{n} = n^\mu\vec{e}_\mu$ and multilinearity. The Hodge dual of the 1-form $\underline{n}$ (with $n^\mu = \eta^{\mu\nu}n_\nu$) is, by definition, the 3-form with components $(\star\underline{n})_{\alpha\beta\gamma} = n^\mu\epsilon_{\mu\alpha\beta\gamma}$. These are *identical*, so
> $$\epsilon_{\mathscr{V}} = \star\underline{n}.$$
> The volume element of a hypersurface is the Hodge dual of its normal's 1-form — not by a computation, but because "contract $\vec{n}$ into the first slot of $\epsilon$" is precisely the operation the Hodge star performs on $\underline{n}$.

**Step 2: $\mathrm{d}V = n^0\sqrt{|g|}\,\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3$.**

> [!note]- Derivation
> In adapted coordinates, the infinitesimal tangent vectors are $\mathrm{d}\vec{\ell}_i = \mathrm{d}x^i\vec{e}_i$ ($i=1,2,3$, no sum). Evaluating the 3-form,
> $$\mathrm{d}V = \epsilon_{\mathscr{V}}(\mathrm{d}\vec{\ell}_1, \mathrm{d}\vec{\ell}_2, \mathrm{d}\vec{\ell}_3) = (\epsilon_{\mathscr{V}})_{123}\,\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3 .$$
> From Step 1, $(\epsilon_{\mathscr{V}})_{123} = n^\mu\epsilon_{\mu123}$, and $\epsilon_{\mu123}$ is nonzero only for $\mu=0$, giving $n^0\epsilon_{0123} = n^0\sqrt{|g|}$. Hence
> $$\mathrm{d}V = n^0\sqrt{|g|}\,\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3 .$$
> The volume element is the time component of the normal times the metric volume factor.

**Step 3: The volume of a ball of radius $R$ is $\frac{4}{3}\pi R^3$.**

> [!note]- Derivation
> Take the hyperplane $\Sigma$ ($t=0$) in inertial spherical coordinates, with future timelike unit normal $\vec{n} = \vec{e}_0$, so $n^0 = 1$. The metric factor is $\sqrt{|g|} = r^2\sin\theta$. By Step 2,
> $$\mathrm{d}V = 1\cdot r^2\sin\theta\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi = r^2\sin\theta\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi,$$
> the standard spatial volume element. Integrating over the ball $r\le R$:
> $$\mathrm{vol}(B_R) = \int_0^R r^2\,\mathrm{d}r\int_0^\pi\sin\theta\,\mathrm{d}\theta\int_0^{2\pi}\mathrm{d}\varphi = \frac{R^3}{3}\cdot2\cdot2\pi = \frac{4}{3}\pi R^3 .$$
> The abstract $\star\underline{n}$ machinery reproduces the elementary ball volume. (The bounding *sphere* $r=R$ is a 2-surface; its area element $R^2\sin\theta\,\mathrm{d}\theta\,\mathrm{d}\varphi$ is computed by the analogous area construction in [[Ex - Length, area, and volume elements in spherical coordinates]].)

**Step 4: $\mathrm{vol}(\mathscr{V}) = \Phi_{\mathscr{V}}(\vec{n})$.**

> [!note]- Derivation
> Take the vector field $\vec{v} = \vec{n}$ (the unit normal itself) in the flux formula $\Phi_{\mathscr{V}}(\vec{v}) = \pm\int_{\mathscr{V}}\vec{v}\cdot\vec{n}\,\mathrm{d}V$. The inner product is $\vec{n}\cdot\vec{n} = \pm1$ (the same sign as in the flux convention: $+1$ for a spacelike hypersurface with timelike normal, with the flux sign $-$; the two signs combine to $+$). Concretely, $\Phi_{\mathscr{V}}(\vec{n}) = \pm\int(\pm1)\,\mathrm{d}V = \int_{\mathscr{V}}\mathrm{d}V = \mathrm{vol}(\mathscr{V})$. Equivalently, via $\Phi_{\mathscr{V}}(\vec{n}) = \int_{\mathscr{V}}\star\underline{n} = \int_{\mathscr{V}}\epsilon_{\mathscr{V}} = \mathrm{vol}(\mathscr{V})$ using Step 1. The volume of a hypersurface is the flux of its own unit normal through it — a clean consistency check tying the flux formula to $\epsilon_{\mathscr{V}} = \star\underline{n}$.

> [!note]- Complete formal solution
> The volume-element 3-form has components $(\epsilon_{\mathscr{V}})_{\alpha\beta\gamma} = \epsilon(\vec{n},\vec{e}_\alpha,\vec{e}_\beta,\vec{e}_\gamma) = n^\mu\epsilon_{\mu\alpha\beta\gamma}$, which is exactly the component formula for $\star\underline{n}$, so $\epsilon_{\mathscr{V}} = \star\underline{n}$. Evaluating on the coordinate triad, $\mathrm{d}V = (\epsilon_{\mathscr{V}})_{123}\mathrm{d}^3x = n^0\epsilon_{0123}\mathrm{d}^3x = n^0\sqrt{|g|}\,\mathrm{d}x^1\mathrm{d}x^2\mathrm{d}x^3$. For the $t=0$ hyperplane in spherical coordinates ($n^0=1$, $\sqrt{|g|}=r^2\sin\theta$), $\mathrm{d}V = r^2\sin\theta\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi$, so $\mathrm{vol}(B_R)=\int_0^R r^2\mathrm{d}r\int_0^\pi\sin\theta\,\mathrm{d}\theta\int_0^{2\pi}\mathrm{d}\varphi = \frac{4}{3}\pi R^3$. Finally, taking $\vec{v}=\vec{n}$ gives $\Phi_{\mathscr{V}}(\vec{n}) = \int\star\underline{n} = \int\epsilon_{\mathscr{V}} = \mathrm{vol}(\mathscr{V})$. $\blacksquare$

---

# Key Takeaways

**The volume element of a hypersurface is the Hodge dual of its normal, by definition of the Hodge star.** The identity $\epsilon_{\mathscr{V}} = \star\underline{n}$ is not a coincidence to be verified by grinding through components — it is what the Hodge star *is*. The Hodge star of a 1-form is precisely "fill the first slot of the volume form $\epsilon$ with the dual vector and leave the rest open", which is exactly the geometric construction of the hypersurface volume element. The trigger to recognise this is any volume/area element built by contracting normals into $\epsilon$: it is automatically a Hodge dual. This unifies the three constructions of the chapter — $\star\underline{n}$ for hypersurfaces, $\star(\underline{n}\wedge\underline{s})$ for surfaces, $\pm\underline{u}$ for curves — into the single statement "Hodge-star the wedge of the unit normals", and it is why the Hodge star, an apparently abstract algebraic operation, is the natural language for integration over submanifolds.

**The factor $n^0$ in $\mathrm{d}V = n^0\sqrt{|g|}\,\mathrm{d}^3x$ is the projection of the four-volume onto the slice.** The hypersurface volume element carries not just $\sqrt{|g|}$ but also the time component $n^0$ of the normal, and this has a clean meaning: it is the factor by which the four-volume of the box erected on the normal projects down to the three-volume of the base. When the slice is a constant-time hyperplane with $\vec{n} = \vec{e}_0$, $n^0 = 1$ and the volume element is the naive $\sqrt{|g|}\,\mathrm{d}^3x$; but for a *tilted* or *boosted* slice $n^0\ne 1$, and the $n^0$ factor correctly accounts for the slice's orientation in spacetime. The transferable point is that a hypersurface's volume element depends on *how the slice sits in spacetime* (through $\vec{n}$), not just on the intrinsic coordinates — which is the geometric content of the normal appearing in the formula, and the seed of how different observers' "space at an instant" relate.

**"Volume of a slice = flux of its normal" is the consistency check that ties the whole construction together.** The corollary $\mathrm{vol}(\mathscr{V}) = \Phi_{\mathscr{V}}(\vec{n})$ looks like a curiosity but is a structural check: it confirms that the flux formula $\Phi = \int\star\underline{v}$ and the volume element $\epsilon_{\mathscr{V}} = \star\underline{n}$ are mutually consistent, since taking $\vec{v} = \vec{n}$ in the flux must return the volume. The diagnostic use is that any error in the flux convention or the volume element would break this identity, so it is a one-line audit of both. More conceptually, it says the unit normal is the field whose flux through the slice counts the slice's own size — the normal is "the field of unit crossing", and integrating its crossing gives the area swept. This idea recurs whenever a measure is realised as a flux, and recognising the volume-as-normal-flux pattern is a portable check on flux computations.
