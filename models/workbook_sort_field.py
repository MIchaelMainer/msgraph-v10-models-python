# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_icon import WorkbookIcon
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookSortField(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def ascending(self):
        """Gets and sets the ascending
        
        Returns: 
            bool:
                The ascending
        """
        if "ascending" in self._prop_dict:
            return self._prop_dict["ascending"]
        else:
            return None

    @ascending.setter
    def ascending(self, val):
        self._prop_dict["ascending"] = val

    @property
    def color(self):
        """Gets and sets the color
        
        Returns: 
            str:
                The color
        """
        if "color" in self._prop_dict:
            return self._prop_dict["color"]
        else:
            return None

    @color.setter
    def color(self, val):
        self._prop_dict["color"] = val

    @property
    def data_option(self):
        """Gets and sets the dataOption
        
        Returns: 
            str:
                The dataOption
        """
        if "dataOption" in self._prop_dict:
            return self._prop_dict["dataOption"]
        else:
            return None

    @data_option.setter
    def data_option(self, val):
        self._prop_dict["dataOption"] = val

    @property
    def icon(self):
        """
        Gets and sets the icon
        
        Returns: 
            :class:`WorkbookIcon<onedrivesdk.model.workbook_icon.WorkbookIcon>`:
                The icon
        """
        if "icon" in self._prop_dict:
            if isinstance(self._prop_dict["icon"], OneDriveObjectBase):
                return self._prop_dict["icon"]
            else :
                self._prop_dict["icon"] = WorkbookIcon(self._prop_dict["icon"])
                return self._prop_dict["icon"]

        return None

    @icon.setter
    def icon(self, val):
        self._prop_dict["icon"] = val
    @property
    def key(self):
        """Gets and sets the key
        
        Returns: 
            int:
                The key
        """
        if "key" in self._prop_dict:
            return self._prop_dict["key"]
        else:
            return None

    @key.setter
    def key(self, val):
        self._prop_dict["key"] = val

    @property
    def sort_on(self):
        """Gets and sets the sortOn
        
        Returns: 
            str:
                The sortOn
        """
        if "sortOn" in self._prop_dict:
            return self._prop_dict["sortOn"]
        else:
            return None

    @sort_on.setter
    def sort_on(self, val):
        self._prop_dict["sortOn"] = val

