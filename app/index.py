import base64
import typing

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext
from jinja2 import Template
from weasyprint import HTML

logger = Logger()


@logger.inject_lambda_context
def lambda_handler(
    event: dict[str, typing.Any],
    context: LambdaContext,
) -> dict[str, typing.Any]:
    with open("invoice.tpl", "r") as fh:
        template = "\n".join(fh.readlines())

    render_context = {
        "invoice_date": "2000 年 1 月 23 日",
        "invoice_number": "00000000-00000000-0000-0000",
    }

    html_string = Template(source=template).render(render_context)

    HTML(string=html_string).write_pdf("/tmp/sample.pdf")
    pdf_binary: bytes = HTML(string=html_string).write_pdf()

    return {
        "body": base64.b64encode(pdf_binary).decode(),
        "isBase64Encoded": True,
    }
