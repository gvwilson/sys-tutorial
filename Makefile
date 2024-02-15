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

PY_FILES := $(wildcard ${SRC}/*.py)
OUT_FILES := $(patsubst ${SRC}/%.py,${OUT}/%.out,${PY_FILES})

## run: re-run all examples
.PHONY: run
run: ${OUT_FILES}

${OUT}/get_nonexistent.out: ${SRC}/get_nonexistent.py
	python $< > $@

${OUT}/get_motto.out: ${SRC}/get_motto.py
	python $< > $@

${OUT}/show_response_headers.out: ${SRC}/show_response_headers.py
	python $< > $@
