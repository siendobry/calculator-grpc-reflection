import json
import subprocess


class Client:

    def __init__(self, address, port):
        self.grpcurl_path = "D:\\grpcurl\\grpcurl.exe" # replace with actual grpcurl.exe location
        self.address = address
        self.port = port

    def list_services(self):
        result = subprocess.check_output([self.grpcurl_path, "-plaintext", self.server_assoc(), "list"])
        return result.decode('utf-8')

    def list_methods(self, service_name):
        result = subprocess.check_output([self.grpcurl_path, "-plaintext", self.server_assoc(), "list", service_name])
        return result.decode('utf-8')

    def describe_symbol(self, symbol_name):
        result = subprocess.check_output([self.grpcurl_path, "-plaintext", self.server_assoc(), "describe", symbol_name])
        return result.decode('utf-8')

    def execute_method(self, method_name, args):
        result = subprocess.check_output([self.grpcurl_path, "-plaintext", "-d", args, self.server_assoc(), method_name])
        return json.loads(result)

    def server_assoc(self):
        return f"{self.address}:{self.port}"
