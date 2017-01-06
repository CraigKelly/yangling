all: business.csv

clean:
	rm -f business.csv

business.csv : business.py yelp_academic_dataset_business.json
	./business.py < yelp_academic_dataset_business.json > business.csv
