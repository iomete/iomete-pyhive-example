import base64
from dataclasses import dataclass

from pyhive import hive
from thrift.transport import THttpClient


@dataclass
class ConnectionArgs:
    account_id: str = None
    cluster: str = None
    user: str = None
    password: str = None
    database: str = "default"

    def __post_init__(self):
        if not self.account_id:
            raise TypeError("'account_id' must be provided.")

        if not self.cluster:
            raise TypeError("'cluster' must be provided.")

        if not self.user:
            raise TypeError("'user' must be provided.")
        
        if not self.password:
            raise TypeError("'password' must be provided.")

    def connection_string(self):
        return "https://dwh-{account_id}.iomete.com/{cluster}/cliservice".format(
            account_id = self.account_id,
            cluster=self.cluster
        )


def create_connection(connection_args: ConnectionArgs):
    transport = THttpClient.THttpClient(connection_args.connection_string())
    credentials = "%s:%s" % (connection_args.user, connection_args.password)
    transport.setCustomHeaders(
        {"Authorization": "Basic " + base64.b64encode(credentials.encode()).decode().strip()})

    return hive.connect(database=connection_args.database, thrift_transport=transport)
