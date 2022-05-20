from fastapi import FastAPI

import uvicorn

from router import router


def get_application() -> FastAPI():
    application = FastAPI()

    application.include_router(router=router, prefix="/api")

    return application


app = get_application()


if __name__ == '__main__':
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8432,
                reload=True
                )
