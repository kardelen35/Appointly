import logging

logger = logging.getLogger(__name__)


class LoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response 

    def __call__(self, request):
        logger.info(f"[REQUEST] {request.method} {request.path}")

        try:
            response = self.get_response(request)  #sıradaki adıma geç. Bnedne sonra ki adımı çalıştır.
        except Exception as e:
            logger.error(f"[ERROR] {request.method} {request.path} -> {str(e)}")
            raise

        logger.info(
            f"[RESPONSE] {request.method} {request.path} -> {response.status_code}"
        )

        return response