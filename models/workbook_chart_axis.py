# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.json import Json
from ..model.workbook_chart_axis_format import WorkbookChartAxisFormat
from ..model.workbook_chart_gridlines import WorkbookChartGridlines
from ..model.workbook_chart_axis_title import WorkbookChartAxisTitle
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookChartAxis(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def major_unit(self):
        """
        Gets and sets the majorUnit
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The majorUnit
        """
        if "majorUnit" in self._prop_dict:
            if isinstance(self._prop_dict["majorUnit"], OneDriveObjectBase):
                return self._prop_dict["majorUnit"]
            else :
                self._prop_dict["majorUnit"] = Json(self._prop_dict["majorUnit"])
                return self._prop_dict["majorUnit"]

        return None

    @major_unit.setter
    def major_unit(self, val):
        self._prop_dict["majorUnit"] = val

    @property
    def maximum(self):
        """
        Gets and sets the maximum
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The maximum
        """
        if "maximum" in self._prop_dict:
            if isinstance(self._prop_dict["maximum"], OneDriveObjectBase):
                return self._prop_dict["maximum"]
            else :
                self._prop_dict["maximum"] = Json(self._prop_dict["maximum"])
                return self._prop_dict["maximum"]

        return None

    @maximum.setter
    def maximum(self, val):
        self._prop_dict["maximum"] = val

    @property
    def minimum(self):
        """
        Gets and sets the minimum
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The minimum
        """
        if "minimum" in self._prop_dict:
            if isinstance(self._prop_dict["minimum"], OneDriveObjectBase):
                return self._prop_dict["minimum"]
            else :
                self._prop_dict["minimum"] = Json(self._prop_dict["minimum"])
                return self._prop_dict["minimum"]

        return None

    @minimum.setter
    def minimum(self, val):
        self._prop_dict["minimum"] = val

    @property
    def minor_unit(self):
        """
        Gets and sets the minorUnit
        
        Returns: 
            :class:`Json<onedrivesdk.model.json.Json>`:
                The minorUnit
        """
        if "minorUnit" in self._prop_dict:
            if isinstance(self._prop_dict["minorUnit"], OneDriveObjectBase):
                return self._prop_dict["minorUnit"]
            else :
                self._prop_dict["minorUnit"] = Json(self._prop_dict["minorUnit"])
                return self._prop_dict["minorUnit"]

        return None

    @minor_unit.setter
    def minor_unit(self, val):
        self._prop_dict["minorUnit"] = val

    @property
    def format(self):
        """
        Gets and sets the format
        
        Returns: 
            :class:`WorkbookChartAxisFormat<onedrivesdk.model.workbook_chart_axis_format.WorkbookChartAxisFormat>`:
                The format
        """
        if "format" in self._prop_dict:
            if isinstance(self._prop_dict["format"], OneDriveObjectBase):
                return self._prop_dict["format"]
            else :
                self._prop_dict["format"] = WorkbookChartAxisFormat(self._prop_dict["format"])
                return self._prop_dict["format"]

        return None

    @format.setter
    def format(self, val):
        self._prop_dict["format"] = val

    @property
    def major_gridlines(self):
        """
        Gets and sets the majorGridlines
        
        Returns: 
            :class:`WorkbookChartGridlines<onedrivesdk.model.workbook_chart_gridlines.WorkbookChartGridlines>`:
                The majorGridlines
        """
        if "majorGridlines" in self._prop_dict:
            if isinstance(self._prop_dict["majorGridlines"], OneDriveObjectBase):
                return self._prop_dict["majorGridlines"]
            else :
                self._prop_dict["majorGridlines"] = WorkbookChartGridlines(self._prop_dict["majorGridlines"])
                return self._prop_dict["majorGridlines"]

        return None

    @major_gridlines.setter
    def major_gridlines(self, val):
        self._prop_dict["majorGridlines"] = val

    @property
    def minor_gridlines(self):
        """
        Gets and sets the minorGridlines
        
        Returns: 
            :class:`WorkbookChartGridlines<onedrivesdk.model.workbook_chart_gridlines.WorkbookChartGridlines>`:
                The minorGridlines
        """
        if "minorGridlines" in self._prop_dict:
            if isinstance(self._prop_dict["minorGridlines"], OneDriveObjectBase):
                return self._prop_dict["minorGridlines"]
            else :
                self._prop_dict["minorGridlines"] = WorkbookChartGridlines(self._prop_dict["minorGridlines"])
                return self._prop_dict["minorGridlines"]

        return None

    @minor_gridlines.setter
    def minor_gridlines(self, val):
        self._prop_dict["minorGridlines"] = val

    @property
    def title(self):
        """
        Gets and sets the title
        
        Returns: 
            :class:`WorkbookChartAxisTitle<onedrivesdk.model.workbook_chart_axis_title.WorkbookChartAxisTitle>`:
                The title
        """
        if "title" in self._prop_dict:
            if isinstance(self._prop_dict["title"], OneDriveObjectBase):
                return self._prop_dict["title"]
            else :
                self._prop_dict["title"] = WorkbookChartAxisTitle(self._prop_dict["title"])
                return self._prop_dict["title"]

        return None

    @title.setter
    def title(self, val):
        self._prop_dict["title"] = val

