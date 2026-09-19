# Reproducing Yang et al. Figure 1 with OpenAlex — methodological note

**Extraction:** 2026-09-19, 10:45:15 UTC. The exact execution [succeeded on GitHub Actions](https://github.com/BillyThmtUR/Awesome-Load-Generation-Models/actions/runs/35438248111) and its annual counts were archived in [counts.csv](../results/openalex_figure1/counts.csv). The [script](../scripts/openalex_figure1.py) reproduces the API calls.

## Comparison with the survey

The original figure (Yang et al., *A Survey on Diffusion Models for Time Series and Spatio-Temporal Data*, ACM Computing Surveys 58(8), 2026, Fig. 1, p. 2) shows cumulative papers until approximately 2024, annotated with exemplar model architectures and two keyword queries. **It does not report its search database, fields, query dates or screening rules**. Exact replication cannot be established.

| Query | OpenAlex total 2020–2024 | OpenAlex total 2020–2026 |
|---|---:|---:|
| `"diffusion model" AND "time series"` | **8,455** | **16,646** |
| `"diffusion model" AND "spatial temporal"` | **2,656** | **6,490** |

These numbers are **not counts of validated diffusion architectures or load-generation studies**. OpenAlex default search includes title, abstract **and indexed fulltext**, so merely citing or discussing an expression can qualify. Different databases have different coverage and metadata updates; the original study's counts and OpenAlex counts have no common verified inclusion rules. The qualitative ordering also differs in the survey graphic (visually its spatial-temporal curve is larger), so do not claim equivalence.

The years 2025/2026 are not directly comparable to the original figure that stops in 2024. **2026 is incomplete** and OpenAlex may contain future-dated and backfilled records.

## Why a cumulative count can mislead

For annual counts n_y, cumulative C_y = Σ_{k≤y} n_k, so C_y − C_{y−1} = n_y ≥ 0. It necessarily never decreases as long as annual counts are nonnegative. Its slope is informative about yearly counts, but annotations marking individual model architectures on a steadily increasing curve are **milestones, not counts attributed to those architectures**. The two query series can overlap: they are not mutually exclusive categories, so do not stack them as a partition.

**Suggested primary figure:** annual, independently screened articles by year, split across tasks (generation versus forecasting/imputation) and verified model families (GAN/WGAN-GP/cWGAN-GP/DDPM/conditional/DDiT); use separate panels instead of stacking overlapping series. Supplement with cumulative curves for long-term volume, clearly labelled and optionally normalized to the annual total of indexed works. Display 2026 with partial-year styling and retrieval timestamp. Verify country/load inclusion manually before a thesis-specific plot.

**Reproducibility package:** API URL, UTC retrieval time, raw year counts, CSV, script, run link and caveats. If using year of earliest preprint versus formal journal publication, choose a consistent rule; do not count both as separate works.

**Note on terminology:** searching for `"spatial temporal"` omits some papers using only `"spatio-temporal"` or `"spatiotemporal"`. Expanding synonyms is appropriate for a full systematic search, but must be reported as a **different search** rather than a faithful reproduction of the graphic.
