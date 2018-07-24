import component_pb2 as pb
import requests

pi = pb.predictInput()
pi.id.append(1)
pi.overall_Xstar_Xrating.append(0)
pi.price_Xrange.append("$")

pi.restaurant_Xservices_Xdelivery.append(0)
pi.restaurant_Xservices_Xcatering.append(0)
pi.restaurant_Xservices_Xgroups.append(0)
pi.restaurant_Xservices_Xkids.append(0)
pi.restaurant_Xservices_Xoutdoor.append(0)
pi.restaurant_Xservices_Xreserve.append(0)
pi.restaurant_Xservices_Xtakeout.append(0)
pi.restaurant_Xservices_Xwaiter.append(0)
pi.restaurant_Xservices_Xwalkins.append(0)

pi.parking_Xlot.append(0)
pi.parking_Xstreet.append(0)
pi.parking_Xvalet.append(0)

restURL = "http://localhost:3330/predict"
response = requests.post(restURL, pi.SerializeToString())
print "Status code: %d" % response.status_code

po = pb.predictOutput()
po.ParseFromString(response.content)
print "Probability of star rating >= 4: %s" % po.x[0]
