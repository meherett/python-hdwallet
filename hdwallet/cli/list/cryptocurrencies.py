#!/usr/bin/env python

from tabulate import tabulate

import inspect

from hdwallet import cryptocurrencies
from hdwallet.cli import click


def list_cryptocurrencies():

    documents, table, headers = [], [], [
        "Cryptocurrency", "Symbol", "Mainnet", "Testnet", "Segwit", "Coin Type", "Default Path"
    ]

    for name, cryptocurrency in inspect.getmembers(cryptocurrencies):
        if inspect.isclass(cryptocurrency):
            if issubclass(cryptocurrency, cryptocurrencies.Cryptocurrency) \
                    and cryptocurrency != cryptocurrencies.Cryptocurrency:

                if cryptocurrency.NETWORK == "mainnet":
                    document: dict = {
                        "name": cryptocurrency.NAME,
                        "symbol": cryptocurrency.SYMBOL,
                        "source_code": cryptocurrency.SOURCE_CODE,
                        "mainnet": "Yes" if cryptocurrency.NETWORK == "mainnet" else "No",
                        "testnet": "Yes" if cryptocurrency.NETWORK == "testnet" else "No",
                        "segwit": "Yes" if cryptocurrency.SEGWIT_ADDRESS.HRP else "No",
                        "coin_type": cryptocurrency.COIN_TYPE.INDEX,
                        "default_path": cryptocurrency.DEFAULT_PATH
                    }
                    documents.append(document)
                elif cryptocurrency.NETWORK == "testnet":
                    for index, document in enumerate(documents):
                        if document["name"] == cryptocurrency.NAME:
                            documents[index]["symbol"] = f"{document['symbol']}, {cryptocurrency.SYMBOL}"
                            documents[index]["testnet"] = "Yes"
                else:
                    raise Exception("Invalid cryptocurrency network type.")

    for document in documents:
        table.append([
            document["name"],
            document["symbol"],
            document["mainnet"],
            document["testnet"],
            document["segwit"],
            document["coin_type"],
            document["default_path"]
        ])

    click.echo(tabulate(table, headers, tablefmt="github"))
