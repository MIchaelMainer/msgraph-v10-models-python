# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..one_drive_object_base import OneDriveObjectBase


class AndroidPkcsCertificateProfile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def certification_authority(self):
        """
        Gets and sets the certificationAuthority
        
        Returns:
            str:
                The certificationAuthority
        """
        if "certificationAuthority" in self._prop_dict:
            return self._prop_dict["certificationAuthority"]
        else:
            return None

    @certification_authority.setter
    def certification_authority(self, val):
        self._prop_dict["certificationAuthority"] = val

    @property
    def certification_authority_name(self):
        """
        Gets and sets the certificationAuthorityName
        
        Returns:
            str:
                The certificationAuthorityName
        """
        if "certificationAuthorityName" in self._prop_dict:
            return self._prop_dict["certificationAuthorityName"]
        else:
            return None

    @certification_authority_name.setter
    def certification_authority_name(self, val):
        self._prop_dict["certificationAuthorityName"] = val

    @property
    def certificate_template_name(self):
        """
        Gets and sets the certificateTemplateName
        
        Returns:
            str:
                The certificateTemplateName
        """
        if "certificateTemplateName" in self._prop_dict:
            return self._prop_dict["certificateTemplateName"]
        else:
            return None

    @certificate_template_name.setter
    def certificate_template_name(self, val):
        self._prop_dict["certificateTemplateName"] = val

    @property
    def subject_alternative_name_format_string(self):
        """
        Gets and sets the subjectAlternativeNameFormatString
        
        Returns:
            str:
                The subjectAlternativeNameFormatString
        """
        if "subjectAlternativeNameFormatString" in self._prop_dict:
            return self._prop_dict["subjectAlternativeNameFormatString"]
        else:
            return None

    @subject_alternative_name_format_string.setter
    def subject_alternative_name_format_string(self, val):
        self._prop_dict["subjectAlternativeNameFormatString"] = val

