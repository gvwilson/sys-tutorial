include lib/tut/tutorial.mk

PY_FILES := $(wildcard ${SRC}/*.py)
PY_EXCLUDED := ${SRC}/headers.py
OUT_FILES := $(patsubst ${SRC}/%.py,${OUT}/%.out,$(filter-out ${PY_EXCLUDED},${PY_FILES}))

RUNNER := bin/runner.sh
SITE_SERVER := python -m http.server -d site

## release: create a release
.PHONY: release
release:
	@rm -rf safety-tutorial.zip
	@zip -r safety-tutorial.zip \
	src \
	out \
	-x \*~

## listen: listen on port 8000
.PHONY: listen
listen:
	nc -l -p 8000

## run: re-run all examples
.PHONY: run
run: ${OUT_FILES}

${OUT}/get_nonexistent_file.out: ${SRC}/get_nonexistent_file.py
	python $< > $@

${OUT}/requests_get_json.out: ${SRC}/requests_get_json.py
	python $< > $@

${OUT}/requests_get_motto.out: ${SRC}/requests_get_motto.py
	python $< > $@

${OUT}/requests_local_motto.out: ${SRC}/requests_local_motto.py ${RUNNER}
	${RUNNER} 8000 "${SITE_SERVER}" "python $<" &> $@

${OUT}/requests_prepared_structure.out: ${SRC}/requests_prepared_structure.py
	python $< | grep -e '< ' | sed -e 's/< //g' > $@

${OUT}/show_response_headers.out: ${SRC}/show_response_headers.py
	python $< > $@
