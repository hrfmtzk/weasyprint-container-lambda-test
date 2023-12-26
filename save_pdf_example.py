import base64
import json
import typing
import urllib.request


def invoke_local(message: dict[str, typing.Any]) -> dict[str, typing.Any]:
    url = "http://localhost:9000/2015-03-31/functions/function/invocations"
    request = urllib.request.Request(
        url=url,
        data=json.dumps(message).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request) as response:
        body = response.read()
    return json.loads(body)


def save_pdf(response: dict[str, typing.Any], filepath: str) -> None:
    pdf_binary = base64.b64decode(response["body"])
    with open(filepath, "wb") as fh:
        fh.write(pdf_binary)
    return


def main() -> None:
    message = {}
    response = invoke_local(message=message)
    save_pdf(response=response, filepath="./volume/example.pdf")


if __name__ == "__main__":
    main()
