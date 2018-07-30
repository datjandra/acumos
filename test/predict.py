import component_pb2 as pb
import requests

def colored(text, color="\033[1;32m"):
    return color + text + "\033[0m"

def yes_no(number):
    return "Yes" if (number == 1) else "No"

def test_data():
    pi = pb.predictInput()
    # these variables have no effect on prediction
    pi.id.append(1)
    pi.overall_Xstar_Xrating.append(0)

    # these are the dependent variables for prediction
    pi.price_Xrange.append("$")
    pi.restaurant_Xservices_Xdelivery.append(0)
    pi.restaurant_Xservices_Xcatering.append(0)
    pi.restaurant_Xservices_Xgroups.append(1)
    pi.restaurant_Xservices_Xkids.append(1)
    pi.restaurant_Xservices_Xoutdoor.append(1)
    pi.restaurant_Xservices_Xreserve.append(0)
    pi.restaurant_Xservices_Xtakeout.append(1)
    pi.restaurant_Xservices_Xwaiter.append(1)
    pi.restaurant_Xservices_Xwalkins.append(1)
    pi.parking_Xlot.append(0)
    pi.parking_Xstreet.append(1)
    pi.parking_Xvalet.append(0)
    return pi

def dump_input(pi):
    print colored("#=============================================================================#", "\033[1;36m")
    print colored("# --- Restaurant Features --- #", "\033[1;31m")
    print colored("Price: %s" % pi.price_Xrange[0])
    print colored("Catering: %s" % yes_no(pi.restaurant_Xservices_Xcatering[0]))
    print colored("Delivery: %s" % yes_no(pi.restaurant_Xservices_Xdelivery[0]))
    print colored("Groups: %s" % yes_no(pi.restaurant_Xservices_Xgroups[0]))
    print colored("Kids: %s" % yes_no(pi.restaurant_Xservices_Xkids[0]))
    print colored("Outdoors: %s" % yes_no(pi.restaurant_Xservices_Xoutdoor[0]))
    print colored("Reservations: %s" % yes_no(pi.restaurant_Xservices_Xreserve[0]))
    print colored("Takeout: %s" % yes_no(pi.restaurant_Xservices_Xtakeout[0]))
    print colored("Walkins: %s" % yes_no(pi.restaurant_Xservices_Xwalkins[0]))
    print colored("Waiters: %s" % yes_no(pi.restaurant_Xservices_Xwaiter[0]))
    print colored("Lot Parking: %s" % yes_no(pi.parking_Xlot[0]))
    print colored("Street Parking: %s" % yes_no(pi.parking_Xstreet[0]))
    print colored("Valet Parking: %s" % yes_no(pi.parking_Xvalet[0]))
    print colored("#=============================================================================#", "\033[1;36m")

def dump_output(po):
    print colored("#=============================================================================#", "\033[1;36m")
    print colored("# --- Prediction --- #", "\033[1;31m")
    print colored("Probability of restaurant having >=4 rating: %s" % po.x[0])
    print colored("#=============================================================================#", "\033[1;36m")

def predict(pi):
    restURL = "http://localhost:3330/predict"
    response = requests.post(restURL, pi.SerializeToString())

    po = pb.predictOutput()
    po.ParseFromString(response.content)
    return po


print """
  Be sure to run Docker micro-service before running this test script, e.g.:

  docker load -i facebookstarratings_a54da5e1-3603-46bc-ab89-f7d07f5d1147_1.tar
  docker run -p 3330:3330 acumos-devchallenge-nexus:18001/facebookstarratings_a54da5e1-3603-46bc-ab89-f7d07f5d1147:1
  """

pi = test_data()
dump_input(pi)
print "\n"
po = predict(pi)
dump_output(po)
