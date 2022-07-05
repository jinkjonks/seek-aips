"""
Tests for Traffic Counter
"""

import pytest
from traffic_counter import TrafficCounter


@pytest.mark.total_cars
def test_get_total_cars_sample():
    tc = TrafficCounter()
    tc.read_file(GIVEN_SAMPLE_TEXT)
    assert tc.get_total_cars() == SAMPLE_TOTAL_CARS


@pytest.mark.date_totals
def test_get_totals_by_dates_sample():
    tc = TrafficCounter()
    tc.read_file(GIVEN_SAMPLE_TEXT)
    assert tc.get_totals_by_dates(
        """2021-12-01\n2021-12-09""") == "2021-12-01 179\n2021-12-09 4"


@pytest.mark.date_totals
def test_get_totals_by_dates_no_entries():
    """
    Case where there are no entries for the given date
    """
    tc = TrafficCounter()
    tc.read_file(GIVEN_SAMPLE_TEXT)
    assert tc.get_totals_by_dates("2021-11-01") == "2021-11-01 0"


@pytest.mark.most_cars
def test_get_most_cars_sample():
    tc = TrafficCounter()
    tc.read_file(GIVEN_SAMPLE_TEXT)
    assert tc.get_most_cars() == SAMPLE_MOST_CARS


@pytest.mark.least_cars
def test_get_least_cars_sample():
    tc = TrafficCounter()
    tc.read_file(GIVEN_SAMPLE_TEXT)
    assert tc.get_least_cars() == SAMPLE_LEAST_CARS


@pytest.mark.least_cars
def test_get_least_cars_no_contiguous_periods():
    tc = TrafficCounter()
    tc.read_file(NO_CONTIGUOUS_PERIODS_TEXT)
    assert tc.get_least_cars() == -1  # No such period should be found


@pytest.mark.least_cars
def test_get_least_cars_multiple_periods():
    tc = TrafficCounter()
    tc.read_file(MULTIPLE_PERIODS_TEXT)
    assert tc.get_least_cars() == MULTIPLE_PERIODS_LEAST_CARS


GIVEN_SAMPLE_TEXT = """2021-12-01T05:00:00 5
2021-12-01T05:30:00 12
2021-12-01T06:00:00 14
2021-12-01T06:30:00 15
2021-12-01T07:00:00 25
2021-12-01T07:30:00 46
2021-12-01T08:00:00 42
2021-12-01T15:00:00 9
2021-12-01T15:30:00 11
2021-12-01T23:30:00 0
2021-12-05T09:30:00 18
2021-12-05T10:30:00 15
2021-12-05T11:30:00 7
2021-12-05T12:30:00 6
2021-12-05T13:30:00 9
2021-12-05T14:30:00 11
2021-12-05T15:30:00 15
2021-12-08T18:00:00 33
2021-12-08T19:00:00 28
2021-12-08T20:00:00 25
2021-12-08T21:00:00 21
2021-12-08T22:00:00 16
2021-12-08T23:00:00 11
2021-12-09T00:00:00 4"""

SAMPLE_TOTAL_CARS = 398

SAMPLE_MOST_CARS = """2021-12-01T07:30:00 46
2021-12-01T08:00:00 42
2021-12-08T18:00:00 33"""

SAMPLE_LEAST_CARS = "2021-12-01T05:00:00"


NO_CONTIGUOUS_PERIODS_TEXT = """2021-12-01T05:00:00 5
2021-12-01T05:30:00 5
2021-12-01T07:30:00 46
2021-12-01T08:00:00 46
2021-12-05T10:30:00 15
2021-12-05T14:30:00 11"""

MULTIPLE_PERIODS_TEXT = """2021-12-01T05:00:00 5
2021-12-01T05:30:00 12
2021-12-01T06:00:00 14
2021-12-01T06:30:00 15
2021-12-01T08:00:00 3
2021-12-01T08:30:00 13
2021-12-01T09:00:00 15
2021-12-05T11:30:00 7
2021-12-05T12:30:00 6
2021-12-05T13:30:00 9"""

MULTIPLE_PERIODS_LEAST_CARS = """2021-12-01T05:00:00
2021-12-01T08:00:00"""
