# ********************************************************************************
# *         WARNING: This file is automatically generated by unasync.py.         *
# *                             DO NOT MANUALLY EDIT                             *
# *            Source File: patent_client/_async/uspto/odp/manager.py            *
# ********************************************************************************

import typing as tp
from patent_client.util.manager import Manager
from patent_client.util.request_util import get_start_and_row_count
from .api import ODPApi
from .model import SearchRequest
from .model import USApplicationBiblio, USApplication
from .query import create_post_search_obj

if tp.TYPE_CHECKING:
    from .model import (
        USApplication,
        USApplicationBiblio,
        Document,
        Continuity,
        SearchResult,
    )


api = ODPApi()


class USApplicationManager(Manager):
    default_filter = "appl_id"
    default_fields = []
    response_model = USApplication

    def count(self):
        return (
            api.post_search(
                self._create_search_obj(fields=["applicationNumberText"])
            )
        )["count"]

    def _get_results(self) -> tp.Iterator["SearchResult"]:
        query_obj = self._create_search_obj()
        for start, rows in get_start_and_row_count(self.config.limit):
            page_query = query_obj.model_dump()
            page_query["pagination"] = {"offset": start, "limit": rows}
            page_query_obj = SearchRequest(**page_query)
            for result in (api.post_search(page_query_obj))["patentBag"]:
                yield self.response_model(**result)

    def _create_search_obj(self, fields: tp.Optional[tp.List[str]] = None):
        if fields is None:
            fields = self.default_fields
        if "query" in self.config.filter:
            return SearchRequest(**self.config.filter["query"][0], fields=fields)
        elif "q" in self.config.filter:
            return SearchRequest(q=self.config.filter["q"][0], fields=fields)
        else:
            return create_post_search_obj(self.config, fields=fields)


class USApplicationBiblioManager(USApplicationManager):
    default_filter = "appl_id"
    default_fields = [
        "firstInventorToFileIndicator",
        "filingDate",
        "inventorBag",
        "customerNumber",
        "groupArtUnitNumber",
        "inventionTitle",
        "correspondenceAddressBag",
        "applicationConfirmationNumber",
        "docketNumber",
        "applicationNumberText",
        "firstInventorName",
        "firstApplicantName",
        "cpcClassificationBag",
        "businessEntityStatusCategory",
        "earliestPublicationNumber",
    ]
    response_model = USApplicationBiblio


class AttributeManager(Manager):
    def filter(self, *args, **kwargs):
        raise NotImplementedError("Filtering attributes is not supported")

    def get(self, *args, **kwargs):
        raise NotImplementedError("Getting attributes is not supported")

    def limit(self, *args, **kwargs):
        raise NotImplementedError("Limit is not supported")

    def offset(self, *args, **kwargs):
        raise NotImplementedError("Offset is not supported")


class ContinuityManager(AttributeManager):
    def get(self, appl_id: str) -> "Continuity":
        return api.get_continuity_data(appl_id)


class DocumentManager(Manager):
    default_filter = "appl_id"

    def count(self):
        return len(api.get_documents(self.config.filter["appl_id"][0]))

    def _get_results(self) -> tp.Iterator["Document"]:
        for doc in api.get_documents(self.config.filter["appl_id"][0]):
            yield doc
