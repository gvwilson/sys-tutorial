include lib/tut/tutorial.mk

OTHER_DIRS := site
LINT_OTHER_PAGES := 
LINT_OTHER_FILES := 

## release: create a release
.PHONY: release
release:
	@rm -rf sys-tutorial.zip
	@zip -r sys-tutorial.zip \
	${OTHER_DIRS} \
	${SRC} \
	${OUT} \
	-x \*~
