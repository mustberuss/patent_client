# ********************************************************************************
# *         WARNING: This file is automatically generated by unasync.py.         *
# *                             DO NOT MANUALLY EDIT                             *
# *      Source File: patent_client/_async/uspto/bulk_data/manager_test.py       *
# ********************************************************************************

import datetime

from .manager import date_ranges
from .model import File, Product


class TestProduct:
    def test_can_get_latest(self):
        latest = [p for p in Product.objects.filter_by_latest()]
        assert isinstance(latest[0], Product)

    def test_can_get_by_short_name(self):
        first = Product.objects.get_by_short_name("PTGRXML")
        assert isinstance(first, Product)
        assert isinstance(first.files[0], File)

    def test_can_filter_by_name(self):
        first = [p for p in Product.objects.filter_by_name("Assignment")]
        first = list(first)[0]
        assert isinstance(first, Product)
        assert isinstance(first.files[0], File)


class TestFile:
    def test_can_filter_by_short_name(self):
        results = [
            f
            for f in File.objects.filter_by_short_name(
                "PTGRXML", from_date="2023-06-15", to_date="2023-08-15"
            )
        ]
        assert len(results) == 10
        assert isinstance(results[0], File)

    def test_can_get_daily_assignments(self):
        results = [f for f in File.objects.filter_by_short_name("PASDL")]
        assert len(results) > 1
        assert isinstance(results[0], File)


def test_date_ranges():
    result = list(date_ranges(datetime.date(2020, 1, 15), datetime.date(2021, 2, 15)))
    assert result[0] == (datetime.date(2020, 1, 15), datetime.date(2020, 1, 31))
    assert result[-1] == (datetime.date(2021, 2, 1), datetime.date(2021, 2, 15))
    assert len(result) == 14
