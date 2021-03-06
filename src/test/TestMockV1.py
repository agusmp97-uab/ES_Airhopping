from src.test.conftest import *


class TestMockV1:
    """ When the payment of a journey is confirmed, the program reports it"""
    def test_do_payment(self, monkeypatch, payment_data, billing_user, journey_multiple_passengers):
        def mock_return(self, user, payment_data):
            return True
        monkeypatch.setattr(Bank, "do_payment", mock_return)

        journey_multiple_passengers[0].add_payment_data(payment_data)
        journey_multiple_passengers[0].add_billing_user(billing_user)
        assert journey_multiple_passengers[0].do_payment() is True

    """ When the reserve of the flights is confirmed, the program reports it"""
    def test_do_reserve(self, monkeypatch, user, journey_multiple_passengers):
        def mock_return(self, user, flights):
            return True
        monkeypatch.setattr(Skyscanner, "confirm_reserve", mock_return)

        journey_multiple_passengers[0].add_user(user)
        assert journey_multiple_passengers[0].confirm_reserve_flights() is True


