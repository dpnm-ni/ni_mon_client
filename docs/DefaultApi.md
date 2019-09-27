# ni_mon_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_link**](DefaultApi.md#get_link) | **GET** /link/{id} | get detailed information of a link
[**get_link_between_nodes**](DefaultApi.md#get_link_between_nodes) | **GET** /link_between_nodes | get detailed information of a link between two specific nodes
[**get_links**](DefaultApi.md#get_links) | **GET** /links | get list of link
[**get_mesurement**](DefaultApi.md#get_mesurement) | **GET** /vnfinstances/{id}/{mesurement_type} | get mesurement value
[**get_node**](DefaultApi.md#get_node) | **GET** /nodes/{id} | get detailed information of a node
[**get_node_list**](DefaultApi.md#get_node_list) | **GET** /nodes | get a list of nodes
[**get_topology**](DefaultApi.md#get_topology) | **GET** /topology | get topology
[**get_vnf_flavor**](DefaultApi.md#get_vnf_flavor) | **GET** /vnfflavors/{id} | get detailed information of a vnfflavor
[**get_vnf_flavor_list**](DefaultApi.md#get_vnf_flavor_list) | **GET** /vnfflavors | get a list of vnfflavors
[**get_vnf_instance**](DefaultApi.md#get_vnf_instance) | **GET** /vnfinstances/{id} | get detailed information of a vnf instance
[**get_vnf_instance_list**](DefaultApi.md#get_vnf_instance_list) | **GET** /vnfinstances | get a list of vnf instances


# **get_link**
> Link get_link(id)

get detailed information of a link

Return detailed information of a link. 

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()
id = 'id_example' # str | The id of the link

try:
    # get detailed information of a link
    api_response = api_instance.get_link(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the link | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link_between_nodes**
> Link get_link_between_nodes(node1_id, node2_id)

get detailed information of a link between two specific nodes

Return detailed information of a link between two specific nodes. 

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()
node1_id = 'node1_id_example' # str | The id of the first node in the link
node2_id = 'node2_id_example' # str | The id of the second node in the link

try:
    # get detailed information of a link between two specific nodes
    api_response = api_instance.get_link_between_nodes(node1_id, node2_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_link_between_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node1_id** | **str**| The id of the first node in the link | 
 **node2_id** | **str**| The id of the second node in the link | 

### Return type

[**Link**](Link.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_links**
> str get_links()

get list of link

Return list of link id. 

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()

try:
    # get list of link
    api_response = api_instance.get_links()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_links: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mesurement**
> list[MonitoringEntry] get_mesurement(id, mesurement_type, start_time, end_time)

get mesurement value

Return the value of a mesurement of a vnf instance at a timestamp or a timestamp period 

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()
id = 'id_example' # str | The id of the vnf instance
mesurement_type = 'mesurement_type_example' # str | The mesurement_type
start_time = '2013-10-20T19:20:30+01:00' # datetime | starting time to get the mesurement
end_time = '2013-10-20T19:20:30+01:00' # datetime | ending time to get the mesurement

try:
    # get mesurement value
    api_response = api_instance.get_mesurement(id, mesurement_type, start_time, end_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_mesurement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the vnf instance | 
 **mesurement_type** | **str**| The mesurement_type | 
 **start_time** | **datetime**| starting time to get the mesurement | 
 **end_time** | **datetime**| ending time to get the mesurement | 

### Return type

[**list[MonitoringEntry]**](MonitoringEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node**
> Node get_node(id)

get detailed information of a node

Return detailed information of a node 

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()
id = 'id_example' # str | The id of the node

try:
    # get detailed information of a node
    api_response = api_instance.get_node(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the node | 

### Return type

[**Node**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_node_list**
> list[str] get_node_list()

get a list of nodes

Return a list of nodes 

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()

try:
    # get a list of nodes
    api_response = api_instance.get_node_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_node_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_topology**
> Topology get_topology()

get topology

Return a topology with lists of node ids and link ids 

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()

try:
    # get topology
    api_response = api_instance.get_topology()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_topology: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Topology**](Topology.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vnf_flavor**
> VNFFlavor get_vnf_flavor(id)

get detailed information of a vnfflavor

Return detailed information of a vnfflavor 

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()
id = 'id_example' # str | The name of the vnfflavor

try:
    # get detailed information of a vnfflavor
    api_response = api_instance.get_vnf_flavor(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_vnf_flavor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of the vnfflavor | 

### Return type

[**VNFFlavor**](VNFFlavor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vnf_flavor_list**
> list[str] get_vnf_flavor_list()

get a list of vnfflavors

Return a list of vnfflavors 

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()

try:
    # get a list of vnfflavors
    api_response = api_instance.get_vnf_flavor_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_vnf_flavor_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vnf_instance**
> VNFInstance get_vnf_instance(id)

get detailed information of a vnf instance

Return detailed information of a vnf instance 

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()
id = 'id_example' # str | The id of the vnf instance

try:
    # get detailed information of a vnf instance
    api_response = api_instance.get_vnf_instance(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_vnf_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the vnf instance | 

### Return type

[**VNFInstance**](VNFInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vnf_instance_list**
> list[str] get_vnf_instance_list()

get a list of vnf instances

Return a list of vnf instances 

### Example
```python
from __future__ import print_function
import time
import ni_mon_client
from ni_mon_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = ni_mon_client.DefaultApi()

try:
    # get a list of vnf instances
    api_response = api_instance.get_vnf_instance_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_vnf_instance_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

