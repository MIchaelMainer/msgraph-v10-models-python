# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.certificate_status import CertificateStatus
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class EnterpriseCodeSigningCertificate(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def status(self):
        """
        Gets and sets the status
        
        Returns: 
            :class:`CertificateStatus<onedrivesdk.model.certificate_status.CertificateStatus>`:
                The status
        """
        if "status" in self._prop_dict:
            if isinstance(self._prop_dict["status"], OneDriveObjectBase):
                return self._prop_dict["status"]
            else :
                self._prop_dict["status"] = CertificateStatus(self._prop_dict["status"])
                return self._prop_dict["status"]

        return None

    @status.setter
    def status(self, val):
        self._prop_dict["status"] = val

    @property
    def subject_name(self):
        """
        Gets and sets the subjectName
        
        Returns:
            str:
                The subjectName
        """
        if "subjectName" in self._prop_dict:
            return self._prop_dict["subjectName"]
        else:
            return None

    @subject_name.setter
    def subject_name(self, val):
        self._prop_dict["subjectName"] = val

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
    def issuer_name(self):
        """
        Gets and sets the issuerName
        
        Returns:
            str:
                The issuerName
        """
        if "issuerName" in self._prop_dict:
            return self._prop_dict["issuerName"]
        else:
            return None

    @issuer_name.setter
    def issuer_name(self, val):
        self._prop_dict["issuerName"] = val

    @property
    def issuer(self):
        """
        Gets and sets the issuer
        
        Returns:
            str:
                The issuer
        """
        if "issuer" in self._prop_dict:
            return self._prop_dict["issuer"]
        else:
            return None

    @issuer.setter
    def issuer(self, val):
        self._prop_dict["issuer"] = val

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
    def upload_date_time(self):
        """
        Gets and sets the uploadDateTime
        
        Returns:
            datetime:
                The uploadDateTime
        """
        if "uploadDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["uploadDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @upload_date_time.setter
    def upload_date_time(self, val):
        self._prop_dict["uploadDateTime"] = val.isoformat()+"Z"

