# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class Office365ActivationsUserCounts(OneDriveObjectBase):

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
    def assigned(self):
        """
        Gets and sets the assigned
        
        Returns:
            int:
                The assigned
        """
        if "assigned" in self._prop_dict:
            return self._prop_dict["assigned"]
        else:
            return None

    @assigned.setter
    def assigned(self, val):
        self._prop_dict["assigned"] = val

    @property
    def activated(self):
        """
        Gets and sets the activated
        
        Returns:
            int:
                The activated
        """
        if "activated" in self._prop_dict:
            return self._prop_dict["activated"]
        else:
            return None

    @activated.setter
    def activated(self, val):
        self._prop_dict["activated"] = val

    @property
    def shared_computer_activation(self):
        """
        Gets and sets the sharedComputerActivation
        
        Returns:
            int:
                The sharedComputerActivation
        """
        if "sharedComputerActivation" in self._prop_dict:
            return self._prop_dict["sharedComputerActivation"]
        else:
            return None

    @shared_computer_activation.setter
    def shared_computer_activation(self, val):
        self._prop_dict["sharedComputerActivation"] = val

