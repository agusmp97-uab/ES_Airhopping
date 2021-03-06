import src.main.Flights
from src.test.conftest import *
from src.main.Bank import Bank
import src.main.Flights
from src.main.Journey import Journey
from src.test.conftest import *


class TestMockV2:
    """ When the user selects a payment method, the payment is realized with this method"""
    def test_payment_method(self, monkeypatch, journey_multiple_passengers, billing_user, payment_data_type):
        def mock_return(self, user, payment_data):
            return payment_data.get_payment_type()
        monkeypatch.setattr(Bank, "do_payment", mock_return)

        journey_multiple_passengers[0].add_payment_data(payment_data_type[0])
        journey_multiple_passengers[0].add_billing_user(billing_user)
        assert journey_multiple_passengers[0].do_payment() == payment_data_type[1][0]

    """ When there is an error on the payment of a journey, the program reports it"""
    def test_do_payment_fail(self, monkeypatch, journey_multiple_passengers, billing_user, payment_data):
        def mock_return(self, user, payment_data):
            return False
        monkeypatch.setattr(Bank, "do_payment", mock_return)

        journey_multiple_passengers[0].add_payment_data(payment_data)
        journey_multiple_passengers[0].add_billing_user(billing_user)
        assert journey_multiple_passengers[0].do_payment() is False

    """ When there is an error on the reserve of the flights, the program reports it"""
    def test_do_reserve_fail(self, monkeypatch, journey_multiple_passengers, user):
        def mock_return(self, user, aux):
            return False
        monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_return)

        journey_multiple_passengers[0].add_user(user)
        assert journey_multiple_passengers[0].confirm_reserve_flights() is False
