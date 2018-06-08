# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.domain_state import DomainState
from ..model.domain_dns_record import DomainDnsRecord
from ..model.directory_object import DirectoryObject
from ..one_drive_object_base import OneDriveObjectBase


class Domain(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def authentication_type(self):
        """
        Gets and sets the authenticationType
        
        Returns:
            str:
                The authenticationType
        """
        if "authenticationType" in self._prop_dict:
            return self._prop_dict["authenticationType"]
        else:
            return None

    @authentication_type.setter
    def authentication_type(self, val):
        self._prop_dict["authenticationType"] = val

    @property
    def availability_status(self):
        """
        Gets and sets the availabilityStatus
        
        Returns:
            str:
                The availabilityStatus
        """
        if "availabilityStatus" in self._prop_dict:
            return self._prop_dict["availabilityStatus"]
        else:
            return None

    @availability_status.setter
    def availability_status(self, val):
        self._prop_dict["availabilityStatus"] = val

    @property
    def is_admin_managed(self):
        """
        Gets and sets the isAdminManaged
        
        Returns:
            bool:
                The isAdminManaged
        """
        if "isAdminManaged" in self._prop_dict:
            return self._prop_dict["isAdminManaged"]
        else:
            return None

    @is_admin_managed.setter
    def is_admin_managed(self, val):
        self._prop_dict["isAdminManaged"] = val

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

    @property
    def is_initial(self):
        """
        Gets and sets the isInitial
        
        Returns:
            bool:
                The isInitial
        """
        if "isInitial" in self._prop_dict:
            return self._prop_dict["isInitial"]
        else:
            return None

    @is_initial.setter
    def is_initial(self, val):
        self._prop_dict["isInitial"] = val

    @property
    def is_root(self):
        """
        Gets and sets the isRoot
        
        Returns:
            bool:
                The isRoot
        """
        if "isRoot" in self._prop_dict:
            return self._prop_dict["isRoot"]
        else:
            return None

    @is_root.setter
    def is_root(self, val):
        self._prop_dict["isRoot"] = val

    @property
    def is_verified(self):
        """
        Gets and sets the isVerified
        
        Returns:
            bool:
                The isVerified
        """
        if "isVerified" in self._prop_dict:
            return self._prop_dict["isVerified"]
        else:
            return None

    @is_verified.setter
    def is_verified(self, val):
        self._prop_dict["isVerified"] = val

    @property
    def supported_services(self):
        """
        Gets and sets the supportedServices
        
        Returns:
            str:
                The supportedServices
        """
        if "supportedServices" in self._prop_dict:
            return self._prop_dict["supportedServices"]
        else:
            return None

    @supported_services.setter
    def supported_services(self, val):
        self._prop_dict["supportedServices"] = val

    @property
    def state(self):
        """
        Gets and sets the state
        
        Returns: 
            :class:`DomainState<onedrivesdk.model.domain_state.DomainState>`:
                The state
        """
        if "state" in self._prop_dict:
            if isinstance(self._prop_dict["state"], OneDriveObjectBase):
                return self._prop_dict["state"]
            else :
                self._prop_dict["state"] = DomainState(self._prop_dict["state"])
                return self._prop_dict["state"]

        return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

    @property
    def service_configuration_records(self):
        """Gets and sets the serviceConfigurationRecords
        
        Returns: 
            :class:`ServiceConfigurationRecordsCollectionPage<onedrivesdk.request.service_configuration_records_collection.ServiceConfigurationRecordsCollectionPage>`:
                The serviceConfigurationRecords
        """
        if "serviceConfigurationRecords" in self._prop_dict:
            return ServiceConfigurationRecordsCollectionPage(self._prop_dict["serviceConfigurationRecords"])
        else:
            return None

    @property
    def verification_dns_records(self):
        """Gets and sets the verificationDnsRecords
        
        Returns: 
            :class:`VerificationDnsRecordsCollectionPage<onedrivesdk.request.verification_dns_records_collection.VerificationDnsRecordsCollectionPage>`:
                The verificationDnsRecords
        """
        if "verificationDnsRecords" in self._prop_dict:
            return VerificationDnsRecordsCollectionPage(self._prop_dict["verificationDnsRecords"])
        else:
            return None

    @property
    def domain_name_references(self):
        """Gets and sets the domainNameReferences
        
        Returns: 
            :class:`DomainNameReferencesCollectionPage<onedrivesdk.request.domain_name_references_collection.DomainNameReferencesCollectionPage>`:
                The domainNameReferences
        """
        if "domainNameReferences" in self._prop_dict:
            return DomainNameReferencesCollectionPage(self._prop_dict["domainNameReferences"])
        else:
            return None

