import sentry_sdk
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import (
    LambdaFunctionUrlResolver,
    Response,
    content_types,
)
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext
from jinja2 import Template
from sentry_sdk import capture_exception
from sentry_sdk.integrations.aws_lambda import AwsLambdaIntegration
from weasyprint import HTML

logger = Logger()
tracer = Tracer()

app = LambdaFunctionUrlResolver()


sentry_sdk.init(
    integrations=[
        AwsLambdaIntegration(),
    ],
    traces_sample_rate=1.0,
)


class Receipt:
    def __init__(self) -> None:
        pass

    def _generate_html(self) -> str:
        with open("invoice.tpl", "r") as fh:
            template = "\n".join(fh.readlines())

        render_context = {
            "invoice_date": "2000 年 1 月 23 日",
            "invoice_number": "00000000-00000000-0000-0000",
        }

        html_string = Template(source=template).render(render_context)

        return html_string

    def print(self) -> bytes:
        html = self._generate_html()

        pdf_binary = HTML(string=html).write_pdf()

        return pdf_binary


@app.get(".+")
@tracer.capture_method(capture_response=False)
def get_pdf() -> Response:
    return Response(
        status_code=200,
        content_type="application/pdf",
        body=Receipt().print(),
        headers={
            "Content-Disposition": "; ".join(
                [
                    "attachment",
                    'filename="example.pdf"',
                ]
            ),
        },
    )


@app.exception_handler(Exception)
def unhandled_exception(ex: Exception) -> Response:
    logger.error(ex)
    capture_exception(ex)

    return Response(
        status_code=500,
        content_type=content_types.APPLICATION_JSON,
        body={
            "statusCode": 500,
            "message": "Internal Server Error",
        },
    )


@logger.inject_lambda_context(
    correlation_id_path=correlation_paths.LAMBDA_FUNCTION_URL,
)
@tracer.capture_lambda_handler(capture_response=False)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
