def check_ioc(ioc):
    return {
        "ioc": ioc,
        "status": "checked"
    }


if __name__ == "__main__":
    print(check_ioc("8.8.8.8"))