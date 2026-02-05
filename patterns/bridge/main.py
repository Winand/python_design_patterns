from abc import ABC, abstractmethod
from typing import override


class Exchange(ABC):
    "Crypto exchange abstract class."

    @abstractmethod
    def connect(self) -> None:
        "Connect to the Crypto exchange."

    @abstractmethod
    def get_market_data(self, coin: str) -> list[float]:
        "Get market data for a given coin."


class BinanceExchange(Exchange):
    "Binance exchange connector."

    @override
    def connect(self) -> None:
        print("Connecting to Binance...")

    @override
    def get_market_data(self, coin: str) -> list[float]:
        return [10, 12, 18, 14]


class BybitExchange(Exchange):
    "Bybit exchange connector."

    @override
    def connect(self) -> None:
        print("Connecting to Bybit...")

    @override
    def get_market_data(self, coin: str) -> list[float]:
        return [10, 12, 18, 20]


class TradingBot(ABC):
    "Trading bot template class."

    def __init__(self, exchange: Exchange) -> None:
        "Initialize the trading bot for a given exchange."
        self.exchange = exchange

    @abstractmethod
    def should_buy(self, prices: list[float]) -> bool:
        "Check if user should buy a coin."

    @abstractmethod
    def should_sell(self, prices: list[float]) -> bool:
        "Check if user should sell a coin."

    def check_prices(self, coin: str) -> None:  # this is from Template pattern
        "Check prices for a given coin and decide which action to take."
        self.exchange.connect()
        prices = self.exchange.get_market_data(coin)
        if self.should_buy(prices):
            print(f"You should buy {coin}!")
        elif self.should_sell(prices):
            print(f"You should sell {coin}!")
        else:
            print(f"You should hodl {coin}.")


class AverageTrader(TradingBot):
    "Buy when price is below average, sell when it is above average."

    def list_average(self, lst: list[float]) -> float:
        "Calculate the average from a list of floats."
        return sum(lst) / len(lst)

    def should_buy(self, prices: list[float]) -> bool:
        "Check if user should buy a coin."
        return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: list[float]) -> bool:
        "Check if user should sell a coin."
        return prices[-1] > self.list_average(prices)


class MinMaxTrader(TradingBot):
    "Buy when price is at minimum, sell when it reaches maximum."

    def should_buy(self, prices: list[float]) -> bool:
        "Check if user should buy a coin."
        return prices[-1] == min(prices)

    def should_sell(self, prices: list[float]) -> bool:
        "Check if user should sell a coin."
        return prices[-1] == max(prices)


def main() -> None:
    "Template pattern."
    print("Hello from bridge!")

    application = MinMaxTrader(BybitExchange())
    application.check_prices("BTC/USD")


if __name__ == "__main__":
    main()
