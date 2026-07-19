# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from time import sleep

from ansible.module_utils.basic import AnsibleModule
from yandexcloud import SDK, RetryInterceptor


def yc_argument_spec():
    return dict(
        auth=dict(type='dict', options=dict(
            token=dict(type="str", required=False, default=None, no_log=True),
            iam_token=dict(type="str", required=False, default=None, no_log=True),
            service_account_key=dict(type="dict", required=False, default=None, no_log=True),
            endpoint=dict(type="str", required=False, default='api.cloud.yandex.net'),
            root_certificates=dict(type="str", required=False, default=None))))


class YC(AnsibleModule):
    def __init__(self, *args, **kwargs):
        argument_spec = yc_argument_spec()
        argument_spec.update(kwargs.get("argument_spec", dict()))
        kwargs["argument_spec"] = argument_spec
        super().__init__(*args, **kwargs)
        if not (self.params["auth"]["token"] or self.params["auth"]["iam_token"] or self.params["auth"]["service_account_key"]):
            self.fail_json(msg="authorization token, iam token or service account key should be provided.")
        interceptor = RetryInterceptor(max_retry_count=10)
        auth_params = {}
        if self.params["auth"]["token"]:
            auth_params["token"] = self.params["auth"]["token"]
        if self.params["auth"]["iam_token"]:
            auth_params["iam_token"] = self.params["auth"]["iam_token"]
        if self.params["auth"]["service_account_key"]:
            auth_params["service_account_key"] = self.params["auth"]["service_account_key"]
        if self.params["auth"]["endpoint"]:
            auth_params["endpoint"] = self.params["auth"]["endpoint"]
        if self.params["auth"]["root_certificates"]:
            auth_params["root_certificates"] = self.params["auth"]["root_certificates"].encode("utf-8")
        self.sdk = SDK(interceptor=interceptor, **auth_params)

    def waiter(self, operation):
        waiter = self.sdk.waiter(operation.id)
        for _ in waiter:
            sleep(1)
        return waiter.operation


def response_error_check(response):
    if "response" not in response or response["response"].get("error"):
        response["failed"] = True
        response["changed"] = False
    else:
        response["changed"] = True
    return response
