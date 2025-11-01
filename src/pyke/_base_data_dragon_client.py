from __future__ import annotations

import json
import logging
from typing import Any

import requests
from requests import Response

from . import exceptions

logger = logging.getLogger(__name__)


class _BaseDataDragonClient:  # pyright: ignore[reportUnusedClass]
    DATA_DRAGON_BASE = "https://ddragon.leagueoflegends.com"

    def __init__(self, version: str | None, timeout: int) -> None:
        self.session = requests.Session()
        self.timeout = timeout

        if version is None:
            self.version = self._get_latest_version()
        else:
            self.version = version

        self._status_code_registry = {
            400: exceptions.BadRequest("Bad request", 400),
            401: exceptions.Unauthorized("Unauthorized", 401),
            403: exceptions.Forbidden("Forbidden", 403),
            404: exceptions.DataNotFound("Data not found", 404),
            405: exceptions.MethodNotAllowed("Method not allowed", 405),
            415: exceptions.UnsupportedMediaType("Unsupported media type", 415),
            500: exceptions.InternalServerError("Internal server error", 500),
            502: exceptions.BadGateway("Bad gateway", 502),
            503: exceptions.ServiceUnavailable("Service unavailable", 503),
            504: exceptions.GatewayTimeout("Gateway timeout", 504),
        }

    def _get_latest_version(self) -> str:
        versions = self._data_dragon_request("/api/versions.json")

        try:
            version = versions[0]
        except IndexError:
            raise exceptions.InternalServerError(
                "Could not index version from ddragon", 500
            )

        return version

    def _response_json(self, response: Response) -> Any:
        try:
            return response.json()
        except json.JSONDecodeError:
            raise exceptions.InternalServerError("Could not decode JSON", 500)
        except ValueError:
            raise exceptions.InternalServerError("Empty JSON response", 500)

    def _get(self, url: str) -> Any:
        logger.info(url)

        try:
            response = self.session.get(url, timeout=self.timeout)
        except requests.exceptions.Timeout:
            raise exceptions.RequestTimeout(
                f"Request timed out after {self.timeout} seconds", 408
            )

        code = response.status_code

        if code == 200:
            return self._response_json(response)
        else:
            raise self._status_code_registry.get(
                code,
                exceptions.UnknownError(
                    "Unexpected response, something has gone terribly wrong", code
                ),
            )

    def _data_dragon_request(self, path: str) -> Any:  # TODO: use real return
        url = f"{self.DATA_DRAGON_BASE}{path}"

        return self._get(url)
