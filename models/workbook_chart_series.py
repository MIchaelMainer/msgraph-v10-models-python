# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_chart_series_format import WorkbookChartSeriesFormat
from ..model.workbook_chart_point import WorkbookChartPoint
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookChartSeries(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def name(self):
        """
        Gets and sets the name
        
        Returns:
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def format(self):
        """
        Gets and sets the format
        
        Returns: 
            :class:`WorkbookChartSeriesFormat<onedrivesdk.model.workbook_chart_series_format.WorkbookChartSeriesFormat>`:
                The format
        """
        if "format" in self._prop_dict:
            if isinstance(self._prop_dict["format"], OneDriveObjectBase):
                return self._prop_dict["format"]
            else :
                self._prop_dict["format"] = WorkbookChartSeriesFormat(self._prop_dict["format"])
                return self._prop_dict["format"]

        return None

    @format.setter
    def format(self, val):
        self._prop_dict["format"] = val

    @property
    def points(self):
        """Gets and sets the points
        
        Returns: 
            :class:`PointsCollectionPage<onedrivesdk.request.points_collection.PointsCollectionPage>`:
                The points
        """
        if "points" in self._prop_dict:
            return PointsCollectionPage(self._prop_dict["points"])
        else:
            return None

