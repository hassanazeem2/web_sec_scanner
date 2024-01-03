import sys
print(sys.path)
print(sys.version)


from src.scanner import crawl_and_scan


if __name__ == "__main__":
    print("Web Security Scanner")
    print("--------------------")


    url = input("Enter the URL to scan:")

    crawl_and_scan(url)