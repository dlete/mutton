
def reconcile_client():

    ''' Here we only sets/not logging '''
    import logging
    logger = logging.getLogger(__name__)
    # Set to INFO if you do WANT to see DEBUG and INFO messages.
    # Set to WARNING if you do NOT WANT to see DEBUG and INFO messages.
    logging.basicConfig(level=logging.INFO)
    #logging.basicConfig(level=logging.WARNING)

    logger.info('hola:  %s', "Pepe")

    # import lxml so that we can work with xml
    from lxml import etree

    '''
    f = open('get_customer_all.xml')
    customers_xml = f.read()
    f.close()
    '''
    #customers_xml = etree.parse('get_customer_all.xml')
    #root = customers_xml.getroot()
    #print(root)

    # To work with a local file
    doc_to_read = 'get_customer_all.xml'
    tree = etree.parse(doc_to_read)
    root = tree.getroot()

    for element in root.findall('.//{services.schema.networkapi.jmp.juniper.net}Customer'):
        customer_name = element.find('.//{services.schema.networkapi.jmp.juniper.net}CustomerName').text
        identity = element.find('.//{services.schema.networkapi.jmp.juniper.net}Identity').text
        create_date = element.find('.//{services.schema.networkapi.jmp.juniper.net}CreatedDate').text
        last_update_date = element.find('.//{services.schema.networkapi.jmp.juniper.net}LastUpdatedDate').text
        account_number = element.find('.//{services.schema.networkapi.jmp.juniper.net}AccountNo').text

        logger.info('customer_name is: %s', customer_name)
        logger.info('identity is: %s', identity)
        logger.info('create_date is: %s', create_date)
        logger.info('last_update_date is: %s', last_update_date)
        logger.info('account_number is: %s', account_number)

       


reconcile_client()
