# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class EventCreationOptions(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def save_to_group_calendar_only(self):
        """Gets and sets the saveToGroupCalendarOnly
        
        Returns: 
            bool:
                The saveToGroupCalendarOnly
        """
        if "saveToGroupCalendarOnly" in self._prop_dict:
            return self._prop_dict["saveToGroupCalendarOnly"]
        else:
            return None

    @save_to_group_calendar_only.setter
    def save_to_group_calendar_only(self, val):
        self._prop_dict["saveToGroupCalendarOnly"] = val

