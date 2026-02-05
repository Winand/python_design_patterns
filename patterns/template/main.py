from abc import ABC, abstractmethod


class TradingBot(ABC):
    "Trading bot template class."

    def connect(self) -> None:
        "Connect to the Crypto exchange mock."
        print("Connecting to Crypto exchange...")

    def get_market_data(self, coin: str) -> list[float]:  # noqa: ARG002
        "Get market data for a given coin mock."
        return [10, 12, 18, 14]

    @abstractmethod
    def should_buy(self, prices: list[float]) -> bool:
        "Check if user should buy a coin."

    @abstractmethod
    def should_sell(self, prices: list[float]) -> bool:
        "Check if user should sell a coin."

    def check_prices(self, coin: str) -> None:
        "Check prices for a given coin and decide which action to take."
        self.connect()
        prices = self.get_market_data(coin)
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


# from typing import Literal

# type Strategy = Literal["average", "minmax"]


# class Application:
#     "Trading strategies for coins."

#     def __init__(self, trading_strategy: Strategy = "average") -> None:
#         "Initialize the trading strategy."
#         self.trading_strategy: Strategy = trading_strategy

#     def connect(self) -> None:
#         "Connect to the Crypto exchange mock."
#         print("Connecting to Crypto exchange...")

#     def get_market_data(self, coin: str) -> list[float]:
#         "Get market data for a given coin mock."
#         return [10, 12, 18, 14]

#     def list_average(self, lst: list[float]) -> float:
#         "Calculate the average from a list of floats."
#         return sum(lst) / len(lst)

#     def should_buy(self, prices: list[float]) -> bool:
#         "Check if user should buy a coin."
#         if self.trading_strategy == "minmax":
#             return prices[-1] == min(prices)
#         return prices[-1] < self.list_average(prices)

#     def should_sell(self, prices: list[float]) -> bool:
#         "Check if user should sell a coin."
#         if self.trading_strategy == "minmax":
#             return prices[-1] == max(prices)
#         return prices[-1] > self.list_average(prices)

#     def check_prices(self, coin: str) -> None:
#         "Check prices for a given coin and decide which action to take."
#         self.connect()
#         prices = self.get_market_data(coin)
#         if self.should_buy(prices):
#             print(f"You should buy {coin}!")
#         elif self.should_sell(prices):
#             print(f"You should sell {coin}!")
#         else:
#             print(f"You should hodl {coin}.")


def main() -> None:
    "Template pattern."
    print("Hello from template!")

    application = AverageTrader()
    application.check_prices("BTC/USD")


if __name__ == "__main__":
    main()
