import osfrom configparser import ConfigParserclass Config:    config = ConfigParser()    def __init__(self):        if os.path.exists(os.path.join(os.path.dirname(__file__),            'config.ini')):            #print("Using path ",os.path.join(os.path.dirname(__file__),            #'config.ini'))            self.config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))        else:            #print("Using path ",os.path.join(os.path.dirname(__file__),            #'default.ini'))            self.config.read(os.path.join(os.path.dirname(__file__), 'default.ini'))    def get_database_connection_string(self):        if 'nourskin_db' in self.config:            nourskin_db = self.config['nourskin_db']            dbtype = nourskin_db.get('type', 'mysql')            dbhost = nourskin_db.get('hostname', 'localhost')            dbport = nourskin_db.get('port', '3306')            dbuser = nourskin_db.get('username', 'root')            dbpass = nourskin_db.get('password', 'nopass')            dbname = nourskin_db.get('database', 'nodb')            return "%s://%s:%s@%s:%s/%s" % (                    dbtype,                    dbuser,                    dbpass,                    dbhost,                    dbport,                    dbname)        else:            return 'no_configuration_string'    def woo_get_url(self);        if 'wooapi' in self.config:            return config['wooapi'].get('url', 'https://localhost')        else:            return 'https://localhost'    def woo_get_consumer_key(self);        if 'wooapi' in self.config:            return config['wooapi'].get('consumer_key', '')        else:            return ''    def woo_get_consumer_secret(self);        if 'wooapi' in self.config:            return config['wooapi'].get('consumer_secret', '')        else:            return ''