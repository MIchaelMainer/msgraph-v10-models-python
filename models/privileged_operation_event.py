# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class PrivilegedOperationEvent(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def user_id(self):
        """
        Gets and sets the userId
        
        Returns:
            str:
                The userId
        """
        if "userId" in self._prop_dict:
            return self._prop_dict["userId"]
        else:
            return None

    @user_id.setter
    def user_id(self, val):
        self._prop_dict["userId"] = val

    @property
    def user_name(self):
        """
        Gets and sets the userName
        
        Returns:
            str:
                The userName
        """
        if "userName" in self._prop_dict:
            return self._prop_dict["userName"]
        else:
            return None

    @user_name.setter
    def user_name(self, val):
        self._prop_dict["userName"] = val

    @property
    def user_mail(self):
        """
        Gets and sets the userMail
        
        Returns:
            str:
                The userMail
        """
        if "userMail" in self._prop_dict:
            return self._prop_dict["userMail"]
        else:
            return None

    @user_mail.setter
    def user_mail(self, val):
        self._prop_dict["userMail"] = val

    @property
    def role_id(self):
        """
        Gets and sets the roleId
        
        Returns:
            str:
                The roleId
        """
        if "roleId" in self._prop_dict:
            return self._prop_dict["roleId"]
        else:
            return None

    @role_id.setter
    def role_id(self, val):
        self._prop_dict["roleId"] = val

    @property
    def role_name(self):
        """
        Gets and sets the roleName
        
        Returns:
            str:
                The roleName
        """
        if "roleName" in self._prop_dict:
            return self._prop_dict["roleName"]
        else:
            return None

    @role_name.setter
    def role_name(self, val):
        self._prop_dict["roleName"] = val

    @property
    def expiration_date_time(self):
        """
        Gets and sets the expirationDateTime
        
        Returns:
            datetime:
                The expirationDateTime
        """
        if "expirationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["expirationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @expiration_date_time.setter
    def expiration_date_time(self, val):
        self._prop_dict["expirationDateTime"] = val.isoformat()+"Z"

    @property
    def creation_date_time(self):
        """
        Gets and sets the creationDateTime
        
        Returns:
            datetime:
                The creationDateTime
        """
        if "creationDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["creationDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @creation_date_time.setter
    def creation_date_time(self, val):
        self._prop_dict["creationDateTime"] = val.isoformat()+"Z"

    @property
    def requestor_id(self):
        """
        Gets and sets the requestorId
        
        Returns:
            str:
                The requestorId
        """
        if "requestorId" in self._prop_dict:
            return self._prop_dict["requestorId"]
        else:
            return None

    @requestor_id.setter
    def requestor_id(self, val):
        self._prop_dict["requestorId"] = val

    @property
    def requestor_name(self):
        """
        Gets and sets the requestorName
        
        Returns:
            str:
                The requestorName
        """
        if "requestorName" in self._prop_dict:
            return self._prop_dict["requestorName"]
        else:
            return None

    @requestor_name.setter
    def requestor_name(self, val):
        self._prop_dict["requestorName"] = val

    @property
    def tenant_id(self):
        """
        Gets and sets the tenantId
        
        Returns:
            str:
                The tenantId
        """
        if "tenantId" in self._prop_dict:
            return self._prop_dict["tenantId"]
        else:
            return None

    @tenant_id.setter
    def tenant_id(self, val):
        self._prop_dict["tenantId"] = val

    @property
    def request_type(self):
        """
        Gets and sets the requestType
        
        Returns:
            str:
                The requestType
        """
        if "requestType" in self._prop_dict:
            return self._prop_dict["requestType"]
        else:
            return None

    @request_type.setter
    def request_type(self, val):
        self._prop_dict["requestType"] = val

    @property
    def additional_information(self):
        """
        Gets and sets the additionalInformation
        
        Returns:
            str:
                The additionalInformation
        """
        if "additionalInformation" in self._prop_dict:
            return self._prop_dict["additionalInformation"]
        else:
            return None

    @additional_information.setter
    def additional_information(self, val):
        self._prop_dict["additionalInformation"] = val

    @property
    def reference_key(self):
        """
        Gets and sets the referenceKey
        
        Returns:
            str:
                The referenceKey
        """
        if "referenceKey" in self._prop_dict:
            return self._prop_dict["referenceKey"]
        else:
            return None

    @reference_key.setter
    def reference_key(self, val):
        self._prop_dict["referenceKey"] = val

    @property
    def reference_system(self):
        """
        Gets and sets the referenceSystem
        
        Returns:
            str:
                The referenceSystem
        """
        if "referenceSystem" in self._prop_dict:
            return self._prop_dict["referenceSystem"]
        else:
            return None

    @reference_system.setter
    def reference_system(self, val):
        self._prop_dict["referenceSystem"] = val

