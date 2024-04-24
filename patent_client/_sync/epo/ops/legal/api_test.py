# ********************************************************************************
# *         WARNING: This file is automatically generated by unasync.py.         *
# *                             DO NOT MANUALLY EDIT                             *
# *         Source File: patent_client/_async/epo/ops/legal/api_test.py          *
# ********************************************************************************

from pathlib import Path

import pytest

from .api import LegalAsyncApi

fixtures = Path(__file__).parent / "fixtures"



def test_async_example():
    result = LegalAsyncApi.get_legal("EP1000000A1")
    assert str(result.publication_reference) == "EP1000000A1"
    assert len(result.events) >= 50
