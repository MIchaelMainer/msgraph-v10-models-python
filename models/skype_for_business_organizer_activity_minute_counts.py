# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class SkypeForBusinessOrganizerActivityMinuteCounts(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def audio_video(self):
        """
        Gets and sets the audioVideo
        
        Returns:
            int:
                The audioVideo
        """
        if "audioVideo" in self._prop_dict:
            return self._prop_dict["audioVideo"]
        else:
            return None

    @audio_video.setter
    def audio_video(self, val):
        self._prop_dict["audioVideo"] = val

    @property
    def dial_in_microsoft(self):
        """
        Gets and sets the dialInMicrosoft
        
        Returns:
            int:
                The dialInMicrosoft
        """
        if "dialInMicrosoft" in self._prop_dict:
            return self._prop_dict["dialInMicrosoft"]
        else:
            return None

    @dial_in_microsoft.setter
    def dial_in_microsoft(self, val):
        self._prop_dict["dialInMicrosoft"] = val

    @property
    def dial_out_microsoft(self):
        """
        Gets and sets the dialOutMicrosoft
        
        Returns:
            int:
                The dialOutMicrosoft
        """
        if "dialOutMicrosoft" in self._prop_dict:
            return self._prop_dict["dialOutMicrosoft"]
        else:
            return None

    @dial_out_microsoft.setter
    def dial_out_microsoft(self, val):
        self._prop_dict["dialOutMicrosoft"] = val

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
    def report_date(self):
        """
        Gets and sets the reportDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The reportDate
        """
        if "reportDate" in self._prop_dict:
            if isinstance(self._prop_dict["reportDate"], OneDriveObjectBase):
                return self._prop_dict["reportDate"]
            else :
                self._prop_dict["reportDate"] = Date(self._prop_dict["reportDate"])
                return self._prop_dict["reportDate"]

        return None

    @report_date.setter
    def report_date(self, val):
        self._prop_dict["reportDate"] = val

    @property
    def report_period(self):
        """
        Gets and sets the reportPeriod
        
        Returns:
            str:
                The reportPeriod
        """
        if "reportPeriod" in self._prop_dict:
            return self._prop_dict["reportPeriod"]
        else:
            return None

    @report_period.setter
    def report_period(self, val):
        self._prop_dict["reportPeriod"] = val

