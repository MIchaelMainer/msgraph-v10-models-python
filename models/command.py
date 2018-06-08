# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.payload_request import PayloadRequest
from ..model.payload_response import PayloadResponse
from ..one_drive_object_base import OneDriveObjectBase


class Command(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def status(self):
        """
        Gets and sets the Status
        
        Returns:
            str:
                The Status
        """
        if "Status" in self._prop_dict:
            return self._prop_dict["Status"]
        else:
            return None

    @status.setter
    def status(self, val):
        self._prop_dict["Status"] = val

    @property
    def type(self):
        """
        Gets and sets the Type
        
        Returns:
            str:
                The Type
        """
        if "Type" in self._prop_dict:
            return self._prop_dict["Type"]
        else:
            return None

    @type.setter
    def type(self, val):
        self._prop_dict["Type"] = val

    @property
    def app_service_name(self):
        """
        Gets and sets the AppServiceName
        
        Returns:
            str:
                The AppServiceName
        """
        if "AppServiceName" in self._prop_dict:
            return self._prop_dict["AppServiceName"]
        else:
            return None

    @app_service_name.setter
    def app_service_name(self, val):
        self._prop_dict["AppServiceName"] = val

    @property
    def package_family_name(self):
        """
        Gets and sets the PackageFamilyName
        
        Returns:
            str:
                The PackageFamilyName
        """
        if "PackageFamilyName" in self._prop_dict:
            return self._prop_dict["PackageFamilyName"]
        else:
            return None

    @package_family_name.setter
    def package_family_name(self, val):
        self._prop_dict["PackageFamilyName"] = val

    @property
    def error(self):
        """
        Gets and sets the Error
        
        Returns:
            str:
                The Error
        """
        if "Error" in self._prop_dict:
            return self._prop_dict["Error"]
        else:
            return None

    @error.setter
    def error(self, val):
        self._prop_dict["Error"] = val

    @property
    def payload(self):
        """
        Gets and sets the Payload
        
        Returns: 
            :class:`PayloadRequest<onedrivesdk.model.payload_request.PayloadRequest>`:
                The Payload
        """
        if "Payload" in self._prop_dict:
            if isinstance(self._prop_dict["Payload"], OneDriveObjectBase):
                return self._prop_dict["Payload"]
            else :
                self._prop_dict["Payload"] = PayloadRequest(self._prop_dict["Payload"])
                return self._prop_dict["Payload"]

        return None

    @payload.setter
    def payload(self, val):
        self._prop_dict["Payload"] = val

    @property
    def permission_ticket(self):
        """
        Gets and sets the PermissionTicket
        
        Returns:
            str:
                The PermissionTicket
        """
        if "PermissionTicket" in self._prop_dict:
            return self._prop_dict["PermissionTicket"]
        else:
            return None

    @permission_ticket.setter
    def permission_ticket(self, val):
        self._prop_dict["PermissionTicket"] = val

    @property
    def post_back_uri(self):
        """
        Gets and sets the PostBackUri
        
        Returns:
            str:
                The PostBackUri
        """
        if "PostBackUri" in self._prop_dict:
            return self._prop_dict["PostBackUri"]
        else:
            return None

    @post_back_uri.setter
    def post_back_uri(self, val):
        self._prop_dict["PostBackUri"] = val

    @property
    def responsepayload(self):
        """
        Gets and sets the responsepayload
        
        Returns: 
            :class:`PayloadResponse<onedrivesdk.model.payload_response.PayloadResponse>`:
                The responsepayload
        """
        if "responsepayload" in self._prop_dict:
            if isinstance(self._prop_dict["responsepayload"], OneDriveObjectBase):
                return self._prop_dict["responsepayload"]
            else :
                self._prop_dict["responsepayload"] = PayloadResponse(self._prop_dict["responsepayload"])
                return self._prop_dict["responsepayload"]

        return None

    @responsepayload.setter
    def responsepayload(self, val):
        self._prop_dict["responsepayload"] = val

