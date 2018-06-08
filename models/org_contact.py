# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.on_premises_provisioning_error import OnPremisesProvisioningError
from ..model.directory_object import DirectoryObject
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class OrgContact(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def business_phones(self):
        """
        Gets and sets the businessPhones
        
        Returns:
            str:
                The businessPhones
        """
        if "businessPhones" in self._prop_dict:
            return self._prop_dict["businessPhones"]
        else:
            return None

    @business_phones.setter
    def business_phones(self, val):
        self._prop_dict["businessPhones"] = val

    @property
    def city(self):
        """
        Gets and sets the city
        
        Returns:
            str:
                The city
        """
        if "city" in self._prop_dict:
            return self._prop_dict["city"]
        else:
            return None

    @city.setter
    def city(self, val):
        self._prop_dict["city"] = val

    @property
    def company_name(self):
        """
        Gets and sets the companyName
        
        Returns:
            str:
                The companyName
        """
        if "companyName" in self._prop_dict:
            return self._prop_dict["companyName"]
        else:
            return None

    @company_name.setter
    def company_name(self, val):
        self._prop_dict["companyName"] = val

    @property
    def country(self):
        """
        Gets and sets the country
        
        Returns:
            str:
                The country
        """
        if "country" in self._prop_dict:
            return self._prop_dict["country"]
        else:
            return None

    @country.setter
    def country(self, val):
        self._prop_dict["country"] = val

    @property
    def department(self):
        """
        Gets and sets the department
        
        Returns:
            str:
                The department
        """
        if "department" in self._prop_dict:
            return self._prop_dict["department"]
        else:
            return None

    @department.setter
    def department(self, val):
        self._prop_dict["department"] = val

    @property
    def display_name(self):
        """
        Gets and sets the displayName
        
        Returns:
            str:
                The displayName
        """
        if "displayName" in self._prop_dict:
            return self._prop_dict["displayName"]
        else:
            return None

    @display_name.setter
    def display_name(self, val):
        self._prop_dict["displayName"] = val

    @property
    def given_name(self):
        """
        Gets and sets the givenName
        
        Returns:
            str:
                The givenName
        """
        if "givenName" in self._prop_dict:
            return self._prop_dict["givenName"]
        else:
            return None

    @given_name.setter
    def given_name(self, val):
        self._prop_dict["givenName"] = val

    @property
    def job_title(self):
        """
        Gets and sets the jobTitle
        
        Returns:
            str:
                The jobTitle
        """
        if "jobTitle" in self._prop_dict:
            return self._prop_dict["jobTitle"]
        else:
            return None

    @job_title.setter
    def job_title(self, val):
        self._prop_dict["jobTitle"] = val

    @property
    def mail(self):
        """
        Gets and sets the mail
        
        Returns:
            str:
                The mail
        """
        if "mail" in self._prop_dict:
            return self._prop_dict["mail"]
        else:
            return None

    @mail.setter
    def mail(self, val):
        self._prop_dict["mail"] = val

    @property
    def mail_nickname(self):
        """
        Gets and sets the mailNickname
        
        Returns:
            str:
                The mailNickname
        """
        if "mailNickname" in self._prop_dict:
            return self._prop_dict["mailNickname"]
        else:
            return None

    @mail_nickname.setter
    def mail_nickname(self, val):
        self._prop_dict["mailNickname"] = val

    @property
    def mobile_phone(self):
        """
        Gets and sets the mobilePhone
        
        Returns:
            str:
                The mobilePhone
        """
        if "mobilePhone" in self._prop_dict:
            return self._prop_dict["mobilePhone"]
        else:
            return None

    @mobile_phone.setter
    def mobile_phone(self, val):
        self._prop_dict["mobilePhone"] = val

    @property
    def on_premises_sync_enabled(self):
        """
        Gets and sets the onPremisesSyncEnabled
        
        Returns:
            bool:
                The onPremisesSyncEnabled
        """
        if "onPremisesSyncEnabled" in self._prop_dict:
            return self._prop_dict["onPremisesSyncEnabled"]
        else:
            return None

    @on_premises_sync_enabled.setter
    def on_premises_sync_enabled(self, val):
        self._prop_dict["onPremisesSyncEnabled"] = val

    @property
    def on_premises_last_sync_date_time(self):
        """
        Gets and sets the onPremisesLastSyncDateTime
        
        Returns:
            datetime:
                The onPremisesLastSyncDateTime
        """
        if "onPremisesLastSyncDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["onPremisesLastSyncDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @on_premises_last_sync_date_time.setter
    def on_premises_last_sync_date_time(self, val):
        self._prop_dict["onPremisesLastSyncDateTime"] = val.isoformat()+"Z"

    @property
    def on_premises_provisioning_errors(self):
        """Gets and sets the onPremisesProvisioningErrors
        
        Returns: 
            :class:`OnPremisesProvisioningErrorsCollectionPage<onedrivesdk.request.on_premises_provisioning_errors_collection.OnPremisesProvisioningErrorsCollectionPage>`:
                The onPremisesProvisioningErrors
        """
        if "onPremisesProvisioningErrors" in self._prop_dict:
            return OnPremisesProvisioningErrorsCollectionPage(self._prop_dict["onPremisesProvisioningErrors"])
        else:
            return None

    @property
    def office_location(self):
        """
        Gets and sets the officeLocation
        
        Returns:
            str:
                The officeLocation
        """
        if "officeLocation" in self._prop_dict:
            return self._prop_dict["officeLocation"]
        else:
            return None

    @office_location.setter
    def office_location(self, val):
        self._prop_dict["officeLocation"] = val

    @property
    def postal_code(self):
        """
        Gets and sets the postalCode
        
        Returns:
            str:
                The postalCode
        """
        if "postalCode" in self._prop_dict:
            return self._prop_dict["postalCode"]
        else:
            return None

    @postal_code.setter
    def postal_code(self, val):
        self._prop_dict["postalCode"] = val

    @property
    def proxy_addresses(self):
        """
        Gets and sets the proxyAddresses
        
        Returns:
            str:
                The proxyAddresses
        """
        if "proxyAddresses" in self._prop_dict:
            return self._prop_dict["proxyAddresses"]
        else:
            return None

    @proxy_addresses.setter
    def proxy_addresses(self, val):
        self._prop_dict["proxyAddresses"] = val

    @property
    def state(self):
        """
        Gets and sets the state
        
        Returns:
            str:
                The state
        """
        if "state" in self._prop_dict:
            return self._prop_dict["state"]
        else:
            return None

    @state.setter
    def state(self, val):
        self._prop_dict["state"] = val

    @property
    def street_address(self):
        """
        Gets and sets the streetAddress
        
        Returns:
            str:
                The streetAddress
        """
        if "streetAddress" in self._prop_dict:
            return self._prop_dict["streetAddress"]
        else:
            return None

    @street_address.setter
    def street_address(self, val):
        self._prop_dict["streetAddress"] = val

    @property
    def surname(self):
        """
        Gets and sets the surname
        
        Returns:
            str:
                The surname
        """
        if "surname" in self._prop_dict:
            return self._prop_dict["surname"]
        else:
            return None

    @surname.setter
    def surname(self, val):
        self._prop_dict["surname"] = val

    @property
    def manager(self):
        """
        Gets and sets the manager
        
        Returns: 
            :class:`DirectoryObject<onedrivesdk.model.directory_object.DirectoryObject>`:
                The manager
        """
        if "manager" in self._prop_dict:
            if isinstance(self._prop_dict["manager"], OneDriveObjectBase):
                return self._prop_dict["manager"]
            else :
                self._prop_dict["manager"] = DirectoryObject(self._prop_dict["manager"])
                return self._prop_dict["manager"]

        return None

    @manager.setter
    def manager(self, val):
        self._prop_dict["manager"] = val

    @property
    def direct_reports(self):
        """Gets and sets the directReports
        
        Returns: 
            :class:`DirectReportsCollectionPage<onedrivesdk.request.direct_reports_collection.DirectReportsCollectionPage>`:
                The directReports
        """
        if "directReports" in self._prop_dict:
            return DirectReportsCollectionPage(self._prop_dict["directReports"])
        else:
            return None

    @property
    def member_of(self):
        """Gets and sets the memberOf
        
        Returns: 
            :class:`MemberOfCollectionPage<onedrivesdk.request.member_of_collection.MemberOfCollectionPage>`:
                The memberOf
        """
        if "memberOf" in self._prop_dict:
            return MemberOfCollectionPage(self._prop_dict["memberOf"])
        else:
            return None

