# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.sensitive_content_evidence import SensitiveContentEvidence
from ..one_drive_object_base import OneDriveObjectBase


class SensitiveContentLocation(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def id_match(self):
        """Gets and sets the idMatch
        
        Returns: 
            str:
                The idMatch
        """
        if "idMatch" in self._prop_dict:
            return self._prop_dict["idMatch"]
        else:
            return None

    @id_match.setter
    def id_match(self, val):
        self._prop_dict["idMatch"] = val

    @property
    def offset(self):
        """Gets and sets the offset
        
        Returns: 
            int:
                The offset
        """
        if "offset" in self._prop_dict:
            return self._prop_dict["offset"]
        else:
            return None

    @offset.setter
    def offset(self, val):
        self._prop_dict["offset"] = val

    @property
    def length(self):
        """Gets and sets the length
        
        Returns: 
            int:
                The length
        """
        if "length" in self._prop_dict:
            return self._prop_dict["length"]
        else:
            return None

    @length.setter
    def length(self, val):
        self._prop_dict["length"] = val

    @property
    def evidences(self):
        """
        Gets and sets the evidences
        
        Returns: 
            :class:`SensitiveContentEvidence<onedrivesdk.model.sensitive_content_evidence.SensitiveContentEvidence>`:
                The evidences
        """
        if "evidences" in self._prop_dict:
            if isinstance(self._prop_dict["evidences"], OneDriveObjectBase):
                return self._prop_dict["evidences"]
            else :
                self._prop_dict["evidences"] = SensitiveContentEvidence(self._prop_dict["evidences"])
                return self._prop_dict["evidences"]

        return None

    @evidences.setter
    def evidences(self, val):
        self._prop_dict["evidences"] = val
