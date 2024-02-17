include lib/tut/tutorial.mk

PY_FILES := $(wildcard ${SRC}/*.py)
PY_EXCLUDED := ${SRC}/headers.py
OUT_FILES := $(patsubst ${SRC}/%.py,${OUT}/%.out,$(filter-out ${PY_EXCLUDED},${PY_FILES}))

## release: create a release
.PHONY: release
release:
	@rm -rf safety-tutorial.zip
	@zip -r safety-tutorial.zip \
	src \
	out \
	-x \*~

## run: re-run all examples
.PHONY: run
run: ${OUT_FILES}

${OUT}/requests_get_json.out: ${SRC}/requests_get_json.py
	python $< > $@

${OUT}/requests_get_motto.out: ${SRC}/requests_get_motto.py
	python $< > $@

${OUT}/get_nonexistent_file.out: ${SRC}/get_nonexistent_file.py
	python $< > $@

${OUT}/show_response_headers.out: ${SRC}/show_response_headers.py
	python $< > $@
