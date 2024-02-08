include lib/tut/tutorial.mk
include depend.mk

PAGE := pages/index.md

## release: create a release
.PHONY: release
release:
	@rm -rf web-tutorial.zip
	@zip -r web-tutorial.zip \
	src \
	out \
	-x \*~
