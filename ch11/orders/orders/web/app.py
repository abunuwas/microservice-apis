from fastapi import FastAPI

app = FastAPI(debug=True)


from orders.web.api import api
