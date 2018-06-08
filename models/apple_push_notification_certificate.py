# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class ApplePushNotificationCertificate(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def apple_identifier(self):
        """
        Gets and sets the appleIdentifier
        
        Returns:
            str:
                The appleIdentifier
        """
        if "appleIdentifier" in self._prop_dict:
            return self._prop_dict["appleIdentifier"]
        else:
            return None

    @apple_identifier.setter
    def apple_identifier(self, val):
        self._prop_dict["appleIdentifier"] = val

    @property
    def topic_identifier(self):
        """
        Gets and sets the topicIdentifier
        
        Returns:
            str:
                The topicIdentifier
        """
        if "topicIdentifier" in self._prop_dict:
            return self._prop_dict["topicIdentifier"]
        else:
            return None

    @topic_identifier.setter
    def topic_identifier(self, val):
        self._prop_dict["topicIdentifier"] = val

    @property
    def last_modified_date_time(self):
        """
        Gets and sets the lastModifiedDateTime
        
        Returns:
            datetime:
                The lastModifiedDateTime
        """
        if "lastModifiedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["lastModifiedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @last_modified_date_time.setter
    def last_modified_date_time(self, val):
        self._prop_dict["lastModifiedDateTime"] = val.isoformat()+"Z"

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
    def certificate_upload_status(self):
        """
        Gets and sets the certificateUploadStatus
        
        Returns:
            str:
                The certificateUploadStatus
        """
        if "certificateUploadStatus" in self._prop_dict:
            return self._prop_dict["certificateUploadStatus"]
        else:
            return None

    @certificate_upload_status.setter
    def certificate_upload_status(self, val):
        self._prop_dict["certificateUploadStatus"] = val

    @property
    def certificate_upload_failure_reason(self):
        """
        Gets and sets the certificateUploadFailureReason
        
        Returns:
            str:
                The certificateUploadFailureReason
        """
        if "certificateUploadFailureReason" in self._prop_dict:
            return self._prop_dict["certificateUploadFailureReason"]
        else:
            return None

    @certificate_upload_failure_reason.setter
    def certificate_upload_failure_reason(self, val):
        self._prop_dict["certificateUploadFailureReason"] = val

    @property
    def certificate(self):
        """
        Gets and sets the certificate
        
        Returns:
            str:
                The certificate
        """
        if "certificate" in self._prop_dict:
            return self._prop_dict["certificate"]
        else:
            return None

    @certificate.setter
    def certificate(self, val):
        self._prop_dict["certificate"] = val

