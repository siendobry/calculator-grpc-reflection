from client import Client

if __name__ == "__main__":
    client = Client("localhost", 50051)

    cmd = input()
    while cmd is not None and cmd != '':
        op, *args = cmd.split(' ')
        result = None

        try:
            match op:
                case "list_services":
                    result = client.list_services()
                case "list_methods":
                    if len(args) != 1:
                        raise Exception("Expected service name")
                    result = client.list_methods(args[0])
                case "describe_symbol":
                    if len(args) != 1:
                        raise Exception("Expected symbol name")
                    result = client.describe_symbol(args[0])
                case "execute_method":
                    if len(args) < 1 or len(args) > 2:
                        raise Exception("Expected method name and (optional) method arguments")
                    elif len(args) == 1:
                        result = client.execute_method(args[0], '')
                    else:
                        result = client.execute_method(args[0], args[1])
                    result = str(result) + '\n'
                case _:
                    raise Exception("Unknown operation")

            print(result)

        except Exception as ex:
            print(ex, end="\n\n")

        finally:
            cmd = input()
