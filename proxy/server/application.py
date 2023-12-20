from fastapi import FastAPI
from fastapi.exception_handlers import request_validation_exception_handler
from fastapi.exceptions import RequestValidationError
from fastapi.responses import ORJSONResponse
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from proxy.server.api import router


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    app = FastAPI(
        title="shade-proxy",
        default_response_class=ORJSONResponse,  # optimization: https://fastapi.tiangolo.com/advanced/custom-response/
    )

    _register_exception_handlers(app)
    _add_cors_middleware(app)

    app.include_router(router=router)

    return app


def _add_cors_middleware(app: FastAPI) -> None:
    """
    Adds CORS middleware to the app.

    :param app: FastAPI application.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )


def _register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError) -> JSONResponse:
        # log the error
        print(f'{request.method} {request.url} {exc}')
        return await request_validation_exception_handler(request, exc)
