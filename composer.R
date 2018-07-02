library(acumos)
csv = read.csv("training.csv", header=TRUE)

train = csv[, c("id",
  "overall_star_rating",
  "price_range",
  "restaurant_services_delivery",
  "restaurant_services_catering",
  "restaurant_services_groups",
  "restaurant_services_kids",
  "restaurant_services_outdoor",
  "restaurant_services_reserve",
  "restaurant_services_takeout",
  "restaurant_services_waiter",
  "restaurant_services_walkins",
  "parking_lot",
  "parking_street",
  "parking_valet")]

train = train[!duplicated(train$id), ]
train = train[!(is.na(train$overall_star_rating) | train$overall_star_rating==""), ]
train$price_range = as.character(train$price_range)
train$overall_star_rating = ifelse(train$overall_star_rating < 4, 0, 1)

descriptor = lapply(train, class)
compose(predict=function(..., inputs=descriptor) as.character(predict(model, as.data.frame(list(...)))),
        aux = list(
          model = glm(overall_star_rating ~
            price_range +
            restaurant_services_delivery +
            restaurant_services_catering +
            restaurant_services_groups +
            restaurant_services_kids +
            restaurant_services_outdoor +
            restaurant_services_reserve +
            restaurant_services_takeout +
            restaurant_services_waiter +
            restaurant_services_walkins +
            parking_lot +
            parking_street +
            parking_valet,
            data=train, family=binomial)
        ), name="Facebook Star Ratings")
