# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.location import Location
from ..model.date_time_time_zone import DateTimeTimeZone
from ..model.duration import Duration
from ..model.booking_price_type import BookingPriceType
from ..model.booking_reminder import BookingReminder
from ..model.booking_invoice_status import BookingInvoiceStatus
from ..one_drive_object_base import OneDriveObjectBase


class BookingAppointment(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def self_service_appointment_id(self):
        """
        Gets and sets the selfServiceAppointmentId
        
        Returns:
            str:
                The selfServiceAppointmentId
        """
        if "selfServiceAppointmentId" in self._prop_dict:
            return self._prop_dict["selfServiceAppointmentId"]
        else:
            return None

    @self_service_appointment_id.setter
    def self_service_appointment_id(self, val):
        self._prop_dict["selfServiceAppointmentId"] = val

    @property
    def customer_id(self):
        """
        Gets and sets the customerId
        
        Returns:
            str:
                The customerId
        """
        if "customerId" in self._prop_dict:
            return self._prop_dict["customerId"]
        else:
            return None

    @customer_id.setter
    def customer_id(self, val):
        self._prop_dict["customerId"] = val

    @property
    def customer_name(self):
        """
        Gets and sets the customerName
        
        Returns:
            str:
                The customerName
        """
        if "customerName" in self._prop_dict:
            return self._prop_dict["customerName"]
        else:
            return None

    @customer_name.setter
    def customer_name(self, val):
        self._prop_dict["customerName"] = val

    @property
    def customer_email_address(self):
        """
        Gets and sets the customerEmailAddress
        
        Returns:
            str:
                The customerEmailAddress
        """
        if "customerEmailAddress" in self._prop_dict:
            return self._prop_dict["customerEmailAddress"]
        else:
            return None

    @customer_email_address.setter
    def customer_email_address(self, val):
        self._prop_dict["customerEmailAddress"] = val

    @property
    def customer_phone(self):
        """
        Gets and sets the customerPhone
        
        Returns:
            str:
                The customerPhone
        """
        if "customerPhone" in self._prop_dict:
            return self._prop_dict["customerPhone"]
        else:
            return None

    @customer_phone.setter
    def customer_phone(self, val):
        self._prop_dict["customerPhone"] = val

    @property
    def customer_location(self):
        """
        Gets and sets the customerLocation
        
        Returns: 
            :class:`Location<onedrivesdk.model.location.Location>`:
                The customerLocation
        """
        if "customerLocation" in self._prop_dict:
            if isinstance(self._prop_dict["customerLocation"], OneDriveObjectBase):
                return self._prop_dict["customerLocation"]
            else :
                self._prop_dict["customerLocation"] = Location(self._prop_dict["customerLocation"])
                return self._prop_dict["customerLocation"]

        return None

    @customer_location.setter
    def customer_location(self, val):
        self._prop_dict["customerLocation"] = val

    @property
    def customer_notes(self):
        """
        Gets and sets the customerNotes
        
        Returns:
            str:
                The customerNotes
        """
        if "customerNotes" in self._prop_dict:
            return self._prop_dict["customerNotes"]
        else:
            return None

    @customer_notes.setter
    def customer_notes(self, val):
        self._prop_dict["customerNotes"] = val

    @property
    def service_id(self):
        """
        Gets and sets the serviceId
        
        Returns:
            str:
                The serviceId
        """
        if "serviceId" in self._prop_dict:
            return self._prop_dict["serviceId"]
        else:
            return None

    @service_id.setter
    def service_id(self, val):
        self._prop_dict["serviceId"] = val

    @property
    def service_name(self):
        """
        Gets and sets the serviceName
        
        Returns:
            str:
                The serviceName
        """
        if "serviceName" in self._prop_dict:
            return self._prop_dict["serviceName"]
        else:
            return None

    @service_name.setter
    def service_name(self, val):
        self._prop_dict["serviceName"] = val

    @property
    def start(self):
        """
        Gets and sets the start
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The start
        """
        if "start" in self._prop_dict:
            if isinstance(self._prop_dict["start"], OneDriveObjectBase):
                return self._prop_dict["start"]
            else :
                self._prop_dict["start"] = DateTimeTimeZone(self._prop_dict["start"])
                return self._prop_dict["start"]

        return None

    @start.setter
    def start(self, val):
        self._prop_dict["start"] = val

    @property
    def end(self):
        """
        Gets and sets the end
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The end
        """
        if "end" in self._prop_dict:
            if isinstance(self._prop_dict["end"], OneDriveObjectBase):
                return self._prop_dict["end"]
            else :
                self._prop_dict["end"] = DateTimeTimeZone(self._prop_dict["end"])
                return self._prop_dict["end"]

        return None

    @end.setter
    def end(self, val):
        self._prop_dict["end"] = val

    @property
    def duration(self):
        """
        Gets and sets the duration
        
        Returns: 
            :class:`Duration<onedrivesdk.model.duration.Duration>`:
                The duration
        """
        if "duration" in self._prop_dict:
            if isinstance(self._prop_dict["duration"], OneDriveObjectBase):
                return self._prop_dict["duration"]
            else :
                self._prop_dict["duration"] = Duration(self._prop_dict["duration"])
                return self._prop_dict["duration"]

        return None

    @duration.setter
    def duration(self, val):
        self._prop_dict["duration"] = val

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
    def service_location(self):
        """
        Gets and sets the serviceLocation
        
        Returns: 
            :class:`Location<onedrivesdk.model.location.Location>`:
                The serviceLocation
        """
        if "serviceLocation" in self._prop_dict:
            if isinstance(self._prop_dict["serviceLocation"], OneDriveObjectBase):
                return self._prop_dict["serviceLocation"]
            else :
                self._prop_dict["serviceLocation"] = Location(self._prop_dict["serviceLocation"])
                return self._prop_dict["serviceLocation"]

        return None

    @service_location.setter
    def service_location(self, val):
        self._prop_dict["serviceLocation"] = val

    @property
    def price_type(self):
        """
        Gets and sets the priceType
        
        Returns: 
            :class:`BookingPriceType<onedrivesdk.model.booking_price_type.BookingPriceType>`:
                The priceType
        """
        if "priceType" in self._prop_dict:
            if isinstance(self._prop_dict["priceType"], OneDriveObjectBase):
                return self._prop_dict["priceType"]
            else :
                self._prop_dict["priceType"] = BookingPriceType(self._prop_dict["priceType"])
                return self._prop_dict["priceType"]

        return None

    @price_type.setter
    def price_type(self, val):
        self._prop_dict["priceType"] = val

    @property
    def price(self):
        """
        Gets and sets the price
        
        Returns:
            float:
                The price
        """
        if "price" in self._prop_dict:
            return self._prop_dict["price"]
        else:
            return None

    @price.setter
    def price(self, val):
        self._prop_dict["price"] = val

    @property
    def service_notes(self):
        """
        Gets and sets the serviceNotes
        
        Returns:
            str:
                The serviceNotes
        """
        if "serviceNotes" in self._prop_dict:
            return self._prop_dict["serviceNotes"]
        else:
            return None

    @service_notes.setter
    def service_notes(self, val):
        self._prop_dict["serviceNotes"] = val

    @property
    def reminders(self):
        """Gets and sets the reminders
        
        Returns: 
            :class:`RemindersCollectionPage<onedrivesdk.request.reminders_collection.RemindersCollectionPage>`:
                The reminders
        """
        if "reminders" in self._prop_dict:
            return RemindersCollectionPage(self._prop_dict["reminders"])
        else:
            return None

    @property
    def opt_out_of_customer_email(self):
        """
        Gets and sets the optOutOfCustomerEmail
        
        Returns:
            bool:
                The optOutOfCustomerEmail
        """
        if "optOutOfCustomerEmail" in self._prop_dict:
            return self._prop_dict["optOutOfCustomerEmail"]
        else:
            return None

    @opt_out_of_customer_email.setter
    def opt_out_of_customer_email(self, val):
        self._prop_dict["optOutOfCustomerEmail"] = val

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

    @property
    def invoice_amount(self):
        """
        Gets and sets the invoiceAmount
        
        Returns:
            float:
                The invoiceAmount
        """
        if "invoiceAmount" in self._prop_dict:
            return self._prop_dict["invoiceAmount"]
        else:
            return None

    @invoice_amount.setter
    def invoice_amount(self, val):
        self._prop_dict["invoiceAmount"] = val

    @property
    def invoice_date(self):
        """
        Gets and sets the invoiceDate
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The invoiceDate
        """
        if "invoiceDate" in self._prop_dict:
            if isinstance(self._prop_dict["invoiceDate"], OneDriveObjectBase):
                return self._prop_dict["invoiceDate"]
            else :
                self._prop_dict["invoiceDate"] = DateTimeTimeZone(self._prop_dict["invoiceDate"])
                return self._prop_dict["invoiceDate"]

        return None

    @invoice_date.setter
    def invoice_date(self, val):
        self._prop_dict["invoiceDate"] = val

    @property
    def invoice_id(self):
        """
        Gets and sets the invoiceId
        
        Returns:
            str:
                The invoiceId
        """
        if "invoiceId" in self._prop_dict:
            return self._prop_dict["invoiceId"]
        else:
            return None

    @invoice_id.setter
    def invoice_id(self, val):
        self._prop_dict["invoiceId"] = val

    @property
    def invoice_status(self):
        """
        Gets and sets the invoiceStatus
        
        Returns: 
            :class:`BookingInvoiceStatus<onedrivesdk.model.booking_invoice_status.BookingInvoiceStatus>`:
                The invoiceStatus
        """
        if "invoiceStatus" in self._prop_dict:
            if isinstance(self._prop_dict["invoiceStatus"], OneDriveObjectBase):
                return self._prop_dict["invoiceStatus"]
            else :
                self._prop_dict["invoiceStatus"] = BookingInvoiceStatus(self._prop_dict["invoiceStatus"])
                return self._prop_dict["invoiceStatus"]

        return None

    @invoice_status.setter
    def invoice_status(self, val):
        self._prop_dict["invoiceStatus"] = val

    @property
    def invoice_url(self):
        """
        Gets and sets the invoiceUrl
        
        Returns:
            str:
                The invoiceUrl
        """
        if "invoiceUrl" in self._prop_dict:
            return self._prop_dict["invoiceUrl"]
        else:
            return None

    @invoice_url.setter
    def invoice_url(self, val):
        self._prop_dict["invoiceUrl"] = val

