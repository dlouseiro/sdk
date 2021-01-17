"""tap-base library for building singer-compliant taps."""

from singer_sdk.streams.core import Stream
from singer_sdk.streams.rest import RESTStream
from singer_sdk.streams.database import DatabaseStream
from singer_sdk.streams.graphql import GraphQLStream


__all__ = [
    "Stream",
    "RESTStream",
    "DatabaseStream",
    "GraphQLStream",
]
