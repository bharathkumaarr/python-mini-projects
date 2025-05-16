from fastapi import FastAPI as fa

app = fa()


food_items = {
    'indian' : ['samosa', 'Dosa'],
    'american': ['hot dog', 'apple pie']
}

@app.get("/hello/{name}")
def hello(name):
    return f'welcome, {name}'


@app.get('/')
def land():
    return 'landing page'

validation_keys = food_items.keys().
@app.get('/get_items/{cuisine}')
async def get_items(cuisine):
    if cuisine not in validation_keys:
        return f'only available cuisines are {validation_keys}'
    else:
        return food_items.get(cuisine)


