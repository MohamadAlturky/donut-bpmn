


from mapping.mapper import Mapper
from pydantic import BaseModel

class Person(BaseModel):
    id:int
    name:str

mapper = Mapper(Person)

print(mapper)
text = """
    "identifire":1,
    "name of the person": "jack"
"""

res = mapper.map(text,"json object contains id and name for the person")
print(res)