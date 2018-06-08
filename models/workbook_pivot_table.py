# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_worksheet import WorkbookWorksheet
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookPivotTable(OneDriveObjectBase):

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
    def worksheet(self):
        """
        Gets and sets the worksheet
        
        Returns: 
            :class:`WorkbookWorksheet<onedrivesdk.model.workbook_worksheet.WorkbookWorksheet>`:
                The worksheet
        """
        if "worksheet" in self._prop_dict:
            if isinstance(self._prop_dict["worksheet"], OneDriveObjectBase):
                return self._prop_dict["worksheet"]
            else :
                self._prop_dict["worksheet"] = WorkbookWorksheet(self._prop_dict["worksheet"])
                return self._prop_dict["worksheet"]

        return None

    @worksheet.setter
    def worksheet(self, val):
        self._prop_dict["worksheet"] = val

