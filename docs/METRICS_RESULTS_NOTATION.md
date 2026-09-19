# Metrics, numerical results, and equation-notation crosswalk

**Status:** evidence-extraction template, not a completed numerical meta-analysis. The existing papers.csv records reported metric names but not source-verified numerical results. Empty results are **not reported / not yet verified**, never zero.

## Per-experiment results

Extract one row per paper × dataset × task × model × metric × evaluation setting in [results_extraction.csv](../catalogue/results_extraction.csv). Include source DOI, PDF page/table/figure, original numerical value (mean ± SD/CI if provided), comparison baseline, metric definition, resolution, horizon, geography, sample count, train/test split, normalization, physical unit, conditions, EMA, sampler, NFE, seeds and compute.

**Never compare absolute numerical metric values across datasets or scaling without a justified conversion.** Preserve published values rather than estimating them from charts; if figure digitization is necessary, mark as approximate and document the procedure. Compare only methods evaluated under a shared experiment. Do not treat notebook observations as published literature results.

### Core metric interpretation

| Aspect | Metrics and necessary metadata |
|---|---|
| Statistical fidelity | Wasserstein / EMD (1D vs multivariate, units, aggregation), MMD (kernel, bandwidth, estimator), KS, quantiles. Critic/WGAN training loss is NOT post-hoc Wasserstein evaluation. |
| Temporal dynamics | DTW (normalization, warping constraint, scale), ACF, PSD, peak timing/duration, ramp rates, load-duration curves. |
| Predictive utility | TSTR vs TRTR, both with same downstream learner, target, features, split and downstream metric (R², MAE, RMSE etc.). TSTR alone is a protocol, not a scalar. |
| Diversity/privacy | Coverage, distinguishability, nearest-neighbour and membership-inference tests where reported. |
| Computational cost | Training time, inference time, NFE, hardware, seeds and number of independent runs. |
| Load realism | P95/P99/P99.5, maxima, peak amplitude/frequency, physical constraints, daily energy, multiresolution consistency; report native units and conditioning scope. |

## Equation-notation concordance

Yang et al., A Survey on Diffusion Models for Time Series and Spatio-Temporal Data, ACM Computing Surveys 58(8), 2026, Sections 2.3.1–2.3.2, use k/K for discrete diffusion and t/T for continuous SDEs. Other series papers may use t for the observation index. Compare *meaning*, not letter choices.

| Quantity | Canonical notation for our survey | Watch for in source papers |
|---|---|---|
| Observation time within electricity sequence | τ; series length L | t or i: do not confuse with diffusion timestep. |
| Discrete noise level / total steps | k / K | t / T in other DDPM papers. |
| Continuous SDE time | s | t or τ elsewhere. |
| Step noise variance | β_k | σ²; determine whether σ means SD or variance. |
| Single-step signal retention | α_k = 1 − β_k | a_k. |
| Cumulative signal retention | ᾱ_k = ∏_(i=1)^k α_i | other alpha/SNR parameterizations; not identical to α_k. |
| Network target | ε_θ(x_k,k,c) | score s_θ, clean sample x0_hat, velocity v_θ: distinct parameterizations. |
| Conditioning variables | c | y, h, metadata; specify what is available at inference. |
| WGAN gradient penalty | λ_GP | λ(t) may mean diffusion loss weighting. |
| EMA decay | γ_EMA | β_EMA is not noise β_k or Adam β1,β2. |

**Worked equivalence:** a single DDPM sample has x_k = √(ᾱ_k) x_0 + √(1−ᾱ_k) ε. For an electrical series, annotate its observation index explicitly as x_(τ,k) = √(ᾱ_k) x_(τ,0) + √(1−ᾱ_k) ε_(τ,k). Reindexing does not create a new method.

Prioritize notational differences that hide changes in the objective, sampler, units or conditioning, not cosmetic differences. Quote an original equation faithfully before giving a harmonized form; flag possible source inconsistencies rather than silently changing them.

## Publication-ready tables

1. Landscape: bibliographic metadata, family, task, native resolution, geography, conditioning.
2. Metrics: each paper's exact metric definition, scaling, aggregation and source location.
3. Results: published values and within-study baselines; mean ± SD/CI where available, no cross-paper ranking.
4. Equations: original notation → canonical notation; genuine methodological differences.
5. Gaps: peak evaluation, transfer, multiresolution, privacy, compute, reproducible runs.

**Source boundary:** the supplied Yang survey documents diffusion equations and a task taxonomy but does not offer one directly comparable table of numerical metrics for synthetic electricity-load studies. Exact metric values must be checked against the original papers.
