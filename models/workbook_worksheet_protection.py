# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.workbook_worksheet_protection_options import WorkbookWorksheetProtectionOptions
from ..one_drive_object_base import OneDriveObjectBase


class WorkbookWorksheetProtection(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def options(self):
        """
        Gets and sets the options
        
        Returns: 
            :class:`WorkbookWorksheetProtectionOptions<onedrivesdk.model.workbook_worksheet_protection_options.WorkbookWorksheetProtectionOptions>`:
                The options
        """
        if "options" in self._prop_dict:
            if isinstance(self._prop_dict["options"], OneDriveObjectBase):
                return self._prop_dict["options"]
            else :
                self._prop_dict["options"] = WorkbookWorksheetProtectionOptions(self._prop_dict["options"])
                return self._prop_dict["options"]

        return None

    @options.setter
    def options(self, val):
        self._prop_dict["options"] = val

    @property
    def protected(self):
        """
        Gets and sets the protected
        
        Returns:
            bool:
                The protected
        """
        if "protected" in self._prop_dict:
            return self._prop_dict["protected"]
        else:
            return None

    @protected.setter
    def protected(self, val):
        self._prop_dict["protected"] = val

