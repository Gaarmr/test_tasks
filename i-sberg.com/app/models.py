from pydantic import BaseModel


class AnagramQuery(BaseModel):
    str_1: str
    str_2: str


class AnagramResponse(BaseModel):
    is_anagram: bool
    anagrams_count: int
