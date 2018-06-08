# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.item_body import ItemBody
from ..model.date_time_time_zone import DateTimeTimeZone
from ..model.importance import Importance
from ..model.patterned_recurrence import PatternedRecurrence
from ..model.sensitivity import Sensitivity
from ..model.task_status import TaskStatus
from ..model.single_value_legacy_extended_property import SingleValueLegacyExtendedProperty
from ..model.multi_value_legacy_extended_property import MultiValueLegacyExtendedProperty
from ..model.attachment import Attachment
from ..one_drive_object_base import OneDriveObjectBase


class OutlookTask(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def assigned_to(self):
        """
        Gets and sets the assignedTo
        
        Returns:
            str:
                The assignedTo
        """
        if "assignedTo" in self._prop_dict:
            return self._prop_dict["assignedTo"]
        else:
            return None

    @assigned_to.setter
    def assigned_to(self, val):
        self._prop_dict["assignedTo"] = val

    @property
    def body(self):
        """
        Gets and sets the body
        
        Returns: 
            :class:`ItemBody<onedrivesdk.model.item_body.ItemBody>`:
                The body
        """
        if "body" in self._prop_dict:
            if isinstance(self._prop_dict["body"], OneDriveObjectBase):
                return self._prop_dict["body"]
            else :
                self._prop_dict["body"] = ItemBody(self._prop_dict["body"])
                return self._prop_dict["body"]

        return None

    @body.setter
    def body(self, val):
        self._prop_dict["body"] = val

    @property
    def completed_date_time(self):
        """
        Gets and sets the completedDateTime
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The completedDateTime
        """
        if "completedDateTime" in self._prop_dict:
            if isinstance(self._prop_dict["completedDateTime"], OneDriveObjectBase):
                return self._prop_dict["completedDateTime"]
            else :
                self._prop_dict["completedDateTime"] = DateTimeTimeZone(self._prop_dict["completedDateTime"])
                return self._prop_dict["completedDateTime"]

        return None

    @completed_date_time.setter
    def completed_date_time(self, val):
        self._prop_dict["completedDateTime"] = val

    @property
    def due_date_time(self):
        """
        Gets and sets the dueDateTime
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The dueDateTime
        """
        if "dueDateTime" in self._prop_dict:
            if isinstance(self._prop_dict["dueDateTime"], OneDriveObjectBase):
                return self._prop_dict["dueDateTime"]
            else :
                self._prop_dict["dueDateTime"] = DateTimeTimeZone(self._prop_dict["dueDateTime"])
                return self._prop_dict["dueDateTime"]

        return None

    @due_date_time.setter
    def due_date_time(self, val):
        self._prop_dict["dueDateTime"] = val

    @property
    def has_attachments(self):
        """
        Gets and sets the hasAttachments
        
        Returns:
            bool:
                The hasAttachments
        """
        if "hasAttachments" in self._prop_dict:
            return self._prop_dict["hasAttachments"]
        else:
            return None

    @has_attachments.setter
    def has_attachments(self, val):
        self._prop_dict["hasAttachments"] = val

    @property
    def importance(self):
        """
        Gets and sets the importance
        
        Returns: 
            :class:`Importance<onedrivesdk.model.importance.Importance>`:
                The importance
        """
        if "importance" in self._prop_dict:
            if isinstance(self._prop_dict["importance"], OneDriveObjectBase):
                return self._prop_dict["importance"]
            else :
                self._prop_dict["importance"] = Importance(self._prop_dict["importance"])
                return self._prop_dict["importance"]

        return None

    @importance.setter
    def importance(self, val):
        self._prop_dict["importance"] = val

    @property
    def is_reminder_on(self):
        """
        Gets and sets the isReminderOn
        
        Returns:
            bool:
                The isReminderOn
        """
        if "isReminderOn" in self._prop_dict:
            return self._prop_dict["isReminderOn"]
        else:
            return None

    @is_reminder_on.setter
    def is_reminder_on(self, val):
        self._prop_dict["isReminderOn"] = val

    @property
    def owner(self):
        """
        Gets and sets the owner
        
        Returns:
            str:
                The owner
        """
        if "owner" in self._prop_dict:
            return self._prop_dict["owner"]
        else:
            return None

    @owner.setter
    def owner(self, val):
        self._prop_dict["owner"] = val

    @property
    def parent_folder_id(self):
        """
        Gets and sets the parentFolderId
        
        Returns:
            str:
                The parentFolderId
        """
        if "parentFolderId" in self._prop_dict:
            return self._prop_dict["parentFolderId"]
        else:
            return None

    @parent_folder_id.setter
    def parent_folder_id(self, val):
        self._prop_dict["parentFolderId"] = val

    @property
    def recurrence(self):
        """
        Gets and sets the recurrence
        
        Returns: 
            :class:`PatternedRecurrence<onedrivesdk.model.patterned_recurrence.PatternedRecurrence>`:
                The recurrence
        """
        if "recurrence" in self._prop_dict:
            if isinstance(self._prop_dict["recurrence"], OneDriveObjectBase):
                return self._prop_dict["recurrence"]
            else :
                self._prop_dict["recurrence"] = PatternedRecurrence(self._prop_dict["recurrence"])
                return self._prop_dict["recurrence"]

        return None

    @recurrence.setter
    def recurrence(self, val):
        self._prop_dict["recurrence"] = val

    @property
    def reminder_date_time(self):
        """
        Gets and sets the reminderDateTime
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The reminderDateTime
        """
        if "reminderDateTime" in self._prop_dict:
            if isinstance(self._prop_dict["reminderDateTime"], OneDriveObjectBase):
                return self._prop_dict["reminderDateTime"]
            else :
                self._prop_dict["reminderDateTime"] = DateTimeTimeZone(self._prop_dict["reminderDateTime"])
                return self._prop_dict["reminderDateTime"]

        return None

    @reminder_date_time.setter
    def reminder_date_time(self, val):
        self._prop_dict["reminderDateTime"] = val

    @property
    def sensitivity(self):
        """
        Gets and sets the sensitivity
        
        Returns: 
            :class:`Sensitivity<onedrivesdk.model.sensitivity.Sensitivity>`:
                The sensitivity
        """
        if "sensitivity" in self._prop_dict:
            if isinstance(self._prop_dict["sensitivity"], OneDriveObjectBase):
                return self._prop_dict["sensitivity"]
            else :
                self._prop_dict["sensitivity"] = Sensitivity(self._prop_dict["sensitivity"])
                return self._prop_dict["sensitivity"]

        return None

    @sensitivity.setter
    def sensitivity(self, val):
        self._prop_dict["sensitivity"] = val

    @property
    def start_date_time(self):
        """
        Gets and sets the startDateTime
        
        Returns: 
            :class:`DateTimeTimeZone<onedrivesdk.model.date_time_time_zone.DateTimeTimeZone>`:
                The startDateTime
        """
        if "startDateTime" in self._prop_dict:
            if isinstance(self._prop_dict["startDateTime"], OneDriveObjectBase):
                return self._prop_dict["startDateTime"]
            else :
                self._prop_dict["startDateTime"] = DateTimeTimeZone(self._prop_dict["startDateTime"])
                return self._prop_dict["startDateTime"]

        return None

    @start_date_time.setter
    def start_date_time(self, val):
        self._prop_dict["startDateTime"] = val

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`TaskStatus<onedrivesdk.model.task_status.TaskStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = TaskStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def subject(self):
        """
        Gets and sets the subject
        
        Returns:
            str:
                The subject
        """
        if "subject" in self._prop_dict:
            return self._prop_dict["subject"]
        else:
            return None

    @subject.setter
    def subject(self, val):
        self._prop_dict["subject"] = val

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

    @property
    def attachments(self):
        """Gets and sets the attachments
        
        Returns: 
            :class:`AttachmentsCollectionPage<onedrivesdk.request.attachments_collection.AttachmentsCollectionPage>`:
                The attachments
        """
        if "attachments" in self._prop_dict:
            return AttachmentsCollectionPage(self._prop_dict["attachments"])
        else:
            return None

