# Code2040 API Challenge

Here I will discuss my experience with this year's Code2040 API challenge. I will first discuss the general structure of my implementation, and then I will discuss what was interesting to me about each question and possibly the distinctions between implementing the solutions in Python vs Ruby.

## General Implementation Organization

At first I thought about implementing each stage as a standalone script. However, when I completed all stages, I realized this code would benefit if I took all calls to the API if I separated them into a different module. Moreover, I created the runStages file to run all stages at once, allowing for easy addition of any additional stages. I also allowed user input of the email and github repo's, and never had to expose the token generated for the user. In general I think this modularization of the code, makes it easily expandable and testable.

## Stages

### Stage 1

Stage 1 was simple to implement both in ruby and in python. An interesting nugget of information is the difference between ruby methods that have (!) vs those that lack it. Usually the methods that end with a bang, are more risky. In this case the
	reverse!
method reverses the string in place overriding the original string, which makes this code even shorter, without the need of an additional variable.

### Stage 2

For stage 2 both the python and ruby implementation are identical. The python implementation needs error checking because the
	index
call creates an error if a particular element is not in the list.

### Stage 3

I think this is where ruby shines. While the python list comprehensions are nice, I prefer Ruby's functional approach to solving this problem.

### Stage 4

Stage 4 was interesting as I had never dealt with ISO8601 formatting. It seems to me that Ruby's time module was more expressive when solving this problem.

## Running the Code

1. To run the ruby version, from the root in the project folder:

	```
	cd ruby
	ruby runStages.rb
	```

2. To run the python version, from the root in the project folder:

	```
	cd python
	python runStages.py
	```