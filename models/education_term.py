# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class EducationTerm(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def external_id(self):
        """Gets and sets the externalId
        
        Returns: 
            str:
                The externalId
        """
        if "externalId" in self._prop_dict:
            return self._prop_dict["externalId"]
        else:
            return None

    @external_id.setter
    def external_id(self, val):
        self._prop_dict["externalId"] = val

    @property
    def start_date(self):
        """
        Gets and sets the startDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The startDate
        """
        if "startDate" in self._prop_dict:
            if isinstance(self._prop_dict["startDate"], OneDriveObjectBase):
                return self._prop_dict["startDate"]
            else :
                self._prop_dict["startDate"] = Date(self._prop_dict["startDate"])
                return self._prop_dict["startDate"]

        return None

    @start_date.setter
    def start_date(self, val):
        self._prop_dict["startDate"] = val
    @property
    def end_date(self):
        """
        Gets and sets the endDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The endDate
        """
        if "endDate" in self._prop_dict:
            if isinstance(self._prop_dict["endDate"], OneDriveObjectBase):
                return self._prop_dict["endDate"]
            else :
                self._prop_dict["endDate"] = Date(self._prop_dict["endDate"])
                return self._prop_dict["endDate"]

        return None

    @end_date.setter
    def end_date(self, val):
        self._prop_dict["endDate"] = val
    @property
    def display_name(self):
        """Gets and sets the displayName
        
        Returns: 
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

