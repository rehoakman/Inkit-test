from fastapi import FastAPI
from datetime import datetime
from dateutil.relativedelta import relativedelta
from fastapi.middleware.cors import CORSMiddleware


import uuid



app = FastAPI()
#to ensure CORS error doesn't happen again
#this is where the frontend is coming from
ports = [
    "http://localhost:5000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins= ports,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


"""
The returned json/dict is the data struct
you need already. Now you need to modify what it returns
"""
@app.get("/")
async def root():
    uuid = random_uuid()
    cur_time,future_time = get_times()
    data = {   
            "uuid": str(uuid),
            "document_name": "My important document",
            "created_at": cur_time,
            "description": "This is sample text",
            "expires_at": future_time
        }  
    return data
"""
This function generates a uuid using uuid4, this function
will be called in the root() function. This also ensures a new uuid
is generated.
"""
def random_uuid():
    id = uuid.uuid4()
    return id


def get_times():
    cur_time = datetime.utcnow()
    time_str = cur_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    #incrementing by one month
    one_month = cur_time + relativedelta(months=1)
    string_one_month = one_month.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    return time_str, string_one_month




