# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_kiosk_uwp_app import WindowsKioskUWPApp
from ..one_drive_object_base import OneDriveObjectBase


class WindowsKioskSingleUWPApp(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def uwp_app(self):
        """
        Gets and sets the uwpApp
        
        Returns: 
            :class:`WindowsKioskUWPApp<onedrivesdk.model.windows_kiosk_uwp_app.WindowsKioskUWPApp>`:
                The uwpApp
        """
        if "uwpApp" in self._prop_dict:
            if isinstance(self._prop_dict["uwpApp"], OneDriveObjectBase):
                return self._prop_dict["uwpApp"]
            else :
                self._prop_dict["uwpApp"] = WindowsKioskUWPApp(self._prop_dict["uwpApp"])
                return self._prop_dict["uwpApp"]

        return None

    @uwp_app.setter
    def uwp_app(self, val):
        self._prop_dict["uwpApp"] = val
