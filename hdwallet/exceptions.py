#!/usr/bin/env python

from typing import Optional


class DerivationError(Exception):

    def __init__(self, error_message: str, error_detail: Optional[str] = None):
        self.error_message = error_message
        self.error_detail = error_detail

    def __str__(self):
        if self.error_detail:
            return f"{self.error_message}, {self.error_detail}"
        return f"{self.error_message}"


class SemanticError(Exception):

    def __init__(self, error_message: str, error_detail: Optional[str] = None):
        self.error_message = error_message
        self.error_detail = error_detail

    def __str__(self):
        if self.error_detail:
            return f"{self.error_message}, {self.error_detail}"
        return f"{self.error_message}"


class AddressError(Exception):

    def __init__(self, error_message: str, error_detail: Optional[str] = None):
        self.error_message = error_message
        self.error_detail = error_detail

    def __str__(self):
        if self.error_detail:
            return f"{self.error_message}, {self.error_detail}"
        return f"{self.error_message}"


class SymbolError(Exception):

    def __init__(self, error_message: str, error_detail: Optional[str] = None):
        self.error_message = error_message
        self.error_detail = error_detail

    def __str__(self):
        if self.error_detail:
            return f"{self.error_message}, {self.error_detail}"
        return f"{self.error_message}"


class NetworkError(Exception):

    def __init__(self, error_message: str, error_detail: Optional[str] = None):
        self.error_message = error_message
        self.error_detail = error_detail

    def __str__(self):
        if self.error_detail:
            return f"{self.error_message}, {self.error_detail}"
        return f"{self.error_message}"
