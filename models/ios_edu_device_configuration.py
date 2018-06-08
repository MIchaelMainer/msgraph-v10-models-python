# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.ios_edu_certificate_settings import IosEduCertificateSettings
from ..one_drive_object_base import OneDriveObjectBase


class IosEduDeviceConfiguration(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def teacher_certificate_settings(self):
        """
        Gets and sets the teacherCertificateSettings
        
        Returns: 
            :class:`IosEduCertificateSettings<onedrivesdk.model.ios_edu_certificate_settings.IosEduCertificateSettings>`:
                The teacherCertificateSettings
        """
        if "teacherCertificateSettings" in self._prop_dict:
            if isinstance(self._prop_dict["teacherCertificateSettings"], OneDriveObjectBase):
                return self._prop_dict["teacherCertificateSettings"]
            else :
                self._prop_dict["teacherCertificateSettings"] = IosEduCertificateSettings(self._prop_dict["teacherCertificateSettings"])
                return self._prop_dict["teacherCertificateSettings"]

        return None

    @teacher_certificate_settings.setter
    def teacher_certificate_settings(self, val):
        self._prop_dict["teacherCertificateSettings"] = val

    @property
    def student_certificate_settings(self):
        """
        Gets and sets the studentCertificateSettings
        
        Returns: 
            :class:`IosEduCertificateSettings<onedrivesdk.model.ios_edu_certificate_settings.IosEduCertificateSettings>`:
                The studentCertificateSettings
        """
        if "studentCertificateSettings" in self._prop_dict:
            if isinstance(self._prop_dict["studentCertificateSettings"], OneDriveObjectBase):
                return self._prop_dict["studentCertificateSettings"]
            else :
                self._prop_dict["studentCertificateSettings"] = IosEduCertificateSettings(self._prop_dict["studentCertificateSettings"])
                return self._prop_dict["studentCertificateSettings"]

        return None

    @student_certificate_settings.setter
    def student_certificate_settings(self, val):
        self._prop_dict["studentCertificateSettings"] = val

    @property
    def device_certificate_settings(self):
        """
        Gets and sets the deviceCertificateSettings
        
        Returns: 
            :class:`IosEduCertificateSettings<onedrivesdk.model.ios_edu_certificate_settings.IosEduCertificateSettings>`:
                The deviceCertificateSettings
        """
        if "deviceCertificateSettings" in self._prop_dict:
            if isinstance(self._prop_dict["deviceCertificateSettings"], OneDriveObjectBase):
                return self._prop_dict["deviceCertificateSettings"]
            else :
                self._prop_dict["deviceCertificateSettings"] = IosEduCertificateSettings(self._prop_dict["deviceCertificateSettings"])
                return self._prop_dict["deviceCertificateSettings"]

        return None

    @device_certificate_settings.setter
    def device_certificate_settings(self, val):
        self._prop_dict["deviceCertificateSettings"] = val

