# Facebook star ratings prediction.
## What is this project about?
Basic "hello world" example to:

1. Compose ratings prediction model for on-boarding to Acumos.
2. Script to test model locally.

## How to run it?
1. Install Docker, R and Python.
2. Install Acumos library for R one time.
3. Run composer.R script to compose model file.
4. On-board model to Acumos portal.
5. Download on-boarded model for local testing.
6. Run Docker micro-service container.
7. Run Python script to test prediction against micro-service.

Run Docker micro-service container.
```
$ docker load -i facebookstarratings_a54da5e1-3603-46bc-ab89-f7d07f5d1147_1.tar
Loaded image: acumos-devchallenge-nexus:18001/facebookstarratings_a54da5e1-3603-46bc-ab89-f7d07f5d1147:1

$ docker run -p 3330:3330 acumos-devchallenge-nexus:18001/facebookstarratings_a54da5e1-3603-46bc-ab89-f7d07f5d1147:1
-- running Rserve in this R session (pid=1), 1 server(s) --
(This session will block until Rserve is shut down)
```

Run Python script to test prediction against micro-service.
```
$ python test/predict.py

  Be sure to run Docker micro-service before running this test script, e.g.:

  docker load -i facebookstarratings_a54da5e1-3603-46bc-ab89-f7d07f5d1147_1.tar
  docker run -p 3330:3330 acumos-devchallenge-nexus:18001/facebookstarratings_a54da5e1-3603-46bc-ab89-f7d07f5d1147:1

#=============================================================================#
# --- Restaurant Features --- #
Price: $
Catering: No
Delivery: No
Groups: Yes
Kids: Yes
Outdoors: Yes
Reservations: No
Takeout: Yes
Walkins: Yes
Waiters: Yes
Lot Parking: No
Street Parking: Yes
Valet Parking: No
#=============================================================================#


#=============================================================================#
# --- Prediction --- #
Probability of restaurant having >=4 rating: 0.87276280000479
#=============================================================================#
$
```

Test prediction with different inputs in predict.py script.
```
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
```
