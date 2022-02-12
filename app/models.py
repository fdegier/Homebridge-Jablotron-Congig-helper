from typing import List

from pydantic import BaseModel


class ConfigModel(BaseModel):
    id: int
    name: str
    username: str
    password: str
    service_type: str = "JA100"
    autoRefresh: str = "true"
    poolInterval: int = 60
    refreshOnStateChange: bool = True
    debug: bool = False
    sections: List
    switches: List
    outlets: List


class ResponseModel(BaseModel):
    status: str = "OK"
    configs: List[ConfigModel]
