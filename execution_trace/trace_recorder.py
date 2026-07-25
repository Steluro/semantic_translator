from flask import g

from .trace import Trace


class TraceRecorder:
    @staticmethod
    def init(app):
        @app.before_request
        def record_trace():
            g.trace = Trace()

    @staticmethod
    def current() -> Trace:
        return g.trace
