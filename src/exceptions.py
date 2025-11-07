from fastapi import HTTPException


class CustomExceptions(Exception):
    detail = "Error"

    def __init__(self, **kwargs):
        super().__init__(self.detail, **kwargs)


class ObjectNotFoundException(CustomExceptions):
    detail = "Object Not Found"


class CustomHTTPExceptions(HTTPException):
    status_code = 500
    detail = "Error"

    def __init__(self):
        super().__init__(status_code=self.status_code, detail={
            "status_code": self.status_code,
            "message": self.detail,
        })


class ObjectNotFoundHTTPException(CustomHTTPExceptions):
    status_code = 404
    detail = "Object Not Found"
