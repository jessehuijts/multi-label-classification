**Multi label classification with logistic regression**

This is a prototype ML project consisting of scraped data from a big Dutch webshop. The labels are `categoryName` and `title` and `subTitle` are features.

__Summary__
- `Scrapy SitemapSpider` to scrape items iteratively.
- Preprocess the data by removing `stopwords` and use a `SnowballStemmer` which transforms all the different forms of a word into a single word 
- Pipeline with `LabelPowerset` and `LogisticRegression`. This transforms the multi-classification problem into a multi-class problem. The classifier is trained on all the unique label combinations in the training dataset.

