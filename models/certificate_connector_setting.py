# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class CertificateConnectorSetting(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def status(self):
        """Gets and sets the status
        
        Returns: 
            int:
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
    def cert_expiry_time(self):
        """Gets and sets the certExpiryTime
        
        Returns: 
            datetime:
                The certExpiryTime
        """
        if "certExpiryTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["certExpiryTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @cert_expiry_time.setter
    def cert_expiry_time(self, val):
        self._prop_dict["certExpiryTime"] = val.isoformat()+"Z"

    @property
    def enrollment_error(self):
        """Gets and sets the enrollmentError
        
        Returns: 
            str:
                The enrollmentError
        """
        if "enrollmentError" in self._prop_dict:
            return self._prop_dict["enrollmentError"]
        else:
            return None

    @enrollment_error.setter
    def enrollment_error(self, val):
        self._prop_dict["enrollmentError"] = val

    @property
    def last_connector_connection_time(self):
        """Gets and sets the lastConnectorConnectionTime
        
        Returns: 
            datetime:
                The lastConnectorConnectionTime
        """
        if "lastConnectorConnectionTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastConnectorConnectionTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_connector_connection_time.setter
    def last_connector_connection_time(self, val):
        self._prop_dict["lastConnectorConnectionTime"] = val.isoformat()+"Z"

    @property
    def connector_version(self):
        """Gets and sets the connectorVersion
        
        Returns: 
            str:
                The connectorVersion
        """
        if "connectorVersion" in self._prop_dict:
            return self._prop_dict["connectorVersion"]
        else:
            return None

    @connector_version.setter
    def connector_version(self, val):
        self._prop_dict["connectorVersion"] = val

    @property
    def last_upload_version(self):
        """Gets and sets the lastUploadVersion
        
        Returns: 
            int:
                The lastUploadVersion
        """
        if "lastUploadVersion" in self._prop_dict:
            return self._prop_dict["lastUploadVersion"]
        else:
            return None

    @last_upload_version.setter
    def last_upload_version(self, val):
        self._prop_dict["lastUploadVersion"] = val

