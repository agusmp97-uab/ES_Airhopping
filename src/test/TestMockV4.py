import src.main.Flights
from src.test.conftest import *
from src.main.Bank import Bank
import src.main.Flights
from src.main.Journey import Journey
from src.test.conftest import *
from src.main.Journey import Journey
from unittest.mock import Mock


class TestMockV4:

    def test_retry_payment(self, monkeypatch, journey_multiple_passengers, billing_user, payment_data):
        def mock_return(self, user, payment_data):
            return False
        monkeypatch.setattr(Bank, "do_payment", mock_return)

        journey_multiple_passengers[0].add_payment_data(payment_data)
        journey_multiple_passengers[0].add_billing_user(billing_user)
        journey_multiple_passengers[0].do_payment()
        assert journey_multiple_passengers[0].get_tryings() < 2

    def test_retry_payment_success(self, monkeypatch, journey_multiple_passengers, billing_user, payment_data):
        Bank.do_payment.side_effect = [False, True]

        journey_multiple_passengers[0].add_payment_data(payment_data)
        journey_multiple_passengers[0].add_billing_user(billing_user)
        assert journey_multiple_passengers[0].do_payment() is True

    def test_retry_payment_max_reties(self, monkeypatch, journey_multiple_passengers, billing_user, payment_data):
        def mock_return(self, user, payment_data):
            return False

        monkeypatch.setattr(Bank, "do_payment", mock_return)
        journey_multiple_passengers[0].add_payment_data(payment_data)
        journey_multiple_passengers[0].add_billing_user(billing_user)
        assert journey_multiple_passengers[0].do_payment() is False

    def test_retry_flights_reserve(self, monkeypatch, journey_multiple_passengers, user):
        def mock_return(self, user, flight):
            return False
        monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_return)

        journey_multiple_passengers[0].add_user(user)
        journey_multiple_passengers[0].confirm_reserve_flights()
        assert journey_multiple_passengers[0].get_tryings() < 2

    def test_retry_flights_reserve_success(self, monkeypatch, journey_multiple_passengers, user):
        Skyscanner.confirm_reserve.side_effect = [False, True]

        journey_multiple_passengers[0].add_user(user)
        assert journey_multiple_passengers[0].confirm_reserve_flights() is True

    def test_retry_flights_reserve_max_reties(self, monkeypatch, journey_multiple_passengers, user):
        def mock_return(self, user, flight):
            return False
        monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_return)

        journey_multiple_passengers[0].add_user(user)
        assert journey_multiple_passengers[0].confirm_reserve_flights() is False



