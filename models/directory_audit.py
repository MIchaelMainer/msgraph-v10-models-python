# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.operation_result import OperationResult
from ..model.audit_activity_initiator import AuditActivityInitiator
from ..model.target_resource import TargetResource
from ..model.key_value import KeyValue
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class DirectoryAudit(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

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
    def result(self):
        """
        Gets and sets the result
        
        Returns: 
            :class:`OperationResult<onedrivesdk.model.operation_result.OperationResult>`:
                The result
        """
        if "result" in self._prop_dict:
            if isinstance(self._prop_dict["result"], OneDriveObjectBase):
                return self._prop_dict["result"]
            else :
                self._prop_dict["result"] = OperationResult(self._prop_dict["result"])
                return self._prop_dict["result"]

        return None

    @result.setter
    def result(self, val):
        self._prop_dict["result"] = val

    @property
    def result_reason(self):
        """
        Gets and sets the resultReason
        
        Returns:
            str:
                The resultReason
        """
        if "resultReason" in self._prop_dict:
            return self._prop_dict["resultReason"]
        else:
            return None

    @result_reason.setter
    def result_reason(self, val):
        self._prop_dict["resultReason"] = val

    @property
    def activity_display_name(self):
        """
        Gets and sets the activityDisplayName
        
        Returns:
            str:
                The activityDisplayName
        """
        if "activityDisplayName" in self._prop_dict:
            return self._prop_dict["activityDisplayName"]
        else:
            return None

    @activity_display_name.setter
    def activity_display_name(self, val):
        self._prop_dict["activityDisplayName"] = val

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
    def initiated_by(self):
        """
        Gets and sets the initiatedBy
        
        Returns: 
            :class:`AuditActivityInitiator<onedrivesdk.model.audit_activity_initiator.AuditActivityInitiator>`:
                The initiatedBy
        """
        if "initiatedBy" in self._prop_dict:
            if isinstance(self._prop_dict["initiatedBy"], OneDriveObjectBase):
                return self._prop_dict["initiatedBy"]
            else :
                self._prop_dict["initiatedBy"] = AuditActivityInitiator(self._prop_dict["initiatedBy"])
                return self._prop_dict["initiatedBy"]

        return None

    @initiated_by.setter
    def initiated_by(self, val):
        self._prop_dict["initiatedBy"] = val

    @property
    def target_resources(self):
        """Gets and sets the targetResources
        
        Returns: 
            :class:`TargetResourcesCollectionPage<onedrivesdk.request.target_resources_collection.TargetResourcesCollectionPage>`:
                The targetResources
        """
        if "targetResources" in self._prop_dict:
            return TargetResourcesCollectionPage(self._prop_dict["targetResources"])
        else:
            return None

    @property
    def logged_by_service(self):
        """
        Gets and sets the loggedByService
        
        Returns:
            str:
                The loggedByService
        """
        if "loggedByService" in self._prop_dict:
            return self._prop_dict["loggedByService"]
        else:
            return None

    @logged_by_service.setter
    def logged_by_service(self, val):
        self._prop_dict["loggedByService"] = val

    @property
    def additional_details(self):
        """Gets and sets the additionalDetails
        
        Returns: 
            :class:`AdditionalDetailsCollectionPage<onedrivesdk.request.additional_details_collection.AdditionalDetailsCollectionPage>`:
                The additionalDetails
        """
        if "additionalDetails" in self._prop_dict:
            return AdditionalDetailsCollectionPage(self._prop_dict["additionalDetails"])
        else:
            return None

