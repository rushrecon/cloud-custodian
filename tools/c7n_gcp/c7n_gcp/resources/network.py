# Copyright 2018 Capital One Services, LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import time
import re

from c7n_gcp.actions import MethodAction
from c7n_gcp.query import QueryResourceManager, TypeInfo

from c7n_gcp.provider import resources
from c7n.utils import type_schema


@resources.register('vpc')
class Network(QueryResourceManager):

    class resource_type(TypeInfo):
        service = 'compute'
        version = 'v1'
        component = 'networks'
        scope_template = "projects/{}/global/networks"


@resources.register('subnet')
class Subnet(QueryResourceManager):

    class resource_type(TypeInfo):
        service = 'compute'
        version = 'v1'
        component = 'subnetworks'
        enum_spec = ('aggregatedList', 'items.*.subnetworks[]', None)

        @staticmethod
        def get(client, resource_info):
            return client.execute_query(
                'get', {'project': resource_info['project_id'],
                        'region': resource_info['location'],
                        'subnetwork': resource_info['subnetwork_name']})


class SubnetAction(MethodAction):

    path_param_re = re.compile(
        '.*?/projects/(.*?)/regions/(.*?)/subnetworks/(.*)')

    def get_resource_params(self, model, resource):
        project, region, subnet = self.path_param_re.match(
            resource['selfLink']).groups()
        return {'project': project, 'region': region, 'subnetwork': subnet}


@Subnet.action_registry.register('set-flow-log')
class SetFlowLog(SubnetAction):
    """Enable vpc flow logs on a subnet.

    :example: Enable flow logs on all subnets

    .. yaml:

     policies:
       - name: flow-active
         resource: gcp.subnet
         filters:
          - enableFlowLogs: empty
         actions:
          - set-flow-log

    """

    schema = type_schema(
        'set-flow-log',
        state={'type': 'boolean', 'default': True})
    method_spec = {'op': 'patch'}

    def get_resource_params(self, m, r):
        params = super(SetFlowLog, self).get_resource_params(m, r)
        params['body'] = dict(r)
        params['body']['enableFlowLogs'] = self.data.get('state', True)
        return params


@Subnet.action_registry.register('set-private-api')
class SetGcpPrivateAccess(SubnetAction):
    """Enable/Disable GCP Private IP Access for a subnet"""

    schema = type_schema(
        'set-gcp-private',
        state={'type': 'boolean', 'default': True})
    method_spec = {'op': 'setPrivateIpGoogleAccess'}

    def get_resource_params(self, m, r):
        params = super(SetGcpPrivateAccess, self).get_resource_params(m, r)
        params['body'] = {
            'privateIpGoogleAccess': self.data.get('state', True)}
        return params


@resources.register('firewall')
class Firewall(QueryResourceManager):

    class resource_type(TypeInfo):
        service = 'compute'
        version = 'v1'
        component = 'firewalls'

        @staticmethod
        def get(client, resource_info):
            return client.execute_query(
                'get', {'project': resource_info['project_id'],
                        'firewall': resource_info['resourceName'].rsplit('/', 1)[-1]})


@resources.register('router')
class Router(QueryResourceManager):

    class resource_type(TypeInfo):
        service = 'compute'
        version = 'v1'
        component = 'routers'
        enum_spec = ('aggregatedList', 'items.*.routers[]', None)
        scope_template = "projects/{}/aggregated/routers"


@resources.register('route')
class Route(QueryResourceManager):

    class resource_type(TypeInfo):
        service = 'compute'
        version = 'v1'
        component = 'routes'
        scope_template = "projects/{}/global/routes"


@resources.register('managed-zone')
class ManagedZone(QueryResourceManager):
    # roles/dns.admin
    class resource_type(TypeInfo):
        service = 'dns'
        version = 'v1'
        component = 'managedZones'
        enum_spec = ('list', 'managedZones[]', None)
        scope = 'project'


