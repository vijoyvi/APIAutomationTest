import requests;

class AuthorizeOrder_Implementation:

    def __init__(self,orderNo,orderHdrKey):
        self.orderNo=orderNo
        self.orderHdrKey = orderHdrKey

    def  authorizeOrder(self):
        print "Authorizing the Order"
        data = {
            'InteropApiName': 'requestCollection',
            'IsFlow': 'N',
            'YFSEnvironment.userId': 'postestadmin',
            'InteropApiData': "<Order OrderNo="+"\'"+str(self.orderNo)+"\'"+" OrderHeaderKey="+"\'"+str(self.orderHdrKey)+"\'"+" IgnoreTransactionDependencies='Y' CarrierServiceCode='UPS_FEDEX_STANDARD' EnterpriseCode='PETCOCOMUS' DocumentType='0001'/>"
        }

        try:
            r = requests.post("http://cmsomsappt01:9080/smcfs/interop/InteropHttpServlet", data=data);
        except:
            print "Exception while authorizing the Order"
            return False

        print "Order is authorized successfully"

        return True

#obj1=RemorseHoldRelease_Implementation('76177259');
#obj1.remorseHoldRelease()