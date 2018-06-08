# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.automatic_replies_setting import AutomaticRepliesSetting
from ..model.locale_info import LocaleInfo
from ..model.working_hours import WorkingHours
from ..one_drive_object_base import OneDriveObjectBase


class MailboxSettings(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def automatic_replies_setting(self):
        """
        Gets and sets the automaticRepliesSetting
        
        Returns: 
            :class:`AutomaticRepliesSetting<onedrivesdk.model.automatic_replies_setting.AutomaticRepliesSetting>`:
                The automaticRepliesSetting
        """
        if "automaticRepliesSetting" in self._prop_dict:
            if isinstance(self._prop_dict["automaticRepliesSetting"], OneDriveObjectBase):
                return self._prop_dict["automaticRepliesSetting"]
            else :
                self._prop_dict["automaticRepliesSetting"] = AutomaticRepliesSetting(self._prop_dict["automaticRepliesSetting"])
                return self._prop_dict["automaticRepliesSetting"]

        return None

    @automatic_replies_setting.setter
    def automatic_replies_setting(self, val):
        self._prop_dict["automaticRepliesSetting"] = val
    @property
    def archive_folder(self):
        """Gets and sets the archiveFolder
        
        Returns: 
            str:
                The archiveFolder
        """
        if "archiveFolder" in self._prop_dict:
            return self._prop_dict["archiveFolder"]
        else:
            return None

    @archive_folder.setter
    def archive_folder(self, val):
        self._prop_dict["archiveFolder"] = val

    @property
    def time_zone(self):
        """Gets and sets the timeZone
        
        Returns: 
            str:
                The timeZone
        """
        if "timeZone" in self._prop_dict:
            return self._prop_dict["timeZone"]
        else:
            return None

    @time_zone.setter
    def time_zone(self, val):
        self._prop_dict["timeZone"] = val

    @property
    def language(self):
        """
        Gets and sets the language
        
        Returns: 
            :class:`LocaleInfo<onedrivesdk.model.locale_info.LocaleInfo>`:
                The language
        """
        if "language" in self._prop_dict:
            if isinstance(self._prop_dict["language"], OneDriveObjectBase):
                return self._prop_dict["language"]
            else :
                self._prop_dict["language"] = LocaleInfo(self._prop_dict["language"])
                return self._prop_dict["language"]

        return None

    @language.setter
    def language(self, val):
        self._prop_dict["language"] = val
    @property
    def working_hours(self):
        """
        Gets and sets the workingHours
        
        Returns: 
            :class:`WorkingHours<onedrivesdk.model.working_hours.WorkingHours>`:
                The workingHours
        """
        if "workingHours" in self._prop_dict:
            if isinstance(self._prop_dict["workingHours"], OneDriveObjectBase):
                return self._prop_dict["workingHours"]
            else :
                self._prop_dict["workingHours"] = WorkingHours(self._prop_dict["workingHours"])
                return self._prop_dict["workingHours"]

        return None

    @working_hours.setter
    def working_hours(self, val):
        self._prop_dict["workingHours"] = val
