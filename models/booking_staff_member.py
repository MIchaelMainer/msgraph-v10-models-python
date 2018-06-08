# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.booking_staff_role import BookingStaffRole
from ..model.booking_work_hours import BookingWorkHours
from ..one_drive_object_base import OneDriveObjectBase


class BookingStaffMember(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def availability_is_affected_by_personal_calendar(self):
        """
        Gets and sets the availabilityIsAffectedByPersonalCalendar
        
        Returns:
            bool:
                The availabilityIsAffectedByPersonalCalendar
        """
        if "availabilityIsAffectedByPersonalCalendar" in self._prop_dict:
            return self._prop_dict["availabilityIsAffectedByPersonalCalendar"]
        else:
            return None

    @availability_is_affected_by_personal_calendar.setter
    def availability_is_affected_by_personal_calendar(self, val):
        self._prop_dict["availabilityIsAffectedByPersonalCalendar"] = val

    @property
    def color_index(self):
        """
        Gets and sets the colorIndex
        
        Returns:
            int:
                The colorIndex
        """
        if "colorIndex" in self._prop_dict:
            return self._prop_dict["colorIndex"]
        else:
            return None

    @color_index.setter
    def color_index(self, val):
        self._prop_dict["colorIndex"] = val

    @property
    def role(self):
        """
        Gets and sets the role
        
        Returns: 
            :class:`BookingStaffRole<onedrivesdk.model.booking_staff_role.BookingStaffRole>`:
                The role
        """
        if "role" in self._prop_dict:
            if isinstance(self._prop_dict["role"], OneDriveObjectBase):
                return self._prop_dict["role"]
            else :
                self._prop_dict["role"] = BookingStaffRole(self._prop_dict["role"])
                return self._prop_dict["role"]

        return None

    @role.setter
    def role(self, val):
        self._prop_dict["role"] = val

    @property
    def use_business_hours(self):
        """
        Gets and sets the useBusinessHours
        
        Returns:
            bool:
                The useBusinessHours
        """
        if "useBusinessHours" in self._prop_dict:
            return self._prop_dict["useBusinessHours"]
        else:
            return None

    @use_business_hours.setter
    def use_business_hours(self, val):
        self._prop_dict["useBusinessHours"] = val

    @property
    def working_hours(self):
        """Gets and sets the workingHours
        
        Returns: 
            :class:`WorkingHoursCollectionPage<onedrivesdk.request.working_hours_collection.WorkingHoursCollectionPage>`:
                The workingHours
        """
        if "workingHours" in self._prop_dict:
            return WorkingHoursCollectionPage(self._prop_dict["workingHours"])
        else:
            return None

