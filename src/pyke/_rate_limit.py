from dataclasses import dataclass

from httpx import Response


@dataclass
class RateLimit:
    app_limit: str = ""
    app_count: str = ""
    method_limit: str = ""
    method_count: str = ""


def _parse_response(response: Response) -> RateLimit:  # pyright: ignore[reportUnusedFunction]
    headers = response.headers

    return RateLimit(
        headers.get("x-app-rate-limit", ""),
        headers.get("x-app-rate-limit-count", ""),
        headers.get("x-method-rate-limit", ""),
        headers.get("x-method-rate-limit-count", ""),
    )
