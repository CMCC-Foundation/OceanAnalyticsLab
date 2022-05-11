# Input Parameters

This module take in charge to read the input parameter string, extract the information and store it in a python class object.
It provides also some useful function to perform a (basic) validation on the input string.

## String format

The input parameter string, is defined as a **json-like** string.
What does it mean? It means that it respect the json standard syntax, but the single quote are used instead of the double ones.
In this way is it possible to guarantee the use of the input parameter string with many service or protocol wihtout to worry
about the parsing of the string. 
Some service can put the input string inside the double quote, this will cause a break of our string into many small string, causing a crash in the method.

Example:

`{ 'arg1': 'value2', 'arg2': int1, 'arg2': ['v1', 'v2'] }`

## iparameter.py

The class iparameter.py should be seen as a super class which contains all the parameters that are common between all methods.
It provides some useful function:

- Convert json-like string to json string filtering all None values
- Validate the type of input parameter
- Validate the syntax of some complex parameter like working domain

The access to the input argument in a method should be always done using this class.

## Specialization

As specified in the previous paragraph, iparameter.py should be considered as a super class which contains all the basic parameter needed by a method.
In general a method should need additional parameters, closely related to the method itself.
For a correct implementation, each method should extend the iparameter class, adding its specific parameter and the related validation.

## Parameter definition

Each parameter is defined by a class. Each class can include some variations of the same parameter, or it can group parameters with a common property.
An example of variations of a parameter is the working domain, because it can appear with or without the depth section.
Instead, all the int parameter are included in the numeric_parameter fields.

Associating a parameter to a class allows the web app to treat all parameters belonging to the same class in the same way.

### Attributes

Some attributes are mandatory for all parameters. 
Each class can instead specify attributes exclusively for each class.

#### Common attributes

Here a list of the common attributes:

- **id**: An integer to uniquely identify an attribute (a criteria so set this id still missing, is set manually)
- **label**: A string human-readable used to present the attributes to the user by the web interface
- **label method** The name of the parameter inside the input parameter string (used by the web app to build the string to send to the method)

###### NOTE: the class **start_end_time** is the unique to not implement the label method attribute

#### Optional attributes

Here a list of attributes that a class can implement:

- **values**: a list of pre-defined value from which the user can choose
- **type**: to indicate a specific attribute among the various possible attributes belonging to the same class
- **range**: in case of numeric parameter, it is possible to indicate the range of that value

### Parameters

Now, a table will present all the already defined parameter class. In a second column each class will
define the behavior of the wep app, instead a third column will specify the optional attributes.

| parameter_class   | Web App                                                                                                        | Specific Parameters                                                           |
|-------------------|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| id_field          | the web app receive from the register a list of field entity from which the user can make a choose             | values: list of output field object                                           |
| working_domain    | ask value inside spatial domain                                                                                | type:<br/>- w -> only spatial domain<br/>- wd -> spatial domain + depth       |
| start_end_time    | ask value inside spatial domain<br/>start < end                                                                | type:<br/>- y -> year only<br/>- ym -> year + month                           |
| year              | yyyy inside the time coverage                                                                                  |                                                                               |
| numeric_parameter | show the label associated to the parameter<br/> ask the value in according to the type and the range specified | type: <br/>- int<br/>- float<br/>range:<br/>- string with syntax: "[min,max]" |
| model             | the web app receive from the register a list of model entity from which the user can make a choose             | values: list of model object                                                  |
