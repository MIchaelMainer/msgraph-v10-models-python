# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_filter_criteria import WorkbookFilterCriteria
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookFilter(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def criteria(self):
        """
        Gets and sets the criteria
        
        Returns: 
            :class:`WorkbookFilterCriteria<onedrivesdk.model.workbook_filter_criteria.WorkbookFilterCriteria>`:
                The criteria
        """
        if "criteria" in self._prop_dict:
            if isinstance(self._prop_dict["criteria"], OneDriveObjectBase):
                return self._prop_dict["criteria"]
            else :
                self._prop_dict["criteria"] = WorkbookFilterCriteria(self._prop_dict["criteria"])
                return self._prop_dict["criteria"]

        return None

    @criteria.setter
    def criteria(self, val):
        self._prop_dict["criteria"] = val

