class Connection:
    def __init__(self):
        self.xid = 0

    def start_transaction(self):
        print('starting transaction', self.xid)
        result = self.xid
        self.xid = self.xid + 1
        return result

    @staticmethod
    def commit_transaction(xid):
        print('committing transaction', xid)

    @staticmethod
    def rollback_transaction(xid):
        print('rolling back transaction', xid)