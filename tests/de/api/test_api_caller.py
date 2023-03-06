from src.de.api.api_caller import ApiCaller


def test_constructor():
    api_token = "test"
    apicaller = ApiCaller(url="http://api.marketstack.com/v1/eod?",
                          ticker="AAPL",
                          access_key=api_token)
