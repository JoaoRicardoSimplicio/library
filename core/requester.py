import os
from typing import Dict, Any, Optional

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


RETRIES = os.environ.get('REQUEST_RETRIES', 3)


class Requests:

    def __init__(self) -> None:
        self.session = self._start_session()

    def _start_session(self):
        session = requests.Session()

        retry_strategy = Retry(
            total=RETRIES,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS", "POST"],
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("https://", adapter)
        session.mount("http://", adapter)

        return session

    def _request(
        self,
        method: str,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        payload: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: int = 30,
    ) -> requests.Response:
        response = self.session.request(
            method=method,
            url=url,
            params=params,
            json=payload,
            headers=headers,
            timeout=timeout,
        )
        response.raise_for_status()
        return response

    def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> requests.Response:
        return self._request("GET", url, params=params, headers=headers)


requests = Requests()
