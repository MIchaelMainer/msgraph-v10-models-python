# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.caas_error import CaasError
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class JobResponseBase(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def type(self):
        """
        Gets and sets the type
        
        Returns:
            str:
                The type
        """
        if "type" in self._prop_dict:
            return self._prop_dict["type"]
        else:
            return None

    @type.setter
    def type(self, val):
        self._prop_dict["type"] = val

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns:
            str:
                The status
        """
        if "status" in self._prop_dict:
            return self._prop_dict["status"]
        else:
            return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

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
    def start_date_time(self):
        """
        Gets and sets the startDateTime
        
        Returns:
            datetime:
                The startDateTime
        """
        if "startDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["startDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @start_date_time.setter
    def start_date_time(self, val):
        self._prop_dict["startDateTime"] = val.isoformat()+"Z"

    @property
    def end_date_time(self):
        """
        Gets and sets the endDateTime
        
        Returns:
            datetime:
                The endDateTime
        """
        if "endDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["endDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @end_date_time.setter
    def end_date_time(self, val):
        self._prop_dict["endDateTime"] = val.isoformat()+"Z"

    @property
    def error(self):
        """
        Gets and sets the error
        
        Returns: 
            :class:`CaasError<onedrivesdk.model.caas_error.CaasError>`:
                The error
        """
        if "error" in self._prop_dict:
            if isinstance(self._prop_dict["error"], OneDriveObjectBase):
                return self._prop_dict["error"]
            else :
                self._prop_dict["error"] = CaasError(self._prop_dict["error"])
                return self._prop_dict["error"]

        return None

    @error.setter
    def error(self, val):
        self._prop_dict["error"] = val

