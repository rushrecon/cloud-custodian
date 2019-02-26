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

import re

from c7n.utils import type_schema
from c7n_gcp.actions import MethodAction
from c7n_gcp.provider import resources
from c7n_gcp.query import QueryResourceManager, TypeInfo


@resources.register('sql-instance-database')
class SqlInstanceDatabase(QueryResourceManager):
    class resource_type(TypeInfo):
        service = 'sqladmin'
        version = 'v1beta4'
        component = 'databases'
        enum_spec = ('list', "items[]", None)
        scope = 'project'

    def get_resource_query(self):
        if 'query' in self.data:
            return self.data.get('query')[0]


class SqlInstanceDatabaseAction(MethodAction):
    def get_resource_params(self, model, resource):
        return {
            'project': resource['default_project']
        }


@SqlInstanceDatabase.action_registry.register('delete')
class SqlInstanceDatabaseDelete(SqlInstanceDatabaseAction):
    schema = type_schema(
        'delete'
    )

    method_spec = {
        'op': 'delete',
        'annotation_key': 'c7n.gcp:sql-instance-database-create',
        'result_key': 'status'
    }

    path_param_re = re.compile('.*?/projects/(.*?)/instances/(.*)/databases/(.*)')

    def get_resource_params(self, model, resource):
        project, instance, database = self.path_param_re.match(
            resource['selfLink']).groups()
        return {
            'project': project,
            'instance': instance,
            'database': database
        }


@SqlInstanceDatabase.action_registry.register('create')
class SqlInstanceDatabaseCreate(SqlInstanceDatabaseAction):
    schema = type_schema(
        'create',
        instance={'type': 'string'},
        database={'type': 'string'}
    )

    method_spec = {
        'op': 'insert',
        'annotation_key': 'c7n.gcp:sql-instance-database-create',
        'result_key': 'status'
    }

    def get_resource_params(self, model, resource):
        params = SqlInstanceDatabaseAction.get_resource_params(self, model, resource)
        params['instance'] = self.data['instance']
        params['database'] = self.data['database']
        params['body'] = {
            'instance': params['instance'],
            'name' : params['database'],
            'project': params['project']
        }
        del params['database']
        return params