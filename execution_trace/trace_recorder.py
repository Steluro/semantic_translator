from flask import Response, g, jsonify

from .trace import Trace


class TraceRecorder:
    @staticmethod
    def init(app):
        @app.before_request
        def initialize_trace():
            g.trace = Trace()

        @app.after_request
        def return_trace(response: Response):
            trace = g.get("trace", None)
            if trace and trace.events:
                if response.is_json:
                    data = response.get_json()
                    if data is None:
                        data = {}
                    data["execution_trace"] = trace.to_json()
                    new_response = jsonify(data)
                    new_response.status_code = response.status_code

            return new_response

    @staticmethod
    def current() -> Trace:
        return g.trace
