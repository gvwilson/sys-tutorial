include lib/tut/tutorial.mk

PAGE := pages/index.md
RUN2 := bin/silent.sh bin/run2.sh
SITE_SERVER := python -m http.server -d site

## release: create a release
.PHONY: release
release:
	@rm -rf safety-tutorial.zip
	@zip -r safety-tutorial.zip \
	src \
	out \
	-x \*~
