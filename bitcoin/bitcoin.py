import os
import sys

import requests


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    # Prefer an environment variable for local runs, but default to the
    # placeholder required by the spec (check50 may stub the API response).
    api_key = os.environ.get("COINCAP_API_KEY", "YourApiKey")
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        payload = response.json()
        price_usd = float(payload["data"]["priceUsd"])
    except requests.RequestException:
        sys.exit("Error fetching Bitcoin price")
    except (KeyError, TypeError, ValueError):
        sys.exit("Unexpected API response")

    total_cost = bitcoins * price_usd
    print(f"${total_cost:,.4f}")


if __name__ == "__main__":
    main()
