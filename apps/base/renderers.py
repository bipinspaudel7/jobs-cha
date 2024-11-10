from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json


class EnhancedJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        common_keys = {
            "success",
        }
        standard_keys = {
            "message",
            "errors",
            "data",
            "meta",
        }

        non_standard_keys = (set(data.keys()) - standard_keys) - common_keys
        success = data.get("success", True)

        response_dict = {
            "success": success,
        }

        for key in standard_keys:
            if key in data and data[key] is not None:
                response_dict[key] = data[key]

        if non_standard_keys:
            non_standard_data = {key: data.pop(key, None) for key in non_standard_keys}
            if "data" in response_dict:
                response_dict["data"].update(non_standard_data)
            else:
                response_dict["data"] = non_standard_data

        ret = json.dumps(
            response_dict,
            cls=self.encoder_class,
            ensure_ascii=self.ensure_ascii,
            allow_nan=not self.strict,
            indent=4,
        )
        ret = ret.replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
        return ret.encode()
