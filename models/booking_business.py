# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.physical_address import PhysicalAddress
from ..model.booking_work_hours import BookingWorkHours
from ..model.booking_scheduling_policy import BookingSchedulingPolicy
from ..model.booking_appointment import BookingAppointment
from ..model.booking_customer import BookingCustomer
from ..model.booking_service import BookingService
from ..model.booking_staff_member import BookingStaffMember
from ..one_drive_object_base import OneDriveObjectBase


class BookingBusiness(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def business_type(self):
        """
        Gets and sets the businessType
        
        Returns:
            str:
                The businessType
        """
        if "businessType" in self._prop_dict:
            return self._prop_dict["businessType"]
        else:
            return None

    @business_type.setter
    def business_type(self, val):
        self._prop_dict["businessType"] = val

    @property
    def address(self):
        """
        Gets and sets the address
        
        Returns: 
            :class:`PhysicalAddress<onedrivesdk.model.physical_address.PhysicalAddress>`:
                The address
        """
        if "address" in self._prop_dict:
            if isinstance(self._prop_dict["address"], OneDriveObjectBase):
                return self._prop_dict["address"]
            else :
                self._prop_dict["address"] = PhysicalAddress(self._prop_dict["address"])
                return self._prop_dict["address"]

        return None

    @address.setter
    def address(self, val):
        self._prop_dict["address"] = val

    @property
    def phone(self):
        """
        Gets and sets the phone
        
        Returns:
            str:
                The phone
        """
        if "phone" in self._prop_dict:
            return self._prop_dict["phone"]
        else:
            return None

    @phone.setter
    def phone(self, val):
        self._prop_dict["phone"] = val

    @property
    def email(self):
        """
        Gets and sets the email
        
        Returns:
            str:
                The email
        """
        if "email" in self._prop_dict:
            return self._prop_dict["email"]
        else:
            return None

    @email.setter
    def email(self, val):
        self._prop_dict["email"] = val

    @property
    def web_site_url(self):
        """
        Gets and sets the webSiteUrl
        
        Returns:
            str:
                The webSiteUrl
        """
        if "webSiteUrl" in self._prop_dict:
            return self._prop_dict["webSiteUrl"]
        else:
            return None

    @web_site_url.setter
    def web_site_url(self, val):
        self._prop_dict["webSiteUrl"] = val

    @property
    def default_currency_iso(self):
        """
        Gets and sets the defaultCurrencyIso
        
        Returns:
            str:
                The defaultCurrencyIso
        """
        if "defaultCurrencyIso" in self._prop_dict:
            return self._prop_dict["defaultCurrencyIso"]
        else:
            return None

    @default_currency_iso.setter
    def default_currency_iso(self, val):
        self._prop_dict["defaultCurrencyIso"] = val

    @property
    def business_hours(self):
        """Gets and sets the businessHours
        
        Returns: 
            :class:`BusinessHoursCollectionPage<onedrivesdk.request.business_hours_collection.BusinessHoursCollectionPage>`:
                The businessHours
        """
        if "businessHours" in self._prop_dict:
            return BusinessHoursCollectionPage(self._prop_dict["businessHours"])
        else:
            return None

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
    def is_published(self):
        """
        Gets and sets the isPublished
        
        Returns:
            bool:
                The isPublished
        """
        if "isPublished" in self._prop_dict:
            return self._prop_dict["isPublished"]
        else:
            return None

    @is_published.setter
    def is_published(self, val):
        self._prop_dict["isPublished"] = val

    @property
    def public_url(self):
        """
        Gets and sets the publicUrl
        
        Returns:
            str:
                The publicUrl
        """
        if "publicUrl" in self._prop_dict:
            return self._prop_dict["publicUrl"]
        else:
            return None

    @public_url.setter
    def public_url(self, val):
        self._prop_dict["publicUrl"] = val

    @property
    def appointments(self):
        """Gets and sets the appointments
        
        Returns: 
            :class:`AppointmentsCollectionPage<onedrivesdk.request.appointments_collection.AppointmentsCollectionPage>`:
                The appointments
        """
        if "appointments" in self._prop_dict:
            return AppointmentsCollectionPage(self._prop_dict["appointments"])
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
    def customers(self):
        """Gets and sets the customers
        
        Returns: 
            :class:`CustomersCollectionPage<onedrivesdk.request.customers_collection.CustomersCollectionPage>`:
                The customers
        """
        if "customers" in self._prop_dict:
            return CustomersCollectionPage(self._prop_dict["customers"])
        else:
            return None

    @property
    def services(self):
        """Gets and sets the services
        
        Returns: 
            :class:`ServicesCollectionPage<onedrivesdk.request.services_collection.ServicesCollectionPage>`:
                The services
        """
        if "services" in self._prop_dict:
            return ServicesCollectionPage(self._prop_dict["services"])
        else:
            return None

    @property
    def staff_members(self):
        """Gets and sets the staffMembers
        
        Returns: 
            :class:`StaffMembersCollectionPage<onedrivesdk.request.staff_members_collection.StaffMembersCollectionPage>`:
                The staffMembers
        """
        if "staffMembers" in self._prop_dict:
            return StaffMembersCollectionPage(self._prop_dict["staffMembers"])
        else:
            return None

