# coding: utf-8

"""
    playground

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel
from openapi_client.models.entry_info import EntryInfo

class ListFilesystemDirResponse(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    entries: List[EntryInfo] = ...
    __properties = ["entries"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ListFilesystemDirResponse:
        """Create an instance of ListFilesystemDirResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in entries (list)
        _items = []
        if self.entries:
            for _item in self.entries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['entries'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListFilesystemDirResponse:
        """Create an instance of ListFilesystemDirResponse from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ListFilesystemDirResponse.parse_obj(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in ListFilesystemDirResponse) in the input: " + obj)

        _obj = ListFilesystemDirResponse.parse_obj({
            "entries": [EntryInfo.from_dict(_item) for _item in obj.get("entries")] if obj.get("entries") is not None else None
        })
        return _obj
