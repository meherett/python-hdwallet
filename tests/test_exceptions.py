#!/usr/bin/env python3

from hdwallet.exceptions import (
    NetworkError, DerivationError, SemanticError, AddressError, SymbolError
)

import pytest


def test_exceptions():

    with pytest.raises(NetworkError, match="error"):
        raise NetworkError("error")
    with pytest.raises(NetworkError, match="error, error"):
        raise NetworkError("error", "error")
    with pytest.raises(DerivationError, match="error"):
        raise DerivationError("error")
    with pytest.raises(DerivationError, match="error, error"):
        raise DerivationError("error", "error")
    with pytest.raises(SemanticError, match="error"):
        raise SemanticError("error")
    with pytest.raises(SemanticError):
        raise SemanticError("error", "error")
    with pytest.raises(AddressError, match="error"):
        raise AddressError("error")
    with pytest.raises(AddressError, match="error, error"):
        raise AddressError("error", "error")
    with pytest.raises(SymbolError, match="error"):
        raise SymbolError("error")
    with pytest.raises(SymbolError, match="error, error"):
        raise SymbolError("error", "error")
