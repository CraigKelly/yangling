all: business.csv reviews.csv

clean:
	rm -f business.csv

business.csv : business.py common.py yelp_academic_dataset_business.json
	./business.py < yelp_academic_dataset_business.json > business.csv

reviews.csv: review.py common.py yelp_academic_dataset_review.json
	./review.py < yelp_academic_dataset_review.json > review.csv