class ManagedZoneAction(MethodAction):
    def get_resource_params(self, model, resource):
        return {'managedZone': resource['name'], 'project': resource['default_project']}


@ManagedZone.action_registry.register('delete')
class DeleteManagedZone(ManagedZoneAction):
    """https://cloud.google.com/dns/docs/reference/v1/managedZones/delete"""
    schema = type_schema(
        'delete',
        state={})
    method_spec = {'op': 'delete'}


@ManagedZone.action_registry.register('patch')
class PatchManagedZone(ManagedZoneAction):
    """https://cloud.google.com/dns/docs/reference/v1/managedZones/patch"""
    schema = type_schema(
        'patch',
        state={})
    method_spec = {'op': 'patch'}

    def get_resource_params(self, model, resource):
        params = ManagedZoneAction.get_resource_params(self, model, resource)
        #https://cloud.google.com/dns/docs/reference/v1/managedZones#resource
        params['body'] = {
            #CANNOT be modified:
            #'kind'
            #'name'
            #'dnsName'
            #'id'
            #'nameServers'
            #'nameServerSet'
            #'creationTime'
            #EDIBLE:
            #private zones: ONLY empty:
            'dnssecConfig' : {},
            #public zones: error code 503 (though used 'Equivalent REST request')
            # 'dnssecConfig' : {
            #     "kind": "dns#managedZoneDnsSecConfig",
            #     "state": 'off',
            #     "defaultKeySpecs": [
            #         {#there must be records both for key and zone signing
            #             "kind": "dns#dnsKeySpec",
            #             "keyType": 'keySigning',
            #             "algorithm": 'rsasha256',
            #             "keyLength": 2048 #512, 1024 won't work
            #         },
            #         {
            #             "kind": "dns#dnsKeySpec",
            #             "keyType": 'zoneSigning',
            #             "algorithm": 'rsasha256',
            #             "keyLength": 1024
            #         }
            #     ],
            #     "nonExistence": 'nsec3'
            # },
            'description': 'patched-' + resource['description'],
            'labels': {'custodian':'patched'} #replaces the existing ones
        }
        return params


@ManagedZone.action_registry.register('update')
class UpdateManagedZone(ManagedZoneAction):
    """https://cloud.google.com/dns/docs/reference/v1/managedZones/update"""
    schema = type_schema(
        'update',
        state={})
    method_spec = {'op': 'update'}

    def get_resource_params(self, model, resource):
        params = ManagedZoneAction.get_resource_params(self, model, resource)
        #
        params['body'] = {
            #required, cannot be modified: START
            'id': resource['id'],
            'name': resource['name'],
            'dnsName': resource['dnsName'],
            'nameServers': resource['nameServers'],
            'creationTime': resource['creationTime'],
            #required, cannot be modified: END
            #??? The 'entity.managedZone.visibility' parameter is required but was missing
            #regardless of the specified type (though there is no 'visibility' mentined in the docs)
            'visibility': 'private', #https://cloud.google.com/dns/zones/?hl=en_US
            #required, potentially updateable according to 'patch' method:
            'description': 'updated-' + resource['description']
        }
        return params


@ManagedZone.action_registry.register('create')
class CreateManagedZone(ManagedZoneAction):
    """https://cloud.google.com/dns/docs/reference/v1/managedZones/create"""
    schema = type_schema(
        'create',
        state={})
    method_spec = {'op': 'create'}

    def get_resource_params(self, model, resource):
        suffix = str(int(round(time.time() * 1000)))
        params = {
            'project': resource['default_project'],
            'body': {
                'name': 'custodian' + suffix,
                'dnsName': 'custodian%s.ns-gcp-private.googledomains.' % suffix,
                'description': 'custodian' + suffix,
                'visibility': 'private',
                'privateVisibilityConfig': {'networks': []}
            }}
        return params

    def filter_resources(self, resources):
        return {}
