# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.windows_kiosk_app_base import WindowsKioskAppBase
from ..one_drive_object_base import OneDriveObjectBase


class WindowsKioskMultipleApps(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def apps(self):
        """
        Gets and sets the apps
        
        Returns: 
            :class:`WindowsKioskAppBase<onedrivesdk.model.windows_kiosk_app_base.WindowsKioskAppBase>`:
                The apps
        """
        if "apps" in self._prop_dict:
            if isinstance(self._prop_dict["apps"], OneDriveObjectBase):
                return self._prop_dict["apps"]
            else :
                self._prop_dict["apps"] = WindowsKioskAppBase(self._prop_dict["apps"])
                return self._prop_dict["apps"]

        return None

    @apps.setter
    def apps(self, val):
        self._prop_dict["apps"] = val
    @property
    def show_task_bar(self):
        """Gets and sets the showTaskBar
        
        Returns: 
            bool:
                The showTaskBar
        """
        if "showTaskBar" in self._prop_dict:
            return self._prop_dict["showTaskBar"]
        else:
            return None

    @show_task_bar.setter
    def show_task_bar(self, val):
        self._prop_dict["showTaskBar"] = val

