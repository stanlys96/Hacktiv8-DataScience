from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def root():
  return {
    'message': 'Hello World'
  }

@app.get("/data")
def get_data():
  return "This is the endpoint of this API"

@app.get("/names/{name}")
def read_name(name):
  return {"name":name,"message":f"Hello, my name is {name}"}

@app.get("/items/{id}")
def read_items(id):
  return {"id":id}

df = {
    1: {"name": "Hana", "age": 10},
    2: {"name": "Rifdah", "age": 18}
}

@app.get('/data_frame')
def read_data():
    return df

@app.put("/items/{item_id}")
def update_item(item_id: int, update_data: dict):

    # Perform the update using the data from the request body
    df[item_id].update(update_data)

    return {"message": f"Item with ID {item_id} has been updated successfully."}

data = []

@app.get('/post-data')
def cart():
    if len(data) == 0:
        return "There are no items in your cart"
    else:
        return data

@app.post('/input_data/')
def add_cart(added_item:dict):
    id = len(data) + 1
    added_item['id'] = id
    data.append(added_item)
    return added_item

df_2 = {
    1: {"name": "Hana", "age": 10},
    2: {"name": "Rifdah", "age": 18},
    3: {"name": "Sakinah", "age": 27}
}

@app.get('/data_frame_2')
def read_data():
    return df_2

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    df_2.pop(item_id)
    return {"message": f"Item with ID {item_id} has been deleted successfully."}

df_3 = {
    1: {"name": "Hana", "age": 10},
    2: {"name": "Rifdah", "age": 18}
}

@app.get('/data_frame_3')
def read_data():
    return df_3

@app.put("/items_3/{item_id}")
def update_item(item_id: int, update_data: dict):
    if item_id not in df_3.keys():
      raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")
    df_3[item_id].update(update_data)
    return {"message": f"Item with ID {item_id} has been updated successfully."}