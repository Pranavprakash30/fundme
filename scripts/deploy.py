from brownie import FundMe, config, MockV3Aggregator, network
from scripts.helpful_scripts import (
    get_account,
    deploy_mock,
    LOCAL_BLOCKCHAIN_ENVIRONMENT,
)


def deploy_fund_me():
    account = get_account()
    # pass pricefeed address to fundme conract

    # if on persistent network like rinkeby, use associate address
    # otherwise deploy mock
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        priceFeed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mock()
        priceFeed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        priceFeed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
