# Quality control: prior art and proposed validation

**The literature already evaluates synthetic load.** The defensible gap is inconsistent and non-standardized protocols, limited joint testing of fidelity/dynamics/utility/privacy/conditionality and weak cross-domain comparability, **not** the absence of Wasserstein, DTW, MMD or TSTR.

| Publication / date | Already evaluates | Caution | Source |
|---|---|---|---|
| Turowski et al. · Aug 2024 online, Dec issue | Review of 169 synthetic energy time-series papers, generation/evaluation taxonomy | Calls for standardized evaluation; broader than electricity demand | [RSER review](https://doi.org/10.1016/j.rser.2024.114842) |
| Stenger et al. · May 2024 | 83 time-series quality measures across 56 works; fidelity, coherence, utility, privacy and more | No generally accepted universal procedure | [Journal of Big Data survey](https://doi.org/10.1186/s40537-024-00924-7) |
| Baasch et al. · Sep 2021 | Conditional temporal building GAN; JSD, PCA, forecasting utility, trend and seasonality; discusses DTW/MMD | Marginal metrics can miss temporal failure | [Energy and AI](https://doi.org/10.1016/j.egyai.2021.100087) |
| Xia et al. · Jun 2024 | GAN/WGAN/WGAN-GP/VAE/GMM/copula comparison at 15,30,60-min, client and transformer | Configuration/dataset-dependent | [SEGAN](https://doi.org/10.1016/j.segan.2024.101338) |
| DGAN + wavelets · Apr 2024 | Annual consumption, autocorrelation, variability and downstream PV/BESS | Restricted data / different scale | [Applied Energy](https://doi.org/10.1016/j.apenergy.2024.122831) |
| Conv1D-WGAN-GP · Jul 2025 | Wasserstein, mean/std, JS, discriminator/classifier, RMSE and empirical thresholds | Table 1 thresholds are explicitly **heuristics, not universal** | [Applied Sciences](https://doi.org/10.3390/app15147835) |
| AC-WTGAN+ · Jun 2026 | DTW, KS, ACF, PCC, utility, ablations and membership inference | Irish CER weekly scenario; not globally transferable by assumption | [EPSR](https://doi.org/10.1016/j.epsr.2026.113338) |
| Fu et al. · Jun 2024 | FID/KL on annual building meters | FID feature extractor and task-specific units matter | [Energy and Buildings](https://doi.org/10.1016/j.enbuild.2024.114216) |
| Yilmaz & Korn · Sep 2024 | GAN comparison and average coverage error (ACE) for individual industry demand | Proposed criterion, not a universally adopted standard | [ESWA](https://doi.org/10.1016/j.eswa.2024.123851) |

## Proposed GATE-LOCO × generator QA matrix (not experimentally validated)

| Axis | Tests and explicit definitions to preregister |
|---|---|
| Source QA | Per-domain coverage, sampling, duplicate keys, timezones/DST, quality flags, country IDs, power units, availability at generation time |
| Statistical fidelity | Per-time and trajectory distribution: Wasserstein definition + units, RBF MMD kernel/bandwidth, KS, quantiles, load-duration curve |
| Dynamics | DTW with warping window and normalization; ACF, frequency spectrum, ramping, peak timing/magnitude, daily/weekly/seasons |
| Conditions | Drop/add group ablations, per-season and per-climate calibration, response within observed support, country-identity leakage |
| Utility | TSTR and TRTR using the *same* downstream task, features, estimator, split and metric |
| Physical consistency | Joint cross-locality correlation, MW↔MWh integration, 30-min → hourly/daily/monthly consistency and load bounds |
| Diversity/privacy | Coverage, mode collapse, nearest-neighbour distance and membership-inference when data privacy is claimed |
| Reproducibility | Prespecified seeds (e.g. 10), report all runs and failures, mean±SD/CI, code versions, checkpoints and compute |

**A low marginal Wasserstein score is not a proof of temporal quality or privacy.** Raw DTW and Wasserstein results from other papers cannot be ranked alongside differently normalized RTE results. A high R² on a downstream task is only one utility dimension. For a publishable QA contribution, compare metrics on deliberately corrupted controls (e.g. marginal-preserving time shuffle, shifted peaks, memorized records, swapped country labels, inconsistent aggregation) and show what each detects or misses. Publish exact preprocessing and metric code.

See also [GATE-LOCO conditioning](GATE_LOCO.md) and [proposed evaluation protocol](EVALUATION_PROTOCOL.md).
