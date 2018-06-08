# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.bit_locker_encryption_method import BitLockerEncryptionMethod
from ..one_drive_object_base import OneDriveObjectBase


class BitLockerRemovableDrivePolicy(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def encryption_method(self):
        """
        Gets and sets the encryptionMethod
        
        Returns: 
            :class:`BitLockerEncryptionMethod<onedrivesdk.model.bit_locker_encryption_method.BitLockerEncryptionMethod>`:
                The encryptionMethod
        """
        if "encryptionMethod" in self._prop_dict:
            if isinstance(self._prop_dict["encryptionMethod"], OneDriveObjectBase):
                return self._prop_dict["encryptionMethod"]
            else :
                self._prop_dict["encryptionMethod"] = BitLockerEncryptionMethod(self._prop_dict["encryptionMethod"])
                return self._prop_dict["encryptionMethod"]

        return None

    @encryption_method.setter
    def encryption_method(self, val):
        self._prop_dict["encryptionMethod"] = val
    @property
    def require_encryption_for_write_access(self):
        """Gets and sets the requireEncryptionForWriteAccess
        
        Returns: 
            bool:
                The requireEncryptionForWriteAccess
        """
        if "requireEncryptionForWriteAccess" in self._prop_dict:
            return self._prop_dict["requireEncryptionForWriteAccess"]
        else:
            return None

    @require_encryption_for_write_access.setter
    def require_encryption_for_write_access(self, val):
        self._prop_dict["requireEncryptionForWriteAccess"] = val

    @property
    def block_cross_organization_write_access(self):
        """Gets and sets the blockCrossOrganizationWriteAccess
        
        Returns: 
            bool:
                The blockCrossOrganizationWriteAccess
        """
        if "blockCrossOrganizationWriteAccess" in self._prop_dict:
            return self._prop_dict["blockCrossOrganizationWriteAccess"]
        else:
            return None

    @block_cross_organization_write_access.setter
    def block_cross_organization_write_access(self, val):
        self._prop_dict["blockCrossOrganizationWriteAccess"] = val

