import sys
import requests

print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("World"))
print(greet("Corey"))
r = requests.get("https://coreyms.com")
print(r.status_code)
print(r.ok)

# name = input("Your name? ")
# print("Hello, ", name)
