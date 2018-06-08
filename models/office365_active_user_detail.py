# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.date import Date
from ..one_drive_object_base import OneDriveObjectBase


class Office365ActiveUserDetail(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def report_refresh_date(self):
        """
        Gets and sets the reportRefreshDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The reportRefreshDate
        """
        if "reportRefreshDate" in self._prop_dict:
            if isinstance(self._prop_dict["reportRefreshDate"], OneDriveObjectBase):
                return self._prop_dict["reportRefreshDate"]
            else :
                self._prop_dict["reportRefreshDate"] = Date(self._prop_dict["reportRefreshDate"])
                return self._prop_dict["reportRefreshDate"]

        return None

    @report_refresh_date.setter
    def report_refresh_date(self, val):
        self._prop_dict["reportRefreshDate"] = val

    @property
    def user_principal_name(self):
        """
        Gets and sets the userPrincipalName
        
        Returns:
            str:
                The userPrincipalName
        """
        if "userPrincipalName" in self._prop_dict:
            return self._prop_dict["userPrincipalName"]
        else:
            return None

    @user_principal_name.setter
    def user_principal_name(self, val):
        self._prop_dict["userPrincipalName"] = val

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
    def is_deleted(self):
        """
        Gets and sets the isDeleted
        
        Returns:
            bool:
                The isDeleted
        """
        if "isDeleted" in self._prop_dict:
            return self._prop_dict["isDeleted"]
        else:
            return None

    @is_deleted.setter
    def is_deleted(self, val):
        self._prop_dict["isDeleted"] = val

    @property
    def deleted_date(self):
        """
        Gets and sets the deletedDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The deletedDate
        """
        if "deletedDate" in self._prop_dict:
            if isinstance(self._prop_dict["deletedDate"], OneDriveObjectBase):
                return self._prop_dict["deletedDate"]
            else :
                self._prop_dict["deletedDate"] = Date(self._prop_dict["deletedDate"])
                return self._prop_dict["deletedDate"]

        return None

    @deleted_date.setter
    def deleted_date(self, val):
        self._prop_dict["deletedDate"] = val

    @property
    def has_exchange_license(self):
        """
        Gets and sets the hasExchangeLicense
        
        Returns:
            bool:
                The hasExchangeLicense
        """
        if "hasExchangeLicense" in self._prop_dict:
            return self._prop_dict["hasExchangeLicense"]
        else:
            return None

    @has_exchange_license.setter
    def has_exchange_license(self, val):
        self._prop_dict["hasExchangeLicense"] = val

    @property
    def has_one_drive_license(self):
        """
        Gets and sets the hasOneDriveLicense
        
        Returns:
            bool:
                The hasOneDriveLicense
        """
        if "hasOneDriveLicense" in self._prop_dict:
            return self._prop_dict["hasOneDriveLicense"]
        else:
            return None

    @has_one_drive_license.setter
    def has_one_drive_license(self, val):
        self._prop_dict["hasOneDriveLicense"] = val

    @property
    def has_share_point_license(self):
        """
        Gets and sets the hasSharePointLicense
        
        Returns:
            bool:
                The hasSharePointLicense
        """
        if "hasSharePointLicense" in self._prop_dict:
            return self._prop_dict["hasSharePointLicense"]
        else:
            return None

    @has_share_point_license.setter
    def has_share_point_license(self, val):
        self._prop_dict["hasSharePointLicense"] = val

    @property
    def has_skype_for_business_license(self):
        """
        Gets and sets the hasSkypeForBusinessLicense
        
        Returns:
            bool:
                The hasSkypeForBusinessLicense
        """
        if "hasSkypeForBusinessLicense" in self._prop_dict:
            return self._prop_dict["hasSkypeForBusinessLicense"]
        else:
            return None

    @has_skype_for_business_license.setter
    def has_skype_for_business_license(self, val):
        self._prop_dict["hasSkypeForBusinessLicense"] = val

    @property
    def has_yammer_license(self):
        """
        Gets and sets the hasYammerLicense
        
        Returns:
            bool:
                The hasYammerLicense
        """
        if "hasYammerLicense" in self._prop_dict:
            return self._prop_dict["hasYammerLicense"]
        else:
            return None

    @has_yammer_license.setter
    def has_yammer_license(self, val):
        self._prop_dict["hasYammerLicense"] = val

    @property
    def has_teams_license(self):
        """
        Gets and sets the hasTeamsLicense
        
        Returns:
            bool:
                The hasTeamsLicense
        """
        if "hasTeamsLicense" in self._prop_dict:
            return self._prop_dict["hasTeamsLicense"]
        else:
            return None

    @has_teams_license.setter
    def has_teams_license(self, val):
        self._prop_dict["hasTeamsLicense"] = val

    @property
    def exchange_last_activity_date(self):
        """
        Gets and sets the exchangeLastActivityDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The exchangeLastActivityDate
        """
        if "exchangeLastActivityDate" in self._prop_dict:
            if isinstance(self._prop_dict["exchangeLastActivityDate"], OneDriveObjectBase):
                return self._prop_dict["exchangeLastActivityDate"]
            else :
                self._prop_dict["exchangeLastActivityDate"] = Date(self._prop_dict["exchangeLastActivityDate"])
                return self._prop_dict["exchangeLastActivityDate"]

        return None

    @exchange_last_activity_date.setter
    def exchange_last_activity_date(self, val):
        self._prop_dict["exchangeLastActivityDate"] = val

    @property
    def one_drive_last_activity_date(self):
        """
        Gets and sets the oneDriveLastActivityDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The oneDriveLastActivityDate
        """
        if "oneDriveLastActivityDate" in self._prop_dict:
            if isinstance(self._prop_dict["oneDriveLastActivityDate"], OneDriveObjectBase):
                return self._prop_dict["oneDriveLastActivityDate"]
            else :
                self._prop_dict["oneDriveLastActivityDate"] = Date(self._prop_dict["oneDriveLastActivityDate"])
                return self._prop_dict["oneDriveLastActivityDate"]

        return None

    @one_drive_last_activity_date.setter
    def one_drive_last_activity_date(self, val):
        self._prop_dict["oneDriveLastActivityDate"] = val

    @property
    def share_point_last_activity_date(self):
        """
        Gets and sets the sharePointLastActivityDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The sharePointLastActivityDate
        """
        if "sharePointLastActivityDate" in self._prop_dict:
            if isinstance(self._prop_dict["sharePointLastActivityDate"], OneDriveObjectBase):
                return self._prop_dict["sharePointLastActivityDate"]
            else :
                self._prop_dict["sharePointLastActivityDate"] = Date(self._prop_dict["sharePointLastActivityDate"])
                return self._prop_dict["sharePointLastActivityDate"]

        return None

    @share_point_last_activity_date.setter
    def share_point_last_activity_date(self, val):
        self._prop_dict["sharePointLastActivityDate"] = val

    @property
    def skype_for_business_last_activity_date(self):
        """
        Gets and sets the skypeForBusinessLastActivityDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The skypeForBusinessLastActivityDate
        """
        if "skypeForBusinessLastActivityDate" in self._prop_dict:
            if isinstance(self._prop_dict["skypeForBusinessLastActivityDate"], OneDriveObjectBase):
                return self._prop_dict["skypeForBusinessLastActivityDate"]
            else :
                self._prop_dict["skypeForBusinessLastActivityDate"] = Date(self._prop_dict["skypeForBusinessLastActivityDate"])
                return self._prop_dict["skypeForBusinessLastActivityDate"]

        return None

    @skype_for_business_last_activity_date.setter
    def skype_for_business_last_activity_date(self, val):
        self._prop_dict["skypeForBusinessLastActivityDate"] = val

    @property
    def yammer_last_activity_date(self):
        """
        Gets and sets the yammerLastActivityDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The yammerLastActivityDate
        """
        if "yammerLastActivityDate" in self._prop_dict:
            if isinstance(self._prop_dict["yammerLastActivityDate"], OneDriveObjectBase):
                return self._prop_dict["yammerLastActivityDate"]
            else :
                self._prop_dict["yammerLastActivityDate"] = Date(self._prop_dict["yammerLastActivityDate"])
                return self._prop_dict["yammerLastActivityDate"]

        return None

    @yammer_last_activity_date.setter
    def yammer_last_activity_date(self, val):
        self._prop_dict["yammerLastActivityDate"] = val

    @property
    def teams_last_activity_date(self):
        """
        Gets and sets the teamsLastActivityDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The teamsLastActivityDate
        """
        if "teamsLastActivityDate" in self._prop_dict:
            if isinstance(self._prop_dict["teamsLastActivityDate"], OneDriveObjectBase):
                return self._prop_dict["teamsLastActivityDate"]
            else :
                self._prop_dict["teamsLastActivityDate"] = Date(self._prop_dict["teamsLastActivityDate"])
                return self._prop_dict["teamsLastActivityDate"]

        return None

    @teams_last_activity_date.setter
    def teams_last_activity_date(self, val):
        self._prop_dict["teamsLastActivityDate"] = val

    @property
    def exchange_license_assign_date(self):
        """
        Gets and sets the exchangeLicenseAssignDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The exchangeLicenseAssignDate
        """
        if "exchangeLicenseAssignDate" in self._prop_dict:
            if isinstance(self._prop_dict["exchangeLicenseAssignDate"], OneDriveObjectBase):
                return self._prop_dict["exchangeLicenseAssignDate"]
            else :
                self._prop_dict["exchangeLicenseAssignDate"] = Date(self._prop_dict["exchangeLicenseAssignDate"])
                return self._prop_dict["exchangeLicenseAssignDate"]

        return None

    @exchange_license_assign_date.setter
    def exchange_license_assign_date(self, val):
        self._prop_dict["exchangeLicenseAssignDate"] = val

    @property
    def one_drive_license_assign_date(self):
        """
        Gets and sets the oneDriveLicenseAssignDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The oneDriveLicenseAssignDate
        """
        if "oneDriveLicenseAssignDate" in self._prop_dict:
            if isinstance(self._prop_dict["oneDriveLicenseAssignDate"], OneDriveObjectBase):
                return self._prop_dict["oneDriveLicenseAssignDate"]
            else :
                self._prop_dict["oneDriveLicenseAssignDate"] = Date(self._prop_dict["oneDriveLicenseAssignDate"])
                return self._prop_dict["oneDriveLicenseAssignDate"]

        return None

    @one_drive_license_assign_date.setter
    def one_drive_license_assign_date(self, val):
        self._prop_dict["oneDriveLicenseAssignDate"] = val

    @property
    def share_point_license_assign_date(self):
        """
        Gets and sets the sharePointLicenseAssignDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The sharePointLicenseAssignDate
        """
        if "sharePointLicenseAssignDate" in self._prop_dict:
            if isinstance(self._prop_dict["sharePointLicenseAssignDate"], OneDriveObjectBase):
                return self._prop_dict["sharePointLicenseAssignDate"]
            else :
                self._prop_dict["sharePointLicenseAssignDate"] = Date(self._prop_dict["sharePointLicenseAssignDate"])
                return self._prop_dict["sharePointLicenseAssignDate"]

        return None

    @share_point_license_assign_date.setter
    def share_point_license_assign_date(self, val):
        self._prop_dict["sharePointLicenseAssignDate"] = val

    @property
    def skype_for_business_license_assign_date(self):
        """
        Gets and sets the skypeForBusinessLicenseAssignDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The skypeForBusinessLicenseAssignDate
        """
        if "skypeForBusinessLicenseAssignDate" in self._prop_dict:
            if isinstance(self._prop_dict["skypeForBusinessLicenseAssignDate"], OneDriveObjectBase):
                return self._prop_dict["skypeForBusinessLicenseAssignDate"]
            else :
                self._prop_dict["skypeForBusinessLicenseAssignDate"] = Date(self._prop_dict["skypeForBusinessLicenseAssignDate"])
                return self._prop_dict["skypeForBusinessLicenseAssignDate"]

        return None

    @skype_for_business_license_assign_date.setter
    def skype_for_business_license_assign_date(self, val):
        self._prop_dict["skypeForBusinessLicenseAssignDate"] = val

    @property
    def yammer_license_assign_date(self):
        """
        Gets and sets the yammerLicenseAssignDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The yammerLicenseAssignDate
        """
        if "yammerLicenseAssignDate" in self._prop_dict:
            if isinstance(self._prop_dict["yammerLicenseAssignDate"], OneDriveObjectBase):
                return self._prop_dict["yammerLicenseAssignDate"]
            else :
                self._prop_dict["yammerLicenseAssignDate"] = Date(self._prop_dict["yammerLicenseAssignDate"])
                return self._prop_dict["yammerLicenseAssignDate"]

        return None

    @yammer_license_assign_date.setter
    def yammer_license_assign_date(self, val):
        self._prop_dict["yammerLicenseAssignDate"] = val

    @property
    def teams_license_assign_date(self):
        """
        Gets and sets the teamsLicenseAssignDate
        
        Returns: 
            :class:`Date<onedrivesdk.model.date.Date>`:
                The teamsLicenseAssignDate
        """
        if "teamsLicenseAssignDate" in self._prop_dict:
            if isinstance(self._prop_dict["teamsLicenseAssignDate"], OneDriveObjectBase):
                return self._prop_dict["teamsLicenseAssignDate"]
            else :
                self._prop_dict["teamsLicenseAssignDate"] = Date(self._prop_dict["teamsLicenseAssignDate"])
                return self._prop_dict["teamsLicenseAssignDate"]

        return None

    @teams_license_assign_date.setter
    def teams_license_assign_date(self, val):
        self._prop_dict["teamsLicenseAssignDate"] = val

    @property
    def assigned_products(self):
        """
        Gets and sets the assignedProducts
        
        Returns:
            str:
                The assignedProducts
        """
        if "assignedProducts" in self._prop_dict:
            return self._prop_dict["assignedProducts"]
        else:
            return None

    @assigned_products.setter
    def assigned_products(self, val):
        self._prop_dict["assignedProducts"] = val

