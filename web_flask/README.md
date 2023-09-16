# AirBnB clone - Web framework

## Web framework using Flask and Jinja2
### 0-hello_route.py
* Start Flask web application that listens on 0:5000
* Has route `/` that displays `Hello HBNB!`

### 1-hbnb_route.pyt
* Add route `/hbnb` that displays `HBNB`

### 2-c_route.py
* Add route `/c/<text>` displays `C ` followed by `text`

### 3-python_route.py
* Add route `/python/<text>` that displays `Python ` followed by `text`
* Default value of `text = "is cool"`

### 4-number_route.py
* Add route /number/<n> that displays 'n is a number' if n is an integer

### 5-number_template.py, templates/5-number.html
* Add route /number_template/<n> to display HTML only if n is an integer
* HTML to display: <H1>Number: `n`</H1>

### 6-number_odd_or_even.py, templates/6-number_odd_or_even.html
* Add /number_odd_or_even/<n> route displays HTML if n is an integer
* HTML to display: <H1>Number: `n` is `even|odd`</H1>

### 7-states_list.py, web_flask/templates/7-states_list.html
* Start Flask web application with HBNB data

### 8-cities_by_states.py, web_flask/templates/8-cities_by_states.html
* Add route /cities_by_states to display webpage listing each city within each state

### 9-states.py, web_flask/templates/9-states.html
* Add route /states/<id> to display specific state with given id

### web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/
* Add route /hbnb_filters to display HBNB HTML page

### web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/
* Add route /hbnb to display HBNB HTML page
