# Disclaimer

This is just a draft done in a bit less than two hours with some copy paste from previous templates I had

# How to install

- Have docker installed
- `ln -s env.dev.tpl .env`
- docker compose up
- Create the database by connecting to mariadb on port 3306 of the pyshortener-mariadb container, and running the contents of create_database.sql in it.

The application is now exposed in localhost:8080
To shorten an URL, POST localhost:8080/shorten/ with a body like:

```json
{"url": "http://www.google.com"}
```

To be redirected, use the link returned by that endpoint
