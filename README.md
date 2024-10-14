# Tutors Linux Course

## Development

Generate static files for local development.
```sh
npx tutors-html
```
This will generate the contains of the `public-site` folder.

Serving the site can be done by the built-in python module `http.server`, which will be pre-installed on most OS's.
```sh
python -m http.server -d public-site
```

## Local Deployment

To deploy the site locally and test your changes, you can use `make all`, which will build and then run a container that will be available at `localhost:8000`.
```sh
make all
```