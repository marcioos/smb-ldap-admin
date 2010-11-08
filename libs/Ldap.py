from time import time
from subprocess import Popen, PIPE
from ldap import SCOPE_SUBTREE, ldapobject


class NoSuchUser(Exception):
    pass


class CommandError(Exception):
    pass


class Ldap(ldapobject.SimpleLDAPObject):
    '''
    handles usual ldap operations on a samba domain
    using smbldap-tools
    '''

    def __init__(self, **opts):
        '''
        Establishes an ldap connection and bind if needed.
        '''

        self._host = opts['host']
        self._base_dn = opts['base_dn']
        self._ldap_tools = opts['ldap_tools']
        self._bind_dn = opts.get('bind_dn', '')
        self._bind_pw = opts.get('bind_pw', '')

        ldapobject.SimpleLDAPObject.__init__(self, self._host)

        if (len(self._bind_dn) > 0) and (len(self._bind_pw) > 0):
            self.simple_bind_s(self._bind_dn, self._bind_pw)

    def get_user(self, username, just=['uid']):
        query = '(uid=%s)' % username
        return self.search_s(self._base_dn, SCOPE_SUBTREE, query, just)

    def get_user_by_attr(self, attr, value, just=['uid']):
        query = '(%s=%s)' % (attr, value)
        return self.search_s(self._base_dn, SCOPE_SUBTREE, query, just)

    def list_users(self):
        return self.get_user('*')

    def user_expired(self, username):
        user = self.get_user(username, ['sambaKickoffTime'])
        if len(user) > 0:
            try:
                expire_date = user[0][1]['sambaKickoffTime'][0]
            except KeyError:
                return False
            return float(expire_date) < time()
        else:
            raise NoSuchUser

    def user_exists(self, username):
        results = self.get_user(username)
        return len(results) > 0

    def del_user(self, username):
        command = [self._ldap_tools['user_del'], username]
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        error = process.stderr.read()
        if len(error) > 0:
            raise CommandError(error)
        elif 'does not exist' in process.stdout.read():
            raise NoSuchUser
        return True
