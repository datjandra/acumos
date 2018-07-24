## Change directory so that this script and training.csv are in current directory.
## Comment out next line to install acumos library.
## install.packages("acumos",,c("http://rforge.net"))
library(acumos)

## Boilerplate code to read CSV into R data frame
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

## Remove duplicate ID's if any.
train = train[!duplicated(train$id), ]

## Remove rows without a star rating.
train = train[!(is.na(train$overall_star_rating) | train$overall_star_rating==""), ]

## Acumos compose function doesn't like factors, convert them to characters.
train$price_range = as.character(train$price_range)

## Convert star ratings prediction to a logistic regression problem with positive/negative sentiment.
## If star ratings < 4 then sentiment is negative, otherwise sentiment is positive.
## This method seems to have lowest error rates according to a similar experiment.
## Chen Li and Jin Zhang, “Prediction of Yelp Review Star Rating using Sentiment Analysis”, Stanford Univ., Stanford, CA, 2014.
train$overall_star_rating = ifelse(train$overall_star_rating < 4, 0, 1)

## Attempt to compose logistic regression model.
descriptor = lapply(train, class)
compose(predict=function(..., inputs=descriptor) as.character(predict(model, as.data.frame(list(...)), type="response")),
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

## If there are no errors R console should show something like the following.
##        adding: component.bin (deflated 1%)
##        adding: meta.json (deflated 58%)
##        adding: component.proto (deflated 67%)
