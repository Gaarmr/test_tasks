from pydantic import BaseModel


class AnagramQuery(BaseModel):
    anagram1: str
    anagram2: str


class DeviceQuery(BaseModel):
    device_count: int
