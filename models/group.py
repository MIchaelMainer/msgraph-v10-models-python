# -*- coding: utf-8 -*- 
'''
# Copyright (c) Microsoft Corporation.  All Rights Reserved.  Licensed under the MIT License.  See License in the project root for license information.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..model.on_premises_provisioning_error import OnPremisesProvisioningError
from ..model.group_access_type import GroupAccessType
from ..model.extension import Extension
from ..model.directory_object import DirectoryObject
from ..model.directory_setting import DirectorySetting
from ..model.endpoint import Endpoint
from ..model.conversation_thread import ConversationThread
from ..model.calendar import Calendar
from ..model.event import Event
from ..model.conversation import Conversation
from ..model.profile_photo import ProfilePhoto
from ..model.drive import Drive
from ..model.site import Site
from ..model.planner_group import PlannerGroup
from ..model.onenote import Onenote
from ..model.team import Team
from ..model.channel import Channel
from ..model.group_lifecycle_policy import GroupLifecyclePolicy
from datetime import datetime
from ..one_drive_object_base import OneDriveObjectBase


class Group(OneDriveObjectBase):

    def __init__(self, prop_dict={}):
        self._prop_dict = prop_dict

    @property
    def classification(self):
        """
        Gets and sets the classification
        
        Returns:
            str:
                The classification
        """
        if "classification" in self._prop_dict:
            return self._prop_dict["classification"]
        else:
            return None

    @classification.setter
    def classification(self, val):
        self._prop_dict["classification"] = val

    @property
    def created_date_time(self):
        """
        Gets and sets the createdDateTime
        
        Returns:
            datetime:
                The createdDateTime
        """
        if "createdDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["createdDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @created_date_time.setter
    def created_date_time(self, val):
        self._prop_dict["createdDateTime"] = val.isoformat()+"Z"

    @property
    def description(self):
        """
        Gets and sets the description
        
        Returns:
            str:
                The description
        """
        if "description" in self._prop_dict:
            return self._prop_dict["description"]
        else:
            return None

    @description.setter
    def description(self, val):
        self._prop_dict["description"] = val

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
    def group_types(self):
        """
        Gets and sets the groupTypes
        
        Returns:
            str:
                The groupTypes
        """
        if "groupTypes" in self._prop_dict:
            return self._prop_dict["groupTypes"]
        else:
            return None

    @group_types.setter
    def group_types(self, val):
        self._prop_dict["groupTypes"] = val

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
    def mail_enabled(self):
        """
        Gets and sets the mailEnabled
        
        Returns:
            bool:
                The mailEnabled
        """
        if "mailEnabled" in self._prop_dict:
            return self._prop_dict["mailEnabled"]
        else:
            return None

    @mail_enabled.setter
    def mail_enabled(self, val):
        self._prop_dict["mailEnabled"] = val

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
    def membership_rule(self):
        """
        Gets and sets the membershipRule
        
        Returns:
            str:
                The membershipRule
        """
        if "membershipRule" in self._prop_dict:
            return self._prop_dict["membershipRule"]
        else:
            return None

    @membership_rule.setter
    def membership_rule(self, val):
        self._prop_dict["membershipRule"] = val

    @property
    def membership_rule_processing_state(self):
        """
        Gets and sets the membershipRuleProcessingState
        
        Returns:
            str:
                The membershipRuleProcessingState
        """
        if "membershipRuleProcessingState" in self._prop_dict:
            return self._prop_dict["membershipRuleProcessingState"]
        else:
            return None

    @membership_rule_processing_state.setter
    def membership_rule_processing_state(self, val):
        self._prop_dict["membershipRuleProcessingState"] = val

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
    def on_premises_security_identifier(self):
        """
        Gets and sets the onPremisesSecurityIdentifier
        
        Returns:
            str:
                The onPremisesSecurityIdentifier
        """
        if "onPremisesSecurityIdentifier" in self._prop_dict:
            return self._prop_dict["onPremisesSecurityIdentifier"]
        else:
            return None

    @on_premises_security_identifier.setter
    def on_premises_security_identifier(self, val):
        self._prop_dict["onPremisesSecurityIdentifier"] = val

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
    def preferred_language(self):
        """
        Gets and sets the preferredLanguage
        
        Returns:
            str:
                The preferredLanguage
        """
        if "preferredLanguage" in self._prop_dict:
            return self._prop_dict["preferredLanguage"]
        else:
            return None

    @preferred_language.setter
    def preferred_language(self, val):
        self._prop_dict["preferredLanguage"] = val

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
    def renewed_date_time(self):
        """
        Gets and sets the renewedDateTime
        
        Returns:
            datetime:
                The renewedDateTime
        """
        if "renewedDateTime" in self._prop_dict:
            return datetime.strptime(self._prop_dict["renewedDateTime"].replace("Z", ""), "%Y-%m-%dT%H:%M:%S.%f")
        else:
            return None

    @renewed_date_time.setter
    def renewed_date_time(self, val):
        self._prop_dict["renewedDateTime"] = val.isoformat()+"Z"

    @property
    def resource_behavior_options(self):
        """
        Gets and sets the resourceBehaviorOptions
        
        Returns:
            str:
                The resourceBehaviorOptions
        """
        if "resourceBehaviorOptions" in self._prop_dict:
            return self._prop_dict["resourceBehaviorOptions"]
        else:
            return None

    @resource_behavior_options.setter
    def resource_behavior_options(self, val):
        self._prop_dict["resourceBehaviorOptions"] = val

    @property
    def resource_provisioning_options(self):
        """
        Gets and sets the resourceProvisioningOptions
        
        Returns:
            str:
                The resourceProvisioningOptions
        """
        if "resourceProvisioningOptions" in self._prop_dict:
            return self._prop_dict["resourceProvisioningOptions"]
        else:
            return None

    @resource_provisioning_options.setter
    def resource_provisioning_options(self, val):
        self._prop_dict["resourceProvisioningOptions"] = val

    @property
    def security_enabled(self):
        """
        Gets and sets the securityEnabled
        
        Returns:
            bool:
                The securityEnabled
        """
        if "securityEnabled" in self._prop_dict:
            return self._prop_dict["securityEnabled"]
        else:
            return None

    @security_enabled.setter
    def security_enabled(self, val):
        self._prop_dict["securityEnabled"] = val

    @property
    def theme(self):
        """
        Gets and sets the theme
        
        Returns:
            str:
                The theme
        """
        if "theme" in self._prop_dict:
            return self._prop_dict["theme"]
        else:
            return None

    @theme.setter
    def theme(self, val):
        self._prop_dict["theme"] = val

    @property
    def visibility(self):
        """
        Gets and sets the visibility
        
        Returns:
            str:
                The visibility
        """
        if "visibility" in self._prop_dict:
            return self._prop_dict["visibility"]
        else:
            return None

    @visibility.setter
    def visibility(self, val):
        self._prop_dict["visibility"] = val

    @property
    def access_type(self):
        """
        Gets and sets the accessType
        
        Returns: 
            :class:`GroupAccessType<onedrivesdk.model.group_access_type.GroupAccessType>`:
                The accessType
        """
        if "accessType" in self._prop_dict:
            if isinstance(self._prop_dict["accessType"], OneDriveObjectBase):
                return self._prop_dict["accessType"]
            else :
                self._prop_dict["accessType"] = GroupAccessType(self._prop_dict["accessType"])
                return self._prop_dict["accessType"]

        return None

    @access_type.setter
    def access_type(self, val):
        self._prop_dict["accessType"] = val

    @property
    def allow_external_senders(self):
        """
        Gets and sets the allowExternalSenders
        
        Returns:
            bool:
                The allowExternalSenders
        """
        if "allowExternalSenders" in self._prop_dict:
            return self._prop_dict["allowExternalSenders"]
        else:
            return None

    @allow_external_senders.setter
    def allow_external_senders(self, val):
        self._prop_dict["allowExternalSenders"] = val

    @property
    def auto_subscribe_new_members(self):
        """
        Gets and sets the autoSubscribeNewMembers
        
        Returns:
            bool:
                The autoSubscribeNewMembers
        """
        if "autoSubscribeNewMembers" in self._prop_dict:
            return self._prop_dict["autoSubscribeNewMembers"]
        else:
            return None

    @auto_subscribe_new_members.setter
    def auto_subscribe_new_members(self, val):
        self._prop_dict["autoSubscribeNewMembers"] = val

    @property
    def is_favorite(self):
        """
        Gets and sets the isFavorite
        
        Returns:
            bool:
                The isFavorite
        """
        if "isFavorite" in self._prop_dict:
            return self._prop_dict["isFavorite"]
        else:
            return None

    @is_favorite.setter
    def is_favorite(self, val):
        self._prop_dict["isFavorite"] = val

    @property
    def is_subscribed_by_mail(self):
        """
        Gets and sets the isSubscribedByMail
        
        Returns:
            bool:
                The isSubscribedByMail
        """
        if "isSubscribedByMail" in self._prop_dict:
            return self._prop_dict["isSubscribedByMail"]
        else:
            return None

    @is_subscribed_by_mail.setter
    def is_subscribed_by_mail(self, val):
        self._prop_dict["isSubscribedByMail"] = val

    @property
    def unseen_count(self):
        """
        Gets and sets the unseenCount
        
        Returns:
            int:
                The unseenCount
        """
        if "unseenCount" in self._prop_dict:
            return self._prop_dict["unseenCount"]
        else:
            return None

    @unseen_count.setter
    def unseen_count(self, val):
        self._prop_dict["unseenCount"] = val

    @property
    def unseen_conversations_count(self):
        """
        Gets and sets the unseenConversationsCount
        
        Returns:
            int:
                The unseenConversationsCount
        """
        if "unseenConversationsCount" in self._prop_dict:
            return self._prop_dict["unseenConversationsCount"]
        else:
            return None

    @unseen_conversations_count.setter
    def unseen_conversations_count(self, val):
        self._prop_dict["unseenConversationsCount"] = val

    @property
    def unseen_messages_count(self):
        """
        Gets and sets the unseenMessagesCount
        
        Returns:
            int:
                The unseenMessagesCount
        """
        if "unseenMessagesCount" in self._prop_dict:
            return self._prop_dict["unseenMessagesCount"]
        else:
            return None

    @unseen_messages_count.setter
    def unseen_messages_count(self, val):
        self._prop_dict["unseenMessagesCount"] = val

    @property
    def extensions(self):
        """Gets and sets the extensions
        
        Returns: 
            :class:`ExtensionsCollectionPage<onedrivesdk.request.extensions_collection.ExtensionsCollectionPage>`:
                The extensions
        """
        if "extensions" in self._prop_dict:
            return ExtensionsCollectionPage(self._prop_dict["extensions"])
        else:
            return None

    @property
    def members(self):
        """Gets and sets the members
        
        Returns: 
            :class:`MembersCollectionPage<onedrivesdk.request.members_collection.MembersCollectionPage>`:
                The members
        """
        if "members" in self._prop_dict:
            return MembersCollectionPage(self._prop_dict["members"])
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

    @property
    def created_on_behalf_of(self):
        """
        Gets and sets the createdOnBehalfOf
        
        Returns: 
            :class:`DirectoryObject<onedrivesdk.model.directory_object.DirectoryObject>`:
                The createdOnBehalfOf
        """
        if "createdOnBehalfOf" in self._prop_dict:
            if isinstance(self._prop_dict["createdOnBehalfOf"], OneDriveObjectBase):
                return self._prop_dict["createdOnBehalfOf"]
            else :
                self._prop_dict["createdOnBehalfOf"] = DirectoryObject(self._prop_dict["createdOnBehalfOf"])
                return self._prop_dict["createdOnBehalfOf"]

        return None

    @created_on_behalf_of.setter
    def created_on_behalf_of(self, val):
        self._prop_dict["createdOnBehalfOf"] = val

    @property
    def owners(self):
        """Gets and sets the owners
        
        Returns: 
            :class:`OwnersCollectionPage<onedrivesdk.request.owners_collection.OwnersCollectionPage>`:
                The owners
        """
        if "owners" in self._prop_dict:
            return OwnersCollectionPage(self._prop_dict["owners"])
        else:
            return None

    @property
    def settings(self):
        """Gets and sets the settings
        
        Returns: 
            :class:`SettingsCollectionPage<onedrivesdk.request.settings_collection.SettingsCollectionPage>`:
                The settings
        """
        if "settings" in self._prop_dict:
            return SettingsCollectionPage(self._prop_dict["settings"])
        else:
            return None

    @property
    def endpoints(self):
        """Gets and sets the endpoints
        
        Returns: 
            :class:`EndpointsCollectionPage<onedrivesdk.request.endpoints_collection.EndpointsCollectionPage>`:
                The endpoints
        """
        if "endpoints" in self._prop_dict:
            return EndpointsCollectionPage(self._prop_dict["endpoints"])
        else:
            return None

    @property
    def threads(self):
        """Gets and sets the threads
        
        Returns: 
            :class:`ThreadsCollectionPage<onedrivesdk.request.threads_collection.ThreadsCollectionPage>`:
                The threads
        """
        if "threads" in self._prop_dict:
            return ThreadsCollectionPage(self._prop_dict["threads"])
        else:
            return None

    @property
    def calendar(self):
        """
        Gets and sets the calendar
        
        Returns: 
            :class:`Calendar<onedrivesdk.model.calendar.Calendar>`:
                The calendar
        """
        if "calendar" in self._prop_dict:
            if isinstance(self._prop_dict["calendar"], OneDriveObjectBase):
                return self._prop_dict["calendar"]
            else :
                self._prop_dict["calendar"] = Calendar(self._prop_dict["calendar"])
                return self._prop_dict["calendar"]

        return None

    @calendar.setter
    def calendar(self, val):
        self._prop_dict["calendar"] = val

    @property
    def calendar_view(self):
        """Gets and sets the calendarView
        
        Returns: 
            :class:`CalendarViewCollectionPage<onedrivesdk.request.calendar_view_collection.CalendarViewCollectionPage>`:
                The calendarView
        """
        if "calendarView" in self._prop_dict:
            return CalendarViewCollectionPage(self._prop_dict["calendarView"])
        else:
            return None

    @property
    def events(self):
        """Gets and sets the events
        
        Returns: 
            :class:`EventsCollectionPage<onedrivesdk.request.events_collection.EventsCollectionPage>`:
                The events
        """
        if "events" in self._prop_dict:
            return EventsCollectionPage(self._prop_dict["events"])
        else:
            return None

    @property
    def conversations(self):
        """Gets and sets the conversations
        
        Returns: 
            :class:`ConversationsCollectionPage<onedrivesdk.request.conversations_collection.ConversationsCollectionPage>`:
                The conversations
        """
        if "conversations" in self._prop_dict:
            return ConversationsCollectionPage(self._prop_dict["conversations"])
        else:
            return None

    @property
    def photo(self):
        """
        Gets and sets the photo
        
        Returns: 
            :class:`ProfilePhoto<onedrivesdk.model.profile_photo.ProfilePhoto>`:
                The photo
        """
        if "photo" in self._prop_dict:
            if isinstance(self._prop_dict["photo"], OneDriveObjectBase):
                return self._prop_dict["photo"]
            else :
                self._prop_dict["photo"] = ProfilePhoto(self._prop_dict["photo"])
                return self._prop_dict["photo"]

        return None

    @photo.setter
    def photo(self, val):
        self._prop_dict["photo"] = val

    @property
    def photos(self):
        """Gets and sets the photos
        
        Returns: 
            :class:`PhotosCollectionPage<onedrivesdk.request.photos_collection.PhotosCollectionPage>`:
                The photos
        """
        if "photos" in self._prop_dict:
            return PhotosCollectionPage(self._prop_dict["photos"])
        else:
            return None

    @property
    def accepted_senders(self):
        """Gets and sets the acceptedSenders
        
        Returns: 
            :class:`AcceptedSendersCollectionPage<onedrivesdk.request.accepted_senders_collection.AcceptedSendersCollectionPage>`:
                The acceptedSenders
        """
        if "acceptedSenders" in self._prop_dict:
            return AcceptedSendersCollectionPage(self._prop_dict["acceptedSenders"])
        else:
            return None

    @property
    def rejected_senders(self):
        """Gets and sets the rejectedSenders
        
        Returns: 
            :class:`RejectedSendersCollectionPage<onedrivesdk.request.rejected_senders_collection.RejectedSendersCollectionPage>`:
                The rejectedSenders
        """
        if "rejectedSenders" in self._prop_dict:
            return RejectedSendersCollectionPage(self._prop_dict["rejectedSenders"])
        else:
            return None

    @property
    def drive(self):
        """
        Gets and sets the drive
        
        Returns: 
            :class:`Drive<onedrivesdk.model.drive.Drive>`:
                The drive
        """
        if "drive" in self._prop_dict:
            if isinstance(self._prop_dict["drive"], OneDriveObjectBase):
                return self._prop_dict["drive"]
            else :
                self._prop_dict["drive"] = Drive(self._prop_dict["drive"])
                return self._prop_dict["drive"]

        return None

    @drive.setter
    def drive(self, val):
        self._prop_dict["drive"] = val

    @property
    def drives(self):
        """Gets and sets the drives
        
        Returns: 
            :class:`DrivesCollectionPage<onedrivesdk.request.drives_collection.DrivesCollectionPage>`:
                The drives
        """
        if "drives" in self._prop_dict:
            return DrivesCollectionPage(self._prop_dict["drives"])
        else:
            return None

    @property
    def sites(self):
        """Gets and sets the sites
        
        Returns: 
            :class:`SitesCollectionPage<onedrivesdk.request.sites_collection.SitesCollectionPage>`:
                The sites
        """
        if "sites" in self._prop_dict:
            return SitesCollectionPage(self._prop_dict["sites"])
        else:
            return None

    @property
    def planner(self):
        """
        Gets and sets the planner
        
        Returns: 
            :class:`PlannerGroup<onedrivesdk.model.planner_group.PlannerGroup>`:
                The planner
        """
        if "planner" in self._prop_dict:
            if isinstance(self._prop_dict["planner"], OneDriveObjectBase):
                return self._prop_dict["planner"]
            else :
                self._prop_dict["planner"] = PlannerGroup(self._prop_dict["planner"])
                return self._prop_dict["planner"]

        return None

    @planner.setter
    def planner(self, val):
        self._prop_dict["planner"] = val

    @property
    def onenote(self):
        """
        Gets and sets the onenote
        
        Returns: 
            :class:`Onenote<onedrivesdk.model.onenote.Onenote>`:
                The onenote
        """
        if "onenote" in self._prop_dict:
            if isinstance(self._prop_dict["onenote"], OneDriveObjectBase):
                return self._prop_dict["onenote"]
            else :
                self._prop_dict["onenote"] = Onenote(self._prop_dict["onenote"])
                return self._prop_dict["onenote"]

        return None

    @onenote.setter
    def onenote(self, val):
        self._prop_dict["onenote"] = val

    @property
    def team(self):
        """
        Gets and sets the team
        
        Returns: 
            :class:`Team<onedrivesdk.model.team.Team>`:
                The team
        """
        if "team" in self._prop_dict:
            if isinstance(self._prop_dict["team"], OneDriveObjectBase):
                return self._prop_dict["team"]
            else :
                self._prop_dict["team"] = Team(self._prop_dict["team"])
                return self._prop_dict["team"]

        return None

    @team.setter
    def team(self, val):
        self._prop_dict["team"] = val

    @property
    def channels(self):
        """Gets and sets the channels
        
        Returns: 
            :class:`ChannelsCollectionPage<onedrivesdk.request.channels_collection.ChannelsCollectionPage>`:
                The channels
        """
        if "channels" in self._prop_dict:
            return ChannelsCollectionPage(self._prop_dict["channels"])
        else:
            return None

    @property
    def group_lifecycle_policies(self):
        """Gets and sets the groupLifecyclePolicies
        
        Returns: 
            :class:`GroupLifecyclePoliciesCollectionPage<onedrivesdk.request.group_lifecycle_policies_collection.GroupLifecyclePoliciesCollectionPage>`:
                The groupLifecyclePolicies
        """
        if "groupLifecyclePolicies" in self._prop_dict:
            return GroupLifecyclePoliciesCollectionPage(self._prop_dict["groupLifecyclePolicies"])
        else:
            return None

