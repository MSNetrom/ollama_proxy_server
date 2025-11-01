import os
import sys
from typing import Optional

try:
    from openai import OpenAI
except Exception as exc:  # pragma: no cover
    print("This example requires the 'openai' package. Install with: pip install openai", file=sys.stderr)
    raise


def get_env(name: str, required: bool = True, default: Optional[str] = None) -> Optional[str]:
    value = os.getenv(name, default)
    if required and not value:
        print(f"Missing environment variable: {name}", file=sys.stderr)
        sys.exit(1)
    return value


def main() -> None:
    # Required for any OpenAI-compatible endpoint
    api_key = "op_7dfba04bd7bf9c17_2f5437fb777a32377a24f39cf175b76e3b11a12f6cd67685"

    # Optional: point to a custom endpoint (must expose OpenAI-compatible /v1 APIs)
    base_url = "https://ai.marmelli.com/ollamapi/v1"

    # Choose a model
    model = os.getenv("OPENAI_MODEL", "gpt-oss:20b")

    client = OpenAI(api_key=api_key, base_url=base_url) if base_url else OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hello in one sentence."},
        ],
        temperature=0.2,
    )

    content = response.choices[0].message.content if response.choices else "<no content>"
    print(content)


if __name__ == "__main__":
    main()

