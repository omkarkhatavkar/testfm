import configparser

config = configparser.ConfigParser()
config.read('testfm.properties')

RHN_USERNAME = config['subscription']['RHN_USERNAME']
RHN_PASSWORD = config['subscription']['RHN_PASSWORD']
RHN_POOLID = config['subscription']['RHN_POOLID']
DOGFOOD_ORG = config['subscription']['DOGFOOD_ORG']
DOGFOOD_ACTIVATIONKEY = config['subscription']['DOGFOOD_ACTIVATIONKEY']
DOGFOOD_URL = config['subscription']['DOGFOOD_URL']
katello_ca_consumer = DOGFOOD_URL + '/pub/katello-ca-consumer-latest.noarch.rpm'
upstream_url = {
    'candlepin_repo': (
        'https://fedorapeople.org/groups/katello/releases/yum/3.8/candlepin/el7/x86_64/'),
    'client_repo': 'https://fedorapeople.org/groups/katello/releases/yum/3.8/client/el7/x86_64/',
    'katello_repo': (
        'https://fedorapeople.org/groups/katello/releases/yum/latest/katello/el7/x86_64/'),
    'plugins_repo': 'https://yum.theforeman.org/plugins/latest/el7/x86_64/',
    'pulp_repo': 'https://fedorapeople.org/groups/katello/releases/yum/3.5/pulp/el7/x86_64/',
    'puppet_repo': 'http://yum.puppetlabs.com/el/6.4/x86_64/',
    'releases_repo': 'https://yum.theforeman.org/releases/latest/el7/x86_64/'
}
sat_63_repo = ['rhel-7-server-rpms', 'rhel-7-server-satellite-6.3-rpms',
               'rhel-7-server-satellite-maintenance-6-rpms', 'rhel-server-rhscl-7-rpms',
               'rhel-7-server-satellite-tools-6.3-rpms',
               ]
sat_64_repo = ['rhel-7-server-ansible-2.6-rpms', 'rhel-7-server-rpms',
               'rhel-7-server-satellite-6.4-rpms', 'rhel-7-server-satellite-maintenance-6-rpms',
               'rhel-7-server-satellite-tools-6.4-rpms', 'rhel-server-rhscl-7-rpms']
sat_65_repo = ['rhel-7-server-ansible-2.6-rpms', 'rhel-7-server-rpms',
               'rhel-7-server-satellite-6.5-rpms', 'rhel-7-server-satellite-maintenance-6-rpms',
               'rhel-7-server-satellite-tools-6.5-rpms', 'rhel-server-rhscl-7-rpms']