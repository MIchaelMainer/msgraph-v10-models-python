# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.json import Json
from ..model.workbook_chart_point_format import WorkbookChartPointFormat
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookChartPoint(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def value(self):
        """
        Gets and sets the value
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The value
        """
        if "value" in self._prop_dict:
            if isinstance(self._prop_dict["value"], OneDriveObjectBase):
                return self._prop_dict["value"]
            else :
                self._prop_dict["value"] = Json(self._prop_dict["value"])
                return self._prop_dict["value"]

        return None

    @value.setter
    def value(self, val):
        self._prop_dict["value"] = val

    @property
    def format(self):
        """
        Gets and sets the format
        
        Returns: 
            :class:`WorkbookChartPointFormat<onedrivesdk.model.workbook_chart_point_format.WorkbookChartPointFormat>`:
                The format
        """
        if "format" in self._prop_dict:
            if isinstance(self._prop_dict["format"], OneDriveObjectBase):
                return self._prop_dict["format"]
            else :
                self._prop_dict["format"] = WorkbookChartPointFormat(self._prop_dict["format"])
                return self._prop_dict["format"]

        return None

    @format.setter
    def format(self, val):
        self._prop_dict["format"] = val

