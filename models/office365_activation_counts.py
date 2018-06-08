# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class Office365ActivationCounts(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def report_refresh_date(self):
        """
        Gets and sets the reportRefreshDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The reportRefreshDate
        """
        if "reportRefreshDate" in self._prop_dict:
            if isinstance(self._prop_dict["reportRefreshDate"], OneDriveObjectBase):
                return self._prop_dict["reportRefreshDate"]
            else :
                self._prop_dict["reportRefreshDate"] = Date(self._prop_dict["reportRefreshDate"])
                return self._prop_dict["reportRefreshDate"]

        return None

    @report_refresh_date.setter
    def report_refresh_date(self, val):
        self._prop_dict["reportRefreshDate"] = val

    @property
    def product_type(self):
        """
        Gets and sets the productType
        
        Returns:
            str:
                The productType
        """
        if "productType" in self._prop_dict:
            return self._prop_dict["productType"]
        else:
            return None

    @product_type.setter
    def product_type(self, val):
        self._prop_dict["productType"] = val

    @property
    def windows(self):
        """
        Gets and sets the windows
        
        Returns:
            int:
                The windows
        """
        if "windows" in self._prop_dict:
            return self._prop_dict["windows"]
        else:
            return None

    @windows.setter
    def windows(self, val):
        self._prop_dict["windows"] = val

    @property
    def mac(self):
        """
        Gets and sets the mac
        
        Returns:
            int:
                The mac
        """
        if "mac" in self._prop_dict:
            return self._prop_dict["mac"]
        else:
            return None

    @mac.setter
    def mac(self, val):
        self._prop_dict["mac"] = val

    @property
    def android(self):
        """
        Gets and sets the android
        
        Returns:
            int:
                The android
        """
        if "android" in self._prop_dict:
            return self._prop_dict["android"]
        else:
            return None

    @android.setter
    def android(self, val):
        self._prop_dict["android"] = val

    @property
    def ios(self):
        """
        Gets and sets the ios
        
        Returns:
            int:
                The ios
        """
        if "ios" in self._prop_dict:
            return self._prop_dict["ios"]
        else:
            return None

    @ios.setter
    def ios(self, val):
        self._prop_dict["ios"] = val

    @property
    def windows10_mobile(self):
        """
        Gets and sets the windows10Mobile
        
        Returns:
            int:
                The windows10Mobile
        """
        if "windows10Mobile" in self._prop_dict:
            return self._prop_dict["windows10Mobile"]
        else:
            return None

    @windows10_mobile.setter
    def windows10_mobile(self, val):
        self._prop_dict["windows10Mobile"] = val

