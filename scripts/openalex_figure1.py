#!/usr/bin/env python3
"""Reproduce (approximately) Yang et al. Fig 1 with a disclosed OpenAlex corpus.
Run: python scripts/openalex_figure1.py
OpenAlex searches title + abstract + indexed fulltext, which may differ from survey corpus.
"""
import csv, datetime as dt, json, os, pathlib, time, urllib.error, urllib.parse, urllib.request

BASE = "https://api.openalex.org/works"
QUERIES = {
    "time_series": '"diffusion model" AND "time series"',
    "spatio_temporal": '"diffusion model" AND "spatial temporal"',
}
LAST_YEAR = dt.datetime.now(dt.timezone.utc).year
YEARS = list(range(2020, LAST_YEAR + 1))
OUT = pathlib.Path("results/openalex_figure1")
OUT.mkdir(parents=True, exist_ok=True)

def request(query):
    # Bibliographic counts can change with OpenAlex index updates.
    params = {
        "search": query,
        "filter": f"from_publication_date:2020-01-01,to_publication_date:{LAST_YEAR}-12-31",
        "group_by": "publication_year",
        "per-page": "100",
    }
    url = BASE + "?" + urllib.parse.urlencode(params)
    headers = {"User-Agent": "AwesomeLoadGenerationModels/1.0 (research reproducibility)"}
    if os.getenv("OPENALEX_API_KEY"):
        params["api_key"] = os.environ["OPENALEX_API_KEY"]
        url = BASE + "?" + urllib.parse.urlencode(params)
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=35) as resp:
                return json.load(resp), url
        except urllib.error.HTTPError as ex:
            body = ex.read().decode("utf-8", "replace")[:1000]
            if ex.code not in (429,500,502,503,504) or attempt == 3:
                raise RuntimeError(f"OpenAlex HTTP {ex.code}: {body}") from ex
        except (OSError, TimeoutError):
            if attempt == 3: raise
        time.sleep(2**attempt)

def main():
    records = []
    metadata = {"extracted_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                "source": BASE, "years": [YEARS[0], LAST_YEAR],
                "scope": "OpenAlex title+abstract+fulltext; no substantive relevance screening",
                "queries": QUERIES, "counts": {}}
    for name, query in QUERIES.items():
        response, url = request(query)
        groups = {int(x["key"]): int(x["count"]) for x in response.get("group_by", []) if str(x["key"]).isdigit()}
        total = response["meta"]["count"]
        metadata["counts"][name] = {"total_2020_to_last_year": total, "by_year": groups}
        metadata.setdefault("urls", {})[name] = url.replace(os.getenv("OPENALEX_API_KEY","<none>"), "***") if os.getenv("OPENALEX_API_KEY") else url
        cumulative = 0
        print(f"\n{name}: {query}; total 2020–{LAST_YEAR}: {total}")
        for year in YEARS:
            annual = groups.get(year, 0)
            cumulative += annual
            records.append({"series": name, "year": year, "annual": annual, "cumulative_since_2020": cumulative})
            print(f"  {year}  annual={annual:6d}  cumulative={cumulative:7d}")
        print(f"  grouped sum={cumulative}; metadata total={total}; match={cumulative==total}")
        if cumulative != total:
            raise RuntimeError("Incomplete OpenAlex group_by response: check per_page and pagination")
    with (OUT / "counts.csv").open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=list(records[0]))
        w.writeheader()
        w.writerows(records)
    (OUT / "metadata.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print("\nResults at", OUT.resolve())
if __name__ == "__main__":
    main()
