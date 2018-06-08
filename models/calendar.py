# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.calendar_color import CalendarColor
from ..model.email_address import EmailAddress
from ..model.event import Event
from ..model.single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
from ..model.multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from ..one_drive_object_base import OneDriveObjectBase


class Calendar(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def name(self):
        """
        Gets and sets the name
        
        Returns:
            str:
                The name
        """
        if "name" in self._prop_dict:
            return self._prop_dict["name"]
        else:
            return None

    @name.setter
    def name(self, val):
        self._prop_dict["name"] = val

    @property
    def color(self):
        """
        Gets and sets the color
        
        Returns: 
            :class:`CalendarColor<onedrivesdk.model.calendar_color.CalendarColor>`:
                The color
        """
        if "color" in self._prop_dict:
            if isinstance(self._prop_dict["color"], OneDriveObjectBase):
                return self._prop_dict["color"]
            else :
                self._prop_dict["color"] = CalendarColor(self._prop_dict["color"])
                return self._prop_dict["color"]

        return None

    @color.setter
    def color(self, val):
        self._prop_dict["color"] = val

    @property
    def hex_color(self):
        """
        Gets and sets the hexColor
        
        Returns:
            str:
                The hexColor
        """
        if "hexColor" in self._prop_dict:
            return self._prop_dict["hexColor"]
        else:
            return None

    @hex_color.setter
    def hex_color(self, val):
        self._prop_dict["hexColor"] = val

    @property
    def is_default_calendar(self):
        """
        Gets and sets the isDefaultCalendar
        
        Returns:
            bool:
                The isDefaultCalendar
        """
        if "isDefaultCalendar" in self._prop_dict:
            return self._prop_dict["isDefaultCalendar"]
        else:
            return None

    @is_default_calendar.setter
    def is_default_calendar(self, val):
        self._prop_dict["isDefaultCalendar"] = val

    @property
    def change_key(self):
        """
        Gets and sets the changeKey
        
        Returns:
            str:
                The changeKey
        """
        if "changeKey" in self._prop_dict:
            return self._prop_dict["changeKey"]
        else:
            return None

    @change_key.setter
    def change_key(self, val):
        self._prop_dict["changeKey"] = val

    @property
    def can_share(self):
        """
        Gets and sets the canShare
        
        Returns:
            bool:
                The canShare
        """
        if "canShare" in self._prop_dict:
            return self._prop_dict["canShare"]
        else:
            return None

    @can_share.setter
    def can_share(self, val):
        self._prop_dict["canShare"] = val

    @property
    def can_view_private_items(self):
        """
        Gets and sets the canViewPrivateItems
        
        Returns:
            bool:
                The canViewPrivateItems
        """
        if "canViewPrivateItems" in self._prop_dict:
            return self._prop_dict["canViewPrivateItems"]
        else:
            return None

    @can_view_private_items.setter
    def can_view_private_items(self, val):
        self._prop_dict["canViewPrivateItems"] = val

    @property
    def is_shared(self):
        """
        Gets and sets the isShared
        
        Returns:
            bool:
                The isShared
        """
        if "isShared" in self._prop_dict:
            return self._prop_dict["isShared"]
        else:
            return None

    @is_shared.setter
    def is_shared(self, val):
        self._prop_dict["isShared"] = val

    @property
    def is_shared_with_me(self):
        """
        Gets and sets the isSharedWithMe
        
        Returns:
            bool:
                The isSharedWithMe
        """
        if "isSharedWithMe" in self._prop_dict:
            return self._prop_dict["isSharedWithMe"]
        else:
            return None

    @is_shared_with_me.setter
    def is_shared_with_me(self, val):
        self._prop_dict["isSharedWithMe"] = val

    @property
    def can_edit(self):
        """
        Gets and sets the canEdit
        
        Returns:
            bool:
                The canEdit
        """
        if "canEdit" in self._prop_dict:
            return self._prop_dict["canEdit"]
        else:
            return None

    @can_edit.setter
    def can_edit(self, val):
        self._prop_dict["canEdit"] = val

    @property
    def owner(self):
        """
        Gets and sets the owner
        
        Returns: 
            :class:`EmailAddress<onedrivesdk.model.email_address.EmailAddress>`:
                The owner
        """
        if "owner" in self._prop_dict:
            if isinstance(self._prop_dict["owner"], OneDriveObjectBase):
                return self._prop_dict["owner"]
            else :
                self._prop_dict["owner"] = EmailAddress(self._prop_dict["owner"])
                return self._prop_dict["owner"]

        return None

    @owner.setter
    def owner(self, val):
        self._prop_dict["owner"] = val

    @property
    def events(self):
        """Gets and sets the events
        
        Returns: 
            :class:`EventsCollectionPage<onedrivesdk.request.events_collection.EventsCollectionPage>`:
                The events
        """
        if "events" in self._prop_dict:
            return EventsCollectionPage(self._prop_dict["events"])
        else:
            return None

    @property
    def calendar_view(self):
        """Gets and sets the calendarView
        
        Returns: 
            :class:`CalendarViewCollectionPage<onedrivesdk.request.calendar_view_collection.CalendarViewCollectionPage>`:
                The calendarView
        """
        if "calendarView" in self._prop_dict:
            return CalendarViewCollectionPage(self._prop_dict["calendarView"])
        else:
            return None

    @property
    def single_value_extended_properties(self):
        """Gets and sets the singleValueExtendedProperties
        
        Returns: 
            :class:`SingleValueExtendedPropertiesCollectionPage<onedrivesdk.request.single_value_extended_properties_collection.SingleValueExtendedPropertiesCollectionPage>`:
                The singleValueExtendedProperties
        """
        if "singleValueExtendedProperties" in self._prop_dict:
            return SingleValueExtendedPropertiesCollectionPage(self._prop_dict["singleValueExtendedProperties"])
        else:
            return None

    @property
    def multi_value_extended_properties(self):
        """Gets and sets the multiValueExtendedProperties
        
        Returns: 
            :class:`MultiValueExtendedPropertiesCollectionPage<onedrivesdk.request.multi_value_extended_properties_collection.MultiValueExtendedPropertiesCollectionPage>`:
                The multiValueExtendedProperties
        """
        if "multiValueExtendedProperties" in self._prop_dict:
            return MultiValueExtendedPropertiesCollectionPage(self._prop_dict["multiValueExtendedProperties"])
        else:
            return None

