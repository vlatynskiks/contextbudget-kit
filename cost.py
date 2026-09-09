import argparse
import json
from pathlib import Path

PRICING = json.loads(
    (Path(__file__).parent / "pricing.json").read_text(encoding="utf-8"))


def estimate_tokens(text):
    # rough heuristic: ~4 chars per token for english text
    return max(1, len(text) // 4)


def cost(model, in_tokens, out_tokens):
    p = PRICING[model]
    return in_tokens / 1e6 * p["in"] + out_tokens / 1e6 * p["out"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--model", default="gpt-4o-mini",
                    choices=sorted(PRICING))
    ap.add_argument("--expect-out", type=int, default=500)
    args = ap.parse_args()

    text = Path(args.file).read_text(encoding="utf-8")
    n_in = estimate_tokens(text)
    usd = cost(args.model, n_in, args.expect_out)
    print("input tokens : ~%d" % n_in)
    print("output tokens: ~%d" % args.expect_out)
    print("model        : %s" % args.model)
    print("est. cost    : $%.5f" % usd)


if __name__ == "__main__":
    main()
