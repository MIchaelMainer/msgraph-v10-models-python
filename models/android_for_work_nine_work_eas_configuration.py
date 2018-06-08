# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class AndroidForWorkNineWorkEasConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def sync_calendar(self):
        """
        Gets and sets the syncCalendar
        
        Returns:
            bool:
                The syncCalendar
        """
        if "syncCalendar" in self._prop_dict:
            return self._prop_dict["syncCalendar"]
        else:
            return None

    @sync_calendar.setter
    def sync_calendar(self, val):
        self._prop_dict["syncCalendar"] = val

    @property
    def sync_contacts(self):
        """
        Gets and sets the syncContacts
        
        Returns:
            bool:
                The syncContacts
        """
        if "syncContacts" in self._prop_dict:
            return self._prop_dict["syncContacts"]
        else:
            return None

    @sync_contacts.setter
    def sync_contacts(self, val):
        self._prop_dict["syncContacts"] = val

    @property
    def sync_tasks(self):
        """
        Gets and sets the syncTasks
        
        Returns:
            bool:
                The syncTasks
        """
        if "syncTasks" in self._prop_dict:
            return self._prop_dict["syncTasks"]
        else:
            return None

    @sync_tasks.setter
    def sync_tasks(self, val):
        self._prop_dict["syncTasks"] = val

