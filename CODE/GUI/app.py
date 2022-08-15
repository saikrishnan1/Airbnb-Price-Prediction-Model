from flask import Flask, render_template, request
import pickle
import pandas as pd
app = Flask('airbnb_OccupancyRate')
@app.route('/')
def show_predict_OccupancyRate_form():
    return render_template('predictorform.html')

@app.route('/results', methods=['POST'])
def results():
    form = request.form
    airbnbDF = pd.read_csv('airbnb_final_ALL.csv')
    if request.method == 'POST':
      #write your function that loads the model
      model = pickle.load(open('XGBoost.pickle', 'rb')) #you can use pickle to load the trained model
      price = request.form['price']
      bedrooms = request.form['bedrooms']
      beds = request.form['beds']
      minimum_nights = request.form['minimum_nights']
      maximum_nights = request.form['maximum_nights']
      median = airbnbDF[airbnbDF['Zip'] == int(request.form['zipcode'])]
      median_household = median['Median household income in 1999'].max()
      attraction_count = median['Attraction_Count'].max()
      restaurant_count = median['Restaurant_Count'].max()
      review = median['number_of_reviews_ltm'].median()

      zipcode = int(request.form['zipcode'])
      print(zipcode)
      zip_7870_0 = 0
      zip_7871_0 = 0
      zip_7872_0 = 0
      zip_7873_0 = 0
      zip_7874_0 = 0
      zip_7875_0 = 0

      range_1 = range(78701, 78709)
      range_2 = range(78710, 78719)
      range_3 = range(78720, 78729)
      range_4 = range(78730, 78739)
      range_5 = range(78740, 78749)

      if zipcode in range_1:
          print("Got here")
          zip_7870_0 = 1
      elif zipcode in range_2:
          zip_7871_0 = 1
      elif zipcode in range_3:
          zip_7872_0 = 1
      elif zipcode in range_4:
          zip_7873_0 = 1
      elif zipcode in range_5:
          zip_7874_0 = 1
      else:
          zip_7875_0 = 1

      room_type_hotel_room = 0
      room_type_private_room = 0
      room_type_entire_home_apt = 0
      room_type_shared_room = 0

      if request.form['room_type'] == "hotel":
          room_type_hotel_room = 1
      elif request.form['room_type'] == "private room":
          room_type_private_room = 1
      elif request.form['room_type'] == "home apartment":
          room_type_entire_home_apt = 1
      elif request.form['room_type'] == "shared room":
          room_type_shared_room = 1

      freeparking = 0
      paidparking = 0
      longtermstay = 0
      kitchen = 0
      pool = 0
      gym = 0
      workspace = 0

      option = request.form.getlist('freeparking')
      if len(option) == 1:
          freeparking = 1
      option1 = request.form.getlist('paidparking')
      if len(option1) == 1:
         paidparking = 1
      option2 = request.form.getlist('longtermstay')
      if len(option2) == 1:
          longtermstay = 1
      option3 = request.form.getlist('kitchen')
      if len(option3) == 1:
          kitchen = 1
      option4 = request.form.getlist('pool')
      if len(option4) == 1:
          pool = 1
      option5 = request.form.getlist('gym')
      if len(option5) == 1:
          gym = 1
      option6 = request.form.getlist('workspace')
      if len(option6) == 1:
          workspace = 1

      req = pd.DataFrame(columns=['price','number_of_reviews_ltm','bedrooms','beds','minimum_nights','maximum_nights',
                                  'median_household_income_in_1999','restaurant_count','attraction_count','room_type_entire_home_apt',
                                  'room_type_hotel_room','room_type_private_room','room_type_shared_room','freeparking',
                                  'paidparking','longtermstay','kitchen','pool','gym','workspace',
                                  'zip_7870_0','zip_7871_0','zip_7872_0','zip_7873_0','zip_7874_0','zip_7875_0'])

      req.loc[0] = [float(price), int(review), float(bedrooms), float(beds), int(minimum_nights), int(maximum_nights), float(median_household), int(restaurant_count), int(attraction_count), room_type_entire_home_apt,
                    room_type_hotel_room, room_type_private_room, room_type_shared_room, freeparking,
                    paidparking,longtermstay,kitchen,pool, gym,workspace, zip_7870_0,zip_7871_0,zip_7872_0,zip_7873_0,zip_7874_0,zip_7875_0]

      availability_365 = model.predict(req)
      predicted_occupancy_rate = (1 - (availability_365 / 365)) * 100
      return render_template('resultsform.html',  predicted_occupancy_rate=predicted_occupancy_rate)


app.run("localhost", "9999", debug=False)