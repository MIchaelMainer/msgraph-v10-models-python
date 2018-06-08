# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.duration import Duration
from ..model.location import Location
from ..model.booking_price_type import BookingPriceType
from ..model.booking_reminder import BookingReminder
from ..model.booking_scheduling_policy import BookingSchedulingPolicy
from ..one_drive_object_base import OneDriveObjectBase


class BookingService(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def default_duration(self):
        """
        Gets and sets the defaultDuration
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The defaultDuration
        """
        if "defaultDuration" in self._prop_dict:
            if isinstance(self._prop_dict["defaultDuration"], OneDriveObjectBase):
                return self._prop_dict["defaultDuration"]
            else :
                self._prop_dict["defaultDuration"] = Duration(self._prop_dict["defaultDuration"])
                return self._prop_dict["defaultDuration"]

        return None

    @default_duration.setter
    def default_duration(self, val):
        self._prop_dict["defaultDuration"] = val

    @property
    def default_location(self):
        """
        Gets and sets the defaultLocation
        
        Returns: 
            :class:`Location<onedrivesdk.model.location.Location>`:
                The defaultLocation
        """
        if "defaultLocation" in self._prop_dict:
            if isinstance(self._prop_dict["defaultLocation"], OneDriveObjectBase):
                return self._prop_dict["defaultLocation"]
            else :
                self._prop_dict["defaultLocation"] = Location(self._prop_dict["defaultLocation"])
                return self._prop_dict["defaultLocation"]

        return None

    @default_location.setter
    def default_location(self, val):
        self._prop_dict["defaultLocation"] = val

    @property
    def default_price(self):
        """
        Gets and sets the defaultPrice
        
        Returns:
            float:
                The defaultPrice
        """
        if "defaultPrice" in self._prop_dict:
            return self._prop_dict["defaultPrice"]
        else:
            return None

    @default_price.setter
    def default_price(self, val):
        self._prop_dict["defaultPrice"] = val

    @property
    def default_price_type(self):
        """
        Gets and sets the defaultPriceType
        
        Returns: 
            :class:`BookingPriceType<onedrivesdk.model.booking_price_type.BookingPriceType>`:
                The defaultPriceType
        """
        if "defaultPriceType" in self._prop_dict:
            if isinstance(self._prop_dict["defaultPriceType"], OneDriveObjectBase):
                return self._prop_dict["defaultPriceType"]
            else :
                self._prop_dict["defaultPriceType"] = BookingPriceType(self._prop_dict["defaultPriceType"])
                return self._prop_dict["defaultPriceType"]

        return None

    @default_price_type.setter
    def default_price_type(self, val):
        self._prop_dict["defaultPriceType"] = val

    @property
    def default_reminders(self):
        """Gets and sets the defaultReminders
        
        Returns: 
            :class:`DefaultRemindersCollectionPage<onedrivesdk.request.default_reminders_collection.DefaultRemindersCollectionPage>`:
                The defaultReminders
        """
        if "defaultReminders" in self._prop_dict:
            return DefaultRemindersCollectionPage(self._prop_dict["defaultReminders"])
        else:
            return None

    @property
    def description(self):
        """
        Gets and sets the description
        
        Returns:
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

    @property
    def is_hidden_from_customers(self):
        """
        Gets and sets the isHiddenFromCustomers
        
        Returns:
            bool:
                The isHiddenFromCustomers
        """
        if "isHiddenFromCustomers" in self._prop_dict:
            return self._prop_dict["isHiddenFromCustomers"]
        else:
            return None

    @is_hidden_from_customers.setter
    def is_hidden_from_customers(self, val):
        self._prop_dict["isHiddenFromCustomers"] = val

    @property
    def notes(self):
        """
        Gets and sets the notes
        
        Returns:
            str:
                The notes
        """
        if "notes" in self._prop_dict:
            return self._prop_dict["notes"]
        else:
            return None

    @notes.setter
    def notes(self, val):
        self._prop_dict["notes"] = val

    @property
    def pre_buffer(self):
        """
        Gets and sets the preBuffer
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The preBuffer
        """
        if "preBuffer" in self._prop_dict:
            if isinstance(self._prop_dict["preBuffer"], OneDriveObjectBase):
                return self._prop_dict["preBuffer"]
            else :
                self._prop_dict["preBuffer"] = Duration(self._prop_dict["preBuffer"])
                return self._prop_dict["preBuffer"]

        return None

    @pre_buffer.setter
    def pre_buffer(self, val):
        self._prop_dict["preBuffer"] = val

    @property
    def post_buffer(self):
        """
        Gets and sets the postBuffer
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The postBuffer
        """
        if "postBuffer" in self._prop_dict:
            if isinstance(self._prop_dict["postBuffer"], OneDriveObjectBase):
                return self._prop_dict["postBuffer"]
            else :
                self._prop_dict["postBuffer"] = Duration(self._prop_dict["postBuffer"])
                return self._prop_dict["postBuffer"]

        return None

    @post_buffer.setter
    def post_buffer(self, val):
        self._prop_dict["postBuffer"] = val

    @property
    def scheduling_policy(self):
        """
        Gets and sets the schedulingPolicy
        
        Returns: 
            :class:`BookingSchedulingPolicy<onedrivesdk.model.booking_scheduling_policy.BookingSchedulingPolicy>`:
                The schedulingPolicy
        """
        if "schedulingPolicy" in self._prop_dict:
            if isinstance(self._prop_dict["schedulingPolicy"], OneDriveObjectBase):
                return self._prop_dict["schedulingPolicy"]
            else :
                self._prop_dict["schedulingPolicy"] = BookingSchedulingPolicy(self._prop_dict["schedulingPolicy"])
                return self._prop_dict["schedulingPolicy"]

        return None

    @scheduling_policy.setter
    def scheduling_policy(self, val):
        self._prop_dict["schedulingPolicy"] = val

    @property
    def staff_member_ids(self):
        """
        Gets and sets the staffMemberIds
        
        Returns:
            str:
                The staffMemberIds
        """
        if "staffMemberIds" in self._prop_dict:
            return self._prop_dict["staffMemberIds"]
        else:
            return None

    @staff_member_ids.setter
    def staff_member_ids(self, val):
        self._prop_dict["staffMemberIds"] = val

