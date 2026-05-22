---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Least Squares Data Fitting"
tags: [algebra, linear-algebra, applied, data-fitting, machine-learning]
---

# Notation

The data set is partitioned: a *training set* $\mathcal{T}_{\text{train}}$ used to fit the model parameters $\hat{\theta}$, and a *test set* (or *validation set*) $\mathcal{T}_{\text{test}}$ used only to evaluate the trained model. Common split ratios are 80/20 or 90/10. The *training error* is the RMS prediction error on $\mathcal{T}_{\text{train}}$; the *test error* is the RMS prediction error on $\mathcal{T}_{\text{test}}$. *Cross-validation* (typically 5-fold or 10-fold) extends this by partitioning the data into $k$ folds and rotating which fold is held out as test. The remaining $k-1$ folds train the model; the held-out fold tests it. This yields $k$ estimates of test error and a check for parameter stability across folds.

---

# Axiom Motivation

The least squares data-fitting framework gives you a way to *fit* a model to a given dataset — but it does not tell you whether the fitted model will *work on new data*. This distinction is the difference between *training error* (how well the model fits the data you used to train it) and *generalization error* (how well it predicts on data you have not seen). The training error can be driven to zero by using a sufficiently rich model — interpolation at $N$ data points with $N$ parameters achieves training error zero. But this tells you nothing about the model's behavior on the $(N+1)$th, $(N+2)$th, etc. data points.

The fundamental difficulty is that we cannot directly measure generalization error: by definition, it is the error on data we haven't seen. We need some *proxy* for it that we *can* measure.

The proxy is *out-of-sample validation*: hold back some of the data from training, treat it as if it were unseen, and use the model's performance on this held-back data as an estimate of generalization performance. This is the *validation principle*. It rests on one essential assumption: *the held-back data is representative of future data*. If the data are i.i.d. samples from a distribution, this holds; if the distribution shifts between when the model is trained and when it is deployed (a common failure mode in real-world ML, especially in finance), it does not.

The choice to hold back 10-20% of the data is a compromise. Smaller test sets give noisier estimates of test error; larger test sets give better estimates but leave less data for training. The 80/20 split is a rough empirical compromise. Cross-validation extends this: by rotating which fold is held out, every data point gets to participate in both training and testing (in different fold rotations), at the cost of training the model $k$ times. The cross-validation error is the average of $k$ test errors, smoother than a single train/test split and with the bonus diagnostic of comparing fold-to-fold parameter stability.

Why not just train on all the data and use a *theoretical* bound on generalization error (e.g., from PAC theory or VC dimension)? Three reasons. First, such bounds are typically very loose in practice — they describe worst-case behavior, not typical behavior. Second, they require assumptions (smoothness, boundedness, finite hypothesis class) that may not hold in real applications. Third, the empirical validation procedure is *direct*: it estimates the actual quantity we care about, without assumptions about the data distribution beyond "future data looks like past data." This is the same reason Bayesians and frequentists disagree but both use validation: validation is the lowest-assumption way to estimate generalization performance.

The *overfitting diagnostic* falls out directly. If training error is much smaller than test error, the model has overfit — it has memorized noise in the training data that does not generalize. If both are similar, the model has good *generalization ability*, regardless of whether it has good *prediction quality*. If both are large, the model is underfit — it lacks the capacity to capture the patterns in the data, even on the training set. The three cases — underfit, healthy, overfit — are diagnosed by the *gap* between training and test error, and the *level* of each.

The standard remedy for overfitting is one of: (i) reduce model complexity (fewer basis functions), (ii) add regularization (penalize $\|\theta\|^2$ — see [[Def - Regularized Least Squares]]), (iii) collect more data. Each addresses the bias-variance tradeoff differently. Validation is the diagnostic that tells you which approach is needed.

---

# The Definition

> **Definition (Validation, Training and Test Error).** Given a dataset $\{(x^{(i)}, y^{(i)})\}_{i=1}^N$, partition it into a *training set* $\mathcal{T}_{\text{train}}$ and a *test set* $\mathcal{T}_{\text{test}}$ (disjoint, $\mathcal{T}_{\text{train}} \cup \mathcal{T}_{\text{test}}$ = full dataset). Fit the model parameters $\hat{\theta}$ by minimizing the LS objective on $\mathcal{T}_{\text{train}}$ alone:
> $$\hat{\theta} = \arg\min_\theta \sum_{i \in \mathcal{T}_{\text{train}}} (y^{(i)} - \hat{f}_\theta(x^{(i)}))^2.$$
> The *training error* (RMS) is
> $$\mathrm{RMS}_{\text{train}} = \sqrt{\frac{1}{|\mathcal{T}_{\text{train}}|} \sum_{i \in \mathcal{T}_{\text{train}}} (y^{(i)} - \hat{f}_{\hat\theta}(x^{(i)}))^2},$$
> and the *test error* (RMS) is the same quantity computed over $\mathcal{T}_{\text{test}}$. The model is said to be:
> - *Overfit* if $\mathrm{RMS}_{\text{train}} \ll \mathrm{RMS}_{\text{test}}$.
> - *Underfit* if both are large (compared to the optimal achievable on this data).
> - *Well-calibrated* if both are similar and small.
>
> *$k$-fold cross-validation* partitions the dataset into $k$ disjoint folds $F_1, \ldots, F_k$. For each $j \in \{1, \ldots, k\}$, fit the model on $\bigcup_{i \neq j} F_i$ and compute the test error on $F_j$. The cross-validation error is the average of the $k$ test errors.

