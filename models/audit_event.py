# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.audit_actor import AuditActor
from ..model.audit_resource import AuditResource
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class AuditEvent(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def component_name(self):
        """
        Gets and sets the componentName
        
        Returns:
            str:
                The componentName
        """
        if "componentName" in self._prop_dict:
            return self._prop_dict["componentName"]
        else:
            return None

    @component_name.setter
    def component_name(self, val):
        self._prop_dict["componentName"] = val

    @property
    def actor(self):
        """
        Gets and sets the actor
        
        Returns: 
            :class:`AuditActor<onedrivesdk.model.audit_actor.AuditActor>`:
                The actor
        """
        if "actor" in self._prop_dict:
            if isinstance(self._prop_dict["actor"], OneDriveObjectBase):
                return self._prop_dict["actor"]
            else :
                self._prop_dict["actor"] = AuditActor(self._prop_dict["actor"])
                return self._prop_dict["actor"]

        return None

    @actor.setter
    def actor(self, val):
        self._prop_dict["actor"] = val

    @property
    def activity(self):
        """
        Gets and sets the activity
        
        Returns:
            str:
                The activity
        """
        if "activity" in self._prop_dict:
            return self._prop_dict["activity"]
        else:
            return None

    @activity.setter
    def activity(self, val):
        self._prop_dict["activity"] = val

    @property
    def activity_date_time(self):
        """
        Gets and sets the activityDateTime
        
        Returns:
            datetime:
                The activityDateTime
        """
        if "activityDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["activityDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @activity_date_time.setter
    def activity_date_time(self, val):
        self._prop_dict["activityDateTime"] = val.isoformat()+"Z"

    @property
    def activity_type(self):
        """
        Gets and sets the activityType
        
        Returns:
            str:
                The activityType
        """
        if "activityType" in self._prop_dict:
            return self._prop_dict["activityType"]
        else:
            return None

    @activity_type.setter
    def activity_type(self, val):
        self._prop_dict["activityType"] = val

    @property
    def activity_operation_type(self):
        """
        Gets and sets the activityOperationType
        
        Returns:
            str:
                The activityOperationType
        """
        if "activityOperationType" in self._prop_dict:
            return self._prop_dict["activityOperationType"]
        else:
            return None

    @activity_operation_type.setter
    def activity_operation_type(self, val):
        self._prop_dict["activityOperationType"] = val

    @property
    def activity_result(self):
        """
        Gets and sets the activityResult
        
        Returns:
            str:
                The activityResult
        """
        if "activityResult" in self._prop_dict:
            return self._prop_dict["activityResult"]
        else:
            return None

    @activity_result.setter
    def activity_result(self, val):
        self._prop_dict["activityResult"] = val

    @property
    def correlation_id(self):
        """
        Gets and sets the correlationId
        
        Returns:
            UUID:
                The correlationId
        """
        if "correlationId" in self._prop_dict:
            return self._prop_dict["correlationId"]
        else:
            return None

    @correlation_id.setter
    def correlation_id(self, val):
        self._prop_dict["correlationId"] = val

    @property
    def resources(self):
        """Gets and sets the resources
        
        Returns: 
            :class:`ResourcesCollectionPage<onedrivesdk.request.resources_collection.ResourcesCollectionPage>`:
                The resources
        """
        if "resources" in self._prop_dict:
            return ResourcesCollectionPage(self._prop_dict["resources"])
        else:
            return None

    @property
    def category(self):
        """
        Gets and sets the category
        
        Returns:
            str:
                The category
        """
        if "category" in self._prop_dict:
            return self._prop_dict["category"]
        else:
            return None

    @category.setter
    def category(self, val):
        self._prop_dict["category"] = val

