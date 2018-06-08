# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class SharepointIds(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def list_id(self):
        """Gets and sets the listId
        
        Returns: 
            str:
                The listId
        """
        if "listId" in self._prop_dict:
            return self._prop_dict["listId"]
        else:
            return None

    @list_id.setter
    def list_id(self, val):
        self._prop_dict["listId"] = val

    @property
    def list_item_id(self):
        """Gets and sets the listItemId
        
        Returns: 
            str:
                The listItemId
        """
        if "listItemId" in self._prop_dict:
            return self._prop_dict["listItemId"]
        else:
            return None

    @list_item_id.setter
    def list_item_id(self, val):
        self._prop_dict["listItemId"] = val

    @property
    def list_item_unique_id(self):
        """Gets and sets the listItemUniqueId
        
        Returns: 
            str:
                The listItemUniqueId
        """
        if "listItemUniqueId" in self._prop_dict:
            return self._prop_dict["listItemUniqueId"]
        else:
            return None

    @list_item_unique_id.setter
    def list_item_unique_id(self, val):
        self._prop_dict["listItemUniqueId"] = val

    @property
    def site_id(self):
        """Gets and sets the siteId
        
        Returns: 
            str:
                The siteId
        """
        if "siteId" in self._prop_dict:
            return self._prop_dict["siteId"]
        else:
            return None

    @site_id.setter
    def site_id(self, val):
        self._prop_dict["siteId"] = val

    @property
    def site_url(self):
        """Gets and sets the siteUrl
        
        Returns: 
            str:
                The siteUrl
        """
        if "siteUrl" in self._prop_dict:
            return self._prop_dict["siteUrl"]
        else:
            return None

    @site_url.setter
    def site_url(self, val):
        self._prop_dict["siteUrl"] = val

    @property
    def web_id(self):
        """Gets and sets the webId
        
        Returns: 
            str:
                The webId
        """
        if "webId" in self._prop_dict:
            return self._prop_dict["webId"]
        else:
            return None

    @web_id.setter
    def web_id(self, val):
        self._prop_dict["webId"] = val

