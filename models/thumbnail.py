# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class Thumbnail(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def height(self):
        """Gets and sets the height
        
        Returns: 
            int:
                The height
        """
        if "height" in self._prop_dict:
            return self._prop_dict["height"]
        else:
            return None

    @height.setter
    def height(self, val):
        self._prop_dict["height"] = val

    @property
    def source_item_id(self):
        """Gets and sets the sourceItemId
        
        Returns: 
            str:
                The sourceItemId
        """
        if "sourceItemId" in self._prop_dict:
            return self._prop_dict["sourceItemId"]
        else:
            return None

    @source_item_id.setter
    def source_item_id(self, val):
        self._prop_dict["sourceItemId"] = val

    @property
    def url(self):
        """Gets and sets the url
        
        Returns: 
            str:
                The url
        """
        if "url" in self._prop_dict:
            return self._prop_dict["url"]
        else:
            return None

    @url.setter
    def url(self, val):
        self._prop_dict["url"] = val

    @property
    def width(self):
        """Gets and sets the width
        
        Returns: 
            int:
                The width
        """
        if "width" in self._prop_dict:
            return self._prop_dict["width"]
        else:
            return None

    @width.setter
    def width(self, val):
        self._prop_dict["width"] = val

