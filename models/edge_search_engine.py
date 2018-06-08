# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.edge_search_engine_type import EdgeSearchEngineType
from ..one_drive_object_base import OneDriveObjectBase


class EdgeSearchEngine(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def edge_search_engine_type(self):
        """
        Gets and sets the edgeSearchEngineType
        
        Returns: 
            :class:`EdgeSearchEngineType<onedrivesdk.model.edge_search_engine_type.EdgeSearchEngineType>`:
                The edgeSearchEngineType
        """
        if "edgeSearchEngineType" in self._prop_dict:
            if isinstance(self._prop_dict["edgeSearchEngineType"], OneDriveObjectBase):
                return self._prop_dict["edgeSearchEngineType"]
            else :
                self._prop_dict["edgeSearchEngineType"] = EdgeSearchEngineType(self._prop_dict["edgeSearchEngineType"])
                return self._prop_dict["edgeSearchEngineType"]

        return None

    @edge_search_engine_type.setter
    def edge_search_engine_type(self, val):
        self._prop_dict["edgeSearchEngineType"] = val