---

# Relate to Other Fields / Compression

**True name:** validation is *out-of-sample estimation of generalization error*. The held-out test set is a *proxy* for future data; the test error is an *estimator* of the future RMS prediction error. The estimator is unbiased when the data are i.i.d., and approximately unbiased for non-i.i.d. data that is at least *stationary* (distribution does not shift between training and testing).

This is the same construction as:
- **Bootstrap** in statistics: resampling with replacement to estimate sampling distribution of a statistic; the bootstrap sample plays the role of the training set, the original sample plays the role of the test set.
- **Backtesting** in finance and trading: testing a strategy on historical data not used to design it. This is exactly validation applied to portfolio optimization (see [[Ex - Portfolio optimization as constrained LS]] for the financial setup); the same overfitting concerns apply.
- **Hold-out validation** in machine learning: the canonical version of this concept; cross-validation is its generalization.

---

# Examples / Corollaries

*Example 1 (the canonical overfit signature).* Fit polynomials of degree 0, 1, ..., 20 to 100 noisy data points; use 80 points as training and 20 as test. Training error monotonically decreases with degree (more parameters always reduce training residuals). Test error follows a U-shape: high for low-degree models (underfit), low at some intermediate degree (typically 4-8), high again for high-degree models (overfit). The optimal model is at the test-error minimum. See [[Ex - Polynomial fitting and overfitting]].

*Example 2 (cross-validation parameter stability).* For a regression model with 8 coefficients, run 5-fold cross-validation and examine the 5 sets of fitted coefficients. If the coefficients are similar across folds, the model is *stable* — small perturbations in the training data do not dramatically change the model. If the coefficients vary wildly, the model is *unstable*, which is often (though not always) a sign of overfitting or near-collinearity in the features.

*Example 3 (a "good generalization, bad prediction" model).* The model $\hat{f}(x) = 0$ (constant zero) achieves the same RMS error on training and test sets, equal to $\mathrm{RMS}(y^d_{\text{train}})$ and $\mathrm{RMS}(y^d_{\text{test}})$ respectively. These are approximately equal for an i.i.d. dataset, so this model has *good generalization* — it predicts about as well on training as on test. But both errors are large; the model is useless. The point is that low generalization gap is *not* the same as good prediction; both matter.

*Example 4 (is NOT a valid validation — using test data to choose hyperparameters).* If you split into train/test, then for each value of a hyperparameter $\lambda$ you (a) fit on train, (b) evaluate on test, (c) pick the $\lambda$ that minimizes test error — this corrupts the test set. You have used the test set to *choose* $\lambda$, so its error estimate is now optimistic. The correct procedure is a *three-way split* (train / validation / test): use train to fit, validation to choose $\lambda$, and test (used only at the end) to estimate final generalization performance. This nested-validation pitfall is one of the most common methodological errors in applied ML.

**Calibration check.** Verify: (i) for an i.i.d. sample with equal-sized train and test sets, the expected training and test errors of the fitted LS model are equal in expectation (but differ in variance); (ii) for a model that is fit *only on the training data*, the training error is a downward-biased estimator of the population error (because the parameters were chosen to minimize it), while the test error is an unbiased estimator; (iii) cross-validation with $k = N$ (leave-one-out) gives an unbiased but high-variance estimate; $k = 5$ or $k = 10$ gives biased but lower-variance estimates.

---

# Unlocked by This

> [!tip] Bias-Variance Tradeoff *(from Statistical Learning)*
> Validation is the empirical diagnostic for the **bias-variance tradeoff**. The training error tracks bias (systematic error); test error tracks bias plus variance. The optimal model complexity is the one minimizing test error. Sweeping the complexity parameter (polynomial degree, number of features, regularization strength) and plotting train/test errors against complexity gives the canonical U-shaped curve. This is the *theoretical content* of validation — the procedural recipe of "split data, evaluate held-out" is the practical realization of the bias-variance principle.

> [!tip] Cross-Validation and Model Selection *(from Machine Learning)*
> Cross-validation generalizes the train/test split to a procedure that (i) yields a more reliable estimate of test error (by averaging over folds), (ii) uses all data for both training and testing (across different folds), and (iii) provides a parameter-stability check (by comparing fold-to-fold parameter estimates). It is the standard tool for choosing hyperparameters in any LS-based or ML model, from regularization strength to network architecture. The natural extensions are **nested CV** (for honest hyperparameter tuning) and **time-series CV** (for non-i.i.d. data, where the future-from-past constraint must be preserved).

> [!tip] Backtesting *(from Math Finance)*
> In quantitative finance, validation is called **backtesting** — testing a trading strategy on historical data that was not used to design it. Pitfalls (look-ahead bias, survivorship bias, data snooping) all arise from violations of the train/test independence assumption. The portfolio optimization problem in §XI.4 is a least squares problem and its overfitting / generalization concerns are exactly those addressed by validation here. The financial-domain warning that "past performance is no guarantee of future performance" is exactly the i.i.d. assumption that validation requires.
