
from os import getenv
from e2b import Sandbox

api_key = getenv("E2B_API_KEY")
sbx = Sandbox(api_key=api_key)
