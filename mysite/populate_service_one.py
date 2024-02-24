
# set the Python environment to use Django.
# Equivalent to "python manage.py startshell"
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()
from inventories.models import Client
from inventories.models import ElineLdp
from inventories.models import Ne
from inventories.models import ServiceType
from inventories.models import Service
from inventories.models import ServiceEndpoint

def add_object(service_id, ne_id, interface_name, interface_index):
    s = ServiceEndpoint.objects.get_or_create(
        service = service_id,
        ne = ne_id,
        interface_name = interface_name,
        interface_index = interface_index
    )[0]
    return s


def populate():
    import logging
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.INFO)
    
    # import lxml so that we can work with xml
    from lxml import etree

    # To work with a local file
    #doc_to_read = 'get_eline_ldp_all.xml'
    #doc_to_read = 'get_l3vpn_all.xml'
    #doc_to_read = 'get_eline_ldp_one.xml'
    doc_to_read = 'get_l3vpn_one.xml'
    tree = etree.parse(doc_to_read)
    root = tree.getroot()

    for element in root.findall('.//{services.schema.networkapi.jmp.juniper.net}Service'):
        name = element.find('.//{services.schema.networkapi.jmp.juniper.net}Name').text
        identity = element.find('.//{services.schema.networkapi.jmp.juniper.net}Identity').text
        service_id = Service.objects.get(csd_id=identity)
        logger.info('name is: %s', name)
        logger.info('identity is: %s', identity)

        for element in root.findall('.//{services.schema.networkapi.jmp.juniper.net}ServiceEndPointGroup'):
            device_name = element.find('.//{services.schema.networkapi.jmp.juniper.net}DeviceName').text

            device_id = element.find('.//{services.schema.networkapi.jmp.juniper.net}DeviceID').text
            ne_id = Ne.objects.get(id_csd=device_id)
            interface_name = element.find('.//{services.schema.networkapi.jmp.juniper.net}InterfaceName').text
            try:
                interface_index = element.find('.//{services.schema.networkapi.jmp.juniper.net}InterfaceIndex').text
            except:
                interface_index = element.find('.//{services.schema.networkapi.jmp.juniper.net}InterfaceId').text
            logger.info('device_name is: %s', device_name)
            logger.info('device_id is: %s', device_id)
            logger.info('interface_name is: %s', interface_name)
            logger.info('interface_index is: %s', interface_index)
            a = add_object(service_id, ne_id, interface_name, interface_index)
            #print(a)

populate()
