# Path Parameters
## Points to remember:
1. Path parameters are usd to pass inputs using the url route or path.
2. Defining the input datatype within the method helps FastAPI validate for the datatype and return appropriate error message when needed.
3. Precedence matters! If there is a conflict between the route of two endpoints, FastAPI will route to the one that is defined first in the code.
4. File path can be used a path parameters, but we need to take care that we mention in the method's decorator that it's a path using `:path` so that FastAPI can accomodate for any slashes (`/`) in the file path and not cause error with the url path.
