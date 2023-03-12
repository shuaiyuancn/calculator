import logging

import azure.functions as func


def main(req):
    logging.info("Hello world!")

    return func.HttpResponse(f"Hello {req}!")
