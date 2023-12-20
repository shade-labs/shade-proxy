import uvicorn
from proxy.providers.gcs import GCS


provider = GCS()


def main():
    _run_fastapi_app()


def _run_fastapi_app() -> None:
    uvicorn.run(
        "proxy.server.application:get_app",

    )


if __name__ == "__main__":
    main()
