# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class EdgeSearchEngineCustom(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def edge_search_engine_open_search_xml_url(self):
        """Gets and sets the edgeSearchEngineOpenSearchXmlUrl
        
        Returns: 
            str:
                The edgeSearchEngineOpenSearchXmlUrl
        """
        if "edgeSearchEngineOpenSearchXmlUrl" in self._prop_dict:
            return self._prop_dict["edgeSearchEngineOpenSearchXmlUrl"]
        else:
            return None

    @edge_search_engine_open_search_xml_url.setter
    def edge_search_engine_open_search_xml_url(self, val):
        self._prop_dict["edgeSearchEngineOpenSearchXmlUrl"] = val

