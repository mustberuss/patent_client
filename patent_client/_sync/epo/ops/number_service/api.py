# ********************************************************************************
# *         WARNING: This file is automatically generated by unasync.py.         *
# *                             DO NOT MANUALLY EDIT                             *
# *       Source File: patent_client/_async/epo/ops/number_service/api.py        *
# ********************************************************************************

from .model import NumberServiceResult
from ..session import asession


class NumberServiceException(Exception):
    pass


class NumberServiceApi:
    @classmethod
    def convert_number(
        cls,
        number,
        doc_type="publication",
        input_format="original",
        output_format="docdb",
    ) -> NumberServiceResult:
        """Number Conversion Service
        number: number to convert. Must include at least country and doc number,
            can optionally include kind code or publication date. e.g.
            MD.20050130
            MD.20050130.A
            MD.20050130.A.20050130
            JP.2006-147056.A.20060526
            JP.2006147056.A.20060526
            US.(08/921,321).A.19970829
        doc_type: type of document (publication / application / priority)
        input_format: input type (original / docdb / epodoc)
        output_format: output type (original / docdb / epodoc)

        """
        response = asession.get(
            f"http://ops.epo.org/3.2/rest-services/number-service/{doc_type}/{input_format}/{number}/{output_format}",
            extensions={"force_cache": True},
        )
        result = NumberServiceResult.model_validate(response.text)
        errors = [m for m in result.messages if m["kind"] == "ERROR"]
        if errors:
            raise NumberServiceException("\n".join(str(e) for e in errors))
        return result
