# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_icon import WorkbookIcon
from ..model.json import Json
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookFilterCriteria(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def criterion1(self):
        """Gets and sets the criterion1
        
        Returns: 
            str:
                The criterion1
        """
        if "criterion1" in self._prop_dict:
            return self._prop_dict["criterion1"]
        else:
            return None

    @criterion1.setter
    def criterion1(self, val):
        self._prop_dict["criterion1"] = val

    @property
    def criterion2(self):
        """Gets and sets the criterion2
        
        Returns: 
            str:
                The criterion2
        """
        if "criterion2" in self._prop_dict:
            return self._prop_dict["criterion2"]
        else:
            return None

    @criterion2.setter
    def criterion2(self, val):
        self._prop_dict["criterion2"] = val

    @property
    def dynamic_criteria(self):
        """Gets and sets the dynamicCriteria
        
        Returns: 
            str:
                The dynamicCriteria
        """
        if "dynamicCriteria" in self._prop_dict:
            return self._prop_dict["dynamicCriteria"]
        else:
            return None

    @dynamic_criteria.setter
    def dynamic_criteria(self, val):
        self._prop_dict["dynamicCriteria"] = val

    @property
    def filter_on(self):
        """Gets and sets the filterOn
        
        Returns: 
            str:
                The filterOn
        """
        if "filterOn" in self._prop_dict:
            return self._prop_dict["filterOn"]
        else:
            return None

    @filter_on.setter
    def filter_on(self, val):
        self._prop_dict["filterOn"] = val

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
    def operator(self):
        """Gets and sets the operator
        
        Returns: 
            str:
                The operator
        """
        if "operator" in self._prop_dict:
            return self._prop_dict["operator"]
        else:
            return None

    @operator.setter
    def operator(self, val):
        self._prop_dict["operator"] = val

    @property
    def values(self):
        """
        Gets and sets the values
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The values
        """
        if "values" in self._prop_dict:
            if isinstance(self._prop_dict["values"], OneDriveObjectBase):
                return self._prop_dict["values"]
            else :
                self._prop_dict["values"] = Json(self._prop_dict["values"])
                return self._prop_dict["values"]

        return None

    @values.setter
    def values(self, val):
        self._prop_dict["values"] = val
