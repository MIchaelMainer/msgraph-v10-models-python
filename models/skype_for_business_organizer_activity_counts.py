# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class SkypeForBusinessOrganizerActivityCounts(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def im(self):
        """
        Gets and sets the im
        
        Returns:
            int:
                The im
        """
        if "im" in self._prop_dict:
            return self._prop_dict["im"]
        else:
            return None

    @im.setter
    def im(self, val):
        self._prop_dict["im"] = val

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
    def app_sharing(self):
        """
        Gets and sets the appSharing
        
        Returns:
            int:
                The appSharing
        """
        if "appSharing" in self._prop_dict:
            return self._prop_dict["appSharing"]
        else:
            return None

    @app_sharing.setter
    def app_sharing(self, val):
        self._prop_dict["appSharing"] = val

    @property
    def web(self):
        """
        Gets and sets the web
        
        Returns:
            int:
                The web
        """
        if "web" in self._prop_dict:
            return self._prop_dict["web"]
        else:
            return None

    @web.setter
    def web(self, val):
        self._prop_dict["web"] = val

    @property
    def dial_in_out3rd_party(self):
        """
        Gets and sets the dialInOut3rdParty
        
        Returns:
            int:
                The dialInOut3rdParty
        """
        if "dialInOut3rdParty" in self._prop_dict:
            return self._prop_dict["dialInOut3rdParty"]
        else:
            return None

    @dial_in_out3rd_party.setter
    def dial_in_out3rd_party(self, val):
        self._prop_dict["dialInOut3rdParty"] = val

    @property
    def dial_in_out_microsoft(self):
        """
        Gets and sets the dialInOutMicrosoft
        
        Returns:
            int:
                The dialInOutMicrosoft
        """
        if "dialInOutMicrosoft" in self._prop_dict:
            return self._prop_dict["dialInOutMicrosoft"]
        else:
            return None

    @dial_in_out_microsoft.setter
    def dial_in_out_microsoft(self, val):
        self._prop_dict["dialInOutMicrosoft"] = val

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

