# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.agreement_file_data import AgreementFileData
from ..one_drive_object_base import OneDriveObjectBase


class AgreementFile(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def language(self):
        """
        Gets and sets the language
        
        Returns:
            str:
                The language
        """
        if "language" in self._prop_dict:
            return self._prop_dict["language"]
        else:
            return None

    @language.setter
    def language(self, val):
        self._prop_dict["language"] = val

    @property
    def file_name(self):
        """
        Gets and sets the fileName
        
        Returns:
            str:
                The fileName
        """
        if "fileName" in self._prop_dict:
            return self._prop_dict["fileName"]
        else:
            return None

    @file_name.setter
    def file_name(self, val):
        self._prop_dict["fileName"] = val

    @property
    def file_data(self):
        """
        Gets and sets the fileData
        
        Returns: 
            :class:`AgreementFileData<onedrivesdk.model.agreement_file_data.AgreementFileData>`:
                The fileData
        """
        if "fileData" in self._prop_dict:
            if isinstance(self._prop_dict["fileData"], OneDriveObjectBase):
                return self._prop_dict["fileData"]
            else :
                self._prop_dict["fileData"] = AgreementFileData(self._prop_dict["fileData"])
                return self._prop_dict["fileData"]

        return None

    @file_data.setter
    def file_data(self, val):
        self._prop_dict["fileData"] = val

    @property
    def is_default(self):
        """
        Gets and sets the isDefault
        
        Returns:
            bool:
                The isDefault
        """
        if "isDefault" in self._prop_dict:
            return self._prop_dict["isDefault"]
        else:
            return None

    @is_default.setter
    def is_default(self, val):
        self._prop_dict["isDefault"] = val

