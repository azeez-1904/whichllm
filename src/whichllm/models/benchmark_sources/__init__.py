"""External benchmark sources beyond Chatbot Arena and Open LLM Leaderboard.

Each module here fetches an independent leaderboard / index, normalizes it to
the same 0-100 scale, and returns a ``dict[str, float]`` keyed by HuggingFace
model id (or a list of synonyms).

The functions are intentionally defensive: if a source is unreachable or
returns malformed data, they log a warning and return an empty dict so the
main benchmark merge pipeline does not abort.
"""

from whichllm.models.benchmark_sources.aa_index import fetch_aa_index_scores
from whichllm.models.benchmark_sources.aider import fetch_aider_polyglot_scores
from whichllm.models.benchmark_sources.livebench import fetch_livebench_scores

__all__ = [
    "fetch_aa_index_scores",
    "fetch_aider_polyglot_scores",
    "fetch_livebench_scores",
]
